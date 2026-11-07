# 卷二《向量、矩阵与多元微积分》：谱分析大纲

所属：卷二《向量、矩阵与多元微积分》第二部分“谱分析”。正文入口：[volume.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/volume.tex) → [part.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/02-spectral-analysis/part.tex)。本提要依据实际接入的五章正文（卷内第6—10章）组织。

本部分研究怎样选基才能看清一个给定的线性作用，再用所得表示回答两个问题：数据带误差时结果有多可靠，同一作用反复施加时最终会怎样。第6章让输入、输出共用一组基，依次讨论可逆换基的对角化、正交换基的谱定理与一般方阵的实Schur形；第7章让两端各取一组标准正交基，得到对任意矩阵成立的奇异值分解，并读出范数和秩；第8章把同一作用重组为对称伸缩与保长转向，并把沿谱运算归纳为矩阵函数。第9章先固定矩阵研究输入误差的放大，再让矩阵带误差，给出特征值、奇异值、秩与特征子空间的有限扰动界；第10章研究固定仿射更新的反复作用。Rayleigh商以及低秩、正交逼近的最优性在第三部分第17章“矩阵逼近”；沿指定方向的一阶响应与局部条件数在第四部分第22章“微分与扰动分析”。

## 部分导读（不编号）

正文：[part.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/02-spectral-analysis/part.tex)中的`\BookPartGuide`。

1. 承接第一部分“矩阵是线性映射在坐标下的记录、同一映射在不同基下有不同矩阵”，提出本部分的主线：怎样选基才能看清给定的线性作用，以及用这些表示回答误差可靠性与反复作用两个实际问题。

2. 说明前三章建立表示：特征值与谱分解一章共用一组基、寻找只被伸缩的方向，正交基下能对角化的恰是对称矩阵，一般方阵只能化为实Schur形；奇异值分解一章两端各取标准正交基，使任何矩阵化为非负对角伸缩并读出范数与秩；极分解一章重组为对称伸缩与保长转向，并归纳出矩阵函数。

3. 说明后两章使用这些表示：条件数与谱扰动一章先研究输入误差的放大，再估计矩阵带误差时特征值、奇异值、秩与特征子空间的变化，结论都是有限扰动界；线性递推一章由谱半径判断初值影响是否消失，由Neumann级数求平衡，并分析暂时放大与逐步误差的累积。

4. 列出阅读时须区分的几组概念：相似变换与两端分别换基、特征值与奇异值、谱半径与范数、输入误差与矩阵误差、有限扰动界与一阶响应；并交代Rayleigh商与低秩、正交逼近的最优性在第三部分的矩阵逼近一章，一阶响应与局部条件数在第四部分借助微分讨论。

## 第6章 特征值与谱分解

正文入口：[01-eigenvalues-and-spectral-decomposition.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/02-spectral-analysis/01-eigenvalues-and-spectral-decomposition.tex)。

1. 从第2章的相似关系$\bm B=\bm P^{-1}\bm A\bm P$（第~`sec:ls-similarity`节）进入：同一算子有许多矩阵写法，$T(x_1,x_2)=(2x_1+x_2,3x_2)$在标准基下有非零非对角元，换到只被伸缩、不被转向的两个基方向后成为对角矩阵。

2. 提出本章的表示问题：能否找到这样的方向、能找到多少，若再要求新基保持长度和夹角，矩阵最多能化到多简单；说明这几个问题依次加强对基的要求，答案也依次收窄。

3. 说明四节的分工与衔接：6.1节寻找特征向量、用特征多项式求特征值并说明其与基无关；6.2节判断特征向量何时足以组成基，此时矩阵幂化为乘方，但特征基一般不正交；6.3节要求正交换基，证明恰是实对称矩阵能这样对角化并写成谱投影之和；6.4节允许复特征值，说明正交换基只能得到实Schur形，能化为分块对角形的恰是正规矩阵。

4. 交代依赖与用途：用到第1章的矩阵运算与行列式、第2章的线性映射与相似、第3章的范数、内积、正交投影与正定矩阵；谱定理将在第7章构造SVD、第8章开方，特征值与谱半径在第7、8章分析扰动与反复作用。

### 6.1 特征值与特征向量

1. 从相似一节事先给出、再加验证的对角化基进入，指出那组基是猜出来的。

2. 说明本节的推进顺序及理由：定义只说明要找什么，系统求解需把条件改写成特征多项式的根，特征值须与基无关才是算子本身的性质，最后证明不同特征值的特征向量线性无关，为下一节组基作准备。

#### 6.1.1 线性作用中的特征方向

1. 从线性算子一般同时改变长度与方向出发，提出寻找作用后仍落在原直线上的非零向量，写出$T\bm v=\lambda\bm v$、$\bm v\neq\bm0$（式`eq:matrix-analysis-eigenpair`），定义特征值、特征向量与特征方向。

2. 说明要求非零的原因，并解释$\lambda$的大小与符号对应拉长、缩短、反向与落入核。

3. 由线性性归纳得$T^k\bm v=\lambda^k\bm v$，说明特征方向上的反复作用化为数的乘方。

4. 由坐标形式$[T]_{\mathcal B}[\bm v]_{\mathcal B}=\lambda[\bm v]_{\mathcal B}$说明特征值属于算子本身、换基只改变特征向量的坐标。

5. 反过来把方阵看作算子$\bm x\mapsto\bm A\bm x$，规定方阵的特征值与特征向量。

6. 示例`ex:ls-operator-eigenvector-check`对$\left[\begin{smallmatrix}2&1\\0&3\end{smallmatrix}\right]$直接相乘，验证$\bm e_1$与$(1,1)^\top$是特征向量、正是相似一节的新基方向，而$\bm e_2$不是；图`fig:ls-operator-eigenvectors`画出两条特征方向上的向量只变长、其他方向被转开。

7. 反例`ex:ls-rotation-no-real-eigenvector`对$90^\circ$旋转由$(1+\lambda^2)x_2=0$推出只有零解，说明并非每个算子都有实特征向量。

#### 6.1.2 特征空间与不变子空间

1. 把同一特征值的特征方向放在一起，定义特征空间$\ker(T-\lambda\operatorname{id}_V)$，由它是线性映射的核说明它是子空间。

2. 以$\bm I_2$（特征空间是整个平面）与示例`ex:ls-operator-eigenvector-check`中特征值$2$（$\bm e_1$所在直线）对照，说明特征空间的维数可以不同。

3. 定义不变子空间，说明作用可限制在其上研究，特征空间是不变子空间。

4. 证明一维不变子空间恰为特征方向；再以$90^\circ$旋转下不变而不含特征方向的整个平面说明高维不变子空间未必含特征方向，并指出它对应一对共轭复特征值（6.4节）。

#### 6.1.3 特征多项式

1. 为系统求出特征值，把条件依次改写为$\ker(\bm A-\lambda\bm I)\neq\{\bm0\}$、秩小于$n$、不可逆（第~`sec:ls-injective-surjective-invertible`节）。

2. 用行列式乘法性与古典伴随恒等式证明不可逆等价于行列式为零，得$\lambda$是特征值当且仅当$\det(\bm A-\lambda\bm I)=0$。

3. 由此解释相似一节列出的不变量$\operatorname{rank}(\bm A-c\bm I)$：使它小于$n$的$c$恰是特征值。

4. 定义首项系数为$1$的特征多项式$p_{\bm A}(z)=\det(z\bm I-\bm A)$（式`eq:matrix-analysis-characteristic-polynomial`），实特征值即其实根。

5. 由排列展开只有对角线一项含$z^n$，说明它是$n$次多项式、至多$n$个根，求出特征值后解齐次方程得特征空间。

6. 示例`ex:ls-characteristic-polynomial-two-by-two`用特征多项式重求$\left[\begin{smallmatrix}2&1\\0&3\end{smallmatrix}\right]$的特征值并说明旋转的$z^2+1$无实根；随后推广到三角矩阵的特征值是对角元。

7. 说明把矩阵代入自身的特征多项式得到零矩阵，先以示例`ex:ls-cayley-hamilton-two-by-two`核对$\bm A^2-5\bm A+6\bm I=\bm0$，再陈述Cayley--Hamilton定理`thm:ls-cayley-hamilton`；证明把古典伴随恒等式（定理`thm:ls-adjugate-identity`）用于$z\bm I-\bm A$，按$z$的幂次写出伴随矩阵$\sum z^j\bm B_j$。

8. 续证：两边按幂次比较系数，各式左乘$\bm A^j$相加，左端相邻项逐对相消、右端为$p_{\bm A}(\bm A)$；指出证明不要求先求特征值，也不要求$p_{\bm A}$有实根。

9. 陈述定理`thm:ls-power-reduction`（高次幂的降次），对$k$归纳：由Cayley--Hamilton得$\bm A^n\in\operatorname{span}\{\bm I,\ldots,\bm A^{n-1}\}$，左乘$\bm A$后把出现的$\bm A^n$再代换。

10. 作用于向量$\bm g$得$\bm A^k\bm g$属于前$n$项张成的子空间，故该子空间至多$n$维、在前$n$项后不再增大，供第18章Sylvester方程与第14章Krylov子空间方法使用。

11. 回到重根，定义代数重数与几何重数；示例`ex:ls-multiplicity-gap`以$\left[\begin{smallmatrix}0.8&1\\0&0.8\end{smallmatrix}\right]$算出代数重数$2$、几何重数$1$；一般关系留给6.2节，并引出下一小节的基无关性。

#### 6.1.4 相似变换与谱的不变性

1. 承接相似一节列出的不变量，说明本小节证明特征值、特征多项式与两种重数也是相似不变量，再由特征值读出迹与行列式，最后指出不变量只能否定相似。

###### paragraph：特征值、特征空间与特征多项式

1. 用一句话引出定理。

2. 陈述并证明定理`thm:ls-spectrum-similarity-invariance`：由$\bm B(\bm P^{-1}\bm v)=\lambda\bm P^{-1}\bm v$得特征值相同，由$\ker(\bm B-\lambda\bm I)=\bm P^{-1}\ker(\bm A-\lambda\bm I)$得几何重数相同（亦可由式`eq:ls-similarity-shifted-rank`与秩零度定理得到）。

3. 续证第二条：由$\det(\bm P^{-1}\bm M\bm P)=\det\bm M$得$p_{\bm B}=p_{\bm A}$与代数重数相同；结论是这些量可用任意基下的矩阵计算。

###### paragraph：特征多项式的系数

1. 陈述并证明定理`thm:ls-trace-det-eigenvalues`：比较常数项与$z^{n-1}$系数得$p_{\bm A}(z)=z^n-(\operatorname{tr}\bm A)z^{n-1}+\cdots+(-1)^n\det\bm A$，分解为实一次因子时$\operatorname{tr}\bm A=\sum\lambda_i$、$\det\bm A=\prod\lambda_i$；以前例核对，并指出计入复根后对每个方阵成立（6.4节）。

###### paragraph：相似不变量只能否定相似

1. 说明不变量不同可否定相似、全同却未必相似；反例`ex:ls-same-charpoly-not-similar`中$\bm I_2$与$\bm J_1=\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$特征多项式相同而几何重数为$2$与$1$，由定理知不相似。

2. 指出特征多项式相同只是相似的必要条件，比较几何重数更细但仍不充分，完整分类需要Jordan标准形，本书不展开。

#### 6.1.5 特征向量的线性无关性

