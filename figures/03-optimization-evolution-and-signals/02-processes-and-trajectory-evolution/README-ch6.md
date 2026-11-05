# 第十二章“连续时间随机过程”图像（前缀 `ctsp-`）

本章全部数据图由 `tikz/generate_ch6.py` 生成。当前环境未安装 numpy/Matplotlib，因此生成器只用 Python 标准库（`random.Random`，固定种子 `20261030+k`）计算数据，并写成可编辑的 pgfplots/TikZ 源 `tikz/ctsp-*/figure.tex`；每个源文件开头注释记录模型、参数、种子与参考曲线公式。随后调用 `figures/00-shared/academic-drawing/render_tikz.py` 用书籍字体渲染 PDF/SVG/PNG。

重放命令（项目根目录）：

```sh
python3 figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/tikz/generate_ch6.py            # 全部
python3 figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/tikz/generate_ch6.py ula-mala   # 单幅
python3 .../generate_ch6.py --no-render                                                                                      # 只重写源文件
```

| 图名 | 内容 | 正文位置 |
| --- | --- | --- |
| `ctsp-poisson-three-views` | 指数等待时间、到达时刻、计数阶梯三联图 | 6.1.1 |
| `ctsp-compound-poisson` | 复合Poisson路径与均值线 | 6.1.1 |
| `ctsp-brownian-zoom` | Brownian路径逐级放大的自相似 | 6.1.2 |
| `ctsp-quadratic-variation` | 平方增量和趋于$t$、绝对增量和发散 | 6.1.2 |
| `ctsp-path-versions` | 随机单点尖峰：修改而可区分 | 6.1.3 |
| `ctsp-ctmc-path` | 三状态链速率图、生成矩阵与停留—跳跃路径 | 6.2.2 |
| `ctsp-birth-death` | 出生死亡链与几何平衡分布 | 6.2.2 |
| `ctsp-compensated-poisson` | 计数与补偿计数的路径束 | 6.3.1 |
| `ctsp-ito-stratonovich-sums` | 左端点、中点、右端点黎曼和 | 6.4.4 |
| `ctsp-gbm-mean-median` | 几何Brownian运动的均值与中位数 | 6.5.3 |
| `ctsp-ou-envelope` | OU路径束与矩包络 | 6.5.3 |
| `ctsp-fokker-planck-snapshots` | OU密度时间截面（解析） | 6.6.2 |
| `ctsp-exit-problem` | 区间退出路径与边值问题解的模拟核对 | 6.6.3 |
| `ctsp-multiplicative-stability` | 乘性噪声：几乎必然稳定、均方不稳定 | 6.7.1 |
| `ctsp-em-orders` | Euler--Maruyama强/弱误差阶 | 6.8.3 |
| `ctsp-jump-event-grid` | 事件驱动与固定网格的跳跃模拟 | 6.8.2 |
| `ctsp-occupation-embedded` | 占据比例$2/3$与嵌入跳链比例$1/2$ | 6.9.1 |
| `ctsp-langevin-double-well` | 双峰势上的Langevin路径与直方图 | 6.9.2 |
| `ctsp-ula-mala` | ULA步长偏差与MALA接受率 | 6.9.3 |
| `ctsp-sa-paths` | 连续随机逼近$\theta_t=(\theta_0+Y_t)/(1+t)$路径束 | 6.10.3 |
| `ctsp-donsker` | Donsker缩放折线 | 6.11.3 |
| `ctsp-path-space-examples` | Skorokhod时间对齐与窄尖峰反例 | 6.11.1 |

正文引用宽度：单栏图 95–105mm，跨栏图（`figure*`）`\linewidth`。图内主字 8pt、刻度与图例 7.5pt（少数密集图例 7pt）。
