# 卷三第1部分“优化”图像

本目录保存第1—9章（优化问题与解、线性规划、光滑优化、非光滑与复合优化、约束优化与对偶、随机与分块优化、多目标极小极大与双层优化、函数拟合与正则化、泛函优化）独用的138幅图，于2026-10-31随九章重写新增。图名前缀`c1`—`c9`对应本部分第1—9章。图中数值均来自正文算例的解析式、精确迭代或固定种子（20261030）的计算，参数记录在各图的`figure.json`中。

## 重放

Matplotlib图每章一个生成器（第2、3章没有Matplotlib图），从项目根目录运行，可在命令后列出图名只重画指定图；依赖NumPy、Matplotlib，第5、9章另用SciPy：

```sh
python3 figures/03-optimization-evolution-and-signals/01-optimization/matplotlib/generate_c1.py
```

字体、色板和导出方式来自`figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py`。Fira Math缺少`\star`、`\top`等字形，部分图内改写为`x^*`、`^{\mathrm T}`，以图注说明为准。

TikZ图以`tikz/<图名>/figure.tex`为图源，用共享工具导出PDF、SVG与PNG，`figure.render.json`记录源文件校验值与物理尺寸：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/03-optimization-evolution-and-signals/01-optimization/tikz/<图名>/figure.tex
```

第3章的15幅曲线与等值线图采用TikZ/pgfplots绘制：`tikz/generate_c3.py`以纯Python按解析式或精确迭代采样，写出各`c3-*/figure.tex`与`figure.json`，再用上述工具渲染。

## 第1章 

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
| --- | --- | --- | --- | --- |
| c1-resource-region | Matplotlib（generate_c1.py） | 01-formulation.tex，`fig:opt-prob-resource-region` | 80 × 66 | 资源分配可行四边形（顶点$(0,0),(3,0),(2,2),(0,4)$）与利润等值线$3x_1+2x_2=4,8,10$，$c=10$只交于$(2,2)$。 |
| c1-failure-modes | Matplotlib（generate_c1.py） | 01-formulation.tex，`fig:opt-prob-failure-modes` | 150 × 46（figure*） | 三种无最优解：$x\leq0$与$x\geq1$不可行；$f(x)=x$无下界；$e^x$下确界$0$未达到。 |
| c1-local-global | Matplotlib（generate_c1.py） | 01-formulation.tex，`fig:opt-prob-local-global` | 100 × 56 | $f=x^4/4-x^3/3-x^2$在$C=[-1.5,1.5]$上：局部最优$x=-1$，边界全局最优$x=1.5$（$f'=-1.875$），$C$外更低点$x=2$。 |
| c1-extended-value | Matplotlib（generate_c1.py） | 01-formulation.tex，`fig:opt-prob-extended-value` | 100 × 52 | $(x-2)^2$加$\iota_{\{x\leq1\}}$最小点$x=1$（值$1$）对比加惩罚$\max\{0,x-1\}$最小点$x=1.5$（值$0.75$）。 |
| c1-lsc-gap | Matplotlib（generate_c1.py） | 02-existence.tex，`fig:opt-prob-lsc-gap` | 112 × 48 | 跳跃函数在$0$处取$0.4$或$1$，下水平集$\{f\leq0.6\}$分别为$[0,0.4]$与$(0,0.4]$。 |
| c1-existence-failures | Matplotlib（generate_c1.py） | 02-existence.tex，`fig:opt-prob-existence-failures` | 150 × 48（figure*） | 存在性三环节失效：$(0,1]$上的$x$、$[1,\infty)$上的$1/x$、$[-1,1]$上$f(0)=0.6$的跳高$x^2$。 |
| c1-ls-sublevel | Matplotlib（generate_c1.py） | 02-existence.tex，`fig:opt-prob-ls-sublevel` | 124 × 62（figure*） | $\frac12(x_1+x_2-2)^2+\frac{\lambda}{2}\lVert\bm x\rVert^2$的$\{f\leq1\}$：$\lambda=0$为无界带，$\lambda=0.5$为椭圆，$\bm x^\star=(0.8,0.8)$、$f^\star=0.4$。 |
| c1-convex-sets | TikZ（render_tikz.py） | 03-convexity.tex，`fig:opt-prob-convex-sets` | 97.0 × 38.8 | 椭圆盘（凸）、月牙形（线段穿出）、资源四边形中$P=(3,0)$与$Q=(0,4)$的混合$M=(1.5,2)$。 |
| c1-chord-tangent | Matplotlib（generate_c1.py） | 03-convexity.tex，`fig:opt-prob-chord-tangent` | 112 × 50 | $x^2/2$的弦（$-1$到$2$）在上、切线（$x_0=1/2$）在下；非凸$x^4/4-x^2$的弦（$-1.6$到$1$）与$x=0$水平切线反例。 |
| c1-strong-convex-gap | Matplotlib（generate_c1.py） | 03-convexity.tex，`fig:opt-prob-strong-convex-gap` | 150 × 54（figure*） | (a) $x^2/2+|x-0.5|$（$\mu=1$）的弦减二次间隔；(b) $\bm H=[[2,1],[1,2]]$沿三方向的增长$t^2/2,t^2,3t^2/2$。 |
| c1-stationary-types | Matplotlib（generate_c1.py） | 04-optimality-conditions.tex，`fig:opt-prob-stationary-types` | 160 × 46（figure*） | $x^2+y^2$、$x^2-y^2$、$x^2+y^4$、$x^2+y^3$的等值线，红色为$f<0$区域。 |
| c1-saddle-curvature | Matplotlib（generate_c1.py） | 04-optimality-conditions.tex，`fig:opt-prob-saddle-curvature` | 150 × 58（figure*） | $x^2-y^2$线框曲面与沿$(1,0),(1,1)/\sqrt2,(0,1)$的一元限制，曲率$2,0,-2$。 |
| c1-flat-gradient | Matplotlib（generate_c1.py） | 05-approximation.tex，`fig:opt-prob-flat-gradient` | 150 × 58（figure*） | (a) 导数同为$0.1$而目标差$0.5$对$0.005$、距离$10$对$0.1$；(b) $\lambda=0.01$实例中$\hat{\bm x}=(11,-9)$梯度范数$0.142$、目标差$1.00$、距离$14.1$。 |
| c1-convergence-cost | Matplotlib（generate_c1.py） | 05-approximation.tex，`fig:opt-prob-convergence-cost` | 150 × 54（figure*） | 公式序列$1/(t+1)$、$0.9^t$、平方递推按轮数与按代价（每轮$1$对$40$）比较；到$10^{-8}$代价$175$对$200$，到$10^{-12}$为$263$对$240$。 |

## 第2章 优化问题与解

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
| --- | --- | --- | --- | --- |
| c2-resource-polygon | TikZ | 01-linear-models.tex，`fig:opt-lp-resource-polygon` | 64.9 × 59.8 | 资源例可行四边形（顶点(0,0),(2,0),(4/3,4/3),(0,2)）与等值线3x1+2x2=2,4,6,20/3，最优顶点(4/3,4/3)及方向(3,2) |
| c2-active-faces | TikZ | 01-linear-models.tex，`fig:opt-lp-active-faces` | 58.0 × 46.6 | 内部点、边上点与顶点(4/3,4/3)处的可行方向（圆盘、半盘、由(1,-2)与(-2,1)张成的锥），一条边作为面 |
| c2-polyhedron-cases | TikZ | 01-linear-models.tex，`fig:opt-lp-polyhedron-cases`（figure*） | 156.5 × 39.4 | 空集；{x≥0,x1+x2≥1}上min x1+2x2在(1,0)取1；同一区域min x2−x1沿x0=(1,0)+t(1,0)无下界；条带0≤x2≤1无极点 |
| c2-basic-solutions | TikZ | 02-basic-solutions.tex，`fig:opt-lp-basic-solutions` | 72.8 × 66.6 | 资源例6个基本解：4个可行顶点与B={1,3}(x3=−4)、B={2,4}(x4=−4)两个不可行点 |
| c2-optimal-face | TikZ | 02-basic-solutions.tex，`fig:opt-lp-optimal-face` | 93.4 × 51.3 | max 3x1+2x2唯一顶点最优（20/3）；max 2x1+x2整条边[(2,0),(4/3,4/3)]最优（值4），含非顶点最优解(5/3,2/3) |
| c2-simplex-path | TikZ | 03-simplex.tex，`fig:opt-lp-simplex-path` | 107.3 × 55.4 | 单纯形路径(0,0)→(2,0)→(4/3,4/3)（目标0,−6,−20/3）及经(0,2)的另一路径；比值检验x3=4−2θ、x4=4−θ，θ*=2 |
| c2-two-phase-flow | TikZ | 03-simplex.tex，`fig:opt-lp-two-phase-flow` | 108.1 × 70.0 | 两阶段法流程：第一阶段最优值>0给Farkas证书，=0则移出人工变量进入第二阶段，结局为最优证书或无下界射线 |
| c2-degenerate-vertex | TikZ | 03-simplex.tex，`fig:opt-lp-degenerate-vertex` | 72.2 × 48.0 | 加x1≤2后顶点(2,0)有三条边界、三个基{1,4,5},{1,3,4},{1,2,4}；路径含一次零步长换基后到(4/3,4/3) |
| c2-dual-bounds | TikZ | 04-duality.tex，`fig:opt-lp-dual-bounds`（figure*） | 113.8 × 56.3 | 价格可行域2u1+u2≥3,u1+2u2≥2,u≥0，最小总价20/3于(4/3,1/3)；数轴上原始获利0,5,6与对偶上界8,10夹住20/3 |
| c2-farkas | TikZ | 04-duality.tex，`fig:opt-lp-farkas` | 111.9 × 65.0 | 列a1=(2,1),a2=(1,2)张成的锥；b=(4,4)=4/3a1+4/3a2在锥内；b'=(4,−1)在锥外，z=(−1,2)给出分离超平面，b'ᵀz=−6 |
| c2-rhs-sensitivity | TikZ | 05-sensitivity.tex，`fig:opt-lp-rhs-sensitivity`（figure*） | 122.4 × 67.7 | b1=2,4,6,8时最优顶点沿x1+2x2=4从(0,2)移到(4,0)；v(b1)分段线性，斜率2,4/3,0，原基有效区间[2,8] |
| c2-cost-sensitivity | TikZ | 05-sensitivity.tex，`fig:opt-lp-cost-sensitivity`（figure*） | 123.1 × 66.5 | 顶点(4/3,4/3)处由法向(2,1),(1,2)张成的最优性锥，c1=3在内、c1=6在外；v(c1)=max{4,4c1/3+8/3,2c1}，有效区间[1,4] |
| c2-exact-hull | TikZ | 06-relaxation.tex，`fig:opt-lp-exact-hull` | 56.3 × 46.0 | S={(0,0),(1,0),(0,1)}的凸包上max x1+x2，最优值1，最优面为斜边，含分数点(1/2,1/2) |
| c2-outer-relaxation | TikZ | 06-relaxation.tex，`fig:opt-lp-outer-relaxation` | 101.0 × 52.9 | 二元选择2x1+2x2≤3的松弛五边形与精确凸包，松弛值3/2、整数最优1；四舍五入(1,1)不可行、向下取整(0,0)值0、从(1,1/2)修复到(1,0)值1 |

## 第3章 线性规划

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
|---|---|---|---|---|
| c3-quadratic-upper-bound | TikZ/pgfplots（`tikz/generate_c3.py`采样） | `01-local-upper-bounds.tex`，`fig:opt-smooth-upper-bound` | 99.5×62.2 | $\log(1+x^2)$在$x^{(0)}=1.5$处被$L=2$的二次上下界夹住，上界最小点$x^{(1)}\approx1.038$，上界值约0.966，真实值约0.732 |
| c3-step-size | TikZ/pgfplots | `02-gradient-methods.tex`，`fig:opt-smooth-step-size` | 110.0×51.5 | $x^{(t)}=(1-\eta\lambda)^t$在$\eta\lambda=0.5,1.5,2,2.1$下的四种行为及因子$|1-\eta\lambda|$ |
| c3-gd-zigzag | TikZ/pgfplots | `02-gradient-methods.tex`，`fig:opt-smooth-gd-zigzag` | 149.7×57.0 | 共同例$\tfrac12(x_1^2+16x_2^2)$从$(2,2)$出发，$\eta=1/16,\,2/17,\,0.13$的梯度下降路径 |
| c3-armijo | TikZ/pgfplots | `02-gradient-methods.tex`，`fig:opt-smooth-armijo` | 98.0×57.2 | 共同例负梯度截面$\varphi(\eta)$、切线$34-1028\eta$、Armijo线$34-257\eta$；$\eta=1/8$拒绝、$1/16$接受 |
| c3-preconditioning | TikZ/pgfplots | `02-gradient-methods.tex`，`fig:opt-smooth-preconditioning` | 155.7×57.7 | 原坐标中GD($2/17$)与$\bm P=\operatorname{diag}(1,1/16)$、$\eta=1/2$的对比；好坐标中等高线为圆；坏预条件$\operatorname{diag}(1/16,1)$使条件数256 |
| c3-momentum-stability | TikZ/pgfplots | `02-gradient-methods.tex`，`fig:opt-smooth-momentum-stability` | 96.6×53.1 | 重球递推最大根模随$\eta\lambda$变化，$\beta=0,9/25,0.81$；$[0.16,2.56]$上恒为0.6 |
| c3-momentum-paths | TikZ/pgfplots | `02-gradient-methods.tex`，`fig:opt-smooth-momentum-paths` | 132.0×69.3 | 共同例上GD($1/16$)、重球($4/25,9/25$)、Nesterov($L=16$)的路径与目标差，含上界$256/(t+1)^2$ |
| c3-newton-model | TikZ/pgfplots | `03-curvature-local-models.tex`，`fig:opt-smooth-newton-model` | 102.6×53.3 | $e^x-2x$在1.5处的二次模型与牛顿步$x^{(1)}\approx0.946$；牛顿误差$0.81\to4.3\times10^{-15}$（5步）对比GD |
| c3-trust-region | TikZ/pgfplots | `03-curvature-local-models.tex`，`fig:opt-smooth-trust-region` | 121.1×57.2 | 共同例$\Delta=2.5$的Cauchy点、牛顿点与狗腿步$(-1.497,-2.002)$；$x^4/4$、$B=1/2$下$\Delta=2$拒绝($\rho=0$)、$\Delta=1/2$接受($\rho=15/28$) |
| c3-secant | TikZ/pgfplots | `03-curvature-local-models.tex`，`fig:opt-smooth-secant` | 105.5×55.2 | $f'=e^x-2$在0、1间割线斜率$e-1$；$B^{(0)}=I$、$H=\operatorname{diag}(1,16)$与沿$s=(1,1)$一次BFGS后$B^{(1)}$的曲率椭圆 |
| c3-cubic-model | TikZ/pgfplots | `03-curvature-local-models.tex`，`fig:opt-smooth-cubic-model` | 92.9×55.8 | $x^4/4-x^2/2$在0.2处二次模型无下界，立方模型($\sigma=3$)给$s\approx0.439$，目标$-0.0196\to-0.163$ |
| c3-saddle-escape | TikZ/pgfplots | `04-nonconvex-saddles.tex`，`fig:opt-smooth-saddle-escape` | 141.7×64.6 | $\tfrac14x_1^4-\tfrac12x_1^2+\tfrac12x_2^2$，$\eta=0.2$：稳定流形上收敛到鞍点、偏移$10^{-3}$第35步离开、第23步扰动（种子20261030，半径$10^{-2}$）后离开 |
| c3-convergence-cost | TikZ/pgfplots | `05-accuracy-cost.tex`，`fig:opt-smooth-convergence-cost` | 154.6×57.4 | 二维指数和目标上GD/BFGS/阻尼牛顿（Armijo，$c=10^{-4}$）的路径、按轮数与按成本的目标差；到$10^{-8}$：20/96、7/19、4/18 |
| c3-error-propagation | TikZ/pgfplots | `05-accuracy-cost.tex`，`fig:opt-smooth-error-propagation` | 108.5×53.4 | $x^2/2$、$\eta=1/2$下固定梯度误差$e=0,0.01,0.1$的下限$e^2/2$；$\delta^{(t+1)}=q\delta^{(t)}+10^{-3}$在$q=0.9,1,1.05$的衰减、积累与放大 |
| c3-sensitivity | TikZ/pgfplots | `06-solution-sensitivity.tex`，`fig:opt-smooth-sensitivity` | 95.8×61.1 | $\tfrac12\bm x^\top\bm H\bm x-\bm b^\top\bm x$中$b_2$加0.1：$\bm H=\operatorname{diag}(1,0.1)$时最小点移动1，$\bm H=\bm I$时移动0.1 |

## 第4章 光滑优化

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
|---|---|---|---|---|
| c4-abs-supports | Matplotlib（`generate_c4.py abs-supports`） | `01-nonsmooth-optimality.tex`，`fig:opt-ns-abs-supports` | 112×46 | $\lvert x\rvert$在原点的支撑线族（斜率$-1,-0.5,0,0.5,1$）与次微分集合值映射，原点处为$[-1,1]$。 |
| c4-max-affine-subdiff | Matplotlib | `01-nonsmooth-optimality.tex`，`fig:opt-ns-max-affine` | 112×48 | $\max\{-x,x/2,2x-3\}$的分支与支撑线，次微分在$0,2$处为$[-1,1/2],[1/2,2]$。 |
| c4-clarke-abs | Matplotlib | `01-nonsmooth-optimality.tex`，`fig:opt-ns-clarke` | 112×42 | $\lvert x\rvert$与$-\lvert x\rvert$在原点的Clarke广义梯度同为$[-1,1]$，$g=0$直线分别为全域支撑与上方直线。 |
| c4-subgrad-not-descent | Matplotlib | `02-subgradient-methods.tex`，`fig:opt-ns-subgrad-not-descent` | 80×62 | $\lvert x_1\rvert+2\lvert x_2\rvert$在$(1,0)$处，$-(1,2)$使目标升为$1+3s$但进入距最小点为1的圆内，$-(1,0)$下降。 |
| c4-subgrad-steps | Matplotlib | `02-subgradient-methods.tex`，`fig:opt-ns-subgrad-steps` | 112×50 | 初值$(1.47,0.93)$，$\eta=0.1$锯齿路径；最佳目标差：$\eta=0.1$停约0.17，$\eta=0.01$停约0.02，递减步长2000步约0.013，参考$RG/\sqrt T$。 |
| c4-prox-subproblem | Matplotlib | `03-proximal-mappings.tex`，`fig:opt-ns-prox-subproblem` | 112×46 | $\lvert w\rvert+(w-z)^2/2$，$z=0.5\mapsto p=0$，$z=2\mapsto p=1$。 |
| c4-prox-maps | Matplotlib | `03-proximal-mappings.tex`，`fig:opt-ns-prox-maps` | 86×56 | 参数1下的软阈值、二次收缩$z/2$、区间$[-1,1]$投影与恒等映射。 |
| c4-projection-normal-cone | TikZ | `03-proximal-mappings.tex`，`fig:opt-ns-projection` | 59.33×49.35 | $[0,1]^2$上$(1.6,0.6)\mapsto(1,0.6)$（法线射线）、$(1.7,-0.5)\mapsto(1,0)$（顶点法锥象限），钝角关系。 |
| c4-prox-point | Matplotlib | `03-proximal-mappings.tex`，`fig:opt-ns-prox-point` | 112×46 | $\lvert x\rvert$、$\eta=1$、初值2.5：邻近点法$2.5,1.5,0.5,0$停住，次梯度法在$\pm0.5$振荡。 |
| c4-lasso-path | Matplotlib | `04-proximal-gradient.tex`，`fig:opt-ns-lasso-path` | 100×74 | 二维Lasso（$\bm A=[[1,1],[1,0]]$，$\bm b=(1,2)$，$\lambda=1$，$\eta=1/4$）从$(-1,2)$出发，第7步到横轴，趋于$(1,0)$；光滑部分梯度下降趋于$(2,-1)$。 |
| c4-ista-fista | Matplotlib | `04-proximal-gradient.tex`，`fig:opt-ns-ista-fista` | 112×50 | 种子20261030的Lasso（$60\times100$）：第100轮目标差邻近梯度约0.21、FISTA约$4.8\times10^{-6}$；FISTA 600轮中254轮上升；附理论界。 |
| c4-smooth-max | Matplotlib | `05-smoothing.tex`，`fig:opt-ns-smooth-max` | 112×48 | $\nu=0.5$时$\lvert x\rvert$的对数和指数光滑化（偏差$\nu\log2$）与Huber函数（偏差$\leq\nu/2$）及其导数$\tanh(x/\nu)$、截断$x/\nu$。 |
| c4-smoothing-budget | Matplotlib | `05-smoothing.tex`，`fig:opt-ns-smoothing-budget` | 100×56 | 五分支平面最大值（$F^\star\approx0.3065$），$\nu=1,0.1,0.01$的梯度下降平台约0.093、0.026、0.0026，均低于$\nu\log5$。 |
| c4-mm-surrogates | Matplotlib | `06-surrogate-models.tex`，`fig:opt-ns-mm-surrogates` | 112×50 | (a) $x^2/2$在1处代理$(x-1/2)^2+1/4$与切线$x-1/2$；(b) Cauchy拟合$0,0,10$从4出发的三轮代理，$w=4\to1.868\to0.324\to0.058$。 |
| c4-bundle-model | Matplotlib | `06-surrogate-models.tex`，`fig:opt-ns-bundle` | 112×50 | $\lvert x-1\rvert+x^2/4$的邻近束方法（$\tau=1$）：中心0候选1实质步；中心1候选0.9模型值0.1、真实0.3025空步。 |

## 第5章 非光滑与复合优化

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
|---|---|---|---|---|
| c5-normal-cone | Matplotlib（generate_c5.py） | 01-optimality-conditions.tex，`fig:opt-con-normal-cone` | 169×60 | 三角形$x\ge0,x_1+x_2\le2$上$c=(0.6,0.8),(2,1),(3,-1)$的最近点与法锥，角点处$-\nabla f=(1,-1)=1\cdot(1,1)+2\cdot(0,-1)$ |
| c5-cusp | Matplotlib | 01-optimality-conditions.tex，`fig:opt-con-cusp` | 96×56 | 尖点$x_2\le(1-x_1)^3$、$x_2\ge0$在$(1,0)$处线性化方向$d_2=0$多于真实方向$(-1,0)$ |
| c5-tangency | Matplotlib | 01-optimality-conditions.tex，`fig:opt-con-tangency` | 100×70 | $\frac12(x_1^2+4x_2^2)$等值线与$x_1+x_2=1$相切于$(4/5,1/5)$，非最优点$(0.2,0.8)$梯度有切向分量 |
| c5-dual-envelope | Matplotlib | 02-duality.tex，`fig:opt-con-dual-envelope` | 169×62 | $\min x^2$、$1-x\le0$的像集与斜率$-\lambda$支撑直线，$q(\lambda)=\lambda-\lambda^2/4$在$\lambda=2$达到1 |
| c5-conjugate | Matplotlib | 02-duality.tex，`fig:opt-con-conjugate` | 169×58 | $x^2/2$在$y=1.5$的切线与$f^*=1.125$；$|x|$的支撑斜率$|y|\le1$ |
| c5-slater | Matplotlib | 02-duality.tex，`fig:opt-con-slater` | 169×58 | 值函数$((1-u)_+)^2$有斜率$-2$支撑；$-\sqrt u$在$u=0$竖直，$q=-1/(4\lambda)\uparrow0$不达到 |
| c5-sensitivity | Matplotlib | 03-sensitivity.tex，`fig:opt-con-sensitivity` | 169×58 | 预算例$V(\tau)$、乘子与$\tau=2$处斜率$-1/2$支撑线；$V(b)=\max\{-b,-1\}$折点处斜率$[-1,0]$ |
| c5-soc | Matplotlib（3D） | 04-quadratic-conic.tex，`fig:opt-con-soc` | 84×66 | $\mathbb R^3$二阶锥，截面$t=1,0.6$，锥内点$(0.3,0.2,0.8)$ |
| c5-psd-disk | Matplotlib | 04-quadratic-conic.tex，`fig:opt-con-psd-disk` | 100×66 | 迹1的$2\times2$矩阵：半正定圆盘$(a-\frac12)^2+b^2\le\frac14$与逐元素非负区域，$\langle C,X\rangle=2+2b$最小值1于$(1/2,-1/2)$ |
| c5-pg-fw | Matplotlib | 05-feasible-updates.tex，`fig:opt-con-pg-fw` | 169×64 | 三角形上$\frac12((x_1-2.5)^2+4(x_2-1)^2)$：投影梯度（$\eta=1/4$）线性收敛，条件梯度振荡、100步误差约$7\times10^{-5}$，界$2LD^2/(t+2)$ |
| c5-mirror-simplex | Matplotlib | 05-feasible-updates.tex，`fig:opt-con-mirror-simplex` | 169×62 | 单纯形上$\frac12\|x-c\|^2$，$c=(0.8,0.6,-0.1)$：投影梯度第3步起$x_3=0$，熵镜像下降$x_3$保持为正、40步约$1.2\times10^{-6}$ |
| c5-penalty-path | Matplotlib | 06-penalty.tex，`fig:opt-con-penalty-path` | 169×64 | 二次惩罚解路径$(4\rho,\rho)/(4+5\rho)$、$\rho=20$等值线；违约$4/(4+5\rho)$与条件数（约$0.8\rho$） |
| c5-exact-penalty | Matplotlib | 06-penalty.tex，`fig:opt-con-exact-penalty` | 169×56 | $\min x$、$x\ge1$：二次惩罚最小点$1-1/\rho$；精确惩罚$\rho=0.5,1,2$，阈值为乘子1 |
| c5-al-multiplier | Matplotlib | 07-multipliers.tex，`fig:opt-con-al-multiplier` | 169×56 | 等式二次例：对偶上升误差减半，增广Lagrange比率$4/(4+5\rho)$（$\rho=1,10$），对照二次惩罚违约 |
| c5-admm | Matplotlib | 07-multipliers.tex，`fig:opt-con-admm` | 169×64 | $\frac12(x-3)^2+|z|$、$x=z$的ADMM交替路径收拢到$(2,2)$；$\rho=0.5,1,2$误差比率$\rho/(1+\rho)$ |
| c5-sqp | Matplotlib | 08-sqp.tex，`fig:opt-con-sqp` | 100×70 | $\min x_1+x_2$、$x_1^2+x_2^2=2$从$(0.2,-1.6)$出发的SQP迭代与首个线性化约束 |
| c5-central-path | Matplotlib | 09-interior-point.tex，`fig:opt-con-central-path` | 96×78 | $\min x_1+2x_2+3x_3$单纯形上的中心路径（$\mu=10^3\to10^{-3}$）与$\mu=0.3$障碍等值线，间隙$3\mu$ |
| c5-pdipm | Matplotlib | 09-interior-point.tex，`fig:opt-con-pdipm` | 100×56 | 资源分配LP（$n=4,m=2$）原始—对偶内点法：残差两步消失，$x^\top s$由8按约0.2比率降到$7\times10^{-6}$（第9步） |
| c5-sdp-rounding | Matplotlib | 10-sdp-relaxation.tex，`fig:opt-con-sdp-rounding` | 169×62 | 最大割松弛向量：四顶点圈秩一（割值4）；三角形$120^\circ$向量，松弛值$9/4$，超平面舍入得割值2 |

## 第6章 约束优化与对偶

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
| --- | --- | --- | --- | --- |
| c6-sum-vs-block | TikZ | 06-stochastic-block-optimization/01-finite-sum-expectation.tex，`fig:opt-sto-sum-vs-block` | 96.9×55.9 | 8×6 数据矩阵上目标项分解（读第 2、6 行、更新全部坐标）与变量分块（读全部行、只更新坐标块 J={3,4}）的对照。 |
| c6-gradient-fan | Matplotlib | 02-stochastic-gradient.tex，`fig:opt-sto-gradient-fan` | 100×62 | n=10、d=2 岭回归一点处 10 个逐项下降方向与平均方向，其中 3 个与平均方向成钝角（种子 20261031）。 |
| c6-sgd-noise-ball | Matplotlib | 02-stochastic-gradient.tex，`fig:opt-sto-noise-ball` | 160×60 | n=40、d=2 岭回归（μ≈0.304，L_max≈9.83，σ*²≈0.577）上梯度下降与随机梯度路径、300 次运行终点云，以及 η=1/(2L_max),1/(4L_max),1/(8L_max) 的平均误差平台与上界 2ησ*²/μ。 |
| c6-step-schedules | Matplotlib | 02-stochastic-gradient.tex，`fig:opt-sto-step-schedules` | 160×56 | 常数 η0≈0.051、递减 2/(μ(t+t0))（t0≈129）、每 500 步减半三种调度的步长曲线与 400 次运行平均误差，附 ν/(t+t0) 界。 |
| c6-return-points | Matplotlib | 02-stochastic-gradient.tex，`fig:opt-sto-return-points` | 105×58 | 常数步长下最后一点（平台约 8.6e-3）、全程平均点与后半程平均点（4000 步约 1.4e-4）的平均目标差。 |
| c6-importance-sampling | Matplotlib | 03-sampling-variance.tex，`fig:opt-sto-importance` | 160×54 | 前 4 行放大 6 倍的岭回归：p_i∝‖a_i‖² 抽样分布；均匀（t0≈458）、重加权（t0≈32，σ*,p²≈1.12 对 0.645）与不重加权（收敛到有偏点，平方距离 0.042）的误差。 |
| c6-minibatch-variance | Matplotlib | 03-sampling-variance.tex，`fig:opt-sto-minibatch` | 100×58 | n=200、d=5 最小二乘在 x=0 处（σ²≈11.7）小批量方差：有放回 σ²/b 与无放回 σ²(n−b)/(b(n−1)) 公式及各 4000 次抽样的经验值。 |
| c6-variance-reduction | Matplotlib | 03-sampling-variance.tex，`fig:opt-sto-variance-reduction` | 160×58 | n=200、d=10 岭逻辑回归上梯度下降、常数/递减随机梯度、SVRG、SAGA 的目标差与方向条件方差随读取量（30 遍）变化；30 遍时 SAGA≈7e-14、SVRG≈1.3e-7、常数随机梯度≈1.6e-2。 |
| c6-adaptive-paths | Matplotlib | 04-adaptive-updates.tex，`fig:opt-sto-adaptive-paths` | 160×56 | 精确梯度下梯度下降、AdaGrad、Adam 在 diag(1,25) 二次目标上的路径与目标值，以及旋转 45° 后的目标值（60 步：对齐时 AdaGrad≈1.3e-8，旋转后 AdaGrad≈0.026、Adam≈0.027、梯度下降≈0.060）。 |
| c6-adafactor | Matplotlib | 04-adaptive-updates.tex，`fig:opt-sto-adafactor` | 160×46 | 6×8 平方统计的完整表、由 6 个行和与 8 个列和重建的表及逐元素相对误差（平均约 0.18，最大约 0.63）。 |
| c6-lion-muon | Matplotlib | 04-adaptive-updates.tex，`fig:opt-sto-lion-muon` | 160×56 | (a) 读数 (0.2,0.05)、(4,1)、(3,−0.4) 的符号方向；(b) Muon 五次多项式迭代 5 次的奇异值映射（s∈[0.02,1] 输出约 [0.68,1.13]）与三次 Newton–Schulz（s=0.01 时约 0.076）。 |
| c6-coordinate-descent | Matplotlib | 05-block-alternating.tex，`fig:opt-sto-coordinate-descent` | 160×64 | (a) ½(u−v)²+½(u−1)² 上循环坐标下降的阶梯路径与梯度下降；(b) 2|u−v|+|u+v−2| 在原点沿坐标轴严格最小（F=2）而最小点为 (1,1)。 |
| c6-alternating | Matplotlib | 05-block-alternating.tex，`fig:opt-sto-alternating` | 105×72 | ½(uv−1)²+0.025(u²+v²) 上从 (3,0.1) 的 8 轮交替最小化（目标 0.470→0.0499，最小值 0.04875）与停在原点鞍点的情形。 |
| c6-clipping | Matplotlib | 06-direction-processing.tex，`fig:opt-sto-clipping` | 160×58 | (a) (3,4) 在 c=1 下逐坐标裁剪为 (1,1)、范数裁剪为 (0.6,0.8)；(b) 两点读数 2,−1 与 −1+Exp(1.5) 裁剪后均值随阈值的变化。 |
| c6-ste | Matplotlib | 06-direction-processing.tex，`fig:opt-sto-ste` | 105×56 | 取整前向损失 ½(round(w)−a)²，a=1 与 a=0.4；从 w=0.2 沿 STE 方向到 w=0.6，损失分别 0.5→0 与 0.08→0.18。 |
| c6-perturbation | Matplotlib | 07-perturbation.tex，`fig:opt-sto-perturbation` | 160×60 | (a) 仅噪声（η0=0.4、η0/4、批量 4）与仅偏差 β=(0.25,0) 的误差平台，偏差平台 ‖H⁻¹β‖²≈0.023；(b) 替换一个样本后耦合运行的平均参数距离（约 0.064）与非扩张界、压缩界（G≈2.78）。 |
| c6-batch-cost | Matplotlib | 08-cost-comparison.tex，`fig:opt-sto-batch-cost` | 100×58 | n=10000、d=5 岭回归，精确矩递推下各批量取最优常数步长达到 E f−f*≤1e-3 的读取量：b≤64 约 4.1e4，b=4096 约 1.39e5；梯度下降 4.3e5。 |

## 第7章 随机与分块优化

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
|---|---|---|---|---|
| c7-pareto-candidates | Matplotlib（generate_c7.py） | 01-multiobjective.tex，`fig:opt-mmb-pareto-candidates` | 92×66 | 六个候选A(1,5)…F(6,1)在目标平面上，B、D的被支配区域，A–D为前沿，F仅弱Pareto |
| c7-pareto-set-front | Matplotlib | 01-multiobjective.tex，`fig:opt-mmb-pareto-set-front` | 150×62 | 两二次指标（a=(1,0),b=(−1,0)）的参数空间Pareto线段与目标空间前沿、可达集合，p=(0,1)的像(1,1)被(1/2,1/2)支配 |
| c7-weighted-sum | Matplotlib | 01-multiobjective.tex，`fig:opt-mmb-weighted-sum` | 150×62 | 凹陷前沿上α=0.62/0.5/0.3的支撑线及不可达段（约0.27<u<0.63）；有限例α=0.85/0.5/0.2分别选A/B/D，C永不被选 |
| c7-threshold | Matplotlib | 01-multiobjective.tex，`fig:opt-mmb-threshold` | 150×62 | 阈值τ=0.2/0.4/0.55/0.8扫过前沿含凹陷段；有限例加权和与阈值法所选候选的阶梯对比 |
| c7-common-descent | Matplotlib | 01-multiobjective.tex，`fig:opt-mmb-common-descent` | 150×64 | p=(0,1)处梯度(−1,1)、(1,1)、最小范数元(0,1)、共同下降锥与透镜区域；η=1/2共同下降路径收敛到Pareto线段 |
| c7-worst-case-envelope | Matplotlib | 02-minimax.tex，`fig:opt-mmb-worst-case` | 96×62 | (x−y)²的上包络(|x|+1)²最小值1；只查y=±1/2时低估为1/4 |
| c7-saddle-surfaces | Matplotlib（3D） | 02-minimax.tex，`fig:opt-mmb-saddle-surfaces` | 150×64 | x²−y²（极小极大鞍点）与y²−x²（仅微分鞍点）的曲面及两方向截线 |
| c7-gda-bilinear | Matplotlib | 02-minimax.tex，`fig:opt-mmb-gda-bilinear` | 150×64 | φ=xy、η=1/2、起点(1/2,0)、16步：同时法距离²每步×1.25，交替法有界振荡，外梯度×0.8125 |
| c7-box-cycle | TikZ | 02-minimax.tex，`fig:opt-mmb-box-cycle` | 52.5×47.8 | 盒[−1,1]²上η=1的投影同时梯度下降—上升八点循环，间隙≥1 |
| c7-extragradient-step | TikZ | 02-minimax.tex，`fig:opt-mmb-extragradient-step` | 54.0×51.0 | u=(1.6,0)、η=1/2：试探点(1.6,0.8)、外梯度校正点(1.2,0.8)、两次普通步(1.2,1.6) |
| c7-inner-selection | Matplotlib | 03-bilevel.tex，`fig:opt-mmb-inner-selection` | 88×70 | θ=0内层解集x1+x2=2、正则路径2/(2+θ)(1,1)趋于最小范数解(1,1)、外层目标点c=(1.5,0.5) |
| c7-bilevel-chain | TikZ | 03-bilevel.tex，`fig:opt-mmb-bilevel-chain` | 140.1×53.5 | 双层复合结构与迭代展开（反向伴随回传）、隐式微分（驻点方程+伴随方程）两条路线 |
| c7-unroll-vs-implicit | Matplotlib | 03-bilevel.tex，`fig:opt-mmb-unroll` | 150×62 | 岭例a=3,b=1,η=1/2：x^(T)(θ)与x*=3/(1+θ)，J_2最小于5/3、J于2；θ=0超梯度0,−15/16,−39/16…→−6及T=20截断反传 |
| c7-branch-switch | Matplotlib | 03-bilevel.tex，`fig:opt-mmb-branch-switch` | 150×62 | 倾斜双势阱x³−x+θ=0两条分支与折点θ=±2/(3√3)；外层值沿全局选解在θ=0跳变（乐观0/悲观2），沿右分支光滑 |

## 第8章 多目标、极小极大与双层优化

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
| --- | --- | --- | --- | --- |
| c8-interpolation-vs-regularization | Matplotlib（generate_c8.py） | 08-function-fitting-regularization.tex，`fig:opt-fit-interpolation-vs-regularization` | 100×50 | 15个带噪读数上14次多项式插值（最大2.60，曲率积分8.0e6）与曲率惩罚λ=1e-4拟合（最大1.17，曲率积分1.2e3） |
| c8-invisible-direction | Matplotlib | 01-observations-objectives.tex，`fig:opt-fit-invisible-direction` | 78×46 | f0=4x(1-x)与f0+c·x(x-1/2)(x-1)（c=0,±8,±16）在0,1/2,1读数相同 |
| c8-residual-losses | Matplotlib | 01-observations-objectives.tex，`fig:opt-fit-residual-losses` | 112×46 | 平方、绝对值、Huber(δ=1)、Cauchy代价及等效权重1,1/|r|,min(1,1/|r|),1/(1+r²) |
| c8-decay-vs-l2 | Matplotlib | 01-observations-objectives.tex，`fig:opt-fit-decay-vs-l2` | 112×50 | (a)零数据梯度下AdamW首步0.8与Adam+L2首步14/15的30步轨迹；(b)P=diag(1,4)下两种更新的不动点(1/2,1/2)与(1/2,4/5) |
| c8-ridge-filter | Matplotlib | 02-linear-representation.tex，`fig:opt-fit-ridge-filter` | 80×46 | 滤波因子σ²/(σ²+λ)，λ=1e-4,1e-2,1，σ=√λ处为1/2 |
| c8-irls-outliers | Matplotlib | 02-linear-representation.tex，`fig:opt-fit-irls` | 112×50 | (a)两离群点下LS斜率0.71与Cauchy IRLS斜率1.89、离群权重≈0.009/0.006；(b)拟合0,0,10的Cauchy目标、0处代理、首步10/203、局部最小点≈9.79 |
| c8-gn-lm-scalar | Matplotlib | 03-nonlinear-parameters.tex，`fig:opt-fit-gn-lm-scalar` | 96×52 | r=θ²-4、θ0=1/2：GN候选17/4（F≈98.9），τ=4的LM候选5/4（F=1521/512） |
| c8-lm-path | Matplotlib | 03-nonlinear-parameters.tex，`fig:opt-fit-lm-path` | 96×62 | 指数模型拟合中LM步路径θ0+p(τ)，GN点(1.78,0.60)、最小点(2.00,0.59)、τ→∞沿负梯度 |
| c8-representer-geometry | TikZ | 04-hilbert-finite-observations.tex，`fig:opt-fit-representer-geometry` | 73.5×49.3 | M、M⊥、等读数仿射集P_Mf+M⊥与余项r的正交几何，过P_Mf的圆弧相切 |
| c8-min-kernel-fit | Matplotlib | 04-hilbert-finite-observations.tex，`fig:opt-fit-min-kernel` | 112×54 | 最小值核读f(1/2)=f(1)=1：λ=1/4解(4/5,2/5)、读数(3/5,4/5)；最小范数插值2min(·,1/2)范数²=2，加¼sin2πx后≈3.23 |
| c8-spectral-shrinkage | Matplotlib | 05-global-derivative-observations.tex，`fig:opt-fit-spectral-shrinkage` | 112×48 | 最小值核谱保留比例μj/(μj+λ)，常数数据的拟合边界层；有效维度1.58、5.00、15.81 |
| c8-gradient-projection | Matplotlib | 05-global-derivative-observations.tex，`fig:opt-fit-gradient-projection` | 112×42 | 单位正方形上v=∇φ+curlψ，投影∇φ与旋转余项curlψ（φ=sinπx sinπy，ψ=0.8φ） |
| c8-data-perturbation | Matplotlib | 06-error-stability.tex，`fig:opt-fit-data-perturbation` | 112×48 | 高斯核12点，单读数+0.4：λ=1e-7时‖δf‖_H≈16.3（界183），λ=1e-2时≈0.33（界0.58） |
| c8-lcurve | Matplotlib | 06-error-stability.tex，`fig:opt-fit-lcurve` | 112×50 | 15点核岭回归解族与L曲线；‖e‖≈0.559，残差匹配得λ≈2.8e-2 |
| c8-implicit-bias-gd | Matplotlib | 07-implicit-bias.tex，`fig:opt-fit-implicit-bias-gd` | 80×62 | X=(1,1),y=1：P=I极限(1/2,1/2)，P=diag(1,4)极限(1/5,4/5)，初值(1.2,-0.5)极限(1.35,-0.35) |
| c8-separable-direction | Matplotlib | 07-implicit-bias.tex，`fig:opt-fit-separable` | 112×50 | 六点可分数据，硬间隔解(0.8,0.4)；logistic GD方向夹角25°→5.9°（t=10⁶） |

## 第9章 函数拟合与正则化

| 图名 | 制作方式 | 引用位置（文件，`fig:` 标签） | 物理尺寸（mm） | 内容 |
|---|---|---|---|---|
| c9-perturbation-family | Matplotlib（generate_c9.py） | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/01-differential.tex，`fig:opt-fn-perturbation-family` | 110 × 46 | $u=x^2$加$t\sin\pi x$（$t=\pm0.2,\pm0.4$）的曲线族及$J_0(u+th)=2/3-4t/\pi+\pi^2t^2/4$，切线斜率$-4/\pi$ |
| c9-nonlinear-directional | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/01-differential.tex，`fig:opt-fn-nonlinear-directional` | 110 × 50 | $a^3/(a^2+b^2)$的等值线与原点方向导数$\cos^3\theta$对照$\cos\theta$，$\theta=\pi/4$处为$1/(2\sqrt2)$ |
| c9-gateaux-not-frechet | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/01-differential.tex，`fig:opt-fn-gateaux-not-frechet` | 110 × 50 | $a^3b/(a^4+b^2)$等值线；沿20°、60°射线比值趋0，沿抛物线$b=a^2$趋$1/2$ |
| c9-l2-h1-gradient | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/01-differential.tex，`fig:opt-fn-l2-h1-gradient` | 110 × 44 | $r=\sin\pi x+0.5\sin15\pi x$与$H_0^1$梯度（第$k$频除以$1+k^2\pi^2$），高频比例0.5→约0.0024 |
| c9-positivity-vi | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/02-optimality-conditions.tex，`fig:opt-fn-positivity-vi` | 96 × 46 | $g=\sin2\pi x$、$u^\star=\max(g,0)$与梯度$\max(-g,0)$，最小值1/8 |
| c9-no-uniform-curvature | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/02-optimality-conditions.tex，`fig:opt-fn-no-uniform-curvature` | 90 × 48 | 截线$t^2/k-t^4$，$k=1,4,16,64$，零点$1/\sqrt k$ |
| c9-smoothed-abs | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/03-integral-variations.tex，`fig:opt-fn-smoothed-abs` | 110 × 44 | $\sqrt{p^2+\varepsilon^2}$及导数，$\varepsilon=0,0.1,0.5,1$，导数最大斜率$1/\varepsilon$ |
| c9-fixed-endpoint-candidates | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/03-integral-variations.tex，`fig:opt-fn-fixed-endpoint-candidates` | 100 × 52 | 四条固定端点曲线的能量与长度：$x$（0.5，1.414）、$x^2$（0.667，1.479）、$x+0.15\sin2\pi x$（0.722，1.501）、$\sqrt x$（∞，1.479） |
| c9-boundary-conditions | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/03-integral-variations.tex，`fig:opt-fn-boundary-conditions` | 96 × 48 | $\int(u'^2/2-u)$两端固定解$x(1-x)/2$（$J=-1/24$）与右端自由解$x-x^2/2$（$J=-1/6$） |
| c9-bolza-sawtooth | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/04-existence.tex，`fig:opt-fn-bolza-sawtooth` | 110 × 44 | 锯齿$u_n$（$n=2,4,8$），$J(u_n)=1/(12n^2)$，$u_4'=\pm1$ |
| c9-transition-width | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/04-existence.tex，`fig:opt-fn-transition-width` | 110 × 44 | 宽$\delta=0.5,0.2,0.05$的单位过渡；$\int|u'|=1$，$\int|u'|^2=1/\delta$ |
| c9-projection-geometry | TikZ | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/04-existence.tex，`fig:opt-fn-projection-geometry` | 96.7 × 35.2 | 闭凸集投影的钝角关系与支撑线；闭子空间上的正交关系 |
| c9-ritz-hat | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/05-finite-approximation.tex，`fig:opt-fn-ritz-hat` | 110 × 48 | 帽函数Ritz近似（$N=4,8$）与$\sin\pi x$；$N=4..128$导数误差0.499→0.0157（阶约1）、$L^2$误差0.0393→3.9e-5（阶约2） |
| c9-energy-consistency | Matplotlib | tex/03-optimization-evolution-and-signals/01-optimization/09-functional-optimization/05-finite-approximation.tex，`fig:opt-fn-energy-consistency` | 110 × 44 | $E_N(\sin\pi x)=N^2\sin^2(\pi/2N)$趋于$\pi^2/4$，误差约$\pi^4/(48N^2)$ |
