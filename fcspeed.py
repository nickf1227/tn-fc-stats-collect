#!/usr/bin/env python3

import os
import subprocess
import time
import csv
import json
from datetime import datetime

LOG_FILE = '/var/log/fc_bandwidth.csv'
INTERVAL = 5  # seconds
FRAME_SIZE = 2148  
# bytes per frame - Assuming The Maximum FC Frame Size accoding to https://en.wikipedia.org/wiki/Fibre_Channel_frame

def run_midclt_call(method):
    """Call midclt and parse JSON output."""
    result = subprocess.run(
        ['midclt', 'call', method],
        capture_output=True, text=True, check=True
    )
    return json.loads(result.stdout)

def get_fc_ports_info():
    """Return mapping of online FC host → metadata (path, wwpn, wwpn_b, iscsi_target_name)."""
    fc_hosts   = run_midclt_call('fc.fc_hosts')
    fc_port_q  = run_midclt_call('fcport.query')
    fchost_q   = run_midclt_call('fc.fc_host.query')

    # Build lookup of wwpn → (wwpn_b, iscsi_target_name)
    wwpn_map = {}
    for port in fc_port_q:
        wwpn = port.get('wwpn')
        if not wwpn:
            continue
        wwpn_map[wwpn] = {
            'wwpn_b': port.get('wwpn_b'),
            'iscsi_target_name': port.get('target', {}).get('iscsi_target_name')
        }

    port_map = {}
    for host in fc_hosts:
        if host.get('port_state') != 'Online':
            continue

        name      = host['name']
        path      = host['path']
        port_name = host['port_name']        # e.g. "0x2100000e1e2596b0"
        naa       = f"naa.{port_name[2:]}"  # convert to "naa.xxxx"

        # Find matching entry in fchost_q for wwpn/wwpn_b
        wwpn = None
        wwpn_b = None
        for entry in fchost_q:
            if entry.get('wwpn') == naa:
                wwpn   = entry['wwpn']
                wwpn_b = entry.get('wwpn_b')
                break

        # Merge in iSCSI target name from wwpn_map
        iscsi_name = wwpn_map.get(wwpn, {}).get('iscsi_target_name')

        port_map[name] = {
            'path': path,
            'wwpn': wwpn,
            'wwpn_b': wwpn_b,
            'iscsi_target_name': iscsi_name
        }

    return port_map

def read_hex_value(p):
    try:
        with open(p, 'r') as f:
            return int(f.read().strip(), 16)
    except:
        return 0

def main():
    print(f"Logging to: {LOG_FILE}")
    headers_written = os.path.exists(LOG_FILE)

    port_data  = get_fc_ports_info()
    prev_stats = {}

    with open(LOG_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not headers_written:
            writer.writerow([
                'timestamp', 'host', 'wwpn', 'wwpn_b', 'iscsi_target_name',
                'rx_MBps', 'tx_MBps'
            ])

        while True:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            current_stats = {}

            for host, meta in port_data.items():
                stat_dir = os.path.join(meta['path'], 'statistics')
                rx = read_hex_value(os.path.join(stat_dir, 'rx_frames'))
                tx = read_hex_value(os.path.join(stat_dir, 'tx_frames'))
                current_stats[host] = (rx, tx)

                if host in prev_stats:
                    d_rx = rx - prev_stats[host][0]
                    d_tx = tx - prev_stats[host][1]
                    rx_mb = (d_rx * FRAME_SIZE) / (1024**2) / INTERVAL
                    tx_mb = (d_tx * FRAME_SIZE) / (1024**2) / INTERVAL

                    print(f"[{timestamp}] {host} - {meta.get('wwpn','N/A')} - "
                          f"{meta.get('iscsi_target_name','N/A')} - "
                          f"RX: {rx_mb:.2f} MB/s, TX: {tx_mb:.2f} MB/s")

                    writer.writerow([
                        timestamp,
                        host,
                        meta.get('wwpn',''),
                        meta.get('wwpn_b',''),
                        meta.get('iscsi_target_name',''),
                        f"{rx_mb:.2f}",
                        f"{tx_mb:.2f}"
                    ])
                    csvfile.flush()

            prev_stats = current_stats
            time.sleep(INTERVAL)

if __name__ == '__main__':
    main()
