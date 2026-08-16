# Novel OS — Codex Project Instructions

## Authority model

The human author is the sole authority over plot, canon, retcons, character death/resurrection, world rules, mystery resolution, and final prose approval.
Agents propose. Humans approve. Only approved changes may become canonical state.

The author may add, revise, or replace an earlier setting at any time. An explicit current author change outranks older canon and draft evidence. The agent must identify obvious conflicts and impact before applying the change, but must not treat existing files as a veto over an explicit author override.

## Source-of-truth hierarchy

When sources conflict, use this precedence unless an explicit author decision says otherwise:
1. Current explicit author decision in `07_workbench/<CHAPTER>/04_author_decision.md`
2. Current chapter brief in `07_workbench/<CHAPTER>/00_author_brief.md`
3. `01_canon/`
4. Current entity state in `02_characters/` and `03_world/`
5. Final manuscript in `05_manuscript/`
6. Approved memory in `06_memory/`
7. Story plans in `04_story/`
8. Agent suggestions and generated context

Never silently reconcile conflicting sources. Report the conflict and cite the files involved.

## Write boundaries

Agents may freely create or edit files inside:
- `07_workbench/`
- `08_review/pending/`
- `09_index/` (derived data only)

Do NOT directly modify these controlled areas unless the current chapter has explicit human approval authorizing the exact delta:
- `01_canon/`
- `02_characters/`
- `03_world/`
- `05_manuscript/`
- `06_memory/`

Never treat `09_index/` as canonical. It must be rebuildable from source files.

## Chapter transaction workflow

Every chapter is a transaction:
1. Author writes the core chapter material in `00_author_brief.md`, including intended events, any usable prose/dialogue fragments, prohibited content, and deliberate setting changes.
2. Build `01_context.auto.md` from relevant authoritative sources.
3. Produce a boundary contract and expansion proposal in `02_expansion.agent.md` without changing canon.
4. Run parallel continuity review and write `03_conflict_report.agent.md`.
5. Stop for human decisions in `04_author_decision.md` when blockers/high-impact choices exist.
6. Write `05_draft.md` only from approved constraints.
7. Run final prose continuity review into `06_final_review.agent.md`.
8. Extract only chapter deltas into `07_memory_delta.agent.yaml`.
9. Do not commit deltas until `08_approval.yaml` explicitly says `approved: true`.
10. After approval, update canonical state, copy final prose into `05_manuscript/`, and record provenance.

The author supplies the chapter's creative payload. Agents may set continuity/reveal boundaries and expand transitions, scene mechanics, sensory detail, dialogue support, emotional subtext, and pacing. Agents may not originate a major plot turn, mystery answer, permanent setting rule, death/resurrection, identity resolution, or irreversible relationship change unless the brief marks it as author-owned material or the author later approves it.

## Prose fidelity and author-input challenge

All production prose from `CH_0009` onward must follow `00_system/prose_generation_policy.md` (`prose_fidelity_v1`). Naturalization must preserve core meaning, fact relations, logical structure, knowledge boundaries, event order, and useful information quantity while reducing mechanical sentence patterns, over-summary, repeated scaffolding, and voice flattening.

Do not assume human input is logically complete. Check causality, timeline, location, capability, character knowledge, reveal gates, and mutually incompatible requirements. If an obvious missing fact or contradiction could change plot, character choice, world rules, reveal, or durable state, stop draft generation and request the missing information. Minor reversible ambiguity may be handled only as an explicitly labeled bounded assumption.

Chinese-internet meme language may appear only through a character whose voice, relationship, knowledge, mood, and scene permit it. Do not leak real-world cultural lineage or create anachronistic platform/event references; prefer in-world meme-like phrasing when exact contemporary wording would exceed the reveal boundary. Memes cannot replace required information or emotional consequences.

## Locked prose style

All production prose from `CH_0009` onward uses `00_system/prose_style_profile.md` (`daily_light_detailed_v1`). Keep the baseline everyday, relaxed, and human while preserving the weight of grief, danger, conflict, and revelation. Strengthen environment and dialogue detail through character interaction, spatial/causal function, subtext, interruption, correction, and differentiated voices; do not turn detail into catalogs or dialogue into exposition Q&A.

This profile changes expression only. It may not change plot, facts, causality, event order, knowledge boundaries, or useful information quantity. Do not silently switch profiles. Only an explicit author override recorded in the workflow may unlock or replace it.

## Overall narrative-generation directive

All drafting and prose review from `CH_0009` onward must read and apply `00_system/narrative_generation_directive.md` (`situated_prose_v1`). Treat character state, relationship, environment, dialogue, and narrative rhythm as one situated system. Maintain a scene through spatial relations, ongoing conditions, causal consequences, and distributed indirect cues; do not repeatedly name one object merely to preserve environmental consistency.

Write prose, not a shot list. Avoid camera-stage language, one-action-per-line fragmentation, and extended one-line dialogue ladders with uniform action beats. Brief rapid exchanges and short-sentence sequences are allowed when pressure, conflict, timing, or comic rhythm specifically justifies them. Preserve fixed narrative information, distinguish reversible scene texture from durable state, and route any durable addition through Delta approval.