1. 说明为用特征方向组成基，本小节先证明不同特征值的特征向量线性无关，再推出特征空间之和是直和。

###### paragraph：特征向量的线性无关

1. 先用“同一向量不能被乘以两个不同倍数”的直观引出，再陈述并证明定理`thm:ls-distinct-eigenvectors-independent`：取项数最少的非平凡线性依赖，作用$T-\lambda_1\operatorname{id}_V$得到更短的依赖而矛盾；推出$n$维空间上至多$n$个不同特征值。

2. 指出这一上界与特征多项式次数给出的上界一致。

###### paragraph：特征空间的直和

1. 从“各特征空间的基合在一起是否仍线性无关”引出，陈述并证明定理`thm:ls-eigenspaces-direct-sum`：非零分量是不同特征值的特征向量，由上一定理不能相加为零，故和为直和，各基合起来仍线性无关、维数相加。

2. 说明开头例子的$\bm e_1$与$(1,1)^\top$属于不同特征值，自动组成基。

3. 回顾本节：特征方向与特征值、由特征多项式求特征值、与基无关的谱不变量。

4. 续述线性无关性给出的上界与Cayley--Hamilton定理、高次幂降次，并把特征向量何时足以组成基交给下一节。

### 6.2 对角化

1. 承接上一节，说明本节考察特征向量足以组成基的情形，先看此时矩阵与矩阵幂的形式以说明这种基为何值得寻找，再给出存在条件与计算步骤。

2. 强调本节的换基矩阵只要求可逆、各列不必垂直，正交换基留给下一节。

#### 6.2.1 特征向量基下的矩阵表示

1. 由线性映射表示的列约定（第~`sec:ls-map-representation`节）说明特征基下的矩阵是对角的，每个基方向被独立伸缩。

2. 回到$\operatorname{diag}(2,3)$与相似变换图`fig:ls-similarity-change-of-basis-flow`，说明平行四边形只沿两条特征方向分别伸长。

3. 把特征向量排成$\bm V$，说明它是换基矩阵且可逆。

4. 按列读法比较$\bm A\bm V$与$\bm V\bm\Lambda$，得$\bm A\bm V=\bm V\bm\Lambda$，即$\bm V^{-1}\bm A\bm V=\bm\Lambda$、$\bm A=\bm V\bm\Lambda\bm V^{-1}$。

5. 转向定常迭代，由相邻$\bm V^{-1}\bm V$相消得$\bm A^k=\bm V\bm\Lambda^k\bm V^{-1}$（式`eq:ls-diagonalization-power`）。

6. 把三个因子从右向左读作“取特征坐标、逐个乘方、合回标准坐标”，说明它把特征方向上的$\bm A^k\bm v=\lambda^k\bm v$推广到任意初值。

7. 说明下面用一个上三角矩阵演示这种计算，给出示例`ex:ls-triangular-power`的矩阵$\left[\begin{smallmatrix}0.8&4\\0&0.5\end{smallmatrix}\right]$与任务。

8. 续例：说明直接连乘会混合两个坐标，转而找特征方向；由对角元得特征值，解出并验证特征向量$(1,0)^\top$与$(-40/3,1)^\top$。

9. 续例：把初值$(0,1)^\top$拆成$\tfrac{40}{3}\bm v_1+\bm v_2$得轨迹，并以$k=1$核对。

10. 续例：对任意初值作同样的拆分与合回，写出$\bm V$、$\bm V^{-1}$与完整的$\bm A^k$，核对第二列即前面的轨迹，迭代拆成两个独立衰减的数列，右上角的$4$只影响$\bm v_2$的形状；指出这种计算的前提是特征向量组成基。

#### 6.2.2 可对角化的判别

1. 把相似于实对角矩阵取作定义`def:ls-real-diagonalizable`并说明“实”的含义；按列读法证明对角化判据`thm:ls-diagonalization-criterion`：可对角化当且仅当有$n$个线性无关的实特征向量；再由不同特征值的特征向量线性无关推出$n$个不同实特征值是充分条件，并以$\bm I_n$说明它不必要。

###### paragraph：不能对角化的矩阵

1. 说明判据可能落空的第一种情形：$90^\circ$旋转没有实特征值（回指示例`ex:ls-rotation-no-real-eigenvector`与`ex:ls-characteristic-polynomial-two-by-two`）。

2. 第二种情形：$\bm J=\left[\begin{smallmatrix}0.8&1\\0&0.8\end{smallmatrix}\right]$有实特征值，但特征向量只有$(1,0)^\top$的倍数。

3. 示例`ex:ls-jordan-block-power`把$\bm J$写成$0.8\bm I+\bm N$，借$\bm N^2=\bm0$与可交换性二项展开得$\bm J^k$，再由相邻项之比$0.8(k+1)/k$说明右上角$k\,0.8^{k-1}$先增后减，不能由单个特征值的乘方描述。

###### paragraph：重数判据

1. 用重数说明两个反例的缺陷：$z^2+1$不能分解为实一次因子，$(z-0.8)^2$分解了但几何重数小于代数重数；指出这两种缺陷恰是全部障碍。

2. 陈述并证明定理`thm:ls-geometric-algebraic-multiplicity`（$1\leq g\leq m$且$(z-\lambda)^g$整除$p_{\bm A}$）：把特征空间的基扩充为全空间的基组成$\bm P$，$\bm P^{-1}\bm A\bm P$成分块上三角形，沿前$g$列逐次展开行列式得$p_{\bm A}(z)=(z-\lambda)^gp_{\bm C}(z)$；示例`ex:ls-multiplicity-gap`说明不等号可严格成立。

3. 以这一不等式为过渡，陈述重数判据`thm:ls-diagonalization-multiplicity`并证明充分性：重数之和为$n$，由特征空间之和是直和与定理`thm:ls-diagonalization-criterion`得可对角化。

4. 证明必要性：由相似不变性，$p_{\bm A}=p_{\bm\Lambda}$已分解，$\bm\Lambda$的两种重数相等且相似不改变几何重数。

5. 说明$n$个不同实特征值的充分条件是重数判据的特例。

#### 6.2.3 对角化的计算与用途

1. 按判据归纳“求特征值、求特征空间、组成$\bm V$与$\bm\Lambda$、核对”四步。

2. 说明四步同时指示失败：实根不够或特征空间维数不足时在第一步或第三步停止，对应上一小节的两种情形。

3. 由每期$10\%$与$20\%$的两状态转移写出$\bm x^{(k+1)}=\bm A\bm x^{(k)}$；示例`ex:ls-transition-matrix-diagonalization`对$\left[\begin{smallmatrix}0.9&0.2\\0.1&0.8\end{smallmatrix}\right]$完整执行四步：特征值$1,0.7$，特征向量$(2,1)^\top,(1,-1)^\top$，写出$\bm V^{-1}$，核对$\bm A\bm V=\bm V\bm\Lambda$并用迹与行列式快速检查。

4. 示例`ex:ls-transition-matrix-long-run`沿用该分解写出$\bm A^k$与从状态一出发的轨迹，得长期比例$(2/3,1/3)^\top$；再对一般初值求$\bm V^{-1}\bm x^{(0)}$，沿$\bm v_1$的分量恒为$1/3$、沿$\bm v_2$的分量按$0.7^k$消失，长期比例与初值无关。

5. 回顾本节的特征基、$\bm A^k=\bm V\bm\Lambda^k\bm V^{-1}$与两种判据。

6. 指出转移矩阵的两条特征方向内积为$1$、并不垂直，换基要解方程且不保持长度，引出下一节的正交对角化。

### 6.3 正交对角化

1. 承接上一节只要求$\bm V$可逆，指出特征基一般是斜基；本节保持同一分解问题但要求正交换基，依次回答哪些矩阵能正交对角化、怎样求出并检验、重特征值时哪些部分唯一。

2. 预告三个答案：实对称矩阵（谱定理）、手算路线与逐项核验、特征子空间与谱投影（并由此读出定号性）。

3. 说明一般方阵留给6.4节；本节的谱分解是第7章构造SVD与第8章开方的出发点，二次型极值与最佳低秩逼近在第17章讨论。

#### 6.3.1 实对称矩阵的谱定理

1. 说明特征方向互相垂直时换基最简单：$\bm Q^{-1}=\bm Q^\top$，新坐标是内积且长度保持（第~`sec:ls-orthonormal-bases`节），$\bm S=\bm Q\bm\Lambda\bm Q^\top$可读成“取坐标、逐个伸缩、合回去”。

2. 由转置得对称是必要条件，联系第~`sec:ls-adjoints`节的自伴映射，提出对称是否充分。

3. 交代证明思路：先找一个实特征向量、再在正交补中重复；旋转矩阵说明第一步并不平凡，对称性的作用正是排除这种情形。

4. 由代数基本定理得复根$\lambda$，说明行列式与消元在复数域中成立，故有非零复向量$\bm z$满足$\bm S\bm z=\lambda\bm z$。

5. 说明复向量需要另一种长度度量，在当前位置写出共轭的性质（$\bar zz=|z|^2$、共轭与加乘可交换），可参考卷一“实数、复数与函数”章；定义共轭内积$\bar{\bm z}^\top\bm z=\sum|z_i|^2>0$，说明它将用来证明$\lambda$为实数。

6. 说明在正交补中重复即得谱定理。

7. 陈述谱定理`thm:ls-real-symmetric-spectral`（式`eq:matrix-analysis-symmetric-eigendecomposition`与二次型展开式`eq:matrix-analysis-quadratic-spectral-form`），证明对维数归纳并说明$d=1$的情形。

8. 证明第一步：两种方式计算$\bar{\bm z}^\top\bm S\bm z$得$(\lambda-\bar\lambda)\bar{\bm z}^\top\bm z=0$，故$\lambda$为实数。

9. 证明第二步：比较$\bm z=\bm x+\mathrm i\bm y$的实部与虚部得实特征向量$\bm q_1$。

10. 证明第三步：由对称性得$\bm q_1^\perp$不变，写$\bm S\bm U=\bm U\bm S'$，对$d-1$阶对称矩阵用归纳假设并合成$\bm Q$。

11. 证明最后代入二次型说明交叉项为零。

12. 说明证明所用的是代数基本定理与对称性，复数只出现在第一步；证明不依赖二次型在单位球面上的极值，第17章反过来由谱分解读出极值；并约定特征值降序排列。

13. 补充对称性直接给出的正交关系：属于不同特征值的特征空间互相正交，下一小节计算时要用。

#### 6.3.2 谱分解的计算与核验

1. 指出谱定理的归纳证明没有直接给出计算步骤。

2. 给出手算次序：解特征多项式得全部实特征值、对每个特征值解齐次方程、在特征空间内部Gram--Schmidt正交化（定理`thm:ls-gram-schmidt`）并单位化、按同一顺序组装。

3. 解释为什么只需在特征空间内部正交化，以及维数之和为$d$由谱定理保证。

4. 给出两项核验$\bm Q^\top\bm Q=\bm I$与$\bm S\bm Q=\bm Q\bm\Lambda$及其作用。

5. 示例`ex:ls-symmetric-spectral-two-by-two`对$\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$给出题目。

6. 续例：由$(z-3)(z-1)$得特征值，求特征空间并单位化，写出$\bm Q$与$\bm\Lambda$。

7. 续例：逐项核对正交性与$\bm S\bm Q=\bm Q\bm\Lambda$及对角顺序。

