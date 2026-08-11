---
document_type: genesis_source_entity_registry
status: PASS_2_COMPLETE
canonical: false
evidence_class: LEGACY_SOURCE
reader_state_effect: NONE
context_policy: LEGACY_ONLY_ON_EXPLICIT_AUTHOR_BRIEF
source_sha256: 227f21fe7082fe528cbd9afcc470206565c399d6f76943b7b16d8ce695487643
created: 2026-08-11
---

# Source Entity Registry — Pass 2

`SRCENT` 是证据去重 ID，不是 Canon ID。作者批准某实体进入正式状态时，另行分配 `CHR/LOC/FAC/ITEM/SYS`，并保存对应 `SRCENT` 来源。

## Characters and AI

| Source ID | Name | Evidence | Source segments | Production constraint |
|---|---|---|---|---|
| `SRCENT_0001` | 何筠 / K-47 | `SOURCE_EXPLICIT` | 0001–0031 | 一个叙事身份、多状态/实例；最终 L0 身份 `OPEN_CANON`。 |
| `SRCENT_0002` | 林塞（原稿亦作林赛） | `SOURCE_EXPLICIT + CONFLICT` | 0001–0031 | 主管、遗迹任务接口；规范拼写待作者决定。 |
| `SRCENT_0003` | 克里斯蒂娜 | `SOURCE_EXPLICIT` | 0011–0031 | 遗迹专家；深层论述多为 `TEXT_HYPOTHESIS`，不是旁白真相。 |
| `SRCENT_0004` | 德雷克 | `SOURCE_EXPLICIT` | 0011–0030 | 老舰长；“冬墓号/灰鲨号”关联存在舰名连续性风险。 |
| `SRCENT_0005` | 安德鲁 | `SOURCE_EXPLICIT` | 0011–0021 | 静海号后勤主管兼副舰长；与雷蒙德舰队级后勤职责分开。 |
| `SRCENT_0006` | 苏恩 | `SOURCE_EXPLICIT` | 0019–0029 | 红雀号舰长/高风险驾驶者；后段扫描平台是否即红雀号未明示。 |
| `SRCENT_0007` | 雷蒙德 | `SOURCE_EXPLICIT` | 0019–0029 | 舰队综合后勤主管、铁砧号负责人；与克里斯汇报关系待明示。 |
| `SRCENT_0008` | 克里斯 | `SOURCE_EXPLICIT + CONFLICT` | 0006–0030 | 童年好友、轨道工程师；目的地知识与正式职级存在冲突/空缺。 |
| `SRCENT_0009` | 何松 | `SOURCE_EXPLICIT + CONFLICT` | 0004–0023 | 何筠父亲；“何振川”疑似残留名，不另建实体。 |
| `SRCENT_0010` | 毛晓 | `SOURCE_EXPLICIT + CONFLICT` | 0004–0023 | 何筠母亲；“陈岚”疑似残留名，不另建实体。 |
| `SRCENT_0011` | 雅典娜 | `SOURCE_EXPLICIT / NATURE_OPEN` | 0013–0031 | 二级舰载 AI；人格、自我意识、复制连续性均开放。 |
| `SRCENT_0012` | 雷恩·维尔斯 | `SOURCE_EXPLICIT` | 0027–0031 | 晨星总舰队长；其履历来自数据库/人物声誉层。 |
| `SRCENT_0013` | 谢庭 | `SOURCE_EXPLICIT` | 0031 | 27 岁超空间认知研究员；登舰物流及学科定义缺失。 |
| `SRCENT_0014` | 冯·萨克森 | `SOURCE_EXPLICIT` | 0030 | 联邦边界舰队第三巡逻群中尉。 |
| `SRCENT_0015` | “血腥玛丽” | `SOURCE_EXPLICIT / DETAILS_OPEN` | 0027 | 黑脊犬扩张关键人物；真实身份、舰船、控制范围未定。 |
| `SRCENT_0016` | 林塞之父 | `SOURCE_EXPLICIT` | 0013 | 十五年前墓灯深层任务失联；不得补名或判死。 |
| `SRCENT_0017` | 克里斯蒂娜之父 | `SOURCE_EXPLICIT` | 0021 | 《海底两万里》旧主人；职业和结局未完整确认。 |
| `SRCENT_0018` | EIDOLON-2 | `SOURCE_EXPLICIT` | 0002–0003 | 科隆诺二级异常建模 AI；输出属于 L3 机构模型。 |

## Organizations and social systems

| Source ID | Name | Evidence | Source segments | Production constraint |
|---|---|---|---|---|
| `SRCENT_0019` | 科隆诺科技 | `SOURCE_EXPLICIT` | 0001–0031 | 巨企、克隆与遗迹任务主体；前身与现公司连续性细节开放。 |
| `SRCENT_0020` | 遗迹事务部 | `SOURCE_EXPLICIT + LAYER_AMBIGUITY` | 0002–0031 | 多数语境为科隆诺部门，部分标题似联邦机构；隶属关系需统一。 |
| `SRCENT_0021` | 现代联邦 | `SOURCE_EXPLICIT / SPEAKER_MODEL` | 0003–0031 | 法律/政治框架；“空壳”是人物概括，不是完整宪制。 |
| `SRCENT_0022` | 联邦海军 | `SOURCE_EXPLICIT` | 0003、0030 | 上层军事机构候选；与边界/边境舰队的组织关系开放。 |
| `SRCENT_0023` | 军事巨企联合体 | `SOURCE_EXPLICIT / SPEAKER_MODEL` | 0003、0018 | 权力结构候选；需正式政治模型。 |
| `SRCENT_0024` | 黑脊犬 | `SOURCE_EXPLICIT` | 0002、0026–0030 | 海盗组织；下属集团与主力层级未完全拆分。 |
| `SRCENT_0025` | 黑脊犬第十九掠袭群 | `SOURCE_EXPLICIT` | 0002 | 灰烬号事故附近覆灭舰队；与后续搜索集团关系开放。 |
| `SRCENT_0026` | 拾荒人远航编队 | `SOURCE_EXPLICIT` | 0002–0031 | 何筠相关任务编队；正式名称、完整编制与职位表未定。 |
| `SRCENT_0027` | 晨星勘探舰队 | `SOURCE_EXPLICIT` | 0026–0031 | 联邦注册 A 级远航编队；具体任务保密。 |
| `SRCENT_0028` | 诺瓦尔轨道维护局 | `SOURCE_EXPLICIT` | 0006、0015 | 克里斯原单位；“轨道局”等为简称。 |
| `SRCENT_0029` | ORPHEUS EDUCATION | `SOURCE_EXPLICIT / HISTORY_MODEL` | 0003 | 旧时代教培设施企业标识；与回声井技术链的精确关系开放。 |
| `SRCENT_0030` | 联邦边界舰队第三巡逻群 | `SOURCE_EXPLICIT` | 0030 | 六舰边境执法单位。 |
| `SRCENT_0031` | 恒辉轻工联合 | `SOURCE_EXPLICIT` | 0004–0005 | 毛晓旧单位；地方工业企业。 |
| `SRCENT_0070` | 联邦边界/边境舰队 | `SOURCE_EXPLICIT + NAMING_OPEN` | 0003、0030 | “边界/边境”用词、与联邦海军的上下级关系待统一。 |
| `SRCENT_0071` | 联邦边境舰队第七巡航群 | `SOURCE_EXPLICIT` | 0003 | 何筠旧部队/任务背景；与第三巡逻群不是同一单位。 |

## Locations, systems and routes

