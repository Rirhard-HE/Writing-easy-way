---
document_type: production_contract
status: active
mode: author_led_agent_expansion
created: 2026-08-11
---

# Production Contract

## 角色分工

### 作者负责

- 每章核心内容与剧情所有权；
- 关键事件、角色选择、谜底与情感落点；
- 新增/修改设定及 Retcon；
- 最终正文与长期状态批准。

### Agent 负责

- 从权威状态和相关原稿证据构建最小上下文；
- 把作者输入整理成可执行边界合同；
- 在 `flexible` 范围内补充连接、细节、节奏和表达；
- 检查人物、时间线、世界规则、知识边界、伏笔与揭示门；
- 对明显设定冲突给出影响提醒；
- 提取待批准的章节 Delta。

## 生产正文准入条件

生成生产级章节正文前必须满足：

1. 作者核心材料非空，且 brief 标记为 `status: ready / author_input_complete: true`；
2. `must_happen` 与 `must_not_happen` 可执行且不互斥；
3. POV 或视角处理方式明确；
4. `BLOCKER` 和重大 `HIGH` 已由作者决定；
5. 边界合同没有把 Agent 提案伪装成作者事实；
6. 秘密揭示门已检查；
7. 正文扩写范围已由作者允许。
8. 已生成阶段记录的来源 SHA-256 与当前来源一致；作者输入变化后必须重新生成或标记 `stale`。

## 默认扩写原则

- 优先保留作者的事件顺序、人物意图、关键表达与情绪方向。
- 优先补“可见、可听、可执行”的场景内容，不用抽象解释替代戏剧行动。
- 不确定时收缩扩写范围并标记问题，不用新设定填洞。
- 作者文本与 Agent 新增内容在审批前都留在 workbench；最终批准后才进入 manuscript。

## 完成定义

一章只有在正文、最终审查、Memory/Setting Delta 和人工批准全部完成后，才算生产完成。提交与推送仍需独立授权。