8. 续例结论：$\bm S$把$(1,1)^\top$方向放大$3$倍、保持$(1,-1)^\top$方向。

9. 用这个分解解释作用的三步，并以$\bm S\bm e_1$与$\bm S\bm e_2$夹角余弦为$4/5$说明整体作用一般改变夹角，只有特征方向间的直角得以保持。

10. 限定路线的适用范围：适合手算小矩阵，大规模数值特征值算法不在本节讨论；两项核验只用矩阵乘法，对任何方法得到的因子都适用。

#### 6.3.3 特征子空间与谱投影

1. 从重特征值时$\bm Q$不唯一进入，把分解展开为秩一和并说明每项是到$\bm q_i$方向的正交投影（式`eq:linear-algebra-orthogonal-projector`），写出二阶例子的两项分解，指出单项会随选择改变、应合并同一特征值的项。

2. 引入记号：不同特征值$\mu_j$、特征空间$E_j$、$\bm Q_j$与$\bm P_j=\bm Q_j\bm Q_j^\top$。

3. 陈述谱投影定理`thm:ls-spectral-projections`的四条结论。

4. 证明第一条：代入$(\bm S-\mu_j\bm I)\bm x$得$E_j=\operatorname{range}\bm Q_j$，两两正交且维数之和为$d$。

5. 证明第二条：$\bm P_j$是正交投影，$\bm P_j\bm P_k=\bm0$，$\sum\bm P_j=\bm I$。

6. 证明第三条：合并同一特征值的项得$\bm S=\sum\mu_j\bm P_j$。

7. 证明第四条：另一组标准正交基写成$\bm Q_j'=\bm Q_j\bm R$，验证$\bm R$正交，从而投影与基的选取无关。

8. 定义谱投影，说明重根空间内的基选择只是同一投影的不同写法。

9. 示例`ex:ls-repeated-eigenspace-projection`给出$\bm S=\bm I+\bm 1\bm 1^\top$。

10. 续例：由$\bm S\bm 1=4\bm 1$与$\bm x\perp\bm 1$时$\bm S\bm x=\bm x$得特征值$4$与二重的$1$，对平面中不正交的基作Gram--Schmidt，再从另一向量出发得另一组基，两次都得$\bm P_1=\bm I-\frac13\bm 1\bm 1^\top$。

11. 续例结论：$\bm S=4\bm P_4+\bm P_1$，基可换而投影不变。

12. 转向定号性：第~`sec:ls-positive-definite`节的定义要检查全部二次型，而特征坐标下交叉项消失。

13. 陈述定理`thm:ls-symmetric-definiteness-eigenvalues`。

14. 证明必要性：取$\bm x=\bm q_i$得$\bm q_i^\top\bm S\bm q_i=\lambda_i$。

15. 证明充分性：由$\sum\lambda_ic_i^2\geq\lambda_d\lVert\bm x\rVert_2^2$得正定情形的正下界。

16. 说明判据的用途与界限：第7章由$\bm A^\top\bm A$半正定得特征值可开方；在全部单位方向中二次型何者最大最小留到第17章用Rayleigh商讨论。

17. 回顾本节：恰是对称矩阵能正交对角化，计算次序，谱投影唯一，定号性由特征值符号决定。

18. 以平面旋转与$\left[\begin{smallmatrix}0.8&4\\0&0.5\end{smallmatrix}\right]$不对称为由，引出下一节。

### 6.4 一般方阵的Schur形

1. 从前两节对角化的前提出发，指出不对称方阵可能实特征值不够（$90^\circ$旋转），也可能特征向量互不正交（夹角约$4.3^\circ$的上三角例子）。

2. 说明本节三步及其因果：以复特征值补救实特征值不足、由共轭对得到不变平面与谱半径；借这些不变平面证明实Schur形；再刻画Schur形何时分块对角（正规矩阵），并指出非正规矩阵的范数与谱半径可相差很远。

#### 6.4.1 复特征值与实不变平面

1. 借代数基本定理把特征多项式的复根都算作特征值、定义谱，说明非实根成共轭对出现。

2. 说明计入复特征值后，迹与特征值和、行列式与特征值积的关系对每个方阵成立。

3. 比较复特征向量的实部与虚部，得到$\bm A\bm u=a\bm u-b\bm w$、$\bm A\bm w=b\bm u+a\bm w$。

4. 用反证说明$\bm u,\bm w$线性无关，从而一对共轭特征值对应二维实不变子空间；在基$(\bm u,\bm w)$下作用为模长乘旋转，并提醒这组基一般不标准正交。

5. 说明$|\lambda|$是特征方向或平面坐标中的每次倍率而非一步最大放大，定义谱半径$\rho(\bm A)$，以$90^\circ$旋转（谱半径$1$）示例。

#### 6.4.2 实Schur分解

1. 说明一般方阵退而求其次化为上三角形的好处，以及实特征值不够时须允许$2\times2$对角块。

2. 陈述并证明实Schur形定理`thm:ls-real-schur`（式`eq:matrix-analysis-schur-decomposition`）：对维数归纳，每次取一维特征方向或二维不变子空间并扩充为正交矩阵，对右下角的压缩矩阵归纳（正交补未必不变）；指出数值上由Hessenberg化与带位移QR迭代求得，本卷只用其存在性，Sylvester方程的求解（第~`sec:ls-sylvester-schur`节）使用这一形式。

#### 6.4.3 正规矩阵与非正规矩阵

1. 说明本小节确定Schur形何时分块对角，并说明不满足时出现的现象。

###### paragraph：正规矩阵的分块对角形

1. 先看实对称矩阵：其Schur形仍对称、只能是对角矩阵，再次得到谱定理。

2. 由第~`sec:ls-adjoints`节的正规算子定义正规矩阵$\bm A^\top\bm A=\bm A\bm A^\top$，对称、反对称、正交矩阵均是。

3. 证明正规矩阵的Schur形分块对角：$\bm T$也正规，比较左上角块的迹得第一块行的非对角块为零，逐块递推。

4. 比较$2\times2$对角块的元素，推出每块形如$\left[\begin{smallmatrix}a&b\\-b&a\end{smallmatrix}\right]$；反过来这种分块对角形必正规，从而刻画正规矩阵。

5. 由此得$\lVert\bm A^k\rVert_2=\rho(\bm A)^k$，即正规矩阵每一步的最大放大等于谱半径。

###### paragraph：非正规矩阵

1. 由上述刻画指出非正规矩阵的Schur形不是上述分块对角形，也不能用标准正交特征向量对角化，范数可远大于谱半径；给出示例`ex:ls-nonnormal-norm-radius`的矩阵$\left[\begin{smallmatrix}0.8&4\\0&0.5\end{smallmatrix}\right]$与比较任务。

2. 续例：比较$(1,1)$元验证不正规，得$\rho=0.8$、$\lVert\bm A\rVert_2>4$、特征方向夹角约$4.3^\circ$，并用初值沿两条近乎平行的特征方向的相消解释放大；例后区分谱半径描述的长期倍率与范数描述的一步放大，指出二者分离可能伴随先放大、后衰减的瞬态（第~`sec:ls-convergence-rate-transient`节）。

3. 回顾本节：复特征值与不变平面、谱半径、实Schur形与正规矩阵。

4. 以“输入、输出用同一组基”的限制引出第7章的奇异值分解。

### 6.5 本章小结

1. 回应章首问题：答案取决于对基的要求，三种要求依次加强、能达到的形式依次退让。

2. 可逆换基：特征值是特征多项式的根且与基无关，Cayley--Hamilton定理使高次幂可由前$n$个幂表示。

3. 可对角化当且仅当有$n$个线性无关实特征向量（等价于重数条件），此时$\bm A^k=\bm V\bm\Lambda^k\bm V^{-1}$；失败的两种方式及多项式因子。

4. 正交换基：恰是对称矩阵，谱投影唯一，定号性由特征值符号决定。

5. 一般方阵：实Schur形；正规矩阵分块对角且一步放大等于谱半径，非正规矩阵的一步放大可远大于谱半径。

6. 指出特征方向不足与不正交时分别应采用的表示，并预告不正交在第9章使特征值更敏感、在第10章造成先放大后衰减。

7. 指出本章所有分解都共用一组基，引出第7章的奇异值分解。

## 第7章 奇异值分解

正文入口：[02-singular-value-decomposition.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/02-spectral-analysis/02-singular-value-decomposition.tex)。

1. 回顾第6章共用一组基时正交换基的三种结果，指出矩形矩阵的输入、输出不在同一空间，“同一组基”与特征向量都无从谈起。

2. 提出放宽后的问题：两端各取一组标准正交基时，是否任意矩阵都能得到对角形，哪些部分唯一，能读出哪些大小。

3. 说明四节的分工：7.1节说明为何两组基都须标准正交并写出目标形式；7.2节由$\bm A^\top\bm A$的谱分解构造并讨论形式与唯一性；7.3节在奇异坐标中比较输出长度读出范数与秩；7.4节说明核验与几何解释。

4. 交代依赖与边界：只用谱定理与定号性判据、标准正交基与矩阵范数；最佳低秩近似与Rayleigh商的极值性质在第17章，第8章用本章处理奇异与矩形情形的极分解。

### 7.1 输入与输出的正交坐标

1. 回忆两端分别换基时矩阵变为$\bm U^{-1}\bm A\bm V$（第~`sec:ls-map-representation`节），相似变换是$\bm U=\bm V$的特例。

2. 说明两端只要求可逆时自由度过大：取核的基扩充为输入基、其余像扩充为输出基，证明像线性无关后得$\left[\begin{smallmatrix}\bm I_r&\bm0\\\bm0&\bm0\end{smallmatrix}\right]$，这一形式只记录秩，长度信息被吸收。

3. 因此要求$\bm U$、$\bm V$正交，写出目标$\bm U^\top\bm A\bm V=\bm\Sigma$，逐列即$\bm A\bm v_i=\sigma_i\bm u_i$、$\sigma_i\geq0$，多出的输入基向量映到零。

4. 说明伸缩倍数可取非负（把$\bm u_i$变号），并指出正交矩阵的行列式为$\pm1$，“转向”可以包含反射。

5. 与特征分解的要求对照：它对矩形矩阵、不能对角化与非正规方阵都有意义；对称矩阵取$\sigma_i=|\lambda_i|$、负特征值处输出方向反号即满足要求，半正定时两组基相同。

### 7.2 奇异值分解的构造

1. 先倒推所求方向应满足的条件：由$\lVert\bm A\bm x\rVert_2^2=\sum\sigma_i^2c_i^2$与二次型展开式比较，看出$\bm v_i$应是$\bm A^\top\bm A$的特征向量、$\sigma_i^2$是对应特征值。

2. 构造输入方向：$\bm A^\top\bm A$对称半正定，由谱定理与定号性判据取标准正交特征基、特征值降序非负，正特征值开方得$\sigma_i$，其余$\bm v_j$满足$\bm A\bm v_j=\bm0$。

3. 构造输出方向：令$\bm u_i=\bm A\bm v_i/\sigma_i$并验证标准正交，再扩充为$\mathbb R^m$的标准正交基，说明这一步处理零奇异值。

4. 把任意$\bm x$按$\bm v_i$展开，写出秩一和式$\bm A=\sum_{i\leq r}\sigma_i\bm u_i\bm v_i^\top$（式`eq:matrix-analysis-svd-rank-one-sum`）。

