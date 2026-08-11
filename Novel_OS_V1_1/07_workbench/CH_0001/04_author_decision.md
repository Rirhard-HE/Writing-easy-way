---
chapter: CH_0001
status: author_decided
boundary_approved: true
expand_author_material: true
expansion_scope_approved: true
unresolved_blocker_count: 0
unresolved_high_count: 0
source_conflict_report_sha256: 30ccc2c51946d7b3b9fa3fe60337c73ba2e8540b1b0e88d35514ac1d8aa138a2
---

# Author Decisions

## Boundary Contract Decision

> 机器权威值在 front matter 的 `boundary_approved`。作者已批准边界合同。

- current state: approved
- required changes: 按下列作者决定执行。

## Conflict Decisions

### `C001` — 公司规范名（正文前必须决定）

- `A`：确认改为“克诺龙公司”，视为当前作者版本；旧稿“科隆诺科技”保留为被替代来源。
- `B`：本次为笔误，统一使用旧稿名称“科隆诺科技”。
- `C`：作者给出第三个规范名称。
- decision: `B` — 使用“科隆诺科技”；本次“克诺龙公司”为笔误。

### `C002` — POV（正文前必须决定）

- `A`：第三人称限知，贴近主角身体感受（推荐）。
- `B`：第三人称客观/较远距离。
- `C`：第一人称或作者给出的其他 POV。
- decision: `A` — 第三人称限知，贴近主角身体感受。

### `C003` — 匿名工作人员的自我介绍（正文前必须决定）

- `A`：只介绍岗位与公司所属，不报姓名或员工编号（推荐）。
- `B`：只介绍岗位，不说明公司所属。
- `C`：作者提供其他匿名介绍方式。
- decision: `A` — 只介绍岗位与公司所属，不报姓名或员工编号。

### `C004` — 舰型称谓（可延期）

- `A`：本章沿用“矿骡级探勘型驱逐舰”，是否成为正式舰型细分留到 Delta 审批（推荐）。
- `B`：改为旧稿较宽泛的“矿骡级驱逐舰”。
- `C`：作者提供其他称谓。
- decision: `A` — 本章使用“矿骡级探勘型驱逐舰”；正式舰型细分留待 Delta 审批。

## Setting Change Decisions

- change_id: `C001`
- decision: `CLARIFY`
- exact_author_wording: `C001：B`
- effective_scope: `CH_0001` 使用“科隆诺科技”；作为后续组织规范名候选进入本章 Delta 审批。
- supersedes: `00_author_brief.md` 中误写的“克诺龙公司”；与 `LEGACY_SOURCE SRCENT_0019` 一致，但不因一致而自动提升旧稿其他事实。

## Accepted Opportunities

- 批准 `02_expansion.agent.md` 的场景顺序、局部赛博朋克环境、动作微节拍、对话功能和信息分配方案。
- 接受死亡白光与复苏区冷白灯的纯视觉转场，不建立客观因果。
- 接受工作人员以岗位和科隆诺科技所属完成匿名自我介绍。

## Rejected Suggestions

- 拒绝为工作人员编造员工编号。
- 拒绝导入旧稿未被本 brief 采用的人名、编号、舰名、债务、合同、克隆批次、技术年代和后续任务。

## Additional Instructions

- 作者决定来源：当前对话；`C001:B / C002:A / C003:A / C004:A`。
- 边界合同：批准。
- 正文扩写：批准。

## Draft Authorization

> 机器权威值在 front matter 的 `expand_author_material` 与 `expansion_scope_approved`。作者已授权生成工作台正文草稿。

- allowed_expansion_scope: `02_expansion.agent.md` 中的环境、动作、对话、衔接、感官细节、即时情绪与节奏；不得越出作者事件顺序。
- forbidden_agent_additions: 旧稿未采用细节、身份/复活机制答案、事故真因、永久世界硬规则和后续主线。
