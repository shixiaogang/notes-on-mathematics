# 项目说明

这是从机器学习笔记独立出的中文 LaTeX 数学笔记。十卷重组计划位于 `plans/ten-volume-migration/README.md`，完整包含卷章分工与内容，正在分批实施：当前正文为卷一至卷三（10部分、44章），入口登记于 `tex/volumes.json`；卷四至卷十暂不编写、不构建。迁移前的五卷正文、索引词条与旧提要保存在 `tex_bak/`，只作后续迁移的来源，不参与构建，普通开发不修改。

开始修改前阅读 [开发要求](specs/development.md)，检查 Git 状态和已有工作区。首次迁移按用户要求在本仓库根目录初始化；后续任务使用独立 worktree 和分支，构建与提交串行处理，不覆盖其他任务成果。

- [LaTeX 与数学记号](specs/latex.md)：入口、宏、符号、引用与构建。
- [写作](specs/writings.md)：中文论述与技术含义；各章保留独立的“本章小结”。
- [大纲](specs/outlines.md)：`outlines/current/` 记录实际正文；outlines/ 只保存当前正文提要，未来目标结构与内容放在 plans/。只调整计划时不改正文。
- [工作计划](specs/plans.md)：`plans/` 当前仅有 `ten-volume-migration/` 这一项计划（进行中），完整保存已确定的十卷内容结构、逐部分细纲与实施步骤。
- [图像](specs/figures.md)与[样式](specs/design.md)：资源复现、字体、黄色主题与语义环境。

正文修改须同步相应大纲。沿用稳定语义标签；数学卷之间的引用从源文件生成，指向尚未迁入的计划卷时使用 `tex/planned-references.json` 登记的位置，机器学习延伸阅读使用外部链接，不依赖源仓库的文件或构建缓存。正文结构迁移前先确认所用目标大纲版本。

交付前运行 `./build.sh build`、`./build.sh check-target`、`python3 scripts/check_outline.py` 及与修改相关的检查；首次构建或共享样式变化时执行 `./build.sh all`。PDF 与构建清单随对应源文件维护。卷一至卷三按十卷计划分卷出版，其余各卷随后续迁移加入出版登记。不得用源仓库旧成品替代本仓库构建。

字体、图源、数据及许可证保留相对路径。原机器学习仓库仅作为迁移来源；本仓库的普通开发不修改源仓库。
