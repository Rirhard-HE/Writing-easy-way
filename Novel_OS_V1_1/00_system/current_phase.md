---
phase: CHAPTER_PRODUCTION
project: 灰烬重生
status: READY
source_draft: 00_sources/initial_drafts/灰烬重生_initial.docx
genesis_started: 2026-08-11
genesis_completed: 2026-08-11
production_ready_at: 2026-08-11
last_finalized_chapter: CH_0001
last_finalized_at: 2026-08-11
approved_decision_batches:
  - GENESIS_DECISION_001
default_entry_mode: AUTHOR_LED_REWRITE
reader_state_baseline: EMPTY_UNLESS_AUTHOR_APPROVED
legacy_source_policy: ON_DEMAND_EVIDENCE
---

# Current Production Phase

## Objective

以作者提供每章创作核心、Agent 建立边界合同并在授权范围内扩写的方式，开始正式章节生产。

## Genesis completion record

- 不可变原稿已建立 2 个源组、31 个源段和段落级溯源。
- 已建立 71 个源实体、39 个源事件和 35 个冲突/开放 Canon 提醒项。
- 已记录旧稿末端状态、旧稿读者暴露面和按需续写准入条件。
- `GENESIS_DECISION_001` 已应用；作者秘密基线已锁定，揭示门保持 `HIDDEN`。
- 旧稿没有被批量提升为 Canon；未获批准的原稿事实继续只作为 `LEGACY_SOURCE`。
- 专项 Truth/Reveal、Retcon/Conflict 和 Production Readiness 复核已完成。

完整审计见 `08_review/genesis_audit/13_production_readiness_audit.md`。

## Production entry rule

1. `CH_0001` 默认采用作者主导的重写入口；作者可以明确改为继承旧稿末端或采用部分旧稿要素。
2. 生产读者状态默认从空状态建立；旧稿暴露面只有经作者明确批准才继承。
3. 作者先完成 `07_workbench/CH_0001/00_author_brief.md`，并设置 `status: ready / author_input_complete: true`。
4. Agent 随后生成最小上下文、边界合同、扩写方案和冲突报告。
5. 未解决 `BLOCKER/HIGH`、未批准边界或未授权扩写时，不得生成生产级正文。
6. 作者的明确新增/覆盖/Retcon 可以取代旧设定；Agent 先提示明显冲突和影响，再按明确决定执行并保存被替代来源。

## Current chapter gate

`CH_0001` 已完成正式章节事务：正文、全部 Delta、`CHANGE_0001–0002` 与拟议稳定 ID 均获作者批准，并已写入正式 Manuscript、人物/世界状态、Story Open Questions 与 Memory。`canon_changes` 为空，未修改普通或秘密 Canon。下一生产入口为作者提供下一章核心材料，或明确要求对已批准设定发起新的变更事务。
