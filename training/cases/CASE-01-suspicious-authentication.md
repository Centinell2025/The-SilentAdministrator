# CASE-01 — The After-Hours Login
**Level:** Medium

## Scenario
A fictional finance workstation, `WS-FIN-12`, records successful access by `fin_ops` outside its normal operating window. Failed attempts immediately precede the successful session. Routine administrative activity creates noise.

## Evidence design
Security EVTX, PowerShell Operational log, Prefetch/Amcache subset and account-baseline CSV.

## Analyst mission
Use TRACE to determine whether the login is merely unusual or part of malicious execution. Establish the earliest defensible suspicious timestamp and support the conclusion with independent evidence.

## Required result
Return all 12 standard TRACE result fields. Lateral movement and persistence may legitimately be N/A if unsupported.

## Training lesson
An anomaly is not automatically an incident; authentication must be correlated with subsequent host activity.
