# 卷2《向量、矩阵与多元微积分》：线性方程与优化大纲

所属：卷二《向量、矩阵与多元微积分》第三部分“线性方程与优化”，第11—19章。正文入口：[part.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/part.tex)。本提要依据实际接入的九章正文组织。

本部分研究反向的线性问题：给定矩阵与希望的输出，求输入向量，或在结构约束下求一张矩阵。第11章确定选解目标（精确解、最小二乘解、最小范数代表、伪逆，以及加权与齐次变形）和相应的检验条件；第12—16章分别给出直接分解（线性方程与最小二乘各一章）、定常迭代、Krylov子空间与行列投影四类计算路线；第17章区分问题敏感性、算法误差与提前停止误差，用正则化与谱截断改变目标，并在同一目标下比较方法；第18章把未知量换成矩阵，在秩、加权或正交约束下求最佳逼近；第19章研究Sylvester与Lyapunov矩阵方程。主要依赖第一部分的列空间、零空间、秩与正交投影，以及第二部分的谱分解、SVD、极分解、条件数与矩阵幂。

## 部分导读

正文入口：[part.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/part.tex)中的 `\BookPartGuide`（不编号的阅读指引，不计入章数）。

1. 从前两部分以正向计算为主进入，说明本部分转向已知矩阵与输出、反求输入向量或在约束下求矩阵的问题；列出所依赖的第一部分（列空间、零空间、秩、正交投影）与第二部分（谱分解、SVD、极分解、条件数、矩阵幂）工具，并说明不依赖多元微分或一般优化理论。

2. 说明第11—17章围绕线性方程依次回答四个问题，先介绍第11章：相容时保留全部精确解，不相容时求最小二乘解，多解时取最小范数代表，伪逆统一这些情形并给出各目标的核对条件。

3. 说明第12—16章的四类计算路线：直接分解在有限步内求解（线性方程用LU、Cholesky与分块LDL，最小二乘用正规方程、QR与SVD，各成一章），定常迭代用易解分裂反复修正，Krylov子空间法在扩大的子空间中按残差准则选取近似，行列投影法每步只读一行或一列；各算法均按主要思想、算法实现与算法分析展开，并用原始数据核验输出。

4. 说明第17章区分问题敏感性、有限精度算法误差与提前停止误差，用正则化或谱截断主动改变目标，并在同一目标与精度下比较总成本。

5. 说明第18、19章把未知量换成矩阵：矩阵逼近一章由Rayleigh商与迹极值得到截断SVD的最优性，再讨论加权、正交与旋转约束；矩阵方程一章给出Sylvester与Lyapunov方程的谱条件、Schur求解与离散型级数解，连续型正定解的积分证明留给后续演化理论。

6. 列出阅读时需要区分的对象：原残差、正规残差与行空间三种验收条件；拟合值唯一与系数唯一；迭代步数与达到同一精度的总成本；问题病态与算法不稳定；正则化改变问题本身；第17章为稳定求解截断取逆与第18章把截断矩阵作为近似对象的区别。

## 第11章 线性方程与最小二乘的选解

正文入口：[01-solution-selection.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/01-solution-selection.tex)。

1. 从正向计算转到反求输入：以三个时刻观测直线变化量、反推截距与斜率为例，指出观测可能恰好共线、互相矛盾，或因参数重复而对应无穷多组系数，由此提出本章问题：对$\bm A\bm x=\bm b$，每种情况下要求什么样的解。
2. 说明各节分工：先判断有无解、有几个解；无解时取最小二乘解，多解时取欧氏范数最小者；因为有限维最小二乘总有解且最小范数代表唯一，所以伪逆能统一各种情形；再说明加权与齐次两种变形改变目标的哪一部分，最后把目标写成可核对的条件。
3. 交代依赖：列空间、零空间、秩与秩零度定理来自第2章，正交分解、正交投影与Gram因子来自第3章，奇异值分解来自第7章；结论只靠正交分解和代数恒等式，不需要多元微分或一般优化。本章只讨论目标的定义、存在唯一性与最优性，算法从第12章开始。
4. 给出本部分线性方程各章共用的记号约定：已知$\bm A\in\mathbb R^{m\times d}$、$\bm b\in\mathbb R^m$，未知$\bm x\in\mathbb R^d$，方阵取$m=d$；$\bm x_\star$表示精确解或选定的最小范数解，$\hat{\bm x}$表示最小二乘解，$\bm x_k$表示迭代近似，$\bm r_k=\bm b-\bm A\bm x_k$表示残差；多右端写成$\bm A\bm X=\bm B$，逐列求解并共用分解。
5. 区分输入、参数与中间量：求解过程以$\bm A,\bm b$为输入、以$\bm x$为输出；初值、容差、步数上限、松弛参数、权矩阵和预条件是方法参数；分解因子、残差、子空间坐标和搜索方向是中间量，最后要换回$\bm x$。Sylvester方程的系数角色留到第19章说明。

### 11.1 方程的相容性与解集

1. 把$\bm A\bm x$写成列的组合，说明方程问的是能否用列组合出$\bm b$及组合系数是什么；输出取遍列空间，故有解当且仅当$\bm b\in\operatorname{range}(\bm A)$，定义相容。
2. 用增广矩阵把相容条件化为秩判据：$\bm b$已在列空间中则添列不增秩，否则秩恰加一，得到$\operatorname{rank}[\bm A\;\bm b]=\operatorname{rank}\bm A$。强调方程数与未知量数不能单独决定相容性：两条相同方程$x=1$多于未知量却有唯一解，方程$x_1+x_2=1$与$x_1+x_2=2$个数等于未知量数却无解。
3. 指出相容后解的个数由零空间决定：两解之差在$\ker\bm A$中，核向量加到解上不改变输出，由此引出三分法定理。
4. 定理“线性方程的三种情况”：设$r=\operatorname{rank}\bm A$、$\tilde r=\operatorname{rank}[\bm A\;\bm b]$，$\tilde r=r=d$唯一解，$\tilde r=r<d$无穷多解，$\tilde r>r$无解。证明先由添一列至多增一维得$\tilde r\in\{r,r+1\}$，再用相容判据与秩零度定理$\dim\ker\bm A=d-r$区分唯一与无穷多。
5. 回顾第2章的满列秩与满行秩，说明前者只保证至多一解（例$\bm A=(1,1)^\top$），后者只保证每个右端有解（例$\bm A=(1,1)$，解沿$(1,-1)^\top$平移），方阵满秩时两者同时成立即可逆。随后给出方阵可逆当且仅当$\det\bm A\neq0$及伴随公式$\bm A^{-1}=\operatorname{adj}(\bm A)/\det\bm A$，由行列式乘法性和古典伴随恒等式证明两个方向，并说明实际计算用消元读秩而不展开行列式。
6. 预告用同一个拟合问题依次产生三种情况，并在本章后面反复使用。
7. 示例“直线观测中的三种情况”第一段：在$t=0,1,2$观测$a+st$，系数矩阵为常数列与时刻列；$\bm b=(1,2,3)^\top$时满列秩，唯一解$(1,1)^\top$。
8. 示例第二段：复制常数列得到$\widetilde{\bm A}$，方程只约束$x_1+x_3=1$、$x_2=1$，秩$2<3$，有无穷多解。
9. 示例第三段：保留两列而把观测改为$(1,2,2)^\top$，前两式给出$a=s=1$，第三式要求$3=2$；$\det[\bm A\;\bm b]=-1$，$\tilde r=3>r=2$，无解，留待最小二乘处理。
10. 给出相容时的完整解集$\bm x_p+\ker\bm A$，称为仿射空间，自由度为$d-r$；核为零退化为唯一解，核非零给出仿射解集，并指向以$\bm A=(1,1)$画出的零空间纤维图。
11. 在复制常数列的例子中算出特解$(1,1,0)^\top$与核方向$(1,0,-1)^\top$，得到全部解$(1+t,1,-t)^\top$，逐分量代回验证对每个$t$都等于$\bm b$；说明自由参数对应常数项在两相同列间的拆法，计算过程留给第12章的消元与分解。
12. 图“同一输出对应的整组输入”：对$\bm A=(1,1)$画出$x_1+x_2=1,0,-1$三条平行直线及其输出，绿色直线是$\ker\bm A$，其余是其平移，说明整条直线才与可达输出一一对应。

### 11.2 最小二乘解

1. $\bm b$不在列空间时改求残差平方最小，定义最小二乘问题；区分系数、拟合值与残差三个对象，说明目标只通过拟合值依赖系数，因此先求列空间中离$\bm b$最近的点，即子空间最近点问题。
2. 由正交分解把$\bm b$唯一写成$\hat{\bm b}+\bm e$，对列空间中任一点$\bm u$用勾股关系得$\lVert\bm b-\bm u\rVert_2^2=\lVert\hat{\bm b}-\bm u\rVert_2^2+\lVert\bm e\rVert_2^2$，等号当且仅当$\bm u=\hat{\bm b}$；结论是最优拟合值唯一，且由残差与列空间正交完全刻画，并指向直线子空间上的最近点图。
3. 图“子空间最近点”：方向$(2,1)$的直线上离$(1,3)^\top$最近的点为$(2,1)^\top$，误差$(-1,2)^\top$与直线垂直，另一候选$(4,2)^\top$距离$\sqrt{10}$大于最短距离$\sqrt5$。
4. 残差与每列正交合写为$\bm A^\top\bm r=\bm0$，代入得正规方程$\bm A^\top\bm A\hat{\bm x}=\bm A^\top\bm b$，解释“正规”指法向；说明最小二乘解等价于满足正规方程，不需要梯度或一般最优化条件，并把$\bm A^\top\bm r$称为正规残差。
5. 把拟合值写成投影：用列空间的标准正交基得$\bm P=\bm Q_1\bm Q_1^\top$，满列秩时由正规方程得$\bm P=\bm A(\bm A^\top\bm A)^{-1}\bm A^\top$；解释对称与幂等的几何含义，并说明实际求解不必形成这个$m\times m$矩阵。
6. 引出把最优性、存在性与唯一性合在一起的定理，作为后续算法的正确性依据。
7. 定理“最小二乘解的刻画”及证明：最优等价于$\bm A\hat{\bm x}=\bm P\bm b$，又等价于正规方程；$\bm P\bm b$在列空间中故解存在；由$\bm x^\top\bm A^\top\bm A\bm x=\lVert\bm A\bm x\rVert_2^2$得$\ker(\bm A^\top\bm A)=\ker\bm A$，解集为特解加核，唯一当且仅当满列秩，此时$\bm A^\top\bm A$正定。
8. 归纳两层唯一性：拟合值总唯一，系数只在满列秩时唯一；相容方程是残差为零的特例。
9. 示例“三条不相容观测的最佳折中”第一段：对$\bm b=(1,2,2)^\top$列出正规方程，解得$\hat{\bm x}=(7/6,1/2)^\top$与残差$(-1/6,1/3,-1/6)^\top$，逐项验证$\bm A^\top\bm r=\bm0$，残差平方和为$1/6$。
10. 示例第二段：解释中间观测高于拟合直线、两端低于它的折中含义；对相容观测$(1,2,3)^\top$同一正规方程给出零残差解，说明精确求解是同一目标的特例。
11. 转向系数稳定性：满列秩只保证唯一，不保证稳定，引出近共线设计。
12. 示例“近共线设计”：两列为$\bm c$与$\bm c+\varepsilon\bm q$、观测$\bm c+\delta\bm q$，$\varepsilon\neq0$时系数$(1-\delta/\varepsilon,\delta/\varepsilon)^\top$精确拟合，$\varepsilon=0$时残差跳为$\delta\bm q$且系数满足$w_1+w_2=1$的都是解。
13. 对照三个对象：$\varepsilon\to0$时拟合值突变、系数趋于无穷并对数据极敏感，说明这是几何性质而非舍入造成，量化留给第17章。

### 11.3 最小范数解

1. 秩亏时最小二乘解集含无穷多点，需要额外选解条件，定义最小范数解；用$\mathbb R^d=\operatorname{range}(\bm A^\top)\oplus\ker\bm A$说明核分量不影响拟合却增加长度。
2. 定理“最小范数代表”及证明：把解分为行空间分量与核分量，去掉核分量仍为解；两解行空间分量之差同时属于行空间与核，只能为零，故全部解共享同一$\bm x_\star$；勾股关系给出唯一最小。相容和唯一可解是特例。
3. 区分三层确定性：拟合值由$\bm b$与列空间唯一决定，系数只在满列秩时由拟合值决定，秩亏时的唯一性来自额外选解条件；指出选解依据是给定的欧氏范数，换范数一般换点。
4. 满行秩时把“落在行空间”写成$\bm x=\bm A^\top\bm w$，代入得$\bm A\bm A^\top\bm w=\bm b$。
5. 定理“满行秩时的最小范数解”及证明：由$\ker(\bm A\bm A^\top)=\ker\bm A^\top=\{\bm0\}$得可逆，$\bm x_\star=\bm A^\top(\bm A\bm A^\top)^{-1}\bm b$满足方程且在行空间中，故为最小范数解。
6. 解释解是行的组合，计算上形成Gram矩阵还是作QR留到第13章比较；两个满秩公式都不适用时，转入下一节的一般秩公式。

补充图解：最小范数代表的几何意义。示例为$\bm A=(1,2)$、$b=7$，蓝线是全部精确解，绿色虚线是行空间；$\bm x_\star=(7/5,14/5)^\top$与核方向正交。黄色箭头$\bm z\in\ker\bm A$把$\bm x_\star$移到另一解$\bm x$，不改变输出，却增加向量的长度。

### 11.4 伪逆与解的表示

1. 回顾前三节的处理方式，指出一般矩阵既不满列秩也不满行秩，两种选择都要作；预告沿奇异方向“可恢复方向取逆、其余置零”的构造，以及用Penrose条件和两个正交投影说明它不依赖分解选取。

#### 11.4.1 伪逆的构造

1. 写出秩$r$的奇异值分解并扩充为两组标准正交基，说明$\bm A$把$\bm v_i$送到$\sigma_i\bm u_i$，反向应把$\bm u_i$送回$\bm v_i/\sigma_i$。
2. 把$\bm b$按$\bm u_i$展开，区分三类分量的去向：$i\leq r$的分量配给$\bm v_i/\sigma_i$，$i>r$的分量没有原像、留在残差里，零空间方向不分配分量。
3. 定义Moore–Penrose伪逆$\bm A^\dagger=\sum_{i\leq r}\sigma_i^{-1}\bm v_i\bm u_i^\top$，并规定$\bm0^\dagger=\bm0$。
4. 引出伪逆同时完成最小二乘与最小范数两次选择的定理。
5. 定理“伪逆给出最小范数最小二乘解”及证明：用坐标$b_i=\bm u_i^\top\bm b$、$c_i=\bm v_i^\top\bm x$把残差平方写成$\sum_{i\leq r}(\sigma_ic_i-b_i)^2+\sum_{i>r}b_i^2$，最优当且仅当$c_i=b_i/\sigma_i$而其余坐标任取；$\bm A^\dagger\bm b$与核正交，故为最小范数解。
6. 说明前面公式都是特例：满列秩时$\bm A^\dagger=(\bm A^\top\bm A)^{-1}\bm A^\top$，满行秩时$\bm A^\dagger=\bm A^\top(\bm A\bm A^\top)^{-1}$，可逆时为$\bm A^{-1}$；一般秩只有和式可用。
7. 说明显式逆或伪逆只是数学表达，计算时让分解因子依次作用于右端，步骤见第13章的SVD求解。
8. 示例“复制常数列后的最小范数拟合”第一段：对$\widetilde{\bm A}$与$(1,2,2)^\top$，全部最小二乘解为$(7/6-t,1/2,t)^\top$，最小化范数平方得$t=7/12$，$\bm x_\star=(7/12,1/2,7/12)^\top$。
9. 示例第二段：验证$\bm x_\star$与核方向$(1,0,-1)^\top$正交，解释最小范数把常数项平均分给两个相同的列。

#### 11.4.2 Penrose条件与正交投影

1. 指出奇异向量不唯一（如重奇异值的子空间内可旋转），因此需要不提奇异向量又能唯一确定伪逆的条件。
2. 定理“Penrose条件”及证明：由和式算出$\bm A\bm A^\dagger=\sum_{i\leq r}\bm u_i\bm u_i^\top$、$\bm A^\dagger\bm A=\sum_{i\leq r}\bm v_i\bm v_i^\top$，验证四个条件；反过来由前两条得幂等、由后两条得对称，故$\bm A\bm G$、$\bm G\bm A$分别是到列空间与$(\ker\bm A)^\perp$的正交投影，由投影唯一性推出$\bm G=\bm A^\dagger$。
3. 解释四个条件：前两条是可恢复方向上的一致性，只有它们时投影可以是斜的；后两条的对称性对应“最近拟合值”和“最小范数系数”；条件不涉及奇异向量，所以伪逆不依赖分解选取。
4. 把两次选择写成可检查的等式：$\bm A\bm x_\star=\bm P\bm b$说明拟合值是投影，$\bm A^\dagger\bm A\bm x_\star=\bm x_\star$说明不含零空间分量。
5. 在复制常数列的示例中核验：$\widetilde{\bm A}\bm x_\star=(7/6,5/3,13/6)^\top$与最小二乘拟合值相同；$\bm x_\star$写成$\widetilde{\bm A}$两行的组合，已在行空间中。
6. 指出统一公式的代价：小正奇异值的倒数放大数据误差，量化留到第17章，本节只为后续计算方法确定目标。

### 11.5 加权最小二乘

图解保留两种投影及残差的几何关系，坐标、权矩阵和投影值集中置于图注。

1. 从观测可靠程度不同或误差相关引出，用对称正定$\bm M$定义加权最小二乘目标$(\bm A\bm x-\bm b)^\top\bm M(\bm A\bm x-\bm b)$。
2. 说明权矩阵怎样改变目标：对角权$\sum_im_ir_i^2$使大权观测的误差更昂贵、拟合值被拉向它，适合精度不同的观测；非对角元引入交叉项，例如$\bm M=\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$时残差$(1,1)^\top$代价为$2$、$(1,-1)^\top$代价为$6$，同向偏离被看得较轻，适合误差倾向一起偏移的情形；由统计性质选$\bm M$不在本章讨论。
3. 用Gram因子或正定平方根写$\bm M=\bm R^\top\bm R$，目标化为$\lVert\bm R\bm A\bm x-\bm R\bm b\rVert_2^2$，定义白化，并说明普通最小二乘的结论可以搬过来。
4. 定理“加权最小二乘解的刻画”及证明：对$\bm R\bm A$、$\bm R\bm b$应用最小二乘刻画得加权正规方程$\bm A^\top\bm M(\bm b-\bm A\hat{\bm x})=\bm0$，解集为特解加$\ker(\bm R\bm A)=\ker\bm A$，唯一当且仅当满列秩。
5. 解释加权正规方程即残差在$\bm M$内积下与列空间正交；权矩阵只改变误差度量；$\bm M$半正定时$\ker\bm M$中的残差不受惩罚，唯一性条件变为$\ker(\bm M\bm A)=\{\bm0\}$，拟合值也可能不唯一。
6. 满列秩时写出$\bm P_{\bm M}=\bm A(\bm A^\top\bm M\bm A)^{-1}\bm A^\top\bm M$，说明它幂等、一般不对称，是欧氏斜投影，但由双线性形式的对称性在$\bm M$内积下自伴，是该内积下的正交投影；同一数据换权矩阵最近点随之移动。
7. 说明白化只变换观测端，加权问题与白化后问题解集相同；秩亏时最小范数代表仍按原系数欧氏范数选取，即$(\bm R\bm A)^\dagger\bm R\bm b$，计算步骤见第13章。
8. 示例“同一直线上的两种最近点”：$\bm A=(1,1)^\top$、$\bm b=(2,1)^\top$，欧氏拟合值$(1.5,1.5)^\top$，$\bm M=\operatorname{diag}(1,4)$时为$(1.2,1.2)^\top$；加权残差$(0.8,-0.2)^\top$的欧氏内积为$0.6$而加权内积为零，说明正交性依赖所选内积。
9. 图“欧氏投影与加权投影”：并排画出同一直线上的两种投影与残差，提醒右图残差不必成欧氏直角。

### 11.6 齐次最小二乘

1. 引入只确定比例的模型$\bm A\bm h\approx\bm0$，以直线$h_1u+h_2v+h_3=0$拟合平面点为例，说明直接最小化总得到零向量，必须先固定尺度。
2. 比较两种归一化：固定$h_3=1$会排除过原点的直线，固定欧氏长度对各分量一视同仁，得到$\min_{\lVert\bm h\rVert_2=1}\lVert\bm A\bm h\rVert_2^2$；区分它与求$\ker\bm A$全部解的问题，并指出右端是$\bm A^\top\bm A$的二次型，可由第7章构造SVD所用的特征基求出。
3. 定理“齐次最小二乘的最优解”及证明：在$\bm A^\top\bm A$的标准正交特征基下$\bm h^\top\bm A^\top\bm A\bm h=\sum\lambda_ic_i^2\geq\lambda_{\min}$，取最小特征向量时等号成立；等号当且仅当$\bm h$在最小特征值的特征空间中；单重时只差符号；由$\ker\bm A=\ker(\bm A^\top\bm A)$，核非零时$\lambda_{\min}=0$。
4. 用$\bm A=[\,1\ -2\,]$核验：特征值$0$与$5$，最优单位向量$\pm(2,1)^\top/\sqrt5$，残差为零，比例$2:1$。
5. 换成奇异值语言：最优解是最小奇异值对应的右奇异方向，最小值为最小奇异值平方（$d>r$时补零）；同类长度约束极值在第18章推广为Rayleigh商的一般结论。
6. 指出最小特征值接近重根时最优方向对扰动敏感，由第9章子空间扰动界控制；具体用SVD选取单位向量的步骤见第13章。

### 11.7 解的检验条件

1. 说明算出候选解后要用与目标对应的条件核对，用错条件会误判；约定检验对象为候选解$\bm x$及原残差$\bm r=\bm b-\bm A\bm x$。
2. 精确方程检查原残差$\bm r=\bm0$，只对相容方程适用；相容性由秩判据判断，而不是由残差能否降到零来猜测。
3. 普通最小二乘检查正规残差$\bm A^\top\bm r=\bm0$并报告$\lVert\bm r\rVert_2$即$\bm b$到列空间的距离；不相容示例的残差范数为$1/\sqrt6$且正规残差为零，说明残差非零不是失败。
4. 最小范数解再检查行空间条件$\bm x\perp\ker\bm A$，等价于$\bm A^\dagger\bm A\bm x=\bm x$或$\bm x=\bm A^\top\bm w$；在秩亏示例中$(7/6-t,1/2,t)^\top$对每个$t$都满足正规残差为零，只要求最小二乘时都是合格答案，说明系数不唯一不是失败，只有$t=7/12$满足行空间条件。
5. 加权问题核对$\bm A^\top\bm M\bm r=\bm0$并报告加权残差范数与所用权矩阵，加权示例中欧氏正规残差为$0.6$并非错误；齐次拟合检查单位长度与最小特征方向，不能照搬正规残差条件。
6. 说明这些条件是后续算法的目标；浮点计算中“为零”要换成相对容限，容限及残差与误差的关系见第17章，直接法与迭代法的检验分别见第10、11、12章。

### 11.8 本章小结

1. 回应章首问题：相容当且仅当$\bm b\in\operatorname{range}(\bm A)$即增广秩不变，相容时解集为特解加$\ker\bm A$；方程与未知量个数不能单独决定情况，满列秩只保证至多一解，满行秩只保证有解。
2. 总结最小二乘：最优拟合值是列空间上的正交投影，总存在且唯一；系数为最小二乘解当且仅当正规残差为零，只在满列秩时唯一；近共线例子说明唯一不等于稳定。
3. 总结最小范数与伪逆：最小范数解唯一且是解集中唯一落在行空间中的点；$\bm A^\dagger\bm b$同时完成两次选择，Penrose条件唯一确定伪逆，两个乘积是到列空间与行空间的正交投影；小奇异值放大误差是统一公式的边界。
4. 总结两种变形：加权最小二乘经白化化为普通问题，最优条件为$\bm A^\top\bm M\bm r=\bm0$，最小范数仍按原系数欧氏范数；齐次最小二乘在单位长度约束下取最小奇异值的右奇异方向，不同于求核中全部解。
5. 汇总检验条件：精确方程看原残差，最小二乘看正规残差，最小范数再看行空间条件，加权与齐次按各自度量与约束检查；残差非零或系数不唯一都可能是正确结果；计算方法从第12章开始，误差下的可信程度在第17章讨论。

## 第12章 线性方程的直接求解

正文入口：[02-direct-methods.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/02-direct-methods.tex)（章标题、标签与章引言），依次接入[00-gaussian-elimination.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/02-direct-methods/00-gaussian-elimination.tex)（12.1）、[01-factorizations.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/02-direct-methods/01-factorizations.tex)（12.2—12.5）、[02-method-selection.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/02-direct-methods/02-method-selection.tex)（12.6）与[03-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/02-direct-methods/03-summary.tex)（12.7）。

1. 从第11章已经确定求解目标出发，指出非奇异方阵的精确解$\bm A^{-1}\bm b$只是表达式，先求逆再相乘多做运算；提出本章问题，即不求逆、在有限步内算出精确解，并让一次分解服务于多个右端；最小二乘的直接求解留给第13章。

2. 说明共同做法是用消元把方阵化为三角方程并逐分量代入；称这类方法为直接法，并与第14章起的迭代法对照。

3. 说明各节分工：12.1节用初等行变换讲清消元的手算过程；随后三节按矩阵结构选择LU、Cholesky与分块LDL；12.5节说明低秩修改下复用已有分解；最后一节按结构归纳方法选择与结果核验。

4. 列出依赖：三角分解存在性用到行列式，Cholesky用到正定矩阵；说明本章证明正确性、只给算法层面的稳定性结论（主元增长），系统误差分析在第17章。

5. 交代记号：非奇异$\bm A\in\mathbb R^{d\times d}$、$\bm b\in\mathbb R^d$，精确解$\bm x_\star$；算法以$\bm A,\bm b$为输入、以$\bm x$为输出，主元策略单独说明；多个右端写成$\bm A\bm X=\bm B$并共用一次分解。

6. 说明除12.1节外，每种算法分为主要思想、算法实现和算法分析三部分。

### 12.1 Gauss消元与阶梯形

1. 说明后面的分解都建立在消元之上，本节先在精确算术下把消元当作手算过程：用第1章的初等行变换化为阶梯形、读出解并求逆；记录因子与选主元从第12.2节开始。

#### 12.1.1 阶梯形与行最简形

1. 描述逐列寻找主元、必要时换行、消去下方元素并跳过无主元列的过程。

2. 定义行阶梯形（零行在底部、各行首个非零元依次右移）与行最简形（主元化为$1$并消去上方元素）。

3. 说明主元个数等于秩：各步行变换合为左乘可逆矩阵，不改变秩；阶梯形非零行线性无关，其秩等于非零行数；指出第11.1节用秩判断相容性时，实际就这样读秩。

#### 12.1.2 用消元解方程

1. 用增广矩阵$[\bm A\mid\bm b]$处理方程，每次对整行执行同一操作。

2. 说明三种行变换对应交换等式、等式乘非零数、把一个等式的倍数加到另一个等式，这些操作可撤销，故不改变解；化到阶梯形后主元列对应确定的未知量，无主元列对应自由变量。

3. 示例`ex:ls-elementary-row-reduction`演示首元为零时换行、消元，读出主元列、自由变量$x_3=t$与通解，并说明零行与矛盾行的含义。

4. 指出例中秩为$2$、比未知量个数少$1$，解集恰带一个自由参数，与第11.1节“特解加零空间、自由度为未知量个数减秩”的结论一致。

#### 12.1.3 用消元求逆

1. 由逆矩阵第$j$列是$\bm A\bm x=\bm e_j$的解，说明$n$个方程系数相同、消元步骤只由$\bm A$决定，可对$[\bm A\mid\bm I_n]$一并作行变换。

2. 回答右侧为什么是逆矩阵：若左侧化为$\bm I_n$，各步初等矩阵之积$\bm E$满足$\bm E\bm A=\bm I_n$且可逆，从而$\bm A\bm E=\bm I_n$，右侧的$\bm E$即$\bm A^{-1}$。

3. 说明找不到主元时左侧出现零行：若$\bm A$可逆则$\bm E\bm A$可逆，而有零行的矩阵左乘任何矩阵都保留零行，不能等于$\bm I_n$，故$\bm A$不可逆。

4. 指出只要一个方程的解时直接对$[\bm A\mid\bm b]$消元，先求逆再相乘多做运算。

### 12.2 LU分解

1. 说明一般非奇异方阵没有可利用的结构，基本做法是Gauss消元；本节把消元记录成两个三角因子，使求解化为两次三角代入，行交换避开零主元与小主元，因子可对多个右端复用。

#### 12.2.1 主要思想

1. 设$\bm A$为$d$阶非奇异方阵，求唯一精确解$\bm x_\star$；假设已得到LU分解$\bm P\bm A=\bm L\bm U$（$\bm P$置换、$\bm L$单位下三角、$\bm U$非奇异上三角），分解的计算留到下一小节。

2. 两边左乘$\bm P$只重排方程，记$\bm c=\bm P\bm b$得$\bm L\bm U\bm x=\bm c$；令$\bm y=\bm U\bm x$，拆成先解$\bm L\bm y=\bm c$、再解$\bm U\bm x=\bm y$两个三角方程。

###### paragraph：前代：求解$\bm L\bm y=\bm c$

1. 为供Cholesky复用，按一般下三角矩阵逐行列出方程组；由第一个方程得$y_1$，第二个方程移项得$y_2$，一般第$i$个方程移项除以$l_{i,i}$得前代公式$y_i=(c_i-\sum_{j<i}l_{i,j}y_j)/l_{i,i}$；说明按$i=1,\ldots,d$顺序计算，LU中$l_{i,i}=1$可省除法。

###### paragraph：回代：求解$\bm U\bm x=\bm y$

1. 由$\bm U$非奇异知对角元非零，逐行列出方程组；由最后一个方程得$x_d$，倒数第二个方程移项得$x_{d-1}$，一般第$i$个方程得回代公式$x_i=(y_i-\sum_{j>i}u_{i,j}x_j)/u_{i,i}$，按$i=d,\ldots,1$顺序计算。

2. 结合图说明前代自上而下、回代自下而上的依赖方向，后面各节直接调用二者，换右端只需重做两次代入。

3. 图：四阶下三角与上三角方程中计算$y_3$与$x_2$时所用元素与已算分量，标出除数与计算方向。

#### 12.2.2 算法实现

1. 说明输入$\bm A,\bm b$、输出$\bm x$与部分选主元规则（取绝对值最大者，平局取行号最小者），算法分为LU分解、前代、回代三个模块（各为一个小小节），并取$\bm A=\left[\begin{smallmatrix}1&3&4\\2&2&4\\1&2&5\end{smallmatrix}\right]$、$\bm b=(2,4,4)^\top$在每一步演示。

##### 12.2.2.1 LU分解

1. 说明计算中维护工作矩阵$\bm W$、乘子矩阵$\bm L$与置换$\bm P$，每一步后给出例中三者的当前值。

2. 第1步初始化$\bm W=\bm A$、$\bm L=\bm P=\bm I$、$k=1$，写出例中的三个矩阵。

3. 第2步选主元行$r=\arg\max_{k\leq i\leq d}|w_{i,k}|$，交换$\bm W$、$\bm P$及$\bm L$已存乘子的两行，主元为零时停止；例中$k=1$时$r=2$，写出交换后的$\bm W,\bm L,\bm P$。

4. 第3步由$w_{i,k}-l_{i,k}w_{k,k}=0$得乘子$l_{i,k}=w_{i,k}/w_{k,k}$与尾块更新$w_{i,j}\leftarrow w_{i,j}-l_{i,k}w_{k,j}$，乘子存入$\bm L$、$\bm P$不变；例中写出$k=1$消元后的$\bm W,\bm L,\bm P$。

5. 第4步判断是否结束：$k<d-1$时令$k\leftarrow k+1$回到第2步，$k=d-1$时所有列处理完毕；例中$k=2$无需交换、乘子$\tfrac12$，写出结束时的$\bm W,\bm L,\bm P$。

6. 第5步取出因子：结束时$\bm W$对角线下方全为零，取$\bm U=\bm W$，$\bm L$与$\bm P$即为所求；例中验证$\bm L\bm U=\bm P\bm A$。

7. 指出上面的演示只在首轮换行，引出检查LU分解第2步“已存乘子随行交换”规则的第二个例子。

8. 示例（第二轮换行时交换已存乘子）：$\bm A=\left[\begin{smallmatrix}0&2&1\\1&1&0\\2&0&1\end{smallmatrix}\right]$、$\bm b=(3,2,3)^\top$；首轮把第三行换到首行，乘子$\tfrac12$与$0$，后两行变为$(0,1,-\tfrac12)$与$(0,2,1)$。

9. 次轮交换后两行并同时交换已存乘子，再以乘子$\tfrac12$消元得$\bm L$与$\bm U=\left[\begin{smallmatrix}2&0&1\\0&2&1\\0&0&-1\end{smallmatrix}\right]$；逐行核对$\bm L\bm U=\bm P\bm A$，并说明若忘记交换乘子，乘出的第二行$(1,2,\tfrac32)$不是$\bm P\bm A$的任一行。

10. 右端经两次交换为$(3,3,2)^\top$，前代得$\bm y=(3,3,-1)^\top$，回代得$\bm x=(1,1,1)^\top$，代回原方程核验。

##### 12.2.2.2 前代

1. 重排右端$\bm c=\bm P\bm b$，再根据前代公式（$l_{i,i}=1$）对$i=1,\ldots,d$得$y_i=c_i-\sum_{j<i}l_{i,j}y_j$；例中$\bm c=(4,2,4)^\top$，逐个算出$\bm y=(4,0,2)^\top$。

##### 12.2.2.3 回代

1. 根据回代公式对$i=d,\ldots,1$得$x_i=(y_i-\sum_{j>i}u_{i,j}x_j)/u_{i,i}$，例中逐个算出$\bm x=(1,-1,1)^\top$。

2. 输出并检验，说明浮点实现报告缩放残差（含义见第17章），例中代回残差为零；指出LU分解只依赖$\bm A$，换右端只重做前代与回代。

#### 12.2.3 算法分析

###### paragraph：乘子与置换的拼合

1. 说明第3步的乘子为何恰好组成$\bm L$：把第$k$轮写成左乘$\bm M_k=\bm I-\bm\ell_k\bm e_k^\top$，由$\bm e_k^\top\bm\ell_k=0$验证$\bm M_k^{-1}=\bm I+\bm\ell_k\bm e_k^\top$；不交换时交叉项消失，得到$\bm L=\bm I+\sum_k\bm\ell_k\bm e_k^\top$。

2. 有行交换时，利用$\bm P_k\bm e_j=\bm e_j$（$j<k$）推出$\bm P_k\bm M_j=(\bm I-(\bm P_k\bm\ell_j)\bm e_j^\top)\bm P_k$，把置换逐个移到右侧得$\bm P\bm A=\bm L\bm U$，并由此解释第2步交换已存乘子的规则。

###### paragraph：正确性

1. 说明能否进行取决于主元非零，部分选主元对非奇异矩阵总能进行，不选主元需额外条件，引出定理。
2. 定理（LU分解的存在与唯一）：非奇异时部分选主元给出$\bm P\bm A=\bm L\bm U$且$|l_{i,j}|\leq1$；不选主元时分解存在当且仅当各顺序主子式非零，此时唯一。
3. 证明：（1）若第$k$列从第$k$行起全零则前$k$列线性相关、$\bm A$奇异，主元取最大故乘子不超过1，置换右移的推导给出分解；（2）由三角块乘法得$\det\bm A_k=\prod u_{i,i}$，反向用单位下三角消元保持顺序主子式并归纳得主元非零，唯一性由“单位下三角等于上三角只能是单位阵”得到。
4. 说明行交换只重排方程，故代入给出原方程的解；以$\left[\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right]$说明非奇异不保证不选主元可行。

###### paragraph：主元增长与数值敏感度

1. 说明选主元为有限精度服务：小主元产生大乘子与大元素，淹没原数据；定义增长因子$\rho$为消元中最大元素与$\bm A$最大元素之比，部分选主元使每轮元素至多翻倍，故$\rho\leq2^{d-1}$，上界可达但实际极少出现；后向误差与$\rho$成正比，误差界见第17章。

###### paragraph：计算代价

1. 第$k$步更新$(d-k)^2$个元素，分解约$\tfrac23d^3$次运算，每个右端约$2d^2$次，$s$个右端合计约$\tfrac23d^3+2sd^2$；稀疏情形引入填充概念，其多少取决于消元顺序。

### 12.3 Cholesky分解

1. 说明对称正定矩阵常见于正规方程、Hessian与协方差矩阵，利用对称性只构造一个三角因子、运算与存储减半，正定性保证每次开方和除法可进行。

补充图解：Cholesky分解的列依赖（四阶示意）。从左到右处理第1、2、3列，绿色为已完成列，黄色为当前先求的对角元，蓝色为随后求出的本列下方元素；空白的右下三角位置尚未计算，上三角位置恒为零。

#### 12.3.1 主要思想

1. 设$\bm A$实对称正定，定义Cholesky分解$\bm A=\bm L\bm L^\top$（$\bm L$对角元为正的下三角）；说明求解与LU相同，先前代解$\bm L\bm y=\bm b$再回代解$\bm L^\top\bm x=\bm y$，只是须保留除以$l_{i,i}$、$\bm L^\top$的元素取$l_{k,i}$，本小节只讲怎样算出$\bm L$。

###### paragraph：逐元素等式

1. 写出三阶$\bm A=\bm L\bm L^\top$的矩阵等式，由两行内积与三角结构得$a_{i,j}=\sum_{k\leq\min(i,j)}l_{i,k}l_{j,k}$，列出下三角的六个等式。

###### paragraph：逐列递推

1. 按列读取三阶等式：第一列得$l_{1,1}=\sqrt{a_{1,1}}$与$l_{2,1},l_{3,1}$，第二列移项得$l_{2,2}$与$l_{3,2}$，第三列得$l_{3,3}$，开方取正根。

2. 推广到第$j$列：先取$i=j$移项开方，再对$i>j$移项除以$l_{j,j}$，得逐列公式；说明空和、依赖方向、只读下三角与上三角自动成立，并把开方量为正的论证交给算法分析。

#### 12.3.2 算法实现

1. 说明输入、输出与$\bm L\bm L^\top$分解、前代、回代三个模块，取$\bm A=\left[\begin{smallmatrix}4&2&2\\2&5&3\\2&3&6\end{smallmatrix}\right]$、$\bm b=(8,10,11)^\top$在每一步演示。

##### 12.3.2.1 $\bm L\bm L^\top$分解

1. 说明逐列按逐列公式计算：先算开方量$\delta_j$并检查为正，开方得$l_{j,j}$，再算下方元素，处理完第$d$列后结束。

2. 例中按列列出$l_{1,1},l_{2,1},l_{3,1}$、$l_{2,2},l_{3,2}$与$l_{3,3}$的计算，得$\bm L=\left[\begin{smallmatrix}2&0&0\\1&2&0\\1&1&2\end{smallmatrix}\right]$并核对$\bm L\bm L^\top=\bm A$。

3. 说明$\delta_j\leq0$时停止并报告不正定或接近奇异，不取绝对值、不截零；对称不定改用分块LDL，半正定或秩亏按目标改用SVD求解或第17章的正则化。

##### 12.3.2.2 前代

1. 根据前代公式对$i=1,\ldots,d$计算$y_i=(b_i-\sum_{k<i}l_{i,k}y_k)/l_{i,i}$；例中逐个算出$\bm y=(4,3,2)^\top$。

##### 12.3.2.3 回代

1. 根据回代公式取$\bm L^\top$的元素$l_{k,i}$，对$i=d,\ldots,1$计算$x_i$；例中逐个算出$\bm x=(1,1,1)^\top$。

2. 用原始数据检验残差为零，说明程序只存下三角因子，换右端只重做前代与回代。

#### 12.3.3 算法分析

###### paragraph：开方量为什么为正

1. 记左上角$j-1$阶块$\bm B=\bm L_{j-1}\bm L_{j-1}^\top$与其上方列$\bm c$，由$\bm L_{j-1}\bm\ell=\bm c$推出已算平方和等于$\bm c^\top\bm B^{-1}\bm c$，故开方量是Schur补$a_{j,j}-\bm c^\top\bm B^{-1}\bm c$；代入向量$(-\bm B^{-1}\bm c,1,0,\ldots)$的二次型说明它严格为正，正定性因而在每一列被实际使用。

###### paragraph：正确性

1. 说明定理进一步表明正定性也是分解存在的必要条件。
2. 定理（Cholesky分解的存在与唯一）：对称矩阵存在正对角下三角因子当且仅当正定，此时因子唯一且由逐列公式给出。
3. 证明：必要性由$\bm v^\top\bm A\bm v=\lVert\bm L^\top\bm v\rVert^2$；充分性按首行首列分块并对首变量配方，证明剩余Schur补仍正定后归纳；唯一性由逐列公式逐个确定元素。
4. 由分解直接验证所得$\bm x$满足$\bm A\bm x=\bm b$。

###### paragraph：数值敏感度

1. 由$a_{j,j}=\sum_kl_{j,k}^2$得因子元素不增长，故不选主元也后向稳定，解的误差仍由条件数决定；区分数学正定与有限精度可计算性：最小特征值相对很小时开方量可能被舍入算成非正，失败提示接近奇异，处理属于第17章。

###### paragraph：计算代价

1. 分解约$\tfrac13d^3$次运算、只存一个三角因子，每个右端约$2d^2$次。

### 12.4 分块LDL分解

1. 以带约束二次问题的鞍点系统为例说明对称不定矩阵的需要：Cholesky开方量可能为负，LU又浪费对称性；分块LDL不开方并在必要时用二阶主元块，同时保留对称结构与可解性。

补充图解：标量主元与二阶块主元。(a)矩阵$\left[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right]$的两个对角位置均为零；(b)把整个矩阵作为主元块$\bm E$，其行列式为$-1$，可以解出两个分量。蓝色区域表示联合求解的范围，不表示矩阵正定。

#### 12.4.1 主要思想

1. 设$\bm A$实对称非奇异、不一定正定，指出Cholesky开方量可能为负或为零：负数可不开方而把主元连同正负号放入对角因子，零则不能靠对称交换避开（以$\left[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right]$为例，对称置换只在对角位置间移动对角元），须把两行两列合成可逆二阶块；由此定义分块LDL分解式`eq:ls-ldlt`$\bm P\bm A\bm P^\top=\bm L\bm D\bm L^\top$，$\bm D$由可逆的一阶、二阶对称块组成。

2. 由分解记$\bm c=\bm P\bm b$、$\bm w=\bm P\bm x$，把求解拆成前代$\bm L\bm y=\bm c$、块对角方程$\bm D\bm z=\bm y$、回代$\bm L^\top\bm w=\bm z$与还原$\bm x=\bm P^\top\bm w$三段，说明与LU相比只新增中间一步。

###### paragraph：块对角方程

1. 说明$\bm D\bm z=\bm y$按对角块分成互不相关的小方程，一阶块直接相除；对二阶块$\bm E$写出两个方程，分别消去$z_2$与$z_1$，得系数$\det\bm E$与显式公式式`eq:ls-ldlt-two-by-two-solve`，块可逆时分母不为零；转向怎样由$\bm A$算出$\bm P,\bm L,\bm D$。

###### paragraph：一步块消元

1. 把对称交换后的剩余矩阵写成$\left[\begin{smallmatrix}\bm E&\bm C^\top\\\bm C&\bm F\end{smallmatrix}\right]$，设块三角—块对角—块三角的乘积形式并逐块比较：右上块由$\bm E$对称是左下块的转置，剩下$\bm M\bm E=\bm C$与$\bm M\bm E\bm M^\top+\bm S=\bm F$，用$\bm E$对称化简得式`eq:ls-ldlt-block-step`$\bm S=\bm F-\bm M\bm C^\top$。

2. 说明不显式求逆：$\bm M$的每行满足$\bm E\bm m_i^\top=\bm c_i^\top$；一阶块即除以标量，与Cholesky逐列递推相同但不开方、主元可负，二阶块每行按式`eq:ls-ldlt-two-by-two-solve`求解。

###### paragraph：逐块递推

1. 对$\bm S$重复选块与消元，$\bm M$存入$\bm L$、$\bm E$放入$\bm D$，后续交换时已存乘子随之交换（理由同LU），合成置换得式`eq:ls-ldlt`；剩余矩阵为何仍非奇异、所选块为何可逆留到算法分析。

#### 12.4.2 算法实现

1. 说明输入、输出与精确算术下可执行的选块规则：$w_{k,k}\neq0$取一阶块；为零则在第$k$列下方取绝对值最大者$w_{p,k}$（平局取行号最小者），对称交换到第$k+1$位置组成二阶块$\left[\begin{smallmatrix}0&w_{p,k}\\w_{p,k}&w_{p,p}\end{smallmatrix}\right]$；下方全零则报告不适用；强调规则只保证构造可进行而不保证稳定。

2. 说明算法分为$\bm L\bm D\bm L^\top$分解、前代、块对角求解、回代四个模块（各为一个小小节），并取$\bm A=\left[\begin{smallmatrix}0&1&2\\1&2&4\\2&4&4\end{smallmatrix}\right]$、$\bm b=(1,3,2)^\top$在每一步演示。

##### 12.4.2.1 $\bm L\bm D\bm L^\top$分解

1. 说明以$k$记当前主元块起始位置、$s$记其阶数，维护工作矩阵$\bm W$、乘子矩阵$\bm L$、置换$\bm P$与逐块填入的$\bm D$。

2. 第1步初始化$\bm W=\bm A$、$\bm L=\bm P=\bm I$、$\bm D$为空、$k=1$。

3. 第2步按规则选块并在$s=2$、$p\neq k+1$时对称交换$\bm W$的行列，同时交换$\bm P$的行与$\bm L$已存乘子的行；例中$w_{1,1}=0$、下方$(1,2)^\top$，取$p=3$、$s=2$，写出交换后的$\bm W$与$\bm P$，$\bm L$尚无乘子不变。

4. 第3步取$\bm E,\bm C,\bm F$，按式`eq:ls-ldlt-block-step`逐行解$\bm M\bm E=\bm C$，$\bm M$存入$\bm L$、$\bm E$放入$\bm D$，尾块更新为$\bm F-\bm M\bm C^\top$并把$\bm C,\bm C^\top$置零，只算下三角；例中$\bm E=\left[\begin{smallmatrix}0&2\\2&4\end{smallmatrix}\right]$、$\det\bm E=-4$、$\bm C=(1,4)$，按式`eq:ls-ldlt-two-by-two-solve`得$\bm M=(1,\tfrac12)$、尾块$-1$，写出$\bm W$与$\bm L$。

5. 第4步令$k\leftarrow k+s$，$k\leq d$时回到第2步；例中$k=3$时$w_{3,3}=-1$取一阶块，$\bm C,\bm F$为空，只把$-1$放入$\bm D$，随后$k=4>d$结束。

6. 第5步取出因子：每轮置零使结束时$\bm W$为块对角，即$\bm D$；例中逐项验证$\bm L\bm D\bm L^\top$等于交换后的$\bm W$即$\bm P\bm A\bm P^\top$（如$(3,3)$元$1+2-1=2$），并以$\det\bm E\cdot(-1)=4=\det\bm A$核对。

7. 指出上例第一轮即用二阶块、一阶消元时下方无元素，引出零主元在一阶消元之后才出现的例子，以检查一阶块消元。

8. 示例（一阶消元之后出现零主元）：$\bm A=\left[\begin{smallmatrix}1&1&1\\1&1&2\\1&2&1\end{smallmatrix}\right]$；先取一阶块$1$，除以标量得$\bm M=(1,1)^\top$，尾块化为$\left[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right]$；再取无需交换的二阶块，得$\bm L$、$\bm D$与$\bm P=\bm I_3$并验证$\bm L\bm D\bm L^\top=\bm A$；对照Cholesky在第二列开方量$1-1^2=0$处中断，并由$\det\bm A=-1<0$说明$\bm A$不定。

##### 12.4.2.2 前代

1. 重排右端$\bm c=\bm P\bm b$，再根据前代公式（$l_{i,i}=1$）对$i=1,\ldots,d$求$y_i$；例中$\bm c=(1,2,3)^\top$，逐个算出$\bm y=(1,2,1)^\top$。

##### 12.4.2.3 块对角求解

1. 按$\bm D$的对角块自上而下求解，一阶块相除、二阶块按式`eq:ls-ldlt-two-by-two-solve`；例中第一块对应$(y_1,y_2)=(1,2)$、第二块$-1$对应$y_3=1$，得$\bm z=(0,\tfrac12,-1)^\top$。

##### 12.4.2.4 回代

1. 根据回代公式取$\bm L^\top$的元素$l_{k,i}$、对角元为1，对$i=d,\ldots,1$计算$w_i=z_i-\sum_{k>i}l_{k,i}w_k$；例中逐个算出$w_3=-1$、$w_2=1$、$w_1=1$。

2. 由$\bm x=\bm P^\top\bm w$还原次序并用原始数据检验；例中交换第二、三个分量得$\bm x=(1,-1,1)^\top$，代回得$\bm A\bm x=\bm b$、残差为零。

#### 12.4.3 算法分析

###### paragraph：正确性

1. 块消元恒等式可由式`eq:ls-ldlt-block-step`乘开验证，单位块三角因子与对称置换不改变行列式，故剩余矩阵行列式为$\det\bm E\cdot\det\bm S$；所选一阶块非零、二阶块行列式$-w_{p,k}^2\neq0$，由$\bm A$非奇异逐轮推出每个$\bm S$非奇异。

2. 若首对角元与其下方全零，则由对称性剩余矩阵首行首列全零而奇异，矛盾，所以选块规则不会中途失败；乘子随交换换行的理由同LU中乘子与置换的拼合，累积得式`eq:ls-ldlt`，三段求解与还原给出原方程的解；负主元或不定二阶块只反映二次型有负方向，不妨碍求解。

###### paragraph：数值敏感度

1. 区分保证构造可进行的选块规则与控制误差的稳定主元策略：小主元块带来大乘子与元素增长，与LU的主元增长相同；以Bunch–Kaufman策略按对角元与列最大非对角元的相对大小决定块阶数为例。

###### paragraph：计算代价

1. 稠密约$\tfrac13d^3$次运算、存储约$\tfrac12d^2$，比LU省一半。

### 12.5 低秩更新下的求解

1. 以增删约束、调整参数为例说明连续求解只差少量修改的方程；复用旧分解、只多解低阶系统，节省依赖旧分解已存在且修改秩远小于阶数。

#### 12.5.1 主要思想

1. 设$\bm A=\bm A_0+\bm U\bm C\bm V^\top$，$\bm A_0$非奇异且已有分解，$k\ll d$，$\bm A$非奇异；说明更新表示是输入的结构信息，$\bm C$吸收系数，$\bm C=\bm I_k$即$\bm A_0+\bm U\bm V^\top$。

###### paragraph：辅助变量

1. 指出修改项只经$k$维量$\bm C\bm V^\top\bm x$影响方程，令$\bm z=\bm C\bm V^\top\bm x$，把原方程与$\bm z$的定义合写成以$\bm A_0$为系数的第一个方程和约束$\bm C\bm V^\top\bm x-\bm z=\bm0$。

2. 由第一个方程与旧因子求解式`eq:ls-woodbury-old-solves`（$\bm A_0\bm u=\bm b$、$\bm A_0\bm Z=\bm U$）得修正式`eq:ls-woodbury-correction`$\bm x=\bm u-\bm Z\bm z$，代入第二个方程移项得$k$阶方程式`eq:ls-woodbury-small-system`$\bm K\bm z=\bm h$，$\bm K=\bm I_k+\bm C\bm V^\top\bm Z$、$\bm h=\bm C\bm V^\top\bm u$；总计只需$k+1$次旧因子求解与一个低阶求解，反向等价与$\bm K$的可逆性判据留到算法分析。

###### paragraph：秩一修改

1. 对$\bm A_0+\bm p\bm q^\top$，记$\bm A_0\bm w=\bm p$，$\bm K$与$\bm h$均为标量，辅助方程退化为一次除法$z=\bm q^\top\bm u/(1+\bm q^\top\bm w)$、$\bm x=\bm u-z\bm w$；分母为零时更新矩阵奇异，回指定理`thm:ls-sherman-morrison`。

#### 12.5.2 算法实现

1. 说明输入为$\bm A_0$的分解、修改项$\bm U,\bm C,\bm V$与$\bm b$，需预先确定$\bm A_0$的求解方法（通常复用已有分解，否则按结构调用前面各节方法），节省计算的比较以分解已存在为前提。

2. 说明算法分为用旧因子求解、形成小系统、求解小系统并修正三个模块（各为一个小小节），并取$\bm A_0=\operatorname{diag}(3,2)$、$\bm U=\bm V=(1,1)^\top$、$\bm C=1$、$\bm b=(1,2)^\top$在每一步演示，更新后矩阵为$\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$。

##### 12.5.2.1 用旧因子求解

1. 按式`eq:ls-woodbury-old-solves`用$\bm A_0$的因子求$\bm u$；例中$\bm A_0$为对角矩阵，逐个相除得$\bm u=(\tfrac13,1)^\top$。

2. 对$\bm U$的$k$列复用同一组因子求$\bm Z$，说明它记录修改方向经$\bm A_0^{-1}$作用后的结果；例中$\bm Z=(\tfrac13,\tfrac12)^\top$。

##### 12.5.2.2 形成小系统

1. 先投影到$k$维，计算$\bm V^\top\bm Z$与$\bm V^\top\bm u$；例中分别为$\tfrac56$与$\tfrac43$。

2. 按式`eq:ls-woodbury-small-system`左乘$\bm C$组装$\bm K$与$\bm h$，全程不形成新的$d$阶矩阵；例中$\bm K=\tfrac{11}6$、$\bm h=\tfrac43$。

##### 12.5.2.3 求解小系统并修正

1. 调用直接法求解$\bm K\bm z=\bm h$，$\bm K$奇异时停止并说明更新矩阵也奇异（定理`thm:ls-woodbury`）；例中$k=1$，一次除法得$z=\tfrac8{11}$。

2. 按式`eq:ls-woodbury-correction`修正得$\bm x=\bm u-\bm Z\bm z$；例中$\bm x=(\tfrac1{11},\tfrac7{11})^\top$。

3. 在更新后的矩阵下重算原残差而非只查辅助方程；例中$\bm A\bm x=(1,2)^\top=\bm b$，残差为零且全程未分解$\bm A$。

4. 指出上例$\bm U=\bm V$看不出两者用途之别，引出$\bm U\neq\bm V$、更新矩阵不对称的例子，检查$\bm U$只进入旧因子求解、$\bm V$只进入投影。

5. 示例`ex:ls-woodbury-nonsymmetric`（非对称的秩一更新）：$\bm A_0=\operatorname{diag}(2,3)$、$\bm U=(1,1)^\top$、$\bm V=(1,0)^\top$、$\bm b=(4,5)^\top$，更新矩阵$\left[\begin{smallmatrix}3&0\\1&3\end{smallmatrix}\right]$；得$\bm u=(2,\tfrac53)^\top$、$\bm Z=(\tfrac12,\tfrac13)^\top$、$K=\tfrac32$、$h=2$、$z=\tfrac43$，修正得$(\tfrac43,\tfrac{11}9)^\top$，用更新矩阵重算原残差为零。

#### 12.5.3 算法分析

###### paragraph：正确性

1. 补出反方向：由$\bm K\bm z=\bm h$与$\bm x=\bm u-\bm Z\bm z$推出$\bm C\bm V^\top\bm x=\bm z$，从而$\bm A\bm x=\bm b$，小系统与原方程等价；对任意右端写成矩阵形式即得可逆性判据与逆矩阵公式。

2. 定理`thm:ls-woodbury`（Woodbury恒等式）：$\det(\bm A_0+\bm U\bm C\bm V^\top)=\det\bm A_0\det\bm K$，可逆当且仅当$\bm K$可逆；$\bm C$也可逆时给出式`eq:matrix-analysis-woodbury`。

3. 证明：把更新矩阵写成$\bm A_0(\bm I+\bm Z\bm C\bm V^\top)$，对辅助分块矩阵$\bm T$用两种分块三角分解与分块三角矩阵的行列式得行列式等式；再由$\bm K=\bm C(\bm C^{-1}+\bm V^\top\bm A_0^{-1}\bm U)$与等价关系对任意右端写出逆。

4. 说明判据允许$\bm C$奇异，这是算法只用$\bm K$、不用$\bm C^{-1}$的原因；引出秩一情形。

5. 定理`thm:ls-sherman-morrison`（Sherman–Morrison公式）及证明：取$k=1$代入Woodbury恒等式，可逆当且仅当$1+\bm q^\top\bm A_0^{-1}\bm p\neq0$。

###### paragraph：数值敏感度

1. 代数恒等式不保证稳定：$\bm K$接近奇异放大误差，$\bm A_0$求解敏感时$\bm u,\bm Z$的误差即使$\bm A$良态也进入结果，$\bm u$与$\bm Z\bm z$相近时相减相消。

###### paragraph：计算代价

1. 已有因子时代价为$O(kd^2+k^2d+k^3)$，在$k\ll d$时远少于重新分解的$\tfrac23d^3$；连续多次更新后辅助维数与误差增长，重新分解更合算。

### 12.6 方法选择与结果检验

1. 说明面对方阵方程时先看矩阵结构选择分解，再用原始数据核验结果。

###### paragraph：按结构选择

1. 归纳：非奇异方阵用部分选主元LU，对称正定用Cholesky（运算量约为LU一半且不需选主元），对称不定非奇异用分块LDL。

2. 明确低秩更新的复用条件：已有分解、秩远小于阶数且$\bm K$可逆不病态，多次更新后与重新分解比较。

###### paragraph：用原始数据核验

1. 说明代回原方程检查$\bm A\bm x=\bm b$，以LU演示与低秩更新例为例，浮点计算报告缩放残差。

2. 说明分解残差$\lVert\bm P\bm A-\bm L\bm U\rVert$、$\lVert\bm A-\bm L\bm L^\top\rVert$只是旁证，不能代替对原方程的检验。

###### paragraph：残差小不等于误差小

1. 指出通过检验不保证误差小；汇总本章算法层面的结论（选主元与增长、Cholesky无增长、低秩更新中$\bm K$病态的放大），系统解释与整体比较交给第17章。

### 12.7 本章小结

1. 回应章首问题：不求逆、有限步算出非奇异方阵的精确解，共同做法是用消元化为三角方程并把分解与右端分开以复用分解。

2. 消元是起点：初等行变换不改变解，化为阶梯形可读出主元、自由变量与秩；对$[\bm A\mid\bm I_n]$消元可求逆，但只解一个方程时不必先求逆。

3. 有了分解求解化为前代与回代；部分选主元LU逐列消元、处理完前$d-1$列结束，乘子随行交换，非奇异时总能进行，不选主元要求顺序主子式非零。

4. 对称结构：Cholesky的开方量是Schur补、正定当且仅当分解存在，运算减半；分块LDL保留负主元、零对角时用二阶块使可逆矩阵总能消元。

5. 复用：低秩更新只需$k+1$次旧因子求解与$k$阶方程，可逆性由$\bm K$决定，Woodbury与Sherman–Morrison是矩阵形式；节省须已有分解且修改秩小。

6. 结果须代回原方程检验，但检验不说明误差大小，主元增长的系统分析在第17章；不相容或非方阵问题改求最小二乘解，交给第13章。

## 第13章 最小二乘的直接求解

正文入口：[03-least-squares-direct-methods.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/03-least-squares-direct-methods.tex)（章标题、标签与章引言），依次接入[01-orthogonal-methods.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/03-least-squares-direct-methods/01-orthogonal-methods.tex)（13.1—13.3）与[03-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/03-least-squares-direct-methods/03-summary.tex)（13.4）。

1. 从第11章的最小二乘与最小范数目标及其检验条件出发，指出$(\bm A^\top\bm A)^{-1}\bm A^\top\bm b$与$\bm A^\dagger\bm b$只是表达式，显式形成$\bm A^\top\bm A$还可能丢失信息；提出在有限步内算出选定的最小二乘解。

2. 说明矩阵一般不是方阵、消元不再保持目标，改用正交变换保持长度化为三角方程，或用奇异值分解拆成互不耦合的标量问题。

3. 说明各节分工：13.1节经正规方程交给第12章的Cholesky；13.2节正交三角化并给出修正Gram–Schmidt、Householder与Givens三种因子计算；13.3节用SVD处理任意形状与秩并推广到加权、齐次目标。

4. 列出依赖：QR用到第4章的Gram–Schmidt、QR分解与正交投影，正规方程法用到第12章的Cholesky与三角代入，SVD求解与条件数平方用到第7章；系统误差与正则化在第17章。

5. 交代记号：$\bm A\in\mathbb R^{m\times d}$、$\bm b\in\mathbb R^m$，满列秩最小二乘解$\hat{\bm x}$与最小范数解$\bm x_\star$；每种算法仍按主要思想、算法实现与算法分析三部分讲解。

### 13.1 正规方程法

1. 说明第12章都是方阵精确解，转向超定最小二乘：最小二乘解满足正规方程，满列秩时系数矩阵对称正定，正好交给Cholesky。

#### 13.1.1 主要思想

1. 输入满列秩$\bm A$（$m\geq d$）与$\bm b$，求唯一最小二乘解$\hat{\bm x}$；核心是化为$d$阶方程式`eq:ls-normal-system`$\bm G\hat{\bm x}=\bm c$（$\bm G=\bm A^\top\bm A$、$\bm c=\bm A^\top\bm b$）再用Cholesky求解，下面先说明方程来源、再说明$\bm G,\bm c$的计算。

###### paragraph：正规方程

1. 依据第11章最优拟合值是正交投影，最优残差与每一列正交，把$d$个等式堆叠成向量得式`eq:ls-normal-system`即正规方程式`eq:linear-algebra-normal-equations`，说明推导只用正交投影、不用多元求导，并读出$\bm G$与$\bm c$的元素是列间内积。

2. 指出满列秩时$\bm G$对称正定（理由留到算法分析），于是分解$\bm G=\bm L\bm L^\top$后先前代解$\bm L\bm y=\bm c$、再回代解$\bm L^\top\hat{\bm x}=\bm y$。

###### paragraph：按行累计

1. 由$\bm a_j^\top\bm a_k=\sum_ia_{i,j}a_{i,k}$得式`eq:ls-gram-row-accumulation`$\bm G=\sum_i\bm A_{i,:}^\top\bm A_{i,:}$、$\bm c=\sum_ib_i\bm A_{i,:}^\top$，每读入一行即可累加、不必保存全部观测，这是数据量大时的优点；代价在精度，条件数平方见算法分析。

#### 13.1.2 算法实现

1. 说明输入、输出且无需预选规则，算法分为形成Gram矩阵与右端、$\bm L\bm L^\top$分解、前代与回代三个模块（各为一个小小节），并取示例`ex:ls-line-least-squares`的直线拟合数据$\bm A=\left[\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\right]$、$\bm b=(1,2,2)^\top$在每一步演示，本章QR求解及其三种因子计算沿用这组数据。

##### 13.1.2.1 形成Gram矩阵与右端

1. 第1步初始化$\bm G=\bm0$、$\bm c=\bm0$、$i=1$。

2. 第2步按式`eq:ls-gram-row-accumulation`累加第$i$行的外积与右端贡献，只累加下三角；例中列出三行对$\bm G$的增量与对$\bm c$的增量$(1,0)^\top,(2,2)^\top,(2,4)^\top$。

3. 第3步判断是否结束；例中三行累加完毕得$\bm G=\left[\begin{smallmatrix}3&3\\3&5\end{smallmatrix}\right]$、$\bm c=(5,6)^\top$。

##### 13.1.2.2 $\bm L\bm L^\top$分解

1. 逐列按Cholesky逐列公式先算开方量$\delta_j$并检查为正，再算$l_{j,j}$与下方元素；例中按列算得$\bm L=\left[\begin{smallmatrix}\sqrt3&0\\\sqrt3&\sqrt2\end{smallmatrix}\right]$。

2. 说明满列秩保证每个$\delta_j>0$，若$\delta_j\leq0$则$\bm A$秩亏或条件很差，停止并改用QR求解或SVD求解。

##### 13.1.2.3 前代与回代

1. 前代按$y_i=(c_i-\sum_{k<i}l_{i,k}y_k)/l_{i,i}$求$\bm y$；例中$\bm y=(5/\sqrt3,1/\sqrt2)^\top$。

2. 回代取$\bm L^\top$的元素$l_{k,i}$，对$i=d,\ldots,1$求$\hat x_i$；例中得$\hat x_2=\tfrac12$、$\hat x_1=\tfrac76$。

3. 输出并用原始数据核验$\bm A^\top\bm r=\bm0$；例中残差$\bm r=(-\tfrac16,\tfrac13,-\tfrac16)^\top$与两列正交，$\lVert\bm r\rVert^2=\tfrac16$。

4. 说明残差非零是因为三点不共线、方程不相容，最小二乘完成的标志是$\bm A^\top\bm r=\bm0$而非$\bm r=\bm0$；Cholesky失败或结果对舍入敏感时，不能只凭正规方程小系统的残差小宣布可靠。

#### 13.1.3 算法分析

###### paragraph：满列秩保证正定

1. 由满列秩得$\bm z^\top\bm G\bm z=\lVert\bm A\bm z\rVert^2>0$，$\bm G$对称正定，由定理`thm:ls-cholesky-existence`知开方量都为正；秩亏时存在$\bm A\bm z=\bm0$的非零$\bm z$，$\bm G$只是半正定，论证失效。

###### paragraph：正确性

1. 两次三角求解给出$\bm A^\top\bm A\hat{\bm x}=\bm A^\top\bm b$，由定理`thm:ls-least-squares-solutions`即唯一最小二乘解。

###### paragraph：数值敏感度

1. 对满列秩矩阵定义$\kappa_2(\bm A)=\sigma_{\max}/\sigma_{\min}$，方阵时与第9章的定义一致。

2. 定理`thm:ls-normal-equations-condition-squaring`（正规方程使条件数平方）及证明：由SVD得$\bm A^\top\bm A=\bm V\operatorname{diag}(\sigma_i^2)\bm V^\top$，其极端特征值为$\sigma_1^2,\sigma_d^2$。

3. 说明压缩方向在$\bm G$中被压缩两次，累计内积的舍入可能抹掉信息，代数等价不意味着数值条件相同，这是引入QR的原因；故适合条件较好的满列秩问题，误差界见第17章。

###### paragraph：计算代价与适用范围

1. 一行全非零即使$\bm G$稠密，稠密时形成$\bm G$约$md^2$、分解约$d^3/3$，总量$O(md^2+d^3)$；秩亏时正规方程仍刻画全部最小二乘解但$\bm G$半正定、Cholesky遇零主元，选解交给SVD路线。

### 13.2 QR求解

1. 说明正规方程的精度损失来自形成$\bm A^\top\bm A$，QR求解直接对$\bm A$正交三角化；先写最小二乘与满行秩最小范数解的共同求解过程，再给修正Gram–Schmidt、Householder与Givens三种因子计算方法。

#### 13.2.1 主要思想

补充图解：满列秩最小二乘的QR分解，示意$m=5,d=3$。正交变换后，矩阵上方的蓝色三角块为$\bm R$，下方为零；右端相应分成$\bm c_1$与$\bm c_2$。取$\bm R\hat{\bm x}=\bm c_1$后，残差$\bm r=\bm b-\bm A\hat{\bm x}$在变换后的坐标中上方为零，下方为$\bm c_2$，最小残差范数为$\lVert\bm c_2\rVert_2$。图中的近似号表示最小二乘匹配。

###### paragraph：满列秩的解

1. 输入满列秩$\bm A$与$\bm b$，写出完整QR分解$\bm A=\bm Q\left[\begin{smallmatrix}\bm R\\\bm0\end{smallmatrix}\right]$、$\bm Q=[\bm Q_1\;\bm Q_2]$，其中$\bm A=\bm Q_1\bm R$是第4章的薄QR、$\bm Q_2$补全标准正交基；正交变换保持长度，把最小二乘变成三角方程而不形成$\bm A^\top\bm A$。

2. 把$\bm Q^\top\bm b$分成$\bm c_1,\bm c_2$，由长度保持推出残差分解式`eq:ls-qr-residual-split`$\lVert\bm A\bm x-\bm b\rVert^2=\lVert\bm R\bm x-\bm c_1\rVert^2+\lVert\bm c_2\rVert^2$，第二项是不可拟合部分。

3. 第一项在三角方程式`eq:ls-qr-triangular-system`$\bm R\hat{\bm x}=\bm c_1$时为零，回代即得$\hat{\bm x}$，最小残差为$\lVert\bm c_2\rVert$；薄分解下不可拟合部分即$\bm b-\bm Q_1\bm Q_1^\top\bm b$，唯一性与最优性回指定理`thm:ls-qr-least-squares`。

###### paragraph：满行秩的最小范数解

1. 对满行秩$\bm A$（$m<d$），因最小范数解位于$\operatorname{range}(\bm A^\top)$而分解$\bm A^\top=\bm Q\bm R$；写$\bm x=\bm Q\bm y+\bm w$且$\bm Q^\top\bm w=\bm0$，代入得方程只约束$\bm y$，取$\bm w=\bm0$（理由见算法分析）得式`eq:ls-qr-min-norm`：前代$\bm R^\top\bm y=\bm b$、重建$\bm x_\star=\bm Q\bm y$。

###### paragraph：只需应用正交因子

1. 说明两个分支只需$\bm Q$或$\bm Q^\top$对向量的作用；修正Gram–Schmidt直接算出$\bm Q_1$的列，Householder保存反射向量，Givens保存旋转参数，三者服务于同一求解逻辑。

#### 13.2.2 算法实现

1. 说明输入满列秩$\bm A$与$\bm b$、输出$\hat{\bm x}$，满行秩输入走最后的转置QR分支；只需预选因子计算方法，算法分为QR分解、变换右端、回代三个模块，仍用13.1节直线拟合数据演示。

##### 13.2.2.1 QR分解

1. 按13.2.4—13.2.6节之一计算$\bm R$并记录正交因子或变换，$r_{j,j}=0$说明秩亏，改用SVD求解。

2. 例中引用修正Gram–Schmidt的结果$\bm q_1=\tfrac1{\sqrt3}(1,1,1)^\top$、$\bm q_2=\tfrac1{\sqrt2}(-1,0,1)^\top$、$\bm R=\left[\begin{smallmatrix}\sqrt3&\sqrt3\\0&\sqrt2\end{smallmatrix}\right]$，说明Householder与Givens给出的$\bm R$至多相差各行符号。

##### 13.2.2.2 变换右端

1. 按式`eq:ls-qr-triangular-system`算$\bm c_1=\bm Q_1^\top\bm b$，反射或旋转按分解次序作用于$\bm b$取前$d$个分量，MGS的计算次序见13.2.4节；例中$\bm c_1=(5/\sqrt3,1/\sqrt2)^\top$。

2. 读出最小残差：用反射或旋转时其余分量即$\bm c_2$；例中补齐$\bm q_3=\tfrac1{\sqrt6}(1,-2,1)^\top$，得$\bm c_2=-1/\sqrt6$、最小残差$1/\sqrt6$。

##### 13.2.2.3 回代

1. 按回代公式由式`eq:ls-qr-triangular-system`逐个求$\hat x_i$；例中$\hat x_2=\tfrac12$、$\hat x_1=\tfrac76$。

2. 以原数据核验$\bm A^\top(\bm b-\bm A\hat{\bm x})=\bm0$；例中残差$(-\tfrac16,\tfrac13,-\tfrac16)^\top$，长度$1/\sqrt6$与读出的$|\bm c_2|$相同。

3. 指出例中$\bm R$与$\bm c_1$恰是正规方程法的$\bm L^\top$与前代结果$\bm y$，两条路线回代同一个三角方程，区别在于不形成$\bm A^\top\bm A$。

##### 13.2.2.4 欠定情形：转置QR

1. 给出三步：分解$\bm A^\top=\bm Q\bm R$（零对角元则转SVD）、按式`eq:ls-qr-min-norm`前代$\bm R^\top\bm y=\bm b$、重建$\bm x_\star=\bm Q\bm y$并检查$\bm A\bm x_\star=\bm b$与$\bm x_\star\in\operatorname{range}(\bm A^\top)$。

2. 对比经$\bm A\bm A^\top\bm z=\bm b$的做法需要先形成Gram矩阵；指出直线拟合是超定问题、不能演示本分支，引出欠定例子。

3. 示例`ex:ls-qr-min-norm-run`（转置QR给出最小范数解）：$\bm A=\left[\begin{smallmatrix}1&0&1\\0&1&1\end{smallmatrix}\right]$、$\bm b=(1,2)^\top$，对$\bm A^\top$修正Gram–Schmidt得$\bm q_1,\bm q_2$与$\bm R=\left[\begin{smallmatrix}\sqrt2&1/\sqrt2\\0&\sqrt{3/2}\end{smallmatrix}\right]$，前代$\bm y=(1/\sqrt2,\sqrt{3/2})^\top$，重建$\bm x_\star=(0,1,1)^\top$。

4. 由全部解$(1-t,2-t,t)^\top$的范数平方$3(t-1)^2+2$在$t=1$最小，直接确认$\bm x_\star$范数最小。

#### 13.2.3 算法分析

###### paragraph：正确性

1. 说明两个分支的正确性合写为一个定理。

2. 定理`thm:ls-qr-least-squares`（QR给出最小二乘解与最小范数解）：满列秩时$\bm R^{-1}\bm c_1$是唯一最小二乘解、最小残差$\lVert\bm c_2\rVert$；满行秩时$\bm Q\bm y$是唯一最小范数解。

3. 证明：（1）由正交矩阵保持长度得式`eq:ls-qr-residual-split`，$\bm R$可逆使第一项仅在$\bm R^{-1}\bm c_1$处为零；（2）验证$\bm A\bm x_\star=\bm b$且$\bm x_\star\in(\ker\bm A)^\perp$，其他解相差核中非零向量$\bm w$，由勾股关系范数更大。

###### paragraph：数值敏感度

1. 区分问题本身对数据的敏感度（第17章）与计算QR因子时正交化过程引入的误差，三种实现在工作量、数值正交性与残差核验方式上不同，分别在后三个小节说明。

###### paragraph：秩亏情形

1. 秩亏时$\bm R$有零对角元不能回代；带列主元QR只取主元变量回代、其余置零，一般给出基本解而非最小范数解，故一般秩统一用SVD。

#### 13.2.4 修正Gram–Schmidt正交化

1. 说明13.2.4—13.2.6节计算同一组QR因子的两类思路：修正Gram–Schmidt从$\bm A$的列逐个造出标准正交方向，直接得到$\bm Q_1$与$\bm R$；Householder与Givens对$\bm A$和$\bm b$依次施加正交变换直到$\bm A$成为上三角形，$\bm Q$只以变换记录隐含存在，每步保持$\lVert\bm A\bm x-\bm b\rVert$不变，最后得到式`eq:ls-qr-triangular-system`的三角方程。

2. 用一句话概括修正Gram–Schmidt的想法：每列减去在已有方向上的分量，剩余部分归一化为下一个$\bm q_j$，减去的分量与剩余长度记入$\bm R$。

##### 13.2.4.1 主要思想

1. 按列比较$\bm A=\bm Q_1\bm R$得$\bm a_k=\sum_{i\leq k}r_{i,k}\bm q_i$，据此解释$\bm R$的元素：$r_{i,k}$（$i<k$）是$\bm a_k$沿$\bm q_i$的分量，$r_{k,k}$是扣除后剩余部分的长度，$\bm q_k$是其方向；$\bm R$上三角使方向可按列的次序逐个求出。

###### paragraph：$d=2$的情况

1. 由第一式得$r_{1,1}=\lVert\bm a_1\rVert,\bm q_1$，第二式与$\bm q_1$作内积得$r_{1,2}$，移项后剩余向量的长度与方向给出$r_{2,2},\bm q_2$。

###### paragraph：一般情况

1. 把剩余向量$\bm v_k$解释为第$k$列中尚未由已有方向表示的部分，每得到一个新方向就从所有未处理列中扣除，轮到第$j$列时只剩新方向，得归一化式`eq:ls-mgs-normalize`与更新式`eq:ls-mgs-update`。

2. 与第4章Gram–Schmidt的区别只在投影系数用当前剩余向量计算，精确算术中给出同一组因子；用直观机制说明有限精度下的差别：经典形式中$\bm q_2$对正交性的微小偏离乘上$\bm a_k$在$\bm q_1$方向的大分量混入$r_{2,k}$，修正形式只乘上很小的残留分量，并声明这只说明误差来源，正交性检查见算法分析。

3. 把右端当作额外一列按同样次序扣除得式`eq:ls-mgs-rhs`，每次取走$\bm b$在一个方向上能由列表示的部分，$c_i$记录取走的量；全部扣除后$\bm s$即最小二乘残差，$\bm c_1$交给式`eq:ls-qr-triangular-system`回代。

##### 13.2.4.2 算法实现

1. 说明输入、输出且无需预选规则，逐列维护剩余向量、$\bm R$的已算元素与右端剩余$\bm s$，仍用直线拟合数据演示。

2. 第1步初始化$\bm v_k=\bm a_k$、$\bm R=\bm0$、$\bm s=\bm b$、$j=1$，写出例中的$\bm v_1,\bm v_2,\bm s$。

3. 第2步先说明$\bm v_j$已扣除全部已有方向、剩下的是新方向，再按式`eq:ls-mgs-normalize`归一化，$r_{j,j}=0$说明列相关，停止并改用SVD；例中$r_{1,1}=\sqrt3$、$\bm q_1=\tfrac1{\sqrt3}(1,1,1)^\top$。

4. 第3步说明新方向一经确定就从后面各列和右端扣除，按式`eq:ls-mgs-update`与式`eq:ls-mgs-rhs`更新；例中$r_{1,2}=\sqrt3$、$\bm v_2=(-1,0,1)^\top$、$c_1=5/\sqrt3$、$\bm s=(-\tfrac23,\tfrac13,\tfrac13)^\top$，并解释在直线拟合中扣除全一方向$\bm q_1$就是减去平均值。

5. 第4步判断是否结束；例中$j=2$时得$r_{2,2}=\sqrt2$、$\bm q_2$，只处理右端得$c_2=1/\sqrt2$、$\bm s=(-\tfrac16,\tfrac13,-\tfrac16)^\top$，写出$\bm R$与$\bm c_1$，核验$\bm q_1^\top\bm q_2=0$与$\sqrt3\bm q_1+\sqrt2\bm q_2=\bm a_2$，并以后者解读$\bm R$第二列；剩下的$\bm s$正是长度$1/\sqrt6$的拟合残差。

6. 第5步回代求解$\bm R\hat{\bm x}=\bm c_1$；例中$\bm R,\bm c_1$与13.2节算法实现所用相同，得$\hat{\bm x}=(\tfrac76,\tfrac12)^\top$。

7. 补充说明：$\bm Q_1$、$\bm R$与剩余向量只是内部状态；按列组织的次序对每列执行相同运算；某列扣除后明显变短时再正交化，并把第二遍系数加到已累计的$r_{i,j}$上以保持$\bm A=\bm Q_1\bm R$；右端须按式`eq:ls-mgs-rhs`逐次扣除，不宜另算$\bm Q_1^\top\bm b$。

##### 13.2.4.3 算法分析

1. 精确算术中更新后$\bm v_k$与$\bm q_j$及此前各方向正交，各$\bm q_i$两两正交，并维持$\bm a_k=\sum_{i\leq j}r_{i,k}\bm q_i+\bm v_k$，最终得$\bm A=\bm Q_1\bm R$；对剩余向量与原始列的内积相同，故给出与原Gram–Schmidt相同的QR分解且$c_i=\bm q_i^\top\bm b$，由定理`thm:ls-qr-least-squares`得最小二乘解。

2. 有限精度下近相关列的剩余向量很短，舍入影响被放大而失去正交性，这是再正交化处理的情形；正交性$\lVert\bm Q_1^\top\bm Q_1-\bm I\rVert$与重构质量$\lVert\bm A-\bm Q_1\bm R\rVert$须分开检查，后者小不保证前者小，损失程度与条件数有关（第17章）；主要工作约$2md^2$。

#### 13.2.5 Householder反射

1. 概括Householder方法：不构造$\bm Q_1$的列，第$k$步用一个镜面反射把第$k$列从对角元往下的部分变成坐标轴方向，下方元素随之为零，同一反射作用于其余各列与$\bm b$；$d$次反射后得到$\bm R$与变换后的右端，正交因子是反射之积。

##### 13.2.5.1 主要思想

1. 写出$\bm Q^\top=\bm H_d\cdots\bm H_1$，提出把列段$\bm y\neq\bm0$映到第一坐标轴的问题。

2. 几何构造：长度保持使目标只能是$\alpha\bm e_1$、$|\alpha|=\lVert\bm y\rVert$；平面上原点在$\bm y$与$\alpha\bm e_1$连线的垂直平分线上，以它为镜子反射即把$\bm y$送到$\alpha\bm e_1$，镜子的法向是$\bm v=\bm y-\alpha\bm e_1$，高维时换成以$\bm v$为法向的超平面。

3. 据此定义Householder反射$\bm H=\bm I-2\bm v\bm v^\top/(\bm v^\top\bm v)$：$\bm v$方向分量变号、正交分量不变，它对称正交，只需选好$\bm v$。

4. 图`fig:ls-householder-reflection`：$\bm y=(2,1)^\top$与其像$-\sqrt5\bm e_1$关于超平面$\bm v^\perp$对称，二者之差为$\bm v$，圆弧表示反射保持长度。

5. 从代数上确认几何构造：由长度保持得$\alpha=\pm\lVert\bm y\rVert$，展开$\bm H\bm y=\alpha\bm e_1$知$\bm y-\alpha\bm e_1$须是$\bm v$的倍数，故取$\bm v=\bm y-\alpha\bm e_1$，系数等于1的验证交给算法分析中的引理。

6. 解释符号选择的几何直觉：两个候选目标中，若$\bm y$接近其中一个，二者之差$\bm v$很短、镜子朝向难以准确算出，所以取与$y_1$异号、离$\bm y$较远的目标$\alpha=-s\lVert\bm y\rVert$，得式`eq:ls-householder`，使$v_1$为两个同号数相加（数值理由见算法分析）。

7. 作用于向量时用$\tau=2/(\bm v^\top\bm v)$与式`eq:ls-householder-apply`，即减去$\bm v$方向分量的两倍，只需一次内积与一次更新，不形成稠密$\bm H$；第$k$步嵌入为$\bm H_k=\operatorname{diag}(\bm I_{k-1},\bm H)$，前$k-1$行与前面各列的零不被改动，逐列进行时已造出的零不被破坏。

##### 13.2.5.2 算法实现

1. 说明输入、输出与预选的符号规则$s$，保持列顺序、不选列主元，逐列维护工作矩阵$\bm F$与右端$\bm c$，仍用直线拟合数据演示并在每列处理后给出当前值。

2. 第1步初始化$\bm F=\bm A$、$\bm c=\bm b$、$k=1$。

3. 第2步取第$k$列从对角元往下、尚未处理的列段$\bm y=\bm F_{k:m,k}$，按式`eq:ls-householder`构造并保存$\bm v,\tau$；$\bm y=\bm0$说明列相关，停止改用SVD，下方已为零则取恒等跳过第3步；例中$\bm v=(1+\sqrt3,1,1)^\top$、$\bm v^\top\bm v=6+2\sqrt3$、$\tau=1/(3+\sqrt3)$。

4. 第3步说明整个问题须经受同一正交变换才保持残差长度，故按式`eq:ls-householder-apply`把反射作用于剩余子块与右端，第$k$列直接成为$(-s\lVert\bm y\rVert,0,\ldots)^\top$；例中写出更新后的$\bm F$与$\bm c=(-5/\sqrt3,1/\sqrt3,1/\sqrt3)^\top$，指出第一列已成坐标轴方向、第一行从此确定，并以两列与右端长度平方$3,5,9$不变核验。

5. 第4步判断是否结束；例中$k=2$时取第二列后两个元素，$\lVert\bm y\rVert=\sqrt2$，反射只作用于后两行，这一段也成为坐标轴方向而第一列的零与第一行不变，得$\bm F$的上三角部分$\left[\begin{smallmatrix}-\sqrt3&-\sqrt3\\0&-\sqrt2\end{smallmatrix}\right]$与$\bm c=(-5/\sqrt3,-1/\sqrt2,-1/\sqrt6)^\top$。

6. 第5步取$\bm R=\bm F_{1:d,1:d}$检查对角元后回代，$\bm F$后$m-d$行为零，$\bm c_{d+1:m}$是不可拟合部分，其范数为最小残差；例中得$\hat{\bm x}=(\tfrac76,\tfrac12)^\top$、$|c_3|=1/\sqrt6$。

7. 指出例中$\bm R$与正规方程法的$\bm L^\top$只差各行符号，负对角元不影响求解，统一为正对角须同时变号$\bm R$的行与右端相应分量。

##### 13.2.5.3 算法分析

1. 引理`lem:ls-householder-reflection`（Householder反射）及证明：$\bm H$对称且$\bm H^2=\bm I$，由$\bm v^\top\bm v=2\bm v^\top\bm y>0$得$\bm H\bm y=-s\lVert\bm y\rVert\bm e_1$。

2. 每个$\bm H_k$只作用于第$k$行以下，保持旧零结构，$d$步后得到$\bm Q^\top=\bm H_d\cdots\bm H_1$的QR分解，由定理`thm:ls-qr-least-squares`得最小二乘解。

3. 说明符号选择避免$y_1-\alpha$的相消；Householder QR后向稳定（第17章），所得$\bm Q$在舍入范围内正交，工作量约$2md^2-\tfrac23d^3$；列主元可辅助辨认近相关列，但秩亏的最小范数选择仍交给SVD。

#### 13.2.6 Givens旋转

1. 概括Givens方法：同样用正交变换把$\bm A$与$\bm b$化为上三角形，但每次在两行构成的平面内旋转、只消去一个元素；与Householder一步处理一整列相比，每步只改动两行，下方非零元很少或在已有$\bm R$上补入新观测时只需少数旋转，这种局部性带来节省。

##### 13.2.6.1 主要思想

1. 介绍Givens旋转只在两个坐标的平面内旋转、其余坐标不变，每次混合两行消去一个元素，正交因子为一串旋转之积。

2. 图`fig:ls-givens-householder-elimination`：Givens旋转沿圆弧、Householder反射沿角平分线把$(2,1)^\top$映到$(\sqrt5,0)^\top$，区分行列式为$+1$的旋转与对称正交的反射，并注明图中反射取相反符号。

3. 二维问题的几何直觉：向量$(\alpha,\beta)^\top$与第一坐标轴夹角为$\theta$，顺时针转过$\theta$即落到$(\rho,0)^\top$，$\rho$为长度，旋转矩阵元素$c=\cos\theta$、$s=\sin\theta$就是$\alpha/\rho,\beta/\rho$，不必求角度。

4. 代数确认：由$-s\alpha+c\beta=0$得$(c,s)$与$(\alpha,\beta)$平行，结合$c^2+s^2=1$与$\rho>0$得式`eq:ls-givens`$\rho=\sqrt{\alpha^2+\beta^2}$、$c=\alpha/\rho$、$s=\beta/\rho$；说明这里的$s$与Householder符号无关，零向量取恒等。

5. 写出两行同时更新的式`eq:ls-givens-rows`，右端同样更新；说明$c,s$由两行在某一列的元素确定，使下一行该元素为零、上一行为$\rho$，同一旋转作用于其余元素与右端以保持整个问题经受同一正交变换。

6. 三角化逐列、自下而上用相邻两行消元：每次把下一行的元素并入上一行，非零部分逐行向上汇集到对角元，对角元等于该列段的长度；被消零的行不再参与本列的旋转，零不被破坏的理由见算法分析。

##### 13.2.6.2 算法实现

1. 说明输入、输出与预选的消元次序（按列、列内$i=m,\ldots,k+1$用相邻两行），维护$\bm F$与右端$\bm t$（避免与$c$混淆），先给三角化与回代、再给新增观测的更新，仍用直线拟合数据并写成增广列。

###### paragraph：三角化与回代

1. 第1步初始化$\bm F=\bm A$、$\bm t=\bm b$、$k=1$、$i=m$，写出增广矩阵。

2. 第2步构造旋转：$f_{i,k}=0$跳过，否则以上一行元素为$\alpha$、待消元素为$\beta$按式`eq:ls-givens`算$\rho,c,s$，用缩放或hypot避免上溢下溢；例中$k=1,i=3$时$\alpha=\beta=1$、$\rho=\sqrt2$、$c=s=1/\sqrt2$。

3. 第3步按式`eq:ls-givens-rows`旋转两行第$k$列及以后的部分与右端并保存参数，第$k$列以前两行均为零不必计算，强调先用临时量保存旧值，否则不再是旋转；例中写出第2、3行的结果，解释第3行的元素并入第2行、首元素成为$\sqrt2$。

4. 第4步推进$i$与$k$；例中用第1、2行以$\rho=\sqrt3$、$c=1/\sqrt3$、$s=\sqrt{2/3}$完成第一列，指出三个1向上汇集为$\sqrt3=\lVert\bm a_1\rVert$，再用第2、3行以$\rho=\sqrt2$、$c=\sqrt3/2$、$s=\tfrac12$消去$f_{3,2}$，写出最终增广矩阵。

5. 第5步回代并用原数据检查残差；例中$\bm R$恰为Cholesky因子$\bm L^\top$、$\bm t_{1:2}$恰为前代结果$\bm y$，得$\hat{\bm x}=(\tfrac76,\tfrac12)^\top$，$|t_3|=1/\sqrt6$为最小残差。

###### paragraph：新增观测的更新

1. 提出问题：已有$\bm R$与$\bm c_1$，新到观测行$\bm w^\top$与右端$\eta$，要求不重新处理旧观测而得到新的最小二乘解；由式`eq:ls-qr-residual-split`说明旧观测对$\bm x$的约束已由$\lVert\bm R\bm x-\bm c_1\rVert^2$表达、$\lVert\bm c_2\rVert^2$为常数，所以只需把新行逐个元素旋转并入$\bm R$。

2. 第1步把新行排在$[\bm R\mid\bm c_1]$下方；例中在三点之外新增点$(3,3)$，即$\bm w=(1,3)^\top$、$\eta=3$。

3. 第2步对$k=1,\ldots,d$用$\bm R$的第$k$行旋转消去新行第$k$个元素，同时旋转右端，并说明两行在前$k-1$列上都是零、已有的零不被破坏；例中$k=1$时$\rho=2$、$c=\sqrt3/2$、$s=\tfrac12$，$k=2$时$\rho=\sqrt5$、$c=\sqrt{2/5}$、$s=\sqrt{3/5}$，写出各次两行结果，指出右端剩下的$1/\sqrt{30}$是新观测带来的新增不可拟合部分。

4. 第3步回代：例中$\bm R=\left[\begin{smallmatrix}2&3\\0&\sqrt5\end{smallmatrix}\right]$、$\bm c_1=(4,3/\sqrt5)^\top$，得$\hat{\bm x}=(\tfrac{11}{10},\tfrac35)^\top$，与对四点直接求最小二乘相同，残差平方和由$\tfrac16$增至$\tfrac16+\tfrac1{30}=\tfrac15$。

5. 说明更新约需$3d^2$次运算且不需旧观测，重新处理全部$m+1$条观测则需$O(md^2)$。

##### 13.2.6.3 算法分析

1. 旋转正交且给出$(\rho,0)$；处理第$k$列时前$k-1$列的零与列内已消的零不被后续旋转改动，结束时得到QR分解，由定理`thm:ls-qr-least-squares`得最小二乘解；新增观测的更新同理是对全部$m+1$条观测的正交三角化，残差平方和只增加新行最后剩余分量的平方。

2. Givens QR后向稳定，稠密时约$3md^2-d^3$次运算、约为Householder的1.5倍；带状、上Hessenberg与局部更新需要的旋转少得多，选择依据是矩阵结构与更新方式。

### 13.3 SVD求解

1. 说明秩亏或秩未知时正规方程与QR回代不再适用，本节以最小范数最小二乘解为目标，由第7章的SVD因子构造解，再讨论加权与齐次目标。

#### 13.3.1 主要思想

1. 输入任意$\bm A$与$\bm b$、$\operatorname{rank}\bm A=r$，用完整SVD说明在输入、输出两组标准正交方向下$\bm A$只是逐坐标乘以$\sigma_i$。

2. 图`fig:ls-svd-solve-coordinates`：$m=4,d=3,r=2$时右端变到左奇异坐标，前$r$个坐标可拟合、其余留在残差中，可拟合坐标除以奇异值、零奇异方向取零，再由右奇异向量还原。

###### paragraph：目标在奇异坐标下分离

1. 用$\bm z=\bm V^\top\bm x$、$\bm c=\bm U^\top\bm b$把残差平方写成式`eq:ls-svd-coordinate-split`$\sum_{i\leq r}(c_i-\sigma_iz_i)^2+\sum_{i>r}c_i^2$，指出$z_{r+1},\ldots,z_d$不出现在目标中。

###### paragraph：逐个坐标求解

1. 各平方项互不耦合，对正奇异值取$z_i=c_i/\sigma_i$，输出端$i>r$的分量不可拟合，最小二乘解的全部自由度是输入零空间坐标。

###### paragraph：取最小范数

1. 由$\lVert\bm x\rVert=\lVert\bm z\rVert$令自由坐标为零，得式`eq:ls-svd-solution`$\bm x_\star=\sum_{i\leq r}(\bm u_i^\top\bm b/\sigma_i)\bm v_i$，读出“投影—取逆—重建”的执行顺序，它等于伪逆作用于右端的证明见算法分析。

#### 13.3.2 算法实现

1. 说明输入任意$\bm A,\bm b$、输出$\bm x_\star$、无额外规则，按精确秩描述，数值秩判定与截断小奇异值属于第17章；算法分为计算SVD、由奇异坐标求解两个模块（各为一个小小节），并取$\bm A=\left[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right]$、$\bm b=(1,3)^\top$演示，方程不相容且秩为1、最小二乘解不唯一。

##### 13.3.2.1 计算SVD

1. 调用数值SVD取得紧凑形式$\bm U_r\bm\Sigma_r\bm V_r^\top$，$\bm A=\bm0$时直接输出零。

2. 例中$\bm A=2\bm u_1\bm v_1^\top$、$\sigma_1=2$、$\bm u_1=\bm v_1=\tfrac1{\sqrt2}(1,1)^\top$，补齐的$\bm u_2=\bm v_2=\tfrac1{\sqrt2}(1,-1)^\top$对应零奇异值、不进入薄分解。

##### 13.3.2.2 由奇异坐标求解

1. 第1步投影右端$c_i=\bm u_i^\top\bm b$，其余方向上的部分留在残差中；例中$c_1=2\sqrt2$，被舍弃分量$\bm u_2^\top\bm b=-\sqrt2$。

2. 第2步只对正奇异值缩放$z_i=c_i/\sigma_i$；例中$z_1=\sqrt2$。

3. 第3步按式`eq:ls-svd-solution`还原$\bm x_\star=\bm V_r\bm z$；例中$\bm x_\star=(1,1)^\top$。

4. 第4步用原数据核验$\bm A^\top(\bm b-\bm A\bm x_\star)=\bm0$与$\bm x_\star\perp\ker\bm A$；例中拟合值$(2,2)^\top$取两观测平均，残差$(-1,1)^\top$与列空间正交、长度$\sqrt2$等于$|\bm u_2^\top\bm b|$，全部解$(1+t,1-t)^\top$的范数平方$2+2t^2$在$t=0$最小。

5. 说明全过程只用因子对向量的作用，不形成伪逆。

#### 13.3.3 算法分析

###### paragraph：正确性

1. 引出上述过程算出的正是伪逆作用于右端。

2. 定理`thm:ls-svd-solve`（SVD求解给出$\bm A^\dagger\bm b$）：输出等于$\bm A^\dagger\bm b$，是唯一最小范数最小二乘解。

3. 证明：与伪逆公式式`eq:matrix-analysis-pseudoinverse`逐项相同，最优性由定理`thm:matrix-analysis-pseudoinverse-minimum-norm`给出；也可直接验证残差与列空间正交且解位于$(\ker\bm A)^\perp$，由定理`thm:ls-minimum-norm-representative`得范数最小。

###### paragraph：数值敏感度

1. 右端扰动的放大至多$1/\sigma_r$；稳定地算出SVD不能消除问题本身的病态；截去真实正奇异值求的已不是$\bm A^\dagger\bm b$，属于第17章的截断SVD与正则化。

#### 13.3.4 加权最小二乘

##### 13.3.4.1 主要思想

1. 由第11章加权目标出发，把$\bm M=\bm R^\top\bm R$代入得白化式`eq:ls-weighted-whitening`$\lVert\bm R\bm A\bm x-\bm R\bm b\rVert^2$，对$\widetilde{\bm A}=\bm R\bm A$、$\widetilde{\bm b}=\bm R\bm b$调用SVD求解。

2. 说明$\bm R$的取法：Cholesky写作$\bm L\bm L^\top$时须取$\bm R=\bm L^\top$（取$\bm L$得$\bm L^\top\bm L\neq\bm M$），对角权取平方根，权以协方差逆$\bm\Gamma^{-1}$给出时分解$\bm\Gamma=\bm L\bm L^\top$、取$\bm R=\bm L^{-1}$并用前代求$\widetilde{\bm A},\widetilde{\bm b}$而不求逆。

3. 说明变换只作用于观测端、未知量不变，白化后的解无须变换回去，它为何是加权解中欧氏范数最小的代表见算法分析；权矩阵度量残差而非系数。

##### 13.3.4.2 算法实现

1. 说明输入、输出且无额外规则，取$\bm A=\left[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right]$、$\bm b=(0,2)^\top$、$\bm M=\operatorname{diag}(1,3)$演示：系数矩阵与SVD求解例相同，秩为1、加权解不唯一，两观测权重比$1:3$。

2. 第1步按三种形式之一构造权因子；例中$\bm R=\operatorname{diag}(1,\sqrt3)$。

3. 第2步按式`eq:ls-weighted-whitening`白化数据，协方差形式改用前代；例中写出$\widetilde{\bm A}$与$\widetilde{\bm b}=(0,2\sqrt3)^\top$。

4. 第3步对白化数据调用SVD求解（满列秩时也可QR）；例中唯一正奇异值$2\sqrt2$，左右奇异向量为$\tfrac12(1,\sqrt3)^\top$与$\tfrac1{\sqrt2}(1,1)^\top$，投影得3，缩放并还原得$\bm x_\star=(\tfrac34,\tfrac34)^\top$。

5. 第4步用原数据核验加权正规残差与$\bm x_\star\perp\ker\bm A$；例中拟合值$\tfrac32$是$0$与$2$按$1:3$的加权平均而非普通平均1，残差$(-\tfrac32,\tfrac12)^\top$满足$\bm A^\top\bm M\bm r=\bm0$、加权残差平方为3，核方向$(1,-1)^\top$上分量为零。

##### 13.3.4.3 算法分析

1. 变换前后目标逐点相等、未知量与范数不变，故最优解集与最小范数代表相同（定理`thm:ls-weighted-least-squares`）；$\bm R$可逆使$\ker\widetilde{\bm A}=\ker\bm A$；数值敏感度取决于$\bm R\bm A$，权重可能改善或恶化条件，应在变换后的系统上判断。

#### 13.3.5 齐次最小二乘

##### 13.3.5.1 主要思想

1. 由第11章齐次最小二乘出发，说明它是$\bm b=\bm0$的情形，单位长度约束排除零解，核心是选择被$\bm A$伸缩得最小的方向。

2. 用完整右奇异基写$\bm x=\bm V\bm z$，定义伸缩量$\hat\sigma_i=\lVert\bm A\bm v_i\rVert$（含$m<d$时多出的零伸缩方向），由$\bm A\bm v_i$两两正交得式`eq:ls-homogeneous-coordinates`，目标是平方伸缩量的加权平均、不小于$\hat\sigma_d^2$，在$\hat{\bm x}=\pm\bm v_d$处达到；何时还在别的方向达到留到算法分析。

##### 13.3.5.2 算法实现

1. 说明输入、输出且无额外规则，取$\bm A=\left[\begin{smallmatrix}3&0\\0&1\\0&0\end{smallmatrix}\right]$演示。

2. 第1步取得完整右因子并按伸缩量排序、检查维数与秩；$m<d$时须补齐右零空间，不能机械取薄SVD最后一列，也不经$\bm A^\top\bm A$的特征分解；例中两列正交，$\sigma_1=3,\sigma_2=1$，$\bm V=\bm I$，$m>d$无须补齐。

3. 第2步输出$\hat{\bm x}=\bm v_d$（有零空间时为零空间单位向量，否则为最小正奇异值方向），已是单位向量，$\pm\hat{\bm x}$表示同一比例；例中$\hat{\bm x}=\bm e_2$、$\lVert\bm A\hat{\bm x}\rVert=1$。

4. 第3步核验单位长度与最小伸缩量；例中约束下目标为$1+8x_1^2$，在$x_1=0$最小，最小残差为1，并说明零向量不满足约束。

5. 指出上例$m>d$、薄SVD已列出全部右奇异向量，引出$m<d$时第1步必须补齐的例子。

6. 示例（宽矩阵的齐次最小二乘）：$\bm A=\left[\begin{smallmatrix}1&0&0\\0&2&0\end{smallmatrix}\right]$，薄SVD只给$\bm e_2,\bm e_1$，补齐后得$\bm e_3$使残差为零；只看正奇异值而取$\bm e_1$则残差为1，漏掉真正的最小方向。

##### 13.3.5.3 算法分析

1. 正确性由定理`thm:ls-homogeneous-minimizers`（单位球面上的最小值为$\bm A^\top\bm A$的最小特征值）给出，加权平均论证进一步刻画全部最优解：最小伸缩量单重时只有$\pm\bm v_d$，重数大于一或零空间多维时应报告整个最优子空间；方向的敏感度由谱间隙控制，可用第9章子空间扰动界估计，检验按第11章进行。

### 13.4 本章小结

1. 回应章首问题：求最小二乘或最小范数解时不求逆、不显式形成不必要的矩阵，三条路线的区别在于怎样处理$\bm A$。

2. 正规方程化为对称正定方程交给Cholesky，可按行累计但使条件数平方；QR保持残差长度、满列秩回代、满行秩对转置分解得最小范数解。

3. 三种QR实现的差别（MGS可能失去正交性、Householder同号避免相消适合稠密、Givens适合稀疏与逐行更新）；SVD对任意秩给出$\bm A^\dagger\bm b$，加权经白化、齐次取完整右基中最小伸缩方向。

4. 结果须按目标在原数据上检验，但检验不说明误差大小；条件数平方与小奇异值放大的系统分析、数值秩与正则化在第17章，矩阵无法分解或只能作矩阵向量乘积时转向第14章起的迭代法。

## 第14章 定常迭代法

正文入口：[03-stationary-iterations.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/04-stationary-iterations.tex)。

1. 从可逆方阵$\bm A\in\mathbb R^{d\times d}$的方程$\bm A\bm x=\bm b$进入：第12章的直接法要存储分解因子，大型稀疏矩阵消元产生的填充使存储和运算难以承受。
2. 提出另一条路线：选一个易解且与$\bm A$相近的$\bm M$，每轮由当前残差解以$\bm M$为系数的方程求修正量，每轮只需一次矩阵乘向量和一次对角缩放或三角求解；由此列出本章要回答的问题：何时从任意初值收敛、收敛多快、每轮代价多大、何时停止。
3. 交代依赖：第10章证明了仿射迭代$\bm x\mapsto\bm T\bm x+\bm c$对任意初值收敛当且仅当$\rho(\bm T)<1$，渐近速度由谱半径决定、非正规时可能暂时放大误差；本章把各方法写成这种形式，三角求解采用第12章LU一节的前代与回代。
4. 说明各节分工：第一节建立修正方程、统一流程与谱半径判据；随后五节依次取标量矩阵、对角部分、下三角部分、带松弛参数的下三角修正与对称双向扫掠作为$\bm M$，各先简述所取的$\bm M$与迭代形式，再分算法实现、算法分析，算法实现逐步写出执行公式并在同一二维例子上逐轮计算。
5. 指出SSOR的修正矩阵对称正定，因而可作为第15章共轭梯度法的预条件；最后一节区分达到残差要求与仅仅停止计算。
6. 列出记号：$\bm x_\star$、$\bm x_k$、$\bm r_k=\bm b-\bm A\bm x_k$、$\bm\delta_k$、$\bm e_k=\bm x_k-\bm x_\star$与分量记法$(\bm x_k)_i$。

### 14.1 定常迭代

#### 14.1.1 算法思想

1. 概括定常迭代的两步思路：把方程拆成易解部分与其余部分并改写成不动点方程，再用同一个固定映射反复更新。

###### paragraph：矩阵分裂

1. 指出直接处理$\bm A^{-1}$约需$d^3$量级运算，把$\bm A$拆成$\bm A=\bm M-\bm N$（$\bm M$可逆且极易求解，如对角或三角矩阵），定义矩阵分裂；代入得$\bm M\bm x=\bm N\bm x+\bm b$，左乘$\bm M^{-1}$得不动点方程式`eq:ls-stationary-fixed-point`$\bm x=\bm T\bm x+\bm c$，定义迭代矩阵$\bm T=\bm M^{-1}\bm N=\bm I-\bm M^{-1}\bm A$与常向量$\bm c=\bm M^{-1}\bm b$。

###### paragraph：迭代求解

1. 由不动点方程写出递推式`eq:ls-stationary-iteration`$\bm x_{k+1}=\bm T\bm x_k+\bm c$，说明收敛时极限即原方程的解；因$\bm T,\bm c$固定不变而称为定常迭代，并与第15章Krylov子空间法每轮按残差重新计算方向与步长对照。

###### paragraph：修正的迭代求解

1. 说明$\bm M^{-1}$只是理论表示，乘回后得等价的修正形式式`eq:ls-stationary-correction`$\bm M\bm\delta_k=\bm r_k$、$\bm x_{k+1}=\bm x_k+\bm\delta_k$，每轮算一次残差并解一个以$\bm M$为系数的方程。

2. 由精确修正满足$\bm A\bm\delta=\bm r_k$说明$\bm M$代替$\bm A$只解近似修正方程，$\bm M$同时决定单步成本与误差消除程度，“易解”不保证收敛。

3. 列出输入、输出与事先给定的初值、容差、最大轮数和方法参数，计算$\bm r_0$与阈值$\tau$；每轮依次停止检查（达到容差、步数耗尽、数值异常、停滞四种状态）、按修正形式求$\bm\delta_k$、更新并按原方程重算残差，说明递推残差须定期重算，后面各方法只替换求$\bm\delta_k$的一步。

4. 说明先取对角矩阵作$\bm M$只为核对流程，选择理由留到Jacobi一节。

5. 例“定常迭代的贯穿例”：取$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$、$\bm b=(1,2)^\top$、$\bm x_0=\bm0$，精确解$(1/11,7/11)^\top$，$\bm M=\operatorname{diag}(4,3)=\bm D$。第一轮由$\bm r_0=(1,2)^\top$得$\bm\delta_0=(1/4,2/3)^\top$、$\bm x_1=(1/4,2/3)^\top$，重乘原矩阵得$\bm A\bm x_1=(5/3,9/4)^\top$、$\bm r_1=(-2/3,-1/4)^\top$。

6. 第二轮得$\bm\delta_1=(-1/6,-1/12)^\top$、$\bm x_2=(1/12,7/12)^\top$、$\bm r_2=(1/12,1/6)^\top$，残差范数约为$2.24$、$0.71$、$0.19$。

7. 指出每轮修正方程都精确解出而$\bm x_2$仍不是解，区分“修正已算出”与“方程已解完”，完成与否只能由原残差判断。

###### paragraph：按元素构造分裂

1. 统一约定$\bm A=\bm D+\bm L+\bm U$，$\bm L,\bm U$为保留原符号的严格下、上三角部分，并指出与文献中$\bm A=\bm D-\bm L-\bm U$约定差一个负号；凡除以对角元的方法要求$a_{i,i}\neq0$。

#### 14.1.2 算法分析

###### paragraph：误差传播

1. 用$\bm x_\star=\bm T\bm x_\star+\bm c$与递推相减得$\bm e_{k+1}=\bm T\bm e_k$，接上第10章的矩阵幂问题并引出收敛判据。

###### paragraph：收敛条件

1. 由迭代矩阵$\bm T=\bm I-\bm M^{-1}\bm A$每轮把误差变成什么引出收敛判据，说明后面各节只需估计各自的$\rho(\bm T)$。
2. 定理“定常迭代的收敛判据”：误差满足$\bm e_k=\bm T^k\bm e_0$，从任意初值收敛到$\bm x_\star$当且仅当$\rho(\bm T)<1$。证明由$\bm r_k=-\bm A\bm e_k$得误差递推，再说明仿射映射唯一的固定点就是$\bm x_\star$，引用第10章的共同极限判据。
3. 区分可执行与收敛：$a_{i,i}\neq0$不保证$\rho(\bm T)<1$，反之亦然。

###### paragraph：收敛速度与总成本

1. 由Gelfand公式，渐近速度由$\rho(\bm T)$控制，误差缩小十倍约需$1/\log_{10}(1/\rho(\bm T))$轮；非正规$\bm T$可能暂时放大误差，前几轮不能代替渐近判断。
2. 把收缩率与单步成本分开：总工作量约为轮数乘每轮成本，$\bm M$越接近$\bm A$谱半径通常越小但求解越贵，比较分裂时两者合起来看。

### 14.2 Richardson迭代

1. 取$\bm M=\alpha^{-1}\bm I$，由修正方程得$\bm\delta_k=\alpha\bm r_k$，写出更新式$\bm x_{k+1}=\bm x_k+\alpha(\bm b-\bm A\bm x_k)$与迭代矩阵$\bm T=\bm I-\alpha\bm A$；说明每个残差分量按同一比例转成修正，$\bm A$只通过矩阵乘向量进入，步长条件留给算法分析。

2. 说明$\bm M=\alpha^{-1}\bm I$时修正方程两边乘$\alpha$即得$\bm\delta_k=\alpha\bm r_k$，给出迭代公式$\bm x_{k+1}=(\bm I-\alpha\bm A)\bm x_k+\alpha\bm b$与迭代矩阵$\bm I-\alpha\bm A$。

#### 14.2.1 算法实现

1. 说明输入$\bm A,\bm b$、输出$\bm x$与预先选定的步长$\alpha$，停止检查与更新沿用14.1节的执行流程、只替换求修正量一步，并在贯穿例上取$\alpha=1/4$逐步演示前两轮。
2. 第1步核对步长：用对称正定的收敛保证时按谱界核对$0<\alpha<2/\lambda_{\max}$，经验步长不能写成收敛条件；例中由$\lambda_{\max}=(7+\sqrt5)/2<5$确认$1/4$在区间内。
3. 第2步求修正量$(\bm\delta_k)_i=\alpha(\bm r_k)_i$；例中由$\bm r_0=(1,2)^\top$得$\bm\delta_0=(1/4,1/2)^\top$。
4. 第3步更新并按分量重算残差$(\bm r_{k+1})_i=b_i-\sum_ja_{i,j}(\bm x_{k+1})_j$，说明重算残差兼作停止检查与下一轮输入、每轮一次矩阵乘向量；例中$\bm x_1=(1/4,1/2)^\top$，逐分量算出$\bm r_1=(-1/2,1/4)^\top$。
5. 第4步令$k\leftarrow k+1$回到停止检查；例中$\lVert\bm r_1\rVert_2\approx0.56$，第二轮得$\bm\delta_1=(-1/8,1/16)^\top$、$\bm x_2=(1/8,9/16)^\top$，逐分量算出$\bm r_2=(-1/16,3/16)^\top$。
6. 两轮后残差长度约$0.198$，误差$\bm e_2=(3/88,-13/176)^\top$长度约$0.081$；由$\bm e_k=-\bm A^{-1}\bm r_k$说明误差与残差是不同的数值对象。

#### 14.2.2 算法分析

###### paragraph：收敛条件与最优步长

1. 对称正定时把误差递推$\bm e_{k+1}=(\bm I-\alpha\bm A)\bm e_k$按正交特征基展开，特征值$\lambda_i$方向的倍率为$1-\alpha\lambda_i$，收敛条件与最优步长由这些倍率读出。
2. 定理“对称正定矩阵的Richardson迭代”：收敛当且仅当$0<\alpha<2/\lambda_{\max}$，最优步长$\alpha_\star=2/(\lambda_{\min}+\lambda_{\max})$，收缩因子$(\kappa_2-1)/(\kappa_2+1)$。证明由$\rho(\bm T)=\max_i|1-\alpha\lambda_i|$写出$q(\alpha)=\max\{|1-\alpha\lambda_{\min}|,|1-\alpha\lambda_{\max}|\}$，令两端倍率大小相等、符号相反求出$\alpha_\star$并代回。
3. 指出步长过大时大特征值方向倍率小于$-1$，误差正负交替放大，残差非零不意味着应加大修正。
4. 一般非对称矩阵仍用同一更新式，但特征值可能为复数、无正交特征基，步长区间不再直接适用，应回到$\rho(\bm I-\alpha\bm A)<1$检查。

###### paragraph：沿残差方向修正的含义

1. 对称正定时$\bm r_k$是$\phi(\bm x)=\tfrac12\bm x^\top\bm A\bm x-\bm b^\top\bm x$的负梯度，方法是固定步长的最速下降；残差范数平方的负梯度为$2\bm A^\top\bm r_k$，不能说沿残差方向使残差范数下降最快。

###### paragraph：收敛速度与代价

1. 谱范围越宽收敛越慢；谱端点未知时按谱界选步长；贯穿例中$\alpha=1/4$给出$\rho\approx0.40$，最优步长$2/7$给出$\sqrt5/7\approx0.32$；每轮约$2\operatorname{nnz}(\bm A)$次运算，残差与误差的关系留到第14.7节。

### 14.3 Jacobi迭代

1. 从Richardson没有利用各方程尺度进入，取$\bm M=\bm D$：第$i$个方程只修正$x_i$、其余分量取上一轮值，耦合方程拆成独立标量计算；写出修正方程$\bm D\bm\delta_k=\bm r_k$与迭代矩阵$\bm T_{\mathrm J}=\bm I-\bm D^{-1}\bm A=-\bm D^{-1}(\bm L+\bm U)$，并指出贯穿例所取的$\bm M$正是这个分裂。

###### paragraph：求修正量

1. 把对角修正方程$\bm D\bm\delta_k=\bm r_k$按元素写成矩阵形式，乘出得按行方程$a_{i,i}(\bm\delta_k)_i=(\bm r_k)_i$，与前代对比说明每个方程只含一个未知量，除以对角元得式`eq:ls-jacobi-correction`。

###### paragraph：迭代公式

1. 把修正加到当前近似得分量式`eq:ls-jacobi-update`$(\bm x_{k+1})_i=(\bm x_k)_i+(\bm r_k)_i/a_{i,i}$与向量式$\bm x_{k+1}=\bm x_k+\bm D^{-1}\bm r_k$，说明残差由旧向量算出，各分量可同时计算。

#### 14.3.1 算法实现

1. 说明输入、输出与沿用的执行流程，求修正量一步换成逐分量除以对角元；维护新旧两个向量，旧向量整轮只读，在贯穿例上标明每个代入值的轮次演示前两轮。
2. 第1步检查对角元非零并保存倒数，零对角元时当前排列不可执行、重排后须重核条件；例中$a_{1,1}=4$、$a_{2,2}=3$。
3. 第2步根据式`eq:ls-jacobi-update`用由旧向量算出的残差逐分量修正，各分量可并行；例中第一轮由$\bm r_0=(1,2)^\top$得$\bm x_1=(1/4,2/3)^\top$。
4. 第3步全部分量算完才整体替换并按分量重算残差，逐个覆盖就不再是Jacobi，单个分量变化小不能代替全局残差检查；例中逐分量得$\bm r_1=(-2/3,-1/4)^\top$，解释两个残差分量都变负是各分量假定对方不变而同时修正、修正过了头。
5. 第4步回到停止检查；例中$\lVert\bm r_1\rVert_2\approx0.71$，第二轮用$\bm r_1=(-2/3,-1/4)^\top$修正得$\bm x_2=(1/12,7/12)^\top$，重算$\bm r_2=(1/12,1/6)^\top$，与贯穿例一致。

#### 14.3.2 算法分析

###### paragraph：收敛条件

1. 由$\bm T_{\mathrm J}$第$i$行的元素$-a_{i,j}/a_{i,i}$引出行和范数，定义严格行对角占优。
2. 定理“Jacobi迭代的收敛条件”：严格行对角占优时$q=\lVert\bm T_{\mathrm J}\rVert_\infty<1$，$\lVert\bm e_k\rVert_\infty\leq q^k\lVert\bm e_0\rVert_\infty$；证明用最大行绝对值和与范数次乘性。
3. 贯穿例$q=1/3$；反例$\bm I+2\bm1\bm1^\top\in\mathbb R^{3\times3}$对称正定，而$\bm T_{\mathrm J}$沿$\bm1$的特征值为$-4/3$、其余为$2/3$，谱半径$4/3$，说明对称正定不保证Jacobi收敛。

###### paragraph：并行性

1. 各分量可并行，一轮工作量与$\operatorname{nnz}(\bm A)$同阶，但单步便宜不等于衰减快。

###### paragraph：数值敏感度

1. 修正要除以对角元，小对角元放大修正与其中的舍入误差。

### 14.4 Gauss--Seidel迭代

1. 从Jacobi求第$i$个分量的修正时只用本轮开始时的残差、没有计入本轮已求出的前面各分量修正进入：Gauss--Seidel按顺序处理各行，把已求出的修正立即计入后面的方程，原方程不变、只改变读取信息的时刻；这相当于取$\bm M=\bm D+\bm L$，比$\bm D$多保留严格下三角元素、更接近$\bm A$，而下三角方程仍可逐行前代求解。

补充图解：两种定常迭代在一次扫掠中读取的分量。每行对应一个待更新分量：蓝色非对角位置使用$x_j^{(k)}$，绿色位置使用本轮已更新的$x_j^{(k+1)}$；黄色对角元是本行的除数。箭头表示由上到下的更新顺序。

###### paragraph：求修正量

1. 把修正方程$(\bm D+\bm L)\bm\delta_k=\bm r_k$按元素写成下三角矩阵形式，乘出得第$i$行只含前$i$个分量的按行方程；把它作为第12章LU一节的下三角方程按前代求解，先由第一、二个方程依次解出$(\bm\delta_k)_1$与$(\bm\delta_k)_2$，一般地把已求出的前$i-1$个分量移到右边再除以$a_{i,i}$，得式`eq:ls-gauss-seidel-correction`。

2. 与Jacobi的式`eq:ls-jacobi-correction`比较，分子多减去前面各分量修正对第$i$个方程的影响，正是前$i-1$个分量修正之后第$i$个方程的残差，因而$(\bm\delta_k)_i$使该方程此刻恰好成立；代价是第$i$个分量必须等前$i-1$个算完，各分量不能再同时计算。

###### paragraph：迭代公式

1. 把修正加到当前近似上得分量式`eq:ls-gauss-seidel-update`与向量式$\bm x_{k+1}=\bm x_k+(\bm D+\bm L)^{-1}\bm r_k$，说明逆只是记号、计算时逐行前代；变量排列决定哪些元素落在$\bm L$或$\bm U$，重排改变$\bm M$本身，“用了较新的信息”只是直观理由，不能推出对所有矩阵都比Jacobi快。

#### 14.4.1 算法实现

1. 说明输入、输出与固定为$1,\ldots,d$的变量顺序，停止检查与残差重算沿用14.1节的执行流程，求修正量一步换成按顺序的前代；本轮$\bm r_k$整轮不变，修正量逐分量写入$\bm\delta_k$、整轮算完再加到$\bm x_k$上，在贯穿例上演示前两轮并与Jacobi对照。

2. 第1步与Jacobi相同检查所有对角元非零；例中$a_{1,1}=4$、$a_{2,2}=3$。

3. 第2步按式`eq:ls-gauss-seidel-correction`对$i=1,\ldots,d$依次求$(\bm\delta_k)_i$，指出前$i-1$个分量构成真正的计算依赖，右端始终是本轮开始时的$\bm r_k$，不能与部分更新后重算的残差混用；例中由$\bm r_0=(1,2)^\top$得$(\bm\delta_0)_1=1/4$、$(\bm\delta_0)_2=(2-1/4)/3=7/12$，第一分量与Jacobi相同，第二分量扣除了第一分量修正的影响$a_{2,1}(\bm\delta_0)_1=1/4$，所以比Jacobi的$2/3$小。

4. 第3步按式`eq:ls-gauss-seidel-update`更新并按原方程逐分量重算残差，并说明也可省去$\bm\delta_k$、在一个向量上原位逐分量更新并现算该行残差，前面位置已是新值、后面仍是旧值，结果相同；例中$\bm x_1=(1/4,7/12)^\top$、$\bm r_1=(-7/12,0)^\top$，解释第二个残差分量为零是最后求出的修正恰好使第二个方程成立，而第一个方程因第二分量随后改变而失配，末行满足不代表各行满足，停止判断须用完整残差。

5. 第4步令$k\leftarrow k+1$回到停止检查；例中$\lVert\bm r_1\rVert_2\approx0.58$，第二轮由$\bm r_1=(-7/12,0)^\top$求得$\bm\delta_1=(-7/48,7/144)^\top$，$\bm x_2=(5/48,91/144)^\top$，重算$\bm r_2=(-7/144,0)^\top$、长度约$0.049$，第二个残差分量再次为零，原因与第一轮相同。

#### 14.4.2 算法分析

###### paragraph：收敛条件

1. 由迭代公式的向量形式写出$\bm T_{\mathrm{GS}}=\bm I-(\bm D+\bm L)^{-1}\bm A=-(\bm D+\bm L)^{-1}\bm U$，第二个等号用到$(\bm D+\bm L)-\bm A=-\bm U$；由定理`thm:ls-stationary-convergence`只需说明$\rho(\bm T_{\mathrm{GS}})<1$，引出两类常用充分条件。

2. 定理“Gauss--Seidel迭代的收敛条件”（`thm:ls-gauss-seidel-convergence`）：严格行对角占优或实对称正定时收敛。证明一取模最大分量写出第$i$行关系导出与对角占优的矛盾；证明二用$\phi$的坐标能量下降$r_i^2/(2a_{i,i})$，说明整轮不降只能$\bm e_k=\bm0$，得$\bm A-\bm T_{\mathrm{GS}}^\top\bm A\bm T_{\mathrm{GS}}$正定，再对复特征向量取二次型得$(1-|\lambda|^2)\bm v^*\bm A\bm v>0$，故$|\lambda|<1$。

3. 补充对称正定时误差的能量范数每轮严格减小。

###### paragraph：收敛速度与代价

1. 速度取决于$\bm T_{\mathrm{GS}}$的谱且随变量排列变化；一轮一次三角扫掠，工作量与$\operatorname{nnz}(\bm A)$同阶，但行间有依赖、不像Jacobi那样直接并行；贯穿例$\rho(\bm T_{\mathrm{GS}})=1/12$小于Jacobi的$1/\sqrt{12}\approx0.289$。

2. 读图：左图Gauss--Seidel每个半步只改一个坐标并落在对应方程的直线上，迅速收拢到$\bm x_\star$，Jacobi在解两侧来回跳动；右图半对数坐标中误差大致沿直线下降，斜率对应谱半径；指出新值复用带来顺序依赖却不保证更快，存在Jacobi收敛而Gauss--Seidel发散的矩阵。

3. 图“定常迭代的路径与误差”（`fig:ls-stationary-iteration-paths`）：左为两条方程直线、Jacobi前四轮与Gauss--Seidel前三轮路径，右为Richardson（$\alpha=1/4$）、Jacobi、SOR（$\omega=6/5$）与Gauss--Seidel的误差半对数曲线，渐近斜率约$0.40$、$0.29$、$0.20$与$1/12$。

### 14.5 SOR迭代

1. 由Gauss--Seidel每个分量修正都恰好让当前方程成立、修正幅度固定进入，引入逐次超松弛迭代与固定松弛参数$\omega\neq0$：把每个分量的这一修正乘以$\omega$，以便在误差沿同一方向缓慢衰减时走得更快、或在修正过冲时更稳；这相当于把下三角修正矩阵的对角部分除以$\omega$，取$\bm M=\bm D/\omega+\bm L$，并解释$\omega=1$即Gauss--Seidel、$0<\omega<1$为欠松弛、$\omega>1$为过松弛，强调松弛参数改变修正而不改变目标方程。

###### paragraph：求修正量

1. 把修正方程$(\bm D/\omega+\bm L)\bm\delta_k=\bm r_k$按元素写出（对角元为$a_{i,i}/\omega$），列出第$i$行方程，两边乘$\omega$合成等价的$(\bm D+\omega\bm L)\bm\delta_k=\omega\bm r_k$；系数矩阵仍是下三角，按前代依次解出前两个分量，一般地把前$i-1$个已求出的分量移到右边再乘$\omega/a_{i,i}$，得式`eq:ls-sor-correction`。

2. 解释括号内仍是前$i-1$个分量修正之后第$i$个方程的残差，除以$a_{i,i}$即Gauss--Seidel此刻的修正，SOR再乘以$\omega$；$\omega=1$时逐项退化为式`eq:ls-gauss-seidel-correction`；前面的$(\bm\delta_k)_j$已是松弛后的修正，所以SOR不等于先做一轮Gauss--Seidel再把整个修正量乘以$\omega$。

###### paragraph：迭代公式

1. 把修正加到当前近似上得分量式`eq:ls-sor-update`与向量式$\bm x_{k+1}=\bm x_k+\omega(\bm D+\omega\bm L)^{-1}\bm r_k$。

#### 14.5.1 算法实现

1. 说明输入、输出与预先选定的$\omega$和固定为$1,\ldots,d$的变量顺序，沿用执行流程，求修正量一步换成带松弛参数的前代，本轮$\bm r_k$整轮不变，在贯穿例上取$\omega=6/5$演示前两轮。

2. 第1步核对对角元非零，并区分参数是否合格与矩阵是否满足假设两项检查：定理`thm:ls-sor-convergence`的对称正定保证要求$0<\omega<2$，同时要求$\bm A$确实对称正定；例中$\bm A$对称正定、$6/5\in(0,2)$。

3. 第2步按式`eq:ls-sor-correction`对$i=1,\ldots,d$依次求修正量，后面的行扣除前面已松弛的修正；例中$(\bm\delta_0)_1=3/10$、$(\bm\delta_0)_2=\tfrac25(2-3/10)=17/25$，第二行扣除的是松弛后的$3/10$而非Gauss--Seidel的$1/4$；对照先做整轮Gauss--Seidel再乘$\omega$得到的$(3/10,7/10)^\top$，说明那一般是另一种方法而不是SOR。

4. 第3步按式`eq:ls-sor-update`更新并按原方程重算残差，也可与Gauss--Seidel一样原位逐分量更新；例中$\bm x_1=(3/10,17/25)^\top$、$\bm r_1=(-22/25,-17/50)^\top$，第二个方程因修正被放大五分之一而不再恰好成立。

5. 第4步令$k\leftarrow k+1$回到停止检查；例中$\lVert\bm r_1\rVert_2\approx0.94$，第二轮由$\bm r_1$求得$\bm\delta_1=(-33/125,-19/625)^\top$，$\bm x_2=(9/250,406/625)^\top$，$\bm r_2=(129/625,19/1250)^\top$。

6. 比较两轮残差长度$0.94$、$0.21$与Gauss--Seidel的$0.58$、$0.049$，说明本例过松弛没有好处，有限轮算例只解释计算过程，参数优劣要由谱半径判断。

#### 14.5.2 算法分析

###### paragraph：收敛条件

1. 由迭代公式的向量形式得$\bm M^{-1}=\omega(\bm D+\omega\bm L)^{-1}$，写出$\bm T_\omega=\bm I-\omega(\bm D+\omega\bm L)^{-1}\bm A=(\bm D+\omega\bm L)^{-1}[(1-\omega)\bm D-\omega\bm U]$并核对第二个等号；说明$\omega$同时影响单个坐标的修正幅度与整轮误差传播，其取值范围对一般矩阵有一条必要条件、对实对称正定矩阵也是充分条件。

2. 定理“SOR迭代的收敛条件”（`thm:ls-sor-convergence`）：一般地$\rho(\bm T_\omega)\geq|1-\omega|$，故必要条件为$0<\omega<2$；对称正定且$0<\omega<2$时收敛。证明一由两个三角阵的行列式得$\det\bm T_\omega=(1-\omega)^d$；证明二算出步长$\omega r_i/a_{i,i}$下能量减少$\omega(2-\omega)r_i^2/(2a_{i,i})$，再沿用Gauss--Seidel的论证。

###### paragraph：参数选择与代价

1. 区间内收敛不等于比Gauss--Seidel快；三对角等特殊结构有由$\rho(\bm T_{\mathrm J})$给出的最优参数公式但不能普遍套用，贯穿例$\omega=6/5$使谱半径由$1/12$升到$0.2$；$\omega$接近端点时谱半径接近一；一轮成本与Gauss--Seidel同阶。

### 14.6 SSOR迭代

1. 由单向扫掠依赖变量顺序、$\bm M=\bm D/\omega+\bm L$不对称进入，对实对称正定$\bm A$引入对称逐次超松弛迭代：按$i=1,\ldots,d$做一次前向SOR得半步近似$\bm x_{k+1/2}$，再按$i=d,\ldots,1$做一次反向SOR得$\bm x_{k+1}$，参数取固定的$0<\omega<2$；记$\bm F=\bm D+\omega\bm L$（由对称性$\bm F^\top=\bm D+\omega\bm U$），预告算法分析将证明两次扫掠等价于修正矩阵$\bm M_{\mathrm{SSOR}}=\bm F\bm D^{-1}\bm F^\top/[\omega(2-\omega)]$，它是下三角、对角、上三角因子之积可逐个求解，又对称正定，可为第15章共轭梯度法提供预条件。

###### paragraph：求修正量

1. 修正方程$\bm M_{\mathrm{SSOR}}\bm\delta_k=\bm r_k$两边乘$\omega(2-\omega)$，令$\bm z=\bm\delta_k/(\omega(2-\omega))$、$\bm y=\bm D^{-1}\bm F^\top\bm z$，拆成两个三角方程：先前代解$\bm F\bm y=\bm r_k$，再回代解$\bm F^\top\bm z=\bm D\bm y$，最后$\bm\delta_k=\omega(2-\omega)\bm z$。

2. 按元素写出下三角因子$\bm F$（对角元取$a_{i,i}$、严格下三角元乘$\omega$），列出$\bm F\bm y=\bm r_k$的第$i$行方程，从$y_1=(\bm r_k)_1/a_{1,1}$起移项除以$a_{i,i}$，得前代式`eq:ls-ssor-forward`。

3. 由对称性写出$\bm F^\top$在$j>i$处的元素$\omega a_{i,j}$与右端$\bm D\bm y$的分量$a_{i,i}y_i$，列出第$i$行方程，这次从最后一个方程$z_d=y_d$起向上回代，得式`eq:ls-ssor-backward`，再乘常数得式`eq:ls-ssor-correction`。

###### paragraph：迭代公式

1. 把修正加到当前近似上得分量式`eq:ls-ssor-update`（$\bm z$由前代、回代依次求出）与向量式$\bm x_{k+1}=\bm x_k+\omega(2-\omega)\bm F^{-\top}\bm D\bm F^{-1}\bm r_k$。

#### 14.6.1 算法实现

1. 说明输入为实对称正定$\bm A$与$\bm b$、预先选定$\omega$，沿用执行流程，求修正量一步换成一次前代与一次回代，内部多两个与$\bm x$同长的向量$\bm y,\bm z$；在贯穿例上取$\omega=1$演示前两轮，此时$\bm F=\bm D+\bm L$、$\omega(2-\omega)=1$。

2. 第1步核对$\bm A$对称正定且$0<\omega<2$，正定矩阵的对角元都为正，所以各次除法都能执行；例中$a_{1,1}=4$、$a_{2,2}=3$、$\omega=1$。

3. 第2步按式`eq:ls-ssor-forward`由本轮开始时的残差对$i=1,\ldots,d$前代求$\bm y$；例中$y_1=1/4$、$y_2=7/12$，指出$\omega=1$时$\bm y$就是Gauss--Seidel的修正量$\bm\delta_0$。

4. 第3步按式`eq:ls-ssor-backward`对$i=d,\ldots,1$回代求$\bm z$，再按式`eq:ls-ssor-correction`乘$\omega(2-\omega)$得$\bm\delta_k$；例中先得$z_2=7/12$，再用它得$z_1=1/4-\tfrac14\cdot\tfrac7{12}=5/48$，$\bm\delta_0=(5/48,7/12)^\top$。

5. 第4步按式`eq:ls-ssor-update`更新并重算残差；例中$\bm x_1=(5/48,7/12)^\top$、$\bm r_1=(0,7/48)^\top$，按双向扫掠来看第一个分量为零是因为反向扫掠最后修正的是第一行。

6. 第5步回到停止检查；例中$\lVert\bm r_1\rVert_2\approx0.15$，第二轮前代得$\bm y=(0,7/144)^\top$、回代得$\bm z=(-7/576,7/144)^\top$，$\bm x_2=(53/576,91/144)^\top$，$\bm r_2=(0,7/576)^\top$；各三角子问题都精确解出而残差仍非零，验收用原方程残差，不能以子问题解完代替。

###### paragraph：双向扫掠

1. 给出代替第2、3步的等价实现：前向扫掠按式`eq:ls-sor-correction`由$\bm r_k$求$\bm\delta_{\mathrm f}$，得$\bm x_{k+1/2}$并按原方程算出半步残差$\bm r_{k+1/2}$；反向扫掠按$i=d,\ldots,1$扣除大下标分量已求出的修正求$(\bm\delta_{\mathrm b})_i$，右端必须是半步残差而非本轮开始时的$\bm r_k$；两次扫掠也可原位逐坐标更新、每行残差访问时现算，两次修正之和正是式`eq:ls-ssor-correction`的依据见算法分析。

2. 例中第一轮前向扫掠就是一轮Gauss--Seidel，$\bm x_{1/2}=(1/4,7/12)^\top$、$\bm r_{1/2}=(-7/12,0)^\top$；反向扫掠先得$(\bm\delta_{\mathrm b})_2=0$、再得$(\bm\delta_{\mathrm b})_1=-7/48$，$\bm x_1=(5/48,7/12)^\top$与因子求解一致，第二分量不变是因为前向扫掠的最后一步已让第二个方程成立。

###### paragraph：作为预条件

1. 作为共轭梯度法的预条件时SSOR不更新近似解，以外层残差$\bm r$代替$\bm r_k$，按式`eq:ls-ssor-forward`、`eq:ls-ssor-backward`前代、回代并缩放，返回$\bm M_{\mathrm{SSOR}}^{-1}\bm r$，近似解由外层方法更新；同一次外层求解中$\omega$与三角因子保持不变，否则预条件矩阵逐轮变化、外层依赖的固定内积结构不成立；具体用法见第15章预条件一节。

#### 14.6.2 算法分析

###### paragraph：修正矩阵

1. 说明要把两次扫掠的修正合并成一个修正矩阵并确定缩放常数，使独立迭代与预条件采用同一约定；前向半步是一次SOR，解$\bm F\bm\delta_{\mathrm f}=\omega\bm r_k$，反向半步因先访问大下标分量、本轮新值出现在上三角部分而解$\bm F^\top\bm\delta_{\mathrm b}=\omega\bm r_{k+1/2}$，右端为半步残差$\bm r_k-\bm A\bm\delta_{\mathrm f}$。

2. 把两次修正相加，在第一项前插入$\bm F^{-\top}\bm F^\top$、第二项中插入$\bm F\bm F^{-1}$，整理为$\omega\bm F^{-\top}(\bm F^\top+\bm F-\omega\bm A)\bm F^{-1}\bm r_k$，再由$\bm F^\top+\bm F-\omega\bm A=(2-\omega)\bm D$得整轮修正$\omega(2-\omega)\bm F^{-\top}\bm D\bm F^{-1}\bm r_k$，即$\bm M_{\mathrm{SSOR}}\bm\delta_k=\bm r_k$；求解次序为先解$\bm F$、乘$\bm D$、再解$\bm F^\top$，不显式形成矩阵或其逆，算法实现的第2、3步正按这一次序。

3. 由$\bm D\succ0$、$\bm F$可逆与$0<\omega<2$证明$\bm v^\top\bm M_{\mathrm{SSOR}}\bm v>0$，区分对称正定的修正矩阵与一般不对称的迭代矩阵。

###### paragraph：收敛性

1. 指出仅有$\bm M_{\mathrm{SSOR}}\succ0$不足以断言收敛；展开$\bm F\bm D^{-1}\bm F^\top$并减去$\omega(2-\omega)\bm A$，得$\omega(2-\omega)(\bm M_{\mathrm{SSOR}}-\bm A)=\bm C\bm D^{-1}\bm C^\top\succeq0$，$\bm C=(1-\omega)\bm D-\omega\bm L$，从而$\bm0\prec\bm A\preceq\bm M_{\mathrm{SSOR}}$。

2. 用正定平方根令$\bm S=\bm M_{\mathrm{SSOR}}^{-1/2}\bm A\bm M_{\mathrm{SSOR}}^{-1/2}$，由特征向量把特征值写成$\bm y^\top\bm A\bm y/\bm y^\top\bm M_{\mathrm{SSOR}}\bm y\in(0,1]$；迭代矩阵与$\bm I-\bm S$相似，特征值在$[0,1)$，故收敛，并说明迭代矩阵本身一般不对称、只是相似于对称矩阵。

###### paragraph：代价与用途

1. 一轮两次三角扫掠（或等价的前代、对角缩放与回代）加一次残差计算，约为SOR的两倍，只多一个中间向量；贯穿例$\omega=1$时谱半径与Gauss--Seidel同为$1/12$而成本加倍，说明不能只数轮数；SSOR的主要价值在对称正定修正矩阵，作为预条件是否划算要按外层总成本比较。

### 14.7 收敛检验与停止准则

1. 重申终止条件：残差达阈值表示达到要求，$k=K$只表示停止计算，两种情况都只输出当前$\bm x_k$，须报告结束状态，残差用真实$\bm b-\bm A\bm x_k$。
2. 列出不能代替残差检验的情形：修正量很小可能只是收缩因子接近一；残差长期不降应报告停滞；溢出或非数报告数值异常，通常提示发散或对角元过小。
3. 由$\bm x_\star-\bm x_k=\bm A^{-1}\bm r_k$说明残差小不等于误差小，误差界与后向误差留到第17章第一节；比较方法应按相同精度下的总工作量；递推维护残差的方法停止前须用真实残差复核。

### 14.8 本章小结

1. 回应章首问题：共同框架是矩阵分裂与修正方程$\bm M\bm\delta_k=\bm r_k$，误差乘迭代矩阵，由第10章结论对任意初值收敛当且仅当谱半径小于一，速度也由谱半径决定。
2. 汇总Richardson与Jacobi：前者只需矩阵乘向量，对称正定时步长条件为$0<\alpha<2/\lambda_{\max}$、最优收缩因子$(\kappa_2-1)/(\kappa_2+1)$；后者可并行，严格行对角占优保证收敛而对称正定不保证。
3. 汇总Gauss--Seidel、SOR与SSOR：前者相当于前代，对角占优或对称正定保证收敛；SOR的$0<\omega<2$对一般矩阵必要、对对称正定矩阵充分；SSOR的修正矩阵对称正定且不小于$\bm A$，由此收敛并可作预条件。
4. 说明边界：可执行不等于收敛，新信息与过松弛不自动更快（贯穿例中$1/12$与$0.2$的对比），比较须合并轮数与单轮成本。
5. 区分达到残差目标与仅停止，指出前向误差仍受条件数制约（第17章），并引向第15章用扩展子空间改善收敛速度。

## 第15章 Krylov子空间法

正文入口：[05-krylov-methods.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods.tex)（章首与章引言），依次输入[01-krylov-subspaces.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/01-krylov-subspaces.tex)（15.1）、[02-arnoldi.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/02-arnoldi.tex)（15.2）、[03-lanczos.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/03-lanczos.tex)（15.3）、[04-golub-kahan.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/04-golub-kahan.tex)（15.4）、[05-minres.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/05-minres.tex)（15.5）、[06-conjugate-gradient.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/06-conjugate-gradient.tex)（15.6）、[07-gmres.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/07-gmres.tex)（15.7）、[08-bicg.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/08-bicg.tex)（15.8）、[09-bicgstab.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/09-bicgstab.tex)（15.9）、[10-lsqr.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/10-lsqr.tex)（15.10）、[11-lsmr.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/11-lsmr.tex)（15.11）、[12-preconditioning.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/12-preconditioning.tex)（15.12）与[13-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/05-krylov-methods/13-summary.tex)（15.13）。

1. 从第14章的定常迭代进入：每轮算残差、解一次$\bm M\bm\delta_k=\bm r_k$并修正，残差用完即弃；指出历次残差及其矩阵乘积都携带解的信息，只用最新一个等于放弃已积累的方向。

2. 提出本章做法与三个问题：保留这些向量张成的子空间，在逐步扩大的子空间中按准则重新选近似；由此要回答怎样以数值上可靠的方式生成子空间的基，按什么准则选解及该准则对矩阵的要求，怎样只用固定数量的向量完成计算。

3. 说明各节先建立生成子空间基的工具，再给出使用这些基的求解方法：15.1建立Krylov子空间与残差多项式的对应并比较选解准则；随后三节给出生成基的过程，15.2的Arnoldi正交化对一般方阵把$\bm A\bm v_j$与全部已有基向量正交化，得标准正交基并把$\bm A$压缩成上Hessenberg小矩阵，原方程化为小型方程组或小型最小二乘问题，15.3的Lanczos过程是它在对称矩阵上的简化，只剩三项递推、小矩阵为对称三对角，15.4的Golub--Kahan双对角化针对残差与未知量不在同一空间的长方或秩亏最小二乘问题，交替作用$\bm A$与$\bm A^\top$在两个空间各生成一组标准正交基、把$\bm A$压缩成下双对角小矩阵；此后MINRES借Lanczos过程对对称（可不定）矩阵最小化原残差，对称正定矩阵还可用CG最小化误差的能量范数并借三对角矩阵的分解把递推压到只用上一步，GMRES借Arnoldi正交化对一般方阵最小化原残差而存储随步数增长，非对称而要固定存储时放弃残差最小化，BiCG借转置维持双正交，BiCGSTAB以局部残差平滑取代转置乘法，LSQR与LSMR借Golub--Kahan双对角化分别最小化原残差与正规残差。

4. 说明三个生成基的过程是求解方法共用的底层子空间工具，只给出基与压缩后的小矩阵，不作方程求解的输出；它们集中放在所有求解方法之前，读到求解方法时所需的基与小矩阵关系都已建立；最后一节讨论共用的预条件（改善谱分布，并以左预条件、右预条件或PCG的形式嵌入求解器），停止判断沿用14.7节以真实残差为准。

5. 交代依赖：第11章的正规方程、最小范数解与加权最小二乘，第13章的修正Gram--Schmidt与Givens旋转，第12章的三角代入与LU、Cholesky消元公式，第6章的实对称谱定理，第14章的停止准则、贯穿例与SSOR分裂；强调Krylov方法的步长与组合系数由当前向量算出，第10章固定误差矩阵的谱半径判据不能直接套用，收敛性要从各自的选解准则推出。

6. 重申记号（方阵$d\times d$、最小二乘$m\times d$，$\bm x_\star$、$\hat{\bm x}$、$\bm x_k$、$\bm r_k=\bm b-\bm A\bm x_k$），说明三个生成基的过程都按任务与递推、计算公式、分析、应用四部分展开，分析说明$\bm A$被压缩成怎样的小矩阵，应用说明小矩阵怎样用于求解方程；每种求解方法先在主要思想中给出计算公式，再在算法实现中逐步执行并结合贯穿例给出数值，最后在算法分析中说明正确性与收敛性。

### 15.1 Krylov子空间

1. 说明本节依次定义Krylov子空间与残差多项式、把残差尽量小转化为寻找多项式、讨论怎样选择多项式并由此对照定常迭代与本章各方法。

#### 15.1.1 Krylov子空间与残差多项式

1. 设$\bm A$可逆，由$\bm A(\bm x_\star-\bm x_0)=\bm r_0$得$\bm x_\star-\bm x_0=\bm A^{-1}\bm r_0$；$\bm A^{-1}$无法直接使用而矩阵乘向量容易，由此定义从$\bm r_0$反复乘$\bm A$张成的第$k$个Krylov子空间$\mathcal K_k(\bm A,\bm r_0)$，近似解取在$\bm x_0+\mathcal K_k$中，每增加一个基向量只需再乘一次$\bm A$。

2. 由$\bm x_k=\bm x_0+q_{k-1}(\bm A)\bm r_0$算出$\bm r_k=(\bm I-\bm A q_{k-1}(\bm A))\bm r_0$，令$p_k(t)=1-tq_{k-1}(t)$得$\bm r_k=p_k(\bm A)\bm r_0$，并解释$p_k(0)=1$对应“近似总是$\bm x_0$加修正”，$p_0=1$即不作修正。

3. 引理“Krylov残差多项式”（`lem:ls-krylov-residual-polynomial`，式`eq:ls-krylov-residual-polynomial`）：记$\mathcal P_k=\{p:\deg p\le k,\ p(0)=1\}$，候选解与$\mathcal P_k$中多项式双向对应；反向证明把$1-p_k(t)$写成$tq_{k-1}(t)$构造候选；结论是在$\bm x_0+\mathcal K_k$中选近似与在$\mathcal P_k$中选残差多项式是同一件事。

#### 15.1.2 残差多项式的目标

1. 承接$\bm r_k=p_k(\bm A)\bm r_0$，说明本小节讨论对固定的一轮$k$，$p_k$应满足什么要求才能使残差尽量小，并约定$p$与$p_k$的含义。

###### paragraph：残差多项式在特征方向上的分解

1. 定义矩阵多项式$p(\bm A)$，由$\bm A^j\bm v=\lambda^j\bm v$得$p(\bm A)\bm v=p(\lambda)\bm v$，再把$\bm r_0=\sum_i\xi_i\bm v_i$展开得$\bm r_k=\sum_i\xi_ip_k(\lambda_i)\bm v_i$，各方向分量互不干扰地乘以$p_k(\lambda_i)$。

###### paragraph：目标残差多项式

1. 把目标写成找$p_k$使$p_k(0)=1$且在各特征值处尽量小，说明$p_k(0)=1$使问题不平凡。

2. 由以$m$个不同特征值为根的$p_m$及低次多项式不能在$m$个点都为零，得出最优准则下的Krylov子空间法在精确算术下最大迭代次数就是不同特征值的个数$m\le d$；特征值少而集中时步数少，靠近原点的特征值最难处理，浮点计算依残差停止。

#### 15.1.3 残差多项式的选择策略

补充图解：贯穿例$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$的残差多项式。蓝线为Richardson两步的$(1-t/4)^2$，绿虚线为$1-7t/11+t^2/11$；圆点标记两个特征值处的值。二者均满足$p_2(0)=1$，只有后者在两个谱点同时为零。这是解释多项式自由度的解析对照，实际算法不需要预先知道特征值。

###### paragraph：定常迭代：由$p_k$得到$p_{k+1}$

1. Richardson满足$p_{k+1}(t)=(1-\alpha t)p_k(t)$，根固定为$1/\alpha$，好坏只能由谱半径判断，一般分裂由迭代矩阵的幂确定。

###### paragraph：Krylov子空间法：每一步重新选择

1. 在整个$\mathcal P_k$中选$p_k$，因$\mathcal P_{k-1}\subseteq\mathcal P_k$最优准则下不会变差，新多项式可与旧的完全不同；需要保留方向信息，由15.2—15.4的过程提供。

###### paragraph：贯穿例

1. 第一步$\bm x_1=c\bm r_0$、$p_1(t)=1-ct$：Richardson取$c=1/4$得因子约$-0.15$与$0.40$，取$c=2/7$则约$\mp0.32$。

2. 第二步Richardson得$p_2=(1-t/4)^2$、因子约$0.024$与$0.16$，残差不为零；Krylov法取以两个特征值为根的$p_2=1-\tfrac7{11}t+\tfrac1{11}t^2$，$c_0=7/11$、$c_1=-1/11$，得$\bm x_2=\bm x_\star$，且$p_2$不是$p_1$乘某个因子。

###### paragraph：选择策略

1. 说明实际中不知道特征值而用可计算的准则隐式选$p_k$，区分残差$\bm r_k=p_k(\bm A)\bm r_0$（可算）与误差$\bm e_k=p_k(\bm A)\bm e_0$（含未知$\bm x_\star$），按衡量对象分四类。

2. 第一类使误差最小：对称正定时$\lVert\bm e_k\rVert_{\bm A}^2=\bm r_k^\top\bm A^{-1}\bm r_k$，梯度条件只含残差即Galerkin条件，不必知道$\bm x_\star$；CG采用，欧氏残差不必单调。

3. 第二类使残差最小：只要求可逆、残差单调不增，MINRES、GMRES与LSQR采用。第三类使正规残差最小：LSQR的正规残差在病态问题中可能小幅波动，LSMR使其单调不增。

4. 第四类由正交条件确定：BiCG引入影子残差与$\bm A^\top$的Krylov子空间作检验空间，由$k$阶方程式`eq:ls-krylov-projection`代数地确定$p_k$（Petrov–Galerkin条件，Galerkin为其特例），不使任何长度最小、可能起伏或中断，BiCGSTAB每步乘$1-\omega_jt$缓和；最后汇总四类。

### 15.2 Arnoldi正交化

1. 从15.1的选解准则都要在$\mathcal K_k(\bm A,\bm r_0)$中计算进入，指出幂向量$\bm r_0,\bm A\bm r_0,\ldots$随次数增加趋于同一方向、不宜直接作基；对一般方阵引入Arnoldi正交化，逐个生成子空间的标准正交基，并把$\bm A$在子空间上的作用记录为上Hessenberg小矩阵；预告任务与正交化、计算公式、分析、应用四部分，并说明后两节的Lanczos过程与Golub--Kahan双对角化分别是它在对称矩阵与长方矩阵上的变形。

#### 15.2.1 任务与正交化

###### paragraph：任务

1. 给定不要求对称、只便于乘向量的方阵$\bm A\in\mathbb R^{d\times d}$，以及$\bm r_0\ne\bm0$与步数$k$；任务是生成标准正交的$\bm v_1,\ldots,\bm v_k$，使前$j$个张成$\mathcal K_j(\bm A,\bm r_0)$，起步取$\bm v_1=\bm r_0/\lVert\bm r_0\rVert_2$，此后每步只作一次矩阵乘向量；顺带得到的系数$h_{i,j}$组成上Hessenberg矩阵，其意义留到分析一小节。

###### paragraph：修正Gram--Schmidt正交化

1. 设已有标准正交的$\bm v_1,\ldots,\bm v_j$张成$\mathcal K_j$；由$\bm v_j$在$\bm A^{j-1}\bm r_0$上的系数非零得$\mathcal K_{j+1}=\mathcal K_j+\operatorname{span}\{\bm A\bm v_j\}$，所以新方向来自$\bm A\bm v_j$；作$\bm w=\bm A\bm v_j$，用第13章的修正Gram--Schmidt对$i=1,\ldots,j$依次按式`eq:ls-arnoldi-coefficients`取$h_{i,j}=\bm v_i^\top\bm w$并扣除$h_{i,j}\bm v_i$。

2. 说明每个内积都用已扣除前面分量的当前$\bm w$：由于已扣除的方向与$\bm v_i$正交，精确算术下与$h_{i,j}=\bm v_i^\top\bm A\bm v_j$相同，有限精度下正交性更好；余项与已有基都正交，按式`eq:ls-arnoldi-normalize`取$h_{j+1,j}=\lVert\bm w\rVert_2$并归一化得$\bm v_{j+1}$；把扣除的分量加回，得列关系式`eq:ls-arnoldi-column`$\bm A\bm v_j=\sum_{i\le j+1}h_{i,j}\bm v_i$。

###### paragraph：与全部旧基向量耦合

1. 指出一般方阵的$h_{i,j}$（$i\le j$）通常都不为零，新向量与全部旧基向量耦合：第$j$轮要与$\bm v_1,\ldots,\bm v_j$逐个求内积并扣除，整组基都须保存；预告15.3将说明对称时只有最近两项非零，扣除缩短为三项递推。

#### 15.2.2 计算过程

1. 说明按上一小节的推导每轮乘矩阵、逐个扣除、归一化，并在贯穿例上取$k=2$执行。

###### paragraph：变量

1. 列出全部基向量$\bm v_1,\ldots,\bm v_j$、工作向量$\bm w$、第$j$轮系数$h_{1,j},\ldots,h_{j+1,j}$与轮次$j$。

###### paragraph：初始化

1. $\bm v_1=\bm r_0/\lVert\bm r_0\rVert_2$、$j=1$；例中$\bm v_1=(1,2)^\top/\sqrt5$。

###### paragraph：每轮更新

1. 乘矩阵$\bm w=\bm A\bm v_j$；例中$(6,7)^\top/\sqrt5$。

2. 按式`eq:ls-arnoldi-coefficients`逐个扣除；例中$h_{1,1}=4$，余项$(2,-1)^\top/\sqrt5$。

3. 按式`eq:ls-arnoldi-normalize`归一化；例中$h_{2,1}=1$、$\bm v_2=(2,-1)^\top/\sqrt5$，第二轮$h_{1,2}=1$、$h_{2,2}=3$、$h_{3,2}=0$。

4. 停止：$h_{j+1,j}=0$或做满$k$轮时退出；例中第二轮退出。

5. 说明相消严重时的再正交化，例中不需要。

6. 给出最终结果$\bm V_2$与$\bm H_2=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$、$\bm A\bm V_2=\bm V_2\bm H_2$并逐列核对，指出小矩阵对称是因为$\bm A$对称。

#### 15.2.3 算法分析

###### paragraph：基矩阵与投影矩阵

1. 把基并排成$\bm V_k\in\mathbb R^{d\times k}$，说明$k\ll d$时它是瘦长矩阵，用$k$个坐标表示$k$维子空间；把列关系并排得矩阵形式式`eq:ls-arnoldi-relation`$\bm A\bm V_k=\bm V_{k+1}\overline{\bm H}_k=\bm V_k\bm H_k+h_{k+1,k}\bm v_{k+1}\bm e_k^\top$，以$k=3$写出各矩阵，并由$\bm A\bm v_j$只用前$j+1$个基向量说明上Hessenberg形是生成过程的结果。

2. 图“Arnoldi关系中各矩阵的形状”（`fig:ls-arnoldi-relation-shapes`）：示意$d=7$、$k=4$，$\overline{\bm H}_k$的非零元只在主对角线、其上方与下次对角线上，末行只剩$h_{k+1,k}$，绿色标出$\bm A\bm v_2$只用到$\bm v_1,\bm v_2,\bm v_3$。

3. 左乘$\bm V_k^\top$得$\bm H_k=\bm V_k^\top\bm A\bm V_k$，解释它是$\bm A$在$\mathcal K_k$上的投影：子空间中$\bm z=\bm V_k\bm y$的像在子空间中的坐标为$\bm H_k\bm y$，伸出的部分只沿$\bm v_{k+1}$、大小由$h_{k+1,k}$记录；$d$维矩阵的作用由此压缩成$k$阶上Hessenberg矩阵。

###### paragraph：正确性

1. 指出上面的论证用到此前各步的基已标准正交，需要归纳确认。定理“Arnoldi关系”（`thm:ls-arnoldi-relation`）：精确算术下执行$k$轮且前$k-1$轮次对角元非零；$h_{k+1,k}\ne0$时$\bm v_1,\ldots,\bm v_{k+1}$标准正交、逐级张成$\mathcal K_j$，式`eq:ls-arnoldi-relation`成立且$\bm H_k=\bm V_k^\top\bm A\bm V_k$；$h_{k+1,k}=0$时$\bm A\bm V_k=\bm V_k\bm H_k$、$\mathcal K_k$不变，$\bm A$非奇异时$\bm x_\star\in\bm x_0+\mathcal K_k$。

2. 证明分三部分：正交性由第$i$次扣除后$\bm w\perp\bm v_i$且此后扣除的方向都与$\bm v_i$正交得到；张成由$\bm v_{j+1}\in\operatorname{span}\{\bm A\bm v_j,\bm v_1,\ldots,\bm v_j\}\subseteq\mathcal K_{j+1}$及维数比较得到，加回扣除分量得矩阵关系；不再扩张时$\bm A\mathcal K_k\subseteq\mathcal K_k$，非奇异时由单射得满射，$\bm r_0$在$\mathcal K_k$中有原像。

3. 说明维数上限使至多$d$轮出现$h_{k+1,k}=0$，此时精确解已在候选集合中，求解器在这一步得精确解，但仍须用原残差确认。

###### paragraph：数值敏感度

1. 有限精度下基的正交性逐渐损失，判断与补救沿用第13章对修正Gram--Schmidt的讨论，必要时按每轮的更新所述再正交化；Arnoldi本来就保存全部基，补救的代价只是多做一遍投影。

###### paragraph：计算代价

1. 每轮一次矩阵乘向量；第$j$轮扣除约$4dj$次运算、$k$轮约$2dk^2$次，保存$\bm V_{k+1}$约$(k+1)d$个数，两者都随轮数增长，原因是整组基要保存并参与扣除；本过程只生成候选空间，收敛快慢由调用它的求解器的选解准则决定。

#### 15.2.4 应用

1. 把近似写成$\bm x_k=\bm x_0+\bm V_k\bm y$，由$\bm r_0=\bm V_{k+1}\lVert\bm r_0\rVert_2\bm e_1$与关系`eq:ls-arnoldi-relation`把残差写成$\bm V_{k+1}(\lVert\bm r_0\rVert_2\bm e_1-\overline{\bm H}_k\bm y)$，$d$维残差由$k+1$个坐标表示，15.1的准则都可在这个小问题上实现。

2. 按Galerkin条件，由$\bm H_k=\bm V_k^\top\bm A\bm V_k$得$k$阶上Hessenberg方程组$\bm H_k\bm y=\lVert\bm r_0\rVert_2\bm e_1$，但非对称时没有极小性、$\bm H_k$可能奇异；按极小残差条件，$\bm V_{k+1}$保长，问题化为$(k+1)\times k$小最小二乘问题$\min_{\bm y}\lVert\lVert\bm r_0\rVert_2\bm e_1-\overline{\bm H}_k\bm y\rVert_2$，对非奇异$\bm A$有唯一解，这就是15.7 GMRES的做法，每增一列只需一次新的Givens旋转延续三角化。

3. 指出两种用法都要用$\bm V_k$还原$\bm x_k$，存储与正交化工作随步数增长，实际常做满$m$步后以当前近似重新开始（重启），以失去跨周期最优性为代价限制存储；预告对称时$\bm H_k$成为对称三对角矩阵、扣除只剩三项、基不必全部保存。

### 15.3 Lanczos过程

1. 从Arnoldi正交化每轮都要与全部旧基向量正交化的代价进入，指出$\bm A$对称时大部分系数自动为零；引入Lanczos过程作为Arnoldi在对称矩阵上的简化：每轮只扣除两个方向，生成同一组标准正交基，并把$\bm A$的作用记录为对称三对角小矩阵；预告任务与三项递推、计算公式、分析、应用四部分，与Arnoldi相同的论证只作引用。

#### 15.3.1 主要思想

1. 说明任务与Arnoldi正交化相同而矩阵对称：生成标准正交的$\bm v_1,\ldots,\bm v_k$，起步$\bm v_1=\bm r_0/\lVert\bm r_0\rVert_2$。

补充图解：Lanczos过程在精确算术下的局部关系。左侧$\bm A\bm v_j$由$\bm v_{j-1},\bm v_j,\bm v_{j+1}$三个方向组成；右侧对称三对角矩阵$\bm T_k$只在主对角线和相邻两条对角线上可能非零。有限精度下可能需要重新正交化，图示不代表舍入后仍自动保持全局正交。

###### paragraph：三项递推

1. 从Arnoldi系数$h_{i,j}=\bm v_i^\top\bm A\bm v_j$与列关系`eq:ls-arnoldi-column`出发，由对称性$h_{i,j}=(\bm A\bm v_i)^\top\bm v_j$得$i<j-1$时为零、$h_{j-1,j}=h_{j,j-1}$，记$a_j,\gamma_j$得Lanczos三项递推式`eq:ls-arnoldi-lanczos`。

#### 15.3.2 算法实现

1. 说明每轮乘矩阵、扣除两个方向、归一化，在贯穿例上取$k=2$执行。

###### paragraph：变量

1. 列出$\bm v_{j-1},\bm v_j$、工作向量$\bm w$、$a_j$、$\gamma_j$与轮次$j$。

###### paragraph：初始化

1. $\bm v_0=\bm0$、$\gamma_0=0$、$\bm v_1=\bm r_0/\lVert\bm r_0\rVert_2$、$j=1$；例中$\bm v_1=(1,2)^\top/\sqrt5$。

###### paragraph：每轮更新

1. 乘矩阵、求对角元、扣除两个方向、归一化四步，每步给出例中数值：第一轮$a_1=4$、$\gamma_1=1$、$\bm v_2=(2,-1)^\top/\sqrt5$，第二轮$a_2=3$、$\gamma_2=0$。

2. 停止：$\gamma_j=0$或做满$k$轮时退出；四步合写为式`eq:ls-lanczos-step`，并说明修正Gram–Schmidt变体。

3. 最终得$\bm V_2$与$\bm T_2=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$、$\bm A\bm V_2=\bm V_2\bm T_2$，逐列核对，与Arnoldi算出的$\bm H_2$相同而每轮只扣两个方向。

#### 15.3.3 算法分析

###### paragraph：基矩阵与投影矩阵

1. 与15.2一样把基并排成瘦长矩阵$\bm V_k$，由三项递推并排得矩阵形式式`eq:ls-arnoldi-tridiagonal`$\bm A\bm V_k=\bm V_k\bm T_k+\gamma_k\bm v_{k+1}\bm e_k^\top=\bm V_{k+1}\overline{\bm T}_k$，写出对称三对角的$\bm T_k$，$\overline{\bm T}_k$在其下添一行$\gamma_k\bm e_k^\top$；左乘$\bm V_k^\top$得$\bm T_k=\bm V_k^\top\bm A\bm V_k$。

2. 说明这就是Arnoldi关系`eq:ls-arnoldi-relation`的对称情形，$\overline{\bm H}_k=\overline{\bm T}_k$、$\bm H_k=\bm T_k$；$\bm T_k$同样是$\bm A$在$\mathcal K_k$上的投影，上Hessenberg又对称，因而是三对角的，$d$维对称矩阵的作用被压缩成只需$2k-1$个数$a_1,\ldots,a_k,\gamma_1,\ldots,\gamma_{k-1}$记录的$k$阶矩阵。

###### paragraph：正确性

1. 指出推导三项递推时用到的基的正交性原由完整扣除保证，只扣两项时需重新确认。定理“Lanczos关系”（`thm:ls-arnoldi-lanczos`）：$\bm A$对称、$\bm r_0\ne\bm0$，精确算术下按式`eq:ls-lanczos-step`执行$k$轮且$\gamma_1,\ldots,\gamma_{k-1}$非零；$\gamma_k\ne0$时$\bm v_1,\ldots,\bm v_{k+1}$标准正交、逐级张成$\mathcal K_j$，式`eq:ls-arnoldi-tridiagonal`成立且$\bm T_k=\bm V_k^\top\bm A\bm V_k$；$\gamma_k=0$时$\bm A\bm V_k=\bm V_k\bm T_k$、$\mathcal K_k$不变，非奇异时$\bm x_\star\in\bm x_0+\mathcal K_k$。

2. 证明正交性：对$j$归纳，$i=j$时由$a_j$的定义得$\bm v_j^\top\hat{\bm w}=0$；$i<j$时用对称性与$\bm A\bm v_i$的三项展开算出$\bm v_i^\top\bm A\bm v_j$在$i=j-1$时为$\gamma_{j-1}$、$i<j-1$时为零，于是$\hat{\bm w}$与$\bm v_{j-1}$的内积为$\gamma_{j-1}-\gamma_{j-1}=0$，与更早的基的三项内积都为零。

3. 证明张成与矩阵关系：由$\bm v_{j+1}\in\operatorname{span}\{\bm A\bm v_j,\bm v_j,\bm v_{j-1}\}\subseteq\mathcal K_{j+1}$与维数比较得张成，加回扣除的两项得递推并并排成矩阵关系；不再扩张的情形同Arnoldi，由单射得满射。

4. 说明定理表明精确算术下只扣两项与扣除全部分量结果相同，被省略的系数本来为零；对称时15.2的上Hessenberg矩阵退化为$\bm T_k$，两种过程给出相同的基与系数，贯穿例上两节的数值完全一致；至多$d$轮出现$\gamma_k=0$。

###### paragraph：数值敏感度

1. 有限精度下三项递推只对最近两个方向扣除，舍入引入的旧方向分量不被去掉并随迭代放大，正交性损失比完整正交化明显，典型表现是$\bm T_k$出现$\bm A$同一特征值的多个近似副本；保存全部基再正交化可补救但失去固定存储，不保存基时求解器只能靠真实残差复核。

###### paragraph：计算代价

1. 每轮一次矩阵乘向量，另有两次内积、两次向量更新与一次缩放，约$9d$次运算；除矩阵外只存$\bm v_{j-1},\bm v_j,\bm w$三个向量，存储不随轮数增长；与Arnoldi$k$轮约$2dk^2$次运算、$(k+1)d$个数的存储相比，这是利用对称性的主要收益。

#### 15.3.4 应用

1. 用法同15.2的应用一小节：把近似写成$\bm x_k=\bm x_0+\bm V_k\bm y$，按Galerkin条件，由$\bm r_0=\lVert\bm r_0\rVert_2\bm v_1$与$\bm T_k=\bm V_k^\top\bm A\bm V_k$得三对角方程组式`eq:ls-lanczos-projected-system`$\bm T_k\bm y=\lVert\bm r_0\rVert_2\bm e_1$，用第12章的消元约$O(k)$次运算解出，再用$\bm V_k$还原$\bm x_k$。

2. 说明这是两种对称求解器的共同骨架：对称正定时$\bm T_k$正定、方程有唯一解，所得近似即15.6 CG的迭代值，CG借$\bm T_k$分解随步数延伸的结构把求解与还原合并为短递推、不必保存基；对称不定时$\bm T_k$可能奇异，15.5的MINRES改用$\overline{\bm T}_k$求$\min_{\bm y}\lVert\lVert\bm r_0\rVert_2\bm e_1-\overline{\bm T}_k\bm y\rVert_2$；两者的子空间、基与三对角矩阵都来自同一个Lanczos过程，区别只在确定坐标的准则。

### 15.4 Golub--Kahan双对角化

1. 从Arnoldi与Lanczos都针对方阵、残差与未知量同在$d$维空间进入，指出长方或秩亏最小二乘问题中残差在$m$维数据空间、未知量在$d$维空间，不能把残差反复乘$\bm A$，送回未知量空间的是$\bm A^\top$，所需的是$\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$；对$\bm A^\top\bm A$作Lanczos会因形成它而损失信息，于是引入交替作用$\bm A$与$\bm A^\top$的Golub--Kahan双对角化，得到与之相同的基并把$\bm A$压缩成双对角小矩阵；预告主要思想、计算过程、算法分析、应用四部分。

#### 15.4.1 主要思想

1. 给定可以秩亏的$\bm A\in\mathbb R^{m\times d}$、$\bm b\in\mathbb R^m$与步数$k$，取零初值、初始残差即$\bm b$；要在数据空间生成标准正交的$\bm u_1,\ldots,\bm u_{k+1}$、在未知量空间生成配对的标准正交$\bm v_1,\ldots,\bm v_k$，使前$j$个$\bm v$张成$\mathcal K_j(\bm A^\top\bm A,\bm A^\top\bm b)$，第一对取$\bm u_1=\bm b/\lVert\bm b\rVert_2$、$\bm v_1$为$\bm A^\top\bm u_1$的方向。

###### paragraph：交替的两项递推

1. 仿照Arnoldi，$\bm u_{j+1}$由$\bm A\bm v_j$对$\bm u_1,\ldots,\bm u_j$正交化、$\bm v_{j+1}$由$\bm A^\top\bm u_{j+1}$对$\bm v_1,\ldots,\bm v_j$正交化；由$\bm u_i^\top\bm A\bm v_j=(\bm A^\top\bm u_i)^\top\bm v_j$与$\bm v_i^\top\bm A^\top\bm u_{j+1}=(\bm A\bm v_i)^\top\bm u_{j+1}$，且$\bm A^\top\bm u_i\in\operatorname{span}\{\bm v_1,\ldots,\bm v_i\}$、$\bm A\bm v_i\in\operatorname{span}\{\bm u_1,\ldots,\bm u_{i+1}\}$，$i<j$的系数都为零，每个新向量只需扣除对面空间中相邻的一个方向。

2. 写出列关系式`eq:ls-golub-kahan-columns`$\bm A\bm v_i=\alpha_i\bm u_i+\beta_{i+1}\bm u_{i+1}$、$\bm A^\top\bm u_i=\beta_i\bm v_{i-1}+\alpha_i\bm v_i$（$\bm v_0=\bm0$，系数非负），说明扣除用的系数就是上一步的归一化系数而不必另作内积；与Arnoldi列关系`eq:ls-arnoldi-column`对照，不必保存整组基，原因与Lanczos只需三项相同，右侧基正是$\bm A^\top\bm A$的Lanczos基。

#### 15.4.2 计算过程

1. 由列关系移项，每轮先作一次$\bm A$乘向量、扣除一个方向并归一化得新的$\bm u$，再作一次$\bm A^\top$乘向量、扣除一个方向并归一化得新的$\bm v$；在不相容长方系统$\bm A=\left[\begin{smallmatrix}1&0\\0&2\\0&0\end{smallmatrix}\right]$、$\bm b=(1,1,1)^\top$上执行，其最小二乘解$\hat{\bm x}=(1,1/2)^\top$、最优残差$(0,0,1)^\top$，15.10与15.11继续沿用以便对照。

###### paragraph：变量

1. 以列表列出：当前基向量$\bm u_j\in\mathbb R^m$、$\bm v_j\in\mathbb R^d$（是否保存整组基由调用者决定），存放余项的工作向量$\bm p\in\mathbb R^m$、$\bm q\in\mathbb R^d$，对角元$\alpha_j$（$\bm v_j$的归一化系数），次对角元$\beta_j$（$\bm u_j$的归一化系数），轮次$j$。

###### paragraph：初始化

1. 把$\bm u_1$初始化为$\bm b$的方向，由列关系第二式在$i=1$时把$\bm v_1$初始化为$\bm A^\top\bm u_1$的方向，即式`eq:ls-golub-kahan-start`$\beta_1=\lVert\bm b\rVert_2$、$\bm u_1=\bm b/\beta_1$、$\alpha_1=\lVert\bm A^\top\bm u_1\rVert_2$、$\bm v_1=\bm A^\top\bm u_1/\alpha_1$、$j=1$；$\bm b=\bm0$或$\alpha_1=0$（零向量已满足正规方程`eq:linear-algebra-normal-equations`）时由求解器直接输出零向量；例中$\beta_1=\sqrt3$、$\bm u_1=(1,1,1)^\top/\sqrt3$、$\alpha_1=\sqrt{5/3}$、$\bm v_1=(1,2)^\top/\sqrt5$。

###### paragraph：每轮更新

1. 第$j$轮依次：送到数据空间并扣除，$\bm p=\bm A\bm v_j-\alpha_j\bm u_j$；归一化得$\beta_{j+1}=\lVert\bm p\rVert_2$、$\bm u_{j+1}=\bm p/\beta_{j+1}$；送回未知量空间并扣除，$\bm q=\bm A^\top\bm u_{j+1}-\beta_{j+1}\bm v_j$；归一化得$\alpha_{j+1}=\lVert\bm q\rVert_2$、$\bm v_{j+1}=\bm q/\alpha_{j+1}$，交出系数后令$j\leftarrow j+1$；每步给出例中第一轮的值$\bm p=(-2,7,-5)^\top/(3\sqrt5)$、$\beta_2\approx1.3166$、$\bm u_2=(-2,7,-5)^\top/\sqrt{78}$、$\bm q=18(-2,1)^\top/(5\sqrt{78})$、$\alpha_2\approx0.9115$、$\bm v_2=(-2,1)^\top/\sqrt5$，以及第二轮的$\beta_3=\sqrt{10/13}\approx0.8771$、$\bm u_3=(-4,1,3)^\top/\sqrt{26}$与$\bm q=\bm0$、$\alpha_3=0$。

2. 停止：$\beta_{j+1}=0$时约定$\alpha_{j+1}=0$并退出，$\beta_{j+1}>0$而$\alpha_{j+1}=0$时不生成$\bm v_{j+1}$并退出，否则在求解器决定继续时进入下一轮，至多$k$轮；略去未生成的基向量后列关系仍成立，求解器照常用本轮系数完成解的更新；强调基停止扩张不等于原残差为零；例中$\alpha_3=0$，未知量空间已被取尽。第1—4步合为式`eq:ls-golub-kahan-step`。

3. 最终结果：例中$\bm V_2=\frac1{\sqrt5}\left[\begin{smallmatrix}1&-2\\2&1\end{smallmatrix}\right]$、$\bm B_2\approx\left[\begin{smallmatrix}1.2910&0\\1.3166&0.9115\\0&0.8771\end{smallmatrix}\right]$，单独一行写出$\bm A\bm V_2=\bm U_3\bm B_2$并逐列核对，指出$\bm b$的第三个分量仍不可拟合、原残差不会降到零。

4. 转向稠密矩阵，说明可以只用双对角系数核对计算。例“直线拟合上的两步双对角化”（`ex:ls-golub-kahan-line`）：沿用`ex:ls-line-least-squares`的$\bm A$与$\bm b=(1,2,2)^\top$，起步$\beta_1=3$、$\alpha_1=\sqrt{61}/3\approx2.6034$、$\bm v_1=(5,6)^\top/\sqrt{61}$；第一轮$\beta_2\approx0.5944$、$\alpha_2\approx0.7446$、$\bm v_2=(-6,5)^\top/\sqrt{61}$，第二轮$\beta_3\approx0.5607$而$\alpha_3=0$；由$\bm A=\bm U_3\bm B_2\bm V_2^\top$知$\bm B_2^\top\bm B_2$与$\bm A^\top\bm A$有相同的迹$8$与行列式$6$，数值核对两个不变量吻合，不必重新比较各个基向量。

#### 15.4.3 算法分析

###### paragraph：基矩阵与投影矩阵

1. 把两组基并排成瘦长矩阵$\bm U_{k+1}\in\mathbb R^{m\times(k+1)}$、$\bm V_k\in\mathbb R^{d\times k}$，由两条列关系并排得式`eq:ls-golub-kahan-relations`$\bm A\bm V_k=\bm U_{k+1}\bm B_k$、$\bm A^\top\bm U_{k+1}=\bm V_k\bm B_k^\top+\alpha_{k+1}\bm v_{k+1}\bm e_{k+1}^\top$，写出$(k+1)\times k$下双对角$\bm B_k$（第$i$列只有$\alpha_i$与$\beta_{i+1}$），说明边界项来自$\bm u_{k+1}$被送回时的新方向。

2. 左乘$\bm U_{k+1}^\top$得$\bm B_k=\bm U_{k+1}^\top\bm A\bm V_k$，解释它是$\bm A$从$\operatorname{range}(\bm V_k)$到$\operatorname{range}(\bm U_{k+1})$的坐标矩阵，$m\times d$长方矩阵被压缩成只需$2k$个数的双对角矩阵；再由第一式得$\bm V_k^\top\bm A^\top\bm A\bm V_k=\bm B_k^\top\bm B_k$，它是对角元$\alpha_i^2+\beta_{i+1}^2$、次对角元$\alpha_{i+1}\beta_{i+1}$的对称三对角矩阵，相当于对$\bm A^\top\bm A$作Lanczos得到的$\bm T_k$。

###### paragraph：正确性

1. 指出上面的论证用到两组基的标准正交性而每步只扣一项。定理“Golub--Kahan关系”（`thm:ls-golub-kahan-relations`）：$\alpha_1,\ldots,\alpha_k$与$\beta_2,\ldots,\beta_{k+1}$都为正时，精确算术下$\bm U_{k+1}$、$\bm V_k$的列分别标准正交，式`eq:ls-golub-kahan-relations`成立（$\alpha_{k+1}=0$时末项为零），且$\operatorname{range}(\bm V_k)=\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$。

2. 证明分三步：矩阵关系只是列关系的汇总，第二式第$k+1$列中$\alpha_{k+1}\bm v_{k+1}$单独写成边界项；正交性对轮数归纳，用列关系算出$\beta_{k+1}\bm u_j^\top\bm u_{k+1}=0$，再借刚证得的$\bm u$的正交性算出$\alpha_{k+1}\bm v_j^\top\bm v_{k+1}=0$；张成的空间由$\bm v_1\parallel\bm A^\top\bm b$与三项关系$\alpha_{i+1}\beta_{i+1}\bm v_{i+1}=\bm A^\top\bm A\bm v_i-(\alpha_i^2+\beta_{i+1}^2)\bm v_i-\alpha_i\beta_i\bm v_{i-1}$归纳，并比较维数。

3. 说明零初值下双对角化生成的正是长方矩阵的Krylov空间而从不形成$\bm A^\top\bm A$，证明中的三项关系就是对$\bm A^\top\bm A$从$\bm A^\top\bm b$出发的Lanczos递推`eq:ls-arnoldi-lanczos`，$a_i=\alpha_i^2+\beta_{i+1}^2$、$\gamma_i=\alpha_{i+1}\beta_{i+1}$。图“Golub--Kahan双对角化的递推与矩阵关系”（`fig:ls-golub-kahan-bidiagonal`）：$k=3$时(a)画两空间中的交替递推，进出$\bm v_i$的两支箭头给出$\alpha_i,\beta_{i+1}$，(b)画$\bm A\bm V_3=\bm U_4\bm B_3$中$4\times3$的下双对角矩阵；每个新向量只与对面空间中相邻的一个向量相连，这是每步只扣一项的原因。

###### paragraph：数值敏感度

1. 浮点下相消只近似成立，短递推不去掉舍入引入的旧方向分量，两组基逐渐失去正交性；影响交给两种求解器，由14.7的真实残差复核控制，必要时以保存基并重正交化的代价换取正交性。

###### paragraph：计算代价

1. 每轮至多一次$\bm A$乘向量与一次$\bm A^\top$乘向量，外加两次向量更新、两次范数与两次缩放；不保存整组基、不作完整再正交化时工作存储为$O(m+d)$，与Lanczos一样不随轮数增长；收敛快慢取决于求解器怎样在子空间中选近似。

#### 15.4.4 应用

1. 零初值下把近似写成$\bm x=\bm V_k\bm y$，由$\bm b=\bm U_{k+1}\beta_1\bm e_1$与关系`eq:ls-golub-kahan-relations`第一式得$\bm b-\bm A\bm V_k\bm y=\bm U_{k+1}(\beta_1\bm e_1-\bm B_k\bm y)$；$\bm U_{k+1}$保长，最小化原残差化为双对角小最小二乘问题$\min_{\bm y}\lVert\beta_1\bm e_1-\bm B_k\bm y\rVert_2$，这就是15.10 LSQR的做法，$\bm B_k$每增一列只在右下角多两个非零元，一次新的正交变换就能延续三角化，解由短递推累加。

2. 改为最小化正规残差时，再用第二式作用$\bm A^\top$，借$\bm B_k$首行$\alpha_1\bm e_1^\top$、末行$\beta_{k+1}\bm e_k^\top$得$\bm A^\top(\bm b-\bm A\bm V_k\bm y)=\bm V_k(\alpha_1\beta_1\bm e_1-\bm B_k^\top\bm B_k\bm y)-\alpha_{k+1}\beta_{k+1}y_k\bm v_{k+1}$，正规残差的长度化为关于$\bm B_k^\top\bm B_k$及一个边界项的小问题，这就是15.11 LSMR的做法，实际计算不形成$\bm B_k^\top\bm B_k$。

3. 说明两者共用同一个双对角化，区别只在最小化原残差还是正规残差；与方阵情形对应，对正规方程而言LSQR相当于在Lanczos基上用Galerkin条件、LSMR相当于极小残差条件，15.10与15.11将分别证明它们与正规方程上的CG和MINRES等价。

### 15.5 最小残差法

1. 设$\bm A$实对称非奇异且允许不定，指出$\bm u^\top\bm A\bm u$可为负、能量范数无定义而原残差长度始终有意义；定义最小残差法MINRES：在$\bm x_0+\mathcal K_k$中取使$\lVert\bm b-\bm A\bm x\rVert_2$最小的近似，即15.1的极小残差条件。点明它紧接15.3.4的应用：Lanczos过程（式`eq:ls-lanczos-step`）已给出基$\bm V_k$与$\overline{\bm T}_k$并化为$(k+1)\times k$小最小二乘问题，不定时$\bm T_k$可能奇异，故不解Galerkin方程`eq:ls-lanczos-projected-system`，而在小问题上求残差最小的坐标；本节说明怎样随Lanczos过程逐列求解，使每轮工作量与存储不随步数增长。

#### 15.5.1 主要思想

###### paragraph：逐步长大的小问题

1. 候选写成$\bm x=\bm x_0+\bm V_k\bm y$，由$\bm r_0=\beta\bm V_{k+1}\bm e_1$与关系`eq:ls-arnoldi-tridiagonal`及定理`thm:ls-arnoldi-lanczos`得式`eq:ls-minres-small-problem`$\lVert\bm b-\bm A\bm x\rVert_2=\lVert\beta\bm e_1-\overline{\bm T}_k\bm y\rVert_2$。

2. 按元素写出$(k+1)\times k$的$\overline{\bm T}_k$，指出从第$k-1$步到第$k$步只添一列$(0,\ldots,0,\gamma_{k-1},a_k,\gamma_k)^\top$与一行；每步重做QR代价随$k$增长，应沿用前一步的分解、只处理新增部分。

###### paragraph：沿用前一步的消元结果

1. 第$j$个Givens旋转$\bm G_j$只作用于第$j,j+1$行；前$k-1$步已把$\overline{\bm T}_{k-1}$消成每列三个非零元$\epsilon_j,\delta_j,\rho_j$的上三角矩阵，以$k=4$为例按元素写出前三列，它们以后不再改变。

###### paragraph：新列只需三次旋转

1. 新列只在最后三行非零，更早的旧旋转不起作用，只需$\bm G_{k-2},\bm G_{k-1}$与新旋转$\bm G_k$；以$k=4$为例按元素写出新列$(0,0,\gamma_3,a_4,\gamma_4)^\top$经$\bm G_2,\bm G_3,\bm G_4$依次变为含$\epsilon_4,\theta$、$\delta_4,\bar\delta$、$\rho_4,0$的列，并写出整个矩阵在$\bm G_4$前后的形状。

2. 一般地得式`eq:ls-minres-rotation`，逐行说明三行分别对应$\bm G_{j-2}$、$\bm G_{j-1}$与新旋转$\bm G_j$，不存在的旧旋转取单位变换。

###### paragraph：右端与残差

1. 同一组旋转作用于右端，得式`eq:ls-minres-rhs`$g_j=c_j\bar g_j$、$\bar g_{j+1}=-s_j\bar g_j$，以$k=4$写出右端在$\bm G_4$前后的变化；前$k$个方程由$\bm R_k$精确满足，最后一个分量无法消去，单独一行写出最小残差长度$\lvert\bar g_{k+1}\rvert$。

###### paragraph：增量求解的两个好处

1. 每步工作量固定：只作用两个旧旋转、构造一个新旋转、更新两个右端分量，加上一次Lanczos递推与向量更新，工作量与存储不随步数增长。

2. 残差长度随消元得到：精确算术下$\lvert\bar g_{k+1}\rvert$就是原残差长度，每步一次乘法即可读出且随步数不增；浮点下会偏离，最终仍须复核。

###### paragraph：方向与解的短递推

1. 回代需保存全部基，改为令$\bm D_k=\bm V_k\bm R_k^{-1}$，比较$\bm D_k\bm R_k=\bm V_k$的列得方向递推式`eq:ls-minres-direction`（$\bm d_{-1}=\bm d_0=\bm0$）；解按式`eq:ls-minres-update`逐项累加，只留两个旧方向与两个旧旋转；定理`thm:ls-minres-optimality`说明累加结果正是小问题的解。

#### 15.5.2 算法实现

1. 每轮作一步Lanczos递推得新列，用两个旧旋转与一个新旋转消元，再更新右端、方向与解；输入实对称非奇异矩阵与$\bm b$、只需矩阵乘向量，参数与阈值$\tau$沿用第14章的执行流程；在贯穿例`ex:ls-stationary-running-example`上执行，$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$、$\bm b=(1,2)^\top$、$\bm x_0=\bm0$、$\bm x_\star=(1/11,7/11)^\top$，Lanczos数值同15.3。

###### paragraph：变量

1. 以列表列出：Lanczos基向量$\bm v_{j-1},\bm v_j$与工作向量$\bm w$，$\overline{\bm T}_k$第$j$列的$a_j,\gamma_j$（$\gamma_{j-1}$留到本轮），两个旧旋转与新旋转$(c,s)$，$\bm R_k$第$j$列的$\epsilon_j,\delta_j,\rho_j$及临时量$\theta,\bar\delta$，右端分量$\bar g_j$与$g_j$（$\lvert\bar g_{j+1}\rvert$为残差长度），方向$\bm d_{j-2},\bm d_{j-1},\bm d_j$，近似解$\bm x_j$，轮次$j$。

###### paragraph：初始化

1. 先算$\bm r_0$并作停止检查，否则初始化$\beta=\lVert\bm r_0\rVert_2$、$\bm v_0=\bm0$、$\bm v_1=\bm r_0/\beta$、$\gamma_0=0$、$\bm d_{-1}=\bm d_0=\bm0$、$\bar g_1=\beta$、两个旧旋转为$(1,0)$、$j=1$；例中$\beta=\sqrt5$、$\bm v_1=(1,2)^\top/\sqrt5$、$\bar g_1=\sqrt5$。

###### paragraph：每轮更新

1. 第$j$轮依次：Lanczos递推，按式`eq:ls-lanczos-step`得$a_j$、余项$\bm w$与$\gamma_j$，归一化留到停止步；旋转消元，按式`eq:ls-minres-rotation`得$\epsilon_j,\delta_j,\rho_j,c_j,s_j$，出现$\rho_j=0$时不作除法而先检查小问题的秩与相容性；更新右端，按式`eq:ls-minres-rhs`得$g_j,\bar g_{j+1}$；更新方向与解，按式`eq:ls-minres-direction`与`eq:ls-minres-update`，再舍去最旧的方向与旋转。每步给出例中第一轮的值：$a_1=4$、$\gamma_1=1$、第一列$(0,4,1)^\top$，$\rho_1=\sqrt{17}$、$c_1=4/\sqrt{17}$、$s_1=1/\sqrt{17}$，$g_1=4\sqrt5/\sqrt{17}$、$\bar g_2=-\sqrt5/\sqrt{17}$、$\lvert\bar g_2\rvert\approx0.542$，$\bm d_1=(1,2)^\top/\sqrt{85}$、$\bm x_1=(4,8)^\top/17$，并用$\bm b-\bm A\bm x_1=(-7,6)^\top/17$核对长度。

2. 在最后一个计算步骤后集中给出第二轮：$\bm v_2=(2,-1)^\top/\sqrt5$，$a_2=3$、$\bm w=\bm0$、$\gamma_2=0$、第二列$(1,3,0)^\top$；$\epsilon_2=0$、$\theta=1$、$\delta_2=7/\sqrt{17}$、$\bar\delta=\rho_2=11/\sqrt{17}$、$c_2=1$、$s_2=0$；$g_2=-\sqrt5/\sqrt{17}$、$\bar g_3=0$；$\bm d_2=(27,-31)^\top/(11\sqrt{85})$、$\bm x_2=(1,7)^\top/11$。

3. 停止：残差估计$\lvert\bar g_{j+1}\rvert\le\tau$、$\gamma_j=0$（此时$s_j=0$、$\bar g_{j+1}=0$）或$j=K$时，用$\bm b-\bm A\bm x_j$复核真实残差（14.7）后输出，并按14.7节报告结束原因；否则令$\bm v_{j+1}=\bm w/\gamma_j$进入下一轮；例中第一轮未达标而继续，第二轮$\bar g_3=0$且$\gamma_2=0$，复核真实残差为零，以“达到容差”退出。

4. 最终结果：例中两个旋转把$\overline{\bm T}_2$化为$\bm R_2=\frac1{\sqrt{17}}\left[\begin{smallmatrix}17&7\\0&11\end{smallmatrix}\right]$，回代得$\bm y=(3\sqrt5,-\sqrt5)^\top/11$，单独一行写出$\bm x_2=\bm x_0+\bm V_2\bm y=(1,7)^\top/11=\bm x_\star$，与短递推一致，代回满足$\bm A\bm x_2=\bm b$；二维问题第二轮子空间用尽，MINRES给出精确解。

5. 说明贯穿例是正定的，改用对称不定矩阵展示能量范数无定义、CG不适用而MINRES仍可用。

6. 例“对称不定矩阵上的MINRES”（`ex:ls-minres-indefinite`）：取$\bm A=\operatorname{diag}(1,-2)$、$\bm b=(1,1)^\top$、$\bm x_0=\bm0$，由$\bm b^\top\bm A\bm b=-1$说明$\bm u^\top\bm A\bm u$不能作范数平方；第一轮$a_1=-1/2$、$\gamma_1=3/2$、$\bm v_2=(1,-1)^\top/\sqrt2$，$\rho_1=\sqrt{10}/2$、$c_1=-1/\sqrt{10}$、$s_1=3/\sqrt{10}$、$g_1=-1/\sqrt5$、$\bar g_2=-3/\sqrt5$，$\bm x_1=(-1/5,-1/5)^\top$，直接计算$\bm r_1=(6/5,3/5)^\top$的长度$3/\sqrt5=\lvert\bar g_2\rvert$。

7. 第二轮$a_2=-1/2$、$\gamma_2=0$，旋转得$\delta_2=-3/\sqrt{10}$、$\rho_2=4/\sqrt{10}$、$c_2=-1$、$g_2=3/\sqrt5$、$\bar g_3=0$，$\bm x_2=(1,-1/2)^\top$满足$\bm A\bm x_2=\bm b$；独立核验：直接解$\bm T_2\bm y=\beta\bm e_1$（$\bm T_2$行为$(-1/2,3/2),(3/2,-1/2)$）得$\bm y=(\sqrt2/4,3\sqrt2/4)^\top$，$\bm V_2\bm y$与短递推结果一致。

#### 15.5.3 算法分析

###### paragraph：正确性

1. 说明正确性归结为两点：小问题与原问题等价，旋转与短递推给出小问题的解。

2. 定理“MINRES的最小残差性”（`thm:ls-minres-optimality`）：$\bm A$实对称非奇异、精确算术、此前$\gamma_j$非零时，$\bm x_k$是$\bm x_0+\mathcal K_k$上残差长度的唯一最小点，$\lVert\bm r_k\rVert_2=\lvert\bar g_{k+1}\rvert$不增，至多$d$步得精确解，并有$\lVert\bm r_k\rVert_2\le\min_{p\in\mathcal P_k}\max_{\lambda\in\sigma(\bm A)}\lvert p(\lambda)\rvert\lVert\bm r_0\rVert_2$。

3. 证明“化为小问题”：由Lanczos关系与$\bm r_0=\beta\bm V_{k+1}\bm e_1$得残差等于$\bm V_{k+1}(\beta\bm e_1-\overline{\bm T}_k\bm y)$，标准正交列不改变长度；$\gamma_k=0$时略去零末行照样成立；$\bm V_k$满列秩使两个最小化问题的解一一对应。

4. 证明“旋转与短递推”：三对角结构使只有第$j-2$、$j-1$个旧旋转起作用，$\bm R_k$上带宽为$2$；旋转之积$\bm\Omega_k$把目标拆成$\lVert(g_1,\ldots,g_k)^\top-\bm R_k\bm y\rVert_2^2+\bar g_{k+1}^2$，由$\bm A\bm V_k$满列秩得$\bm R_k$可逆、唯一最小点与最小值；比较$\bm D_k\bm R_k=\bm V_k$的列得方向递推，后来的旋转不改已定的$g_j$与列，逐步累加即得最小点。

5. 证明“单调性与有限步终止”：$\lvert\bar g_{k+1}\rvert=\lvert s_k\rvert\lvert\bar g_k\rvert$；$\gamma_k=0$时$s_k=0$、残差为零，维数上限给出至多$d$步。

6. 证明“残差界”：由残差多项式引理与最小残差性得$\lVert\bm r_k\rVert_2=\min_p\lVert p(\bm A)\bm r_0\rVert_2$，用实对称谱定理`thm:ls-real-symmetric-spectral`把$p(\bm A)$对角化，谱范数化为特征值上的最大值。

7. 定理后指出15.7的GMRES对一般方阵采用同一准则，对称时两者近似相同，MINRES只是借对称性改用短递推。

###### paragraph：收敛速度

1. 界中只剩特征值，收敛快慢完全由谱决定；不定时特征值分布在原点两侧，多项式在原点必须取$1$，同时压低两侧比只压低一侧更难。

###### paragraph：奇异系统的边界

1. 说明结论假定非奇异：用于奇异对称矩阵时，不相容情形最小残差非零，到达最小二乘解要看$\lVert\bm A\bm r_k\rVert_2$而非$\lVert\bm r_k\rVert_2$，普通MINRES的解也不自动是最小范数解；不展开MINRES-QLP等专门算法。

###### paragraph：数值敏感度与计算代价

1. Lanczos向量在浮点下失去正交性（15.3），残差估计须用真实残差复核；每轮一次矩阵乘向量、只存固定数量的向量，而保存全部基的GMRES执行$k$步约需$kd$个数，完整再正交化同样要保存全部基。

### 15.6 共轭梯度法

1. 设$\bm A$对称正定，定义共轭梯度法CG：第$k$步取$\bm x_0+\mathcal K_k$中使误差能量范数最小的近似，等价于15.1的Galerkin条件；指出它紧接15.3的应用一小节，是对称正定时求解Lanczos基下三对角方程的一种特殊做法。

#### 15.6.1 主要思想

###### paragraph：逐步长大的三对角方程

1. 由Lanczos应用写出Galerkin方程$\bm T_k\bm y_k=\lVert\bm r_0\rVert_2\bm e_1$并按元素写出$\bm T_k$；与MINRES一样每步只添一行一列，但$\bm T_k$对称正定、要解的是方阵方程。

2. 对比MINRES用Givens旋转作QR以应付不定矩阵，指出对称正定的$\bm T_k$可直接作无开方的Cholesky即$\bm L\bm D\bm L^\top$分解且不必选主元。

###### paragraph：分解的增量更新

1. 写$\bm T_k=\bm L_k\bm D_k\bm L_k^\top$（单位下双对角$\bm L_k$，次对角元$\ell_j$；$\bm D_k$的对角元$d_j$），以$k=3$按元素展开乘积并与$\bm T_3$比较，得递推式`eq:ls-cg-ldl`$\ell_j=\gamma_j/d_j$、$d_{j+1}=a_{j+1}-\ell_j\gamma_j$，正定保证$d_j>0$。

2. 说明从第$k$步到第$k+1$步只在末尾追加$\ell_k,d_{k+1}$、已有部分不变，按元素写出$\bm L_4,\bm D_4$；例中$d_1=4$、$\ell_1=1/4$、$d_2=11/4$。

###### paragraph：翻译回向量

1. 方程分两步解：前代$\bm L_k\bm w=\lVert\bm r_0\rVert_2\bm e_1$给出$w_1=\lVert\bm r_0\rVert_2$、$w_{j+1}=-\ell_jw_j$；令$\widehat{\bm P}_k=\bm V_k\bm L_k^{-\top}$、$\zeta_j=w_j/d_j$，得$\bm x_k=\bm x_0+\sum\zeta_j\hat{\bm p}_j$，由$\widehat{\bm P}_k\bm L_k^\top=\bm V_k$得方向递推，解与方向都成为短递推，不保存基、不重解方程。

###### paragraph：CG的形式

1. 由关系`eq:ls-arnoldi-tridiagonal`与Galerkin条件得$\bm r_k=-\gamma_k(\bm e_k^\top\bm y_k)\bm v_{k+1}=w_{k+1}\bm v_{k+1}$，$w_j$符号交替，故$\bm r_k=(-1)^k\lVert\bm r_k\rVert_2\bm v_{k+1}$；按同样比例缩放方向，两条递推成为式`eq:ls-cg-update`与`eq:ls-cg-direction`，且$\alpha_k=1/d_{k+1}$、$\beta_k=\ell_{k+1}^2$。

2. 给出直接由向量计算的式`eq:ls-cg-step`与`eq:ls-cg-beta`，并说明$\alpha_k$的线搜索意义与$\beta_k$的共轭意义；例中$\alpha_0=1/4$、$\beta_0=1/16$、$\alpha_1=4/11$；反过来写出$a_{k+1},\gamma_{k+1}$由CG系数表示的式子；定理`thm:ls-cg-convergence`说明逐步计算给出能量范数误差最小的近似。

#### 15.6.2 算法实现

1. 说明每轮作一次矩阵乘向量、求步长、更新解与残差、形成新方向；输入对称正定$\bm A$与$\bm b$，初值、容差与最大轮数$K$沿用第14章的执行流程，阈值$\tau=\mathrm{atol}+\mathrm{rtol}\lVert\bm b\rVert_2$，结束原因见14.7节；在贯穿例$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$、$\bm b=(1,2)^\top$、$\bm x_0=\bm0$上执行。

###### paragraph：变量

1. 以列表列出：近似解$\bm x$、递推残差$\bm r$、搜索方向$\bm p$（均在原处更新），存放$\bm A\bm p_k$的工作向量$\bm q$，残差长度平方$\rho_k=\bm r_k^\top\bm r_k$（旧值留作$\beta_k$的分母），步长与组合系数$\alpha_k,\beta_k$，轮次$k$。

###### paragraph：初始化

1. $\bm r_0=\bm b-\bm A\bm x_0$、$\bm p_0=\bm r_0$、$\rho_0=\bm r_0^\top\bm r_0$、$k=0$，初始残差已达标时复核后直接输出$\bm x_0$；例中$\bm r_0=\bm p_0=(1,2)^\top$、$\rho_0=5$、$\lVert\bm r_0\rVert_2\approx2.24$，进入第一轮。

###### paragraph：每轮更新

1. 第$k$轮依次：乘矩阵$\bm q=\bm A\bm p_k$；按式`eq:ls-cg-step`求步长$\alpha_k=\rho_k/(\bm p_k^\top\bm q)$，未收敛而$\bm p_k^\top\bm q\le0$时报告矩阵并非对称正定或数值状态严重受损并停止；按式`eq:ls-cg-update`更新解与残差，$\bm A\bm p_k$取$\bm q$；按式`eq:ls-cg-beta`、`eq:ls-cg-direction`算$\rho_{k+1}$、$\beta_k$与$\bm p_{k+1}$，分母已在初始化或上一轮停止检查中确认非零，然后$k\leftarrow k+1$；每步给出例中第一轮的值$\bm q=(6,7)^\top$、$\alpha_0=1/4$、$\bm x_1=(1/4,1/2)^\top$、$\bm r_1=(-1/2,1/4)^\top$（核对$\bm r_1^\top\bm p_0=0$）、$\rho_1=5/16$、$\beta_0=1/16$、$\bm p_1=(-7/16,3/8)^\top$（核对$\bm p_1^\top\bm A\bm p_0=0$），以及第二轮的$\bm q=(-11/8,11/16)^\top$、$\alpha_1=4/11$、$\bm x_2=(1/11,7/11)^\top$、$\bm r_2=\bm0$。

2. 停止：$\sqrt{\rho_{k+1}}\le\tau$时先用$\bm b-\bm A\bm x_{k+1}$复核（14.7）再以“达到容差”结束，做满$K$轮时以“步数耗尽”结束，并说明递推残差会偏离真实残差，每隔若干轮也重算一次；例中第一轮后$\lVert\bm r_1\rVert_2=\sqrt5/4\approx0.559$，大于MINRES第一步的$\sqrt{5/17}\approx0.542$，因为CG最小化的是能量范数误差而非原残差；第二轮后$\rho_2=0$，逐行代回复核真实残差为零，以“达到容差”退出。第1—4步合起来就是式`eq:ls-cg-update`—`eq:ls-cg-beta`，只是把$\bm A\bm p_k$存进$\bm q$、把$\bm r_k^\top\bm r_k$存为$\rho_k$。

3. 最终结果：单独一行写出$\bm x_2=(1/11,7/11)^\top=\bm x_\star$，二维问题两步得精确解，与$\mathcal K_2=\mathbb R^2$相符；与15.3在同一例上的Lanczos过程对照，$\bm r_1=-(\sqrt5/4)\bm v_2$与$\bm v_2$平行，由$\alpha_0,\beta_0,\alpha_1$算出$a_1=4$、$\gamma_1=1$、$a_2=3$，正是那里的$\bm T_2$。

4. 对照每轮取$\beta_k=0$的最速下降，第一步与CG相同，此后在互相垂直的方向间折返，$\bm x_2=(1/12,7/12)^\top$、$\bm x_3=(5/48,5/8)^\top$只能逐步逼近，并指向路径图。图“贯穿例上CG与最速下降的路径”（`fig:ls-cg-steepest-descent-paths`）：在$\phi$的等值线上画出两条路径，第一步相同，CG第二个方向与第一个方向$\bm A$共轭、直指中心，最速下降来回折返，右图放大10倍。

#### 15.6.3 算法分析

###### paragraph：正确性与收敛速度

1. 说明正确性归结为残差两两正交与方向两两共轭，由它们推出最优性，再由残差多项式得收敛速度。

2. 定理“CG的最优性与收敛速度”（`thm:ls-cg-convergence`）：精确算术下残差正交、方向共轭，$\bm x_k$是$\bm x_0+\mathcal K_k$上误差能量范数的唯一最小点，误差满足$2((\sqrt\kappa-1)/(\sqrt\kappa+1))^k$的界，至多$d$步得精确解。

3. 证明“正交与共轭关系”：归纳证明正交与共轭，关键步骤是$\bm p_k^\top\bm r_k=\bm r_k^\top\bm r_k$、对$i<k$用归纳假设的共轭性与$\bm A\bm p_i\in\mathcal K_{k+1}$、对$i=k$用$\bm A\bm p_k=(\bm r_k-\bm r_{k+1})/\alpha_k$与$\beta_k$抵消，以及两两正交的非零残差线性无关从而张成$\mathcal K_{k+2}$。

4. 证明“最优性”：由$\bm A\bm e_k=-\bm r_k$与$\bm r_k\perp\mathcal K_k$展开$\lVert\bm e_k+\bm z\rVert_{\bm A}^2=\lVert\bm e_k\rVert_{\bm A}^2+\lVert\bm z\rVert_{\bm A}^2$得唯一最优，并由正交向量个数得有限步终止。

5. 证明“收敛速度”：用谱定理把误差展开到特征向量，化为特征值上的多项式极小化；取平移缩放后的Chebyshev多项式，验证$x>1$时的显式式，计算$\ell(0)=(\kappa+1)/(\kappa-1)$处的值，得到所述界，$\kappa=1$时一步得解。

6. 解释界只依赖两端特征值、步数约与$\sqrt\kappa$成正比，控制的是能量范数，欧氏残差不必每步下降。

###### paragraph：数值敏感度

1. 说明浮点下正交与共轭关系逐步受损、不承诺恰好$d$步，递推残差偏离真实残差，宣布达标前须用$\bm b-\bm A\bm x_k$复核。

###### paragraph：计算代价

1. 每轮一次矩阵乘向量、两次内积、三次向量更新，只存四个向量，复核所需乘法另计。

### 15.7 广义最小残差法

1. 设$\bm A$是一般非奇异方阵，定义广义最小残差法GMRES：第$k$步取$\bm x_0+\mathcal K_k$中使原残差长度最小的近似，与MINRES同用极小残差条件；说明本节紧接15.2的应用（`sec:ls-arnoldi-application`），那里已把准则化为$(k+1)\times k$上Hessenberg最小二乘问题，本节说明怎样逐列求解、读出残差并还原近似解，Arnoldi递推只作引用。

#### 15.7.1 主要思想

###### paragraph：逐步长大的小问题

1. 以周期起点$\bm x^{(s)}$、$\beta=\lVert\bm r^{(s)}\rVert_2$、$\bm v_1=\bm r^{(s)}/\beta$作$j$轮Arnoldi，由定理`thm:ls-arnoldi-relation`得Arnoldi关系与小问题式`eq:ls-gmres-small-problem`。

2. 按元素写出$(j+1)\times j$的上Hessenberg矩阵$\overline{\bm H}_j$，指出与MINRES一样每步只添一列一行，但新列$(h_{1,j},\ldots,h_{j+1,j})^\top$一般全不为零。

###### paragraph：沿用前一步的消元结果

1. 第$i$个Givens旋转$\bm G_i$只作用于第$i,i+1$行；前$j-1$步已把$\overline{\bm H}_{j-1}$消成满的上三角矩阵（元素$r_{i,l}$），以$j=4$按元素写出前三列，它们以后不再改变。

###### paragraph：新列要经过全部旧旋转

1. 新列在各行都可能非零，须依次经过$\bm G_1,\ldots,\bm G_{j-1}$，再由新旋转消去$h_{j+1,j}$；以$j=4$按元素写出新列经$\bm G_1,\ldots,\bm G_4$的变化与整个矩阵在$\bm G_4$前后的形状，给出每个旧旋转作用于两个分量的形式。

2. 新旋转式`eq:ls-gmres-givens`把$(a,h_{j+1,j})$变为$(\rho_j,0)$，用$\operatorname{hypot}$计算，旋转全部保存。

###### paragraph：右端与残差

1. 同一组旋转作用于右端，得式`eq:ls-gmres-rhs`，以$j=4$写出右端在$\bm G_4$前后的变化；目标化为$\lVert(g_1,\ldots,g_j)^\top-\bm R_j\bm y\rVert_2^2+g_{j+1}^2$，最小残差为$\lvert g_{j+1}\rvert=\lvert s_j\rvert\lvert g_j\rvert$且不增，每步即可读出。

###### paragraph：与MINRES的差别

1. 差别都来自新列是满的：每步要作用$j-1$个旧旋转、Arnoldi要与$j$个旧基向量正交化，工作量与存储随步数增长；$\bm R_j$是满的上三角，没有短递推，$\bm y$的分量每步都会变，所以只在停下时回代式`eq:ls-gmres-back-substitution`并按式`eq:ls-gmres-solution`用整组基还原。

2. $\bm A$对称时$\overline{\bm H}_j$成为三对角、新列只需两个旧旋转且回代化为短递推，即MINRES。

###### paragraph：重启

1. 每个周期最多走$m$步，更新$\bm x$、用原矩阵重算残差后重新生成基；限制了存储，代价是不再利用旧周期的子空间。

#### 15.7.2 算法实现

1. 说明输入非奇异方阵与$\bm b$、只需矩阵乘向量、输出近似解；预先选定$\bm x_0$、容差、总步数上限$K$与重启长度$1\le m\le d$，阈值与流程沿用第14章（`sec:ls-matrix-splitting`、`sec:ls-stationary-stopping`）。

2. 概述每轮作Arnoldi扩展、让新列经过全部旧旋转、构造新旋转并更新右端，由$\lvert g_{j+1}\rvert$判断是否停下，停下后回代、还原并由真实残差决定是否重启；在贯穿例$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$、$\bm x_0=\bm0$、$\bm b=(1,2)^\top$上取$m=2$执行，Arnoldi部分的数值与15.2相同。

###### paragraph：变量

1. 以列表列出：周期起点$\bm x^{(s)}$；本周期的整组基$\bm v_1,\ldots,\bm v_{j+1}$（全部保存，用于还原）；Arnoldi工作向量$\bm w$；$\overline{\bm H}_j$的新列，旋转后在原处变为$\bm R_j$的第$j$列；已构造的旋转$c_i,s_i$；经旋转的右端$\bm g$，$\lvert g_{j+1}\rvert$为残差估计；周期内轮次$j$与累计步数。

###### paragraph：初始化

1. 把周期起点初始化为$\bm x_0$，计算$\bm r^{(s)}$并作停止检查（达标或步数耗尽都输出$\bm x^{(s)}$，不再归一化），否则置$\beta$、$\bm v_1=\bm r^{(s)}/\beta$、$\bm g=\beta\bm e_1$、$j=1$；重启时回到这里，所以这里的检查总用真实残差；例中$\beta=\sqrt5$、$\bm v_1=(1,2)^\top/\sqrt5$、$\bm g=(\sqrt5,0)^\top$。

###### paragraph：每轮更新

1. 第$j$轮依次：Arnoldi扩展（按15.2计算过程每轮更新的第1—3步，即`eq:ls-arnoldi-coefficients`、`eq:ls-arnoldi-normalize`，$h_{j+1,j}=0$时不生成$\bm v_{j+1}$）；对新列依次作用旧旋转$\bm G_1,\ldots,\bm G_{j-1}$；按式`eq:ls-gmres-givens`构造并保存新旋转，令$h_{j,j}\leftarrow\rho_j$、$h_{j+1,j}\leftarrow0$，$a=h=0$时小问题秩亏须先检查而不相除；按式`eq:ls-gmres-rhs`更新右端，$\lvert g_{j+1}\rvert$即残差估计；每步给出例中第一轮的值$\bm A\bm v_1=(6,7)^\top/\sqrt5$、新列$(4,1)^\top$、$\bm v_2=(2,-1)^\top/\sqrt5$、无旧旋转、$\rho_1=\sqrt{17}$、$c_1=4/\sqrt{17}$、$s_1=1/\sqrt{17}$、$\bm g=\sqrt5(4,-1)^\top/\sqrt{17}$、$\lvert g_2\rvert\approx0.542$。

2. 停止：估计达标、$h_{j+1,j}=0$、本周期满$m$轮或累计步数达$K$时退出每轮更新转入回代，否则$j\leftarrow j+1$；估计只用于决定何时复核，是否结束由初始化中的真实残差检查决定（`sec:ls-stationary-stopping`）；例中第一轮继续，并指出若此时退出则$\bm x_1=(4/17,8/17)^\top$与MINRES第一步相同；第二轮$h_{1,2}=1$、$h_{2,2}=3$、$h_{3,2}=0$，经$\bm G_1$得$(7,11)^\top/\sqrt{17}$，$\rho_2=11/\sqrt{17}$、$c_2=1$、$s_2=0$、$g_3=0$，二维空间用尽而退出。

###### paragraph：回代与重启

1. 退出后按式`eq:ls-gmres-back-substitution`自下而上回代、按式`eq:ls-gmres-solution`还原，再令$\bm x^{(s)}\leftarrow\bm x$回到初始化复核真实残差，达标或达上限则输出，否则开始新周期；几个周期后真实残差几乎不降时报告停滞；例中$\bm R_2=\frac1{\sqrt{17}}\left[\begin{smallmatrix}17&7\\0&11\end{smallmatrix}\right]$，回代得$y_2=-\sqrt5/11$、$y_1=3\sqrt5/11$，$\bm x=\bm V_2\bm y=(1/11,7/11)^\top$。

2. 最终结果：例中回到初始化后真实残差为零，以“达到容差”输出$\bm x_\star=(1/11,7/11)^\top$，核对$\bm A\bm x_\star=\bm b$，与MINRES相同，$\bm R_2$与$\bm g$正是15.2的$\overline{\bm H}_2$与$\sqrt5\bm e_1$经同两个旋转的结果。

3. 说明贯穿例对称，改用MINRES不再适用、GMRES仍可用的非对称矩阵。

4. 例“非对称矩阵上的GMRES”（`ex:ls-gmres-nonsymmetric`）：$\bm A$行为$(3,1),(0,2)$、$\bm b=(1,1)^\top$、$\bm x_0=\bm0$、$m=2$；第一轮新列$(3,1)^\top$，$\rho_1=\sqrt{10}$、$c_1=3/\sqrt{10}$、$s_1=1/\sqrt{10}$、$\bm g=(3,-1)^\top/\sqrt5$，若此时结束则$\bm x_1=(3/10,3/10)^\top$，直接计算$\bm r_1=(-1/5,2/5)^\top$的长度等于$\lvert g_2\rvert=1/\sqrt5$。

5. 第二轮新列$(0,2,0)^\top$与$h_{2,1}=1$不对称，经$\bm G_1$变为$(2,6,0)^\top/\sqrt{10}$，$h_{3,2}=0$使$c_2=1$、$s_2=0$、$g_3=0$；回代得$y_2=-\sqrt2/6$、$y_1=\sqrt2/3$，恢复$\bm x_2=(1/6,1/2)^\top$并代回验证原残差为零；指出Arnoldi系数可按15.2的计算过程逐步核对。

#### 15.7.3 算法分析

###### paragraph：正确性

1. 说明定理针对不重启的完整GMRES，即$m=d$、$\bm x^{(s)}=\bm x_0$。

2. 定理“GMRES的最小残差性”（`thm:ls-gmres-optimality`）：$\bm A$非奇异、精确算术下$\bm x_k$是$\bm x_0+\mathcal K_k$中残差长度的唯一最小点，$\lVert\bm r_k\rVert_2=\lvert g_{k+1}\rvert$等于上一步残差乘$\lvert s_k\rvert\le1$而不增，至多$d$步得精确解；$\bm A=\bm X\bm\Lambda\bm X^{-1}$可对角化（可为复矩阵）时有$\kappa_2(\bm X)\min_p\max_{\lambda}\lvert p(\lambda)\rvert\lVert\bm r_0\rVert_2$的残差界。

3. 证明“化为小问题”：由Arnoldi关系与$\bm r_0=\beta\bm V_{k+1}\bm e_1$把残差写成$\bm V_{k+1}(\beta\bm e_1-\overline{\bm H}_k\bm y)$，标准正交列保长，$\bm V_k$满列秩给出解的一一对应。

4. 证明“旋转后的小问题”：旋转之积$\bm\Omega_k$把$\overline{\bm H}_k$化为$[\bm R_k;\bm0^\top]$、把$\beta\bm e_1$化为$\bm g$，目标拆成两项；$\bm A\bm V_k$满列秩使$\bm R_k$可逆，回代所得$\bm y$是唯一最小点，最小值$\lvert g_{k+1}\rvert$。

5. 证明“单调性与有限步终止”：第$k$个旋转把旋转前的$g_k$（即上一步残差长度）分成$c_kg_k$与$-s_kg_k$，得$\lvert g_{k+1}\rvert=\lvert s_k\rvert\lvert g_k\rvert$；$h_{k+1,k}=0$时残差为零，维数上限给出至多$d$步。

6. 证明“残差界”：由残差多项式引理得$\lVert\bm r_k\rVert_2=\min_p\lVert p(\bm A)\bm r_0\rVert_2$，用$p(\bm A)=\bm X p(\bm\Lambda)\bm X^{-1}$与对角矩阵的谱范数放大出$\kappa_2(\bm X)$。

###### paragraph：收敛速度

1. 界把收敛化为找原点取一、在全部特征值上都小的低次多项式；非正规矩阵的$\kappa_2(\bm X)$可能很大，界因此变弱，只看特征值是否集中不能判断收敛快慢。

###### paragraph：重启与数值敏感度

1. GMRES($m$)丢弃历史空间，周期内的残差最小只是本周期子空间上的最优，不能说成累计空间上的最优，可能停滞，也失去$d$步得精确解的保证；浮点下基不再精确正交、$\lvert g_{j+1}\rvert$偏离真实残差，所以每个周期结束时用$\bm b-\bm A\bm x$复核。

###### paragraph：计算代价

1. 每轮一次矩阵乘向量；完整GMRES执行$k$步正交化约$2dk^2$次运算、基存储约$kd$个数，都随步数增长；GMRES($m$)每周期至多约$2dm^2$次运算、存储约$(m+1)d$个数，与总步数无关。

### 15.8 双共轭梯度法

1. 从15.2的应用（`sec:ls-arnoldi-application`）进入：一般方阵上无论按Galerkin条件还是极小残差条件都要用整组基还原近似解，GMRES须保存全部基；15.3的应用（`sec:ls-lanczos-application`）的短递推依赖$\bm A^\top=\bm A$使大部分$h_{i,j}$为零；本节针对非对称可逆方阵，改用15.1第四类准则（`sec:ls-krylov-selection-criteria`）中的影子空间，即Petrov--Galerkin条件`eq:ls-krylov-projection`，恢复与CG式`eq:ls-cg-update`—`eq:ls-cg-beta`相仿的短递推，代价是放弃残差最小化，下一节BiCGSTAB减缓残差起伏。

#### 15.8.1 主要思想

###### paragraph：为什么需要影子空间

1. 一般非对称矩阵在单一Krylov子空间中短递推与最优性不能兼得；BiCG放弃最优性、保住短递推，引入以$\bm A^\top$为系数的影子方程与影子空间$\mathcal K_k(\bm A^\top,\widetilde{\bm r}_0)$，要求$\bm r_k\perp\mathcal K_k(\bm A^\top,\widetilde{\bm r}_0)$，即Petrov--Galerkin条件`eq:ls-krylov-projection`，并定义BiCG。

###### paragraph：双正交的两组基

1. 由$\bm w_i^\top\bm A\bm v_j=(\bm A^\top\bm w_i)^\top\bm v_j$要求两组基双正交并归一化为$\bm W_k^\top\bm V_k=\bm I$，得投影矩阵$\bm T_k=\bm W_k^\top\bm A\bm V_k$为不对称的三对角矩阵，以$k=3$按元素写出（对角元$a_j$、次对角元$\gamma_j$、上对角元$\eta_j$）；写出双边Lanczos的两条三项递推，并指出无法归一化时中断。

###### paragraph：逐步长大的三对角方程

1. 取$\bm v_1=\bm r_0/\beta$、$\bm w_1^\top\bm v_1=1$，由$\bm W_k^\top\bm r_0=\beta\bm e_1$把Petrov--Galerkin条件化为$\bm T_k\bm y_k=\beta\bm e_1$，每步只添一行一列，与CG同；例中$a_1=22/5$、$\gamma_1=4/5$、$\eta_1=9/5$、$a_2=13/5$。

###### paragraph：分解的增量更新

1. 不对称三对角矩阵改作不选主元的LU分解$\bm T_k=\bm L_k\bm U_k$，以$k=3$按元素展开，得递推式`eq:ls-bicg-lu`$\ell_j=\gamma_j/d_j$、$d_{j+1}=a_{j+1}-\ell_j\eta_j$，对称时即CG的式`eq:ls-cg-ldl`；每步只追加$\ell_k,d_{k+1}$，$d_j=0$时中断；例中$d_1=22/5$、$\ell_1=2/11$、$d_2=25/11$。

###### paragraph：翻译回向量

1. 前代$g_1=\beta$、$g_{j+1}=-\ell_jg_j$，令$\widehat{\bm P}_k=\bm V_k\bm U_k^{-1}$得解与方向的短递推；由关系与最后一个方程得$\bm r_k=g_{k+1}\bm v_{k+1}$，影子残差同理落在$\bm w_{k+1}$方向，故可用残差代替基向量。

###### paragraph：BiCG的形式

1. 以$\bm p_k=g_{k+1}d_{k+1}\hat{\bm p}_{k+1}$缩放，得更新式`eq:ls-bicg-update`与方向式`eq:ls-bicg-direction`，且$\alpha_k=1/d_{k+1}$、$\beta_k=\gamma_{k+1}\eta_{k+1}/d_{k+1}^2$，对称时回到CG。

2. 给出直接计算的式`eq:ls-bicg-step`与`eq:ls-bicg-beta`及其正交、双共轭意义；例中$\alpha_0=5/22$、$\beta_0=9/121$、$\alpha_1=11/25$、$\bm r_1=(-4/11,2/11)^\top$；定理`thm:ls-bicg-biorthogonality`保证双正交与双共轭；对称且$\widetilde{\bm r}_0=\bm r_0$时退化为CG。

###### paragraph：代价

1. 不最小化任何范数、残差可能振荡；每步多一次$\bm A^\top$乘向量；$\rho_k=0$对应双边Lanczos中断，$\widetilde{\bm p}_k^\top\bm A\bm p_k=0$对应LU中$d_{k+1}=0$；下一节的BiCGSTAB去掉$\bm A^\top$并减缓振荡。

#### 15.8.2 算法实现

1. 说明输入实可逆方阵与$\bm b$、需要$\bm A$与$\bm A^\top$乘向量，输出近似解；参数除第14章的$\bm x_0$、容差与$K$外还有影子初值（默认$\widetilde{\bm r}_0=\bm r_0$），阈值与结束原因沿用第14章；每轮一次$\bm A$与一次$\bm A^\top$乘向量，同一步长更新解与两个残差，同一组合系数形成两个新方向；$\rho_k$与$\widetilde{\bm p}_k^\top\bm A\bm p_k$不受正定性保护，相除前都要检查并区分收敛与中断。

2. 说明对称矩阵配$\widetilde{\bm r}_0=\bm r_0$时BiCG与CG完全一致、贯穿例显示不出影子序列，因此改用把$a_{2,1}$由$1$改为$2$的非对称矩阵。

3. 例“非对称二阶系统上的BiCG”（`ex:ls-bicg-two-steps`）：$\bm A$行为$(4,1),(2,3)$、$\bm b=(1,2)^\top$、$\bm x_0=\bm0$、$\widetilde{\bm r}_0=\bm r_0$，精确解$(1/10,3/5)^\top$并代回两行核验；下面每步后给出它的数值，15.9沿用此例。

###### paragraph：变量

1. 以列表列出：近似解$\bm x$，残差$\bm r$与影子残差$\widetilde{\bm r}$，方向$\bm p$与影子方向$\widetilde{\bm p}$，存$\bm A\bm p_k$与$\bm A^\top\widetilde{\bm p}_k$的工作向量$\bm q,\widetilde{\bm q}$（均在$\mathbb R^d$中），留作下一轮分母的配对量$\rho_k$，步长与组合系数$\alpha_k,\beta_k$，轮次$k$；除矩阵外保存七个向量，存储不随轮数增长。

###### paragraph：初始化

1. 把$\bm r_0=\bm b-\bm A\bm x_0$、$\bm p_0=\bm r_0$、$\widetilde{\bm p}_0=\widetilde{\bm r}_0$、$\rho_0=\widetilde{\bm r}_0^\top\bm r_0$、$k=0$作为初值；$\lVert\bm r_0\rVert_2\le\tau$时复核后直接输出，$\rho_0=0$时另取影子初值；例中四个向量都为$(1,2)^\top$、$\rho_0=5$、$\lVert\bm r_0\rVert_2\approx2.24$，开始迭代。

###### paragraph：每轮更新

1. 第$k$轮依次：乘矩阵得$\bm q=\bm A\bm p_k$、$\widetilde{\bm q}=\bm A^\top\widetilde{\bm p}_k$；求步长，分母$\widetilde{\bm p}_k^\top\bm q$为零而残差非零时报告中断，否则按式`eq:ls-bicg-step`；按式`eq:ls-bicg-update`用$\bm q,\widetilde{\bm q}$更新解与两个残差；算$\rho_{k+1}$，按式`eq:ls-bicg-beta`、`eq:ls-bicg-direction`形成两个新方向并令$k\leftarrow k+1$。例中第一轮$\bm q=(6,8)^\top$、$\widetilde{\bm q}=(8,7)^\top$、分母$22$、$\alpha_0=5/22$，$\bm x_1=(5/22,5/11)^\top$、$\bm r_1=(-4/11,2/11)^\top$、$\widetilde{\bm r}_1=(-9/11,9/22)^\top$，核对$\widetilde{\bm r}_0^\top\bm r_1=\widetilde{\bm r}_1^\top\bm r_0=0$；$\rho_1=45/121$、$\beta_0=9/121$、$\bm p_1=(-35,40)^\top/121$、$\widetilde{\bm p}_1=(-90/121,135/242)^\top$，核对$\widetilde{\bm p}_0^\top\bm A\bm p_1=0$。

2. 第二轮$\bm q=(-100,50)^\top/121$、$\widetilde{\bm q}=(-225/121,225/242)^\top$，$\widetilde{\bm p}_0^\top\bm q=0$再次印证双共轭；分母$1125/1331$、$\alpha_1=11/25$，得$\bm x_2=(1/10,3/5)^\top$、$\bm r_2=\widetilde{\bm r}_2=\bm0$、$\rho_2=0$、$\beta_1=0$。

3. 停止：残差达标时先用$\bm b-\bm A\bm x_k$复核（`sec:ls-stationary-stopping`）再以“达到容差”结束，$\bm r_k\ne\bm0$而$\rho_k=0$时以“中断”结束、不当作收敛，$k=K$时“步数耗尽”，残差长期不降按停滞处理；例中第一轮后$\lVert\bm r_1\rVert_2=\sqrt{20}/11\approx0.41$、$\rho_1\ne0$，继续，第二轮后$\bm r_2=\bm0$，复核后以“达到容差”结束。第1—4步即式`eq:ls-bicg-update`—`eq:ls-bicg-beta`，两次矩阵作用各算一次并复用。

4. 最终结果：单独一行写出$\bm x_2=(1/10,3/5)^\top=\bm x_\star$；由小问题`eq:ls-krylov-projection`取$\bm V_1=\bm r_0$、$\bm W_1=\widetilde{\bm r}_0$得$22y=5$、$y=\alpha_0$，核对第一步；说明$\bm A$不对称、CG前提不成立，BiCG借影子序列维持双正交与双共轭，二维问题同样两步结束。

#### 15.8.3 算法分析

###### paragraph：正确性

1. 说明BiCG选近似的依据是双正交关系，证明沿用CG的归纳，只把每个内积的左因子换成影子序列。

2. 定理“BiCG的双正交性”（`thm:ls-bicg-biorthogonality`）：精确算术下此前配对量与分母非零时，$i\ne j$有$\widetilde{\bm r}_i^\top\bm r_j=0$、$\widetilde{\bm p}_i^\top\bm A\bm p_j=0$，且$\bm r_k\perp\mathcal K_k(\bm A^\top,\widetilde{\bm r}_0)$，这一条件确定了BiCG的近似。

3. 证明“双正交”：由归纳假设得$\widetilde{\bm p}_k^\top\bm r_k=\rho_k$，代入步长得$\widetilde{\bm p}_k^\top\bm r_{k+1}=0$，对$i<k$用双共轭性；互换两序列角色得影子残差的对应结论。

4. 证明“双共轭”：由$\bm A^\top\widetilde{\bm p}_i=(\widetilde{\bm r}_i-\widetilde{\bm r}_{i+1})/\alpha_i$与刚证的双正交算出$\widetilde{\bm p}_i^\top\bm A\bm r_{k+1}$，$i<k$时为零，$i=k$时为$-\rho_{k+1}/\alpha_k$，恰与$\beta_k\widetilde{\bm p}_k^\top\bm A\bm p_k=\rho_{k+1}/\alpha_k$抵消；另一方向同理。

5. 证明“检验空间”：$\rho_i\ne0$与双正交性给出影子残差线性无关，它们张成$\mathcal K_k(\bm A^\top,\widetilde{\bm r}_0)$，$\bm r_k$与之正交。

###### paragraph：收敛性与数值敏感度

1. 双正交条件不是范数最小化，BiCG没有单调最小性，残差可能波动，一般不存在只靠$\kappa_2(\bm A)$承诺的统一下降速度；即使解唯一，配对量也可能在残差非零时为零而中断，配对量很小时放大舍入误差；保留这一限制，不展开中断的分类与修补。

###### paragraph：计算代价

1. 每轮一次$\bm A$与一次$\bm A^\top$乘向量，工作向量数量固定；与GMRES相比以失去最小残差性和需要转置作用换取短递推，$\bm A^\top$难以获得时不适用。

### 15.9 稳定化双共轭梯度法

1. 设$\bm A$是一般实可逆方阵，紧接15.8 BiCG的结果进入：BiCG以影子序列满足Petrov--Galerkin条件，但影子残差的更新`eq:ls-bicg-update`每轮需要$\bm A^\top$乘向量，双正交又不最小化任何范数，残差可能振荡；定义van der Vorst提出的稳定化双共轭梯度法BiCGSTAB：仍取BiCG的步长与组合系数，但只用固定影子向量$\widehat{\bm r}$计算，不生成影子序列、不需要$\bm A^\top$，每轮在BiCG半步后接一个一维残差最小化半步（相当于只走一步的GMRES）。

2. 说明它是GMRES存储过大、BiCG振荡过剧时的常用选择。

#### 15.9.1 主要思想

补充图解：BiCGSTAB的局部残差最小化。灰色虚线是候选残差$\bm s_k-\omega\bm t_k$的端点所在直线，绿色向量是从原点到这条直线的最短向量；黄色箭头为修正量$-\omega_k\bm t_k$。图示$\bm t_k\ne\bm0$，仅保证$\lVert\bm r_{k+1}\rVert_2\leq\lVert\bm s_k\rVert_2$，不保证跨轮残差单调下降。

###### paragraph：BiCG的残差多项式

1. BiCG的原、影子序列用同一组系数更新，由同样的残差多项式$\phi_k$与方向多项式$\pi_k$生成，写出它们的递推与$\bm r_k=\phi_k(\bm A)\bm r_0$、$\widetilde{\bm r}_k=\phi_k(\bm A^\top)\widetilde{\bm r}_0$等，并给出最高次项系数。

###### paragraph：把影子多项式移到内积另一侧

1. 系数只通过内积用到影子序列，把$\bm A^\top$的多项式移到另一侧；由$\bm r_k\perp\mathcal K_k(\bm A^\top,\widetilde{\bm r}_0)$，对任何$k$次$\psi_k$，$\widetilde{\bm r}_0^\top\psi_k(\bm A)\bm r_k$只取决于最高次项系数，所以可用固定向量的内积求出同样的$\alpha_k,\beta_k$而不需要$\bm A^\top$。

###### paragraph：用平滑多项式代替影子多项式

1. 取$\psi_k(t)=\prod_{j<k}(1-\omega_jt)$并让原序列携带它，$\bm r_k=\psi_k(\bm A)\phi_k(\bm A)\bm r_0$、$\bm p_k=\psi_k(\bm A)\pi_k(\bm A)\bm r_0$，只用$\bm A$递推；$\omega_k$局部最小化残差而起平滑作用；固定影子向量$\widehat{\bm r}$通常取$\bm r_0$，每轮分两个半步再形成新方向。

###### paragraph：BiCG半步

1. 把$\phi_k$推进到$\phi_{k+1}$：步长式`eq:ls-bicgstab-alpha`中$\psi_k$的因子在分子分母中抵消，中间残差式`eq:ls-bicgstab-intermediate`，使$\widehat{\bm r}^\top\bm s_k=0$。

###### paragraph：残差最小化半步

1. 把$\psi_k$推进到$\psi_{k+1}$：沿$\bm s_k$走$\omega_k$，式`eq:ls-bicgstab-omega`使$\lVert\bm s_k-\omega\bm t_k\rVert_2$最小，即一步GMRES；解与残差更新式`eq:ls-bicgstab-update`。

###### paragraph：新方向

1. 由$\pi_{k+1}=\phi_{k+1}+\beta\pi_k$乘以$\psi_{k+1}$得新方向；最高次项系数一轮中分别多乘$-\omega$与$-\alpha$，所以BiCG的配对量之比等于这里之比乘$\alpha/\omega$，得式`eq:ls-bicgstab-direction`；定理`thm:ls-bicgstab-bicg-relation`说明系数与BiCG相同、残差为BiCG残差乘$\psi_k(\bm A)$。

###### paragraph：代价

1. 每轮两次$\bm A$乘向量、不需$\bm A^\top$；局部最小只相对于中间残差，不保证单调下降；保留BiCG的中断（$\rho_k=0$或$\widehat{\bm r}^\top\bm v_k=0$），且$\omega_k=0$时无法计算下一轮的$\beta$。

#### 15.9.2 算法实现

1. 说明输入实可逆方阵与$\bm b$、只需$\bm A$乘向量，输出近似解；参数另含固定影子向量（默认$\widehat{\bm r}=\bm r_0$），阈值$\tau$沿用第14章但每轮检查两次（含中间残差）；$\rho_k$、$\widehat{\bm r}^\top\bm v_k$与$\omega_k$都可能在残差非零时为零，相除前检查。

2. 每轮先作BiCG半步、检查中间残差，再作残差最小化半步，更新解与残差后形成新方向，两个半步各一次$\bm A$乘向量；写法参照文献中的模板；对称贯穿例配$\widehat{\bm r}=\bm r_0$时BiCG就是CG，故沿用15.8的非对称系统$\bm A=\left[\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\right]$、$\bm b=(1,2)^\top$、$\bm x_0=\bm0$（精确解$(1/10,3/5)^\top$），取$\widehat{\bm r}=\bm r_0$执行，与BiCG的数值逐项比较。

###### paragraph：变量

1. 以列表列出：原处更新的近似$\bm x$与递推残差$\bm r$，固定影子向量$\widehat{\bm r}$，搜索方向$\bm p$，保留到本轮末的$\bm v=\bm A\bm p_k$，中间残差$\bm s$与$\bm t=\bm A\bm s_k$，保留到下一轮的配对量$\rho_k$，两个半步的步长$\alpha_k,\omega_k$（也用于$\beta_{k+1}$），轮次$k$；除矩阵外共七个向量。

###### paragraph：初始化

1. 把残差初始化为$\bm r_0=\bm b-\bm A\bm x_0$，检查$\widehat{\bm r}^\top\bm r_0\ne0$，令$\rho_0=\widehat{\bm r}^\top\bm r_0$、$\bm p_0=\bm r_0$、$k=0$，$\lVert\bm r_0\rVert_2\le\tau$时复核后直接输出；例中$\widehat{\bm r}=\bm r_0=\bm p_0=(1,2)^\top$、$\rho_0=5$、$\lVert\bm r_0\rVert_2\approx2.24$。

###### paragraph：每轮更新

1. 第$k$轮依次：BiCG半步，$\bm v_k=\bm A\bm p_k$、$\alpha_k$、$\bm s_k$，例中第一轮$\bm v_0=(6,8)^\top$、$\widehat{\bm r}^\top\bm v_0=22$、$\alpha_0=5/22$、$\bm s_0=(-4/11,2/11)^\top$，中间近似与中间残差正是BiCG第一步的$\bm x_1,\bm r_1$，且$\widehat{\bm r}^\top\bm s_0=0$；检查中间残差，达标时复核后输出$\bm x_k+\alpha_k\bm p_k$、不走第二个半步，因而以后不会出现$0/0$，例中$\lVert\bm s_0\rVert_2\approx0.407$未达标；求$\omega_k$，例中$\bm t_0=(-14/11,-2/11)^\top$、$\bm t_0^\top\bm s_0=52/121$、$\bm t_0^\top\bm t_0=200/121$、$\omega_0=13/50$。

2. 更新解与残差，新残差达标时复核后输出，例中$\bm x_1=(73/550,138/275)^\top$、$\bm r_1=(-9/275,63/275)^\top$，直接计算核对，$\lVert\bm r_1\rVert_2\approx0.231$小于中间残差的$0.407$，下降来自第二个半步；形成新方向，按式`eq:ls-bicgstab-direction`算$\rho_{k+1}$、$\beta_{k+1}$、$\bm p_{k+1}$后令$k\leftarrow k+1$，例中$\rho_1=117/275$、$\beta_1=9/121$（同BiCG的$\beta_0$）、$\bm p_0-\omega_0\bm v_0=(-14/25,-2/25)^\top$、$\bm p_1=(-9,27)^\top/121$；随后给出第二轮第1步$\bm v_1=(-9,63)^\top/121$、$\widehat{\bm r}^\top\bm v_1=117/121$、$\alpha_1=11/25$（同BiCG的$\alpha_1$）、$\bm s_1=\bm0$。

3. 停止：三种原因——中间残差或新残差达标时按14.7用原矩阵复核；残差非零而$\widehat{\bm r}^\top\bm v_k$、$\bm t_k^\top\bm t_k$、$\rho_{k+1}$为零或相对过小，或$\omega_k=0$，报告中断或采用明确的重启策略（如以当前残差重选影子向量），不误报为达标；做满$K$轮；例中第二轮第2步发现$\bm s_1=\bm0$，复核后退出，不计算$\bm t_1$与$\omega_1$以免零除。

4. 最终结果：输出第二轮中间近似$\bm x_1+\alpha_1\bm p_1=(1/10,3/5)^\top=\bm x_\star$，原残差为零；$\alpha_0,\beta_1,\alpha_1$分别等于BiCG的$\alpha_0,\beta_0,\alpha_1$，印证定理`thm:ls-bicgstab-bicg-relation`，且未用$\bm A^\top$；残差长度依次$2.24$、$0.407$、$0.231$、$0$；在对称贯穿例`ex:ls-stationary-running-example`上同样执行得$\alpha_0=1/4$、$\omega_0=3/10$、$\beta_1=1/16$、$\alpha_1=4/11$，输出$(1/11,7/11)^\top$，系数即CG的系数。

#### 15.9.3 算法分析

###### paragraph：正确性

1. 为比较两种方法，用残差多项式描述BiCG：由其更新式存在多项式$P_k,T_k$使残差与方向为$P_k(\bm A)\bm r_0$、$T_k(\bm A)\bm r_0$，满足$P_{k+1}=P_k-\alpha_k^BzT_k$、$T_{k+1}=P_{k+1}+\beta_k^BT_k$，影子序列用同样的系数；第二个半步对应一次因子，记平滑多项式$Q_k(z)=\prod_{j<k}(1-\omega_jz)$。

2. 定理“BiCGSTAB与BiCG的关系”（`thm:ls-bicgstab-bicg-relation`）：取$\widehat{\bm r}=\widetilde{\bm r}_0$、精确算术且均未中断时，$\bm r_k=Q_k(\bm A)P_k(\bm A)\bm r_0$、$\bm p_k=Q_k(\bm A)T_k(\bm A)\bm r_0$，且$\alpha_k=\alpha_k^B$、$\beta_k=\beta_{k-1}^B$。

3. 证明“正交关系”：定义线性泛函$L[f]=\widehat{\bm r}^\top f(\bm A)\bm r_0$，把BiCG的双正交与双共轭写成$L[z^jP_k]=0$、$L[z^{j+1}T_k]=0$（$j<k$），并由两条递推得首项系数之比$\pi_{k+1}/\pi_k=-\alpha_k^B$、$\chi_{k+1}/\chi_k=-\omega_k$。

4. 证明“配对量与步长”：低次项被正交关系消去，$\rho_k^B=\pi_kL[z^kP_k]$、$\rho_k=\chi_kL[z^kP_k]$，两种步长的分母同样只差$\pi_k$与$\chi_k$，约去后相等。

5. 证明“表示的保持”：由步长相等写出$\bm s_k$与$\bm r_{k+1}$的多项式表示，代入首项系数之比得$\beta_k^B=\beta_{k+1}$，再由方向递推与$Q_{k+1}=(1-\omega_kz)Q_k$得$\bm p_{k+1}$的表示。

6. 定理后说明：精确算术且不中断时，第一个半步保持BiCG的Petrov--Galerkin条件，第二个半步只在BiCG残差多项式上再乘一个一次因子。

###### paragraph：第二个半步的作用

1. 一元二次式在$\omega_k$处取得最小值$\lVert\bm s_k\rVert_2^2-(\bm t_k^\top\bm s_k)^2/\lVert\bm t_k\rVert_2^2$，所以$\lVert\bm r_{k+1}\rVert_2\le\lVert\bm s_k\rVert_2$；但第一个半步可能使$\lVert\bm s_k\rVert_2$大于$\lVert\bm r_k\rVert_2$，故不保证整轮下降，也不保证在所有可逆系统上收敛，速度取决于实际形成的$Q_kP_k$。

###### paragraph：中断与数值敏感度

1. 稳定化半步不消除BiCG的中断，$\rho_k$或$\widehat{\bm r}^\top\bm v_k$为零的情形依然存在，另多了$\omega_k=0$使下一轮$\beta$无法计算；配对量或$\omega_k$很小时后续系数对舍入敏感，仍按公共准则复核原残差。

###### paragraph：计算代价

1. 完整一轮通常两次$\bm A$乘向量、不需要$\bm A^\top$、工作向量固定，在中间阶段终止时只需一次乘法；与BiCG相比每轮矩阵作用次数相同但都是$\bm A$，并多一次局部平滑。

### 15.10 LSQR算法

1. 设$\bm A\in\mathbb R^{m\times d}$可秩亏、方程可不相容，定义Paige与Saunders提出的LSQR：从零初值出发，第$k$步在$\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$中取使原残差最小的近似；紧接15.4.4，那里已把最小化化为双对角小最小二乘问题，基与系数由递推`eq:ls-golub-kahan-step`生成、关系`eq:ls-golub-kahan-relations`由定理`thm:ls-golub-kahan-relations`保证，不再重述；本节讨论怎样随双对角矩阵逐列增长逐步解出小问题，并只用短递推更新近似解。

#### 15.10.1 主要思想

###### paragraph：逐步长大的小问题

1. 由Golub--Kahan应用写出小问题式`eq:ls-lsqr-subproblem`，按元素写出$(k+1)\times k$下双对角矩阵$\bm B_k$；每步只添一列$(0,\ldots,0,\alpha_k,\beta_{k+1})^\top$（只有两个非零元）与一行，右端多一个零分量。

###### paragraph：沿用前一步的消元结果

1. 采用Paige与Saunders的反射式变换$\bm Q_i$（与MINRES的旋转只差第二行符号），前$k-1$步把$\bm B_{k-1}$消成上双对角矩阵（对角元$\rho_i$、上对角元$\theta_i$），以$k=3$按元素写出前两列，它们以后不再改变。

###### paragraph：新列只需两次变换

1. 新列只需最后一个旧变换$\bm Q_{k-1}$把$(0,\alpha_k)$变成$(\theta_k,\bar\rho_k)$，再由新变换$\bm Q_k$消去$\beta_{k+1}$；以$k=3$按元素写出新列经$\bm Q_2,\bm Q_3$的变化与整个矩阵在$\bm Q_3$前后的形状。

2. 实际中$\bm Q_k$构造后即作用于下一列与右端，写成$2\times3$块，逐元素比较得式`eq:ls-lsqr-rotation`，逐行说明构造$\bm Q_k$、作用于下一列与作用于右端；起步$\bar\rho_1=\alpha_1$、$\bar\phi_1=\beta_1$。

###### paragraph：右端与残差

1. 以$k=3$写出右端在$\bm Q_3$前后的变化；前$k$个方程由$\bm R_k$精确满足，$\bm y_k=\bm R_k^{-1}\bm f_k$，最小残差为$\lvert\bar\phi_{k+1}\rvert$；给出原残差与正规残差的估计式`eq:ls-lsqr-estimates`，有限精度下须复核。

###### paragraph：增量求解的两个好处

1. 每步只作用一个旧变换、构造一个新变换、更新两个右端分量，工作量与存储不随步数增长；两种残差都由几个标量读出，不必形成近似解。

###### paragraph：方向与解

1. 把$\bm V_k\bm R_k^{-1}$的第$i$列写成$\bm w_i/\rho_i$，比较$(\bm V_k\bm R_k^{-1})\bm R_k=\bm V_k$的第$k+1$列得方向递推式`eq:ls-lsqr-direction`，解按式`eq:ls-lsqr-update`逐步累加，只需保留一个旧方向；定理`thm:ls-lsqr-recursion`说明逐步计算正好解出小问题。

#### 15.10.2 算法实现

1. 每轮先作一步双对角化得$\bm B_k$的新一列，再作一次正交变换延续三角化，然后更新解与方向并读出两个残差估计；只需$\bm A$与$\bm A^\top$乘向量，以最小二乘为目标时用正规残差的绝对阈值$\tau_n\ge0$，以相容方程为目标时用第14章的$\mathrm{atol},\mathrm{rtol}$，停止与复核见14.7；在15.4的不相容系统$\bm A=\left[\begin{smallmatrix}1&0\\0&2\\0&0\end{smallmatrix}\right]$、$\bm b=(1,1,1)^\top$上执行，$\hat{\bm x}=(1,1/2)^\top$、最优残差$(0,0,1)^\top$，只列求解器用到的量，15.11继续沿用。

###### paragraph：变量

1. 以列表列出：双对角化的当前基向量$\bm u\in\mathbb R^m$、$\bm v\in\mathbb R^d$（连同工作向量按15.4保存，不保存整组基），本轮系数$\alpha_{k+1},\beta_{k+1}$（$\alpha_k$留到扣除时使用），上一轮留下的$\bar\rho_k,\bar\phi_k$，本轮变换定下的$\rho_k,\theta_{k+1},\phi_k$与$c_k,s_k$（用完即弃），方向$\bm w\in\mathbb R^d$，近似解$\bm x\in\mathbb R^d$，轮次$k$。

###### paragraph：初始化

1. $K=0$时输出$\bm x_0=\bm0$；否则按式`eq:ls-golub-kahan-start`起步，$\beta_1=0$或$\alpha_1=0$时零向量已满足正规方程而输出$\bm x_0$；初始正规残差$\alpha_1\beta_1\bm v_1$的长度与起步共用同一次$\bm A^\top$乘法，已满足条件时也输出$\bm x_0$。

2. 否则初始化$\bm x_0=\bm0$、$\bm w_1=\bm v_1$、$\bar\rho_1=\alpha_1$、$\bar\phi_1=\beta_1$、$k=1$；例中$\bm w_1=\bm v_1=(1,2)^\top/\sqrt5$、$\bar\rho_1=\sqrt{5/3}$、$\bar\phi_1=\sqrt3$，初始正规残差长度$\sqrt5$未达标。

###### paragraph：每轮更新

1. 第$k$轮依次：双对角化一步，按递推`eq:ls-golub-kahan-step`得$\beta_{k+1},\bm u_{k+1},\alpha_{k+1},\bm v_{k+1}$，零系数时后续步骤照常完成、只跳过不存在的新基；正交变换按式`eq:ls-lsqr-rotation`；更新解按式`eq:ls-lsqr-update`；若生成了$\bm v_{k+1}$则按式`eq:ls-lsqr-direction`更新方向，排在更新解之后，因为两者都用旧的$\bm w_k$。每步给出例中第一轮的值：$\beta_2\approx1.3166$、$\alpha_2\approx0.9115$、$\bm v_2=(-2,1)^\top/\sqrt5$；$\rho_1=\sqrt{17/5}\approx1.8439$、$c_1=5/\sqrt{51}$、$s_1=\sqrt{26/51}$、$\theta_2=6/\sqrt{85}$、$\bar\rho_2=-\sqrt{90/221}$、$\phi_1=5/\sqrt{17}$、$\bar\phi_2=\sqrt{26/17}$；$\bm x_1=5(1,2)^\top/17$；$\bm w_2=(-40,5)^\top/(17\sqrt5)$。

2. 第二轮集中给出：$\beta_3=\sqrt{10/13}\approx0.8771$、$\alpha_3=0$，未知量空间已被取尽，不再生成$\bm v_3,\bm w_3$；$\rho_2=\sqrt{20/17}\approx1.0847$、$c_2=-3/\sqrt{26}$、$s_2=\sqrt{17/26}$、$\phi_2=-3/\sqrt{17}$、$\bar\phi_3=1$、$\theta_3=\bar\rho_3=0$；$\bm x_2=\bm x_1+(\phi_2/\rho_2)\bm w_2=(1,1/2)^\top$。

3. 停止：按式`eq:ls-lsqr-estimates`读出两个估计，达阈值、出现零系数或做满$K$轮时按14.7用真实残差按目标复核后输出，否则进入下一轮；零系数使相应估计为零，出现零$\rho_k$、明显失去正交性或残差长期不降时分别报告原因；例中第一轮估计$\sqrt{26/17}\approx1.2367$与$6\sqrt5/17\approx0.7892$，与直接计算的$\bm r_1=(12,-3,17)^\top/17$、$\bm A^\top\bm r_1=(12,-6)^\top/17$的长度吻合，继续；第二轮估计为$1$与$0$，复核$\bm r_2=(0,0,1)^\top$、$\bm A^\top\bm r_2=\bm0$后退出。

4. 最终结果：例中$\bm R_2=\left[\begin{smallmatrix}\sqrt{17/5}&6/\sqrt{85}\\0&\sqrt{20/17}\end{smallmatrix}\right]$、$\bm f_2=(5,-3)^\top/\sqrt{17}$，回代得$\bm y_2=(2/\sqrt5,-3/(2\sqrt5))^\top$，单独一行写出$\bm x_2=\bm V_2\bm y_2=(1,1/2)^\top=\hat{\bm x}$，与逐步累加一致；再由小问题的正规方程$\bm B_2^\top\bm B_2\bm y=\alpha_1\beta_1\bm e_1$（$\bm B_2^\top\bm B_2=\left[\begin{smallmatrix}17/5&6/5\\6/5&8/5\end{smallmatrix}\right]$）独立核对；原残差停在长度$1$，即$\bm b$中无法拟合的第三个分量。

#### 15.10.3 算法分析

###### paragraph：正确性

1. 说明先证递推解出小问题，并给出两个残差估计的来源。

2. 定理“LSQR递推的正确性”（`thm:ls-lsqr-recursion`）：双对角化在第$k$轮前未终止时，$\bm x_k=\bm V_k\bm y_k$是$\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$中使原残差最小的点，两个残差长度由式`eq:ls-lsqr-estimates`给出。

3. 证明“化为小问题”：由Golub--Kahan关系与$\bm b=\bm U_{k+1}\beta_1\bm e_1$把残差写成$\bm U_{k+1}(\beta_1\bm e_1-\bm B_k\bm y)$，正交列保长。

4. 证明“小问题的解”：新列只在第$k,k+1$行非零，此前变换不触及其第$k+1$行，一次新变换就能延续三角化，得$\bm Q_k[\bm B_k\ \beta_1\bm e_1]$的上双对角形与$\bm f_k$；最小点$\bm R_k^{-1}\bm f_k$、最小值$\lvert\bar\phi_{k+1}\rvert$；比较$(\bm V_k\bm R_k^{-1})\bm R_k=\bm V_k$的列得方向递推，已定的量不再改动，回代化为逐步累加。

5. 证明“正规残差”：由最优性$\bm B_k^\top\bm g_k=\bm0$与关系`eq:ls-golub-kahan-relations`第二式得$\bm A^\top\bm r_k=\alpha_{k+1}(\bm e_{k+1}^\top\bm g_k)\bm v_{k+1}$，只有最后一次变换触及第$k+1$分量，得$\bm e_{k+1}^\top\bm g_k=-c_k\bar\phi_{k+1}$。

6. 定理后由$\bar\rho_1=\alpha_1>0$与$\bar\rho_{k+1}=-c_k\alpha_{k+1}$归纳说明正常步骤中$\rho_k>0$，除非双对角化已给出零系数而结束，不会出现零除数。

###### paragraph：残差的单调性与选出的解

1. 候选空间嵌套使精确算术下原残差不增，正规残差无此保证、可能某步上升；零初值使各步留在$\operatorname{range}(\bm A^\top)$中，到达正规方程时$\bm x_k$是与$\operatorname{null}(\bm A)$正交的最小二乘解，即第11章的$\bm A^\dagger\bm b$，$\alpha_{k+1}=0$正是这种情形。

###### paragraph：与正规方程上CG的关系

1. 定理“LSQR与正规方程上的CG”（`thm:ls-lsqr-cg-equivalence`）：精确算术下两者都未终止时，LSQR第$k$步等于对$\bm A^\top\bm A\bm x=\bm A^\top\bm b$从零初值施行CG的第$k$步。

2. 证明分三部分：“CG的准则”由$\bm A^\top\bm A$在行空间上正定与定理`thm:ls-cg-convergence`得CG最小化$\lVert\bm A(\bm x-\hat{\bm x})\rVert_2$；“LSQR的准则”由$\hat{\bm r}\perp\operatorname{range}(\bm A)$的勾股分解得LSQR最小化同一函数；“唯一性”由$\bm A$在$\operatorname{range}(\bm A^\top)$上单射得最小点唯一。

###### paragraph：收敛速度与数值敏感度

1. 由等价把CG的界搬到LSQR：收敛快慢由非零奇异值平方的分布决定，满列秩时$\sqrt{\kappa_2(\bm A^\top\bm A)}=\kappa_2(\bm A)$，得$\lVert\bm A(\bm x_k-\hat{\bm x})\rVert_2\le2((\kappa_2(\bm A)-1)/(\kappa_2(\bm A)+1))^k\lVert\bm A\hat{\bm x}\rVert_2$。

2. 说明LSQR不形成Gram矩阵，避免第13章正规方程法的信息丢失，但不消除原问题的病态性；有限精度下正交性与两个估计都会偏离，仍按14.7复核。

###### paragraph：计算代价

1. 每轮一次$\bm A$与一次$\bm A^\top$乘向量，另有十几次标量运算、一次正交变换与两次长度为$d$的向量更新，工作存储$O(m+d)$；LSQR也能解相容方程，但每轮多一次转置作用，是否划算要结合矩阵结构与精度目标比较。

### 15.11 LSMR算法

1. 说明问题类与LSQR相同（长方、可秩亏、可不相容），定义Fong与Saunders提出的LSMR：从零初值出发，在同一Krylov子空间$\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$中改以正规残差$\lVert\bm A^\top(\bm b-\bm A\bm x)\rVert_2$最小为选解准则，即判断是否到达最小二乘解所看的量；点明本节紧接15.4.4 Golub--Kahan的应用（`sec:ls-golub-kahan-application`），那里已把正规残差化为关于$\bm B_k$的小问题，本节说明怎样不形成$\bm B_k^\top\bm B_k$而逐步解出它。

#### 15.11.1 主要思想

###### paragraph：逐步长大的小问题

1. 由Golub--Kahan应用把正规残差写成$\bm V_{k+1}(\alpha_1\beta_1\bm e_1-\bm C_k\bm y)$，式`eq:ls-lsmr-subproblem`，小问题为$\min\lVert\alpha_1\beta_1\bm e_1-\bm C_k\bm y\rVert_2$；$\alpha_{k+1}=0$时删去末行。

2. 以$k=3$按元素写出$\bm C_3$（上部为三对角的$\bm B_k^\top\bm B_k$），指出它与MINRES的$\overline{\bm T}_k$同形、每步添一列一行，但直接形成元素就是形成Gram矩阵、会损失精度，所以从$\bm B_k$出发用两层旋转逐列消元。

###### paragraph：两层分解

1. 第一层把$\bm B_k$消成上双对角$\bm R_k$，由旋转保内积得$\bm B_k^\top\bm B_k=\bm R_k^\top\bm R_k$，由$\theta_{k+1}\rho_k=\alpha_{k+1}\beta_{k+1}$得末行，于是分解式`eq:ls-lsmr-factorization`；以$k=3$按元素写出$\bm R_3$与下双对角的$\bm L_3$，换元$\bm t=\bm R_k\bm y$后小问题与LSQR同形，需第二层消元$\bm L_k$。

###### paragraph：第一层：消元$\bm B_k$

1. 采用MINRES的旋转约定；$\bm B_k$的新列只需最后一个旧旋转$\bm G_{k-1}$与新旋转$\bm G_k$，以$k=3$按元素写出新列的变化；$\bm G_k$提前作用于下一列，得式`eq:ls-lsmr-first-rotation`并逐行说明；$\rho_k,\theta_{k+1}$与LSQR同名量相同，第一层不作用于右端。

###### paragraph：第二层：消元$\bm L_k$

1. 第一层给出的$\rho_k,\theta_{k+1}$恰是$\bm L_k$的新列；第二层旋转$\bar{\bm G}_i$把它消成上双对角$\bar{\bm R}_k$，新列只需$\bar{\bm G}_{k-1}$与$\bar{\bm G}_k$；以$k=3$按元素写出新列的变化与整个矩阵在$\bar{\bm G}_3$前后的形状。

2. 指出新列要等第一层算出$\theta_{k+1}$才完整，旧旋转在本步补上；右端只经过第二层旋转；得式`eq:ls-lsmr-second-rotation`并逐行说明，起步$\bar c_0=1$、$\bar s_0=0$、$\bar\zeta_1=\alpha_1\beta_1$。

###### paragraph：右端与残差

1. 以$k=3$写出右端在$\bar{\bm G}_3$前后的变化；小问题化为上块$\bm z_k-\bar{\bm R}_k\bm t$与末分量$\bar\zeta_{k+1}$，得正规残差估计式`eq:ls-lsmr-estimate`，单调不增；不直接给出原残差。

###### paragraph：方向与解

1. 由$\bm x_k=\bm V_k\bm R_k^{-1}\bar{\bm R}_k^{-1}\bm z_k$，比较两层上双对角因子的第$k$列得两层方向与解的递推式`eq:ls-lsmr-update`，只需保留两个旧方向；每步作用两个旧旋转、构造两个新旋转，工作量与存储不随步数增长；定理`thm:ls-lsmr-minres-equivalence`说明逐步计算正好解出小问题。

#### 15.11.2 算法实现

1. 说明输入、阈值$\tau_n$或`sec:ls-stationary-stopping`的$\mathrm{atol},\mathrm{rtol}$、步数上限$K$与零初值；每轮依次扩展双对角化、第一层旋转得$\bm L_k$新列、第二层旋转消去并变换右端、更新两层方向与解；在不相容长方系统上执行。

###### paragraph：变量

1. 以列表列出：当前基向量$\bm u\in\mathbb R^m$、$\bm v\in\mathbb R^d$；双对角化系数$\alpha_{k+1},\beta_{k+1}$（$\alpha_k$留到扣除时用）；第一层旋转的$\bar\alpha_k,\rho_k,c_k,s_k,\theta_{k+1}$（$\theta_k$留给方向更新）；第二层旋转的$\bar c_{k-1},\bar s_{k-1}$与$\bar\theta_k,\bar\rho_k,\bar c_k,\bar s_k$；右端分量$\zeta_k$与末分量$\bar\zeta_{k+1}$（正规残差估计）；两层方向$\bm w,\bar{\bm w}$与近似解$\bm x$；轮次$k$。

###### paragraph：初始化

1. $K=0$时输出$\bm x_0$；否则按`eq:ls-golub-kahan-start`算$\beta_1,\bm u_1,\alpha_1,\bm v_1$，$\beta_1=0$或$\alpha_1=0$时输出$\bm x_0$；否则置$\bm x_0=\bm w_0=\bar{\bm w}_0=\bm0$、$\theta_1=0$、$\bar\alpha_1=\alpha_1$、$\bar\zeta_1=\alpha_1\beta_1$、$\bar c_0=1$、$\bar s_0=0$、$k=1$，$\bar\zeta_1=\lVert\bm A^\top\bm b\rVert_2$已达阈值时输出，并说明占位量的作用；例中$\beta_1=\sqrt3$、$\alpha_1=\sqrt{5/3}$、$\bm v_1=(1,2)^\top/\sqrt5$、$\bar\zeta_1=\sqrt5\approx2.2361$，未达目标。

###### paragraph：每轮更新

1. 第$k$轮依次：扩展双对角化（`eq:ls-golub-kahan-step`，零系数的约定），例中第一轮$\beta_2\approx1.3166$、$\alpha_2\approx0.9115$、$\bm v_2=(-2,1)^\top/\sqrt5$；第一层旋转（按$2\times2$块写出$(\bar\alpha_k,\beta_{k+1})$与下一列在$\bm G_k$前后的数值，`eq:ls-lsmr-first-rotation`），例中$\rho_1=\sqrt{17/5}\approx1.8439$、$c_1=5/\sqrt{51}$、$s_1=\sqrt{26/51}$、$\theta_2=6/\sqrt{85}\approx0.6508$、$\bar\alpha_2=\sqrt{90/221}\approx0.6382$；第二层旋转（按$2\times2$块写出新列与右端在$\bar{\bm G}_k$前后的数值，`eq:ls-lsmr-second-rotation`），例中$\bar\theta_1=0$、$\bar\rho_1=\sqrt{65/17}\approx1.9554$、$\bar c_1=17/(5\sqrt{13})$、$\bar s_1=6/(5\sqrt{13})$、$\zeta_1=17/\sqrt{65}\approx2.1086$、$\bar\zeta_2=-6/\sqrt{65}$；更新方向与解（`eq:ls-lsmr-update`，$\bm w_k$用上一轮的$\theta_k$），例中$\bm w_1=(1,2)^\top/\sqrt{17}$、$\bar{\bm w}_1=(1,2)^\top/\sqrt{65}$、$\bm x_1=17(1,2)^\top/65$。

2. 在第4步后集中给出例中第二轮：$\beta_3=\sqrt{10/13}\approx0.8771$、$\alpha_3=0$，$\rho_2=\sqrt{20/17}\approx1.0847$、$c_2=3/\sqrt{26}$、$\theta_3=\bar\alpha_3=0$；第二层旋转为恒等，$\bar\theta_2=12/\sqrt{1105}\approx0.3610$、$\bar\rho_2=2\sqrt{17}/\sqrt{65}\approx1.0228$、$\zeta_2=-6/\sqrt{65}$、$\bar\zeta_3=0$；$\bm w_2=(-4,1/2)^\top/\sqrt{17}$、$\bar{\bm w}_2=(-8,1/4)^\top/\sqrt{65}$，$\bm x_2=(1,1/2)^\top$。

3. 停止：读估计$\lvert\bar\zeta_{k+1}\rvert$（`eq:ls-lsmr-estimate`），以最小二乘为目标时达到$\tau_n$、出现零系数或达到$K$就按14.7复核后输出，以相容方程为目标时在候选终止处计算原残差；$\alpha_{k+1}=0$使$\theta_{k+1}=\bar s_k=0$从而$\bar\zeta_{k+1}=0$；零分母、失去正交性或残差不降时在相除前检查并报告原因；例中第一轮直接算得$\bm A^\top\bm r_1=(48,-6)^\top/65$，长度$6/\sqrt{65}\approx0.7442=\lvert\bar\zeta_2\rvert$，继续；第二轮$\alpha_3=0$、$\bar\zeta_3=0$，复核$\bm r_2=(0,0,1)^\top$、$\bm A^\top\bm r_2=\bm0$后退出。

4. 最终结果：按元素写出$\bm R_2,\bar{\bm R}_2,\bm z_2$，$\bm x_2=\bm V_2\bm R_2^{-1}\bar{\bm R}_2^{-1}\bm z_2=\hat{\bm x}$，原残差停在$1$；单独一行写出正规残差$\sqrt5\approx2.2361$、$0.7442$、$0$，单调不增；与LSQR对照，第一步正规残差$0.7442$小于LSQR的约$0.7892$，原残差约$1.2440$大于LSQR的约$1.2367$，同一一维空间中因优化对象不同选出不同的点。

5. 直接解小问题核对：$\bm C_1=(17/5,6/5)^\top$，最小点$y=17\sqrt5/65$，$y\bm v_1=\bm x_1$；$k=2$时$\bm C_2$末行为零，小问题成为$\bm B_2^\top\bm B_2\bm y=\alpha_1\beta_1\bm e_1$，等价于完整正规方程，解得$\hat{\bm x}$；可用来检查旋转符号、下标与旧量读取顺序。

#### 15.11.3 算法分析

###### paragraph：正确性

1. 说明两组旋转对应两层三角分解，由此一并写出最优性及与MINRES的关系。

2. 定理“LSMR的最小正规残差性及与MINRES的等价”（`thm:ls-lsmr-minres-equivalence`）：双对角化在第$k$轮前未终止时，$\bm x_k$是$\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$中使正规残差最小的唯一点，最小值$\lvert\bar\zeta_{k+1}\rvert$，也等于对正规方程从零初值施行MINRES的第$k$步。

3. 证明“化为小问题”：由15.4.4的原残差表示左乘$\bm A^\top$，用关系`eq:ls-golub-kahan-relations`第二式及$\bm B_k^\top\bm e_1=\alpha_1\bm e_1$、$\bm e_{k+1}^\top\bm B_k=\beta_{k+1}\bm e_k^\top$得式`eq:ls-lsmr-subproblem`，正交列保长。

4. 证明“两层旋转”：第一层逐列把$\bm B_k$化为上三角，给出$\bm B_k^\top\bm B_k=\bm R_k^\top\bm R_k$，由$\theta_{k+1}\rho_k=\alpha_{k+1}\beta_{k+1}$得分解`eq:ls-lsmr-factorization`、换元可逆；第二层逐列三角化$\bm L_k$，写出旧旋转与本轮旋转作用于新列与右端的两个二阶乘积，即式`eq:ls-lsmr-second-rotation`；最小点$\bm x_k=\bm V_k\bm R_k^{-1}\bar{\bm R}_k^{-1}\bm z_k$，比较$\bm W_k\bm R_k=\bm V_k$与$\bar{\bm W}_k\bar{\bm R}_k=\bm W_k$的列得两条方向递推，已定分量不变而逐步累加。

5. 证明“唯一性与MINRES”：$\operatorname{range}(\bm V_k)\subseteq\operatorname{range}(\bm A^\top)$而$\operatorname{null}(\bm A^\top\bm A)=\operatorname{null}(\bm A)$与之正交，故最小点唯一；MINRES对$\bm A^\top\bm A$、右端$\bm A^\top\bm b$与零初值在同一空间最小化同一函数，两者第$k$步相同。

6. 定理后说明正常步骤中$\rho_k,\bar\rho_k$为正：前者同LSQR，后者由$\bar\rho_k\ge\lvert\bar c_{k-1}\rvert\rho_k$与$\bar c_i$均为非零量之比得出。

###### paragraph：残差的单调性

1. 候选空间嵌套使正规残差单调不增；原残差同样单调不增，理由是LSMR近似是截至当前步各LSQR近似的凸组合、$\bm x_{k+1}^{\mathrm M}$又是$\bm x_k^{\mathrm M}$与$\bm x_{k+1}^{\mathrm Q}$的凸组合，而原残差平方是凸函数且$\bm x_{k+1}^{\mathrm Q}$在包含$\bm x_k^{\mathrm M}$的空间上使它最小（正文说明“可以证明”而未展开凸组合的证明）；正规残差单调不增使按$\tau_n$停止更平稳，原残差则是LSQR每步最小，与实现中的第一步对照一致。

###### paragraph：选出的解与收敛速度

1. 零初值使各步留在行空间，到达正规方程时选出$\bm A^\dagger\bm b$；由等价定理，LSMR在行空间上等价于正规方程上的MINRES，速度受非零奇异值平方分布控制；小奇异值与正交性损失仍影响精度，两个残差单调不推出误差单调，仍需真实残差复核。

###### paragraph：与缩放方向的关系

1. 说明文献常用缩放方向$\bm h_k=\rho_k\bm w_k$、$\bar{\bm h}_k=\rho_k\bar\rho_k\bar{\bm w}_k$，代入得等价递推（$\bm h_1=\bm v_1$、$\rho_0=\bar\rho_0=1$、$\bar{\bm h}_0=\bm0$），$\bm h_k$与Paige--Saunders原文LSQR所用的方向相同；两种写法乘法次数相同，只影响保存的标量。

###### paragraph：计算代价

1. 每轮核心仍是一次$\bm A$与一次$\bm A^\top$乘向量，比LSQR多一组标量旋转与一套方向$\bar{\bm w}_k$，保存$\bm u,\bm v,\bm w,\bar{\bm w},\bm x$，工作存储仍为$O(m+d)$。

### 15.12 预条件

1. 指出求解器只规定怎样在子空间中选解，步数却由系数矩阵决定；预条件不是另一种求解器，而是套在求解器外面的加速与预处理方法；预告主要思想、常见预条件方法与预条件的使用三部分，后者对左预条件、右预条件与PCG各举一个求解器写出计算过程。

#### 15.12.1 主要思想

1. 收敛慢的原因：Krylov方法的步数由谱决定，以CG误差界每步乘以$(\sqrt\kappa-1)/(\sqrt\kappa+1)$为例，步数大致与$\sqrt\kappa$成正比；网格加细或量级悬殊使条件数很大，Krylov方法要走很多步。

2. 用易解的近似矩阵改写方程：先把方程改写成同解而条件更好的方程；预条件选可逆$\bm M$，既接近$\bm A$又使$\bm M\bm z=\bm r$易解，左乘$\bm M^{-1}$后求解器面对$\bm M^{-1}\bm A$，$\bm M$越接近$\bm A$特征值越集中在$1$附近；以$\bm M=\bm A$与$\bm M=\bm I$说明两个要求相互牵制。

3. 实现方式：不求$\bm M^{-1}$、不形成$\bm M^{-1}\bm A$，每次需要时解一次辅助方程，代价最好与一次矩阵乘向量相当；$\bm M$须固定不变；由此引出怎样构造$\bm M$与怎样在求解器中使用两个问题。

#### 15.12.2 常见预条件方法

1. 说明三种构造分别取自第14章定常迭代的分裂与第12章的LU、Cholesky分解，由简到繁，越接近$\bm A$效果越好、代价越高；都以贯穿例$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$为例比较$\bm M$与$\bm A$的差别。

##### 15.12.2.1 对角预条件

###### paragraph：构造

1. 只保留对角部分$\bm M=\operatorname{diag}(a_{1,1},\ldots,a_{d,d})$，即Jacobi的分裂矩阵，求解为逐分量相除式`eq:ls-diagonal-preconditioner`；例中$\bm M=\operatorname{diag}(4,3)$，$\bm M^{-1}\bm A=\left[\begin{smallmatrix}1&1/4\\1/3&1\end{smallmatrix}\right]$的对角元都变为$1$。

###### paragraph：性质

1. 把每个方程按对角元缩放、消除尺度差异；$\bm A$对称正定时$\bm M$也对称正定；无额外存储、应用只需$d$次除法，但只能消除尺度差异。

###### paragraph：应用场景

1. 适合尺度相差大而非对角部分较小的矩阵；例$\bm A=\bm S\bm T\bm S$缩放后$\bm M^{-1}\bm A$与$\bm T$相似，图“对角缩放前后的特征值分布”（`fig:ls-preconditioned-spectrum`）显示特征值比由约$182.7$降到约$7.61$、CG收缩因子由约$0.862$降到约$0.468$；最小二乘问题用列范数作对角缩放。

##### 15.12.2.2 SSOR预条件

###### paragraph：构造

1. 为保留非对角信息借用SSOR迭代：写$\bm A=\bm D+\bm L+\bm L^\top$，一轮SSOR把残差变成修正量`eq:ls-ssor-correction`，这一线性映射记作$\bm M^{-1}$，得$\bm M=(\bm D+\omega\bm L)\bm D^{-1}(\bm D+\omega\bm L)^\top/[\omega(2-\omega)]$；$\omega=1$时$\bm M=\bm A+\bm L\bm D^{-1}\bm L^\top$。

2. 求解$\bm M\bm z=\bm r$拆成下三角求解、对角缩放与上三角求解三步，式`eq:ls-ssor-preconditioner`；例中$\omega=1$时$\bm M=\left[\begin{smallmatrix}4&1\\1&13/4\end{smallmatrix}\right]$只在右下角差$1/4$，对$(1,2)^\top$求解得$\bm y=(1/4,7/12)^\top$、$\bm t=(1,7/4)^\top$、$\bm z=(5/48,7/12)^\top$，即一轮SSOR所得的$\bm x_1$。

###### paragraph：性质

1. 还保留三角部分的信息，通常比对角预条件更接近$\bm A$；$\bm A$对称正定且$0<\omega<2$时$\bm M$对称正定；无额外因子存储，一次应用约为两次矩阵乘向量，扫掠难以并行，$\omega$须固定。

###### paragraph：应用场景

1. 适合中等规模对称正定稀疏矩阵（如椭圆型方程离散化），作为不付分解代价时对角预条件的改进；取$\omega=1$常常可用。

##### 15.12.2.3 不完全分解

###### paragraph：为什么要不完全

1. 完整分解给出$\bm M=\bm A$，但消元会在原为零的位置产生填充，因子远比$\bm A$稠密；不完全分解照常消元，但事先规定允许非零的位置集合$\mathcal S$（常取$\bm A$的非零位置），舍去$\mathcal S$之外的填充。

###### paragraph：不完全LU分解

1. 回顾不选主元的LU消元$l_{i,k}=w_{i,k}/w_{k,k}$、$w_{i,j}\leftarrow w_{i,j}-l_{i,k}w_{k,j}$；不完全LU只在$\mathcal S$中计算乘子与尾块更新，其余位置保持为零，通常不选主元；得到稀疏的$\widetilde{\bm L},\widetilde{\bm U}$，预条件取$\bm M=\widetilde{\bm L}\widetilde{\bm U}$，求解为一次前代`eq:ls-forward-substitution`与一次回代`eq:ls-back-substitution`；$\bm M$与$\bm A$的差来自被舍去的填充。

###### paragraph：不完全Cholesky分解

1. 对称正定时按Cholesky列公式只计算$\mathcal S$中的元素，式`eq:ls-incomplete-cholesky`，得稀疏下三角$\bm L$，预条件取$\bm M=\bm L\bm L^\top$；它是对称情形下的不完全LU，$\bm L$与$\widetilde{\bm L}$只差各列的正缩放因子。

###### paragraph：例子

1. 以三阶矩阵$\bm A$（行为$(4,1,1),(1,4,0),(1,0,4)$）为例，$\mathcal S$取其非零位置：完整消元第一步后在$(2,3),(3,2)$产生填充$-1/4$，第二步还要算$l_{3,2}=-1/15$；不完全LU舍去填充，得$\widetilde{\bm L}$、$\widetilde{\bm U}=\left[\begin{smallmatrix}4&1&1\\0&15/4&0\\0&0&15/4\end{smallmatrix}\right]$与$\bm M$，$\bm M$只在$(2,3),(3,2)$两处为$1/4$而与$\bm A$不同，正是被舍去填充的相反数。

2. 不完全Cholesky得$\bm L$，各列为$\widetilde{\bm L}$的各列乘以$2,\sqrt{15}/2,\sqrt{15}/2$，$\bm L\bm L^\top$给出同一个$\bm M$。

###### paragraph：性质

1. $\bm M$与$\bm A$之差来自舍去的填充，$\mathcal S$越大越接近$\bm A$、代价越高；舍去填充后开方量可能非正、不完全LU可能遇到零主元，须逐列检查，失败时报告或加对角移位重构；不完全Cholesky的$\bm M$对称正定，不完全LU一般不对称。

###### paragraph：应用场景

1. 一般稀疏矩阵最常用的预条件之一：对称正定用不完全Cholesky，非对称用不完全LU；需先付出构造与存储代价，适合条件很差、对角与SSOR不足的问题，或同一矩阵求解多个右端的情形。

#### 15.12.3 预条件的使用

1. 说明$\bm M^{-1}$乘在左边、右边或拆开乘在两边，三种矩阵彼此相似、特征值相同，区别在迭代看到的残差与未知量；写出左、右预条件式`eq:ls-left-right-preconditioning`。

##### 15.12.3.1 左预条件

###### paragraph：思想

1. 未知量仍是$\bm x$，求解器作用在$\bm M^{-1}\bm A$与$\bm M^{-1}\bm b$上，每次先乘$\bm A$再解一次辅助方程，GMRES与BiCGSTAB常用；MINRES须取对称正定$\bm M$、在$\bm M$诱导的内积下最小化$\lVert\bm r\rVert_{\bm M^{-1}}$。

2. 指出代价是扭曲残差：迭代看到$\bm M^{-1}\bm r$，阈值施加在预条件残差上，结束前须复核原残差；对最小二乘问题它是以$\bm M^{-\top}\bm M^{-1}$为权的加权目标（`sec:ls-weighted-ls`），一般改变解，故最小二乘求解器不用左预条件。

###### paragraph：计算过程：左预条件GMRES

1. 与GMRES相比只改初始残差与Arnoldi扩展中的一次辅助求解；在贯穿例上取$\bm M=\operatorname{diag}(4,3)$，$\widetilde{\bm A}=\left[\begin{smallmatrix}1&1/4\\1/3&1\end{smallmatrix}\right]$。

###### paragraph：变量

1. 沿用GMRES的全部变量，基张成$\mathcal K_j(\widetilde{\bm A},\tilde{\bm r}_0)$，$\lvert g_{j+1}\rvert$估计预条件残差；另有预条件$\bm M$。

###### paragraph：初始化

1. 把预条件残差初始化为$\tilde{\bm r}_0=\bm M^{-1}(\bm b-\bm A\bm x_0)$；例中$\tilde{\bm r}_0=(1/4,2/3)^\top$、$\beta=\sqrt{73}/12$、$\bm v_1=(3,8)^\top/\sqrt{73}$。

###### paragraph：每轮更新

1. 第$j$轮依次：乘矩阵并解$\bm M\bm w=\bm A\bm v_j$；Arnoldi正交化；作用旋转并更新右端；停止并复核原残差；例中第一轮$\bm w=(5,9)^\top/\sqrt{73}$、$h_{1,1}=87/73$、$h_{2,1}=13/73$、$\lvert g_2\rvert=13/(12\sqrt{106})\approx0.1052$，此时$\bm x_1=(87/424,29/53)^\top$的原残差约$0.3986$，GMRES报告的残差小了将近$4$倍；第二轮$h_{3,2}=0$退出。

2. 最终回代得$\bm x_2=\bm x_\star$，与无预条件GMRES对照，说明估计与原残差不等即左预条件对残差的扭曲。

##### 15.12.3.2 右预条件

###### paragraph：思想

1. 求解器作用在$\bm A\bm M^{-1}$上、迭代变量为$\bm y=\bm M\bm x$，每次先解辅助方程再乘$\bm A$；由$\bm b-\bm A\bm M^{-1}\bm y=\bm b-\bm A\bm x$，迭代看到的是物理上真实的原残差，最小二乘目标与解集保持不变。

2. 说明变量解耦：递推只在$\bm y$坐标进行，结束时作一次$\bm x=\bm M^{-1}\bm y$；LSQR与LSMR用右预条件，并把$\widehat{\bm A}^\top\bm u$算成$\bm M^{-\top}(\bm A^\top\bm u)$；指出零初值选出的是$\lVert\bm M\bm x\rVert_2$最小的解、正规残差估计变为$\lVert\bm M^{-\top}\bm A^\top\bm r\rVert_2$。

###### paragraph：计算过程：右预条件LSQR

1. 与LSQR相比，双对角化的两次矩阵作用各接一次辅助求解，解在$\bm y$上累加；在不相容系统上取列缩放$\bm M=\operatorname{diag}(1,2)$，$\bm A\bm M^{-1}$的两列标准正交。

###### paragraph：变量

1. 沿用LSQR的全部变量（针对$\widehat{\bm A}$），另有$\bm y$坐标的近似解与预条件$\bm M$。

###### paragraph：初始化

1. 按式`eq:ls-golub-kahan-start`起步，$\bm y_0=\bm0$、$\bm w_1=\bm v_1$、$\bar\rho_1=\alpha_1$、$\bar\phi_1=\beta_1$；例中$\beta_1=\sqrt3$、$\alpha_1=\sqrt{2/3}$、$\bm v_1=(1,1)^\top/\sqrt2$。

###### paragraph：每轮更新

1. 第$k$轮依次：带辅助求解的双对角化；正交变换`eq:ls-lsqr-rotation`；在$\bm y$坐标中更新解与方向；停止时换回$\bm x$并复核；例中第一轮$\beta_2=1/\sqrt3$、$\alpha_2=0$、$\rho_1=1$、$\phi_1=\sqrt2$、$\bar\phi_2=1$、$\bm y_1=(1,1)^\top$，正规残差估计为零而退出。

2. 最终$\bm x_1=\bm M^{-1}\bm y_1=(1,1/2)^\top=\hat{\bm x}$，真实残差长度恰为估计值$1$；无预条件的LSQR需两轮，列缩放后一轮即得。

##### 15.12.3.3 预条件共轭梯度法

###### paragraph：CG对$\bm M$的要求

1. 说明左、右预条件都不能直接用于CG：即使$\bm A,\bm M$对称正定，$\bm M^{-1}\bm A$一般不对称（以$\widetilde{\bm A}$为例）；用于CG的$\bm M$须对称正定、固定，并拆成两个因子分别乘在$\bm A$两侧；对角、SSOR与构造成功的不完全Cholesky满足要求，不完全LU不满足。

###### paragraph：保持对称的变换

1. 设$\bm A,\bm M$对称正定，写$\bm M=\bm C\bm C^\top$、代换$\bm x=\bm C^{-\top}\bm y$并左乘$\bm C^{-1}$，得变换系统式`eq:ls-pcg-transformed-system`，验证$\widehat{\bm A}$对称正定且与$\bm M^{-1}\bm A$相似。

###### paragraph：递推

1. 对变换系统施行CG再换回原变量得到PCG；记$\bm z_k=\bm M^{-1}\bm r_k$与$\tau_k=\bm r_k^\top\bm z_k$，给出系数式`eq:ls-pcg-coefficients`与更新式`eq:ls-pcg-updates`；新方向由$\bm z$组合，递推残差仍是原残差，每轮多一次辅助求解。

2. 定理“PCG与变换后CG的等价”（`thm:ls-pcg-equivalence`）：迭代量满足$\bm y_k=\bm C^\top\bm x_k$等对应关系，$\bm x_k$在$\bm x_0+\mathcal K_k(\bm M^{-1}\bm A,\bm M^{-1}\bm r_0)$中使能量范数误差最小，收敛界由$\hat\kappa=\lambda_{\max}/\lambda_{\min}(\bm M^{-1}\bm A)$控制；证明分起点、系数相同、迭代量对应与最优性四步；指出$\bm C$只用于论证、$\bm M^{-1}$须固定。

###### paragraph：计算过程

1. 在贯穿例上取对称正定的$\bm M=\operatorname{diag}(4,3)$执行PCG，精确解为$(1/11,7/11)^\top$，停止按原残差判断。

###### paragraph：变量

1. 以列表列出$\bm x$、原残差$\bm r$、预条件残差$\bm z$、方向$\bm p$、工作向量$\bm q=\bm A\bm p$、配对量$\tau_k$与系数$\alpha_k,\beta_k$、轮次$k$，保存五个向量。

###### paragraph：初始化

1. 把残差初始化为$\bm r_0$，已达标或$K=0$时输出，否则解$\bm M\bm z_0=\bm r_0$，取$\bm p_0=\bm z_0$、$\tau_0=\bm r_0^\top\bm z_0$；例中$\bm z_0=(1/4,2/3)^\top$、$\tau_0=19/12$。

###### paragraph：每轮更新

1. 第$k$轮依次：乘矩阵并求步长；更新解与残差；预条件求解；形成新方向；停止；例中第一轮$\alpha_0=19/23$、$\bm x_1=(19/92,38/69)^\top$、$\bm r_1=(-26/69,13/92)^\top$，能量范数误差从约$1.168$降到约$0.236$（普通CG约$0.337$），$\tau_1=3211/76176$、$\beta_0=169/6348$，第二轮$\alpha_1=276/209$得$\bm x_2=\bm x_\star$而退出。

2. 最终结果：$\bm x_2=\bm x_\star$；本例只用于核对公式，预条件的收益看$\bm M^{-1}\bm A$的谱并与构造、应用代价一起比较；预条件不改变原问题对数据的敏感度。

### 15.13 本章小结

1. 回应章首问题：保留Krylov子空间、在$\bm x_0+\mathcal K_k$中选近似等价于选原点取一的残差多项式；方法之别在选解准则与所用的基，收敛由选解准则而非固定误差矩阵的谱半径推出。

2. 综合方阵方法：对称（可不定）矩阵用MINRES，借Lanczos三项递推与带状QR在固定存储下最小化原残差，界只依赖特征值；对称正定矩阵还可用CG，最小化能量范数误差，短递推保持正交与共轭，误差界由$\sqrt{\kappa_2(\bm A)}$控制；一般方阵用GMRES，在Arnoldi小问题上最小化原残差、单调不增但存储与正交化工作随步数增长，重启限制存储也失去跨周期最优性、可能停滞。

3. 综合非对称短递推：BiCG以原矩阵与转置矩阵维持双正交与双共轭，系数与CG同形，但残差可能波动、配对量为零时中断；BiCGSTAB以固定影子向量代替影子序列，方向系数由残差多项式首项系数比推出，再加一次局部最小残差步，只用$\bm A$，局部改进不保证整轮单调也不消除中断。

4. 综合长方问题：LSQR最小化原残差、等价于正规方程上的CG，LSMR最小化正规残差、等价于正规方程上的MINRES并需两层正交变换与两套方向；两者零初值，到达正规方程时选出$\bm A^\dagger\bm b$，避免形成Gram矩阵的信息损失，但速度仍由非零奇异值平方分布决定，病态性不因算法消失。

5. 综合三个底层子空间工具，并说明它们放在所有求解方法之前讨论：Arnoldi正交化对一般方阵把$\bm A\bm v_j$与全部已有基向量正交化，生成标准正交基并把$\bm A$压缩成上Hessenberg矩阵$\bm H_k=\bm V_k^\top\bm A\bm V_k$，原方程在子空间中化为小问题，按极小残差条件求解即GMRES，代价是整组基都要保存；Lanczos过程是它在对称矩阵上的简化，被省略的系数本来为零，每轮只扣最近两个方向，小矩阵为对称三对角，MINRES直接在其上选解，CG的残差与Lanczos向量平行、短递推相当于延续$\bm L\bm D\bm L^\top$分解；Golub--Kahan双对角化交替作用$\bm A$与$\bm A^\top$，在两个空间各得一组标准正交基、把$\bm A$压缩成下双对角矩阵，右侧基张成$\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$而不形成$\bm A^\top\bm A$，供LSQR与LSMR使用；它们给出的基与小矩阵只是求解器的中间量。

6. 综合预条件：作为加速与预处理手段以易解的$\bm M$改变谱，对角缩放、SSOR与不完全分解复用前几章公式，PCG是对称正定变换系统上的CG、每轮多解一次$\bm M\bm z=\bm r$；选用须计入构造与应用代价，并核对方法前提与求解目标（PCG与MINRES需对称正定$\bm M$，左预条件改变残差度量，右预条件在秩亏时可能改变选解）。

7. 收束停止准则：方阵查原残差，不相容最小二乘查正规残差而允许原残差非零；估计只是复核提示，上限、停滞与中断须与达到精度区分；残差多小才说明解可信取决于条件数，这一问题及同一目标下的方法比较留给第17章。

## 第16章 行列投影迭代法

正文入口：[06-row-projection-methods.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/06-row-projection-methods.tex)。

1. 从数据访问方式进入：第14章的定常迭代和第15章的Krylov方法每轮都要用整个矩阵作矩阵乘向量，而观测逐行到达或矩阵过大时只能逐行读取；由此提出每次只让一个方程成立、用局部修正逼近解的做法，以及本章要回答的问题：能求出什么解、何时收敛、不相容时怎样修改。
2. 说明各节分工：Kaczmarz算法把当前解投影到所选方程的超平面上，适用于相容方程，零初值时收敛到第11章的最小范数解；不相容时单纯行投影不会停在最小二乘解上，扩展Kaczmarz算法再用列投影估计右端的不可拟合部分。
3. 交代依赖与约定：推导只用超平面上的最短修正（第3章的正交投影），收敛分析用伪逆、行空间与零空间的正交分解及第7章谱范数与最小正奇异值的刻画；$\bm A\in\mathbb R^{m\times d}$不必是方阵，算法以$\bm A,\bm b$为输入、$\bm x$为输出，残差与辅助向量是内部状态。

### 16.1 Kaczmarz算法

1. 概述Kaczmarz算法每次只读一行、把当前解修正到满足该行的最近点，并说明本节依次由最短修正推导行投影、说明怎样依次处理各行，在贯穿例上逐步执行循环版本，再分析相容方程上的收敛、随机选行及不相容时的局限。

#### 16.1.1 主要思想

1. 从要解的问题出发：$\bm A\bm x=\bm b$相容，按行写成$m$个方程$\bm a_i^\top\bm x=b_i$，非零行的解集是以$\bm a_i$为法向的超平面，解是这些超平面的公共点；只能逐行读取时，一步只能利用一个方程，由此提出怎样修正当前点使所选方程成立。

###### paragraph：满足一行的最短修正

1. 把满足第$i$行写成$\bm a_i^\top\bm\delta=s$，其中$s=b_i-\bm a_i^\top\bm x_k$为行残差；$d\geq2$时修正有无穷多个，取欧氏范数最小者。

2. 在贯穿例第一行$\bm a_1=(4,1)^\top$上按元素求解：把修正写成$\gamma(4,1)^\top+t(-1,4)^\top$，代入条件得$17\gamma=s$，长度平方为$17\gamma^2+17t^2$，故$t=0$最短，最短修正为$(s/17)(4,1)^\top$。

3. 一般情形把修正分为$\gamma\bm a_i+\bm w$且$\bm a_i^\top\bm w=0$，由行约束与勾股关系得Kaczmarz更新式`eq:ls-kaczmarz-update`；逐项解释分子为行残差、除以$\lVert\bm a_i\rVert_2^2$换算成沿法向的系数而非另选步长、方向为法向，代回验证所选行精确成立，新点是到超平面的正交投影，称为行投影。

4. 例中从$\bm x_0=\bm0$出发，行残差为$1$，得$\bm x_1=(4/17,1/17)^\top$，并核对第一个方程成立。

###### paragraph：依次处理各行

1. 例中再对第二行作行投影：行残差为$27/17$，得$\bm x_2=(67/170,91/170)^\top$，第二个方程成立而第一个方程左端变为$359/170\neq1$，说明要反复访问各行。

2. 给出两种选行规则：循环版本按固定顺序遍历非零行，一次遍历为一轮扫掠；随机版本按$p_i=\lVert\bm a_i\rVert_2^2/\lVert\bm A\rVert_F^2$独立选行，取这一概率的原因留到本节“随机选行”一段说明；两者投影公式相同。

###### paragraph：到精确解的距离

1. 对相容方程任取精确解$\bm y$，把更新写成$\bm x_{k+1}-\bm y=\bm P_i(\bm x_k-\bm y)$，$\bm P_i$为到$\bm a_i^\perp$的正交投影，由勾股关系得距离恒等式`eq:ls-kaczmarz-distance`：距离平方每步减少$(b_i-\bm a_i^\top\bm x_k)^2/\lVert\bm a_i\rVert_2^2$；距离减少不意味着各行残差都减少，例中第一个方程就重新失配。

2. 例中由$\lVert\bm x_0-\bm x_\star\rVert_2^2=50/121$与两步减少量$1/17$、$729/2890$算出$729/2057$与$35721/349690$，三个点到$\bm x_\star=(1/11,7/11)^\top$的距离约为$0.643$、$0.595$、$0.320$。

###### paragraph：零初值与最小范数解

1. 每次修正是$\bm a_i$的倍数，零空间分量等于初值的零空间分量；零初值时迭代留在行空间，收敛到精确解时即为最小范数解（`thm:ls-minimum-norm-representative`）；不相容时没有共同的$\bm y$，距离论证不能照搬，留到本节最后讨论。

#### 16.1.2 算法实现

1. 说明每次更新选一行、算行残差、沿法向作行投影，每轮扫掠后用全部方程检查残差；输入逐行访问的$\bm A$与$\bm b$，输出$\bm x$，超参数为初值、选行规则、$\mathrm{atol},\mathrm{rtol}$与更新次数上限$K$，阈值$\tau=\mathrm{atol}+\mathrm{rtol}\lVert\bm b\rVert_2$沿用第14章；在贯穿例$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$、$\bm b=(1,2)^\top$、$\bm x_0=\bm0$上执行循环版本，取$\mathrm{atol}=0$、$\mathrm{rtol}=0.1$，$\tau=\sqrt5/10\approx0.224$。

###### paragraph：变量

1. 以列表列出：近似解$\bm x$（原处更新），预存的行平方范数$n_i$，所选行$i_k$，用后即弃的行残差$s_k$与修正系数$\gamma_k$，只在检查时计算的全残差$\bm r$，更新次数$k$。

###### paragraph：初始化

1. 预存$n_i$并处理零行：零行且右端为零时跳过，零行而右端非零说明精确方程不相容，报告并停止而不能除以零；$\bm A=\bm0$且$\bm b=\bm0$时返回零解。

2. 初始化$\bm x=\bm x_0$、$k=0$；$K=0$或初始残差已达标时直接返回初值；例中$n_1=17$、$n_2=10$，初始残差$\sqrt5\approx2.24>\tau$，进入第一次更新。

###### paragraph：每次更新

1. 第$k$次更新依次：选行（循环取下一个非零行并在末行后回到第一行；随机按$p_i$抽样、零行不会被抽到、记录选行序列；例中顺序$1,2,1,2,\ldots$）；只读第$i_k$行算行残差$s_k$（例中$s_0=1$）；按式`eq:ls-kaczmarz-update`算$\gamma_k=s_k/n_{i_k}$与$\bm x_{k+1}$并令$k\leftarrow k+1$（例中$\gamma_0=1/17$、$\bm x_1=(4/17,1/17)^\top$；第二次更新$s_1=27/17$、$\gamma_1=27/170$、$\bm x_2=(67/170,91/170)^\top$，完成第一轮扫掠）；集中给出后两轮的行残差与迭代点，$\bm x_3\approx(0.1325,0.4699)^\top$、$\bm x_4\approx(0.1783,0.6072)^\top$、$\bm x_5\approx(0.1029,0.5884)^\top$、$\bm x_6\approx(0.1161,0.6280)^\top$。

2. 停止：$k=K$时立即结束（即使一轮未扫完）；每轮扫掠末（随机版本按预定间隔）用全部方程计算残差与$\tau$比较，行残差为零不能作为成功依据；例中三轮末全残差为$(-189/170,0)^\top$、$(-9261/28900,0)^\top$、约$(-0.0924,0)^\top$，长度约$1.112$、$0.320$、$0.092$，每次刚投影的一行残差为零而前两轮仍大于$\tau$，第三轮末以“达到容差”结束。

3. 最终结果：单独一行写出$\bm x_6\approx(0.1161,0.6280)^\top$，与$\bm x_\star\approx(0.0909,0.6364)^\top$相距约$0.027$；七个迭代点的距离依次约为$0.643$、$0.595$、$0.320$、$0.172$、$0.092$、$0.049$、$0.027$，与距离恒等式一致，并指向路径图。

#### 16.1.3 算法分析

###### paragraph：收敛性

1. 说明循环版本的收敛由投影几何得到，并回顾$\bm I-\bm A^\dagger\bm A$是到$\ker\bm A$的正交投影。

2. 定理“相容方程上循环Kaczmarz的收敛”（`thm:ls-kaczmarz-convergence`）：方程相容且$\bm A\neq\bm0$时，令$\bm x_\star=\bm A^\dagger\bm b+(\bm I-\bm A^\dagger\bm A)\bm x_0$，固定循环顺序下距离不增、每轮按与初值无关的因子$q<1$几何收缩，$\bm x_k\to\bm x_\star$，零初值时极限为$\bm A^\dagger\bm b$。

3. 证明第一段：由相容性验证$\bm A\bm x_\star=\bm b$，由距离恒等式得距离不增；误差满足$\bm\varepsilon_{k+1}=\bm P_{i_k}\bm\varepsilon_k$，初始误差在行空间中且各$\bm P_i$保持行空间，故误差始终在行空间中。

4. 证明第二段：一轮误差映射$\bm K$若在行空间中某向量上不缩短长度，则该向量与每个非零行正交，只能为零；把$\bm K$限制到行空间得$\bm C=\bm Q^\top\bm K\bm Q$，由谱范数在某单位向量上达到，推出$q=\lVert\bm C\rVert_2<1$，于是每轮误差至多乘以$q$，结合轮内不增得收敛。

5. 解释零初值使迭代留在行空间并选出最小范数解，任意初值的极限也满足方程但带有初值的零空间分量。

###### paragraph：收敛速度与代价

1. 说明速度受行间夹角与访问顺序影响；二维时第一步后每次投影把误差乘以两法向夹角的余弦$\cos\theta=|\bm a_1^\top\bm a_2|/(\lVert\bm a_1\rVert_2\lVert\bm a_2\rVert_2)$（单独一行写出）。

2. 用算法实现的执行核对：贯穿例余弦$7/\sqrt{170}\approx0.537$，从第二个点起距离每步按此比例缩小（如$0.320/0.595$）；每轮两次投影，轮末全残差比值$0.320/1.112\approx0.288$正是$\cos^2\theta=49/170$；由此引出两行接近平行的情形。

3. 示例“循环Kaczmarz的两轮扫掠”（`ex:ls-kaczmarz-two-sweeps`）：$\bm A=\left[\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right]$、$\bm b=(1,2)^\top$、零初值，精确解$(0,1)^\top$，行平方范数$2$与$5$，余弦$3/\sqrt{10}\approx0.949$；先列出修正系数$\gamma_0=1/2$、$\gamma_1=1/10$、$\gamma_2=-3/20$、$\gamma_3=9/100$，再逐行列出四次更新的行残差、迭代点$(1/2,1/2)^\top$、$(3/5,7/10)^\top$、$(9/20,11/20)^\top$、$(27/50,73/100)^\top$与全残差$(0,1/2)^\top$、$(-3/10,0)^\top$、$(0,9/20)^\top$、$(-27/100,0)^\top$；说明每步一行残差为零而另一行不为零，距离依次约为$1$、$0.707$、$0.671$、$0.636$、$0.604$，第一步后每步只缩短约百分之五，比值正是$0.949$，是否停止要按轮末全残差判断。

4. 由此说明越接近垂直收拢越快、越接近平行越在狭窄夹角中往复，并指向路径图；给出代价：一次投影$O(\operatorname{nnz}(\bm a_i))$，全局残差检查另需一次完整矩阵乘向量。

5. 图“循环Kaczmarz的交替投影路径”（`fig:ls-kaczmarz-projection-path`）：在贯穿例的两条直线之间从原点依次垂直投影，折线连接前六个精确迭代点并收拢到交点，坐标轴等比例。

###### paragraph：随机选行

1. 说明随机版本只改选行方式，结论是期望意义下的；在误差位于行空间时，对所选行求平均，由距离恒等式与$p_i$的选取得平均减少量为$\lVert\bm A\bm\varepsilon_k\rVert_2^2/\lVert\bm A\rVert_F^2$，再由最小正奇异值的下界得一步平均缩小因子$1-\sigma_r^2/\lVert\bm A\rVert_F^2$，并解释按行平方范数抽样正是为了抵消分母$\lVert\bm a_i\rVert_2^2$而得到这一形式。

2. 逐步叠加得$\mathbb E\lVert\bm\varepsilon_k\rVert_2^2\leq(1-\sigma_r^2/\lVert\bm A\rVert_F^2)^k\lVert\bm\varepsilon_0\rVert_2^2$（单独一行写出），满列秩时由Strohmer与Vershynin给出；叠加需对此前选行取条件期望，可参考卷七“随机变量与概率分布”章；强调这是期望结论，单条轨迹只保证距离不增。

###### paragraph：不相容情形

1. 用$\bm A=(1,1)^\top$、$\bm b=(1,3)^\top$说明：两行长度为一，投影化为$x\gets b_i$，循环投影在$1$与$3$间往返而最小二乘解为$2$；随机选行时$x$也只取$1$或$3$，因此改选行方式不能得到最小二乘解，转入下一节的扩展算法。

补充图解：循环行投影在不相容方程$x=1$、$x=3$之间往返。两条弧形箭头表示依次满足两行后的跳转；黄色点$\hat x=2$是最小二乘解，并非任何一次原始行投影的落点。

### 16.2 扩展Kaczmarz算法

1. 承接上例，指出不相容的原因是右端含有任何$\bm x$都拟合不了的部分；扩展Kaczmarz算法先用列投影取出这一部分，再对校正后的相容方程作行投影，把方法推广到一般最小二乘；说明本节依次推导两种投影及其配合、在不相容例上逐步执行、分析收敛与代价。

#### 16.2.1 主要思想

1. 从要解的问题出发：$\min_{\bm x}\lVert\bm b-\bm A\bm x\rVert_2$，方程可以不相容，目标为$\bm A^\dagger\bm b$；行投影只适用于相容方程，故先把问题改写成相容方程。

###### paragraph：右端的分解

1. 把$\bm b$正交分解为$\bm b_\parallel\in\operatorname{range}(\bm A)$与$\bm b_\perp\in\ker(\bm A^\top)$，由第11章最小二乘解即$\bm A\bm x=\bm b_\parallel$的解、最小范数者为$\bm A^\dagger\bm b$，$\bm b_\perp$不可拟合。

2. 不相容例中按元素算出$\bm b_\parallel=(2,2)^\top$、$\bm b_\perp=(-1,1)^\top$，校正后的方程两行都要求$x=2$，即最小二乘解。

3. 因$\bm b_\perp$未知，引入$m$维辅助向量$\bm z$逼近它并求解$\bm A\bm x=\bm b-\bm z$，于是要做两件事：用列信息推动$\bm z$、用行投影求解校正方程。

###### paragraph：列投影

1. $\bm b_\perp$满足$\bm A^\top\bm z=\bm0$，即$d$个齐次方程$\bm c_j^\top\bm z=0$组成的相容方程组；对其中一个方程应用最短修正得到列投影。

2. 不相容例中唯一一列$\bm c_1=(1,1)^\top$，按元素写出列投影$\bm z\gets\tfrac12(z_1-z_2,\,z_2-z_1)^\top$，即减去两分量的平均值；从$\bm z=\bm b$出发一步得到$\bm b_\perp$。

3. 给出一般公式`eq:ls-extended-kaczmarz-column`并逐项解释：$\bm c_j^\top\bm z_k$衡量偏离正交的程度，除以$\lVert\bm c_j\rVert_2^2$换算成系数，投影后$\bm c_j^\top\bm z_{k+1}=0$，即对$\bm A^\top\bm z=\bm0$作Kaczmarz投影。

4. 从$\bm z_0=\bm b$出发只减去列的倍数，$\ker(\bm A^\top)$中的分量始终为$\bm b_\perp$，只有$\bm z_k-\bm b_\perp$变化，且$\bm b-\bm z_k$始终在列空间中，校正方程始终相容。

###### paragraph：校正后的行投影

1. 校正量为$\bm z_k$时第$i$条目标方程为$\bm a_i^\top\bm x=b_i-(\bm z_k)_i$，把行投影中的$b_i$换成$b_i-(\bm z_k)_i$得式`eq:ls-extended-kaczmarz-row`，分子是校正方程的行残差。

2. 不相容例中行投影化为$x\gets b_i-(\bm z_k)_i$：不校正时在$1$与$3$间往返，以$\bm b_\perp$校正后两行都给出$2$，即最小二乘解。

###### paragraph：两种投影的配合

1. 明确采用同步读取轮初状态的版本：$\bm z_{k+1}$与$\bm x_{k+1}$都由$(\bm z_k,\bm x_k)$计算；先更新$\bm z$再用新值的版本轨迹不同，实现须与收敛分析一致；行列选取沿用随机规则，采用Zouzias与Freris的随机版本。

2. 写出误差来源：列投影缩小$\bm z_k-\bm b_\perp$，行投影在右端受此误差扰动时逼近$\bm A\bm x=\bm b_\parallel$；零初值与沿行方向修正保证最终选出最小范数代表。

#### 16.2.2 算法实现

1. 说明每轮抽取一行一列，作一次列投影和一次行投影，两者都读轮初状态，按间隔检查两项判据；输入$\bm A,\bm b$，输出$\bm x$，超参数$\mathrm{atol},\mathrm{rtol}$与轮数上限$K$；在不相容例$\bm A=(1,1)^\top$、$\bm b=(1,3)^\top$上执行，取$\mathrm{atol}=0$、$\mathrm{rtol}=0.1$，每轮检查。

###### paragraph：变量

1. 以列表列出：近似解$\bm x$，辅助向量$\bm z$（逼近$\bm b_\perp$，不作为输出），预存的行、列平方范数（兼作抽样权重），抽到的行列$i_k,j_k$，用后即弃的系数$\eta_k,\gamma_k$，轮次$k$。

###### paragraph：初始化

1. $\bm A=\bm0$时返回零解；否则预存行列平方范数，得抽样概率$p_i=\lVert\bm a_i\rVert_2^2/\lVert\bm A\rVert_F^2$、$q_j=\lVert\bm c_j\rVert_2^2/\lVert\bm A\rVert_F^2$，零行零列不会被抽到；初始化$\bm x_0=\bm0$、$\bm z_0=\bm b$、$k=0$；阈值取$\tau_r=\mathrm{atol}+\mathrm{rtol}\lVert\bm b\rVert_2$、$\tau_n=\mathrm{atol}+\mathrm{rtol}\lVert\bm A\rVert_F\lVert\bm b\rVert_2$，后者尺度来自$\lVert\bm A^\top\bm b\rVert_2\leq\lVert\bm A\rVert_F\lVert\bm b\rVert_2$。

2. 例中$p_1=p_2=1/2$、$q_1=1$、$\tau_r\approx0.316$、$\tau_n\approx0.447$；初始时校正方程残差为零但$\bm A^\top\bm z_0=4>\tau_n$，进入第一轮。

###### paragraph：每轮更新

1. 第$k$轮依次：抽样（独立抽取行列并记录序列；例中$j_k=1$，行以各半概率取$1$或$2$）；列投影（保存轮初状态，按式`eq:ls-extended-kaczmarz-column`算$\eta_k$与$\bm z_{k+1}$；例中第一轮$\eta_0=2$、$\bm z_1=(-1,1)^\top=\bm b_\perp$）；行投影（仍读旧的$(\bm z_k)_{i_k}$，按式`eq:ls-extended-kaczmarz-row`算$\gamma_k$与$\bm x_{k+1}$；例中第一轮分子$b_i-b_i-0=0$，$\gamma_0=0$、$x_1=0$，并指出若改用新校正量会提前得到$x=2$而同步版本不这样做）；替换状态（同时写回$(\bm x_{k+1},\bm z_{k+1})$，$k\leftarrow k+1$；例中第二轮$\eta_1=0$、$\bm z_2=\bm z_1$，抽到任一行都得$\gamma_1=2$、$x_2=2$）。

2. 停止：检查轮次上两项判据$\lVert\bm b-\bm z_k-\bm A\bm x_k\rVert_2\leq\tau_r$与$\lVert\bm A^\top\bm z_k\rVert_2\leq\tau_n$都满足时以“达到容差”结束，做满$K$轮时以“次数耗尽”结束；说明两项分别检查校正方程的拟合与辅助向量的正交性，宣布达标前复核正规残差，不要求原残差趋于零；例中第一轮后$\bm A^\top\bm z_1=0$已满足而校正残差$(2,2)^\top$长度约$2.83>\tau_r$，继续；第二轮后两项都为零，复核正规残差为零后结束。

3. 最终结果：单独一行写出$x_2=2$；原残差$(-1,1)^\top$的平方和为$2$，等于$\min_x[(x-1)^2+(x-3)^2]$，原方程无精确解而$x_2$已是最小二乘解；并指出第一轮后$\bm z$已正确而$x$未动，说明两项判据缺一不可。

#### 16.2.3 算法分析

###### paragraph：极限的含义

1. 说明列投影保留$\bm b_\perp$并缩小$\bm z_k-\bm b_\perp$，$\bm x_k$始终在行空间中；$\bm z_k\to\bm b_\perp$时行投影求解相容方程$\bm A\bm x=\bm b_\parallel$，其行空间中的唯一解为$\bm A^\dagger\bm b$，因此构造指向最小范数最小二乘解。

###### paragraph：列校正的收敛

1. 把列投影视为对相容方程$\bm A^\top\bm z=\bm0$、初值$\bm b$的Kaczmarz投影，对$\bm A^\top$应用收敛定理，得循环选列时$\bm z_k$几何收敛到$\bm b$在$\ker(\bm A^\top)$上的投影$\bm b_\perp$；随机选列时一步平均估计同样适用于$\bm z_k-\bm b_\perp\in\operatorname{range}(\bm A)$，因子为$1-\sigma_r^2/\lVert\bm A\rVert_F^2$。

###### paragraph：行迭代的误差递推

1. 令$\bm x_\star=\bm A^\dagger\bm b$，由$b_i=\bm a_i^\top\bm x_\star+(\bm b_\perp)_i$得误差递推$\bm\varepsilon_{k+1}=\bm P_{i_k}\bm\varepsilon_k+(\bm b_\perp-\bm z_k)_{i_k}\bm a_{i_k}/\lVert\bm a_{i_k}\rVert_2^2$：第一项为标准Kaczmarz误差映射，第二项为校正误差带来的扰动，长度不超过$\lVert\bm z_k-\bm b_\perp\rVert_2/\lVert\bm a_{i_k}\rVert_2$，误差始终在行空间中。

2. 循环版本中把一轮行扫掠合起来得$\lVert\bm\varepsilon_{\text{轮末}}\rVert_2\leq q\lVert\bm\varepsilon_{\text{轮初}}\rVert_2+\varphi$（单独一行写出）且$\varphi\to0$，由有界性与上极限$L\leq qL$推出$\bm x_k\to\bm A^\dagger\bm b$；随机版本在规定独立抽样下期望平方误差以由$1-\sigma_r^2/\lVert\bm A\rVert_F^2$决定的几何速率趋于零（Zouzias与Freris），证明需条件期望；不宣称原残差逐步下降，并以算法实现的例子中第一轮$x$不动为证。

###### paragraph：代价

1. 每轮访问一行一列并保存长度为$m$的$\bm z_k$，代价按非零元计；停止检查需$\bm A\bm x_k$与$\bm A^\top\bm z_k$两次完整乘法，故按间隔进行；两种收缩因子都由$\sigma_r^2/\lVert\bm A\rVert_F^2$决定，它很小时收敛很慢。

### 16.3 本章小结

1. 回应章首问题：Kaczmarz每次满足一个方程，由最短修正得到沿行法向、系数为行残差除以行平方范数的正交投影；相容时距离不增，循环版本每轮按小于一的因子收缩，收敛到$\bm A^\dagger\bm b$加初值的零空间分量，零初值即最小范数解；随机版本按行平方范数抽样，期望平方误差以$1-\sigma_r^2/\lVert\bm A\rVert_F^2$为因子几何减小。

2. 总结使用条件：行越接近平行收敛越慢；零行对应非零右端说明不相容，须单独处理；单行残差为零不表示完成；不相容时标准算法在各行解之间往返，不会停在最小二乘解上。

3. 总结扩展算法：列投影从$\bm b$出发逼近$\bm b_\perp$，行投影求解校正后的相容方程；同步版本读取轮初状态，零初值保证极限是最小范数最小二乘解。

4. 总结检验与代价：标准算法看全部方程原残差，扩展算法看$\lVert\bm A^\top\bm z\rVert_2$与校正方程残差并复核正规残差，原残差非零正常；最小范数性质依赖零初值与行空间保持；每步只读一行或一列，代价低而收敛速度受$\sigma_r^2/\lVert\bm A\rVert_F^2$限制，误差与方法比较在第17章。

## 第17章 求解误差、正则化与方法选择

正文入口：[06-solution-error-and-regularization.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/07-solution-error-and-regularization.tex)，依次输入[01-solution-error.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/07-solution-error-and-regularization/01-solution-error.tex)、[02-regularization.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/07-solution-error-and-regularization/02-regularization.tex)、[03-method-selection.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/07-solution-error-and-regularization/03-method-selection.tex)与[04-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/07-solution-error-and-regularization/04-summary.tex)。

1. 从具体情形进入：第12—17章的各条路线都交出一个向量，但两列近平行的矩阵配上带误差的观测时，精确解可能离真值很远，算法可能没有算准，迭代提前停止又多出截断误差，小残差也不保证系数可靠。
2. 提出本章的三个问题：算出的解能相信多少，问题本身太敏感时怎么办，多种方法可用时怎样选择。
3. 说明第一节的分工与依赖：用有限扰动界与条件数度量数据误差的放大，用残差、前向误差与后向误差判断近似解，比较最小二乘三类输出的敏感性，并讨论伪逆在秩变化处的不连续与数值秩；依赖第9章的条件数与奇异值扰动界和第11章的伪逆与选解。
4. 说明第二节处理算法无法消除的敏感性：岭回归与Tikhonov正则化加入惩罚，谱截断舍弃小奇异值方向，二者都改变求解目标；截断矩阵的最佳低秩性质留到第18章。
5. 说明第三节在前两节的误差标准下比较第12—17章的方法，依次看目标、矩阵条件、开销与收敛速度、数值稳定性和典型问题；并指出本章针对有限扰动，局部线性化观点在第23章讨论。

### 17.1 解的误差与敏感性

1. 提出求解后还要判断结果可信程度，列出本节四方面：数据扰动的传播、残差判断近似解、最小二乘不同输出的敏感性、秩变化时伪逆的变化。

2. 强调每种误差先说明参照与允许修改的数据：比较两个精确解时改$\bm A$或$\bm b$、以原精确解为参照，残差判断时以未知真解为参照，后向误差问数据至少改多少。

3. 交代结论由精确方程、范数估计与奇异值性质建立，扰动可有有限大小，条件数与奇异值扰动界来自第9章；局部观点留到后文：第21章建立逆矩阵等运算的微分公式，第23章从同样的精确关系提取解映射的一阶响应。

#### 17.1.1 系数矩阵与右端项的扰动

1. 说明数据来自测量或前一步计算而带误差，本小节比较两个精确解，放大来自问题本身而与算法、舍入无关。

2. 设$\bm A$可逆、$\bm b\neq\bm0$，向量范数与诱导矩阵范数取同一种，display定义$\kappa(\bm A)=\lVert\bm A\rVert\lVert\bm A^{-1}\rVert$，二范数下记$\kappa_2$。

###### paragraph：右端扰动

1. 问题：固定$\bm A$只改右端，关心解的相对变化与右端相对变化之比。

2. 写出新旧两个方程并相减，得$\bm A\Delta\bm x=\Delta\bm b$即$\Delta\bm x=\bm A^{-1}\Delta\bm b$，指出对任意大小的扰动精确成立。

3. 取范数得绝对变化界，再由$\bm b=\bm A\bm x_\star$得$1/\lVert\bm x_\star\rVert\leq\lVert\bm A\rVert/\lVert\bm b\rVert$，两式相乘得相对误差不超过$\kappa(\bm A)$乘右端相对扰动，即第9章的条件数界。

4. 把$\Delta\bm b$按左奇异向量展开为$\sum_i\beta_i\bm u_i$，得$\Delta\bm x=\sum_i(\beta_i/\sigma_i)\bm v_i$，说明沿$\bm u_i$的分量放大$1/\sigma_i$倍，最小奇异值方向放大最多。

5. 例“良态矩阵与近平行列矩阵”（`ex:ls-rhs-perturbation-near-parallel`）：$\bm A_1=\operatorname{diag}(2,1)$上$\Delta\bm b=(0,0.01)^\top$给出$\Delta\bm x=(0,0.01)^\top$，相对变化$0.00447$与$0.00707$，放大约$1.58$倍，不超过$\kappa_2=2$。

6. 同例：按元素写出$\bm A_2=\left[\begin{smallmatrix}1&1\\0&\varepsilon\end{smallmatrix}\right]$与$\bm A_2^{-1}$，$\varepsilon=10^{-2}$，$\Delta\bm b=(0,\eta)^\top$给出$\Delta\bm x=(-\eta/\varepsilon,\eta/\varepsilon)^\top$；$\eta=0.01$时解由$(2,0)^\top$变为$(1,1)^\top$，相对变化$0.005$与$0.707$，放大约$141$倍。

7. 同例：由$\bm A_2^\top\bm A_2$的迹与行列式解出$\sigma_{\max}\approx1.41423$、$\sigma_{\min}\approx0.0070710$，$\kappa_2\approx200$，说明$141$未达到$200$是因为$\lVert\bm b\rVert_2/\lVert\bm x_\star\rVert_2=1$而界中用$\lVert\bm A_2\rVert_2\approx1.414$。

8. 同例：数值给出$\bm v_{\min}\approx(0.7071,-0.7071)^\top$、$\bm u_{\min}\approx(0.0050,-1.0000)^\top$，$\Delta\bm b$几乎全在$\bm u_{\min}$上，$\Delta\bm x\approx-1.4142\,\bm v_{\min}\approx(-1,1)^\top$，两个系数此增彼减，引向图示。

9. 图“近平行列的系数分裂”（`fig:matrix-analysis-coefficient-sensitivity`）：固定右端扰动$(0,10^{-4})^\top$，图中对照系数相对变化与右端相对扰动；$\varepsilon$越小两个系数沿相反方向偏离越远，变化量随$1/\varepsilon$增长。

###### paragraph：系数矩阵的扰动

1. 问题：$\bm B=\bm A+\bm E$可能不可逆（如$\bm E=-\bm A$），须先确定可逆条件再估计逆的变化。

2. 直观：扰动是否算小要看$\bm A$离奇异多远，所以用$\bm A^{-1}\bm E$或$\lVert\bm A^{-1}\rVert\lVert\bm E\rVert$衡量。

3. 定理“逆矩阵的有限扰动”（`thm:ls-inverse-finite-perturbation`）：$\lVert\bm A^{-1}\bm E\rVert<1$时$\bm B$可逆，display给出$\lVert\bm B^{-1}\rVert$的界与恒等式$\bm B^{-1}-\bm A^{-1}=-\bm B^{-1}\bm E\bm A^{-1}$（`eq:ch06-inverse-finite-perturbation`）；$q=\lVert\bm A^{-1}\rVert\lVert\bm E\rVert<1$时相对变化不超过$q/(1-q)$。

4. 证明分四步display：由$\bm x=-\bm A^{-1}\bm E\bm x$得零空间只含零向量；由$\bm x=\bm A^{-1}\bm y-\bm A^{-1}\bm E\bm x$移项得$\lVert\bm B^{-1}\rVert$的界；由$\bm B^{-1}(\bm A-\bm B)\bm A^{-1}$得恒等式；对恒等式取范数并除以$\lVert\bm A^{-1}\rVert$得第2条，并写出$q=\kappa\lVert\bm E\rVert/\lVert\bm A\rVert$。

5. 解释分子为条件数乘相对扰动、分母为到可逆性保证边界的余量。

6. 例“一次系数扰动”（`ex:ls-inverse-perturbation-numeric`）：贯穿例$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$加$\bm E=\operatorname{diag}(0,1/2)$，按元素写出$\bm A^{-1}$、$\bm B^{-1}$与差$\frac1{286}\left[\begin{smallmatrix}-1&4\\4&-16\end{smallmatrix}\right]$并用恒等式核对，谱范数$17/286\approx0.0594$。

7. 同例：$\lVert\bm A\rVert_2\approx4.618$、$\lVert\bm A^{-1}\rVert_2\approx0.4198$、$\kappa_2\approx1.939$，$q\approx0.210$，界$0.266$对实际$0.142$；第1条的界$0.517$对$\lVert\bm B^{-1}\rVert_2\approx0.368$。

8. 用$\operatorname{diag}(1,\varepsilon)$与$\operatorname{diag}(0,-\delta)$说明界取等号，$\varepsilon=0.1$、$\delta=0.05$时$q=0.5$、相对变化恰为$1$，$\delta\to\varepsilon$时无界。

9. 指出$q\geq1$只是失去保证，例如$\bm E=\bm A$时$\bm B=2\bm A$仍可逆。

###### paragraph：矩阵与右端同时扰动

1. 写出扰动方程并展开、减去原方程，得精确关系$(\bm A+\bm E)\Delta\bm x=\Delta\bm b-\bm E\bm x_\star$（`eq:ls-joint-perturbation-exact`）。

2. 说明解的变化由右端变化与$\bm E\bm x_\star$两部分驱动，可逆时$\Delta\bm x=(\bm A+\bm E)^{-1}(\Delta\bm b-\bm E\bm x_\star)$。

3. 定理“矩阵与右端同时扰动时的解误差”（`thm:ls-linear-system-perturbation`）：$\kappa\rho_A<1$时相对误差不超过$\kappa(\rho_A+\rho_b)/(1-\kappa\rho_A)$（`eq:matrix-analysis-linear-system-perturbation`）。

4. 证明display逐步写出：改写为$\Delta\bm x=\bm A^{-1}(\Delta\bm b-\bm E\bm x_\star-\bm E\Delta\bm x)$，取范数，移项，右端两项分别化为$\kappa\rho_b\lVert\bm x_\star\rVert$与$\kappa\rho_A\lVert\bm x_\star\rVert$，再除以正的系数。

5. 解读为两类相对扰动相加、被条件数放大、再除以余量，$\bm E=\bm0$时退回右端界。

6. 例“矩阵与右端同时扰动”（`ex:ls-joint-perturbation-numeric`）：沿用上例，$\bm b=(1,2)^\top$，$\bm E\bm x_\star=(0,7/22)^\top$；$\Delta\bm b=(0,-1/4)^\top$时驱动项$(0,-25/44)^\top$、$\Delta\bm x=(25/572,-25/143)^\top$，相对变化约$0.280$。

7. 同例：$\rho_A\approx0.108$、$\rho_b\approx0.112$、$\kappa_2\rho_A\approx0.210$，界约$0.540$；改取$\Delta\bm b=(0,1/4)^\top$时两项部分抵消，$\Delta\bm x=(3/572,-3/143)^\top$、相对变化约$0.034$，说明界只看大小、给出最坏情形。

8. 指出第23章逆矩阵扰动一节从同一精确式提取一阶响应，这里的结论对完整的有限变化有效。

#### 17.1.2 残差、前向误差与后向误差

###### paragraph：残差与前向误差

1. 问题：实际只有近似解，真解未知，能算的是残差$\bm r=\bm b-\bm A\tilde{\bm x}$；问残差小能否说明误差小。

2. 由$\bm r=\bm A(\bm x_\star-\tilde{\bm x})$说明$\tilde{\bm x}$是右端改为$\bm b-\bm r$的精确解，残差扮演右端误差，得前向相对误差不超过$\kappa$乘相对残差。

3. 按元素写出$\operatorname{diag}(1,\varepsilon)$、$\bm b=(1,\varepsilon)^\top$、近似解$(1,0)^\top$：残差$(0,\varepsilon)^\top$趋零而相对误差始终为$1/\sqrt2$；界的右端$1/\sqrt{1+\varepsilon^2}$与之不矛盾，小残差在病态时不保证精度。

4. 定义前向误差与后向误差，指出前者需要真解、后者只用数据与近似解，引向度量方式。

###### paragraph：后向误差的度量

1. 说明后向误差的想法：近似解若是误差水平内邻近问题的精确解就不能要求更多；其大小取决于允许的修改方式。

2. display写出范数型模型的两个约束与方程$(\bm A+\Delta\bm A)\tilde{\bm x}=\bm b+\Delta\bm b$，定义最小相对扰动$\eta(\tilde{\bm x})$。

3. 定理“范数型后向误差”（`thm:ls-backward-error-formulas`）：二范数下$\eta_2=\lVert\bm r\rVert_2/(\lVert\bm A\rVert_2\lVert\tilde{\bm x}\rVert_2+\lVert\bm b\rVert_2)$且可取到。

4. 证明display逐步写出：由$\bm r=\Delta\bm A\tilde{\bm x}-\Delta\bm b$取范数得下界；$\tilde{\bm x}=\bm0$时取$\Delta\bm b=-\bm b$；否则用秩一扰动$\bm r\tilde{\bm x}^\top$构造，验证$\Delta\bm A\tilde{\bm x}-\Delta\bm b=\bm r$与两项相对大小都等于$\lVert\bm r\rVert_2/s$。

5. 说明分母为零时近似解已精确。

6. 只允许改右端时后向误差就是相对残差，且$\eta_2\leq\lVert\bm r\rVert_2/\lVert\bm b\rVert_2$，所以第14章停止准则$\lVert\bm r_k\rVert_2\leq\mathrm{rtol}\lVert\bm b\rVert_2$保证后向误差不超过$\mathrm{rtol}$。

7. 介绍逐元素模型的约束与公式$\omega(\tilde{\bm x})=\max_i|r_i|/(|\bm A||\tilde{\bm x}|+|\bm b|)_i$，它不允许把零元改成非零。

8. 用对角例逐项计算：范数型$\eta_2=\varepsilon/(1+\sqrt{1+\varepsilon^2})\approx\varepsilon/2$，逐元素型分母向量$(2,\varepsilon)^\top$、$\omega=1$，说明两种模型回答不同问题。

9. 例“计算一次后向误差”（`ex:ls-backward-error-computation`）：贯穿例上取$\tilde{\bm x}=(0.09,0.64)^\top$，按元素算出残差$(0,-0.01)^\top$。

10. 同例：由$\lVert\bm A\rVert_2\approx4.618$、$\lVert\tilde{\bm x}\rVert_2\approx0.6463$、$\lVert\bm b\rVert_2\approx2.236$得$s\approx5.221$、$\eta_2\approx1.92\times10^{-3}$。

11. 同例：按构造写出$\Delta\bm A\approx\left[\begin{smallmatrix}0&0\\-0.0012&-0.0088\end{smallmatrix}\right]$、$\Delta\bm b\approx(0,0.0043)^\top$，并逐个方程验证。

###### paragraph：后向稳定与常用分解

1. display写出舍入模型$\operatorname{fl}(x\circ y)=(x\circ y)(1+\delta)$，定义单位舍入$u=2^{-53}$与后向稳定。

2. 指出后向稳定不说明答案准确，由后向误差到前向误差还要经过条件数。

3. 定理“由后向误差估计前向误差”（`thm:ls-forward-backward-error`）：后向扰动不超过$\eta$且$\kappa\eta<1$时前向相对误差不超过$2\kappa\eta/(1-\kappa\eta)$；证明把近似解看作扰动问题的精确解，由前一定理的界关于$\rho_A,\rho_b$单调代入。

4. 回到后向误差例：$\kappa_2\eta_2\approx0.0037$，界约$0.0075$；实际误差$(-0.0009,0.0036)^\top$，相对前向误差约$0.0058$。

5. 总结后向误差评价算法、条件数评价问题，$\kappa u$接近一时后向稳定算法也可能无有效数字，第12章各直接法以此为标准。

6. 部分主元LU的后向误差依赖增长因子$\rho$，最坏为$2^{d-1}$；按元素展示$3\times3$矩阵消元后末列依次为$1,2,4$、$\rho=4$，说明只在增长不大时后向稳定，可在消元中记录$\rho$。

7. 由$a_{j,j}=\sum_kl_{j,k}^2$得Cholesky因子元素不超过$\sqrt{a_{j,j}}$，贯穿例中$l_{2,1}=1/2$、$l_{2,2}\approx1.658\leq\sqrt3$，故后向稳定。

8. Householder与Givens保持长度，求最小二乘解后向稳定；修正Gram--Schmidt的$\bm Q$可能失去正交，应核验$\bm Q^\top\bm Q-\bm I$或残差。

#### 17.1.3 最小二乘的敏感性与数值误差

###### paragraph：三类输出的敏感性

1. display写出系数、拟合值与残差三类输出，问右端改变时各变多少；直观上后两者是投影不放大，系数含奇异值倒数。

2. 写出三者在右端变化下的精确变化$\bm A^\dagger\Delta\bm b$、$\bm P\Delta\bm b$、$(\bm I-\bm P)\Delta\bm b$。

3. 由正交分解说明拟合值与残差的变化不超过$\lVert\Delta\bm b\rVert_2$；由$\bm A^\dagger=\sum_i\sigma_i^{-1}\bm v_i\bm u_i^\top$说明系数按$1/\sigma_r$放大且沿$\bm u_r$取等号，拟合好与系数可靠是两回事。

4. 例“三类输出的不同变化”（`ex:ls-three-outputs-sensitivity`）：在$\bm A_2$下添零行得$3\times2$矩阵，$\bm b=(2,0,1)^\top$，按元素写出$\bm A^\dagger$、$\bm P=\operatorname{diag}(1,1,0)$与三类输出$(2,0)^\top$、$(2,0,0)^\top$、$(0,0,1)^\top$。

5. 同例：$\Delta\bm b=(0,0.01,0)^\top$在列空间内，系数变化$(-1,1)^\top$、拟合值只变$0.01$、残差不变，几乎取到$\lVert\Delta\bm b\rVert_2/\sigma_r\approx1.414$；$\Delta\bm b=(0,0,0.01)^\top$与列空间正交，只有残差改变。

6. 补充两点限制：接近零的输出其相对误差解释要重查；$\bm A$也变化时误差界中出现$\kappa_2^2\lVert\hat{\bm r}\rVert_2$项，$\kappa_2(\bm A)$不是完整条件数。

###### paragraph：正规方程的条件数平方

1. 回顾第13章对满列秩长方矩阵定义的$\kappa_2(\bm A)$，说明本段讨论正规方程面对条件数平方后的矩阵。

2. 由$\bm A^\dagger$的奇异值为$1/\sigma_i$得$\kappa_2(\bm A)=\lVert\bm A\rVert_2\lVert\bm A^\dagger\rVert_2$，由第13章定理得$\kappa_2(\bm A^\top\bm A)=\kappa_2(\bm A)^2$（`eq:matrix-analysis-normal-equation-condition-square`）。

3. 指出正规方程法即使后向稳定，前向误差定理中的条件数也是$\kappa_2^2$，与残差大小无关。

4. 以$\varepsilon=10^{-8}$的$\bm A_2$为例：$\kappa_2\approx2\times10^8$远小于$1/u\approx9\times10^{15}$，但Gram矩阵中$1+\varepsilon^2$因$\varepsilon^2<u$舍入为$1$，成为奇异的全一矩阵，与$\kappa_2^2\approx4\times10^{16}>1/u$相符，信息在形成时丢失。

5. 比较QR与SVD的放大因子为$\kappa_2$加以残差为权的$\kappa_2^2$项，残差小时与$\kappa_2$同阶；正规方程只在$\kappa_2^2u\ll1$时可取。

#### 17.1.4 伪逆扰动与数值秩

###### paragraph：伪逆的扰动与不连续

1. 问题：一般矩阵改变时伪逆改变多少；与逆矩阵相比多了行空间、列空间转动与秩改变两种可能。

2. 写出$\bm B^\dagger-\bm A^\dagger$的三项恒等式，display展开第一项并说明交叉项抵消；第一项对应逆矩阵恒等式，后两项对应列空间与行空间的变化，可逆时为零。

3. 定理“伪逆的扰动界”（`thm:ls-pseudoinverse-perturbation`）：两矩阵正奇异值都不小于$s_0$时$\lVert\bm B^\dagger-\bm A^\dagger\rVert_2\leq3\lVert\bm E\rVert_2/s_0^2$（`eq:ch06-pseudoinverse-fixed-rank-perturbation`）；证明逐项display，用Penrose条件把后两项改写为含$\bm E^\top$与正交投影的乘积。

4. 例“秩不变时的伪逆变化”（`ex:ls-pseudoinverse-fixed-rank`）：$\bm A=\operatorname{diag}(1,0)$、$\bm B=\left[\begin{smallmatrix}1&t\\0&0\end{smallmatrix}\right]$，按元素写出两个伪逆与差，$s_0=1$。

5. 同例：第一、二项为零（列空间不变），差全部来自第三项，反映行空间由$\bm e_1$转到$(1,t)^\top$；差的范数$|t|/\sqrt{1+t^2}$，$t=0.1$时约$0.0995$，不超过$0.3$。

6. 指出关键是正奇异值的共同下界；display给出$\operatorname{diag}(1,0)$与$\operatorname{diag}(1,\varepsilon)$，扰动$\varepsilon\to0$而伪逆差$1/\varepsilon\to\infty$，新产生的小奇异值被取倒数。

7. 在固定秩$r$的矩阵集合$\mathcal M_r$上由Weyl界得$\sigma_r(\bm B)>\sigma_r(\bm A)/2$，进而$\lVert\bm B^\dagger-\bm A^\dagger\rVert_2\leq12\lVert\bm E\rVert_2/\sigma_r^2$，伪逆在其上连续；允许秩增加时加$t\bm u_{r+1}\bm v_{r+1}^\top$使伪逆差为$1/t$，伪逆不连续。

8. 对比求逆在可逆矩阵集合上连续，差别来自定义域；固定秩集合不是开集，伪逆的微分本部分不展开。

###### paragraph：数值秩

1. 由秩的微小改变使伪逆剧变、奇异值移动不超过$\lVert\bm E\rVert_2$，说明小于误差尺度的奇异值与零不可区分。

2. display定义阈值$\tau$下的数值秩$k=\#\{i:\sigma_i(\tilde{\bm A})>\tau\}$。

3. 取$\tau$为数据误差上界、定义相容矩阵：由第9章秩保证定理，相容矩阵的秩不小于$k$；由SVD截断得$\lVert\tilde{\bm A}-\tilde{\bm A}_k\rVert_2=\sigma_{k+1}\leq\tau$，$\tilde{\bm A}_k$是秩恰为$k$的相容矩阵；合起来数值秩是相容矩阵的最小秩。

4. 例“数值秩与阈值”（`ex:ls-numerical-rank`）：$\operatorname{diag}(1,0.5,0.001)$、$\tau=0.01$时数值秩为$2$，截断误差$0.001$，相容矩阵秩至少为$2$，间隔明显时$\tau\in[0.001,0.5)$都给出$2$；奇异值$1,0.012,0.009$时$\tau=0.01$与$0.015$分别给出$2$与$1$。

5. 阈值按舍入误差（$u\sigma_1$乘维数常数）或测量噪声在谱范数下的规模选取。

6. 区分精确秩与给定误差水平下可辨认的方向数，间隔明显时稳定、缓慢衰减时随阈值变化，不能机械判断是否为零，引出下一节的正则化。

### 17.2 正则化方法

1. 由小奇异值方向的放大无法被正交算法改变进入，提出主动修改目标、以拟合误差换取稳定。

2. 说明两小节分工（惩罚与截断）及每小节先从问题出发说明新目标与奇异方向上的作用、再在小例子上逐步执行算法、最后分析误差与代价的顺序，强调算出的是新目标的解，不能当作原问题更准确的解。

#### 17.2.1 岭回归与Tikhonov正则化

补充图解：确定扰动下的岭回归误差。取$\bm A=\operatorname{diag}(1,0.05)$、真实系数$(1,1)^\top$，在右端加入扰动$(0,0.05)^\top$。蓝线是无扰动岭解相对真实系数的偏差范数，绿虚线是扰动经正则化映射后的范数，黄色点划线为总误差范数。向量可以抵消，所以两条分量范数不能直接相加；这不是统计方差曲线。

##### 17.2.1.1 主要思想

###### paragraph：在目标中加入惩罚

1. 由近秩亏时拟合几乎同样好的系数可相差很远、含此增彼减的大分量，提出在目标中同时衡量系数大小；写出岭回归目标（式`eq:ls-ridge-objective`），说明惩罚使目标在拟合同样好的解中偏向长度较小者，$\lambda$越大偏向越强。

2. 引入惩罚矩阵$\bm\Gamma\in\mathbb R^{p\times d}$与一般Tikhonov目标，岭回归是$\bm\Gamma=\bm I$，$\bm\Gamma=[1\ -1]$惩罚分量之差；说明因$\bm L$已表示严格下三角部分而改记$\bm\Gamma$。

###### paragraph：化为增广最小二乘

1. 以$\bm A=\operatorname{diag}(3,1)$、$\bm b=(3,1)^\top$、$\bm\Gamma=\bm I$、$\lambda=1$按元素写出目标$(3x_1-3)^2+(x_2-1)^2+x_1^2+x_2^2$，指出它是向量$(3x_1-3,x_2-1,x_1,x_2)^\top$的平方长度，并把该向量写成$4\times2$矩阵乘$\bm x$减右端，说明惩罚添了两行零右端。

2. 一般情形写成增广最小二乘式`eq:ls-augmented-system`，说明惩罚在计算上增加了$p$行，每行要求$\sqrt\lambda(\bm\Gamma\bm x)_i$接近零。

###### paragraph：解的存在与唯一

1. 指出新目标是普通最小二乘问题，可直接沿用第11章普通最小二乘的解集结论（`sec:ls-ordinary-ls`）。

2. 定理“Tikhonov解的存在与唯一”（`thm:ls-tikhonov-existence-uniqueness`）：极小点恰为$(\bm A^\top\bm A+\lambda\bm\Gamma^\top\bm\Gamma)\bm x=\bm A^\top\bm b$的解，总存在，唯一当且仅当$\ker\bm A\cap\ker\bm\Gamma=\{\bm0\}$（式`eq:linear-algebra-tikhonov-common-nullspace`），岭回归总有唯一解；证明由增广残差与增广列空间正交得正规方程，再用$\bm x^\top(\bm A^\top\bm A+\lambda\bm\Gamma^\top\bm\Gamma)\bm x=\lVert\bm A\bm x\rVert_2^2+\lambda\lVert\bm\Gamma\bm x\rVert_2^2$确定$\ker\tilde{\bm A}$。

3. 用$\bm A=\bm\Gamma=[1\ -1]$说明唯一性条件可能失败：$(1,1)^\top$方向既不影响拟合也不受惩罚。

4. 指出目标中的平方不能去掉：加入惩罚后最小化$\lVert\bm A\bm x-\bm b\rVert_2+\lambda\lVert\bm x\rVert_2$是另一个问题。

###### paragraph：奇异方向上的滤波

1. 引入秩$r$、奇异三元组，单独一行写出$c_i=\bm u_i^\top\bm b$。

2. 定理“岭回归的滤波因子”（`thm:ls-ridge-filter-factors`）：$\bm x_\lambda=\sum_if_i(c_i/\sigma_i)\bm v_i$，$f_i=\sigma_i^2/(\sigma_i^2+\lambda)$（式`eq:matrix-analysis-ridge-filter-factor`），增益不超过$1/(2\sqrt\lambda)$，给出残差公式与单调性及$\lambda\to0^+$的极限。

3. 证明把目标写到补全的右奇异基坐标中，逐坐标配方得$z_i=\sigma_ic_i/(\sigma_i^2+\lambda)$，零空间坐标只受惩罚取零；再由增益界、残差的正交分解与$1-f_i$、$f_i/\sigma_i$的单调性完成其余结论。

4. 回到$\operatorname{diag}(3,1)$小例子按分量写出：两个方向的最小范数系数都是$1$，滤波因子为$9/10$与$1/2$，单独一行得$\bm x_\lambda=(9/10,1/2)^\top$；奇异值大的方向只压低十分之一，小的方向压掉一半。

5. 解释增益由$1/\sigma_i$变为有界量，滤波因子在$\sigma_i=\sqrt\lambda$处取$1/2$，例中第二个方向正落在转折点上；读图说明$\lambda$增大百倍时转折点移动一个数量级、峰值降为十分之一。

6. 说明代价是拟合改变、引入偏差，$\lambda$过小放大噪声、过大压掉信号，参数按误差规模或留出数据选取。

7. 图“岭回归与截断SVD沿奇异方向的作用”（`fig:ls-ridge-tsvd-filter-factors`）：(a)两种滤波因子的光滑曲线与阶梯，(b)最小二乘、岭回归与截断的方向增益。

##### 17.2.1.2 算法实现

1. 区分正交算法改善计算过程与正则化修改问题；修改后的问题是增广最小二乘，首选对增广矩阵作QR，适用于任意$\bm\Gamma$，在主要思想的小例子上执行。

2. 例“增广QR求岭回归”（`ex:ls-ridge-augmented-qr`）：给出设定$\bm A=\operatorname{diag}(3,1)$、$\bm b=(3,1)^\top$、$\bm\Gamma=\bm I$、$\lambda=1$，无惩罚解为$(1,1)^\top$。

###### paragraph：变量

1. 以列表列出：增广矩阵与右端$\tilde{\bm A},\tilde{\bm b}$，经济型QR因子$\bm Q,\bm R$，变换后的右端$\bm g=\bm Q^\top\tilde{\bm b}$，正则化解$\bm x$，原残差$\bm r$与惩罚量$\lVert\bm\Gamma\bm x\rVert_2$。

###### paragraph：输入与预处理

1. 输入$\bm A,\bm b,\bm\Gamma,\lambda$，核对尺寸，构造$\tilde{\bm A},\tilde{\bm b}$；例中写出$4\times2$的$\tilde{\bm A}$与$\tilde{\bm b}=(3,1,0,0)^\top$。

2. 步骤要求唯一性条件成立（岭回归总成立）；否则按第11章准则另选代表，例如对$\tilde{\bm A}$作SVD取最小范数解。

###### paragraph：计算步骤

1. QR分解：对$\tilde{\bm A}$作Householder QR；例中两列正交、长度$\sqrt{10}$与$\sqrt2$，写出单位化所得$\bm Q$与$\bm R=\operatorname{diag}(\sqrt{10},\sqrt2)$。

2. 变换右端：$\bm g=\bm Q^\top\tilde{\bm b}=(9/\sqrt{10},1/\sqrt2)^\top$。

3. 回代：解$\bm R\bm x=\bm g$，得$x_1=9/10$、$x_2=1/2$。

4. 核验：原残差$(3/10,1/2)^\top$、惩罚量约$1.030$，增广正规残差$\bm A^\top\bm r-\lambda\bm x=\bm0$。

5. 最终得到：单独一行写出$\bm x_\lambda=(9/10,1/2)^\top$，与按滤波因子算出的结果一致；原方程有精确解$(1,1)^\top$而残差非零，这不是计算误差而是新目标的解。

###### paragraph：SVD路线

1. $\bm\Gamma=\bm I$时作一次SVD，对每个$\lambda$按$z_i=\sigma_ic_i/(\sigma_i^2+\lambda)$重算系数并组合，分解与$\lambda$无关，扫描多个参数时最省；例中改取$\lambda=9$，滤波因子为$1/2$与$1/10$，立即得$(1/2,1/10)^\top$。

###### paragraph：Cholesky路线

1. 对$\bm A^\top\bm A+\lambda\bm\Gamma^\top\bm\Gamma$作Cholesky分解后前代、回代；说明正规矩阵不是必须形成的对象，形成它会使条件数平方。

2. 例“直线拟合的岭回归”（`ex:ls-ridge-line-fit`）：沿用第11章直线拟合数据（`ex:ls-line-least-squares`），$\bm\Gamma=\bm I$、$\lambda=1$。

3. 逐步执行：形成方程$\left[\begin{smallmatrix}4&3\\3&6\end{smallmatrix}\right]\bm x=(5,6)^\top$；分解得$l_{1,1}=2$、$l_{2,1}=1.5$、$l_{2,2}=\sqrt{15}/2\approx1.9365$；前代得$y_1=2.5$、$y_2\approx1.1619$；回代得$x_2=0.6$、$x_1=0.8$；核验拟合值$(0.8,1.4,2.0)^\top$、残差$(0.2,0.6,0)^\top$与$\bm A^\top\bm r=\lambda\bm x$。

4. 最终得到$\bm x_\lambda=(0.8,0.6)^\top$；与最小二乘解比较残差平方由$1/6$增至$0.4$、长度由$1.269$降为$1$，按SVD路线核对滤波因子约$0.877$与$0.456$。

###### paragraph：大型问题

1. 只能乘向量访问时把LSQR用于增广问题，$\tilde{\bm A}$乘向量只需分别乘$\bm A$与$\bm\Gamma$。

##### 17.2.1.3 算法分析

###### paragraph：正确性

1. 由定理`thm:ls-tikhonov-existence-uniqueness`，正则化目标的极小点即增广最小二乘解；唯一性条件成立时$\bm R$可逆，增广QR给出唯一解，三条路线在精确算术下给出同一结果。

###### paragraph：数值敏感度

1. 增广QR的误差由$\kappa_2(\tilde{\bm A})$控制，Cholesky路线的条件数为$\kappa_2(\tilde{\bm A})^2$；单独一行写出岭回归中$\kappa_2(\tilde{\bm A})=((\sigma_1^2+\lambda)/(\sigma_d^2+\lambda))^{1/2}\leq(1+\sigma_1^2/\lambda)^{1/2}$，即使秩亏也有界，只在$\lambda$不太小时与增广QR同样可靠；直线拟合例中$\kappa_2(\bm A)^2\approx8.55$而$\kappa_2(\tilde{\bm A})^2\approx4.44$。

###### paragraph：结果检验

1. 结果回到正则化目标核验，分别报告拟合误差与惩罚大小，正规残差检查$\bm A^\top(\bm b-\bm A\bm x_\lambda)-\lambda\bm\Gamma^\top\bm\Gamma\bm x_\lambda$；增广QR例中两者约为$0.583$与$1.030$，而$\bm A^\top\bm r=(9/10,1/2)^\top$不为零，用原问题的检查会误判。

###### paragraph：计算代价

1. 增广QR为$O((m+p)d^2)$；Cholesky路线形成正规矩阵约$md^2$、分解约$d^3/3$，同正规方程法；SVD路线一次分解$O(md^2)$，此后每个新$\lambda$只需$O(rd)$。

#### 17.2.2 谱截断正则化

##### 17.2.2.1 主要思想

###### paragraph：最小范数解中的放大

1. 由第7章的SVD写出$\bm A^\dagger\bm b=\sum_i(c_i/\sigma_i)\bm v_i$，说明第$i$个方向的误差经$c_i$放大$1/\sigma_i$，由误差预算提出只在可靠方向上恢复系数。

###### paragraph：只保留可靠方向

1. 以阈值$\tau$取$J=\{i:\sigma_i>\tau\}$或指定保留$k$个，定义$\bm x_k$并称为截断SVD求解；与岭回归对照，相当于取滤波因子为$1$或$0$。

2. 例“对角矩阵的谱截断”（`ex:ls-tsvd-diagonal`）：$\bm A=\operatorname{diag}(1,1/100)$，真值$(1,1)^\top$，带误差观测$(1,3/100)^\top$；按分量写出不截断系数$1$与$3$、$\tau=1/10$时滤波因子$1$与$0$，不截断得$(1,3)^\top$（误差放大百倍），截断得$(1,0)^\top$。

3. 两种恢复误差范数为$2$与$1$，但改善以丢弃真实第二分量为代价，不能从一个算例推断截断总更好，一般情形见算法分析的误差分解。

###### paragraph：限制子空间上的最小二乘

1. 把系数限制在$\operatorname{span}\{\bm v_1,\ldots,\bm v_k\}$，展开残差平方为三部分，只有保留方向一项依赖系数，推出$\bm x_k$是限制子空间中的最小二乘解，被舍弃的观测分量转入残差；对角例中残差$(0,3/100)^\top$即舍弃的$c_2$。

###### paragraph：与截断矩阵的关系

1. 在此直接定义$\bm A_k=\sum_{i\leq k}\sigma_i\bm u_i\bm v_i^\top$，写成$\bm x_k=\bm A_k^\dagger\bm b$；指出第18章将把$\bm A_k$作为低秩逼近研究，区分低秩重建与稳定恢复输入两种目的。

##### 17.2.2.2 算法实现

1. 说明每步做什么：求SVD并投影右端，按保留规则设置系数，合成解并读出残差；在近共线设计上执行。

2. 例“近共线设计的截断求解”（`ex:ls-tsvd-steps`）：给出$3\times2$设计矩阵（两列$(1,1,1)^\top$与$(1,1.01,0.99)^\top$）与$\bm b=(1,1.1,0.9)^\top$，指出它是例`ex:ls-nearly-collinear-design`取$\varepsilon=0.01$、$\delta=0.1$的情形，阈值$\tau=0.1$。

###### paragraph：变量

1. 以列表列出：奇异三元组$\sigma_i,\bm u_i,\bm v_i$，投影分量$\bm c$，保留集$J$与$k$，系数$\bm z$，截断解$\bm x$，原残差$\bm r$。

###### paragraph：输入与预处理

1. 输入$\bm A,\bm b$与$\tau$（或$k$），求经济型SVD；例中$\sigma_1\approx2.4495$、$\sigma_2\approx0.0100$，$\bm v_1\approx(1,1)^\top/\sqrt2$、$\bm v_2\approx(1,-1)^\top/\sqrt2$，$\bm u_1\approx(0.5773,0.5802,0.5745)^\top$、$\bm u_2\approx(0.0024,-0.7047,0.7095)^\top$。

###### paragraph：计算步骤

1. 投影右端：$\bm c=\bm U^\top\bm b$，例中$c_1\approx1.7326$、$c_2\approx-0.1343$。

2. 确定保留集：例中只有$\sigma_1>0.1$，$J=\{1\}$、$k=1$。

3. 设置系数：保留方向$z_i=c_i/\sigma_i$、其余为零，除法只在保留的正奇异值上做；例中$z_1\approx0.7073$、$z_2=0$，不截断时第二个系数约$-13.435$。

4. 合成解：$\bm x=\sum_{i\in J}z_i\bm v_i$，例中$\bm x_1\approx(0.5001,0.5002)^\top$。

5. 读出拟合值与残差：$\bm A\bm x_k=\sum_{i\in J}c_i\bm u_i$不必再乘$\bm A$；例中$\bm b$在列空间内，残差$c_2\bm u_2\approx(-0.0003,0.0947,-0.0953)^\top$，长度$|c_2|\approx0.1343$。

6. 核验：限制子空间中的正规条件$\bm v_1^\top\bm A^\top\bm r=0$成立，完整正规残差$\sigma_2c_2\bm v_2\approx(-0.00095,0.00095)^\top$长度约$0.0013$，$\bm x_1$不是原最小二乘解。

7. 最终得到$\bm x_1\approx(0.50,0.50)^\top$；换阈值只需增减项，取$\tau<\sigma_2$时加入$-13.4\,\bm v_2$得精确拟合的$(-9,10)^\top$，与例`ex:ls-nearly-collinear-design`的最小二乘解相同；截断以约$0.134$的残差换来两个接近$0.5$的系数。

##### 17.2.2.3 算法分析

###### paragraph：误差分解

1. 设观测为真实输入加噪声，说明误差与拟合损失可按奇异方向分开。

2. 定理“截断SVD的误差分解”（`thm:ls-tsvd-error-decomposition`）：误差等于保留方向的噪声放大减去舍弃方向的真实分量，两项正交且第一项不超过$\lVert\bm e\rVert_2/\sigma_k$，并给出残差平方与正规残差公式；证明代入$c_i=\sigma_i\bm v_i^\top\bm x_{\mathrm{true}}+\bm u_i^\top\bm e$相减，再用正交分解与$\bm A^\top\bm u_i=\sigma_i\bm v_i$。

3. 解读两项为噪声放大与偏差，用对角例说明不截断时误差$(0,2)^\top$全是噪声放大、截断后误差$(0,-1)^\top$全是偏差。

4. 残差平方多出舍弃的$c_i^2$，正规残差只在舍弃方向上，限制子空间中的正规条件成立而完整条件一般不成立；近共线例中约$0.0013$的正规残差正是这一项。

###### paragraph：计算代价

1. 主要代价是一次SVD，为$O(md^2)$；此后投影右端约$mr$、合成解约$dk$次运算，换阈值不必重新分解。

##### 17.2.2.4 与岭回归的比较

1. 把截断看成取值$0$或$1$的滤波因子，与岭回归的光滑曲线对照，提出在同一组数据上比较解、残差与观测改动后的变化。

2. 例“岭回归与截断SVD的比较”（`ex:ls-regularization-response`）：沿用近共线数据并改动观测为$(1,1.11,0.89)^\top$，表中列出最小二乘、$\lambda=10^{-4}$、$\lambda=10^{-2}$与$k=1$的解、残差（$0$、$0.067$、$0.133$、$0.134$）及响应比（$100$、$50$、$0.99$、$0.002$），解释响应比即第二方向增益。

3. 从表中读出两点：精确拟合的大系数全来自第二方向，系数越稳定残差越大；$\lambda=10^{-2}$时$f_2\approx0.0099$，岭回归与$k=1$的截断已很接近。

4. 讨论适用场景：奇异值有明显间隔时截断更清楚、缓慢衰减时岭回归更平稳；阈值联系噪声规模与间隔，取数据误差估计即只在17.1意义下可辨认的方向上反演，不同于按机器精度判定精确秩。

##### 17.2.2.5 与低秩逼近的边界

1. 指出截断求解与低秩逼近共用$\bm A_k$但最优性不能互借：第18章将证明$\bm A_k$是最佳秩$k$重建（`thm:matrix-analysis-best-low-rank`），但由正规残差$\bm x_k$一般不是原最小二乘解，矩阵逼近的最优性也不涉及真值与噪声。

2. 要求说明保留方向、噪声水平与拟合损失，并用截断处的间隔判断保留方向是否可靠，可用第9章的子空间扰动界。

### 17.3 求解方法的比较与选择

1. 说明第12—16章各在自己的前提下给出方法，本节把它们放到同一问题上比较；同一矩阵上方法可能求的不是同一个解、要求的矩阵性质也不同，故按四个维度依次比较。

2. 逐一说明四个维度的直观含义：求解目标（要哪种解、方法能否直接面对）、矩阵条件（形状、对称正定、秩与访问方式）、计算开销与收敛速度（达到同一精度的运算、存储与数据读取）、数值稳定性（误差来源与算法是否额外放大）；最后合起来给出典型问题的取舍。

3. 比较对象是达到相同要求的总成本；17.2节的正则化与谱截断改变了目标，系数较小、成本较低不表示原问题解得更准，不与求原问题的方法直接比较。

#### 17.3.1 求解目标与方法适用性

###### paragraph：三种验收要求

1. 相容方程、一般最小二乘与最小范数解三种目标的检验标准不同，单独一行写出$\bm r=\bm0$、$\bm A^\top\bm r=\bm0$、$\bm A^\top\bm r=\bm0$且$\bm x\in\operatorname{range}\bm A^\top$三种要求。

2. 以15.10节的不相容系统$\bm A=\left[\begin{smallmatrix}1&0\\0&2\\0&0\end{smallmatrix}\right]$、$\bm b=(1,1,1)^\top$为例，$\hat{\bm x}=(1,1/2)^\top$、$\hat{\bm r}=(0,0,1)^\top$，原残差为$1$而正规残差为零，说明不能一律按原残差趋于零检验。

3. 以例`ex:ls-qr-min-norm-run`为例，$(0,1,1)^\top$与$(1,2,0)^\top$残差都为零，前者与零空间方向$(1,1,-1)^\top$正交、范数$\sqrt2$，后者范数$\sqrt5$，只有第三种要求能挑出最小范数解。

###### paragraph：经正规方程转换

1. 满列秩时最小二乘解是正规方程（单独一行写出）的唯一解，系数矩阵对称正定，可交给Cholesky、CG或在对称正定矩阵上收敛的定常迭代。

2. 三项代价：稀疏矩阵可能变稠密；条件数平方，单独一行写出$\kappa_2(\bm A^\top\bm A)=\kappa_2(\bm A)^2$，并以例`ex:ls-rhs-perturbation-near-parallel`的$\bm A_2$（$\varepsilon=10^{-8}$）说明Gram矩阵舍入后奇异；不显式形成时每次需$\bm A$与$\bm A^\top$各一次乘法；秩亏时正定保证不能照搬。

###### paragraph：经增广方程转换

1. 把残差作为未知量，残差定义与正交条件合成方阵方程，引出下面的定理。

2. 定理`thm:ls-augmented-kkt-system`“最小二乘的增广方程”：满列秩时分块系统有唯一解，对应最小二乘解与残差，系数矩阵对称、可逆且不定；证明分别验证解的对应、可逆性与正负二次型。

3. 在上述不相容例上，重排未知量后5阶增广矩阵分为三个对角块，二阶块特征值$(1\pm\sqrt{1+4\sigma^2})/2$，单独一行写出五个特征值约$1.618,-0.618,2.562,-1.562,1$，确认不定；解为$(0,0,1;1,1/2)$。

4. 因此可用分块$\mathrm{LDL}^\top$或MINRES而不能用Cholesky或CG；与正规方程相比保留稀疏结构、不使条件数平方，代价是未知量增至$m+d$个。

###### paragraph：三种适用方式

1. 定义“直接适用”“需转换”“需扩展版本”三种说法并各举例。

2. 指出三种方式只说明能面对目标，能写出迭代公式不等于满足收敛条件。

#### 17.3.2 矩阵条件

1. 说明方法的正确性与收敛建立在形状、对称正定性与秩之上，还规定了读取矩阵的方式（存储分解、矩阵乘向量、转置乘向量、逐行），按章分组说明，每组之后用一张正文宽短表汇总；迭代法按第14—16章的基本版本比较。

###### paragraph：方阵的直接分解

1. LU、Cholesky、分块$\mathrm{LDL}^\top$与低秩更新各自的矩阵要求，均需存储矩阵与因子；用于不相容最小二乘须经正规方程或增广方程转换。

###### paragraph：最小二乘的直接求解

1. 正规方程法要求满列秩并承受条件数平方，QR分满列秩与满行秩两支、秩亏时不能直接给最小范数解，SVD对任意形状和秩给出$\bm A^\dagger\bm b$；三者需存储$\bm A$，正规方程法可按行累计。

###### paragraph：定常迭代

1. 单独一行写出收敛条件$\rho(\bm I-\bm M^{-1}\bm A)<1$，分述Richardson、Jacobi、Gauss--Seidel、SOR与SSOR的保证条件；指出对称正定不保证Jacobi收敛。

2. 用于最小二乘须经正规方程，满列秩时Gauss--Seidel、SOR、SSOR的保证成立而Jacobi须另查；贯穿例`ex:ls-stationary-running-example`上各方法都收敛，速度留到下一小节比较。

###### paragraph：Krylov子空间法

1. CG要求对称正定，MINRES要求对称非奇异可不定（奇异时看$\lVert\bm A\bm r_k\rVert_2$且一般不给最小范数解），GMRES、BiCG、BiCGSTAB适用于一般非奇异方阵。

2. 访问要求：BiCG需转置作用，其余方阵方法只需$\bm A\bm v$；用于最小二乘须转换，CG经正规方程、MINRES经增广方程。

3. LSQR与LSMR直接处理长方、秩亏与不相容问题，每轮需$\bm A\bm v$与$\bm A^\top\bm u$，零初值选出最小范数解，也能解相容方程。

###### paragraph：行列投影法

1. 标准Kaczmarz求解相容方程，不相容时在各行间往返而不停在最小二乘解；扩展Kaczmarz以列投影分离不可拟合部分，需按列访问。

###### paragraph：汇总

1. 指出“需转换”须重查转换后系统的结构、条件数、零空间与误差度量，“直接适用”也不能省去预条件、停止检验与退化处理。

2. 五张短表分别置于方阵直接分解、最小二乘直接方法、定常迭代、Krylov方法与行列投影的讲解之后；首表保留`tab:ls-method-applicability`，其余分别为`tab:ls-least-squares-method-applicability`、`tab:ls-stationary-method-applicability`、`tab:ls-krylov-method-applicability`、`tab:ls-row-method-applicability`。表中仍完整保留原来的20行：对LU、Cholesky、分块$\mathrm{LDL}^\top$、低秩更新、正规方程法、QR、SVD、各定常迭代、CG、MINRES、GMRES、BiCG、BiCGSTAB、LSQR、LSMR、标准与扩展Kaczmarz，列出对矩阵的要求、对矩阵的访问与对不相容最小二乘的适用方式。

#### 17.3.3 计算开销与收敛速度

###### paragraph：总成本的组成

1. 单独一行写出总成本约为准备成本加步数乘每步成本，说明各项包含什么，并计入存储与通信；直接法成本集中在准备，迭代法由步数决定。

2. 设$\bm A$有$q$个非零元，一次矩阵乘向量约$2q$次运算。

###### paragraph：直接法的运算量

1. 稠密方阵LU约$\tfrac23d^3$，Cholesky与$\mathrm{LDL}^\top$约一半，每个右端约$2d^2$；单独一行写出$s$个右端的总量$\tfrac23d^3+2sd^2$，以$d=1000$、$s=100$比较复用分解（约$8.7\times10^8$）与每次重新分解（约$6.9\times10^{10}$）。

2. 稠密长方矩阵Householder QR约$2md^2-\tfrac23d^3$，正规方程法约$md^2+\tfrac13d^3$，以$m=1000$、$d=100$得约$1.9\times10^7$与$1.0\times10^7$；SVD同量级但常数更大并提供更多信息。

3. 稀疏分解成本由依赖排序的填充决定，不能套用稠密估计。

###### paragraph：迭代法的每步开销

1. 短递推方法存储固定；GMRES第$k$步正交化约$4kd$次运算，$k$步共约$2dk^2$，基存储约$kd$个数。

2. 表`tab:ls-iterative-cost`“Krylov方法的每步开销”：列出CG、MINRES、GMRES、BiCG、BiCGSTAB、LSQR、LSMR每步的矩阵作用与工作存储。

3. 以$d=10^6$、$q=5\times10^6$、$100$步为例，矩阵乘向量约$10^9$次运算而正交化约$2\times10^{10}$次、基存储约$10^8$个数，正交化成为主要开销；重启限制增长但可能停滞。

4. 统一“一步”的含义：Kaczmarz一步读一行、一轮扫掠才相当于一次矩阵乘向量，BiCGSTAB一轮两次乘法，SSOR一轮两次扫掠；应按数据遍历次数或总运算量比较。

###### paragraph：收敛速度

1. 各方法的收敛机制：定常迭代看谱半径，单独一行写出缩小到$10^{-6}$倍所需轮数$\ln10^{-6}/\ln\rho$；CG因子由$\sqrt\kappa$控制而最优Richardson由$\kappa$控制，CG还取决于特征值分布；GMRES对非正规矩阵只看特征值不足；LSQR、LSMR由非零奇异值平方的分布决定；Kaczmarz由行法向夹角与访问顺序决定。

2. 在贯穿例上（$\kappa_2\approx1.939$）单独列出Richardson（最优步长）、Jacobi、Gauss--Seidel、SOR（$\omega=6/5$）的谱半径$0.319,0.289,0.083,0.2$与CG界因子$0.164$及对应轮数；指出CG两步即精确，Gauss--Seidel远快于Jacobi而SOR反而慢于Gauss--Seidel。

3. 由几何推出二维Kaczmarz每轮扫掠误差长度乘以$\cos^2\theta$（单独一行写出），贯穿例$\cos^2\theta=49/170\approx0.288$，并用16.1节算法实现中的距离比$0.537=\cos\theta$核对；例`ex:ls-kaczmarz-two-sweeps`两行近平行，$\cos^2\theta=9/10$，误差长度$0.671\to0.604$，缩小到$10^{-6}$倍约需$131$轮。

4. 结论：单独一行写出达到同一精度的总成本，应在同一问题与停止要求下比较，不能凭单步便宜或个别算例断言普遍更快。

#### 17.3.4 数值稳定性

###### paragraph：三种误差来源

1. 区分问题病态、有限精度算法行为与提前停止三种来源。

2. 后向稳定算法的后向误差与机器精度同阶，单独一行写出定理`thm:ls-forward-backward-error`的前向误差界，以例`ex:ls-backward-error-computation`的$\eta_2\approx1.92\times10^{-3}$、界$0.0075$与实际误差$0.0058$说明。

3. 正规方程法的放大因子为$\kappa_2(\bm A)^2$，QR与SVD在残差小时与$\kappa_2(\bm A)$同阶；LSQR、LSMR不形成正规矩阵，改善计算路线但不消除病态。

###### paragraph：按目标核验

1. 相容方程看原残差，不相容最小二乘看原残差与正规残差，最小范数还要看初值与零空间处理，零初值使迭代留在$\operatorname{range}\bm A^\top$中。

2. 递推残差与预条件残差须回到原数据重算真实残差，并区分达到容差与步数用尽、停滞或中断。

###### paragraph：各类方法的数值风险

1. 直接分解的风险在主元增长，Cholesky在对称正定时无此问题；Krylov递推的风险在基失去正交，可再正交化或以真实残差核验。

2. BiCG、BiCGSTAB与非正定CG可能遇到过小分母，须区分收敛与中断；重启GMRES可能停滞；标准Kaczmarz在不相容时循环；各有处理办法，不宜统称不稳定。

###### paragraph：预条件是否仍解同一个问题

1. 在相容可逆方程上左右预条件不改变解，引用15.12.3节。

2. 不相容最小二乘左预条件后单独一行写出以$\bm M^{-\top}\bm M^{-1}$为权的加权目标；以16.2节算法实现中例子的$\bm A=(1,1)^\top$、$\bm b=(1,3)^\top$、$\bm M=\operatorname{diag}(1,2)$为例，解由$2$变为$7/5$。

3. 右预条件保持残差与解集，但零初值下取$\lVert\bm M\bm x\rVert_2$最小的解；以$x_1+x_2=2$、$\bm M=\operatorname{diag}(1,2)$为例，最小范数解$(1,1)^\top$变为$(8/5,2/5)^\top$（单独一行）；比较预条件须回到第11章的目标与选解准则。

#### 17.3.5 典型问题的方法选择

1. 说明把四个维度合起来对典型问题取舍，每类先说特点再说方法与理由。

###### paragraph：能分解的中小型问题

1. 直接法无收敛问题、多右端可复用分解；对称正定用Cholesky、对称不定用分块$\mathrm{LDL}^\top$、一般方阵用部分主元LU、低秩修改用低秩更新；最小二乘条件良好时可用正规方程法，一般用Householder QR，秩亏或秩未知用SVD。

###### paragraph：大型稀疏方程

1. 按结构选CG、MINRES、GMRES或BiCGSTAB（能取转置时也可用BiCG）并配预条件；定常迭代单独求解较慢，但常作Krylov方法的预条件。

###### paragraph：大型稀疏或长方的最小二乘

1. 用LSQR或LSMR：只需$\bm A\bm v$与$\bm A^\top\bm u$，不形成Gram矩阵、存储固定；也能解相容方程，不能笼统说在方阵上效率更低。

2. 原方阵可直接用CG、MINRES时后者通常更有优势：每步一次矩阵作用、收敛由$\bm A$的谱决定，而LSQR、LSMR面对$\kappa_2(\bm A)^2$；取舍还看预条件、访问成本与精度。

###### paragraph：逐行访问的数据

1. Kaczmarz每步成本最低但全局收敛可能很慢（贯穿例每轮$0.288$、近平行时$0.9$），应按数据遍历次数比较；不相容最小二乘须用扩展版本并计入列投影成本。

2. 一切取舍回到第11章的目标与选解准则、17.1节的误差要求，再比较满足矩阵条件的方法的总成本。

### 17.4 本章小结

1. 点明本章讨论结果的可信程度，误差分为问题敏感性、算法误差与提前停止三种来源，再说明改变目标与比较方法两部分。

2. 回应问题敏感性：单独一行写出矩阵与右端同时扰动时的相对误差界，分子为条件数乘相对扰动、分母为到奇异边界的余量，小奇异值方向放大最多。

3. 汇总最小二乘输出的不同敏感性、伪逆在秩增加处的不连续，以及数值秩须按误差水平确定。

4. 汇总算法误差与提前停止误差：残差小只说明后向误差小，前向误差约不超过条件数乘后向误差，正规方程使条件数平方而QR、SVD、LSQR、LSMR直接作用于$\bm A$，提前停止须以真实残差与正规残差核验。

5. 汇总正则化：Tikhonov等价于增广最小二乘，单独一行写出唯一性条件$\ker\bm A\cap\ker\bm\Gamma=\{\bm0\}$，岭回归使增益有界，谱截断是限制子空间中的最小二乘，误差分为噪声放大与偏差；二者解的是新目标。

6. 汇总方法选择：先固定目标与验收标准，再按矩阵条件确定可用方法，按相同精度下的总成本比较，并分开三种误差来源。

7. 指出没有普遍最优的方法，分别说明直接分解、Krylov方法、LSQR与LSMR及行投影法的适用场景。

## 第18章 矩阵逼近

正文入口：[08-matrix-approximation.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/08-matrix-approximation.tex)；子文件依次为[01-problem-and-rank-one.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/08-matrix-approximation/01-problem-and-rank-one.tex)、[02-rank-k.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/08-matrix-approximation/02-rank-k.tex)、[03-weighted.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/08-matrix-approximation/03-weighted.tex)、[04-orthogonal.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/08-matrix-approximation/04-orthogonal.tex)、[05-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/08-matrix-approximation/05-summary.tex)。

1. 从两个具体问题进入：数据矩阵的许多列大致落在少数方向上，能否只用$k$个方向重建全部列并使误差最小；测得的旋转矩阵因噪声不再正交，离它最近的正交矩阵是哪一个。归结为给定$\bm A$、在秩或正交约束下找最近矩阵，提出本章要回答的四件事：最小误差、取得它的矩阵、唯一性，以及误差度量或约束改变时的变化。
2. 区分本章与第11—18章：那里求$\bm A\bm x\approx\bm b$的输入向量，这里没有右端，未知量与残差都是矩阵。
3. 说明前三节的路线：第18.1节写清约束与误差；秩约束下先固定方向由投影求系数、再选方向；第18.2节在秩一情形完成这两步并求一般实对称矩阵Rayleigh商的极值；第18.3节推广到$k$维子空间，经迹极值证明截断SVD在两种范数下最优并讨论唯一性。
4. 说明后两节的分工：第18.4节改用加权长度，得到广义Rayleigh商并化归可分离权重的低秩逼近；第18.5节把约束换成正交性，目标成为线性的迹，最优解是极分解正交因子，要求旋转时在最小奇异方向作符号修正。
5. 依赖说明（一）：使用第6章的对称谱分解与第7章的SVD，两种分解的存在不依赖本章的极值结论；指出第9章已提前使用本章的Rayleigh--Ritz定理与最佳低秩逼近定理，它们的证明只依赖这两种分解。
6. 依赖说明（二）：正交逼近依赖第8章构造的极分解正交因子，本章证明其最优性；加权部分用第3章的加权内积与Gram因子，计算用第12章的Cholesky分解；第17章也用截断SVD，但为稳定求解方程，本章把截断矩阵本身作为近似对象。

### 18.1 矩阵逼近问题

1. 给出两类动机：近似低秩的数据矩阵希望用低秩矩阵代替，同时使重建误差尽量小。

2. 按含义应正交、受测量误差影响的矩阵希望用最近的正交矩阵代替。

###### paragraph：问题的形式

1. 引入术语“矩阵逼近”，单独一行写出一般形式式`eq:matrix-approximation-problem`$\min_{\bm X\in\mathcal X}\lVert\bm A-\bm X\rVert$及取得最小值的$\bm X$。

2. 说明问题的三部分：目标是离$\bm A$最近的矩阵，约束由允许集合表达，范数规定“近”的含义；单独一行写出秩不超过$k$的集合$\mathcal X_k$与正交矩阵集合$\mathcal O_d$（要求$m=d$）。

3. 回指章首：$\bm A$不是方程的系数矩阵，没有右端、不求输入向量，输出是近似矩阵与最小误差。

###### paragraph：Frobenius误差

1. 按列归并元素，得式`eq:matrix-approximation-frobenius-columns`：Frobenius误差等于各列重建的平方偏差之和，每一列的偏差都计入总误差。

2. 说明秩不超过$k$等价于存在$k$个向量使每列重建落在其张成中，即全部重建列共用至多$k$个独立方向，因此要同时选方向与系数。

###### paragraph：谱范数误差

1. 回引第`sec:ls-common-induced-norms`节的谱范数$\lVert\bm A-\bm X\rVert_2=\max_{\lVert\bm x\rVert_2=1}\lVert(\bm A-\bm X)\bm x\rVert_2$，说明它只记录最坏单位输入方向的偏差。

2. 数值对照：$\bm A=\operatorname{diag}(3,2,1)$、$\bm X=\operatorname{diag}(3,0,0)$，残差$\operatorname{diag}(0,2,1)$的Frobenius平方误差为$5$、谱范数误差为$2$，由$4x_2^2+x_3^2\leq4$且在$\bm e_2$取等说明后者；两种范数下的最优解在第18.3.3节比较。

3. 第18.5节换成正交约束时，允许集合不再由秩的上限描述，求解方法随之改变；本节与后两节只讨论秩约束。

###### paragraph：边界情形

1. 记$r=\operatorname{rank}\bm A$，$k=0$时只能取零矩阵，平方误差为$\lVert\bm A\rVert_{\mathrm F}^2$。

2. $k\geq r$时取$\bm A$本身误差为零；范数为零的矩阵只有零矩阵，故误差为零迫使$\bm X=\bm A$。

3. 需要研究的是$1\leq k<r$：$\bm A$不在允许集合中，必须舍弃部分信息，问题在于舍弃哪部分损失最小。

4. 示例“三个坐标向量的重建”（`ex:ls-low-rank-three-columns`）：$\bm A=\operatorname{diag}(3,2,1)$、总平方长度$14$、$k=2$；说明投影到坐标平面时被消去的列，单独一行比较三个坐标平面的保留量$13,10,5$与损失$1,4,9$；指出两个尚未回答的问题：倾斜平面能否更好、平面内取投影是否最好。

5. 预告先在$k=1$时回答“给定方向怎样取系数、怎样选方向”，再推广到一般$k$。

### 18.2 秩一逼近

1. 说明$k=1$时全部列用同一方向的倍数重建，分两步：先固定方向求系数，再选保留平方长度最多的方向，后一步化为单位向量上的二次型极值并由谱分解求解；最后由奇异值分解写出最优近似矩阵。

#### 18.2.1 固定方向下的最优系数

###### paragraph：秩一矩阵的写法

1. 非零的秩一矩阵列空间是一条直线，每列是同一向量的倍数，写成$\bm a\bm b^\top$；归一化后单独一行写出$\bm X=\bm u\bm c^\top=[c_1\bm u,\ldots,c_d\bm u]$、$\lVert\bm u\rVert_2=1$；说明长度吸收到系数中，单位约束不丢失非零候选，零矩阵对应$\bm c=\bm0$。

###### paragraph：逐列求最优系数

1. 由式`eq:matrix-approximation-frobenius-columns`，总误差是各列误差之和且第$j$列只含$c_j$，故各列分开处理。

2. 展开并配方得式`eq:matrix-approximation-rank-one-completing-square`，只有末项依赖$c_j$且非负，单独一行写出唯一最优系数$c_j=\bm u^\top\bm a_j$（正交投影系数）。

3. 按分量排成向量得式`eq:matrix-approximation-rank-one-coefficients`$\bm c=\bm A^\top\bm u$、重建$\bm u\bm u^\top\bm A$，说明方向固定后最优重建就是把每列投影到直线上。

###### paragraph：保留量

1. 代回求和得式`eq:matrix-approximation-rank-one-error`$\lVert\bm A-\bm u\bm u^\top\bm A\rVert_{\mathrm F}^2=\lVert\bm A\rVert_{\mathrm F}^2-\bm u^\top\bm A\bm A^\top\bm u$，并说明第二个等号所用的$\sum_j(\bm u^\top\bm a_j)^2=\lVert\bm A^\top\bm u\rVert_2^2$。

2. 定义保留量，总平方长度与方向无关，误差最小等价于保留量最大；把秩一逼近分成“求投影系数”和“找保留量最大的方向”两步。

3. 示例“固定方向时的秩一重建”（`ex:matrix-approximation-rank-one-fixed-direction`）：$\bm A=\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$、$\bm u=(1,1)^\top/\sqrt2$，按元素求内积得$c_1=c_2=3/\sqrt2$，重建矩阵四个元素均为$3/2$，残差元素为$\pm1/2$、平方和为$1$，再由$\lVert\bm A\rVert_{\mathrm F}^2=10$与保留量$9$核对；对照$\bm u=\bm e_1$得系数$(2,1)^\top$、残差只剩第二行$(1,2)$、平方误差$5$；是否在全部方向中最好留待下一小节。

#### 18.2.2 Rayleigh商与最优方向

###### paragraph：从保留量到二次型极值

1. 由上一小节把选方向写成在单位向量中最大化$\bm u^\top\bm G\bm u$，$\bm G=\bm A\bm A^\top$对称半正定。

2. 说明同样的单位向量二次型极值也出现在齐次最小二乘与第9章的特征值比较中，因此先对一般实对称$\bm S$求最大、最小值及取到的方向，再回到$\bm G$。

3. 用$\bm S=\operatorname{diag}(4,1)$单独一行写出$4x_1^2+x_2^2$，比较$\bm e_1$、$\bm e_2$与倾斜方向$(1,1)^\top/\sqrt2$（值$5/2$），说明证明全局极值必须比较全部单位方向。

###### paragraph：Rayleigh商

1. 说明长度约束的作用：不加约束时放大输入（如$3\bm e_2$给出$9$）就能增大二次型，与方向无关；除去长度得到只依赖方向的量，给出Rayleigh商的定义（`def:matrix-analysis-rayleigh-quotient`，式`eq:matrix-analysis-rayleigh-quotient`）。

2. 说明Rayleigh商在缩放下不变、只依赖直线，因此其在非零向量上的极值等价于单位球面上二次型的极值。

###### paragraph：用谱分解比较全部方向

1. 用谱分解把单位向量写成$\sum_ic_i\bm q_i$，单独一行写出$\sum_ic_i^2=1$，由二次型展开式得式`eq:matrix-approximation-rayleigh-weighted-average`$R_{\bm S}(\bm x)=\sum_i\lambda_ic_i^2$，指出它是各特征值的加权平均；以$\operatorname{diag}(4,1)$的倾斜方向核对$\tfrac12\cdot4+\tfrac12\cdot1=5/2$。

2. Rayleigh--Ritz定理（`thm:matrix-analysis-rayleigh-ritz`，式`eq:matrix-analysis-rayleigh-ritz`）：$\lambda_d\leq R_{\bm S}\leq\lambda_1$，两端分别在$\bm q_1$、$\bm q_d$取到，取等当且仅当$\bm x$是相应特征空间中的非零向量。证明第一段由$\lambda_1-R_{\bm S}(\bm x)=\sum_i(\lambda_1-\lambda_i)c_i^2\geq0$等得到两端的界及可达性。

3. 证明第二段：和式为零当且仅当$\lambda_i<\lambda_1$的系数都为零，由谱投影定理这正是特征空间$\ker(\bm S-\lambda_1\bm I)$；最小值同理。

4. 引出图“单位圆约束下的极值落在特征方向”（`fig:ls-sphere-constrained-extremum`）：二次型水平椭圆在特征方向与单位圆相切；图注给出$\bm S=\left[\begin{smallmatrix}2&0.5\\0.5&1\end{smallmatrix}\right]$、$\lambda_{1,2}=(3\pm\sqrt2)/2$，并说明子空间约束直线供第9章最小最大原理使用。

5. 示例“对角矩阵在全部单位方向上的比较”（`ex:ls-rayleigh-diagonal-two-by-two`）：$\bm x=(\cos\theta,\sin\theta)^\top$给出$1+3\cos^2\theta\in[1,4]$，最大、最小值在$\pm\bm e_1$、$\pm\bm e_2$取到，$\theta=\pi/4$给出开头的$5/2$；结论段确认它们正是特征值与特征方向，倾斜方向严格介于两者之间。

6. 说明定理不要求半正定，以$\operatorname{diag}(1,-2)$为例单独一行写出$x_1^2-2x_2^2$，单位方向上的值介于$-2$与$1$之间。

###### paragraph：最优方向的唯一性

1. 区分最优值与最优方向：最大值总是唯一的数，取到它的方向由特征空间决定。

2. $\lambda_1$单重时最优方向只有$\pm\bm q_1$，重复时特征空间中每个单位向量都最优，例如$\bm S=\bm I$。

3. 重根时$\bm q_1$只是代表，最优方向集合由谱投影唯一确定；最小值相同。

###### paragraph：特例：$\bm S=\bm A^\top\bm A$

1. Rayleigh商是输出与输入长度比的平方。

2. 结合第7章，单位输入的最大输出长度为$\sigma_1$、在$\bm v_1$取到，最小为$\bm A^\top\bm A$最小特征值的平方根。

3. 联系齐次最小二乘：零空间非零时最小值为零、任一单位零空间向量最优；满列秩时$\bm A^\top\bm A\succ0$，最小值为正。

###### paragraph：回到秩一逼近

1. 取$\bm S=\bm G=\bm A\bm A^\top$，最大保留量为$\lambda_1(\bm G)$，在最大特征空间的单位向量取到；代入式`eq:matrix-approximation-rank-one-error`单独一行写出最小平方误差$\lVert\bm A\rVert_{\mathrm F}^2-\lambda_1(\bm G)$。

2. 强调这里只使用第6章已证明的谱分解，分解的存在不依赖本节极值结论。

3. 示例“比较两个特征方向”（`ex:matrix-approximation-rank-one-eigen-directions`）：沿用前例，按元素求出$\bm G=\left[\begin{smallmatrix}5&4\\4&5\end{smallmatrix}\right]$，逐行相乘验证特征向量$(1,1)^\top$、$(1,-1)^\top$及特征值$9,1$，误差分别为$10-9=1$与$10-1=9$；再对全部单位方向$\bm u=(\cos\theta,\sin\theta)^\top$算出$\bm u^\top\bm G\bm u=5+4\sin2\theta\in[1,9]$，$\bm e_1$给出$5$与前例一致，确认上一小节所取方向最优、另一方向最差。

#### 18.2.3 最优解与逼近误差

###### paragraph：由奇异值分解读出最优解

1. 设$\bm A\neq\bm0$，由式`eq:ls-svd-transpose-relation`，$\bm A\bm A^\top$的特征值为$\sigma_i^2$及零、左奇异向量为特征向量，最大保留量$\sigma_1^2$在$\bm u_1$取到；由$\lVert\bm A\rVert_{\mathrm F}^2=\operatorname{tr}\bm G$单独一行写出最小平方误差$\sum_{i\geq2}\sigma_i^2$。

2. 由$\bm A^\top\bm u_1=\sigma_1\bm v_1$得系数$\sigma_1\bm v_1$，合成式`eq:matrix-approximation-rank-one-optimum`$\bm A_1=\bm u_1\bm u_1^\top\bm A=\sigma_1\bm u_1\bm v_1^\top$。

3. 指出它是SVD和式的第一项、是$\bm A$而非$\bm G$的秩一近似，输入是$\bm A$、输出是近似矩阵而非解向量。

###### paragraph：计算步骤

1. 开场说明计算只需求方向、求系数、合成三件事，在示例`ex:matrix-approximation-rank-one-fixed-direction`的$\bm A=\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$上执行。

2. 以列表列出变量：$\sigma_1^2$与$\bm u_1$（最大保留量与最优方向）、系数$\bm c=\sigma_1\bm v_1$、近似矩阵$\bm A_1$、核对用的平方误差$e$。

3. 以编号步骤执行：求最优方向（$\bm G$的最大特征对，或由SVD直接读出），例中$\sigma_1^2=9$、$\bm u_1=(1,1)^\top/\sqrt2$；求系数$\bm c=\bm A^\top\bm u_1=\tfrac3{\sqrt2}(1,1)^\top$，即$\sigma_1\bm v_1$、$\sigma_1=3$；合成$\bm A_1=\bm u_1\bm c^\top$；核对误差，残差元素为$\pm1/2$、$e=1=10-9$。

4. 最终结果单独一行写出$\bm A_1=\tfrac32\left[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right]$，四个元素均为$3/2$、秩一，$\sigma_2=1$，平方误差$1=\sigma_2^2$。

5. 同样步骤用于$\operatorname{diag}(3,2,1)$示例：$\bm u_1=\bm e_1$、$\bm c=(3,0,0)^\top$、$\bm A_1=3\bm e_1\bm e_1^\top$，只保留第一列，平方误差$14-9=5=4+1$。

###### paragraph：列重建与行重建

1. 说明为何用$\bm A\bm A^\top$：重建的是列向量，保留量是列向量投影长度平方和，对应左奇异方向。

2. 改为重建行向量时用$\bm A^\top\bm A$与$\bm v_1$，由$\bm A\bm v_1=\sigma_1\bm u_1$单独一行写出$\bm A\bm v_1\bm v_1^\top=\sigma_1\bm u_1\bm v_1^\top$，是同一个矩阵。

3. 指出这种解释依赖Gram矩阵，一般不定对称矩阵的Rayleigh商极值不能解释为某个矩阵的最佳秩一逼近。

###### paragraph：最优矩阵的唯一性

1. $\bm A=\bm0$时唯一最优近似是零矩阵。

2. $\sigma_1>\sigma_2$（或$r=1$）时最优方向只有$\pm\bm u_1$，成对变号不改变外积，最优矩阵唯一，不唯一的只是写法。

3. $\sigma_1=\sigma_2$时最大特征空间至少二维，不同直线给出不同的最优矩阵；例如$\bm A=\bm I_2$时每个单位向量的保留量都是$1$，单独一行写出误差$\lVert\bm I_2-\bm u\bm u^\top\rVert_{\mathrm F}^2=2-1=1$，$\bm e_1\bm e_1^\top$与$\bm e_2\bm e_2^\top$是两个不同的最优近似。

4. 结论：近似矩阵的非唯一性只来自最大奇异值重复，并转入$k$个方向的情形。

### 18.3 秩$k$逼近

1. 说明把共同方向扩展为$k$维子空间，仍先固定子空间求系数、再选子空间；保留量写成迹，选子空间成为迹极值问题，再由SVD写出截断SVD并证明最优性与讨论唯一性。

#### 18.3.1 子空间选择与迹极值

###### paragraph：固定子空间时的最优重建

1. 提出问题：先固定$k$维子空间，问各列怎样重建，直观答案是正交投影；用列标准正交的$\bm Y$表示子空间（不用$\bm V$以免与右奇异向量混淆），候选写成$\bm X=\bm Y\bm C$，$\bm Y\bm Y^\top$为正交投影。

2. 以$m=3$、$k=2$、$\bm Y=[\bm e_1,\bm e_2]$按元素写出$\bm Y\bm Y^\top$与$\bm Y\bm C$：投影去掉第三个分量，候选的第三行只能为零。

3. 引理“固定子空间时的正交误差分解”（`lem:ls-low-rank-projection-error`）：式`eq:ls-low-rank-projection-split`，第一项等于$\lVert\bm A\rVert_{\mathrm F}^2-\operatorname{tr}(\bm Y^\top\bm A\bm A^\top\bm Y)$，最优系数唯一为$\bm Y^\top\bm A$。证明第一段把误差拆成投影残差与$\bm Y(\bm Y^\top\bm A-\bm C)$，逐列验证正交，由勾股定理求和。

4. 证明第二段：再用勾股定理得残差平方等于总长度减去$\lVert\bm Y^\top\bm a_j\rVert_2^2$，求和成迹；第二项非负且仅在$\bm C=\bm Y^\top\bm A$时为零。

5. 解释引理：误差等于总平方长度减保留量；$k=1$时回到18.2.1的逐列公式；示例`ex:ls-low-rank-three-columns`中“先投影再计损失”正是最优重建；共同子空间把$d$个最小二乘问题合成一个矩阵近似问题。

6. 在$\bm Y=[\bm e_1,\bm e_2]$、$\bm A=\operatorname{diag}(3,2,1)$上按元素写出最优系数$\bm Y^\top\bm A$与重建$\bm Y\bm Y^\top\bm A$，平方误差$14-13=1$，与示例中坐标平面的损失一致。

###### paragraph：化为子空间的选择

1. 证明化归覆盖全部候选：把任一$\bm X$的列空间补成$k$维子空间得到$\bm Y$，误差不低于对应的投影误差；反之每个$\bm Y$给出投影候选，从而得到式`eq:ls-low-rank-subspace-reduction`，最大值的存在与取值留给迹极值定理。

###### paragraph：保留量的含义

1. 按列展开保留量为$k$个正交方向上的保留量之和，$k=1$时回到Rayleigh商；用迹的循环性说明它只依赖子空间而不依赖基；写出迹极值问题。

###### paragraph：两个候选界

1. 逐列套用Rayleigh--Ritz只得$k\lambda_1(\bm G)$，该界忽略正交约束，最大特征值单重且$k\geq2$时取不到。

2. 只比较由特征向量组成的子空间，保留量为所选特征值之和，前$k$个特征方向给出最大候选值。

3. 在$\bm G=\operatorname{diag}(9,4,1)$上核对：第一个界为$18$，超过总长度$14$；三个坐标平面给出$13,10,5$，前两个特征方向最好；一般地候选子空间为$\operatorname{span}\{\bm u_1,\ldots,\bm u_k\}$。

###### paragraph：倾斜子空间与权重

1. 以倾斜平面$\bm Y=\left[\begin{smallmatrix}1&0\\0&1/\sqrt2\\0&1/\sqrt2\end{smallmatrix}\right]$为例，权重$w_i=\lVert\bm Y^\top\bm e_i\rVert_2^2$为各行平方长度$1,\tfrac12,\tfrac12$，保留量$9+2+\tfrac12=\tfrac{23}2<13$；权重各不超过$1$、总和为$k$，引出定理（同时回答下界问题）。

2. 迹极值定理（`thm:matrix-analysis-trace-minimum`）：式`eq:matrix-analysis-trace-minimum`，$k$维子空间上$\operatorname{tr}(\bm Y^\top\bm S\bm Y)$介于后$k$个与前$k$个特征值之和之间，两端由相应特征向量取到；$\lambda_k>\lambda_{k+1}$时上界取等当且仅当$\operatorname{range}(\bm Y)$为前$k$个特征向量的张成。证明第一段把迹写成$\sum_i\lambda_iw_i$，由投影不增长度得$0\leq w_i\leq1$，由正交矩阵保持Frobenius范数得$\sum_iw_i=k$。

3. 证明第二段：以$\lambda_k$为分界写出恒等式，逐项判断符号得到上界，并由前$k$个特征向量取到。

4. 证明第三段：由恒等式读出取等条件——有间隙时$i>k$的权重必须为零，从而子空间含于并等于前$k$个特征向量的张成；反向验证。

5. 证明第四段：对$-\bm S$应用上界得到下界。

6. 在倾斜平面例中逐项核对恒等式：三项为$0,0,-\tfrac32$，合计正是$\tfrac{23}2-13$，亏损全部来自让给第三个特征值的权重。

###### paragraph：回到低秩逼近

1. $\bm A\bm A^\top$的前$k$个特征值之和为$\sum_{i\leq k}\sigma_i^2$，单独写出最大保留量，化归式中的最大值存在并由$\operatorname{span}\{\bm u_1,\ldots,\bm u_k\}$取到；在示例中确认任意倾斜平面的保留量不超过$13$。

2. 指出迹极值界对一般对称矩阵成立，但只有半正定Gram情形中迹才表示投影保留的长度平方，并转入把最优重建写成矩阵。

#### 18.3.2 截断SVD的构造

##### 18.3.2.1 主要思想

1. 写出SVD和式与最优$\bm Y=\bm U_k$，说明最优重建是$\bm U_k\bm U_k^\top\bm A$，化简只需看$\bm U_k^\top\bm u_i$。

2. 以$r=3$、$k=2$按元素写出$\bm U_2^\top\bm u_1=(1,0)^\top$、$\bm U_2^\top\bm u_2=(0,1)^\top$、$\bm U_2^\top\bm u_3=\bm0$；一般地推出$\bm U_k\bm U_k^\top\bm A=\sum_{i\leq k}\sigma_i\bm u_i\bm v_i^\top$，即投影到前$k$个左奇异方向等于保留SVD和式的前$k$项。

3. 定义截断SVD（式`eq:matrix-analysis-truncated-svd`）$\bm A_k=\sum_{i=1}^{\min(k,r)}\sigma_i\bm u_i\bm v_i^\top=\bm U_k\bm\Sigma_k\bm V_k^\top$，说明$k=0$时为零矩阵、$k\geq r$时为$\bm A$本身，与18.1的直接回答一致。

4. 由$\bm A_k\bm v_i=\sigma_i\bm u_i$（$i\leq k$）、$\bm A_k\bm v_i=\bm0$（$i>k$）说明列空间恰为前$k$个左奇异向量的张成，秩为$k$，满足约束。

##### 18.3.2.2 算法实现

1. 开场说明输入为已求出的SVD与$k$，输出$\bm A_k$或三个因子，计算不迭代，在倾斜且有重奇异值的矩阵上逐步执行。

2. 示例“有重奇异值的三阶截断”（`ex:matrix-approximation-truncated-three-by-three`）给出设定：$\bm A=\left[\begin{smallmatrix}3&2&0\\2&3&0\\0&0&1\end{smallmatrix}\right]$，核验$\bm u_1=(1,1,0)^\top/\sqrt2$、$\bm u_2=(1,-1,0)^\top/\sqrt2$、$\bm u_3=\bm e_3$是特征向量，可取$\bm v_i=\bm u_i$，奇异值为$5,1,1$，分别取$k=1,2$。

###### paragraph：变量

1. 以列表列出：秩预算$k$与秩$r$，奇异值与配对的左右奇异向量，截取的因子$\bm U_k,\bm\Sigma_k,\bm V_k$，缩放后的右因子$\bm W=\bm\Sigma_k\bm V_k^\top$，截断SVD$\bm A_k$与只在核验时形成的残差$\bm E_k$。

###### paragraph：输入与预处理

1. 核对$0\leq k\leq\min(m,d)$并确定$r$；$k=0$输出零矩阵、$k\geq r$输出$\bm A$；确认奇异值非增，否则连同配对的奇异向量一起重排，配对不能打乱。例中$r=3$，$k=1,2$满足$1\leq k<r$，奇异值已排好。

###### paragraph：计算步骤

1. 截取因子：取前$k$组得$\bm U_k,\bm\Sigma_k,\bm V_k$，只需压缩存储时到此输出；例中$k=1$时$\bm U_1=\bm V_1=\bm u_1$、$\bm\Sigma_1=5$，$k=2$时写出$\bm U_2=\bm V_2$与$\bm\Sigma_2=\operatorname{diag}(5,1)$。

2. 缩放右因子：$\bm W=\bm\Sigma_k\bm V_k^\top$，由$\bm A^\top\bm u_i=\sigma_i\bm v_i$知它等于最优系数$\bm U_k^\top\bm A$；例中$k=2$时$\bm W=\left[\begin{smallmatrix}5&5&0\\1&-1&0\end{smallmatrix}\right]/\sqrt2$。

3. 相乘重建：$\bm A_k=\bm U_k\bm W$；例中$\bm A_1=5\bm u_1\bm u_1^\top$左上四项均为$5/2$，再加$\bm u_2\bm u_2^\top$使对角元变为$3$、非对角元变为$2$，得$\bm A_2$。

4. 核验残差：形成$\bm E_k$并算两种范数；例中$\bm E_1$的Frobenius范数为$\sqrt2$，它是到$\operatorname{span}\{\bm u_2,\bm u_3\}$的正交投影，谱范数为$1$；$\bm E_2=\bm e_3\bm e_3^\top$，两种范数均为$1$。

5. 最终结果：单独写出$\bm A_1$与$\bm A_2=\left[\begin{smallmatrix}3&2&0\\2&3&0\\0&0&0\end{smallmatrix}\right]$，核对秩分别为一、二。

6. 重奇异值：由$\sigma_2=\sigma_3$，交换次序的另一SVD在第三步加上$\bm u_3\bm u_3^\top$，给出$\bm A_2'$，误差相同而矩阵不同，算法输出依赖SVD例程给出的那一组。

7. 引出图“低秩截断的几何”（`fig:ls-low-rank-truncation`）：单位圆的像椭圆被秩一近似压成主轴方向线段，残留谱范数误差为舍弃的$\sigma_2$；图注给出$\bm A=\left[\begin{smallmatrix}2&0.5\\0.5&1\end{smallmatrix}\right]$与$\sigma_{1,2}=(3\pm\sqrt2)/2$。

##### 18.3.2.3 算法分析

###### paragraph：表示与计算代价

1. 存储由$md$降为$k(m+d+1)$，按因子顺序乘向量需$O(k(m+d))$次运算，以$m=d=1000$、$k=10$为例；形成完整$\bm A_k$约需$mdk$次乘法，只在需要矩阵本身或核验时做；上述代价不含计算SVD本身，后者本书不作分析。

###### paragraph：用途的区别

1. 区分用途：第17章截断SVD求解用$\bm A_k$的伪逆稳定求解方程，本章评价的是$\bm A_k$本身的重建误差；误差大小与最优性由下一小节回答。

#### 18.3.3 最佳误差与最优性

###### paragraph：截断SVD的误差

1. 说明误差应由舍弃的奇异值决定；设$0\leq k<r$，写出余项$\bm A-\bm A_k=\sum_{i>k}\sigma_i\bm u_i\bm v_i^\top$，可按第7章读出大小。

2. 对$\bm x=\sum_ic_i\bm v_i$计算$\lVert(\bm A-\bm A_k)\bm x\rVert_2^2\leq\sigma_{k+1}^2\lVert\bm x\rVert_2^2$，并由$(\bm A-\bm A_k)^\top(\bm A-\bm A_k)$取迹，得式`eq:ls-truncated-errors`（谱范数误差$\sigma_{k+1}$、Frobenius误差$(\sum_{i>k}\sigma_i^2)^{1/2}$）；再由投影误差公式核对Frobenius误差，并在三阶例中核对$\sqrt2$与$1$。

3. 示例“对角矩阵的截断误差”（`ex:ls-truncated-svd-diagonal`）：$\operatorname{diag}(3,2,1)$截断得$\bm A_1=\operatorname{diag}(3,0,0)$、$\bm A_2=\operatorname{diag}(3,2,0)$，残差$\operatorname{diag}(0,2,1)$与$\operatorname{diag}(0,0,1)$，平方误差$5,1$、谱范数误差$2,1$，与误差公式一致，并分别等于只保留$\bm e_1$的坐标直线与最佳坐标平面的损失。

###### paragraph：为什么还要比较全部候选

1. 区分两种误差的含义，指出这只是一个构造的误差，尚需比较全部候选；Frobenius情形可用化归与迹极值，谱范数因$\lVert\bm M\rVert_2\leq\lVert\bm M\rVert_{\mathrm F}$不能由Frobenius下界推出，需另证。

2. 说明谱范数下界的想法（候选的核与前$k+1$个右奇异方向相交），并以$\operatorname{diag}(3,2,1)$、$k=1$与秩一候选$\left[\begin{smallmatrix}3&2&0\\0&0&0\\0&0&0\end{smallmatrix}\right]$按元素演示：核与$\operatorname{span}\{\bm e_1,\bm e_2\}$交于$(2,-3,0)^\top/\sqrt{13}$，在此$(\bm A-\bm X)\bm x=\bm A\bm x$，长度$\sqrt{72/13}\approx2.353\geq\sigma_2=2$。

3. Eckart--Young--Mirsky定理（`thm:ls-best-low-rank`）：式`eq:matrix-analysis-best-rank-k-spectral`与`eq:matrix-analysis-best-rank-k-frobenius`，对$0\leq k<r$，秩不超过$k$的矩阵中谱范数最小误差为$\sigma_{k+1}$、Frobenius最小误差为$(\sum_{i>k}\sigma_i^2)^{1/2}$，均由$\bm A_k$达到。证明第一段说明只需证明下界，$k=0$直接成立。

4. 证明第二段（Frobenius情形）：把$\bm X$的列空间补成$k$维子空间，由投影误差引理与迹极值定理得下界。

5. 证明第三段（谱范数情形）：由秩零度定理$\dim\ker\bm X\geq d-k$，与$\operatorname{span}\{\bm v_1,\ldots,\bm v_{k+1}\}$有非零公共单位向量，在该向量上式`eq:ls-spectral-lower-bound`给出$\lVert(\bm A-\bm X)\bm x\rVert_2=\lVert\bm A\bm x\rVert_2\geq\sigma_{k+1}$。

6. 在秩一候选上核对式`eq:ls-spectral-lower-bound`的中间量$9\cdot\tfrac4{13}+4\cdot\tfrac9{13}=\tfrac{72}{13}\geq4$。

7. 注明结论最早由Eckart与Young给出（引用`eckart1936`），说明定理覆盖任意候选：Frobenius情形靠化归归入子空间，谱范数情形靠候选矩阵的核；两种最小误差都由舍弃的奇异值决定。

#### 18.3.4 最优解的唯一性

###### paragraph：Frobenius情形

1. 由三阶例的$\bm A_2$与$\bm A_2'$指出最小误差唯一而最优矩阵未必唯一，提出何时唯一的问题；在$1\leq k<r$下，答案由迹极值取等条件与截断处的奇异值间隙决定。

2. 定理“Frobenius最佳逼近的唯一性”（`thm:ls-best-low-rank-uniqueness`）：$\sigma_k>\sigma_{k+1}$时$\bm A_k$是唯一最优解。证明：两个不等号都须取等，第一个给出$\bm X=\bm Y\bm Y^\top\bm A$，第二个由迹极值取等条件给出$\operatorname{range}(\bm Y)=\operatorname{span}\{\bm u_1,\ldots,\bm u_k\}$，同一子空间的投影相同，故$\bm X=\bm A_k$。

3. 说明$k=1$时间隙条件就是18.2.3的唯一性条件，有间隙时前$k$个左奇异方向的张成是特征空间之和，$\bm A_k$与所选奇异向量无关；三阶例中$k=1$有间隙、$\bm A_1$唯一，$k=2$无间隙、定理不适用。

4. 截断跨过相等奇异值时唯一性失败：$\operatorname{diag}(2,1,1)$、$k=2$时$\operatorname{diag}(2,1,0)$与$\operatorname{diag}(2,0,1)$的残差与平方误差$1=\sigma_3^2$，以及三阶例中的$\bm A_2$与$\bm A_2'$。

###### paragraph：谱范数情形

1. 谱范数最优解即使有间隙也不唯一：先证明对角矩阵的谱范数是对角元绝对值的最大者，再取$\operatorname{diag}(3,2,1)$、$k=1$，$\operatorname{diag}(t,0,0)$的误差$\max(\lvert3-t\rvert,2)$在$1\leq t\leq5$时都达到最小值$2$（如$t=2$时残差$\operatorname{diag}(1,2,1)$）；对比同一族的Frobenius平方误差$(3-t)^2+5$只在$t=3$取最小；解释谱范数只看最坏方向。

###### paragraph：边界情形与适用范围

1. 回指边界情形$k=0$与$k\geq r$的最优矩阵，不需要间隙判据。

2. 说明本节最优性的两个前提（允许集合为全部秩不超过$k$的矩阵、误差为谱范数或Frobenius范数）；非负、稀疏约束或一般逐元素加权误差使投影分解失效，截断SVD一般不再最优，并预告下一节处理可化归的一类加权误差。

### 18.4 加权逼近与广义Rayleigh商

1. 指出前两节在规定单位方向和计算误差时都用欧氏长度；坐标单位或重要性不同时改用第3章的加权内积，这会同时改变单位方向的规定与误差的比较标准。

2. 说明本节先由加权长度得到广义Rayleigh商及其极值，再研究行、列权重可分离的低秩逼近，其最佳方向正由广义Rayleigh商选出；并说明卷九谱划分用度加权长度与广义Rayleigh商作离散划分的松弛（跨卷引用卷九“谱划分”章）。

#### 18.4.1 广义Rayleigh商的极值

1. 用$\bm S=\operatorname{diag}(4,1)$、$\bm B=\operatorname{diag}(9,1)$比较两个坐标方向：加权约束$9x_1^2+x_2^2=1$下$\pm\bm e_1/3$给出$4/9$、$\pm\bm e_2$给出$1$，欧氏约束下最优的方向现在不再最优。

2. 说明改变长度标准会改变答案，仍须比较全部可行方向；给出广义Rayleigh商的定义$R_{\bm S,\bm B}(\bm x)=\bm x^\top\bm S\bm x/\bm x^\top\bm B\bm x$（`def:ls-generalized-rayleigh-quotient`，式`eq:ls-generalized-rayleigh-quotient`，$\bm B$对称正定），并说明分母为正、缩放不变，极值等价于约束$\bm x^\top\bm B\bm x=1$上的二次型极值。

3. 说明$\bm B=\bm I$时回到普通Rayleigh商，两者的差别只在于用哪种长度规定单位输入。

##### 18.4.1.1 主要思想

###### paragraph：把加权长度换成欧氏长度

1. 先在开头的例子中把约束写成$(3x_1)^2+x_2^2$，令$z_1=3x_1$、$z_2=x_2$，约束成为欧氏单位圆，二次型成为$\frac49z_1^2+z_2^2$，问题变为$\operatorname{diag}(4/9,1)$的普通Rayleigh商问题。

2. 一般地取上三角$\bm L$、令$\bm z=\bm L\bm x$，按元素展开二阶的$z_1^2+z_2^2$，看出中间矩阵正是$\bm L^\top\bm L$，所以$\bm B=\bm L^\top\bm L$时加权长度在新坐标中是欧氏长度；由定理`thm:ls-gram-factor`这样的可逆$\bm L$总存在。

###### paragraph：化为普通Rayleigh商

1. 代入$\bm x=\bm L^{-1}\bm z$，得$\bm C=\bm L^{-\top}\bm S\bm L^{-1}$对称且$R_{\bm S,\bm B}(\bm x)=R_{\bm C}(\bm L\bm x)$；说明化归只用Gram因子与换元，不需要平方根、多元微分或Lagrange乘子；开头的例子中$\bm C=\operatorname{diag}(4/9,1)$。

###### paragraph：换回原坐标

1. 把$\bm C$的特征对换回原坐标，推出$\bm S\bm v=\mu\bm B\bm v$，并证明反向对应，得到一一对应。

2. 定义广义特征值、广义特征向量与广义特征问题（`def:matrix-analysis-generalized-eigenvalue`，式`eq:matrix-analysis-generalized-eigenproblem`）。

3. 由$\det(\bm S-\mu\bm B)=(\det\bm L)^2\det(\bm C-\mu\bm I)$说明广义特征值就是$\bm C$的特征值，不依赖$\bm L$的选取；由$\bm C$对称，广义特征值全为实数、按重数共$d$个，排为$\mu_1\geq\cdots\geq\mu_d$。

###### paragraph：极值与最优方向

1. 定理“广义Rayleigh商的极值”（`thm:ls-generalized-rayleigh-extremal`）：$\mu_d\leq R_{\bm S,\bm B}\leq\mu_1$，取等当且仅当相应广义特征方程成立，约束$\bm x^\top\bm B\bm x=1$上的最优解是加权单位化的广义特征向量。证明由$R_{\bm S,\bm B}(\bm x)=R_{\bm C}(\bm z)$得两端的界，由Rayleigh--Ritz的取等条件与一一对应得取等刻画及可达性，再翻译回加权约束上的二次型最大、最小值。

###### paragraph：$\bm B$正交的广义特征向量

1. 定理“$\bm B$正交的广义特征向量”（`thm:ls-generalized-eigen-b-orthogonal`）：存在$\bm v_i$使$\bm S\bm v_i=\mu_i\bm B\bm v_i$、$\bm v_i^\top\bm B\bm v_j=\delta_{i,j}$，即$\bm V^\top\bm B\bm V=\bm I$、$\bm V^\top\bm S\bm V=\bm M$；证明取$\bm V=\bm L^{-1}\bm Z$并逐式验证。

2. 说明在$\bm B$正交的广义特征向量坐标下，$\bm x^\top\bm B\bm x=\sum a_i^2$、$\bm x^\top\bm S\bm x=\sum\mu_ia_i^2$，广义Rayleigh商再次是特征值的加权平均；中间广义特征值可对$\bm C$用第9章的Courant--Fischer原理再换回原坐标。

###### paragraph：用开头的例子核对

1. 示例“加权约束下的最优方向”（`ex:ls-generalized-rayleigh-diagonal`）：由$\bm L=\operatorname{diag}(3,1)$、$\bm C=\operatorname{diag}(4/9,1)$得最大方向$\pm\bm e_2$、最小方向$\pm\bm e_1/3$；核验加权单位约束、广义特征方程（特征值$1$与$4/9$）及$\bm B$正交；再由约束消去$x_2^2$得$\bm x^\top\bm S\bm x=1-5x_1^2\in[4/9,1]$，直接比较全部可行方向，结果一致；对照欧氏约束下最大方向为$\bm e_1$，加权约束使沿$\bm e_1$的可行向量缩短为$\bm e_1/3$，最大方向换成$\bm e_2$。

##### 18.4.1.2 算法实现

1. 说明一般情形按化归顺序计算：求Gram因子、形成$\bm C$、谱分解、换回原坐标，换元用因子分解与三角求解完成，不显式形成$\bm L^{-1}$；输入对称$\bm S$与对称正定$\bm B$，输出广义特征值与加权单位的广义特征向量。

2. 示例“按三角求解的步骤计算”（`ex:matrix-approximation-generalized-cholesky`）：给出设定$\bm S=\operatorname{diag}(2,3)$、$\bm B=\operatorname{diag}(4,1)$，求加权约束下的最大值、最小值与最优方向。

###### paragraph：变量

1. 以列表列出：上三角Gram因子$\bm L$（$\bm B=\bm L^\top\bm L$），中间矩阵$\bm W=\bm L^{-\top}\bm S$，化归后的$\bm C=\bm W\bm L^{-1}$，$\bm C$的特征对$(\mu_i,\bm z_i)$，原坐标中的广义特征向量$\bm v_i$。

###### paragraph：输入与预处理

1. 用第12章的Cholesky分解得$\bm B=\bm G\bm G^\top$，取$\bm L=\bm G^\top$；开方量不为正说明$\bm B$不正定，化归不能继续，停止并报告；例中$\bm L=\operatorname{diag}(2,1)$。

###### paragraph：计算步骤

1. 依次：形成$\bm W$，对$\bm L^\top\bm W=\bm S$逐列前代，例中$\bm W=\operatorname{diag}(1,3)$；形成$\bm C$，对$\bm L^\top\bm C^\top=\bm W^\top$再作前代，舍入时取$(\bm C+\bm C^\top)/2$保持对称，例中$\bm C=\operatorname{diag}(1/2,3)$；对$\bm C$作谱分解，例中$\mu_1=3,\bm z_1=\bm e_2$与$\mu_2=1/2,\bm z_2=\bm e_1$；回代$\bm L\bm v_i=\bm z_i$换回原坐标，$\bm v_i$自动满足$\bm v_i^\top\bm B\bm v_i=1$，例中$\bm v_1=(0,1)^\top$、$\bm v_2=(1/2,0)^\top$；核验广义特征残差与加权长度，例中残差为零、加权长度为$1$。

2. 最终结果：单独一行写出加权约束下最大值$3$在$\pm(0,1)^\top$、最小值$1/2$在$\pm(1/2,0)^\top$；与欧氏Rayleigh商（最大$3$、最小$2$）比较，加权没有改变最优直线而改变了最小值；结合前例说明长度标准可能改变方向，也可能只改变最优值。

##### 18.4.1.3 算法分析

###### paragraph：运算量

1. 形成$\bm C$的代价为$O(d^3)$，主要代价在对称特征值计算（本书不分析算法）；即使只要两端特征对也须先换元，因为$\bm S$的特征向量一般不是广义特征向量。

###### paragraph：为什么不改求普通特征问题

1. 改求$\bm B^{-1}\bm S\bm v=\mu\bm v$：由$\bm B^{-1}\bm S=\bm L^{-1}\bm C\bm L$，它与$\bm C$相似、特征值相同，但一般不对称。

2. 用$\bm S=\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$、$\bm B=\operatorname{diag}(2,1)$算出$\bm B^{-1}\bm S$的特征多项式$\mu^2-3\mu+\frac32$、特征值$(3\pm\sqrt3)/2$与特征向量$(1,1\pm\sqrt3)^\top$，验证它们$\bm B$正交而欧氏不正交（内积$-1$），说明不能对$\bm B^{-1}\bm S$套用谱定理；前两个二维例子只是特殊情形。

###### paragraph：正定性的作用

1. 化归依赖$\bm B$正定：半正定奇异时分母可为零，不定时可为负，且不存在可逆$\bm L$使$\bm B=\bm L^\top\bm L$（否则$\bm B$正定）。

2. 以$\bm S=\bm I$、$\bm B=\operatorname{diag}(1,0)$为例说明约束问题可以没有极值，更一般的广义特征问题不在此展开。

#### 18.4.2 加权低秩逼近

##### 18.4.2.1 主要思想

###### paragraph：加权误差

1. 以行表示不同的量、列表示不同样本为背景，给定对称正定行权重$\bm\Omega_{\mathrm r}$与列权重$\bm\Omega_{\mathrm c}$，定义加权误差$E(\bm X)=\operatorname{tr}((\bm A-\bm X)^\top\bm\Omega_{\mathrm r}(\bm A-\bm X)\bm\Omega_{\mathrm c})$，引入术语“加权低秩逼近”，权重为单位矩阵时回到Frobenius误差。

2. 对角权重时由$\bm M^\top\bm\Omega_{\mathrm r}\bm M$的对角元推出逐元素加权$\sum_{i,j}\omega_i\tau_j(a_{i,j}-x_{i,j})^2$，并按元素写出$m=d=2$的四项，说明这类误差包含权重能分离为行、列因子乘积的逐元素加权。

###### paragraph：化为普通的Frobenius误差

1. 对角情形取$\bm K=\operatorname{diag}(\sqrt{\omega_i})$、$\bm N=\operatorname{diag}(\sqrt{\tau_j})$，按元素看出$(\bm K\bm M\bm N)_{i,j}^2=\omega_i\tau_jm_{i,j}^2$。

2. 一般情形取Gram因子$\bm\Omega_{\mathrm r}=\bm K^\top\bm K$、$\bm\Omega_{\mathrm c}=\bm N\bm N^\top$，由迹的循环性证明$E(\bm X)=\lVert\bm K(\bm A-\bm X)\bm N\rVert_{\mathrm F}^2$。

###### paragraph：秩约束不变

1. 令$\widetilde{\bm A}=\bm K\bm A\bm N$、$\bm Z=\bm K\bm X\bm N$，用列空间包含关系双向证明$\operatorname{rank}\bm Z=\operatorname{rank}\bm X$；$\bm X\mapsto\bm K\bm X\bm N$是秩不超过$k$的矩阵集合上的一一映射，原问题等价于对$\widetilde{\bm A}$作普通低秩逼近。

2. 定理“可分离权重下的最佳低秩逼近”（`thm:matrix-approximation-weighted-low-rank`）：最小加权误差为$\sum_{i>k}\tilde\sigma_i^2$，由$\bm X_k=\bm K^{-1}\widetilde{\bm A}_k\bm N^{-1}$达到，$\tilde\sigma_k>\tilde\sigma_{k+1}$时唯一；证明由一一映射与Eckart--Young--Mirsky定理及唯一性定理得到。

###### paragraph：最佳方向由广义Rayleigh商选出

1. 只设行权重、取$k=1$，把变换后的单位方向$\bm z$换为原坐标方向$\bm w=\bm K^{-1}\bm z$，单位约束变为$\bm w^\top\bm\Omega_{\mathrm r}\bm w=1$。

2. 计算保留量为$\bm w^\top\bm\Omega_{\mathrm r}\bm A\bm A^\top\bm\Omega_{\mathrm r}\bm w$，由定理`thm:ls-generalized-rayleigh-extremal`得最佳方向是广义特征问题$\bm\Omega_{\mathrm r}\bm A\bm A^\top\bm\Omega_{\mathrm r}\bm w=\mu\bm\Omega_{\mathrm r}\bm w$的最大特征向量，化归中的$\bm C=\widetilde{\bm A}\widetilde{\bm A}^\top$，最大广义特征值为$\tilde\sigma_1^2$。

3. 求出最优系数$\bm A^\top\bm\Omega_{\mathrm r}\bm w$与近似$\bm w\bm w^\top\bm\Omega_{\mathrm r}\bm A$，验证$\bm P=\bm w\bm w^\top\bm\Omega_{\mathrm r}$满足$\bm P^2=\bm P$且$\bm\Omega_{\mathrm r}\bm P$对称，是关于$\bm\Omega_{\mathrm r}$内积的正交投影，说明加权秩一逼近与第18.2节平行。

4. 指出决定保留方向的是$\widetilde{\bm A}$的奇异值，直接截断$\bm A$一般不再加权最优。

##### 18.4.2.2 算法实现

1. 说明按化归顺序计算：求两个权重的三角因子、形成$\widetilde{\bm A}$并截断SVD、用三角求解还原；输入$\bm A$、两个对称正定权重与目标秩$k$，输出秩不超过$k$的$\bm X_k$。

2. 示例“行加权改变保留的方向”（`ex:matrix-approximation-weighted-low-rank`）：给出设定$\bm A=\operatorname{diag}(3,2)$、$\bm\Omega_{\mathrm r}=\operatorname{diag}(1,4)$、$\bm\Omega_{\mathrm c}=\bm I$、$k=1$，求加权最优的秩一近似并与直接截断比较。

###### paragraph：变量

1. 以列表列出：上三角因子$\bm K$（$\bm\Omega_{\mathrm r}=\bm K^\top\bm K$），下三角Cholesky因子$\bm N$（$\bm\Omega_{\mathrm c}=\bm N\bm N^\top$），变换后的$\widetilde{\bm A}$，截断SVD的$\widetilde{\bm U}_k,\widetilde{\bm\Sigma}_k,\widetilde{\bm V}_k$，还原后的左右因子$\bm F,\bm H$，原坐标近似$\bm X_k$。

###### paragraph：输入与预处理

1. 用第12章的Cholesky分解得$\bm\Omega_{\mathrm r}=\bm G\bm G^\top$、取$\bm K=\bm G^\top$，$\bm N$直接取$\bm\Omega_{\mathrm c}$的Cholesky因子；对角权重直接开方；开方量不为正时停止并报告；例中$\bm K=\operatorname{diag}(1,2)$、$\bm N=\bm I$。

###### paragraph：计算步骤

1. 依次：形成$\widetilde{\bm A}=\bm K\bm A\bm N$，例中$\operatorname{diag}(3,4)$；截断SVD，例中$\tilde\sigma_1=4$（方向$\bm e_2$）、$\tilde\sigma_2=3$（方向$\bm e_1$），$\widetilde{\bm A}_1=\operatorname{diag}(0,4)$，排在前面的是$\bm A$中较短的方向；还原时回代$\bm K\bm F=\widetilde{\bm U}_k$、$\bm N^\top\bm H=\widetilde{\bm V}_k$，以因子形式$\bm X_k=\bm F\widetilde{\bm\Sigma}_k\bm H^\top$保证秩，也可先解$\bm N^\top\bm Y^\top=\widetilde{\bm A}_k^\top$再解$\bm K\bm X_k=\bm Y$，例中$\bm F=\bm e_2/2$、$\bm H=\bm e_2$、$\bm X_1=\operatorname{diag}(0,2)$；核验秩与加权残差，例中$E(\bm X_1)=9=\tilde\sigma_2^2$，与下界相等。

2. 最终结果：单独一行写出$\bm X_1=\operatorname{diag}(0,2)$、$E(\bm X_1)=9$；直接截断$\bm A$的$\operatorname{diag}(3,0)$加权误差为$16$；再用广义Rayleigh商核对，$\bm\Omega_{\mathrm r}\bm A\bm A^\top\bm\Omega_{\mathrm r}=\operatorname{diag}(9,64)$，广义特征值为$9$与$16$，$\bm w=\bm e_2/2$正是还原中的$\bm F$，系数$(0,4)^\top$，重建即$\bm X_1$；解释第二行权重使最优近似保留第二个坐标方向。

##### 18.4.2.3 算法分析

###### paragraph：运算量与正定性

1. 给出代价$O(m^3+d^3+md(m+d))$加一次SVD；说明权重必须正定，零权重使因子不可逆、还原无法进行。

###### paragraph：还原步骤的误差放大

1. 逐列、逐行应用谱范数的定义，推出$\lVert\bm K^{-1}\bm\Delta\bm N^{-1}\rVert_{\mathrm F}\leq\lVert\bm K^{-1}\rVert_2\lVert\bm\Delta\rVert_{\mathrm F}\lVert\bm N^{-1}\rVert_2$；例中两个谱范数都是$1$，不放大误差；行权重改为$\operatorname{diag}(1,10^{-4})$时$\bm K^{-1}=\operatorname{diag}(1,100)$，放大倍数可达$100$；权重悬殊时须直接计算加权残差并与理论下界比较来核验。

###### paragraph：权重不能分离时

1. 证明化归的必要条件：若加权误差等于逐元素加权，取$\bm A-\bm X=\bm e_i\bm e_j^\top$得权重必为行因子与列因子之积，满足$w_{i,j}w_{k,l}=w_{i,l}w_{k,j}$；以$\left[\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\right]$和缺失元素（零权重）为反例。

2. 说明这些情形没有截断SVD式的闭式解，需迭代优化并另论全局最优性，跨卷引用卷五“优化问题与解”章。

### 18.5 正交约束下的矩阵逼近

1. 把约束换成正交性：在全部正交矩阵中找离方阵$\bm A$最近的一个（Frobenius范数），解释为最接近给定作用的保长作用，以含噪旋转的修正为例。

2. 说明正交矩阵集合不是子空间、不由秩描述，投影化归不能沿用；第8章已构造极分解正交因子，本节证明其最优性并讨论$\det\bm R=1$的约束。

#### 18.5.1 正交逼近的最优解

##### 18.5.1.1 主要思想

###### paragraph：化为迹最大

1. 写出问题$\min_{\bm R^\top\bm R=\bm I}\lVert\bm A-\bm R\rVert_{\mathrm F}^2$，用迹内积展开平方误差；由$\lVert\bm R\rVert_{\mathrm F}^2=\operatorname{tr}\bm I=d$得$\lVert\bm A-\bm R\rVert_{\mathrm F}^2=\lVert\bm A\rVert_{\mathrm F}^2+d-2\operatorname{tr}(\bm R^\top\bm A)$，距离最小等价于迹最大。

2. 以$d=2$按元素写出$\operatorname{tr}(\bm R^\top\bm A)=\sum r_{i,j}a_{i,j}$，说明目标关于$\bm R$线性，与第18.3.1节关于$\bm Y$二次的迹不同，迹极值界不能搬用。

###### paragraph：换到奇异向量坐标

1. 代入SVD，令$\bm Z=\bm U^\top\bm R\bm V$，说明$\bm Z$取遍全部正交矩阵，由迹的循环性得$\operatorname{tr}(\bm R^\top\bm A)=\operatorname{tr}(\bm Z^\top\bm\Sigma)$。

2. 以$d=2$按元素写出$\bm Z^\top\bm\Sigma$（第$i$列乘$\sigma_i$），迹为$\sigma_1z_{1,1}+\sigma_2z_{2,2}$；一般地目标为$\sum_i\sigma_iz_{i,i}$，只用到对角元。

###### paragraph：由SVD读出最优正交矩阵

1. 由单位列向量得$z_{i,i}\leq1$、奇异值非负，逐项求和得上界$\sum_i\sigma_i$；$\bm Z=\bm I$取到上界，单独一行写出$\bm R_\star=\bm U\bm V^\top$，说明最优矩阵由两个正交因子相乘读出。

2. 定理“最佳正交逼近”（`thm:ls-best-orthogonal-approximation`）：$\operatorname{tr}(\bm R^\top\bm A)\leq\sum_i\sigma_i$，$\bm U\bm V^\top$取等，最小平方误差为$\sum_i(\sigma_i-1)^2$，由极分解正交因子达到，可逆时唯一为$\bm W=\bm A(\bm A^\top\bm A)^{-1/2}$。证明第一段由迹的循环性与$|z_{i,i}|\leq1$得上界及取等。

3. 证明第二段：代入$\lVert\bm A\rVert_{\mathrm F}^2=\sum_i\sigma_i^2$得最小值，并由一般极分解定理确认$\bm U\bm V^\top$是正交因子。

4. 证明第三段：可逆时每个$z_{i,i}=1$迫使$\bm Z=\bm I$，由可逆极分解定理得最优解就是$\bm W$。

###### paragraph：误差的含义

1. 引入术语“最佳正交逼近”。

2. 解释误差逐个比较奇异值与$1$，单独一行写出$\bm U\bm\Sigma\bm V^\top\to\bm U\bm I\bm V^\top$：保留两组奇异方向，只把$\bm\Sigma$换成$\bm I$。

###### paragraph：奇异情形

1. 任一极分解的正交因子都使迹达到上界$\operatorname{tr}\bm H=\sum_i\sigma_i$。

2. 取等只约束前$r$列，单独一行写出$\bm Z=\operatorname{diag}(\bm I_r,\bm Z')$。

3. $\bm U\bm Z$只改变乘零的后$d-r$列，仍给出SVD与极分解，说明最优解恰是全部极分解正交因子，自由度对应零伸缩方向上的正交补全。

##### 18.5.1.2 算法实现

1. 说明计算只需一次SVD、两个正交因子相乘并核验，不限制行列式符号。

2. 示例“二阶正交逼近”（`ex:matrix-approximation-orthogonal-two-by-two`）：给出设定$\bm A=\left[\begin{smallmatrix}0&-2\\3&0\end{smallmatrix}\right]$，求最近的正交矩阵，计算由随后的逐步执行给出。

###### paragraph：变量

1. 以列表列出：给定方阵$\bm A$，完整方阵SVD的$\bm U,\bm\Sigma,\bm V$，最优正交矩阵$\bm R_\star$，残差$\bm E=\bm A-\bm R_\star$。

###### paragraph：输入与预处理

1. 输入方阵并求完整方阵SVD；例中$\bm A^\top\bm A=\operatorname{diag}(9,4)$，取$\bm V=\bm I$、$\sigma_1=3$、$\sigma_2=2$，由$\bm u_i=\bm A\bm v_i/\sigma_i$得$\bm u_1=(0,1)^\top$、$\bm u_2=(-1,0)^\top$，写出$\bm U,\bm\Sigma,\bm V$并逐列核对$\bm U\bm\Sigma=\bm A$。

###### paragraph：计算步骤

1. 相乘得最优正交矩阵$\bm R_\star=\bm U\bm V^\top$；例中$\bm R_\star=\bm U=\left[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right]$。

2. 核验正交性（有限精度下看$\lVert\bm R_\star^\top\bm R_\star-\bm I\rVert_{\mathrm F}$）；例中按元素相乘得$\bm I$。

3. 核验误差：残差$\left[\begin{smallmatrix}0&-1\\2&0\end{smallmatrix}\right]$，平方误差$5=(3-1)^2+(2-1)^2$。

4. 记录行列式符号：例中$\det\bm R_\star=1$，与$\det\bm A=6>0$同号。

5. 最终结果：单独一行写出$\bm R_\star$，为逆时针$90$度旋转，满足正交性且平方误差等于理论下界$5$。

6. 用第8章贯穿例$\bm A=\left[\begin{smallmatrix}0&-1\\3&0\end{smallmatrix}\right]$核对：$\bm A^\top\bm A=\operatorname{diag}(9,1)$，奇异值$3,1$，正交因子$\bm W=\left[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right]$，最小平方误差$4$与直接计算$\bm A-\bm W=\left[\begin{smallmatrix}0&0\\2&0\end{smallmatrix}\right]$一致；说明含噪旋转估计常用这一步。

##### 18.5.1.3 算法分析

###### paragraph：计算代价

1. 一次SVD加一次矩阵乘法（约$d^3$次乘法），SVD代价不作分析。

###### paragraph：与SVD选取的关系

1. 可逆时最优解与SVD选取无关；奇异时不同SVD给出的最优解只在零奇异值方向上不同、误差相同。

###### paragraph：行列式的符号

1. 最优解在全部正交矩阵中取得，可逆时$\det\bm W$与$\det\bm A$同号，$\det\bm A<0$时含反射，要求旋转时需要下一小节的修正。

#### 18.5.2 旋转约束下的逼近

补充图解：反射与旋转的几何区别。虚线为原三角形，实色为变换后的位置；(a)关于纵轴反射，行列式为$-1$；(b)绕两轴交点旋转$180^\circ$，行列式为$1$。两幅图仅用于说明允许变换集合的不同，不表示给定矩阵的最优逼近结果。

##### 18.5.2.1 主要思想

###### paragraph：增加行列式约束

1. 以刚体姿态估计为例说明要求结果是旋转（正交且$\det\bm R=1$），单独一行写出带行列式约束的迹最大问题。

2. 记$s=\det(\bm U\bm V^\top)=\det\bm U\det\bm V=\pm1$；$s=1$时无约束解已是旋转，约束不起作用。

###### paragraph：$s=-1$时原来的上界取不到

1. $s=-1$时对任一旋转$\bm Z=\bm U^\top\bm R\bm V$正交且$\det\bm Z=-1$，$\bm Z=\bm I$不再可取。

2. 以$d=2$按元素写出行列式为$-1$的正交矩阵$\left[\begin{smallmatrix}\cos\theta&\sin\theta\\\sin\theta&-\cos\theta\end{smallmatrix}\right]$，目标为$(\sigma_1-\sigma_2)\cos\theta$，在$\theta=0$即$\bm Z=\operatorname{diag}(1,-1)$处最大，比无约束上界少$2\sigma_2$；此时$\operatorname{tr}\bm Z=0=d-2$。

3. 引理“行列式为负的正交矩阵的迹”（`lem:matrix-approximation-reflection-trace`）：$\det\bm Z=-1$的正交矩阵有特征值$-1$且$\operatorname{tr}\bm Z\leq d-2$。证明第一段由$\bm Z+\bm I=\bm Z(\bm I+\bm Z)^\top$得$\det(\bm Z+\bm I)=0$，取单位向量$\bm Z\bm x=-\bm x$，并推出$\bm Z^\top\bm x=-\bm x$。

4. 证明第二段：$d=1$直接成立；$d\geq2$时把$\bm x$扩充为标准正交基，相似变换得$\operatorname{diag}(-1,\bm Z_2)$，$\bm Z_2$对角元不超过$1$，由迹的相似不变性得$\operatorname{tr}\bm Z\leq d-2$。

5. 用特征值语言重述：特征值模为$1$，非实特征值成共轭对、实部之和不超过$2$，实特征值为$\pm1$；行列式为$-1$迫使$-1$出现奇数次，迹至多$d-2$；指出上面的证明只用实向量完成同一论证。

###### paragraph：修正最小奇异方向

1. 写出迹损失$\sum_i\sigma_i(1-z_{i,i})$，由引理缺口之和$d-\operatorname{tr}\bm Z\geq2$且权重不小于$\sigma_d$，单独一行得损失至少$\sigma_d(d-\operatorname{tr}\bm Z)\geq2\sigma_d$；缺口集中于最后一个对角元（$z_{d,d}=-1$）时取到，对应$\bm D_s=\operatorname{diag}(1,\ldots,1,s)$与$\bm R_\star=\bm U\bm D_s\bm V^\top$，$s=1$时也适用。

2. 定理“最佳旋转逼近”（`thm:matrix-approximation-best-rotation`）：对一切旋转$\operatorname{tr}(\bm R^\top\bm A)\leq\sum_{i<d}\sigma_i+s\sigma_d$，由$\bm R_\star$取到，最小平方误差为$\sum_{i<d}(\sigma_i-1)^2+(\sigma_d-s)^2$。证明第一段验证$\bm R_\star$是旋转（$\det\bm R_\star=s^2=1$）。

3. 证明第二段：$s=1$时由最佳正交逼近定理直接得到。

4. 证明第三段：$s=-1$时由引理与$1-z_{i,i}\geq0$、$\sigma_i\geq\sigma_d$，分两行写出$\sum_i\sigma_i(1-z_{i,i})\geq\sigma_d(d-\operatorname{tr}\bm Z)\geq2\sigma_d$，得上界并在$\bm Z=\bm D_s$处取等。

5. 证明第四段：代入展开式并用$s^2=1$化简得最小平方误差。

###### paragraph：修正的代价

1. 修正只发生在最小奇异方向：配对改为$\bm v_d\mapsto s\bm u_d$；把符号放在第$i$个方向迹损失$2\sigma_i$，而任何旋转损失至少$2\sigma_d$。

2. 单独一行写出$s=-1$时平方误差增加$(\sigma_d+1)^2-(\sigma_d-1)^2=4\sigma_d$；$\bm A$可逆时$s$就是$\det\bm A$的符号、与SVD选取无关。

3. $\sigma_d=0$时$s$依赖SVD选取，但修正代价为零，且两种选取给出同一个$\bm R_\star$（乘积$s\bm u_d$不变）。

###### paragraph：唯一性

1. $\bm A$可逆且$s=1$时，无约束唯一解$\bm W$是旋转，因而唯一。

2. $\sigma_{d-1}>\sigma_d$时唯一：$\sigma_d>0$、$s=-1$时取等迫使$\bm Z=\bm D_s$；$\sigma_d=0$时取$s=1$的SVD后迫使$\bm Z=\bm I$。

3. 指出最小奇异值重复且$s=-1$或秩不超过$d-2$时最优旋转可以不唯一，例子见本小节的算法分析。

##### 18.5.2.2 算法实现

1. 说明在上一小节基础上增加求符号$s$与最小奇异方向修正两步。

2. 示例“对角矩阵的旋转逼近”（`ex:matrix-approximation-rotation-diagonal`）：给出设定$\bm A=\operatorname{diag}(3,-1)$，$\det\bm A=-3<0$，求最近的旋转，计算由随后的逐步执行给出。

###### paragraph：变量

1. 以列表列出：给定方阵$\bm A$，奇异值非增排列的完整SVD$\bm U,\bm\Sigma,\bm V$，符号$s=\det\bm U\det\bm V$，修正矩阵$\bm D_s$，最优旋转$\bm R_\star$。

###### paragraph：输入与预处理

1. 输入方阵并求奇异值非增排列的完整SVD，说明修正放在最后一对方向上、排序不能省略；例中$\bm A^\top\bm A=\operatorname{diag}(9,1)$，取$\bm V=\bm I$，由$\bm u_i=\bm A\bm v_i/\sigma_i$得$\bm U=\operatorname{diag}(1,-1)$、$\bm\Sigma=\operatorname{diag}(3,1)$，核对$\bm U\bm\Sigma\bm V^\top=\bm A$。

###### paragraph：计算步骤

1. 计算符号：例中$s=-1$；对照无约束解$\bm U\bm V^\top=\operatorname{diag}(1,-1)$为关于横轴的反射，平方误差$4=(3-1)^2+(1-1)^2$。

2. 构造修正矩阵：例中$\bm D_s=\operatorname{diag}(1,-1)$。

3. 相乘得最优旋转$\bm R_\star=\bm U\bm D_s\bm V^\top$：例中$\bm R_\star=\bm I$。

4. 核验正交性、行列式与误差公式：例中残差$\operatorname{diag}(2,-2)$，平方误差$8=(3-1)^2+(1+1)^2$，比无约束多$4=4\sigma_2$。

5. 最终结果：单独一行写出$\bm R_\star=\bm I$，平方误差$8$。

6. 独立核对：参数化全部二阶旋转，按元素得$\operatorname{tr}(\bm R^\top\bm A)=2\cos\theta$，只在$\theta=0$处取最大值$2=\sigma_1-\sigma_2$，确认$\bm I$是唯一最优旋转，与$\sigma_1>\sigma_2$时的唯一性一致。

##### 18.5.2.3 算法分析

###### paragraph：计算代价

1. 额外工作只是两个行列式与一次对角缩放，主要代价仍是SVD，是否修正完全由$s$决定。

###### paragraph：最优旋转不唯一的情形

1. $\bm A=\operatorname{diag}(1,-1)$：奇异值重复、$s=-1$，所有旋转的迹都为零、误差平方都为$4$（与公式一致），最优旋转有无穷多个；$\bm A=\bm0$说明秩不超过$d-2$时的自由度。

###### paragraph：接近奇异时的敏感性

1. 最小奇异值接近零时$s$对扰动敏感、最优旋转可能跳变，但两种符号误差只差$4\sigma_d$，最优误差连续变化；此时应报告最优误差而不把旋转当作稳定估计。

### 18.6 本章小结

1. 回应章首问题，概括全章路线：写清约束与误差、在固定表示中选最优系数、再选方向或子空间或正交因子，SVD把最优解写成具体矩阵。

2. 总结秩一逼近：投影系数与保留量，Rayleigh商介于两端特征值且取等于特征空间，最优秩一近似$\sigma_1\bm u_1\bm v_1^\top$及误差，唯一性条件与表示的符号自由。

3. 总结秩$k$逼近：投影重建、迹极值、Eckart--Young--Mirsky定理的两种最小误差，Frobenius唯一性条件与谱范数的非唯一性，以及结论适用的允许集合与范数范围。

4. 总结广义Rayleigh商：$\bm B$正定时经Gram因子化归，极值为广义特征值、特征向量$\bm B$正交，计算用Cholesky与三角求解而非$\bm B^{-1}\bm S$，$\bm B$不正定时化归失效。

5. 总结加权低秩逼近：可分离权重经可逆变换化归，最佳方向是广义Rayleigh商的最大特征向量；要求权重为行列因子之积，一般权重交由卷五的优化方法。

6. 总结正交逼近：迹线性化，换到奇异向量坐标后只用对角元，最优正交矩阵是极分解正交因子，误差$\sum_i(\sigma_i-1)^2$及唯一性。

7. 总结旋转逼近：单独一行写出最小奇异方向上作符号修正的$\bm R_\star$，代价$4\sigma_d$，$\sigma_d=0$时为零。

8. 说明Rayleigh商、迹极值与截断SVD作为最优性工具的职责，检验时区分逼近误差与计算误差、最优误差稳定而最优矩阵在小间隙时不稳定。

9. 区分本章截断与第17章截断求解的用途，一般逼近问题由卷五的迭代优化展开。


## 第19章 矩阵方程

正文入口：[08-matrix-equations.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/09-matrix-equations.tex)，依次输入[01-sylvester.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/09-matrix-equations/01-sylvester.tex)、[02-lyapunov.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/09-matrix-equations/02-lyapunov.tex)、[03-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/03-linear-equations-and-optimization/09-matrix-equations/03-summary.tex)。

1. 从未知量由向量变为一整张矩阵、并同时受左乘和右乘的问题进入：回指第9章证明谱隙界时遇到的“左乘对角矩阵、右乘另一对角矩阵、两项相减”的方程，以及第10章递推$\bm x_{k+1}=\bm A\bm x_k$中二次量累计能否由一个矩阵写出的问题，指出后者满足的也是左右两侧都有$\bm A$作用的方程。
2. 提出本章要回答的三个问题：这类方程何时对任意右端唯一可解；怎样在不形成巨大系数矩阵的前提下求解；对称右端的Lyapunov方程，解何时对称、何时正定，正定解又能证明什么。
3. 说明Sylvester方程一节的分工：向量化说明线性结构，可解性由两侧特征值之和决定；计算依赖第6章的实Schur形与第12章的三角回代；特征基路线更简单但受特征基非正交的误差放大限制。
4. 说明Lyapunov方程一节的分工：由离散累计引出方程，连续型作为Sylvester特例；一次Schur分解下保持对称结构逐元素递推；离散型正定解依赖第10章矩阵幂几何上界与绝对收敛级数，连续型积分证明需要矩阵指数，本章只陈述条件并给出代数检验。
5. 给出全章约定：未知矩阵记为$\bm X$，离散型写成$\bm X-\bm A^\top\bm X\bm A=\bm Q$，连续型写成$\bm A^\top\bm X+\bm X\bm A=-\bm Q$；各算法最后都在原方程中计算残差作检验，Schur路线的正交变换保证原坐标与新坐标残差相同。

### 19.1 Sylvester方程

1. 概述本节路线：Sylvester方程是矩阵空间上的线性方程，存在唯一性由两侧系数的特征值给出；计算用正交Schur变换化为准三角形后逐块回代，可对角化时也可换到特征基逐元素相除；两条路线都不形成Kronecker系数矩阵。

#### 19.1.1 矩阵方程的线性算子表示

1. 定义矩阵方程，并区分单侧方程$\bm A\bm X=\bm C$（即共用系数的多右端线性方程）与双侧方程$\bm A\bm X\bm B=\bm C$（$\bm A$作用于列、$\bm B$作用于行，两侧可逆时可依次左乘$\bm A^{-1}$、右乘$\bm B^{-1}$）。
2. 定义Sylvester方程$\bm A\bm X+\bm X\bm B=\bm C$，写明$\bm A\in\mathbb R^{m\times m}$、$\bm B\in\mathbb R^{d\times d}$、$\bm C,\bm X\in\mathbb R^{m\times d}$，并说明$\bm A$的阶数对应$\bm X$的行数、$\bm B$的阶数对应列数。
3. 说明两项相加后不能分别“除以”系数：即使$\bm A$可逆，左乘$\bm A^{-1}$后未知量仍出现在两项中，因而必须把左边整体看成一个映射。
4. 由分配律说明$\mathcal L(\bm X)=\bm A\bm X+\bm X\bm B$是$\mathbb R^{m\times d}$上的线性映射；用第1章的恒等式$\operatorname{vec}(\bm A\bm X\bm B)=(\bm B^\top\otimes\bm A)\operatorname{vec}\bm X$，把两项分别看成$\bm A\bm X\bm I_d$与$\bm I_m\bm X\bm B$，得到向量化方程$(\bm I_d\otimes\bm A+\bm B^\top\otimes\bm I_m)\operatorname{vec}\bm X=\operatorname{vec}\bm C$。
5. 记系数矩阵为$\bm K$，说明一般线性方程判据都适用、小例子可用LU核验；再按$(md)^2$个元素和约$\tfrac23(md)^3$次运算（$m=d=100$时$10^8$个元素）说明向量化只用于理解结构和判断可解性，大规模求解应保留矩阵形状。

#### 19.1.2 可解性与唯一性条件

1. 对单侧方程沿用列空间判据$\operatorname{rank}[\bm A\ \bm C]=\operatorname{rank}(\bm A)$；双侧方程用向量化方程的增广秩判据，两侧可逆时唯一解为$\bm A^{-1}\bm C\bm B^{-1}$，任一侧秩亏时可能无解或沿零空间不唯一。
2. 用对角情形说明Sylvester方程不能逐侧处理：$\bm A=\operatorname{diag}(\lambda_i)$、$\bm B=\operatorname{diag}(\mu_j)$时方程按元素分解为$(\lambda_i+\mu_j)x_{i,j}=c_{i,j}$，分母非零时$x_{i,j}=c_{i,j}/(\lambda_i+\mu_j)$。
3. 分析谱和为零的位置：$c_{i,j}\neq0$时无解、$c_{i,j}=0$时该元任取，由此指出决定可解性的是$\bm A$与$-\bm B$的特征值是否重合，而非两侧各自是否可逆；一般实矩阵要在复数域中检查，并引入记号$\operatorname{spec}$。
4. 图：以$\bm A=\operatorname{diag}(1,2)$与$\bm B=\operatorname{diag}(-3,-4)$在实轴上示意谱分离，$\{1,2\}$与$\{3,4\}$不相交、最近相距$1$，四个分母都不为零。
5. 定理（Sylvester方程的唯一可解性）：对任意右端唯一可解当且仅当$\operatorname{spec}(\bm A)\cap\operatorname{spec}(-\bm B)=\varnothing$，即任一对特征值之和非零。
6. 证明第一段：由秩零度定理，唯一可解等价于齐次方程只有零解、即$\det\bm K\neq0$；行列式在实、复数域中相同，故可在复数域讨论。
7. 证明第二段（必要性）：若$\bm A\bm u=\lambda\bm u$、$\bm B^\top\bm w=-\lambda\bm w$，则$\bm X=\bm u\bm w^\top\neq\bm0$满足齐次方程。
8. 证明第三段（充分性）：由$\bm A\bm X=\bm X(-\bm B)$得$p(\bm A)\bm X=\bm X\,p(-\bm B)$；取$p$为$\bm A$的特征多项式，Cayley--Hamilton定理给出$p(\bm A)=\bm0$，而谱分离使$p(-\bm B)$可逆，故$\bm X=\bm0$。
9. 用$\bm A=\bm0,\bm B=\bm I$（不可逆却唯一可解）与$1\times1$的$\bm A=2,\bm B=-2$（都可逆却退化）说明条件与各自可逆性无关。
10. 指出谱不相交只回答唯一性、不回答敏感度：最小谱和接近零时误差放大，矩阵远离正规时即使谱和远离零也可能敏感，并预告特征基一小节给出原因。

#### 19.1.3 Schur分解法

1. 引入Bartels--Stewart算法，说明其思路与三角方程组相同：正交相似化为准上三角形后逐个回代；设谱条件成立，并预告变换、回代次序、二阶块、算法步骤、算例与分析的顺序。

###### paragraph：主要思想：正交变换到准三角形

1. 对两个系数作实Schur分解$\bm A=\bm U\bm T\bm U^\top$、$\bm B=\bm V\bm S\bm V^\top$，说明对角块为一阶或二阶、这一步与右端无关。
2. 把分解代入原方程，左乘$\bm U^\top$、右乘$\bm V$，令$\bm Y=\bm U^\top\bm X\bm V$、$\bm D=\bm U^\top\bm C\bm V$，得到$\bm T\bm Y+\bm Y\bm S=\bm D$；由相似性说明新方程仍满足谱条件，并指出正交变换保持Frobenius残差，所以新坐标中解得准确时原坐标残差不被放大。

###### paragraph：主要思想：上三角情形的回代次序

1. 设$\bm T,\bm S$上三角，展开$(i,j)$元得$(t_{i,i}+s_{j,j})y_{i,j}=d_{i,j}-\sum_{k>i}t_{i,k}y_{k,j}-\sum_{\ell<j}y_{i,\ell}s_{\ell,j}$；由右端依赖（同列更靠下、同行更靠左）推出“列从左到右、每列行从下到上”的次序，除数由谱条件非零。
2. 给出等价的整列形式$(\bm T+s_{j,j}\bm I)\bm y_j=\bm d_j-\sum_{\ell<j}s_{\ell,j}\bm y_\ell$，说明每列是一个上三角回代，并结合图说明$\bm S$第$j$列对角线以上元素把已求出的列带入右端、对角元并入当前系数。
3. 图：以$j=3$展示$\bm S$第$j$列的元素角色、$\bm Y$的列由左到右求出，以及当前列从最后一行向上回代。

###### paragraph：主要思想：二阶对角块的局部系统

1. 含二阶块时按对角块分块，写出$\bm T_{I,I}\bm Y_{I,J}+\bm Y_{I,J}\bm S_{J,J}$等于$\bm D_{I,J}$减去同块列更靠下的块与更靠左块列的贡献，由此得到按块列从左到右、每块列从下到上的次序。
2. 说明局部方程至多四个未知数，其向量化系数为$\bm I\otimes\bm T_{I,I}+\bm S_{J,J}^\top\otimes\bm I$，只在局部形成Kronecker系数；对角块的特征值是原系数的特征值，故局部方程满足谱条件、唯一可解。

###### paragraph：算法实现

1. 列出三个步骤：两个Schur分解并变换右端；按块次序扣除已知贡献并解局部方程；恢复$\bm X=\bm U\bm Y\bm V^\top$并在原方程中计算残差，浮点下其Frobenius范数等于新坐标残差。
2. 说明局部系数接近奇异时的处理：数值软件引入缩放因子$\sigma\in(0,1]$求解$\bm T\bm Y+\bm Y\bm S=\sigma\bm D$并对小分母报警，使用者应把$\sigma<1$或警告视为方程接近不可解的信号。
3. 示例（Schur形方程的逐元素回代）：$\bm T=\bigl[\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr]$、$\bm S=\bigl[\begin{smallmatrix}4&1\\0&5\end{smallmatrix}\bigr]$、$\bm D=\bigl[\begin{smallmatrix}11&21\\21&35\end{smallmatrix}\bigr]$，谱和$5,6,7,8$；依次算$y_{2,1}=21/7=3$、$y_{1,1}=(11-6)/5=1$、$y_{2,2}=(35-3)/8=4$、$y_{1,2}=(21-8-1)/6=2$，代回$\bm T\bm Y+\bm Y\bm S$核验全部四个元素，并指出次序颠倒时右端含未知元。
4. 过渡说明上例跳过了Schur分解，下一例从一般系数出发。
5. 示例（Bartels--Stewart求解一个二阶方程）第一段：$\bm A=\bigl[\begin{smallmatrix}-2&3\\-4&5\end{smallmatrix}\bigr]$特征值$2,1$，$\bm B$已上三角；由特征向量$(3,4)^\top$取$\bm U$，得$\bm T=\bigl[\begin{smallmatrix}2&7\\0&1\end{smallmatrix}\bigr]$、$\bm D=\bigl[\begin{smallmatrix}-1&24\\-2&3\end{smallmatrix}\bigr]$。
6. 示例第二段：按列回代得$\bm y_1=(2,-1)^\top$、第二列右端$(22,4)^\top$并得$\bm y_2=(3,1)^\top$，变回$\bm X=\bigl[\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\bigr]$，代回原方程残差为零。

###### paragraph：算法分析：正确性

1. 说明要把“每步可进行”和“按次序算出的块满足块等式”合成正确性与残差检验的依据。
2. 定理（Bartels--Stewart算法的正确性）：局部方程按次序均唯一可解；算出的$\bm Y$与$\bm X=\bm U\bm Y\bm V^\top$分别是变换后与原方程的唯一解；任一近似解在原、新坐标中的Frobenius残差相等。
3. 证明三段：由$\bm A\bm Z+\bm Z\bm B-\bm C=\bm U(\bm T\bm W+\bm W\bm S-\bm D)\bm V^\top$得残差等式；由准三角矩阵特征值为对角块特征值之并得局部可解；由块等式合成整体方程并用唯一可解性定理得唯一性。

###### paragraph：算法分析：计算代价

1. 给出两次Schur分解约$25m^3+25d^3$次、变换与还原约$2(m^2d+md^2)$次、回代约$m^2d+md^2$次、存储$O(m^2+d^2+md)$；$m=d=100$时约$6\times10^7$次，对比向量化稠密LU约$7\times10^{11}$次与$10^8$个存储；多右端时分解只做一次。

#### 19.1.4 特征基下的求解

1. 设$\bm A=\bm P\bm\Lambda\bm P^{-1}$、$\bm B=\bm R\bm M\bm R^{-1}$，说明换到特征基可化为对角情形，代价是换基矩阵一般不正交。

###### paragraph：主要思想：换到特征基

1. 令$\bm Y=\bm P^{-1}\bm X\bm R$、$\bm D=\bm P^{-1}\bm C\bm R$，推得$\bm\Lambda\bm Y+\bm Y\bm M=\bm D$与逐元素方程$(\lambda_i+\mu_j)y_{i,j}=d_{i,j}$；谱和为零时区分$d_{i,j}\neq0$的无解与$d_{i,j}=0$的自由变量，并强调检查的是变换后的$d_{i,j}$。

###### paragraph：主要思想：恢复原未知量

1. 给出恢复公式$\bm X=\bm P\bm Y\bm R^{-1}$，说明非正交换基可能把误差放大$\kappa_2(\bm P)\kappa_2(\bm R)$量级，因此要检查特征基条件数；复特征值时全程复数运算并舍去舍入虚部。

###### paragraph：算法实现

1. 列出四步：核验特征基可逆且条件可接受，否则改用Schur路线而不直接求逆；用LU求解$\bm P\bm Z=\bm C$再右乘$\bm R$得$\bm D$；逐项检查谱和并相除；先算$\bm P\bm Y$再求解$\bm X\bm R=\bm W$，最后计算原残差。
2. 示例（对角系数下的逐元素相除与零谱和）第一段：$\bm A=\operatorname{diag}(1,2)$、$\bm B=\operatorname{diag}(3,4)$、$\bm C=\bigl[\begin{smallmatrix}4&10\\15&24\end{smallmatrix}\bigr]$，谱和$4,5,5,6$，依次相除得$\bm X=\bigl[\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr]$并代回核验。
3. 示例第二段：改$\bm B=\operatorname{diag}(3,-2)$使右下谱和为零、其余为$4,-1,5$；$c_{2,2}=24$时无解，$c_{2,2}=0$时其余三元唯一确定而$x_{2,2}$任取，解集为一条直线。
4. 过渡说明对角系数无须换基，下一例使用非正交特征基。
5. 示例（特征基下的逐元素求解）第一段：$\bm A=\bigl[\begin{smallmatrix}1&1\\0&2\end{smallmatrix}\bigr]$、$\bm B=\bigl[\begin{smallmatrix}3&1\\0&4\end{smallmatrix}\bigr]$共享特征向量$(1,0)^\top,(1,1)^\top$，分母$4,5,5,6$；算得$\bm D=\bigl[\begin{smallmatrix}-8&-17\\15&36\end{smallmatrix}\bigr]$、$\bm Y$、$\bm X=\bigl[\begin{smallmatrix}1&8/5\\3&3\end{smallmatrix}\bigr]$，代回残差为零。
6. 示例第二段：把$\bm B$的$(1,1)$元改为$-2$使$\lambda_2+\mu_1=0$，说明特征基随之改变，第$(2,1)$个方程变为$0\cdot y_{2,1}=d_{2,1}$，按变换后右端区分无解与不唯一。

###### paragraph：算法分析：数值敏感度

1. 由$\lVert\bm Y\rVert_{\mathrm F}\leq\lVert\bm D\rVert_{\mathrm F}/\delta_{\min}$与左右乘的范数界，得到$\lVert\bm X\rVert_{\mathrm F}\leq\kappa_2(\bm P)\kappa_2(\bm R)\lVert\bm C\rVert_{\mathrm F}/\delta_{\min}$，说明斜基下谱和远离零不独自保证良好条件。
2. 用$\bm A=\bigl[\begin{smallmatrix}1&1\\0&1+\epsilon\end{smallmatrix}\bigr]$的近平行特征向量说明$\kappa_2(\bm P)\geq1/\epsilon$、中间量约为$1/\epsilon$，换基本身放大舍入误差。
3. 对实对称系数由谱定理得正交特征基、公式可靠；一般情形即使可对角化也宜用正交Schur变换。

### 19.2 Lyapunov方程

1. 从第10章的递推与二次量累计问题进入，提出能否用一个矩阵写出全部累计量，说明本节由此引出Lyapunov方程并把连续型作为Sylvester特例。
2. 给出全节写法：离散型$\bm X-\bm A^\top\bm X\bm A=\bm Q$、连续型$\bm A^\top\bm X+\bm X\bm A=-\bm Q$，两者都是左乘$\bm A^\top$、右乘$\bm A$，因而一次Schur分解、回代次序相同；离散正定性只用矩阵幂与级数，连续型积分证明需要矩阵指数，本节只陈述条件并作代数检验。

#### 19.2.1 离散型与连续型方程

1. 设$\bm Q\succeq0$、$\bm x_k=\bm A^k\bm x_0$，把前$N+1$步累计量写成$\bm x_0^\top\bm X_N\bm x_0$，由和式拆出首项得递推$\bm X_{N+1}=\bm Q+\bm A^\top\bm X_N\bm A$，取极限得离散型Lyapunov方程，并解释为矩阵空间上固定更新的不动点方程。
2. 从逐步角度解读：对解$\bm X$，二次量$\bm x^\top\bm X\bm x$每走一步恰减少$\bm x_k^\top\bm Q\bm x_k$，求和即回到累计量。
3. 指出离散型不是换系数的Sylvester方程，向量化系数为$\bm I-\bm A^\top\otimes\bm A^\top$，唯一可解条件由特征值乘积决定，并说明下面用两侧系数不同的一般形式陈述以供局部块使用。
4. 定理（离散型方程的唯一可解性）：$\bm Y-\bm G^\top\bm Y\bm H=\bm E$对任意右端唯一可解当且仅当$\bm G$、$\bm H$的任意特征值乘积$\lambda\mu\neq1$；取$\bm G=\bm H=\bm A$得离散Lyapunov方程的条件$\lambda\lambda'\neq1$，右端对称时解对称。
5. 证明第一段：系数矩阵为实矩阵，归结为复数域中齐次方程是否只有零解。
6. 证明第二段（必要性）：取$\bm G^\top\bm w=\lambda\bm w$、$\bm H^\top\bm v=\mu\bm v$，$\bm Y=\bm w\bm v^\top$满足$\bm G^\top\bm Y\bm H=\lambda\mu\bm Y=\bm Y$。
7. 证明第三段：把实Schur形的归纳搬到复数域，用酉矩阵得到上三角化$\bm G=\bm W_1\bm R_1\bm W_1^*$、$\bm H=\bm W_2\bm R_2\bm W_2^*$，并由$\bm G$为实矩阵得$\bm G^\top=\bm W_1\bm R_1^*\bm W_1^*$。
8. 证明第四段：令$\bm Z=\bm W_1^*\bm Y\bm W_2$得$\bm Z=\bm R_1^*\bm Z\bm R_2$，逐元素写出系数$1-\overline{(\bm R_1)_{i,i}}(\bm R_2)_{j,j}$（非实特征值共轭成对故仍非零）与只含$k+\ell<i+j$的右端，对$i+j$归纳得$\bm Z=\bm0$。
9. 证明第五段：特化到$\bm G=\bm H=\bm A$，并由转置与唯一性得对称解。
10. 说明$\rho(\bm A)<1$时$|\lambda\lambda'|<1$使条件自然成立，且唯一性可不经三角化直接证明，供级数论证使用。
11. 引理（谱半径小于一时的唯一性）及证明：两解之差满足$\bm X=(\bm A^\top)^k\bm X\bm A^k$，由$\bm A^k\to\bm0$得零；对称性由转置与唯一性得到。
12. 预告级数收敛与正定性在“正定解的存在条件”一小节建立。
13. 引入连续型：若状态按$\dot{\bm x}=\bm A\bm x$演化（解理论在后续卷中），由乘积求导法则二次量变化率为$\bm x^\top(\bm A^\top\bm X+\bm X\bm A)\bm x$，令其等于$-\bm x^\top\bm Q\bm x$得连续型方程；说明此段只解释来历，代数上它是左系数$\bm A^\top$、右系数$\bm A$、右端$-\bm Q$的Sylvester方程。
14. 定理（连续型Lyapunov方程的唯一可解性）：唯一可解当且仅当任意两个特征值之和非零，右端对称时解对称；证明由Sylvester定理的谱条件与转置唯一性给出。
15. 比较条件强弱：特征值实部全负是充分而非必要条件（例$\operatorname{diag}(1,2)$的谱和$2,3,4$），离散型中$\rho(\bm A)<1$亦然（例$\operatorname{diag}(2,3)$的乘积$4,6,9$）；指出这两种强化条件在正定解一小节中决定解是否正定。

补充图解：离散Lyapunov方程给出的下降量。取$\bm A=\left[\begin{smallmatrix}0.7&1\\0&0.5\end{smallmatrix}\right]$、$\bm Q=\bm I$、$\bm x_0=(0,1)^\top$，解$\bm X-\bm A^\top\bm X\bm A=\bm I$，令$V_k=\bm x_k^\top\bm X\bm x_k$。两条曲线分别除以各自初值；欧氏平方长度第一步从$1$增至$1.25$，而$V_k-V_{k+1}=\lVert\bm x_k\rVert_2^2>0$。纵轴取对数。

#### 19.2.2 对称解的计算与检验

1. 说明直接套用Sylvester算法要分别分解$\bm A$与$\bm A^\top$且不利用对称性，本小节只作一次Schur分解并只求上三角部分。

补充图解：四阶上三角Schur形中的求解次序。左：Sylvester方程$\bm T\bm Y+\bm Y\bm S=\bm D$按列从左到右、每列从下到上；右：对称Lyapunov方程中左系数为$\bm T^\top$，只求上三角部分，按列从左到右、每列从上到对角元，下三角由对称性恢复。序号表示先后，含二阶Schur块时须改为对应的块求解。

###### paragraph：主要思想：一次Schur变换

1. 由$\bm A=\bm U\bm T\bm U^\top$得$\bm A^\top=\bm U\bm T^\top\bm U^\top$，令$\bm Y=\bm U^\top\bm X\bm U$、$\bm D=\bm U^\top\bm Q\bm U$，得到$\bm T^\top\bm Y+\bm Y\bm T=-\bm D$与$\bm Y-\bm T^\top\bm Y\bm T=\bm D$；对称性化为$\bm Y=\bm Y^\top$，只需求$i\leq j$的元素。

###### paragraph：主要思想：连续型的逐元素递推

1. 按$\bm T^\top$下三角、$\bm T$上三角展开得$(t_{i,i}+t_{j,j})y_{i,j}=-d_{i,j}-\sum_{k<i}t_{k,i}y_{k,j}-\sum_{k<j}y_{i,k}t_{k,j}$；采用列从左到右、每列从上到对角元的次序，逐项核对右端元素（按对称性改写后）都已求出，除数由唯一可解条件非零。
2. 对比Sylvester算法：那里左系数上三角、每列从下向上，这里左系数是下三角的$\bm T^\top$、依赖指向同列更靠上的元素，所以不能照搬原次序。

###### paragraph：主要思想：离散型的逐元素递推

1. 展开$(\bm T^\top\bm Y\bm T)_{i,j}=\sum_{k\leq i,\ell\leq j}t_{k,i}y_{k,\ell}t_{\ell,j}$，移出$(k,\ell)=(i,j)$一项得$(1-t_{i,i}t_{j,j})y_{i,j}=d_{i,j}+\sum_{(k,\ell)\neq(i,j)}t_{k,i}y_{k,\ell}t_{\ell,j}$；按对称位置的列号$\max(k,\ell)\leq j$分情形说明同一列序只读取已求元素，除数由乘积条件非零。

###### paragraph：主要思想：整列形式与对称性

1. 写出不利用对称性时的整列形式$(\bm T^\top+t_{j,j}\bm I)\bm y_j=-\bm d_j-\sum_{\ell<j}t_{\ell,j}\bm y_\ell$与$(\bm I-t_{j,j}\bm T^\top)\bm y_j=\bm d_j+\bm T^\top\sum_{\ell<j}t_{\ell,j}\bm y_\ell$，每列下三角前代；说明只求上三角时右端会含当前列正在求的未知量，因此应逐元素推进，未知量由$d^2$减为$d(d+1)/2$。

###### paragraph：主要思想：二阶块与局部算子

1. 写出含二阶块时连续型局部算子$\bm T_{I,I}^\top\bm Y_{I,J}+\bm Y_{I,J}\bm T_{J,J}$与离散型局部算子$\bm Y_{I,J}-\bm T_{I,I}^\top\bm Y_{I,J}\bm T_{J,J}$的块递推；局部至多四个未知数，对角块只存三个对称未知量；局部可逆性分别由Sylvester定理与离散型唯一可解定理给出，标量的分母非零推广为局部算子可逆，并保留缩放与条件警告。

###### paragraph：算法实现

1. 列出四步：检查$\bm Q$对称；计算Schur分解与$\bm D$；按块列从左到右、每块列从上到对角块解局部方程并镜像填回；恢复$\bm X=\bm U\bm Y\bm U^\top$并检查原残差、对称性与所需正定性。
2. 强调检验须在原方程中进行，不能只查小系统，也不能把非对称误差强行平均后宣布成功。
3. 示例（连续型方程的逐元素递推）：$\bm A=\bigl[\begin{smallmatrix}-1&1\\0&-2\end{smallmatrix}\bigr]$、$\bm Q=\bm I$，记$\bm X=\bigl[\begin{smallmatrix}p&q\\q&r\end{smallmatrix}\bigr]$，按次序由$-2p=-1$、$p-3q=0$、$2q-4r=-1$得$p=1/2,q=1/6,r=1/3$；代回原方程并由$\det\bm X=5/36>0$判定正定。
4. 示例（离散型方程的逐元素递推）第一段：$\bm A=\bigl[\begin{smallmatrix}1/2&1/4\\0&1/2\end{smallmatrix}\bigr]$、$\bm Q=\bm I$，分母均为$3/4$；由$\tfrac34p=1$、$\tfrac34q=p/8$、$\tfrac34r=1+p/16+q/4$（列出三项来源）得$p=4/3,q=2/9,r=41/27$。
5. 示例第二段：逐元素算出$\bm A^\top\bm X\bm A$的三个元素$1/3,2/9,14/27$，验证$\bm X-\bm A^\top\bm X\bm A=\bm I$，并由$\det\bm X=160/81>0$判定正定。
6. 过渡说明下一例$\bm A$有零特征值，可用累计量核对。
7. 示例（离散型方程的递推与累计量）：$\bm A=\bigl[\begin{smallmatrix}1/2&1\\0&0\end{smallmatrix}\bigr]$、$\bm Q=\bm I$，按逐元素公式得$y_{1,1}=4/3$、$y_{1,2}=2/3$、$y_{2,2}=7/3$，验证残差为零；再从$\bm x_0=(0,1)^\top$出发累加$1+1+\tfrac14+\cdots=7/3$核对$x_{2,2}$。
8. 过渡说明前三例$\bm A$已是上三角，下一例需要Schur变换。
9. 示例（连续型方程的Schur求解）：$\bm A=\bigl[\begin{smallmatrix}0&3\\-1&-4\end{smallmatrix}\bigr]$特征值$-3,-1$，由特征向量$(1,-1)^\top$取$\bm U$，得$\bm T=\bigl[\begin{smallmatrix}-3&4\\0&-1\end{smallmatrix}\bigr]$、$\bm D=\bigl[\begin{smallmatrix}6&-4\\-4&6\end{smallmatrix}\bigr]$；逐元素得$\bm Y=\operatorname{diag}(1,3)$，变回$\bm X=\bigl[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr]$，并核验$\bm A^\top\bm X+\bm X\bm A=-\operatorname{diag}(2,10)$。

###### paragraph：算法分析：对称性、残差与正定性检验

1. 说明三项检验各自回答的问题：对称化只消除舍入不对称，方程是否解对要看原方程相对残差是否在机器精度的若干倍内。
2. 说明Cholesky检验正定的浮点含义：成功只说明一个与$\bm X$相差舍入量级的矩阵正定，只有$\lambda_{\min}(\bm X)$明显大于舍入量级时才能判定；否则结合残差容差和问题本身的正定保证；以连续型Schur例的Cholesky对角元$\sqrt2,\sqrt{3/2}$为例。

###### paragraph：算法分析：计算代价

1. Schur分解约$25d^3$次，变换与恢复$O(d^3)$；连续型递推总量$O(d^3)$，离散型逐元素直接求双重和为$O(d^4)$，按列保存部分乘积可降到$O(d^3)$；总代价$O(d^3)$、存储$O(d^2)$。

#### 19.2.3 正定解的存在条件

1. 说明上一小节的算法不保证正定，回到离散累计：$\rho(\bm A)<1$时解就是累计量的极限，正定性可逐项读出。
2. 定理（离散型Lyapunov方程的级数解）：$\rho(\bm A)<1$、$\bm Q$对称时级数$\sum_k(\bm A^\top)^k\bm Q\bm A^k$收敛且为唯一解，$\bm Q\succeq0$时解半正定，$\bm Q\succ0$时解正定。
3. 证明第一段：由矩阵幂几何上界$\lVert\bm A^k\rVert_2\leq C_rr^k$得通项被收敛几何级数控制，绝对收敛。
4. 证明第二段：$\mathcal M(\bm Y)=\bm A^\top\bm Y\bm A$连续，部分和满足$\bm X_N-\mathcal M(\bm X_N)=\bm Q-(\bm A^\top)^{N+1}\bm Q\bm A^{N+1}$，末项趋于零，取极限得方程，唯一性由引理给出。
5. 证明第三段：每项的二次型为$(\bm A^k\bm x)^\top\bm Q(\bm A^k\bm x)$，由此得半正定；$\bm Q\succ0$时首项严格为正，得正定。
6. 以标量情形$x=q/(1-a^2)$核对分母与唯一性条件中的$1-\lambda\lambda$及符号。

###### paragraph：半正定右端

1. 以只计量线性读数的$\bm Q=\bm c\bm c^\top$说明右端常奇异，级数定理只给半正定，提出是否存在整条轨迹都不被累计量察觉的非零方向。
2. 定理（半正定右端的正定条件）：$\bm x^\top\bm X\bm x=0$当且仅当$\bm Q\bm A^k\bm x=\bm0$（$k=0,\ldots,d-1$），因而$\bm X\succ0$当且仅当堆叠矩阵$[\bm Q;\bm Q\bm A;\ldots;\bm Q\bm A^{d-1}]$秩为$d$。
3. 证明第一段：级数各项非负，故为零当且仅当每项为零；用$\bm Q=\bm L\bm L^\top$说明半正定矩阵的$\bm v^\top\bm Q\bm v=0$等价于$\bm Q\bm v=\bm0$。
4. 证明第二段：由Cayley--Hamilton定理，$k\geq d$的幂是前$d$个幂的线性组合，所以只需检查$k<d$；结合$\bm X\succeq0$得正定的等价条件。
5. 指出该条件在控制理论中称为可观测性，只依赖$\bm A$与$\bm Q$的零空间结构。
6. 示例（未被累计量察觉的方向）第一段：$\bm A=\bigl[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr]$满足$\bm A^2=\bm0$，级数只有两项，$\bm A$把$\bm e_2$送到$\bm e_1$、把$\bm e_1$送到零。
7. 示例第二段：$\bm Q=\operatorname{diag}(1,0)$时$\bm X=\bm I\succ0$，$\bm e_2$方向第一步未被计量但下一步被察觉，与定理的两条零空间条件一致。
8. 示例第三段：$\bm Q=\operatorname{diag}(0,1)$时$\bm Q\bm A=\bm0$、$\bm X=\operatorname{diag}(0,1)$奇异，$\bm e_1$出发的轨迹始终不被计量；比较两种秩一右端，指出区别在于未计量方向是否被$\bm A$送入计量范围。

###### paragraph：正定解给出的谱证书

1. 说明反方向的代数事实：对称正定解本身证明谱条件，为算法输出提供证书，残差小且Cholesky可靠成功即同时检验$\bm A$的稳定性。
2. 定理（正定解给出的谱证书）：$\bm Q\succ0$、$\bm X\succ0$时，离散型方程成立推出$\rho(\bm A)<1$，连续型方程成立推出特征值实部全负。
3. 证明第一段：取复特征向量$\bm v=\bm a+\mathrm i\bm b$，说明实对称矩阵的$\bm v^*\bm M\bm v=\bm a^\top\bm M\bm a+\bm b^\top\bm M\bm b$，故$\bm v^*\bm X\bm v,\bm v^*\bm Q\bm v>0$，并用$\bm v^*\bm A^\top=\bar\lambda\bm v^*$。
4. 证明第二段：离散型得$(1-|\lambda|^2)\bm v^*\bm X\bm v=\bm v^*\bm Q\bm v>0$。
5. 证明第三段：连续型得$2\operatorname{Re}\lambda\,\bm v^*\bm X\bm v=-\bm v^*\bm Q\bm v<0$。
6. 把两个逐元素算例反向读作证书，并与三角矩阵对角元直接读出的结论对照。

###### paragraph：连续型的正定条件

1. 陈述与离散型平行的结论：特征值实部全负且$\bm Q\succ0$时唯一解正定，$\bm Q\succeq0$时半正定且正定当且仅当同样的$\bm Q\bm A^k\bm x=\bm0$（$k<d$）只有零解；唯一性已由本章定理保证，正定性需把级数换成积分$\int_0^\infty e^{t\bm A^\top}\bm Qe^{t\bm A}\,\mathrm dt$另行证明。本章未证明这一结论。
2. 说明所需工具与位置：矩阵指数的定义、导数与指数衰减见卷六“线性微分方程与系统”章，积分表示与轨迹长期稳定性的完整推导见卷九“动力系统与轨迹的长期行为”章；本章只保留条件和代数检验，算法不以它为前提。
3. 用标量方程$x=q/(2|a|)$与连续型Schur例（$\bm A$特征值$-3,-1$，$\bm Q=\operatorname{diag}(2,10)$，$\bm X$特征值$1,3$）核验陈述，并用谱证书反向确认$\bm A$稳定。

### 19.3 本章小结

1. 概括本章对象：左右作用相加的矩阵方程仍是矩阵空间上的线性算子方程，向量化说明判据适用但不宜作为大规模计算方法。
2. 回应可解性问题：Sylvester方程唯一可解当且仅当$\bm A$与$-\bm B$无公共特征值，与各自可逆性无关；谱和为零给出无解与多解，谱分离不回答敏感度，小谱和或非正交特征基会放大误差。
3. 回应计算问题：Bartels--Stewart算法的正交Schur变换、列从左到右每列从下到上的回代、二阶块局部系统与Frobenius残差不变；特征基路线只在特征基接近正交时可靠。
4. 总结Lyapunov方程的唯一可解条件（乘积不为一、和不为零）与对称性，以及一次Schur分解下列从左到右、每列从上到对角元的逐元素递推；强调原方程残差、对称化与Cholesky检验各自的作用。
5. 总结正定性：离散级数解在右端正定时正定，半正定右端时正定当且仅当不存在始终不被累计量察觉的方向；对称正定解反过来给出谱半径小于一或实部全负的代数证书。
6. 指出边界与衔接：连续型正定解本章只陈述条件并作代数检验，其矩阵指数积分证明及与轨迹长期稳定性的关系在后续演化理论中建立。

