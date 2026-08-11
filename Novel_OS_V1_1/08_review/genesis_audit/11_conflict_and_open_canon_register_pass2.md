---
document_type: legacy_conflict_and_open_canon_register
status: PASS_2_COMPLETE
canonical: false
evidence_class: LEGACY_SOURCE
reader_state_effect: NONE
context_policy: LEGACY_ONLY_ON_EXPLICIT_AUTHOR_BRIEF
source_sha256: 227f21fe7082fe528cbd9afcc470206565c399d6f76943b7b16d8ce695487643
created: 2026-08-11
---

# Conflict and Open Canon Register — Pass 2

本登记表用于在作者沿用相关旧稿要素时触发提醒。旧稿尚未批量进入 Canon，因此这些项目默认不是 `CH_0001` 的生产阻塞项。作者明确给出新版本时，以新决定为准，并按 `00_system/change_control.md` 保存被替代来源。

## Legacy discrepancies, ambiguities and conflicts

`Current scope` 说明它们尚未进入生产 Canon；`Severity if invoked` 说明作者若要求沿用相关旧稿要素时需要多强的处理。两者不可混为一列。

| ID | Current scope | Severity if invoked | Class | Topic | Legacy evidence | Production action |
|---|---|---|---|---|---|---|
| `SRCCLAIM_000001` | `LEGACY_ONLY` | `MEDIUM` | direct name conflict | 何筠母亲姓名 | `毛晓` vs `陈岚`；`SRCSEG_0004`–`0005` | 若沿用家庭线，选择规范名；不得当作两人。 |
| `SRCCLAIM_000002` | `LEGACY_ONLY` | `MEDIUM` | direct name conflict | 何筠父亲姓名 | `何松` vs `何振川`；`SRCSEG_0004`–`0005` | 若沿用家庭线，选择规范名；不得静默合并为别名。 |
| `SRCCLAIM_000003` | `LEGACY_ONLY` | `LOW` | spelling conflict | 林塞姓名拼写 | `林塞` vs `林赛`；多段持续出现 | 正式建卡前选规范拼写，另一个只保留来源别名/错字记录。 |
| `SRCCLAIM_000004` | `LEGACY_ONLY` | `MEDIUM` | chronology clarification | 技术发现/遗迹开启年代 | “三年前发现意识回写技术” vs “二百一十四年前开启遗迹”；`SRCSEG_0001`–`0003`, `0024` | 两者可能是现代复现/商业化与遗迹首次接入；不能先验视为同一事件。 |
| `SRCCLAIM_000005` | `LEGACY_ONLY` | `MEDIUM` | institutional ambiguity | 债务处置 | 有条件口头承诺勾销 vs 合同规定任务期冻结、完成后重评；`SRCSEG_0002`, `0010` | 可为合同实现条件或企业话术落差；沿用时明确最终法律效果。 |
| `SRCCLAIM_000006` | `LEGACY_ONLY` | `HIGH` | direct geography conflict | 阿斯特拉地位 | 仙女座探索区首府 vs 旧联邦总首府；`SRCSEG_0018` | 正式地理卡前决定层级；不可让两个称号无解释并存。 |
| `SRCCLAIM_000007` | `LEGACY_ONLY` | `HIGH` | direct knowledge conflict | 克里斯对墓灯目的地的知情 | 克里斯亲口说已告诉家里、何松明确说其要去墓灯；后段克里斯又询问目的地并对墓灯震惊；`SRCSEG_0023`, `0026` | 选择误导/只知高危任务/文本修订；不得静默解释。 |
| `SRCCLAIM_000008` | `LEGACY_ONLY` | `HIGH` | direct ship-name conflict | 德雷克座舰 | 前段 `冬墓号` vs 后段 `灰鲨号`；`SRCSEG_0010`–`0013`, `0028` | 选择同舰改名、两艘不同舰或保留其中一艘。 |
| `SRCCLAIM_000009` | `LEGACY_ONLY` | `LOW` | chronology staging note | 起航顺序 | 晨星先启动推进阵列、德雷克先带拾荒人离泊、拾荒人提前进入外环；`SRCSEG_0026`–`0028` | 启动、离泊、外环与跃迁可自然分阶段；只有时间写死时才需决定。 |
| `SRCCLAIM_000010` | `LEGACY_ONLY` | `LOW` | structure conflict | 原稿篇章编号 | 第十一/十七/十八篇重号，后段出现“第五章/第六章”；全稿标题 | 生产 ID 使用 `CH_*`；原题仅作显示标题和溯源。 |
| `SRCCLAIM_000011` | `LEGACY_ONLY` | `MEDIUM` | currency model open | 货币 | `信用币` 与 `星币` 语汇并存；`SRCSEG_0001`–`0013` | 决定是否为同一货币、不同计价层或残稿混用；旧稿没有充分汇率模型。 |
| `SRCCLAIM_000012` | `LEGACY_ONLY` | `HIGH` | appointment gap | 何筠指挥权 | 合同为有限临时战术权限，后段称其将指挥舰队/已是舰队长；`SRCSEG_0010`, `0020`–`0031` | 保存职权升级证据，同时补正式任命/指挥链或改写称谓。 |
| `SRCCLAIM_000013` | `LEGACY_ONLY` | `HIGH` | fleet composition ambiguity | 舰队后勤舰与主管 | 旧稿称有两艘专门后勤船；前段安德鲁/静海号，后段雷蒙德/铁砧号，职责措辞重叠；`SRCSEG_0010`–`0019`, `0028` | 默认分开保留，明确第二艘后勤舰、舰级与编队级职责。 |
| `SRCCLAIM_000014` | `LEGACY_ONLY` | `LOW` | doctrinal classification | 晨星中央舰舰种 | 正式称纳法尔级战列舰，又被描述为“披着战列舰装甲的航空母舰”；`SRCSEG_0027`–`0029` | 可保留正式舰种与战术俗称；能力范围仍需约束。 |
| `SRCCLAIM_000030` | `LEGACY_ONLY` | `HIGH` | batch terminology conflict | 克隆批次口径 | 第一批量产型号、第一批克隆飞行员与第三批商业化型号并存；`SRCSEG_0001`–`0002` | 明确“代/批次/用途/商业化批”是否为不同维度；不得任选一个数字。 |
| `SRCCLAIM_000031` | `LEGACY_ONLY` | `HIGH` | organization affiliation conflict | 遗迹事务部隶属 | 多处为科隆诺科技深空遗迹事务部/核心部门，诺瓦尔第七观测站又标联邦遗迹事务部；`SRCSEG_0001`–`0024` | 决定公司部门、联邦机构、承包关系、双重挂牌或残稿混用。 |
| `SRCCLAIM_000032` | `LEGACY_ONLY` | `HIGH` | object identity drift | 回声井对象 | 早期黑色立方被直接称为回声井；后段区分巨大环形界面、舰载黑色终端与封锁地本体；`SRCSEG_0001`, `0024` | 至少分开 `SRCENT_0069`、量子阵列界面、`SRCENT_0059` 与开放本体；解释本体时升级为 `BLOCKER`。 |
| `SRCCLAIM_000033` | `LEGACY_ONLY` | `HIGH` | chronology/organization clarification | 科隆诺进入墓灯年代 | 前身二百一十四年前已开启遗迹，十五年前又称第一次正式进入墓灯深层；`SRCSEG_0003`, `0013` | 可能是前身/现法人、接入遗迹/正式深层远航之别；采用前明确。 |
| `SRCCLAIM_000034` | `LEGACY_ONLY` | `MEDIUM` | organization naming/tree open | 联邦军事机构层级 | 联邦海军、边界/边境舰队、第七巡航群、第三巡逻群并存；`SRCSEG_0003`, `0030` | 建立组织树与规范称谓；不得把所有名称扁平合并。 |