## Author-led setting change policy

When the author introduces or changes a setting:

1. Distinguish brainstorming from an explicit setting decision. Brainstorming remains a proposal.
2. Classify an explicit decision as `ADD`, `CLARIFY`, `OVERRIDE`, `RETCON`, or `DEPRECATE`.
3. Scan current canon, entity state, approved memory, story plans, final manuscript, and relevant source evidence for impact.
4. If an obvious conflict exists, report a concise `SETTING_CONFLICT` containing the old fact, new author fact, affected files/IDs/chapters, and likely consequences.
5. If the author explicitly requested the override, apply it after the warning and preserve the old version as superseded provenance. If the author's intent is ambiguous, stop for confirmation.
6. Never silently reconcile, erase, or conceal a contradiction.

Detailed procedure: `00_system/change_control.md`.

## MUST / MUST NOT / FLEXIBLE

Treat the chapter brief as a contract:
- `must_happen`: required beats.
- `must_not_happen`: prohibited beats/disclosures.
- `flexible`: areas the agent may elaborate.

Never move content from FLEXIBLE into canonical facts unless the author approves the resulting memory delta.

## Continuity rules

Always check, where relevant:
- character knowledge boundaries (author knowledge != character knowledge)
- current location and travel feasibility
- injuries, abilities, inventory, identity, age, titles
- relationship state and recent changes
- timeline and event ordering
- world hard rules
- open foreshadowing and reveal gates
- causal consistency with prior events
- POV and narrative voice constraints

Classify findings as `BLOCKER`, `HIGH`, `MEDIUM`, `LOW`, or `OPPORTUNITY`.
Every conflict must include evidence paths; include chapter/event/entity IDs when available.

## Retrieval discipline

Do not dump the entire manuscript into a chapter context. Prefer this order:
1. Explicit IDs from the chapter brief.
2. Current character/world state.
3. Recent chapters.
4. Directly linked events, threads, and foreshadowing.
5. Exact-text/metadata search.
6. Semantic retrieval only when needed.
7. Legacy source evidence only when the author brief requests original-draft continuity, reuse, comparison, or rewrite.

Context packs should be concise, evidence-backed, and oriented toward the current chapter.
Legacy source evidence never overrides a current author decision or Canon, and legacy draft exposure never sets `L5_READER_KNOWLEDGE` for the production manuscript.

## Data conventions

- Use stable IDs, not names, as primary identifiers.
- Markdown + YAML front matter are canonical human-readable storage.
- Use UTF-8.
- Preserve historical versions through Git; do not erase conflicting history to make a problem disappear.
- Derived indexes may be deleted and rebuilt.

## Default agent delegation

For continuity review, use parallel read-only subagents when useful:
- `character_continuity`
- `timeline_continuity`
- `world_continuity`
- `plot_continuity`
- `foreshadow_continuity`

Wait for all requested reviewers, then consolidate duplicates into one report. Reviewers must not edit controlled files.

## Formal Codex work mode

This repository is now in formal production mode. Treat chat discussions as instructions only when they are explicitly written into repository artifacts or clearly stated as author decisions in the current task.

For any substantial task, use this lifecycle:
1. `EVIDENCE` — identify source text / authoritative project files.
2. `PROPOSAL` — write extracted facts, interpretations, edits, or retcon candidates into a review/workbench artifact.
3. `AUTHOR DECISION` — stop when a choice would change canon, reveal policy, plot ownership, or a controlled file.
4. `COMMIT` — only after approval, apply the exact approved delta and preserve provenance in Git.

Never collapse evidence, inference, and author-confirmed canon into one category.

## Genesis migration mode

Current phase is defined in `00_system/current_phase.md`.
While phase = `GENESIS_MIGRATION`:
- `00_sources/initial_drafts/` is immutable source evidence.
- Existing manuscript wording is not automatically canon.
- Extraction output belongs in `08_review/genesis_audit/` until approved.
- Facts must be tagged as `SOURCE_EXPLICIT`, `SOURCE_IMPLIED`, `AUTHOR_CONFIRMED`, `OPEN_CANON`, `RETCON_CANDIDATE`, or `CONFLICT`.
- Do not populate character/world/canon cards from the draft without author approval.
- Prefer preserving a source statement as an in-world belief when it conflicts with a deeper author truth and can safely remain as limited knowledge.

## Secret canon isolation

`01_canon/secret/` contains author-level truths that may be unknown to characters and readers.
- Do not include secret canon in ordinary chapter context packs.
- Do not expose a secret through narration, dialogue, explanation, or agent-added detail unless its reveal gate is explicitly open.
- Continuity reviewers may consult secret canon only when needed to check whether a draft contradicts objective truth or leaks it prematurely.
- When reporting such a conflict, describe the leak minimally and point to the secret file; do not expand the secret into prose suggestions.
- Character knowledge files and reader reveal state always constrain what may appear on-page.
