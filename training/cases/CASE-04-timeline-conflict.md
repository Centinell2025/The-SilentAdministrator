# CASE-04 — The Impossible Timestamp
**Level:** Hard / Expert

## Scenario
A fictional archive on `SRV-FILE-08` appears, from one metadata field, to predate the suspected compromise. Other forensic records disagree.

## Evidence design
MFT-derived metadata, USN-derived records, PowerShell/execution telemetry and Security EVTX.

## Analyst mission
Use TRACE to determine which timestamp cannot be trusted at face value and establish the defensible creation/staging interval using independent artifacts.

## Required result
Return all 12 standard TRACE fields and explicitly separate observed metadata from the analyst's evidence-supported conclusion.

## Training lesson
A timestamp is an artifact value, not automatically ground truth. Timeline conclusions require provenance and corroboration.
