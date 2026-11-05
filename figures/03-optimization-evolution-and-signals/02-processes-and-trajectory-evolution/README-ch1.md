# 第十部分第一章“离散动力系统”图像

本说明登记第7章（离散动力系统）独用的图像。Matplotlib图由正文给出的映射、参数与初值逐步迭代得到；高精度参考轨道用Python标准库`decimal`（120位）计算，带随机残差或噪声的图使用固定种子`20261030`。每幅图目录下的`figure.json`记录公式、参数、关键数值、尺寸与字体校验值。

## 重放

从项目根目录运行（依赖NumPy、Matplotlib；可在命令后列出图名只重画指定图）：

```sh
python3 figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch1.py [图名 ...]
```

字体、色板与导出来自`figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py`。Matplotlib数学文本不能混排中文，图内中文标签与数学标签分开书写。

TikZ图以`tikz/<图名>/figure.tex`为图源：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/tikz/<图名>/figure.tex
```

## 图目

| 图名 | 方法 | 用途（正文位置） |
| --- | --- | --- |
| `dds-temperature-trajectory` | Matplotlib | 温度递推轨迹与偏差几何衰减（7.1.1） |
| `dds-state-augmentation` | TikZ | 二阶递推的状态扩充（7.1.1） |
| `dds-noninvertible-merge` | TikZ | 不可逆更新使过去汇合（7.1.2） |
| `dds-history-moments` | Matplotlib | 指数加权矩状态读出局部直线（7.1.3） |
| `dds-matrix-power-shapes` | Matplotlib | 单位圆在矩阵幂下的形变：实特征值、复特征值、Jordan块（7.2.1） |
| `dds-input-injection` | Matplotlib | 输入的注入时刻与剩余传播（7.2.1） |
| `dds-parallel-scan` | TikZ | 仿射更新的关联扫描（7.2.2） |
| `dds-period-two-graph` | Matplotlib | Logistic映射的$F$与$F^2$（7.3.1） |
| `dds-cobweb` | Matplotlib | 收敛、周期二与离开的蛛网图（7.3.1） |
| `dds-transient-growth` | Matplotlib | 非正规矩阵的瞬态放大（7.3.2） |
| `dds-lyapunov-ellipses` | Matplotlib | 二次Lyapunov函数水平椭圆与欧氏长度对比（7.3.3） |
| `dds-basin-estimate` | Matplotlib | 子水平集认证区域与数值吸引域（7.3.3） |
| `dds-newton-basins` | Matplotlib | 牛顿法求$z^3=1$的吸引域（7.4.1） |
| `dds-bifurcation-branches` | Matplotlib | 鞍结与倍周期分岔的解析分支（7.4.2） |
| `dds-logistic-bifurcation` | Matplotlib | Logistic分岔图与有限时间Lyapunov指数（7.4.2、7.4.3） |
| `dds-sensitive-separation` | Matplotlib | $r=4$近邻轨道的指数分离（7.4.3） |
| `dds-rounding-divergence` | Matplotlib | 单、双精度轨道相对高精度参考的偏离（7.4.3） |
| `dds-error-bound` | Matplotlib | 离散Grönwall上界与实际误差（7.5.1） |
| `dds-forced-response` | Matplotlib | 持续输入偏差与衰减扰动（7.5.2） |

7.1.1另引用既有共享图`figures/00-shared/mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/matplotlib/reader-state-sufficiency/`（路径未变）。
