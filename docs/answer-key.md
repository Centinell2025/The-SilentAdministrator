# Private Author Answer Key — Draft

**Never include this file in the player ZIP.** Values marked TBD must be replaced by exact evidence-derived values.

| Q | Canonical answer | Required corroboration |
|---|---|---|
| 1 | WS-FIN-07 | Security + execution artifact |
| 2 | TBD exact UTC timestamp | PowerShell + execution evidence |
| 3 | svc_backup | Authentication + host activity |
| 4 | TBD exact artifact pair | Two independent sources |
| 5 | TBD exact process chain | PowerShell + process evidence |
| 6 | SRV-MGMT-01 | Authentication + remote-management evidence |
| 7 | WinRM / PowerShell Remoting (target design) | Session + PowerShell evidence |
| 8 | SRV-MGMT-01 | Cross-host timeline |
| 9 | Scheduled task (target design) | Task Scheduler + secondary artifact |
| 10 | BackupHealthCheck (target design) | Task evidence |
| 11 | Event-history clearing/gap | Security + secondary evidence |
| 12 | TBD manipulated timestamp | MFT-derived metadata |
| 13 | USN-derived record (target design) | Journal/timeline evidence |
| 14 | TBD UTC interval | USN + execution evidence |
| 15 | SRV-FILE-02 | Authentication + filesystem activity |
| 16 | Q4_Financial_Archive.zip (fictional) | Filesystem evidence |
| 17 | C:\ProgramData\Cache\ (target design) | Filesystem evidence |
| 18 | WS-FIN-07 → SRV-MGMT-01 → SRV-FILE-02 | Unified timeline |
| 19 | TBD evidence-specific explanation | Two independent sources |
| 20 | Foothold → credential abuse → remote execution → lateral movement → persistence → defense evasion → collection/staging | Unified timeline |

No TBD may remain in the final HTB write-up.
