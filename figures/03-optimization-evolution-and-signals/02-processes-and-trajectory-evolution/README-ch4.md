# 第四章“随机过程与样本路径”图源

正文：`tex/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/04-stochastic-processes-and-sample-paths/`。图名前缀 `spp-`。

## Matplotlib（生成器 `matplotlib/generate_ch4.py`，固定种子 `20261030+k`）

| 图 | 用途（节） | 内容 |
| --- | --- | --- |
| `spp-two-views` | 4.1.1 | 高斯随机游走路径束与两时刻竖切片直方图 |
| `spp-taxonomy` | 4.1.1 | 离散/连续时间 × 状态/路径类型四例 |
| `spp-same-marginals` | 4.1.2 | 相同 N(0,1) 边缘的独立、AR(1)、共享背景序列及相关随间隔 |
| `spp-cylinder` | 4.1.2 | 三道“闸门”的柱集 |
| `spp-stopping-vs-peak` | 4.2.2 | 首次命中阈值（停时）与全程最高点（非停时） |
| `spp-spike` | 4.3.3 | 随机位置尖点 $1\{t=U\}$ 的五次实现 |
| `spp-increment-moments` | 4.3.3 | Brownian 与 Poisson 增量矩随间隔的标度 |
| `spp-gp-kernels` | 4.4.1 | 四种协方差核热图与样本路径（跨栏） |
| `spp-kl-expansion` | 4.4.1 | Brownian 运动正弦基展开的部分和 |
| `spp-rkhs-vs-path` | 4.4.2 | 二进平方增量和；截断展开的 $H_{\min}$ 范数平方 |
| `spp-beta-binomial` | 4.5.1 | Bin(10,1/2) 与 Beta(2,2) 混合的成功次数分布 |
| `spp-polya-frequencies` | 4.5.2 | 独立 Bernoulli 与 Pólya 罐的累计频率及极限直方图（跨栏） |
| `spp-random-measure-partition` | 4.6.1 | 随机离散测度一次实现与分割质量 |
| `spp-stick-breaking` | 4.6.2 | 折棒构造与期望权重 |
| `spp-dp-samples` | 4.6.2 | DP(α, N(0,1)) 随机分布函数，α=1,10,100（跨栏） |

每图目录含 `figure.pdf`、`figure.png`、`figure.json`（参数、种子、关键数值与字体记录）。

重放（需 numpy、scipy、matplotlib）：

```sh
python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch4.py            # 全部
python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch4.py spp-spike  # 单图
```

## TikZ

| 图 | 用途（节） | 内容 |
| --- | --- | --- |
| `tikz/spp-filtration-layers/figure.tex` | 4.2.1 | 三次抛硬币的自然滤过分块与 $S_n$ 取值 |
| `tikz/spp-polya-tree/figure.tex` | 4.3.1 | Pólya 罐三步逐步核构造树 |

重放：`python3 figures/00-shared/academic-drawing/render_tikz.py <figure.tex>`（需 PyMuPDF）。
