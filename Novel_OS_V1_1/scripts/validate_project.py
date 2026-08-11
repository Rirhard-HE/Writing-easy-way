#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRS = [
    "00_system", "01_canon", "02_characters", "03_world", "04_story",
    "05_manuscript", "06_memory", "07_workbench", "08_review", "09_index",
    ".agents/skills", ".codex/agents"
]
REQUIRED_FILES = ["AGENTS.md", "README.md", ".codex/config.toml"]
CHAPTER_RE = re.compile(r"^CH_\d{4,6}$")

errors = []
warnings = []

for rel in REQUIRED_DIRS:
    if not (ROOT / rel).is_dir():
        errors.append(f"Missing directory: {rel}")
for rel in REQUIRED_FILES:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing file: {rel}")

wb = ROOT / "07_workbench"
if wb.exists():
    for p in wb.iterdir():
        if p.is_dir() and p.name != "_templates":
            if not CHAPTER_RE.match(p.name):
                warnings.append(f"Non-standard workbench chapter directory: {p.name}")
            required = [
                "00_author_brief.md", "01_context.auto.md", "02_expansion.agent.md",
                "03_conflict_report.agent.md", "04_author_decision.md", "05_draft.md",
                "06_final_review.agent.md", "07_memory_delta.agent.yaml", "08_approval.yaml"
            ]
            for name in required:
                if not (p / name).exists():
                    errors.append(f"{p.name}: missing {name}")

print("Novel OS validation")
print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
for e in errors:
    print("ERROR:", e)
for w in warnings:
    print("WARN:", w)
sys.exit(1 if errors else 0)
