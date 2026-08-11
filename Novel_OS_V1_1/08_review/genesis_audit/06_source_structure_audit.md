# Source Structure Audit — 灰烬重生.docx

Status: `PASS_1 / STRUCTURE ONLY / NOT_CANON`

- Non-empty paragraphs detected: 10,160
- Approx. text characters excluding inserted paragraph separators: 119,178
- Chapter-style headings detected by exact pattern: 4
- Part-style headings detected by exact pattern: 26

## Detected chapter headings

- Source paragraph 2: `第一章：重生`
- Source paragraph 6228: `第二章：航道已输入`
- Source paragraph 7851: `第五章：童年`
- Source paragraph 8204: `第六章：克里斯`

## Detected part headings

- Source paragraph 3: `第一篇：从死亡归来`
- Source paragraph 290: `第二篇：蠢货`
- Source paragraph 715: `第三篇：真相`
- Source paragraph 1119: `第四篇：回家`
- Source paragraph 1359: `第五篇：家宴`
- Source paragraph 1687: `第六篇：朋友`
- Source paragraph 2028: `第七篇：旧港`
- Source paragraph 2276: `第八篇：梦`
- Source paragraph 2527: `第九篇：明天见`
- Source paragraph 3094: `第十一篇：团队`
- Source paragraph 3753: `第十二篇：林塞`
- Source paragraph 4116: `第十四篇：梦想`
- Source paragraph 4444: `第十五篇：神探`
- Source paragraph 4830: `第十六篇：第二次接触`
- Source paragraph 5165: `第十七篇：海底两万里`
- Source paragraph 5446: `第十七篇：欢迎登舰，教授`
- Source paragraph 5687: `第十八篇：上班`
- Source paragraph 5972: `第十八篇：太阳照常升起`
- Source paragraph 6229: `第一篇：航线`
- Source paragraph 7194: `第三篇：诺瓦尔`
- Source paragraph 7517: `第四篇：回声井`
- Source paragraph 8533: `第七篇：晨星舰队`
- Source paragraph 8881: `第八篇：启航`
- Source paragraph 9223: `第九篇：舰队协调`
- Source paragraph 9609: `第十篇：要塞`
- Source paragraph 9967: `第十一篇：灰烬号`

## Structural warnings

- The current draft appears to use both `章` and `篇` as nested/working structure, but numbering is not currently clean enough to treat as stable IDs.
- Detected missing numbers and duplicate `篇` labels in the first large block (for example duplicated 第十七篇 / 第十八篇 and skipped numbers).
- Exact `章` heading detection jumps from 第二章 to 第五章 and 第六章; this may be intentional draft assembly, formatting drift, or missing headings.
- **Recommendation:** do not map current display numbering directly to permanent `CH_xxxx` IDs. During migration, assign sequential immutable scene/chapter IDs and retain original headings as `source_heading` metadata.

## Migration recommendation

1. Preserve the DOCX as immutable source evidence.
2. Build a source map from each working section to a stable Novel OS ID.
3. Do not rename/reorder the source until the first event/timeline extraction is complete.
4. After author approval, split manuscript into stable Markdown chapter/scene files.