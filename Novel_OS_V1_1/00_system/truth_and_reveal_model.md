# Truth & Reveal Model

This project separates **what is objectively true** from **what the manuscript, civilization, reader, and characters currently know**.

## Status vocabulary

- `AUTHOR_SECRET`: Author-confirmed objective truth that is not yet meant to be revealed.
- `AUTHOR_CONFIRMED`: Author-confirmed objective truth that may be used normally.
- `TEXT_CONFIRMED`: Explicitly stated in the current draft, but not automatically promoted to objective truth if the speaker/source can be wrong.
- `TEXT_HYPOTHESIS`: A theory, inference, belief, corporate explanation, scientific model, or character claim appearing in the draft.
- `IMPLIED`: Strongly suggested by the draft but not explicit.
- `RETCON_PENDING`: Existing text or extracted world rule likely to be revised.
- `UNRESOLVED`: Deliberately undefined or awaiting author decision.
- `DEPRECATED`: Superseded historical version; retain for provenance only.

## Epistemic layers

Every important setting statement should identify one or more layers:

1. `L0_OBJECTIVE_TRUTH` — how the universe actually works.
2. `L1_OLD_FEDERATION_MODEL` — what pre-Collapse humanity believed/knew.
3. `L2_MODERN_FEDERATION_MODEL` — current mainstream science and education.
4. `L3_ORGANIZATION_MODEL` — what a company, military, lab, cult, etc. believes or claims.
5. `L4_CHARACTER_KNOWLEDGE` — what a specific character knows/believes.
6. `L5_READER_KNOWLEDGE` — what has actually been revealed to the reader by a given chapter.

Statements at L1-L4 may be incomplete or false without contradicting L0.

## Internal information classes

Author-approved by `GENESIS_DECISION_001 / AD-002-A`. These labels are Novel OS metadata, not automatically available as in-world terminology:

- `SIGNAL_INFORMATION` — communication, ordinary data, measurements, records, transmissions, and other non-identity engineering information.
- `IDENTITY_INFORMATION` — memory, personality, identity state, and evidence used to evaluate personal continuity.
- `ONTOLOGICAL_INFORMATION` — L0 constitutive information that participates in defining an event, object, or state as reality.
- `UNRESOLVED` — the source does not provide enough evidence to choose safely.

Migration and retrieval rules:

1. A shared word or metaphor does not make two classes equivalent.
2. Character or institutional claims at L1-L4 do not promote a statement to `ONTOLOGICAL_INFORMATION`.
3. When classification is uncertain, use `UNRESOLVED`; never default upward to L0.
4. A single source passage may reference multiple classes, but each claim must be classified separately.

## Reveal gate

Secret canon must include:

- `reveal_status`: `HIDDEN | FORESHADOWED | PARTIAL | REVEALED`
- `earliest_reveal`: chapter/arc or `UNDECIDED`
- `allowed_manifestations`: effects that may appear before the truth is stated
- `forbidden_exposition`: explanations/terms that the prose agent must not use early

## Agent rule

Continuity/retrieval agents may consult secret canon to prevent contradictions.
Writer/expansion agents must not expose secret canon directly unless an author-approved reveal gate allows it. When necessary, context should pass only **sanitized constraints or observable manifestations**.

## Why this matters for 灰烬重生

The draft already contains several different meanings of “information”: ordinary communication/signals, encoded memory/personality, information-layer phenomena, and possible ontological information. These meanings must remain distinct internally even if characters conflate them.
