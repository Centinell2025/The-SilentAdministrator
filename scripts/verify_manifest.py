#!/usr/bin/env python3
"""Verify SHA-256 entries in a '<hash>  <path>' manifest."""
from pathlib import Path
import hashlib
import sys

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    manifest = Path(sys.argv[1] if len(sys.argv) > 1 else "manifest.sha256")
    base = manifest.parent
    failures = 0
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        expected, rel = raw.split(None, 1)
        rel = rel.strip().lstrip("*")
        actual = sha256(base / rel)
        ok = actual.lower() == expected.lower()
        print(f"{'OK' if ok else 'FAIL'}  {rel}")
        failures += 0 if ok else 1
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