5. 由和式读出值域由$\bm u_1,\ldots,\bm u_r$张成、核由$\bm v_{r+1},\ldots,\bm v_d$张成，从而$r=\operatorname{rank}\bm A$。

6. 陈述SVD存在定理`thm:ls-svd-existence`。

7. 说明$\bm\Sigma$与$\bm A$同形、“对角”的含义。

8. 给出奇异值分解、奇异值与左右奇异向量的定义`def:matrix-analysis-svd`（式`eq:matrix-analysis-svd`）。

9. 用图`fig:ls-svd-construction`以$\left[\begin{smallmatrix}2&0.5\\0.5&1\end{smallmatrix}\right]$复述三步构造。

10. 补出输出端的对称关系（式`eq:ls-svd-transpose-relation`）：$\bm A^\top\bm u_i=\sigma_i\bm v_i$，$i>r$时$\bm A^\top\bm u_i=\bm0$，$\bm u_i$构成$\bm A\bm A^\top$的标准正交特征基，两个Gram矩阵有相同的正特征值。

11. 提醒构造路线只用于证明存在性，数值计算问题在7.4节说明。

#### 7.2.1 奇异值分解的形式

1. 说明完整分解给出两端全部正交方向（核与值域的正交补），三个因子的形状。

2. 定义薄奇异值分解$\bm A=\bm U_p\bm\Sigma_p\bm V_p^\top$（$p=\min(m,d)$），说明它删去$\bm\Sigma$中全零的行或列及相应列，并分高矩阵与宽矩阵说明删去哪些列。

3. 给出只保留正奇异值的秩分解形式$\bm A=\bm U_r\bm\Sigma_r\bm V_r^\top$及各因子形状，即秩一和式的矩阵写法。

4. 比较三种写法：区别在于是否保留零伸缩的方向，秩分解的因子只是列标准正交；强调三者都是精确表示，截断近似在第17章讨论。

#### 7.2.2 奇异值分解的唯一性

1. 指出构造中的两处选择（特征基与输出端补全），提出哪些部分由$\bm A$唯一决定。

2. 证明奇异值唯一：任一分解给出$\bm A^\top\bm A=\bm V(\bm\Sigma^\top\bm\Sigma)\bm V^\top$，由相似不变性（定理`thm:ls-spectrum-similarity-invariance`）得$\sigma_i^2$连同重数是$\bm A^\top\bm A$的特征值。

3. 由$\bm A^\top\bm A$只依赖$\bm A$得奇异值与分解的选取无关。

4. 举出奇异向量可变的例子：一对$\bm u_i,\bm v_i$同时变号；$\bm I_2=\bm R\bm I_2\bm R^\top$，而两端不能独立换（$\bm R_1\bm I_2\bm R_2^\top=\bm I_2$迫使$\bm R_1=\bm R_2$）。

5. 陈述唯一性范围定理`thm:svd-uniqueness`：按正奇异值分组的$\bm V_\sigma$、$\bm U_\sigma$的列空间分别是$\ker(\bm A^\top\bm A-\sigma^2\bm I)$与$\ker(\bm A\bm A^\top-\sigma^2\bm I)$且$\bm U_\sigma=\bm A\bm V_\sigma/\sigma$，$\bm V_0$、$\bm U_0$的列空间是$\ker\bm A$与$\operatorname{range}(\bm A)^\perp$；另一分解的同组因子只差同一个正交矩阵$\bm R_\sigma$；反过来这些替换仍给出SVD；每个$\sigma\bm U_\sigma\bm V_\sigma^\top$唯一。证明第一条前半由逐列关系与谱投影定理第一条得到。

6. 续证第一条后半：由维数说明$\bm V_0$、$\bm U_0$分别是核与值域正交补的基。

7. 证明第二条：同一子空间的两组标准正交基相差正交矩阵，再由$\bm U'_\sigma=\bm A\bm V'_\sigma/\sigma$得左侧相差同一个矩阵。

8. 证明第三条：分组和式不含$\bm V_0$、$\bm U_0$，替换不改变乘积且保持正交性，同时右乘$\bm R_\sigma$不改变$\bm U_\sigma\bm V_\sigma^\top$。

9. 总结：奇异值与各正奇异值的左右奇异子空间唯一，同一奇异值内部两组基须一起旋转，零奇异值的两部分可独立选取；奇异值互不相同时只差公共符号；并与谱投影的情形类比。

### 7.3 奇异值与矩阵范数

1. 指出第3章定义了Frobenius范数与谱范数却未给谱范数算法，SVD把问题化为比较坐标平方和。

2. 把零伸缩也计入（$i>\min(m,d)$时$\sigma_i=0$），在奇异坐标中写出$\lVert\bm A\bm x\rVert_2^2=\sum\sigma_i^2c_i^2$与$\lVert\bm x\rVert_2^2=\sum c_i^2$（式`eq:svd-output-length`）。

3. 由加权和得$\sigma_d\lVert\bm x\rVert_2\leq\lVert\bm A\bm x\rVert_2\leq\sigma_1\lVert\bm x\rVert_2$，在$\bm v_1$、$\bm v_d$取等，强调只比较坐标平方和、不涉及极值原理。

4. 读出$\lVert\bm A\rVert_2=\sigma_1$（式`eq:matrix-analysis-spectral-norm`），由迹的循环性得$\lVert\bm A\rVert_{\mathrm F}^2=\sum\sigma_i^2$（式`eq:matrix-analysis-frobenius-norm`），秩等于正奇异值个数，并给出$\lVert\bm A\rVert_2\leq\lVert\bm A\rVert_{\mathrm F}\leq\sqrt r\lVert\bm A\rVert_2$。

5. 说明秩亏时下界为零不提供信息，应在核的正交补上谈最弱放大；满列秩时正交补是整个空间，可逆时逆矩阵把伸缩倒过来。

6. 陈述定理`thm:ls-svd-singular-value-norms`并证明前两条：在$\operatorname{span}\{\bm v_1,\ldots,\bm v_r\}$上由式`eq:svd-output-length`得$\lVert\bm A\bm x\rVert_2\geq\sigma_r\lVert\bm x\rVert_2$，满列秩时得最小值$\sigma_d>0$。

7. 证明第三条：验证$\bm A^{-1}=\sum\sigma_i^{-1}\bm v_i\bm u_i^\top$并读作$\bm A^{-1}$的SVD，得$\lVert\bm A^{-1}\rVert_2=1/\sigma_d$（式`eq:ls-svd-inverse-norm`）。

8. 解释用途：最小奇异值越小，逆矩阵放大输出误差越厉害，最大与最小奇异值之比就是第~`sec:ls-matrix-condition-number`节的条件数。

9. 说明$r<d$时只能在核的正交补上谈最弱放大；第~`sec:linear-algebra-homogeneous-estimation`节齐次最小二乘的最优解就是$\bm v_d$。

10. 指出本节只比较单个输入，在$k$维子空间中挑选保留能量最多者是第17章用Rayleigh商与迹极值处理的问题。

### 7.4 分解的核验与几何解释

1. 说明本节先给检查项目与完整算例，再用单位球的像解释三个因子，最后说明数值计算中的检查。

###### paragraph：因子的核验

1. 列出三项检查（两组正交性、$\bm\Sigma$非负降序、$\bm A\bm V=\bm U\bm\Sigma$），说明三项成立即得$\bm A=\bm U\bm\Sigma\bm V^\top$。

2. 说明正交性不能省略（任意$\bm A=\bm B\bm C$都可伪装成乘积形式），$\bm A^\top\bm U=\bm V\bm\Sigma^\top$可作附加检查。

3. 示例`ex:svd-two-by-two-check`给出$\bm A=\left[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\right]$。

4. 续例：$\bm A^\top\bm A=\left[\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\right]$的特征值$45,5$与特征向量，得$\sigma_1=3\sqrt5$、$\sigma_2=\sqrt5$。

5. 续例：由$\bm u_i=\bm A\bm v_i/\sigma_i$得$\bm u_1=(1,3)^\top/\sqrt{10}$、$\bm u_2=(3,-1)^\top/\sqrt{10}$。

6. 续例核验：正交性、按秩一和式重建$\bm A$，以及附加检查$\bm A^\top\bm u_1=\sigma_1\bm v_1$。

7. 续例结论：$\lVert\bm A\rVert_2=3\sqrt5$，$\lVert\bm A\rVert_{\mathrm F}^2=50$与逐元素平方和一致，$\lVert\bm A^{-1}\rVert_2=1/\sqrt5$。

8. 对照该矩阵的特征值$3,5$与奇异值，说明二者含义不同，只对对称半正定矩阵一致。

###### paragraph：单位球的像

1. 用三步读法说明只有$\bm\Sigma$改变长度，单位球被映成椭球（秩亏时在低维子空间内）。

2. 证明像恰为$\operatorname{span}\{\bm u_1,\ldots,\bm u_r\}$中满足$\sum(\bm u_i^\top\bm y)^2/\sigma_i^2\leq1$的点集，即以$\sigma_i\bm u_i$为半轴的椭球。

3. 以$(\bm v_1+\bm v_d)/\sqrt2$说明$r<d$时球面点可映入内部，所以用单位球描述像；把最长半轴与半轴平方和对应到谱范数与Frobenius范数；引出图`fig:matrix-analysis-svd-geometry`（$\bm R(\pi/6)\operatorname{diag}(2,0.4)\bm R(\pi/5)^\top$，输入与输出方向不同）。

###### paragraph：数值计算中的核验

1. 说明数值因子只近似满足各等式，须分别报告重建误差与两组正交性误差。

2. 说明两类残差不能互相代替，只有都小时才能把计算值当作奇异值的近似，其误差由第9章的奇异值扰动界判断。

3. 说明构造路线不宜照搬到数值计算：$\bm A^\top\bm A$使奇异值之比平方化，小奇异值易被淹没（第~`sec:ls-ls-regularization-sensitivity`节以正规方程分析），实际算法直接作用于$\bm A$，不在本书展开。

### 7.5 本章小结

1. 回应章首问题：由$\bm A^\top\bm A$的谱分解构造$\bm A\bm v_i=\sigma_i\bm u_i$，对任意矩阵成立，只依赖谱定理。

2. 归纳三种写法与唯一性范围：奇异值与正奇异值的左右奇异子空间唯一，同一奇异值内部两组基一起旋转，零奇异值部分可独立选取。

3. 归纳从奇异坐标读出的谱范数、Frobenius范数、秩、最弱放大与逆矩阵范数，以及单位球的椭球像。

4. 归纳核验要求与数值计算中的注意。

5. 指出这些读数在第6、7章的用途，最佳低秩近似留给第17章。

## 第8章 极分解

正文入口：[03-polar-decomposition.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/02-spectral-analysis/03-polar-decomposition.tex)。

1. 以复数$z=e^{\mathrm i\theta}r$为类比提出本章问题：能否写$\bm A=\bm W\bm H$（$\bm H$沿正交方向非负伸缩、$\bm W$保长），是否唯一，顺序能否交换，奇异或非方阵时能保留多少。

2. 说明与SVD的关系：本章把“转向、伸缩、再转向”重组为两段，并关心能否不先求全部奇异向量就直接求出两个因子。

3. 说明五节的分工：8.1节消去正交因子得开方方程；8.2节沿谱开方构造唯一的正定伸缩因子；8.3节撤销伸缩得正交因子并比较左右两种顺序；8.4节借SVD处理奇异与矩形矩阵、说明核怎样破坏唯一性；8.5节把沿谱改写特征值归纳为矩阵函数。