| Source ID | Name | Evidence | Source segments | Production constraint |
|---|---|---|---|---|
| `SRCENT_0032` | 赫卡忒七号空间站 | `SOURCE_EXPLICIT` | 0001–0028 | 克隆、遗迹事务部、军用星港与舰队集结中心。 |
| `SRCENT_0033` | 诺瓦尔 / K-12 殖民世界 | `SOURCE_EXPLICIT` | 0004–0026 | 改造殖民世界；行政层级、生态硬参数待正式卡。 |
| `SRCENT_0034` | 格林港及外围旧城区 | `SOURCE_EXPLICIT` | 0004–0023 | 何筠家乡；格林港与外围小城边界未命名。 |
| `SRCENT_0035` | 墓灯星区 | `SOURCE_EXPLICIT + MODEL_OPEN` | 0002–0031 | 超新星遗骸/危险航区；异常机制不得升格 L0。 |
| `SRCENT_0036` | D-91 碎裂带 | `SOURCE_EXPLICIT` | 0002 | 灰烬号最后定位区域。 |
| `SRCENT_0037` | 赫拉-3 殖民穹顶 | `SOURCE_EXPLICIT` | 0003 | 何筠拒绝轨道轰炸命令的地点。 |
| `SRCENT_0038` | 阿斯特拉星系 | `SOURCE_EXPLICIT + CONFLICT` | 0018 | 仙女座探索区首府/旧联邦首府表述冲突。 |
| `SRCENT_0039` | 伊甸环 | `SOURCE_EXPLICIT / FORM_OPEN` | 0018 | 阿斯特拉主居住星；名称与物理形态需澄清。 |
| `SRCENT_0040` | 王冠 | `SOURCE_EXPLICIT` | 0018 | 气态巨行星，赤道轨道有大型居住带。 |
| `SRCENT_0041` | 17 号海岸城 | `SOURCE_EXPLICIT` | 0024–0025 | 克里斯蒂娜成长地与研究站城市。 |
| `SRCENT_0042` | 诺瓦尔第七观测站 | `SOURCE_EXPLICIT` | 0024 | 回声井旧研究资料所在地，不是本体所在地。 |
| `SRCENT_0043` | 阿格赛斯要塞港 | `SOURCE_EXPLICIT` | 0028–0031 | 墓灯前联邦边界军港/登记补给点。 |
| `SRCENT_0044` | 赫尔墨斯要塞港 | `SOURCE_EXPLICIT / OFFICIAL_RECORD` | 0030 | 三十七年前袭击地点。 |
| `SRCENT_0045` | 长弓回廊 | `SOURCE_EXPLICIT / DATABASE_RECORD` | 0029 | 雷恩二十三年前导航事故区域。 |
| `SRCENT_0046` | 白矛航道 | `SOURCE_EXPLICIT` | 0030 | 较稳定、绕远的路线候选。 |
| `SRCENT_0047` | 灰烬走廊 | `SOURCE_EXPLICIT` | 0030 | 较短、高失联风险路线；与灰烬号无命名因果证据。 |
| `SRCENT_0048` | 永久封锁遗迹星球 | `SOURCE_EXPLICIT / LOCATION_SECRET` | 0024 | 回声井本体关联地；坐标和本体保持受限。 |

## Ships and key items

| Source ID | Name | Evidence | Source segments | Production constraint |
|---|---|---|---|---|
| `SRCENT_0049` | 灰烬号 | `SOURCE_EXPLICIT / FINAL_CAUSE_OPEN` | 0001–0031 | 矿骡级驱逐舰；事故因果与信息状态开放。 |
| `SRCENT_0050` | 伊卡洛斯 | `SOURCE_EXPLICIT` | 0013–0031 | 214 米实验护卫舰、雅典娜舰体；武器/护盾缺实战边界。 |
| `SRCENT_0051` | 冬墓号 | `SOURCE_EXPLICIT` | 0010–0013 | 德雷克的旧舰名候选；与后文灰鲨号可能冲突。 |
| `SRCENT_0052` | 灰鲨号 | `SOURCE_EXPLICIT + CONFLICT` | 0028 | 德雷克老巡洋舰；是否改名/另舰待决定。 |
| `SRCENT_0053` | 静海号 | `SOURCE_EXPLICIT` | 0010–0013 | 综合后勤巡洋舰，安德鲁相关。 |
| `SRCENT_0054` | 铁砧号 | `SOURCE_EXPLICIT` | 0028 | 雷蒙德后勤舰；不与静海号自动合并。 |
| `SRCENT_0055` | 红雀号 | `SOURCE_EXPLICIT` | 0019–0028 | 苏恩驱逐舰；后段扫描平台绑定未明示。 |
| `SRCENT_0056` | 远星号 | `SOURCE_EXPLICIT` | 0010、0020 | 勘探巡洋舰/移动研究平台。 |
| `SRCENT_0057` | 晨星中央纳法尔级舰 | `SOURCE_EXPLICIT / CLASS_DISPUTED` | 0027–0029 | 近四公里；战列舰/航空母舰化战列舰分类有争议。 |
| `SRCENT_0058` | 《海底两万里》纸质书 | `SOURCE_EXPLICIT` | 0017–0023 | 克里斯蒂娜父亲留下/持有过的旧书；父亲当前状态未定。 |
| `SRCENT_0059` | 回声井舰载黑色终端 | `SOURCE_EXPLICIT / FUNCTION_MODEL` | 0024 | 外接人格/意识记录终端；不与早期黑色对象、量子阵列界面或回声井本体合并。 |
| `SRCENT_0069` | 早期“回声井”黑色立方对象 | `SOURCE_EXPLICIT / OBJECT_IDENTITY_OPEN` | 0001 | 林塞直接称其为回声井，但它是投影、接口、终端还是本体表征未定。 |

