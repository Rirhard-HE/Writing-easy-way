# Novel OS V1

一个以“作者提供每章创作核心、Agent 负责边界设定、受约束扩写与连续性审查”为核心的超长篇小说工程。

## 核心原则

- **Author = 剧情与 Canon 的最终权威**
- **Agent = 提案、检索、补充、冲突检查、Delta 提取**
- **Approval before Commit**：未经人工批准，不得把 Agent 新增事实写回长期状态
- **Author may revise settings**：作者可以修改原设定；Agent 负责提示明显冲突与影响，不用旧设定否决作者
- **Markdown/YAML = Source of Truth**
- **09_index = Derived Data**，可随时重建

## 目录

```text
00_system/      系统规则、风格与工作流
01_canon/       世界最高权威事实
02_characters/  人物 Canon / State / Knowledge / Relationships
03_world/       地点、势力、系统、物品等
04_story/       大纲、Arc、Thread、伏笔、未解决问题
05_manuscript/  最终正文
06_memory/      已批准的章节卡、事件、状态变化
07_workbench/   每章事务工作区
08_review/      审核与冲突历史
09_index/       可重建索引
archive/        旧版本/废弃设定的辅助归档（Git仍是主版本历史）
```

## 第一次使用

1. 用 Git 初始化本目录。
2. 在 `00_system/project_rules.md` 和 `00_system/style_guide.md` 填写你的基础规则。
3. 将角色与世界资料按稳定 ID 放入对应目录。
4. 创建新章：

```bash
python scripts/new_chapter.py CH_0001
```

5. 编辑：

```text
07_workbench/CH_0001/00_author_brief.md
```

这里不仅写剧情摘要，也写作者自己的场景材料、关键对话/行动，以及本章是否新增或修改设定。
完成后把 front matter 中的 `status` 改为 `ready`，并把 `author_input_complete` 改为 `true`。

6. 在 Codex 中给出：

```text
准备 CH_0001。读取作者材料，生成 context pack、边界合同、扩写建议，并用并行连续性审查完成冲突报告。不要写正文，不要改 Canon。
```

7. 你完成 `04_author_decision.md` 后：

```text
根据 CH_0001 的作者决定生成正文草稿，并执行最终连续性检查。不要写回长期记忆。
```

8. 正文确认后：

```text
为 CH_0001 提取 memory delta。只记录本章发生的变化，不重写整张人物卡；等待我批准。
```

9. 将 `08_approval.yaml` 改成 `approved: true` 后，再执行 finalize。

## 推荐日常命令语言

- `准备 CH_0123`：Context + Expansion + Review
- `生成 CH_0123 正文`：按作者决定写 Draft + Final Review
- `提取 CH_0123 状态变化`：生成 Memory Delta
- `完成 CH_0123`：仅在批准后正式写回
- `设定修改为……`：记录明确作者变更；如与旧设定冲突，先提示影响再按你的明确决定执行

## 当前 V1 的边界

V1 不依赖向量数据库。优先通过稳定 ID、目录关系、YAML 元数据和全文搜索工作。等进入几十万到百万字后，再把 `09_index/` 升级为 SQLite/FTS/语义检索，不改变 Canon 文件格式。

设定变更规则见 `00_system/change_control.md`，作者与 Agent 的生产分工见 `00_system/production_contract.md`。
