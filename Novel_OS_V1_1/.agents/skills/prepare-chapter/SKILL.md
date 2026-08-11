---
name: prepare-chapter
description: Prepare a Novel OS chapter transaction when the author asks “准备 CH_xxxx” or requests context, expansion proposals, and continuity review before drafting. Use only after an author brief exists; do not generate final prose or modify canon.
---

# Prepare Chapter

1. Normalize the requested ID and read `07_workbench/<CHAPTER>/00_author_brief.md`.
2. Treat `must_happen`, `must_not_happen`, and explicit author constraints as a contract. Report missing or conflicting requirements instead of guessing.
3. Ask `context_retriever` for a concise evidence-backed context pack and write it to `01_context.auto.md`. Exclude secret canon; include only sanitized constraints when required.
4. Write optional connective beats and conflict opportunities to `02_expansion.agent.md`. Label additions as proposals, not facts.
5. Run only relevant read-only reviewers, commonly `character_continuity`, `timeline_continuity`, `world_continuity`, `plot_continuity`, and `foreshadow_continuity`; add `secret_guard` when reveal leakage is possible.
6. Consolidate duplicate findings into `03_conflict_report.agent.md`. For each finding include severity, evidence paths or IDs, impact, and the required author decision.
7. Stop after preparation. Do not write `05_draft.md`, modify controlled directories, commit, or push.
