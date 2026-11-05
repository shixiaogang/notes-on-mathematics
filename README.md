# 数学笔记

从[机器学习笔记](https://github.com/shixiaogang/notes-on-machine-learning)中独立整理的中文 LaTeX 数学笔记，采用 `tufte-book` 版式与暖黄色主题。

本轮迁移保留现行五卷正文，共17个部分、63章；已确定的十卷重组方案作为待执行计划完整保存，尚未据此重组正文。源机器学习仓库的内容继续保留。

- **[大纲总入口](outlines/README.md)**：查看现行正文提要、保留的五卷来源大纲和待迁移材料提要。
- **[十卷重组计划](plans/ten-volume-migration/README.md)**：完整保留已确定的10卷、29个部分、133章的分工与内容，并附逐部分细纲、配套材料及实施安排；这是当前唯一待执行计划。
- **[当前正文大纲](outlines/current/README.md)**：与现行五卷正文对应。
- **[保留的五卷目标纲](outlines/mathematical-foundations/README.md)**：早期结构讨论材料，后续调整以最新十卷方案为准。
- **[工作计划索引](plans/README.md)**：登记十卷重组这一项待执行计划及其状态。
- **[迁移说明](migration/README.md)**：来源版本、复制范围、必要适配与校验结果。

## 构建与阅读

需要 TeX Live（XeLaTeX、`latexmk`、Biber、texindy）、Python 3、PyMuPDF 和 Bash。字体与 Tufte 模板随仓库提供，见[字体说明](fonts/README.md)。

```sh
./build.sh all           # 首次构建全部五卷
./build.sh build         # 此后只更新受影响卷
./build.sh check-target  # 校验 PDF 与当前输入一致
./build.sh volume 01-basic-mathematics
python3 scripts/check_outline.py  # 校验十卷计划章纲与本地链接
make test
```

成品位于 `target/`，每卷独立出版。正文沿用迁移时的卷名与章节组织，书名、前言和版式已适配为独立数学笔记。少量指向机器学习应用的延伸阅读链接定位原仓库固定版本，构建不依赖原仓库。

| 卷 | 内容 | PDF |
| --- | --- | --- |
| 一 | 基础数学 | [阅读](target/vol1-basic-mathematics.pdf) |
| 二 | 抽象数学 | [阅读](target/vol2-abstract-mathematics.pdf) |
| 三 | 优化、动力系统与信号处理 | [阅读](target/vol3-optimization-evolution-and-signals.pdf) |
| 四 | 流形、概率分布与统计推断 | [阅读](target/vol4-manifolds-distributions-and-inference.pdf) |
| 五 | 控制、决策与博弈 | [阅读](target/vol5-control-decision-and-games.pdf) |

各卷 PDF 使用 Git LFS 保存。克隆后运行 `git lfs install --skip-repo`、`git lfs pull` 获取完整成品，并用 `git config --local core.hooksPath .githooks` 启用提交检查。

## 目录与维护

`tex/` 保存正文、文献、索引与共享样式；`outlines/` 保存现行正文大纲、保留的五卷来源大纲及待迁移材料提要；`plans/` 当前只保存十卷重组计划，计划目录同时容纳卷章内容方案、实施安排和配套材料；`figures/`、`fonts/` 保存独立构建与复现所需的资源；`specs/` 保存开发规范。构建缓存 `build/` 不纳入 Git。

每次修改正文都须同步对应大纲；仅整理十卷计划时保留正文结构。后续开发使用独立工作区，见[开发要求](specs/development.md)。

远端仓库：[shixiaogang/notes-on-mathematics](https://github.com/shixiaogang/notes-on-mathematics)。

## 许可

- 书稿正文与原创图表采用 CC BY-NC-ND 4.0。
- LaTeX 样式、构建脚本、测试和代码示例采用 Apache License 2.0，见 [LICENSE](LICENSE)。
- 字体保留各自的上游许可证，见[字体说明](fonts/README.md)。
