# 卷一第2部分“实数与一元函数”图像

本目录保存第4—7章独用的图像。所有曲线均由图源中写明的解析式或确定性双精度计算生成，不含抽样数据。

## Matplotlib

生成器：`matplotlib/generate.py`，从项目任意目录运行

```sh
python3 figures/01-basic-mathematics/02-real-numbers-and-univariate-functions/matplotlib/generate.py [图名 ...]
```

不带参数时依次生成全部图。字体、色板和导出方式来自 `figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py`；每幅图目录下的 `figure.json` 记录解析式、参数、尺寸与字体校验值。

| 图名 | 正文位置 | 内容 |
| --- | --- | --- |
| `function-properties` | 第4.4节 | 单调（严格递增与单调不减）、奇偶（偶函数与奇函数的对称）与周期（标出周期$T$）三面板 |
| `power-sequence-nonuniform` | 第5.5.1节 | $x^n$在$[0,1]$上逐点而非一致收敛 |
| `geometric-partial-sums` | 第5.6.1节 | 几何级数部分和的逼近误差随输入变化 |
| `convex-chord-tangent` | 第6.5.3节 | 凸函数的弦与切线 |
| `finite-difference-error` | 第6.6.4节 | 前向与中心差分的双精度误差及误差模型 |
| `riemann-sums` | 第7.1.1节 | 带符号黎曼和、下和与上和 |
| `narrow-spikes` | 第7.5.1节 | 积分不趋零的逐点收敛窄峰 |
| `quadrature-comparison` | 第7.6.1—7.6.4节 | 同一段上常数、直线与抛物线三种代替函数的近似面积及与被积函数之差 |
| `quadrature-rules` | 第7.6.4节 | 三种求积公式的局部近似与误差阶 |

`matplotlib/analysis-continuity-counterexamples/`（第6.1节）是原微积分部分迁入的既有图组，保留原生成与核验记录。

## TikZ

`tikz/complex-multiplication-roots/figure.tex`（第4.2.2节）与 `tikz/upper-bound-supremum/figure.tex`（第4.1节，集合$\{1-1/n\}$的上界与不属于集合的上确界）以 `figures/00-shared/academic-drawing/render_tikz.py` 导出 PDF、SVG 与 PNG，`figure.render.json` 记录源文件校验值与物理尺寸：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/01-basic-mathematics/02-real-numbers-and-univariate-functions/tikz/complex-multiplication-roots/figure.tex
python3 figures/00-shared/academic-drawing/render_tikz.py figures/01-basic-mathematics/02-real-numbers-and-univariate-functions/tikz/upper-bound-supremum/figure.tex
```

第5—7章另沿用卷内 `00-shared/` 中的既有过程图（误差带、级数部分和、有限覆盖、中值定理等），未复制到本目录。
