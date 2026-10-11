# The Silent Administrator

**Hack The Box Sherlock candidate**  
Category: **DFIR**  
Target difficulty: **Insane**  
Status: **Development / evidence validation**

The Silent Administrator is a senior-level Windows DFIR investigation built around a compromised privileged service account and a multi-host intrusion. No single artifact reveals the complete answer: investigators must correlate authentication, process execution, PowerShell, persistence, filesystem and timeline evidence.

## Investigation goals

Reconstruct the intrusion from initial foothold through credential abuse, lateral movement, persistence, defense evasion, collection and simulated exfiltration. Several timestamps and apparently legitimate administrative events are intentionally ambiguous; conclusions must be supported by independent evidence.

## Design principles

- Evidence-driven, not guess-driven.
- Multi-source and multi-host correlation.
- No live malware and no real credentials.
- Synthetic organization and identities only.
- Reproducible evidence-generation procedure.
- Every scored answer maps to a specific artifact and validation rule.
- Challenge secrets and answer keys remain private.

## Repository layout

- `docs/` — scenario, architecture, questions and validation.
- `artifacts/` — evidence manifest and provenance.
- `scripts/` — safe integrity/validation helpers.
- `submission/` — HTB caption and release checklist.
- `writeup/` — private author solution.

> Private challenge-development repository intended for HTB submission review.


---
**Ethical and educational use / Uso ético y educativo:** This is a fictional or simulated defensive cybersecurity training exercise. Test only systems you own or are explicitly authorized to assess. / Ejercicio de ciberseguridad defensiva ficticio o simulado. Realice pruebas solo en sistemas propios o con autorización expresa. See / Consulte [Educational Purpose Notice](EDUCATIONAL_PURPOSE_NOTICE.md).
