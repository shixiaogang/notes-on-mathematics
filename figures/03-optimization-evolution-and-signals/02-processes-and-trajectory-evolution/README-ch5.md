# 第五章“离散时间随机过程”图像（前缀 `dtsp-`）

本章所在 worktree 没有 numpy/matplotlib，数据图由 `tikz/generate_ch5.py`（仅用 Python 标准库，固定种子 `20261105+k`，精确公式与递推）写成可编辑的 pgfplots 源 `tikz/dtsp-*/figure.tex` 及事实记录 `figure.json`，再用 `figures/00-shared/academic-drawing/render_tikz.py` 以书籍字体渲染为 PDF/SVG/PNG。三幅概念图为手写 TikZ。

重放：

```sh
python3 figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/tikz/generate_ch5.py            # 生成并渲染全部数据图
python3 figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/tikz/generate_ch5.py tv-decay   # 单幅
python3 figures/00-shared/academic-drawing/render_tikz.py figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/tikz/dtsp-two-state-graph/figure.tex  # 手写图
```
（`python3` 须能导入 `pymupdf`，本机为 `/opt/homebrew/bin/python3.15`。）

| 图 | 方式 | 用途（节） | 内容 |
|---|---|---|---|
| dtsp-ar1-path-bundle | 生成 | 5.1.1 | AR(1) 路径束与精确边缘分布 |
| dtsp-two-state-graph | 手写TikZ | 5.1.2 | 两状态链转移图 |
| dtsp-two-state-distribution | 生成 | 5.1.2, 5.2.1 | 两状态链多步分布；交替链振荡与时间平均 |
| dtsp-communicating-classes | 手写TikZ | 5.2.1 | 沟通类、封闭类与周期 |
| dtsp-balance-cycles | 手写TikZ | 5.2.3 | 细致平衡与定向循环 |
| dtsp-martingale-transform | 生成 | 5.3.2 | 可预测下注与事后挑选 |
| dtsp-doob-decomposition | 生成 | 5.3.2 | $S_n^2$ 的 Doob 分解 |
| dtsp-gamblers-ruin | 生成 | 5.4.2 | 停止路径与到达概率（精确+模拟） |
| dtsp-doubling-strategy | 生成 | 5.4.2 | 加倍下注与截断期望分解（精确） |
| dtsp-doob-maximal | 生成 | 5.5.1 | 首次越界与 Doob 界 |
| dtsp-azuma-freedman | 生成 | 5.5.1 | 稀疏下注精确尾概率与 Azuma/Freedman 界 |
| dtsp-upcrossings | 生成 | 5.5.2 | 上穿与 Pólya 坛子收敛 |
| dtsp-tv-decay | 生成 | 5.6.2 | 总变差衰减（两状态链、惰性/非惰性环） |
| dtsp-ergodic-average | 生成 | 5.6.3 | 时间平均与自相关 |
| dtsp-inverse-rejection | 生成 | 5.7.1 | 逆变换与拒绝采样 |
| dtsp-monte-carlo-rate | 生成 | 5.7.1 | Monte Carlo 误差 $n^{-1/2}$ 与误差分布 |
| dtsp-importance-variance | 生成 | 5.7.2 | 提议尾部与权重方差爆炸 |
| dtsp-variance-reduction | 生成 | 5.7.3 | 各方差缩减方法的精确方差 |
| dtsp-mh-gibbs | 生成 | 5.7.4 | 随机游走 MH 与 Gibbs 轨迹、自相关（跨栏 146mm） |
| dtsp-hmc-leapfrog | 生成 | 5.7.5 | 蛙跳相轨迹与能量误差 |
| dtsp-path-weight-degeneracy | 生成 | 5.7.6 | 路径权重退化 |
| dtsp-robbins-monro | 生成 | 5.8.2 | 步长与均方误差 |
| dtsp-mean-ode-tracking | 生成 | 5.8.3 | 迭代与平均 ODE |
| dtsp-fast-slow-averaging | 生成 | 5.8.4 | 快慢更新与 Polyak 平均 |

5.7.3 另引用既有图 `figures/00-shared/mathematical-preliminaries-lower/01-random-variables-distributions-and-causality/matplotlib/probability-rao-blackwell-slice/figure.pdf`（未改动）。正文引用宽度与图自然宽度一致（约 86–104mm，跨栏 140/146mm），图内字号 8pt/7.5pt。
