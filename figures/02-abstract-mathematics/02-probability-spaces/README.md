# 卷二第7部分“概率空间”图像

本目录保存第5—8章独用的图像。Matplotlib图由解析式、精确概率计算或固定种子的模拟生成；每幅图目录下的`figure.json`记录公式、参数、随机种子、样本量、尺寸与字体校验值。

## 重放

Matplotlib每章一个生成器，从项目根目录运行（依赖Matplotlib、NumPy；部分图另用SciPy），可在命令后列出图名只重画指定图：

```sh
python3 figures/02-abstract-mathematics/02-probability-spaces/matplotlib/generate_ch1.py
```

字体、色板和导出方式来自`figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py`。Matplotlib的数学字体Fira Math不含黑板粗体E，相关坐标标签改用中文或图注中定义的记号。

TikZ图以`tikz/<图名>/figure.tex`为图源，用共享工具导出PDF、SVG与PNG，`figure.render.json`记录源文件校验值与物理尺寸：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/02-abstract-mathematics/02-probability-spaces/tikz/<图名>/figure.tex
```

## 图目

| 章 | 生成器 | Matplotlib | TikZ |
| --- | --- | --- | --- |
| 第3章 一般概率模型与随机对象 | `generate_ch1.py` | `pmod-almost-sure-limit`、`pmod-alternating-paths`、`pmod-jensen-support`、`pmod-markov-bounds`、`pmod-mixed-expectation`、`pmod-moment-tails`、`pmod-pushforward-exponential`、`pmod-reflection-uniform` | `pmod-bernoulli-couplings`、`pmod-dice-information`、`pmod-generated-partitions`、`pmod-preimage`、`pmod-product-rectangle`、`pmod-xor-partitions` |
| 第4章 条件期望与条件分布 | `generate_ch2.py` | `cond-bayes-posterior`、`cond-cdf-rationals`、`cond-four-points`、`cond-information-layers`、`cond-jensen`、`cond-kernel-types`、`cond-mixture-two-stage`、`cond-mse-decomposition`、`cond-regression-scatter` | `cond-finite-kernel`、`cond-independence-tables`、`cond-joint-from-kernel`、`cond-kernel-composition`、`cond-tower-layers` |
| 第5章 随机变量的收敛与积分极限 | `generate_ch3.py` | `conv-borel-cantelli`、`conv-chebyshev-nonsummable`、`conv-dyadic-sweep`、`conv-kolmogorov-maximal`、`conv-kronecker`、`conv-random-harmonic`、`conv-slln-paths`、`conv-spike`、`conv-subsequence`、`conv-truncation`、`conv-ui-tails` | `conv-implications`、`conv-limsup-liminf`、`conv-slln-roadmap` |
| 第6章 分布弱收敛、紧性与极限定理 | `generate_ch4.py` | `wlim-characteristic-functions`、`wlim-closed-set-portmanteau`、`wlim-clt-convergence`、`wlim-clt-vector`、`wlim-escape-tight`、`wlim-halfline-sandwich`、`wlim-helly-selection`、`wlim-inversion-atom`、`wlim-levy-counterexample`、`wlim-lindeberg-triangular`、`wlim-point-mass-cdf`、`wlim-spike-mean`、`wlim-studentized-shift` | `wlim-joint-pairings` |
