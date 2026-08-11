---
document_type: reader_state_policy
status: active
created: 2026-08-11
---

# Reader State Policy

## Core rule

`L5_READER_KNOWLEDGE` 只由当前生产线中已经获作者批准的正文建立。旧原稿、Genesis 审计、作者秘密、工作台提案和未批准草稿都不能自动增加读者知识。

## CH_0001 baseline

正式 `CH_0001` 默认从空的生产读者状态开始。只有作者 brief 明确要求保留的前置知识、公开设定或本章实际批准展示的内容，才可进入 L5。

如果作者明确选择“从旧稿末端续写”，Agent 必须先列出准备继承的旧稿暴露面，并由作者批准；不能把 `10_legacy_endpoint_state.md` 整体灌入上下文。

## Update rule

每章批准后，读者状态至少记录：

- 本章明确展示的事实；
- 读者可合理推断但尚未认证的线索；
- 被角色提出但可能错误的理论；
- 明确仍被隐藏或误导的项目；
- 对应章节、场景与来源。

人物知道不等于读者知道，读者猜到不等于旁白认证，作者知道更不等于任何角色或读者知道。

## Reveal changes

涉及 `AUTHOR_SECRET` 的更新必须同时满足：作者明确决定、揭示门允许、章节正文实际呈现、最终审批通过。任何一个条件缺失，都不得升级 L5 或秘密文件的 reveal status。
