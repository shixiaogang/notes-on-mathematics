# 概率与离散数学教学图

这组图片用正文中的解析式和有限构造解释概念，没有实验观测、随机采样、拟造误差条或外部图像。`plots.py` 生成每幅图的真实矢量 PDF/SVG 与 300 DPI PNG；`sources.json` 保存公式、条件、参数、正文来源和实际绘制的数据点。每次生成会同时更新全部格式和数据记录。

运行需要 Python、NumPy 与 Matplotlib：

```sh
python plots.py
```

字体相对于仓库根目录读取：中文为 `fonts/LXGWWenKai-Regular.ttf`，拉丁字符备用字体为 `fonts/SourceSans3-Regular.otf`，数学为 Matplotlib STIX。图宽为 112 mm 或 169 mm，单系列黄、双系列蓝红、三系列蓝红黄，并配合线型区分。

| 正文 | 图文件前缀 | 说明 |
| --- | --- | --- |
| 概率论 | `probability-density-cdf` | 密度面积与分布函数增量 |
| 概率论 | `probability-importance-weights` | 换测度的概率质量和逐项期望贡献 |
| 随机过程 | `stochastic-mixing-variance` | 非周期/周期分布演化与平稳均值方差 |
| 随机过程 | `stochastic-design-ellipsoids` | 统一半径下的设计几何，非等覆盖概率区间 |
| 数理统计 | `statistics-mean-prediction-width` | 已知方差时的均值区间与未来读数区间 |
| 数理统计 | `statistics-huber-loss` | 损失与残差得分，非整个估计量的污染界 |
| 信息论 | `information-gaussian-distances` | 同方差高斯族的 KL、总变差、W₂ 各自尺度 |
| 信息论 | `information-fisher-local` | Bernoulli KL 与局部 Fisher 二阶近似 |
| 因果推断 | `causal-confounding-coverage` | 混杂算例与另一独立构造的覆盖识别范围 |
| 组合数学 | `combinatorics-growth-patterns` | 任意标记与区间类的精确计数 |
| 组合数学 | `combinatorics-coverage-marginals` | 对嵌套背景添加同一候选的边际递减 |
| 图论 | `graph-diffusion-spectrum` | 贯穿图的信号扩散与频率保留系数 |

图像检查直接查看 PNG。按本轮要求，没有运行 LaTeX 或整书编译，也没有据此确认图在书页上的最终浮动位置。