## Open canon and incomplete continuity

| ID | Severity if invoked | Topic | Open evidence | Required boundary |
|---|---|---|---|---|
| `SRCCLAIM_000015` | `BLOCKER` | 何筠最终身份 | 原体死亡、K-47、连续性/重复/缺失提示 | 只有作者可决定 L0；普通写作只能呈现已授权认知和现象。 |
| `SRCCLAIM_000016` | `BLOCKER` | 回声井本体、起源与主体 | 遗迹、自然现象假说、系统回应、外接终端 | 保持 `OPEN_CANON`；终端、界面、模型和本体分离。 |
| `SRCCLAIM_000017` | `BLOCKER` | 灰烬号事故真因 | 无残骸、擦除样效应、梦境回忆与机构推断 | 不得让 Agent 解谜或认证因果。 |
| `SRCCLAIM_000018` | `BLOCKER` | 大崩溃真因 | 旧稿主要说明后果，未给 L0 原因 | 不得与秘密本体自动绑定。 |
| `SRCCLAIM_000019` | `HIGH` | 雅典娜的主体性/连续性 | 人格化反应、称伊卡洛斯为身体、欢迎“回舰” | AI 是否有自我、记忆来源和连续性由作者决定。 |
| `SRCCLAIM_000020` | `HIGH` | 梦境陈述的可靠性 | 两次接触提供强线索 | 作为角色经历保留；不得改写为全知旁白。 |
| `SRCCLAIM_000021` | `MEDIUM` | 26 小时日与交通 | 诺瓦尔日长、地表—轨道—跨星系转换散见旧稿 | 正式场景使用前建立统一时间/交通规则。 |
| `SRCCLAIM_000022` | `MEDIUM` | 伊甸环物理形态 | 名称像环，正文又称主居住星 | 地理卡需明确星球、环世界、轨道居住带或别称。 |
| `SRCCLAIM_000023` | `MEDIUM` | 克里斯职级和舰位 | 工程能力、教培和加入已写，正式岗位不完整 | 进入舰上场景前明确汇报线、所在舰和权限。 |
| `SRCCLAIM_000024` | `MEDIUM` | 谢庭加入物流 | 阿格赛斯末端直接加入 | 续写前明确搭乘舰、时间、许可和工作对象。 |
| `SRCCLAIM_000025` | `MEDIUM` | 苏恩/红雀号后段职责 | 前段明确舰长，后段扫描平台指向不清 | 不自动绑定或拆分，沿用时确认。 |
| `SRCCLAIM_000026` | `MEDIUM` | 舰队完整编制 | 多舰多角色分批出现，缺统一编制表 | 涉及战术/后勤时先建立当时编制。 |
| `SRCCLAIM_000027` | `MEDIUM` | 伊卡洛斯能力边界 | 高同步、相位护盾、主炮、实验舰描述 | 补射程/成本/冷却须作者批准，不得万能化。 |
| `SRCCLAIM_000028` | `LOW` | 旧日志来源 | 无来源童年记录出现 | 只能作为谜团/物件，不补制造者与用途。 |
| `SRCCLAIM_000029` | `LOW` | 感情关系状态 | 何筠与克里斯蒂娜存在共鸣、玩笑与接近 | 默认未确认恋爱或承诺，除非作者明确。 |
| `SRCCLAIM_000035` | `HIGH` | 何筠疑似同型 AI 舰接触史 | 雅典娜推断何筠过去接触过同类型 AI 舰船，但舰载数据库无何筠相关经历 | 推断对象是何筠的过去，不是雅典娜来源；不得补完接触时间、舰船或原因。 |

## Trigger rule

- 新设定仅与本表冲突时，报告 `LEGACY_SOURCE_DIVERGENCE / LEGACY_ONLY`，随后按作者明确决定执行。
- 冲突涉及已批准 Canon、Memory 或 Manuscript 时，升级为 `SETTING_CONFLICT` 并按实际影响分级。
- `BLOCKER` 只在本章实际触碰对应谜底且作者意图不清时生效；未触碰的开放谜题不阻塞生产。
