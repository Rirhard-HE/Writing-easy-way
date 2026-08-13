---
chapter: CH_XXXX
status: not_started
source_draft: 05_draft.md
source_draft_sha256: null
body_character_count: null
length_target_min: 4000
length_target_max: 6000
length_hard_ceiling: 9000
author_length_decision: null
decided_by: null
decided_at: null
repetition_review: NOT_RUN
negative_catalog_review: NOT_RUN
---

# Length Gate

## Measurement

- 计算口径：去除 front matter、章节一级标题和全部空白字符，保留正文中的汉字、字母、数字与标点。
- `4000–6000`：`pass`。
- `6001–9000`：`awaiting_author`，作者决定保留后改为 `author_retained`；选择压缩则改为 `revision_required` 并重写草稿。
- `>9000`：`revision_required`，不得进入最终审阅。

## Repetition Review

- 检查同一标的物是否在没有新增动作、状态、因果或情绪功能时反复点名。
- 检查“安静几秒”“沉默两秒”等同构停顿句及最近章节显眼模板。

## Negative-catalog Review

- 检查并删除“没有 A/B/C，只有 D”式边界审查语言；只正面描写实际出现内容。

## Author Decision

- decision: `RETAIN | CONDENSE | NOT_REQUIRED`
- notes:
