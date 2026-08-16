# Author-led Chapter Transaction Workflow

```text
AUTHOR MATERIAL + INTENT
          ↓
CONTEXT PACK
          ↓
BOUNDARY CONTRACT + EXPANSION PROPOSAL
          ↓
CONTINUITY / SETTING-CONFLICT / REVEAL REVIEW
          + AUTHOR-INPUT LOGIC / INFORMATION-GAP REVIEW
          ↓
AUTHOR DECISION
          ↓
CONSTRAINED EXPANDED DRAFT
          ↓
LENGTH / REPETITION / NEGATIVE-CATALOG GATE
          ↓
FINAL PROSE REVIEW
          ↓
MEMORY + SETTING DELTA
          ↓
AUTHOR APPROVAL
          ↓
MANUSCRIPT / CANON / STATE UPDATE
```

## 1. 作者输入

作者在 `00_author_brief.md` 中提供本章的创作核心。至少包括：

- 作者写出的剧情材料、场景内容、关键行动或关键对话；
- `must_happen`；
- `must_not_happen`；
- Agent 可以扩写的 `flexible` 范围；
- 本章有意新增或修改的设定（如有）。

如果核心材料不足，Agent 可以整理问题和上下文，但不得代替作者决定“本章到底发生什么”。

作者输入同时接受逻辑检查。若因果、时空、能力、知识边界或相互冲突的要求存在明显缺口，并且不同补法会改变剧情、人物选择、揭示或长期状态，Agent 必须先向作者索取信息，不能自行选择一个版本继续写。

## 2. 边界合同

Agent 在 `02_expansion.agent.md` 开头生成本章边界合同：

- 固定剧情与不可改写内容；
- 角色知识与 POV 边界；
- 揭示门与禁止解释；
- 世界、时间线、地点和能力硬约束；
- 可自由扩写的范围；
- 需要作者决定的新增事实。

边界合同是对作者输入和权威状态的整理，不得新增 Canon。

## 3. 内容扩写

在作者授权的范围内，Agent 可以补充：

- 场景衔接与动作微节拍；
- 空间关系、感官细节和环境反应；
- 已有动机支持下的情绪层次与潜台词；
- 不改变含义的对话润色或备选表达；
- 节奏、信息分配和段落结构；
- 不产生永久状态变化的临时细节。

扩写同时执行 `00_system/prose_generation_policy.md`：

- 保留核心观点、事实关系、逻辑结构、事件顺序、知识边界和有效信息量；
- 调整句法与段落分布，减少机械短句链、固定过渡、过度概括与解释性收束；
- 使用有选择的生活细节、人物打断、改口和不完全回应增加真实写作痕迹；
- 网络梗必须符合人物、场景、时代和揭示边界，不得强行进入旁白或替代必要内容。

自 `CH_0009` 起还必须绑定 `00_system/prose_style_profile.md` / `daily_light_detailed_v1`：保持日常轻松的基准语感，增强会影响人物行动与感受的环境细节，以及带有轮次、动作、潜台词和人物差异的对话细节。人物标签只代表倾向，具体反应还须结合目标、压力、疲劳、关系和风险。严肃段落不得被强行卸压；环境不得成为陈列清单，对话不得成为设定问答。

每次生成还自动执行 `00_system/narrative_generation_directive.md` / `situated_prose_v1`。即使作者没有逐次审阅或重述风格，也必须维持锁定基线；这只提供生成一致性，不提供正文、Delta、Canon 或写回批准。

未经作者明确授权，Agent 不得新增：

- 主线转向或谜底；
- 新世界硬规则、永久能力或关键技术结论；
- 死亡、复活、重大身份变化；
- 不可逆关系变化；
- 角色不可能知道的信息；
- 超过揭示门的解释。

## 4. 冲突与设定修改

- 新作者设定可以修改旧设定。
- Agent 必须检测并提醒明显冲突，但提醒不是对作者明确覆盖决定的否决。
- 原稿冲突标记为 `LEGACY_SOURCE_DIVERGENCE`；Canon 冲突标记为 `SETTING_CONFLICT`；秘密揭示冲突标记为 `REVEAL_CONFLICT`。
- 具体变更流程见 `00_system/change_control.md`。

## 5. 审批与写回

在最终正文审阅前，必须完成独立的草稿门检：

- 以 `05_length_decision.md` 记录正文可见字符数；常规目标为 `4000–6000`，硬上限为 `9000`。
- `6001–9000` 必须暂停并由作者决定保留或压缩；超过 `9000` 必须压缩后重新检测。
- 同时检查无功能标的物复述、同构停顿句和“没有 A/B/C，只有 D”式缺席概念清单。
- 同时检查环境是否依赖代表性物件重复、是否出现摄影分镜与逐动作短句链、是否长时间形成一句台词一段的对话梯。
- 自 `CH_0009` 起，终审还必须分别检查原意/信息保持、AI 模板、既有风格一致性、网络梗/语域和逻辑缺口；任一项不通过不得生成可审批 Delta。
- 风格一致性检查必须明确核验 `daily_light_detailed_v1`：日常轻松基线、环境细节功能、对话层次及严肃情绪重量均符合锁定要求；人物情境范围检查必须排除全天候性格标签和无依据变脸。
- 总体叙事方法检查必须核验 `situated_prose_v1` 的三层信息边界、侧面描写、环境连续性、反分镜化和对话段落节奏。
- 长度或去重门未通过时，`06_final_review.agent.md` 和 `07_memory_delta.agent.yaml` 必须保持 `not_started` 或 `stale`。

- “生成/扩写正文”与“写回长期状态”是两个独立动作。
- 一章结束后只提取 Delta，不重写整套设定。
- `BLOCKER` 或未处理的 `HIGH` 不得进入 finalize。
- 只有 `08_approval.yaml` 明确批准的正文、记忆和设定 Delta 才能写回受控目录。
- 所有被覆盖事实必须保留 Git 历史及变更来源。

阶段状态与准入条件见 `00_system/chapter_state_machine.md`。模板文件必须用 `not_started` 表示尚未生成，不能因为占位栏目存在就声称已完成。
