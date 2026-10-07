# Five-Scenario DFIR Training Track

These five fictional cases use one repeatable investigation method and one standardized result format. The evidence and story change; the analyst workflow does not.

## Standard method — TRACE

**T — Triage & Integrity**
- Record case ID and evidence source.
- Verify SHA-256.
- Preserve originals.
- Establish host/time-zone context.

**R — Reconstruct the Timeline**
- Normalize timestamps to UTC.
- Identify the earliest suspicious event.
- Build host-by-host and unified timelines.

**A — Analyze & Correlate**
- Authentication.
- Process/PowerShell execution.
- Persistence.
- Filesystem/Registry evidence.
- Network/session evidence.
- Corroborate important findings with a second source.

**C — Confirm the Attack Chain**
- Determine affected identity and hosts.
- Separate normal administration from suspicious behavior.
- Establish entry, execution, movement, persistence, evasion and staging where supported.
- Mark uncertainty explicitly; never infer unsupported facts.

**E — Evidence-Based Report**
Return the same result fields for every case:
1. Initial affected host
2. Earliest defensible suspicious timestamp (UTC)
3. Account/identity involved
4. Execution evidence
5. Lateral-movement evidence or N/A
6. Persistence evidence or N/A
7. Defense-evasion/timeline anomaly or N/A
8. Collection/staging evidence or N/A
9. Ordered incident timeline
10. Final assessment + confidence
11. Artifact citations
12. SHA-256/provenance verification

## Scoring
Each case uses the same 100-point rubric:
- Integrity & provenance: 10
- Timeline: 15
- Identity/authentication: 10
- Execution: 10
- Cross-artifact correlation: 15
- Persistence/movement/evasion as applicable: 15
- Final attack reconstruction: 15
- Evidence-backed reporting: 10

The objective is methodological consistency: different evidence, same defensible analytical process.
