# 第8章 常微分方程：图像资源

正文：`tex/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/02-ordinary-differential-equations/`。
Matplotlib 图由 `matplotlib/generate_ch2.py` 生成（复用 `figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py` 的字体与色板），每图目录含 `figure.pdf`、`figure.png`、`figure.json`（解析式、参数与关键数值）。无随机数；非线性参考解用 `scipy.integrate.solve_ivp`（DOP853，rtol=atol=1e-11）。

重放（需要 numpy、scipy、matplotlib）：

```sh
python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch2.py            # 全部
python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch2.py ode-stiff  # 单图
python3 figures/00-shared/academic-drawing/render_tikz.py figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/tikz/ode-flow-composition/figure.tex
```

| 图名 | 方法 | 用途（小节） | 内容 |
| --- | --- | --- | --- |
| ode-slope-field | Matplotlib | 8.1.1 | 温度模型斜率场与解；阻尼摆向量场与轨迹 |
| ode-picard | Matplotlib | 8.2.1 | Picard 盒与锥（$\dot x=1+x^2$）；$\dot x=x$ 的 Picard 迭代 |
| ode-nonunique | Matplotlib | 8.2.1 | $\dot x=\sqrt{|x|}$ 的等待解族 |
| ode-blowup | Matplotlib | 8.2.2 | $\dot x=x^2$ 爆炸与翻倍时间 |
| ode-trajectory-tube | Matplotlib | 8.2.3 | 摆的初值小圆轨迹束与 Grönwall 上界 |
| ode-flow-composition | TikZ | 8.2.4 | 演化映射复合关系示意 |
| ode-flow-deformation | Matplotlib | 8.2.4、8.6.1 | 圆盘在摆与阻尼摆流下的像及面积 |
| ode-phase-portraits | Matplotlib | 8.3.2 | 二维线性系统六种相图 |
| ode-zoh-euler | Matplotlib | 8.3.2 | 开关加热下零阶保持离散与 Euler 对比（h=2） |
| ode-transient-growth | Matplotlib | 8.4.1 | 非正规矩阵的瞬态放大 |
| ode-lyapunov-levels | Matplotlib | 8.4.1、8.4.2 | 二次 Lyapunov 椭圆；阻尼摆能量与零导数集 |
| ode-limit-cycle-bifurcation | Matplotlib | 8.4.2 | van der Pol 极限环；叉形分岔 |
| ode-input-response | Matplotlib | 8.4.3 | 周期加热下的响应与输入响应界 |
| ode-convergence-orders | Matplotlib | 8.5.1 | Euler/RK2/RK4 误差—步长与误差—调用次数 |
| ode-stiff | Matplotlib | 8.5.2 | 刚性方程：显式 Euler 失稳与后向 Euler、梯形法 |
| ode-stability-regions | Matplotlib | 8.5.2 | 绝对稳定域 |
| ode-error-fan | Matplotlib | 8.5.3 | 局部误差传播的误差扇 |
| ode-adaptive-step | Matplotlib | 8.5.3 | Heun–Euler 嵌入对的自适应步长 |
| ode-symplectic-energy | Matplotlib | 8.6.2 | 谐振子相轨迹与单摆能量误差 |

另复用既有图 `figures/00-shared/mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/matplotlib/reader-hamilton-gradient-flow/`（8.6.1），路径未改。
