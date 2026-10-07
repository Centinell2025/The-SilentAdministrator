# Training Lab — Two-VM Range

This lab adds a safe, isolated practice environment to **The Silent Administrator**. It is for defensive DFIR training and evidence generation, not for attacking external systems.

## VM 1 — TSA-ANALYST
**Role:** Investigator workstation  
**Recommended OS:** Ubuntu LTS or FLARE-VM-compatible Windows analyst image  
**Resources:** 4 vCPU, 8 GB RAM, 80 GB disk  
**Network:** Host-only / internal network only

Purpose:
- Mount and analyze exported evidence.
- Build timelines.
- Parse EVTX, Registry, Prefetch/Amcache and NTFS-derived artifacts.
- Verify SHA-256 hashes.
- Produce the final investigation report.

Suggested defensive tooling: Eric Zimmerman's tools (when using Windows), Hayabusa, Chainsaw, Timesketch-compatible exports, Python, SQLite utilities, and standard hashing tools.

## VM 2 — TSA-WINDOWS-LAB
**Role:** Disposable Windows evidence-generation target  
**Recommended OS:** Windows 11 Enterprise Evaluation or Windows Server evaluation, properly licensed/evaluated  
**Resources:** 4 vCPU, 8 GB RAM, 100 GB disk  
**Network:** Host-only / internal network only

Purpose:
- Generate benign Windows telemetry for the fictional incident.
- Produce Security, PowerShell and Task Scheduler logs.
- Create fictional filesystem activity and timeline evidence.
- Take snapshots before each scenario run.

## Isolation requirements

- Do not bridge the training network to production.
- Do not use real credentials, domains, customer files or corporate data.
- Use only fictional accounts and documents.
- Keep a clean snapshot named `BASELINE-CLEAN`.
- Restore the snapshot after each evidence-generation run.
- Export only the artifacts required by the challenge.

## Network plan

```
TSA-ANALYST       10.77.77.10
TSA-WINDOWS-LAB   10.77.77.20
Network           10.77.77.0/24
Gateway           none required
DNS               none required
```

The final HTB Sherlock remains artifact-driven. These VMs are development/training infrastructure and are not automatically part of the player download.
