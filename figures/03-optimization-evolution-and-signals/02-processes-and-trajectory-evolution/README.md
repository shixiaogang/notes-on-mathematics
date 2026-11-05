# 卷三第10部分“过程与轨迹演化”图像

本目录保存第7—12章独用的图像，于2026-10-31随六章重写新增。图名前缀对应章：`dds-`（第7章 离散动力系统）、`ode-`（第8章 常微分方程）、`pde-`（第9章 偏微分方程）、`spp-`（第10章 随机过程与样本路径）、`dtsp-`（第11章 离散时间随机过程）、`ctsp-`（第12章 连续时间随机过程）。各章的图目、用途小节与重放命令见同目录 `README-ch1.md` 至 `README-ch6.md`。

| 章 | Matplotlib | TikZ | 生成器 |
| --- | ---: | ---: | --- |
| 第7章 | 16 | 3 | `matplotlib/generate_ch1.py` |
| 第8章 | 18 | 1 | `matplotlib/generate_ch2.py` |
| 第9章 | 20 | 1 | `matplotlib/generate_ch3.py` |
| 第10章 | 15 | 2 | `matplotlib/generate_ch4.py` |
| 第11章 | 0 | 24 | `tikz/generate_ch5.py` |
| 第12章 | 0 | 22 | `tikz/generate_ch6.py` |

Matplotlib 生成器复用 `figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py` 的字体与低饱和色板，需要 NumPy 与 Matplotlib。第11、12章的数据图因制作时环境缺少 NumPy，改由纯标准库脚本以固定种子或解析式计算数据，输出可编辑的 pgfplots 源，再由 `figures/00-shared/academic-drawing/render_tikz.py` 以书籍图字体渲染；这与 `specs/figures.md` “数据图用 Matplotlib”的选型约定不一致，属于待迁移项。各图目录保存源文件、`figure.json` 或文件头参数记录、PDF 与 PNG 预览。

正文另沿用 `figures/00-shared/mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/` 中的少量旧图（状态充分性、Hamilton与梯度流、Rao--Blackwell切片、温度三层模型），路径未变。