4. 交代依赖（谱定理、谱投影、定号性判据，奇异情形用SVD），并说明正交因子是最近正交矩阵这一最优性在第17章证明。

### 8.1 伸缩与正交转向的分离

1. 引入贯穿例$\bm A=\left[\begin{smallmatrix}0&-1\\3&0\end{smallmatrix}\right]$：同时改变长度与方向，希望拆成先由对称正定$\bm H$伸缩、再由正交$\bm W$转向。

2. 说明本节和后两节先假定$\bm A$可逆，此时$\bm H$应正定；正交矩阵允许含反射；奇异或非方阵的情形留到8.4节。

3. 消去一个未知因子：由$\bm W^\top\bm W=\bm I$得$\bm A^\top\bm A=\bm H^2$（式`eq:ls-polar-square-root-equation`），并用$\lVert\bm A\bm x\rVert_2=\lVert\bm H\bm x\rVert_2$解释正交因子为何消失。

4. 把问题前一半化为对已知矩阵$\bm S=\bm A^\top\bm A$开方，强调这只是分解存在时的必要条件。

5. 确认$\bm S$对称正定（用到$\bm A$可逆），可用正交谱分解且特征值全正。

6. 在贯穿例中算出$\bm S=\operatorname{diag}(9,1)$，得候选$\bm H=\operatorname{diag}(3,1)$，并指出一般情形须用谱分解。

### 8.2 伸缩因子的构造

1. 由$\bm S=\bm Q\bm\Lambda\bm Q^\top$写出候选$\bm H=\bm Q\operatorname{diag}(\sqrt{\lambda_i})\bm Q^\top$（式`eq:ls-spectral-square-root`），强调未预先假定$\bm H$与$\bm S$共用特征基，要靠验证。

2. 验证$\bm H^2=\bm S$与$\bm H$对称正定，记为正定平方根$\bm S^{1/2}$（矩阵平方根）。

3. 说明构造对半正定$\bm S$同样可行，提出$\bm Q$在重根时不唯一的问题。

4. 用$\pm\bm I$、$\operatorname{diag}(1,-1)$与$\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]$说明$\bm X^2=\bm S$的代数解可以不对称、不半正定，引出须加半正定要求。

5. 陈述定理`thm:ls-psd-square-root`，存在性与正定性由前面的验证给出。

6. 证明唯一性：对任一半正定解作谱分解，得每个$\bm p_j$是$\bm S$的特征向量。

7. 续证：说明$\ker(\bm S-\lambda\bm I)$恰由$\mu_j^2=\lambda$的$\bm p_j$张成，非负性迫使$\mu_j=\sqrt\lambda$，$\bm X$与$\bm S^{1/2}$在该特征空间上都乘以$\sqrt\lambda$。

8. 续证：特征空间张成全空间，故$\bm X=\bm S^{1/2}$。

9. 从论证读出$\bm S^{1/2}$不依赖$\bm Q$，以及唯一性只针对半正定解。

10. 回到贯穿例核对$\bm H=\operatorname{diag}(3,1)$，交代解题进度。

11. 指出“把特征值换成平方根”将在8.5节成为矩阵函数的例子，但这里只用谱分解、标量开方与矩阵乘法。

12. 给出长度恒等式$\lVert\bm S^{1/2}\bm x\rVert_2^2=\bm x^\top\bm S\bm x$（式`eq:ls-square-root-length`），说明$\bm H$承担全部长度变化、方向差别由$\bm W$补上，并指出第13章分析Gauss--Seidel迭代时使用它。

13. 比较平方根与Gram因子$\bm L$（定理`thm:ls-gram-factor`）：二者给出相同长度但作用不同。

14. 预告二者相差一个正交因子，并指出第12章的Cholesky分解把$\bm L$取成三角矩阵。

### 8.3 正交因子与左右极分解

1. 说明本节先完成$\bm A=\bm W\bm H$，再把伸缩因子放到左侧比较两种顺序。

###### paragraph：先伸缩、后转向

1. 由$\bm H$可逆右乘$\bm H^{-1}$得唯一候选$\bm W=\bm A\bm H^{-1}$，并解释右乘由因子顺序决定。

2. 沿特征方向写出$\bm H^{-1}=\bm S^{-1/2}$（逆平方根）并验证。

3. 验证$\bm W^\top\bm W=\bm I$与$\bm W\bm H=\bm A$，存在性证完。

4. 给出极分解（右极分解）、正交因子与伸缩因子的定义`def:matrix-analysis-polar-decomposition`（式`eq:matrix-analysis-polar-decomposition`）。

5. 说明定义中的$\bm H=(\bm A^\top\bm A)^{1/2}$不是额外要求，引出可逆情形的定理。

6. 陈述可逆矩阵的极分解定理`thm:ls-polar-invertible`并证明存在性。

7. 证明唯一性：由平方根唯一得$\bm H'=\bm H$，再右乘$\bm H^{-1}$得$\bm W'=\bm W$。

8. 由行列式说明$\bm W$与$\bm A$的行列式同号，正交因子可能是旋转或含反射。

9. 用极分解解释Gram因子：$\bm L=(\bm L\bm S^{-1/2})\bm S^{1/2}$，二者相差正交因子。

10. 算完贯穿例：$\bm W=\left[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right]$，核对并识别为逆时针旋转$90$度。

11. 读出原变换是“先沿$\bm e_1$伸长$3$倍、再旋转$90$度”，说明$\bm S$、$\bm H$、$\bm W$的角色。

###### paragraph：先转向、后伸缩

1. 提出$\bm A=\bm K\bm W'$，从右侧消去正交因子得$\bm K^2=\bm A\bm A^\top$，指出左右伸缩因子一般不同。

2. 在$\bm H$左侧插入$\bm W^\top\bm W$得$\bm A=(\bm W\bm H\bm W^\top)\bm W$，验证$\bm K=\bm W\bm H\bm W^\top$对称正定、特征值同$\bm H$、特征方向转过$\bm W$，且$\bm K^2=\bm A\bm A^\top$，故$\bm K=(\bm A\bm A^\top)^{1/2}$。

3. 陈述并证明左极分解定理`thm:polar-left-invertible`：存在性见前段，唯一性由平方根唯一与$\bm K$可逆得到。

4. 在贯穿例中算出$\bm K=\operatorname{diag}(1,3)$并核对$\bm K\bm W=\bm A$，比较“先伸长再旋转”与“先旋转再伸长”：倍数相同，伸缩方向分别在输入端与输出端度量。

5. 与SVD对照：$\bm W=\bm U\bm V^\top$、$\bm H=\bm V\bm\Sigma\bm V^\top$、$\bm K=\bm U\bm\Sigma\bm U^\top$，左右伸缩因子分别沿左、右奇异向量伸缩（验证留到8.4节）。

### 8.4 奇异与矩形矩阵的极分解

1. 说明前两节的正交因子要求$\bm A$可逆，本节先处理奇异方阵、再处理矩形矩阵，借SVD构造因子并确定唯一部分。

###### paragraph：零伸缩方向上的正交补全

1. 说明奇异时仍得唯一的半正定$\bm H$，但$\bm H^{-1}$不存在，$\bm W=\bm A\bm H^{-1}$失效。

2. 改用SVD，在$\bm U$与$\bm\Sigma$之间插入$\bm V^\top\bm V$得候选$\bm W=\bm U\bm V^\top$、$\bm H=\bm V\bm\Sigma\bm V^\top$（式`eq:ls-polar-from-svd`）。

3. 陈述一般方阵的极分解定理`thm:ls-polar-general`，验证候选满足全部要求。

4. 证明$\bm H$唯一，可逆时$\bm W$唯一。

5. 证明奇异时$\bm W$不唯一：把$\bm u_d$变号得另一正交因子，$\bm W-\bm W'=2\bm u_d\bm v_d^\top\neq\bm0$。

6. 说明可逆时SVD给出的因子与谱开方给出的相同，已有SVD时可直接读出。

###### paragraph：规范部分等距因子

1. 从作用上解释不唯一：$i\leq r$时$\bm W\bm v_i=\bm u_i$由$\bm A$确定，$i>r$时$\bm A$不提供信息。

2. 取出由$\bm A$确定的部分，定义$\bm W_0=\bm U_r\bm V_r^\top$，验证它在$(\ker\bm A)^\perp$上保长、在核上为零，并定义部分等距。

3. 证明$\bm W_0\bm H=\bm A$，且满足$\bm Z\bm H=\bm A$、在核上为零的$\bm Z$只能是$\bm W_0$，故$\bm W_0$与所选SVD无关，称为规范部分等距因子。

4. 引入$\bm V_0$、$\bm U_0$（核与值域正交补的标准正交基），说明全部正交因子由$\bm W_0$补全得到。

5. 陈述定理`thm:polar-singular-orthogonal-factors`（正交因子恰为$\bm W_0+\bm U_0\bm R\bm V_0^\top$，$\bm R$正交），证明充分性：在$(\ker\bm A)^\perp$上不变，且把标准正交基送到标准正交基。

6. 证明必要性：$\bm W\bm V_r=\bm U_r$，$\bm W\bm V_0$的列标准正交且落在值域正交补中，故$\bm W\bm V_0=\bm U_0\bm R$，$\bm R$正交。

7. 解释定理：自由度全部来自核，核的维数越大选择越多，可逆时唯一；前一定理中的变号是特例；不定义不存在的$\bm H^{-1}$。

8. 示例`ex:polar-rank-one`给出$\bm A=\left[\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right]$，得$\bm H=\operatorname{diag}(1,0)$。

9. 续例：$\bm W_0=\bm A$，取$\bm R=\pm1$得两个正交因子（反射与旋转），二者只在被压成零的$\bm e_2$方向上不同。

###### paragraph：矩形矩阵

1. 说明矩形矩阵的保长因子只能是列标准正交或行标准正交的矩阵，取决于哪一端更大。

2. 高矩阵$m\geq d$：由薄SVD得$\bm W=\bm U_d\bm V^\top$（列标准正交）、$\bm H=\bm V\bm\Sigma_d\bm V^\top$，验证$\bm W\bm H=\bm A$。

3. 讨论唯一性：$\bm H$唯一，满列秩时$\bm W=\bm A\bm H^{-1}$唯一，否则可在核上改变$\bm W$。

4. 宽矩阵$m<d$：对$\bm A^\top$应用高矩阵结论再转置，得$\bm A=\bm H_1\bm W_1^\top$（行标准正交），即左极分解形式；结论是宽矩阵自然用左极分解、高矩阵用右极分解。

5. 示例`ex:polar-rectangular`对列向量$(3,4)^\top$得$\bm H=5$、$\bm W=(0.6,0.8)^\top$。

6. 续例：行向量$[3,4]=5\cdot[0.6,0.8]$，解释为先读出单位方向上的坐标再乘以$5$。

### 8.5 矩阵函数的谱表示

1. 说明本节把前面反复使用的沿谱运算写成一般定义，检查相容性与适用范围。

###### paragraph：沿谱运算的共同方法

1. 回看求$\bm H$与$\bm H^{-1}$都是“方向不动、只对特征值作用标量函数”。

2. 借6.3.3节的谱投影写$\bm S=\sum_\lambda\lambda\bm P_\lambda$并列出投影关系。

