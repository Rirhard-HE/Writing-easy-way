#!/usr/bin/env python3
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRS = [
    "00_system", "01_canon", "02_characters", "03_world", "04_story",
    "05_manuscript", "06_memory", "07_workbench", "08_review", "09_index",
    "03_world/_templates", "04_story/_templates", "06_memory/_templates",
    ".agents/skills", ".codex/agents"
]
REQUIRED_FILES = [
    "AGENTS.md", "README.md", "START_HERE.md", ".codex/config.toml",
    "00_system/change_control.md", "00_system/chapter_state_machine.md",
    "00_system/production_contract.md", "00_system/reader_state_policy.md",
    "00_system/truth_and_reveal_model.md", "00_system/workflow.md",
    "08_review/genesis_audit/07_source_segment_digest_pass2.md",
    "08_review/genesis_audit/08_source_entity_registry_pass2.md",
    "08_review/genesis_audit/09_source_event_ledger_pass2.md",
    "08_review/genesis_audit/10_legacy_endpoint_state.md",
    "08_review/genesis_audit/11_conflict_and_open_canon_register_pass2.md",
    "08_review/genesis_audit/12_reveal_guard_pass2.md",
    "08_review/genesis_audit/13_production_readiness_audit.md",
]
CHAPTER_RE = re.compile(r"^CH_\d{4,6}$")
WORKBENCH_FILES = [
    "00_author_brief.md", "01_context.auto.md", "02_expansion.agent.md",
    "03_conflict_report.agent.md", "04_author_decision.md", "05_draft.md",
    "06_final_review.agent.md", "07_memory_delta.agent.yaml", "08_approval.yaml"
]
LENGTH_GATE_FILE = "05_length_decision.md"
LENGTH_GATE_ENFORCED_FROM = 5
LENGTH_GATE_STATUSES = {
    "not_started", "awaiting_author", "pass", "author_retained",
    "revision_required", "stale"
}
AUTHOR_BRIEF_SECTIONS = [
    "# 作者写作材料（必填）", "# 本章核心剧情（必填）", "# must_happen",
    "# must_not_happen", "# flexible", "# 本章新增或修改设定"
]
STATUS_BY_FILE = {
    "00_author_brief.md": {"planning", "ready", "stale"},
    "01_context.auto.md": {"not_started", "generated_context", "stale"},
    "02_expansion.agent.md": {"not_started", "agent_proposal", "stale"},
    "03_conflict_report.agent.md": {"not_started", "agent_review", "stale"},
    "04_author_decision.md": {"not_started", "awaiting_author", "author_decided", "stale"},
    "05_draft.md": {"not_started", "expanded_draft", "stale"},
    "06_final_review.agent.md": {"not_started", "agent_review", "ready_for_approval", "stale"},
    "07_memory_delta.agent.yaml": {"not_started", "proposed", "applied", "stale"},
}


def coerce(value):
    value = value.strip().strip('"').strip("'")
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() == "null" or value == "~":
        return None
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def parse_frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = coerce(value)
    return data


