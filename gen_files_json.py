#!/usr/bin/env python3
"""Run from the repo root to regenerate files.json."""
import json, os
from pathlib import Path

root = Path(__file__).parent
out  = {}

# loose PDFs directly in the repo root
root_pdfs = sorted(p.name for p in root.iterdir() if p.suffix.lower() == '.pdf')
if root_pdfs:
    out["(root)"] = root_pdfs

for top in sorted(root.iterdir()):
    if not top.is_dir():
        continue

    # PDFs directly inside a top-level folder (e.g. MANUEL/foo.pdf)
    top_pdfs = sorted(p.name for p in top.iterdir() if p.suffix.lower() == '.pdf')
    if top_pdfs:
        out[top.name] = top_pdfs

    # PDFs one level deeper (e.g. MANUEL/LG AS/*.pdf)
    for folder in sorted(top.iterdir()):
        if not folder.is_dir():
            continue
        pdfs = sorted(p.name for p in folder.iterdir() if p.suffix.lower() == '.pdf')
        if pdfs:
            out[f"{top.name}/{folder.name}"] = pdfs

(root / 'files.json').write_text(json.dumps(out, indent=2))
print(f"wrote files.json — {sum(len(v) for v in out.values())} PDFs across {len(out)} folders")
