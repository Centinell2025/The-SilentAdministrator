# Artifacts

Expected release structure:

```
evidence/
  WS-FIN-07/
  SRV-MGMT-01/
  SRV-FILE-02/
  manifest.sha256
  provenance.csv
```

Large forensic binaries should not be committed casually to Git history. The final player ZIP must never contain the private answer key, author write-up, generation secrets or internal validation notes.
