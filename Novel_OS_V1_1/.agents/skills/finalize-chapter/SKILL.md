---
name: finalize-chapter
description: Finalize an approved Novel OS chapter transaction. Use only when the author asks to complete `CH_xxxx` and `08_approval.yaml` explicitly approves final prose and the exact memory delta; otherwise stop without modifying controlled state.
---

# Finalize Chapter

1. Read the complete chapter workbench and verify `08_approval.yaml` has `approved: true`, `approve_final_prose: true`, and `approve_memory_delta: true`.
2. Stop if final review contains unresolved `BLOCKER` or `HIGH` findings, or if the proposed delta exceeds the recorded author decision.
3. Apply only the approved entries from `07_memory_delta.agent.yaml` to the necessary files in `01_canon/`, `02_characters/`, `03_world/`, `04_story/`, and `06_memory/`.
4. Copy the approved prose into `05_manuscript/` using its stable chapter ID and record source chapter and approval provenance.
5. Preserve history; never erase a contradiction or superseded fact without an explicit retcon decision.
6. Rebuild `09_index/` and run project validation.
7. Show the exact diff. Staging, committing, pushing, and opening a pull request each require separate explicit authorization.
