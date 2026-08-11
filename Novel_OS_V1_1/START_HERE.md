# 从这里开始

当前工程已经创建好 `CH_0001` 的完整工作区。

## 你现在只需要做一件事

打开：

`07_workbench/CH_0001/00_author_brief.md`

把第一章剧情按以下四部分写进去：

1. `本章核心剧情`
2. `must_happen`
3. `must_not_happen`
4. `flexible`

其中最重要的是前三项。其他字段暂时不完整也可以。

## 写完后，在 Codex 里输入

```text
准备 CH_0001。使用 prepare-chapter skill。
读取我的 author brief，构建 context pack，提出情节补充，并调用相关只读 subagents 并行检查人物、时间线、世界规则、剧情因果和伏笔冲突。
不要生成正文，不要修改 Canon。
```

完成后你主要检查两个文件：

- `02_expansion.agent.md`：Agent 对你的剧情做了哪些补充
- `03_conflict_report.agent.md`：是否存在冲突/风险/可利用的旧伏笔

然后把你的决定写入：

`04_author_decision.md`

之后再让 Codex 生成正文。
