---
document_type: genesis_migration_rules
status: active
phase: GENESIS_MIGRATION
source_draft: 00_sources/initial_drafts/灰烬重生_initial.docx
source_sha256: 227f21fe7082fe528cbd9afcc470206565c399d6f76943b7b16d8ce695487643
decision_provenance: 08_review/pending/02_author_decision_batch_001.md
approved_at: 2026-08-11
---

# Genesis Migration Rules

本文件记录作者已批准的创世迁移执行规则。它不把原稿内容自动提升为 Canon。

## Source provenance policy — AD-001-A

1. `00_sources/initial_drafts/灰烬重生_initial.docx` 是不可变证据源。
2. 当前批准的结构映射是 2 个源组和 31 个源段：
   - `SRCGRP_0001`：`SRCSEG_0001`–`SRCSEG_0020`；
   - `SRCGRP_0002`：`SRCSEG_0021`–`SRCSEG_0031`。
3. 每个抽取条目必须保存：
   - 临时源段 ID；
   - 原稿显示标题；
   - 以 1 为起点的非空段落范围；
   - 源文件相对路径与 SHA-256；
   - 证据分类与推断分类。
4. 原稿显示标题永久保留，不因缺号、重号或“章/篇”混用而被覆盖。
5. `顺序工作标题` 仅作为迁移别名；不得作为原稿实际标题或正式章节标题。
6. `SRCGRP`、`SRCSEG` 不得直接转换为永久 `CH###`、`EVT_######` 或其他 Canon ID。
7. 首轮实体、事件和时间线抽取完成前，不重排源段。
8. 正式章序、事件合并/拆分及 Canon 提升仍须独立作者批准。

源实体、源事件和源陈述可以分别获得 `SRCENT_####`、`SRCEVT_######`、`SRCCLAIM_######` 证据 ID。这些 ID 只用于去重和溯源，不构成 Canon 提升。

完整的段落级映射见 `08_review/pending/01_source_segment_map_pass2.md`。

## Information classification policy — AD-002-A

迁移中遇到“信息”时，必须使用 `00_system/truth_and_reveal_model.md` 定义的三分类：

- `SIGNAL_INFORMATION`；
- `IDENTITY_INFORMATION`；
- `ONTOLOGICAL_INFORMATION`。

无法确定的条目标记为 `UNRESOLVED`。不得因术语相同、角色推测或工程类比，将普通信息或身份信息默认提升为本体信息。

## Extraction status tags

每个迁移候选必须明确标记为下列之一：

- `SOURCE_EXPLICIT`；
- `SOURCE_IMPLIED`；
- `AUTHOR_CONFIRMED`；
- `OPEN_CANON`；
- `RETCON_CANDIDATE`；
- `CONFLICT`。

证据、推断与作者决定必须分开记录。

## Secret isolation

`AD-003-A` 与 `AD-004-C` 只存放在 `01_canon/secret/ontology.md`。普通抽取文件、章节上下文和正文生成只能接收经过净化的约束或已授权现象；不得复制其 L0 机制解释。
