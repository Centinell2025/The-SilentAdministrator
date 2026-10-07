# CASE-03 — The Administrative Hop
**Level:** Hard

## Scenario
A privileged fictional account authenticates across `WS-OPS-03`, `SRV-MGMT-02` and `SRV-DATA-01`. Some transitions are approved administration and one sequence is not.

## Evidence design
Security EVTX from all three hosts, PowerShell/WinRM telemetry, session metadata and baseline administration schedule.

## Analyst mission
Use TRACE to reconstruct the host order, identify the anomalous transition and explain why it differs from normal administrative activity.

## Required result
Return all 12 standard TRACE fields. The ordered incident timeline must correlate source and destination evidence.

## Training lesson
A login on a destination host is more useful when correlated with source-host execution and expected administrative behavior.