3. 给出对称矩阵谱函数的定义`def:ls-symmetric-matrix-function`（式`eq:ls-symmetric-spectral-function`）。

4. 说明两种写法相等，由谱投影唯一得定义与基无关。

5. $f(z)=\sqrt z$、$1/\sqrt z$回到$\bm S^{1/2}$与$\bm S^{-1/2}$，强调前面的构造在此得到总结而非以矩阵函数为前提。

6. 提出推广后须与矩阵运算相容。

7. 陈述引理`lem:ls-spectral-function-calculus`并先证第二条（加法与乘法规则，用谱投影的正交关系与幂等性）。

8. 证第一条：常数函数与恒等函数、归纳得多项式情形一致。

9. 证第三条：由乘法规则得逆。

10. 补充多项式情形的直接看法（相邻$\bm Q^\top\bm Q$相消），并由引理重新得到$(\bm S^{1/2})^2=\bm S$与$\bm S^{1/2}\bm S^{-1/2}=\bm I$。

11. 指出矩阵函数沿特征方向作用而非逐元素作用。

12. 示例`ex:ls-matrix-square-root-two-by-two`对$\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$写出$\bm S^{1/2}$与$\bm S^{-1/2}$并核对，再与逐元素开方对照。

13. 说明定义只需$f$在有限个特征值上的值，不要求连续、级数或微分。

14. 把沿谱矩阵函数与第20章研究的一般矩阵输入映射区分开。

15. 以$(\bm S+\bm E)^2-\bm S^2$说明扰动一般不保持特征方向，一阶部分只在可交换时化为$2\bm S\bm E$。

###### paragraph：在已知分解上作用谱函数

1. 说明正交相似下$f(\bm Z\bm S\bm Z^\top)=\bm Zf(\bm S)\bm Z^\top$，并由$\bm A\bm A^\top=\bm W(\bm A^\top\bm A)\bm W^\top$重新得到$\bm K=\bm W\bm H\bm W^\top$。

2. 由SVD写出$f(\bm A^\top\bm A)=\bm Vf(\bm\Sigma^\top\bm\Sigma)\bm V^\top$与$f(\bm A\bm A^\top)$，取平方根得$\bm H$与$\bm K$，可逆时取逆平方根得$\bm W=\bm U\bm V^\top$，与式`eq:ls-polar-from-svd`一致。

###### paragraph：实幂与对数的补充例子

1. 对正定$\bm S$定义实幂$\bm S^\alpha$，得$\bm S^\alpha\bm S^\beta=\bm S^{\alpha+\beta}$与$(\bm S^{1/m})^m=\bm S$，说明$\bm S^{1/m}$对称正定，不讨论$m>2$时的唯一性。

2. 说明零特征值使负幂无定义（平方根要求半正定、逆平方根要求正定的原因），负特征值使平方根与对数失去实值定义。

3. 定义矩阵对数并解释$\log\lambda_i$的符号。

4. 证明沿谱定义下$\log$与$e^{(\cdot)}$在正定矩阵与实对称矩阵之间互为逆映射，零特征值时不能使用。

5. 区分$\log\bm S$与$\log\det\bm S=\operatorname{tr}(\log\bm S)$，说明对数不参与极分解的证明，第~`sec:multivariable-logdet-differential`节求$\log\det$的微分不以矩阵对数的微分为前提。

### 8.6 本章小结

1. 回应章首问题：可逆方阵的极分解由$\bm H^2=\bm A^\top\bm A$与$\bm W=\bm A\bm H^{-1}$唯一确定，$\bm W$可能含反射。

2. 归纳左右两种顺序的关系及其SVD表示。

3. 归纳奇异与矩形情形：伸缩因子仍唯一，由$\bm A$确定的只有规范部分等距因子，全部正交因子的形式，高矩阵用右极分解、宽矩阵用左极分解。

4. 归纳谱函数的定义、相容性与特征值范围的限制。

5. 指出最近正交矩阵的最优性在第17章证明，并转入第9章的误差问题。

## 第9章 条件数与谱扰动

正文入口：[04-condition-and-spectral-perturbation.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/02-spectral-analysis/04-condition-and-spectral-perturbation.tex)。

1. 从数据几乎从不精确进入，提出本章问题：只知道误差上限时由数据算出的结论有多可靠。

2. 按误差位置把问题分成两类：固定矩阵、输入带误差；矩阵本身带误差。

3. 说明两节分工：9.1节由精确增量与最坏方向得到绝对、相对与矩阵条件数；9.2节给出特征值与奇异值的区间、由谱隙控制的子空间偏转，以及一般方阵对特征基条件的依赖。

4. 交代依赖（谱定理、Schur形、SVD读数），强调结论都是有限扰动界、不需要微分。

5. 说明与后续章的分工：第16章区分数据误差与算法误差，第20章建立微分公式，第21章说明解映射何时可微，第22章统一讨论指定方向的一阶响应、局部条件数与余项界。

### 9.1 线性作用的误差放大与条件数

1. 设定问题：固定$\bm A$，实际输入$\bm x+\bm h$，问输出相差多少，并定义扰动。

2. 说明三步：精确增量与绝对误差界；固定输入的相对条件数；对输入也取最坏值的矩阵条件数。

3. 约定欧氏范数与谱范数，限定只讨论输入误差；矩阵误差在下一节，算法误差在第16章。

#### 9.1.1 输入扰动与输出误差

1. 写出精确增量$\Delta\bm y=\bm A\bm h$，说明它对任意大小的扰动成立、与基点无关。

2. 引入误差预算$\lVert\bm h\rVert_2\leq\eta$，提出可靠上界与达到上界的方向两个问题。

3. 定义绝对误差，说明预算不限制方向、可靠的界由最坏方向决定，SVD恰好给出最坏方向。

4. 陈述并证明定理`thm:ls-absolute-error-bound`：按右奇异向量展开得不等式，取$\bm h=\eta\bm v_1$取等，任何更小的常数都不成立。

5. 说明沿$\bm v_i$扰动时放大恰为$\sigma_i$，沿零空间扰动不影响输出，误差界取的是最坏情形。

#### 9.1.2 固定输入处的条件数

1. 由绝对误差比只依赖方向、与基点无关，定义绝对条件数$\lVert\bm A\rVert_2=\sigma_{\max}$，指出线性作用各点的绝对条件数相同。

2. 定义相对误差，说明其尺度不变性、参照量为零或接近零时的处理，以及范数与尺度的选择属于问题本身的规定。

3. 指出同一矩阵在不同基点与方向上相对误差的放大可以很不一样。示例`ex:ls-diagonal-relative-error-basepoints`取$\operatorname{diag}(1,s)$与预算$\eta$。

4. 续例：基点$\bm e_2$、扰动$\eta\bm e_1$时放大$1/s$倍，原因是理想输出被压缩。

5. 续例：基点$\bm e_1$、扰动$\eta\bm e_2$时比值为$s$；例后由比值从$1/s$变到$s$得出须说明基点与方向或取最坏情形，本小节先对方向取最坏、下一小节再对基点取最坏。

6. 指出理想输出很小时也会放大，示例`ex:ls-cancellation-relative-error`用$[1\;1]$把$1.0001$与$-1.0000$相加，输出相对误差可达$1$，放大约$2\times10^4$倍，这是问题本身的敏感性而非舍入误差。

7. 给出相对条件数的定义`def:ls-relative-condition-number`，陈述并证明定理`thm:ls-relative-condition-number`（式`eq:matrix-analysis-condition-number-bound`）：比值拆成与$\bm h$无关的因子与绝对误差比，得$\kappa_{\mathrm{rel}}=\lVert\bm A\rVert_2\lVert\bm x\rVert_2/\lVert\bm A\bm x\rVert_2$；回到对角例子核对，并指出沿具体方向观察到的比值可以更小。

8. 由表达式用奇异方向辨认敏感与不敏感输入：$\bm x$沿$\bm v_1$时相对条件数为$1$，越靠近被压缩的方向越敏感。

9. 说明上确界取遍有限扰动之所以可行，是因为线性作用的误差比只依赖方向；一般非线性映射须先在半径$\delta$内取最坏再令$\delta$缩小，局部条件数及其与微分的联系在第22章建立。

#### 9.1.3 矩阵条件数与方向差异

1. 指出相对条件数随基点变化，对基点也取最坏值时只依赖矩阵。

2. 给出可逆矩阵条件数的定义`def:matrix-analysis-condition-number`（式`eq:matrix-analysis-condition-number`）。

3. 陈述定理`thm:matrix-analysis-condition-number-bound`（式`eq:matrix-analysis-spectral-condition-number`）并证明第一条：由$\lVert\bm A\bm x\rVert_2\geq\sigma_n\lVert\bm x\rVert_2$得上确界$\sigma_1/\sigma_n$并在$\bm v_n$取到。

4. 证明第二条：把相对条件数放大为$\kappa_2$，在$\bm x=\bm v_n$、$\bm h=c\bm v_1$时取等。

5. 证明第三条：$\Delta\bm x=\bm A^{-1}\Delta\bm b$，把第二条用于$\bm A^{-1}$并由$\kappa_2(\bm A^{-1})=\kappa_2(\bm A)$得线性方程解的相对误差界；证明后用等号条件解释条件数比较最强与最弱作用的差异。

6. 说明欧氏范数并非必需，任一诱导范数下最坏值为$\lVert\bm A\rVert\lVert\bm A^{-1}\rVert$。

7. 说明条件数不小于$1$，几何上是像椭球最长与最短半轴之比。

8. 定义良态与病态，图`fig:ls-condition-number-amplification`对比$\kappa_2=1.5$与$\kappa_2\approx12.3$两个矩阵。

9. 强调条件数看方向差异而非大小：$\operatorname{diag}(1,s)$与$s\bm I$对比，奇异值同比例缩放不改变条件数。

10. 示例`ex:ls-condition-number-vs-powers`中$2\bm I$与$\tfrac12\bm I$条件数都为$1$而幂趋势相反，长期行为由谱半径判断（第~`sec:ls-matrix-power-behavior`节）。

11. 限定本节结论只刻画问题本身的敏感性。

12. 指出方程解的完整误差界见第~`sec:ls-numerical-sensitivity`节，求逆的一阶响应见第~`sec:multivariable-inverse-perturbation`节；下一节改变矩阵本身，各输出另有敏感性度量。

### 9.2 谱与奇异值的扰动

1. 从矩阵本身也来自数据进入，提出在预算$\lVert\bm E\rVert_2\leq\varepsilon$下哪些谱结论可靠。

2. 说明三种输出各需相应的界，并给出本节顺序。

3. 强调都是有限变化界，一阶响应留给第22章（第~`sec:multivariable-eigenvalue-differential`节与第~`sec:multivariable-eigenvector-differential`节）。

#### 9.2.1 对称矩阵特征值的扰动

1. 设定对称的$\bm S$与$\bm E$、按降序配对比较，目标是每个特征值的区间与正负性。

2. 用图`fig:ls-perturbation-ellipse`说明半轴对应特征值、主轴对应特征方向，本小节先处理前者。

###### paragraph：有序特征值的比较

1. 由Cauchy--Schwarz得同一单位向量上二次型值相差不超过$\lVert\bm E\rVert_2$，指出难点是两个矩阵的特征方向不同。

2. 提出用子空间刻画有序特征值的办法。

3. 陈述并证明引理`lem:ls-eigen-subspace-quadratic-bounds`：在前$k$个特征方向张成的子空间上二次型不小于$\lambda_k\lVert\bm x\rVert_2^2$，在后$d-k+1$个上不大于，由二次型展开的加权和得到。

