# Stable ID Convention

| 类型 | 格式 | 示例 |
|---|---|---|
| Chapter | `CH_0001` | CH_0843 |
| Character | `CHR_0001` | CHR_0012 |
| Location | `LOC_0001` | LOC_0021 |
| Faction | `FAC_0001` | FAC_0007 |
| Event | `EVT_000001` | EVT_001922 |
| Foreshadow | `F_0001` | F_0102 |
| Item | `ITEM_0001` | ITEM_0044 |
| System / Technology | `SYS_0001` | SYS_0044 |
| Arc | `ARC_0001` | ARC_0005 |
| Sequence | `SEQ_0001` | SEQ_0017 |
| Thread | `THREAD_0001` | THREAD_0017 |
| Setting Change | `CHANGE_0001` | CHANGE_0017 |
| Open Question | `QUESTION_0001` | QUESTION_0017 |
| Source Group | `SRCGRP_0001` | SRCGRP_0002 |
| Source Segment | `SRCSEG_0001` | SRCSEG_0031 |
| Source Entity | `SRCENT_0001` | SRCENT_0042 |
| Source Event | `SRCEVT_000001` | SRCEVT_000127 |
| Source Claim | `SRCCLAIM_000001` | SRCCLAIM_000513 |

## 原则

- ID 永不复用。
- 名称可以变，ID 不变。
- 文件引用尽量同时包含 `名称 [ID]`。
- `SRC*` ID 只标识原稿证据，不等于 Canon ID，也不得自动一一转换为 `CHR/EVT/CH/...`。
- 当作者批准某个源实体或源事件进入 Canon 时，新建正式 ID，并在正式卡中保存对应 `SRC*` provenance。