def parse_flat_yaml(path):
    data = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = coerce(value)
    return data


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def markdown_body_character_count(path):
    """Count visible body characters, excluding front matter, first H1, and whitespace."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                lines = lines[index + 1:]
                break
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return len(re.sub(r"\s+", "", "\n".join(lines)))


def markdown_section(text, heading):
    lines = text.splitlines()
    try:
        start = lines.index(heading) + 1
    except ValueError:
        return ""
    selected = []
    for line in lines[start:]:
        if line.startswith("# "):
            break
        selected.append(line)
    return "\n".join(selected)


def has_author_content(text, heading):
    for line in markdown_section(text, heading).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(">"):
            continue
        if re.fullmatch(r"(?:[-*]|\d+\.)\s*", stripped):
            continue
        if stripped in {"- Agent 可自由补充：", "Agent 可自由补充："}:
            continue
        return True
    return False


def check_fingerprint(chapter, label, data, key, source_path):
    expected = data.get(key)
    actual = file_sha256(source_path)
    if expected != actual:
        errors.append(f"{chapter}/{label}: {key} is missing or stale")

errors = []
warnings = []
current_phase = None

for rel in REQUIRED_DIRS:
    if not (ROOT / rel).is_dir():
        errors.append(f"Missing directory: {rel}")
for rel in REQUIRED_FILES:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing file: {rel}")

for name in WORKBENCH_FILES:
    template = ROOT / "07_workbench" / "_templates" / name
    if not template.is_file():
        errors.append(f"Missing workbench template: {name}")
    elif not template.read_text(encoding="utf-8").strip():
        errors.append(f"Empty workbench template: {name}")
length_gate_template = ROOT / "07_workbench" / "_templates" / LENGTH_GATE_FILE
if not length_gate_template.is_file():
    errors.append(f"Missing workbench template: {LENGTH_GATE_FILE}")
elif not length_gate_template.read_text(encoding="utf-8").strip():
    errors.append(f"Empty workbench template: {LENGTH_GATE_FILE}")

phase_file = ROOT / "00_system" / "current_phase.md"
if phase_file.is_file():
    phase_text = phase_file.read_text(encoding="utf-8")
    phase_match = re.search(r"^phase:\s*([A-Z_]+)\s*$", phase_text, re.MULTILINE)
    if not phase_match:
        errors.append("current_phase.md: missing phase")
    elif phase_match.group(1) not in {"GENESIS_MIGRATION", "CHAPTER_PRODUCTION"}:
        errors.append(f"current_phase.md: unsupported phase {phase_match.group(1)}")
    else:
        phase_data = parse_frontmatter(phase_file)
        current_phase = phase_match.group(1)
        if current_phase == "CHAPTER_PRODUCTION" and phase_data.get("status") != "READY":
            errors.append("current_phase.md: CHAPTER_PRODUCTION requires status READY")

secret_root = ROOT / "01_canon" / "secret"
secret_headings = []
if secret_root.is_dir():
    for secret_path in sorted(secret_root.rglob("*")):
        if not secret_path.is_file() or secret_path.suffix.lower() not in {".md", ".yaml", ".yml"}:
            continue
        data = parse_frontmatter(secret_path) if secret_path.suffix.lower() == ".md" else parse_flat_yaml(secret_path)
        rel = secret_path.relative_to(ROOT).as_posix()
        required_secret_metadata = {
            "audience": "AUTHOR_ONLY",
            "context_policy": "EXCLUDE_FROM_DRAFT_GENERATION",
            "reader_state_effect": "NONE",
        }
        for key, expected in required_secret_metadata.items():
            if data.get(key) != expected:
                errors.append(f"{rel}: secret metadata {key} must be {expected}")
        if data.get("reveal_status") not in {"HIDDEN", "FORESHADOWED", "PARTIAL", "REVEALED"}:
            errors.append(f"{rel}: missing or invalid reveal_status")
        if data.get("earliest_reveal") in {None, ""}:
            errors.append(f"{rel}: missing earliest_reveal")
        if data.get("reveal_status") != "REVEALED":
            for line in secret_path.read_text(encoding="utf-8").splitlines():
                if line.startswith("# "):
                    secret_headings.append(line[2:].strip())
                    break

legacy_policy_files = [
    ROOT / f"08_review/genesis_audit/{number}_{name}"
    for number, name in (
        ("07", "source_segment_digest_pass2.md"),
        ("08", "source_entity_registry_pass2.md"),
        ("09", "source_event_ledger_pass2.md"),
        ("10", "legacy_endpoint_state.md"),
        ("11", "conflict_and_open_canon_register_pass2.md"),
    )
]
for legacy_path in legacy_policy_files:
    if not legacy_path.is_file():
        continue
    data = parse_frontmatter(legacy_path)
    rel = legacy_path.relative_to(ROOT).as_posix()
    if data.get("reader_state_effect") != "NONE":
        errors.append(f"{rel}: legacy evidence must declare reader_state_effect NONE")
    if data.get("context_policy") != "LEGACY_ONLY_ON_EXPLICIT_AUTHOR_BRIEF":
        errors.append(f"{rel}: missing legacy-only context policy")

index_path = ROOT / "09_index" / "file_index.json"
if index_path.is_file() and "01_canon/secret/" in index_path.read_text(encoding="utf-8"):
    errors.append("file_index.json: ordinary retrieval index contains secret path")
if index_path.is_file() and '"audience": "AUTHOR_ONLY"' in index_path.read_text(encoding="utf-8"):
    errors.append("file_index.json: ordinary retrieval index contains author-only entry")

migration_rules = ROOT / "00_system" / "genesis_migration_rules.md"
if migration_rules.is_file():
    migration_data = parse_frontmatter(migration_rules)
    source_rel = migration_data.get("source_draft")
    expected_hash = migration_data.get("source_sha256")
    if source_rel and expected_hash:
        source_path = ROOT / str(source_rel)
        if not source_path.is_file():
            errors.append(f"Missing immutable source draft: {source_rel}")
        else:
            actual_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
            if actual_hash != expected_hash:
                errors.append(f"Immutable source hash mismatch: {source_rel}")

wb = ROOT / "07_workbench"
if wb.exists():
    for p in wb.iterdir():
        if p.is_dir() and p.name != "_templates":
            chapter_number = None
            if not CHAPTER_RE.match(p.name):
                warnings.append(f"Non-standard workbench chapter directory: {p.name}")
            else:
                chapter_number = int(p.name.split("_")[1])
            for name in WORKBENCH_FILES:
                if not (p / name).exists():
                    errors.append(f"{p.name}: missing {name}")
                elif not (p / name).read_text(encoding="utf-8").strip():
                    errors.append(f"{p.name}: empty {name}")
            brief = p / "00_author_brief.md"
            brief_text = ""
            if brief.is_file():
                brief_text = brief.read_text(encoding="utf-8")
                for section in AUTHOR_BRIEF_SECTIONS:
                    if section not in brief_text:
                        errors.append(f"{p.name}: author brief missing section {section}")

            stage = {}
            for name in WORKBENCH_FILES[:-1]:
                path = p / name
                if not path.is_file():
                    continue
                data = parse_frontmatter(path) if path.suffix == ".md" else parse_flat_yaml(path)
                stage[name] = data
                status = data.get("status")
                if status not in STATUS_BY_FILE[name]:
                    errors.append(f"{p.name}/{name}: unsupported status {status!r}")
                if data.get("chapter") != p.name:
                    errors.append(f"{p.name}/{name}: chapter field does not match directory")

            brief_data = stage.get("00_author_brief.md", {})
            author_ready = (
                brief_data.get("author_input_complete") is True
                and brief_data.get("status") == "ready"
            )
            if brief_data.get("author_input_complete") is True and brief_data.get("status") != "ready":
                errors.append(f"{p.name}: author_input_complete true requires status ready")
            if brief_data.get("status") == "ready" and brief_data.get("author_input_complete") is not True:
                errors.append(f"{p.name}: status ready requires author_input_complete true")
            if brief_data.get("author_input_complete") is True:
                for heading in (
                    "# 作者写作材料（必填）",
                    "# 本章核心剧情（必填）",
                    "# must_happen",
                    "# must_not_happen",
                    "# flexible",
                ):
                    if not has_author_content(brief_text, heading):
                        errors.append(f"{p.name}: completed author brief has no content under {heading}")
            if current_phase == "GENESIS_MIGRATION" and author_ready:
                errors.append(f"{p.name}: author-ready production chapter while phase is GENESIS_MIGRATION")
            for name in WORKBENCH_FILES[1:7]:
                status = stage.get(name, {}).get("status")
                if status not in {None, "not_started", "stale"} and not author_ready:
                    errors.append(f"{p.name}/{name}: active downstream stage before author brief is ready")

            context_ready = stage.get("01_context.auto.md", {}).get("status") == "generated_context"
            proposal_ready = stage.get("02_expansion.agent.md", {}).get("status") == "agent_proposal"
            review_ready = stage.get("03_conflict_report.agent.md", {}).get("status") == "agent_review"
            decision_data = stage.get("04_author_decision.md", {})
            decision_ready = (
                decision_data.get("status") == "author_decided"
                and decision_data.get("boundary_approved") is True
                and decision_data.get("unresolved_blocker_count") == 0
                and decision_data.get("unresolved_high_count") == 0
            )
            draft_ready = stage.get("05_draft.md", {}).get("status") == "expanded_draft"
            final_status = stage.get("06_final_review.agent.md", {}).get("status")
            delta_ready = stage.get("07_memory_delta.agent.yaml", {}).get("status") in {"proposed", "applied"}
            length_gate_required = (
                chapter_number is not None
                and chapter_number >= LENGTH_GATE_ENFORCED_FROM
            )
            length_gate_path = p / LENGTH_GATE_FILE
            length_gate_data = {}
            length_gate_ready = not length_gate_required
            if length_gate_required:
                if not length_gate_path.is_file():
                    errors.append(f"{p.name}: missing {LENGTH_GATE_FILE}")
                elif not length_gate_path.read_text(encoding="utf-8").strip():
                    errors.append(f"{p.name}: empty {LENGTH_GATE_FILE}")
                else:
                    length_gate_data = parse_frontmatter(length_gate_path)
                    gate_status = length_gate_data.get("status")
                    if gate_status not in LENGTH_GATE_STATUSES:
                        errors.append(
                            f"{p.name}/{LENGTH_GATE_FILE}: unsupported status {gate_status!r}"
                        )
                    if length_gate_data.get("chapter") != p.name:
                        errors.append(
                            f"{p.name}/{LENGTH_GATE_FILE}: chapter field does not match directory"
                        )

            if proposal_ready and not context_ready:
                errors.append(f"{p.name}: expansion proposal requires generated context")
            if context_ready:
                check_fingerprint(
                    p.name, "01_context.auto.md", stage["01_context.auto.md"],
                    "source_brief_sha256", p / "00_author_brief.md"
                )
            if review_ready and not proposal_ready:
                errors.append(f"{p.name}: conflict review requires expansion proposal")
            if proposal_ready:
                proposal_data = stage["02_expansion.agent.md"]
                check_fingerprint(
                    p.name, "02_expansion.agent.md", proposal_data,
                    "source_brief_sha256", p / "00_author_brief.md"
                )
                check_fingerprint(
                    p.name, "02_expansion.agent.md", proposal_data,
                    "source_context_sha256", p / "01_context.auto.md"
                )
            if review_ready:
                review_data = stage["03_conflict_report.agent.md"]
                check_fingerprint(
                    p.name, "03_conflict_report.agent.md", review_data,
                    "source_brief_sha256", p / "00_author_brief.md"
                )
                check_fingerprint(
                    p.name, "03_conflict_report.agent.md", review_data,
                    "source_proposal_sha256", p / "02_expansion.agent.md"
                )
            if decision_data.get("status") == "author_decided" and not review_ready:
                errors.append(f"{p.name}: author decision requires conflict review")
            if decision_data.get("status") == "author_decided" and not decision_ready:
                errors.append(f"{p.name}: author decision has unapproved boundary or unresolved BLOCKER/HIGH")
            if decision_data.get("status") == "author_decided":
                check_fingerprint(
                    p.name, "04_author_decision.md", decision_data,
                    "source_conflict_report_sha256", p / "03_conflict_report.agent.md"
                )
            if draft_ready and not (
                decision_ready
                and decision_data.get("expand_author_material") is True
                and decision_data.get("expansion_scope_approved") is True
            ):
                errors.append(f"{p.name}: expanded draft lacks author boundary/expansion authorization")
            if draft_ready:
                draft_data = stage["05_draft.md"]
                check_fingerprint(
                    p.name, "05_draft.md", draft_data,
                    "source_author_material_sha256", p / "00_author_brief.md"
                )
                check_fingerprint(
                    p.name, "05_draft.md", draft_data,
                    "source_author_decision_sha256", p / "04_author_decision.md"
                )
                if length_gate_required:
                    actual_count = markdown_body_character_count(p / "05_draft.md")
                    if draft_data.get("body_character_count") != actual_count:
                        errors.append(
                            f"{p.name}/05_draft.md: body_character_count is missing or stale "
                            f"(expected {actual_count})"
                        )
                    for key, expected in (
                        ("length_target_min", 4000),
                        ("length_target_max", 6000),
                        ("length_hard_ceiling", 9000),
                    ):
                        if draft_data.get(key) != expected:
                            errors.append(
                                f"{p.name}/05_draft.md: {key} must be {expected}"
                            )
                    if length_gate_data:
                        check_fingerprint(
                            p.name, LENGTH_GATE_FILE, length_gate_data,
                            "source_draft_sha256", p / "05_draft.md"
                        )
                        if length_gate_data.get("body_character_count") != actual_count:
                            errors.append(
                                f"{p.name}/{LENGTH_GATE_FILE}: body_character_count is missing or stale "
                                f"(expected {actual_count})"
                            )
                        gate_status = length_gate_data.get("status")
                        if actual_count > 9000 and gate_status != "revision_required":
                            errors.append(
                                f"{p.name}: draft exceeds 9000-character hard ceiling and requires revision"
                            )
                        elif 6000 < actual_count <= 9000 and gate_status not in {
                            "awaiting_author", "author_retained", "revision_required"
                        }:
                            errors.append(
                                f"{p.name}: draft above 6000 characters requires author length decision"
                            )
                        elif actual_count <= 6000 and gate_status not in {"pass", "revision_required"}:
                            errors.append(
                                f"{p.name}: in-range draft must pass length gate or be marked for revision"
                            )
                        length_gate_ready = (
                            gate_status in {"pass", "author_retained"}
                            and actual_count <= 9000
                            and length_gate_data.get("repetition_review") == "PASS"
                            and length_gate_data.get("negative_catalog_review") == "PASS"
                        )

                    draft_text = (p / "05_draft.md").read_text(encoding="utf-8")
                    prohibited_patterns = {
                        "fixed-second silence beat": r"(?:林赛|何筠|他|她)沉默了(?:一|两|二|三|\d+)秒",
                        "stock quiet-room beat": r"(?:房间|简报室|空气)[^。\n]{0,12}(?:重新)?安静(?:下来|了)?(?:几|一|两|二|三|\d+)?秒?",
                        "negative catalog narration": r"(?:上面|页面|投影|档案(?:里|中)?)[^。\n]{0,8}没有[^。\n]{0,100}[，,]\s*只有",
                    }
                    for label, pattern in prohibited_patterns.items():
                        if re.search(pattern, draft_text):
                            errors.append(f"{p.name}/05_draft.md: prohibited {label}")
            if final_status in {"agent_review", "ready_for_approval"} and not draft_ready:
                errors.append(f"{p.name}: final review requires expanded draft")
            if final_status in {"agent_review", "ready_for_approval"} and not length_gate_ready:
                errors.append(f"{p.name}: final review bypasses length/repetition gate")
            if delta_ready and not (draft_ready and final_status in {"agent_review", "ready_for_approval"}):
                errors.append(f"{p.name}: proposed delta requires draft and final review")

            final_data = stage.get("06_final_review.agent.md", {})
            if final_status == "ready_for_approval" and not (
                final_data.get("ready_for_author_approval") is True
                and final_data.get("unresolved_blocker_count") == 0
                and final_data.get("unresolved_high_count") == 0
            ):
                errors.append(f"{p.name}: ready_for_approval has unresolved BLOCKER/HIGH or false verdict")
            if final_status in {"agent_review", "ready_for_approval"}:
                check_fingerprint(
                    p.name, "06_final_review.agent.md", final_data,
                    "source_draft_sha256", p / "05_draft.md"
                )
                if length_gate_required:
                    check_fingerprint(
                        p.name, "06_final_review.agent.md", final_data,
                        "source_length_decision_sha256", length_gate_path
                    )
            if delta_ready:
                check_fingerprint(
                    p.name, "07_memory_delta.agent.yaml", stage["07_memory_delta.agent.yaml"],
                    "source_draft_sha256", p / "05_draft.md"
                )

            if secret_headings:
                for name in ("01_context.auto.md", "02_expansion.agent.md", "05_draft.md"):
                    path = p / name
                    if not path.is_file():
                        continue
                    text = path.read_text(encoding="utf-8")
                    if "01_canon/secret/" in text:
                        errors.append(f"{p.name}/{name}: ordinary generation artifact references secret path")
                    if any(heading and heading in text for heading in secret_headings):
                        errors.append(f"{p.name}/{name}: ordinary generation artifact contains hidden secret heading")

            approval_path = p / "08_approval.yaml"
            if approval_path.is_file():
                approval = parse_flat_yaml(approval_path)
                if approval.get("chapter") != p.name:
                    errors.append(f"{p.name}/08_approval.yaml: chapter field does not match directory")
                if approval.get("approved") is True and not (
                    final_status == "ready_for_approval"
                    and delta_ready
                    and approval.get("approve_final_prose") is True
                    and approval.get("approve_memory_delta") is True
                ):
                    errors.append(f"{p.name}: final approval bypasses prose/delta gates")
                if approval.get("approved") is True and approval.get("approved_at") is None:
                    errors.append(f"{p.name}: final approval requires approved_at")
                delta_path = p / "07_memory_delta.agent.yaml"
                if approval.get("approved") is True and delta_path.is_file():
                    delta_text = delta_path.read_text(encoding="utf-8")
                    has_setting_changes = not re.search(
                        r"^setting_changes:\s*\[\]\s*$", delta_text, re.MULTILINE
                    )
                    if has_setting_changes and approval.get("approve_setting_changes") is not True:
                        errors.append(f"{p.name}: setting changes exist but are not approved")
                    if has_setting_changes and approval.get("approved_change_ids") == []:
                        errors.append(f"{p.name}: setting changes require approved_change_ids")

print("Novel OS validation")
print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
for e in errors:
    print("ERROR:", e)
for w in warnings:
    print("WARN:", w)
sys.exit(1 if errors else 0)