4. 由维数公式说明$k$维与$d-k+1$维子空间必有公共非零向量，从而能在两个矩阵各自的特征子空间中找到公共方向。

5. 陈述并证明Weyl界`thm:ls-weyl-eigenvalue`（式`eq:matrix-analysis-weyl-eigenvalue-perturbation`）：取$\bm S$的$\mathcal V_k$与$\widetilde{\bm S}$的$\widetilde{\mathcal W}_k$的公共单位向量，用引理与$\bm x^\top\bm E\bm x\geq-c$连成$\lambda_k(\widetilde{\bm S})\geq\lambda_k(\bm S)-c$，交换角色得另一侧。

6. 说明证明只用谱分解、维数公式与同方向比较，没有求二次型的极值，也不要求特征值分开。

###### paragraph：最小最大原理

1. 说明同一论证给出不依赖特征向量的刻画。

2. 陈述Courant--Fischer定理`thm:matrix-analysis-courant-fischer`，证明内层极值取到：把子空间上的二次型化为压缩矩阵$\bm U^\top\bm S\bm U$的二次型，由谱定理得其最值。

3. 证明第一式：$\mathcal V_k$给出下界，任一$k$维子空间与$\mathcal W_k$的公共向量给出上界。

4. 证明第二式：交换两组特征向量的角色。

5. 称其为最小最大原理，说明Weyl界也可由它推出；$k=1,d$时化为单位球面上的极值，第17章称$\bm x^\top\bm S\bm x/\bm x^\top\bm x$为Rayleigh商并研究它；与迹极值（刻画前$k$个特征值之和）区分。

###### paragraph：谱值区间与正定性保证

1. 读出误差区间$[\lambda_k(\bm S)-\varepsilon,\lambda_k(\bm S)+\varepsilon]$，适用于重特征值，但它是绝对误差界。

2. 由区间判断符号，以$\operatorname{diag}(1,\varepsilon/2)$说明区间含零时预算不足；陈述并证明定理`thm:ls-eigenvalue-sign-definiteness`：第一条由Weyl界，第二条对$t\bm E$得与$t$无关的下界，整条线段正定。

3. 说明这一与$t$无关的下界在求逆、开方、取对数时保证线段留在定义域内，例如第~`sec:multivariable-logdet-perturbation`节。

4. 示例`ex:ls-weyl-double-root`取$\operatorname{diag}(t,-t)$：重根处Weyl界取等，而排序后的最大特征值$|t|$没有双侧导数，有限变化界与可微性是两回事。

5. 指出第~`sec:multivariable-local-condition-number`节再用该例，第~`sec:multivariable-eigenvalue-differential`节研究简单特征值分支的一阶响应。

#### 9.2.2 奇异值的扰动与秩判断

1. 说明秩、可逆性与最佳低秩误差由奇异值决定，本小节把区间移到奇异值上。

###### paragraph：奇异值的误差区间

1. 指出长方矩阵没有特征值，引入对称增广矩阵$\bm H(\bm A)$。

2. 陈述引理`lem:ls-symmetric-augmentation-spectrum`，证明由完整SVD构造$\bm w_i^\pm$得特征值$\pm\sigma_i$与$|m-n|$个零，验证构成标准正交特征基。

3. 续证$\lVert\bm H(\bm A)\rVert_2=\lVert\bm A\rVert_2$。

4. 陈述并证明奇异值的Weyl界`thm:ls-weyl-singular-value`（式`eq:matrix-analysis-singular-value-perturbation`）：对增广矩阵用Weyl界。

5. 写出真实奇异值所在的非负区间。

6. 由第17章将证明的最小谱范数距离$\sigma_{k+1}$（定理`thm:matrix-analysis-best-low-rank`）得最优低秩误差的移动不超过$\varepsilon$，并提醒取得它的方向是否稳定留到下一小节。

###### paragraph：秩保证与可逆性的边界

1. 说明区间不含零给出秩的下界，陈述并证明定理`thm:ls-singular-value-rank-guarantee`。

2. 说明反方向不成立：区间含零时既不能排除也不能断言秩亏。

3. 区分精确秩与有效秩：$\operatorname{diag}(1,0)+t\bm e_2\bm e_2^\top$说明精确秩对任意小扰动跳变，可靠的是大于$\varepsilon$的奇异值个数；按阈值确定数值秩留到第~`sec:ls-pseudoinverse-rank-change`节。

4. 提出使可逆矩阵奇异的最小扰动问题，陈述定理`thm:ls-distance-to-singularity`。

5. 说明证明分两步。

6. 下界：$\lVert\bm E\rVert_2<\sigma_n$时由最小奇异值下界与三角不等式得零空间平凡；可达：$\bm E_*=-\sigma_n\bm u_n\bm v_n^\top$；相对距离$1/\kappa_2$；证明后指出它是最佳低秩逼近$k=n-1$的特例，直接证明只用最小奇异值下界。

7. 给出条件数的另一种解释，限定为允许任意谱范数扰动，结构化扰动只得下界；以$\bm E=\bm A$说明超过$\sigma_n$的扰动不一定使矩阵奇异。

8. 示例`ex:ls-diagonal-distance-to-singularity`取$\operatorname{diag}(1,s)$核对可逆性边界。

9. 指出离奇异近不代表第一奇异方向不稳定，方向稳定性由间隙$1-s$决定。

#### 9.2.3 特征子空间的扰动

1. 指出特征值误差小时方向仍可能变化很大，先建立子空间距离，再检查谱隙。

###### paragraph：子空间的距离

1. 说明比较对象应是子空间本身，从两条直线的夹角与投影残差$\sin\theta$进入（图`fig:ls-principal-angles-subspaces`）。

2. 由一维情形$|\bm q^\top\widetilde{\bm q}|=\cos\theta$过渡到高维，给出主夹角的定义`def:matrix-analysis-principal-angles`。

3. 说明主夹角有定义且只依赖子空间，记$\theta_{\max}$。

4. 引入$\bm C$、$\bm X$与投影$\bm P$、$\widetilde{\bm P}$，陈述定理`thm:ls-principal-angle-projection`。

5. 证明：由勾股定理与极化得$\bm X^\top\bm X=\bm I-\bm C^\top\bm C$，特征值为$\sin^2\theta_i$。

6. 续证：由投影的对称幂等与迹得$\tfrac12\lVert\bm P-\widetilde{\bm P}\rVert_{\mathrm F}^2=\sum\sin^2\theta_i$。

7. 说明Frobenius范数汇总全部夹角，陈述定理`thm:ls-projection-spectral-distance`（$\lVert\bm P-\widetilde{\bm P}\rVert_2=\sin\theta_{\max}$），先由上一定理得$\lVert\bm X\rVert_2=\sin\theta_{\max}$。

8. 续证：借正交补基算出$\lVert(\bm I-\widetilde{\bm P})\bm P\rVert_2$与$\lVert(\bm I-\bm P)\widetilde{\bm P}\rVert_2$都等于$\sin\theta_{\max}$。

9. 续证上界：把$\bm P-\widetilde{\bm P}$拆成落在列空间与其正交补中的两项，两次用勾股定理。

10. 续证上界中各步的依据。

11. 续证下界：取$\bm X$的第一右奇异向量构造$\bm z=\bm Q\bm a$。

###### paragraph：谱隙控制的偏转界

1. 引入原谱隙$\delta$，在$\varepsilon<\delta/2$下由Weyl界证明截断处仍分开、两子空间唯一。

2. 定义交叉谱间隔$\gamma=\lambda_k(\bm S)-\lambda_{k+1}(\widetilde{\bm S})\geq\delta-\varepsilon$。

3. 引入$\bm Q,\bm\Lambda_1,\widetilde{\bm Q}_\perp,\widetilde{\bm\Lambda}_2$与$\bm X$。

4. 陈述并证明Frobenius界`thm:ls-gap-subspace-frobenius`：由两组特征关系得$\widetilde{\bm\Lambda}_2\bm X-\bm X\bm\Lambda_1=\widetilde{\bm Q}_\perp^\top\bm E\bm Q$，逐元素相除。

5. 指出该方程是Sylvester方程（第~`sec:ls-matrix-equations`节），并得$\sqrt k\lVert\bm E\rVert_2/\gamma$的界。

6. 说明最大主夹角的界不是Frobenius界的推论，陈述并证明Davis--Kahan谱隙界`thm:ls-davis-kahan`（式`eq:matrix-analysis-eigenvector-gap-bound`）：用$\bm X$的第一左右奇异向量从两侧检验同一方程，左端至少$s\gamma$、右端不超过$\lVert\bm E\bm Q\rVert_2$。

7. 指出证明只用单侧谱分离，目标组位于谱中间时须另作处理。

8. 把交叉间隔换成事先可检查的$\varepsilon/(\delta-\varepsilon)\leq2\varepsilon/\delta$，说明谱隙在分母上。

9. 示例`ex:ls-gap-direction-rotation`取$\operatorname{diag}(1+\delta,1)$与交叉扰动，精确求出$\tan2\theta=2t/\delta$。

10. 续例：$\kappa_2(\bm S)$接近$1$而$t=\delta/2$时转角达$22.5^\circ$，子空间敏感性不能由条件数判断；最大特征值增量符合Weyl界。

11. 把精确转角与界比较，$t\ll\delta$时两端约为$t/\delta$；图`fig:matrix-analysis-gap-direction`画出增量与转角随谱隙的变化。

###### paragraph：重根、奇异子空间与低秩近似

1. 说明谱隙只需存在于目标组与组外之间：$\operatorname{diag}(2,2,0)$的前二维子空间稳定。

2. 但平面内单个特征向量不稳定，子空间内部基的变化与子空间的变化须区分。

3. 借对称增广把奇异子空间化为特征子空间，说明要求奇异值间隙$\delta_\sigma>0$并保证$\sigma_k>0$的原因。

4. 写出增广矩阵前$k$个特征子空间的投影$\bm P_{\bm H}$的分块形式。

5. 在$\varepsilon<\delta_\sigma/2$下得左、右奇异子空间投影之差不超过$4\varepsilon/\delta_\sigma$。

6. 对照最优误差$\sigma_{k+1}$总是稳定而所用方向只在有间隙时稳定，指出第~`sec:ls-truncated-svd-ridge`节选截断位置时两者都要看。

#### 9.2.4 一般方阵的谱敏感性

1. 说明对称结构使特征值可排序并由二次型在特征子空间上刻画，一般方阵没有这些性质，改问扰动后特征值离原谱多远，约定复欧氏范数。

2. 陈述并证明Bauer--Fike定理`thm:ls-bauer-fike`。

3. 区分$\kappa_2(\bm V)$与$\kappa_2(\bm A)$：$\operatorname{diag}(1,s)$的特征值不敏感而$\kappa_2(\bm A)$可很大。

4. 反过来，$\left[\begin{smallmatrix}1&1\\0&1+\eta\end{smallmatrix}\right]$趋于$\bm A_0$时$\kappa_2(\bm A)$有界、求逆不敏感。

5. 但特征向量趋于平行，$\kappa_2(\bm V)\geq1/\eta$，界变宽；非正交特征基是敏感的来源，对称时与Weyl界同量级。

6. 列出使用这个界的三点注意。

