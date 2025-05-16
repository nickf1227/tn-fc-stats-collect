# tn-fc-stats-collect
A simple script for collecting  stastics for FibreChannel on TrueNAS
## Example Output for fcdump.py
```
root@prod:~# python3 fcdump.py
Warning: EEPROM data too short (0 bytes) in /sys/class/fc_host/host13/device/sfp
             SFP EEPROM:
 /sys/class/fc_host/host12/device/sfp
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Field           ┃ Value            ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Vendor Name     │ FINISAR CORP.    │
│ Vendor OUI      │ 00-90-65         │
│ Part Number     │ FTLF8529P3BCV-QL │
│ Serial Number   │ UUG016A          │
│ Date Code       │ 151012           │
│ Connector Type  │ 7                │
│ Transceiver     │ 0                │
│ Encoding        │ 6                │
│ BR, nominal     │ 140 (x100MBd)    │
│ Length SMF (km) │ 0                │
│ Length OM3 (m)  │ 3                │
│ Length OM2 (m)  │ 0                │
│ Length OM1 (m)  │ 0                │
└─────────────────┴──────────────────┘

Statistics for host13
          General Counters
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                      ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ seconds_since_last_reset │ N/A   │
│ lip_count                │ N/A   │
│ nos_count                │ N/A   │
│ loss_of_signal_count     │ N/A   │
│ loss_of_sync_count       │ N/A   │
└──────────────────────────┴───────┘
         Traffic Stats
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                  ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ rx_frames            │ N/A   │
│ rx_words             │ N/A   │
│ tx_frames            │ N/A   │
│ tx_words             │ N/A   │
│ fcp_input_requests   │ N/A   │
│ fcp_input_megabytes  │ N/A   │
│ fcp_output_requests  │ N/A   │
│ fcp_output_megabytes │ N/A   │
│ fcp_control_requests │ N/A   │
└──────────────────────┴───────┘
         Error Counters
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                   ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ error_frames          │ N/A   │
│ invalid_crc_count     │ N/A   │
│ invalid_tx_word_count │ N/A   │
│ dumped_frames         │ N/A   │
│ link_failure_count    │ N/A   │
└───────────────────────┴───────┘
      Exchange/XID Issues
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                 ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fc_no_free_exch     │ N/A   │
│ fc_no_free_exch_xid │ N/A   │
│ fc_xid_not_found    │ N/A   │
│ fc_xid_busy         │ N/A   │
│ fc_seq_not_found    │ N/A   │
│ fc_non_bls_resp     │ N/A   │
└─────────────────────┴───────┘
        FCP Specific Failures
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                       ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fcp_packet_alloc_failures │ N/A   │
│ fcp_frame_alloc_failures  │ N/A   │
│ fcp_packet_aborts         │ N/A   │
└───────────────────────────┴───────┘
             FPIN - DN
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                     ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fpin_dn                 │ 0     │
│ fpin_dn_device_specific │ 0     │
│ fpin_dn_timeout         │ 0     │
│ fpin_dn_unable_to_route │ 0     │
│ fpin_dn_unknown         │ 0     │
└─────────────────────────┴───────┘
             FPIN - CN
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                      ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fpin_cn                  │ 0     │
│ fpin_cn_clear            │ 0     │
│ fpin_cn_credit_stall     │ 0     │
│ fpin_cn_oversubscription │ 0     │
│ fpin_cn_device_specific  │ 0     │
│ fpin_cn_lost_credit      │ 0     │
└──────────────────────────┴───────┘
                FPIN - LI
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                           ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fpin_li                       │ 0     │
│ fpin_li_device_specific       │ 0     │
│ fpin_li_invalid_crc_count     │ 0     │
│ fpin_li_invalid_tx_word_count │ 0     │
│ fpin_li_link_failure_count    │ 0     │
│ fpin_li_loss_of_signals_count │ 0     │
│ fpin_li_loss_of_sync_count    │ 0     │
│ fpin_li_prim_seq_err_count    │ 0     │
│ fpin_li_failure_unknown       │ 0     │
└───────────────────────────────┴───────┘
    Signals & Alarms
┏━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key          ┃ Value ┃
┡━━━━━━━━━━━━━━╇━━━━━━━┩
│ cn_sig_alarm │ N/A   │
│ cn_sig_warn  │ N/A   │
└──────────────┴───────┘
           Permission Issues
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Key              ┃ Value             ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ reset_statistics │ Permission denied │
└──────────────────┴───────────────────┘
                 Other
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                         ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ prim_seq_protocol_err_count │ N/A   │
└─────────────────────────────┴───────┘

Statistics for host12
          General Counters
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Key                      ┃ Value  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ seconds_since_last_reset │ 155485 │
│ lip_count                │ 0      │
│ nos_count                │ 0      │
│ loss_of_signal_count     │ 0      │
│ loss_of_sync_count       │ 0      │
└──────────────────────────┴────────┘
                 Traffic Stats
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Key                  ┃ Value                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ rx_frames            │ 282891505 (0.03 Gbps) │
│ rx_words             │ 0                     │
│ tx_frames            │ 235693154 (0.03 Gbps) │
│ tx_words             │ 0                     │
│ fcp_input_requests   │ 0                     │
│ fcp_input_megabytes  │ 0                     │
│ fcp_output_requests  │ 0                     │
│ fcp_output_megabytes │ 0                     │
│ fcp_control_requests │ 0                     │
└──────────────────────┴───────────────────────┘
         Error Counters
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                   ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ error_frames          │ 1     │
│ invalid_crc_count     │ 0     │
│ invalid_tx_word_count │ 0     │
│ dumped_frames         │ 1     │
│ link_failure_count    │ 0     │
└───────────────────────┴───────┘
      Exchange/XID Issues
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                 ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fc_no_free_exch     │ N/A   │
│ fc_no_free_exch_xid │ N/A   │
│ fc_xid_not_found    │ N/A   │
│ fc_xid_busy         │ N/A   │
│ fc_seq_not_found    │ N/A   │
│ fc_non_bls_resp     │ N/A   │
└─────────────────────┴───────┘
        FCP Specific Failures
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                       ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fcp_packet_alloc_failures │ N/A   │
│ fcp_frame_alloc_failures  │ N/A   │
│ fcp_packet_aborts         │ N/A   │
└───────────────────────────┴───────┘
             FPIN - DN
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                     ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fpin_dn                 │ 0     │
│ fpin_dn_device_specific │ 0     │
│ fpin_dn_timeout         │ 0     │
│ fpin_dn_unable_to_route │ 0     │
│ fpin_dn_unknown         │ 0     │
└─────────────────────────┴───────┘
             FPIN - CN
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                      ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fpin_cn                  │ 0     │
│ fpin_cn_clear            │ 0     │
│ fpin_cn_credit_stall     │ 0     │
│ fpin_cn_oversubscription │ 0     │
│ fpin_cn_device_specific  │ 0     │
│ fpin_cn_lost_credit      │ 0     │
└──────────────────────────┴───────┘
                FPIN - LI
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                           ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ fpin_li                       │ 0     │
│ fpin_li_device_specific       │ 0     │
│ fpin_li_invalid_crc_count     │ 0     │
│ fpin_li_invalid_tx_word_count │ 0     │
│ fpin_li_link_failure_count    │ 0     │
│ fpin_li_loss_of_signals_count │ 0     │
│ fpin_li_loss_of_sync_count    │ 0     │
│ fpin_li_prim_seq_err_count    │ 0     │
│ fpin_li_failure_unknown       │ 0     │
└───────────────────────────────┴───────┘
    Signals & Alarms
┏━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key          ┃ Value ┃
┡━━━━━━━━━━━━━━╇━━━━━━━┩
│ cn_sig_alarm │ N/A   │
│ cn_sig_warn  │ N/A   │
└──────────────┴───────┘
           Permission Issues
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Key              ┃ Value             ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ reset_statistics │ Permission denied │
└──────────────────┴───────────────────┘
                 Other
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Key                         ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ prim_seq_protocol_err_count │ 0     │
└─────────────────────────────┴───────┘
```
## Example output For fcspeed.py

