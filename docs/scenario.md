# Scenario — The Silent Administrator

## Executive premise
Northbridge Research Group is a fictional Windows enterprise. Analysts discover activity attributed to the privileged service identity `svc_backup`. The account normally performs scheduled backup operations, but several events fall outside its established pattern.

The SOC has no single conclusive alert. Security logs contain gaps, filesystem timestamps do not fully agree with journal evidence, and administrative tools were used in ways that initially appear legitimate.

Evidence comes from three fictional systems:
- `WS-FIN-07` — suspected initial foothold.
- `SRV-MGMT-01` — management/jump server.
- `SRV-FILE-02` — file server containing final collection activity.

## Canonical incident truth
1. Initial compromise occurs on WS-FIN-07.
2. The privileged identity `svc_backup` is abused.
3. Administrative execution and PowerShell are used.
4. The intrusion traverses the management tier before SRV-FILE-02.
5. Persistence is established using a mechanism resembling routine administration.
6. Selected evidence is cleared or manipulated.
7. Fictional files are staged for simulated exfiltration.
8. Cross-artifact correlation exposes the true sequence despite misleading timestamps.

## Player objective
Determine what happened, when, which evidence is trustworthy, which account was abused, how the actor moved between systems, how persistence was achieved, and what was staged. Every scored conclusion must be recoverable from the evidence package.
