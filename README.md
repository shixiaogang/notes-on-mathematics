# 数学笔记

从[机器学习笔记](https://github.com/shixiaogang/notes-on-machine-learning)中独立整理的中文 LaTeX 数学笔记，采用 `tufte-book` 版式与暖黄色主题。

十卷重组计划正在分批实施：卷一至卷三已按新大纲迁入正文，共10个部分、44章；卷四至卷十暂未编写和构建。迁移前的五卷正文与旧正文提要保存在 [tex_bak/](tex_bak/README.md)，仅作迁移来源。源机器学习仓库的内容继续保留。

- **[大纲总入口](outlines/README.md)**：查看与现行正文一致的结构和内容提要。
- **[十卷重组计划](plans/ten-volume-migration/README.md)**：完整保留已确定的10卷、31个部分、152章的分工与内容，并附逐部分细纲与实施安排；这是当前唯一进行中的计划。
- **[当前正文大纲](outlines/current/README.md)**：与已迁入的卷一至卷三正文对应。
- **[工作计划索引](plans/README.md)**：登记十卷重组这一项待执行计划及其状态。

## 构建与阅读

需要 TeX Live（XeLaTeX、`latexmk`、Biber、texindy）、Python 3、PyMuPDF 和 Bash。字体与 Tufte 模板随仓库提供，见[字体说明](fonts/README.md)。

```sh
./build.sh all           # 首次构建已登记的全部各卷
./build.sh build         # 此后只更新受影响卷
./build.sh check-target  # 校验 PDF 与当前输入一致
./build.sh volume 01-sets-and-univariate-calculus
python3 scripts/check_outline.py  # 校验十卷计划章纲与本地链接
make test
```

成品位于 `target/`，每卷独立出版。卷名与章节组织按十卷计划，书名、前言和版式已适配为独立数学笔记。少量指向机器学习应用的延伸阅读链接定位原仓库固定版本，构建不依赖原仓库。

| 卷 | 内容 | PDF |
| --- | --- | --- |
| 一 | 集合与一元微积分 | [阅读](target/vol1-sets-and-univariate-calculus.pdf) |
| 二 | 向量、矩阵与多元微积分 | [阅读](target/vol2-vectors-matrices-and-multivariate-calculus.pdf) |
| 三 | 图 | [阅读](target/vol3-graphs.pdf) |

各卷 PDF 使用 Git LFS 保存。克隆后运行 `git lfs install --skip-repo`、`git lfs pull` 获取完整成品，并用 `git config --local core.hooksPath .githooks` 启用提交检查。

## 目录与维护

`tex/` 保存正文、文献、索引与共享样式；`tex_bak/` 保存迁移前的五卷正文、索引词条与旧正文提要，只作迁移来源，不参与构建；`outlines/` 只保存现行正文大纲；`plans/` 当前只保存十卷重组计划，计划目录同时容纳卷章内容方案与实施安排；`figures/`、`fonts/` 保存独立构建与复现所需的资源；`specs/` 保存开发规范。构建缓存 `build/` 不纳入 Git。

每次修改正文都须同步对应大纲；仅整理十卷计划时保留正文结构。后续开发使用独立工作区，见[开发要求](specs/development.md)。

远端仓库：[shixiaogang/notes-on-mathematics](https://github.com/shixiaogang/notes-on-mathematics)。

## 许可

- 书稿正文与原创图表采用 CC BY-NC-ND 4.0。
- LaTeX 样式、构建脚本、测试和代码示例采用 Apache License 2.0，见 [LICENSE](LICENSE)。
- 字体保留各自的上游许可证，见[字体说明](fonts/README.md)。
