# 数学图像资源

本目录保留迁移数学正文所用的图像、可编辑图源、数据、生成脚本及来源记录。当前正文为集合与一元微积分、向量矩阵与多元微积分、图、函数空间与流形这四卷，实际引用位置以 `tex/volumes.json` 和 `00-shared/academic-drawing/integration-manifest.json` 为准。`01-basic-mathematics/`、`02-abstract-mathematics/`、`03-optimization-evolution-and-signals/` 及共享目录保留迁移前的图组路径，目录旧名不表示现行卷次。按十卷计划新制的图放在与 `tex/` 同名的卷目录下，例如卷二初等行变换图例位于 `02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/tikz/ls-elementary-row-operations/`，由同目录的 `generate.py` 生成图源，再用 `academic-drawing/render_tikz.py` 导出。

`00-shared/mathematical-preliminaries-upper/`、`mathematical-preliminaries-lower/` 保留原数学图组，`mathematical-generators/` 保存共享数学生成器，`academic-drawing/` 保存字体、色板与接入记录，`resource_paths.py` 解析资源清单。历史记录中的旧卷名只表示生成时的归属，现行使用位置以数学正文入口为准。

书籍主题采用暖黄色；图中的数学语义配色保留原样，见[图像规范](../specs/figures.md)。所有路径以仓库根目录为基准，字体使用随仓库分发的文件。
