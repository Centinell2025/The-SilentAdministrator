# CASE-05 — The Silent Administrator
**Level:** Insane / Senior

## Scenario
The capstone case spans `WS-FIN-07`, `SRV-MGMT-01` and `SRV-FILE-02`. The privileged service identity `svc_backup` is mixed with legitimate scheduled activity. Evidence includes administrative execution, persistence, a timeline inconsistency, an event-history gap and fictional data staging.

## Evidence design
Security EVTX, PowerShell Operational, Task Scheduler, Registry context, Prefetch/Amcache, NTFS MFT/USN-derived evidence and session metadata.

## Analyst mission
Apply TRACE without changing methodology. Reconstruct the complete evidence-supported incident chain and explain conflicting evidence.

## Required result
Return all 12 standard TRACE result fields. High-impact conclusions require independent corroboration.

## Training lesson
Senior DFIR is not a hunt for one IOC. It is the disciplined reconstruction of events from imperfect, overlapping evidence.
