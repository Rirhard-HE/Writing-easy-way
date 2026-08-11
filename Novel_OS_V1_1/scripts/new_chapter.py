#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "07_workbench" / "_templates"

FILES = [
    "00_author_brief.md",
    "04_author_decision.md",
    "07_memory_delta.agent.yaml",
    "08_approval.yaml",
]
EMPTY = [
    "01_context.auto.md",
    "02_expansion.agent.md",
    "03_conflict_report.agent.md",
    "05_draft.md",
    "06_final_review.agent.md",
]

def normalize(raw: str) -> str:
    raw = raw.strip().upper()
    m = re.fullmatch(r"(?:CH_?)?(\d{1,6})", raw)
    if not m:
        raise SystemExit("Chapter must look like CH_0001 or 1")
    return f"CH_{int(m.group(1)):04d}"

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/new_chapter.py CH_0002")
    chapter = normalize(sys.argv[1])
    number = int(chapter.split("_")[1])
    previous = None if number <= 1 else f"CH_{number-1:04d}"
    dest = ROOT / "07_workbench" / chapter
    if dest.exists():
        raise SystemExit(f"Already exists: {dest}")
    dest.mkdir(parents=True)
    for name in FILES:
        text = (TEMPLATES / name).read_text(encoding="utf-8")
        text = text.replace("CH_XXXX", chapter)
        if name == "00_author_brief.md":
            text = text.replace("previous_chapter: " + chapter, f"previous_chapter: {previous or 'null'}")
        (dest / name).write_text(text, encoding="utf-8")
    for name in EMPTY:
        (dest / name).write_text("", encoding="utf-8")
    print(dest)

if __name__ == "__main__":
    main()
