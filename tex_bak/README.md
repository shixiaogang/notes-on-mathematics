# 迁移前的五卷正文备份

本目录保存按十卷计划迁移之前的五卷正文（`01-basic-mathematics` 至 `05-control-decision-and-games`）、各卷双语索引词条（`index-terms/`）、旧出版登记（`volumes.json`）与旧正文提要（`outlines/current/`）。

- 卷一至卷三已按[十卷重组计划](../plans/ten-volume-migration/README.md)从这里迁入 `tex/`，迁入后的正文与大纲以 `tex/` 和 `outlines/current/` 为准。
- 尚未迁入的内容（原卷一“概率与统计基础”、原“图上的谱方法”，以及原卷二至卷五）仍在这里，作为卷四至卷十后续迁移的来源。
- 本目录不参与构建，文件中的 `\input` 路径保留迁移前的写法；普通开发不修改这里的文件。迁移某一卷时，从这里复制材料并按计划重组，不直接恢复旧结构。
