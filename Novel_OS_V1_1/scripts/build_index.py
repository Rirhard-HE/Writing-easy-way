#!/usr/bin/env python3
"""V1 lightweight index: records project Markdown/YAML files and obvious stable IDs.
This is derived data only; it is never canonical.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "09_index" / "file_index.json"
SECRET_OUT = ROOT / "09_index" / "secret_guard_index.json"
ID_RE = re.compile(
    r"\b(?:(?:CH|CHR|LOC|FAC|EVT|F|ITEM|SYS|ARC|SEQ|THREAD|CHANGE|QUESTION)_\d{4,6}"
    r"|SRC(?:GRP|SEG|ENT)_\d{4,6}|SRC(?:EVT|CLAIM)_\d{6})\b"
)
SKIP = {".git", "09_index"}

rows = []
secret_rows = []


def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


for p in sorted(ROOT.rglob("*"), key=lambda value: value.as_posix()):
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
    metadata = frontmatter(text)
    row = {
        "path": rel.as_posix(),
        "ids": sorted(set(ID_RE.findall(text))),
        "bytes": p.stat().st_size,
        "audience": metadata.get("audience", "PROJECT"),
        "context_policy": metadata.get("context_policy", "STANDARD"),
        "reader_state_effect": metadata.get("reader_state_effect", "UNSPECIFIED"),
        "reveal_status": metadata.get("reveal_status"),
    }
    if (
        (len(rel.parts) >= 2 and rel.parts[:2] == ("01_canon", "secret"))
        or metadata.get("audience") == "AUTHOR_ONLY"
        or metadata.get("context_policy") == "EXCLUDE_FROM_DRAFT_GENERATION"
    ):
        row["retrieval_scope"] = "SECRET_GUARD_ONLY"
        secret_rows.append(row)
    else:
        row["retrieval_scope"] = "STANDARD"
        rows.append(row)

OUT.write_text(
    json.dumps({"version": 2, "files": rows}, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(f"Indexed {len(rows)} files -> {OUT}")
SECRET_OUT.write_text(
    json.dumps(
        {
            "version": 1,
            "audience": "AUTHOR_ONLY",
            "context_policy": "SECRET_GUARD_ONLY",
            "files": secret_rows,
        },
        ensure_ascii=False,
        indent=2,
    ) + "\n",
    encoding="utf-8",
)
print(f"Indexed {len(secret_rows)} secret guard files -> {SECRET_OUT}")
