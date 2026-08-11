---
document_type: genesis_source_event_ledger
status: PASS_2_COMPLETE
canonical: false
evidence_class: LEGACY_SOURCE
reader_state_effect: NONE
context_policy: LEGACY_ONLY_ON_EXPLICIT_AUTHOR_BRIEF
source_sha256: 227f21fe7082fe528cbd9afcc470206565c399d6f76943b7b16d8ce695487643
created: 2026-08-11
---

# Source Event Ledger — Pass 2

`SRCEVT` 只表示“旧稿中存在这个事件证据”，不表示新生产线已经采用。除明确标为 `SOURCE_IMPLIED` 的行外，事件均为 `SOURCE_EXPLICIT`；这只说明文本明确出现，不认证叙述者、人物、数据库或机构档案的可靠性。没有绝对日期的事件不得擅自换算成年表。

## Historical anchors in the legacy source

| Source event ID | Relative time in source | Event evidence | Source evidence | Truth/reliability status | Knowledge layer | Source type | Source | Production constraint |
|---|---|---|---|---|---|---|---|---|
| `SRCEVT_000001` | 约三百年前 | 大崩溃使旧联邦秩序瓦解，现代文明依赖遗迹技术恢复。 | `SOURCE_EXPLICIT` | `TEXT_CONFIRMED` | `L2_MODERN_FEDERATION_MODEL` | character/institutional history | `SRCSEG_0003`, `SRCSEG_0018` | 后果可作旧稿历史证据；起因、精确年代和权力重组仍为 `OPEN_CANON`。 |
| `SRCEVT_000002` | 二百一十四年前 | 旧联邦相关遗迹中的回声井装置被开启/接入。 | `SOURCE_EXPLICIT` | `TEXT_CONFIRMED` | `L2_MODERN_FEDERATION_MODEL` | institutional history | `SRCSEG_0003`, `SRCSEG_0024` | 与“三年前发现技术”口径需澄清；本体、建造者和实际功能不确认。 |
| `SRCEVT_000003` | 三十七年前 | 赫尔墨斯要塞港遭袭，档案记载 503,271 人死亡。 | `SOURCE_EXPLICIT` | `TEXT_CONFIRMED` | `L2_MODERN_FEDERATION_MODEL` | official record | `SRCSEG_0030` | 精确伤亡数字属于联邦档案层，不自动作为旁白绝对事实。 |
| `SRCEVT_000004` | 二十三年前 | 雷恩·维尔斯经历长弓回廊事故并形成高风险导航履历。 | `SOURCE_EXPLICIT` | `TEXT_CONFIRMED` | `L2_MODERN_FEDERATION_MODEL` | database record | `SRCSEG_0029` | 事故完整过程、责任和记录可靠性未确认。 |
| `SRCEVT_000005` | 十五年前 | 林塞之父参加墓灯深层任务后失联。 | `SOURCE_EXPLICIT` | `TEXT_CONFIRMED` | `L4_CHARACTER_KNOWLEDGE` | character testimony | `SRCSEG_0013` | 不得自动判定死亡、补名或补完任务真相。 |
| `SRCEVT_000006` | 灰烬号事故前，未定 | 何筠曾拒绝对赫拉-3 殖民穹顶执行轨道轰炸命令，并离开军队体系。 | `SOURCE_EXPLICIT` | `TEXT_CONFIRMED` | `L4_CHARACTER_KNOWLEDGE` | memory/account | `SRCSEG_0003` | 处分程序、命令真相与绝对时间未完整给出。 |
| `SRCEVT_000007` | 灰烬号事故前，未定 | 何筠经营/指挥灰烬号并与克里斯等人维持诺瓦尔关系。 | `SOURCE_IMPLIED` | `IMPLIED` | `L4_CHARACTER_KNOWLEDGE` | narrative implication | `SRCSEG_0001`–`0007` | 购舰时间、船员表和各人是否同航未确认。 |

## Legacy narrative sequence

下表按旧稿叙述主顺序排列，不把插叙误当作绝对时间线。

| Source event ID | Sequence | Event evidence | Source | Time certainty | Production constraint |
|---|---:|---|---|---|---|
| `SRCEVT_000008` | 001 | 灰烬号在 D-91 碎裂带附近失联；黑脊犬第十九掠袭群异常毁灭，其中两艘护卫舰呈擦除样失踪。 | `SRCSEG_0001`–`0003` | `RELATIVE_HIGH` | 其余舰船仍有熔化/撕裂残骸；两件事的因果关系、真正先后和机制均开放。 |
| `SRCEVT_000009` | 002 | K-47 克隆体何筠在赫卡忒七号醒来，被告知原体死亡、回传完成度与债务。 | `SRCSEG_0001` | `SEQUENCE_HIGH` | “何筠是否同一人”须分法律、角色自认与 L0；不得由 Agent 裁定。 |
| `SRCEVT_000010` | 003 | 科隆诺对何筠进行异常记忆/事故问询，并提出墓灯调查任务。 | `SRCSEG_0002`–`0003` | `SEQUENCE_HIGH` | 擦除解释为机构模型；92.7% 是系统测量，不是完整人格真值。 |
| `SRCEVT_000011` | 004 | 何筠恢复大部分记忆，异常封闭区仍存在，并获准回诺瓦尔。 | `SRCSEG_0003` | `SEQUENCE_HIGH` | 记忆恢复比例与可靠性不得混同。 |
| `SRCEVT_000012` | 005 | 何筠在失踪七个月后回家，与父母团聚并隐瞒克隆状态。 | `SRCSEG_0004` | `SEQUENCE_HIGH` | 父母姓名冲突；年轻身体的可见差异没有充分处理。 |
| `SRCEVT_000013` | 006 | 家宴中何筠说明将参加遗迹任务，但淡化其风险。 | `SRCSEG_0005` | `SEQUENCE_HIGH` | 对话是角色选择，不是客观任务说明。 |
| `SRCEVT_000014` | 007 | 克里斯到访，谈及轨道维护工作、旧星门兴趣和墓灯传闻。 | `SRCSEG_0006` | `SEQUENCE_HIGH` | 墓灯死亡率为地方传闻；能力与正式岗位需桥接。 |
| `SRCEVT_000015` | 008 | 何筠与克里斯在旧港重建信任，仍未公开克隆真相。 | `SRCSEG_0007` | `SEQUENCE_HIGH` | 黑市航道消息与官方记录需按来源分层。 |
| `SRCEVT_000016` | 009 | 何筠第一次梦见回声井、人物光流及井底呼唤。 | `SRCSEG_0008` | `SEQUENCE_HIGH` | 梦的来源、真实性与主体保持 `OPEN_CANON`。 |
| `SRCEVT_000017` | 010 | 何筠梦醒后异常清醒，获父母支持并离开诺瓦尔。 | `SRCSEG_0009` | `SEQUENCE_HIGH` | 26 小时日与交通耗时不能自行填入正式时间线。 |
| `SRCEVT_000018` | 011 | 何筠签署正式合同，债务被冻结，取得外勤和有限战术权限。 | `SRCSEG_0010` | `SEQUENCE_HIGH` | 与口头“勾销债务”承诺冲突；权限范围不能扩大。 |
| `SRCEVT_000019` | 012 | 德雷克、安德鲁、克里斯蒂娜加入/组成遗迹任务核心团队。 | `SRCSEG_0011` | `SEQUENCE_HIGH` | 舰名、职务和完整编制待统一。 |
| `SRCEVT_000020` | 013 | 团队交流墓灯异常经验；克里斯蒂娜提出信息与擦除理论。 | `SRCSEG_0011`–`0012` | `SEQUENCE_HIGH` | 角色理论不得写成 L0 旁白事实。 |
| `SRCEVT_000021` | 014 | 林塞披露父亲旧案；何筠获得伊卡洛斯和雅典娜的优先权限。 | `SRCSEG_0013` | `SEQUENCE_HIGH` | 权限阶段、AI 主动授权原因和林塞拼写均待决。 |
| `SRCEVT_000022` | 015 | 何筠与克里斯蒂娜返回诺瓦尔并交流远航、身份与梦想。 | `SRCSEG_0014` | `SEQUENCE_HIGH` | 关系只支持共鸣与趋近，不自动确认恋爱。 |
| `SRCEVT_000023` | 016 | 克里斯揭露轨道射灯构件盗卖，随后受邀加入任务。 | `SRCSEG_0015` | `SEQUENCE_HIGH` | 举报结果、风险处置和正式招募手续开放。 |
| `SRCEVT_000024` | 017 | 何筠第二次梦中接触回声井式系统，得到连续性、重复、缺失、归档等反馈。 | `SRCSEG_0016` | `SEQUENCE_HIGH` | 只能作为梦境/系统陈述；不得提升为作者真相或打开揭示门。 |
| `SRCEVT_000025` | 018 | 无来源童年旧日志出现；雅典娜主动联系；何筠再次告别父母。 | `SRCSEG_0017` | `SEQUENCE_MEDIUM` | 日志来源、童年接触和雅典娜预授权保持开放。 |
| `SRCEVT_000026` | 019 | 何筠与克里斯蒂娜讨论阿斯特拉及企业化联邦政治。 | `SRCSEG_0018` | `SEQUENCE_HIGH` | 地理表述冲突；政治判断属于人物模型。 |
| `SRCEVT_000027` | 020 | 拾荒人开始十四天高强度教培，苏恩和雷蒙德加入，何筠同步异常。 | `SRCSEG_0019` | `SEQUENCE_HIGH` | 教培副作用、同步原因和技能边界不补完。 |
| `SRCEVT_000028` | 021 | 编队在第十天提前完成整备，何筠获启航通知并承担伊卡洛斯责任。 | `SRCSEG_0020` | `SEQUENCE_HIGH` | 责任不等于无限舰队指挥权；“灰烬号重生”为情绪表达。 |
| `SRCEVT_000029` | 022 | 四日离港倒计时中，何筠决定先重走灰烬号航线并凝聚团队。 | `SRCSEG_0021` | `SEQUENCE_HIGH` | 记忆坐标与路线可靠性需保留不确定。 |
| `SRCEVT_000030` | 023 | 何筠正式登上伊卡洛斯，与雅典娜达到 78% 同步。 | `SRCSEG_0022` | `SEQUENCE_HIGH` | 舰船参数为旧稿工程证据；AI 连续性和既往接触开放。 |
| `SRCEVT_000031` | 024 | 何筠与克里斯完成离港前家庭告别，克里斯得到雷蒙德认可。 | `SRCSEG_0023` | `SEQUENCE_HIGH` | 克里斯父母已知目的地的文本与后段惊讶冲突。 |
| `SRCEVT_000032` | 025 | 克里斯蒂娜展示回声井旧研究、观测站资料和外接终端解释。 | `SRCSEG_0024` | `SEQUENCE_HIGH` | 自然现象说是研究假说；终端/界面不等于回声井本体。 |
| `SRCEVT_000033` | 026 | 克里斯蒂娜讲述海岸城童年；团队准备接克里斯参加教培。 | `SRCSEG_0025` | `SEQUENCE_HIGH` | 关系玩笑不构成恋爱 Canon。 |
| `SRCEVT_000034` | 027 | 克里斯接受教培；黑脊犬搜索失事区促使编队提前离港；晨星提供伴航。 | `SRCSEG_0026` | `SEQUENCE_HIGH` | 克里斯目的地知识、离港具体调度和黑脊犬兵力层级冲突/开放。 |
| `SRCEVT_000035` | 028 | 雷恩·维尔斯率晨星舰队抵达，双方建立有限伴航关系。 | `SRCSEG_0027` | `SEQUENCE_HIGH` | 晨星秘密任务、中央舰舰种和“血腥玛丽”情报边界开放。 |
| `SRCEVT_000036` | 029 | 拾荒人与晨星离开赫卡忒七号前往阿格赛斯，生还模型为 12%。 | `SRCSEG_0028` | `SEQUENCE_HIGH` | 舰队起航顺序可分阶段解释，但未经作者决定不得静默修正。 |
| `SRCEVT_000037` | 030 | 联合跃迁与导航经验交换后，雅典娜将生还模型调整为 17%。 | `SRCSEG_0029` | `SEQUENCE_MEDIUM` | 第二/第三天叙述含回插；正式时间线需重排而非照搬段落顺序。 |
| `SRCEVT_000038` | 031 | 联合舰队抵达阿格赛斯，接受遗迹装置检查并讨论白矛/灰烬走廊路线。 | `SRCSEG_0030` | `SEQUENCE_HIGH` | 路线风险数据与赫尔墨斯历史仍是机构/档案证据。 |
| `SRCEVT_000039` | 032 | 何筠公开灰烬号失事坐标；雷恩同意护送；谢庭被安排加入后续行动。 | `SRCSEG_0031` | `SEQUENCE_HIGH` | 旧稿在此停止；路线、出发时刻、登舰物流与事故真相均未完成。 |

## Chronology rule

- `SRCEVT_000001`–`000007` 是历史/背景锚点，不与正文事件自动换算绝对日期。
- `SRCEVT_000008`–`000039` 是旧稿叙事序列，不是正式生产章节编号。
- 正式事件只有在作者采用后才获得 `EVT_*` ID；提升时必须记录来源 `SRCEVT`、作者决定和任何改写。
- 原稿冲突只触发 `LEGACY_SOURCE_DIVERGENCE` 或相关提醒，不阻止作者建立新的事件顺序。
