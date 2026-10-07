# Challenge Architecture

| Host | Role | Primary evidence |
|---|---|---|
| WS-FIN-07 | Initial workstation | Security EVTX, PowerShell, Prefetch, Amcache, Registry |
| SRV-MGMT-01 | Management pivot | Security EVTX, WinRM/PowerShell, Task Scheduler |
| SRV-FILE-02 | File server | Security EVTX, MFT/USN-derived evidence, staging metadata |

## Evidence families
Windows Security logs; PowerShell Operational logs; Task Scheduler logs; Registry-derived context; Prefetch/Amcache; NTFS MFT/USN-derived records; LNK/Jump List context where justified; session metadata; SHA-256 integrity manifest.

## Insane-difficulty mechanics
- legitimate and malicious administration overlap;
- one timeline source contains misleading metadata;
- a log gap must be corroborated elsewhere;
- three hosts must be normalized onto one UTC timeline;
- high-value conclusions require independent corroboration;
- final questions test reconstruction rather than string searching.

## Safety
No functional malware, destructive payloads, real secrets, customer data or third-party infrastructure. All identities, hosts, addresses and documents are fictional or laboratory-only.
