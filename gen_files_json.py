#!/usr/bin/env python3
"""Run from the repo root to regenerate files.json."""
import json, os
from pathlib import Path

root = Path(__file__).parent
out  = {}

for folder in sorted(root.iterdir()):
    if not folder.is_dir():
        continue
    pdfs = sorted(p.name for p in folder.iterdir() if p.suffix.lower() == '.pdf')
    if pdfs:
        out[folder.name] = pdfs

(root / 'files.json').write_text(json.dumps(out, indent=2))
print(f"wrote files.json — {sum(len(v) for v in out.values())} PDFs across {len(out)} folders")
