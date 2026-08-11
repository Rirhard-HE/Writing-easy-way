---
name: genesis-migrate
description: Migrate an existing novel draft into Novel OS during GENESIS_MIGRATION. Use for source mapping, evidence extraction, entity/event discovery, truth-layer classification, retcon analysis, author-decision batches, or pre-production consistency audits; never use it to promote draft claims directly into canon.
---

# Genesis Migration

1. Read `00_system/current_phase.md`, `AGENTS.md`, and the relevant migration audit files.
2. Treat `00_sources/` as immutable evidence. Never edit, rename, or reorder the source draft.
3. Preserve source headings and paragraph or section provenance. Do not map unstable source numbering directly to permanent chapter IDs.
4. Use `genesis_extractor` for source-explicit candidates, `truth_layer_classifier` for epistemic status, `retcon_analyst` for conflicts, and `secret_guard` for author-secret compatibility when relevant.
5. Tag every candidate as `SOURCE_EXPLICIT`, `SOURCE_IMPLIED`, `AUTHOR_CONFIRMED`, `OPEN_CANON`, `RETCON_CANDIDATE`, or `CONFLICT`.
6. Keep evidence, inference, and author decisions separate. Write proposals only under `08_review/pending/` unless the author explicitly approves another destination.
7. Present small decision batches. Stop before changing `01_canon/`, `02_characters/`, `03_world/`, `04_story/`, `05_manuscript/`, or `06_memory/`.
8. After an explicit author decision, apply only the approved delta and preserve its provenance. Committing or pushing remains a separate authorization.
