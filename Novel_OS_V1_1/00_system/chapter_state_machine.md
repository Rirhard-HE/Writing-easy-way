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
| Conflict review | `03_conflict_report.agent.md` | `agent_review` | 边界合同/扩写提案已生成；自 CH_0009 起包含作者输入逻辑与信息缺口审查 |
| Author decision | `04_author_decision.md` | `author_decided` | `boundary_approved: true`；未解决 `BLOCKER/HIGH` 均为 0 |
| Expanded draft | `05_draft.md` | `expanded_draft` | `expand_author_material: true`；`expansion_scope_approved: true`；自 CH_0009 起绑定锁定风格档案 |
| Length / repetition gate | `05_length_decision.md` | `pass` 或 `author_retained` | 正文已生成；正文不超过 `9000` 可见字符；超过 `6000` 时已取得作者决定；重复标的物、环境连续性、电影分镜化、对话梯、同构停顿句与缺席概念清单检查均通过 |
| Final review | `06_final_review.agent.md` | `agent_review` 或 `ready_for_approval` | 正文已经生成且长度/去重门通过；进入后者时未解决 `BLOCKER/HIGH` 均为 0，且自 CH_0009 起 prose_fidelity 五项均通过 |
| Delta | `07_memory_delta.agent.yaml` | `proposed` → `applied` | 正文和最终审查存在时先提取提案；正文、Delta、设定变更与受控写回获批并实际写回后标为 `applied` |
| Final approval | `08_approval.yaml` | `approved: true` | 正文、Delta、设定变更分别获得作者明确批准 |

## Gate rules

- `not_started` 文件中的说明文字和空栏目不是已生成内容。
- 下游状态不能越过上游 Gate；工程校验应将这种状态漂移报告为错误。
- 每个已生成阶段必须记录直接来源文件的 SHA-256；来源变化后旧产物视为 `stale`。
- 作者可以要求退回任一阶段；退回后必须把受影响的下游产物标为 `not_started` 或 `stale`，不得继续冒充当前结果。
- Delta 的 `applied` 只表示已按 `08_approval.yaml` 写入受控状态，不表示已暂存、提交或推送。
- `approved: true` 仍不自动授权 Git 提交或推送；版本控制动作需要独立指令。
- 自 `CH_0005` 起，`05_length_decision.md` 是强制门禁。`6001–9000` 字符必须使用 `awaiting_author` 暂停；作者明确保留后才可改为 `author_retained`。超过 `9000` 必须使用 `revision_required`，不得以作者保留直接越过硬上限。
- 长度门的字符数按正文去除 front matter、一级标题和空白后的 Unicode 字符计数；任何正文修改都会使该门的来源指纹失效。
- `repetition_review` 与 `negative_catalog_review` 必须为 `PASS`；边界说明应留在审查文件，不得通过正文中的否定清单表达。
- 自 `CH_0009` 起，作者决定阶段不得绕过 `author_input_logic_review`；明显信息缺口未解决时，正文必须保持 `not_started / stale`。
- 自 `CH_0009` 起，`meaning_preservation_review`、`ai_pattern_review`、`style_consistency_review`、`style_profile_review`、`character_range_review`、`meme_register_review`、`logic_gap_review` 必须全部为 `PASS`，才能进入 `ready_for_approval` 和 Delta。
- 自 `CH_0009` 起，brief、扩写提案、正文和终审必须声明 `style_profile: daily_light_detailed_v1`；只有作者明确记录覆盖决定后才能解除或更换锁定。
- 自 `CH_0009` 起，brief、扩写提案、正文和终审必须声明 `narrative_directive: situated_prose_v1`；该指令在作者未逐次审阅时仍自动执行，但不绕过任何作者审批门。
