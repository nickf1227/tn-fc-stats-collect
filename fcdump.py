#!/usr/bin/env python3
import os
import glob
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

GROUPS = {
    "General Counters": [
        "seconds_since_last_reset", "lip_count", "nos_count",
        "loss_of_signal_count", "loss_of_sync_count"
    ],
    "Traffic Stats": [
        "rx_frames", "rx_words", "tx_frames", "tx_words",
        "fcp_input_requests", "fcp_input_megabytes",
        "fcp_output_requests", "fcp_output_megabytes",
        "fcp_control_requests"
    ],
    "Error Counters": [
        "error_frames", "invalid_crc_count", "invalid_tx_word_count",
        "dumped_frames", "link_failure_count"
    ],
    "Exchange/XID Issues": [
        "fc_no_free_exch", "fc_no_free_exch_xid", "fc_xid_not_found",
        "fc_xid_busy", "fc_seq_not_found", "fc_non_bls_resp"
    ],
    "FCP Specific Failures": [
        "fcp_packet_alloc_failures", "fcp_frame_alloc_failures", "fcp_packet_aborts"
    ],
    "FPIN - DN": [
        "fpin_dn", "fpin_dn_device_specific", "fpin_dn_timeout",
        "fpin_dn_unable_to_route", "fpin_dn_unknown"
    ],
    "FPIN - CN": [
        "fpin_cn", "fpin_cn_clear", "fpin_cn_credit_stall",
        "fpin_cn_oversubscription", "fpin_cn_device_specific", "fpin_cn_lost_credit"
    ],
    "FPIN - LI": [
        "fpin_li", "fpin_li_device_specific", "fpin_li_invalid_crc_count",
        "fpin_li_invalid_tx_word_count", "fpin_li_link_failure_count",
        "fpin_li_loss_of_signals_count", "fpin_li_loss_of_sync_count",
        "fpin_li_prim_seq_err_count", "fpin_li_failure_unknown"
    ],
    "Signals & Alarms": ["cn_sig_alarm", "cn_sig_warn"],
    "Permission Issues": ["reset_statistics"]
}

def decode_str(data, start, length):
    if len(data) < start + length:
        return ""
    return data[start:start+length].decode('ascii', errors='ignore').strip()

def parse_sfp_eeprom(path):
    try:
        with open(path, "rb") as f:
            data = f.read(256)
    except Exception as e:
        console.print(f"[red]Error reading {path}: {e}[/red]")
        return

    if len(data) < 88:
        console.print(f"[yellow]Warning: EEPROM data too short ({len(data)} bytes) in {path}[/yellow]")
        return

    fields = {
        "Vendor Name": decode_str(data, 20, 16),
        "Vendor OUI": f"{data[37]:02X}-{data[38]:02X}-{data[39]:02X}" if len(data) >= 40 else "Not available",
        "Part Number": decode_str(data, 40, 16),
        "Serial Number": decode_str(data, 68, 16),
        "Date Code": decode_str(data, 84, 8),
        "Connector Type": data[2] if len(data) > 2 else 'N/A',
        "Transceiver": data[3] if len(data) > 3 else 'N/A',
        "Encoding": data[11] if len(data) > 11 else 'N/A',
        "BR, nominal": f"{data[12]} (x100MBd)" if len(data) > 12 else 'N/A',
        "Length SMF (km)": data[14] if len(data) > 14 else 'N/A',
        "Length OM3 (m)": data[16] if len(data) > 16 else 'N/A',
        "Length OM2 (m)": data[17] if len(data) > 17 else 'N/A',
        "Length OM1 (m)": data[18] if len(data) > 18 else 'N/A',
    }

    table = Table(title=f"SFP EEPROM: {path}", title_style="bold green")
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")

    for k, v in fields.items():
        table.add_row(k, str(v))

    console.print(table)

def hex_to_dec(value: str) -> str:
    try:
        num = int(value, 16)
    except ValueError:
        try:
            num = int(value)
        except ValueError:
            return value
    if num == 0xFFFFFFFFFFFFFFFF:
        return "N/A"
    return str(num)

def read_fc_statistics():
    hosts = glob.glob('/sys/class/fc_host/host*/statistics')
    for host_stats_dir in hosts:
        host_name = os.path.basename(os.path.dirname(host_stats_dir))
        console.print(f"\n[bold magenta]Statistics for {host_name}[/bold magenta]")
        stats = {}
        try:
            stat_files = os.listdir(host_stats_dir)
        except PermissionError:
            console.print(f"[red]Permission denied reading {host_stats_dir}[/red]")
            continue

        for stat_file in stat_files:
            stat_path = os.path.join(host_stats_dir, stat_file)
            try:
                with open(stat_path, 'r') as f:
                    raw = f.read().strip()
                    stats[stat_file] = hex_to_dec(raw)
            except PermissionError:
                stats[stat_file] = "Permission denied"
            except Exception as e:
                stats[stat_file] = f"Error reading: {e}"

        print_fc_stats_grouped(stats)

def calculate_bandwidth(frames_str, seconds_str):
    if frames_str == "N/A" or not frames_str.isdigit():
        return ""
    frames = int(frames_str)
    if seconds_str == "N/A" or not seconds_str.isdigit():
        return ""
    seconds = int(seconds_str)
    if seconds <= 0:
        return ""
    bandwidth_bps = (frames * 2148 * 8) / seconds
    bandwidth_gbps = bandwidth_bps / 1e9
    return f" ({bandwidth_gbps:.2f} Gbps)"

def print_fc_stats_grouped(stats: dict):
    matched = set()
    for group, keys in GROUPS.items():
        group_table = Table(title=f"{group}", title_style="bold blue")
        group_table.add_column("Key", style="yellow")
        group_table.add_column("Value", style="white")
        any_in_group = False

        for key in keys:
            if key in stats:
                value = stats[key]
                if group == "Traffic Stats" and key in ["rx_frames", "tx_frames"]:
                    seconds_str = stats.get("seconds_since_last_reset", "N/A")
                    bandwidth = calculate_bandwidth(value, seconds_str)
                    value += bandwidth
                group_table.add_row(key, value)
                matched.add(key)
                any_in_group = True

        if any_in_group:
            console.print(group_table)

    other_keys = sorted(set(stats.keys()) - matched)
    if other_keys:
        other_table = Table(title="Other", title_style="bold red")
        other_table.add_column("Key", style="red")
        other_table.add_column("Value", style="white")
        for key in other_keys:
            other_table.add_row(key, stats[key])
        console.print(other_table)

def main():
    sfp_paths = glob.glob('/sys/class/fc_host/host*/device/sfp')
    if not sfp_paths:
        console.print("[yellow]No SFP EEPROM files found under /sys/class/fc_host/host*/device/sfp[/yellow]")
    else:
        for path in sfp_paths:
            parse_sfp_eeprom(path)

    read_fc_statistics()

if __name__ == "__main__":
    main()
