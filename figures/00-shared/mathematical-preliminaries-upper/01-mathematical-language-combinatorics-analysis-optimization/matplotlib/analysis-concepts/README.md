# 数学语言与分析概念图

这组图回应第一章“最小值与下确界”及第三章度量、收敛、连续和导数的读者困难。全部曲线、端点与标注值来自显式解析式，是教学构造，不是观测或实验结果。

| 文件前缀 | 读图任务 | 最终宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `language-minimum-infimum` | 同一下确界是否由定义域中的点达到 | 112 mm | `figure` |
| `analysis-metric-convergence` | 同一数列在不同度量下的距离，以及通常到离散的恒等映射 | 169 mm | `figure*` |
| `analysis-continuity-counterexamples` | 连续的邻域控制、跳跃不连续、连续但不可导 | 169 mm | `figure*` |
| `analysis-derivative-orders` | 统一函数与基点上的一阶/二阶近似及带符号余项 | 169 mm | `figure*` |

每图包含真实矢量 PDF、真实矢量 SVG 和 300 DPI PNG；SVG 字形转为矢量路径，标签和图元可以在绘图源中编辑。`plots.py` 使用仓库内霞鹜文楷和 Source Sans 3 字体，数学字体使用 Matplotlib STIX。`sources.json` 保存解析式、定义域、参数、取样网格和计算结果。当前图注、环境和引用以调用这些图像的正文源文件为准。

在有 NumPy、Matplotlib 的 Python 环境中运行：

```bash
python figures/00-shared/mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/matplotlib/analysis-concepts/plots.py
```

代码不依赖执行机器的绝对路径，不调用 LaTeX，不进行随机采样。输出尺寸固定；前三幅分析比较图须以 169 mm 宽度插入，以保持 8–9 pt 标签大小。

单独更新导数图可运行 `python figures/00-shared/mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/matplotlib/analysis-concepts/plots.py --only analysis-derivative-orders`，保留另外三幅图文件。

端点图以空心点明确排除开区间端点，线段展示其图像闭包。阶跃函数的两段分别绘制，不跨断点连线。通常与离散度量的方向标明为 `id:(R,d_u)->(R,d_d)`；反方向的连续性不能照搬该图的结论。导数图在共同基点 `x0=1/2` 下使用 `h=x-x0`，右图绘制带符号余项，不能把其负值误读为负的误差大小。

导数教学例的精确值：

- `f(x)=x^3-3x`，`f(x0)=-11/8`，`f'(x0)=-9/4`，`f''(x0)=3`。
- 近似的自变量统一为带符号步长：`T1(h)=f(x0)+f'(x0)h`，`T2(h)=T1(h)+f''(x0)h^2/2`；一阶余项为 `3h^2/2+h^3`，二阶余项为 `h^3`。
- `h=-0.1` 时，真值、一阶近似、二阶近似分别为 `-1.136`、`-1.150`、`-1.135`，余项为 `0.014`、`-0.001`。
- `h=0.1` 时，真值、一阶近似、二阶近似分别为 `-1.584`、`-1.600`、`-1.585`，余项为 `0.016`、`0.001`。

独立图的 PNG 和 PDF 原生渲染均进行视觉检查；整页嵌入效果没有编译检查，遵照本轮不运行 LaTeX 的要求。
