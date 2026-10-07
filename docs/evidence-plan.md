# Evidence Generation Plan

The final challenge must come from a controlled, isolated Windows lab. Text files that simply state answers are not forensic evidence.

## Controlled activity
Generate benign activity representing normal `svc_backup` baseline behavior, suspicious authentication, PowerShell administration, remote management between fictional hosts, scheduled-task persistence simulation, a controlled log gap in disposable systems, creation/staging of fictional documents, and a timestamp inconsistency for correlation.

## Collection
Preserve originals read-only, calculate SHA-256, normalize collection times to UTC and record provenance.

## Validation gates
An artifact enters release only if it parses with a standard forensic tool, has a recorded hash and provenance, supports an intended question or justified context, and contains no real secrets or personal/customer data.

## Independent solve
Perform a clean-room solve using only the player package and questions. Every answer must be reproducible without private author notes.
