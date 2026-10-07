# CASE-02 — The Quiet Task
**Level:** Hard

## Scenario
On fictional management host `SRV-MGMT-04`, routine maintenance tasks coexist with one unauthorized scheduled task. The task name and timing are intentionally plausible.

## Evidence design
Security EVTX, Task Scheduler Operational log, Registry/task metadata, PowerShell log and execution artifacts.

## Analyst mission
Use TRACE to identify the suspicious persistence object, determine when it was established and distinguish it from legitimate maintenance.

## Required result
Return all 12 standard TRACE fields and corroborate persistence with at least two independent sources.

## Training lesson
Object names are weak evidence; behavior, creation context and execution telemetry provide stronger attribution.