```
root@prod:~# python3 fcspeed.py
Logging to: /var/log/fc_bandwidth.csv
[2025-05-16 15:30:05] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 598.34 MB/s, TX: 4.66 MB/s
[2025-05-16 15:30:10] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 607.27 MB/s, TX: 4.73 MB/s
[2025-05-16 15:30:15] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 612.57 MB/s, TX: 4.77 MB/s
[2025-05-16 15:30:20] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 613.12 MB/s, TX: 4.77 MB/s
[2025-05-16 15:30:25] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 615.93 MB/s, TX: 4.80 MB/s
[2025-05-16 15:30:30] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 612.95 MB/s, TX: 4.77 MB/s
[2025-05-16 15:30:35] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 617.82 MB/s, TX: 4.81 MB/s
[2025-05-16 15:30:40] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 612.96 MB/s, TX: 4.78 MB/s
[2025-05-16 15:30:45] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 618.28 MB/s, TX: 4.81 MB/s
[2025-05-16 15:30:50] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 612.96 MB/s, TX: 4.77 MB/s
[2025-05-16 15:30:55] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 613.71 MB/s, TX: 4.78 MB/s
[2025-05-16 15:31:00] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 617.33 MB/s, TX: 4.81 MB/s
[2025-05-16 15:31:05] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 617.95 MB/s, TX: 4.81 MB/s
[2025-05-16 15:31:10] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 613.40 MB/s, TX: 4.78 MB/s
[2025-05-16 15:31:15] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 614.37 MB/s, TX: 4.79 MB/s
[2025-05-16 15:31:20] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 617.25 MB/s, TX: 4.81 MB/s
[2025-05-16 15:31:25] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 616.33 MB/s, TX: 4.80 MB/s
[2025-05-16 15:31:30] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 619.77 MB/s, TX: 4.83 MB/s
[2025-05-16 15:31:35] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 616.11 MB/s, TX: 4.79 MB/s
[2025-05-16 15:31:40] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 444.38 MB/s, TX: 461.45 MB/s
[2025-05-16 15:31:45] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 6.48 MB/s, TX: 1638.13 MB/s
[2025-05-16 15:31:50] host12 - naa.2100000e1e2596b0 - bartowski-desktop-lun - RX: 6.39 MB/s, TX: 1636.76 MB/s

```