7. 反例`ex:ls-jordan-eigenvalue-sensitivity`：$\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]$加$t$后特征值移动$\sqrt t$，不存在比例常数，$t<0$时实特征值消失。

8. 说明缺少可对角化条件时特征值变化的量级可与扰动不同，有限变化界须连同结构与分离条件使用。

9. 节末综合三类结论，并把反复作用交给第10章。

### 9.3 本章小结

1. 回应章首问题：先分清误差位置，再分清关心的输出。

2. 归纳输入误差：绝对放大$\sigma_{\max}$、相对条件数、矩阵条件数$\kappa_2$的含义与不描述的内容。

3. 归纳矩阵误差下特征值与奇异值的区间、符号与正定性、秩下界、到奇异矩阵的距离与有效秩。

4. 归纳子空间偏转的谱隙界及重根、奇异子空间的情形。

5. 归纳一般方阵的Bauer--Fike界与不可对角化时的不成比例变化。

6. 总结判断可靠性须同时说明结构、分离条件与预算，一阶响应在第22章，并转入第10章。

## 第10章 线性递推的收敛与稳定性

正文入口：[05-linear-recurrence-stability.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/02-spectral-analysis/05-linear-recurrence-stability.tex)。

1. 承接第9章的一次作用，提出反复执行$\bm x_{k+1}=\bm T\bm x_k+\bm c$的问题：能否趋于同一平衡、平衡在哪里、接近多快、逐步误差累积多大。

2. 说明五节的分工：10.1节展开递推；10.2节证明初值影响消失当且仅当$\rho(\bm T)<1$；10.3节用Neumann级数求累积与共同极限；10.4节估计速度并说明暂时放大；10.5节比较有界、趋零与可求和的逐步误差。

3. 交代依赖（第6章的特征值、实Schur形、谱半径与正规矩阵，第7章的谱范数），限定只分析给定的$\bm T,\bm c$，构造更新规则留给第13章。

4. 说明收敛的含义：逐坐标收敛（定理`thm:multivariable-coordinatewise-convergence`）、与范数无关（定理`thm:ls-norm-equivalence`），矩阵级数按第~`sec:ls-vector-matrix-series`节定义。

### 10.1 递推解的表示

1. 说明用一个二维例子贯穿全章。示例`ex:ls-affine-running-example`给出$\bm T=\left[\begin{smallmatrix}1/2&1\\0&1/2\end{smallmatrix}\right]$、$\bm c=(0,1)^\top$，按分量解释并从$\bm x_0=\bm0$算出前三步。

2. 指出三步之后看不出是否有界、换初值的结果也无法判断，于是先写出展开式；陈述并证明引理`lem:ls-affine-unrolling`。

3. 解释展开的两部分（初值的剩余影响与输入累积），强调只是有限展开。

4. 比较不同初值的两条轨迹，相减只剩$\bm T^k(\bm x_0-\widetilde{\bm x}_0)$，陈述并证明引理`lem:ls-affine-difference-decay`。

5. 由引理得出下一步任务：先研究$\bm T^k$何时趋于零，再回到输入累积。

### 10.2 初值影响的衰减

1. 给出范数小于$1$的充分条件。

2. 用贯穿例说明该条件不必要：$\lVert\bm T\rVert_2,\lVert\bm T\rVert_1,\lVert\bm T\rVert_\infty$都大于$1$，而显式式（示例`ex:ls-matrix-geometric-series`）表明$\bm T^k\to\bm0$，谱半径为$1/2$。

3. 指出$\bm T$不正规、需要只依赖谱半径的判据。

4. 交代核心引理的构造思路，并把实Schur形记为$\bm U$。

5. 陈述几何上界引理`lem:ls-power-geometric-bound`，证明第一步取实Schur形，第二步把二阶块化为模长乘旋转。

6. 续证：用$\bm D_\varepsilon$压小非对角块，得$\lVert\bm D_\varepsilon^{-1}\bm U\bm D_\varepsilon\rVert_2\leq\rho+\varepsilon c$并解释分块对角部分的估计。

7. 续证：构造坐标范数并验证它诱导的矩阵范数是$\lVert\bm M^{-1}\bm B\bm M\rVert_2$，换回二范数得$C_r$。

8. 说明$C_r$与$k$无关但随$r$改变，几何上界不表示原范数下每步收缩。

9. 示例`ex:ls-coordinate-norm-contraction`在贯穿例中走一遍构造，得$\lVert\bm T\rVert_*\approx0.640$与常数$4$，并说明$r$不能直接取为$\rho(\bm T)$。

10. 陈述并证明矩阵幂衰减判据`thm:ls-power-decay`：充分性由几何上界，必要性分实特征值与非实特征值两种情形。

11. 结合引理得所有初值差异消失当且仅当$\rho<1$，并用示例`ex:ls-partial-convergence`（一个初始差衰减不足以说明全部）与示例`ex:ls-separate-limits`（各轨迹收敛但极限不同）说明判据面向全体初值。

12. 讨论$\rho=1$：$\bm I$恒定、$-\bm I$翻转。

13. 续：$90^\circ$旋转以$4$步为周期循环；示例`ex:ls-unit-spectral-radius-growth`以$\bm J_1^k$说明特征向量不足时线性增长。

14. 引入Jordan块并写出展开式`eq:ch06-jordan-power`。

15. 由展开读出块幂何时有界：$|\lambda|=1$时无界，$|\lambda|<1$时仍趋于零但可能先上升；示例`ex:ls-jordan-transient`列出先升后降的第一坐标。

16. 用图`fig:vol1-add-linear-jordan-accumulation`画出轨迹，并说明多项式因子抬高$C_r$、$r$越接近$\rho$常数越大。

17. 补充$\rho>1$的情形。

### 10.3 固定输入下的平衡与收敛

1. 由取极限得平衡方程，陈述并证明共同极限判据`thm:ls-affine-common-limit`。

2. 以$\bm T=2\bm I$说明$\bm I-\bm T$可逆只保证平衡唯一。

3. 说明平衡怎样由输入累积而成，类比标量几何级数。

4. 陈述Neumann级数定理`thm:ls-neumann`（式`eq:ls-neumann-series`、`eq:ls-neumann-tail`），先证绝对收敛（定理`thm:ls-absolute-series-convergence`）。

5. 续证：由有限几何和恒等式识别和为$(\bm I-\bm T)^{-1}$。

6. 续证极限过程中乘以固定矩阵的连续性（第~`sec:multivariable-continuity`节）与$\bm T^{N+1}\to\bm0$。

7. 续证反向结论。

8. 续证截断界。

9. 得$\bm x_\star=\sum_j\bm T^j\bm c$，解释为历次输入的总和，并以$\operatorname{diag}(1/2,2)$说明单个向量级数收敛推不出$\rho<1$。

10. 示例`ex:ls-affine-running-equilibrium`算出贯穿例的平衡$(4,2)^\top$并用级数核对。

11. 区分$\rho<1$与$\lVert\bm T\rVert\leq q<1$两种条件，得从零出发的误差界；图`fig:ls-neumann-series-tail`核对尾界。

12. 只知$\rho<1$时借坐标范数得尾界，须保留比较常数；贯穿例中核对$k=3$。

13. 转向逐轮变化的输入$\bm c_k$，写出展开式，说明平衡方程失去意义。

14. 说明$\rho<1$仍使初值影响消失但不保证轨迹收敛，以$\bm T=\bm0$、$\bm c_k=(-1)^k\bm c$为例；输入趋于固定值的情形留到10.5节。

### 10.4 收敛速度与短期放大

1. 由几何上界得误差至少按略大于谱半径的公比衰减，说明这是一致上界，某些方向更快，平衡位置另由$\bm c$决定。

2. 用图`fig:ls-spectral-radius-convergence`展示正规情形$\rho\bm I$。

3. 指出$C_r$可能大于$1$。示例`ex:ls-running-transient`在贯穿例中算出前两步误差变长。

4. 把放大归因于耦合；示例`ex:ls-transient-growth`取$\left[\begin{smallmatrix}0.8&4\\0&0.5\end{smallmatrix}\right]$（式`eq:ch06-fixed-iteration-example`、`eq:ch06-diagonalizable-finite-trajectory`），前三步长度约$4.03$、$5.21$、$5.16$。

5. 用初值沿近乎反向的两条特征方向相消解释放大（图`fig:ch06-transient-growth`）。

6. 对可对角化的$\bm T$给出$\lVert\bm T^k\rVert_2\leq\lVert\bm V\rVert_2\lVert\bm V^{-1}\rVert_2\rho^k$，并在例中估计该因子超过$178$。

7. 说明贯穿例与Jordan例不可对角化，放大来自多项式因子。

8. 正规矩阵每步放大恰为谱半径，误差从第一步起不增加；长期衰减、有限步放大与具体方向须分别考察。

9. 陈述并证明Gelfand公式`thm:ls-gelfand-formula`（式`eq:ls-gelfand-formula`）：二范数下的上界。

10. 续证下界。

11. 续证上下极限相等。

12. 续证推广到任意范数。

13. 续证次乘性范数下$\rho\leq\lVert\bm T\rVert$。

14. 解释公式：范数小于$1$必使谱半径小于$1$而反之不然，谱半径是长期几何平均。

15. 给出缩小十倍的参考步数，并以贯穿例说明实际要$8$步；停止准则留给第13章。

### 10.5 误差传播与累积

1. 写出带附加误差的序列与误差递推$\bm e_{k+1}=\bm T\bm e_k+\bm\delta_k$。

2. 陈述逐步误差累积定理`thm:ls-accumulated-step-errors`（式`eq:ls-noise-floor`），证明第一条的归纳。

3. 证明第二条（诱导范数下的有界误差界）。

4. 证明第三条（只知$\rho<1$时带$C_r$的界）。

5. 解释初始误差与附加误差的传播，持续误差不会消失。

6. 说明上界是最坏情形、不保证误差有极限，以交替变号的误差为例说明上界不可改进。

7. 说明非正规时两项都带$C_r$。

8. 引出趋零与可求和误差，交代用坐标范数统一书写。

9. 陈述定理`thm:recurrence-vanishing-summable-errors`，写出两条共用的展开估计。

10. 证明第一条：把和式按$j<J$与$j\geq J$分开，前部按$q^{k-J}$衰减、后部不超过$\varepsilon/(1-q)$。

11. 证明第二条：$q^{k-1-j}\leq1$得总量界，通项趋零后由第一条得收敛。

12. 比较三种误差被计入的次数：有界误差留下$\delta/(1-q)$的水平，趋零误差被消除但不快于自身衰减，可求和误差累积不超过总量$D$。

13. 把10.3节的逐步输入作为第一种情形的应用：$\bm c_k\to\bm c$时轨迹收敛到$(\bm I-\bm T)^{-1}\bm c$。

14. 说明本章假设$\bm T$固定，具体算法的误差、参数与停止留给第13章。

### 10.6 本章小结

1. 回应章首问题，三个问题都化为$\bm T^k$的行为。

2. 归纳$\rho(\bm T)<1$的充要性、坐标范数的作用与$\rho=1$时的各种表现。

3. 归纳Neumann级数与共同平衡，以及可逆性与逐步输入的限制。

4. 归纳Gelfand公式、参考步数与非正规矩阵的暂时放大。

5. 归纳三类逐步误差的影响。

6. 总结判断固定递推的三件事，并指出第13章构造具体更新矩阵，连续时间的线性系统可参考卷六“线性微分方程与系统”章。
