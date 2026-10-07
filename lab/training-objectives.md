# Senior DFIR Training Objectives

The two-VM range is designed to train analysts to:

1. Establish evidence integrity before analysis.
2. Normalize timestamps to UTC.
3. Correlate Windows authentication with execution telemetry.
4. Distinguish routine service-account behavior from anomalous use.
5. Correlate PowerShell and process execution.
6. Identify persistence from Windows artifacts.
7. Recognize gaps and inconsistencies in event history.
8. Reconcile filesystem metadata with journal-derived evidence.
9. Build a defensible incident timeline.
10. Document conclusions with artifact-level citations.

## Training progression

**Phase A — Baseline:** learn normal `svc_backup` behavior.

**Phase B — Detection:** identify the first abnormal authentication/execution sequence.

**Phase C — Correlation:** combine logs and filesystem evidence rather than relying on one source.

**Phase D — Expert reconstruction:** explain conflicting timestamps and reconstruct the incident with explicit confidence and supporting artifacts.

The analyst should never need access to the private answer key during a clean-room solve.
