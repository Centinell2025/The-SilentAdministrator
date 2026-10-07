# VirtualBox Setup

Create an **Internal Network** named `TSA-LAB`.

## TSA-ANALYST
- Adapter 1: Internal Network / TSA-LAB
- IPv4: 10.77.77.10/24
- Shared clipboard: disabled for clean-room validation when practical
- Snapshot: BASELINE-CLEAN

## TSA-WINDOWS-LAB
- Adapter 1: Internal Network / TSA-LAB
- IPv4: 10.77.77.20/24
- Snapshot: BASELINE-CLEAN

Avoid Bridged Adapter mode. If temporary Internet access is needed for OS/tool installation, enable NAT only during provisioning, patch the machine, then disable NAT before scenario generation.

## Validation
From TSA-ANALYST, verify only the lab target is reachable. Record the VM software version, OS build, timezone and snapshot identifier in the provenance log before generating evidence.
