#!/usr/bin/env python3
"""V1 lightweight index: records project Markdown/YAML files and obvious stable IDs.
This is derived data only; it is never canonical.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "09_index" / "file_index.json"
ID_RE = re.compile(r"\b(?:CH|CHR|LOC|FAC|EVT|F|ITEM|ARC|SEQ|THREAD)_\d{4,6}\b")
SKIP = {".git", "09_index"}

rows = []
for p in ROOT.rglob("*"):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if rel.parts and rel.parts[0] in SKIP:
        continue
    if p.suffix.lower() not in {".md", ".yaml", ".yml", ".toml"}:
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    rows.append({
        "path": rel.as_posix(),
        "ids": sorted(set(ID_RE.findall(text))),
        "bytes": p.stat().st_size,
    })

OUT.write_text(json.dumps({"version": 1, "files": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Indexed {len(rows)} files -> {OUT}")
