# 卷二第1部分“度量与测度”图像

本目录保存第1—4章（度量空间、测度、积分、密度与换测度）独用的图像。全部为 TikZ 图源（含 pgfplots 曲线），图中数值均来自正文算例；图名前缀 `c1`—`c4` 对应本部分第1—4章。

每幅图一个目录，`figure.tex` 为可编辑图源，`figure.pdf/png/svg` 与 `figure.render.json` 由下列命令导出（从项目根目录运行）：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/02-abstract-mathematics/01-metric-and-measure/tikz/<图名>/figure.tex
```

`c2-cantor-function/generate.py` 计算Cantor函数逼近的折点，`c4-increment-measure/sample_cantor.py` 生成增量测度图中的曲线坐标，`c3-cantor-function` 的逼近点由精确分数递推得到。

| 图名 | 引用位置（章目录/节文件） | 物理尺寸（mm） | 内容 |
| --- | --- | --- | --- |
| c1-triangle-inequality | 01-metric-spaces/01-metrics.tex（`fig:metric-triangle`） | 98.972 × 39.342 | 三角不等式的直达与绕行，以及反向三角不等式中两距离之差不超过移动距离。 |
| c1-three-distances | 01-metric-spaces/01-metrics.tex（`fig:metric-three-distances`） | 52.871 × 40.555 | 点$p=(0,0),q=(4,0),r=(3,3)$在$d_1,d_2,d_\infty$下的距离读数（6、$3\sqrt2$、3；到$q$都为4）。 |
| c1-pseudometric-quotient | 01-metric-spaces/01-metrics.tex（`fig:metric-pseudometric-quotient`） | 104.916 × 44.598 | 横坐标伪度量的竖直线等价类及商化为实轴，$\bar p([0],[2])=2$。 |
| c1-unit-balls | 01-metric-spaces/02-open-closed-sets.tex（`fig:metric-unit-balls`） | 48.055 × 48.426 | $\mathbb R^2$中$d_1$菱形、$d_2$圆盘、$d_\infty$正方形单位开球的嵌套。 |
| c1-relative-ball | 01-metric-spaces/02-open-closed-sets.tex（`fig:metric-relative-ball`） | 91.934 × 25.199 | $A=[0,1]$中相对球$B_A(0,1/2)=[0,1/2)$等于环境球$(-1/2,1/2)$与$A$之交。 |
| c1-interior-closure-boundary | 01-metric-spaces/02-open-closed-sets.tex（`fig:metric-interior-closure-boundary`） | 68.104 × 34.466 | 内点、边界点与闭包外点各自的球与集合$A$的关系。 |
| c1-rational-cauchy | 01-metric-spaces/03-convergence-completeness.tex（`fig:metric-rational-cauchy`） | 76.616 × 33.539 | $\sqrt2$十进制截断在$\mathbb Q$中聚拢到空缺$\sqrt2$，含$[1.41,1.42]$放大。 |
| c1-epsilon-net | 01-metric-spaces/04-compactness.tex（`fig:metric-epsilon-net`） | 93.169 × 51.234 | $[0,1]^2$在$d_\infty$下$\varepsilon=1/2$（4点）与$\varepsilon=1/4$（9点）的有限网。 |
| c1-open-cover | 01-metric-spaces/04-compactness.tex（`fig:metric-open-cover-interval`） | 93.105 × 31.291 | $(0,1)$的开覆盖$U_n=(1/n,1)$无有限子覆盖，有限并留下缺口$(0,1/8]$。 |
| c1-uniform-continuity | 01-metric-spaces/05-continuous-maps.tex（`fig:metric-uniform-continuity`，figure*） | 116.695 × 52.927 | (a)$x^2$在$a=1,3$处$\varepsilon=1$的容差0.414与0.162；(b)$\sqrt x$过原点割线斜率1、2、4无界。 |
| c1-bilipschitz-homeo | 01-metric-spaces/06-comparison.tex（`fig:metric-bilipschitz-homeo`，figure*） | 123.261 × 60.113 | (a)$d_2\leq d_1\leq\sqrt2d_2$的楔形；(b)logit把柯西列$1/(n+1)$拉成$-\ln n$。 |
| c1-contraction | 01-metric-spaces/07-contraction.tex（`fig:metric-contraction`，figure*） | 112.691 × 53.153 | $T(x)=x/2+1$的蛛网图，以及精确迭代与每步误差0.1迭代的误差曲线（趋向界0.2）。 |
| c2-count-length | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/01-size-and-additivity.tex（fig:measure-count-length） | 107.6 × 36.2 | 五点加权计数分组与 $[0,2)\cup[3,4)$ 两种区间分割的共同细分，均满足不交相加。 |
| c2-jordan-rationals | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/01-size-and-additivity.tex（fig:measure-jordan-rationals） | 107.8 × 41.8 | $[0,1]$ 有理点的有限覆盖（总长≥1）与长度 $\varepsilon2^{-k}$ 的可数覆盖（$\varepsilon=0.4$）。 |
| c2-sigma-algebra-partition | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/02-measure-spaces.tex（fig:measure-partition-sigma） | 97.3 × 31.0 | 四点集合按两组、三组、四组分组生成的 $\sigma$ 代数，分别含 4、8、16 个集合。 |
| c2-open-set-components | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/02-measure-spaces.tex（fig:measure-open-set-components） | 98.4 × 38.3 | 开集 $(0,1)\cup(1,2)\cup(2.5,4)$ 的重叠有理端点区间表示与三个不交分量（选有理数 1/2、3/2、3）。 |
| c2-outer-cover | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/03-construction.tex（fig:measure-outer-cover） | 103.7 × 21.2 | $[0,1]\cup\{2-2^{-k}\}$ 的开区间覆盖，总长 1.2+0.2=1.4，外测度为 1。 |
| c2-cantor-set | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/03-construction.tex（fig:measure-cantor-set） | 104.1 × 34.3 | Cantor 集构造 $C_0$–$C_3$，总长 $1,2/3,4/9,8/27$，标注三进制位 0/2。 |
| c2-inner-outer-approx | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/03-construction.tex（fig:measure-inner-outer-approx） | 105.3 × 34.2 | $E=[0,1]\setminus\{1/2\}$ 的开集外逼近（差 0.1）与紧集内逼近（差 0.2）。 |
| c2-stieltjes-jump | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/03-construction.tex（fig:measure-stieltjes-jump） | 96.5 × 43.0 | 斜率 1/2 再在 1 处跳跃 1/2 的右连续 $F$，$\mu_F((0.5,1])=0.75$。 |
| c2-preimage-criterion | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/04-measurable-maps.tex（fig:measure-preimage-criterion） | 105.1 × 39.1 | 半直线 $(a,\infty)$、$(b,\infty)$ 的嵌套原像，$(a,b]$ 的原像为二者之差。 |
| c2-pushforward-merge | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/05-pushforward.tex（fig:measure-pushforward-merge） | 105.1 × 43.9 | 四点权重经多对一映射合并为 0.4、0.6；$\lambda|_{[0,1]}$ 经 $\lfloor2x\rfloor$ 推前为两个 1/2 点质量。 |
| c2-projection-marginal | tex/02-abstract-mathematics/01-metric-and-measure/02-measures/05-pushforward.tex（fig:measure-projection-marginal） | 100.9 × 51.3 | 三个平面点质量的两个边缘，以及单位正方形面积测度投影得到 $[0,1]$ 上的长度。 |
| c2-absolute-continuity | 02-measures/06-relations.tex | 100.669 × 38.28 | 两点空间与实轴两段长度上的绝对连续方向及单点检查的不足 |
| c2-absolute-continuity-blocks | 02-measures/06-relations.tex | 95.324 × 33.32 | 无限测度下小质量控制失败的二进分块反例 |
| c2-mutually-singular | 02-measures/06-relations.tex | 107.668 × 41.469 | 长度与点质量、两组交错稠密点质量的相互奇异 |
| c2-signed-weights | 02-measures/07-signed-measures.tex | 84.36 × 32.706 | 四点有符号权重的正负抵消 |
| c2-hahn-decomposition | 02-measures/07-signed-measures.tex | 84.06 × 44.665 | Hahn分解正区域的两种选择 |
| c2-jordan-decomposition | 02-measures/07-signed-measures.tex | 101.745 × 38.689 | Jordan分解与重叠的非极小差表示 |
| c2-total-variation-partition | 02-measures/07-signed-measures.tex | 75.128 × 42.954 | 三种分割下的绝对值之和与总变差 |
| c2-lebesgue-decomposition | 02-measures/08-decompositions.tex | 85.672 × 32.187 | 同一测度相对不同参考测度的Lebesgue分解 |
| c2-cantor-function | 02-measures/08-decompositions.tex | 58.815 × 50.652 | Cantor函数的分段线性近似F_1、F_2、F_7 |
| c2-cantor-mass-length | 02-measures/08-decompositions.tex | 84.691 × 37.871 | C_n的长度(2/3)^n与Cantor测度质量1的对比 |
| c2-three-part-decomposition | 02-measures/08-decompositions.tex | 88.999 × 44.065 | 离散、绝对连续、奇异连续三成分及其累计函数之和 |
| c3-simple-height-measure | 03-integration/01-definition（3.1.1） | 98.771 × 42.143 | 简单函数按层计算“高度×测度”，积分 2×1.5+0.5×1.5=3.75。 |
| c3-riemann-lebesgue-partitions | 03-integration/01-definition（3.1.2），3.3.2 文字回引 | 104.881 × 40.372 | 对 f=1+0.8 sin 2x 比较按自变量分割与按函数值分层，层 {f≥1.5} 为两段区间。 |
| c3-dyadic-approximation | 03-integration/01-definition（3.1.2） | 102.634 × 46.355 | x² 在 [0,2] 上的二进分层逼近 s₁、s₂，含截断高度。 |
| c3-positive-negative-parts | 03-integration/01-definition（3.1.2） | 100.034 × 35.574 | sin x 的正部与负部。 |
| c3-signed-measure-masses | 03-integration/01-definition（3.1.5） | 107.692 × 41.921 | η=2δa−3δb+δc 上的质量柱与逐点贡献表，∫f dη=−8，∫|f|d|η|=12。 |
| c3-monotone-convergence-sets | 03-integration/02-basic-properties（3.2.1） | 68.273 × 49.579 | 单调收敛定理证明中 E_n={f_n≥cs}=[0.72ⁿ,1] 递增覆盖 (0,1]。 |
| c3-counting-measure-series | 03-integration/03-classical-integrals（3.3.1） | 99.24 × 38.947 | 计数测度下 f(k)=2^{-k} 的积分即级数，截断积分 1−2^{-N}→1。 |
| c3-dirichlet-function | 03-integration/03-classical-integrals（3.3.2） | 105.876 × 36.16 | Dirichlet 函数处处不连续与 Cantor 集示性函数不连续点零测的对照。 |
| c3-sinc-improper | 03-integration/03-classical-integrals（3.3.3） | 101.699 × 26.035 | sin x/x 正负瓣交替，反常积分条件收敛而不 Lebesgue 可积。 |
| c3-escaping-mass | 03-integration/04-limits（3.4.2，3.4.5） | 96.629 × 34.353 | 平移 1_[n,n+1] 与摊平 n⁻¹1_[0,n] 两种积分质量丢失。 |
| c3-dominating-envelope | 03-integration/04-limits（3.4.3） | 96.633 × 41.215 | x^n 受可积常数控制；n1_(0,1/n) 的上包络 ≥1/x−1 不可积。 |
| c3-product-rectangles | 03-integration/05-iterated-integrals.tex（3.5.1，fig:integral-product-rectangles） | 85.930 × 41.099 | 两块组成的可测矩形$A\times B$，以及四分之一圆盘由两层网格矩形不交并内逼近。 |
| c3-sections | 03-integration/05-iterated-integrals.tex（3.5.1，fig:integral-sections） | 60.187 × 35.391 | 区域$0.2\le y\le1.2+0.8\cos(\pi x/2)$在$x_0=1$处的竖直截面与$y_0=1$处由两段区间组成的水平截面。 |
| c3-fubini-counterexample | 03-integration/05-iterated-integrals.tex（3.5.3，fig:integral-fubini-counterexample） | 59.951 × 50.860 | 无穷矩阵$a_{i,j}=\mathbf 1\{j=i\}-\mathbf 1\{j=i+1\}$左上角，行和全为0，第一列和为1。 |
| c3-layer-cake | 03-integration/05-iterated-integrals.tex（3.5.4，fig:integral-layer-cake） | 88.149 × 39.994 | $f=e^{-x}$图像下区域的竖切（长$f(x_0)$）与横切（超水平集$\{f>t_0\}$）。 |
| c3-pushforward-change | 03-integration/06-change-of-variables.tex（3.6.1，fig:integral-pushforward-change） | 75.812 × 39.920 | 四点质量$k/10$经多对一映射汇成$0.6,0.4$，两种算法都得$3.8$。 |
| c3-jacobian-cell | 03-integration/06-change-of-variables.tex（3.6.2，fig:integral-jacobian-cell） | 74.701 × 34.939 | 单位正方形经$\bm A=[[1.5,0.5],[0.5,1]]$映成面积$1.25$的平行四边形。 |
| c3-branch-inverse | 03-integration/06-change-of-variables.tex（3.6.3，fig:integral-branch-inverse） | 61.330 × 45.685 | $x^2$在$(-1,1)$上的两个可逆分支，水平线$y_0$有两个原像$\pm\sqrt{y_0}$。 |
| c3-parameter-continuity | 03-integration/07-parametric-integrals.tex（3.7.1，fig:integral-parameter-continuity） | 102.807 × 53.982 | $te^{-tx}$（$t=2,1,0.5,0.25$）的质量向右逃逸及不可积包络$1/(ex)$。 |
| c3-absolute-continuity-intervals | 03-integration/08-integration-and-differentiation.tex（3.8.1，fig:integral-absolute-continuity-intervals） | 81.933 × 39.254 | $\sqrt x$上四段不交区间（总长1.2）及其增量（总和约0.562）。 |
| c3-vitali-cover | 03-integration/08-integration-and-differentiation.tex（3.8.2，fig:integral-vitali-cover） | 76.616 × 22.768 | Vitali选择中与$I_1$相交的未选区间落入五倍放大区间$5I_1$。 |
| c3-cantor-function | 03-integration/08-integration-and-differentiation.tex（3.8.5，fig:integral-cantor-function） | 103.847 × 53.132 | Cantor函数的分段线性逼近$c_1,c_2,c_6$及第二步四个保留区间（总长4/9、增量和1）。 |
| c4-mass-ratio | 04-densities-and-change-of-measure/01-relative-density.tex（`fig:density-mass-ratio`） | 96.651 × 56.473 | 三点集上目标质量(0.2,0.5,0.3)相对计数测度与权重(2,1,1)两种参考的密度。 |
| c4-weighted-measure | 04-densities-and-change-of-measure/01-relative-density.tex（`fig:density-weighted-measure`） | 106.684 × 53.647 | 阶梯密度产生的测度（A=[1/4,3/4]质量1/2）及在零测点上改动密度不改变测度。 |
| c4-rn-candidate | 04-densities-and-change-of-measure/02-existence.tex（`fig:density-rn-candidate`） | 98.771 × 46.870 | Radon–Nikodym证明第三步：候选h、剩余质量r与在Hahn正集P上加高ε。 |
| c4-lebesgue-density | 04-densities-and-change-of-measure/02-existence.tex（`fig:density-lebesgue-form`） | 94.365 × 41.416 | ν=½λ+¼δ_{1/2}+¼μ_C中只有绝对连续部分由密度1/2表示。 |
| c4-counting-counterexample | 04-densities-and-change-of-measure/02-existence.tex（`fig:density-counting-counterexample`） | 107.636 × 36.851 | 不σ有限的计数测度作参考时长度测度没有密度。 |
| c4-mixed-reference | 04-densities-and-change-of-measure/03-rules.tex（`fig:density-mixed-reference`） | 108.433 × 41.815 | 共同参考μ=λ\|[0,1]+δ_0下混合测度¾λ+¼δ_0的密度。 |
| c4-chain-rule | 04-densities-and-change-of-measure/03-rules.tex（`fig:density-chain-rule`） | 85.651 × 35.754 | ρ→μ→ν的密度相乘，数值例2x·(3/2)x=3x²。 |
| c4-one-sided-loss | 04-densities-and-change-of-measure/03-rules.tex（`fig:density-one-sided-loss`） | 73.914 × 33.927 | 仅单向绝对连续时密度1_[0,1]在(1,2]为零，不能取倒数。 |
| c4-discrete-density | 04-densities-and-change-of-measure/04-computation.tex（`fig:density-discrete`） | 104.712 × 41.561 | 几何参考质量与Poisson目标质量及其比值密度。 |
| c4-increment-measure | 04-densities-and-change-of-measure/04-computation.tex（`fig:density-increment`） | 85.425 × 58.388 | F=x/2+¼·1_[1/2,1]+¼C的图像：斜率、跳跃与Cantor台阶三部分（坐标由同目录sample_cantor.py生成）。 |
| c4-square-branches | 04-densities-and-change-of-measure/04-computation.tex（`fig:density-square-branches`） | 110.144 × 48.084 | 均匀分布经x²推前：两分支原像与输出密度1/(2√y)，B=[0.36,0.49]质量0.1。 |
