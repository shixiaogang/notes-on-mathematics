# 项目说明

这是从机器学习笔记独立出的中文 LaTeX 数学笔记。当前正文为五卷、17部分、63章，入口登记于 `tex/volumes.json`；最新十卷调整方案位于 `outlines/math-ten-volumes/README.md`，尚未实施到正文。

开始修改前阅读 [开发要求](specs/development.md)，检查 Git 状态和已有工作区。首次迁移按用户要求在本仓库根目录初始化；后续任务使用独立 worktree 和分支，构建与提交串行处理，不覆盖其他任务成果。

- [LaTeX 与数学记号](specs/latex.md)：入口、宏、符号、引用与构建。
- [写作](specs/writings.md)：中文论述与技术含义；各章保留独立的“本章小结”。
- [大纲](specs/outlines.md)：`outlines/current/` 记录实际正文，`outlines/math-ten-volumes/` 记录当前调整方案；其余保留大纲也归入 `outlines/`。只调整大纲时不改正文。
- [工作计划与配套材料](specs/plans.md)：`plans/` 保存待办工作、实施步骤、进度与验收依据，以及按任务归档的未出版材料；链接相应大纲。
- [图像](specs/figures.md)与[样式](specs/design.md)：资源复现、字体、黄色主题与语义环境。

正文修改须同步相应大纲。沿用稳定语义标签；数学卷之间的引用从源文件生成，机器学习延伸阅读使用外部链接，不依赖源仓库的文件或构建缓存。正文结构迁移前先确认所用目标大纲版本。

交付前运行 `./build.sh build`、`./build.sh check-target`、`python3 scripts/check_outline.py` 及与修改相关的检查；首次构建或共享样式变化时执行 `./build.sh all`。PDF 与构建清单随对应源文件维护。首次迁移保留五卷正文，首卷超过1000页的现状如实记录于迁移说明；页数拆分随十卷正文迁移处理。不得用源仓库旧成品替代本仓库构建。

字体、图源、数据及许可证保留相对路径。原机器学习仓库仅作为迁移来源；本仓库的普通开发不修改源仓库。