## Technologies, phenomena and models

| Source ID | Name | Evidence | Entity information class | Production constraint |
|---|---|---|---|---|
| `SRCENT_0060` | 回声井 | `SOURCE_EXPLICIT_ENTITY / NATURE_OPEN` | `UNRESOLVED` | 本体、起源、主体性、归档含义均开放；秘密规则只见 secret ontology。 |
| `SRCENT_0061` | 克隆复活与意识回传流程 | `SOURCE_EXPLICIT_MODERN_MODEL` | `UNRESOLVED` | 人格/记忆回传这一具体 claim 可标 `IDENTITY_INFORMATION`；法律连续性、工程成功和 L0 身份必须分开。 |
| `SRCENT_0062` | 教培仪 | `SOURCE_EXPLICIT` | `UNRESOLVED` | 神经写入/记忆内容 claim 可标 `IDENTITY_INFORMATION`；装置本身不按信息类别归类。 |
| `SRCENT_0063` | 擦除样异常 | `SOURCE_EXPLICIT_EFFECT / MECHANISM_SECRET` | `UNRESOLVED` | 普通文本只可写现象；L0 机制不得进入上下文。 |
| `SRCENT_0064` | 稳定航道、超空间锚与漂移 | `SOURCE_EXPLICIT_MODERN_MODEL` | `UNRESOLVED` | 测量/导航记录 claim 可标 `SIGNAL_INFORMATION`；航行工程模型不等于 L0 空间真相。 |
| `SRCENT_0065` | 联合跃迁泡 | `SOURCE_EXPLICIT_TECH / THEORY_MODEL` | `UNRESOLVED` | 教学数据 claim 可标 `SIGNAL_INFORMATION`；曲率说明属于 L2/L3 模型。 |
| `SRCENT_0066` | 伊卡洛斯相位护盾与“长矛”主炮 | `SOURCE_EXPLICIT_ENGINEERING` | `UNRESOLVED` | 性能记录 claim 可标 `SIGNAL_INFORMATION`；缺射程、冷却、弹药/能量、实战验证，不得无限化。 |
| `SRCENT_0067` | 超空间认知理论 | `SOURCE_EXPLICIT_FIELD / DEFINITION_OPEN` | `UNRESOLVED` | 不得自动等同于 L0 信息本体；精神风险为机构观察。 |
| `SRCENT_0068` | 回声井量子阵列操控界面 | `SOURCE_EXPLICIT_INTERFACE` | `UNRESOLVED` | 人格/意识记录 claim 可标 `IDENTITY_INFORMATION`；人造界面与本体必须分开。 |

## Promotion rule

源实体进入正式卡前必须明确：作者是否沿用该实体、规范名/别名、稳定事实、当前状态、知识层、揭示门和来源。存在 `CONFLICT` 的条目不能静默择一。
