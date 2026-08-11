---
document_type: chapter_state_machine
status: active
created: 2026-08-11
---

# Chapter State Machine

每个文件的 `status` 表示已经完成的事实，不表示模板将来要执行的动作。新章所有下游产物从 `not_started` 开始。

| Stage | File | Ready status | Entry gate |
|---|---|---|---|
| Author material | `00_author_brief.md` | `ready` + `author_input_complete: true` | 作者已提供核心写作材料、边界与意图 |
| Context | `01_context.auto.md` | `generated_context` | 作者输入已完成 |
| Boundary / expansion | `02_expansion.agent.md` | `agent_proposal` | 最小上下文已生成 |
| Conflict review | `03_conflict_report.agent.md` | `agent_review` | 边界合同/扩写提案已生成 |
| Author decision | `04_author_decision.md` | `author_decided` | `boundary_approved: true`；未解决 `BLOCKER/HIGH` 均为 0 |
| Expanded draft | `05_draft.md` | `expanded_draft` | `expand_author_material: true`；`expansion_scope_approved: true` |
| Final review | `06_final_review.agent.md` | `agent_review` 或 `ready_for_approval` | 正文已经生成；进入后者时未解决 `BLOCKER/HIGH` 均为 0 |
| Delta | `07_memory_delta.agent.yaml` | `proposed` → `applied` | 正文和最终审查存在时先提取提案；正文、Delta、设定变更与受控写回获批并实际写回后标为 `applied` |
| Final approval | `08_approval.yaml` | `approved: true` | 正文、Delta、设定变更分别获得作者明确批准 |

## Gate rules

- `not_started` 文件中的说明文字和空栏目不是已生成内容。
- 下游状态不能越过上游 Gate；工程校验应将这种状态漂移报告为错误。
- 每个已生成阶段必须记录直接来源文件的 SHA-256；来源变化后旧产物视为 `stale`。
- 作者可以要求退回任一阶段；退回后必须把受影响的下游产物标为 `not_started` 或 `stale`，不得继续冒充当前结果。
- Delta 的 `applied` 只表示已按 `08_approval.yaml` 写入受控状态，不表示已暂存、提交或推送。
- `approved: true` 仍不自动授权 Git 提交或推送；版本控制动作需要独立指令。
