# 卷1《数学准备：基础数学》：向量、矩阵与多元函数大纲

正文入口：[part.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/part.tex)。本提要依据实际接入的七章正文组织。

本部分从具体数组运算进入，以空间、坐标、范数、收敛与连续和内积建立统一语言，再用谱与奇异值研究矩阵作用。方程章区分解结构、各类求解方法及误差；微分章建立局部线性近似并据此分析扰动，积分章以Riemann积分串联区域、路径、曲面及边界。一般测度积分已移至卷二积分章。

## 第8章 向量、矩阵与张量的运算

正文入口：[01-operations.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/01-operations.tex)。

1. 从数据常是一组数进入：一列观测、一张特征表、带通道和像素位置的图像数组；指出三类数组的区别在于定位一个数所需的索引个数（一个、两个、更多）。

2. 列出最先遇到的计算需要：对一列数，要合并、配对并衡量误差大小；对一张表，要一次算出许多加权和、合成两次计算、撤销或重复一次计算，并知道方阵把面积放大多少倍；对多轴数组，要重排、组合并沿指定轴汇总。

3. 按索引个数由少到多说明四节的分工：向量的线性组合、内积与长度；矩阵乘法、行变换、逆与幂；行列式、迹与Frobenius内积把矩阵变成一个数；张量的重排、组合与缩约。对每种运算都交代它做什么、输入条件、输出形状和运算规则。

4. 限定范围：只在有限维实数组层面讨论，只用到第~`part:mathematical-language-analysis-optimization`部分的集合、函数与实数运算；数组记录什么对象、矩阵怎样记录线性映射留给第~`chap:linear-representation`章，一般空间中的长度、夹角与正交留给第~`chap:normed-inner-product-spaces`章。

### 8.1 向量

1. 从观测输入、输出与误差都是一串数进入，定义向量为按固定次序排列的一串实数，并说明本节的三类运算：加法与数乘合成向量，内积把两个向量配成一个数，长度和范数衡量向量的大小。

#### 8.1.1 向量的表示

1. 用一句说明记录数据前要先约定排列方式、各位置的含义和相等的标准。

###### paragraph：坐标向量

1. 由$\mathbb R^d$的有序$d$元组定义列向量、坐标与维数，指出定位一个数只需一个索引。

###### paragraph：列向量与行向量

1. 约定默认使用列向量，引入行向量与转置记号$(u_1,\ldots,u_d)^\top$。

2. 以三次观测的输入$\bm x$与输出$\bm y$说明每个位置的含义须事先固定，两个向量的第$i$个位置对应同一次观测；这是后面逐位置运算有意义的前提。

###### paragraph：相等

规定向量相等要求维数相同且对应坐标相等，以$(1,2)^\top\neq(2,1)^\top$说明次序是向量的一部分。

###### paragraph：零向量

定义所有坐标都为零的零向量$\bm0$。

###### paragraph：标准坐标向量

定义只“点亮”第$j$个位置的标准坐标向量$\bm e_j$，以$\mathbb R^3$中的$\bm e_2$举例。

#### 8.1.2 加法、数乘与线性组合

1. 以两列预测取平均、预测减观测为例，说明本小节要定义加法、数乘及由它们组成的线性组合，并整理运算规则。

##### 8.1.2.1 加法与数乘

1. 给出逐坐标加减与数乘的公式，引出$0\bm x=\bm0$与相反向量，指出结果的每个坐标只由输入的同一坐标决定、维数不变。

2. 示例`ex:ls-vector-addition-scaling`逐坐标计算一组二维向量的加法、减法与数乘。

3. 说明相加的两个条件：维数相同，否则无法逐位置配对；位置含义相同，否则算得出数却没有意义。

##### 8.1.2.2 线性组合

1. 把加法和数乘结合起来，定义线性组合与系数，说明结果的每个坐标是各向量在同一位置上的加权和，系数不要求非负或和为$1$。

2. 示例`ex:ls-residual-vector`把三次观测的残差$\bm r=w\bm x-\bm y$写成以$w,-1$为系数的线性组合，并在$w=1$时算出$\bm r=(1,-2,-3)^\top$。

3. 贯穿例`ex:ls-nearly-collinear-features`给出特征取值向量$\bm c_1$、$\bm c_2$与$\bm q$，逐坐标验证$\bm c_2=\bm c_1+\varepsilon\bm q$；随后一句说明方向“几乎相同”须等第~`sec:ls-inner-product-definition`节定义夹角后说明。

##### 8.1.2.3 加法与数乘的性质

1. 说明加法与数乘逐坐标定义、只用到实数运算，因此每条规则都可在任一坐标上直接验证；给出符号约定。

###### paragraph：加法交换律与结合律

列出加法交换律与结合律。

###### paragraph：零向量与相反向量

列出零向量是加法单位元、$\bm u+(-\bm u)=\bm0$两条规则。

###### paragraph：数乘结合律与单位数

列出$a(b\bm u)=(ab)\bm u$与$1\bm u=\bm u$。

###### paragraph：分配律

1. 列出数乘对标量加法与向量加法的两条分配律。

2. 总结八条规则的用途：有限次加法与数乘可任意加括号、交换次序并展开，线性组合可像多项式一样合并同类项；同形矩阵与多维数组的逐项运算照样满足这些规则，第~`chap:linear-representation`章的许多结论只依赖它们。

#### 8.1.3 内积、长度与距离

1. 从加法与数乘的结果仍是向量过渡：数据分析还要把两个向量配成一个数、用一个数衡量向量大小；本小节只给坐标公式，一般性质在第~`chap:normed-inner-product-spaces`章证明。

##### 8.1.3.1 内积

1. 由线性预测的加权和引出欧氏内积$\langle\bm x,\bm y\rangle=\sum_jx_jy_j=\bm x^\top\bm y$，说明输入两个同维向量、输出标量，并预告它是$1\times d$与$d\times1$矩阵的乘积。

2. 定义内积为零即正交；示例`ex:ls-inner-product-orthogonality`计算三对平面向量的内积，第一对为$2$不正交，后两对为$0$正交。

3. 指出平面上正交就是垂直，一般维数下的理解须等第~`sec:ls-inner-product-definition`节定义夹角。

##### 8.1.3.2 长度与距离

1. 由$\langle\bm x,\bm x\rangle$是平方和而非负，定义长度（式`eq:linear-algebra-inner-product-norm`）与欧氏范数$\lVert\bm x\rVert_2$，说明它推广了勾股定理。

2. 定义单位向量，说明非零向量除以自身长度得到同方向的单位向量。

3. 定义欧氏距离为差向量的长度；示例`ex:ls-length-distance`算出残差长度平方$14$（即平方误差总和）与两点距离$5$。最后提醒比较实际数据前应统一各坐标的单位和尺度。

##### 8.1.3.3 范数

1. 从欧氏长度先平方再相加出发，说明还可以累加绝对值或只看最大绝对值，这些大小度量统称范数。

2. 给出$p$范数与$\infty$范数的公式并解释$p=1,2,\infty$的含义；示例`ex:ls-p-norms`在$(3,-4)^\top$上得到$7,5,4$。

3. 用图`fig:ls-norm-unit-balls`比较三种单位球的形状，并说明非负性、正定性与齐次性可从公式看出，三角不等式见定理`thm:linear-algebra-minkowski`。

4. 本节收束：概括三类运算，并说明把若干向量并排得到矩阵。

### 8.2 矩阵

1. 从样本特征表上用同一组权重求加权和进入，说明矩阵乘法一次写出这些加权和；概述本节先讲写法与常见矩阵，再依次讲加法与数乘、转置、矩阵与向量的乘积、矩阵乘法和逐项乘积（每种运算先定义、再整理性质），最后讲初等行变换、逆矩阵与幂，并指出矩阵乘法与实数乘法规则的异同是重点。

#### 8.2.1 矩阵的表示与常见矩阵

1. 指出数表中的一个数需要行、列两个索引定位。

###### paragraph：矩阵、元素与形状

1. 定义$m\times d$矩阵、元素$\bm A_{i,j}$、形状及行列记号$\bm A_{i,:}$、$\bm A_{:,j}$，以一个$2\times3$矩阵举例。

2. 规定矩阵相等，并说明行向量与列向量是矩阵的特例。

###### paragraph：设计矩阵

约定行对应样本、列对应特征，把示例`ex:ls-nearly-collinear-features`的$\bm c_1,\bm c_2$并排为贯穿例$\bm X_\varepsilon=[\bm c_1\ \bm c_2]$（式`eq:linear-algebra-nearly-collinear-design`），说明后面各章用它考察两列几乎相同时的问题。

##### 8.2.1.1 常见矩阵

1. 从元素分布的固定模式（大部分位置为零或关于主对角线对称）进入，说明下面逐类定义并举例；它们在乘法下的固定模式在8.2.5.3（`sec:ls-common-matrix-products`）中随乘法讨论，依赖内积的正交矩阵与正定矩阵留到第~`chap:normed-inner-product-spaces`章。

###### paragraph：方阵

定义方阵、阶与主对角线，举二阶例与非方阵例，并说明下面的对角矩阵和三角矩阵都限定为方阵。

###### paragraph：零矩阵

定义全零矩阵，说明它不要求是方阵、需要时写明形状。

###### paragraph：对角矩阵

定义$\operatorname{diag}(d_1,\ldots,d_n)$，指出对角元本身可以为零并举二阶、三阶例。

###### paragraph：单位矩阵

定义对角元全为1的$\bm I_n$，指出其第$j$列就是$\bm e_j$。

###### paragraph：上三角矩阵

定义主对角线以下全为零的方阵并举例。

###### paragraph：下三角矩阵

定义主对角线以上全为零的方阵，并说明对角矩阵同属两类三角矩阵。

###### paragraph：对称矩阵

定义关于主对角线镜像对称的方阵，说明有了转置后条件写作$\bm A^\top=\bm A$，对角矩阵都对称。

###### paragraph：置换矩阵

定义由单位矩阵重排各列得到的置换矩阵，说明每行每列恰有一个1，以二阶交换矩阵与三阶循环置换举例，交换坐标的作用留到定义乘法后验证。

#### 8.2.2 加法与数乘

1. 说明加法与数乘沿用向量的逐项规则，给出同形矩阵逐项加减与数乘的元素公式，指出结果形状不变；示例`ex:ls-matrix-addition-scaling`对一组二阶矩阵逐项计算，以$(2,1)$元核对。

2. 说明相加要求形状相同、对应位置含义相同；以$2\times3$与$3\times2$矩阵说明元素个数相同也不能相加，并指出同形矩阵的线性组合按同样方式定义。

##### 8.2.2.1 加法与数乘的性质

1. 由逐项运算说明向量的八条规则在每个位置上照样成立，列出同形矩阵的八条规则，并指出每条都可在任一位置上用实数运算验证。

#### 8.2.3 转置

1. 用$(\bm A^\top)_{j,i}=\bm A_{i,j}$定义转置，说明形状交换而数值不变、第$i$行成为第$i$列，并与向量的转置一致；示例`ex:ls-transpose-two-by-three`转置一个$2\times3$矩阵。

##### 8.2.3.1 转置的性质

1. 说明转置只改变元素位置，本小节只给出它与加法、数乘的关系及转置两次的结果；与矩阵乘积的关系待定义乘法后在8.2.5.2讨论。

###### paragraph：与加法、数乘交换

说明转置只搬动元素，因而$(\bm A+\bm B)^\top=\bm A^\top+\bm B^\top$、$(c\bm A)^\top=c\bm A^\top$。

###### paragraph：转置的转置

列出$(\bm A^\top)^\top=\bm A$：$(i,j)$元先搬到$(j,i)$再搬回。

#### 8.2.4 矩阵与向量的乘积

1. 由$n$次观测共用一组权重的加权和引出$\bm A\bm u$，给出元素定义（式`eq:prelim-matrix-prediction`），要求矩阵列数等于向量维数。

2. 说明按行（各行与$\bm u$的内积）与按列（各列以$u_j$为系数的线性组合）两种算法结果相同；由按列算法得$\bm A\bm e_j=\bm A_{:,j}$，并指出贯穿例$\bm X_\varepsilon\bm w=w_1\bm c_1+w_2\bm c_2$。示例`ex:ls-matrix-vector-rows-columns`核对两种算法。

3. 示例`ex:ls-affine-predictions`在$x=1,2,3$处计算$ax+b$，说明全$1$列给出截距；再写出残差$\bm X\bm w-\bm y$与平方误差总和$\lVert\bm X\bm w-\bm y\rVert_2^2$，并把结论推广到$n$个样本、$d$个特征。

#### 8.2.5 矩阵乘法

1. 由两次加权求和$\bm y=\bm B\bm x$、$\bm z=\bm A\bm y$的复合出发，逐坐标代入并交换有限求和次序（式`eq:linear-algebra-matrix-product`），说明$\bm z$仍是$\bm x$的加权和，括号中的系数排成的表就是乘积。

2. 给出元素公式（式`eq:prelim-matrix-composition`）与形状条件，指出被求和的公共维数就是中间结果的维数，并说明矩阵乘向量与内积（$1\times1$矩阵与其元素等同）是特例。

3. 以$2\times3$乘$3\times2$的非方阵算例说明左矩阵列数须等于右矩阵行数、输出保留左矩阵的行数与右矩阵的列数。

##### 8.2.5.1 矩阵乘法的性质

1. 说明矩阵乘法保留结合律和分配律、一般不满足交换律和消去律，逐条核对并检查形状要求。依次给出单位乘、零乘、结合律、分配律与分块乘法，再说明交换律与消去律不成立；乘积的转置与常见矩阵的乘法模式分别放在其后两小节。

###### paragraph：单位乘

1. 用$\bm I_m$的第$i$行是$\bm e_i^\top$说明$\bm I_m\bm A=\bm A=\bm A\bm I_d$，单位矩阵相当于数$1$。

###### paragraph：零乘

1. 给出$\bm0\bm A=\bm0$与$\bm A\bm0=\bm0$，说明一个因子全为零时乘积为零，零矩阵的形状由另一个因子决定。

2. 指出逆命题不成立：示例`ex:ls-zero-product-nonzero-factors`给出两个非零矩阵的乘积为零。

3. 按列解释原因：$\bm A\bm B$的第$j$列是$\bm A$乘$\bm B$的第$j$列，$\bm A\bm B=\bm0$恰好意味着$\bm B$的每一列都被$\bm A$清零；回到示例说明两列如何被清零。

###### paragraph：结合律

1. 展开两边元素都为$\sum_k\sum_l a_{i,k}b_{k,l}c_{l,j}$，指出这是函数复合结合律的矩阵形式；取$\bm C$为列向量回到引出乘法定义的计算，并说明连乘可省略括号。

###### paragraph：分配律与数乘相容

1. 逐项展开有限和得到两条分配律与数乘相容，并以右因子取列向量得到矩阵与向量的乘积保持线性组合（式`eq:prelim-matrix-linearity`）。

2. 由此说明$\bm u\mapsto\bm A\bm u$由它在$\bm e_1,\ldots,\bm e_d$上的输出即$\bm A$的各列完全确定，并说明第~`chap:linear-representation`章将这样的函数称为线性映射。

###### paragraph：分块乘法

1. 以$2\times2$分块写出块乘公式，给出块尺寸相容的条件，并用中间索引的求和可按列块分段说明理由；指出块的次序不能交换。

2. 把块分到最细，得到按列、按行与“列乘行之和”（式`eq:ls-product-outer-sum`）三种特例，说明后者是低秩近似的出发点；示例`ex:ls-product-as-outer-sum`把一个二阶乘积写成两个“列乘行”矩阵之和，与逐项计算的结果核对。

###### paragraph：交换律不成立

1. 说明形状不同时两种次序未必都有定义，同阶方阵的两种乘积也可能不同；示例`ex:ls-noncommuting-pair`用“只保留第一个坐标”与“交换两个坐标”说明两种作用次序结果不同，并约定作用顺序从右向左。

###### paragraph：消去律不成立

1. 由$\bm A\bm B=\bm A\bm C$等价于$\bm A(\bm B-\bm C)=\bm0$，借零乘的反例说明非零左因子不能消去；示例`ex:ls-cancellation-fails`给出具体反例。

2. 回指第~`sec:prelim-inverse-matrices`节，说明左因子可逆时两边左乘逆矩阵即可消去。

##### 8.2.5.2 转置与乘积

1. 回指8.2.3.1的转置性质只涉及加法、数乘与转置本身，说明乘法把行与列配对求和、转置交换行与列，因此需要单独考察乘积转置后因子的排列；本小节先给出规则，再给出内积与对称性两个推论。

###### paragraph：乘积的转置

逐元素推出$(\bm A\bm B)^\top=\bm B^\top\bm A^\top$，并推广到多个因子时次序整体反转。

###### paragraph：内积中的转置

由乘积的转置得到$\langle\bm A\bm x,\bm y\rangle=\langle\bm x,\bm A^\top\bm y\rangle$，说明作用在左侧向量上的$\bm A$可改写为作用在右侧向量上的$\bm A^\top$。

###### paragraph：$\bm A^\top\bm A$对称

由乘积的转置证明$\bm A^\top\bm A$与$\bm A\bm A^\top$总是对称矩阵，示例`ex:ls-gram-product-symmetric`对一个$2\times3$矩阵算出$\bm A\bm A^\top$，其两个非对角元都是两行的内积。

##### 8.2.5.3 常见矩阵的乘法

1. 回指8.2.1.1的常见矩阵，说明它们参与乘法时结果有固定模式，下面逐类说明；对称矩阵一类要用到上一小节的乘积转置规则。

###### paragraph：对角矩阵的乘法

1. 由乘积公式只剩一项说明左乘对角矩阵缩放各行、右乘缩放各列，作用在向量上是逐坐标缩放；两个对角矩阵相乘对角元逐个相乘，因而可交换。

2. 示例`ex:ls-diagonal-scaling`比较左乘与右乘，说明与一般矩阵相乘仍须区分左右。

###### paragraph：三角矩阵的乘法

1. 由只有$i\leq\ell\leq j$的项可能非零，证明两个上三角矩阵的乘积仍是上三角矩阵且对角元逐个相乘，下三角同理；示例`ex:ls-upper-triangular-product`给出二阶算例。

###### paragraph：置换矩阵的乘法

1. 给出左乘置换矩阵移动行、右乘置换矩阵重排列的公式，以二阶交换矩阵举例。

2. 证明两个置换矩阵的乘积各列是互不相同的标准坐标向量，因而仍是置换矩阵。

###### paragraph：对称矩阵的乘积

1. 由$(\bm A\bm B)^\top=\bm B\bm A$得到两个对称矩阵的乘积对称当且仅当二者可交换；示例`ex:ls-symmetric-product-not-symmetric`给出乘积不对称的反例，并用判据核对。

#### 8.2.6 逐项乘积

1. 与对公共索引求和的矩阵乘法对照，定义只在同一位置相乘的Hadamard积（式`eq:ls-hadamard`），并推广到同维向量和同形数组。

2. 示例`ex:ls-hadamard-vs-matrix-product`对同一对矩阵分别计算两种乘积，结果在每个位置都不同；最后说明固定掩码$\bm M$时$\bm X\mapsto\bm M\odot\bm X$适合表达挑选或调制另一个数组。

##### 8.2.6.1 逐项乘积的性质

1. 说明逐项乘积在每个位置上只是实数乘法，规则都可逐位置推出。

###### paragraph：交换律

由实数乘法可交换得到$\bm A\odot\bm B=\bm B\odot\bm A$，并与矩阵乘积不可交换对照。

###### paragraph：结合律

两边的$(i,j)$元素都是$a_{i,j}b_{i,j}c_{i,j}$。

###### paragraph：分配律

两边的$(i,j)$元素都是$a_{i,j}(b_{i,j}+c_{i,j})$。

###### paragraph：单位元是全$1$数组

说明全$1$数组是单位元，而$\bm I_2\odot\bm A$只保留对角元，单位矩阵不是逐项乘积的单位元。

###### paragraph：对每个因子分别线性

说明固定一个因子时保持线性组合，两个因子都可变时只对每个因子分别线性（同时放大两倍结果放大四倍）；并说明第~`chap:linear-representation`章换记录方向后，矩阵乘积表示的复合关系不变，逐项乘积则随记录方式改变。

#### 8.2.7 初等行变换与阶梯形

1. 从解方程和求逆需要把矩阵逐步化简、且每步可撤销进入，定义三种初等行变换及其逆操作。

2. 说明每种行变换等于左乘对单位矩阵执行同一变换所得的初等矩阵，逆操作也对应初等矩阵，因而初等矩阵可逆。

3. 描述逐列寻找主元、换行、消去下方元素并跳过无主元列的过程，定义行阶梯形与行最简形。

4. 用增广矩阵$[\bm A\mid\bm b]$处理方程，说明三种行变换对应等式的可撤销操作，故不改变解；示例`ex:ls-elementary-row-reduction`演示首元为零时换行、消元，读出主元列、自由变量$x_3=t$与通解，并说明零行与矛盾行的含义。

5. 指出阶梯形使主元与自由变量可见，但主元选择影响数值误差，选主元与计算代价留到第~`sec:ls-direct-methods`节。

#### 8.2.8 逆矩阵

1. 以“撤销一次矩阵乘法”引出可逆与逆矩阵的定义（两侧乘积都等于$\bm I_n$）。

2. 证明可逆时方程$\bm A\bm x=\bm y$有唯一解$\bm A^{-1}\bm y$：左乘逆矩阵得唯一性，代回得存在性。

3. 由结合律证明逆矩阵唯一，因而记号$\bm A^{-1}$无歧义；随后一句说明求逆方法取决于矩阵结构，依次讨论对角矩阵、二阶方阵与一般方阵。

###### paragraph：对角矩阵的逆

对角元全非零时逐个取倒数得到逆；某个对角元为零时，左乘后乘积有一行为零，不可能等于$\bm I_n$，因而不可逆。

###### paragraph：二阶方阵的逆

给出$ad-bc\neq0$时的二阶求逆公式，以左上与右上元素核对乘积为单位矩阵，并指出分母是下一节的二阶行列式。

###### paragraph：一般方阵的逆

1. 由$\bm A^{-1}$的第$j$列是$\bm A\bm x=\bm e_j$的解，说明求逆就是同时解$n$个方程；对$[\bm A\mid\bm I_n]$作行变换，若左侧化为$\bm I_n$，则各步初等矩阵之积$\bm E$满足$\bm E\bm A=\bm I_n$且可逆，从而$\bm A\bm E=\bm I_n$，右侧即$\bm A^{-1}$。

2. 示例`ex:ls-inverse-by-solving`对一个三阶方阵先消下方、再自下而上消上方，求出逆矩阵并核对，指出逆矩阵不能逐元素取倒数。

3. 说明找不到主元时左侧出现零行、矩阵不可逆；只解一个方程时不必先求逆，可逆判据与稳定求解留到第~`chap:linear-equations-and-optimization`章。

###### paragraph：单侧逆

1. 定义矩形矩阵的左逆与右逆。

2. 说明有左逆时方程若有解则只能是$\bm L\bm y$，有右逆时$\bm R\bm y$总是一个解。

3. 指出单侧逆一般不唯一，示例`ex:ls-left-inverse-not-unique`给出无穷多个左逆；随后一句回到可逆方阵，说明下面四条规则说明可逆性在乘积、求逆、数乘与转置下保持。

###### paragraph：乘积的逆

1. 定理`thm:ls-inverse-product`陈述可逆方阵之积可逆且$(\bm A\bm B)^{-1}=\bm B^{-1}\bm A^{-1}$（式`eq:ls-inverse-product`），证明用结合律验证两侧乘积并引用逆的唯一性。

2. 用作用次序解释次序反转：先作用$\bm B$后作用$\bm A$，撤销时先撤销$\bm A$。

###### paragraph：逆的逆

由定义中$\bm A$与$\bm A^{-1}$地位对称得到$(\bm A^{-1})^{-1}=\bm A$。

###### paragraph：数乘的逆

直接相乘验证$(c\bm A)^{-1}=c^{-1}\bm A^{-1}$（$c\neq0$）。

###### paragraph：转置的逆

由乘积的转置验证$(\bm A^\top)^{-1}=(\bm A^{-1})^\top$。

#### 8.2.9 矩阵的幂

1. 以同一方阵反复作用引出正整数幂、$\bm A^0=\bm I_d$与可逆时的负幂，并说明非方阵没有幂。

2. 示例`ex:ls-matrix-square-shear`说明矩阵平方不是逐元素平方。

3. 定义幂等矩阵与幂零矩阵；示例`ex:ls-idempotent-nilpotent`用$\operatorname{diag}(1,0)$与右上元为$1$、其余元素为$0$的二阶矩阵$\bm N$各举一例，从作用和直接相乘两方面验证。

##### 8.2.9.1 幂的性质

说明同一矩阵的幂满足与实数相同的指数法则，并给出指数的取值范围（可逆时可取任意整数）。

###### paragraph：同底幂相乘

1. 由结合律与相邻$\bm A\bm A^{-1}$逐对消去得到$\bm A^m\bm A^n=\bm A^{m+n}$，并指出同一矩阵的不同次幂可交换。

2. 与之对照，不同矩阵一般不交换，故$(\bm A+\bm B)^2$的中间两项只有在$\bm A\bm B=\bm B\bm A$时才能合并。

###### paragraph：幂的幂

由结合律去括号得到$(\bm A^m)^n=\bm A^{mn}$。

###### paragraph：负幂与逆相容

对$k$个相同因子反复使用式`eq:ls-inverse-product`得到$(\bm A^k)^{-1}=(\bm A^{-1})^k=\bm A^{-k}$。

### 8.3 行列式、迹与元素内积

1. 说明本节讨论三种把矩阵变成一个数的运算：行列式衡量有向体积的缩放，迹累加主对角元，Frobenius内积配对两个同形矩阵的对应元素；三者回答的问题不同，单凭一个数无法恢复矩阵。

#### 8.3.1 行列式

1. 用一句说明本小节的顺序：计算公式、几何意义、性质，最后由代数余子式构造古典伴随并证明方阵的单侧逆即逆。

##### 8.3.1.1 行列式的定义

1. 定义排列、逆序对数与符号，给出排列公式定义`def:ls-determinant`，解释每项从每行每列各取一个元素，行列式是元素的多项式。

2. 把每项按列号重排并用$\operatorname{sgn}(\pi^{-1})=\operatorname{sgn}(\pi)$得到按列的写法（式`eq:ls-det-column-form`）。

3. 由两个排列得到二阶公式$ad-bc$；由六个排列的奇偶得到三阶公式，示例`ex:ls-det-three-by-three`代入计算得$7$，并指出高阶时借助性质与消元计算。

##### 8.3.1.2 行列式的几何意义

1. 说明排列公式看不出度量什么，本小节从平行四边形面积与平行六面体体积满足的几何规则出发推出同一公式。

###### paragraph：有向面积

1. 按转向给平行四边形面积配符号，定义有向面积$S(\bm u,\bm v)$，给出三条规则：以一边为底、有向高是另一边在法方向上的分量，故对每边线性；交换两边变号，共线时为零；单位正方形面积为$1$。

2. 把两边按坐标展开成四项，用三条规则得到$u_1v_2-u_2v_1$，即二阶行列式。

3. 示例`ex:ls-oriented-area`用三组向量对说明交换次序变号、共线时面积为零。

###### paragraph：有向体积

1. 按右手系定义平行六面体的有向体积$V(\bm u,\bm v,\bm w)$，以底面积乘有向高说明对每条棱线性，交换两棱变号，单位立方体体积为$1$。

2. 展开成$27$项：下标重复的项为零；其余六项对应排列，每次相邻交换使逆序对数减一，故系数为$\operatorname{sgn}(\sigma)$，得到三阶行列式。

###### paragraph：一般维数

1. 指出展开只用到对每个向量线性与交换变号两条规则，得到式`eq:ls-det-volume`：满足两条规则的函数$D$等于$D(\bm e_1,\ldots,\bm e_d)$乘以行列式；反过来验证排列公式满足两条规则，故行列式是满足规则且在单位矩阵处取$1$的那个函数。

2. 取$D$为$d$维有向体积、代入$\bm a_j=\bm A\bm e_j$，说明$\det\bm A$是$\bm A$作用下有向体积的放大倍数：绝对值是体积比，符号表示定向；图`fig:ls-determinant-oriented-volume`展示平面上保定向与反定向两种情形。

##### 8.3.1.3 行列式的性质

1. 说明行列式是各列张成的有向体积，前两条性质就是有向体积的两条规则，其余由它们和排列公式推出。

###### paragraph：对列的多线性

写出同一列线性组合时的多线性公式。

###### paragraph：交替性

1. 说明交换两列变号、两列相同为零及其理由。

2. 推出加某列倍数不改变行列式、某列是其余列的线性组合时行列式为零，以第二列为第一列两倍的二阶矩阵单独成行举例。

###### paragraph：行变换与可逆性

1. 由排列公式每项从每行恰取一个元素、交换两行相当于与对换复合，直接得到对行的线性与交替性，并分行列出三种初等行变换对行列式的影响。

2. 由消元每步只乘非零数，分有无主元两种情形：有零行时由对该行的线性得行列式为零，各列都有主元时可化为单位矩阵且$\det\bm I=1$，得到方阵可逆当且仅当行列式非零，单独一行写出判据。

###### paragraph：转置

由$\bm A^\top$的排列公式正是按列写法得到$\det\bm A^\top=\det\bm A$，说明行列式对行和对列的性质完全对称。

###### paragraph：数乘与加法

由每列提出一个$c$得$\det(c\bm A)=c^d\det\bm A$，指出行列式对整个矩阵不是线性的；示例`ex:ls-det-not-additive`以$\bm A=\bm B=\bm I_2$给出反例。

###### paragraph：乘法性

从体积倍数应相乘的直观出发，固定$\bm A$，把$\det(\bm A\bm B)$看作$\bm B$各列的函数，验证它对每列线性、交换两列变号，再由式`eq:ls-det-volume`证明$\det(\bm A\bm B)=\det\bm A\det\bm B$，并推出$\det(\bm A\bm B)=\det(\bm B\bm A)$。

###### paragraph：三角矩阵的行列式

1. 由非恒等排列必取到对角线下方的零元素，证明三角矩阵行列式等于对角元之积，以单独成行的三阶上三角矩阵举例，给出对角矩阵的情形，并由乘法性与三角矩阵乘积的对角元结论对照。

2. 结合行变换的规则，以一个三阶例子演示用消元化为上三角矩阵并补偿换行符号来计算行列式。

##### 8.3.1.4 代数余子式与古典伴随

1. 说明按行分组把排列公式化为低阶行列式，再把这些低阶行列式排成与$\bm A$相乘得$(\det\bm A)\bm I_d$的矩阵。

###### paragraph：按行（列）展开

定义子矩阵$\bm A^{(i,j)}$与代数余子式，按第$i$行所取的列分类得到展开公式；示例`ex:ls-det-cofactor-expansion`沿第一行展开示例`ex:ls-det-three-by-three`的矩阵，结果一致。

###### paragraph：古典伴随恒等式

1. 定义古典伴随$\operatorname{adj}(\bm A)=\bm C^\top$，定理`thm:ls-adjugate-identity`给出$\bm A\operatorname{adj}(\bm A)=\operatorname{adj}(\bm A)\bm A=(\det\bm A)\bm I_d$，证明区分$i=k$的展开与$i\neq k$时换行后两行相同。

2. 指出二阶情形就是二阶求逆公式。

3. 区分古典伴随与第~`sec:ls-inner-product-spaces`节由内积定义的伴随，说明其阶乘级代价使它主要作为证明工具，并列出它在单侧逆、第~`sec:ls-determinant-invertibility`节可逆判据与第~`sec:ls-characteristic-polynomial`节Cayley--Hamilton定理中的用途。

###### paragraph：方阵的单侧逆即逆

1. 回指第~`sec:prelim-inverse-matrices`节要求两侧乘积为单位矩阵，定理`thm:ls-square-one-sided-inverse`说明方阵只需一侧；证明由乘法性得$\det\bm A\neq0$，用古典伴随构造逆，再用结合律说明单侧逆等于它。

2. 指出检验方阵的逆只需一侧乘积，并与矩形矩阵单侧逆可能只存在一侧或不唯一（示例`ex:ls-left-inverse-not-unique`）对照。

#### 8.3.2 迹

1. 与用到全部元素的行列式对照，定义方阵的迹为主对角元之和，以二阶例子区分迹与全部元素之和。

##### 8.3.2.1 迹的性质

1. 说明前两条可直接看出，循环性最常用。

###### paragraph：线性

由有限和的线性得到迹的线性。

###### paragraph：转置不变

转置不改变对角元。

###### paragraph：循环性

1. 用交换双重求和次序证明$\operatorname{tr}(\bm A\bm B)=\operatorname{tr}(\bm B\bm A)$（式`eq:linear-algebra-trace-cyclic`），强调两个乘积可以不同阶；示例`ex:ls-trace-cyclic-different-sizes`以$1\times1$与$3\times3$乘积核对。

2. 说明三个因子时只能整体循环移动，并解释两个等号各把哪两部分看作因子；示例`ex:ls-trace-adjacent-swap`给出交换相邻因子改变迹的反例。

#### 8.3.3 矩阵的元素内积

1. 说明行列式与迹只用到一个方阵，比较两个同形矩阵时可像向量内积那样配对全部对应元素。

##### 8.3.3.1 Frobenius内积

1. 把$mn$个元素看作坐标照搬欧氏内积，定义Frobenius内积并指出它等于$\bm A\odot\bm B$的元素和；示例`ex:ls-frobenius-inner-product`沿用逐项乘积一例的矩阵得到$5$。

###### paragraph：Frobenius内积的迹表示

由$\bm A^\top\bm B$的对角元证明$\langle\bm A,\bm B\rangle_{\mathrm F}=\operatorname{tr}(\bm A^\top\bm B)$与$\lVert\bm A\rVert_{\mathrm F}^2=\operatorname{tr}(\bm A^\top\bm A)$；反过来说明计算$\operatorname{tr}(\bm A\bm B)$不必先求乘积，比较$mn$与$m^2n$次乘法的代价。

##### 8.3.3.2 Frobenius范数

1. 由Frobenius内积定义Frobenius范数并举例，说明它是元素排成一列后的$2$范数，范数性质见第~`sec:ls-normed-space-definition`节。

2. 从作用解释$\lVert\bm A\rVert_{\mathrm F}^2=\sum_j\lVert\bm A\bm e_j\rVert_2^2$，区分它与最坏输入的放大倍数，后者在第~`sec:ls-matrix-norms`节讨论。

3. 简述按组汇总的混合范数$\lVert\bm A\rVert_{p,q}$。

### 8.4 张量

1. 从图像、文本数组需要三个以上索引进入，说明本节先给记法，再按对轴的作用讨论三类运算（重排、张量积与Kronecker积、缩约）并各自整理性质，最后指出内积、矩阵乘法与迹都是缩约。

#### 8.4.1 张量的表示与重排

1. 由多路索引引出张量，给出多维数值数组的定义`def:linear-algebra-multidimensional-array`（轴、阶、形状），说明向量、矩阵、标量分别是一、二、零阶数组，轴长不改变阶。

2. 以$\bm X\in\mathbb R^{b\times\ell\times d}$说明三个索引与切片，图`fig:ls-scalar-vector-matrix-tensor`并排比较四类数组。

3. 说明同形数组逐项加法与数乘照旧，并强调须先说清每条轴的含义，否则汇总会落在错误的轴上。

4. 转入第一类运算：轴置换与形状重整只改变元素位置，不改变数值、不求和。

##### 8.4.1.1 轴置换

1. 定义维度重排（轴置换），以交换后两条轴为例写出$y_{i,k,j}=x_{i,j,k}$，指出每个样本切片被转置；示例`ex:ls-axis-swap`给出具体小数组。

2. 指出两条轴时唯一不平凡的轴置换就是转置，并说明轴的含义跟着轴走。

##### 8.4.1.2 形状重整与向量化

1. 定义形状重整为“按遍历顺序读出、再按同序装入”，只要求元素总数不变；示例`ex:ls-reshape-vs-transpose`比较按行重整与转置，图`fig:vol1-add-linear-transpose-reshape`并排展示，说明重整须给出遍历顺序。

2. 定义按列堆叠的向量化及元素$a_{i,j}$的位置$i+(j-1)m$，以示例矩阵核对。

3. 说明矩阵展开把部分轴合并为行、其余合并为列，所选的轴决定形状与后续汇总的轴。

##### 8.4.1.3 重排的性质

1. 用一句概括三条性质：不丢失信息、与逐项运算可交换、一般重整与矩阵乘法不相容。

###### paragraph：可逆性

说明固定形状与遍历顺序后重排一一对应、可由逆操作恢复，给出$\operatorname{vec}^{-1}$的装回方式。

###### paragraph：线性

说明向量化、轴置换与形状重整都保持线性组合，因为它们只搬动元素。

###### paragraph：与矩阵乘法的关系

对照转置与乘法的规则，说明一般重整改变每行每列汇集的元素；示例`ex:ls-reshape-breaks-product`把重整结果误当转置，两个乘积的迹分别为$91$与$86$，并指出把存储格式改变误当计算变换是常见错误。

#### 8.4.2 张量积

1. 转入第二类运算，定义两个向量的张量积$(\bm x\otimes\bm y)_{i,j}=x_iy_j=\bm x\bm y^\top$，联系“列乘行”（式`eq:ls-product-outer-sum`），引入槽位并推广到多个因子；示例`ex:ls-tensor-product-two-vectors`计算二维例，说明各行、各列分别成比例。

2. 图`fig:ls-tensor-product-slots`用长度不同的两个因子展示行轴与列轴的槽位。

3. 给出任意数组的张量积定义，说明输出有$k+\ell$条轴、不求和，交换输入会交换两组轴的次序。

4. 定义简单张量，示例`ex:ls-identity-not-simple`证明$\bm I_2$不是简单张量；再说明每个二阶数组都是简单张量$\bm e_i\otimes\bm f_j$的和。

5. 说明张量积的用处：双线性函数$B(\bm x,\bm y)=\langle\bm G,\bm x\otimes\bm y\rangle_{\mathrm F}$由系数表$\bm G$决定且对$\bm x\otimes\bm y$线性，以欧氏内积$\bm G=\bm I$为例。

6. 指出二阶张量与矩阵是同一组数的两种看法。

##### 8.4.2.1 张量积的性质

1. 说明以下性质都从元素公式逐槽位验证。

###### paragraph：对每个因子线性

列出数乘与两侧加法的线性规则，由$x_iy_j$分别线性逐项验证。

###### paragraph：结合律

两边的$(i,j,k)$元素都是$x_iy_jz_k$。

###### paragraph：交换槽位是转置

证明$\bm y\otimes\bm x=(\bm x\otimes\bm y)^\top$，说明两者相差一次轴置换。

###### paragraph：Frobenius配对与范数分离

由双重和分离成两个单和的乘积得到配对公式与$\lVert\bm x\otimes\bm y\rVert_{\mathrm F}=\lVert\bm x\rVert_2\lVert\bm y\rVert_2$；示例`ex:ls-tensor-product-norm-check`数值核对得$\sqrt{50}$。

###### paragraph：与行列式的联系

说明反对称化$\bm x\otimes\bm y-\bm y\otimes\bm x$的$(i,j)$元素是二阶行列式$x_iy_j-x_jy_i$，即$\bm x,\bm y$在第$i,j$坐标平面上投影张成的有向面积（第~`sec:ls-exterior-determinants`节），交换两者时变号。

#### 8.4.3 Kronecker积

1. 由两个矩阵分别作用在两条轴上的联合作用引出Kronecker积（式`eq:linear-algebra-kronecker-product`），说明把每个元素替换为块；示例`ex:ls-kronecker-two-by-two`计算二阶例，图`fig:ls-kronecker-block-structure`展示分块结构。

2. 说明Kronecker积与张量积共用记号$\otimes$、记录同一组数而排法不同：两个列向量的Kronecker积是$\bm x\otimes\bm y$按行读出的结果，以$(3,-1,6,-2)^\top$核对；一般矩阵时张量积保留四条轴而Kronecker积排成两条，须按上下文和输出形状区分。

##### 8.4.3.1 Kronecker积的性质

1. 说明以下规则都用块运算验证，向量化恒等式将用于矩阵方程。

###### paragraph：分别作用于两个槽位

按分块乘法证明$(\bm A\otimes\bm B)(\bm x\otimes\bm y)=(\bm A\bm x)\otimes(\bm B\bm y)$，对照两个作用并排进行与矩阵乘法的串联。

###### paragraph：混合乘积

按块$(i,k)$证明混合乘积公式（式`eq:matrix-analysis-kronecker-mixed-product`），并指出上一条是其特例。

###### paragraph：转置

由块位置交换、每块各自转置得到$(\bm A\otimes\bm B)^\top=\bm A^\top\otimes\bm B^\top$。

###### paragraph：逆

由混合乘积验证$(\bm A\otimes\bm B)^{-1}=\bm A^{-1}\otimes\bm B^{-1}$。

###### paragraph：迹

由只有对角块的对角元落在主对角线上得到$\operatorname{tr}(\bm A\otimes\bm B)=\operatorname{tr}\bm A\operatorname{tr}\bm B$。

###### paragraph：向量化恒等式

1. 比较两侧输出的第$j$段，证明$\operatorname{vec}(\bm A\bm X\bm B)=(\bm B^\top\otimes\bm A)\operatorname{vec}(\bm X)$（式`eq:matrix-analysis-vec-kronecker`），并给出逐元素形式。

2. 说明它把关于未知矩阵的方程化为普通线性方程组，第~`chap:linear-equations-and-optimization`章将用到。

#### 8.4.4 指标缩约

1. 与保留全部槽位的张量积对照，说明缩约选定长度相同的轴对、共用求和索引并消去这些轴；示例`ex:ls-contraction-shapes`给出消去两对轴得$m\times n$矩阵、消去一对轴得$b\times\ell\times h$数组两种情形。

2. 图`fig:ls-tensor-contraction`展示沿列轴求和，并说明这也是与全$1$向量的缩约。

3. 逐项说明内积、矩阵乘法、迹与Frobenius内积都是缩约，指出各自消去哪些轴。

##### 8.4.4.1 缩约的性质

1. 说明缩约只由有限次乘法与求和组成，因此满足以下规则。

###### paragraph：线性

以示例`ex:ls-contraction-shapes`（2）为例展开，说明固定配对数组后缩约对被作用数组线性，一般情形中每个输出元素都是固定系数的加权和。

###### paragraph：求和次序可交换

说明多对轴的缩约与先消去哪一对无关，以$c_{i,j}$两种求和次序为例。

###### paragraph：简单张量系数可分离

证明系数为简单张量时三重求和分离为三个内积之积（式`eq:linear-algebra-rank-one-contraction`），计算量从$mnp$降到$m+n+p$；示例`ex:ls-rank-one-contraction-check`数值核对得$8$。

###### paragraph：非线性操作不是缩约

由缩约满足$\mathcal C(2\bm X)=2\mathcal C(\bm X)$，用逐元素平方说明逐元素非线性操作与$\operatorname{softmax}$不是缩约，并指出由缩约与非线性操作交替组成的模型不能因每步缩约线性就推出整体线性。

### 8.5 本章小结

1. 回顾本章按索引个数组织，并对每种运算交代输入条件、输出形状与规则。

2. 概括向量部分：逐坐标的加法与数乘组成线性组合，内积配对、长度与$p$范数衡量大小，一般性质留到第~`chap:normed-inner-product-spaces`章。

3. 概括矩阵部分：乘法来自复合，满足结合律与分配律而不满足交换律与消去律；可撤销的行变换给出阶梯形、主元与自由变量，并用于求逆；逆撤销一次乘法，幂记录反复作用。

4. 概括行列式、迹与Frobenius内积：行列式是有向体积的缩放倍数且非零恰对应可逆，由古典伴随得到方阵单侧逆即逆；迹累加对角元并有循环性；Frobenius内积配对全部元素并给出Frobenius范数。

5. 概括张量部分：重排只改位置，张量积与Kronecker积保留全部轴，缩约沿指定轴求和，内积、矩阵乘法与迹都是缩约。

6. 按对索引的处理（配对求和、同位置相乘、全部保留）区分各种乘积，表`tab:linear-algebra-products-and-shapes`汇总形状条件与索引作用，并给出遇到乘积记号时的检查顺序。

7. 说明后续章节的分工：第~`chap:linear-representation`章讨论数组记录的对象与线性映射，第~`chap:normed-inner-product-spaces`章讨论一般空间的大小、夹角与正交，第~`chap:linear-analysis`章讨论反复作用与误差放大，第~`chap:linear-equations-and-optimization`章讨论方程求解。

## 第9章 线性空间、映射与坐标

正文入口：[02-linear-spaces.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/02-linear-spaces.tex)。

1. 指出第~`chap:linear-operations`章没有区分数组与它记录的对象：以仿射函数$f_{a,b}(t)=a+bt$为例，函数本身可以相加缩放，选定$1$与$t$后才记成$(a,b)^\top$，换一组基本函数则记录改变而函数不变。

2. 再以设计矩阵$\bm X_\varepsilon$（式`eq:linear-algebra-nearly-collinear-design`）说明矩阵既是数表，也记录从两个系数到三个拟合值的作用，由此提出本章任务：把对象与记录对象的数分开。

3. 说明路线的依赖：先确定线性组合进行的范围（线性空间与子空间），再选基把对象记成坐标；对象记录清楚后，记录保持线性组合的作用（线性映射的矩阵、核与像、换基）；最后讨论把向量读成一个数的线性泛函，并解释转置。

4. 交代范围：在实数域上展开，只用加法和数乘，长度、收敛与正交留给下一章。

### 9.1 线性空间与子空间

1. 承接章首，说明记录对象之前要先确定线性组合的范围；本节先定义线性空间，再讨论对线性组合封闭的部分（子空间）以及子空间的比较、合并与商空间。

#### 9.1.1 线性空间的定义与示例

1. 从数组、位移、信号与多项式都满足第~`sec:ls-vector-operation-rules`节的八条规则、而后续结论只依赖这些规则出发，统称这类集合为线性空间，“向量”从此指可作线性组合的对象。

2. 给出实线性空间定义`def:ls-real-vector-space`，区分封闭与运算规则两层要求，并说明有了这些规则，有限线性组合有确定意义，与数组的线性组合一致。

3. 简述复线性空间：规则相同而数乘允许复数；以$\mathbb C$在复数与实数数乘下分别需要一个与两个方向，说明标量范围改变线性结构，并说明本章其余推导在实数域中进行。

4. 以$\mathbb R^d$、全体$m\times d$矩阵与次数不超过$k$的多项式空间$P_k$为正例，指出章首的仿射函数全体就是$P_1$。

5. 示例`ex:ls-non-vector-space-sets`以$x_1=1$的集合（加法不封闭、不含零向量）与非负向量集合（数乘不封闭）为反例，结论是判断须逐项检查封闭与规则，不能只看形状。

#### 9.1.2 子空间、和与直和

1. 从一组方向能到达的对象、映射消去的输入与方程的解都只占空间一部分进入，说明本小节先给子空间的判定条件，再比较与合并子空间。

###### paragraph：子空间的判定

1. 定义对线性组合封闭的非空子集为子空间；取特殊系数得到加法、数乘封闭以及零向量与相反向量，其余规则自动继承，所以只需检查这一条。

2. 指出平凡子空间后，示例`ex:ls-subspace-checks`验证过原点直线与齐次方程组解集是子空间，不过原点的直线因不含零向量而不是子空间。

3. 补充说明不过原点的直线与$x_1=1$的约束集都是子空间的平移（仿射集合）；随后列出比较同一空间中子空间的四个方面——包含、交、和、直和，并说明它们不涉及长度或夹角。

###### paragraph：包含

1. 定义子空间之间的包含，说明较小的子空间也是较大子空间的子空间；包含只比较范围，“大小”要等下一节的维数。

###### paragraph：交

1. 证明交仍是子空间，且是同时含于二者的最大子空间。

2. 以平面中重合与不同的两条直线说明交为零只表示没有公共非零向量，再以$\mathbb R^3$中两条不同直线交为零、合起来只到达一个平面说明交为零不意味着能到达整个空间。

3. 把交与联立两组齐次方程对应，例如$\{x_1=0\}\cap\{x_2=0\}$，消元方法留给第~`chap:linear-equations-and-optimization`章。

###### paragraph：和

1. 定义和空间$U+W$，证明它对线性组合封闭，且是同时包含二者的最小子空间。

2. 说明并集虽是包含二者的最小集合，但一般对加法不封闭；示例`ex:ls-union-not-subspace`以两条坐标轴之并不含$\bm e_1+\bm e_2$为例，结论是和空间补入了必需的线性组合。

###### paragraph：直和与补空间

1. 从平面上两条不平行直线给出唯一分解的直观，指出唯一与否由两个子空间的交决定。

2. 定理`thm:ls-direct-sum-uniqueness`（和的分解唯一的条件）：$U+W$中分解唯一当且仅当$U\cap W=\{\bm0\}$；证明分充分性（两种分解之差落在交中）与必要性（交中非零向量给出零向量的两种分解）。

3. 定义直和$U\oplus W$，强调唯一分解不要求垂直。

4. 定义补空间，以平面直线说明补空间不唯一；存在性由下一节的基扩充证明（`sec:ls-dimension`），并区分一般补空间与第~`sec:ls-orthogonality`节的正交补。

#### 9.1.3 商空间

1. 与和、直和相反，提出有意忽略某个子空间内差别的需要：只关心截距时，$f_{a,b}$与$f_{a,b'}$之差落在$\{st\}$中而无区别。

2. 再以非齐次约束$x_1=1$的解集是特解加齐次解子空间为例，归纳共同点：相差某个子空间中的向量即视为相同。

3. 把这一点写成关系$\bm x\sim\bm y\iff\bm x-\bm y\in U$，逐条验证它是定义`def:prelim-equivalence-relation`意义下的等价关系。

4. 写出等价类$\bm x+U$即$U$的平移，说明类相等只要求代表元之差在$U$中，全部类划分$V$；图`fig:ls-quotient-equivalence-classes`以平面中平行于$x$轴的直线展示这种划分。

5. 借代表元定义类的加法与数乘，给出商空间定义`def:linear-algebra-quotient-space`。

6. 验证运算与代表元选取无关，再说明零类、相反类与其余规则的继承，得出$V/U$是线性空间；回到图例说明商空间只记录高度。

7. 示例`ex:ls-quotient-intercept`计算$P_1$对$\{st\}$的商：每个类只依赖截距，类相等当且仅当截距相等，运算即截距的相加缩放，$f_{a,b}+U\mapsto a$是保持运算的双射。

8. 指出商空间的维数在下一节计算（`sec:ls-dimension`），与线性映射的联系见第~`sec:ls-kernel-image`节。

### 9.2 基、维数与坐标

1. 说明本节用有限个数记录对象：先用张成与线性无关判断系数的存在与唯一，二者同时成立即为基，基的向量个数是维数；最后定义坐标并推导换基时的换算。

#### 9.2.1 张成与线性无关

###### paragraph：张成

1. 由平面上一个方向与两个不共线方向能到达范围的对比，定义张成空间（式`eq:ls-span`）。

2. 证明张成空间是子空间且是包含该组向量的最小子空间，定义生成组。

3. 在$\mathbb R^m$中按列读法把张成空间写成$\{\bm V\bm a\}$，指出它即后文的列空间；图`fig:ls-linear-combination-span`对比两个方向张成平面与一个方向只得直线。

###### paragraph：线性无关

1. 从同一对象有两组系数说明存在冗余，两组系数相减化为零向量的非平凡表示，据此定义线性无关与线性相关（式`eq:linear-algebra-independence-relation`）。

2. 说明线性相关时某个向量可由其余向量表示；在$\mathbb R^m$中线性无关即齐次方程只有零解，并预告Gram矩阵判据（第~`sec:ls-gram-orthogonality`节）。

3. 示例`ex:ls-nearly-collinear-independence`先验证$\bm c_1,\bm q$线性无关，再得出$\varepsilon\neq0$时贯穿例两列线性无关、$\varepsilon=0$时相关。

4. 据此区分线性无关这一精确的是非判断与描述接近退化程度的“几乎同向”，后者要用夹角或Gram矩阵衡量（近共线，第~`sec:ls-inner-product-definition`节）。

###### paragraph：表示的存在与唯一

1. 说明张成与线性无关分别回答能否表示与是否冗余；示例`ex:ls-redundant-spanning-set`在$\mathbb R^2$中对照足够且无冗余、不够、足够但冗余三种方向组，图`fig:vol1-add-linear-redundant-directions`画出冗余情形下同一目标的两种表示。

2. 把例子推广：存在性来自张成，唯一性来自线性无关（两组系数之差为零）。

3. 证明反向：零向量的非平凡表示加到任一表示上会产生第二组系数；所以系数唯一与零向量只有平凡表示是同一条件，这是定义坐标的依据。

#### 9.2.2 基与维数

1. 定义同时张成且线性无关的向量组为基，说明它可充当整个空间的“尺子”。

2. 验证$\mathbb R^d$的标准基与$P_k$的基$1,t,\ldots,t^k$。

3. 示例`ex:ls-solution-plane-basis`以$x_2,x_3$为自由系数，求出方程$x_1+2x_2+3x_3=0$解平面的一组基$\bm n_1,\bm n_2$，并核对张成与无关。

###### paragraph：基的抽取与扩充

1. 定义有限维空间，并限定本章只讨论有限维情形。

2. 抽取：从有限生成组反复删去可由其余向量表示的成员，张成范围不变，最终得到基。

3. 扩充：从线性无关组逐次加入张成空间之外的向量，证明新组仍线性无关；借交换引理`thm:ls-exchange-lemma`保证有限步内停止，停止时得到基。

4. 概括抽取压缩生成组、扩充补足无关组，并指出后面的证明常用扩充。

###### paragraph：维数

1. 说明用基的向量个数度量空间大小的前提是个数与基无关，给出交换引理`thm:ls-exchange-lemma`。

2. 证明交换引理：逐步把$\bm u_i$换入生成组、换出一个系数非零的$\bm v_j$而保持张成，若$r>s$则$\bm u_{s+1}$落入前$s$个$\bm u$的张成，矛盾。

3. 互换无关组与生成组的角色得任意两组基个数相同，定义维数$\dim V$，零空间维数为$0$。

4. 给出$\dim\mathbb R^d=d$、$\dim P_k=k+1$、解平面维数$2$、过原点直线维数$1$，并说明论证依赖有限生成组，不能直接用于无限维函数展开。

#### 9.2.3 子空间的维数与分解

1. 由$U\subseteq W$时$U$的基可扩充为$W$的基，得$\dim U\leq\dim W$，新增向量个数$\dim W-\dim U$表示$U$之外的独立方向数。

2. 包含且同维时扩充无需新增向量，故$U=W$；强调包含条件不可省略。

3. 示例`ex:ls-equal-dimension-not-nested`以两条不同直线说明同维不推出包含，维数只数方向个数、不记录方向位置。

4. 指出“先取已有的基、再补新方向”将用于和空间、补空间与商空间的维数，也是秩零度定理的证明思路。

###### paragraph：和空间

1. 说明公共方向在两边各计一次，因此从交的一组基出发计算。

2. 把交的基分别扩充为$U$与$W$的基，证明合并组张成$U+W$，并通过“移项后落在交中”逐步证明它线性无关。

3. 得到维数公式（式`eq:ls-dimension-formula`），说明减去的是重复计入的公共方向个数；示例`ex:ls-dimension-formula-planes`以$\mathbb R^3$中两个坐标平面核对$3=2+2-1$，并以两条坐标轴核对交为零时维数相加。

###### paragraph：补空间

1. 把$U$的基扩充为$V$的基，证明新增向量张成的$W$满足$U+W=V$且$U\cap W=\{\bm0\}$，从而补空间总存在。

2. 由维数公式得直和时$\dim V=\dim U+\dim W$，并说明扩充方式不唯一，所以补空间不唯一。

###### paragraph：商空间

1. 用同样的扩充，证明新增向量的类张成$V/U$（$U$部分落入零类）。

2. 证明这些类线性无关，得到$\dim(V/U)=\dim V-\dim U$（式`eq:ls-quotient-dimension`）。

3. 进一步说明补空间$W$与每个类恰交于一点，所以选定补空间就是为每个类选代表元；补空间需要选择，商空间不依赖选择。

4. 回到截距例与平面图例，核对商空间维数均为$1$。

#### 9.2.4 坐标与坐标变换

1. 说明本小节依次定义坐标并用它代替对象计算、说明坐标大小为何不能直接反映对象大小、推导换基的换算规则。

###### paragraph：有序基下的坐标

1. 固定有序基，把唯一的系数列定义为坐标$[\bm v]_{\mathcal B}$。

2. 由张成与线性无关说明坐标映射是从$V$到$\mathbb R^d$的双射，并证明它保持线性组合，因而线性运算可以在坐标上完成。

3. 在$\mathbb R^d$中坐标是$\bm B\bm x=\bm v$的唯一解；示例`ex:ls-coordinates-two-bases`求出$(1,2)^\top$在斜基$((2,1)^\top,(-1,1)^\top)$下的坐标$(1,1)^\top$，图`fig:ls-basis-coordinates`并排画出两种读法。

###### paragraph：坐标与对象

1. 区分可相加缩放的对象与选定基后记录它的坐标，说明基的顺序是坐标的一部分，$\mathbb R^d$默认标准基时二者恰为同一列数。

2. 示例`ex:ls-affine-function-coordinates`算出仿射函数在基$(1,t)$与$(1,1+t)$下的坐标$(a,b)^\top$与$(a-b,b)^\top$，函数不变而坐标改变。

3. 指出坐标个数等于维数，冗余生成组的记录长度不能用来推断维数。

###### paragraph：坐标对基的敏感性

1. 示例`ex:ls-coordinate-instability`取$\bm y=\bm c_1+\delta\bm q$（式`eq:linear-algebra-nearly-collinear-target`），比较它在$(\bm c_1,\bm q)$与近共线基$(\bm c_1,\bm c_2)$下的坐标（式`eq:linear-algebra-coordinate-instability`），$\delta=0.1$、$\varepsilon=0.01$时由$(1,0.1)^\top$变为$(-9,10)^\top$。

2. 解释两个大系数在几乎同向的基向量上大部分抵消，不能据此判断对象很大；定量讨论留给第~`chap:linear-analysis`章，并引出建立换基一般公式的需要。

###### paragraph：换基矩阵

1. 由坐标映射保持线性组合推出$[\bm v]_{\mathcal C}=\bm S_{\mathcal C\leftarrow\mathcal B}[\bm v]_{\mathcal B}$（式`eq:linear-algebra-coordinate-change`），说明各列是旧基向量的新坐标及下标的读法。

2. 示例`ex:ls-change-of-basis-plane`写出$\bm S_{\mathcal E\leftarrow\mathcal U}$并把$\mathcal U$坐标$(1,1)^\top$换成标准坐标$(2,1)^\top$；图`fig:vol1-add-linear-change-basis`说明目标位置不动，只改变沿哪些方向累加多少。

###### paragraph：连续换基与反向换基

1. 取基向量比较各列，推出连续换基的矩阵相乘$\bm S_{\mathcal D\leftarrow\mathcal B}=\bm S_{\mathcal D\leftarrow\mathcal C}\bm S_{\mathcal C\leftarrow\mathcal B}$。

2. 取$\mathcal D=\mathcal B$得换基矩阵可逆、反向换基即求逆，并用平面例的逆把$(2,1)^\top$送回$(1,1)^\top$。

3. 借“个数等于维数的线性无关组必是基”证明任一可逆矩阵都是某次换基的矩阵。

4. 示例`ex:ls-nearly-collinear-change-of-basis`写出贯穿例中行列式为$\varepsilon$的换基矩阵及其含$1/\varepsilon$的逆，复现式`eq:linear-algebra-coordinate-instability`，说明坐标被放大源于换基矩阵接近不可逆。

###### paragraph：被动换基与主动作用

1. 区分对象不动、记录改变的被动换基与坐标系不动、对象被送走的主动矩阵作用，后者将在下一节推广为线性映射。

2. 示例`ex:ls-passive-vs-active`与图`fig:ls-passive-change-vs-active-map`对照读数从$(3,3)$变为$(2,1)$与切变把$(3,3)$搬到$(6,3)$，结论是并非所有乘矩阵的运算都是换基。

### 9.3 线性与多线性映射

1. 从单个空间的记录转向对象之间保持线性组合的作用，概述本节：矩阵表示及运算对应，核与像、秩零度与可逆判据，相抵与相似两种换基关系，最后简述多线性映射。

#### 9.3.1 线性映射及其矩阵表示

1. 以设计矩阵、求导、读取坐标三种作用的共同性质（先加权相加再作用与先作用再加权相加结果相同）引出线性映射的定义（式`eq:ls-linear-map-def`），说明这一性质使作用可以逐个基向量计算。

2. 由定义得$T\bm0=\bm0$，并指出乘矩阵都是线性映射；示例`ex:ls-linear-map-checks`验证平面映射$T$与求导$D$线性、平移$\tau(x)=x+1$不线性。

3. 定义线性算子并举例，说明算子的两点不同：输出可再作为输入，故可定义$T^k$；两端可用同一组基，决定其换基规律（第~`sec:ls-similarity`节）。

4. 过渡段（标签`sec:ls-map-representation`）：定义域有无穷多个元素，选定基后有限个数即可记录；概述映射与矩阵一一对应、运算对应运算，矩阵由此是线性映射在坐标下的记录。

##### 9.3.1.1 矩阵表示

1. 由线性性说明映射由基向量的像决定，以像的坐标为列定义$[T]_{\mathcal C\leftarrow\mathcal B}$，推出$[T\bm v]_{\mathcal C}=[T]_{\mathcal C\leftarrow\mathcal B}[\bm v]_{\mathcal B}$（式`eq:linear-algebra-map-matrix-representation`）。

2. 说明行列数分别是输出、输入维数，下标的读法，以及算子两端用同一组基的记号$[T]_{\mathcal B}$。

3. 示例`ex:ls-plane-operator-matrix`由基向量的像写出平面映射的矩阵；示例`ex:ls-derivative-matrix`写出$P_2$上求导$D$的矩阵并核对它作用于系数列的结果。

4. 由两个“先有映射再写矩阵”的例子转到反方向，证明对应定理`thm:ls-map-matrix-correspondence`（单射与满射两部分），并提醒对应依赖基的选取，变化规律留给第~`sec:ls-coordinates-change-of-basis`节。

5. 把$\bm X_\varepsilon$读成从两个系数到三个拟合值的映射记录，输入与输出不在同一空间；图`fig:ch06-object-coordinate-map`显示先作用再取坐标与先取坐标再乘矩阵结果相同。

##### 9.3.1.2 基于矩阵的映射运算

1. 说明叠加、复合、求逆分别记录为矩阵加法、乘法与求逆，带偏置的仿射映射可借增广坐标写成更大的矩阵。

###### paragraph：叠加

1. 定义同一对空间之间两个映射的线性叠加，说明它仍线性，矩阵为$a\bm A+b\bm B$。

2. 说明相加要求定义域与陪域分别相同（对应同形矩阵），不要求$V=W$；系数须与输入无关。

###### paragraph：复合

1. 证明复合仍线性，两次使用矩阵表示并按列比较，得到$[S\circ T]=[S][T]$（式`eq:ls-composition-matrix`）。

2. 说明中间空间的基被消去、标准基情形是第~`sec:prelim-linear-actions-composition`节的特例，复合的结合律与不可交换性对应矩阵乘法的相应性质。

3. 对算子推出$[T^k]_{\mathcal B}=([T]_{\mathcal B})^k$，以$[D]^3=\bm0$对应二次多项式求导三次为零。

###### paragraph：逆映射

1. 回到第~`sec:prelim-inverse-matrices`节只作为数表运算的可逆矩阵，提出它记录哪类映射。

2. 证明双射线性映射的逆自动线性，定义可逆线性映射。

3. 由复合公式推出可逆映射的矩阵是可逆方阵且$[T^{-1}]=\bm A^{-1}$，反之可逆矩阵给出可逆映射。

4. 把$(S\circ T)^{-1}=T^{-1}\circ S^{-1}$对应到式`eq:ls-inverse-product`，并说明何时可逆由下一小节判断。

###### paragraph：仿射映射

1. 以带截距的预测与平移引出仿射映射$\bm x\mapsto\bm A\bm x+\bm b$，说明$\bm b\neq\bm0$时不是线性映射。

2. 写出两个仿射映射的复合，指出平移项也受后一映射作用。

3. 用末位补$1$的增广矩阵（式`eq:ls-affine-homogeneous`）把它写成高一维的线性作用，并按分块乘法验证复合。

4. 提醒原输入只取末坐标为$1$的向量，不能据此说原映射线性；仿射解集的几何见第~`chap:linear-equations-and-optimization`章。

##### 9.3.1.3 矩阵基本子空间

1. 对$\bm A$与$\bm A^\top$两个方向各问哪些输出可达、哪些输入被送到零。

2. 由列读法定义列空间，指出$\bm A\bm x=\bm b$有解当且仅当$\bm b\in\operatorname{range}(\bm A)$；定义零空间。

3. 对$\bm A^\top$定义行空间与左零空间，汇总为四个基本子空间（式`eq:ls-four-fundamental-subspaces`）。

4. 说明四个子空间所在的端，以及零空间、行空间、左零空间分别收集被消去的输入方向、读取输出分量的方向、对可达输出读数恒为零的加权方式。

5. 示例`ex:ls-rank-one-four-subspaces`对$\bm A=\left[\begin{smallmatrix}1&2&3\\2&4&6\end{smallmatrix}\right]$求出四个子空间，观察维数相同与互补的规律及逐项相乘再相加得零的现象；一般证明留给第~`sec:ls-kernel-image`节，垂直关系留给第~`sec:ls-orthogonality`节。

#### 9.3.2 核、像与秩

1. 说明能否由输出反求输入取决于丢失与可达的信息，概述本小节：核与像、秩零度定理、商空间解读、四个基本子空间的维数。

###### paragraph：核与像

1. 定义核与像并证明都是子空间。

2. 说明二者分属输入端与输出端，对矩阵分别是零空间与列空间，并约定“矩阵的核、秩”的含义。

3. 由$T\bm x=T\bm y\iff\bm x-\bm y\in\ker T$说明核代表丢失的信息；示例`ex:ls-kernel-indistinguishable`用三个响应读取四个分量，相差$(1,1,1,-1)^\top$倍数的输入给出相同输出。

4. 据此说明线性不可辨识性，并指出另有约束时须结合约束判断。

###### paragraph：秩零度定理

1. 定义秩与零度，取核的基扩充为全空间的基，证明秩零度定理`thm:ls-rank-nullity`（式`eq:ls-rank-nullity`）。

2. 写出矩阵形式$d=\dim\operatorname{null}(\bm A)+\operatorname{rank}\bm A$，用示例`ex:ls-kernel-indistinguishable`核对；图`fig:ls-kernel-image-rank-nullity`给出两个几何算例。

3. 证明$\operatorname{rank}\bm A\leq\min(m,d)$，定义满列秩、满行秩与满秩。

4. 说明矩形矩阵不能同时满列秩与满行秩，以$\bm X_\varepsilon$满列秩而像只是$\mathbb R^3$中的平面为例。

###### paragraph：商空间

1. 按输出把输入分组，每组是$\bm x+\ker T$，全部分组组成$V/\ker T$。

2. 证明$\bm x+\ker T\mapsto T\bm x$与代表元无关、线性、满射且单射，因而是到$\operatorname{im}T$的线性双射。

3. 由两边维数相同与式`eq:ls-quotient-dimension`重新得到秩零度定理，并用示例`ex:ls-kernel-indistinguishable`核对。

###### paragraph：证明行秩等于列秩

1. 对$\bm A$与$\bm A^\top$分别用秩零度定理得两组互补关系，指出还需证明行空间与列空间维数相等。

2. 证明行秩等于列秩（定理`thm:ls-row-rank-column-rank`）：用列空间的基分解$\bm A=\bm C\bm R$，按行读得行秩不超过列秩，对转置重复。

3. 得到四个基本子空间的维数全由$m,d,r$决定（式`eq:ls-four-subspace-dimensions`）。

4. 回到示例`ex:ls-rank-one-four-subspaces`核对并写出$\bm A=\bm C\bm R$，指出垂直关系见第~`sec:ls-orthogonality`节，另一证明见第~`sec:ls-dual-map`节。

#### 9.3.3 单射、满射与可逆性

1. 把由输出唯一还原输入分成单射与满射两个条件。

2. 证明单射等价于核为零、满射等价于像为全空间，并用秩零度定理换成维数条件。

3. 说明维数相等时单射、满射、双射等价；维数不同时不可能满射或不可能单射，故只有等维映射才可能可逆。

4. 汇总方阵可逆、零空间为零、秩为$n$、列（行）线性无关的等价链，预告行列式判据（第~`sec:ls-determinant-invertibility`节）。

5. 据此不借行列式再证方阵单侧逆即逆（第~`sec:ls-square-one-sided-inverse`节），并证明方阵乘积可逆时两因子都可逆。

6. 示例`ex:ls-kernel-invertibility`用核判断对角矩阵与$\left[\begin{smallmatrix}2&1\\0&3\end{smallmatrix}\right]$的可逆性。

###### paragraph：单侧逆

1. 维数不同时构造单射的左逆（像上读回、补空间上任意规定）与满射的右逆（为输出基选原输入再延拓），说明它们一般不唯一。

2. 证明矩阵有左逆当且仅当满列秩、有右逆当且仅当满行秩，以$(1,0)^\top$有无穷多个左逆为例，代表的选择留给第~`chap:linear-equations-and-optimization`章。

#### 9.3.4 换基、矩阵等价与相似

1. 类比坐标随基改变，说明映射的矩阵也随基改变，本小节写出这种变化并判断两个矩阵何时记录同一映射。

2. 说明先讨论两端各自换基的一般映射（相抵），再讨论两端同时换基的算子（相似）；约束减少自由度，相似需要更多不变量。

3. 观察换基矩阵就是恒等映射在两组基下的矩阵，连续换基公式即复合公式的特例。

##### 9.3.4.1 一般线性映射的换基与相抵

1. 说明本小节求两对基下矩阵的关系，证明它刻画记录同一映射，并说明秩是判断相抵的唯一依据。

###### paragraph：换基过程

1. 设定两端的新旧基与换基矩阵$\bm P,\bm Q$，说明绕道旧基分三步求新输出坐标。

2. 逐步写出三步，逐列比较得$\bm B=\bm Q^{-1}\bm A\bm P$（式`eq:ls-equivalence-transform`），并用$T=\operatorname{id}_W\circ T\circ\operatorname{id}_V$与复合公式解释三个因子。

###### paragraph：相抵的定义

1. 定义矩阵相抵`def:ls-matrix-equivalence`，说明$\bm Q,\bm P$可以是任意可逆矩阵。

2. 由任一可逆矩阵都是换基矩阵证明反方向，得出同形矩阵相抵当且仅当记录同一映射，并把初等列、行变换对应为输入、输出基的更换。

###### paragraph：相抵不变量

1. 验证相抵是等价关系，三条性质分别对应不换基、换回原基与连续换基。

2. 说明零空间在输入端、列空间在输出端被可逆矩阵搬运，得到秩与零度不变（式`eq:ls-equivalence-invariants`），并指出幂、迹等只对算子有意义的量不在讨论之列。

###### paragraph：相抵的判定

1. 提出秩相同的同形矩阵一定相抵，证明思路是化为只由秩决定的形状。

2. 取核的基扩充为输入基，证明新增的$r$个向量的像线性无关且张成像，再扩充为输出基，得到秩标准形（式`eq:ls-rank-normal-form`）。

3. 示例`ex:ls-rank-normal-form-two-by-two`对二阶秩$1$矩阵具体算出$\bm P,\bm Q,\bm Q^{-1}$（并列于同一行公式）；图`fig:ls-equivalence-two-sided-bases-flow`说明只有两端各自选基才能同时做到这些。

4. 证明相抵判据`thm:ls-equivalence-criterion`，说明秩是固定形状下相抵的完整不变量，消元算法留给第~`chap:linear-equations-and-optimization`章。

##### 9.3.4.2 线性算子的换基与相似

1. 说明算子两端必须换成同一组新基，本小节由此得到相似关系，讨论不变量与判定。

###### paragraph：换基过程

1. 在三步推导中取$\bm Q=\bm P$，得到$\bm B=\bm P^{-1}\bm A\bm P$（式`eq:linear-algebra-similarity-change-basis`），即式`eq:ls-equivalence-transform`的特例。

###### paragraph：相似的定义

1. 定义矩阵相似`def:ls-matrix-similarity`，证明相似矩阵正是同一算子在两组基下的记录。

2. 说明相似只要求换基矩阵可逆，相似必相抵而反之不然（预告示例`ex:ls-equivalent-not-similar`）。

3. 示例`ex:ls-similarity-diagonal`把$T(x_1,x_2)=(2x_1+x_2,3x_2)$换到基$(\bm e_1,\bm e_1+\bm e_2)$后化为$\operatorname{diag}(2,3)$；图`fig:ls-similarity-change-of-basis-flow`对比斜切与沿基方向伸缩，引出特征方向，留给第~`chap:linear-analysis`章。

###### paragraph：相似不变量

1. 验证相似是等价关系。

2. 继承相抵不变量，得秩与零度不变（式`eq:ls-similarity-invariants`）。

3. 由$\bm P\bm P^{-1}$相消得乘积与幂和换基相容（式`eq:ls-similarity-product`），进而各$\bm A-c\bm I$的秩不变（式`eq:ls-similarity-shifted-rank`）。

4. 由行列式乘法性与迹的循环性证明行列式与迹不变，以示例`ex:ls-similarity-diagonal`核对，说明可以谈论算子的行列式与迹。

5. 预告特征值与特征多项式也是相似不变量（第~`sec:ls-eigen-similarity-invariance`节），并指出长度与夹角不是相似不变量。

###### paragraph：相似的判定

1. 把相似改写为存在可逆$\bm P$满足$\bm A\bm P=\bm P\bm B$（式`eq:ls-similarity-equation`），强调非零但不可逆的解不是换基。

2. 说明不变量只给否定判据；示例`ex:ls-equivalent-not-similar`以$\bm I_2$与$\bm J$秩、行列式、迹相同而$c=1$时平移后的秩不同（且单位矩阵只与自身相似）说明相抵而不相似。

3. 总结“两端换基相同”的代价，指出完整分类需要Jordan标准形，本书不展开。

#### 9.3.5 多线性映射

1. 以元素内积、外积有两个输入且对每个输入分别线性引出槽位的概念。

2. 定义多线性映射与双线性映射，举例$\bm x\bm y^\top$。

3. 以$f(x,y)=xy$说明分别线性不等于整体线性。

4. 选定基后，双线性函数由基向量配对值$b_{i,j}$确定，写出$B(\bm x,\bm y)=\sum x_iy_jb_{i,j}$；换基改变系数而不改变映射，并说明这组系数与第~`chap:linear-operations`章的张量积和指标收缩有关，但重排存放次序不等于换基。

### 9.4 对偶空间

1. 以多项式取值、信号取样、加权和与坐标为例引出把对象读成一个数的作用，说明没有内积时需把读取规则本身当作研究对象。

2. 概述本节：全部线性读取组成对偶空间，坐标读取给出它的基；输出端读取传回输入端在坐标下是转置；读取的大小留给下一章。

#### 9.4.1 线性泛函与对偶基

###### paragraph：线性泛函

1. 定义线性泛函即陪域为$\mathbb R$的线性映射，以取值、积分、坐标读取与加权和为正例。

2. 示例`ex:ls-nonlinear-readouts`以$x_1+1$（不把零读成零）与$\lVert\bm x\rVert_2$（不满足$\varphi(-\bm x)=-\varphi(\bm x)$）为反例。

3. 由矩阵表示把泛函记为$1\times d$行矩阵，说明一列坐标与一行系数相乘得读数。

4. 由秩零度定理说明非零泛函的像是$\mathbb R$、核是$d-1$维子空间，等值集是核的平移，在平面上为一族平行直线。

###### paragraph：对偶空间

1. 定义泛函的线性组合，说明全部线性泛函构成对偶空间$V^*$，并区分被读取的向量与读取规则，二者不能相加。

###### paragraph：对偶基

1. 以坐标读取满足$\varphi_j(\bm b_i)=\delta_{j,i}$（式`eq:ls-dual-basis-def`）定义对偶基，并说明此式也可作定义。

2. 证明它张成$V^*$且线性无关，得$\dim V^*=\dim V$，读取在对偶基下的坐标即它在基向量上的读数。

3. 示例`ex:ls-dual-basis-depends-on-basis`显示只改第二个基向量也会把第一个坐标读取从$x$变成$x-y$；示例`ex:ls-dual-basis-oblique`解出斜基的对偶基，把横坐标读取写成$2\varphi_1-\varphi_2$，图`fig:ls-dual-basis-readout`画出这些读取。

4. 推出换基时坐标按$\bm P^{-1}$、读取系数按$\bm P$变化，二者相消使读数不变。

#### 9.4.2 对偶映射

1. 由“先作用再读取”定义对偶映射$T'f=f\circ T$（式`eq:ls-dual-map-def`），证明它线性、方向与$T$相反且$(S\circ T)'=T'\circ S'$，强调它不是求逆。

###### paragraph：对偶映射的矩阵是转置

1. 在两组对偶基下计算$(T'f)(\bm b_j)$，证明对偶映射的矩阵是$\bm A^\top$，转置的乘积规则即复合反序的坐标记录。

2. 示例`ex:ls-dual-map-first-component`对$T(x_1,x_2)=(2x_1+x_2,3x_2)$核对两种算法，说明读取输出第$i$分量传回得到$\bm A$的第$i$行，$T'$的像在坐标下就是行空间。

###### paragraph：再证行秩等于列秩

1. 说明$\ker T'$由在像上读数恒为零的读取组成，在坐标下即左零空间。

2. 取像的基扩充为输出空间的基，用对偶基算出$\dim\ker T'=m-r$。

3. 对$T'$用秩零度定理得$\operatorname{rank}\bm A^\top=\operatorname{rank}\bm A$。

4. 指出读取的大小由第~`sec:ls-dual-norms`节的对偶范数回答，读取写成与固定向量的内积由第~`sec:ls-riesz-representation`节回答。

### 9.5 本章小结

1. 回应章首的区分：线性空间与子空间规定线性组合的范围，交、和、直和描述子空间的比较与唯一分解，商空间把相差子空间向量的对象视为相同。

2. 基保证坐标唯一，维数与基无关，扩充给出和、补空间与商空间的维数；换基改变坐标而不改变向量，接近退化的基会产生大坐标。

3. 线性映射选基后记成矩阵，运算对应运算；核、像与秩零度定理给出单射、满射与可逆的判据；相抵以秩完全分类，相似在秩、行列式与迹相同时仍可能不成立。

4. 对偶空间由线性泛函组成，对偶基是坐标读取，对偶映射在对偶基下是转置并再次给出行秩等于列秩。

5. 指出这些结构尚未规定大小与夹角，下一章引入范数与内积。

## 第10章 赋范空间与内积空间

正文入口：[03-normed-inner-product.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/03-normed-inner-product.tex)，章内依次输入[01-normed-spaces.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/03-normed-inner-product/01-normed-spaces.tex)、[02-inner-product-spaces.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/03-normed-inner-product/02-inner-product-spaces.tex)与[03-summary.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/03-normed-inner-product/03-summary.tex)。

1. 从上一章只有加法和数乘的局限进入：能判断线性表示是否存在、是否唯一，却无法回答两个向量相差多少、近似序列是否收敛、两个方向是否垂直。由此说明本章先用范数规定大小，再用内积规定角度。

2. 概述前三节的主线：范数与距离一节给出范数并显式比较常用坐标范数；收敛、极限与连续性一节在欧氏与Frobenius范数下定义向量列、矩阵列的收敛和映射的极限与连续性，并证明闭有界集上的极值定理；有限维赋范空间的性质一节证明范数等价与完备性，建立向量与矩阵级数，再讨论矩阵范数、对偶范数与商范数。说明第11章的矩阵幂与Neumann级数、第12章的迭代和第13章的微分都使用这套分析基础。

3. 以一般范数没有角度、最近点可能不唯一承接内积：内积空间一节建立长度、夹角、Cauchy--Schwarz不等式、Hilbert空间名称与Gram矩阵；正交与投影一节研究正交分解、标准正交基并证明正交投影是唯一最近点；最后一节给出泛函的内积表示与伴随。声明本章只讨论有限维空间，收敛与连续性适用于一般映射。

### 10.1 范数与距离

1. 从多项式近似的误差与迭代近似的收敛进入，说明需要先规定向量的大小，并把第8章$\mathbb R^d$上的范数推广到一般线性空间。

2. 用两三句交代本节路线：先给范数公理与例子，再用显式不等式比较常用坐标范数；只用线性运算与标量不等式，收敛、范数等价与完备性在后两节。说明本章只讨论有限维空间。

#### 10.1.1 范数与距离

本小节给出范数公理，检验$p$范数，举出其他空间上的范数与半范数。

###### paragraph：范数的定义

1. 从$\ell_1,\ell_2,\ell_\infty$范数的共同性质（非负、只有零向量为零、齐次、和的大小不超过大小之和）进入，说明它们只涉及线性运算，给出赋范空间定义`def:ls-normed-space`。

2. 说明范数诱导的距离满足度量公理且与平移、缩放相容，因而赋范空间是特殊的度量空间。

3. 把三角不等式用于$\bm x=(\bm x-\bm y)+\bm y$并交换角色，得到反向三角不等式（式`eq:ls-reverse-triangle`），解释为两向量的长度之差不超过差向量的长度，下一节用它说明范数随向量收敛。

###### paragraph：坐标范数的公理检验

1. 指出$p$范数的非负性、正定性与齐次性可直接读出，只需证明三角不等式；$p=1,\infty$逐坐标由实数三角不等式得到，$1<p<\infty$需要先建立Hölder不等式。

###### paragraph：Hölder不等式

1. 说明Hölder不等式用共轭指数$1/p+1/q=1$的两个范数控制逐坐标乘积之和，陈述定理`thm:linear-algebra-holder`。分三步证明$1<p<\infty$的情形：换元$t=v/u^{p-1}$求一元函数最小值得Young不等式，对归一化坐标求和，再恢复尺度；零向量与端点直接处理。

2. 指出$p=q=2$给出$|\bm x^\top\bm y|\leq\lVert\bm x\rVert_2\lVert\bm y\rVert_2$，对任一内积的同形不等式（Cauchy--Schwarz）在10.4.1只用公理证明。

###### paragraph：Minkowski不等式

1. 说明证明思路是把$|x_j+y_j|^p$拆成两个乘积之和再分别用Hölder不等式，陈述定理`thm:linear-algebra-minkowski`；证明先处理$p=1,\infty$，再利用配对向量$\bm s$的$q$范数恰为$\lVert\bm x+\bm y\rVert_p^{p-1}$约去公因子。

2. 结论：每个$p$范数都满足范数定义，特别是欧氏长度满足三角不等式。

###### paragraph：其他空间上的范数

1. 回指Frobenius范数是元素排成向量后的$2$范数、诱导矩阵范数在10.3.4验证。

2. 说明借坐标映射可在一般空间上定义范数，也可直接用对象性质定义；示例`ex:ls-polynomial-norms`在$P_k$上给出系数最大绝对值与一致范数$\max_{[0,1]}|p(t)|$，后者的正定性来自非零多项式根数有限。

3. 作为对照，去掉正定性得到半范数；示例`ex:ls-seminorm-first-coordinate`中$|x_1|$满足其余要求却把$(0,0)^\top$与$(0,1)^\top$判为距离零，提醒使用半范数须说明忽略了哪些差别。

#### 10.1.2 常用坐标范数的比较

1. 从误差估计常需在不同范数之间换算进入，陈述定理`thm:ls-coordinate-norm-comparison`：$1\leq p\leq q\leq\infty$时$\lVert\bm x\rVert_q\leq\lVert\bm x\rVert_p\leq d^{1/p-1/q}\lVert\bm x\rVert_q$。左侧对归一化向量逐项比较$|u_j|^q\leq|u_j|^p$；右侧$q=\infty$直接估计，$p<q<\infty$对$(|x_j|^p)$与全$1$向量用指数$q/p$的Hölder不等式。

2. 分行列出$\ell_\infty,\ell_2,\ell_1$之间的三组比较；示例`ex:ls-norm-comparison-check`在$(3,-4)^\top$上核对前两组，说明同一误差在三种范数下读出$4,5,7$。

3. 示例`ex:ls-l1-linf-constants`以$\bm e_1$与全$1$向量说明两侧取等、常数不能改进；指出常数随维数增长，不能当作对所有维数一致的界；任意有限维范数的等价定理`thm:ls-norm-equivalence`放在10.3.1。

### 10.2 收敛、极限与连续性

说明本节用范数描述“接近”，固定欧氏范数与Frobenius范数建立逐坐标判据、映射的极限与连续性及闭有界集上的基本结论；换用任意范数留到下一节，以免循环论证；这些概念适用于一般映射。

#### 10.2.1 向量列与矩阵列的收敛

1. 回顾一元数列的误差趋零，定义`def:multivariable-sequence-convergence`：向量列按$\lVert\cdot\rVert_2$、同形矩阵列按$\lVert\cdot\rVert_{\mathrm F}$收敛；说明维数、形状固定，复向量与复矩阵拆成实部、虚部处理。

###### paragraph：逐坐标判据

1. 由$\max_j|x_{k,j}-x_j|\leq\lVert\bm x_k-\bm x\rVert_2\leq\sqrt d\max_j|x_{k,j}-x_j|$证明定理`thm:multivariable-coordinatewise-convergence`：收敛等价于逐坐标收敛，矩阵经向量化得逐元素判据；指出取$N=\max_jN_j$依赖坐标有限。

2. 说明取$N=\max_jN_j$依赖坐标有限，换用范数或基的问题留到10.3.1。

###### paragraph：极限的唯一性与运算

1. 由三角不等式证明极限唯一、收敛列有界，由反向三角不等式得范数随之收敛。

2. 说明加法、数乘、内积与形状相容的矩阵乘法保持极限：结果的每个元素是有限个标量数列的和与积，由一元运算法则与逐坐标判据得到。

#### 10.2.2 开集、闭集与有界集

1. 说明讨论极限与连续前须先描述输入所在的集合：基点周围有无移动余地、是否包含边界点、是否伸向无穷远，分别由开集、闭集与有界集回答；矩阵空间按Frobenius范数同样定义。

###### paragraph：开球与开集

1. 定义开球$B(\bm a,r)$并在$d=1,2$时解释，给出定义`def:multivariable-open-closed-bounded`（开集、闭集为补集开、有界）。

2. 解释开集中每点向任何方向走一小步仍在集合内，这是后面在开集上求双侧差商的依据，半径随点而变。

3. 说明开与闭不对立：$\mathbb R^d$与空集既开又闭，半开带$\{0\leq x<1\}$既不开也不闭；有界性与中心选取无关。

###### paragraph：聚点、孤立点与边界点

1. 定义聚点（可以不属于$D$，是讨论极限的前提）、孤立点与边界点，以开圆盘的边界圆说明边界点可以是不属于集合的聚点。

###### paragraph：闭集的序列判据

1. 证明闭集的序列判据`lem:multivariable-closed-sequence`，与实轴上的引理对应，解释为闭集包含自己的全部边界点。

2. 示例`ex:multivariable-open-closed-sets`：开圆盘开而不闭、边界点是聚点，闭圆盘与$\{\lVert\bm X-\bm I_2\rVert_{\mathrm F}\leq1/2\}$闭且有界，说明可以在不属于定义域的边界点处讨论极限。

#### 10.2.3 映射的联合极限

1. 说明本小节与下一小节研究$F:D\subseteq V\to W$，$V,W$取欧氏或Frobenius范数的坐标空间；标量输出、向量值映射与矩阵的函数都是特例，例子多取标量输出。

###### paragraph：多元标量函数

1. 用曲面图像说明多元标量函数，给出定义`def:multivariable-scalar-function`。

2. 以$x^2+xy+y^2$为例介绍切片和等值曲线两种观察方法，指出切片只看一条直线，由此转向在整个空间中趋近基点时函数值的变化。

##### 10.2.3.1 极限的定义

1. 说明一元只能从两侧靠近，平面中可沿直线、抛物线、螺旋线趋近，定义须用一个只依赖距离的条件控制全部输入。

2. 把一元的去心区间换成去心球，要求基点为聚点，输出误差用输出空间的范数度量，给出映射的极限定义`def:multivariable-limit`。

3. 解释$\delta$只依赖$\varepsilon$、不依赖方向，任何趋近方式都由同一个$\delta$覆盖；称之为联合极限，以区别于沿路径或逐个坐标的极限。

##### 10.2.3.2 极限的判据

1. 说明定义直接验证不便，本小节给出序列判据、用于否定的路径检验与累次极限，以及用于证明的统一误差估计。

###### paragraph：序列判据

1. 给出序列判据；由逐坐标判据说明向量值或矩阵值映射的极限等价于各输出分量的极限，并区分分解输出与分别固定输入坐标。

###### paragraph：路径检验

1. 由“路径点列是序列的特例”得到路径检验的两面：两条路径极限不同可以否定联合极限，有限条路径乃至全部直线都不能证明极限存在。

2. 示例`ex:multivariable-path-limits`：$xy/(x^2+y^2)$沿$y=kx$取值$k/(1+k^2)$，原点无联合极限；它的每条坐标切片却都连续。

3. 示例`ex:multivariable-parabola-path-limit`：$x^2y/(x^4+y^2)$沿所有直线极限为$0$，沿$y=x^2$恒为$1/2$；用$y=(k/x)x^2$解释每条直线最终离开“山脊”。

4. 总结路径检验只能否定，证明存在需要对所有路径同时有效的误差估计；图`fig:analysis-process-joint-limit-paths`示直线与抛物线路径。

###### paragraph：累次极限与联合极限

1. 定义累次极限，说明它从不要求两个坐标同时趋近；对第一个示例，两个次序的累次极限都为$0$，联合极限却不存在。

2. 示例`ex:multivariable-iterated-limits-differ`：$x^2/(x^2+y^2)$两个次序的累次极限分别为$1$和$0$，用坐标轴上的取值解释。

3. 总结累次极限相等不足以推出联合极限存在；再证明反方向：联合极限存在且内层极限存在时，累次极限等于联合极限。

###### paragraph：统一误差估计

1. 说明证明联合极限可寻找只依赖距离并趋于零的上界。

2. 示例`ex:multivariable-distance-bound-limit`：用$|xy|\leq(x^2+y^2)/2$证明$x^2y/(x^2+y^2)\to0$，并用与角度无关的极坐标界给出同一结论。

3. 示例`ex:multivariable-polar-fixed-angle`：对$x^2y/(x^4+y^2)$固定角度得到$0$，但让角度随$r$变化可落在抛物线上取值$1/2$；结论是极坐标证明需要对全部$\theta$同时成立的界。

#### 10.2.4 连续性

##### 10.2.4.1 连续性的定义

1. 由联合极限引出连续，给出映射连续性定义`def:multivariable-scalar-continuity`（条件允许$\bm x=\bm a$），说明聚点与孤立点情形、几何含义、连续等价于各输出分量连续，并指出连续函数的坐标切片连续而逆向不成立。

##### 10.2.4.2 连续性的性质

1. 说明连续性在常用运算下保持，逐条检验和、差、数乘、积、商、乘积型运算与复合，再说明求逆在可逆矩阵上连续。

###### paragraph：和的连续性

1. 用三角不等式和取较小半径证明和连续。

###### paragraph：差的连续性

1. 同样的三角不等式证明差连续。

###### paragraph：数乘的连续性

1. 分$c\neq0$与$c=0$证明数乘连续。

###### paragraph：积的连续性

1. 把乘积误差拆成两项，利用$f$在基点附近有界证明积连续；由坐标函数连续推出多项式连续。

###### paragraph：商的连续性

1. 利用分母在基点附近远离零估计$1/g$的误差，再用积的连续性得到商连续，推出有理函数在分母非零处连续。

###### paragraph：内积与矩阵乘法

1. 说明向量值映射的内积与形状相容的矩阵值映射的乘积连续：结果的每个元素是有限个分量乘积之和。

###### paragraph：复合映射

1. 分两步选取$\eta$与$\delta$证明连续映射的复合连续，以$e^{-(x^2+y^2)}$等为例。

###### paragraph：求逆的连续性

1. 由古典伴随公式`thm:ls-adjugate-identity`写出$\bm X^{-1}=\operatorname{adj}(\bm X)/\det\bm X$，分子各元素与分母都是多项式，分母在可逆矩阵集合上非零，故求逆在可逆矩阵上连续。

2. 说明这里只建立连续性，逆矩阵差的精确误差界与求逆的微分分别在第12、13章讨论。

##### 10.2.4.3 一致连续与Lipschitz连续

1. 给出定义`def:ls-lipschitz`：一致连续（$\delta$不依赖基点）、Lipschitz连续与局部Lipschitz连续。

2. 说明Lipschitz蕴含一致连续，以$\sqrt x$在$[0,1]$上一致连续却在零点没有Lipschitz常数作区分；范数由反向三角不等式是常数为$1$的例子；导数求常数留到第13章。

#### 10.2.5 闭有界集上的连续函数

1. 从“求最小点须先保证最小值存在”进入，回顾一元极值定理依赖子列性质，说明本小节先推广子列性质，再得极值定理与一致连续性；矩阵空间经向量化结论相同。

###### paragraph：有限维闭有界集的收敛子列

1. 说明逐坐标使用Bolzano--Weierstrass定理，有界性给出收敛子列，闭性保证极限在集合内；给出定理`thm:multivariable-bolzano-weierstrass`及逐坐标抽取子列的证明，极限由逐坐标判据与闭集序列判据得到。

2. 指出有限维闭有界集具有与闭区间相同的子列性质，一般度量空间的情形交叉引用度量空间章。

###### paragraph：有界性与极值达到

1. 说明趋近确界的序列可能跑向无穷远或趋向集合外的边界点，闭有界性同时排除二者；给出闭有界集上的极值定理`thm:multivariable-extreme-value`，证明沿用一元证明。

2. 示例`ex:multivariable-extreme-value-failures`：开圆盘、整个平面和边界不连续的闭圆盘，分别说明删去闭性、有界性或连续性时最值可能取不到。

3. 指出单位球面是闭有界集，下一节在其上比较范数。

###### paragraph：一致连续性

1. 回用定义`def:ls-lipschitz`，对照一元定理`thm:analysis-uniform-continuity`，陈述并反证定理`thm:multivariable-uniform-continuity`：构造距离趋零而输出差保持$\varepsilon_0$的两列点，取收敛子列得同一极限，与连续性矛盾。

2. 说明第14章的Riemann和、参数积分与换元需要在整个区域上统一控制误差。

### 10.3 有限维赋范空间的性质

说明本节研究范数与有限维线性结构结合后的分析性质：先证明范数等价与完备性，使向量与矩阵级数有统一依据；再以算子范数度量线性映射、以对偶范数度量线性泛函；最后建立商范数与一般范数下最近点的存在；每一步回用上一节的收敛与连续性。

#### 10.3.1 有限维范数等价

1. 从上一节固定欧氏与Frobenius范数、而误差分析常用$\ell_1$、$\ell_\infty$与诱导范数进入，提出换用范数是否改变收敛与连续性。

2. 陈述定理`thm:ls-norm-equivalence`；零维单独处理，固定基后以坐标欧氏长度$\lVert\cdot\rVert_c$为参照，由三角不等式、齐次性与Hölder不等式得上界$C_p$，由反向三角不等式得$p$关于坐标连续。

3. 下界：在坐标单位球面上由极值定理`thm:multivariable-extreme-value`取到最小值（锚点`thm:ls-extreme-value`），由正定性知其为正，合成式`eq:linear-algebra-finite-norm-equivalence`后比较两个范数。

4. 回指示例`ex:ls-l1-linf-constants`说明常数不能改进，指出真正依赖有限维的是下界。

###### paragraph：收敛与连续性不依赖范数

1. 说明换用范数只把误差乘以有界正因子，收敛、极限、映射的极限与连续性（两端范数可分别更换）以及开集、闭集与有界集都与范数无关。

2. 换基后坐标的欧氏长度也是范数，故逐坐标判据与基无关；矩阵序列在任意矩阵范数下收敛等价于逐元素收敛；子列抽取与极值定理可在任何范数下使用。

3. 提醒数值误差与比较常数仍依赖范数与维数，范数等价不给出衰减速度。

#### 10.3.2 完备性

1. 从迭代与级数截断只给出彼此接近的近似、事先不知极限进入，回指实数列的柯西条件。

###### paragraph：Cauchy列与完备性

1. 定义柯西列，说明收敛序列都是柯西列，有限维中柯西性与范数无关，柯西列是否收敛取决于空间中有无极限；定义完备与Banach空间。

2. 陈述定理`thm:ls-finite-dimensional-complete`：借式`eq:linear-algebra-finite-norm-equivalence`把柯西列化为各坐标的实柯西数列，由实数完备性逐坐标构造极限；子空间与矩阵空间同样完备。

3. 指出证明依赖坐标有限、无限维空间是否完备取决于空间与范数（指向度量空间章与函数空间章）；说明完备性使级数、矩阵幂与迭代只需估计误差即可断定极限存在。

###### paragraph：子空间的闭性

1. 从“点与子空间任意接近能否推出属于子空间”进入，陈述并证明定理`thm:ls-subspace-closed`：扩充基后补充方向的坐标恒为零，逐坐标收敛保持为零。

2. 与完备性相互印证；定义点到子空间的距离$d(\bm x,U)$，取距离趋零的子空间序列并由闭性得$d(\bm x,U)=0$当且仅当$\bm x\in U$，供商范数使用。

#### 10.3.3 向量与矩阵级数的收敛

1. 从矩阵幂之和与逐步累积的误差进入，回指实数级数的部分和定义（`sec:analysis-series`）。

###### paragraph：部分和与收敛

1. 用部分和在固定有限维空间中的收敛定义向量、矩阵级数的收敛；由逐坐标判据，收敛等价于各坐标级数收敛；由$u_N=S_N-S_{N-1}$说明通项趋零。

###### paragraph：绝对收敛

1. 用$\sum_k\lVert u_k\rVert<\infty$定义绝对收敛，由范数等价说明它与范数无关。

2. 陈述并证明定理`thm:ls-absolute-series-convergence`：三角不等式把部分和之差控制为标量尾和，得柯西列，由完备性收敛，令$M\to\infty$得尾和估计$\lVert S-S_N\rVert\leq\sum_{k>N}\lVert u_k\rVert$；说明完备性使人不必先知道和。

3. 示例`ex:ls-matrix-geometric-series`对$\left[\begin{smallmatrix}1/2&1\\0&1/2\end{smallmatrix}\right]$写出$\bm A^k$，逐元素与按Frobenius范数绝对收敛，和为$\left[\begin{smallmatrix}2&4\\0&2\end{smallmatrix}\right]=(\bm I-\bm A)^{-1}$，预告第11章的Neumann级数。

###### paragraph：级数的运算

1. 说明收敛级数可逐项相加、数乘，固定矩阵可移入求和号（部分和关系加矩阵乘积保持极限），并指出下一小节可把它看作线性映射连续性的推论；一般级数乘积与重排不需要。

#### 10.3.4 矩阵范数

1. 对照第8章衡量元素总体大小的Frobenius范数，引出把矩阵看作映射、问最大放大倍数的口径。

2. 对任意输入、输出范数定义诱导矩阵范数`def:matrix-analysis-induced-norm`为单位球上的上确界，由齐次性说明它等于非零输入比值的上确界，零空间上取零；预告下面先证明它有限。

##### 10.3.4.1 线性作用的连续性

1. 陈述并证明定理`thm:ls-linear-map-continuity`：按列展开并用范数等价得诱导范数有限且$\lVert\bm A\bm x\rVert_\beta\leq\lVert\bm A\rVert_{\alpha\to\beta}\lVert\bm x\rVert_\alpha$；用于$\bm x-\bm y$得Lipschitz连续；单位球闭且有界，由极值定理`thm:multivariable-extreme-value`得上确界可达。

2. 解释三条结论：诱导范数是放大界中最小的常数，按`def:ls-lipschitz`读作误差放大上界，$\sup$可写成$\max$。

###### paragraph：线性映射的算子范数

1. 对有限维线性映射定义算子范数，把$V,W$的范数搬到坐标空间后它等于表示矩阵的诱导范数，由定理得有限、可达，有限维线性映射都Lipschitz连续；说明换基保持原范数时数值不变，在坐标上另指定范数则改变计量规则。

##### 10.3.4.2 常用的诱导范数

1. 写出最大绝对列和、最大绝对行和两个公式（推导在10.3.4.3），说明谱范数是欧氏诱导范数、等于最大奇异值（11.5节）。

2. 示例`ex:ls-matrix-norms-shear`在$\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$上算出$\lVert\bm A\rVert_1=\lVert\bm A\rVert_\infty=2$、$\lVert\bm A\rVert_{\mathrm F}=\sqrt3$；图`fig:ls-induced-norm-action`把单位圆像的最长半轴读作谱范数。

##### 10.3.4.3 矩阵范数的性质

1. 用一句交代有限性与可达性已得到，本小节求具体公式、核对范数公理，再给出乘积上界，用于计算实际误差常数。

###### paragraph：列和与行和公式

1. 按列读法与行读法分别推出$\lVert\bm A\rVert_1$、$\lVert\bm A\rVert_\infty$的上界，并给出取到上界的输入（标准坐标向量、按行元素符号取值的向量）。

###### paragraph：谱范数不超过Frobenius范数

1. 说明谱范数难以直接计算，Frobenius范数给出容易计算的上界；对每行用$p=q=2$的Hölder不等式再求和，得$\lVert\bm A\bm x\rVert_2\leq\lVert\bm A\rVert_{\mathrm F}\lVert\bm x\rVert_2$与$\lVert\bm A\rVert_2\leq\lVert\bm A\rVert_{\mathrm F}$。

###### paragraph：诱导范数是范数

1. 逐条核对诱导范数满足范数要求：正定性由各$\bm A\bm e_j=\bm0$得出，三角不等式逐点估计后取上确界。

###### paragraph：次乘性

1. 连用两次诱导范数的界，得到中间范数匹配时的次乘性，特别地$\lVert\bm A^k\rVert_p\leq\lVert\bm A\rVert_p^k$。

###### paragraph：Frobenius范数与谱范数的混合界

1. 逐列应用谱范数的界得到式`eq:matrix-analysis-mixed-submultiplicativity`的第一式。

2. 第二式对转置应用第一式，为此由$\lVert\bm B\rVert_2=\sup_{\lVert\bm x\rVert_2=\lVert\bm y\rVert_2=1}|\bm y^\top\bm B\bm x|$证明$\lVert\bm B^\top\rVert_2=\lVert\bm B\rVert_2$；再结合$\lVert\bm A\rVert_2\leq\lVert\bm A\rVert_{\mathrm F}$推出Frobenius范数次乘。

#### 10.3.5 对偶范数

1. 从线性泛函是对向量的读取、误差只知落在范数球内时一次读取$\bm z^\top\bm r$最多变化多少进入，定义对偶范数`def:linear-algebra-dual-norm`（式`eq:linear-algebra-dual-norm-definition`）。

2. 指出它是输出取$\mathbb R$时的诱导范数，有限并可取到，逐条验证正定性（取$\bm e_j/\lVert\bm e_j\rVert$）、三角不等式与齐次性；图`fig:ls-dual-norm-unit-ball`把最大值画成支撑线最后接触单位球的位置。

3. 对$\ell_p$由Hölder不等式得上界并逐类构造达到上界的$\bm r$，得到单行写出的式`eq:linear-algebra-lp-duality`与按预算缩放的式`eq:linear-algebra-linear-perturbation-duality`。

4. 示例`ex:ls-dual-norm-three-budgets`对$\bm z=(2,-1)^\top$算出$\ell_1,\ell_2,\ell_\infty$单位球上的最大值$2,\sqrt5,3$及预算$0.01$下的$0.03$；图`fig:linear-algebra-dual-unit-balls`画出最坏方向。

5. 归纳：$\ell_\infty$预算对应$\ell_1$计量、$\ell_2$对应$\ell_2$。

6. 示例`ex:ls-weighted-dual-norm`对加权$\ell_1$范数$\sum_jw_j|r_j|$换元$s_j=w_jr_j$化回$\ell_1$情形，得$\lVert\bm z\rVert_*=\max_j|z_j|/w_j$；以$\bm z=(2,-1)^\top$在权重$(1,1)$与$(4,1)$下分别得$2$与$1$，说明读取的代数表达不变而大小随原范数改变。

7. 结论：讨论误差放大必须先说明所用范数；内积范数下的对偶范数在10.6.1由表示向量得到；一般有限维空间上的$\lVert\varphi\rVert_*$即取$W=\mathbb R$的算子范数，无限维代数对偶与连续对偶之别留给函数空间章。

#### 10.3.6 商范数

1. 承接子空间闭性，回指商空间只有线性结构；说明类中各点到$U$的距离不依赖代表元，据此定义商范数$\lVert\bm x+U\rVert_{V/U}=d(\bm x,U)$。

2. 验证三角不等式（取任意接近两侧下确界的代表元）与齐次性，正定性由$d(\bm x,U)=0\iff\bm x\in U$得到；指出子空间不闭的更一般空间中公式可能只给出半范数。

###### paragraph：一般范数下的最近点

1. 陈述定理`thm:multivariable-nearest-point-existence`：取距离逼近下确界的子空间点列，由$\lVert\bm u_k\rVert\leq\lVert\bm x\rVert+\lVert\bm x-\bm u_k\rVert$知有界，取收敛子列，由子空间闭性与范数连续性得最近点存在。

2. 示例`ex:ls-linf-nonunique-nearest`算出$\ell_\infty$范数下$(0,1)^\top$到横轴的距离为$1$，全部$(t,0)^\top$、$|t|\leq1$都是最近点；说明存在性不保证唯一性，10.5.4加入内积后证明正交投影给出唯一最近点。

### 10.4 内积空间

1. 从范数没有角度、最近点可能不唯一进入，说明本节提取欧氏内积的共同规则，在一般线性空间上定义内积。

2. 交代本节先由公理推出长度、夹角与基本不等式，再用Gram矩阵记录两两内积；正交投影与伴随留给后两节。

#### 10.4.1 内积与内积诱导的范数

本小节先给出内积公理与例子，再由内积定义长度、正交与夹角，最后从三角不等式出发说明内积诱导的长度是范数并给出距离；平行四边形恒等式说明并非每个范数都来自内积。

##### 10.4.1.1 内积的定义

###### paragraph：一般线性空间上的内积

1. 从欧氏内积的双线性、对称性与正定性只涉及线性运算进入，给出内积空间定义`def:functional-inner-product-space`。

###### paragraph：内积的例子

1. 逐条检验欧氏内积满足三条公理。

2. 说明Frobenius内积就是把元素看作坐标的欧氏内积，因而一般结论对它同样成立。

3. 示例`ex:ls-two-point-inner-product`在$P_1$上规定只看两点取值的内积并验证公理，以$\langle1,t\rangle=1$而系数向量欧氏内积为零说明它与系数内积不同；后面的算例反复使用它。

###### paragraph：复内积的约定

1. 说明复空间中两个变量都线性会破坏正定性，因而采用第一变量共轭线性、第二变量线性与共轭对称的约定，标准例子为$\bm x^*\bm y$。

2. 说明后面的Cauchy--Schwarz不等式与诱导范数在复内积下同样成立，但下一小节的余弦公式不能照搬；下文证明继续使用实内积。

##### 10.4.1.2 由内积定义的夹角

###### paragraph：长度与正交

1. 由内积定义长度（是否为范数留到下一小节检验）与正交，展开$\lVert\bm x+\bm y\rVert^2$消去交叉项得勾股定理。

###### paragraph：Cauchy--Schwarz不等式

1. 为了反过来用$\langle\bm x,\bm y\rangle=\lVert\bm x\rVert\lVert\bm y\rVert\cos\theta$定义夹角，需要比值落在$[-1,1]$中；陈述定理`thm:linear-algebra-cauchy-schwarz`（式`eq:prelim-cauchy-schwarz`），由$\lVert\bm x-s\bm y\rVert^2\geq0$的二次函数在顶点处的最小值得出不等式与等号条件。

2. 指出证明只用公理，标准内积下即$p=q=2$的Hölder不等式，对Frobenius内积同样成立。

###### paragraph：夹角

1. 定义夹角并写成两个单位向量的内积，说明夹角只比较方向、正交对应直角、共线对应$\cos\theta=\pm1$，且分子分母须来自同一内积。

2. 示例`ex:ls-nearly-collinear-angle`对贯穿例两列算得式`eq:linear-algebra-nearly-collinear-angle`（$\varepsilon=0.1$时约$4.7^\circ$）。

3. 据此定义近共线，说明“近”指作为$\mathbb R^3$中向量的夹角小，且夹角依赖所用内积。

##### 10.4.1.3 由内积定义的距离

###### paragraph：三角不等式

1. 从想用$\lVert\bm x-\bm y\rVert$度量距离出发，说明这要求长度是范数，关键是三角不等式（直达不长于绕行），正定性与齐次性直接成立；陈述并证明定理`thm:ls-inner-product-triangle`：展开平方后用Cauchy--Schwarz控制交叉项，等号条件化为$\bm x=s\bm y$且$s\geq0$。

###### paragraph：内积诱导的范数与距离

1. 由三角不等式得内积诱导的长度是范数，给出距离$d(\bm x,\bm y)=\lVert\bm x-\bm y\rVert$（欧氏、Frobenius距离为例），内积空间都是赋范空间，前三节的结论适用。

2. 用$\lVert\bm x-\bm y\rVert^2=\lVert\bm x\rVert^2-2\langle\bm x,\bm y\rangle+\lVert\bm y\rVert^2$说明距离由长度与夹角决定（余弦定理），引出用这一额外结构区分范数是否来自内积。

###### paragraph：平行四边形恒等式

1. 转向反面问题：并非每个范数都来自内积。陈述并证明定理`thm:linear-algebra-parallelogram`（式`eq:functional-parallelogram-identity`）：展开和与差的长度平方后相加，交叉项抵消。

2. 用恒等式检验范数是否来自内积，反例`ex:ls-l1-linf-not-inner-product`取$\bm e_1,\bm e_2$得$\ell_1$下$8\neq4$、$\ell_\infty$下$2\neq4$，因而一般范数不能用上述公式定义夹角。

3. 反过来由展开相减得极化恒等式，说明给出同一范数的两个实内积必相同。

###### paragraph：Hilbert空间

1. 由内积诱导范数与10.3.2的有限维完备性引出Hilbert空间的名称，说明有限维内积空间都是Hilbert空间。

2. 指出后面的正交分解与投影由有限维代数构造得到，不依赖完备性；无限维中完备性与子空间闭性需另行检查，无限正交级数、闭子空间投影与连续泛函的表示留给函数空间章。

#### 10.4.2 Gram矩阵

1. 交代本小节先引入正定与半正定矩阵并定义加权内积，再定义Gram矩阵，说明Gram矩阵恰为全部半正定矩阵、可读出线性无关与正交；借这一刻画证明逐元素乘积保持半正定，最后写出坐标下的内积。

##### 10.4.2.1 正定与半正定

1. 定义对称矩阵的二次型，定义正定、半正定以及$\bm M\succeq\bm N$，强调比较的是二次型而非元素。

2. 示例`ex:ls-pd-psd-completing-square`用配方区分正定的$\left[\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\right]$与仅半正定的$\left[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right]$。

3. 说明对角矩阵正定当且仅当对角元全为正；反例`ex:ls-positive-entries-not-pd`说明元素全为正的对称矩阵可以不定。

###### paragraph：加权内积

1. 说明正定矩阵可在$\mathbb R^d$上定义标准内积以外的内积，给出加权内积与距离（式`eq:linear-algebra-mahalanobis-pseudodistance`），逐条核对公理并指出协方差逆给出Mahalanobis距离。

2. 示例`ex:ls-weighted-length`以$\operatorname{diag}(4,1)$下$(1,1)^\top$的加权长度$\sqrt5$与欧氏长度$\sqrt2$对照，并预告本小节最后说明任一内积选基后都是这种形式。

##### 10.4.2.2 Gram矩阵的定义

1. 从一组向量有$r^2$个内积值、需要一次记录进入，定义Gram矩阵`def:linear-algebra-gram-matrix`及其在欧氏、加权内积下的矩阵形式，说明对称性。

2. 说明正交性写在非对角元里：对角对应两两正交，单位矩阵对应标准正交。图`fig:ls-gram-matrix-coefficients`把两个向量的内积排成数表。

##### 10.4.2.3 Gram矩阵与半正定矩阵

###### paragraph：Gram矩阵的半正定性

1. 由二次型等于线性组合的长度平方，说明Gram矩阵半正定，且正定当且仅当向量线性无关；正定时可逆。

2. 示例`ex:ls-nearly-collinear-gram`说明贯穿例两列的Gram矩阵正定，但系数$(1,-1)^\top$使二次型只有$2\varepsilon^2$，即“正定但几乎退化”。

###### paragraph：Gram因子定理

1. 提出反问题：每个半正定矩阵是否都是Gram矩阵；关键是写成欧氏平方和。对阶数归纳证明定理`thm:ls-gram-factor`：对角元全为零时推出$\bm M=\bm0$，否则置换出正对角元、对第一个变量配方，余项仍半正定，用分块上三角因子拼回；正定时写出该因子的分块逆。

2. 示例`ex:ls-gram-factor-two-by-two`按证明步骤得$\bm L=\left[\begin{smallmatrix}2&1\\0&1\end{smallmatrix}\right]$；说明加权长度即$\lVert\bm L\bm x\rVert_2$，配方即Cholesky分解的雏形。

###### paragraph：半正定矩阵是Gram矩阵

1. 由因子定理回答反问题：半正定矩阵就是$\bm L$各列的Gram矩阵，两者说的是同一件事。

##### 10.4.2.4 Gram矩阵与逐元素乘法

1. 说明“半正定矩阵就是Gram矩阵”可用来判断逐元素乘积是否保持半正定：只需找到一组向量，其两两内积恰为两个Gram矩阵对应元素之积；引出Schur乘积定理。

2. 陈述定理`thm:ls-schur-product`：两个对称半正定矩阵的逐元素乘积仍对称半正定。证明由定理`thm:ls-gram-factor`把两者写成$\bm u_i$、$\bm v_i$的Gram矩阵，借张量积在Frobenius内积下配对的分离性（`sec:ls-tensor-product-properties`），把逐元素乘积写成$\bm u_i\otimes\bm v_i$的Gram矩阵。

3. 示例`ex:ls-schur-product`用配方核对二阶例子，并指出该定理是核矩阵逐元素乘积仍合法的依据。

##### 10.4.2.5 Gram矩阵与内积

###### paragraph：坐标下的内积

1. 按双线性展开得$\langle\bm v,\bm w\rangle=[\bm v]^\top\bm G[\bm w]$，说明选基后任一内积都是以基的Gram矩阵为权重的加权内积，$\mathbb R^d$上的内积与对称正定矩阵一一对应。

2. 示例`ex:ls-two-point-inner-product-coordinates`在两点内积与基$(1,t)$下按定义与按坐标算得同一内积值$-1$，并指出标准正交基使$\bm G=\bm I$。

3. 说明换基时Gram矩阵按合同变换$\bm C^\top\bm G\bm C$变化，与算子的相似变换用途不同。

##### 10.4.2.6 复空间中的Gram矩阵

1. 沿用复内积第一变量共轭线性的约定，定义$G_{i,j}=\langle\bm b_i,\bm b_j\rangle$，说明本小节比较与实情形的异同。

###### paragraph：自共轭代替对称

1. 由交换变量取共轭得$\bm G^*=\bm G$，定义自共轭矩阵（与10.6.2的自伴矩阵相同），说明对角元为实数、非对角元一般为复数、$\bm G$一般不对称，实Gram矩阵是其特例。

###### paragraph：半正定性照样成立

1. 由$\bm c^*\bm G\bm c=\lVert\sum_jc_j\bm b_j\rVert^2\geq0$说明复Gram矩阵半正定，指出自共轭矩阵的二次型总是实数。

###### paragraph：正定与线性无关的关系照样成立

1. 由同一等式得正定当且仅当向量组在复数域上线性无关；以$\mathbb C$中的$1,\mathrm i$（实系数无关、复系数相关，Gram矩阵行列式为零）说明系数域的作用。

2. 说明逐步配方证明照样成立，得$\bm G=\bm L^*\bm L$，每个半正定自共轭矩阵都是Gram矩阵，不借用谱定理。

###### paragraph：坐标下的内积与换基

1. 说明复内积在坐标下为$\bm x^*\bm G\bm y$，换基时Gram矩阵变为$\bm C^*\bm G\bm C$。

2. 示例`ex:ls-complex-gram`对$(1,\mathrm i)^\top$与$(1,1)^\top$算出$\bm G=\left[\begin{smallmatrix}2&1-\mathrm i\\1+\mathrm i&2\end{smallmatrix}\right]$，不对称但自共轭，$\det\bm G=2>0$故正定，与线性无关一致。

### 10.5 正交与投影

1. 说明本节把正交从两个向量推广到向量与子空间，给出正交分解；再引入标准正交基并用Gram--Schmidt正交化构造它，最后写出正交投影并证明它是唯一最近点。

#### 10.5.1 正交补与正交分解

1. 交代本小节由向量与整个子空间的正交得到唯一确定的补空间，并证明四个基本子空间的垂直关系。

###### paragraph：正交补

1. 从补空间一般不唯一进入，定义正交补$U^\perp$，由双线性说明它是子空间，并指出只需检查与$U$的一组基逐个正交。

###### paragraph：正交直和

1. 借正定可逆的Gram矩阵解出分量系数，证明正交直和引理`lem:ls-orthogonal-decomposition`与分解唯一，得$\dim U^\perp=\dim V-\dim U$。

2. 示例`ex:ls-orthogonal-decomposition-line`把$\bm y=(1,1.1,0.9)^\top$分解为$\bm c_1$与余量$(0,0.1,-0.1)^\top$；最近点性质留到10.5.4。

3. 由包含且同维证明$(U^\perp)^\perp=U$。

###### paragraph：四个基本子空间的正交关系

1. 由$\langle\bm A\bm x,\bm y\rangle=\langle\bm x,\bm A^\top\bm y\rangle$证明定理`thm:ls-four-subspaces-orthogonality`（式`eq:ls-four-subspaces-orthogonality`、`eq:ls-four-subspaces-decomposition`）。

2. 再取正交补得另两式，解释输入端分成被消去的零空间与影响输出的行空间，输出端分成可达的列空间与不可达的左零空间。

3. 与秩零度定理比较再得行秩等于列秩，回扣第9章四个子空间的算例；指出由此得到的有解判据（$\bm b$与左零空间正交）供第12章使用。

#### 10.5.2 标准正交基

1. 从Gram方程、坐标下的加权内积与近共线基的系数放大都来自Gram矩阵非对角元进入，说明本小节研究Gram矩阵为单位矩阵的基：证明它是基，再给出坐标、正交矩阵与这类基之间的换基。

###### paragraph：标准正交基的定义

1. 以$\langle\bm q_i,\bm q_j\rangle=\delta_{i,j}$定义标准正交组及子空间的标准正交基，其Gram矩阵为$\bm I_r$。

2. 在$\mathbb R^m$中条件写作$\bm Q^\top\bm Q=\bm I_r$；$r=m$时为正交矩阵，$r<m$时$\bm Q\bm Q^\top\neq\bm I_m$、$\bm Q$只有左逆。

###### paragraph：标准正交组构成基

1. 与各$\bm q_i$作内积证明标准正交组线性无关，并推广到两两正交的非零向量组。

2. 结论：标准正交组是所张成子空间的基，维数个两两正交单位向量自动构成整个空间的标准正交基；举出$\mathbb R^2$中的两组例子。

###### paragraph：标准正交基下的坐标

1. 推出标准正交展开（式`eq:ls-orthonormal-expansion`）与Parseval恒等式（式`eq:ls-parseval`），说明每个系数只与自身方向有关、坐标下的内积成为欧氏内积。

2. 示例`ex:ls-orthonormal-coordinates`对$(3,1)^\top$直接读出坐标并核对平方和为$10$；说明“小对象、大系数”不再发生。

###### paragraph：正交矩阵

1. 把以标准正交基为列的方阵定义为正交矩阵，举单位矩阵与置换矩阵。

2. 示例`ex:ls-rotation-orthogonal`检验平面旋转是正交矩阵，并以$\operatorname{diag}(2,1)$说明只有各列正交还不够；由逐列检验繁琐引出矩阵形式的条件。

###### paragraph：正交矩阵的转置条件

1. 用$(\bm Q^\top\bm Q)_{i,j}$是第$i$、$j$列的内积，把定义改写为$\bm Q^\top\bm Q=\bm I_n$；示例`ex:ls-orthogonality-by-transpose`用这一条件重新检验$\bm R_\phi$与$\operatorname{diag}(2,1)$。

###### paragraph：正交矩阵保持内积

1. 由内积中的转置与转置条件证明$\langle\bm Q\bm x,\bm Q\bm y\rangle=\langle\bm x,\bm y\rangle$，正交矩阵把两两正交的向量送到两两正交的向量。

###### paragraph：正交矩阵的乘法

1. 由转置条件验证$\bm Q_1\bm Q_2$仍正交；示例`ex:ls-rotation-composition`用和角公式说明两个旋转之积为$\bm R_{\phi+\psi}$。

###### paragraph：正交矩阵的逆

1. 说明转置条件只给出左逆，借方阵的单侧逆即逆（`sec:ls-square-one-sided-inverse`）得$\bm Q^{-1}=\bm Q^\top$与$\bm Q\bm Q^\top=\bm I_n$，从而各行也标准正交，且$\bm Q^{-1}$仍正交。

###### paragraph：正交矩阵的行列式

1. 由$\det(\bm Q^\top\bm Q)=1$与转置不变得$\det\bm Q=\pm1$，以旋转与交换坐标分别说明保定向与反定向。

###### paragraph：标准正交基之间的换基

1. 证明两组标准正交基之间的换基矩阵满足$\bm S^\top\bm S=\bm I$，反向换基只需转置，不会出现除以小数$\varepsilon$的放大。

2. 说明对算子相似关系变为$\bm B=\bm P^\top\bm A\bm P$，谱定理在这种受限换基下化简对称矩阵。

###### paragraph：正交不变性

1. 由正交矩阵保持欧氏长度，得到$\lVert\bm Q\rVert_2=1$，左乘正交矩阵不改变Frobenius范数与谱范数。

#### 10.5.3 Gram--Schmidt正交化

1. 说明本小节把任意线性无关组改造成标准正交组：思路来自正交分解，依次扣除已得方向上的分量再归一化；随后写成QR分解，并处理列相关的情形。

##### 10.5.3.1 Gram--Schmidt正交化

1. 写出Gram--Schmidt正交化的递推（式`eq:ls-gram-schmidt`），说明$\bm u_j$是正交分解中的剩余分量。

2. 对$j$归纳证明定理`thm:ls-gram-schmidt`：$\bm u_j$与前面方向正交，$\bm u_j\neq\bm0$由线性无关保证，前$j$个新旧方向张成同一子空间。

3. 推出每个有限维内积空间都有标准正交基，任何标准正交组都能扩充为标准正交基；说明张成空间逐段相等意味着正交化只在每一段内部换基。

###### paragraph：算例

1. 指出两点内积下$\langle1,t\rangle=1\neq0$；示例`ex:ls-gram-schmidt-two-point`对基$(1,t)$分五步正交化：归一化得$q_1=1/\sqrt2$，扣除分量得$t-\tfrac12$，再归一化得$q_2=\sqrt2(t-\tfrac12)$，核对正交与单位长度，最后读出$1+t$的坐标并验证Parseval恒等式。

2. 与系数欧氏内积下$1,t$本已正交对照，说明标准正交基依赖内积。

##### 10.5.3.2 QR分解

1. 在$\mathbb R^m$中把正交化反写为$\bm a_j=\sum_{i\leq j}r_{i,j}\bm q_i$，合写为经济型QR分解（式`eq:ls-qr-factorization`），说明$\bm Q$的列是列空间的标准正交基、$\bm R$上三角且可逆。

2. 图`fig:vol1-add-linear-qr-columns`给出二维情形；说明列空间计算可改在$\bm Q$上进行，第12章解方程与最小二乘时使用。

##### 10.5.3.3 列相关时的处理

1. 说明出现$\bm u_j=\bm0$恰表示该列没有新方向，应跳过并只在$\bm R$中记下系数；处理完后$\bm Q$的列数等于秩，$\bm R$为$r\times d$阶梯形。

2. 示例`ex:ls-qr-dependent-columns`以共线两列$(1,0)^\top,(2,0)^\top$演示；指出有限精度下怎样判断余量为零、怎样减少正交性损失留到数值敏感性一节（`sec:ls-numerical-sensitivity`）。

#### 10.5.4 正交投影

1. 说明本小节把标准正交基下逐个读出的分量合成正交投影，证明它是最近点，再写成矩阵并给出判别方法。

###### paragraph：向子空间的正交分解

1. 在子空间的标准正交基下Gram方程直接给出系数，写出正交投影（式`eq:ls-orthonormal-projection`），由勾股定理得部分系数平方和不超过总长度平方、等号恰在$\bm x\in U$时成立。

2. 把$\bm x-\bm v$拆成$U^\perp$与$U$中两部分，由勾股定理证明投影是唯一最近点；说明非标准正交基可先解Gram方程。

3. 指出唯一性来自内积：回用10.3.6中一般范数下最近点存在的结论与示例`ex:ls-linf-nonunique-nearest`的非唯一最近点，与欧氏范数下只有原点对照。

4. 示例`ex:ls-orthonormal-projection-line`不解Gram方程重算前面的正交分解。

###### paragraph：投影矩阵

1. 由正交分解的唯一性说明投影随原向量线性变化，因而是线性映射。

2. 在欧氏内积下写出$\bm P_U=\bm Q\bm Q^\top$（式`eq:linear-algebra-orthogonal-projector`），验证幂等与对称并解释其含义，指出像为$U$、$\bm Q$非方阵时$\bm P_U$不是单位矩阵。

###### paragraph：正交投影、斜投影与幂等

1. 提出怎样判断一个矩阵是否为正交投影；说明一般幂等矩阵把向量分成像与零空间中的两部分，但两部分不必正交，称为斜投影。

2. 示例`ex:ls-oblique-projection`以$\left[\begin{smallmatrix}1&-1\\0&0\end{smallmatrix}\right]$说明幂等而不对称的投影不给出最近点。

3. 证明幂等且对称时残差与像正交，由正交分解的唯一性得到正交投影；归纳为“先验幂等、再验对称”两步。

### 10.6 线性泛函的内积表示与伴随

1. 从对偶空间中的读取与被读取向量不在同一空间进入，说明有了内积，读取可写成与固定向量的内积，对偶映射随之成为伴随；回指四个基本子空间的证明已用到伴随在欧氏内积下的形式。

#### 10.6.1 线性泛函的内积表示

1. 从欧氏内积下读取即与系数向量的内积进入，借标准正交基构造表示向量并证明唯一，得到有限维Riesz表示定理`thm:ls-riesz-representation`。

2. 说明表示对应是$V^*$到$V$的线性双射，标准正交基的对偶基就是自身，图`fig:ls-dual-basis-readout`中的红色箭头即对偶读取的表示向量。

3. 说明表示向量依赖内积而读取本身不依赖：加权内积下为$\bm M^{-1}\bm a$；示例`ex:ls-riesz-integral-two-point`中积分读取在两点内积下对应常数$\tfrac12$（梯形公式对一次函数精确）。

4. 由Cauchy--Schwarz不等式证明单位球上读取的最大值$\lVert\varphi\rVert_*=\lVert\bm v_\varphi\rVert$，欧氏内积下即$\ell_2$范数自对偶。

#### 10.6.2 伴随与特殊线性算子

1. 从对偶映射把读取$f$传回为$f\circ T$、再把读取换成表示向量进入，给出伴随定义`def:linear-algebra-adjoint`（式`eq:ls-adjoint-pairing`）。

2. 由Riesz表示定理证明伴随存在、唯一且线性；用对偶映射的语言说明伴随就是借内积把读取换成向量后的对偶映射。

3. 在两端的基下用Gram矩阵$\bm M_V,\bm M_W$推出伴随矩阵$\bm M_V^{-1}\bm A^\top\bm M_W$（式`eq:ls-weighted-adjoint`），标准正交基下退化为$\bm A^\top$。

4. 示例`ex:ls-weighted-adjoint`在$\operatorname{diag}(4,1)$加权内积下算出伴随矩阵$\left[\begin{smallmatrix}0&0\\4&0\end{smallmatrix}\right]\neq\bm A^\top$并直接核对；说明差别来自读取与向量的对应随内积改变，并把四个基本子空间的正交关系推广为$\ker T^\star=(\operatorname{im}T)^\perp$、$\ker T=(\operatorname{im}T^\star)^\perp$。

###### paragraph：伴随的运算规则

1. 由配对定义推出伴随对加法、数乘、复合（次序反转）与二次伴随的规则，图`fig:ls-adjoint-action-transfer`示意配对从输出端搬回输入端。

2. 示例`ex:ls-adjoint-not-inverse`以$2\operatorname{id}$的伴随为自身而逆为$\tfrac12\operatorname{id}$说明伴随不是逆。

###### paragraph：自伴、正交与正规算子

1. 用伴随定义自伴算子、保持内积的正交算子与满足$TT^\star=T^\star T$的正规算子，说明前两者在标准坐标下对应对称矩阵与正交矩阵且都是正规算子，谱性质留到第11章。

###### paragraph：复空间中的泛函表示与伴随

1. 按复内积约定把线性泛函写成$\langle\bm v,\bm x\rangle$，给出标准正交基下的表示向量$\sum_j\overline{\varphi(\bm q_j)}\bm q_j$，说明表示对应共轭线性。

2. 以$\mathbb C$上$\varphi(z)=(1+\mathrm i)z$对应$v=1-\mathrm i$核验，说明共轭来自内积约定。

3. 给出复伴随在标准正交基下为$\bm A^*$、一般基下为$\bm M_V^{-1}\bm A^*\bm M_W$，与代数对偶映射的$\bm A^\top$区分，并定义Hermitian（自伴）矩阵与酉矩阵。

### 10.7 本章小结

1. 按“范数与距离—收敛与连续—有限维性质”回顾分析基础：坐标范数的显式比较；收敛等价于逐坐标收敛、联合极限与连续、闭有界集上的极值与一致连续；范数等价使收敛、连续与柯西性质不依赖范数而常数会改变；完备性、绝对收敛级数及尾和估计；矩阵范数与线性映射的Lipschitz连续、对偶范数、商范数与最近点的存在但未必唯一。

2. 回顾内积部分：内积给出长度、夹角与正交，并非每个范数来自内积，有限维内积空间是Hilbert空间；Gram矩阵与半正定矩阵的对应；正交分解与唯一最近点；标准正交基、Gram--Schmidt正交化与QR分解；泛函表示与伴随连接代数对偶与几何结构。

3. 说明这些工具为下一章寻找线性作用的简单表示做准备，并说明后续直接使用的依据：矩阵幂和级数使用收敛与次乘性，迭代使用完备性和误差估计，多元微分用算子范数控制余项。

## 第11章 谱和奇异值

正文入口：[04-spectral-analysis.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/04-spectral-analysis.tex)。

1. 从第~`chap:linear-representation`章的相似关系$\bm B=\bm P^{-1}\bm A\bm P$（第~`sec:ls-similarity`节）进入：同一线性作用有许多矩阵写法，算子$T(x_1,x_2)=(2x_1+x_2,3x_2)$在标准基下有非零非对角元，换到只被伸缩、不被转向的两个基方向后成为对角矩阵。由此提出本章先研究表示问题——线性作用在什么样的基下最简单，再用这些简单表示解决几个具体问题：长度约束下选最优方向、用低秩矩阵保留主要作用、把长度变化与保长作用分开，以及判断误差、扰动和反复作用的影响。

2. 说明前五节怎样处理表示问题：特征值与特征向量一节寻找只被伸缩的方向，说明特征值不随基改变、由特征多项式求出，并证明Cayley--Hamilton定理；对角化一节判断特征向量何时足以组成基，此时矩阵幂化为对角元乘方，实特征值或特征向量不够时不能对角化，且对角化基未必正交；正交对角化一节要求正交换基，证明能这样对角化的恰是实对称矩阵，并写成谱投影的组合；一般方阵一节说明正交换基下一般方阵只能化为实Schur形、能化为分块对角形的恰是正规矩阵，并引入谱半径；奇异值分解一节让输入、输出各取一组标准正交基，使任意矩阵化为对角形。

3. 说明随后三节各解决一个具体问题：二次型极值一节固定对称矩阵，在欧氏长度或加权长度为一的条件下求二次型的最大、最小值，得到Rayleigh商与广义特征问题；低秩逼近一节在秩约束下使重建误差最小，先在秩一情形用Rayleigh商，再用迹极值证明截断SVD最优；伸缩分离一节把方阵分成保长部分与沿正交方向的伸缩，沿谱开方求伸缩因子、再求正交因子得到极分解，最后把开方与求逆归纳为沿谱构造矩阵函数。

4. 说明最后三节研究误差与反复作用：条件数一节固定矩阵，研究输入误差经一次作用放大多少；谱扰动一节把矩阵本身当作有误差的输入，估计特征值、奇异值、秩和特征子空间的变化；反复更新一节研究$\bm x_{k+1}=\bm T\bm x_k+\bm c$，由矩阵幂判断初值影响是否消失，由Neumann级数给出输入累积所得的平衡，由谱半径决定长期速度，并指出非正规矩阵可能先放大再衰减。最后指出第~`chap:linear-equations-and-optimization`章要用到奇异值分解、Rayleigh商、条件数、谱、Cayley--Hamilton定理、实Schur形与Neumann级数。

5. 说明前置工具与依赖边界：前三章的矩阵运算、换基、范数、内积、正交投影与二次型，第~`chap:normed-inner-product-spaces`章在有限维空间中建立的收敛、连续性、范数等价、完备性与向量和矩阵级数，以及第二部分的复数与一元分析。前五节的谱定理与SVD构造不依赖后面的极值问题或矩阵函数；误差放大与谱扰动只用代数恒等式和有限扰动下的误差比；反复更新直接使用第~`sec:multivariable-limits-continuity`节的矩阵列收敛与第~`sec:ls-vector-matrix-series`节的绝对收敛判据。

### 11.1 特征值与特征向量

从相似一节事先给出、再加验证的对角化基进入，说明本节给出寻找只被伸缩方向的一般方法：依次定义特征向量与特征值，用特征多项式求特征值，证明它们不随基改变，最后证明属于不同特征值的特征向量线性无关。

#### 11.1.1 线性作用中的特征方向

1. 从线性算子一般同时改变长度与方向出发，提出寻找作用后仍落在原直线上的非零向量，单行写出$T\bm v=\lambda\bm v$、$\bm v\neq\bm0$（式`eq:matrix-analysis-eigenpair`），定义特征值、特征向量与特征方向；说明要求非零的原因，并解释$\lambda$的大小与符号对应拉长、缩短、反向与落入核。

2. 由线性性归纳得$T^k\bm v=\lambda^k\bm v$，说明特征方向上的反复作用化为数的乘方；再由坐标形式$[T]_{\mathcal B}[\bm v]_{\mathcal B}=\lambda[\bm v]_{\mathcal B}$说明特征值属于算子本身、换基只改变特征向量的坐标，并据此规定方阵的特征值与特征向量。

3. 示例`ex:ls-operator-eigenvector-check`对$\left[\begin{smallmatrix}2&1\\0&3\end{smallmatrix}\right]$直接相乘，验证$\bm e_1$与$(1,1)^\top$是特征向量、正是相似一节的新基方向，而$\bm e_2$不是（图`fig:ls-operator-eigenvectors`）。

4. 反例`ex:ls-rotation-no-real-eigenvector`对$90^\circ$旋转由$(1+\lambda^2)x_2=0$推出只有零解，说明并非每个算子都有实特征向量。

#### 11.1.2 特征空间与不变子空间

1. 把同一特征值的特征方向放在一起，定义特征空间$\ker(T-\lambda\operatorname{id}_V)$并说明它是子空间；以$\bm I_2$（整个平面）与示例`ex:ls-operator-eigenvector-check`中特征值$2$（$\bm e_1$所在直线）对照。

2. 定义不变子空间，说明特征空间是不变子空间、一维不变子空间恰为特征方向；再以$90^\circ$旋转下不变而不含特征方向的整个平面说明高维不变子空间未必含特征方向，并指出它对应一对共轭复特征值（一般方阵一节）。

#### 11.1.3 特征多项式

1. 为系统求出特征值，把条件依次改写为$\ker(\bm A-\lambda\bm I)\neq\{\bm0\}$、秩小于$n$、不可逆，再用行列式乘法性与古典伴随恒等式证明不可逆等价于行列式为零；顺带指出使$\operatorname{rank}(\bm A-c\bm I)<n$的$c$恰是特征值。

2. 定义首项系数为$1$的特征多项式$p_{\bm A}(z)=\det(z\bm I-\bm A)$（式`eq:matrix-analysis-characteristic-polynomial`），实特征值即其实根；由排列展开只有对角线一项含$z^n$，说明它是$n$次多项式、至多$n$个根，求出特征值后解齐次方程得特征空间。

3. 示例`ex:ls-characteristic-polynomial-two-by-two`用特征多项式重求$\left[\begin{smallmatrix}2&1\\0&3\end{smallmatrix}\right]$的特征值并说明旋转的$z^2+1$无实根，再推广到三角矩阵的特征值是对角元。

4. 说明把矩阵代入自身的特征多项式得到零矩阵，示例`ex:ls-cayley-hamilton-two-by-two`核对$\bm A^2-5\bm A+6\bm I=\bm0$；随后陈述Cayley--Hamilton定理`thm:ls-cayley-hamilton`，证明中把古典伴随恒等式（第~`sec:ls-det-cofactor-adjugate`节，定理`thm:ls-adjugate-identity`）用于$z\bm I-\bm A$，按$z$的幂次展开伴随矩阵、比较系数，再左乘$\bm A^j$相加使相邻项相消；指出证明不要求先求特征值，也不要求$p_{\bm A}$有实根。

5. 陈述并证明定理`thm:ls-power-reduction`（高次幂的降次）：由Cayley--Hamilton得$\bm A^n\in\operatorname{span}\{\bm I,\ldots,\bm A^{n-1}\}$，左乘$\bm A$后把出现的$\bm A^n$再代换，归纳得所有$\bm A^k$属于这个子空间；作用于向量$\bm g$得$\bm A^k\bm g$属于前$n$项张成的子空间，故该子空间至多$n$维、在前$n$项后不再增大，供第~`chap:linear-equations-and-optimization`章的Sylvester方程与Krylov子空间方法使用。

6. 回到重根，定义代数重数与几何重数；示例`ex:ls-multiplicity-gap`以$\left[\begin{smallmatrix}0.8&1\\0&0.8\end{smallmatrix}\right]$算出代数重数$2$、几何重数$1$；一般关系留给对角化一节，并引出下一小节的基无关性。

#### 11.1.4 相似变换与谱的不变性

1. 承接相似一节列出的不变量，说明本小节证明特征值、特征多项式与两种重数也是相似不变量，再由特征值读出迹与行列式，最后指出不变量只能否定相似。

###### paragraph：特征值、特征空间与特征多项式

1. 陈述并证明定理`thm:ls-spectrum-similarity-invariance`（谱的相似不变性）：由$\bm B(\bm P^{-1}\bm v)=\lambda\bm P^{-1}\bm v$得特征值相同，由$\ker(\bm B-\lambda\bm I)=\bm P^{-1}\ker(\bm A-\lambda\bm I)$得几何重数相同（亦可由式`eq:ls-similarity-shifted-rank`与秩零度定理得到），由$\det(\bm P^{-1}\bm M\bm P)=\det\bm M$得$p_{\bm B}=p_{\bm A}$与代数重数相同；结论是这些量可用任意基下的矩阵计算。

###### paragraph：特征多项式的系数

1. 陈述并证明定理`thm:ls-trace-det-eigenvalues`：比较常数项与$z^{n-1}$系数得$p_{\bm A}(z)=z^n-(\operatorname{tr}\bm A)z^{n-1}+\cdots+(-1)^n\det\bm A$，分解为实一次因子时$\operatorname{tr}\bm A=\sum\lambda_i$、$\det\bm A=\prod\lambda_i$；以前例核对，并指出计入复根后对每个方阵成立。

###### paragraph：相似不变量只能否定相似

1. 说明不变量不同可否定相似、全同却未必相似；反例`ex:ls-same-charpoly-not-similar`中$\bm I_2$与$\bm J_1=\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$特征多项式相同而几何重数为$2$与$1$，由定理知不相似；完整分类需要Jordan标准形，本书不展开。

#### 11.1.5 不同特征值对应方向的独立性

1. 说明为用特征方向组成基，本小节先证明不同特征值的特征向量线性无关，再推出特征空间之和是直和。

###### paragraph：特征向量的线性无关

1. 陈述并证明定理`thm:ls-distinct-eigenvectors-independent`：取项数最少的非平凡线性依赖并作用$T-\lambda_1\operatorname{id}_V$得到更短的依赖而矛盾；推出$n$维空间上至多$n$个不同特征值，与特征多项式次数的上界一致。

###### paragraph：特征空间的直和

1. 陈述并证明定理`thm:ls-eigenspaces-direct-sum`：非零分量是不同特征值的特征向量，由上一定理不能相加为零，故和为直和，各特征空间的基合起来仍线性无关、维数相加；说明开头例子的$\bm e_1$与$(1,1)^\top$自动组成基。

###### paragraph：本节结论

1. 归纳特征方向、特征多项式、相似不变性、线性无关性、Cayley--Hamilton定理与高次幂降次，并把特征向量何时足以组成基交给下一节。

### 11.2 对角化

承接上一节，考察特征向量足以组成基的情形：先看这时矩阵和矩阵幂的形式，再给出这种基存在的条件，最后整理计算步骤；强调换基矩阵只要求可逆，各列不必垂直。

#### 11.2.1 特征向量基下的矩阵表示

1. 由线性映射表示的列约定说明特征基下的矩阵是对角的，回到$\operatorname{diag}(2,3)$与相似变换图`fig:ls-similarity-change-of-basis-flow`；再把特征向量排成可逆的$\bm V$，按列读法得$\bm A\bm V=\bm V\bm\Lambda$，即$\bm V^{-1}\bm A\bm V=\bm\Lambda$。

2. 转向定常迭代，由相邻$\bm V^{-1}\bm V$相消得$\bm A^k=\bm V\bm\Lambda^k\bm V^{-1}$（式`eq:ls-diagonalization-power`），并从右向左读作“取特征坐标、逐个乘方、合回标准坐标”。

3. 示例`ex:ls-triangular-power`对$\left[\begin{smallmatrix}0.8&4\\0&0.5\end{smallmatrix}\right]$分三步：验证特征向量$(1,0)^\top$与$(-40/3,1)^\top$，把初值$(0,1)^\top$拆成$\tfrac{40}{3}\bm v_1+\bm v_2$得轨迹，再写出完整的$\bm A^k$并核对第二列；指出这种计算的前提是特征向量组成基。

#### 11.2.2 可对角化的条件与边界

把“特征向量组成一组基”写成相似于实对角矩阵，给出判据，说明判据落空的两种方式，再化为可直接计算的重数条件。

1. 把相似于实对角矩阵取作定义`def:ls-real-diagonalizable`并说明“实”的含义；按列读法证明对角化判据`thm:ls-diagonalization-criterion`：可对角化当且仅当有$n$个线性无关的实特征向量。

2. 由不同特征值的特征向量线性无关，推出$n$个不同实特征值是充分条件（前例即属此类），并以$\bm I_n$说明它不必要。

###### paragraph：不能对角化的矩阵

1. 说明判据在两处落空：$90^\circ$旋转没有实特征值（回指示例`ex:ls-rotation-no-real-eigenvector`与`ex:ls-characteristic-polynomial-two-by-two`）；$\bm J=\left[\begin{smallmatrix}0.8&1\\0&0.8\end{smallmatrix}\right]$的特征向量只有$(1,0)^\top$的倍数。

2. 示例`ex:ls-jordan-block-power`把$\bm J$写成$0.8\bm I+\bm N$，借$\bm N^2=\bm0$与可交换性二项展开得$\bm J^k$，再由相邻项之比$0.8(k+1)/k$说明右上角$k\,0.8^{k-1}$先增后减，不能由单个特征值的乘方描述。

###### paragraph：重数判据

1. 用重数说明两个反例的缺陷：$z^2+1$不能分解为实一次因子，$(z-0.8)^2$分解了但几何重数小于代数重数；指出这两种缺陷恰是全部障碍。

2. 陈述并证明定理`thm:ls-geometric-algebraic-multiplicity`（几何重数不超过代数重数，$1\leq g\leq m$且$(z-\lambda)^g$整除$p_{\bm A}$）：把特征空间的基扩充为全空间的基组成$\bm P$，$\bm P^{-1}\bm A\bm P$成分块上三角形，沿前$g$列逐次展开行列式得$p_{\bm A}(z)=(z-\lambda)^g p_{\bm C}(z)$；示例`ex:ls-multiplicity-gap`说明不等号可严格成立。

3. 以这一不等式为过渡，把特征向量判据改写成定理`thm:ls-diagonalization-multiplicity`（重数判据）：可对角化当且仅当特征多项式分解为$n$个实一次因子且各几何重数等于代数重数；证明中充分性用特征空间之和是直和与定理`thm:ls-diagonalization-criterion`，必要性用相似不变性；最后说明$n$个不同实特征值的充分条件是其特例。

#### 11.2.3 对角化的计算与用途

1. 按判据归纳“求特征值、求特征空间、组成$\bm V$与$\bm\Lambda$、核对”四步，并说明实根不够或特征空间维数不足时在第一步或第三步停止，对应上一小节的两种情形。

2. 由每期$10\%$与$20\%$的两状态转移写出$\bm x^{(k+1)}=\bm A\bm x^{(k)}$；示例`ex:ls-transition-matrix-diagonalization`对$\left[\begin{smallmatrix}0.9&0.2\\0.1&0.8\end{smallmatrix}\right]$完整执行四步，得特征值$1,0.7$与特征向量$(2,1)^\top,(1,-1)^\top$，核对$\bm A\bm V=\bm V\bm\Lambda$并用迹与行列式快速检查。

3. 示例`ex:ls-transition-matrix-long-run`沿用该分解写出$\bm A^k$与从状态一出发的轨迹，得长期比例$(2/3,1/3)^\top$；再对一般初值求$\bm V^{-1}\bm x^{(0)}$，沿$\bm v_1$的分量恒为$1/3$、沿$\bm v_2$的分量按$0.7^k$消失，说明长期比例与初值无关。

4. 节末归纳特征基、$\bm A^k=\bm V\bm\Lambda^k\bm V^{-1}$与两种判据；指出转移矩阵的两条特征方向内积为$1$、并不垂直，换基要解方程且不保持长度，引出下一节的正交对角化。

### 11.3 正交对角化

1. 承接上一节的对角化只要求$\bm V$可逆，指出这样的特征基一般是斜基：坐标平方和不等于长度平方，坐标轴夹角也不是直角。本节保持同一分解问题，但要求换基矩阵正交，依次回答三个问题：哪些实矩阵能在标准正交基下对角化；怎样求出并检验这种分解；特征值重复时，分解中哪些部分仍由矩阵唯一确定。

2. 预告三个答案：第一个是实对称矩阵（谱定理）；第二个是一条手算路线和逐项核验；第三个是特征子空间及到它们的正交投影——重根空间内特征基可任意旋转，投影不变，并由此读出定号性。说明一般方阵留给下一节的Schur形，本节的分解从11.6节起分别用于二次型极值、最佳低秩逼近与伸缩分离。

#### 11.3.1 实对称矩阵的谱定理

1. 先说明特征方向互相垂直时换基最简单：标准正交基排成的$\bm Q$满足$\bm Q^{-1}=\bm Q^\top$，新坐标就是内积$c_i=\bm q_i^\top\bm x$且长度保持（第~`sec:ls-orthonormal-bases`节）；若$\bm S=\bm Q\bm\Lambda\bm Q^\top$，作用可读成“取坐标、逐个伸缩、合回去”。

2. 转向哪些矩阵能这样写：对分解取转置由$\bm\Lambda^\top=\bm\Lambda$得$\bm S^\top=\bm S$，故对称是必要条件，并联系第~`sec:ls-adjoints`节的自伴映射；提出对称是否也充分，本小节给出肯定回答。

3. 交代证明思路：先找一个实特征向量，再在与它垂直的子空间中重复；指出第一步并不平凡，旋转矩阵（示例`ex:ls-rotation-no-real-eigenvector`）说明一般实矩阵可能没有实特征值，对称性的作用正是排除这种情形。

4. 引入所需的复数工具：由代数基本定理，$p_{\bm S}$在复数范围内至少有一个根$\lambda$；行列式与消元只用四则运算，在复数域中照样成立，故有非零复向量$\bm z$满足$\bm S\bm z=\lambda\bm z$；再定义共轭内积$\bar{\bm z}^\top\bm z=\sum_i|z_i|^2>0$，说明它将用来证明$\lambda$为实数。

5. 陈述谱定理`thm:ls-real-symmetric-spectral`（式`eq:matrix-analysis-symmetric-eigendecomposition`写出$\bm S=\bm Q\bm\Lambda\bm Q^\top$与$\bm S\bm q_i=\lambda_i\bm q_i$，式`eq:matrix-analysis-quadratic-spectral-form`写出$\bm x^\top\bm S\bm x=\sum\lambda_ic_i^2$），对维数归纳分三步证明：用两种方式计算$\bar{\bm z}^\top\bm S\bm z$得$(\lambda-\bar\lambda)\bar{\bm z}^\top\bm z=0$，故$\lambda$为实数；比较$\bm z=\bm x+\mathrm i\bm y$的实部与虚部得$\bm S\bm x=\lambda\bm x$、$\bm S\bm y=\lambda\bm y$，取非零者单位化为$\bm q_1$；由对称性得$\bm q_1^\perp$不变，取其标准正交基$\bm U$写$\bm S\bm U=\bm U\bm S'$，对$d-1$阶对称矩阵$\bm S'=\bm U^\top\bm S\bm U$用归纳假设并合成$\bm Q$；最后代入二次型说明交叉项为零。

6. 说明证明用到的是代数基本定理与对称性：前者保证复特征向量存在，后者先使特征值为实、再使正交补不变；复数只出现在第一步，所得$\bm Q$、$\bm\Lambda$都是实的；证明不依赖二次型在单位球面上的极值，11.6节反过来由谱分解读出极值；并约定特征值按降序排列。

7. 补充对称性直接给出的正交关系：由$\lambda\bm u^\top\bm w=\bm u^\top\bm S\bm w=\mu\bm u^\top\bm w$得属于不同特征值的特征空间互相正交，说明这一点不依赖$\bm Q$的选法，下一小节计算时要用。

#### 11.3.2 谱分解的计算与核验

1. 指出谱定理的证明是归纳式的，没有直接给出计算步骤，于是对手算规模的对称矩阵给出次序：解$p_{\bm S}(z)=0$得全部（由谱定理均为实数、按重数共$d$个）特征值；对每个不同特征值解齐次方程得特征空间的基；在每个特征空间内部作Gram--Schmidt正交化（定理`thm:ls-gram-schmidt`）并单位化；最后按同一顺序组装$\bm Q$与$\bm\Lambda$。

2. 解释为什么只需在各特征空间内部正交化：上一小节已证不同特征值的特征空间互相正交，跨空间的向量自动垂直；重根空间中解方程得到的基一般不正交，须在空间内部重新选标准正交基；各特征空间维数之和为$d$也由谱定理保证。

3. 给出两项核验及其作用：$\bm Q^\top\bm Q=\bm I$保证$\bm Q^{-1}=\bm Q^\top$；$\bm S\bm Q=\bm Q\bm\Lambda$逐列就是$\bm S\bm q_i=\lambda_i\bm q_i$，同时检查特征值与列的顺序是否一致；两项成立后右乘$\bm Q^\top$即得分解。

4. 示例`ex:ls-symmetric-spectral-two-by-two`对$\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$走完全过程：由$(z-3)(z-1)$得特征值$3,1$，特征空间分别由$(1,1)^\top$与$(1,-1)^\top$张成，单根只需单位化；逐项核对$\bm Q^\top\bm Q=\bm I$与$\bm S\bm Q=\bm Q\bm\Lambda$，结论是$\bm S$把$(1,1)^\top$方向放大$3$倍、保持$(1,-1)^\top$方向。

5. 用这个分解解释作用的三步：$\bm Q^\top$转到特征坐标，$\bm\Lambda$分别伸缩，$\bm Q$转回；正交因子保持长度与夹角，改变形状的只有$\bm\Lambda$。以$\bm S\bm e_1=(2,1)^\top$与$\bm S\bm e_2=(1,2)^\top$夹角余弦为$4/5$说明整体作用一般改变夹角，只有特征方向间的直角得以保持。

6. 限定这条路线的适用范围：它适合手算小矩阵，要求写出特征多项式并求出全部根，阶数较高时这一步本身难以手工完成，大规模矩阵的数值特征值算法不在本节讨论；无论用哪种方法得到$\bm Q$与$\bm\Lambda$，两项核验都只用矩阵乘法，同样适用，且二者成立就足以推出分解。

#### 11.3.3 特征子空间与谱投影

1. 从重特征值时$\bm Q$不唯一进入，提出在这种不唯一下分解中哪些部分由$\bm S$本身确定；先把分解按列展开为秩一和$\bm S=\sum_i\lambda_i\bm q_i\bm q_i^\top$，由式`eq:linear-algebra-orthogonal-projector`说明每项是到$\bm q_i$方向的正交投影，并写出示例`ex:ls-symmetric-spectral-two-by-two`的两项分解；指出单项$\bm q_i\bm q_i^\top$会随重根空间内的选择改变，应把同一特征值的项合并。

2. 引入记号：不同特征值$\mu_1,\ldots,\mu_m$、特征空间$E_j=\ker(\bm S-\mu_j\bm I)$、由$\bm Q$中对应列组成的$\bm Q_j$与$\bm P_j=\bm Q_j\bm Q_j^\top$。陈述谱投影定理`thm:ls-spectral-projections`的四条结论并逐条证明：把$\bm x=\sum c_i\bm q_i$代入$(\bm S-\mu_j\bm I)\bm x$得$E_j=\operatorname{range}\bm Q_j$，由此得两两正交与维数之和为$d$；$\bm P_j$是到$E_j$的正交投影，由$\bm Q_j^\top\bm Q_k=\bm0$得$\bm P_j\bm P_k=\bm0$，把$\bm Q\bm Q^\top$按特征值分组得$\sum\bm P_j=\bm I$；合并同一特征值的项得$\bm S=\sum\mu_j\bm P_j$；对$E_j$的另一组标准正交基写$\bm Q_j'=\bm Q_j\bm R$，验证$\bm R$正交，从而$\bm Q_j'\bm Q_j'^\top=\bm P_j$，即投影与基的选取无关。

3. 定义谱投影，说明重根空间内的基选择只是同一投影的不同写法；示例`ex:ls-repeated-eigenspace-projection`取$\bm S=\bm I+\bm 1\bm 1^\top$，由$\bm S\bm 1=4\bm 1$与$\bm x\perp\bm 1$时$\bm S\bm x=\bm x$得特征值$4$（单根）与$1$（二重），对平面$x_1+x_2+x_3=0$中不正交的基作Gram--Schmidt，再从另一向量出发得另一组标准正交基，两次相加都得$\bm P_1=\bm I-\frac13\bm 1\bm 1^\top$，结论是$\bm S=4\bm P_4+\bm P_1$、基可换而投影不变。

4. 转向谱分解对定号性的回答：第~`sec:ls-positive-definite`节的定义要检查所有$\bm x$上的二次型，而在特征坐标下二次型化为$\sum\lambda_ic_i^2$、交叉项消失。陈述并证明定理`thm:ls-symmetric-definiteness-eigenvalues`：必要性取$\bm x=\bm q_i$得$\bm q_i^\top\bm S\bm q_i=\lambda_i$；充分性由$\sum\lambda_ic_i^2\geq\lambda_d\lVert\bm x\rVert_2^2$得到正定情形的正下界。

5. 说明判据的用途与界限：奇异值分解一节构造奇异值时，要由$\bm A^\top\bm A$半正定得特征值非负、可以开方；证明中的$\bm q_i^\top\bm S\bm q_i=\lambda_i$只说明特征方向上的二次型值，在全部单位方向中何者最大最小是另一个问题，留到11.6节。

6. 节末归纳：能用正交矩阵对角化的恰是对称矩阵，分解是沿互相垂直方向的伸缩，可按“求特征值、求特征空间、空间内正交化、组装并核验”算出；特征子空间与谱投影由$\bm S$唯一确定，$\bm S=\sum\mu_j\bm P_j$；定号性由特征值符号决定。再以平面旋转与上三角矩阵$\left[\begin{smallmatrix}0.8&4\\0&0.5\end{smallmatrix}\right]$不对称为由，引出下一节一般方阵在正交换基下能化到多简单。

### 11.4 一般方阵的Schur形

从前两节对角化的前提出发，指出不对称方阵可能实特征值不够（$90^\circ$旋转），也可能特征向量互不正交（夹角约$4.3^\circ$的上三角例子）；说明本节分三步：复特征值与谱半径、实Schur形、正规矩阵的刻画。

#### 11.4.1 复特征值与实不变平面

1. 借代数基本定理把特征多项式的复根都算作特征值、定义谱，说明非实根成共轭对出现，迹与特征值和、行列式与特征值积的关系对每个方阵成立。

2. 比较复特征向量的实部与虚部得到$\bm A\bm u=a\bm u-b\bm w$、$\bm A\bm w=b\bm u+a\bm w$，用反证（否则得到一条不变直线、$\lambda$为实数）说明$\bm u,\bm w$线性无关，从而一对共轭特征值对应二维实不变子空间；在基$(\bm u,\bm w)$下作用为模长乘旋转，并提醒这组基一般不标准正交。

3. 说明$|\lambda|$是特征方向或平面坐标中的每次倍率而非一步最大放大，定义谱半径$\rho(\bm A)$，以$90^\circ$旋转（谱半径$1$）示例。

#### 11.4.2 实Schur分解

###### paragraph：实Schur形

1. 说明一般方阵退而求其次化为上三角形的好处，以及实特征值不够时须允许$2\times2$对角块；对维数归纳、每次取一维特征方向或二维不变子空间并扩充为正交矩阵，对右下角的压缩矩阵归纳（正交补未必不变），证明实Schur形定理`thm:ls-real-schur`（式`eq:matrix-analysis-schur-decomposition`）；指出数值上由Hessenberg化与带位移QR迭代求得，本卷只用其存在性，并在Sylvester方程一节（第~`sec:ls-sylvester-schur`节）使用。

#### 11.4.3 正规矩阵与非正规矩阵

1. 确定Schur形何时分块对角：先看实对称矩阵，其Schur形仍对称、只能是对角矩阵，再次得到谱定理；再由第~`sec:ls-adjoints`节的正规算子定义正规矩阵$\bm A^\top\bm A=\bm A\bm A^\top$（对称、反对称、正交矩阵均是）。

2. 证明正规矩阵的Schur形分块对角：$\bm T$也正规，比较$\bm T^\top\bm T$与$\bm T\bm T^\top$左上角块的迹，得第一块行的非对角块为零，再逐块递推。

3. 比较$2\times2$对角块的元素，推出每块形如$\left[\begin{smallmatrix}a&b\\-b&a\end{smallmatrix}\right]$；反过来这种分块对角形必正规，从而刻画正规矩阵。由此得$\lVert\bm A^k\rVert_2=\rho(\bm A)^k$，即正规矩阵每一步的最大放大等于谱半径。

###### paragraph：非正规矩阵

1. 由上述刻画指出非正规矩阵的Schur形不是上述分块对角形，也不能用标准正交特征向量对角化；示例`ex:ls-nonnormal-norm-radius`对$\left[\begin{smallmatrix}0.8&4\\0&0.5\end{smallmatrix}\right]$比较$(1,1)$元验证不正规，得$\rho=0.8$、$\lVert\bm A\rVert_2>4$、特征方向夹角约$4.3^\circ$。

2. 区分谱半径描述的长期倍率与范数描述的一步放大，指出二者分离可能伴随先放大、后衰减的瞬态（第~`sec:ls-convergence-rate-transient`节）；节末归纳复特征值、谱半径、实Schur形与正规矩阵，并以“输入、输出用同一组基”的限制引出奇异值分解。

### 11.5 奇异值分解

1. 回顾前几节都让输入与输出使用同一组基，在这一要求下用标准正交基换基时只有对称矩阵化为实对角形、正规矩阵化为分块对角形、一般方阵只能化为实Schur形；指出矩形矩阵$\bm A\in\mathbb R^{m\times d}$的输入、输出不在同一空间，“同一组基”与特征向量都无从谈起。

2. 提出放宽的要求：在输入端与输出端各找一组标准正交方向，使$\bm A\bm v_i=\sigma_i\bm u_i$、$\sigma_i\geq0$，即把第$i$个输入方向伸缩后送到第$i$个输出方向，输入维数更大时多出的基向量映到零。

3. 说明本节的分工与边界：先证明任意矩阵都有这两组方向（输入方向取$\bm A^\top\bm A$的特征方向，构造只用谱定理`thm:ls-real-symmetric-spectral`），再从分解读出谱范数、Frobenius范数、秩与最弱放大倍数；Rayleigh商留给11.6节，最佳低秩逼近留给11.7节，极分解留给11.8节。

#### 11.5.1 奇异值分解的构造

1. 先倒推所求方向应满足的条件：设$\bm x=\sum c_i\bm v_i$，由$\bm u_i$标准正交得$\bm x^\top\bm A^\top\bm A\bm x=\sum\sigma_i^2c_i^2$，与二次型展开式`eq:matrix-analysis-quadratic-spectral-form`比较，看出$\bm v_i$应是$\bm A^\top\bm A$的特征向量、$\sigma_i^2$是对应特征值，所以构造从$\bm A^\top\bm A$出发。

2. 构造输入方向：$\bm A^\top\bm A$对称且半正定，由谱定理取标准正交特征基$\bm v_i$、特征值降序非负；前$r$个正特征值开方得$\sigma_i$，其余$\bm v_j$由$\lVert\bm A\bm v_j\rVert_2^2=0$得$\bm A\bm v_j=\bm0$。

3. 构造输出方向：令$\bm u_i=\bm A\bm v_i/\sigma_i$（$i\leq r$），由$\bm v_i^\top\bm A^\top\bm A\bm v_j=\sigma_j^2\delta_{i,j}$验证标准正交，再扩充为$\mathbb R^m$的标准正交基。

4. 把任意$\bm x$按$\bm v_i$展开，写出秩一和式$\bm A=\sum_{i\leq r}\sigma_i\bm u_i\bm v_i^\top$（式`eq:matrix-analysis-svd-rank-one-sum`），读出值域由$\bm u_1,\ldots,\bm u_r$张成、核由$\bm v_{r+1},\ldots,\bm v_d$张成，从而$r=\operatorname{rank}\bm A$；排成矩阵得SVD存在定理`thm:ls-svd-existence`，并给出奇异值分解、奇异值与左右奇异向量的定义`def:matrix-analysis-svd`（式`eq:matrix-analysis-svd`）。

5. 用图`fig:ls-svd-construction`以$\left[\begin{smallmatrix}2&0.5\\0.5&1\end{smallmatrix}\right]$复述“形成$\bm A^\top\bm A$、谱定理对角化、开方并由$\bm u_i=\bm A\bm v_i/\sigma_i$得左奇异向量”三步。

6. 补出输出端的对称关系：$i\leq r$时$\bm A^\top\bm u_i=\sigma_i\bm v_i$、$\bm A\bm A^\top\bm u_i=\sigma_i^2\bm u_i$（式`eq:ls-svd-transpose-relation`），$i>r$时$\bm u_i$与值域正交，故$\bm A^\top\bm u_i=\bm0$；结论是$\bm u_i$构成$\bm A\bm A^\top$的标准正交特征基，$\bm A^\top\bm A$与$\bm A\bm A^\top$有相同的正特征值，这一关系供11.7节秩一逼近使用。

7. 证明奇异值由$\bm A$唯一确定：对任一满足定理的分解，$\bm A^\top\bm A=\bm V(\bm\Sigma^\top\bm\Sigma)\bm V^\top$与对角矩阵$\bm\Sigma^\top\bm\Sigma$相似，由定理`thm:ls-spectrum-similarity-invariance`二者特征多项式相同，所以$\sigma_i^2$连同重数恰是$\bm A^\top\bm A$的特征值，奇异值与分解的选取无关。

8. 说明奇异向量不唯一：构造对$\bm A^\top\bm A$任一组降序排列的标准正交特征向量都成立，正奇异值重复时可在对应特征空间内另选标准正交基并由$\bm u_i=\bm A\bm v_i/\sigma_i$重新配对；一对$\bm u_i,\bm v_i$同时变号也不改变$\sigma_i\bm u_i\bm v_i^\top$。

9. 比较三种写法：完整分解给出两端全部正交方向（核与值域的正交补）；经济型分解$\bm A=\bm U_p\bm\Sigma_p\bm V_p^\top$（$p=\min(m,d)$）删去$\bm\Sigma$中全零的行或列及相应向量；秩分解$\bm A=\bm U_r\bm\Sigma_r\bm V_r^\top$只保留正奇异值，即秩一和式的矩阵写法。说明三者给出同一矩阵，区别在于是否保留零空间方向。

10. 提醒构造路线只用于证明存在性，不意味着数值计算应显式形成$\bm A^\top\bm A$：其特征值是$\sigma_i^2$，最大与最小奇异值之比在其中变成平方；这种平方带来的误差风险由第~`sec:ls-ls-regularization-sensitivity`节以正规方程为例分析，实际SVD算法直接作用于$\bm A$，其构造与误差分析不在本书展开。

#### 11.5.2 奇异值与矩阵的大小

1. 用三步读法给出几何图像：$\bm V^\top$取右奇异坐标，$\bm\Sigma$逐个伸缩，$\bm U$放到左奇异方向，只有中间一步改变长度；再证明单位球的像恰为$\operatorname{span}\{\bm u_1,\ldots,\bm u_r\}$中满足$\sum_{i\leq r}(\bm u_i^\top\bm y)^2/\sigma_i^2\leq1$的点集——单位球中$\bm x=\sum c_i\bm v_i$的像坐标为$\sigma_ic_i$，反过来满足不等式的$\bm y$是$\sum(y_i/\sigma_i)\bm v_i$的像——即以$\sigma_i\bm u_i$为半轴的椭球（秩亏时落在低维子空间内）；以$(\bm v_1+\bm v_d)/\sqrt2$被送到$\sigma_1\bm u_1/\sqrt2$说明$r<d$时球面上的点可映到椭球内部，所以用单位球描述整个像；图`fig:matrix-analysis-svd-geometry`以$\bm R(\pi/6)\operatorname{diag}(2,0.4)\bm R(\pi/5)^\top$说明输入与输出方向可以不同。

2. 回答第~`sec:ls-frobenius-norm`节与第~`sec:ls-matrix-norms`节未给出的谱范数算法：由$\lVert\bm A\bm x\rVert_2^2=\sum\sigma_i^2c_i^2\leq\sigma_1^2\lVert\bm x\rVert_2^2$且在$\bm v_1$取等，得$\lVert\bm A\rVert_2=\sigma_1$（式`eq:matrix-analysis-spectral-norm`）；由$\bm A^\top\bm A=\bm V(\bm\Sigma^\top\bm\Sigma)\bm V^\top$与迹的循环性得$\lVert\bm A\rVert_{\mathrm F}^2=\operatorname{tr}(\bm A^\top\bm A)=\sum\sigma_i^2$，即Frobenius范数为奇异值平方和的平方根（式`eq:matrix-analysis-frobenius-norm`）；正奇异值个数等于秩已在构造中证明。

3. 转向最弱放大，先说明须区分零空间：核中的非零输入被送到零，有意义的问题是在核的正交补上单位输入至少被送出多远；满列秩时正交补是整个输入空间；可逆时逆矩阵把伸缩倍数倒过来。陈述并证明定理`thm:ls-svd-singular-value-norms`：在$\operatorname{span}\{\bm v_1,\ldots,\bm v_r\}$上由加权和得$\lVert\bm A\bm x\rVert_2\geq\sigma_r\lVert\bm x\rVert_2$并在$\bm v_r$取等；满列秩时推出$\min_{\lVert\bm x\rVert_2=1}\lVert\bm A\bm x\rVert_2=\sigma_d>0$；可逆方阵时验证$\bm A^{-1}=\sum\sigma_i^{-1}\bm v_i\bm u_i^\top$，并把它读作$\bm A^{-1}$的SVD，得$\lVert\bm A^{-1}\rVert_2=1/\sigma_d$（式`eq:ls-svd-inverse-norm`）。

4. 解释这些读数的用途与限制：满列秩只保证最小放大为正、不保证不太小；最小奇异值越小，逆矩阵对输出误差放大越厉害，最大与最小奇异值之比就是第~`sec:ls-matrix-condition-number`节的条件数；$r<d$时只能在零空间正交补上谈最弱放大；第~`sec:linear-algebra-homogeneous-estimation`节的齐次最小二乘在单位向量中最小化$\lVert\bm A\bm x\rVert_2$，最优解就是最弱放大方向$\bm v_d$。

5. 总结表示问题的回答：特征基（若存在）使矩阵对角化；要求标准正交时对称矩阵仍能对角化、一般方阵只能化为实Schur形；两端各取标准正交基时任意矩阵都能对角化。由此转入下一节的第一个具体问题：固定对称矩阵，在长度约束下比较二次型的大小。

### 11.6 长度约束下的二次型极值

1. 承接前五节已回答表示问题，提出用谱分解与SVD解决的三个具体问题中的第一个：固定实对称矩阵$\bm S$，输入方向改变时，二次型$\bm x^\top\bm S\bm x$最大、最小能取多少、在哪些方向取到。

2. 说明本节安排：二次型随长度平方增长，不限制长度时比较没有意义，所以先用欧氏长度约束排除缩放，引入只依赖方向的Rayleigh商并由谱分解求出极值；再保持二次型不变、只改变规定单位长度的方式，得到广义Rayleigh商；通过坐标变换把加权约束化为普通单位约束，导出广义特征方程与最优方向。指出下一节的最佳低秩逼近直接使用本节的极值结论。

#### 11.6.1 欧氏长度约束与Rayleigh商

1. 从$\bm S=\operatorname{diag}(4,1)$进入：单位方向$\bm e_1$、$\bm e_2$分别给出$4$与$1$，倾斜方向$(1,1)^\top/\sqrt2$给出$5/2$，说明只比较两个候选不能证明全局极值；又以$3\bm e_2$给出$9$说明不加长度约束时比较的只是输入的放大，长度约束的作用是让比较只关注方向。

2. 把长度除掉，给出Rayleigh商的定义`def:matrix-analysis-rayleigh-quotient`（式`eq:matrix-analysis-rayleigh-quotient`）；由分子分母同乘$c^2$说明它只依赖$\bm x$所在直线，因而求它在非零向量上的极值等价于在单位球面上求二次型的极值。

3. 用谱分解把比较化为特征值的比较：按11.3.1节的降序约定，单位向量$\bm x=\sum c_i\bm q_i$满足$\sum c_i^2=1$，由式`eq:matrix-analysis-quadratic-spectral-form`得$R_{\bm S}(\bm x)=\sum\lambda_ic_i^2$，它是以$c_i^2$为权的特征值加权平均，介于最小与最大特征值之间。

4. 陈述并证明Rayleigh--Ritz定理`thm:matrix-analysis-rayleigh-ritz`（式`eq:matrix-analysis-rayleigh-ritz`）：由$\lambda_1-R_{\bm S}(\bm x)=\sum(\lambda_1-\lambda_i)c_i^2\geq0$与对称的下界得两端不等式，取$\bm q_1$、$\bm q_d$说明界可达；再由“和式为零当且仅当每项为零”推出取到最大值当且仅当$\bm x$是$\ker(\bm S-\lambda_1\bm I)$中的非零向量，并借定理`thm:ls-spectral-projections`把满足$\lambda_i=\lambda_1$的$\bm q_i$的张成识别为特征空间；最小值同理。

5. 用图`fig:ls-sphere-constrained-extremum`以$\left[\begin{smallmatrix}2&0.5\\0.5&1\end{smallmatrix}\right]$说明二次型水平椭圆在特征方向处与单位圆相切、切点处取极值，并指出图中的子空间约束直线供11.10.1节的最小最大原理使用。

6. 示例`ex:ls-rayleigh-diagonal-two-by-two`回到$\operatorname{diag}(4,1)$，令$\bm x=(\cos\theta,\sin\theta)^\top$得$\bm x^\top\bm S\bm x=1+3\cos^2\theta\in[1,4]$，在$\pm\bm e_1$、$\pm\bm e_2$取到两端，完成全部单位方向的比较，并与定理核对：极值是特征值，极值方向是特征方向，倾斜方向严格介于两者之间。

7. 说明定理不要求半正定：以$\operatorname{diag}(1,-2)$说明二次型可取负值，单位方向上的值仍介于$-2$与$1$之间，两端在相应坐标方向取到。

8. 区分最优值与最优方向的唯一性：最大值$\lambda_1$总是唯一的数，最优方向由特征空间决定；$\lambda_1$单重时单位最优方向只有$\pm\bm q_1$，重复时空间中每个单位向量都最优（如$\bm S=\bm I$）；谱分解中的$\bm q_1$只是一个代表，最优方向集合由谱投影唯一确定。

9. 讨论特例$\bm S=\bm A^\top\bm A$：$R_{\bm A^\top\bm A}(\bm x)=\lVert\bm A\bm x\rVert_2^2/\lVert\bm x\rVert_2^2$是输出与输入长度比的平方，由11.5节特征值是奇异值平方，定理重新解释了单位输入的最大输出长度$\sigma_1$与最小输出长度$\sqrt{\lambda_d}$；联系第~`sec:linear-algebra-homogeneous-estimation`节的齐次最小二乘：有非零零空间时最小值为零，满列秩时$\bm A^\top\bm A\succ0$，由定理`thm:ls-symmetric-definiteness-eigenvalues`最小值为正；最后预告11.7节从重建误差引出另一个用Rayleigh商求解的问题。

#### 11.6.2 加权长度约束与广义Rayleigh商

1. 从各坐标单位或重要性不同时长度按加权内积（第~`sec:ls-weighted-inner-products`节）度量进入：保持$\bm S=\operatorname{diag}(4,1)$，改用$\bm B=\operatorname{diag}(9,1)$规定$\bm x^\top\bm B\bm x=1$，沿第一坐标可行向量为$\pm\bm e_1/3$、值为$4/9$，沿第二坐标值为$1$，说明改变长度标准会改变答案，且同样需要比较全部可行方向。

2. 仿照欧氏情形给出广义Rayleigh商的定义`def:ls-generalized-rayleigh-quotient`（式`eq:ls-generalized-rayleigh-quotient`），说明$\bm B$正定保证分母为正、商不随缩放改变；令$\bm u=\bm x/\sqrt{\bm x^\top\bm B\bm x}$说明求商的极值等价于在$\bm x^\top\bm B\bm x=1$上比较二次型。

3. 指出$\bm B=\bm I$时回到普通Rayleigh商，两者比较的是同一个二次型，区别只在用欧氏长度还是加权长度$\lVert\bm x\rVert_{\bm B}$规定单位输入。

#### 11.6.3 化归与广义特征方程

1. 指出加权约束不是欧氏单位球面、11.6.1节结论不能直接用，思路是换坐标使加权长度成为欧氏长度：由定理`thm:ls-gram-factor`写$\bm B=\bm L^\top\bm L$，令$\bm z=\bm L\bm x$，得$\bm x^\top\bm B\bm x=\bm z^\top\bm z$、$R_{\bm S,\bm B}(\bm x)=R_{\bm C}(\bm L\bm x)$，其中$\bm C=\bm L^{-\top}\bm S\bm L^{-1}$仍对称；强调化归只用Gram因子与换元，不需要矩阵平方根、多元微分或Lagrange乘子法。

2. 把最优方向换回原坐标：由$\bm C\bm z=\mu\bm z$与$\bm v=\bm L^{-1}\bm z$左乘$\bm L^\top$得$\bm S\bm v=\mu\bm B\bm v$，反向亦然，说明$\bm C$的特征对与该方程的解一一对应；据此给出广义特征值、广义特征向量与广义特征问题的定义`def:matrix-analysis-generalized-eigenvalue`（式`eq:matrix-analysis-generalized-eigenproblem`）。

3. 说明广义特征值不依赖$\bm L$的选取：由$\bm S-\mu\bm B=\bm L^\top(\bm C-\mu\bm I)\bm L$得$\det(\bm S-\mu\bm B)=(\det\bm L)^2\det(\bm C-\mu\bm I)$，所以广义特征值就是$\det(\bm S-\mu\bm B)=0$的根；$\bm C$对称，由谱定理它们全为实数、按重数共$d$个，记为降序$\mu_1\geq\cdots\geq\mu_d$。

4. 陈述并证明广义Rayleigh商的极值定理`thm:ls-generalized-rayleigh-extremal`：对$\bm C$用Rayleigh--Ritz得$\mu_d\leq R_{\bm S,\bm B}\leq\mu_1$，再由$R_{\bm C}(\bm z)=\mu_1$当且仅当$\bm C\bm z=\mu_1\bm z$与一一对应得取等条件$\bm S\bm x=\mu_1\bm B\bm x$；结论是约束$\bm x^\top\bm B\bm x=1$上的最大值为$\mu_1$，最优解是满足$\bm v^\top\bm B\bm v=1$的属于$\mu_1$的广义特征向量，最小值同理。

5. 对$\bm C$用完整谱分解得到全部广义特征向量的结构：陈述并证明定理`thm:ls-generalized-eigen-b-orthogonal`，令$\bm V=\bm L^{-1}\bm Z$，直接计算得$\bm V^\top\bm B\bm V=\bm I$与$\bm V^\top\bm S\bm V=\operatorname{diag}(\mu_i)$，即广义特征向量可取关于$\bm B$正交。

6. 用这组基说明广义Rayleigh商再次是特征值的加权平均，与普通情形平行；指出至此两端极值已求出，中间广义特征值可对$\bm C$使用11.10.1节的Courant--Fischer最小最大原理（定理`thm:matrix-analysis-courant-fischer`）再换回原坐标。

#### 11.6.4 最优方向的核验与计算

1. 示例`ex:ls-generalized-rayleigh-diagonal`对$\bm S=\operatorname{diag}(4,1)$、$\bm B=\operatorname{diag}(9,1)$按化归步骤计算：取$\bm L=\operatorname{diag}(3,1)$得$\bm C=\operatorname{diag}(4/9,1)$，由Rayleigh--Ritz读出两端并换回原坐标得最大方向$\pm\bm e_2$、最小方向$\pm\bm e_1/3$；再核验加权单位约束、广义特征方程与$\bm B$正交；最后由约束消元得$\bm x^\top\bm S\bm x=1-5x_1^2\in[4/9,1]$直接比较全部可行方向，与化归结果一致。

2. 说明一般情形的计算方式：通过因子分解与线性求解完成换元，不显式形成$\bm L^{-1}$；用第~`chap:linear-equations-and-optimization`章的Cholesky分解把$\bm L$取成三角矩阵，先后解两个三角方程组得到$\bm C$，求出$\bm z$后再解$\bm L\bm v=\bm z$，全程保持对称结构，只需对称特征值算法。

3. 比较看似直接的做法$\bm B^{-1}\bm S\bm v=\mu\bm v$：由$\bm B^{-1}\bm S=\bm L^{-1}\bm C\bm L$知它与$\bm C$相似、特征值相同，但一般不对称；以$\bm S=\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$、$\bm B=\operatorname{diag}(2,1)$得$\left[\begin{smallmatrix}1&1/2\\1&2\end{smallmatrix}\right]$为例，算出特征值$(3\pm\sqrt3)/2$与特征向量$(1,1\pm\sqrt3)^\top$，验证它们关于$\bm B$正交而欧氏内积为$-1$，不能套用谱定理的欧氏正交结论；上例中它恰为对角矩阵只是特殊情形。

4. 限定化归的条件：$\bm B$半正定而奇异时分母可为零，$\bm B$不定时可为负，都不存在可逆的$\bm L$；以$\bm S=\bm I$、$\bm B=\operatorname{diag}(1,0)$说明约束$x_1^2=1$不限制$x_2$、二次型$1+x_2^2$无上界，更一般的广义特征问题不在此展开。

5. 节末归纳：欧氏约束下两端极值是$\bm S$的最大、最小特征值，加权约束下是最大、最小广义特征值，最优方向分别是相应的特征向量与广义特征向量；指出下一节把重建误差化为保留量的极大化，首先用到这里的Rayleigh商结论。

### 11.7 最佳低秩逼近

1. 从数据矩阵常近似低秩进入：许多列大致落在少数方向张成的子空间中，希望只保留这些方向，用秩较低的矩阵代替原矩阵并使重建误差尽量小；据此提出本节问题：给定$\bm A$与允许保留的秩$k$，怎样选择低秩矩阵。

2. 说明问题同时要选方向与系数，并给出论证路线：先固定方向，证明最优系数由正交投影给出，问题只剩选子空间；秩一时保留量是Rayleigh商，可直接用11.6节的结论；秩$k$时保留量是迹，提出迹极值问题；随后由SVD写出候选截断SVD并计算误差；最后证明迹极值界，从而证明截断SVD在全部秩不超过$k$的矩阵中最优。说明主线用Frobenius平方误差，谱范数下的最优性另作证明。

#### 11.7.1 低秩逼近问题与投影误差

1. 把$\bm A$的列看成待重建的向量，写出$\lVert\bm A-\bm X\rVert_{\mathrm F}^2=\sum_j\lVert\bm a_j-\bm x_j\rVert_2^2$，并把$\operatorname{rank}\bm X\leq k$解释为全部重建向量共用至多$k$个独立方向；先回答边界情形：$k=0$时只能取$\bm0$，$k\geq r$时可取$\bm X=\bm A$且误差为零迫使$\bm X=\bm A$，此后集中研究$1\leq k<r$。

2. 示例`ex:ls-low-rank-three-columns`取$\bm A=\operatorname{diag}(3,2,1)$、$k=2$，比较三个坐标平面的保留量与损失（$13/1$、$10/4$、$5/9$），并明确留下两个疑问：倾斜平面能否更好，以及在平面内取投影是否就是最好的重建。

3. 先回答第二个疑问：用列标准正交的$\bm Y$表示固定子空间（不用$\bm V$以免与右奇异向量混淆），列都在其中的矩阵恰为$\bm X=\bm Y\bm C$，$\bm Y\bm Y^\top$是正交投影（第~`sec:ls-projection-matrices`节）。陈述并证明引理`lem:ls-low-rank-projection-error`（式`eq:ls-low-rank-projection-split`）：把$\bm A-\bm Y\bm C$逐列拆成投影残差$(\bm I-\bm Y\bm Y^\top)\bm a_j$与$\bm Y\bm z_j$，由$\bm Y^\top\bm Y=\bm I$验证二者正交并用勾股定理求和；再由同样的正交分解得残差等于$\lVert\bm A\rVert_{\mathrm F}^2-\operatorname{tr}(\bm Y^\top\bm A\bm A^\top\bm Y)$；结论是固定子空间时最优系数唯一为$\bm Y^\top\bm A$，最优重建是正交投影。

4. 用引理解释示例中“先投影再计损失”的做法正是最优重建：误差等于总平方长度减去保留量$\operatorname{tr}(\bm Y^\top\bm A\bm A^\top\bm Y)$。

5. 说明这一化归覆盖全部候选矩阵：对任一秩$s\leq k$的$\bm X$，取其列空间的标准正交基再补足到$k$列组成$\bm Y$，写$\bm X=\bm Y\bm C$，由引理得误差下界；反过来每个$\bm Y$都给出可行候选$\bm Y\bm Y^\top\bm A$。两方面合起来得到式`eq:ls-low-rank-subspace-reduction`，即最小误差等于总平方长度减去迹的最大值（只要最大值存在，其存在性与取值留到11.7.5节）；指出“选方向与系数”已化成“选方向”，下一小节先处理一条直线。

#### 11.7.2 秩一逼近与Rayleigh商

1. 取$k=1$、$\bm Y=\bm u$，由引理得平方误差为$\lVert\bm A\rVert_{\mathrm F}^2-\bm u^\top\bm A\bm A^\top\bm u=\lVert\bm A\rVert_{\mathrm F}^2-\sum_j(\bm u^\top\bm a_j)^2$，于是秩一逼近归结为在单位向量中最大化$\bm u^\top\bm G\bm u$（$\bm G=\bm A\bm A^\top$），正是11.6.1节已解决的Rayleigh商问题。

2. 由Rayleigh--Ritz定理`thm:matrix-analysis-rayleigh-ritz`与式`eq:ls-svd-transpose-relation`（$\bm A\bm A^\top$的特征值是$\sigma_i^2$与零、特征向量是左奇异向量）得最大保留量$\sigma_1^2$在$\bm u_1$取到，最小平方误差为$\sum_{i\geq2}\sigma_i^2$；再由$\bm A^\top\bm u_1=\sigma_1\bm v_1$得最优重建$\bm u_1\bm u_1^\top\bm A=\sigma_1\bm u_1\bm v_1^\top$，强调它是$\bm A$而非$\bm G$的秩一近似，即秩一和式的第一项；回到示例，最佳直线为$\bm e_1$方向，保留$9$、损失$5$。

3. 解释用$\bm A\bm A^\top$而不用$\bm A^\top\bm A$的原因：重建的是$\mathbb R^m$中的列向量，保留量对应左奇异方向；改为重建行向量时用$\bm A^\top\bm A$与$\bm v_1$，得到同一矩阵$\sigma_1\bm u_1\bm v_1^\top$。再指出这种解释依赖$\bm G$是Gram矩阵，一般不定的对称矩阵的Rayleigh商极值不能都解释为最佳秩一逼近；最后把方向数由一个增加到$k$个。

#### 11.7.3 秩$k$逼近与迹极值

1. 对$\bm Y^\top\bm Y=\bm I_k$按列展开保留量$\operatorname{tr}(\bm Y^\top\bm A\bm A^\top\bm Y)=\sum_l\sum_j(\bm y_l^\top\bm a_j)^2$，说明它把$k$个互相垂直方向上的保留量相加，$k=1$时回到Rayleigh商；由迹的循环性说明换$\bm Y\bm O$不改变迹，所以它只依赖子空间。

2. 由式`eq:ls-low-rank-subspace-reduction`把秩$k$逼近写成迹极值问题：在$\bm Y^\top\bm Y=\bm I_k$下最大化$\operatorname{tr}(\bm Y^\top\bm G\bm Y)$。指出逐列套用Rayleigh--Ritz只得粗界$k\lambda_1(\bm G)$，它一般取不到，因为没有用到各列正交、$k$个方向不能都是最大特征方向；于是先只比较由$\bm G$的特征向量组成的子空间，保留前$k$个特征方向给出最大的特征值和$\sum_{i\leq k}\lambda_i$，作为明确的候选；倾斜子空间是否超过它留到11.7.5节统一证明。

3. 回到示例，$\bm G=\operatorname{diag}(9,4,1)$的前两个特征方向张成$\operatorname{span}\{\bm e_1,\bm e_2\}$，正是坐标平面中最好的一个；一般地由式`eq:ls-svd-transpose-relation`，候选子空间是$\operatorname{span}\{\bm u_1,\ldots,\bm u_k\}$，下一小节把它写成具体矩阵。并预告对任意实对称$\bm S$，迹的最大、最小值分别是前$k$个与后$k$个特征值之和，完整陈述随最优性一并给出。

#### 11.7.4 截断SVD的构造与误差

1. 由秩一和式只保留前$k$项，定义截断SVD$\bm A_k$（式`eq:matrix-analysis-truncated-svd`）；用$\bm U_k^\top\bm u_i$在$i\leq k$时为$\bm e_i$、否则为零，验证$\bm U_k\bm U_k^\top\bm A=\bm A_k$，即$\bm A_k$是到候选子空间的正交投影重建；再由$\bm A_k\bm v_i=\sigma_i\bm u_i$得$\operatorname{rank}\bm A_k=k$，满足秩约束。

2. 计算这个候选的实际误差：余项$\sum_{i>k}\sigma_i\bm u_i\bm v_i^\top$仍是两组标准正交向量与降序正系数构成的和式，照11.5.2节的方法展开$\lVert(\bm A-\bm A_k)\bm x\rVert_2^2=\sum_{i>k}\sigma_i^2c_i^2$并在$\bm v_{k+1}$取等，再对$(\bm A-\bm A_k)^\top(\bm A-\bm A_k)=\sum_{i>k}\sigma_i^2\bm v_i\bm v_i^\top$取迹，得$\lVert\bm A-\bm A_k\rVert_2=\sigma_{k+1}$与Frobenius误差为舍弃奇异值平方和的平方根（式`eq:ls-truncated-errors`），后者也可由引理读出；区分Frobenius误差汇总所有舍弃方向、谱范数误差只记录最坏方向，并强调这只是构造的误差，其他候选是否更小尚待证明。

3. 示例`ex:ls-truncated-svd-diagonal`对$\operatorname{diag}(3,2,1)$写出$\bm A_1$、$\bm A_2$，算出平方误差$5,1$与谱范数误差$2,1$，并与示例`ex:ls-low-rank-three-columns`中最佳坐标直线、坐标平面的损失核对。

4. 用图`fig:ls-low-rank-truncation`以$\left[\begin{smallmatrix}2&0.5\\0.5&1\end{smallmatrix}\right]$说明截断的几何：单位圆的像椭圆被秩一近似压成主轴方向的线段，残留的谱范数误差恰为舍弃的$\sigma_2$。

5. 说明表示代价：保存因子只需$k(m+d+1)$个数，按$\bm U_k(\bm\Sigma_k(\bm V_k^\top\bm x))$的顺序乘向量需$O(k(m+d))$次运算，以$m=d=1000$、$k=10$为例存储由$10^6$降为$20010$；指出这不包括计算SVD本身的代价。

#### 11.7.5 截断SVD的最优性

1. 说明本小节先证明迹极值界，再由式`eq:ls-low-rank-subspace-reduction`把它变回重建误差的下界，截断SVD达到下界才完成证明。

###### paragraph：迹极值的证明

1. 回到11.7.3节留下的问题——在全部$k$维子空间中迹能否超过前$k$个特征值之和，给出证明想法：把迹写成特征值的加权和，看清正交约束对权重施加的限制。

2. 陈述并证明迹极值定理`thm:matrix-analysis-trace-minimum`（式`eq:matrix-analysis-trace-minimum`）：由谱分解得$\operatorname{tr}(\bm Y^\top\bm S\bm Y)=\sum\lambda_iw_i$，其中$w_i=\lVert\bm P\bm q_i\rVert_2^2$；由正交投影不增长度得$0\leq w_i\leq1$，由右乘正交矩阵不改变Frobenius范数得$\sum w_i=k$；以$\lambda_k$为分界写出恒等式，逐项判断符号得上界并由前$k$个特征向量取到；再在$\lambda_k>\lambda_{k+1}$时由取等迫使$i>k$的$w_i=0$，推出上界取等当且仅当子空间就是前$k$个特征方向的张成；下界对$-\bm S$应用上界得到。

3. 回到低秩逼近，取$\bm S=\bm A\bm A^\top$，前$k$个特征值之和为$\sum_{i\leq k}\sigma_i^2$，于是式`eq:ls-low-rank-subspace-reduction`的最大值存在并由$\operatorname{span}\{\bm u_1,\ldots,\bm u_k\}$取到；指出迹极值界对一般对称矩阵成立，但只有在半正定的Gram情形迹才表示投影保留的长度平方；并在示例中确认任意倾斜平面的保留量都不超过$13$。

###### paragraph：最佳低秩逼近定理

1. 说明Frobenius情形由化归和迹极值得到，谱范数不能这样处理：由$\lVert\bm M\rVert_2\leq\lVert\bm M\rVert_{\mathrm F}$，Frobenius误差的下界推不出谱范数误差的下界，需另证。

2. 陈述并证明Eckart--Young--Mirsky定理`thm:ls-best-low-rank`（式`eq:matrix-analysis-best-rank-k-spectral`、`eq:matrix-analysis-best-rank-k-frobenius`）：$\bm A_k$的误差恰为右端，只需证明下界；Frobenius情形把任意候选的列空间补成$k$维子空间，依次用引理`lem:ls-low-rank-projection-error`、迹极值定理与式`eq:matrix-analysis-frobenius-norm`；谱范数情形由秩零度定理`thm:ls-rank-nullity`得$\dim\ker\bm X\geq d-k$，与前$k+1$个右奇异向量张成的空间按维数公式必有公共单位向量，在其上$\lVert(\bm A-\bm X)\bm x\rVert_2=\lVert\bm A\bm x\rVert_2\geq\sigma_{k+1}$（式`eq:ls-spectral-lower-bound`）。

3. 注明结论最早由Eckart与Young给出，并强调定理覆盖任意秩不超过$k$的矩阵：Frobenius情形借化归把任意候选归入某个子空间，谱范数情形直接利用候选矩阵的核；两种范数下的最小误差都由舍弃的奇异值决定，前者看最大的舍弃值，后者看全部舍弃值的平方和。

###### paragraph：唯一性与适用范围

1. 区分最小误差唯一与最优矩阵唯一，陈述并证明定理`thm:ls-best-low-rank-uniqueness`：在$\sigma_k>\sigma_{k+1}$下，最优$\bm X$须使证明中两个不等号都取等，第一个由式`eq:ls-low-rank-projection-split`迫使$\bm X=\bm Y\bm Y^\top\bm A$，第二个由迹极值的取等条件迫使$\operatorname{range}\bm Y=\operatorname{span}\{\bm u_1,\ldots,\bm u_k\}$，于是$\bm X=\bm U_k\bm U_k^\top\bm A=\bm A_k$。

2. 用反例说明唯一性的边界：$\operatorname{diag}(2,1,1)$、$k=2$时截断跨过相等的奇异值，$\operatorname{diag}(2,1,0)$与$\operatorname{diag}(2,0,1)$都最优；谱范数下即使有间隙也不唯一，$\operatorname{diag}(3,2,1)$、$k=1$时$\operatorname{diag}(t,0,0)$对$1\leq t\leq5$都达到最小值$2$；边界情形$k=0$与$k\geq r$已在11.7.1节回答。

3. 说明最优性的两个前提：允许集合是全部秩不超过$k$的矩阵，误差是谱范数或Frobenius范数；要求非负或稀疏因子会缩小允许集合，逐元素加权的平方误差使引理失效，这些情形须重新论证。最后区分矩阵逼近的最优与用它求解方程的合适：第~`sec:ls-truncated-svd-ridge`节选择截断阶数时还要比较舍弃方向的拟合损失与$1/\sigma_k$的噪声放大。

### 11.8 伸缩分离与正交逼近

1. 以复数$z=e^{\mathrm i\theta}r$先乘正数改长度、再乘单位复数转方向为类比，提出本节问题：对实方阵求$\bm A=\bm W\bm H$，使$\bm H$沿一组互相垂直的方向作非负伸缩、$\bm W$保持长度。

2. 说明两个因子同时未知、不能分别求解，给出解题路线：先处理可逆的$\bm A$，用$\bm W^\top\bm W=\bm I$消去$\bm W$得到只含$\bm H$的方程$\bm H^2=\bm A^\top\bm A$；由$\bm A^\top\bm A$的谱分解开方构造$\bm H$，再由$\bm W=\bm A\bm H^{-1}$构造并验证$\bm W$；然后处理奇异情形，并证明所得$\bm W$是离$\bm A$最近的正交矩阵；最后把开方与求逆中共同使用的“沿谱改写特征值”归纳为对称矩阵的函数。

#### 11.8.1 消去正交因子，得到开方方程

1. 引入贯穿例$\bm A=\left[\begin{smallmatrix}0&-1\\3&0\end{smallmatrix}\right]$：它把$\bm e_1$送到$3\bm e_2$、$\bm e_2$送到$-\bm e_1$，同时改变长度与方向，希望拆成先由对称正定$\bm H$沿正交方向伸缩、再由正交$\bm W$保长转向。

2. 说明本小节与下一小节先假定$\bm A$可逆：此时伸缩可以撤销，所求$\bm H$应正定；正交矩阵允许是旋转或含反射；奇异情形留到11.8.4节。

3. 消去一个未知因子：把$\bm A=\bm W\bm H$两边转置后与原式相乘，由$\bm W^\top\bm W=\bm I$、$\bm H^\top=\bm H$得$\bm A^\top\bm A=\bm H^2$（式`eq:ls-polar-square-root-equation`），于是问题的前一半化为对已知矩阵$\bm S=\bm A^\top\bm A$开方；强调这只是分解存在时的必要条件，$\bm H$是否存在、能否再得到正交$\bm W$尚待证明。

4. 确认$\bm S$的结构：它对称，且由$\bm x^\top\bm S\bm x=\lVert\bm A\bm x\rVert_2^2>0$（用到$\bm A$可逆）为正定，可以使用11.3节的正交谱分解且特征值全为正。

5. 在贯穿例中算出$\bm S=\operatorname{diag}(9,1)$，沿两个坐标轴取正平方根得候选$\bm H=\operatorname{diag}(3,1)$，并指出一般的$\bm S$不是对角的，下一小节用谱分解化到这种情形。

#### 11.8.2 由谱分解构造伸缩因子

1. 对$\bm S=\bm Q\bm\Lambda\bm Q^\top$说明$\bm S$在$\bm q_i$上只作$\lambda_i$倍伸缩，自然尝试让$\bm H$沿同一方向伸缩$\sqrt{\lambda_i}$倍，写出候选$\bm H=\bm Q\operatorname{diag}(\sqrt{\lambda_i})\bm Q^\top$（式`eq:ls-spectral-square-root`）；强调这是主动选取的候选，并未预先假定未知的$\bm H$与$\bm S$共用特征基，是否满足要求要靠验证。

2. 用矩阵乘法验证$\bm H^2=\bm S$、$\bm H^\top=\bm H$，并由式`eq:ls-spectral-square-root`本身是正交谱分解且特征值为正得$\bm H$对称正定，记为正定平方根$\bm S^{1/2}$。

3. 提出剩余问题：构造只用到$\lambda_i\geq0$，对半正定$\bm S$同样可行；但$\bm Q$在重根时不唯一，$\bm X^2=\bm S$也可能有许多解（如$\pm\bm I$）。陈述并证明定理`thm:ls-psd-square-root`：存在性已由验证给出；唯一性对任一半正定解$\bm X=\sum\mu_j\bm p_j\bm p_j^\top$先得$\bm S\bm p_j=\mu_j^2\bm p_j$，再展开说明$\ker(\bm S-\lambda\bm I)$恰由满足$\mu_j^2=\lambda$的$\bm p_j$张成，非负性迫使$\mu_j=\sqrt\lambda$，于是$\bm X$与$\bm S^{1/2}$在$\bm S$的每个特征空间上都乘以$\sqrt\lambda$，由特征空间张成全空间得$\bm X=\bm S^{1/2}$。

4. 从唯一性论证读出两点：在重根空间内换基不改变特征空间及其上的作用，所以$\bm S^{1/2}$不依赖$\bm Q$；唯一性只针对半正定解，$-\bm S^{1/2}$仍是平方根。

5. 回到贯穿例取$\bm Q=\bm I$得$\bm H=\operatorname{diag}(3,1)$并核对，说明凭直觉写出的候选正是唯一的正定平方根；交代进度——已得伸缩因子，还需求$\bm W$；并指出“把特征值换成平方根”将在11.8.5节成为矩阵函数的例子，但这里的构造只用谱分解、标量开方与矩阵乘法。

6. 给出后文直接使用的长度恒等式$\lVert\bm S^{1/2}\bm x\rVert_2^2=\bm x^\top\bm S\bm x$（式`eq:ls-square-root-length`），说明它把加权长度化为欧氏长度；对$\bm S=\bm A^\top\bm A$得$\lVert\bm H\bm x\rVert_2=\lVert\bm A\bm x\rVert_2$，即$\bm H$承担全部长度变化而方向差别要由$\bm W$补上；指出第~`sec:ls-stationary-iterations`节分析Gauss--Seidel迭代时用它把能量范数写成欧氏长度。

7. 比较平方根与Gram因子：由定理`thm:ls-gram-factor`，$\bm S=\bm L^\top\bm L$同样给出$\lVert\bm L\bm x\rVert_2^2=\bm x^\top\bm S\bm x$，但这只说明两向量等长，$\bm L$一般不对称而$\bm S^{1/2}$唯一确定，下一小节将看到二者相差一个正交因子；Cholesky分解把$\bm L$取成三角矩阵，作用$\bm L^{-1}$只需解三角方程。

#### 11.8.3 由伸缩因子构造正交因子

1. 由$\bm H$正定可逆，在$\bm A=\bm W\bm H$两边右乘$\bm H^{-1}$得唯一候选$\bm W=\bm A\bm H^{-1}$，并解释右乘由因子顺序决定：$\bm H$先作用，撤销它须在右侧作用$\bm H^{-1}$。

2. 沿特征方向写出$\bm H^{-1}=\bm Q\operatorname{diag}(1/\sqrt{\lambda_i})\bm Q^\top$，验证它与$\bm H$相乘为$\bm I$，并记为对称正定的逆平方根$\bm S^{-1/2}$。

3. 检查候选满足原要求：由$\bm H^{-1}$对称与$\bm A^\top\bm A=\bm H^2$得$\bm W^\top\bm W=\bm I$，又$\bm W\bm H=\bm A$，至此存在性证完；据此给出极分解及正交因子、伸缩因子的定义`def:matrix-analysis-polar-decomposition`（式`eq:matrix-analysis-polar-decomposition`）。

4. 说明定义中$\bm H=(\bm A^\top\bm A)^{1/2}$不是额外要求：任何满足条件的分解都有$\bm H^2=\bm A^\top\bm A$，由定理`thm:ls-psd-square-root`只能是这个平方根。陈述并证明可逆矩阵的极分解定理`thm:ls-polar-invertible`：存在性汇总前面的构造与验证；唯一性先由式`eq:ls-polar-square-root-equation`与平方根唯一性得$\bm H'=\bm H$，再右乘$\bm H^{-1}$得$\bm W'=\bm W$。

5. 由$\det\bm A=\det\bm W\det\bm H$与$\det\bm H>0$说明$\bm W$的行列式与$\bm A$同号：$\det\bm A>0$时是旋转、$<0$时含一次反射，这正是开头不限制正交作用类型的原因；再用极分解解释Gram因子：$\bm L=(\bm L\bm S^{-1/2})\bm S^{1/2}$，$\bm L$与$\bm S^{1/2}$恰好相差正交因子，所以给出相同的长度。

6. 算完贯穿例：$\bm W=\bm A\operatorname{diag}(1/3,1)=\left[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right]$，逐项核对正交性与$\bm W\bm H=\bm A$，读出原变换是“先沿$\bm e_1$伸长$3$倍，再整体逆时针旋转$90$度”，并说明$\bm S$、$\bm H$、$\bm W$在解题中各自的角色。

#### 11.8.4 奇异情形与最佳正交逼近

###### paragraph：零伸缩方向上的正交补全

1. 说明$\bm A$奇异时$\bm S=\bm A^\top\bm A$仍半正定，沿谱开方仍得唯一的半正定$\bm H$，但零特征值不能取倒数，$\bm H^{-1}$不存在，上一小节由$\bm W=\bm A\bm H^{-1}$求正交因子的做法失效。

2. 改用11.5节已有的SVD：在$\bm U$与$\bm\Sigma$之间插入$\bm V^\top\bm V$得候选$\bm W=\bm U\bm V^\top$、$\bm H=\bm V\bm\Sigma\bm V^\top$（式`eq:ls-polar-from-svd`）。陈述并证明一般方阵的极分解定理`thm:ls-polar-general`：验证$\bm H$半正定且$\bm H^2=\bm A^\top\bm A$、$\bm W$正交且$\bm W\bm H=\bm A$；$\bm H$的唯一性同可逆情形；奇异时$\sigma_d=0$，把$\bm u_d$换成$-\bm u_d$得另一组SVD与另一正交因子$\bm W'$，$\bm W-\bm W'=2\bm u_d\bm v_d^\top\neq\bm0$，故正交因子唯一当且仅当$\bm A$可逆。

3. 从作用上解释不唯一：$i\leq r$时由$\bm W\bm v_i=\bm A\bm v_i/\sigma_i=\bm u_i$，正交因子在这些方向上由$\bm A$完全确定；$i>r$时$\bm H$把$\bm v_i$压成零、$\bm A$不提供信息，$\bm W$只需把它们标准正交地送入$\bm u_1,\ldots,\bm u_r$张成空间的正交补，这一正交补全有多种选择；并提醒始终没有定义不存在的$\bm H^{-1}$，也不能用逐元素取倒数代替。

4. 说明可逆时式`eq:ls-polar-from-svd`与定理`thm:ls-polar-invertible`给出同一对因子（极分解唯一）；谱开方路线解释因子为何如此，已有SVD时可直接读出两个因子。

###### paragraph：正交因子的最优性

1. 提出比较全部正交矩阵：极分解的正交因子是否是Frobenius范数下离$\bm A$最近的正交矩阵；由$\lVert\bm Z\rVert_{\mathrm F}^2=d$展开得$\lVert\bm A-\bm Z\rVert_{\mathrm F}^2=\lVert\bm A\rVert_{\mathrm F}^2+d-2\operatorname{tr}(\bm Z^\top\bm A)$，问题化为最大化$\operatorname{tr}(\bm Z^\top\bm A)$；指出这个目标关于$\bm Z$是线性的，与11.7.3节关于子空间基为二次的迹不同，迹极值界不能直接搬用，需重新给出上界。

2. 陈述并证明最佳正交逼近定理`thm:ls-best-orthogonal-approximation`：令$\bm C=\bm U^\top\bm Z\bm V$（仍正交），由迹的循环性得$\operatorname{tr}(\bm Z^\top\bm A)=\sum\sigma_iC_{i,i}$，由单位列向量得$|C_{i,i}|\leq1$，从而上界为$\sum\sigma_i$且$\bm Z=\bm U\bm V^\top$时取等；代入$\lVert\bm A\rVert_{\mathrm F}^2=\sum\sigma_i^2$得最小值$\sum(\sigma_i-1)^2$；可逆时取等迫使每列$\bm C_{:,i}=\bm e_i$，最优解唯一就是$\bm W$。

3. 说明应用与核对：去掉伸缩得到的正交因子把近似正交的矩阵修正为正交矩阵，常用于含噪的旋转估计；贯穿例奇异值为$3,1$，最小平方误差$4$，直接计算$\bm A-\bm W=\left[\begin{smallmatrix}0&0\\2&0\end{smallmatrix}\right]$得到同一结果。

4. 讨论奇异情形：一方面任一极分解的正交因子都使$\operatorname{tr}(\bm W'^\top\bm A)=\operatorname{tr}\bm H$达到上界；另一方面取等只要求前$r$个$C_{i,i}=1$，推出$\bm C=\operatorname{diag}(\bm I_r,\bm C')$，$(\bm U\bm C)\bm\Sigma\bm V^\top$仍是SVD，因而最优解恰好是全部极分解的正交因子，不同的$\bm C'$对应零伸缩方向上不同的正交补全。

5. 说明结论的边界：最优解在全部正交矩阵中取得，$\bm A$可逆时唯一最优解$\bm W$的行列式与$\det\bm A$同号（11.8.3节）；若额外要求$\det\bm Z=1$而$\det\bm A<0$，$\bm W$不可行，带约束的问题本节不展开；贯穿例$\det\bm A=3>0$，$\bm W$本身就是旋转。

#### 11.8.5 从具体构造到矩阵函数

###### paragraph：沿谱运算的共同方法

1. 回看前面两次构造：求$\bm H$时保持特征方向、把$\lambda_i$换成$\sqrt{\lambda_i}$，求$\bm H^{-1}$时换成$1/\sqrt{\lambda_i}$，二者都是“方向不动、只对特征值作用标量函数”，把这一实际用过的操作归纳为对称矩阵的函数。

2. 借11.3.3节的谱投影把$\bm S$写成$\sum_\lambda\lambda\bm P_\lambda$并列出投影关系，给出对称矩阵谱函数的定义`def:ls-symmetric-matrix-function`（式`eq:ls-symmetric-spectral-function`），同时写出用$\bm Q$与用谱投影的两种形式。

3. 说明两种写法相等（按列展开后合并同一特征值的项），由第二式只涉及特征值与唯一确定的谱投影得定义与基的选取无关；$f(z)=\sqrt z$、$1/\sqrt z$分别回到$\bm S^{1/2}$与$\bm S^{-1/2}$，强调前面的构造在此得到总结，而不是必须先建立矩阵函数才能求出$\bm H$与$\bm W$。

4. 提出推广后须与已有矩阵运算相容，陈述并证明引理`lem:ls-spectral-function-calculus`：先由谱投影的正交关系与幂等性证明$f(\bm S)g(\bm S)=(fg)(\bm S)$及加法规则；再由常数函数给出$\bm I$、恒等函数给出$\bm S$，归纳得多项式$p(\bm S)$与按矩阵运算计算的结果一致；最后由乘法规则得$f$在谱上不为零时$f(\bm S)^{-1}=(1/f)(\bm S)$，特别地$f(z)=1/z$给出$\bm S^{-1}$。

5. 补充多项式情形的直接看法：连乘$\bm Q\bm\Lambda\bm Q^\top$时相邻$\bm Q^\top\bm Q$相消得$\bm S^k=\bm Q\bm\Lambda^k\bm Q^\top$，定义只是把这一事实推广到一般$f$；并由引理第二条重新得到$(\bm S^{1/2})^2=\bm S$与$\bm S^{1/2}\bm S^{-1/2}=\bm I$。

6. 示例`ex:ls-matrix-square-root-two-by-two`对$\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]=3\bm q_1\bm q_1^\top+\bm q_2\bm q_2^\top$写出$\bm S^{1/2}$与$\bm S^{-1/2}$，逐元素核对$(\bm S^{1/2})^2=\bm S$；再与逐元素开方对照，后者的平方为$\left[\begin{smallmatrix}3&2\sqrt2\\2\sqrt2&3\end{smallmatrix}\right]\neq\bm S$，结论是矩阵函数沿特征方向作用而非逐元素作用。

7. 说明固定矩阵只有有限个特征值，定义只需要$f$在这些点上的值，不要求$f$连续，也不需要矩阵级数或微分。

8. 把沿谱构造的矩阵函数与第~`sec:multivariable-matrix-perturbation`节的一般矩阵输入映射（行列式、乘法、求逆等）区分开；再以$(\bm S+\bm E)^2-\bm S^2=\bm S\bm E+\bm E\bm S+\bm E^2$说明扰动一般不保持特征方向，一阶部分只有在可交换时才化为标量公式的$2\bm S\bm E$。

###### paragraph：实幂与对数的补充例子

1. 对正定$\bm S$定义实幂$\bm S^\alpha$，由引理得$\bm S^\alpha\bm S^\beta=\bm S^{\alpha+\beta}$与$(\bm S^{1/m})^m=\bm S$，并解释为把伸缩分成$m$次相同作用；由谱分解中特征值$\lambda_i^{1/m}>0$得$\bm S^{1/m}$对称正定，说明这里只用它是$\bm X^m=\bm S$的一个对称正定解，不讨论$m>2$时的唯一性；再说明半正定而奇异时正幂仍有定义、负幂没有，这正是平方根只要求半正定、逆平方根要求正定的原因。

2. 对正定$\bm S$取$f(z)=\log z$定义矩阵对数，解释$\log\lambda_i$的符号对应沿$\bm q_i$拉长或压缩；由该式本身是对称矩阵$\log\bm S$的谱分解且定义与基无关，用同一$\bm Q$对它沿谱作用$e^z$（矩阵指数在本节也按式`eq:ls-symmetric-spectral-function`定义）得$e^{\log\bm S}=\bm S$；反过来任意实对称$\bm T$的$e^{\bm T}$特征值全为正、是正定矩阵且$\log e^{\bm T}=\bm T$，所以沿谱定义下$\log$与$e^{(\cdot)}$在正定矩阵与实对称矩阵之间互为逆映射；$\bm S$有零特征值时$\log0$无定义，这一定义不能使用。

3. 区分矩阵$\log\bm S$与标量$\log\det\bm S$：由$\det\bm S=\prod\lambda_i$与迹的循环性得$\log\det\bm S=\operatorname{tr}(\log\bm S)$；指出对数在本节只是谱函数的又一例，不参与极分解的证明，第~`sec:multivariable-logdet-differential`节求$\log\det$的微分用的是行列式的微分与标量对数的链式法则，不以矩阵对数的微分为前提。

### 11.9 线性作用的误差放大与条件数

1. 从“数据不精确时结论有多可靠”转入误差问题：固定矩阵$\bm A$，理想输入$\bm x$、实际输入$\bm x+\bm h$，问输出相差多少，并把允许范围内的输入增量称为扰动。

2. 说明本节分三步：先确定误差的度量，比较绝对误差与相对误差；再固定输入、对扰动方向取最坏值，得到绝对与相对条件数；最后对输入方向也取最坏值，得到只依赖矩阵的条件数，并用奇异值说明它比较最强与最弱作用的差异。约定欧氏范数与谱范数，并限定本节只讨论输入数据误差的传播，矩阵与计算过程视为精确，算法误差由第~`chap:linear-equations-and-optimization`章讨论。

#### 11.9.1 输入扰动与误差尺度

1. 写出输出的精确变化$\Delta\bm y=\bm A\bm h$，说明它只用分配律、对任意大小的$\bm h$成立，不需要微分或小扰动；实际只知道误差预算$\lVert\bm h\rVert_2\leq\eta$，由此提出两个问题：输出误差有什么可靠上界，哪些扰动方向达到或接近它。

2. 约定误差的读法：定义输入与输出的绝对误差与相对误差，说明相对误差在同乘非零常数时不变、反映变化占原量的比例；指出参照量为零时相对误差无定义、接近零时应同时报告绝对误差，并强调范数与尺度的选择属于问题本身的规定。

3. 示例`ex:ls-diagonal-relative-error-basepoints`取$\operatorname{diag}(1,s)$：基点$\bm e_2$、扰动$\eta\bm e_1$时输出相对误差为$\eta/s$、放大$1/s$倍，原因是理想输出被压缩而扰动方向未被压缩；改取基点$\bm e_1$、扰动$\eta\bm e_2$时比值为$s$，误差反而缩小。

4. 由同一矩阵上比值从$1/s$变到$s$得出：谈论相对误差的放大必须说明基点和扰动方向，或对它们取最坏情形，下一小节按后一种方式定义条件数。

5. 指出相对误差的放大不只来自方向间压缩程度的差别：理想输出本身很小时也会放大。示例`ex:ls-cancellation-relative-error`用行矩阵$[1\;1]$把$1.0001$与$-1.0000$相加，由三角不等式得输出增量至多$10^{-4}$且可取到，输出相对误差可达$1$，而输入相对误差约$5\times10^{-5}$，放大约$2\times10^4$倍。

6. 说明上例只用了精确增量与三角不等式，即使加法精确执行也会如此放大，这是问题在相对尺度下的敏感性，而不是算法造成的舍入误差。

#### 11.9.2 固定输入处的条件数

1. 指出误差预算不限制方向，可靠的界须由最坏方向决定。先看绝对误差：比值$\lVert\bm A\bm h\rVert_2/\lVert\bm h\rVert_2$只依赖扰动方向、与大小和基点无关，其上确界是诱导范数$\lVert\bm A\rVert_2$，称为绝对条件数，由式`eq:matrix-analysis-spectral-norm`等于$\sigma_{\max}$。陈述并证明定理`thm:ls-absolute-error-bound`：按右奇异向量展开得不等式，取$\bm h=\eta\bm v_1$取等，从而任何更小的常数都不成立。

2. 固定基点、两端改用相对尺度，给出相对条件数的定义`def:ls-relative-condition-number`；陈述并证明定理`thm:ls-relative-condition-number`（式`eq:matrix-analysis-condition-number-bound`）：把比值拆成与$\bm h$无关的因子$\lVert\bm x\rVert_2/\lVert\bm A\bm x\rVert_2$与绝对误差比，由上一定理得$\kappa_{\mathrm{rel}}=\lVert\bm A\rVert_2\lVert\bm x\rVert_2/\lVert\bm A\bm x\rVert_2$，等号在扰动沿$\bm v_1$时成立。

3. 回到示例`ex:ls-diagonal-relative-error-basepoints`解释定义：在$\bm e_2$处$\kappa_{\mathrm{rel}}=1/s$且示例中的扰动恰好达到，在$\bm e_1$处为$1$；并指出沿具体方向观察到的比值可以更小（基点$\bm e_2$、扰动$\eta\bm e_2$时比值为$1$）。

4. 说明两个上确界取遍全部非零有限扰动而非先令扰动趋零，这之所以可行，是因为线性作用的误差比只依赖方向，所以误差界对任意大小的扰动成立；一般非线性映射的误差比随扰动半径变化，须先在半径$\delta$内取最坏再令$\delta$缩小，用第~`sec:multivariable-limits-continuity`节的极限定义局部条件数并联系微分，这些在第~`sec:multivariable-local-condition-number`节建立，本节不以一般定义代替直接推导。

#### 11.9.3 矩阵条件数与方向差异

1. 指出相对条件数随基点变化，基点落在被压缩方向时较大；不知道输入落在哪里时须对基点也取最坏值，对可逆方阵它只依赖矩阵。给出可逆矩阵条件数的定义`def:matrix-analysis-condition-number`（式`eq:matrix-analysis-condition-number`）。

2. 陈述并证明定理`thm:matrix-analysis-condition-number-bound`（式`eq:matrix-analysis-spectral-condition-number`）：由$\lVert\bm A\bm x\rVert_2\geq\sigma_n\lVert\bm x\rVert_2$得$\kappa_{\mathrm{rel}}\leq\sigma_1/\sigma_n$并在$\bm v_n$取等，结合$\lVert\bm A^{-1}\rVert_2=1/\sigma_n$得上确界为$\kappa_2(\bm A)$；第二条把相对条件数放大为$\kappa_2$并在$\bm x=\bm v_n$、$\bm h=c\bm v_1$时取等；第三条由$\Delta\bm x=\bm A^{-1}\Delta\bm b$把第二条用于$\bm A^{-1}$，并由$\kappa_2(\bm A^{-1})=\kappa_2(\bm A)$得线性方程解的相对误差界，对任意大小的$\Delta\bm b$成立。

3. 用等号条件解释条件数比较的对象：基点在最弱方向$\bm v_n$使理想输出最短，扰动在最强方向$\bm v_1$使增量最长，二者之比就是最强与最弱作用的差异；再说明欧氏范数并非必需，令$\bm y=\bm A\bm x$可得任一诱导范数下的最坏值为$\lVert\bm A\rVert\lVert\bm A^{-1}\rVert$，定理第二、三条仍成立，只是没有奇异值表达式。

4. 由$1=\lVert\bm A\bm A^{-1}\rVert\leq\kappa(\bm A)$说明条件数不小于$1$；几何上$\kappa_2$是像椭球最长与最短半轴之比，正交矩阵取$1$、椭球越扁$\kappa_2$越大，并定义良态与病态；图`fig:ls-condition-number-amplification`对比良态$\kappa_2=1.5$与病态$\kappa_2\approx12.3$两个矩阵下单位圆的像与误差圆盘反求后的放大。

5. 强调条件数看方向间的差异而非元素或奇异值的大小：$\operatorname{diag}(1,s)$的$\kappa_2=1/s$，$s\bm I$虽整体缩小却对所有方向一视同仁、$\kappa_2=1$且每处相对条件数为$1$；一般地，奇异值按同一比例缩放不改变条件数。

6. 指出条件数也不描述反复作用：示例`ex:ls-condition-number-vs-powers`中$2\bm I$与$\tfrac12\bm I$条件数都为$1$，幂却一增一减；长期行为须由谱半径判断（第~`sec:ls-matrix-power-behavior`节），二者不能互相代替。

7. 限定本节结论：始终固定$\bm A$、只让输入带误差，条件数刻画问题的敏感性而不评价算法；方程解在矩阵与右端同时带误差时的完整误差界及数据误差与算法误差的区分见第~`sec:ls-numerical-sensitivity`节，求逆和解映射的一阶响应见第~`sec:multivariable-inverse-differential`节；下一节改变矩阵本身，说明特征值、奇异值与特征子空间各有敏感性度量，不能只凭$\kappa_2(\bm A)$判断。

### 11.10 谱与奇异值的扰动

1. 从矩阵本身也来自数据（样本协方差、测量与舍入）进入：手中矩阵与真实矩阵相差$\bm E$，只知$\lVert\bm E\rVert_2\leq\varepsilon$，问由手中矩阵算出的特征值、奇异值、秩和特征子空间哪些对真实矩阵仍可靠。

2. 说明谱值大小、是否接近秩亏、子空间方向是三种不同输出，各需相应的界与条件，并给出顺序：对称矩阵每个特征值的误差区间与正负性判断；奇异值区间与秩、可逆性和最佳低秩误差的检查；特征子空间的偏转由谱隙控制；一般方阵为何需要额外条件。强调这些都是对任意大小$\bm E$成立的有限变化界，不需要微分，特征值分支的一阶响应留给第~`sec:multivariable-eigen-differential`节。

#### 11.10.1 对称矩阵特征值的扰动

1. 设定对称的$\bm S$与$\bm E$，把扰动前后的特征值按降序逐个配对比较；用图`fig:ls-perturbation-ellipse`说明正定矩阵受扰动后二次型椭圆半轴微变、主轴微转，图中数值符合Weyl界；指出11.6.1节的Rayleigh商只刻画两端特征值，比较中间特征值须先建立其极值表征。

###### paragraph：有序特征值的极值表征

1. 提出先把方向限制在子空间内、再让子空间变动的思路，陈述并证明引理`lem:ls-restricted-rayleigh`：由$\bm U^\top\bm U=\bm I$得$R_{\bm S}(\bm U\bm y)=R_{\bm U^\top\bm S\bm U}(\bm y)$，$\bm y\mapsto\bm U\bm y$一一对应，于是受限极值取到且等于压缩矩阵$\bm U^\top\bm S\bm U$的两端特征值。

2. 解释引理的作用：$\bm U^\top\bm S\bm U$是$\bm S$在子空间上的压缩，引理把“选哪个子空间”与“在子空间内比较方向”分开，后者已由普通Rayleigh商解决；受限极值与基矩阵$\bm U$的选取无关。

3. 陈述并证明Courant--Fischer定理`thm:matrix-analysis-courant-fischer`：取$\mathcal V_k=\operatorname{span}\{\bm q_1,\ldots,\bm q_k\}$，其上Rayleigh商是前$k$个特征值的加权平均，最小值为$\lambda_k$；对任一$k$维$\mathcal V$，由维数公式它与$\operatorname{span}\{\bm q_k,\ldots,\bm q_d\}$有非零公共向量，其Rayleigh商不大于$\lambda_k$，两方面合起来得max--min式；交换两组特征向量的角色得min--max式。

4. 称其为最小最大原理，说明它只涉及子空间与Rayleigh商、不要求先知道特征向量，所以比较两个对称矩阵的同序特征值只需比较Rayleigh商；并与11.7.5节的迹极值区分：后者汇总$k$个正交方向、刻画前$k$个特征值之和，逐个比较特征值需要前者。

###### paragraph：谱值区间与正定性保证

1. 先估计扰动对同一方向Rayleigh商的影响：由Cauchy--Schwarz不等式得$|\bm x^\top\bm E\bm x|\leq\lVert\bm E\rVert_2\lVert\bm x\rVert_2^2$，最小最大原理把这一估计逐层传到每个有序特征值。

2. 陈述并证明Weyl特征值扰动界`thm:ls-weyl-eigenvalue`（式`eq:matrix-analysis-weyl-eigenvalue-perturbation`）：由$R_{\bm S}-c\leq R_{\bm S+\bm E}\leq R_{\bm S}+c$，在每个$k$维子空间上取受限最小点（引理保证取到）比较两边的最小值，再对子空间取最大，由Courant--Fischer得结论。

3. 读出误差区间$[\lambda_k(\bm S)-\varepsilon,\lambda_k(\bm S)+\varepsilon]$，说明它不要求特征值分开、单重与重复都适用；但它是绝对误差界，特征值接近零时不能据此宣称相对误差小。

4. 由区间判断特征值符号：区间不含零时符号确定，含零时预算不足以判断，以$\operatorname{diag}(1,\varepsilon/2)$在两种满足预算的扰动下第二特征值变号为例；陈述并证明定理`thm:ls-eigenvalue-sign-definiteness`：第一条直接由Weyl界得到；第二条对$t\bm E$应用Weyl界得与$t$无关的下界$\lambda_{\min}(\bm S)-\varepsilon>0$，再由二次型展开得整条线段$\bm S+t\bm E$正定。

5. 说明这一与$t$无关的下界的用途：对正定矩阵求逆、开方或取对数时，常须确认整条线段留在定义域内并与边界保持一致距离，例如第~`sec:multivariable-logdet-differential`节估计对数行列式的变化。

6. 示例`ex:ls-weyl-double-root`取$\bm S(t)=\operatorname{diag}(t,-t)$：$t=0$处是二重根，最大特征值$|t|$的变化恰等于$\lVert\bm S(t)-\bm S(0)\rVert_2$，Weyl界取等，说明重根不妨碍有限绝对误差界；另一方面$|t|$在零点左右导数为$-1$与$1$，排序后的最大特征值没有双侧导数，有限变化界与可微性是两回事。

7. 指出第~`sec:multivariable-local-condition-number`节再用该例区分有限敏感性与可微性，第~`sec:multivariable-eigen-differential`节在特征值简单的条件下研究所选分支的一阶响应。

#### 11.10.2 奇异值的扰动与秩判断

1. 说明秩、可逆性与最佳低秩误差都由奇异值决定，本小节先把特征值区间移到奇异值上，再判断哪些关于秩的结论在误差预算下可靠。

###### paragraph：奇异值的误差区间

1. 指出长方矩阵没有特征值、不能直接用Weyl界，办法是把它放进对称增广矩阵$\bm H(\bm A)=\left[\begin{smallmatrix}\bm0&\bm A\\\bm A^\top&\bm0\end{smallmatrix}\right]$。陈述并证明引理`lem:ls-symmetric-augmentation-spectrum`：由完整SVD构造$\bm w_i^\pm=(\bm u_i;\pm\bm v_i)/\sqrt2$得特征值$\pm\sigma_i$，多出的$\bm u_j$或$\bm v_j$给出$|m-n|$个零，验证这$m+n$个向量构成标准正交特征基，故降序前$p$个特征值就是奇异值；再由分块计算与$\lVert\bm A^\top\rVert_2=\lVert\bm A\rVert_2$得$\lVert\bm H(\bm A)\rVert_2=\lVert\bm A\rVert_2$。

2. 陈述并证明奇异值的Weyl界`thm:ls-weyl-singular-value`（式`eq:matrix-analysis-singular-value-perturbation`）：增广是线性的，对$\bm H(\bm A)$与扰动$\bm H(\bm E)$应用Weyl界，再由引理换回奇异值与$\lVert\bm E\rVert_2$；并写出真实奇异值所在的非负区间。

3. 由定理`thm:matrix-analysis-best-low-rank`的最小谱范数距离$\sigma_{k+1}$得：扰动前后最佳低秩逼近的最优误差之差不超过$\varepsilon$；提醒这只说明最优误差的数值稳定，取得它的低秩矩阵与奇异方向是否稳定留到下一小节。

###### paragraph：秩保证与可逆性的边界

1. 陈述并证明定理`thm:ls-singular-value-rank-guarantee`：$\sigma_k(\bm A)>\varepsilon$时由Weyl界得$\sigma_k(\bm A+\bm E)>0$，再由正奇异值个数等于秩得$\operatorname{rank}(\bm A+\bm E)\geq k$，特别地可保证满列秩。

2. 说明反方向不成立：$\sigma_k(\bm A)\leq\varepsilon$只表示区间含零，既不能排除也不能断言真实矩阵秩亏；本小节只给出预算可以保证的结论，按阈值确定数值秩留到第~`sec:ls-pseudoinverse-rank-change`节结合求解讨论。

3. 对可逆方阵提出使其奇异的最小扰动问题，陈述并证明定理`thm:ls-distance-to-singularity`：一种证法直接由最佳低秩逼近定理取秩$n-1$；另给直接验证——$\lVert\bm E\rVert_2<\sigma_n$时由$\lVert\bm A\bm x\rVert_2\geq\sigma_n\lVert\bm x\rVert_2$与三角不等式得零空间平凡，而$\bm E_*=-\sigma_n\bm u_n\bm v_n^\top$范数为$\sigma_n$且使$\bm v_n$被送到零；相对距离为$1/\kappa_2(\bm A)$。

4. 由此给出条件数的另一种解释：$\kappa_2$越大，按相对尺度$\bm A$离奇异矩阵越近；限定条件是允许任意谱范数扰动，若扰动须保持对称或稀疏等结构，可选扰动变少，定理只给出距离的下界，相应距离须另行分析；并以$\bm E=\bm A$说明超过$\sigma_n$的扰动不一定使矩阵奇异。

5. 示例`ex:ls-diagonal-distance-to-singularity`取$\operatorname{diag}(1,s)$：预算$\varepsilon<s$时可保证可逆，$-s\bm e_2\bm e_2^\top$恰把它变成$\operatorname{diag}(1,0)$，相对距离$s=1/\kappa_2$。

6. 指出在该例中$s$小时矩阵离奇异很近，但第一奇异方向$\bm e_1$并不因此不稳定；预告下一小节将说明方向的稳定性由截断处的间隙$1-s$决定，可逆性的边界由最小奇异值$s$决定，二者不能互相替代。

#### 11.10.3 特征子空间的扰动

1. 指出特征值的绝对误差很小时，按特征值选出的方向仍可能变化很大，提出本小节问题：给定预算下原特征子空间能偏转多少；说明先建立与基选择无关的子空间距离，再检查目标特征值组与其余特征值之间的间隔。

###### paragraph：子空间的距离

1. 说明比较对象应是子空间本身：特征向量可变号、重根时空间内可任意换基，单个基向量的变化不能当作子空间误差；从两条直线的夹角与投影残差长度$\sin\theta$进入（图`fig:ls-principal-angles-subspaces`），并由一维情形$|\bm q^\top\widetilde{\bm q}|=\cos\theta$过渡到高维。

2. 用交叉矩阵$\bm Q^\top\widetilde{\bm Q}$的奇异值定义主夹角`def:matrix-analysis-principal-angles`；由$\lVert\bm Q^\top\widetilde{\bm Q}\rVert_2\leq1$说明它们有定义，由换基相当于两侧乘正交矩阵、奇异值不变说明主夹角只依赖子空间，并记最大主夹角$\theta_{\max}$。

3. 引入$\bm C=\widetilde{\bm Q}^\top\bm Q$、到正交补的交叉矩阵$\bm X=\widetilde{\bm Q}_\perp^\top\bm Q$与两个投影$\bm P$、$\widetilde{\bm P}$。陈述并证明定理`thm:ls-principal-angle-projection`：由勾股定理得$\bm X^\top\bm X$与$\bm I-\bm C^\top\bm C$的二次型处处相等，借极化读出二者相等，从而$\bm X^\top\bm X$的特征值是$\sin^2\theta_i$；再由投影的对称幂等与迹的循环性算出$\tfrac12\lVert\bm P-\widetilde{\bm P}\rVert_{\mathrm F}^2=\sum\sin^2\theta_i$。

4. 说明Frobenius范数汇总全部主夹角、反映整体偏转，只关心最坏方向时用谱范数。陈述并证明定理`thm:ls-projection-spectral-distance`（$\lVert\bm P-\widetilde{\bm P}\rVert_2=\lVert\bm X\rVert_2=\sin\theta_{\max}$）：由上一定理得$\lVert\bm X\rVert_2=\sin\theta_{\max}$；借正交补基$\bm Q_\perp$说明$\lVert(\bm I-\widetilde{\bm P})\bm P\rVert_2=\lVert\bm X\rVert_2$，交换两子空间的角色得$\lVert(\bm I-\bm P)\widetilde{\bm P}\rVert_2$也等于$\sin\theta_{\max}$；上界由$\bm P-\widetilde{\bm P}=\bm P(\bm I-\widetilde{\bm P})-(\bm I-\bm P)\widetilde{\bm P}$两项分别落在$\bm Q$的列空间与其正交补中，用两次勾股定理得到；下界取$\bm X$的第一右奇异向量$\bm a$，令$\bm z=\bm Q\bm a$，得$(\bm P-\widetilde{\bm P})\bm z=\widetilde{\bm Q}_\perp\bm X\bm a$的长度恰为$\sin\theta_{\max}$。

###### paragraph：谱隙控制的偏转界

1. 设定比较前$k$个特征值的子空间，引入原谱隙$\delta=\lambda_k(\bm S)-\lambda_{k+1}(\bm S)>0$，说明它使原特征子空间唯一；在$\varepsilon<\delta/2$下由Weyl界证明扰动后截断处仍严格分开，两子空间都唯一且可用主夹角比较；再定义论证实际使用的交叉谱间隔$\gamma=\lambda_k(\bm S)-\lambda_{k+1}(\widetilde{\bm S})$，并由Weyl界得$\gamma\geq\delta-\varepsilon>0$。

2. 引入$\bm Q,\bm\Lambda_1,\widetilde{\bm Q},\widetilde{\bm Q}_\perp,\widetilde{\bm\Lambda}_2$与$\bm X=\widetilde{\bm Q}_\perp^\top\bm Q$，陈述并证明特征子空间偏转的Frobenius界`thm:ls-gap-subspace-frobenius`：由两组特征关系相减得$\widetilde{\bm\Lambda}_2\bm X-\bm X\bm\Lambda_1=\widetilde{\bm Q}_\perp^\top\bm E\bm Q$，系数为对角矩阵，逐元素读出$(\lambda_j(\widetilde{\bm S})-\lambda_i(\bm S))X_{j,i}$，由降序得分母不小于$\gamma$，平方求和得第一个不等式，再由$\widetilde{\bm Q}_\perp^\top$行标准正交得第二个；等式部分来自主夹角定理。

3. 指出证明中的方程是Sylvester方程（第~`sec:ls-matrix-equations`节专门研究），此处系数对角、逐元素相除即可；并由$\lVert\bm E\bm Q\rVert_{\mathrm F}\leq\sqrt k\lVert\bm E\rVert_2$得右端不超过$\sqrt k\lVert\bm E\rVert_2/\gamma$。

4. 说明对最大主夹角也有同型结论，但它不是Frobenius界的直接推论（后者带因子$\sqrt k$），去掉因子须改用$\bm X$的最大奇异方向从两侧检验同一方程。陈述并证明Davis--Kahan谱隙界`thm:ls-davis-kahan`（式`eq:matrix-analysis-eigenvector-gap-bound`）：由上一定理记$s=\lVert\bm X\rVert_2=\sin\theta_{\max}$，取$\bm X$的第一右、左奇异向量$\bm a,\bm b$，用$\bm b^\top$左乘、$\bm a$右乘Frobenius界证明中的方程，左端化为$s(\bm b^\top\widetilde{\bm\Lambda}_2\bm b-\bm a^\top\bm\Lambda_1\bm a)$，由$\bm a^\top\bm\Lambda_1\bm a\geq\lambda_k(\bm S)$与$\bm b^\top\widetilde{\bm\Lambda}_2\bm b\leq\lambda_{k+1}(\widetilde{\bm S})$得其绝对值至少$s\gamma$，右端不超过$\lVert\bm E\bm Q\rVert_2\leq\lVert\bm E\rVert_2$。

5. 指出这个证明只用到单侧的谱分离——原目标组特征值都不小于$\lambda_k(\bm S)$、扰动后其余特征值都不大于$\lambda_{k+1}(\widetilde{\bm S})$，正是本节的情形；目标组位于谱的中间、两侧都有其余特征值时须另作处理，本节不使用。

6. 把交叉间隔换成事先可检查的量：由$\gamma\geq\delta-\varepsilon$与$\delta-\varepsilon>\delta/2$得$\lVert\widetilde{\bm P}-\bm P\rVert_2\leq\varepsilon/(\delta-\varepsilon)\leq2\varepsilon/\delta$；说明谱隙在分母上，谱隙越小同样扰动的转角越大；已知$\gamma$时也可直接用带$\gamma$的形式。

7. 示例`ex:ls-gap-direction-rotation`取$\operatorname{diag}(1+\delta,1)$与交叉扰动$t\left[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right]$，把扰动后矩阵写成单位阵倍数加迹零部分$\bm M$，借两角差公式精确求出最大特征方向转角满足$\tan2\theta=2t/\delta$；对比$\kappa_2(\bm S)=1+\delta$接近$1$而$t=\delta/2$时转角已达$22.5^\circ$，说明子空间敏感性不能由条件数判断，同时核对最大特征值增量不超过$t$。

8. 把精确转角与界比较：算出$\gamma=\delta/2+r$，验证$\sin\theta=\sqrt{(r-\delta/2)/(2r)}\leq t/(\delta/2+r)$，$t\ll\delta$时两端都约为$t/\delta$，界在量级上准确；指出$t=\delta/2$已超出小扰动形式的条件，只保留精确算例的结论；图`fig:matrix-analysis-gap-direction`固定$t=0.02$画出特征值增量与转角随谱隙的变化。

###### paragraph：重根、奇异子空间与低秩近似

1. 说明谱隙只需存在于目标组与组外之间：$\operatorname{diag}(2,2,0)$、$k=2$时谱隙为$2$，$\varepsilon<1$时前二维子空间稳定（$\sin\theta_{\max}<\varepsilon$）；但平面内单个特征向量不稳定，任意小的$\eta\bm e_1\bm e_1^\top$与$\eta\bm e_2\bm e_2^\top$使最大特征方向分别成为互相正交的$\bm e_1$、$\bm e_2$；结论是子空间内部基的变化不代表子空间的变化，子空间稳定也不保证每个基向量稳定。

2. 借对称增广把奇异子空间化为特征子空间：要求奇异值间隙$\delta_\sigma=\sigma_k-\sigma_{k+1}>0$（同时保证$\sigma_k>0$，否则$\bm w_k^\pm$对应同一特征值$0$而无法分离），写出$\bm H(\bm A)$前$k$个特征子空间的投影$\bm P_{\bm H}$的分块形式；在$\varepsilon<\delta_\sigma/2$下对增广矩阵用上面的推论，再由左上块的谱范数不超过整体得$\lVert\bm U_k\bm U_k^\top-\widetilde{\bm U}_k\widetilde{\bm U}_k^\top\rVert_2\leq4\varepsilon/\delta_\sigma$，右下块给出右奇异子空间的同样结论。

3. 与上一小节对照：最佳秩$k$逼近的误差$\sigma_{k+1}$总只移动不超过$\varepsilon$，而所用主方向只在截断处有足够间隙时才稳定，$\sigma_k=\sigma_{k+1}$时最优矩阵可能在不同子空间间跳变；指出第~`sec:ls-truncated-svd-ridge`节选截断位置时要同时看舍弃的奇异值能否忽略与保留方向是否分得开。

#### 11.10.4 一般方阵的谱敏感性

1. 说明前面按序比较依赖对称结构（实特征值、可排序、Rayleigh商刻画），一般方阵的特征值可能是复数、没有自然次序与极值表征，于是对可对角化方阵改问扰动后的特征值离原谱有多远，并约定复欧氏范数。陈述并证明Bauer--Fike定理`thm:ls-bauer-fike`：设$\mu$不是原特征值，由$(\bm A-\mu\bm I)\bm w=-\bm E\bm w$与$\bm y=\bm V^{-1}\bm w$得$\bm y=-(\bm\Lambda-\mu\bm I)^{-1}\bm V^{-1}\bm E\bm V\bm y$，取范数并用对角矩阵的范数等于最大模，得$\min_i|\mu-\lambda_i|\leq\kappa_2(\bm V)\lVert\bm E\rVert_2$。

2. 区分界中的$\kappa_2(\bm V)$与上一节的$\kappa_2(\bm A)$：$\operatorname{diag}(1,s)$可取$\bm V=\bm I$，特征值移动不超过$\lVert\bm E\rVert_2$而$\kappa_2(\bm A)=1/s$可很大；反过来对$\left[\begin{smallmatrix}1&1\\0&1+\eta\end{smallmatrix}\right]$先验证特征向量$(1,0)^\top$与$(1,\eta)^\top$，再由$\eta\to0$时它趋于$\bm A_0=\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$、$\kappa_2(\bm A_0)=(3+\sqrt5)/2$及奇异值的Weyl界说明求逆不敏感；但特征向量趋于平行，由$\bm V$的奇异值之积为$|\det\bm V|=\eta$、最大奇异值不小于$1$得$\kappa_2(\bm V)\geq1/\eta$，界变得很宽；结论是非正交特征基放大扰动在特征坐标中的表示，对称时可取正交$\bm V$、界与Weyl界同量级。

3. 列出使用这个界的三点注意：特征向量缩放改变$\kappa_2(\bm V)$，引用时须说明所用的基；它只保证每个扰动后特征值接近某个原特征值，不建立固定配对；它要求可对角化，特征向量不足时变化可与扰动不成比例。

4. 反例`ex:ls-jordan-eigenvalue-sensitivity`取不可对角化的$\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]$，左下角加$t$后特征多项式为$z^2-t$，特征值移动$\sqrt t$，$t=10^{-10}$时为扰动的$10^5$倍，$\sqrt t/t\to\infty$说明不存在比例常数；$t<0$时实特征值消失。

5. 由该例说明缺少可对角化条件时特征值变化的量级可与扰动不同，本节不为此引入新的标准形；相应光滑分支的一阶响应在第~`sec:multivariable-eigen-differential`节研究，本节的有限变化界须连同对象结构（对称、可对角化）与谱的分离条件一起使用。

6. 节末综合：对称矩阵的特征值与任意矩阵的奇异值移动不超过$\lVert\bm E\rVert_2$、不要求谱值分开，可据此判断符号、正定性与秩的下界；子空间方向用主夹角比较，偏转由扰动与谱隙之比控制；一般方阵的特征值还取决于特征基的条件，甚至不与扰动成比例。并指出条件数与谱扰动都只涉及一次作用或一次分解，下一节转向同一矩阵的反复作用。

### 11.11 反复更新的极限与误差

1. 承接前两节研究的一次作用，提出反复执行同一更新$\bm x_{k+1}=\bm T\bm x_k+\bm c$的问题：无论从哪里出发，状态能否趋于同一平衡；若能，平衡在哪里、接近多快，每轮带小误差时误差会累积到多大。

2. 说明论证路线：先展开递推，把状态拆成由矩阵幂$\bm T^k$描述的初值剩余影响与由矩阵级数$\sum\bm T^j$描述的输入累积，再依次研究矩阵幂何时趋于零、级数收敛到什么、收敛速度以及逐步误差的累积；限定本节只分析给定的$\bm T$与$\bm c$，怎样从线性方程构造更新规则留给第~`sec:ls-stationary-iterations`节。

3. 说明收敛的含义：按第~`sec:ls-finite-dimensional-sequences`节，向量列或矩阵列收敛等价于逐坐标、逐元素收敛（定理`thm:multivariable-coordinatewise-convergence`），由范数等价（定理`thm:ls-norm-equivalence`）与所选范数无关，所以主要在二范数下估计；矩阵级数按第~`sec:ls-vector-matrix-series`节的部分和定义并使用那里的绝对收敛判据。

#### 11.11.1 展开递推，分离初值与输入

1. 示例`ex:ls-affine-running-example`给出贯穿本节的$\bm T=\left[\begin{smallmatrix}1/2&1\\0&1/2\end{smallmatrix}\right]$、$\bm c=(0,1)^\top$，按分量解释“各留一半、第二分量传给第一分量、再补入$1$”，并从$\bm x_0=\bm0$算出前三步。

2. 指出三步之后第二分量似乎接近$2$、第一分量每步加$1$看不出是否有界、换初值的结果也无法判断，于是先把$\bm x_k$直接写成初值与输入的表达式。陈述并证明引理`lem:ls-affine-unrolling`：对$k$归纳，用分配律并把和式指标平移一位得$\bm x_k=\bm T^k\bm x_0+\sum_{j<k}\bm T^j\bm c$。

3. 解释展开的两部分：$\bm T^k\bm x_0$是初值经$k$轮作用后的剩余影响，$\bm T^j\bm c$是$j$轮前加入的输入再经$j$次作用的结果；$\bm c=\bm0$时只剩纯矩阵幂轨迹；强调这里只是有限展开，尚未假定极限或平衡存在。

4. 比较同一$\bm T,\bm c$下不同初值的两条轨迹，相减后输入部分抵消，只剩$\bm T^k(\bm x_0-\widetilde{\bm x}_0)$；说明只看一个初始差不够，陈述并证明引理`lem:ls-affine-difference-decay`：充分性由$\lVert\bm T^k\bm v\rVert_2\leq\lVert\bm T^k\rVert_{\mathrm F}\lVert\bm v\rVert_2$，必要性依次取$\bm v=\bm e_j$得每列趋零，再由逐元素收敛定理得$\bm T^k\to\bm0$。

5. 由引理得出下一步的任务：判断初值影响能否全部消失须先研究$\bm T^k$何时趋于零，之后再回到输入累积寻找共同极限。

#### 11.11.2 用谱半径判断初值影响的衰减

1. 先给出便于检验的充分条件：某个次乘性范数下$\lVert\bm T\rVert<1$时$\lVert\bm T^k\rVert\leq\lVert\bm T\rVert^k\to0$，在诱导范数下表示每轮把任何差异缩短到$\lVert\bm T\rVert$倍以内。

2. 用贯穿例说明该条件不必要：$\lVert\bm T\rVert_2>1$、$\lVert\bm T\rVert_1=\lVert\bm T\rVert_\infty=3/2$，而第10章示例`ex:ls-matrix-geometric-series`的显式式$\bm T^k=2^{-k}\left[\begin{smallmatrix}1&2k\\0&1\end{smallmatrix}\right]$表明$\bm T^k\to\bm0$，谱半径为$1/2$；指出$\bm T$不正规、对角线上方的耦合使单步放大超过$1$（回指11.4节），所以需要只依赖谱半径、覆盖非正规矩阵的判据。

3. 交代核心引理的构造思路——用相似变换把实Schur形的对角块化为模长乘旋转，再用逐块坐标缩放压小上方的块，得到使诱导范数不超过$r$的坐标范数。陈述并证明几何上界引理`lem:ls-power-geometric-bound`：取实Schur形$\bm T=\bm Q\bm U\bm Q^\top$（定理`thm:ls-real-schur`），二阶块经$\bm P_i$化为$|\lambda_i|\bm R_i$；令$\bm D_\varepsilon=\operatorname{diag}(\varepsilon^{i-1}\bm P_i)$，则第$(i,j)$块带因子$\varepsilon^{j-i}$，分块对角部分范数不超过$\rho(\bm T)$、非对角部分不超过$\varepsilon c$，取$\varepsilon$足够小；最后令$\bm M=\bm Q\bm D_\varepsilon$，验证坐标范数诱导的矩阵范数是$\lVert\bm M^{-1}\bm B\bm M\rVert_2$，由次乘性换回二范数得$C_r=\lVert\bm M\rVert_2\lVert\bm M^{-1}\rVert_2$。

4. 说明常数$C_r$与$k$无关但随$r$改变，几何上界也不表示原范数下每步收缩。示例`ex:ls-coordinate-norm-contraction`在贯穿例中走一遍构造：$\bm M=\operatorname{diag}(1,\varepsilon)$，取$\varepsilon=1/4$，由$\bm G^\top\bm G$的迹与行列式求出$\left[\begin{smallmatrix}a&b\\0&a\end{smallmatrix}\right]$的最大奇异值$(b+\sqrt{b^2+4a^2})/2$，得$\lVert\bm T\rVert_*=(1+\sqrt{17})/8\approx0.640$；再由对角矩阵的二范数是最大对角元模得$\lVert\bm M^{-1}\rVert_2=4$，换回欧氏长度的代价是常数$4$；再由$\lVert\bm T^k\bm e_2\rVert_2\geq k2^{1-k}$说明$r$不能直接取为$\rho(\bm T)$。

5. 陈述并证明矩阵幂的衰减判据`thm:ls-power-decay`（$\bm T^k\to\bm0$当且仅当$\rho(\bm T)<1$）：充分性取$\rho<r<1$由几何上界得到；必要性对模不小于$1$的实特征值取特征向量，对非实特征值取实不变平面的基$\bm P=[\bm u\;\bm w]$，用左逆$\bm L$得$\lVert\bm T^k\bm u\rVert_2\geq1/\lVert\bm L\rVert_2$，两种情形轨迹都不趋于零。

6. 结合引理`lem:ls-affine-difference-decay`得所有初值差异消失当且仅当$\rho(\bm T)<1$，并用两个反例说明判据面向全体初值：示例`ex:ls-partial-convergence`中$\operatorname{diag}(1/2,2)$的初始差$(1,0)^\top$衰减而$(0,1)^\top$按$2^k$增长，某个特殊初始差衰减不能说明$\bm T^k\to\bm0$；示例`ex:ls-separate-limits`中$\operatorname{diag}(1,1/2)$的每条轨迹都收敛但极限保留初值第一坐标，各轨迹收敛不等于趋于同一极限。

7. 讨论$\rho(\bm T)=1$：由判据与引理，初值差异不会全部消失，但轨迹表现因矩阵而异——$\bm I$时恒定、$-\bm I$时来回翻转，$90^\circ$旋转$\bm R$保持长度且$\bm R^4=\bm I$，非零初值以$4$步为周期循环，有界而不收敛；示例`ex:ls-unit-spectral-radius-growth`以$\bm J_1^k=\left[\begin{smallmatrix}1&k\\0&1\end{smallmatrix}\right]$说明特征向量不足时线性增长，谱半径为$1$不能保证矩阵幂有界。

8. 说明多项式因子来自对角线上方的耦合：引入$s$阶Jordan块$\lambda\bm I+\bm N$（只用这一具体形式），由可交换性二项展开得式`eq:ch06-jordan-power`；$s\geq2$、$|\lambda|=1$时$(1,2)$元模为$k$，矩阵幂无界；$|\lambda|<1$时块幂仍趋于零——$\lambda=0$时有限步为零，$0<|\lambda|<1$时非零元被$|\lambda|^{-j}k^j|\lambda|^k$控制，由相邻项之比趋于$|\lambda|<1$得它被几何数列压住——但多项式因子可能使块幂先上升。示例`ex:ls-jordan-transient`对$\left[\begin{smallmatrix}0.8&1\\0&0.8\end{smallmatrix}\right]$从$(0,1)^\top$出发，列出第一坐标在$k=4,5$达约$2.05$后才衰减（图`fig:vol1-add-linear-jordan-accumulation`）；并指出多项式因子也是引理中$C_r$的来源，$r$越接近$\rho$常数可能越大。

9. 补充$\rho(\bm T)>1$的情形：由判据必要性的证明，从模大于$1$的特征方向或不变平面出发的初始差不会消失，但如示例`ex:ls-partial-convergence`所示，仍可能有特殊初值的差异趋于零。

#### 11.11.3 累积输入与共同极限

1. 回到输入累积，说明若所有轨迹趋于同一点，在更新规则两边取极限得平衡方程$(\bm I-\bm T)\bm x_\star=\bm c$。陈述并证明共同极限的判据`thm:ls-affine-common-limit`：$\rho(\bm T)<1$时$1$不是特征值、$\bm I-\bm T$可逆，平衡唯一，相减得$\bm x_k-\bm x_\star=\bm T^k(\bm x_0-\bm x_\star)\to\bm0$；反过来所有轨迹收敛到同一向量则两轨迹之差趋零，由引理与判据得$\rho(\bm T)<1$。

2. 以$\bm T=2\bm I$说明单有$\bm I-\bm T$可逆只保证平衡唯一，不保证它吸引其他初值：误差按$2^k$增长。

3. 指出定理给出平衡位置但未说明它怎样由历次输入累积而成：从$\bm x_0=\bm0$出发，$\bm x_k$是矩阵级数$\sum\bm T^j$的部分和作用于$\bm c$，并以标量几何级数类比。陈述并证明Neumann级数定理`thm:ls-neumann`（式`eq:ls-neumann-series`、`eq:ls-neumann-tail`）：由几何上界与定理`thm:ls-absolute-series-convergence`得绝对收敛；由有限几何和恒等式$\bm S_N(\bm I-\bm T)=(\bm I-\bm T)\bm S_N=\bm I-\bm T^{N+1}$、乘以固定矩阵的连续性（第~`sec:multivariable-continuity`节）与$\bm T^{N+1}\to\bm0$识别和为$(\bm I-\bm T)^{-1}$；反过来级数收敛则通项趋零，由判据得$\rho<1$；在$\lVert\bm T\rVert\leq q<1$时由尾和估计得截断界$q^{N+1}/(1-q)$。

4. 由$\lVert\bm S_N\bm c-\bm S\bm c\rVert_2\leq\lVert\bm S_N-\bm S\rVert_2\lVert\bm c\rVert_2\to0$得$\bm x_\star=\sum_j\bm T^j\bm c$，把平衡解释为全部历次输入经各自轮数传播后的总和；强调充要条件针对整个矩阵级数，以$\operatorname{diag}(1/2,2)$、$\bm c=(1,0)^\top$说明仅一个向量级数收敛推不出$\rho<1$。

5. 示例`ex:ls-affine-running-equilibrium`对贯穿例由平衡方程逐分量解得$\bm x_\star=(4,2)^\top$，用第10章已求的$(\bm I-\bm T)^{-1}$核对，再按级数逐项看$\bm T^j\bm c=2^{-j}(2j,1)^\top$，借第10章示例中的两个标量级数得两个分量的和$4$与$2$；结论是第一分量的增长不会无限持续，且由$\rho=1/2$从任何初值出发都得到同一平衡。

6. 区分定理中的两种条件：$\rho<1$充要但定性，$\lVert\bm T\rVert\leq q<1$充分且给出可计算的误差上界；由式`eq:ls-neumann-tail`取$N=k-1$得从零出发时$\lVert\bm x_k-\bm x_\star\rVert\leq q^k\lVert\bm c\rVert/(1-q)$；图`fig:ls-neumann-series-tail`以$\left[\begin{smallmatrix}0.7&0.6\\0&0.1\end{smallmatrix}\right]$核对真实残差与尾界。

7. 说明只知$\rho<1$时，可用几何上界引理构造坐标范数使尾界成立，但回到原误差度量须乘以$\lVert\bm M\rVert_2\lVert\bm M^{-1}\rVert_2$；在贯穿例中用示例`ex:ls-coordinate-norm-contraction`的范数得$\lVert\bm x_k-\bm x_\star\rVert_2\leq11.1\times0.641^k$，并以$k=3$时真实误差约$2.02$、上界约$2.92$核对。

#### 11.11.4 收敛速度与暂时放大

1. 转向接近平衡的速度：由$\bm e_k=\bm T^k\bm e_0$与几何上界得$\lVert\bm e_k\rVert_2\leq C_rr^k\lVert\bm e_0\rVert_2$，误差至少按略大于谱半径的公比几何衰减；说明这是对全体初始误差一致的上界，某些方向衰减更快，谱半径只决定速度，平衡位置由$\bm c$与$(\bm I-\bm T)^{-1}$决定。

2. 用图`fig:ls-spectral-radius-convergence`展示最简单的正规情形$\rho\bm I$：误差每步乘以$\rho$，$\rho=0.5,0.9$衰减、$\rho=1.1$增长。

3. 指出$C_r$可能大于$1$，长期衰减不排除早期变大。示例`ex:ls-running-transient`在贯穿例中取初始误差$(0,1)^\top$，由显式式算出前三步误差长度约$1.118$、$1.031$、$0.760$，前两步都比初始误差长，说明谱半径$1/2$只描述长期速度。

4. 把放大归因于方向间的耦合，并给出耦合更强的例子：示例`ex:ls-transient-growth`取$\bm B=\left[\begin{smallmatrix}0.8&4\\0&0.5\end{smallmatrix}\right]$、$\bm x_0=(0,1)^\top$（式`eq:ch06-fixed-iteration-example`），沿用示例`ex:ls-triangular-power`的矩阵幂与轨迹（式`eq:ch06-diagonalizable-finite-trajectory`），算出前三步长度约$4.03$、$5.21$、$5.16$，远大于初值长度而$\rho=0.8$保证最终衰减。

5. 用初值沿特征方向的分解解释放大：$\tfrac{40}{3}\bm v_1$与$\bm v_2$都很长且几乎反向，初值由二者相消而成，不同的衰减速度很快打破相消，长度先增后降（图`fig:ch06-transient-growth`）。

6. 对能用实可逆$\bm V$对角化的$\bm T$，由$\lVert\bm\Lambda^k\rVert_2\leq\rho^k$与次乘性得上界$\lVert\bm T^k\rVert_2\leq\lVert\bm V\rVert_2\lVert\bm V^{-1}\rVert_2\rho^k$，说明因子不小于$1$、越大允许的早期放大越强，并在示例`ex:ls-transient-growth`中估计这个因子超过$178$（特征方向夹角约$4.3^\circ$）；再验证贯穿例只有一维特征空间、与示例`ex:ls-jordan-transient`同样不可对角化，放大来自式`eq:ch06-jordan-power`的多项式因子；正规矩阵则由11.4.3节的$\lVert\bm T^k\rVert_2=\rho^k$取$k=1$得每步$\lVert\bm e_{j+1}\rVert_2\leq\rho\lVert\bm e_j\rVert_2$，误差从第一步起不增加；结论是长期衰减、有限步最大放大与具体方向的表现须分别考察。

7. 说明谱半径确切刻画的是长期几何速率，陈述并证明Gelfand公式`thm:ls-gelfand-formula`（式`eq:ls-gelfand-formula`）：二范数下上界由几何上界与$C_r^{1/k}\to1$得到，下界重复判据必要性证明中的估计得$\lVert\bm T^k\rVert_2\geq c\rho^k$；上下极限夹出极限；再由范数等价推广到任意矩阵范数；次乘性范数下由$\lVert\bm T^k\rVert^{1/k}\leq\lVert\bm T\rVert$得$\rho\leq\lVert\bm T\rVert$。

8. 解释公式的含义：次乘性范数小于$1$必使谱半径小于$1$，这正是本节开头的充分条件，而贯穿例说明反之不成立；谱半径是最大放大倍数的长期几何平均，不表示每条轨迹每步乘以同一倍率。

9. 给出缩小十倍的参考步数$1/\log_{10}(1/\rho)$，$\rho=0.5$约$3.3$步、$\rho=0.99$约$229$步；再以贯穿例说明实际步数受常数、初始方向与暂时放大影响——$\lVert\bm e_k\rVert_2=2^{-k}\sqrt{4k^2+1}$到$k=8$才缩小十倍；精确解未知时如何用残差判断停止留给第~`sec:ls-stationary-iterations`节。

#### 11.11.5 逐步误差的累积

1. 放宽每轮精确执行的假设，写出带附加误差的序列$\bm y_{k+1}=\bm T\bm y_k+\bm c+\bm\delta_k$；与平衡方程相减得$\bm e_{k+1}=\bm T\bm e_k+\bm\delta_k$，说明它与原更新同形、只是输入换成$\bm\delta_k$，可以仿照有限展开分析。

2. 陈述并证明逐步误差的累积定理`thm:ls-accumulated-step-errors`（式`eq:ls-noise-floor`）：第一条对$k$归纳得$\bm e_k=\bm T^k\bm e_0+\sum_j\bm T^{k-1-j}\bm\delta_j$；第二条在诱导范数$\lVert\bm T\rVert\leq q<1$与$\lVert\bm\delta_j\rVert\leq\delta$下由三角不等式与有限几何和得$q^k\lVert\bm e_0\rVert+\delta(1-q^k)/(1-q)$，上极限不超过$\delta/(1-q)$；第三条只知$\rho<1$时用$C_rr^i$代替$q^i$得带$C_r$的界。

3. 解释展开的两部分：初始误差按几何速度消失；较早的附加误差衰减得多、较近的几乎原样保留，所以持续误差不会随迭代消失，上界趋于$\delta/(1-q)$，$q$越接近$1$越大。

4. 限定这一上界的性质：它是持续有界扰动下的最坏情形上界，不是每条轨迹必达的下限；也不保证误差有极限——以$\bm T=\bm0$、交替变号的$\bm\delta_k=(-1)^k\delta\bm u$为例，误差长度始终等于上界$\delta$，说明上界不能改进，而误差来回翻转没有极限。

5. 说明第三条中两项都带$C_r$：非正规的$\bm T$下小的附加误差在衰减前也可能先被暂时放大，累积上界按$C_r$倍增大；并指出具体算法如何产生附加误差、怎样选更新规则与参数、何时停止，留给第~`sec:ls-stationary-iterations`节。

### 11.12 本章小结

1. 重述本章的结构：先研究线性作用在什么样的基下最简单，再用这些简单表示解决长度约束下的极值、低秩逼近与伸缩分离三个问题，最后研究误差、扰动与反复作用。

2. 归纳前五节怎样逐步调整对基的要求：特征基使矩阵对角化，特征值是特征多项式的根且不随基改变，Cayley--Hamilton定理给出$p_{\bm A}(\bm A)=\bm0$；可对角化当且仅当有$n$个线性无关的实特征向量，此时$\bm A^k=\bm V\bm\Lambda^k\bm V^{-1}$；要求标准正交基时能对角化的恰是实对称矩阵，分解可写成$\bm S=\sum\lambda\bm P_\lambda$且谱投影唯一；一般方阵只能化为实Schur形，正规矩阵化为分块对角形；两端各取标准正交基时任意矩阵都有SVD，由它读出谱范数、Frobenius范数与秩。

3. 归纳中间三节的三个具体问题：单位长度下二次型的两端极值是两端特征值，加权长度下借$\bm B=\bm L^\top\bm L$换元化为广义特征方程$\bm S\bm v=\mu\bm B\bm v$；截断SVD在秩不超过$k$的矩阵中误差最小，论证由“选矩阵化为选子空间”、秩一的Rayleigh商与秩$k$的迹极值组成，两种范数下的最小误差分别由舍弃奇异值的平方和与$\sigma_{k+1}$给出；极分解先由$\bm W^\top\bm W=\bm I$消去正交因子得$\bm H^2=\bm A^\top\bm A$，沿谱开方求出唯一半正定$\bm H$，可逆时由$\bm W=\bm A\bm H^{-1}$得正交因子，它也是Frobenius范数下最近的正交矩阵；开方与求逆归纳为沿谱定义的矩阵函数$f(\bm S)$。

4. 归纳最后三节读出的三类相关而不能互相代替的性质：一次作用的误差放大（绝对放大是最大奇异值，固定输入处由相对条件数刻画，对全部输入取最坏得$\kappa_2=\sigma_{\max}/\sigma_{\min}$）；矩阵本身受扰动时的变化（有序特征值与奇异值移动不超过$\lVert\bm E\rVert_2$、可据此保证正定性与秩，到奇异矩阵的距离是$\sigma_{\min}$，特征子空间转角由扰动与谱隙之比控制，一般方阵的特征值还受特征基条件数影响、缺少特征向量时可能很敏感）；固定更新的长期行为（初值影响消失当且仅当$\rho(\bm T)<1$，同一条件使Neumann级数收敛、所有初值趋于同一平衡$(\bm I-\bm T)^{-1}\bm c$，谱半径决定长期速度，非正规矩阵可能先放大再衰减，逐步有界误差累积成有界的误差水平）。

5. 指出第~`chap:linear-equations-and-optimization`章求解线性方程、最小二乘与矩阵方程时将用到奇异值分解、Rayleigh商、条件数、谱、Cayley--Hamilton定理、实Schur形与Neumann级数；并说明本章的误差结论都是有限变化界，第~`chap:multivariate-calculus`章再对一般矩阵映射建立微分，求局部条件数与一阶响应。

## 第12章 线性方程与矩阵方程

正文入口：[05-linear-matrix-equations.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/05-linear-matrix-equations.tex)。

1. 从前几章的正向计算转到反向问题：矩阵和希望得到的输出已经给定，要找出输入。本章（`chap:linear-equations-and-optimization`）先研究线性方程，再研究以矩阵为未知量的Sylvester方程与Lyapunov方程。列出所用工具：第`chap:linear-operations`章的向量与矩阵运算，第`chap:linear-representation`章的列空间、零空间与秩，第`chap:normed-inner-product-spaces`章的正交分解及收敛、连续性与矩阵级数，第`chap:linear-analysis`章的特征值、奇异值、条件数、Schur分解与Neumann级数；说明最小二乘与最小范数解用正交分解和代数恒等式建立，迭代方法依靠矩阵幂、谱、内积和投影，不依赖多元微分或一般优化理论。

2. 说明前八节围绕$\bm A\bm x=\bm b$的四个问题展开，第一个是要求什么样的解：第`sec:ls-solution-selection`节由$\bm b$是否落在列空间判断有没有解、由零空间大小判断有几个解；无解时改求最小二乘解，多解时取范数最小的代表；奇异值分解与伪逆把三种情况写成同一公式，加权与齐次最小二乘是同一框架下的两种变形。

3. 第二个问题是怎样算出选定的解，第`sec:ls-direct-methods`—`sec:ls-row-projection`节给出四类路线：直接法按结构选用LU、Cholesky、LDL、分块消元与低秩更新，最小二乘用正规方程或QR；定常迭代把矩阵分裂成易解部分与余项并反复施加同一更新；Krylov子空间法每步在残差与矩阵乘积张成的子空间中选最好的近似，按对称性、正定性与形状选用方法；行列投影法每步只用一行或一列。约定每种方法分“主要思想、算法实现、算法分析”三部分，分别说明核心做法及依据，初始化、每步计算与终止条件，以及正确性、误差敏感性、收敛条件与速度和计算代价。

4. 第三、四个问题：第`sec:ls-numerical-sensitivity`节区分数据误差与计算误差，用条件数、残差与后向误差判断可信程度，并说明正规方程为何放大误差、伪逆为何在秩变化时不连续；第`sec:ls-truncated-svd-ridge`节针对小奇异值的放大，用岭回归与截断SVD以拟合误差换取稳定；第`sec:ls-method-selection`节在同一求解目标下按矩阵结构、计算开销、收敛速度和数值稳定性比较方法。

5. 最后两节把未知量推广为矩阵：Sylvester方程$\bm A\bm X+\bm X\bm B=\bm C$拉直后仍是线性方程但规模很大，因此直接从$\bm A$、$\bm B$的特征值读出可解条件，再用实Schur形逐列求解；Lyapunov方程是其对称特例，另需讨论解的对称性、计算上的节省以及解何时正定。

6. 约定记号：已知$\bm A\in\mathbb R^{m\times d}$、$\bm b\in\mathbb R^m$，未知$\bm x\in\mathbb R^d$，方阵取$m=d$；精确解或选定的最小范数解记$\bm x_\star$，最小二乘解记$\hat{\bm x}$，迭代近似记$\bm x_k$，残差$\bm r_k=\bm b-\bm A\bm x_k$；分解因子、子空间坐标和搜索方向只是中间量，最后换回原变量$\bm x$。

7. 约定输入输出：求解统一以$\bm A$、$\bm b$为输入、以$\bm x$为输出；初值、容差、步数上限、松弛参数、权矩阵和预条件是各方法的参数，因子、残差和搜索方向是中间量。多个右端排成$\bm B=[\bm b_1\;\cdots\;\bm b_s]$时写成$\bm A\bm X=\bm B$，各列分别求解并尽量共用对$\bm A$的分解；Sylvester方程的两个系数矩阵在引入时再说明角色。


### 12.1 线性方程的三种情况与统一选解

1. 对同一个方程$\bm A\bm x=\bm b$，先用列空间与零空间区分唯一解、无穷多解和无解，再规定每种情况要求什么样的解：相容时保留全部精确解，不相容时取离$\bm b$最近的可实现输出即最小二乘，解不唯一时取欧氏范数最小者作代表。说明三种情况针对原精确方程，有限维普通最小二乘总有解且最小范数代表唯一，因而奇异值分解与伪逆能把各情形写成同一公式；随后交代加权与齐次两种变形和可核对的检验条件，并声明本节（第`sec:ls-solution-selection`节）只讨论定义、存在唯一性和最优性，计算过程从第`sec:ls-direct-methods`节开始。

#### 12.1.1 精确方程的三种情况与解集

1. 对$\bm A\in\mathbb R^{m\times d}$、$\bm b\in\mathbb R^m$，由$\bm A\bm x=x_1\bm a_1+\cdots+x_d\bm a_d$把方程解释为能否用各列组合出$\bm b$，得到有解当且仅当$\bm b\in\operatorname{range}(\bm A)$，称为相容。再由添上$\bm b$这一列是否扩大列张成空间，推出增广矩阵秩判据式`eq:ls-augmented-rank`，并用$x=1,x=1$与$x_1+x_2=1,x_1+x_2=2$两个反例说明方程个数与未知量个数本身不能决定解的情况。

2. 承接相容判据转向解的个数：两解之差属于$\ker\bm A$，零空间向量加到解上不改变输出，因而把有没有解与有几个解合并成三分法。

3. 定理`thm:ls-three-solution-cases`：记$r=\operatorname{rank}\bm A$、$\tilde r=\operatorname{rank}[\bm A\;\bm b]$，则$\tilde r=r=d$时唯一解、$\tilde r=r<d$时无穷多解、$\tilde r>r$时无解，三者恰有其一成立。

4. 证明先由添一列至多增加一个方向得$\tilde r\in\{r,r+1\}$，从而三个条件互斥且穷尽；再由式`eq:ls-augmented-rank`识别无解情形，相容时全部解为$\bm x_0+\ker\bm A$，结合秩零度定理`thm:ls-rank-nullity`的$\dim\ker\bm A=d-r$区分唯一与沿核向量平移得到的无穷多解。

5. 区分两种满秩的保证：满列秩$r=d$保证至多一个精确解但不保证有解，以$\bm A=(1,1)^\top$为例；满行秩$r=m$保证每个右端都有解但可能不唯一，以$\bm A=(1,1)$为例；方阵满秩时两者同时成立，即可逆情形。随后（第`sec:ls-determinant-invertibility`处）给出方阵可逆当且仅当$\det\bm A\neq0$及伴随矩阵求逆公式，一方向用行列式乘法性（第`sec:ls-determinant-properties`节），另一方向用古典伴随恒等式（定理`thm:ls-adjugate-identity`）除以$\det\bm A$；说明行列式只作理论判据，实际由第`sec:ls-lu`节的消元在求解时读出秩。

6. 以一句过渡说明下面用同一个拟合问题依次产生三种情况，并在本节后文反复回用。

7. 示例`ex:ls-line-three-cases`：在$t=0,1,2$处拟合$a+st$，系数矩阵两列分别对应常数项与时刻。$\bm b=(1,2,3)^\top$时满列秩且有唯一解$(1,1)^\top$；把常数列重复为第三列得$\widetilde{\bm A}$，方程只要求$x_1+x_3=1$、$x_2=1$，秩$2<3$，有无穷多解；保留两列而改$\bm b=(1,2,2)^\top$，第三个方程矛盾，由$\det[\bm A\;\bm b]=-1$得$\tilde r=3>r=2$，留给第`sec:ls-ordinary-ls`节的最小二乘处理。

8. 对两种相容情形，由两解之差属于核空间写出全部解$\bm x_p+\ker\bm A$（式`eq:ls-affine-solution-set`），称为自由度$d-r$的仿射空间，并以图`fig:vol1-add-linear-nullspace-fibers`中$\bm A=(1,1)$的平行直线族展示同一输出对应的整组输入。回到复制常数列的例子，取特解$(1,1,0)^\top$、核方向$(1,0,-1)^\top$，写出$(1+t,1,-t)^\top$并逐项代回核验，说明自由参数对应常数项在两个相同列之间的拆法；核为零时退化为唯一解，计算过程留给第`sec:ls-direct-methods`节的消元与分解。

#### 12.1.2 无精确解时的最小二乘

1. 当$\bm b$不在列空间中时改求式`eq:linear-algebra-least-squares`的最小二乘问题，区分系数$\bm x$、拟合值$\bm A\bm x$与残差$\bm r=\bm b-\bm A\bm x$三个对象。由于目标只经拟合值依赖系数，先解子空间最近点问题：由正交分解（引理`lem:ls-orthogonal-decomposition`）写$\bm b=\hat{\bm b}+\bm e$，再由勾股关系式`eq:ls-nearest-point-pythagoras`证明正交投影$\hat{\bm b}$是唯一的全局最优拟合值，最近点由残差与列空间正交完全刻画；图`fig:ls-orthogonal-projection-nearest`在一条直线子空间上画出这一几何。

2. 把残差与列空间正交写成与每一列正交，即$\bm A^\top\bm r=\bm0$，代入残差得到正规方程式`eq:linear-algebra-normal-equations`，并解释“正规”指法向。由上一段得出最小二乘解当且仅当满足正规方程，强调这一条件完全由正交分解推出，不需要梯度、Hessian或一般最优化的一阶条件。

3. 由列空间的标准正交基$\bm Q_1$写出投影$\bm P=\bm Q_1\bm Q_1^\top$（第`sec:ls-projection-matrices`节），拟合值与残差分别为$\bm P\bm b$与$(\bm I-\bm P)\bm b$；满列秩时由正规方程对一切$\bm b$成立得到式`eq:ls-column-space-projector`。用对称性解释残差与拟合值正交，用幂等性解释再拟合不变，并指出实际求解只需系数，不必形成这个$m\times m$矩阵。

4. 由正规方程是否总有解、有多少个解仍由列空间与零空间回答，引出把最优性条件、存在性和唯一性合在一起的定理，并指出后面各种最小二乘算法都以它为正确性依据。

5. 定理`thm:ls-least-squares-solutions`：对任意$\bm A,\bm b$，$\hat{\bm x}$是最小二乘解当且仅当满足正规方程；解总存在，全部解为$\hat{\bm x}+\ker\bm A$并共享拟合值$\bm P\bm b$与残差；解唯一当且仅当$\bm A$满列秩，此时$\bm A^\top\bm A$正定且$\hat{\bm x}=(\bm A^\top\bm A)^{-1}\bm A^\top\bm b$。

6. 证明由式`eq:ls-nearest-point-pythagoras`把最优化为$\bm A\hat{\bm x}=\bm P\bm b$，再由正交分解唯一性化为残差与列空间正交即正规方程；由$\bm P\bm b$属于列空间得存在性；由$\lVert\bm A\bm x\rVert_2^2=\bm x^\top\bm A^\top\bm A\bm x$得式`eq:ls-normal-kernel`，从而解集为特解加$\ker\bm A$，核为零时二次型严格为正、$\bm A^\top\bm A$正定。

7. 据定理区分两层唯一性：拟合值总唯一，系数仅在满列秩时唯一；并把相容方程回接为残差为零、$\bm P\bm b=\bm b$、最小二乘解集即精确解集的特例。

8. 示例`ex:ls-line-least-squares`：回到示例`ex:ls-line-three-cases`的$\bm b=(1,2,2)^\top$，写出$2\times2$正规方程并解得$\hat{\bm x}=(7/6,1/2)^\top$、$\bm r=(-1/6,1/3,-1/6)^\top$。逐分量核对$\bm A^\top\bm r=\bm0$及残差平方和$1/6\neq0$，说明这是三条观测不能同时满足时的最佳折中；对相容观测$(1,2,3)^\top$同一方程给出零残差，精确求解是同一目标的特例。

9. 由“满列秩只保证系数唯一”转入系数是否稳定的问题，指出设计矩阵两列接近共线时最明显。

10. 示例`ex:ls-nearly-collinear-design`：取非零正交向量$\bm c,\bm q$，两列为$\bm c$与$\bm c+\varepsilon\bm q$，观测$\bm y=\bm c+\delta\bm q$。由列组合展开，$\varepsilon\neq0$时系数$(1-\delta/\varepsilon,\delta/\varepsilon)^\top$精确拟合；$\varepsilon=0$时两列重合，只能拟合$\bm c$分量，残差跳为$\delta\bm q$，满足$w_1+w_2=1$的系数都是解。

11. 对照三个对象：$\varepsilon\to0$时拟合值从$\bm y$突变为$\bm c$，系数趋于无穷并对$\varepsilon,\delta$极敏感。说明这是近共线几何本身的性质而非舍入所致，留待第`sec:ls-ls-regularization-sensitivity`节用奇异值量化。

#### 12.1.3 多解时的最小范数代表

1. 承接秩亏时最小二乘解集$\hat{\bm x}+\ker\bm A$含无穷多点而方程不指定代表，规定取欧氏范数最小者，所用工具是输入空间的正交直和$\mathbb R^d=\operatorname{range}(\bm A^\top)\oplus\ker\bm A$（定理`thm:ls-four-subspaces-orthogonality`）。

2. 定理`thm:ls-minimum-norm-representative`：对任意$\bm A,\bm b$，最小二乘解中存在唯一的范数最小者$\bm x_\star$，它是解集中唯一落在行空间中的点；相容时它是范数最小的精确解，唯一可解时就是该解。

3. 证明把任一最小二乘解分解为行空间分量与核分量，由$\bm A\bm x_R=\bm A\bm x$说明去掉核分量后仍是最小二乘解；两解行空间分量之差同时属于行空间与核，只能为零，故全部解共享同一$\bm x_R$；再由勾股关系得到范数最小且唯一，相容与唯一可解情形作为特例。

4. 强调选代表依据的是事先给定的欧氏范数，并未把多解方程改成唯一可解，换范数一般会改变所选点。满行秩时把“落在行空间中”的刻画直接变成公式：所求解形如$\bm x=\bm A^\top\bm w$，代入方程得$\bm A\bm A^\top\bm w=\bm b$。

5. 定理`thm:ls-min-norm-full-row-rank`：$\bm A$满行秩时$\bm A\bm A^\top$可逆，方程对每个$\bm b$相容，最小范数解由式`eq:ls-min-norm-full-row-rank`给出。

6. 证明与式`eq:ls-normal-kernel`同理得$\ker(\bm A\bm A^\top)=\ker\bm A^\top=\{\bm0\}$，故$\bm A\bm A^\top$可逆；所给$\bm x_\star$满足方程且落在$\operatorname{range}(\bm A^\top)$中，由定理`thm:ls-minimum-norm-representative`即为最小范数解。

7. 解释解是各行的组合、组合系数由$m$阶方程确定；用Gram矩阵还是对$\bm A^\top$作QR留到第`sec:ls-normal-equations-method`节与第`sec:ls-qr-method`节比较，并指出既不满行秩也不满列秩时两个满秩公式都不能用，由此转入奇异值分解。

#### 12.1.4 用SVD与伪逆统一选解

1. 回顾前三小节对三种情形的处理（可逆取唯一解、无解取最近拟合值、多解取最小范数系数），指出一般的$\bm A$可能两种选择都要作；预告沿第`sec:ls-svd`节的奇异方向作统一构造，对可恢复方向取逆、其余方向置零，再用Penrose条件和两个投影核验其性质。

##### 12.1.4.1 伪逆的构造与统一解

1. 由秩$r$的奇异值分解式`eq:matrix-analysis-svd-rank-one-sum`并扩充奇异向量为标准正交基，从$\bm A$把$\bm v_i$送到$\sigma_i\bm u_i$得出反向应把$\bm u_i$送回$\bm v_i/\sigma_i$。按$\bm u_i$展开$\bm b$：$i\leq r$的分量可拟合并配给$\bm v_i/\sigma_i$，$i>r$的分量无原像而留在残差中，零空间方向不分配任何分量。

2. 定义`def:matrix-analysis-pseudoinverse`：据此定义Moore--Penrose伪逆式`eq:matrix-analysis-pseudoinverse`，并规定$\bm A=\bm0$时$\bm A^\dagger=\bm0$。

3. 以一句过渡说明这一构造恰好完成最小二乘与最小范数两次选择。

4. 定理`thm:matrix-analysis-pseudoinverse-minimum-norm`：全部最小二乘解为$\bm A^\dagger\bm b+\ker\bm A$，其中$\bm A^\dagger\bm b$是唯一的最小范数解。

5. 证明在奇异向量坐标下把残差平方写成$\sum_{i\le r}(\sigma_ic_i-b_i)^2+\sum_{i>r}b_i^2$，第二项与$\bm x$无关，第一项为零当且仅当$c_i=b_i/\sigma_i$，其余坐标任取构成核向量；再由$\bm A^\dagger\bm b$只含$\bm v_1,\ldots,\bm v_r$方向而与核正交，依定理`thm:ls-minimum-norm-representative`得最小范数性。

6. 说明定理对秩与$\bm b$的位置均无要求，前面的公式都是特例：满列秩时$\bm A^\dagger=(\bm A^\top\bm A)^{-1}\bm A^\top$，满行秩时由式`eq:ls-min-norm-full-row-rank`得$\bm A^\dagger=\bm A^\top(\bm A\bm A^\top)^{-1}$，可逆时都化为$\bm A^{-1}$，一般秩时只有和式可用。强调显式写出逆或伪逆只是数学表达，分解因子依次作用于右端的步骤见第`sec:ls-svd-solve`节。

7. 示例`ex:ls-line-min-norm`：取示例`ex:ls-line-three-cases`中复制常数列的$\widetilde{\bm A}$与$\bm b=(1,2,2)^\top$，拟合值只确定两个常数系数之和；由示例`ex:ls-line-least-squares`得全部最小二乘解$(7/6-t,1/2,t)^\top$，对范数平方关于$t$求最小得$\bm x_\star=(7/12,1/2,7/12)^\top$，并用与核方向$(1,0,-1)^\top$的内积为零核验它在行空间中。说明最小二乘选定拟合值，最小范数再在实现它的系数中把常数项平均分给两个相同列。

##### 12.1.4.2 Penrose条件与两个投影

1. 从奇异向量不唯一出发，提出需要不涉及奇异向量又能唯一确定$\bm A^\dagger$的条件，以说明伪逆与所选分解无关。

2. 定理`thm:ls-penrose-conditions`：$\bm A^\dagger$满足$\bm A\bm G\bm A=\bm A$、$\bm G\bm A\bm G=\bm G$及$\bm A\bm G$、$\bm G\bm A$对称四个条件，且满足这四个条件的$\bm G$唯一。

3. 证明先由和式与正交性算出$\bm A\bm A^\dagger=\sum_{i\le r}\bm u_i\bm u_i^\top$、$\bm A^\dagger\bm A=\sum_{i\le r}\bm v_i\bm v_i^\top$，得对称性并右乘得前两条；反向由第一、三条推出$\bm A\bm G$是到列空间的正交投影，由第二、四条推出$\bm G\bm A$是到$(\ker\bm A)^\perp$的正交投影，借正交投影由子空间唯一决定，连等式化出$\bm G=\bm A^\dagger$。

4. 解释四个条件的含义：前两条是可恢复方向上的一致性（$\bm G$确实实现可达输出、输出不含被消去的多余成分）；只有前两条时两个乘积可以是斜投影，后两条对称性使其成为正交投影，分别对应取最近拟合值与取范数最小系数；由于条件不涉及奇异向量，$\bm A^\dagger$不依赖分解的选取。

5. 由证明读出$\bm A\bm A^\dagger$投影到列空间、$\bm A^\dagger\bm A$投影到行空间，把两次选择写成$\bm A\bm x_\star=\bm P\bm b$与$\bm A^\dagger\bm A\bm x_\star=\bm x_\star$两个可检查等式，并在示例`ex:ls-line-min-norm`中核对拟合值$(7/6,5/3,13/6)^\top$与示例`ex:ls-line-least-squares`一致、$\bm x_\star$已在行空间中。最后指出小正奇异值的倒数会放大数据误差，留待第`sec:ls-numerical-sensitivity`节量化，本节先完成统一表达，为选择计算方法提供目标。

#### 12.1.5 加权最小二乘

1. 从观测可靠程度不同或误差相关需要按权度量残差进入，对对称正定$\bm M$给出式`eq:ls-weighted-objective`。由Gram因子（定理`thm:ls-gram-factor`）或正定平方根（第`sec:ls-matrix-square-root`节）写$\bm M=\bm R^\top\bm R$且$\bm R$可逆，经白化把各坐标误差变到同一欧氏尺度，化为$\bm R\bm A$、$\bm R\bm b$上的普通最小二乘，从而可搬用定理`thm:ls-least-squares-solutions`。

2. 定理`thm:ls-weighted-least-squares`：$\bm M$对称正定时，$\hat{\bm x}$是加权问题的解当且仅当满足加权正规方程式`eq:linear-algebra-weighted-normal-equations`；这组方程总有解，全部解为$\hat{\bm x}+\ker\bm A$，解唯一当且仅当$\bm A$满列秩。

3. 证明对$\bm R\bm A$、$\bm R\bm b$应用定理`thm:ls-least-squares-solutions`，由$\bm R^\top\bm R=\bm M$得加权正规方程；解集为特解加$\ker(\bm R\bm A)$，而$\bm R$可逆使$\ker(\bm R\bm A)=\ker\bm A$。

4. 解释加权正规方程即残差在$\bm M$内积下与列空间正交，权矩阵只改变误差度量而不改变系数与拟合值的含义；并指出半正定时$\ker\bm M$中残差不受惩罚、$\bm R$奇异，唯一性改为要求$\ker(\bm M\bm A)=\{\bm0\}$、拟合值也可能不唯一，正定结论不能全部沿用。

5. 满列秩时写出加权投影$\bm P_{\bm M}=\bm A(\bm A^\top\bm M\bm A)^{-1}\bm A^\top\bm M$，说明它幂等而一般不对称，在欧氏内积下是斜投影，但由$\bm u^\top\bm M\bm P_{\bm M}\bm v$关于$\bm u,\bm v$对称得其在$\bm M$内积下自伴，是该内积下的正交投影；同一$\bm A,\bm b$换权矩阵时最近点移动，引出下例与图`fig:linear-algebra-weighted-projection`。再说明白化只变换观测端、不改变未知量及其欧氏范数，所以解集与最小范数代表都与白化后普通问题一致，构造权因子并调用求解方法的步骤见第`sec:ls-svd-solve`节。

6. 示例`ex:linear-algebra-weighted-projection`：取$\bm A=(1,1)^\top$、$\bm b=(2,1)^\top$，欧氏正规方程给出拟合值$(1.5,1.5)^\top$，改用$\bm M=\operatorname{diag}(1,4)$后给出$(1.2,1.2)^\top$，解释第二坐标误差代价更大使最近点向$b_2$靠近。核对加权残差$(0.8,-0.2)^\top$与列向量的欧氏内积为$0.6$、加权内积为$0$，说明正交性只在所选内积下成立；图`fig:linear-algebra-weighted-projection`对照两种投影，右图残差不必形成欧氏直角。

#### 12.1.6 齐次最小二乘

1. 从只确定参数比例的模型$\bm A\bm h\approx\bm0$进入，以平面直线$h_1u+h_2v+h_3=0$拟合点为例，说明直接最小化$\lVert\bm A\bm h\rVert_2^2$总得零解，必须固定尺度。比较固定$h_3=1$会排除过原点的真实直线，而固定欧氏长度对各分量一视同仁，得到式`eq:linear-algebra-homogeneous-least-squares`；并区分它与求$\bm A\bm h=\bm0$全部解：后者是子空间$\ker\bm A$，满列秩时只含零向量，前者总给出最接近满足的单位方向。

2. 指出右端是对称半正定矩阵$\bm A^\top\bm A$的Rayleigh商在单位向量上的最小值，正是第`sec:ls-rayleigh-extremal`节研究的问题。

3. 定理`thm:ls-homogeneous-minimizers`：最小值存在且等于$\bm A^\top\bm A$的最小特征值$\lambda_{\min}$，最优解恰为对应特征空间中的单位向量；$\lambda_{\min}$单重时最优解只差符号，$\ker\bm A\neq\{\bm0\}$时$\lambda_{\min}=0$且任一单位零空间向量都最优。

4. 证明由Rayleigh--Ritz定理`thm:matrix-analysis-rayleigh-ritz`得到下界及取等条件，特征空间一维时单位向量只有$\pm\bm h_\star$；再由式`eq:ls-normal-kernel`与半正定矩阵特征值非负，得核非零时$\lambda_{\min}=0$。

5. 用$\bm A=[\,1\ -2\,]$核验：$\bm A^\top\bm A$的特征值为$0$与$5$，最优解$\pm(2,1)^\top/\sqrt5$满足$h_1-2h_2=0$、残差为零，两个符号给出同一比例$2:1$。

6. 由第`sec:ls-svd`节中右奇异向量是$\bm A^\top\bm A$的特征向量、特征值为奇异值平方，把最优解解释为最小奇异值对应右奇异子空间中的单位向量，最小值为最小奇异值的平方。最小特征值接近重根时扰动可能选出不同方向，其敏感度由第`sec:ls-subspace-sensitivity`节的子空间界控制；用SVD选取具体单位向量的步骤见第`sec:ls-svd-solve`节。

#### 12.1.7 求解目标的检验条件

1. 对普通最小二乘，以$\bm A^\top\bm r=\bm0$为最优性条件并报告残差范数（即$\bm b$到列空间的距离），要求最小范数时再检查$\bm x\perp\ker\bm A$，等价于$\bm A^\dagger\bm A\bm x=\bm x$。用示例`ex:ls-line-least-squares`的残差范数$1/\sqrt6$说明无解方程的最优残差本就非零而非求解失败，并用示例`ex:ls-line-min-norm`说明$(7/6-t,1/2,t)^\top$都满足前两项、只有$t=7/12$满足第三项。

2. 加权问题核对$\bm A^\top\bm M\bm r=\bm0$、报告$\sqrt{\bm r^\top\bm M\bm r}$并说明权矩阵，以示例`ex:linear-algebra-weighted-projection`中欧氏$\bm A^\top\bm r=0.6\neq0$说明这不是错误；齐次拟合不能照搬$\bm A^\top\bm r=\bm0$（否则把解推向零向量），应检查单位长度与最小特征方向。最后指出这些条件规定了后续算法的目标，浮点计算中“为零”须换成相对容限，容限与残差能否控制误差见第`sec:ls-numerical-stability`节，直接法的分解质量与迭代法的停止条件分别见第`sec:ls-direct-method-comparison`节、第`sec:ls-stationary-stopping`节和第`sec:ls-krylov-stopping`节。


### 12.2 利用分解直接求解

1. 从第`sec:ls-solution-selection`节确定的求解目标（精确解、最小二乘解或最小范数解）进入，说明本节用消元或正交变换把问题化为三角方程或较小的方程，在有限步内求解。约定各算法以$\bm A$和$\bm b$为输入、以所求$\bm x$为输出，分解因子、置换、变换后的右端和残差只作中间量，主元策略等需要选择的规则单列为超参数。

2. 交代本节顺序：先用LU、Cholesky与分块LDL处理一般非奇异、对称正定与对称不定方阵，再利用块结构和低秩修改复用这些方法，最后比较最小二乘的三条路线，即调用Cholesky的正规方程法（第`sec:ls-normal-equations-method`节）以及利用原矩阵分解的QR求解与SVD求解（第`sec:ls-qr-method`节、第`sec:ls-svd-solve`节）。每种算法按主要思想、算法实现、算法分析展开，QR之后介绍三种因子计算方法，SVD之后讨论加权与齐次目标；实现按计算次序逐段写，分析说明正确性与数值敏感度。

#### 12.2.1 LU分解

##### 12.2.1.1 主要思想

1. 设$\bm A\in\mathbb R^{d\times d}$非奇异，求$\bm A\bm x=\bm b$的唯一精确解$\bm x_\star$；一般解结构已在第`sec:ls-solution-selection`节讨论，这里只计算非奇异方阵的解。用行消元把$\bm A$化为上三角$\bm U$，把乘子收集为单位下三角$\bm L$，为避开零主元和过小主元而作的行交换累积为置换$\bm P$，得到式`eq:ls-palu`的$\bm P\bm A=\bm L\bm U$；原方程于是化为两个可逐个代入的三角方程，分解只依赖$\bm A$，换右端时可直接复用。

##### 12.2.1.2 算法实现

1. 输入$\bm A$、$\bm b$，超参数为主元策略，本小节固定为部分选主元：在当前列未处理元素中取绝对值最大者，相同时取行号最小者，使给定数据下的过程可以复算。交代算法分三步：先分解$\bm P\bm A=\bm L\bm U$，再依次解两个三角方程。

###### paragraph：LU分解

1. 初始化工作矩阵$\bm W=\bm A$、$\bm L=\bm I_d$、$\bm P=\bm I_d$，对$k=1,\ldots,d-1$先选主元：在第$k$列第$k$至$d$行中找出$|w_{r,k}|$最大的行$r$，交换$\bm W$的第$k,r$行并对$\bm P$作同样交换，$\bm L$前$k-1$列已保存的乘子也随之交换，使乘子始终跟随所在方程。主元$w_{k,k}\neq0$由$\bm A$非奇异保证，理由引定理`thm:ls-lu-existence`。

2. 再用主元行消去下方各行的第$k$个元素：对$i>k$计算乘子$l_{i,k}=w_{i,k}/w_{k,k}$并更新$w_{i,j}$（$j>k$），令$w_{i,k}=0$，每步使用工作矩阵的当前值而非最初的$a_{i,j}$。处理完第$d-1$列后取$\bm U=\bm W$。

3. 图`fig:ls-lu-elimination-steps`以无需换行的三阶矩阵示意消元过程：依次画出$\bm A$、消去第一列后的矩阵与$\bm U$，标出主元、待消元素与消出的零，乘子按被消元素位置填入$\bm L$，满足$\bm L\bm U=\bm A$。

###### paragraph：求解$\bm L\bm y=\bm c$

1. 分解后处理右端：令$\bm c=\bm P\bm b$，由式`eq:ls-palu`原方程等价于$\bm L\bm U\bm x=\bm c$，引入$\bm y=\bm U\bm x$后分成$\bm L\bm y=\bm c$与$\bm U\bm x=\bm y$两个三角方程，依次求解。解下三角方程时从第一个只含$y_1$的方程出发，按$i=1,\ldots,d$用式`eq:ls-forward-substitution`逐个计算$y_i$，右侧只用已算出的$y_1,\ldots,y_{i-1}$。把这一顺序称为前代，指出对角元非零时它逐个唯一地给出解；本处$l_{i,i}=1$，除法可省。

###### paragraph：求解$\bm U\bm x=\bm y$

1. 解上三角方程时从只含$x_d$的最后一个方程出发，按$i=d,\ldots,1$用式`eq:ls-back-substitution`逐个计算，右侧只用已算出的$x_{i+1},\ldots,x_d$。把这一顺序称为回代，完成后即得$\bm x_\star$；用图`fig:ls-triangular-substitution-order`对比两种顺序：前代自上而下，每个分量只依赖上方已求出的分量，回代自下而上，依赖关系相反。约定后文遇到三角方程时直接调用前代与回代。

2. 算例`ex:ls-lu-three-steps`用一个三阶矩阵与右端按三步核对：第一列换行选主元后乘子均为$\tfrac12$，第二列无需换行，得到$\bm P,\bm L,\bm U$；前代由$\bm c=\bm P\bm b$得$\bm y=(4,0,2)^\top$，回代得$\bm x=(1,-1,1)^\top$，并代回验证$\bm A\bm x=\bm b$与$\bm L\bm U$等于交换前两行后的$\bm A$。

##### 12.2.1.3 算法分析

###### paragraph：正确性

1. 指出算法能否进行取决于每步是否有非零主元：部分选主元对任何非奇异矩阵都能进行，不选主元则需额外条件，由此引出定理。

2. 定理`thm:ls-lu-existence`：非奇异的$\bm A$在部分选主元下每步都有非零主元，给出$\bm P\bm A=\bm L\bm U$，其中$|l_{i,j}|\leq1$、$\bm U$非奇异；不选主元时$\bm A=\bm L\bm U$存在当且仅当各顺序主子式$\det\bm A_k\neq0$，且此时分解唯一。

3. 证明第一部分：第$k$步开始时$\bm W=\bm M\bm A$且$\bm M$可逆，若第$k$列从第$k$行起全为零，前$k$列落在$\operatorname{span}\{\bm e_1,\ldots,\bm e_{k-1}\}$中而线性相关，与$\bm A$非奇异矛盾；主元取绝对值最大故$|l_{i,k}|\leq1$，倒读消元过程即得$\bm P\bm A=\bm L\bm U$。第二部分由$\bm A_k=\bm L_k\bm U_k$得必要性，由单位下三角消元保持$\det\bm W_k=\det\bm A_k$归纳得充分性，唯一性来自$\bm L_2^{-1}\bm L_1=\bm U_2\bm U_1^{-1}$只能为$\bm I_d$。

4. 由定理第一部分得出前代与回代给出原方程的解，行交换只重排方程；用$\left[\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right]$说明第二部分的条件不能仅由$\bm A$非奇异推出。

###### paragraph：数值敏感度

1. 部分选主元使$|l_{i,k}|\leq1$，但舍入影响仍取决于消元中元素的增长，误差界见第`sec:ls-numerical-stability`节。

###### paragraph：计算代价

1. 第$k$步更新$(d-k)^2$个元素，稠密分解约$\tfrac23d^3$次运算，每个新右端只需前代与回代各一次，约$2d^2$次；稀疏时还须考虑随消元顺序变化的填充。

#### 12.2.2 Cholesky分解

##### 12.2.2.1 主要思想

1. 设$\bm A$实对称正定，求精确解$\bm x_\star$。利用对称性把LU的两个三角因子取成互为转置，得到式`eq:matrix-analysis-cholesky`的Cholesky分解$\bm A=\bm L\bm L^\top$，其中$\bm L$为正对角下三角矩阵；只需构造一个因子，原方程$\bm L(\bm L^\top\bm x)=\bm b$即化为前代与回代各一次。

##### 12.2.2.2 算法实现

###### paragraph：$\bm L\bm L^\top$分解

1. 将$\bm L$初始化为零矩阵，按列用式`eq:ls-cholesky-columns`先算对角元、再算其下方元素。两式由比较$\bm A$与$\bm L\bm L^\top$的$(i,j)$元（$i\geq j$）得到：$k<j$的项只含已完成的列，令其等于$a_{i,j}$即可解出剩下的$l_{i,j}l_{j,j}$；计算只读$\bm A$的下三角部分，$\bm L^\top$由转置直接得到。

###### paragraph：求解$\bm L\bm y=\bm b$

1. 用第`sec:ls-lu`节的前代`eq:ls-forward-substitution`求解$\bm L\bm y=\bm b$，并指出与LU不同，这里$l_{i,i}$一般不为$1$，除法要保留。

###### paragraph：求解$\bm L^\top\bm x=\bm y$

1. 用回代`eq:ls-back-substitution`求解$\bm L^\top\bm x=\bm y$，上三角元素直接从$\bm L$读出；两次三角求解的次序来自$\bm L(\bm L^\top\bm x)=\bm b$，先解括号内的$\bm y$再求$\bm x$。

2. 算例`ex:ls-cholesky-three-steps`用一个三阶对称正定矩阵与右端核对三步：逐列算出$\bm L$的各元素（对角元均为$2$、下方元素均为$1$），前代得$\bm y=(4,3,2)^\top$，回代得$\bm x=(1,1,1)^\top$，并代回验证$\bm A\bm x=\bm b$。

##### 12.2.2.3 算法分析

###### paragraph：正确性

1. 指出逐列构造能否进行取决于每次开方的数是否为正，引出定理`thm:ls-cholesky-existence`：对称矩阵存在正对角下三角因子使$\bm A=\bm L\bm L^\top$，当且仅当$\bm A\succ0$，此时$\bm L$唯一并由式`eq:ls-cholesky-columns`给出。

2. 证明必要性由$\bm v^\top\bm A\bm v=\lVert\bm L^\top\bm v\rVert_2^2>0$得到。充分性对阶数归纳：把$\bm A$按首行首列分块，正定性给出$a_{1,1}>0$，对首变量配方后取$v_1$使平方项为零，推出剩余矩阵$\bm A_{22}-\bm a\bm a^\top/a_{1,1}$仍正定；后续各列正是对它重复同一步骤，故每次开方的数都为正。对角元取正后式`eq:ls-cholesky-columns`逐个唯一确定各元素。

3. 由$\bm A=\bm L\bm L^\top$确认所得$\bm x$满足$\bm A\bm x=\bm L\bm y=\bm b$。

###### paragraph：数值敏感度

1. 由$a_{j,j}=\sum_{k\leq j}l_{j,k}^2$得$|l_{j,k}|\leq\sqrt{a_{j,j}}$，因子不增长，故不选主元也后向稳定（第`sec:ls-numerical-stability`节），解的误差仍由条件数决定（第`sec:ls-matrix-condition-number`节）。

###### paragraph：计算代价

1. 稠密分解约$\tfrac13d^3$次运算，为LU的一半，只存一个三角因子。

#### 12.2.3 分块LDL分解

##### 12.2.3.1 主要思想

1. 设$\bm A$实对称非奇异但不一定正定，求唯一精确解；指出此时Cholesky的根号内可能出现负数。分块LDL不开方，把主元连同正负号保留在块对角矩阵$\bm D$中，构造式`eq:ls-ldlt`的$\bm P\bm A\bm P^\top=\bm L\bm D\bm L^\top$；对称置换保持对称，允许二阶块是因为对角元可能全为零而找不到一阶主元。

##### 12.2.3.2 算法实现

1. 把选块策略列为超参数，为可复算给出默认代数规则：有非零对角元时取绝对值最大者作一阶块，对角元全为零时取绝对值最大的非零非对角元及其两个下标组成二阶块，相同时按下标顺序。后一种块$\left[\begin{smallmatrix}0&a\\a&0\end{smallmatrix}\right]$行列式为$-a^2\neq0$而可逆；并说明该规则只保证构造可进行，不保证数值稳定。

###### paragraph：选块与对称交换

1. 初始化$\bm W=\bm A$、$\bm L=\bm I_d$、$\bm P=\bm I_d$，$\bm D$为空。每轮按选块策略把主元下标交换到剩余矩阵前端，同时交换$\bm W$的行与列，对$\bm P$和$\bm L$中已算出的乘子作相应交换，再把剩余矩阵写成以可逆块$\bm E$为左上块的$2\times2$分块形式。

###### paragraph：块消元

1. 逐行求解一阶或二阶方程$\bm M\bm E=\bm C$得乘子块$\bm M$，写入$\bm L$中主元块下方，把$\bm E$放入$\bm D$的下一个对角块，剩余矩阵更新为$\bm F-\bm M\bm C^\top$。它仍对称，只需算下三角部分；对更小的矩阵重复，直到剩余矩阵为空。

###### paragraph：三段求解

1. 由式`eq:ls-ldlt`把$\bm A\bm x=\bm b$改写为$\bm L\bm D\bm L^\top(\bm P\bm x)=\bm P\bm b$，先重排右端$\bm c=\bm P\bm b$，再用前代求解$\bm L\bm y=\bm c$；接着按$\bm D$的对角块逐个求解$\bm D\bm z=\bm y$，一阶块作标量除法，二阶块由二阶逆矩阵公式写出两个分量，分母因所选块可逆而非零；最后用回代求解$\bm L^\top\bm w=\bm z$，此时$\bm w=\bm P\bm x$，按$\bm x=\bm P^\top\bm w$恢复未知量原次序。

2. 算例`ex:ls-ldlt-two-by-two`取对角元全为零的三阶对称矩阵，按默认规则选出二阶块$\bm E=\left[\begin{smallmatrix}0&2\\2&0\end{smallmatrix}\right]$且无需置换，由$\bm M\bm E=\bm C$得$\bm M=(\tfrac12,\tfrac12)$，剩余一阶块为$-1$；再依次作前代、二阶块与一阶块求解和回代，得$\bm x=(1,1,1)^\top$并代回验证。

##### 12.2.3.3 算法分析

###### paragraph：正确性

1. 把一步块消元写成单位块下三角、块对角与单位块上三角三个因子之积，利用$\bm M\bm E=\bm C$与$\bm E^\top=\bm E$验证；两侧因子行列式为$1$、对称置换不改行列式，故每轮剩余矩阵都非奇异，非零对称矩阵总能选出可逆块，逐轮累积即得式`eq:ls-ldlt`，三段求解与还原次序因而给出原方程的解。负主元或不定二阶块只说明二次型有负方向，不妨碍求解。

###### paragraph：数值敏感度

1. 存在可逆主元不等于稳定，小主元块导致大乘子和元素增长；以Bunch--Kaufman策略为例说明实用选块须控制增长，它按当前对角元与所在列最大非对角元的相对大小决定取一阶块还是二阶块。

###### paragraph：计算代价

1. 稠密计算约$\tfrac13d^3$次运算、存储约$\tfrac12d^2$，利用对称性比LU减半。

#### 12.2.4 分块消元

##### 12.2.4.1 主要思想

1. 把非奇异的$\bm A$、$\bm b$和$\bm x$按两组未知量$\bm u,\bm v$分块，设左上块$\bm B\in\mathbb R^{p\times p}$可逆，指出分块只是输入的写法，目标仍是精确解。做法是用第一组方程把$\bm u$用$\bm v$表示，代入第二组消去$\bm u$，解只含$\bm v$的较小方程后再恢复$\bm u$。

##### 12.2.4.2 算法实现

###### paragraph：用$\bm B$的因子求解

1. 按$\bm B$的结构调用前面的LU、Cholesky或分块LDL得到其因子，已有分解时直接复用；再用这组因子解$\bm B\bm Z=\bm C$的各列和$\bm B\bm z=\bm f$，得到$\bm Z=\bm B^{-1}\bm C$与$\bm z=\bm B^{-1}\bm f$，计算时只做前代与回代，不形成$\bm B^{-1}$。

###### paragraph：形成Schur补方程

1. 由第一组方程得$\bm u=\bm z-\bm Z\bm v$，代入第二组得到式`eq:ls-schur-reduced-system`的约化方程$\bm S\bm v=\bm h$，并把$\bm S=\bm E-\bm D\bm B^{-1}\bm C$定义为关于被消块$\bm B$的Schur补。指出消去$\bm u$时系数和右端都要扣除经由$\bm u$传来的部分，所以$\bm S$与$\bm h$必须同时形成。

2. 图`fig:ls-block-elimination-schur`把这一步画成增广分块矩阵$[\bm A\mid\bm b]$的块行变换：第二块行减去$\bm D\bm B^{-1}$乘第一块行后，左下块变为零，右下块与右端换成$\bm S$与$\bm h$，剩下块上三角方程。

###### paragraph：求解$\bm S\bm v=\bm h$并恢复$\bm u$

1. 按$\bm S$的结构调用已有直接法解出$\bm v$；引用定理`thm:ls-schur-complement`说明$\bm A$与$\bm B$非奇异时$\bm S$也非奇异，这一步结果唯一。最后计算$\bm u=\bm z-\bm Z\bm v$，按原分组拼成$\bm x$，完成求解。

2. 算例`ex:ls-block-elimination-run`在二阶贯穿例$\bm A=\left[\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right]$、$\bm b=(1,2)^\top$上取$p=q=1$走完三步：$\bm Z=\bm z=\tfrac14$，$\bm S=\tfrac{11}4$、$\bm h=\tfrac74$，解得$v=\tfrac7{11}$、$u=\tfrac1{11}$并代回验证，同时由$\det\bm A=4\cdot\tfrac{11}4=11$预示随后定理的行列式公式。

##### 12.2.4.3 算法分析

###### paragraph：正确性

1. 按构造$(\bm u,\bm v)$满足第一组方程，而在$\bm u=\bm z-\bm Z\bm v$下第二组方程恰与$\bm S\bm v=\bm h$等价，故算法给出原方程的解；并引出把消元写成矩阵乘法还能读出可逆性、逆矩阵和正定性。

2. 定理`thm:ls-schur-complement`：$\bm B$可逆时$\det\bm A=\det\bm B\det\bm S$，$\bm A$可逆当且仅当$\bm S$可逆，此时逆矩阵由式`eq:matrix-analysis-block-inverse`给出；$\bm E$可逆时有对称的行列式公式；$\bm A$对称且$\bm B\succ0$时，式`eq:matrix-analysis-schur-positive-definite`给出$\bm A\succ0$与Schur补正定的等价。

3. 证明先把$\bm A$写成单位块下三角、$\operatorname{diag}(\bm B,\bm S)$与单位块上三角之积，取行列式得行列式公式与可逆性等价，三个因子分别求逆后反序相乘得逆矩阵；$\bm E$可逆时先消去$\bm v$得第二个公式。对称情形写成$\bm A=\bm G\operatorname{diag}(\bm B,\bm S)\bm G^\top$，二次型展开即对$\bm u$配方，由$\bm G^\top$可逆与$\bm B\succ0$推出正定性等价。

###### paragraph：数值敏感度

1. 误差来自用$\bm B$的因子求$\bm Z,\bm z$、形成$\bm S$时的相减以及约化方程求解三处；$\bm B$病态时$\bm Z,\bm z$的误差传入$\bm S,\bm h$，相当于块层面的小主元，应换一种分组。

###### paragraph：计算代价

1. $\bm B$稠密时各步合计与对整个$\bm A$作LU同为$(p+q)^3$量级，单纯改写为分块形式并不省事，节省须依赖被消块易于求解（如块对角，各小块可分别分解）或保留块较小。

#### 12.2.5 低秩更新下的求解

##### 12.2.5.1 主要思想

1. 设新系数矩阵为$\bm A=\bm A_0+\bm U\bm C\bm V^\top$，其中$\bm A_0$非奇异、$\bm U,\bm V\in\mathbb R^{d\times k}$、$k\ll d$，且$\bm A$非奇异，求新方程的精确解。更新表示是输入矩阵的结构信息，$\bm A_0$的分解只在内部复用；核心做法是把修改项的作用集中到$k$维辅助量$\bm C\bm V^\top\bm x$上，用旧矩阵求解若干次再解一个$k$阶小方程，避免重新分解$d$阶矩阵。

##### 12.2.5.2 算法实现

###### paragraph：用旧因子求解

1. 先取得$\bm A_0$的分解，通常可直接复用，尚无时按结构调用前面的方法；约定后面关于节省计算的比较以分解已存在为前提。用这组因子求解$\bm A_0\bm u=\bm b$得到未作更新时的解$\bm u$，再对$\bm U$的$k$列复用同一组因子求解$\bm A_0\bm Z=\bm U$，所得$\bm Z$记录修改方向经$\bm A_0^{-1}$作用后的结果。

###### paragraph：形成小系统

1. 形成$k$阶矩阵$\bm K=\bm I_k+\bm C\bm V^\top\bm Z$与向量$\bm h=\bm C\bm V^\top\bm u$，先算$\bm V^\top\bm Z$与$\bm V^\top\bm u$再左乘$\bm C$，全程不形成新的$d$阶矩阵。

###### paragraph：求解小系统并修正

1. 用已有直接法求解$\bm K\bm z=\bm h$，再计算$\bm x=\bm u-\bm Z\bm z$，得到新方程的解。

2. 算例`ex:ls-woodbury-rank-one`把二阶贯穿例写成$\bm A_0=\operatorname{diag}(3,2)$加秩一修改（$\bm U=\bm V=(1,1)^\top$、$\bm C=1$），对角$\bm A_0$的求解只需逐个相除，标量小系统$\bm K=\tfrac{11}6$、$\bm h=\tfrac43$给出$\bm z=\tfrac8{11}$，修正后得到与算例`ex:ls-block-elimination-run`相同的$\bm x=(\tfrac1{11},\tfrac7{11})^\top$，全程不分解$\bm A$本身。

##### 12.2.5.3 算法分析

###### paragraph：正确性

1. 令$\bm z=\bm C\bm V^\top\bm x$，把原方程化为$\bm x=\bm u-\bm Z\bm z$与$\bm K\bm z=\bm h$，并反向验证二者推出原方程，故小系统与原方程等价；指出把这一等价关系对任意右端写成矩阵形式即得可逆性判据与逆矩阵公式。

2. 定理`thm:ls-woodbury`：记$\bm K=\bm I_k+\bm C\bm V^\top\bm A_0^{-1}\bm U$，则$\det(\bm A_0+\bm U\bm C\bm V^\top)=\det\bm A_0\det\bm K$，新矩阵可逆当且仅当$\bm K$可逆；$\bm C$也可逆时成立式`eq:matrix-analysis-woodbury`的Woodbury恒等式。证明由$\bm A=\bm A_0(\bm I_d+\bm Z\bm C\bm V^\top)$，对一个辅助分块矩阵分别消去两个单位对角块，用定理`thm:ls-schur-complement`的两个行列式公式得行列式等式；再由$\bm K=\bm C(\bm C^{-1}+\bm V^\top\bm A_0^{-1}\bm U)$和上面的等价关系写出任意右端的解，去掉右端即得恒等式。

3. 指出判据部分允许$\bm C$奇异，这正是算法只用$\bm K$、不用$\bm C^{-1}$的原因。定理`thm:ls-sherman-morrison`给出最常见的秩一情形：$\bm A_0+\bm p\bm q^\top$可逆当且仅当$1+\bm q^\top\bm A_0^{-1}\bm p\neq0$，逆矩阵只含这一标量分母；证明在Woodbury恒等式中取$k=1$、$\bm C=1$直接代入。

###### paragraph：数值敏感度

1. 强调代数恒等式不自动保证数值稳定：$\bm K$近奇异时小系统求解放大误差，$\bm A_0$的求解本身敏感时$\bm u,\bm Z$的误差即使在$\bm A$良态时也会进入结果，$\bm u$与$\bm Z\bm z$大小相近时相减还会相消。

###### paragraph：计算代价

1. 已有因子时，$k+1$个右端的三角求解约$O(kd^2)$，形成$\bm V^\top\bm Z$约$O(k^2d)$，小系统约$O(k^3)$，合计$O(kd^2+k^2d+k^3)$；优势来自$k\ll d$，远少于重新分解的$\tfrac23d^3$。

#### 12.2.6 正规方程法

##### 12.2.6.1 主要思想

1. 转向超定最小二乘：输入满列秩的$\bm A\in\mathbb R^{m\times d}$（$m\geq d$）和$\bm b$，求唯一最小二乘解$\hat{\bm x}$。依据第`sec:ls-ordinary-ls`节已证的等价性，目标化为正规方程（式`eq:linear-algebra-normal-equations`）；满列秩时$\bm A^\top\bm A$对称正定，于是问题变成$d$阶正定方程，交给第`sec:ls-cholesky`节的Cholesky分解求解。

##### 12.2.6.2 算法实现

###### paragraph：形成Gram矩阵

1. 第一步形成Gram矩阵$\bm G=\bm A^\top\bm A$与右端$\bm c=\bm A^\top\bm b$：按行写开为各行贡献之和，从零开始逐行累加外积与$b_i\bm A_{i,:}^\top$，每读入一行即完成其贡献，不必同时保存所有观测行，且只需累加下三角部分。

###### paragraph：$\bm L\bm L^\top$分解

1. 用第`sec:ls-cholesky`节的逐列过程计算$\bm G=\bm L\bm L^\top$，并由$\bm z\neq\bm0$时$\bm A\bm z\neq\bm0$得$\bm z^\top\bm G\bm z=\lVert\bm A\bm z\rVert_2^2>0$，说明满列秩恰好保证所需的正定性。

###### paragraph：前代与回代

1. 先用第`sec:ls-lu`节的前代求解$\bm L\bm y=\bm c$，再用回代求解$\bm L^\top\hat{\bm x}=\bm y$得到最小二乘解，指出两次三角求解的次序来自$\bm L(\bm L^\top\hat{\bm x})=\bm c$，与用Cholesky解正定方程相同；这三步在直线拟合数据上的数值留到第`sec:ls-direct-method-comparison`节。

##### 12.2.6.3 算法分析

###### paragraph：正确性

1. 两次三角求解给出$\bm L\bm L^\top\hat{\bm x}=\bm c$，即正规方程，由定理`thm:ls-least-squares-solutions`知$\hat{\bm x}$是唯一最小二乘解。

###### paragraph：数值敏感度

1. 指出这条路线的代价在精度：对满列秩矩阵定义$\kappa_2(\bm A)=\sigma_{\max}/\sigma_{\min}$，方阵时与第`sec:ls-matrix-condition-number`节一致。

2. 定理`thm:ls-normal-equations-condition-squaring`陈述$\kappa_2(\bm A^\top\bm A)=\kappa_2(\bm A)^2$；证明由第`sec:ls-svd`节的SVD写出$\bm A^\top\bm A=\bm V\operatorname{diag}(\sigma_i^2)\bm V^\top$，这是对称正定矩阵的谱分解，最大、最小特征值为$\sigma_1^2$与$\sigma_d^2$。

3. 解释后果：$\bm A$强压缩的方向在$\bm G$中被压缩两次，形成$\bm G$的舍入可能抹掉这些方向上的信息，误差界随之带上$\kappa_2(\bm A)^2$（第`sec:ls-ls-regularization-sensitivity`节）。

###### paragraph：计算代价与适用范围

1. 形成Gram矩阵可能增加填充（一行全非零即使$\bm G$稠密）；稠密时形成$\bm G$约$md^2$次、分解约$d^3/3$次，总工作为$O(md^2+d^3)$。秩亏时正规方程仍刻画全部最小二乘解，但$\bm G$只半正定、Cholesky遇到零主元，前提不再成立，选解交给第`sec:ls-svd-solve`节的SVD路线。

#### 12.2.7 QR求解

1. 从正规方程法的精度损失来自形成$\bm A^\top\bm A$进入，说明QR求解改为直接对$\bm A$作正交三角化；先写清最小二乘与满行秩最小范数解的共同求解过程，再分别说明修正Gram--Schmidt、Householder反射与Givens旋转怎样计算因子。

##### 12.2.7.1 主要思想

1. 输入满列秩的$\bm A\in\mathbb R^{m\times d}$（$m\geq d$）和$\bm b$，求唯一最小二乘解$\hat{\bm x}$。正交变换保持欧氏长度，同时变换$\bm A$和$\bm b$不改变残差长度，因此找正交矩阵把$\bm A$化为上三角，最小二乘问题即变成三角方程，全程不形成$\bm A^\top\bm A$；因子计算留给后面三个小节。

##### 12.2.7.2 算法实现

###### paragraph：QR分解

1. 第一步由第`chap:normed-inner-product-spaces`章的薄QR分解（式`eq:ls-qr-factorization`）得$\bm A=\bm Q_1\bm R$，把$\bm Q_1$补成$\mathbb R^m$的标准正交基得到完整形式$\bm A=\bm Q\left[\begin{smallmatrix}\bm R\\\bm0\end{smallmatrix}\right]$，$\bm R$为$d$阶可逆上三角矩阵；实际计算由后面三种方法完成，反射和旋转只需记录变换。

###### paragraph：变换右端

1. 对右端施加同一正交变换，把$\bm Q^\top\bm b$分为前$d$个分量$\bm c_1$与其余部分$\bm c_2$；回代只需$\bm c_1=\bm Q_1^\top\bm b$，使用薄正交基时只算这一部分，修正Gram--Schmidt中的具体顺序见第`sec:ls-mgs`节。

###### paragraph：求解$\bm R\hat{\bm x}=\bm c_1$

1. 最后用回代求解$\bm R\hat{\bm x}=\bm c_1$，得到最小二乘解。

###### paragraph：欠定情形：转置QR

1. 转向欠定方程：设$\bm A$满行秩、$m<d$，目标改为第`sec:ls-select-among-solutions`节的最小范数精确解$\bm x_\star$；由于$\bm x_\star$应在$\operatorname{range}(\bm A^\top)$中，把分解用于$\bm A^\top$而非$\bm A$。计算薄QR分解$\bm A^\top=\bm Q\bm R$，$\bm Q\in\mathbb R^{d\times m}$列标准正交、$\bm R$为$m$阶可逆上三角，于是$\bm A=\bm R^\top\bm Q^\top$；用前代求解$\bm R^\top\bm y=\bm b$得到$\bm x_\star$在行空间基$\bm Q$下的坐标，再算$\bm x_\star=\bm Q\bm y$。与先解$\bm A\bm A^\top\bm z=\bm b$再取$\bm A^\top\bm z$相比，转置QR避免了形成Gram矩阵。

##### 12.2.7.3 算法分析

###### paragraph：正确性

1. 定理`thm:ls-qr-least-squares`把两个分支合写：满列秩时$\hat{\bm x}=\bm R^{-1}\bm c_1$是唯一最小二乘解、最小残差范数为$\lVert\bm c_2\rVert_2$；满行秩时$\bm x_\star=\bm Q\bm y$是唯一最小范数解。

2. 证明第一部分由正交变换保持长度得式`eq:ls-qr-residual-split`的残差分解：第二项$\lVert\bm c_2\rVert_2^2$与$\bm x$无关，$\bm R$可逆使第一项当且仅当$\bm x=\bm R^{-1}\bm c_1$时为零。第二部分验证$\bm A\bm x_\star=\bm R^\top\bm y=\bm b$且$\bm x_\star\in\operatorname{range}(\bm A^\top)=(\ker\bm A)^\perp$，其他解与它相差核中非零向量，由勾股关系范数更大。

###### paragraph：数值敏感度

1. 区分问题本身的敏感度（第`sec:ls-ls-regularization-sensitivity`节）与计算QR因子引入的误差，指出三种实现的稳定性不同，留待各自说明。

###### paragraph：秩亏情形

1. 秩亏时$\bm R$有零对角元，不能照搬回代，最小范数最小二乘解按第`sec:ls-svd-solve`节用SVD求。带列主元QR只取主元变量回代、其余坐标置零，一般得到基本解而非最小范数解，所以一般秩情形统一使用SVD路线。

##### 12.2.7.4 修正GS

1. 引入修正Gram--Schmidt：对满列秩$\bm A$，它与第`chap:normed-inner-product-spaces`章的Gram--Schmidt只差一处，即每次对当前剩余向量作投影、扣除后再算下一个投影，而不都用原始列算内积；所得QR因子用于同一$\bm A,\bm b$的最小二乘求解，输出仍为$\hat{\bm x}$。

###### paragraph：逐列正交化

1. 令$\bm R=\bm0$，按列处理：第$j$列令$\bm u=\bm a_j$，对$i=1,\ldots,j-1$依次计算$r_{i,j}=\bm q_i^\top\bm u$并扣除$r_{i,j}\bm q_i$，强调每次内积用的是刚更新的剩余向量。扣除全部旧方向后取$r_{j,j}=\lVert\bm u\rVert_2$、$\bm q_j=\bm u/r_{j,j}$，进入下一列；满列秩保证精确算术下$r_{j,j}>0$，全部完成后得到$\bm Q_1$与上三角$\bm R$。

###### paragraph：变换右端与回代

1. 把右端当作额外一列，令$\bm s=\bm b$，按同样的逐次投影顺序计算$c_i$并更新$\bm s$，得到$\bm c$；说明有限精度下$\bm Q_1$不完全正交，不宜改为另算$\bm Q_1^\top\bm b$。最后用回代求解$\bm R\hat{\bm x}=\bm c$并输出，$\bm Q_1$、$\bm R$和剩余向量都只是内部状态。

###### paragraph：正确性

1. 精确算术中各$\bm q_i$两两正交，对剩余向量与原始列算出的内积相同，故修正形式给出相同的QR分解，由定理`thm:ls-qr-least-squares`得到最小二乘解。

###### paragraph：数值正交性与计算代价

1. 有限精度下近相关列的剩余向量很短，舍入的相对影响被放大，$\bm q_j$偏离正交，必要时再正交化一遍；检查时分别用$\lVert\bm Q_1^\top\bm Q_1-\bm I\rVert$与$\lVert\bm A-\bm Q_1\bm R\rVert$衡量正交性与重构质量。主要工作约$2md^2$次运算。

##### 12.2.7.5 Householder

1. 说明Householder方法逐列用正交反射消去对角元下方元素、同时变换右端、最后回代。定义Householder反射$\bm H=\bm I-2\bm v\bm v^\top/(\bm v^\top\bm v)$，解释它是以$\bm v$为法向的超平面镜面反射，选好$\bm v$即可把当前列段反射到第一坐标轴；以下保持原列顺序。

2. 图`fig:ls-householder-reflection`取$\bm y=(2,1)^\top$与$\bm v=\bm y+\sqrt5\bm e_1$，画出反射超平面$\bm v^\perp$是$\bm y$与$\bm H\bm y=-\sqrt5\bm e_1$连线的垂直平分线，两者之差恰为$\bm v$，并以圆弧表示长度保持。

###### paragraph：构造反射向量

1. 令$\bm F=\bm A$、$\bm c=\bm b$，第$k$步取列段$\bm y=\bm F_{k:m,k}$，按$y_1$的符号取$s$，用式`eq:ls-householder`构造$\bm v$与$\bm H$；由后面的引理$\bm H\bm y=-s\lVert\bm y\rVert_2\bm e_1$，下方元素被消去，对照图中$\bm y$与其像关于$\bm v^\perp$对称；$\bm y=\bm0$时取恒等变换。

###### paragraph：作用于剩余子块

1. 把同一$\bm H$按一次内积加一次向量更新的方式作用于剩余子块各列和右端$\bm c_{k:m}$，不形成整个反射矩阵，恒等变换时跳过；按$k=1,\ldots,d$重复。

###### paragraph：回代

1. 最后取$\bm R=\bm F_{1:d,1:d}$，回代求解$\bm R\hat{\bm x}=\bm c_{1:d}$并输出。

2. 示例`ex:ls-householder-line-fit`在示例`ex:ls-line-least-squares`的直线拟合数据上演算：第一步$\bm v=(1+\sqrt3,1,1)^\top$把第一列化为$(-\sqrt3,0,0)^\top$，同步更新第二列与右端，并核对三个向量长度平方仍为$3,5,9$；第二步作用于后两行得$r_{2,2}=-\sqrt2$。回代得$\hat{\bm x}=(7/6,1/2)^\top$，$\lvert c_3\rvert=1/\sqrt6$为最小残差范数，$\bm R$与Cholesky因子$\bm L^\top$只差各行符号。

###### paragraph：正确性

1. 引理`lem:ls-householder-reflection`陈述$\bm y\neq\bm0$时$\bm H$对称正交且$\bm H\bm y=-s\lVert\bm y\rVert_2\bm e_1$；证明由$\bm H^2=\bm I$得正交性，由$s^2=1$、$sy_1=\lvert y_1\rvert$得$\bm v^\top\bm v=2\bm v^\top\bm y>0$，从而$\bm H\bm y=\bm y-\bm v$。

2. 每个$\bm H$嵌入$m$阶后只作用于第$k$至$m$行，前$k-1$列在这些行上已为零，故旧零结构保持，$d$步后得到取$\bm Q^\top=\bm H_d\cdots\bm H_1$的QR分解，由定理`thm:ls-qr-least-squares`回代所得即最小二乘解。

###### paragraph：数值稳定性与计算代价

1. 说明$s$与$y_1$同号可避免$\bm y$接近$\bm e_1$方向时的严重相消；Householder QR后向稳定（第`sec:ls-numerical-stability`节），工作约$2md^2-\tfrac23d^3$次运算；列主元可辅助辨认近相关列，但秩亏时的最小范数选择仍回到第`sec:ls-svd-solve`节。

##### 12.2.7.6 Givens

1. 输入满列秩$\bm A$与$\bm b$，求唯一最小二乘解。定义Givens旋转为两坐标平面内的旋转，每次只混合两行、消去一个指定元素，逐列三角化后回代；因只触及需消去的元素，适合下三角部分非零元很少的矩阵和新增观测行的情形。

2. 图`fig:ls-givens-householder-elimination`把两种初等正交消元并置：左侧Givens旋转沿圆弧把$(2,1)^\top$旋到$(\sqrt5,0)^\top$，右侧Householder反射沿角平分线把同一向量映到同一位置，对照旋转（行列式$+1$）与反射（对称正交）的区别，并注明图中反射取与式`eq:ls-householder`相反的符号。

###### paragraph：消元顺序

1. 令$\bm F=\bm A$、$\bm t=\bm b$（避免与旋转参数$c$混淆），按列处理，在第$k$列中按$i=m,\ldots,k+1$自下而上用相邻的第$i-1,i$两行消去$f_{i,k}$。

###### paragraph：构造旋转

1. $f_{i,k}=0$时跳过；否则由$\alpha=f_{i-1,k}$、$\beta=f_{i,k}$按式`eq:ls-givens`算出$\rho,c,s$与$\bm G$，使$\bm G(\alpha,\beta)^\top=(\rho,0)^\top$，并说明此处$s$与Householder中的符号无关；平方和可先按$\max(|\alpha|,|\beta|)$缩放以防上溢下溢，两分量全零已被跳过，不会除以零。

###### paragraph：旋转两行

1. 用同一$\bm G$左乘两行在第$k$列及以后的部分并同步变换$(t_{i-1},t_i)^\top$，强调两个新分量都由同一对旧值计算，第$k$列这两个元素变为$(\rho,0)^\top$；继续向上消元，完成后进入下一列。全部列完成后取$\bm R=\bm F_{1:d,1:d}$，回代求解$\bm R\hat{\bm x}=\bm t_{1:d}$并输出。

###### paragraph：新增观测行的更新

1. 用新增观测说明局部消元的好处：把新行$\bm w^\top$排在已有$\bm R$下方，依次与$\bm R$的第$1,\ldots,d$行旋转消去其各元素并同步旋转右端，得到更新后的$\bm R$与$\bm c_1$再回代；约需$3d^2$次运算且不需旧观测，而重新处理全部观测需$O(md^2)$。

2. 示例`ex:ls-givens-line-fit`在同一直线拟合数据上用增广列演算三次旋转：第一列先用第$2,3$行、再用第$1,2$行消元，第二列用第$2,3$行消元，逐次写出$\rho,c,s$与两行结果。所得$\bm R$恰为Cholesky因子$\bm L^\top$，回代得$\hat{\bm x}=(7/6,1/2)^\top$，$\lvert t_3\rvert=1/\sqrt6$为最小残差范数。

###### paragraph：正确性

1. 由$c^2+s^2=1$得$\bm G$正交，且旋转使$\alpha,\beta$变为$(\rho,0)$；前$k-1$列的零在旋转后保持，第$k$列内被消零的行不再被后续旋转改动，故结束时$\bm F$为上三角，$\bm t$是对$\bm b$施加同一串旋转的结果，由定理`thm:ls-qr-least-squares`回代所得即最小二乘解。

###### paragraph：数值稳定性与计算代价

1. Givens QR同样后向稳定（第`sec:ls-numerical-stability`节）；稠密时第$k$列需$m-k$次旋转，工作约$3md^2-d^3$次，约为Householder的$1.5$倍，带状、上Hessenberg或局部更新问题所需旋转少得多。由此总结：稠密一次性分解用Householder更省，局部结构与逐行更新用Givens更合适。

#### 12.2.8 SVD求解

1. 从秩亏或秩未知时正规方程与QR回代都不再适用进入，说明本小节以最小二乘解中的最小范数解为目标，先讲主要思想、算法实现与分析，再讨论加权与齐次最小二乘；SVD形式已在第`sec:ls-svd`节建立，这里只说明取得因子后怎样得到解。

##### 12.2.8.1 主要思想

1. SVD在输入端与输出端各给一组标准正交方向，在这两组坐标下$\bm A$只是把第$i$个输入坐标乘以$\sigma_i$送到第$i$个输出坐标；于是把可拟合的输出坐标除以正奇异值得到输入坐标，并令零空间方向坐标为零，得到范数最小的解。

2. 图`fig:ls-svd-solve-coordinates`以$m=4$、$d=3$、$r=2$示意这一坐标变换：右端变到左奇异坐标后，前$r$个坐标可拟合、其余留在残差中，可拟合坐标除以奇异值、零奇异方向取零，最后由右奇异向量还原为原变量。

##### 12.2.8.2 算法实现

1. 输入$\bm A\in\mathbb R^{m\times d}$与$\bm b$，不要求满秩，输出最小范数最小二乘解$\bm x_\star$，无额外超参数；按精确正奇异值描述，数值秩判定与截断分别见第`sec:ls-pseudoinverse-rank-change`节与第`sec:ls-tsvd-solve`节。

###### paragraph：计算SVD

1. 第一步调用数值SVD过程，按第`sec:ls-svd`节取得$\bm A=\bm U_r\bm\Sigma_r\bm V_r^\top$，$r=\operatorname{rank}\bm A$且各$\sigma_i>0$；$\bm A=\bm0$时直接取$\bm x_\star=\bm0$。

###### paragraph：投影右端

1. 计算$\bm c=\bm U_r^\top\bm b$，把右端投影到能够拟合的输出方向上，并指出$\bm b$在其余方向上的部分无论怎样选$\bm x$都留在残差中。

###### paragraph：按奇异值缩放

1. 对$i=1,\ldots,r$计算$z_i=c_i/\sigma_i$得到所需输入坐标，除法只对正奇异值进行。

###### paragraph：还原原变量

1. 最后计算$\bm x_\star=\bm V_r\bm z$，写成沿奇异方向的展开式并输出，只用到因子对向量的作用，无需形成完整伪逆。

2. 示例`ex:ls-svd-solve-rank-one`取不相容的秩一系统$\bm A=\left[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right]$、$\bm b=(1,3)^\top$，依次完成投影、缩放与还原得$\bm x_\star=(1,1)^\top$；再核对残差$(-1,1)^\top$与列空间正交、长度等于$\bm b$在$\bm u_2$上分量的绝对值，$\bm x_\star$与核方向正交，并在全部解$(1+t,1-t)^\top$中取$t=0$为范数最小者。

##### 12.2.8.3 算法分析

###### paragraph：正确性

1. 定理`thm:ls-svd-solve`陈述对任意$\bm A,\bm b$，上述输出$\bm x_\star=\bm A^\dagger\bm b$是唯一最小范数最小二乘解。证明由式`eq:matrix-analysis-pseudoinverse`把$\bm A^\dagger\bm b$写成相同的展开式，最优性引定理`thm:matrix-analysis-pseudoinverse-minimum-norm`；也可直接验证残差$\bm b-\bm U_r\bm U_r^\top\bm b$与列空间正交，且$\bm x_\star\in(\ker\bm A)^\perp$，由定理`thm:ls-minimum-norm-representative`得范数最小。

###### paragraph：数值敏感度

1. 敏感性来自除以小奇异值：固定$\bm A$且$r>0$时，右端扰动$\delta\bm b$使解改变$\sum_i(\bm u_i^\top\delta\bm b)\bm v_i/\sigma_i$，放大倍数至多为$1/\sigma_r$；为压低放大而截去真实正奇异值就改变了目标，属于第`sec:ls-tsvd-solve`节的截断SVD。

##### 12.2.8.4 加权最小二乘

1. 核心做法是把权矩阵写成$\bm M=\bm R^\top\bm R$，用同一$\bm R$变换$\bm A$和$\bm b$，再求普通最小二乘。输入$\bm A$、$\bm b$，超参数为对称正定权矩阵$\bm M$，规定目标$(\bm A\bm x-\bm b)^\top\bm M(\bm A\bm x-\bm b)$；输出加权最小二乘解中欧氏范数最小的代表$\bm x_\star$。

###### paragraph：构造权因子

1. 用第`sec:ls-cholesky`节作$\bm M=\bm L\bm L^\top$并取$\bm R=\bm L^\top$，对角权直接取$\bm R=\operatorname{diag}(\sqrt{w_i})$；若权以$\bm M=\bm C^{-1}$给出，则分解$\bm C=\bm L\bm L^\top$，取$\bm R=\bm L^{-1}$，其作用在下一步用前代实现。

###### paragraph：白化数据

1. 计算$\widetilde{\bm A}=\bm R\bm A$与$\widetilde{\bm b}=\bm R\bm b$；在$\bm M=\bm C^{-1}$形式下用前代求解$\bm L\widetilde{\bm A}=\bm A$与$\bm L\widetilde{\bm b}=\bm b$，不显式求逆。

###### paragraph：求解普通最小二乘

1. 对$(\widetilde{\bm A},\widetilde{\bm b})$调用上面的SVD求解过程得到$\bm x_\star$，满列秩时也可用第`sec:ls-qr-method`节的QR求解；变换只作用于观测端，未知量坐标未变，无须恢复。

2. 示例`ex:ls-weighted-whitening-solve`沿用示例`ex:linear-algebra-weighted-projection`的$\bm A=(1,1)^\top$、$\bm b=(2,1)^\top$、$\bm M=\operatorname{diag}(1,4)$：取$\bm R=\operatorname{diag}(1,2)$白化得$\widetilde{\bm A}=(1,2)^\top$、$\widetilde{\bm b}=(2,2)^\top$，用单列QR求得$x_\star=6/5$，与该示例中加权正规方程的解一致。

###### paragraph：正确性与数值敏感度

1. 由第`sec:ls-weighted-ls`节，变换前后目标函数逐点相等，未知量及其欧氏范数不变，故最优解集与最小范数代表相同（定理`thm:ls-weighted-least-squares`）。数值敏感度取决于$\widetilde{\bm A}=\bm R\bm A$，权重可能改善也可能恶化条件，应在变换后的系统上判断。

##### 12.2.8.5 齐次最小二乘

1. 核心做法是在$\lVert\bm x\rVert_2=1$约束下选择被$\bm A$伸缩得最小的方向。它是$\bm b=\bm0$的特例，只依赖$\bm A$，无额外超参数，输出使$\lVert\bm A\bm x\rVert_2$最小的单位向量$\hat{\bm x}$；单位长度约束属于求解目标，用于排除零解。

###### paragraph：计算完整右奇异基

1. 调用数值SVD过程取得第`sec:ls-svd`节的完整右因子$\bm V$，各列按伸缩量从大到小排列；$m<d$时多出的零空间方向伸缩量记为零也要保留，且方向直接从$\bm A$的SVD取得，不经显式形成$\bm A^\top\bm A$。

###### paragraph：取最小方向

1. 取$\hat{\bm x}=\bm v_d$输出，它已是单位向量；最小伸缩量重复时它只是最优子空间中的一个选择，$\pm\hat{\bm x}$表示同一组参数比例。

###### paragraph：正确性与数值敏感度

1. 正确性直接来自定理`thm:ls-homogeneous-minimizers`：单位球面上$\bm x^\top\bm A^\top\bm A\bm x$的最小值是最小特征值，由$\bm v_d$达到。方向敏感度由最小特征值与其余谱的间隙控制，用第`sec:ls-subspace-sensitivity`节的子空间扰动界估计，重根时不能保证方向唯一；单位长度与最优性的检验按第`sec:ls-least-squares-verification`节进行。

#### 12.2.9 直接求解的选择与核验

1. 回到第`sec:ls-solution-selection`节的求解目标汇总适用关系：精确解按非奇异、对称正定、对称不定分别用LU、Cholesky、分块LDL；最小二乘解满列秩用QR，条件数适中时也可用正规方程法，满行秩欠定方程的最小范数解用转置QR，一般秩用SVD。已知块结构时经Schur补方程求解（第`sec:ls-block-elimination`节），低秩修改时复用旧分解只多解一个小系统（第`sec:ls-woodbury`节），二者都只是复用已有求解步骤。

2. 沿用示例`ex:ls-line-least-squares`的直线拟合数据比较路线：正规方程法逐步给出$\bm G$、Cholesky因子、前代与回代结果$\hat{\bm x}=(7/6,1/2)^\top$，QR路线得到$\bm R=\bm L^\top$与$\bm c_1=\bm y$，两者解同一个三角方程。复制常数列后列空间与最优残差不变但秩降为$2$，正规方程与QR回代遇到零主元，SVD略去$\sigma_3=0$的方向得最小范数解$(7/12,1/2,7/12)^\top$；由此区分计算方式的差别与选解目标的差别。

3. 算出$\bm x$后代回检查：精确解查$\bm A\bm x=\bm b$，普通最小二乘查$\bm A^\top(\bm b-\bm A\bm x)=\bm0$，最小范数再查$\bm x\perp\ker\bm A$，并在上例中核对非零残差与两列正交、$\bm x_\star$与核方向正交。加权与齐次问题分别用第`sec:ls-least-squares-verification`节的加权正交条件和单位长度、最小特征方向条件；这些量只用于核对，各算法仍只返回$\bm x$。

4. 分解的重构误差与正交性可分别核对中间变换，但只是旁证，不属于算法本身。残差小不保证解误差小，接近奇异时小残差可对应大误差；条件数与前后向误差的解释见第`sec:ls-numerical-sensitivity`节，与迭代法的整体比较留到第`sec:ls-method-selection`节。


### 12.3 定常迭代法

1. 从直接法在大型稀疏矩阵上要存储分解因子、并因填充而代价过高进入，提出对可逆方阵$\bm A\in\mathbb R^{d\times d}$改用容易求解的矩阵近似$\bm A$、每轮按残差修正近似解的路线，每轮只需矩阵乘向量或一次三角求解。说明第`sec:ls-convergence`节已建立固定更新$\bm x\mapsto\bm T\bm x+\bm c$的收敛判据，本节据此选择修正规则，并先写共用的输入、超参数、内部状态和终止条件，再分述各方法的修正公式。

#### 12.3.1 矩阵分裂与定常迭代

##### 12.3.1.1 主要思想

1. 提出选固定、可逆且易求解的$\bm M$，解$\bm M\bm\delta_k=\bm r_k$把残差转成修正量，再令$\bm x_{k+1}=\bm x_k+\bm\delta_k$；用$\bm M=\bm A$一步得精确解但须解原方程的极端情形，说明近似$\bm M$以不完全准确换取便宜、靠反复修正逼近解。记$\bm N=\bm M-\bm A$得矩阵分裂$\bm A=\bm M-\bm N$，由两式都等于$\bm M\bm x_{k+1}=\bm M\bm x_k+\bm r_k$说明更新与$\bm M\bm x_{k+1}=\bm N\bm x_k+\bm b$等价；强调实际执行对$\bm M$的求解而不形成$\bm M^{-1}$，并以$\bm M$不随轮次变化解释“定常迭代”的名称。

##### 12.3.1.2 算法实现

###### paragraph：初始化

1. 规定输入为$\bm A,\bm b$、输出为近似解$\bm x$，单独列出超参数：初值$\bm x_0$、绝对与相对容差$\mathrm{atol},\mathrm{rtol}\geq0$、最大迭代次数$K$及各方法的固定参数。内部保存$\bm x_k,\bm r_k,\bm\delta_k$，初始化$\bm r_0=\bm b-\bm A\bm x_0$并令阈值$\tau=\mathrm{atol}+\mathrm{rtol}\lVert\bm b\rVert_2$。

###### paragraph：停止检查

1. 每轮开始先检查$\lVert\bm r_k\rVert_2\leq\tau$或$k=K$，满足时结束并取$\bm x=\bm x_k$，否则进入本轮修正。

###### paragraph：求修正量并更新

1. 求解$\bm M\bm\delta_k=\bm r_k$得本轮修正量，并说明这一步的算法随$\bm M$而变，具体公式留给后面各小节。

2. 得到修正量后更新$\bm x_{k+1}=\bm x_k+\bm\delta_k$，用更新后的解按原方程重算$\bm r_{k+1}=\bm b-\bm A\bm x_{k+1}$，计数加一后回到停止检查；说明后续各方法沿用这套状态与终止规则，只替换求$\bm\delta_k$的一步。

###### paragraph：矩阵记号与贯穿例

1. 为逐分量方法统一写$\bm A=\bm D+\bm L+\bm U$，其中$\bm L,\bm U$为保留原符号的严格下、上三角部分，并规定凡涉及对角除法都要求$a_{i,i}\neq0$，引出各方法共用的对照小例。

2. 例`ex:ls-stationary-running-example`取$\bm A=\begin{bmatrix}4&1\\1&3\end{bmatrix}$、$\bm b=(1,2)^\top$、$\bm x_0=\bm 0$，给出精确解$\bm x_\star=(1/11,7/11)^\top$和初始残差$\bm r_0=\bm b$；说明各方法只算第一轮，足以辨认更新方式的差别，不重复完整求解。

##### 12.3.1.3 算法分析

###### paragraph：收敛条件

1. 从各方法是否收敛取决于每轮把误差变成什么进入，令$\bm T=\bm I-\bm M^{-1}\bm A$、$\bm e_k=\bm x_k-\bm x_\star$，说明下面的定理把收敛归结为$\rho(\bm T)$，后面各小节只需分别估计各自的谱半径。

2. 定理`thm:ls-stationary-convergence`：设$\bm A,\bm M$可逆、$\bm x_\star$为解，则误差满足$\bm e_{k+1}=\bm T\bm e_k$、$\bm e_k=\bm T^k\bm e_0$，且对任意初值收敛到$\bm x_\star$当且仅当$\rho(\bm T)<1$。

3. 证明由$\bm r_k=-\bm A\bm e_k$推出误差递推并归纳；把更新写成仿射映射$\bm x\mapsto\bm T\bm x+\bm M^{-1}\bm b$，由$\bm I-\bm T=\bm M^{-1}\bm A$可逆得唯一固定点就是$\bm x_\star$，再据定理`thm:ls-affine-common-limit`得共同极限存在当且仅当$\rho(\bm T)<1$，且该极限只能是固定点。

4. 定理之后区分可执行与收敛两个条件：$a_{i,i}\neq0$只保证每轮能算下去，不保证$\rho(\bm T)<1$，反之亦然。

###### paragraph：收敛速度

1. 据定理`thm:ls-gelfand-formula`说明渐近速度由谱控制、误差缩小十倍约需$1/\log_{10}(1/\rho(\bm T))$轮，并据第`sec:ls-convergence-rate-transient`节指出非正规$\bm T$可能在衰减前暂时放大误差。

#### 12.3.2 Richardson迭代

##### 12.3.2.1 主要思想

1. 说明Richardson迭代把残差乘固定步长加到解上，以残差指出未满足的方程、朝减小残差方向修正；超参数为非零步长$\alpha$，对应$\bm M=\alpha^{-1}\bm I$，并指出方法只需计算$\bm A\bm v$、不必读取矩阵元素。

##### 12.3.2.2 算法实现

1. 内部状态沿用$\bm x_k,\bm r_k,\bm\delta_k$，每轮通过检查后计算$\bm\delta_k=\alpha\bm r_k$、$\bm x_{k+1}=\bm x_k+\bm\delta_k$、$\bm r_{k+1}=\bm b-\bm A\bm x_{k+1}$，再按第`sec:ls-matrix-splitting`节的条件决定停止；说明重算的残差兼作检查和下一轮修正，因而每轮只需一次矩阵乘向量。贯穿例取$\alpha=1/4$，第一轮得$\bm x_1=(1/4,1/2)^\top$。

##### 12.3.2.3 算法分析

###### paragraph：收敛条件与最优步长

1. 写出此时$\bm T=\bm I-\alpha\bm A$，并指出$\bm A$实对称正定时，由定理`thm:ls-stationary-convergence`，收敛条件与最优步长可从特征值直接读出，引出下面的定理。

2. 定理`thm:ls-richardson-spd`：设$\bm A$实对称正定、特征值在$[\lambda_{\min},\lambda_{\max}]$中且两端取到，则对所有初值收敛当且仅当$0<\alpha<2/\lambda_{\max}$，最优固定步长$\alpha_\star=2/(\lambda_{\min}+\lambda_{\max})$，收缩因子$\rho(\bm T)=(\kappa_2(\bm A)-1)/(\kappa_2(\bm A)+1)$。

3. 证明把误差按标准正交特征基展开，得每个系数乘以$1-\alpha\lambda_i$，故$\rho(\bm T)=\max_i|1-\alpha\lambda_i|$，由每个$\alpha\lambda_i\in(0,2)$得收敛区间；再由最大值在端点取得、两端随$\alpha$反向变化，令$1-\alpha\lambda_{\min}=\alpha\lambda_{\max}-1$解出$\alpha_\star$，代回并用$\kappa_2(\bm A)=\lambda_{\max}/\lambda_{\min}$得收缩因子。

###### paragraph：收敛速度与代价

1. 由定理指出谱范围越宽、$\kappa_2(\bm A)$越大，收缩因子越接近一、收敛越慢；每轮主要代价是一次矩阵乘向量，约$2\operatorname{nnz}(\bm A)$次运算。说明实际中谱端点未知，步长按已知谱界选取（如用$\lVert\bm A\rVert$作$\lambda_{\max}$的上界），并以贯穿例$\lambda_{\max}\approx4.618$核对$\alpha=1/4$在收敛区间内；残差与解误差的关系留到第`sec:ls-stationary-stopping`节。

#### 12.3.3 Jacobi迭代

##### 12.3.3.1 主要思想

1. 说明Jacobi迭代从第$i$个方程解出$x_i$、其余分量暂取旧值，相当于用对角矩阵近似$\bm A$、取$\bm M=\bm D$，并指出对角元相对非对角元越大，这一近似越好。

##### 12.3.3.2 算法实现

###### paragraph：逐分量修正

1. 给出每轮全部分量由同一旧状态$\bm x_k,\bm r_k$计算的公式$(\bm\delta_k)_i=(\bm r_k)_i/a_{i,i}$及等价的逐分量形式$(\bm x_{k+1})_i=\bigl(b_i-\sum_{j\neq i}a_{i,j}(\bm x_k)_j\bigr)/a_{i,i}$。

###### paragraph：整体替换

1. 强调右端求和只读旧向量、新分量写入另一向量，全部分量算完才替换并重算残差、检查终止；指出若算出一个分量就覆盖旧值，后面的行会读到本轮新值，便得到下一小节的Gauss--Seidel迭代。

###### paragraph：加权Jacobi

1. 说明加权Jacobi只增加固定超参数$\omega>0$，把修正改为$\bm\delta_k=\omega\bm D^{-1}\bm r_k$，其余流程不变，$\omega=1$恢复原方法。

2. 例`ex:ls-jacobi-first-sweep`在贯穿例上从$\bm r_0=(1,2)^\top$出发，两分量都用旧残差除以对角元，得$\bm x_1=(1/4,2/3)^\top$；整体替换后重算得$\bm r_1=(-2/3,-1/4)^\top$，范数由约$2.24$降到约$0.71$。由残差变负说明两个修正都过了头，原因是每个分量都假定另一分量不变，而另一分量同时也在变。

##### 12.3.3.3 算法分析

###### paragraph：收敛条件

1. 写出$\bm T_{\mathrm J}=-\bm D^{-1}(\bm L+\bm U)$，其第$i$行非对角元为$-a_{i,j}/a_{i,i}$，说明对角元压过同行其余元素时其行和范数小于一，引出常用充分条件。

2. 定理`thm:ls-jacobi-convergence`：若$\bm A$严格行对角占优，则$q=\lVert\bm T_{\mathrm J}\rVert_\infty=\max_i\sum_{j\neq i}|a_{i,j}|/|a_{i,i}|<1$，迭代对所有初值收敛且$\lVert\bm e_k\rVert_\infty\leq q^k\lVert\bm e_0\rVert_\infty$。证明由$\infty$-范数诱导的矩阵范数等于最大行绝对值和得$q<1$，再由定理`thm:ls-stationary-convergence`的$\bm e_k=\bm T_{\mathrm J}^k\bm e_0$和范数次乘性得几何速度界。

3. 定理后指出贯穿例中$q=1/3$，再用$\bm A=\bm I+2\bm 1\bm 1^\top\in\mathbb R^{3\times3}$说明对称正定不够：其特征值为$7,1,1$，而$\bm T_{\mathrm J}=-\tfrac23(\bm 1\bm 1^\top-\bm I)$沿$\bm 1$的特征值为$-4/3$，迭代发散。

###### paragraph：并行性与数值敏感度

1. 指出各分量更新互不依赖、可并行，一轮工作量与$\operatorname{nnz}(\bm A)$同阶；很小的对角元会把残差分量放大成很大的修正，也放大其中的舍入误差。

###### paragraph：加权Jacobi的步长范围

1. 对实对称正定$\bm A$的加权Jacobi，由$\bm D$对角元为正得$\bm I-\omega\bm D^{-1}\bm A$与对称的$\bm I-\omega\bm D^{-1/2}\bm A\bm D^{-1/2}$相似，借Richardson的同样论证得收敛当且仅当$0<\omega<2/\lambda_{\max}(\bm D^{-1/2}\bm A\bm D^{-1/2})$。以上例$\bm D^{-1/2}\bm A\bm D^{-1/2}=\bm A/3$、区间为$(0,6/7)$说明原方法的$\omega=1$未必落在区间内。

#### 12.3.4 Gauss--Seidel迭代

##### 12.3.4.1 主要思想

1. 从Jacobi未利用本轮已算出的前面分量进入，说明Gauss--Seidel迭代按顺序更新并立即使用本轮修正，取$\bm M=\bm D+\bm L$；新信息进入更早、修正通常更准确，代价是各行之间有了先后依赖。

##### 12.3.4.2 算法实现

###### paragraph：前代求修正量

1. 把变量顺序作为超参数固定为$1,\ldots,d$，每轮依次计算$(\bm\delta_k)_i=\bigl((\bm r_k)_i-\sum_{j<i}a_{i,j}(\bm\delta_k)_j\bigr)/a_{i,i}$；由第$i$个修正只用前$i-1$个修正，指出这正是用第`sec:ls-lu`节的前代求解$(\bm D+\bm L)\bm\delta_k=\bm r_k$。

###### paragraph：更新与原位覆盖

1. 完成修正后更新解、重算残差并检查终止；把$(\bm r_k)_i$的定义代入，得到下三角部分用本轮新值、上三角部分用旧值的逐坐标形式，说明实现时可在一个向量上原位覆盖。

2. 例`ex:ls-gauss-seidel-first-sweep`在贯穿例上先得$(\bm\delta_0)_1=1/4$，第二行扣掉刚得到的修正的影响得$(\bm\delta_0)_2=7/12$，于是$\bm x_1=(1/4,7/12)^\top$、$\bm r_1=(-7/12,0)^\top$。由第二个残差分量为零说明最后一次坐标修正恰使第二个方程成立，并与例`ex:ls-jacobi-first-sweep`的$(1/4,2/3)^\top$对照，差别正来自第二行用了新的第一分量。

##### 12.3.4.3 算法分析

###### paragraph：收敛条件

1. 写出$\bm T_{\mathrm{GS}}=-(\bm D+\bm L)^{-1}\bm U$，由定理`thm:ls-stationary-convergence`只需说明$\rho(\bm T_{\mathrm{GS}})<1$，引出两类常用的充分条件。

2. 定理`thm:ls-gauss-seidel-convergence`：若$\bm A$严格行对角占优，或实对称正定，则$\rho(\bm T_{\mathrm{GS}})<1$，迭代对所有初值收敛。

3. 证明对角占优情形：设$\bm T_{\mathrm{GS}}\bm v=\lambda\bm v$且$|\lambda|\geq1$，改写为$-\bm U\bm v=\lambda(\bm D+\bm L)\bm v$，取模最大的分量$v_i$，由第$i$行估计得$|a_{i,i}|\leq\sum_{j\neq i}|a_{i,j}|$，与对角占优矛盾。

4. 证明对称正定情形：引入$\phi(\bm x)=\tfrac12\bm x^\top\bm A\bm x-\bm b^\top\bm x$，其超出最小值的部分为$\tfrac12\bm e^\top\bm A\bm e$；沿第$i$个坐标取$t=r_i/a_{i,i}$使$\phi$减少$r_i^2/(2a_{i,i})\geq0$，一整轮不减少则残差为零，故$\bm A-\bm T_{\mathrm{GS}}^\top\bm A\bm T_{\mathrm{GS}}$正定。再借第`sec:ls-matrix-square-root`节的正定平方根构造$\bm C$，由定理`thm:matrix-analysis-rayleigh-ritz`取其最小特征值$\mu\in(0,1]$，得误差$\bm A$范数的统一收缩$\lVert\bm e_{k+1}\rVert_{\bm A}^2\leq(1-\mu)\lVert\bm e_k\rVert_{\bm A}^2$，从而$\rho(\bm T_{\mathrm{GS}})\leq\sqrt{1-\mu}<1$。

###### paragraph：收敛速度与代价

1. 指出速度取决于$\bm T_{\mathrm{GS}}$的谱，而重排变量会改变$\bm L,\bm U$的划分从而改变迭代矩阵；一轮是一次三角扫掠，工作量与$\operatorname{nnz}(\bm A)$同阶。以贯穿例$\rho(\bm T_{\mathrm{GS}})=1/12$小于$\rho(\bm T_{\mathrm J})=1/\sqrt{12}\approx0.289$作对照。

2. 借图`fig:ls-stationary-iteration-paths`解释这一差别：左图中Gauss--Seidel每个半步只改一个坐标并恰好落在对应方程的直线上，折线很快收拢到$\bm x_\star$，而Jacobi两个分量同时按旧值修正，在解的两侧来回跳动；右图半对数坐标中Richardson、Jacobi、SOR与Gauss--Seidel的误差大致沿直线下降，斜率对应各自的谱半径。

3. 最后说明新值复用带来顺序依赖，却不保证对所有矩阵都比Jacobi快，有的矩阵上Jacobi收敛而Gauss--Seidel发散。

#### 12.3.5 SOR迭代

##### 12.3.5.1 主要思想

1. 从Gauss--Seidel每次坐标修正恰使当前方程成立、修正幅度固定进入，说明SOR在每次坐标修正中乘固定松弛参数$\omega\neq0$：$\omega>1$放大修正以加快沿同一方向缓慢衰减的误差，$\omega<1$缩小修正以抑制过冲。

##### 12.3.5.2 算法实现

###### paragraph：松弛前代

1. 每轮按既定顺序求解$(\bm D+\omega\bm L)\bm\delta_k=\omega\bm r_k$，给出逐分量公式$(\bm\delta_k)_i=\tfrac{\omega}{a_{i,i}}\bigl((\bm r_k)_i-\sum_{j<i}a_{i,j}(\bm\delta_k)_j\bigr)$；指出当前分量用到的已是前面分量松弛后的修正，$\omega=1$恢复Gauss--Seidel。

###### paragraph：更新与检查

1. 随后令$\bm x_{k+1}=\bm x_k+\bm\delta_k$，重算残差并检查终止。

2. 例`ex:ls-sor-first-sweep`在贯穿例上取$\omega=6/5$，逐分量算得修正$3/10$与$17/25$，$\bm x_1=(3/10,17/25)^\top$、$\bm r_1=(-22/25,-17/50)^\top$；与例`ex:ls-gauss-seidel-first-sweep`对照，第二个方程因修正被放大五分之一而不再恰好成立。再与先做完整一轮Gauss--Seidel再按$\omega$加权所得的$(3/10,7/10)^\top$对比，说明SOR的松弛发生在每个坐标内部。

##### 12.3.5.3 算法分析

###### paragraph：收敛条件

1. 写出$\bm T_\omega=\bm I-\omega(\bm D+\omega\bm L)^{-1}\bm A=(\bm D+\omega\bm L)^{-1}[(1-\omega)\bm D-\omega\bm U]$，指出松弛参数的取值范围对一般矩阵有必要条件，对实对称正定矩阵恰好也是充分条件。

2. 定理`thm:ls-sor-convergence`：设$\bm A$对角元全不为零，则(1)对任意这样的方阵$\rho(\bm T_\omega)\geq|1-\omega|$，故对所有初值收敛的必要条件是$0<\omega<2$；(2)若$\bm A$实对称正定且$0<\omega<2$，则$\rho(\bm T_\omega)<1$，对所有初值收敛。

3. 证明第一部分由两个三角因子的行列式得$\det\bm T_\omega=(1-\omega)^d$，再由行列式为特征值之积、其模不超过$\rho(\bm T_\omega)^d$得下界，并据定理`thm:ls-stationary-convergence`排除$\omega\leq0$或$\omega\geq2$。第二部分把步长$t=\omega r_i/a_{i,i}$代入定理`thm:ls-gauss-seidel-convergence`证明中的能量变化式，得$\phi$减少$\omega(2-\omega)r_i^2/(2a_{i,i})$，在$0<\omega<2$时非负且仅在$r_i=0$时为零，此后沿用统一收缩论证。

###### paragraph：参数选择与代价

1. 指出速度取决于参数与排列，三对角等特殊结构有由$\rho(\bm T_{\mathrm J})$给出的最优参数公式但不能普遍套用（贯穿例$\omega=6/5$使谱半径由$1/12$升到$0.2$）；一轮成本与Gauss--Seidel同阶，$\omega$接近区间端点时收缩因子接近一、收敛可能很弱。

#### 12.3.6 SSOR迭代

##### 12.3.6.1 主要思想

1. 从单向扫掠依赖变量顺序、对应$\bm M$不对称进入，说明对实对称正定$\bm A$，SSOR把一次前向与一次反向SOR扫掠配成一轮，超参数取固定$0<\omega<2$，修正矩阵为$\bm M_{\mathrm{SSOR}}=\tfrac{1}{\omega(2-\omega)}(\bm D+\omega\bm L)\bm D^{-1}(\bm D+\omega\bm U)$；指出它对称正定，因而还能为第`sec:ls-krylov-iterations`节的方法提供预条件。

##### 12.3.6.2 算法实现

1. 说明内部状态除$\bm x_k,\bm r_k,\bm\delta_k$外只多一个本轮中间向量$\bm y_k$，并按$\bm M_{\mathrm{SSOR}}$的三个因子直接求修正量。

###### paragraph：前代求中间向量

1. 第一步用第`sec:ls-lu`节的前代求解$(\bm D+\omega\bm L)\bm y_k=\bm r_k$，得到中间向量$\bm y_k$。

###### paragraph：缩放后回代

1. 把中间向量按对角元缩放后，用回代求解$(\bm D+\omega\bm U)\bm\delta_k=\omega(2-\omega)\bm D\bm y_k$，并由依次代入说明所得$\bm\delta_k$正是$\bm M_{\mathrm{SSOR}}\bm\delta_k=\bm r_k$的解。

###### paragraph：更新与检查

1. 最后更新解、重算残差并检查终止。贯穿例取$\omega=1$，前代得$\bm y_0=(1/4,7/12)^\top$，缩放后右端为$(1,7/4)^\top$，回代先得第二分量$7/12$再得第一分量$5/48$，整轮得$\bm x_1=(5/48,7/12)^\top$。

##### 12.3.6.3 算法分析

###### paragraph：对称正定性与扫掠的等价

1. 由$\bm U=\bm L^\top$令$\bm F=(\bm D+\omega\bm L)\bm D^{-1/2}$，得$\bm M_{\mathrm{SSOR}}=\bm F\bm F^\top/(\omega(2-\omega))$对称正定；再把前向扫掠$\bm x_k+\omega(\bm D+\omega\bm L)^{-1}\bm r_k$与随后的反向扫掠合并，用$(\bm D+\omega\bm L)+(\bm D+\omega\bm U)-\omega\bm A=(2-\omega)\bm D$化简得$\bm M_{\mathrm{SSOR}}^{-1}\bm r_k$，说明按因子求解与两次逐坐标扫掠是同一个更新。

###### paragraph：收敛性与代价

1. 由两次扫掠的每一步都是SOR坐标修正、能量下降不依赖顺序，沿用定理`thm:ls-sor-convergence`第二部分的统一收缩论证得对所有初值收敛，速度由整轮误差矩阵$\bm I-\bm M_{\mathrm{SSOR}}^{-1}\bm A$的谱决定。最后指出每轮含两次扫掠、代价约为SOR两倍，比较时不能只数轮数，并说明这一对称正定因子可在第`sec:ls-preconditioning`节作预条件。

#### 12.3.7 收敛检验与停止准则

1. 回顾第`sec:ls-matrix-splitting`节的终止条件$\lVert\bm r_k\rVert_2\leq\mathrm{atol}+\mathrm{rtol}\lVert\bm b\rVert_2$或$k=K$，区分前者表示达到残差要求、后者只表示不再计算而未必达到精度，两种情况输出都只有当前$\bm x_k$。说明残差与修正量是内部计算量、不追加到输出，并以收缩因子接近一时步长很小可能只说明迭代很慢，指出$\lVert\bm\delta_k\rVert$很小不能代替原方程的残差检验。

2. 由$\bm x_\star-\bm x_k=\bm A^{-1}\bm r_k$说明误差是残差经$\bm A^{-1}$放大的结果，残差小与误差小之间隔着问题的敏感性，误差界与后向误差留到第`sec:ls-numerical-sensitivity`节。再规定比较方法时应在相同精度下比较总工作量而非轮数，收敛率与代价只用于解释算法、不加入输出；并指出用递推维护残差的其他方法会因舍入偏离真实残差，停止前须用$\bm b-\bm A\bm x_k$复核。


### 12.4 Krylov子空间法

1. 本节（第`sec:ls-krylov-iterations`节）从定常迭代用过即弃的残差出发，改为保留残差及其矩阵乘积张成的子空间，每轮在逐步扩大的子空间中重新选择近似。先研究非奇异方阵上的CG、Arnoldi与GMRES、MINRES、BiCG与BiCGSTAB，再经Golub--Kahan双对角化进入允许长方矩阵和秩亏的LSQR、LSMR，并逐一说明各方法对矩阵的要求与所最小化的量。由于每轮系数随当前向量变化，迭代不是同一线性映射的反复作用，第`sec:ls-convergence`节关于固定误差矩阵的判据不能直接套用；Arnoldi正交化与Golub--Kahan双对角化只作为求解器内部生成基的过程介绍。

#### 12.4.1 Krylov子空间

1. 设$\bm A\in\mathbb R^{d\times d}$，从初值$\bm x_0$算出残差$\bm r_0=\bm b-\bm A\bm x_0$作为修正方向的起点，反复乘$\bm A$定义第$k$个Krylov子空间$\mathcal K_k(\bm A,\bm r_0)=\operatorname{span}\{\bm r_0,\bm A\bm r_0,\ldots,\bm A^{k-1}\bm r_0\}$，并把第$k$步候选解限制在仿射集合$\bm x_0+\mathcal K_k$中。每个新向量由上一个向量再乘一次$\bm A$得到，扩大子空间只需一次矩阵乘向量，不必形成矩阵的幂。

2. 引理`lem:ls-krylov-residual-polynomial`：记$\mathcal P_k$为次数不超过$k$且$p(0)=1$的多项式集合，$\bm x_0+\mathcal K_k$中每个候选的残差都可写成式`eq:ls-krylov-residual-polynomial`即$\bm r_k=p_k(\bm A)\bm r_0$（$p_k\in\mathcal P_k$），反之每个$p_k\in\mathcal P_k$也对应一个候选。证明把$\bm x_k-\bm x_0$写成$q_{k-1}(\bm A)\bm r_0$代入残差得$p_k(t)=1-t\,q_{k-1}(t)$，反方向由$1-p_k(t)$在原点为零而可写成$t\,q_{k-1}(t)$。

3. 由引理，选候选解就是选残差多项式。多项式由方法按各自准则选择：CG使误差的$\bm A$范数最小，GMRES使原残差长度最小，BiCG通过左右两组方向的配对确定近似；因为多项式随步数整体改变而非固定更新矩阵的幂，收敛性须由各方法的选择准则推出，不能用谱半径判断。

4. 子空间嵌套增大$\mathcal K_k\subseteq\mathcal K_{k+1}$，使新一步能在更大候选集合中利用已有方向改进旧近似；但若$\bm A$有按模严格最大的特征值，幂向量$\bm A^j\bm r_0$的方向趋向相应特征向量，以它们为列的矩阵越来越病态，所以后面的方法要么显式正交化，要么利用矩阵结构得到有数学依据的短递推。精确算术下$\mathcal K_k$维数不超过$d$，不再扩张时即为$\bm A$的不变子空间，但某个方法能否有限步求得精确解，须结合其选解准则和前提判断，不能只由维数上限推出。

5. 对长方矩阵$\bm A\in\mathbb R^{m\times d}$，残差$\bm r_0\in\mathbb R^m$与未知量空间维数不同，$\bm A\bm r_0$没有意义。为此预告第`sec:ls-bidiagonal-iteration`节的Golub--Kahan双对角化：取零初值，在未知量空间生成$\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$的标准正交基并在数据空间生成配对基，计算时交替作用$\bm A$与$\bm A^\top$而不形成$\bm A^\top\bm A$。

#### 12.4.2 共轭梯度法

##### 12.4.2.1 主要思想

1. 设$\bm A=\bm A^\top\succ0$，正定性给出内积$\langle\bm u,\bm v\rangle_{\bm A}=\bm u^\top\bm A\bm v$及$\bm A$范数；误差无法直接计算，便借二次函数$\phi(\bm x)=\tfrac12\bm x^\top\bm A\bm x-\bm b^\top\bm x$，代入$\bm b=\bm A\bm x_\star$配方得$\phi(\bm x)-\phi(\bm x_\star)=\tfrac12\lVert\bm x-\bm x_\star\rVert_{\bm A}^2$，因此在任何候选集合上最小化$\phi$就是最小化误差的$\bm A$范数。再沿方向$\bm p$展开$\phi(\bm x+\alpha\bm p)$为$\alpha$的一元二次式，求得最小点$\alpha=\bm p^\top\bm r/(\bm p^\top\bm A\bm p)$，作为后面所用的步长。

2. 逐个方向一维最小化时，后一步可能破坏前一步的最优，于是共轭梯度法（CG）要求搜索方向两两$\bm A$共轭，使各方向对误差$\bm A$范数的贡献互不耦合，依次一维最小化就等于在全部方向张成的子空间上一次完成最小化。本段还指出关键的结构便利：新方向只需由新残差加上最近一个旧方向的倍数得到，与更早方向的共轭关系自动成立，因此每轮只保存固定数量的向量。

##### 12.4.2.2 算法实现

###### paragraph：输入与初始化

1. 说明输入为对称正定矩阵$\bm A$与右端$\bm b$，只需矩阵乘向量；超参数为$\bm x_0,\mathrm{atol},\mathrm{rtol},K$，输出为近似解$\bm x$。停止沿用第`sec:ls-stationary-stopping`节的公共准则，达到阈值或步数上限都输出当前近似；初始化$\bm r_0=\bm b-\bm A\bm x_0$、$\bm p_0=\bm r_0$，初值已满足准则或$K=0$时直接输出$\bm x_0$。

###### paragraph：沿当前方向更新

1. 第$k$轮先作唯一一次矩阵乘向量$\bm q_k=\bm A\bm p_k$，以$\alpha_k=\bm r_k^\top\bm r_k/(\bm p_k^\top\bm q_k)$更新$\bm x_{k+1}=\bm x_k+\alpha_k\bm p_k$与$\bm r_{k+1}=\bm r_k-\alpha_k\bm q_k$。分子用$\bm r_k^\top\bm r_k$代替主要思想中的$\bm p_k^\top\bm r_k$，两者在精确算术下相等（留待定理证明），前者可复用上一轮内积；正定性保证分母为正，残差借$\bm q_k$递推而不另乘$\bm A$。

###### paragraph：停止检验与新方向

1. 随后检验新残差，满足公共准则或$k+1=K$时输出$\bm x_{k+1}$，否则以$\beta_k=\bm r_{k+1}^\top\bm r_{k+1}/(\bm r_k^\top\bm r_k)$形成$\bm p_{k+1}=\bm r_{k+1}+\beta_k\bm p_k$进入下一轮。检验放在形成新方向之前，残差为零时先结束，不再计算组合系数。

2. 例`ex:ls-cg-two-steps`在贯穿例（例`ex:ls-stationary-running-example`，$\bm A$的行为$(4,1),(1,3)$，$\bm b=(1,2)^\top$，$\bm x_0=\bm 0$）上逐步执行两轮CG：第一轮$\alpha_0=1/4$得$\bm x_1=(1/4,1/2)^\top$、$\bm r_1=(-1/2,1/4)^\top$，由$\beta_0=1/16$得$\bm p_1$，并核对$\bm r_1\perp\bm r_0$、$\bm p_1^\top\bm A\bm p_0=0$；第二轮$\alpha_1=4/11$得$\bm x_2=(1/11,7/11)^\top=\bm x_\star$、零残差，两步即得精确解。对照取$\beta_k=0$的最速下降，第一步相同，此后在互相垂直的方向间折返，只能逐步逼近$\bm x_\star$。

3. 图`fig:ls-cg-steepest-descent-paths`把两条路径画在$\phi$经过最速下降迭代点的等值线上：两者共用第一步，CG的第二个方向与第一个方向$\bm A$共轭而直指椭圆中心，最速下降在$\bm x_\star$附近来回折返，右图放大其中的小框。

##### 12.4.2.3 算法分析

###### paragraph：正确性与收敛速度

1. 先交代论证路线：正确性归结为残差两两正交与方向两两共轭，由此推出最优性，再借残差多项式得到收敛速度。

2. 定理`thm:ls-cg-convergence`：设$\bm A$对称正定、精确算术且$\bm r_0,\ldots,\bm r_{k-1}$均非零，则残差两两正交、方向两两$\bm A$共轭，$\bm x_k$是$\lVert\bm x-\bm x_\star\rVert_{\bm A}$在$\bm x_0+\mathcal K_k$上的唯一最小点，并有$\lVert\bm x_k-\bm x_\star\rVert_{\bm A}\le2\bigl((\sqrt\kappa-1)/(\sqrt\kappa+1)\bigr)^k\lVert\bm x_0-\bm x_\star\rVert_{\bm A}$，其中$\kappa=\kappa_2(\bm A)$；CG至多$d$步得到精确解。

3. 证明第一段归纳建立正交与共轭关系，并保持两组向量都张成$\mathcal K_{k+1}$：由$\bm r_k\perp\bm p_{k-1}$得$\bm p_k^\top\bm r_k=\bm r_k^\top\bm r_k$（回收实现中分子替换的依据），步长使$\bm p_k^\top\bm r_{k+1}=0$，较早方向由共轭性给出正交，故$\bm r_{k+1}\perp\mathcal K_{k+1}$。对$i<k$利用$\bm A\bm p_i\in\mathcal K_{k+1}$得新方向与旧方向共轭，对$i=k$由$\bm A\bm p_k=(\bm r_k-\bm r_{k+1})/\alpha_k$说明$\beta_k$恰好抵消相应项；非零正交残差线性无关，从而张成关系推进到$\mathcal K_{k+2}$。

4. 证明第二段由$\bm A\bm e_k=-\bm r_k$与$\bm r_k\perp\mathcal K_k$展开$\lVert\bm e_k+\bm z\rVert_{\bm A}^2=\lVert\bm e_k\rVert_{\bm A}^2+\lVert\bm z\rVert_{\bm A}^2$（$\bm z\in\mathcal K_k$），得到$\bm x_k$是唯一最小点；又因$\mathbb R^d$中两两正交的非零向量至多$d$个，至多$d$步出现零残差。

5. 证明第三段按式`eq:ls-krylov-residual-polynomial`把候选误差写成$p(\bm A)\bm e_0$，用谱定理（定理`thm:ls-real-symmetric-spectral`）展开得$\lVert p(\bm A)\bm e_0\rVert_{\bm A}\le\max_i\lvert p(\lambda_i)\rvert\,\lVert\bm e_0\rVert_{\bm A}$，把问题化为多项式在特征值上的最大值。取Chebyshev多项式$T_k$，由三角定义得$[-1,1]$上$\lvert T_k\rvert\le1$，由共同递推得$x>1$时的显式表达，再经线性变换$\ell$把$[\lambda_{\min},\lambda_{\max}]$映到$[-1,1]$并归一化$p(t)=T_k(\ell(t))/T_k(\ell(0))$，计算$T_k(\ell(0))$的下界即得所述速度；$\kappa=1$时一步得解。

6. 解释结论的含义：界只依赖两端特征值，误差缩小到给定比例所需步数约与$\sqrt\kappa$成正比；它控制误差的$\bm A$范数，欧氏残差不必每步下降。

###### paragraph：数值敏感度

1. 浮点计算中正交与共轭关系逐步受损，定理的有限步结论不能直接移用，实际计算不承诺恰好$d$步结束；递推残差也会偏离真实残差，所以宣布达到要求前按公共准则用$\bm b-\bm A\bm x_k$复核。

###### paragraph：计算代价

1. 统计代价：每轮核心递推一次$\bm A$乘向量、两次内积和三次向量更新，除矩阵外只保存$\bm x,\bm r,\bm p,\bm q$四个向量，存储不随步数增长；复核真实残差的矩阵乘向量另计。

#### 12.4.3 Arnoldi正交化

##### 12.4.3.1 主要思想

1. 承接CG短递推依赖对称正定结构这一点，指出一般非对称方阵要在Krylov子空间中选解，先需可靠的基。Arnoldi正交化不对病态的幂向量正交化，而把第`sec:ls-qr-method`节的修正Gram--Schmidt用于最新基向量的像$\bm A\bm v_j$，扣除已有基向量上的分量后归一化得到下一个基向量，扣除系数记入一个小矩阵；它是GMRES的内部步骤，所得基与小矩阵不作为方程求解的输出。

##### 12.4.3.2 算法实现

###### paragraph：起始向量

1. 输入沿用GMRES的$\bm A,\bm b$与$\bm x_0$，生成步数由GMRES的重启长度与总步数上限限定。先算$\bm r_0=\bm b-\bm A\bm x_0$，已满足公共停止准则就不生成基，否则令$\beta=\lVert\bm r_0\rVert_2$、$\bm v_1=\bm r_0/\beta$。

###### paragraph：扣除已有分量

1. 第$j$轮作一次$\bm w=\bm A\bm v_j$，按$i=1,\ldots,j$依次以当前已扣除前面分量的$\bm w$计算$h_{i,j}=\bm v_i^\top\bm w$并更新$\bm w\leftarrow\bm w-h_{i,j}\bm v_i$。

###### paragraph：归一化与提前终止

1. 扣除完毕后令$h_{j+1,j}=\lVert\bm w\rVert_2$衡量$\bm A\bm v_j$中的新方向。该系数非零时归一化得$\bm v_{j+1}$进入下一轮；为零时不再归一化，把本轮系数交给GMRES完成当前小问题。

##### 12.4.3.3 算法分析

###### paragraph：正确性

1. 把扣除的分量加回得$\bm A\bm v_j=\sum_{i=1}^{j+1}h_{i,j}\bm v_i$，各轮合成矩阵即引出Arnoldi关系，并指向图`fig:ls-arnoldi-relation-shapes`所示的矩阵形状。

2. 定理`thm:ls-arnoldi-relation`：精确算术下执行$k$轮且前$k-1$轮$h_{j+1,j}$均非零，记$\bm V_k=[\bm v_1,\ldots,\bm v_k]$与$(k+1)\times k$上Hessenberg矩阵$\overline{\bm H}_k$。若$h_{k+1,k}\ne0$，则$\bm v_1,\ldots,\bm v_{k+1}$标准正交、前$j$个依次张成$\mathcal K_j$，并有式`eq:ls-arnoldi-relation`即$\bm A\bm V_k=\bm V_{k+1}\overline{\bm H}_k$；若$h_{k+1,k}=0$，则$\bm A\bm V_k=\bm V_k\bm H_k$，$\mathcal K_k$在$\bm A$下不变，$\bm A$非奇异时$\bm x_\star\in\bm x_0+\mathcal K_k$。

3. 证明中关系式逐列就是加回分量的等式；正交性归纳：每次扣除后$\bm w\perp\bm v_i$，后续扣除的方向都与$\bm v_i$正交，不破坏这一关系；又因$\bm A\bm v_j\in\mathcal K_{j+1}$而依次张成各Krylov子空间。$h_{k+1,k}=0$时$\bm A\mathcal K_k\subseteq\mathcal K_k$，非奇异的$\bm A$在其上是单射因而是满射，由$\bm r_0\in\mathcal K_k$得到$\bm A\bm z=\bm r_0$的解$\bm z\in\mathcal K_k$。

4. 图`fig:ls-arnoldi-relation-shapes`以$d=7$、$k=4$示意各矩阵形状：$\overline{\bm H}_k$的非零元只在主对角线、其上方与紧邻的下次对角线上，末行只剩$h_{k+1,k}$，并标出$\bm A\bm v_2$只用到$\bm v_1,\bm v_2,\bm v_3$。图后指出$d$维矩阵作用被压缩成一个小矩阵，GMRES与MINRES正在其上求解；子空间不再扩张时精确解已在候选集合中，GMRES此步得到精确解。

###### paragraph：数值敏感度与计算代价

1. 有限精度下的正交性损失沿用第`sec:ls-qr-method`节对修正Gram--Schmidt的讨论。每轮新增一次$\bm A$乘向量，第$j$轮投影约$4dj$次、$k$轮合计约$2dk^2$次浮点运算，保存$\bm V_{k+1}$约需$(k+1)d$个数，二者都随保留的向量数增长；本过程只负责生成候选空间，收敛快慢由后面的选解方法决定。

#### 12.4.4 广义最小残差法

##### 12.4.4.1 主要思想

1. 广义最小残差法（GMRES）在当前仿射Krylov空间中直接使原残差最小：以当前重启周期起点$\bm x^{(s)}$及其残差出发作Arnoldi，写$\bm x=\bm x^{(s)}+\bm V_j\bm y$，由$\bm r^{(s)}=\beta\bm V_{j+1}\bm e_1$与式`eq:ls-arnoldi-relation`得$\bm b-\bm A\bm x=\bm V_{j+1}(\beta\bm e_1-\overline{\bm H}_j\bm y)$。$\bm V_{j+1}$列标准正交不改变长度，于是$d$维最小化化为$(j+1)\times j$的小型最小二乘$\min_{\bm y}\lVert\beta\bm e_1-\overline{\bm H}_j\bm y\rVert_2$，用第`sec:ls-qr-method`节的Givens旋转化为上三角再回代；因$\overline{\bm H}_j$每列只在对角线下多一个非零元，每增一列只需一次新旋转，旧旋转可重复使用。

##### 12.4.4.2 算法实现

###### paragraph：输入与初始化

1. 输入为非奇异方阵$\bm A$与$\bm b$，超参数为$\bm x_0,\mathrm{atol},\mathrm{rtol},K$及重启长度$m$（$1\le m\le d$），输出为$\bm x$。初始化$\bm x^{(s)}=\bm x_0$及其残差，公共准则未满足时令$\beta=\lVert\bm r^{(s)}\rVert_2$、$\bm v_1=\bm r^{(s)}/\beta$，并置小问题右端$\bm g=(\beta,0,\ldots,0)^\top$。

###### paragraph：Arnoldi扩展

1. 每个内步先按第`sec:ls-arnoldi`节作一轮Arnoldi，扩充所存的基，得到$\overline{\bm H}_j$的新列$(h_{1,j},\ldots,h_{j+1,j})^\top$。

###### paragraph：旋转更新残差

1. 新列依次经过已保存的旋转$\bm G_1,\ldots,\bm G_{j-1}$，使整个矩阵对应同一正交变换；剩下第$j$、$j+1$行的元素$(a,h)$，由$\rho_j=\sqrt{a^2+h^2}$、$c_j=a/\rho_j$、$s_j=h/\rho_j$构造$\bm G_j$把它变为$(\rho_j,0)^\top$。同一旋转作用于右端得$g_j\leftarrow c_jg_j$、$g_{j+1}=-s_jg_j$，前面分量不变，旋转后前$j$行构成上三角$\bm R_j$，最小残差即$\lvert g_{j+1}\rvert$，不形成近似解就能判断是否停止。

###### paragraph：回代、恢复解与重启

1. 当$\lvert g_{j+1}\rvert$满足阈值、Arnoldi不再生成新方向、本周期达$m$步或总步数达$K$时结束内步，回代解$\bm R_j\bm y=(g_1,\ldots,g_j)^\top$并恢复$\bm x=\bm x^{(s)}+\bm V_j\bm y$。再用原矩阵计算真实残差按公共准则复核，满足或达总步数上限即输出，否则以该$\bm x$为新周期起点重新生成基；$h_{j+1,j}=0$时$s_j=0$且$g_{j+1}=0$，先完成小问题而不再用该系数作除法。

2. 例`ex:ls-gmres-two-steps`在同一贯穿例上取$m=2$执行两个内步：第一步得$h_{1,1}=4$、$h_{2,1}=1$与旋转$c_1=4/\sqrt{17}$、$s_1=1/\sqrt{17}$，残差估计$\lvert g_2\rvert=\sqrt{5/17}$；若此时停止，回代所得$\bm x_1=(4/17,8/17)^\top$的真实残差长度恰为该估计，并小于CG第一步的$\sqrt5/4$。第二步得$h_{1,2}=1$、$h_{2,2}=3$、$h_{3,2}=0$，二维空间用尽，新旋转$s_2=0$使$g_3=0$，回代$2\times2$上三角系统恢复出$\bm x_2=\bm x_\star$。

##### 12.4.4.3 算法分析

###### paragraph：正确性

1. 限定下面的定理针对不重启的完整GMRES，即$m=d$的情形。

2. 定理`thm:ls-gmres-optimality`：设$\bm A$非奇异、精确算术，完整GMRES第$k$步的$\bm x_k$是$\bm x_0+\mathcal K_k$中残差长度的唯一最小点，$\lVert\bm r_k\rVert_2=\lvert g_{k+1}\rvert$等于上一步残差长度乘以$\lvert s_k\rvert\le1$，因而不增，且至多$d$步得到精确解；若$\bm A=\bm X\bm\Lambda\bm X^{-1}$可对角化（可为复矩阵），还有$\lVert\bm r_k\rVert_2\le\kappa_2(\bm X)\min_{p\in\mathcal P_k}\max_{\lambda\in\sigma(\bm A)}\lvert p(\lambda)\rvert\,\lVert\bm r_0\rVert_2$，其中$\mathcal P_k$同引理`lem:ls-krylov-residual-polynomial`。

3. 证明先由$\bm V_k$满列秩与$\bm A$非奇异推出$\overline{\bm H}_k$满列秩，并用$\bm y\mapsto\bm x_0+\bm V_k\bm y$的双射及长度相等说明两个最小化问题的解一一对应；再以旋转之积$\bm\Omega_k$把目标分解为$\lVert(g_1,\ldots,g_k)^\top-\bm R_k\bm y\rVert_2^2+g_{k+1}^2$，$\bm R_k$可逆，回代解唯一使第一项为零，最小值为$\lvert g_{k+1}\rvert$，第$k$个旋转给出$\lvert g_{k+1}\rvert=\lvert s_k\rvert\,\lvert g_k\rvert$。$h_{k+1,k}=0$时$\bm H_k$可逆给出零残差，结合维数上限得至多$d$步；最后由引理`lem:ls-krylov-residual-polynomial`把残差写成$\min_{p\in\mathcal P_k}\lVert p(\bm A)\bm r_0\rVert_2$，借$p(\bm A)=\bm Xp(\bm\Lambda)\bm X^{-1}$与$\kappa_2(\bm X)$得到所述界。

###### paragraph：收敛速度

1. 解释这个界把收敛化为多项式逼近问题：找在原点取$1$、在全部特征值上都很小的低次多项式；非正规矩阵的$\kappa_2(\bm X)$可能很大，界因此变弱，只看特征值是否集中不能判断收敛快慢。

###### paragraph：重启与数值敏感度

1. 重启的GMRES($m$)丢弃历史空间，最优性只在一个周期内成立，可能停滞，也无$d$步精确解的保证；浮点下基不再精确正交，$\lvert g_{j+1}\rvert$与真实残差会偏离，这正是每个周期末用$\bm b-\bm A\bm x$复核的原因。

###### paragraph：计算代价

1. 统计代价：每个内步一次$\bm A$乘向量；完整GMRES执行$k$步时正交化约$2dk^2$次运算、存储约$kd$个数，随步数增长，GMRES($m$)每周期至多约$2dm^2$次运算、存储约$(m+1)d$个数，与总步数无关。

#### 12.4.5 最小残差法

##### 12.4.5.1 主要思想

1. 若$\bm A$对称，Arnoldi所得$\bm H_k=\bm V_k^\top\bm A\bm V_k$既对称又是上Hessenberg矩阵，因而是三对角矩阵，Arnoldi退化为每轮只扣除两个方向的Lanczos三项递推。最小残差法（MINRES）在这一递推上仍最小化当前Krylov空间中的欧氏残差，不要求正定而适用于对称不定矩阵；小问题的三角因子带宽固定，解也能用短递推更新，不必保存全部基。

##### 12.4.5.2 算法实现

###### paragraph：输入与初始化

1. 输入为实对称非奇异矩阵$\bm A$（允许不定）与$\bm b$，超参数为$\bm x_0,\mathrm{atol},\mathrm{rtol},K$，输出为$\bm x$。先算$\bm r_0$并按公共准则检查，未结束时令$\beta=\lVert\bm r_0\rVert_2$、$\bm v_1=\bm r_0/\beta$，并把$\bm v_0,\gamma_0,\bm d_{-1},\bm d_0$置零、$\bar g_1=\beta$，两个尚不存在的旧旋转置为$(1,0)$。

###### paragraph：Lanczos三项递推

1. 第$j$轮先作一步Lanczos递推：$\bm w=\bm A\bm v_j-\gamma_{j-1}\bm v_{j-1}$，算$a_j=\bm v_j^\top\bm w$并扣除，再令$\gamma_j=\lVert\bm w\rVert_2$，于是三对角矩阵第$j$列为位于第$j-1,j,j+1$行的$(\gamma_{j-1},a_j,\gamma_j)^\top$。

###### paragraph：旋转消元

1. 然后按GMRES的旋转约定处理这一列：第$j-2$个旋转作用于$(0,\gamma_{j-1})$得$\epsilon_j$与$\theta$，第$j-1$个旋转作用于$\theta$与$a_j$得$\delta_j$与$\bar\delta$，再由$\bar\delta$与$\gamma_j$构造消去$\gamma_j$的新旋转$(c_j,s_j)$及$\rho_j$。旋转后三角因子第$j$列只有$\epsilon_j,\delta_j,\rho_j$三个非零元，分别位于第$j-2,j-1,j$行。

###### paragraph：更新解与停止

1. 最后更新右端$g_j=c_j\bar g_j$、$\bar g_{j+1}=-s_j\bar g_j$，以$\bm d_j=(\bm v_j-\delta_j\bm d_{j-1}-\epsilon_j\bm d_{j-2})/\rho_j$更新方向，并令$\bm x_j=\bm x_{j-1}+g_j\bm d_j$。$\lvert\bar g_{j+1}\rvert$作为残差长度的内部估计用于公共准则判断；$\gamma_j=0$时完成本轮解更新即结束，未结束才归一化得$\bm v_{j+1}$，非奇异条件保证正常步骤中$\rho_j>0$。

##### 12.4.5.3 算法分析

###### paragraph：正确性

1. 先说明MINRES是GMRES在对称矩阵上的短递推实现，因而保留GMRES的最小残差性。

2. 定理`thm:ls-minres-optimality`：设$\bm A$实对称非奇异、精确算术且$\gamma_1,\ldots,\gamma_{k-1}$均非零，则MINRES第$k$步的$\bm x_k$与完整GMRES的第$k$个近似相同，是残差长度在$\bm x_0+\mathcal K_k$上的唯一最小点；$\lVert\bm r_k\rVert_2=\lvert\bar g_{k+1}\rvert$随$k$不增，至多$d$步得到精确解，并有不含$\kappa_2(\bm X)$因子的界$\lVert\bm r_k\rVert_2\le\min_{p\in\mathcal P_k}\max_{\lambda\in\sigma(\bm A)}\lvert p(\lambda)\rvert\,\lVert\bm r_0\rVert_2$。

3. 证明由式`eq:ls-arnoldi-relation`与基的标准正交性得$\bm H_k=\bm V_k^\top\bm A\bm V_k$，对称时上Hessenberg矩阵上下各只剩一条次对角线，故为三对角且$h_{j-1,j}=h_{j,j-1}=\gamma_{j-1}$，Arnoldi投影只剩Lanczos的两项，所施旋转正是GMRES的旋转，上三角因子$\bm R_k$上带宽为$2$。令$\bm D_k\bm R_k=\bm V_k$，比较第$j$列即得方向递推；GMRES的解$\bm x_0+\bm V_k\bm R_k^{-1}(g_1,\ldots,g_k)^\top$等于$\bm x_0+\bm D_k(g_1,\ldots,g_k)^\top$，而右端已定分量不再改变，所以每步只需加上$g_k\bm d_k$。其余结论由定理`thm:ls-gmres-optimality`得到，对称矩阵可取正交特征向量矩阵使$\kappa_2(\bm X)=1$。

###### paragraph：收敛速度

1. 界中只剩特征值，收敛快慢完全由谱决定。不定时特征值分布在原点两侧，而多项式在原点须取$1$，同时压低两侧比只压低一侧更难。

###### paragraph：数值敏感度与计算代价

1. 浮点下Lanczos向量失去正交性，残差估计须用真实残差复核，本节不扩展到奇异对称系统与MINRES-QLP。每轮一次$\bm A$乘向量，只保存$\bm v_{j-1},\bm v_j,\bm w,\bm d_{j-2},\bm d_{j-1},\bm x$等固定数量的向量；若为保持正交性作完整再正交化，就须保存全部基，存储随步数增长。

#### 12.4.6 双共轭梯度法

##### 12.4.6.1 主要思想

1. 承接Arnoldi在非对称矩阵上须对全部旧基投影、代价随步数增长的问题，双共轭梯度法（BiCG）放弃残差最小化，改用$\bm A$与$\bm A^\top$同时生成位于$\mathcal K_k(\bm A,\bm r_0)$的原序列和位于$\mathcal K_k(\bm A^\top,\widetilde{\bm r}_0)$的影子序列。它不要求原残差彼此正交，而要求原残差与影子残差双正交；这一条件只用相邻两项的递推就能维持，形式与CG相同，但不需要CG的正定误差内积。

##### 12.4.6.2 算法实现

###### paragraph：输入与初始化

1. 输入为实非奇异方阵$\bm A$与$\bm b$，需要$\bm A$与$\bm A^\top$乘向量；超参数为$\bm x_0,\mathrm{atol},\mathrm{rtol},K$及影子初值$\widetilde{\bm r}_0$，输出为$\bm x$。按公共准则检查初始残差后，选取满足$\widetilde{\bm r}_0^\top\bm r_0\ne0$的影子初值（默认$\widetilde{\bm r}_0=\bm r_0$），并取$\bm p_0=\bm r_0$、$\widetilde{\bm p}_0=\widetilde{\bm r}_0$、$\rho_0=\widetilde{\bm r}_0^\top\bm r_0$。

###### paragraph：两个序列同步更新

1. 第$k$轮先算$\bm q_k=\bm A\bm p_k$与$\widetilde{\bm q}_k=\bm A^\top\widetilde{\bm p}_k$，再以$\alpha_k=\rho_k/(\widetilde{\bm p}_k^\top\bm q_k)$同时更新解、原残差与影子残差。

###### paragraph：停止检验与新方向

1. 随后按公共准则检验原残差与步数上限，未结束时算$\rho_{k+1}=\widetilde{\bm r}_{k+1}^\top\bm r_{k+1}$与$\beta_k=\rho_{k+1}/\rho_k$，并同时更新原方向与影子方向。这些公式要求配对分母$\rho_k$与$\widetilde{\bm p}_k^\top\bm A\bm p_k$非零：零残差先由停止检验结束，残差非零而配对量为零时递推中断，不再相除，也不能当作收敛。

##### 12.4.6.3 算法分析

###### paragraph：正确性

1. 先说明BiCG选取近似的依据是双正交关系，证明沿用CG的归纳，只把每个内积的左因子换成影子序列。

2. 定理`thm:ls-bicg-biorthogonality`：设精确算术下BiCG执行到第$k$步，此前的$\rho_0,\ldots,\rho_k$与$\widetilde{\bm p}_i^\top\bm A\bm p_i$（$i<k$）均非零，则对$i\ne j$有$\widetilde{\bm r}_i^\top\bm r_j=0$与$\widetilde{\bm p}_i^\top\bm A\bm p_j=0$，并且$\bm r_k\perp\mathcal K_k(\bm A^\top,\widetilde{\bm r}_0)$，正是这个正交条件确定BiCG在$\bm x_0+\mathcal K_k$中的近似。

3. 证明第一段由方向与残差张成同一空间得$\widetilde{\bm p}_k^\top\bm r_k=\rho_k$，步长使$\widetilde{\bm p}_k^\top\bm r_{k+1}=0$，较早影子方向由配对共轭给出正交，于是新原残差与全部旧影子残差正交，互换两个序列的角色得影子残差的对应结论。

4. 证明第二段处理共轭：CG中“$\bm A\bm p_i$落在较小Krylov空间”一步，这里由$\bm A^\top\widetilde{\bm p}_i=(\widetilde{\bm r}_i-\widetilde{\bm r}_{i+1})/\alpha_i$承担，得$i<k$时新方向与旧影子方向配对正交，$i=k$时$\beta_k$恰好抵消相应项，另一侧同理。最后由$\rho_i\ne0$与双正交性推出$\widetilde{\bm r}_0,\ldots,\widetilde{\bm r}_{k-1}$线性无关，从而张成$\mathcal K_k(\bm A^\top,\widetilde{\bm r}_0)$，$\bm r_k$与之正交。

###### paragraph：收敛性与数值敏感度

1. 指出该条件不是任何范数的最小化，BiCG没有CG或GMRES那样的单调最小性，一般也不存在只靠$\kappa_2(\bm A)$就能承诺的统一下降速度。配对量很小时除法放大舍入误差，残差可能剧烈振荡，配对量为零时递推中断；本节保留这一限制，不展开中断的分类与修补策略。每轮一次$\bm A$乘向量和一次$\bm A^\top$乘向量，工作向量数量固定。

#### 12.4.7 稳定化双共轭梯度法

##### 12.4.7.1 主要思想

1. 针对BiCG每轮需要$\bm A^\top$且残差可能剧烈振荡，稳定化双共轭梯度法（BiCGSTAB）只用一个固定影子向量$\widehat{\bm r}$计算BiCG型配对系数，不再生成影子序列。每轮先沿BiCG型方向走一步得到中间残差，再沿$\bm A$作用于中间残差的方向作一次一元最小化压低残差，因此每轮只需要$\bm A$的作用。

##### 12.4.7.2 算法实现

###### paragraph：输入与初始化

1. 输入为实非奇异方阵$\bm A$与$\bm b$，超参数为$\bm x_0,\mathrm{atol},\mathrm{rtol},K$及固定影子向量$\widehat{\bm r}$，输出为$\bm x$，写法参照Barrett等人的模板文献。按公共准则检查初始残差后，取满足$\widehat{\bm r}^\top\bm r_0\ne0$的影子向量，默认$\widehat{\bm r}=\bm r_0$。

###### paragraph：形成搜索方向

1. 第$k$轮先算$\rho_k=\widehat{\bm r}^\top\bm r_k$再形成搜索方向：首轮取$\bm p_0=\bm r_0$，以后由$\beta_k=(\rho_k/\rho_{k-1})(\alpha_{k-1}/\omega_{k-1})$与$\bm p_k=\bm r_k+\beta_k(\bm p_{k-1}-\omega_{k-1}\bm v_{k-1})$得到。

###### paragraph：BiCG半步

1. 第一个半步计算$\bm v_k=\bm A\bm p_k$、$\alpha_k=\rho_k/(\widehat{\bm r}^\top\bm v_k)$与$\bm s_k=\bm r_k-\alpha_k\bm v_k$，其中$\bm s_k$是中间近似$\bm x_k+\alpha_k\bm p_k$的残差。先用它检验中间近似，满足公共准则就直接输出中间近似，不再走第二个半步。

###### paragraph：残差最小化半步

1. 未结束时第二个半步计算$\bm t_k=\bm A\bm s_k$与$\omega_k=\bm t_k^\top\bm s_k/(\bm t_k^\top\bm t_k)$，更新$\bm x_{k+1}=\bm x_k+\alpha_k\bm p_k+\omega_k\bm s_k$与$\bm r_{k+1}=\bm s_k-\omega_k\bm t_k$，再按公共准则终止或进入下一轮。配对分母$\rho_k$、$\widehat{\bm r}^\top\bm v_k$及下一轮要除的$\omega_k$都须非零；中间残差为零已由前面的检验结束，避免在已得解时计算$0/0$，其余中断情形不展开。

2. 例`ex:ls-bicgstab-one-step`在同一贯穿例上取$\widehat{\bm r}=\bm r_0$执行一轮：第一个半步与CG第一步相同，得中间近似$(1/4,1/2)^\top$与$\lVert\bm s_0\rVert_2=\sqrt5/4$；第二个半步由$\bm t_0=\bm A\bm s_0$算得$\omega_0=3/10$，得$\bm x_1=(1/10,23/40)^\top$、$\bm r_1=(1/40,7/40)^\top$，并以$\bm b-\bm A\bm x_1$核对递推残差，残差长度约$0.177$，比中间残差小约三分之二。

##### 12.4.7.3 算法分析

###### paragraph：第二个半步的作用

1. 展开$\lVert\bm s_k-\omega\bm t_k\rVert_2^2$为$\omega$的一元二次式，说明第二个半步的系数$\omega_k$正是其最小点，最小值给出$\lVert\bm r_{k+1}\rVert_2\le\lVert\bm s_k\rVert_2$。这只是相对中间残差的局部改进：第一个半步可能使$\lVert\bm s_k\rVert_2$大于$\lVert\bm r_k\rVert_2$，因而不保证残差逐轮下降，也不保证在所有非奇异系统上收敛；收敛快慢取决于实际形成的残差多项式。

###### paragraph：数值敏感度与计算代价

1. 影子配对量或$\omega_k$很小时后续系数对舍入敏感，仍按公共准则复核原残差。完整一轮通常需要两次$\bm A$乘向量，使用固定数量的工作向量；在中间阶段终止时只需第一个半步的一次乘法。

#### 12.4.8 Golub--Kahan双对角化

##### 12.4.8.1 主要思想

1. 从一般长方矩阵$\bm A\in\mathbb R^{m\times d}$的残差与未知量分属不同空间、不能反复乘$\bm A$入手，指出须用$\bm A^\top$把数据空间的向量送回未知量空间。Golub--Kahan双对角化因此交替作用$\bm A$与$\bm A^\top$，在两个空间各建一组配对的标准正交基，使$\bm A$只剩下双对角系数，长方问题压缩为下双对角小问题；它是LSQR与LSMR共用的内部过程，基与系数只作中间状态，不作为输出。

##### 12.4.8.2 算法实现

###### paragraph：起步

1. 沿用输入$\bm A,\bm b$，固定零初值$\bm x_0=\bm0$作为选出最小范数解的约定，步数由求解器的上限$K$控制。起步先处理右端：$\bm b=\bm0$时直接输出零解；否则令$\beta_1=\lVert\bm b\rVert_2$、$\bm u_1=\bm b/\beta_1$、$\bm q=\bm A^\top\bm u_1$、$\alpha_1=\lVert\bm q\rVert_2$，若$\alpha_1=0$则零向量已满足正规方程式`eq:linear-algebra-normal-equations`而直接输出，其余情况令$\bm v_1=\bm q/\alpha_1$。

###### paragraph：交替扩展两组基

1. 第$k$轮先把$\bm v_k$送到数据空间，减去在$\bm u_k$上的分量得$\bm p=\bm A\bm v_k-\alpha_k\bm u_k$、$\beta_{k+1}=\lVert\bm p\rVert_2$，再把$\bm u_{k+1}$送回未知量空间得$\bm q=\bm A^\top\bm u_{k+1}-\beta_{k+1}\bm v_k$、$\alpha_{k+1}=\lVert\bm q\rVert_2$，非零时分别归一化。说明减去的系数正是已算出的$\alpha_k,\beta_{k+1}$，无需另算内积，两次归一化所得长度就是新的双对角系数。

###### paragraph：零系数的处理

1. 规定零系数的处理：$\beta_{k+1}=0$时约定$\alpha_{k+1}=0$并停止生成，$\beta_{k+1}>0$而$\alpha_{k+1}=0$时不生成$\bm v_{k+1}$。两种情况都把本轮已得系数交给LSQR或LSMR完成旋转与解更新后再结束，不在当前小问题解完之前提前返回。

2. 示例`ex:ls-golub-kahan-line`沿用示例`ex:ls-line-least-squares`的直线拟合数据，逐步算出$\beta_1=3$、$\alpha_1=\sqrt{61}/3$、$\bm v_1=(5,6)^\top/\sqrt{61}$，再经两轮得到$\beta_2,\alpha_2,\beta_3$及$\bm u_2,\bm u_3,\bm v_2$，第二轮出现$\alpha_3=0$，说明二维未知量空间已被$\bm v_1,\bm v_2$取尽而停止生成，正好演示零系数的处理。最后核对$\bm u_i$两两正交，并由$\bm A=\bm U_3\bm B_2\bm V_2^\top$得$\bm B_2^\top\bm B_2$与$\bm A^\top\bm A$的迹$8$、行列式$6$相同，用系数平方和与乘积组合数值验证。

##### 12.4.8.3 算法分析

###### paragraph：正确性

1. 把前$k$轮系数排成$(k+1)\times k$下双对角矩阵$\bm B_k$（主对角$\alpha_1,\ldots,\alpha_k$，次对角$\beta_2,\ldots,\beta_{k+1}$），并记$\bm U_{k+1},\bm V_k$为两组基，引出下面把短递推整理为矩阵关系的定理。

2. 定理`thm:ls-golub-kahan-relations`在$\alpha_i,\beta_{i+1}$都为正的条件下断言：精确算术中$\bm U_{k+1},\bm V_k$的列分别标准正交，满足式`eq:ls-golub-kahan-relations`的两式$\bm A\bm V_k=\bm U_{k+1}\bm B_k$与$\bm A^\top\bm U_{k+1}=\bm V_k\bm B_k^\top+\alpha_{k+1}\bm v_{k+1}\bm e_{k+1}^\top$，且$\operatorname{range}(\bm V_k)=\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$。

3. 证明先由$\bm p,\bm q$的定义写出两个列关系，即式`eq:ls-golub-kahan-relations`的各列；再对$k$归纳，利用列关系与已有正交性推出$\bm u_{k+1}$与$\bm v_{k+1}$分别和此前的基正交。最后由$\bm v_1\parallel\bm A^\top\bm b$及$\bm v_{i+1}$由$\bm A^\top\bm A\bm v_i$减去旧方向组合得到，归纳得$\bm v_i$落在Krylov空间中，再比较维数得两者相等。

4. 据此说明零初值下双对角化生成的正是第`sec:ls-krylov-subspaces`节的长方矩阵Krylov空间，而从不形成$\bm A^\top\bm A$；终止时略去未生成的基向量及其零系数，两式仍成立。

5. 图`fig:ls-golub-kahan-bidiagonal`以$k=3$把递推与矩阵关系并列：(a)中进出$\bm v_i$的两支箭头给出$\alpha_i$与$\beta_{i+1}$，对应(b)中$\bm B_3$的第$i$列；每个新向量只与对面空间中相邻的一个向量相连，说明每步只需扣除一项。

###### paragraph：数值稳定性

1. 浮点运算中正交性所依赖的相消只近似成立，短递推也不去掉舍入引入的旧方向分量，两组基会逐渐失去正交性；其对结果的影响交给两种求解器，由第`sec:ls-krylov-stopping`节的真实残差复核控制。

###### paragraph：计算代价

1. 每轮至多一次$\bm A$乘向量和一次$\bm A^\top$乘向量，外加两次向量更新、两次范数和两次缩放；只用当前$\bm u_k,\bm v_k$、不保存整组基、不作完整再正交化时工作存储为$O(m+d)$。双对角化只负责生成候选空间，收敛快慢取决于下一步在子空间中如何选取近似解，由此过渡到两种求解器。

#### 12.4.9 LSQR算法

##### 12.4.9.1 主要思想

1. 交代LSQR出自Paige与Saunders，其做法是在$\operatorname{range}(\bm V_k)$中直接最小化原残差。令$\bm x=\bm V_k\bm y$，由$\bm b=\bm U_{k+1}\beta_1\bm e_1$和式`eq:ls-golub-kahan-relations`得残差表示，再借$\bm U_{k+1}$列标准正交把问题化为式`eq:ls-lsqr-subproblem`的双对角最小二乘小问题；这一做法不要求方阵、满秩或相容，且$\bm B_k$每轮只增一行一列，可用一次新的Givens旋转延续QR分解并以短递推更新解。

##### 12.4.9.2 算法实现

###### paragraph：初始化

1. 规定输入为一般实矩阵$\bm A$与$\bm b$，允许秩亏，输出$\bm x$；超参数为步数上限$K$与阈值，最小二乘目标用正规残差绝对阈值$\tau_n\ge0$，相容方程目标另用第`sec:ls-stationary-stopping`节的$\mathrm{atol},\mathrm{rtol}$。固定$\bm x_0=\bm0$，$K=0$时直接输出，否则按第`sec:ls-krylov-stopping`节检查初值，并指出正规残差长度$\alpha_1\beta_1$与双对角化起步共用一次$\bm A^\top$乘法；未结束时取$\bm w_1=\bm v_1$、$\bar\rho_1=\alpha_1$、$\bar\phi_1=\beta_1$，并说明三者分别是未旋转的对角元、右端首分量与第一个更新方向。

###### paragraph：双对角化与Givens旋转

1. 第$k$轮先做一次双对角化，说明前$k-1$行已上三角化、第$k,k+1$两行待处理的元素，再按第`sec:ls-gmres`节的旋转约定取Givens旋转消去$\beta_{k+1}$，得到$\rho_k,c_k,s_k$。同一旋转作用于新列和右端，得到$\theta_{k+1},\bar\rho_{k+1},\phi_k,\bar\phi_{k+1}$，并指明哪些是上双对角因子$\bm R_k$与变换后右端的元素、哪些留给下一轮。

###### paragraph：更新解与停止

1. 旋转后以$\bm x_k=\bm x_{k-1}+(\phi_k/\rho_k)\bm w_k$更新解，原残差与正规残差长度分别从标量$|\bar\phi_{k+1}|$与$|\bar\phi_{k+1}|\alpha_{k+1}|c_k|$读出，达到第`sec:ls-krylov-stopping`节阈值或$K$时复核后输出，否则取$\bm w_{k+1}=\bm v_{k+1}-(\theta_{k+1}/\rho_k)\bm w_k$，并说明它须排在$\bm x_k$之后。零系数时照常完成本轮旋转与更新后结束，$\beta_{k+1}=0$与$\alpha_{k+1}=0$分别使原残差与正规残差估计为零；最后归纳说明正常步骤中$\rho_k>0$。

2. 示例`ex:ls-lsqr-line`沿用示例`ex:ls-golub-kahan-line`的系数执行LSQR：第一轮旋转得$\rho_1,c_1,s_1$及$\theta_2,\bar\rho_2,\phi_1,\bar\phi_2$，更新得$\bm x_1=\tfrac{61}{435}(5,6)^\top$，即沿$\bm A^\top\bm b$方向使残差最小的点，两个残差估计与直接计算一致。因$\alpha_3=0$，第二轮完成旋转与更新后结束，得$\bm x_2=(7/6,1/2)^\top$，正是最小二乘解，原残差估计$1/\sqrt6$等于最优残差长度，正规残差估计为零。

##### 12.4.9.3 算法分析

###### paragraph：正确性

1. 定理`thm:ls-lsqr-recursion`断言：精确算术中双对角化在第$k$轮前未终止时，递推所得$\bm x_k=\bm V_k\bm y_k$，$\bm y_k$解式`eq:ls-lsqr-subproblem`，即$\bm x_k$在$\operatorname{range}(\bm V_k)$中使原残差最小，且$\lVert\bm r_k\rVert_2=|\bar\phi_{k+1}|$、$\lVert\bm A^\top\bm r_k\rVert_2=|\bar\phi_{k+1}|\alpha_{k+1}|c_k|$。

2. 证明说明新列只在第$k,k+1$行非零，一次新旋转就能延续三角化，归纳得到旋转之积$\bm Q_k$把增广矩阵化为$\bm R_k,\bm f_k,\bar\phi_{k+1}$的形式，由正交性得$\bm y_k=\bm R_k^{-1}\bm f_k$且最小残差$|\bar\phi_{k+1}|$就是$\lVert\bm r_k\rVert_2$。再把$\bm V_k\bm R_k^{-1}$的列记为$\bm w_i/\rho_i$，逐列比较得方向递推与逐步累加的解更新；正规残差估计则由式`eq:ls-golub-kahan-relations`第二式及$\bm B_k^\top\bm g_k=\bm0$推出。

###### paragraph：残差的单调性与选出的解

1. 由此读出LSQR的性质：候选空间嵌套使精确算术中原残差不增，正规残差则可能上升；零初值使各步留在$\operatorname{range}(\bm A^\top)$，达到正规方程时即得第`sec:ls-pseudoinverse`节的$\bm A^\dagger\bm b$，$\alpha_{k+1}=0$正是此情形。

###### paragraph：与正规方程上CG的关系

1. 定理`thm:ls-lsqr-cg-equivalence`断言：精确算术中两种方法都未终止时，LSQR第$k$步近似等于对正规方程从$\bm x_0=\bm0$施行第`sec:ls-conjugate-gradient`节CG的第$k$步近似。

2. 证明先说明CG的第$k$步是Krylov空间中使$\lVert\bm A(\bm x-\hat{\bm x})\rVert_2^2$最小的点，再由$\hat{\bm r}$与$\operatorname{range}(\bm A)$正交用勾股定理把原残差平方分解为常数加同一函数。由定理`thm:ls-golub-kahan-relations`两者候选空间相同，又因$\bm A$在$\operatorname{range}(\bm A^\top)$上单射而最小点唯一，故两者相等。

###### paragraph：收敛速度与数值敏感度

1. 借这一等价把CG收敛界搬到LSQR：速度由非零奇异值平方的分布决定，满列秩时CG界中的$\sqrt\kappa$正是$\kappa_2(\bm A)$，给出$\lVert\bm A(\bm x_k-\hat{\bm x})\rVert_2$的几何收敛界。随后指出LSQR不形成Gram矩阵，避免了第`sec:ls-normal-equations-method`节的信息丢失，但不消除原问题的病态性；有限精度下正交性与残差估计仍须按第`sec:ls-krylov-stopping`节复核。

###### paragraph：计算代价

1. 每轮核心工作是一次$\bm A$与一次$\bm A^\top$乘向量，另加十几次标量运算、一次旋转和两次长度为$d$的向量更新；保存$\bm u,\bm v,\bm w,\bm x$，工作存储为$O(m+d)$。

#### 12.4.10 LSMR算法

##### 12.4.10.1 主要思想

1. 交代LSMR出自Fong与Saunders，它与LSQR在同一子空间$\operatorname{range}(\bm V_k)$中取点，改为最小化判断最小二乘解所看的正规残差。用$\bm A^\top$左乘原残差表示，借式`eq:ls-golub-kahan-relations`第二式及$\bm B_k$的两条边界关系得到式`eq:ls-lsmr-subproblem`，再由$\bm V_{k+1}$列标准正交化为小问题$\min_{\bm y}\lVert\alpha_1\beta_1\bm e_1-\overline{\bm T}_k\bm y\rVert_2$；强调实际计算不形成$\bm B_k^\top\bm B_k$，而用两组旋转逐层处理双对角系数。

##### 12.4.10.2 算法实现

###### paragraph：初始化

1. 输入、超参数、零初值与输出约定都同LSQR；按双对角化起步并检查初值，零解直接输出，否则初始化$\bm h_1=\bm v_1$、$\bar{\bm h}_0=\bm0$、$\bar\alpha_1=\alpha_1$、$\bar\zeta_1=\alpha_1\beta_1$及$\rho_0=\bar\rho_0=1$、$\bar c_0=1$、$\bar s_0=0$。说明$\bar\zeta_1$是初始正规残差长度，$\bar\alpha_1$改名是为把带横线的$\rho$留给第二组旋转，其余量只是占位，使第一轮公式不必单独处理。

###### paragraph：第一组旋转

1. 第$k$轮先完成一次双对角化，再作与LSQR相同的第一组旋转，把$\bm B_k$化为上双对角因子$\bm R_k$，得到$\rho_k,c_k,s_k,\theta_{k+1},\bar\alpha_{k+1}$。

###### paragraph：第二组旋转

1. 接着作第二组旋转，处理以$\rho_i$为对角、$\theta_{i+1}$为下对角的下双对角矩阵：上一轮旋转先作用于新列产生$\bar\theta_k$并留下$\bar c_{k-1}\rho_k$，本轮旋转再消去$\theta_{k+1}$，并把右端$\bar\zeta_k$分成$\zeta_k$与$\bar\zeta_{k+1}$。因第二组用到本轮的$\rho_k,\theta_{k+1}$，须排在第一组之后。

###### paragraph：更新方向与解

1. 两组旋转后先形成第二层方向$\bar{\bm h}_k$，再更新$\bm x_k$；以$|\bar\zeta_{k+1}|$为正规残差估计，按第`sec:ls-krylov-stopping`节阈值或$K$复核后输出，相容方程目标则在候选终止处由$\bm b-\bm A\bm x_k$计算原残差。未结束时最后取$\bm h_{k+1}=\bm v_{k+1}-(\theta_{k+1}/\rho_k)\bm h_k$；零系数时完成本轮旋转与更新后结束，并说明$\alpha_{k+1}=0$使$\bar\zeta_{k+1}=0$，正常步骤的$\rho_k,\bar\rho_k$为正。

##### 12.4.10.3 算法分析

###### paragraph：正确性

1. 以两组旋转对应两层三角分解引入定理`thm:ls-lsmr-minres-equivalence`：精确算术中双对角化在第$k$轮前未终止时，LSMR的$\bm x_k$是$\operatorname{range}(\bm V_k)=\mathcal K_k(\bm A^\top\bm A,\bm A^\top\bm b)$中使正规残差最小的唯一点，最小值为$|\bar\zeta_{k+1}|$，且等于对正规方程从零初值施行第`sec:ls-minres`节MINRES的第$k$步近似。

2. 证明由式`eq:ls-lsmr-subproblem`化为小问题，第一组旋转得$\bm B_k^\top\bm B_k=\bm R_k^\top\bm R_k$，再用$\theta_{k+1}\rho_k=\alpha_{k+1}\beta_{k+1}$把$\overline{\bm T}_k$分解为下双对角因子乘$\bm R_k$；换元$\bm t=\bm R_k\bm y$后第二组旋转像LSQR一样给出$\bar{\bm R}_k$与$\bm z_k$，得$\bm x_k=\bm V_k\bm R_k^{-1}\bar{\bm R}_k^{-1}\bm z_k$，逐列比较即得两套方向来自两层三角求解。

3. 唯一性由$\operatorname{range}(\bm V_k)\subseteq\operatorname{range}(\bm A^\top)$与$\operatorname{null}(\bm A^\top\bm A)=\operatorname{null}(\bm A)$正交、$\bm A^\top\bm A$在该子空间上单射得到；再由定理`thm:ls-golub-kahan-relations`识别出Krylov空间，MINRES在同一空间最小化同一函数，故两者第$k$步相同。

###### paragraph：残差的单调性

1. 候选空间嵌套使精确算术中正规残差不增；原残差也不增，依据是LSMR近似为截至当前步LSQR近似的凸组合、$\bm x_{k+1}^{\mathrm M}$是$\bm x_k^{\mathrm M}$与$\bm x_{k+1}^{\mathrm Q}$的凸组合（正文只陈述“可以证明”而未展开），以及原残差平方的凸性与$\bm x_{k+1}^{\mathrm Q}$在包含$\bm x_k^{\mathrm M}$的空间中的最优性。

###### paragraph：选出的解与收敛速度

1. 零初值使各步留在$\operatorname{range}(\bm A^\top)$，与LSQR同理达到正规方程时选出$\bm A^\dagger\bm b$；由定理`thm:ls-lsmr-minres-equivalence`，行空间上LSMR等价于正规方程上的MINRES，速度受非零奇异值平方分布控制。小奇异值与正交性损失仍影响精度，残差单调并不推出解误差单调。

###### paragraph：计算代价

1. 每轮核心工作仍是一次$\bm A$与一次$\bm A^\top$乘向量，比LSQR多一组标量旋转和一套方向$\bar{\bm h}_k$更新；保存$\bm u,\bm v,\bm h,\bar{\bm h},\bm x$，工作存储仍为$O(m+d)$。

#### 12.4.11 预条件

##### 12.4.11.1 主要思想

1. 从前面各方法的收敛快慢由谱或奇异值分布决定出发，引入接近$\bm A$且$\bm M\bm z=\bm r$易解的固定可逆矩阵$\bm M$，把方程改写为左或右预条件形式，使迭代面对更集中的谱。实现时不显式求$\bm M^{-1}$、不形成变换后矩阵，每次需要时求解一次$\bm M\bm z=\bm r$。

##### 12.4.11.2 算法实现

###### paragraph：常用预条件

1. 说明预条件$\bm M$是超参数，输入输出不变，并各用一句给出三种常用预条件的结构与一次应用的工作：对角缩放要求对角元非零，一次应用为逐项相除；SSOR取第`sec:ls-ssor`节的分裂矩阵，$\bm A$对称正定且$0<\omega<2$时对称正定，一次应用为前代、缩放与回代；不完全分解在第`sec:ls-lu`节或第`sec:ls-cholesky`节的消元中只保留指定位置元素，一次应用为两次稀疏三角回代。

###### paragraph：PCG的初始化

1. 以PCG为例写完整步骤：要求$\bm A,\bm M$都对称正定，超参数为$\bm x_0,\mathrm{atol},\mathrm{rtol},K,\bm M$，并申明本小节的$\alpha_k,\beta_k,\rho_k$与双对角化系数无关。初始化计算$\bm r_0$并按第`sec:ls-stationary-stopping`节检查，未结束时解$\bm M\bm z_0=\bm r_0$，取$\rho_0=\bm r_0^\top\bm z_0$、$\bm p_0=\bm z_0$。

###### paragraph：PCG的每轮更新

1. 第$k$轮计算$\bm q_k=\bm A\bm p_k$与步长$\alpha_k$，更新$\bm x_{k+1},\bm r_{k+1}$后按第`sec:ls-stationary-stopping`节检查；未结束时解$\bm M\bm z_{k+1}=\bm r_{k+1}$，取$\rho_{k+1},\beta_k$与新方向$\bm p_{k+1}=\bm z_{k+1}+\beta_k\bm p_k$。与CG对比，只是方向由预条件残差组合、内积换成$\bm r^\top\bm z$，正定性保证正常步骤分母为正，零残差先已结束。

###### paragraph：其他方法中的预条件

1. 其他方法只需替换系数矩阵的作用：右预条件求解$\bm A\bm M^{-1}\bm y=\bm b$再令$\bm x=\bm M^{-1}\bm y$，以GMRES为例先解$\bm M\bm z=\bm v$再乘$\bm A$；LSQR与LSMR把$\bm A\bm v$换成$\bm A(\bm M^{-1}\bm v)$、$\bm A^\top\bm u$换成$\bm M^{-\top}(\bm A^\top\bm u)$，结束时由$\bm y$换回$\bm x$。

2. 示例`ex:ls-pcg-one-step`在示例`ex:ls-stationary-running-example`的贯穿例上取对角缩放$\bm M=\operatorname{diag}(4,3)$与零初值，逐项算出$\bm r_0,\bm z_0,\rho_0,\bm p_0$及第一轮的$\bm q_0,\alpha_0$，得$\bm x_1=(19/92,38/69)^\top$并以直接计算核对残差。对比$\bm A$范数误差从约$1.168$降到约$0.236$，而普通CG第一步只降到约$0.337$；再算一轮得$\bm x_2=\bm x_\star$，与二维问题至多两步结束一致。

##### 12.4.11.3 算法分析

###### paragraph：正确性

1. 用保持对称的变换引入正确性：取$\bm M=\bm C\bm C^\top$与对称正定的$\widehat{\bm A}=\bm C^{-1}\bm A\bm C^{-\top}$。定理`thm:ls-pcg-equivalence`断言：精确算术中PCG未终止时，其迭代量与对$\widehat{\bm A}\bm y=\bm C^{-1}\bm b$从$\bm y_0=\bm C^\top\bm x_0$施行CG的迭代量满足$\bm y_k=\bm C^\top\bm x_k$、$\hat{\bm r}_k=\bm C^{-1}\bm r_k$、$\hat{\bm p}_k=\bm C^\top\bm p_k$；因此$\bm x_k$在$\bm x_0+\mathcal K_k(\bm M^{-1}\bm A,\bm M^{-1}\bm r_0)$中使$\bm A$范数误差最小，并满足以$\hat\kappa=\kappa_2(\widehat{\bm A})=\lambda_{\max}(\bm M^{-1}\bm A)/\lambda_{\min}(\bm M^{-1}\bm A)$表示的收敛界。

2. 证明对$k$归纳，关键在两个内积$\hat{\bm r}_k^\top\hat{\bm r}_k=\bm r_k^\top\bm z_k$与$\hat{\bm p}_k^\top\widehat{\bm A}\hat{\bm p}_k=\bm p_k^\top\bm A\bm p_k$相等，故步长和组合系数相同、对应关系延续。再由定理`thm:ls-cg-convergence`得变换问题的最优性，换回原变量时范数与仿射子空间一一对应；$\bm M^{-1}\bm A$与$\widehat{\bm A}$相似，故条件数是特征值之比。

3. 定理之后指出一般不对称的$\bm M^{-1}\bm A$不能直接交给普通CG，$\bm C$只用于论证；论证要求固定的线性预条件，变动预条件不沿用标准PCG的共轭性与最优性。

###### paragraph：收敛速度

1. 定理把速度归结为$\bm M^{-1}\bm A$的特征值分布，并以对角缩放适合尺度悬殊矩阵为例：取$d=10$、$\bm A=\bm S\bm T\bm S$，$\bm S=\operatorname{diag}(1,\ldots,10)$，$\bm T$为对角元$1$、次对角元$0.4$的三对角矩阵，取$\bm M=\bm S^2$即$\bm C=\bm S$，变换后恰好$\widehat{\bm A}=\bm T$，特征值为$1+0.8\cos(j\pi/11)$。

2. 图`fig:ls-preconditioned-spectrum`在对数横轴上比较两组特征值：$\bm A$的特征值从约$0.73$铺到约$133$，比值约$182.7$；缩放后落在$[0.23,1.77]$内，比值约$7.61$。由此定理中的收缩因子从约$0.862$降到约$0.468$，而每轮只多一次逐项除法。

###### paragraph：计算代价

1. 每轮比CG多一次$\bm M$求解，选用时须同时计入构造$\bm M$与每轮应用的成本，比较达到同一精度的总工作量。

###### paragraph：GMRES与MINRES的预条件

1. 对GMRES比较左右预条件的目标：左预条件最小化$\lVert\bm M^{-1}(\bm b-\bm A\bm x)\rVert_2$，右预条件保留原残差，两者结束时都回到第`sec:ls-stationary-stopping`节检查原残差。MINRES须保持对称性，只能用对称正定预条件的分裂变换；并强调预条件只改善变换后的谱，不改变原问题对数据的敏感度。

###### paragraph：最小二乘目标的保持

1. 对不相容最小二乘核对变换是否保持原目标：左变换给出第`sec:ls-weighted-ls`节意义下以$\bm M^{-\top}\bm M^{-1}$为权的加权目标，一般改变解；可逆右变换使残差逐点相同，保留原目标与解集，但零初值在$\bm y$坐标下选出$\lVert\bm M\bm x\rVert_2$最小的解，秩亏时未必是原坐标下的最小范数解。

#### 12.4.12 收敛检验与停止准则

1. 方阵上的CG、PCG、GMRES、MINRES、BiCG与BiCGSTAB统一沿用第`sec:ls-stationary-stopping`节规则：超参数为$\bm x_0,\mathrm{atol},\mathrm{rtol},K$，以$\tau=\mathrm{atol}+\mathrm{rtol}\lVert\bm b\rVert_2$检查真实原残差，达到阈值或上限时输出当前$\bm x$，并指出达到上限本身不表示收敛；递推残差与小问题残差只用于内部决定何时复核，不另作输出。

2. LSQR与LSMR以相容方程为目标时沿用同一原残差阈值；以最小二乘为目标时，因不相容问题最优原残差不为零、原残差阈值可能永远达不到，单列非负超参数$\tau_n$检查$\lVert\bm A^\top(\bm b-\bm A\bm x_k)\rVert_2\le\tau_n$。说明$\tau_n$是与数据尺度相配的绝对阈值，不除以可能为零的参照量；初值满足条件时输出$\bm x_0=\bm0$，其余情况在每次候选终止和最终输出前用$\bm A,\bm b,\bm x_k$重算残差复核，达到$K$时只输出当前$\bm x$。

3. 最后提示残差小的含义须结合原问题条件数解释，要求最小范数解时还须保持零初值、迭代留在行空间并核对预条件下的选解准则，真实残差复核的矩阵乘法计入成本；误差解释留到第`sec:ls-numerical-sensitivity`节，同一精度下的综合比较留到第`sec:ls-method-selection`节。


### 12.5 行列投影迭代法

1. 从前两节的迭代每轮都要访问整个矩阵进入，提出在数据按行到达或只便于逐行读取时，每次只让一个方程成立、用投影逐步求解。说明标准Kaczmarz算法处理相容方程，不相容时再用列投影修正右端形成扩展Kaczmarz算法；本节$\bm A\in\mathbb R^{m\times d}$不必是方阵，两种算法都以$\bm A,\bm b$为输入、$\bm x$为输出，投影中的残差和辅助向量只是内部状态。

#### 12.5.1 Kaczmarz算法

##### 12.5.1.1 主要思想

1. 说明Kaczmarz算法把当前解正交投影到一个行方程的超平面上：非零行$\bm a_i^\top\bm x=b_i$的解集以$\bm a_i$为法向量，据第`sec:ls-orthogonal-projection`节的正交投影，把最近点写成$\bm x_k+t\bm a_i$代入方程，得修正方向$\bm a_i$与长度$t=(b_i-\bm a_i^\top\bm x_k)/\lVert\bm a_i\rVert_2^2$。指出一次更新让所选方程成立却可能改变其他行残差，相容时各超平面有公共点，反复投影便逐渐逼近它；本小节假设方程相容，只遍历非零行。

##### 12.5.1.2 算法实现

###### paragraph：初始化

1. 单独列出超参数：初值$\bm x_0$、固定循环顺序、容差$\mathrm{atol},\mathrm{rtol}$和最大更新次数$K$，要求最小范数解时取$\bm x_0=\bm 0$；内部保存$\bm x_k$与当前行修正量$\bm\delta_k$，全局残差只在初始时和每轮完整扫掠后计算。初始化$k=0$，$K=0$时直接取$\bm x=\bm x_0$并结束。

###### paragraph：行投影

1. 按循环顺序选行$i_k$，执行$\bm\delta_k=\tfrac{b_{i_k}-\bm a_{i_k}^\top\bm x_k}{\lVert\bm a_{i_k}\rVert_2^2}\bm a_{i_k}$、$\bm x_{k+1}=\bm x_k+\bm\delta_k$，每完成一次行更新计数加一。

###### paragraph：停止检查

1. 规定达到更新次数上限时立即结束并取当前$\bm x$（即使本轮未扫完）；在初始时与每轮完整扫掠后，若原残差$\lVert\bm b-\bm A\bm x_k\rVert_2$不超过第`sec:ls-matrix-splitting`节的阈值$\mathrm{atol}+\mathrm{rtol}\lVert\bm b\rVert_2$，也结束并取当前$\bm x$。

###### paragraph：随机选行

1. 说明随机版本只把选行改为按$p_i=\lVert\bm a_i\rVert_2^2/\lVert\bm A\rVert_F^2$独立抽样，投影公式不变，每次更新后检查全局残差和次数上限；零行概率为零、不会被抽到，因而不会除以零。

2. 示例`ex:ls-kaczmarz-two-steps`用例`ex:ls-stationary-running-example`的方程（行$(4,1)^\top,(1,3)^\top$，平方范数$17,10$），从$\bm x_0=\bm 0$按$1,2$顺序投影：第一步修正长度$1/17$得$\bm x_1=(4/17,1/17)^\top$、第一个方程成立；第二步残差$27/17$、修正长度$27/170$得$\bm x_2=(67/170,91/170)^\top$，第二个方程成立而第一个又不成立。列出到$\bm x_\star=(1/11,7/11)^\top$的距离依次约为$0.643,0.595,0.320$，供下文分析速度时使用。

##### 12.5.1.3 算法分析

###### paragraph：收敛性

1. 指出循环版本的收敛可由投影的几何性质直接得到，并引入第`sec:ls-pseudoinverse`节的伪逆$\bm A^\dagger$，说明$\bm I-\bm A^\dagger\bm A$是到$\mathcal N(\bm A)$的正交投影。

2. 定理`thm:ls-kaczmarz-convergence`：设$\bm A\bm x=\bm b$相容且$\bm A\neq\bm 0$，令$\bm x_\star=\bm A^\dagger\bm b+(\bm I-\bm A^\dagger\bm A)\bm x_0$；按固定循环顺序遍历非零行时，$\bm x_\star$是解，到它的距离逐步不增且每轮按与初值无关的因子$q<1$几何收缩，从而$\bm x_k\to\bm x_\star$，$\bm x_0=\bm 0$时极限为最小范数解$\bm A^\dagger\bm b$。

3. 证明先对任一解$\bm y$把更新写成正交投影$\bm P_i$作用于误差，由勾股关系得距离不增；再由修正都在行空间中，得$\bm x_k$的零空间分量保持为$\bm x_0$的、$\bm A\bm x_\star=\bm b$且误差始终在行空间中。一轮误差映射$\bm K$把行空间映到自身，若其中某$\bm v$长度不变，则$\bm v$与每个非零行正交，从而落在$\mathcal N(\bm A)\cap\mathcal R(\bm A^\top)=\{\bm 0\}$；取行空间标准正交基得$\bm C=\bm Q^\top\bm K\bm Q$，由定理`thm:matrix-analysis-rayleigh-ritz`得$\lVert\bm C\rVert_2\leq q=\sqrt{1-\mu}<1$，再用第`sec:ls-convergence`节的固定更新结论与轮内距离不增得整个序列收敛。

4. 由定理说明零初值使迭代留在行空间，相容而解不唯一时选出最小范数解，任意初值的极限也满足方程但带着初值的零空间分量。

###### paragraph：收敛速度与代价

1. 指出速度受行间夹角和访问顺序影响，行越接近两两正交一轮去掉的误差越多。借图`fig:ls-kaczmarz-projection-path`（示例`ex:ls-kaczmarz-two-steps`的交替投影折线，前六个迭代点收拢到交点）说明二维时第一步后误差平行于刚投影过的直线，此后每次投影把误差长度乘以法向夹角余弦$7/\sqrt{170}\approx0.537$，与例中距离由$0.595$降到$0.320$的比值一致；两直线越近垂直收拢越快，越近平行越在狭窄夹角里往复。最后给出一次投影成本$O(\operatorname{nnz}(\bm a_i))$，全局残差检查另需一次完整矩阵乘向量。

###### paragraph：随机版本与不相容情形

1. 说明随机选行的概率收敛与速率由Strohmer与Vershynin给出，其证明要用期望，留到第`chap:random-variables`章之后。再转向不相容情形：取$\bm A=(1,1)^\top$、$\bm b=(0,1)^\top$，两行投影化为$x\gets b_i$，循环投影在$0$与$1$之间往返而最小二乘解为$\hat x=1/2$，随机选行时$x$也只取$0$或$1$，说明仅改选行方式不能保证得到最小二乘解，不相容问题交给下一算法。

#### 12.5.2 扩展Kaczmarz算法

##### 12.5.2.1 主要思想

1. 把不相容归因于右端：分解$\bm b=\bm b_\parallel+\bm b_\perp$，$\bm b_\parallel\in\mathcal R(\bm A)$，$\bm b_\perp\in\mathcal N(\bm A^\top)$为不可拟合部分，由第`sec:ls-ordinary-ls`节得最小二乘解就是相容方程$\bm A\bm x=\bm b_\parallel$的解。据此说明扩展Kaczmarz算法同时逼近$\bm b_\perp$与最小范数解：用列投影使$m$维辅助向量$\bm z$趋向$\bm b_\perp$，再用行投影求解$\bm A\bm x=\bm b-\bm z$，并说明采用Zouzias与Freris的随机版本。

##### 12.5.2.2 算法实现

1. 说明采用同步版本：每轮的列投影和行投影都使用本轮开始时的状态$(\bm x_k,\bm z_k)$。

###### paragraph：初始化与抽样

1. 规定输入为$\bm A,\bm b$、输出为$\bm x$，超参数为停止容差$\tau_r,\tau_n\geq0$与更新次数上限$K$；初始化$\bm x_0=\bm 0$、$\bm z_0=\bm b$，计算非零行、列的平方范数作抽样权重，$\bm A=\bm 0$时直接取$\bm x=\bm 0$。记第$j$列为$\bm c_j$，每轮独立地按$\lVert\bm a_i\rVert_2^2/\lVert\bm A\rVert_F^2$和$\lVert\bm c_j\rVert_2^2/\lVert\bm A\rVert_F^2$抽取行$i_k$与列$j_k$。

###### paragraph：列投影

1. 列投影计算$\bm z_{k+1}=\bm z_k-\tfrac{\bm c_{j_k}^\top\bm z_k}{\lVert\bm c_{j_k}\rVert_2^2}\bm c_{j_k}$，说明它去掉$\bm z_k$在所选列方向的分量，相当于对相容方程$\bm A^\top\bm z=\bm 0$做一次Kaczmarz投影；由减去的总是列的倍数，$\bm z$在$\mathcal N(\bm A^\top)$中的分量始终为$\bm b_\perp$，从而逐步识别与列空间正交的残差。旧的$\bm z_k$保留给本轮行更新。

###### paragraph：行投影

1. 行投影计算$\bm\delta_k=\tfrac{b_{i_k}-(\bm z_k)_{i_k}-\bm a_{i_k}^\top\bm x_k}{\lVert\bm a_{i_k}\rVert_2^2}\bm a_{i_k}$、$\bm x_{k+1}=\bm x_k+\bm\delta_k$，本轮完成后才替换为$(\bm x_{k+1},\bm z_{k+1})$。

###### paragraph：停止检查

1. 规定在初始时和每轮更新后，若$\lVert\bm b-\bm z_k-\bm A\bm x_k\rVert_2\leq\tau_r$且$\lVert\bm A^\top\bm z_k\rVert_2\leq\tau_n$，或已达$k=K$，就终止并取$\bm x=\bm x_k$；说明前一项检查$\bm x_k$对修正方程的拟合，后一项检查辅助向量与列空间的正交性，二者只是内部判据，$\bm z_k$和检查值都不输出。

2. 示例`ex:ls-extended-kaczmarz-two-rounds`沿用上一小节的不相容例核对更新先后：唯一列$\bm c_1=(1,1)^\top$，$\bm b_\perp=(-1/2,1/2)^\top$；第一轮抽到第一行时列投影给出$\bm z_1=\bm b_\perp$，行投影用旧$\bm z_0$、修正量为零而$x$不动；第二轮$\bm z_2=\bm z_1$，修正后右端$(1/2,1/2)^\top$已相容，无论抽到哪一行都把$x$移到最小二乘解$1/2$并保持不变，此时两项检查值都为零、算法停止。

##### 12.5.2.3 算法分析

###### paragraph：极限的含义

1. 由列投影只减去列的倍数，说明它保留$\bm b_\perp$并缩小$\bm z_k-\bm b_\perp$，零初值与沿行方向的修正使$\bm x_k$留在行空间；当$\bm z_k$趋于$\bm b_\perp$时行投影求解$\bm A\bm x=\bm b_\parallel$，其行空间中的唯一解为$\bm A^\dagger\bm b$，故构造指向最小范数最小二乘解。

###### paragraph：收敛性与代价

1. 说明规定抽样下的均方收敛与速率证明需用期望而后置，此处不宣称每条轨迹的原残差逐步下降（示例`ex:ls-extended-kaczmarz-two-rounds`中第一轮$x$未动）；每轮访问一行一列并保存长度$m$的$\bm z_k$，代价按访问的非零元计，数值敏感性仍受原问题小奇异值影响。

#### 12.5.3 迭代结果与停止检验

1. 对比标准Kaczmarz以原残差检验相容方程，而扩展算法的原残差趋于非零的$\bm b_\perp$，不能以其为零为成功标准。令$\bm r_k=\bm b-\bm A\bm x_k$，由$\bm r_k=\bm z_k+(\bm b-\bm z_k-\bm A\bm x_k)$得$\lVert\bm A^\top\bm r_k\rVert_2\leq\lVert\bm A^\top\bm z_k\rVert_2+\lVert\bm A\rVert_2\lVert\bm b-\bm z_k-\bm A\bm x_k\rVert_2$，说明两项内部判据都小便控制了正交条件$\bm A^\top\bm r=\bm 0$的偏离，停止前再直接计算$\bm A^\top(\bm b-\bm A\bm x_k)$复核；最小范数要求另依赖零初值与行空间保持。

2. 说明两种方法的输出都只是当前$\bm x$，达到次数上限不代表达到目标精度。比较速度时区分一次行投影、一次完整扫掠和Krylov方法中含矩阵乘法的一次迭代：一次行投影只读一行，一轮扫掠才相当于一次矩阵乘向量，并把抽样权重准备与全局残差检查计入总成本；误差解释与方法选择分别见第`sec:ls-numerical-sensitivity`节和第`sec:ls-method-selection`节。


### 12.6 求解结果的误差与可信程度

1. 以“算出的结果能相信多少”进入第`sec:ls-numerical-sensitivity`节，分三方面展开：数据扰动怎样传到解、近似解怎样用残差判断、秩变化时伪逆怎样变化。先约定每种误差的参照量与允许修改的数据：比较两个精确解时修改$\bm A$或$\bm b$，用残差判断时数据不改而参照未知真解，后向误差则问数据至少改多少；结论由精确方程、范数估计和奇异值性质建立，扰动可以有限，第`chap:multivariate-calculus`章再从同一精确关系提取局部线性响应。

#### 12.6.1 右端项与系数矩阵的有限扰动

1. 设定本小节的对象（第`sec:ls-equation-sensitivity`节）：$\bm A\in\mathbb R^{d\times d}$可逆、$\bm b\ne\bm0$、精确解$\bm x_\star=\bm A^{-1}\bm b$，向量范数与诱导矩阵范数始终取同一种，并记$\kappa(\bm A)=\lVert\bm A\rVert\lVert\bm A^{-1}\rVert$。

###### paragraph：右端扰动

1. 先固定$\bm A$只改右端：两方程相减得对任意大小$\Delta\bm b$都精确成立的$\Delta\bm x=\bm A^{-1}\Delta\bm b$，取范数并用$\lVert\bm b\rVert\leq\lVert\bm A\rVert\lVert\bm x_\star\rVert$得相对误差界，指出它即第`sec:ls-matrix-condition-number`节的条件数界（定理`thm:matrix-analysis-condition-number-bound`）。再用奇异值分解把$\Delta\bm b$按$\bm u_i$展开，读出沿$\bm u_i$的误差放大$1/\sigma_i$倍、最小奇异值方向放大最多，并说明随后的例子在精确算术中计算，放大只来自问题本身。

2. 示例`ex:ls-rhs-perturbation-near-parallel`对照良态的$\bm A_1=\operatorname{diag}(2,1)$（放大约$1.6$倍）与两列近平行的$\bm A_2$（$\varepsilon=10^{-2}$）：由$\bm A_2^\top\bm A_2$的迹与行列式估计$\kappa_2(\bm A_2)\approx200$，右端微小变化使解由$(2,0)^\top$变为$(1,1)^\top$，放大约$141$倍，且变化几乎沿小奇异值的右奇异方向、两系数此增彼减。图`fig:matrix-analysis-coefficient-sensitivity`画出$\varepsilon$减小时系数沿相反方向分裂、绝对误差随$1/\varepsilon$增长。

###### paragraph：系数矩阵的扰动

1. 转入系数矩阵也带误差的情形（第`sec:ls-inverse-sensitivity`节）：$\bm B=\bm A+\bm E$可能不可逆，所以先确定何时可逆，再估计$\bm B^{-1}$离$\bm A^{-1}$多远。

2. 定理`thm:ls-inverse-finite-perturbation`给出两条结论：在$\lVert\bm A^{-1}\bm E\rVert<1$下$\bm B$可逆，得$\lVert\bm B^{-1}\rVert$的界与精确逆差恒等式`eq:ch06-inverse-finite-perturbation`；在更强的$q=\lVert\bm A^{-1}\rVert\lVert\bm E\rVert<1$下得到逆差相对界$q/(1-q)$，且$q=\kappa(\bm A)\lVert\bm E\rVert/\lVert\bm A\rVert$。

3. 证明由$\bm B\bm x=\bm0$推出$\bm x=-\bm A^{-1}\bm E\bm x$，取范数得核为零而可逆；对$\bm x=\bm B^{-1}\bm y$写$\bm x=\bm A^{-1}\bm y-\bm A^{-1}\bm E\bm x$并移项得$\lVert\bm B^{-1}\rVert$的界；恒等式由$\bm B^{-1}(\bm A-\bm B)\bm A^{-1}$展开，第2条对恒等式取范数后除以$\lVert\bm A^{-1}\rVert$。

4. 解读界的结构：分子是条件数乘相对扰动，分母$1-q$是到奇异边界的余量。用$\bm A=\operatorname{diag}(1,\varepsilon)$、$\bm E=\operatorname{diag}(0,-\delta)$说明界在谱范数下恰好取到且$\delta\to\varepsilon$时无界；反过来以$\bm E=\bm A$说明$q\geq1$只表示定理不再给出保证，不意味着$\bm B$已奇异。

###### paragraph：矩阵与右端同时扰动

1. 矩阵与右端同时扰动时，由扰动方程减去原方程得精确关系式`eq:ls-joint-perturbation-exact`，读出解的变化由右端变化与矩阵变化作用于原解的$\bm E\bm x_\star$两部分驱动，并在定理`thm:ls-inverse-finite-perturbation`的条件下写成$\Delta\bm x=(\bm A+\bm E)^{-1}(\Delta\bm b-\bm E\bm x_\star)$。

2. 定理`thm:ls-linear-system-perturbation`以相对扰动$\rho_A,\rho_b$表述：若$\kappa(\bm A)\rho_A<1$，则$\bm A+\bm E$可逆，并有解的相对误差界式`eq:matrix-analysis-linear-system-perturbation`。

3. 证明由上一定理第2条得可逆性，把精确关系改写为$\Delta\bm x=\bm A^{-1}(\Delta\bm b-\bm E\bm x_\star-\bm E\Delta\bm x)$，取范数、把含$\lVert\Delta\bm x\rVert$的项移到左边并除以$\lVert\bm x_\star\rVert$，再用$\lVert\Delta\bm b\rVert\leq\rho_b\lVert\bm A\rVert\lVert\bm x_\star\rVert$得到结论。

4. 解读界的三层结构：两类相对扰动相加、被条件数放大、再除以到奇异边界的余量，$\bm E=\bm0$时退回只扰动右端的界。指出第`sec:multivariable-matrix-perturbation`节从同一精确式提取解映射的一阶响应，这里保留的是对完整变化有效的结论。

#### 12.6.2 残差、前向误差与后向误差

###### paragraph：残差与前向误差

1. 从比较两个精确解转到只有一个近似解$\tilde{\bm x}$的情形（第`sec:ls-numerical-stability`节）：由$\bm A(\bm x_\star-\tilde{\bm x})=\bm r$，残差扮演右端误差的角色，得相对误差不超过$\kappa(\bm A)\lVert\bm r\rVert/\lVert\bm b\rVert$。用$\bm A=\operatorname{diag}(1,\varepsilon)$的例子说明病态时残差趋零而相对误差始终为$1/\sqrt2$，由此区分前向误差（近似解离真解多远）与后向误差（数据至少改多少才能使$\tilde{\bm x}$成为精确解）。

###### paragraph：后向误差的度量

1. 说明后向误差取决于允许怎样修改数据：范数型模型限制$\lVert\Delta\bm A\rVert\leq\epsilon\lVert\bm A\rVert$与$\lVert\Delta\bm b\rVert\leq\epsilon\lVert\bm b\rVert$，满足$(\bm A+\Delta\bm A)\tilde{\bm x}=\bm b+\Delta\bm b$的最小$\epsilon$记作$\eta(\tilde{\bm x})$，并预告二范数下它可由残差直接算出。

2. 定理`thm:ls-backward-error-formulas`对一般$\bm A\in\mathbb R^{m\times d}$、在分母$s=\lVert\bm A\rVert_2\lVert\tilde{\bm x}\rVert_2+\lVert\bm b\rVert_2>0$的条件下，给出二范数型后向误差$\eta_2(\tilde{\bm x})=\lVert\bm r\rVert_2/s$，且下确界可以取到。

3. 证明分两向：任何可行扰动都有$\bm r=\Delta\bm A\tilde{\bm x}-\Delta\bm b$，故$\epsilon\geq\lVert\bm r\rVert_2/s$；反过来对$\tilde{\bm x}=\bm0$与$\tilde{\bm x}\ne\bm0$分别构造扰动，后者用秩一矩阵$\bm r\tilde{\bm x}^\top$，由其谱范数验证两项相对大小都等于$\lVert\bm r\rVert_2/s$且恰好满足扰动方程。

4. 补充分母为零只在$\bm b=\bm0$且$\tilde{\bm x}=\bm0$时发生，此时$\tilde{\bm x}$已是精确解；指出迭代法常用的归一化残差恰为范数型后向误差（第`sec:ls-stationary-stopping`节、第`sec:ls-krylov-stopping`节）。再引入逐元素模型及其后向误差公式，用同一对角例子对比范数型约$\varepsilon/2$与逐元素为$1$，说明两种模型回答不同问题，结论不能不加说明地互用。

5. 示例`ex:ls-backward-error-computation`取示例`ex:ls-stationary-running-example`的$\bm A,\bm b$与近似解$\tilde{\bm x}=(0.09,0.64)^\top$，算出残差$(0,-0.01)^\top$，由对称矩阵特征值得$\lVert\bm A\rVert_2\approx4.618$、$\kappa_2(\bm A)\approx1.939$，再算分母$s\approx5.221$得$\eta_2\approx1.92\times10^{-3}$；按定理中的秩一构造写出$\Delta\bm A,\Delta\bm b$并验证扰动方程成立，最后对照实际相对前向误差约$0.0058$不超过定理`thm:ls-forward-backward-error`的界约$0.0075$。

###### paragraph：后向稳定与常用分解

1. 引入浮点运算模型与单位舍入$u$（双精度约$1.1\times10^{-16}$），定义后向稳定算法：结果是某邻近问题的精确解，后向误差不超过$u$乘只依赖维数的温和常数；并预告其前向误差仍受条件数制约。

2. 定理`thm:ls-forward-backward-error`在$\bm A$可逆、$\bm b\ne\bm0$、两项后向扰动相对大小不超过$\eta$且$\kappa(\bm A)\eta<1$的条件下，给出前向相对误差不超过$2\kappa(\bm A)\eta/(1-\kappa(\bm A)\eta)$。

3. 证明把$\tilde{\bm x}$看作扰动问题的精确解，在定理`thm:ls-linear-system-perturbation`中取$\bm E=\Delta\bm A$、$\rho_A,\rho_b\leq\eta$即得。

4. 归纳“前向误差约不超过条件数乘后向误差”：后向误差评价算法，条件数评价问题，$\kappa(\bm A)u$接近$1$时后向稳定算法也可能没有有效数字。据此逐一说明本章直接法的稳定性：带部分主元的LU（第`sec:ls-lu`节）的后向误差含增长因子$\rho$，最坏可达$2^{d-1}$，只在增长因子不大时后向稳定，可在消元时记录$\rho$；Cholesky（第`sec:ls-cholesky`节）因因子元素受$\sqrt{a_{j,j}}$控制而无增长问题；Householder与Givens（第`sec:ls-qr-method`节）保持长度，求最小二乘解后向稳定，修正Gram--Schmidt的$\bm Q$则可能偏离正交，需核验。

#### 12.6.3 最小二乘的不同输出与正规方程的风险

###### paragraph：三类输出的敏感性

1. 区分最小二乘的三类输出——系数$\bm A^\dagger\bm b$、拟合值$\bm P\bm b$与残差$(\bm I-\bm P)\bm b$，其中$\bm P=\bm A\bm A^\dagger$为正交投影（第`sec:ls-pseudoinverse`节）——并在固定$\bm A$时写出三者对$\Delta\bm b$的精确线性响应（第`sec:ls-ls-regularization-sensitivity`节）。由后两项正交得拟合值与残差的绝对变化不超过$\lVert\Delta\bm b\rVert_2$，系数变化却以$1/\sigma_r$放大，说明拟合得好与系数可靠是两回事；输出接近零时相对误差的解释须重新检查。最后指出$\bm A$也变化时误差界出现与$\kappa_2(\bm A)^2\lVert\hat{\bm r}\rVert_2$成比例的项，故$\kappa_2(\bm A)$不是同时改变$\bm A,\bm b$时所有输出的完整条件数。

###### paragraph：正规方程的条件数平方

1. 复用第`sec:ls-normal-equations-method`节对满列秩长方矩阵定义的$\kappa_2(\bm A)$，由伪逆的奇异值表示得$\kappa_2(\bm A)=\lVert\bm A\rVert_2\lVert\bm A^\dagger\rVert_2$，再由定理`thm:ls-normal-equations-condition-squaring`得式`eq:matrix-analysis-normal-equation-condition-square`。

2. 结合定理`thm:ls-forward-backward-error`说明正规方程法即使后向稳定，放大因子也是$\kappa_2(\bm A)^2$；以示例`ex:ls-rhs-perturbation-near-parallel`的$\bm A_2$取$\varepsilon=10^{-8}$说明Gram矩阵在舍入后已成奇异矩阵、信息在形成一步就丢失。对比QR与SVD直接作用于$\bm A$、放大因子为$\kappa_2(\bm A)$加以残差为权的平方项，得出两条路线代数等价而数值不同，正规方程法只在$\kappa_2(\bm A)^2u$远小于$1$时可取。

#### 12.6.4 伪逆、秩变化与数值秩

###### paragraph：伪逆的扰动与不连续

1. 指出伪逆的变化取决于最小正奇异值是否远离零（第`sec:ls-pseudoinverse-rank-change`节），对$\bm B=\bm A+\bm E$写出伪逆差的三项恒等式，并通过第一项展开后交叉项全部抵消加以验证，由此导出下面的估计。

2. 定理`thm:ls-pseudoinverse-perturbation`在$\bm A$与$\bm B$的全部正奇异值有共同下界$s_0>0$的条件下，给出$\lVert\bm B^\dagger-\bm A^\dagger\rVert_2\leq3\lVert\bm E\rVert_2/s_0^2$（式`eq:ch06-pseudoinverse-fixed-rank-perturbation`）。

3. 证明逐项估计三项：第一项直接由$\lVert\bm A^\dagger\rVert_2,\lVert\bm B^\dagger\rVert_2\leq1/s_0$得到；第二项用Penrose条件把$\bm B^\dagger$写成$\bm B^\dagger(\bm B^\dagger)^\top\bm B^\top$，再用$\bm A^\top(\bm I-\bm A\bm A^\dagger)=\bm0$把$\bm B^\top$换成$\bm E^\top$，借正交投影范数不超过$1$估计；第三项同理，三项相加。

4. 强调估计本身不要求同秩，关键是与扰动无关的正奇异值下界，并以$\operatorname{diag}(1,0)$与$\operatorname{diag}(1,\varepsilon)$说明秩增加时扰动趋零而伪逆差为$1/\varepsilon$。用第`sec:multivariable-continuity`节的连续性定义把估计与反例合起来：在固定秩集合$\mathcal M_r$上借Weyl界（定理`thm:ls-weyl-singular-value`）得$12\lVert\bm E\rVert_2/\sigma_r(\bm A)^2$的界，伪逆连续；允许秩增加时伪逆在秩亏处不连续；并与求逆在可逆矩阵集合上的连续性比较，说明差别来自定义域。最后指出$\mathcal M_r$在$r<\min(m,d)$时不是矩阵空间或线性子空间中的开集，第`chap:multivariate-calculus`章的微分定义在秩亏处不能直接套用，本部分不展开一般伪逆的微分。

###### paragraph：数值秩

1. 由奇异值移动不超过$\lVert\bm E\rVert_2$（式`eq:matrix-analysis-singular-value-perturbation`）说明小于误差尺度的奇异值与零无法区分，定义阈值$\tau$下的数值秩。取$\tau$为数据误差上界时，与观测相容的精确矩阵秩都不小于数值秩（定理`thm:ls-singular-value-rank-guarantee`），截断SVD又给出秩恰为数值秩的相容矩阵（定理`thm:matrix-analysis-best-low-rank`）；阈值联系误差来源，只有舍入误差时取$u\sigma_1$乘维数常数的量级，带测量噪声时按噪声在谱范数下的规模选取。区分精确秩这一代数性质与给定误差水平下可可靠辨认的方向数，说明奇异值在阈值附近有明显间隔时这一数目稳定、缓慢衰减时随阈值变化，并引出下一节针对难辨方向的截断与正则化。


### 12.7 敏感方向的正则化与截断

1. 承接上一节沿小奇异值方向误差放大$1/\sigma_i$倍的结论，指出QR等正交算法只能避免额外损失精度、改变不了这种放大；本节（第`sec:ls-truncated-svd-ridge`节）改为惩罚系数大小或舍弃部分方向，主动修改求解目标，以拟合误差换取解的稳定，依次给出岭回归与Tikhonov正则化、截断SVD及各自的计算路线与取舍。

#### 12.7.1 岭回归与Tikhonov正则化

###### paragraph：目标与可解条件

1. 对$\lambda>0$定义岭回归目标式`eq:ls-ridge-objective`，推广为惩罚$\bm L\bm x$的Tikhonov正则化，岭回归为$\bm L=\bm I$的情形（第`sec:ls-regularized-ls`节）。由两项平方长度之和等于堆叠残差的平方长度，改写为增广最小二乘式`eq:ls-augmented-system`，由此读出解的存在性与唯一性。

2. 定理`thm:ls-tikhonov-existence-uniqueness`：设$\lambda>0$，Tikhonov目标的极小点恰为$(\bm A^\top\bm A+\lambda\bm L^\top\bm L)\bm x=\bm A^\top\bm b$的解且总存在，解唯一当且仅当式`eq:linear-algebra-tikhonov-common-nullspace`成立，特别地岭回归对任意$\bm A$都有唯一解。证明把目标看作增广问题，借第`sec:ls-ordinary-ls`节的正规方程与唯一性判据，再由$\lambda>0$时$\ker\bm F=\ker\bm A\cap\ker\bm L$得出条件。

3. 用$\bm A=\bm L=[\,1\ \ -1\,]$说明一般$\bm L$下唯一性可能失效：$(1,1)^\top$方向既不影响拟合也不受惩罚。并强调加入惩罚后残差范数与其平方不能互换。

###### paragraph：奇异方向上的滤波

1. 设$\bm A$秩为$r$，记$c_i=\bm u_i^\top\bm b$，准备在奇异方向上逐个看岭回归的作用。

2. 定理`thm:ls-ridge-filter-factors`给出式`eq:matrix-analysis-ridge-filter-factor`：岭回归解对最小范数解逐方向乘滤波因子$f_i=\sigma_i^2/(\sigma_i^2+\lambda)\in(0,1)$，增益$\sigma_i/(\sigma_i^2+\lambda)$不超过$1/(2\sqrt\lambda)$；残差平方等于最小二乘残差平方加$\sum_i(1-f_i)^2c_i^2$，随$\lambda$不减，解长度随$\lambda$不增，$\lambda\to0^+$时回到$\bm A^\dagger\bm b$。证明在右奇异向量坐标中把正规方程按方向分开，增益界来自$\sigma_i^2+\lambda\geq2\sigma_i\sqrt\lambda$，残差公式来自列空间内外分量正交，单调性由$1-f_i$与$f_i/\sigma_i$的单调性得到。

3. 解读：伪逆增益$1/\sigma_i$换成有界增益，$\sigma_i^2\gg\lambda$的方向几乎不变、$\sigma_i^2\ll\lambda$的方向被压低，转折点在$\sigma_i=\sqrt\lambda$处$f_i=1/2$、增益达峰值。图`fig:ls-ridge-tsvd-filter-factors`画出两种$\lambda$下岭回归与截断SVD的滤波因子与方向增益，读出$\lambda$每增大一百倍转折点向大奇异值移动一个数量级、增益峰值降为十分之一。说明$\lambda$过小放大噪声、过大压掉信号，参数应依数据误差与任务目标选取（如使残差约等于误差规模，或在留出数据上检验），不能只因计算容易就宣称最合适。

###### paragraph：算法实现

1. 区分第`sec:ls-qr-method`节正交算法改善同一问题的计算过程与正则化主动修改问题，然后给出三条计算路线：对堆叠矩阵作Householder QR（任意$\bm L$）；$\bm L=\bm I$时一次SVD后按滤波因子扫描多个$\lambda$；对正则化正规矩阵作Cholesky（第`sec:ls-cholesky`节）再前代、回代；大型问题可对增广问题用LSQR（第`sec:ls-lsqr`节）。

2. 示例`ex:ls-ridge-line-fit`沿用示例`ex:ls-line-least-squares`的直线拟合数据，取$\lambda=1$走Cholesky路线：写出正则化方程的$2\times2$系数矩阵，逐步求出Cholesky因子、前代与回代得$\bm x_\lambda=(0.8,0.6)^\top$，核验正则化的正规残差$\bm A^\top\bm r-\lambda\bm x_\lambda=\bm 0$；与最小二乘解相比残差平方由$1/6$增至$0.4$、解长度由$1.269$降为$1$，并按SVD路线算出$f_1\approx0.877$、$f_2\approx0.456$，说明与$\lambda$相当的第二方向被压掉约一半。

###### paragraph：算法分析

1. 给出Cholesky路线的条件数为$\kappa_2(\bm F)^2$，而岭回归中$\kappa_2(\bm F)\leq(1+\sigma_1^2/\lambda)^{1/2}$，即使$\bm A$秩亏也有界，得出只在$\lambda$不太小、$(1+\sigma_1^2/\lambda)u\ll1$时该路线与QR同样可靠。最后要求回到正则化目标核验，分别报告拟合误差与惩罚大小，并检查正则化的正规残差$\bm A^\top(\bm b-\bm A\bm x_\lambda)-\lambda\bm L^\top\bm L\bm x_\lambda$而非原问题的$\bm A^\top\bm r$。

#### 12.7.2 截断SVD求解

###### paragraph：主要思想

1. 定义只在前$k$个奇异方向取倒数的$\bm x_k=\bm A_k^\dagger\bm b$（第`sec:ls-tsvd-solve`节），说明$\bm A_k$即第`sec:ls-low-rank-approximation`节的截断SVD（式`eq:matrix-analysis-truncated-svd`），$\bm x_k$是以$\bm A_k$代替$\bm A$后的最小范数最小二乘解。指出它与最佳低秩逼近共用分解而目的不同：低秩逼近要重建矩阵，截断求解要从带误差的观测中稳定恢复输入。

###### paragraph：算法实现

1. 给出计算步骤：求经济型SVD并算$c_i=\bm u_i^\top\bm b$，按阈值$\tau$取$k=\#\{i:\sigma_i>\tau\}$，由$c_i/\sigma_i$组合得解，由$\sum_{i\leq k}c_i\bm u_i$直接读出拟合值与残差，换阈值只需增减和式中的项。

2. 示例`ex:ls-tsvd-steps`取两列近共线的$3\times2$设计矩阵与观测$\bm b=(1,1.1,0.9)^\top$，SVD给出$\sigma_1\approx2.449$、$\sigma_2\approx0.0100$及$c_1,c_2$；取$\tau=0.1$得$k=1$、$\bm x_1\approx(0.50,0.50)^\top$，残差$|c_2|\approx0.134$全来自舍弃方向，正规残差长度约$0.0013$不为零，说明$\bm x_1$不是原问题的最小二乘解；不截断时第二方向贡献约$-13.4\bm v_2$，得到精确拟合的$(-9,10)^\top$。

###### paragraph：算法分析

1. 定理`thm:ls-tsvd-error-decomposition`：在$\bm b=\bm A\bm x_{\mathrm{true}}+\bm e$、$\bm x_{\mathrm{true}}\in\operatorname{range}\bm A^\top$下，把$\bm x_k-\bm x_{\mathrm{true}}$分成保留方向的噪声放大（长度不超过$\lVert\bm e\rVert_2/\sigma_k$）与舍弃方向上真实输入的损失两项正交部分，并给出残差平方比最小二乘多出$\sum_{i>k}c_i^2$、正规残差为$\sum_{i>k}\sigma_ic_i\bm v_i$。证明由$c_i=\sigma_i\bm v_i^\top\bm x_{\mathrm{true}}+\bm u_i^\top\bm e$代入后相减，残差分成最小二乘残差与舍弃方向两正交部分，再用$\bm A^\top\bm u_i=\sigma_i\bm v_i$得正规残差。

2. 解读第一项的界由$\sigma_k$而非$\sigma_r$决定，第二项是舍弃方向的全部损失，拟合代价是残差平方多出被舍弃的$c_i^2$，主要计算代价是一次$O(md^2)$的SVD。

###### paragraph：与岭回归的比较

1. 把截断解释为滤波因子取$1$或$0$，与岭回归的连续衰减对照，对应图`fig:ls-ridge-tsvd-filter-factors`中的阶梯与光滑曲线，引出同一数据上的比较。

2. 示例`ex:ls-regularization-response`沿用示例`ex:ls-tsvd-steps`的数据，把$\bm b$改为几乎只在$\bm u_2$上变化的$(1,1.11,0.89)^\top$，列表比较最小二乘、两个$\lambda$的岭回归与$k=1$截断的系数、残差和响应比。由响应比即第二方向增益读出：精确拟合的大系数全来自第二方向，系数越稳定残差越大，$\lambda=10^{-2}$的岭回归已接近$k=1$截断。

3. 比较两种方法的适用情形：奇异值有明显下降时截断位置自然、可信方向分得最清，缓慢衰减时岭回归更平稳。阈值应联系噪声规模、奇异值间隔和任务目标，取为数据误差估计即只在第`sec:ls-pseudoinverse-rank-change`节意义下可辨认的方向上反演；它不等同于按机器精度判定精确秩，只在数据仅含舍入误差时两者一致。

###### paragraph：与低秩逼近的边界

1. 划清与第`sec:ls-low-rank-approximation`节结论的边界：$\bm A_k$在谱范数与Frobenius范数下是最佳秩$k$重建（定理`thm:matrix-analysis-best-low-rank`），但由定理`thm:ls-tsvd-error-decomposition`的正规残差知除非舍弃的$c_i$全为零，$\bm x_k$不是原问题的最小二乘解，矩阵逼近的最优性也不涉及$\bm x_{\mathrm{true}}$与$\bm e$，不能推出它最接近真实输入。因此截断求解须说明保留方向、噪声水平与允许的拟合损失，保留方向是否可靠还要看间隔$\sigma_k-\sigma_{k+1}$，可用第`sec:ls-subspace-sensitivity`节的奇异值与子空间扰动界判断。


### 12.8 在同一求解目标下选择方法

1. 在目标、算法与误差标准都已建立后，把前面的方法放回同一组问题比较（第`sec:ls-method-selection`节）：先确认精确求解、普通或加权最小二乘、最小范数或正则化目标，再按矩阵结构、数据访问、资源和精度选择路线。强调比较的是达到相同要求的总成本，正则化与截断（第`sec:ls-truncated-svd-ridge`节）已改变目标，其较小系数或较低成本不能视为把原问题解得更准确。

#### 12.8.1 求解目标与方法适用性

1. 分开相容方程、一般最小二乘与最小范数三个目标（第`sec:ls-method-selection-goals`节）：相容时最小二乘最优残差为零而两者重合，不相容时要求的是$\bm A^\top\bm r=\bm0$、原残差停在正长度，故不能都按$\lVert\bm r\rVert\to0$判断；最小范数还要求排除$\ker\bm A$分量，即第`sec:ls-select-among-solutions`节的额外选解条件。

2. 满列秩时由正规方程的唯一解与$\bm A^\top\bm A$对称正定，说明矩形问题可转成对称正定方程，调用Cholesky、CG或满足收敛条件的定常迭代。分别指出显式形成的填充、条件数平方与舍入丢失信息（第`sec:ls-ls-regularization-sensitivity`节），以及不显式形成时每次作用仍需一次$\bm A$和一次$\bm A^\top$乘法；秩亏时正规矩阵仅半正定，正定算法的保证不能照搬。

3. 引出另一种保留残差为未知量的转换：把$\bm r+\bm A\bm x=\bm b$与$\bm A^\top\bm r=\bm0$合写为一个方阵方程。定理`thm:ls-augmented-kkt-system`：$\bm A$满列秩时该增广方程有唯一解，$\bm x$为最小二乘解、$\bm r$为相应残差，系数矩阵对称、可逆且不定。证明由两块行分别得残差定义与正规方程，由核为零证可逆，再用$(\bm u;\bm0)$与$(-\bm A\bm x;\bm x)$两类测试向量给出正负二次型证不定。

4. 据定理说明可用分块$\mathrm{LDL}^\top$（第`sec:ls-ldlt`节）或MINRES（第`sec:ls-minres`节）而不能用Cholesky或CG，并比较保留稀疏结构的好处与未知量增至$m+d$个带来的存储与预条件代价。

5. 定义“直接适用”“需转换”“需扩展版本”三种说法，分别以QR、SVD、LSQR，经正规方程或增广方程的转换，以及扩展Kaczmarz为例；并指出能写出迭代公式不等于已满足其收敛条件。

#### 12.8.2 矩阵条件

1. 目标确定后再按方阵或长方、对称性、正定性、秩、稠密或稀疏，以及能否取得$\bm A^\top\bm u$或单独一行核对各方法的输入要求（第`sec:ls-method-selection-matrix`节），用表`tab:ls-method-applicability`组织；说明表中迭代法按本章基本版本比较，某行的限制不能推广到所有同名扩展。

2. 说明表的读法：“需转换”时须重新检查转换后系统的结构、条件数、零空间和误差度量，“直接”也不省去预条件、停止检验或退化处理。随后的长表逐行列出LU、Cholesky、分块$\mathrm{LDL}^\top$、Schur补、Woodbury、正规方程法、QR、SVD、Richardson、Jacobi、Gauss--Seidel与SOR、SSOR、CG、MINRES、GMRES、BiCG、BiCGSTAB、LSQR、LSMR、标准与扩展Kaczmarz在直接求解方程时的主要条件、对一般不相容最小二乘的适用方式及需特别核对的条件，各方法注明所在小节。

#### 12.8.3 计算开销与收敛速度

1. 把总开销拆成准备、每步计算、迭代步数、额外存储和通信五部分（第`sec:ls-method-selection-cost`节）；设$\bm A$有$q$个非零元，矩阵向量积需$O(q)$次运算。指出Kaczmarz一步只访问一行，其步数不能与完整矩阵向量积直接比较，应报告遍历全部数据的次数或总算术量。

2. 给出稠密情形的运算量：LU分解约$\tfrac23d^3$，Cholesky与分块$\mathrm{LDL}^\top$约为其一半，每个右端两次三角求解约$2d^2$，故多右端应复用分解；矩形情形Householder QR约$2md^2-\tfrac23d^3$，经济型SVD同为$O(md^2)$但常数更大、换来奇异值与最小范数解等信息，正规方程法约$md^2$加$\tfrac13d^3$。稀疏分解成本由依赖排序的填充决定，不能套用稠密估计。

3. 以表`tab:ls-iterative-cost`列出不计预条件时CG、MINRES、GMRES、BiCG、BiCGSTAB、LSQR与LSMR每步的矩阵作用与工作存储，说明短递推只需固定个数向量，而GMRES保存全部基、第$k$步正交化约$4kd$次运算，重启与再正交化另计。

4. 分述各方法步数的决定因素：定常迭代看谱半径，CG看误差$\bm A$范数最小性、$\sqrt{\kappa_2(\bm A)}$与特征值聚簇，GMRES对非正规矩阵不能只看特征值且重启可能停滞，LSQR、LSMR由$\bm A$的奇异值分布决定（相当于对$\bm A^\top\bm A$用CG），Kaczmarz由行法向夹角与访问顺序决定。由此要求在同一问题、同一停止要求下按总成本比较，不以单步便宜、条件数较小或单次算例宣布普遍更快。

#### 12.8.4 数值稳定性

1. 区分问题病态、有限精度下的算法行为与提前停止误差三种来源（第`sec:ls-method-selection-stability`节）；回用满列秩下$\kappa_2(\bm A)$的定义与条件数平方关系（式`eq:matrix-analysis-normal-equation-condition-square`），以第`sec:ls-numerical-stability`节的残差、前向误差与后向误差为比较标准。指出LSQR、LSMR不形成正规矩阵改善的是计算路线，不消除原问题的病态。

2. 按目标核验：相容方程查原残差与尺度化容差，不相容最小二乘查原残差与正规残差，需最小范数时查初值与零空间处理（如Krylov方法与Kaczmarz从零初值出发时迭代量留在$\operatorname{range}\bm A^\top$中）。说明有限精度下递推残差可能偏离重新计算的$\bm b-\bm A\bm x_k$，预条件后的残差范数也可能不同，最终应回到原数据重算残差。

3. 把风险对应到算法步骤并给出处理办法：直接分解监测增长因子或改用正交分解，Krylov基失去正交时再正交化或以真实残差核验，过小递推分母须区分收敛与失效后重启或换用GMRES、MINRES，重启GMRES停滞时增大重启长度或改进预条件，标准Kaczmarz用于不相容系统时改用扩展版本或LSQR；由此说明这些偏差不宜统称为“不稳定”。

4. 回到预条件是否仍解同一问题（第`sec:ls-preconditioning`节）：相容方程上左右预条件不改变解；不相容最小二乘左乘$\bm M^{-1}$后变为以$(\bm M\bm M^\top)^{-1}$为权的加权最小二乘（第`sec:ls-weighted-ls`节）；秩亏问题右换元后对应使$\lVert\bm N\bm x\rVert_2$最小的解，一般不是原坐标的最小范数解。因此比较预条件须结合第`sec:ls-solution-selection`节的目标与选解准则。

#### 12.8.5 典型场景中的取舍

1. 可保存并分解矩阵的中小型或多右端问题，先比较直接分解：对称正定用Cholesky，对称不定用分块$\mathrm{LDL}^\top$，一般方阵用部分主元LU，低秩修改用Woodbury（第`sec:ls-method-selection-scenarios`节）。大型稀疏方程按结构选CG、MINRES、GMRES或BiCGSTAB并配预条件；定常迭代作为独立求解器往往较慢，但准备成本低、更新局部、易实现，常用作预条件或平滑步骤。

2. 大型稀疏、长方或不相容最小二乘用LSQR或LSMR，它们只需$\bm A\bm v$与$\bm A^\top\bm u$、保留原始矩形问题并以有限向量存储迭代，也能有效求解方程，不能笼统断言在方阵上效率更低。但原方阵可直接用CG、MINRES时，后者每步一次矩阵作用、收敛由$\bm A$本身的谱决定，通常更有优势；实际取舍还取决于预条件、访问成本和目标精度。

3. 只能逐行读取、观测按行到达或行非常稀疏时，Kaczmarz单步成本最低但全局收敛可能很慢，应按遍历数据次数比较；标准Kaczmarz首先是相容方程的行投影方法，处理不相容最小二乘须用扩展版本并计入列校正成本。最后把所有比较收回到第`sec:ls-solution-selection`节的求解目标与选解准则以及第`sec:ls-numerical-sensitivity`节的误差要求。


### 12.9 Sylvester方程

1. 第`sec:ls-matrix-equations`节以问题进入：未知量是矩阵$\bm X$且同时受左乘和右乘时，怎样判断可解、怎样保持矩阵形状求解。路线是从$\bm A\bm X=\bm C$、$\bm A\bm X\bm B=\bm C$进入$\bm A\bm X+\bm X\bm B=\bm C$，先用向量化确认其线性，再借第`sec:ls-general-square-spectrum`节的谱与实Schur形给出条件和算法；可解性看线性算子是否可逆，计算利用左右结构，不以形成Kronecker系数矩阵为默认算法。

#### 12.9.1 矩阵未知量与线性算子

1. 定义矩阵方程，并与单侧方程$\bm A\bm X=\bm C$（共用系数的多右端方程）和两侧系数可逆的双侧方程$\bm A\bm X\bm B=\bm C$（两次“除法”互不干扰）对照，引出Sylvester方程$\bm A\bm X+\bm X\bm B=\bm C$。标明$\bm A$、$\bm B$、$\bm C$、$\bm X$的尺寸，说明$\bm A$作用在列上、$\bm B$作用在行上；两项相加后左乘$\bm A^{-1}$只得到$\bm X+\bm A^{-1}\bm X\bm B=\bm A^{-1}\bm C$，不能分别“除以”两个系数。

2. 由分配律，$\mathcal L(\bm X)=\bm A\bm X+\bm X\bm B$是$\mathbb R^{m\times d}$上的线性算子；用第`sec:ls-kronecker-products`节的恒等式$\operatorname{vec}(\bm A\bm X\bm B)=(\bm B^\top\otimes\bm A)\operatorname{vec}\bm X$，把两项分别看成$\bm A\bm X\bm I_d$与$\bm I_m\bm X\bm B$，得到向量化方程式`eq:ls-sylvester-vectorized`。该表达使线性方程的判据都适用，也便于用LU（第`sec:ls-lu`节）核验小例子；但系数矩阵$\bm K$有$(md)^2$个元素、稠密消元约需$\tfrac23(md)^3$次运算，大规模求解应保留矩阵形状。

#### 12.9.2 存在唯一性的谱条件

1. 单侧方程沿用列空间判据$\operatorname{rank}[\bm A\ \bm C]=\operatorname{rank}(\bm A)$，双侧方程用向量化后$(\bm B^\top\otimes\bm A)\operatorname{vec}\bm X=\operatorname{vec}\bm C$的增广秩判据。两侧可逆时唯一解为$\bm A^{-1}\bm C\bm B^{-1}$；任一侧秩亏时可能无解，有解也可沿零空间变动而不唯一。

2. 以对角情形说明Sylvester方程不能逐侧处理：方程按元素分解为$(\lambda_i+\mu_j)x_{i,j}=c_{i,j}$，分母非零时得式`eq:ls-sylvester-diagonal-closed-form`；某个$\lambda_i+\mu_j=0$时，按$c_{i,j}$是否为零分别无解或可任取。由此看出关键是$\bm A$与$-\bm B$的特征值是否重合（图`fig:ls-sylvester-separation`以实轴示意谱分离），一般情形要在复数域检查，并引入记号$\operatorname{spec}(\bm A)$。

3. 定理`thm:ls-sylvester-unique-solvability`陈述：方程对每个$\bm C$唯一可解，当且仅当谱分离条件式`eq:ls-sylvester-spectral-separation`成立，即任意$\lambda+\mu\neq0$。

4. 证明先由秩零度定理把唯一可解归结为齐次方程只有零解即$\det\bm K\neq0$，并说明可在复数域讨论。必要性取$\bm A\bm u=\lambda\bm u$、$\bm B^\top\bm w=-\lambda\bm w$，构造非零解$\bm u\bm w^\top$；充分性由$\bm A\bm X=\bm X(-\bm B)$推出$p(\bm A)\bm X=\bm X\,p(-\bm B)$，取$p$为$\bm A$的特征多项式，用Cayley--Hamilton定理`thm:ls-cayley-hamilton`得$p(\bm A)=\bm0$，而$p(-\bm B)$各因子可逆，故$\bm X=\bm0$。

5. 指出谱条件与$\bm A$、$\bm B$各自是否可逆无关：$\bm A=\bm0$、$\bm B=\bm I_d$时仍唯一可解，$1\times1$的$\bm A=2$、$\bm B=-2$都可逆却退化。再区分唯一性与敏感性：最小$|\lambda_i+\mu_j|$越小误差放大越多，矩阵远离正规时即使谱和远离零也可能敏感，原因留待第`sec:ls-sylvester-diagonalizable`节说明。

#### 12.9.3 基于Schur分解的求解

1. 介绍Bartels--Stewart算法的思路：与解三角方程组相同，先用正交相似把两个系数化为准上三角形，使未知元有先后依赖、可按列回代，而正交变换不改变特征值和残差大小。下文在谱条件式`eq:ls-sylvester-spectral-separation`成立的前提下展开。

###### paragraph：实Schur分解

1. 第一步分别作实Schur分解$\bm A=\bm U\bm T\bm U^\top$、$\bm B=\bm V\bm S\bm V^\top$（定理`thm:ls-real-schur`），$\bm T$、$\bm S$的对角块为$1\times1$或$2\times2$；这一步只依赖系数，与右端无关。

###### paragraph：变换右端与未知量

1. 承接两个Schur分解，左乘$\bm U^\top$、右乘$\bm V$，记$\bm Y=\bm U^\top\bm X\bm V$、$\bm D=\bm U^\top\bm C\bm V$，得到变换后的方程式`eq:ls-sylvester-transformed`；由于$\bm T$、$\bm S$与$\bm A$、$\bm B$同谱，新方程同样满足谱条件。

###### paragraph：逐列求解$\bm Y$

1. 先看上三角情形：比较式`eq:ls-sylvester-transformed`的第$j$列得$(\bm T+s_{j,j}\bm I_m)\bm y_j=\bm d_j-\sum_{\ell<j}s_{\ell,j}\bm y_\ell$，右端只用更靠左的列，故按列从左到右、每列用第`sec:ls-lu`节的回代从下往上，除数$t_{i,i}+s_{j,j}$是一对特征值之和，由谱条件非零。

2. 图`fig:ls-bartels-stewart-column-order`以当前列$j=3$画出这一依赖：$\bm S$第$j$列对角线以上的元素把已求出的列带进右端，对角元$s_{j,j}$并入当前列的三角系数，当前列从最后一行向上回代。

3. 含$2\times2$块时按对角块分块比较第$(i,j)$块，右端只含同一块列中更靠下的块和更靠左的块列，故按块列从左到右、每块列从下到上计算；每个局部问题是至多四个未知量的小Sylvester方程，借式`eq:ls-sylvester-vectorized`化为至多$4$阶方程直接消元。

###### paragraph：恢复原未知量

1. 最后令$\bm X=\bm U\bm Y\bm V^\top$，并在原方程中计算残差$\bm A\bm X+\bm X\bm B-\bm C$：精确算术下为零，浮点中其Frobenius范数与新坐标中的残差相同（由下文定理给出），可直接用来检验整个流程。

2. 示例`ex:ls-bartels-stewart-2x2`取特征值为$2,1$的二阶$\bm A$与上三角$\bm B$（$-\bm B$的特征值为$-1,-3$），由特征向量$(3,4)^\top$构造正交$\bm U$得上三角$\bm T$，$\bm V=\bm I$、$\bm S=\bm B$；算出$\bm D=\bm U^\top\bm C$后先解第$1$列、再以$\bm d_2-s_{1,2}\bm y_1$为右端解第$2$列，每列从下往上回代，变回得$\bm X$并核验残差为零，演示上一段的列次序。

###### paragraph：正确性

1. 以一句过渡说明：上面的推导表明每一步都能进行、按次序算出的块满足各自的块等式，合起来即得算法正确性与残差检验的依据。

2. 定理`thm:ls-bartels-stewart`陈述三点：按块列从左到右、块列内从下到上的次序，每个局部方程$\bm T_{i,i}\bm Y_{i,j}+\bm Y_{i,j}\bm S_{j,j}=\bm E_{i,j}$唯一可解；由此算出的$\bm Y$是式`eq:ls-sylvester-transformed`的唯一解，$\bm X=\bm U\bm Y\bm V^\top$是原方程的唯一解；对任意$\bm Z$及$\bm W=\bm U^\top\bm Z\bm V$，原坐标与新坐标的残差Frobenius范数相等。

3. 证明先由$\bm A\bm Z+\bm Z\bm B-\bm C=\bm U(\bm T\bm W+\bm W\bm S-\bm D)\bm V^\top$及正交矩阵保持Frobenius范数得第三条；再由准上三角矩阵的特征值是各对角块特征值之并、$\bm T$与$\bm A$相似，说明每个局部方程满足谱条件，由定理`thm:ls-sylvester-unique-solvability`得第一条；最后由各块等式的右端只含已算出的块，合起来即式`eq:ls-sylvester-transformed`，结合唯一性与第三条（取$\bm Z=\bm X$）得第二条。

###### paragraph：计算代价

1. 比较代价：实Schur分解约$25m^3$与$25d^3$次运算，变换右端与变回原坐标各约$2(m^2d+md^2)$次，逐列回代约$m^2d+md^2$次，存储$O(m^2+d^2+md)$；$m=d=100$时总量约$6\times10^7$次，而对式`eq:ls-sylvester-vectorized`作稠密LU约需$7\times10^{11}$次并存储$10^8$个数。多组右端共用系数时，两个Schur分解只做一次，每个新右端只增加$O(m^2d+md^2)$。

#### 12.9.4 可对角化系数的特殊情形

1. 引出特殊情形：$\bm A$、$\bm B$都可对角化时，设$\bm A=\bm P\bm\Lambda\bm P^{-1}$、$\bm B=\bm R\bm M\bm R^{-1}$，可以换到各自的特征基，把方程化为对角情形。

###### paragraph：换到特征基

1. 记$\bm Y=\bm P^{-1}\bm X\bm R$、$\bm D=\bm P^{-1}\bm C\bm R$，由$\bm P^{-1}\bm A=\bm\Lambda\bm P^{-1}$与$\bm B\bm R=\bm R\bm M$把方程化为$\bm\Lambda\bm Y+\bm Y\bm M=\bm D$；计算$\bm D$时不求逆，先对$\bm P$作LU后解$\bm P\bm Z=\bm C$，再令$\bm D=\bm Z\bm R$。

###### paragraph：逐元素相除

1. 对角方程按式`eq:ls-sylvester-diagonal-closed-form`逐元素求解$y_{i,j}=d_{i,j}/(\lambda_i+\mu_j)$，谱条件保证所有分母非零。

###### paragraph：恢复原未知量

1. 次序与换基相反：先算$\bm W=\bm P\bm Y$，再用$\bm R$的LU分解解$\bm X\bm R=\bm W$。实矩阵有复特征值时$\bm P$、$\bm R$为复矩阵，全程用复数运算，最后舍去舍入产生的虚部。

2. 示例`ex:ls-sylvester-eigenbasis`取二阶上三角$\bm A$、$\bm B$，两者共用特征基，四个分母为$4,5,5,6$；依次算出$\bm D$、$\bm Y$、$\bm X$并代回核验残差为零。再把$\bm B$的$(1,1)$元改为$-2$，使$\lambda_2+\mu_1=0$，展示该位置按$d_{2,1}$是否为零而无解或不唯一。

###### paragraph：数值敏感度

1. 说明这条路线只在特征基接近正交时可靠：由$\lVert\bm Y\rVert_{\mathrm F}\leq\lVert\bm D\rVert_{\mathrm F}/\delta_{\min}$和双侧乘积的范数界只能得到含$\kappa_2(\bm P)\kappa_2(\bm R)/\delta_{\min}$的上界，故斜基下谱和远离零不独自保证良好条件；换基的中间量也可能放大到$\kappa_2(\bm P)$量级，并以特征向量几乎平行的二阶矩阵为例。实对称时谱定理`thm:ls-real-symmetric-spectral`给出正交特征基，元素公式可靠；一般情形宜用第`sec:ls-sylvester-schur`节的正交Schur变换。


### 12.10 Lyapunov方程

1. 第`sec:ls-lyapunov`节接续第`sec:ls-convergence`节的反复作用$\bm x_{k+1}=\bm A\bm x_k$，提出能否用一个矩阵$\bm X$把每步$\bm x_k^\top\bm Q\bm x_k$的累计量写成$\bm x_0^\top\bm X\bm x_0$。本节由离散累计引出Lyapunov方程，再讨论连续型方程、保持对称结构的求解与正定解条件；离散论证只用矩阵幂和级数，连续型正定解的积分证明推后。

#### 12.10.1 离散型与连续型方程

1. 对$\bm Q=\bm Q^\top\succeq0$，有限累计$\bm X_N=\sum_{k=0}^{N}(\bm A^\top)^k\bm Q\bm A^k$与初值无关并满足$\bm X_{N+1}=\bm Q+\bm A^\top\bm X_N\bm A$，其极限应满足离散型Lyapunov方程式`eq:ls-discrete-lyapunov`，即矩阵空间上固定更新的不动点方程。指出它不是替换系数后的Sylvester方程，向量化系数为$\bm I-\bm A^\top\otimes\bm A^\top$，唯一可解当且仅当任意两特征值$\lambda_i\lambda_j\neq1$：必要性仿定理`thm:ls-sylvester-unique-solvability`构造$\bm w\bm v^\top$，充分性仅说明可仿照多项式论证；下文只需$\rho(\bm A)<1$的情形，此时唯一性可直接证明。

2. 引理`lem:ls-discrete-lyapunov-uniqueness`陈述：$\rho(\bm A)<1$时方程式`eq:ls-discrete-lyapunov`至多有一个解，$\bm Q$对称且解存在时解对称。证明由两解之差满足$\bm X=(\bm A^\top)^k\bm X\bm A^k$与定理`thm:ls-power-decay`得$\bm X=\bm0$，再对方程转置并用唯一性得对称；级数的收敛与正定性留到第`sec:ls-lyapunov-positivity`节。

3. 在Sylvester方程中取$\bm B=\bm A^\top$、右端对称，得到连续型方程式`eq:ls-continuous-lyapunov`；因$\bm A^\top$与$\bm A$同谱，谱条件变成$\bm A$自身特征值两两之和的条件。

4. 定理`thm:ls-continuous-lyapunov-unique`陈述：方程对每个$\bm Q$唯一可解当且仅当$\bm A$的任意两个特征值（可相同）之和不为零，此时$\bm Q$对称则解对称。证明由$\operatorname{spec}(-\bm A^\top)=-\operatorname{spec}(\bm A)$把条件式`eq:ls-sylvester-spectral-separation`化为谱和条件并引用定理`thm:ls-sylvester-unique-solvability`，对称性由转置后$\bm X^\top$也是解及唯一性得到。

5. 特征值实部全负只是唯一性的充分条件，以$\bm A=\operatorname{diag}(1,2)$为反例说明不必要。这里先作为矩阵方程求解，与连续演化和累计积分的关系在后续过程理论中建立。

#### 12.10.2 保持结构的求解与检验

###### paragraph：实Schur变换

1. 两类方程都只需对$\bm A$作一次实Schur分解，令$\bm Y=\bm U^\top\bm X\bm U$、$\bm D=\bm U^\top\bm Q\bm U$（仍对称），离散型化为$\bm Y-\bm T^\top\bm Y\bm T=\bm D$，连续型化为$\bm T\bm Y+\bm Y\bm T^\top=\bm D$，且由唯一性$\bm Y$对称。下面先设$\bm T$上三角，从依赖关系分别推出计算次序。

###### paragraph：离散型：从左到右前代

1. 离散型比较第$j$列得$(\bm I-t_{j,j}\bm T^\top)\bm y_j=\bm d_j+\bm T^\top\sum_{\ell<j}t_{\ell,j}\bm y_\ell$，右端只用更靠左的列，故按列从左到右、每列用下三角系数从上到下前代，除数$1-t_{i,i}t_{j,j}$由$\lambda_i\lambda_j\neq1$保证非零。

###### paragraph：连续型：从右到左回代

1. 连续型比较第$j$列得$(\bm T+t_{j,j}\bm I)\bm y_j=\bm d_j-\sum_{\ell>j}t_{j,\ell}\bm y_\ell$，右端用更靠右的列，故按列从右到左、每列从下到上回代，除数为$t_{i,i}+t_{j,j}$。两者方向相反，源于离散型右乘上三角的$\bm T$而连续型右乘下三角的$\bm T^\top$。

###### paragraph：利用对称性并恢复原坐标

1. 利用对称性只算一半未知量：连续型算到第$j$列时$i>j$的元素已在右边各列求出，只算$i\leq j$的部分，离散型只算$i\geq j$的部分，未知量由$d^2$减为$d(d+1)/2$。含$2\times2$块时成对处理行和列，每次解至多四个未知量的局部方程；最后$\bm X=\bm U\bm Y\bm U^\top$，总代价由一次Schur分解主导，为$O(d^3)$。

2. 示例`ex:ls-discrete-lyapunov-recursion`取特征值为$1/2,0$的上三角$\bm A$与$\bm Q=\bm I$，可取$\bm U=\bm I$；先由下三角系数从上往下解第$1$列，再在第$2$列用对称性只取第二个分量，得$\bm X$并核验$\bm X-\bm A^\top\bm X\bm A=\bm I$。又因$\rho(\bm A)<1$，以$\bm x_0=(0,1)^\top$的累计量$\sum_k\lVert\bm x_k\rVert_2^2=7/3$核对$x_{2,2}$，回应本节开头的累计解释。

3. 示例`ex:ls-continuous-lyapunov-schur`取特征值为$-1,-3$的二阶$\bm A$，由特征向量$(1,1)^\top$构造正交$\bm U$得到上三角$\bm T$与$\bm D$；按连续型次序先解第$2$列的局部系统，再用对称性解第$1$列，得$\bm Y=\operatorname{diag}(3,1)$，变回得$\bm X$并核验残差为零、$\bm X$对称。

###### paragraph：对称性与正定性检验

1. 对需要正定解的应用，另检查对称性与正定性并合起来解释：对称化只消除舍入量级的不对称，解是否正确看相对残差；Cholesky分解（第`sec:ls-cholesky`节）在浮点中成功只说明相近的对称矩阵正定（第`sec:ls-numerical-stability`节），只有$\lambda_{\min}(\bm X)$明显大于舍入量级时才能据此判定，否则还要结合残差容差和问题是否保证正定（第`sec:ls-lyapunov-positivity`节）。上例的Cholesky分解成功，$\bm X\succ0$。

#### 12.10.3 正定解及其条件

1. 以一句过渡说明：$\rho(\bm A)<1$时，离散型方程的解就是第`sec:ls-lyapunov-solvability`节累计量$\bm X_N$的极限。

2. 定理`thm:ls-discrete-lyapunov-series`陈述：$\rho(\bm A)<1$、$\bm Q$对称时，级数式`eq:ls-discrete-lyapunov-series`收敛且是方程式`eq:ls-discrete-lyapunov`的唯一解；$\bm Q\succeq0$时$\bm X\succeq0$，$\bm Q\succ0$时$\bm X\succ0$。

3. 证明取$r\in(\rho(\bm A),1)$，由引理`lem:ls-power-geometric-bound`把第$k$项范数控制在$\lVert\bm Q\rVert_2C_r^2r^{2k}$，再由定理`thm:ls-absolute-series-convergence`得级数绝对收敛。用映射$\mathcal M(\bm Y)=\bm A^\top\bm Y\bm A$的连续性对部分和逐项作用，移项相消得$\bm X_N-\mathcal M(\bm X_N)=\bm Q-(\bm A^\top)^{N+1}\bm Q\bm A^{N+1}$，令$N\to\infty$即得方程，唯一性由引理`lem:ls-discrete-lyapunov-uniqueness`给出。各项可写成$(\bm A^k\bm x)^\top\bm Q(\bm A^k\bm x)$，由此得半正定；$\bm Q\succ0$时首项为正、其余非负，得正定。

4. 用标量情形核对符号和分母：$|a|<1$时$x=q/(1-a^2)$满足$x-a^2x=q$，分母对应唯一性条件中的$1-\lambda\lambda$，$q>0$时$x>0$。

5. 连续型写成$\bm A\bm X+\bm X\bm A^\top=-\bm W$，陈述特征值实部全负且$\bm W\succ0$时唯一解正定，并以标量方程和示例`ex:ls-continuous-lyapunov-schur`（$\bm W=\operatorname{diag}(2,10)$，解的特征值为$1,3$）核验。一般证明需把解写成$\int_0^\infty e^{t\bm A}\bm We^{t\bm A^\top}\,\mathrm dt$，用到矩阵指数、导数和无穷积分，指向卷三“常微分方程”章（`chap:ordinary-differential-equations`），本章求解算法不以它为前提。


### 12.11 本章小结

1. 第`sec:ls-equations-summary`节概括本章主题：已知输出反求输入，先是线性方程$\bm A\bm x=\bm b$，再是矩阵未知量的Sylvester方程与Lyapunov方程；线性方程部分依次回答要求什么解、怎样算、结果能信多少、怎样选方法四个问题。

2. 回收求解目标：由秩判断相容，解集为特解加$\operatorname{null}(\bm A)$；无解时求残差与列空间正交的最小二乘解，不唯一时取$\operatorname{range}(\bm A^\top)$中的最小范数解，伪逆$\bm A^\dagger\bm b$统一三种选解。加权最小二乘经白化化为普通情形，齐次最小二乘的解是最小右奇异向量。

3. 回收四类计算路线：直接法（部分选主元LU、Cholesky、分块LDL、Schur补、Woodbury复用分解，最小二乘用正规方程或QR并比较Householder、Givens与修正Gram--Schmidt）；定常迭代的收敛由迭代矩阵谱半径决定；Krylov方法按不同准则在$\bm x_0+\mathcal K_k$中选近似，含LSQR、LSMR与预条件的作用；Kaczmarz及其扩展版本分别在相容时收敛和收敛到最小二乘解。

4. 回收可信度与方法选择：条件数刻画数据扰动放大，残差小不等于误差小，前向误差约不超过条件数乘后向误差；正规方程使条件数平方，伪逆在秩变化处不连续，岭回归与截断SVD以拟合误差换稳定。选方法时先固定目标，再按结构、数据访问、开销、收敛速度和稳定性比较。

5. 回收矩阵方程：Sylvester方程唯一可解当且仅当$\bm A$与$-\bm B$无公共特征值，求解用实Schur分解逐列回代而不形成Kronecker系数矩阵，特征坐标路线在特征向量病态时放大误差。Lyapunov方程是对称特例，只需算一半未知量；离散型在$\rho(\bm A)<1$时有级数解，并由此读出右端正定时解正定。

## 第13章 多元函数微分

正文入口：[06-multivariate-differentiation.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/06-multivariate-differentiation.tex)（章首与第13.7节本章小结）；章内依次输入[01-multivariable-differentiation.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/06-multivariate-differentiation/01-multivariable-differentiation.tex)（第13.1–13.4节）、[02-matrix-perturbation.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/06-multivariate-differentiation/02-matrix-perturbation.tex)（第13.5节）与[03-implicit-inverse-functions.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/06-multivariate-differentiation/03-implicit-inverse-functions.tex)（第13.6节）。

1. 从一元导数是“输出改变量与输入改变量之比的极限”出发，指出平板温度、模型损失、逆矩阵与行列式等量同时依赖多个输入，需要把变化率推广到多个输入。

2. 以$f(x,y)=x^2+xy+y^2$为地形高度，说明从一点出发可以向东、向北、斜向或沿弯曲路线靠近；提出本章的两个问题：能否用一个线性映射统一预测所有走法下的输出变化、它在什么条件下成立；对一次有限扰动，这个预测会被放大多少、又还差多少。

3. 说明前几章从两个方向准备了材料：第10章建立收敛、极限与连续，证明有限维范数等价与完备，定义算子范数、对偶范数与伴随；第11、12章不借助微分，直接比较精确变化$F(\bm x+\bm h)-F(\bm x)$，得到条件数、谱的有限扰动界及逆矩阵与方程解的误差界。本章新增的问题是把精确变化分成对$\bm h$线性的一阶响应与更小的余项，并指出有限变化有界不保证这种分解存在。

4. 交代六节的分工与次序：13.1由偏导数、方向导数判断何时组成全微分，梯度是全微分在指定内积下的表示；13.2用Jacobian记录向量输出的微分，用伴随解释梯度沿复合的传递，用导数的算子范数估计有限增量；13.3只用一阶微分说明局部条件数等于微分的算子范数，并由导数的变化估计余项，因而放在Hessian之前；13.4得到Hessian、多元Taylor公式与驻点判别；13.5以矩阵为变量逐个分析乘积、求逆、行列式与对数行列式；13.6从方程出发建立隐函数定理，证明简单特征值及特征向量可微，再得到局部反函数定理。

5. 列出所用前置章节（第8章的运算、迹与行列式，第9章的线性映射、多线性映射与对偶空间，第10章的极限、连续、范数与内积，第11章的特征值、奇异值与扰动界，第12章的方程误差分析，以及一元微分章），说明下一章研究多维累计，并给出两份参考文献。

### 13.1 多元标量函数的一阶微分

1. 承接10.2只问函数值是否趋近的极限与连续，说明本节度量函数值变化的快慢：先沿直线把多元函数化为一元函数得到偏导数与方向导数，再判断这些方向信息何时组成对全部小扰动有效的全微分，然后借对偶空间与内积把全微分表示为梯度，最后沿线段用一元中值定理把梯度大小化为有限变化的界。

2. 限定研究开集$U\subseteq\mathbb R^d$上的实值函数，说明开集保证从基点出发向任何方向走足够小的一步仍在定义域内，双侧差商因而有意义。

#### 13.1.1 偏导数与方向导数

1. 固定除$x_j$以外的坐标得到一元函数，给出偏导数定义`def:multivariable-partial-derivative`；用竖直平面截曲面所得截线的切线斜率和“向正东移动时温度的变化”解释其几何含义。

2. 说明计算时把其余坐标当作常数；示例`ex:multivariable-quadratic-partials`对$x^2+xy+y^2$求得$f_x=2x+y$、$f_y=x+2y$，在$(1,2)$处为$4,5$，并用定义和数值$f(1.01,2)=7.0401$等核对。

3. 指出每个偏导数只描述自己那条坐标切片；同时走$(0.01,0.01)$时增量约为$0.04+0.05$，像是两个偏导数贡献之和，但这种相加并非总是成立，保证它的可微性留给13.1.2。

###### paragraph：方向导数

1. 让多个坐标按固定向量比例共同移动，得到另一条直线上的一元切片，给出方向导数定义`def:multivariable-directional-derivative`，用“沿地图方向前进时脚下的坡度”解释；说明$\bm v=\bm e_j$回到偏导数，定义采用双侧极限，单侧方向导数是另一概念，边界点只能讨论指向内部的单侧差商，本章只在开集内部使用双侧定义。

2. 说明方向向量不必是单位向量，此时导数按参数$t$计量，表示每单位水平距离的变化率须取单位向量；示例`ex:multivariable-diagonal-directional-derivative`由$f(1+t,2+t)=7+9t+3t^2$得沿$(1,1)^\top$为$9$，改用同向单位向量得$9/\sqrt2$。

3. 由两个方向向量描述同一直线、只是参数速度不同，提醒比较变化率前先统一归一化；再指出$9=4\cdot1+5\cdot1$恰为偏导数按方向分量加权之和，提出这些切片变化率能否组成对所有方向乃至方向不断改变的扰动都有效的线性近似，引出下一小节。

#### 13.1.2 全微分与可微性判别

1. 从一元可微$f(a+h)=f(a)+f'(a)h+o(h)$即图像放大后像切线出发，说明两个输入时对应的是切平面；预测规则应与扰动的叠加和数乘相容，故用线性映射，遗漏的误差还须比扰动长度小得多。

2. 给出可微性与全微分定义`def:multivariable-total-differential`（式`eq:analysis-total-differentiability`）；写出余项条件，说明$\bm h\to\bm0$按10.2.3的联合极限理解，强调同一个$A$适用于全部趋零扰动，而不是按方向分别控制误差；$d=2$时解释为曲面与切平面的高度差比水平距离小得多。

3. 示例`ex:multivariable-tangent-plane-error`：取$A(h,k)=4h+5k$，在$(0.01,0.02)$处误差与步长之比约$0.031$，步长减半后约$0.016$，说明这个比值随步长缩小而趋零正是余项条件的要求。

###### paragraph：可微性的要求与判别

1. 固定开集、函数与基点，说明下面依次讨论可微必然带来什么、一个便于核查的充分条件，以及区分偏导数存在、全部双侧方向导数存在、可微和连续可微的反例。

###### paragraph：可微的必要条件

1. 说明统一线性近似限制到一条直线上必须与该直线上的一元导数相同，函数增量也必须趋零，由此联系全微分与偏导数、方向导数。

2. 定理`thm:multivariable-differentiable-necessary`：可微蕴含连续、各偏导数存在、全微分唯一，$\mathrm df_{\bm a}(\bm h)=\sum_j\partial_jf(\bm a)h_j$且$D_{\bm v}f(\bm a)=\mathrm df_{\bm a}(\bm v)$。证明先由有限和的Cauchy--Schwarz不等式得线性项趋零（即10.3.4有限维线性映射的Lipschitz连续）从而连续，再取$\bm h=t\bm e_j$读出系数并得唯一性，最后取$\bm h=t\bm v$得方向导数公式。

3. 指出可微时候选线性映射已由偏导数确定，只需估计余项；示例`ex:multivariable-quadratic-differential`展开$f(1+h,2+k)=7+4h+5k+(h^2+hk+k^2)$，用$|hk|\leq(h^2+k^2)/2$把余项比控制在$\tfrac32\sqrt{h^2+k^2}$内，证明全微分为$4h+5k$并写出切平面。

4. 说明这个全微分同时给出示例`ex:multivariable-quadratic-partials`的偏导数与示例`ex:multivariable-diagonal-directional-derivative`的$9$；图`fig:analysis-process-total-differential-remainder`画出切平面及所有方向共同的余项界$r/2\leq R/r\leq3r/2$。

###### paragraph：偏导数连续给出的充分条件

1. 说明按定义估计余项通常不便，若各坐标变化率在基点附近连续变化，可沿坐标逐段走来共同控制增量；与必要条件不同，这是直接保证全微分存在的充分条件。

2. 定理`thm:multivariable-continuous-partials-sufficient`及证明：先在$d=2$时把增量拆成水平、竖直两段，各用一元中值定理写成$\partial_jf(\bm\xi_j)h_j$；一般维数拆成$d$段，误差不超过$\max_j|\partial_jf(\bm\xi_j)-\partial_jf(\bm a)|\sum_j|h_j|$，再由中间点趋于基点、偏导数在基点连续及$\sum_j|h_j|\leq\sqrt d\lVert\bm h\rVert_2$得余项为$o(\lVert\bm h\rVert_2)$。

3. 指出这只是充分条件，可微不要求系数随基点连续变化；实际计算中多项式、分母非零的有理函数及其与连续函数的复合可直接断定可微。

###### paragraph：连续可微函数

1. 由要求全微分系数随基点连续变化引出$C^1(U)$与$C^k(U)$，指出$C^1$函数处处可微而逆向不成立。

2. 示例`ex:multivariable-differentiable-not-c1`：$r(x)=x^2\sin(1/x^2)$在$0$处导数为$0$，取$x_n=(2\pi n)^{-1/2}$得$r'(x_n)=-2/x_n\to-\infty$，处处可微而导数在$0$附近无界；直观上振幅被压到零而振荡越来越快；令$f(\bm x)=r(x_1)$得到多元例子。

3. 用同一例子说明可微不保证局部Lipschitz连续（定义`def:ls-lipschitz`）：若在原点邻域内以$L$为常数，各点导数都应满足$|r'|\leq L$，与$r'(x_n)\to-\infty$矛盾。

###### paragraph：必要条件不能反推可微

1. 汇总可微蕴含连续、偏导数存在与全部双侧方向导数存在；对比一元情形导数存在即等价于可微，说明多元函数还须协调无穷多个方向与弯曲路径，这些必要条件单独或合起来都不保证可微，下面依次检查逆向。

###### paragraph：偏导数存在不保证可微

1. 示例`ex:analysis-partials-not-differentiable`：$xy/\sqrt{x^2+y^2}$沿坐标轴恒为零，偏导数为零，候选线性部分只能是零映射，但沿$(t,t)$余项与步长之比恒为$1/2$，故不可微。

2. 用极坐标$f=\tfrac r2\sin2\theta$说明曲面由斜率随方向变化的射线组成，像起伏的锥面，放大后形状不变、永不像平面；正向方向导数$ab/\sqrt{a^2+b^2}$存在但不是$\bm v$的线性函数，$ab\neq0$时双侧方向导数不存在，函数在原点连续。

3. 总结偏导数只看坐标轴，本例连同全部正向方向导数存在与连续也推不出可微，并提醒区分单侧与双侧定义。

###### paragraph：全部方向导数存在不保证可微

1. 说明把坐标切片换成所有固定直线后仍要检查两件事：方向变化率能否组成线性映射，以及是否有统一的余项控制；先看缺少线性性的情形。

2. 示例`ex:multivariable-nonlinear-directional-derivatives`：$x^3/(x^2+y^2)$的差商不依赖$t$，双侧方向导数全部存在且为$a^3/(a^2+b^2)$，但由偏导数$1,0$预测沿$(1,1)^\top$应为$1$，实际为$1/2$，不能拼成线性映射。

3. 对照前例只有单侧方向导数，本例失败只来自线性性；转入方向导数组成线性映射后仍可能缺少统一余项控制的情形。

4. 示例`ex:multivariable-linear-directionals-not-differentiable`：$x^3y/(x^4+y^2)$满足$|q|\leq|x|/2$故连续，所有双侧方向导数为零、组成零映射，但沿$(t,t^2)$余项比趋于$1/2$，不可微。

5. 回指10.2.3示例`ex:multivariable-parabola-path-limit`：函数沿抛物线有一道坡，每条直线都避开它；说明方向导数先固定方向再取极限，全微分则要求方向随扰动改变时误差仍受同一个控制。

###### paragraph：连续与偏导数存在互不蕴含

1. 用处处Lipschitz连续的$|x|$在原点关于$x$的双侧偏导数不存在说明连续推不出偏导数存在，用示例`ex:multivariable-path-limits`中原点置零的$xy/(x^2+y^2)$说明偏导数存在推不出连续；结论是二者互不蕴含，可微同时保证二者。

###### paragraph：条件之间的蕴含关系

1. 写出“邻域内连续可微$\Rightarrow$可微$\Rightarrow$全部双侧方向导数存在$\Rightarrow$全部偏导数存在”的蕴含链，逐条指出依据（两条定理与取坐标方向），并补充可微蕴含连续、方向导数关于方向线性。

2. 区分第一行前提涉及整个邻域、其余条件只涉及基点；逐个回指示例`ex:multivariable-differentiable-not-c1`、`ex:multivariable-nonlinear-directional-derivatives`、`ex:multivariable-linear-directionals-not-differentiable`与`ex:analysis-partials-not-differentiable`说明各箭头不能反向，并提醒不满足偏导数连续时应回到定义检查余项。

#### 13.1.3 微分的运算法则

1. 说明与一元情形一样从简单函数的微分组合复杂函数的微分；固定在基点可微的$f,g$与常数$c$，各法则统一用“代入一阶展开、整理线性项、确认余项仍为$o(\lVert\bm h\rVert_2)$”证明，同时读出全微分。

###### paragraph：和、差与数乘的微分

1. 把两个一阶展开相加，由线性映射之和仍线性、两个小量余项之和仍是小量，得到$\mathrm d(f+g)=\mathrm df+\mathrm dg$；同理得到差，固定系数只缩放线性项与余项，得到数乘法则（含常函数情形）。

###### paragraph：积的微分

1. 把两个带余项的展开相乘，说明其余各项要么含余项乘以有界量，要么是两个线性增量之积$O(\lVert\bm h\rVert_2^2)$，从而得到$\mathrm d(fg)=g(\bm a)\mathrm df+f(\bm a)\mathrm dg$；与一元$(fg)'=f'g+fg'$对照，解释两个变化同时发生的部分是高阶小量。

###### paragraph：商的微分

1. 由可微蕴含连续保证$g$在基点附近远离零，把$\delta=g(\bm a+\bm h)-g(\bm a)=O(\lVert\bm h\rVert_2)$代入$1/y$的一元展开得$\mathrm d(1/g)=-\mathrm dg/g(\bm a)^2$，再由积的法则得商的微分；指出分母非零既是定义条件也是估计余项的条件。

###### paragraph：标量复合函数的微分

1. 把内层增量代入外层一元函数的展开，由$\delta=O(\lVert\bm h\rVert_2)$使外层余项$o(|\delta|)$仍为$o(\lVert\bm h\rVert_2)$，得到$\mathrm d(\psi\circ f)=\psi'(f(\bm a))\mathrm df$；以$e^{-(x^2+y^2)}$为例说明外层只把内层全微分乘上一个正数。

###### paragraph：沿参数曲线的变化率

1. 换成外层多元、内层为参数曲线的复合，在各坐标于$t_0$可微、$f$在$\bm x(t_0)$可微的条件下给出式`eq:multivariable-curve-chain-rule`；推导中先由坐标展开得内层增量$\bm k=s\bm x'(t_0)+o(|s|)$，再代入$f$的展开并用全微分的线性。

2. 解释内层先产生速度向量、外层全微分再作用于它；取直线回到方向导数公式，并说明13.1.4用该式证明梯度与等值曲线切向正交，一般向量值复合留给13.2.2。

###### paragraph：二次型的微分

1. 说明平方误差、能量函数含二次型结构；对$q(\bm x)=\bm x^\top\bm A\bm x$把两个$\bm x$看作两个因子，用乘积法则并利用标量等于自身转置，得到$\mathrm dq_{\bm x}(\bm h)=\bm x^\top(\bm A^\top+\bm A)\bm h$及偏导数向量式`eq:analysis-quadratic-form-gradient`。

2. 说明$\bm A$对称时化为$2\bm A\bm x$，不对称时不能这样写；用$\bm A=\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]$即$q=x_1x_2$核对$(\bm A+\bm A^\top)\bm x=(x_2,x_1)^\top$，而$2\bm A\bm x$是错的。

###### paragraph：二次型的精确增量

1. 说明乘积法则只给出一阶项，对对称$\bm S$直接写出完整增量$2\bm x^\top\bm S\bm h+\bm h^\top\bm S\bm h$；由Cauchy--Schwarz与谱范数（10.3.4）得$|\bm h^\top\bm S\bm h|\leq\lVert\bm S\rVert_2\lVert\bm h\rVert_2^2$，余项受明确二次量控制，也独立证明了可微。

2. 以$x^2+xy+y^2$的$\bm S$特征值为$3/2,1/2$说明$\lVert\bm S\rVert_2=3/2$正是示例`ex:multivariable-quadratic-differential`中的余项常数；预告$\bm h^\top\bm S\bm h$在13.4成为Hessian二次型，梯度与余项估计将复用此例。

#### 13.1.4 梯度与内积

1. 说明全微分是$\mathbb R^d$上的线性泛函即对偶空间元素（9.4），不能画成输入空间中的箭头；由10.6.1的Riesz表示定理，选定内积后它等于与唯一向量的内积，给出梯度定义`def:multivariable-gradient`，未加说明时取标准欧氏内积。

2. 在标准内积下逐个取$\bm h=\bm e_j$，得到梯度的坐标式`eq:multivariable-gradient-coordinates`，从而$f(\bm a+\bm h)=f(\bm a)+\nabla f(\bm a)^\top\bm h+o(\lVert\bm h\rVert_2)$、$D_{\bm v}f=\nabla f^\top\bm v$；以$\nabla f(1,2)=(4,5)^\top$与一般二次型为例，说明梯度与输入同属一个空间，可画成地图平面上的箭头。

3. 由表示向量随泛函线性变化，把13.1.3的法则改写成梯度的和、数乘、积与复合法则，以$\nabla e^{-(x^2+y^2)}$指向原点为例。

###### paragraph：偏导数向量与梯度

1. 说明偏导数全部存在时本书也用$\nabla f$记这一列偏导数，但它此时只是坐标变化率的排列：示例`ex:multivariable-nonlinear-directional-derivatives`中这一列为$(1,0)^\top$却给不出沿$(1,1)^\top$的方向导数；只有确认可微后才能用内积计算任意方向导数并解释为最快上升方向，偏导数连续只是方便的充分判别。

2. 指出列向量的排列来自所选内积与坐标：标准内积把全微分系数原样排成列向量，换用其他内积时同一全微分由另一个向量表示。

###### paragraph：改变内积时的梯度

1. 设内积为$\bm x^\top\bm G\bm y$（10.4.2说明任何内积在坐标下都是这种形式，$\bm G$为Gram矩阵），由$\bm c^\top\bm h=\bm g^\top\bm G\bm h$对所有$\bm h$成立推出$\bm G\bm g=\bm c$，得式`eq:multivariable-gradient-gram`；强调系数向量由函数决定，改变的只是表示向量。

2. 示例`ex:multivariable-weighted-gradient`：$\bm G=\operatorname{diag}(4,1)$时梯度为$(1,5)^\top$，核对它给出同一全微分$4h+5k$，并解释加权长度使第一坐标方向的同样加权距离只需更小的坐标位移；与10.6.1“读取不变、表示随内积改变”的结论对应。

###### paragraph：最陡上升方向

1. 对所选内积诱导长度下的单位向量，由Cauchy--Schwarz不等式（定理`thm:linear-algebra-cauchy-schwarz`）得$D_{\bm u}f\leq\lVert\nabla f\rVert$，梯度非零时取其方向达到等号；结论是梯度方向上升最快、最大坡度为梯度长度、反方向下降最快，并用加权例子说明“最快”总相对某种长度而言。

###### paragraph：梯度与等值曲线

1. 由与梯度正交的方向导数为零进入；对落在等值集中、经过基点的可微曲线，用式`eq:multivariable-curve-chain-rule`求导得梯度与切向量正交。

2. 限定这里假定了这样的曲线存在，等值集在基点附近是否光滑需要13.6的隐函数定理与梯度非零条件；梯度为零只说明一阶项消失，局部形状留给13.4；图`fig:analysis-process-gradient-level-curves`对照梯度方向、等值曲线切向$(5,-4)^\top$与另一单位方向，并提醒比较前先归一化。

#### 13.1.5 中值估计与局部Lipschitz性

1. 说明微分只描述一点附近的变化，估计两点之间的有限变化要沿连接两点的线段把函数化为一元函数，前提是整条线段在定义域内；给出线段记号。

2. 定理`thm:multivariable-scalar-mean-value`及证明：令$\phi(t)=f(\bm x+t(\bm y-\bm x))$，其导数是沿$\bm y-\bm x$的方向导数，对$\phi$用一元中值定理；解释为一元“平均斜率等于某点切线斜率”的推广，并以$x^2+y^2$从原点到$(1,1)$的中值点为线段中点为例。

###### paragraph：局部Lipschitz性

1. 回指定义`def:ls-lipschitz`已给出Lipschitz与局部Lipschitz连续，说明本小节的新任务是由导数求出常数：中值公式把增量写成梯度与位移的内积，梯度长度有统一上界时即可用距离控制输出变化，并指出优化中常用这种控制。

2. 先给不依赖导数的例子：线性函数的常数是$\lVert\bm a\rVert_2$即梯度长度，欧氏范数由三角不等式以$1$为常数却在原点不可微，说明Lipschitz连续不要求处处可微。

3. 引入凸集，定理`thm:multivariable-gradient-lipschitz`：凸开集上可微函数以$L$为Lipschitz常数当且仅当梯度长度处处不超过$L$；充分性用中值公式与内积不等式，必要性沿梯度单位方向取单侧差商极限。几何上解释坡度与高度变化的关系，并以$\sin x+\cos y$的常数$\sqrt2$为例。

4. 示例`ex:multivariable-nonconvex-lipschitz-failure`：去掉负$x$轴的环形区域上极角函数梯度长度小于$1$，但负$x$轴两侧距离$2\varepsilon$的两点极角相差接近$2\pi$，不是Lipschitz函数；解释连接两点的线段穿过被去掉的部分，中值公式不能使用，故凸性不能省略。

5. 说明局部情形不需整体凸：$C^1$函数在基点附近闭球上梯度长度有界（定理`thm:multivariable-extreme-value`），在同心开球上用前述定理得局部Lipschitz；用$x^2$说明各点局部常数不一定有共同上界。

###### paragraph：三种控制的强弱

1. 比较已出现的三种结论：连续不给出趋近速度；可微给出$o(\lVert\bm h\rVert_2)$的渐近线性近似，但不说明给定有限步长的误差；梯度的统一界沿线段控制有限变化的大小，却不估计线性预测还差多少。指出13.3估计一阶余项时要结合后两者考察导数沿线段的变化，13.4再用二阶导数描述这种变化。

### 13.2 多元向量值函数的微分

1. 从每个输入只产生一个实数转到产生$m$个输出分量的映射$F:U\subseteq\mathbb R^d\to\mathbb R^m$，以极坐标映射、神经网络的一层、参数曲线与参数曲面为例，关心输入稍变时输出点整体怎样移动。

2. 说明可以逐个分量使用前面的结论，但每个分量仍须对全部输入方向整体扰动；本节先定义整体可微并引入Jacobian，再给出复合映射的导数，最后用导数的算子范数估计有限增量。

#### 13.2.1 向量值映射与Jacobian

1. 按输出分量给出多元向量值函数定义`def:multivariable-vector-function`；回用10.2.3、10.2.4已建立的极限与连续性（输出点整体接近等价于各分量接近），说明本节在连续性基础上研究线性近似。

###### paragraph：微分与Jacobian矩阵

1. 说明向量输出的全微分要把输入扰动映为$m$维输出扰动，有限维线性映射由矩阵表示，每行记录一个分量的系数；给出可微性与Jacobian矩阵定义`def:multivariable-vector-differential`（式`eq:analysis-jacobian-linearization`），余项按输出欧氏范数理解。

2. 证明向量值函数可微当且仅当各分量可微：正向取向量余项的分量，反向用欧氏范数合并有限个小量余项；由此Jacobian第$i$行是$\nabla F_i^\top$，微分唯一，并定义向量值$C^k$。

3. 说明列向量约定下Jacobian为“输出维数$\times$输入维数”，$\bm J_F\bm h$与输出同形；$m=1$时Jacobian是行向量$\nabla f^\top$，与列向量梯度互为转置。

###### paragraph：Jacobian矩阵的几何意义

1. 说明按行看是各分量的梯度，按列看第$j$列是只增加第$j$个输入时输出点的移动方向，一般扰动的一阶效果是各列按$h_j$加权求和。

2. 对$d=m=2$说明小正方形的像近似为两列张成的平行四边形，由8.3.1行列式的面积缩放含义得面积约$|\det\bm J_F|\varepsilon^2$，符号表示定向是否翻转。

3. 示例`ex:multivariable-polar-jacobian`：极坐标映射的Jacobian行列式为$r$，第一列是单位径向向量、第二列长度为$r$沿切向，小矩形变为面积约$r\,\mathrm dr\,\mathrm d\theta$的扇形块；说明离原点越远面积放大越多，14.3的区域积分换元用这个倍数校正面积。

4. 图`fig:analysis-process-jacobian-grid-cell`对一般非线性映射$T$对照弯边像块与线性像平行四边形，$\det J_T(a)=0.525$，说明有限块不与线性像重合，缩小扰动后才由可微余项控制差异。

5. 示例`ex:multivariable-helix-jacobian`：螺旋线的Jacobian是$3\times1$的切向量，长度$\sqrt2$表示参数每增加一单位点约移动$\sqrt2$；结论是Jacobian形状随输入输出维数改变，不能默认为方阵或有行列式，并预告13.4把梯度映射也作为向量值映射研究其微分。

###### paragraph：Jacobian矩阵的计算

1. 给出逐分量求偏导、按行排列并核对形状的做法，以$F(x,y)=(x^2+xy,y^2)^\top$在$(1,2)$处的一阶影响$(4h+k,4k)^\top$为例，按行、按列解读。

2. 引入softmax（归一化指数映射）把得分变为总和为$1$的正权重，由商法则推出式`eq:analysis-softmax-jacobian`；解释对角项为正、非对角项为负来自共同分母，$n=1$时Jacobian为零，每行和为零对应所有得分加同一常数不改变输出。

3. 示例`ex:multivariable-softmax-jacobian-check`：二维softmax在原点的Jacobian为$\tfrac14\left[\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right]$，提高$z_1$为$0.1$时线性近似$0.525$与实际$0.52498$只差约$2\times10^{-5}$，两分量增量一正一负、和为零。

#### 13.2.2 复合映射与导数的运算

1. 说明复杂映射的Jacobian由简单映射组合得到，列出各运算有定义的前提（输出同形才能相加，复合要求前一映射的输出落在后一映射的定义域内）；指出两个向量的乘法须先指定含义，先处理线性运算与复合，再用链式法则处理内积等乘法结构。

###### paragraph：和、差与数乘的微分

1. 逐分量使用标量的和、差与数乘法则，再按行排回矩阵，得到$\bm J_{F\pm H}=\bm J_F\pm\bm J_H$与$\bm J_{cF}=c\bm J_F$，并提醒输出与Jacobian形状须一致。

###### paragraph：复合函数的链式法则

1. 用输入扰动先被$F$变为$\bm J_F\bm h$、再被$G$变为$\bm J_G\bm J_F\bm h$的传递说明复合Jacobian是按计算顺序的乘积，引入术语链式法则。

2. 定理`thm:multivariable-vector-chain-rule`（式`eq:analysis-vector-chain-rule`）及证明：先说明中间量增量$\bm k$与$\bm h$同阶，再代入$G$的展开，分别用矩阵放大有界与$\lVert\bm k\rVert_2=O(\lVert\bm h\rVert_2)$控制两项余项。

3. 说明矩阵形状$(p\times m)(m\times d)$决定乘法次序，即使两种次序都有定义也不能交换；用局部伸缩解释复合的伸缩依次作用，方阵时面积缩放倍数由行列式乘法公式相乘。

###### paragraph：内积、范数平方与复合二次型

1. 把内积$F^\top G$看作映射$(F,G)$与双线性函数$b(\bm u,\bm w)=\bm u^\top\bm w$的复合；由$b$的精确增量中$\bm p^\top\bm r$是联合扰动的二次量得$b$可微，再由链式法则得$\nabla\phi=\bm J_F^\top G+\bm J_G^\top F$，特例为$\nabla\lVert F\rVert_2^2=2\bm J_F^\top F$与复合二次型的梯度$2\bm J_F^\top\bm SF$。

2. 单独判断范数本身：非零处是平方根与光滑函数的复合，梯度为$\bm x/\lVert\bm x\rVert_2$；原点处沿直线得$|t|\lVert\bm v\rVert_2$，双侧方向导数不存在，说明范数平方光滑推不出范数可微，因为平方根在$0$处不满足链式法则的条件。

3. 示例`ex:analysis-chain-rule-calculation`：$F(x_1,x_2)=(x_1^2,x_1x_2,x_2)^\top$与$\ell(\bm y)=\tfrac12\lVert\bm y\rVert_2^2$复合，由$\nabla L=\bm J_F^\top\nabla\ell(F)$在$(1,2)$处得$(6,4)^\top$，与直接展开一致；解释转置来自梯度按列书写，形状$(2\times3)(3\times1)$核对传递次序，链式形式保留中间映射便于分层计算与复用。

###### paragraph：梯度沿复合的传递与伴随

1. 说明上例中的转置是10.6的伴随：输入、输出各取内积，链式法则写成线性映射的复合，依次用梯度定义与伴随定义式`eq:ls-adjoint-pairing`，由梯度唯一性得式`eq:multivariable-gradient-adjoint`。

2. 解释微分把输入扰动推向输出端、伴随把输出端梯度拉回输入端；标准内积下伴随矩阵为$\bm J_F^\top$，回到上例，加权内积下由式`eq:ls-weighted-adjoint`为$\bm M_V^{-1}\bm J_F^\top\bm M_W$，与式`eq:multivariable-gradient-gram`相容；指出矩阵函数的梯度与隐函数的导数都沿用这一规则。

#### 13.2.3 向量增量与导数范数估计

1. 说明标量中值公式不能照搬到向量值函数：各分量的中值点可能不同；以单位圆参数化走完一圈增量为零而速度长度恒为$1$为例，改为估计增量长度或把增量写成沿线段的积分。

###### paragraph：导数的算子范数

1. 说明向量输出时同一线性映射在不同方向放大倍数不同，取最大者；回用10.3.4已定义且有限维时有限可达的算子范数，写出$\lVert\mathrm dF_{\bm a}\rVert$，两端欧氏范数时即Jacobian的谱范数，标量情形就是梯度长度；计算时先给对全部单位向量成立的上界，再找达到上界的方向。

2. 示例`ex:multivariable-diagonal-operator-norm`：由$4h_1^2+h_2^2\leq4$且$\bm e_1$取等得$\lVert\operatorname{diag}(2,1)\rVert_2=2$；补充旋转矩阵的算子范数为$1$。

3. 定理`thm:multivariable-vector-mean-value`（式`eq:analysis-operator-mean-value-bound`）及证明：在含线段的开集上连续可微时，把向量增量投影到自身单位方向得到标量函数，用链式法则与一元中值定理，再用内积不等式与谱范数的界；说明这样不再需要各分量共用中值点。

###### paragraph：向量增量的积分表示

1. 说明中值估计只给长度上界，在同样条件下逐分量用式`eq:multivariable-curve-chain-rule`与一元微积分基本定理，可精确写出式`eq:multivariable-vector-integral-increment`，各分量变化率沿整条线段累计而不需共同中间点。

2. 由积分的线性、单调性与Cauchy--Schwarz不等式证明向量积分的范数不超过范数的积分，用于积分表示再次得到式`eq:analysis-operator-mean-value-bound`；指出积分形式可先从被积函数中扣除固定线性项，13.3.2据此估计一阶余项。

###### paragraph：Lipschitz估计与压缩

1. 说明凸开集上Jacobian谱范数有统一界$L$时映射以$L$为Lipschitz常数，局部球上得局部版本；界$q<1$时称压缩，但压缩本身不保证迭代留在球内、也不单独给出不动点，还须检查自映射并借有限维完备性（定理`thm:ls-finite-dimensional-complete`）取极限，13.6证明隐函数定理时依次核对这三点。

### 13.3 微分与扰动分析

1. 把前两节的一阶预测与第11、12章不借助微分的精确变化比较（固定线性作用的误差比、谱与奇异值的有限变化、逆矩阵与方程解的有限扰动界）放在一起，写成$\Delta F=\mathrm dF_{\bm x}(\bm h)+R_{\bm x}(\bm h)$，提出两个问题：一阶误差在全部允许方向中最多放大多少，有限步长下一阶预测还差多少；前者由微分的算子范数回答，后者要控制导数沿扰动线段的变化。

2. 说明输入、输出取有限维赋范空间（如某种范数下的$\mathbb R^d$或按元素排成坐标的矩阵空间），由范数等价（定理`thm:ls-norm-equivalence`）可微与否不依赖范数，只有算子范数的数值依赖；13.5把本节结论逐个用于矩阵函数。

#### 13.3.1 局部条件数与导数范数

1. 回指11.9.2对固定线性作用的条件数只依赖扰动方向，说明非线性映射的误差比还随扰动大小改变，须先在半径$\delta$的扰动中取最坏情形再令半径缩小；固定基点、两端范数，并用非零线性子空间$\mathcal E$表示允许的结构化扰动方向。

2. 给出局部条件数定义`def:multivariable-local-condition-number`，说明内层上确界随$\delta$减小而不增，极限在$[0,\infty]$中存在；定义只用有限变化、不要求可微，也不同于沿某个给定方向的响应。

3. 定理`thm:multivariable-local-condition-number`及证明：可微时局部条件数等于微分限制在$\mathcal E$上的算子范数；记余项比的上确界为$\eta(\delta)\to0$，用三角不等式得上界$N+\eta(\delta)$，取达到算子范数的单位方向（10.3.4）并用反向三角不等式得下界$N-\eta(\delta)$，夹逼得结论。说明结构化扰动时最坏方向限于允许子空间，数值一般不大于无结构情形。

###### paragraph：相对条件数

1. 在参照量非零时乘以输入尺度、除以输出尺度定义相对条件数，衡量相对扰动在一阶上的放大倍数。

2. 对线性作用$\bm A\bm x$说明余项为零，绝对条件数为$\lVert\bm A\rVert$，相对条件数$\lVert\bm A\rVert\lVert\bm x\rVert/\lVert\bm A\bm x\rVert$在可逆时不超过$\kappa(\bm A)$，回到11.9.3的精确结论。

3. 区分三个易混的量：矩阵条件数$\kappa(\bm A)$是对全部输入的统一上界，固定输入处的相对条件数只涉及这一点，矩阵函数（如求逆）以矩阵为输入的条件数留给13.5计算；指出它们都描述问题本身的敏感性，与算法稳定性的分工见12.6.2。

###### paragraph：有限条件数而不可微

1. 反例：$\bm S(t)=\operatorname{diag}(t,-t)$排序后的最大特征值为$|t|$，由Weyl界（定理`thm:ls-weyl-eigenvalue`）有限变化受控，在$0$处局部条件数为$1$，却没有双侧导数；解释失去可微性的是“排序取最大”这一步，未排序的分支$t,-t$光滑并在$0$处相交，13.6.2将在特征值简单时证明所选局部分支可微。

2. 反方向说明局部条件数为零不表示输出不变：$t^2$在$0$处条件数为$0$，有限步长仍有变化$t^2$，被一阶分析遗漏的部分留给下一小节的余项界。

#### 13.3.2 一阶近似的余项界

1. 说明可微只保证余项为$o(\lVert\bm h\rVert)$，得到有限扰动的数值误差界需要知道导数沿线段怎样变化；约定本小节输入输出取欧氏范数、矩阵空间取Frobenius范数、导数用谱范数，其他范数借范数等价改变常数。

2. 在含线段的开集上连续可微时，从式`eq:multivariable-vector-integral-increment`中扣除常向量$\bm J_F(\bm x)\bm h$，得余项的精确积分表示式`eq:multivariable-remainder-integral`；对照完整增量由导数大小控制、余项由导数相对基点的变化控制，说明导数大而变化慢时增量大而一阶预测仍准确。

3. 定理`thm:multivariable-first-order-remainder-bound`及证明：Jacobian相对基点满足$L$倍的Lipschitz型界时，对积分表示取范数得余项不超过$\tfrac L2\lVert\bm h\rVert_2^2$；指出定理不以二阶导数存在为前提，凸邻域内Jacobian以$L$为Lipschitz常数即满足假设，13.4将说明二阶导数统一界是取得$L$的一种充分办法。

4. 说明上界正比于步长平方只表示所保证误差的量级，实际误差可能远小于上界；以对称二次型为例，定理给出的$\lVert\bm S\rVert_2\lVert\bm h\rVert_2^2$与13.1.3由精确增量得到的界一致。

###### paragraph：三种保证的分工

1. 归纳可微给出步长趋零时的$o(\lVert\bm h\rVert)$，导数的Lipschitz界给出带明确常数的二次余项，13.2.3的导数界控制整个有限变化；提醒使用后两者前须检查扰动线段留在定义域内、可逆或正定等结构条件在整条线段上保持、常数在该范围内统一成立。

2. 说明矩阵映射的这些检查可借第11章的Weyl界与奇异值扰动界、12.6.1的逆矩阵有限界完成；基点条件数只描述无穷小扰动，不能代替范围检查与余项估计。

### 13.4 高阶微分与局部形状

1. 承接上一节对一阶误差的估计，说明本节描述误差中最先保留的变化：切平面看不出曲面弯向哪边，碗底、山顶和马鞍点的切平面都是水平的；把13.2的向量值微分用于梯度映射以研究弯曲，并说明多线性映射、二次型和谱判别分别用于表示高阶导数、衡量二阶项和判断局部形状。

2. 交代路线：先把二阶偏导数集中为Hessian并解释为二阶微分，再借一元Taylor公式建立二阶近似，最后判断驻点类型。

#### 13.4.1 二阶偏导数、Hessian与高阶微分

1. 定义记号$f_{x_ix_j}=\partial_j(\partial_if)$，解释$f_{xx}$为切片的弯曲、$f_{xy}$为曲面的扭转；以$x^2+xy+y^2$及每条坐标切片都是直线却扭曲的$xy$为例，指出一般函数混合偏导数能否交换需要额外条件。

###### paragraph：混合偏导数的交换

1. 示例`ex:multivariable-mixed-partials-differ`：$xy(x^2-y^2)/(x^2+y^2)$由$f_x(0,y)=-y$、$f_y(x,0)=x$得两个次序的混合偏导数分别为$-1$与$1$。

2. 定理`thm:multivariable-mixed-partials`及证明：混合偏导数在邻域存在并在基点连续时可交换，$C^2$函数处处可交换；证明对小矩形四顶点的二阶差分按两种方式分组，各用两次一元中值定理得到不同中间点处的两种混合偏导数，令步长趋零并用连续性；回指反例说明缺少连续性时结论可能失败。

###### paragraph：Hessian矩阵

1. 把全部二阶偏导数排成方阵，给出Hessian定义`def:multivariable-hessian`，解释第$i$行是$\partial_if$偏导数向量的转置，即“梯度的梯度”；指出二阶偏导数存在不保证梯度映射有统一线性近似，二阶可微指$\nabla f$作为向量值映射可微。

###### paragraph：Hessian是梯度映射的Jacobian

1. 对$C^2$函数由定理`thm:multivariable-continuous-partials-sufficient`逐分量得梯度映射可微，$C^2$是二阶可微的充分条件；按Jacobian约定得$\bm J_{\nabla f}=\nabla^2f$，说明Hessian既是二阶偏导数表又是梯度映射微分的矩阵，描述基点移动时梯度怎样变化，$C^2$时对称。

2. 说明沿直线求两次导数得方向二次型$\bm v^\top\nabla^2f\bm v$（依据见Taylor定理的证明），它衡量切片曲线向上或向下弯；对二次函数$\tfrac12\bm x^\top\bm A\bm x+\bm b^\top\bm x+c$说明只有对称部分$\bm H$影响函数值，由式`eq:analysis-quadratic-form-gradient`得Hessian为常数矩阵$\bm H$。

3. 用$\operatorname{diag}(2,100)$说明狭长山谷与半轴之比$\sqrt{50}$，用$\operatorname{diag}(2,-100)$说明马鞍形；回指8.2.1的正定与半正定，补充负定、半负定与不定，对应碗形、倒扣的碗与马鞍。

4. 示例`ex:multivariable-hessian-definiteness`：配方证明$\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$正定，$\left[\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\right]$对角元为正却沿$(1,-1)^\top$为负、不定；说明判断定性须检查整个二次型，对角元只反映坐标轴方向。

###### paragraph：高阶微分的多线性形式

1. 说明Hessian可同时作用于两个方向：对固定$\bm h$把一阶变化看作基点的函数，沿$\bm k$求全微分得$D^2f_{\bm x}[\bm h,\bm k]=\bm h^\top\nabla^2f\bm k$，它是9.3意义下的对称双线性形式，两个方向相同时给出Taylor二次项。

2. 把$\bm x\mapsto\mathrm df_{\bm x}$看作取值于有限维泛函空间的映射，逐次求微分得$C^r$函数的$r$重线性形式，其系数就是$r$阶偏导数数组，与9.3多线性映射的坐标表示一致；以$x^2y$在$(1,2)$处的二次变化$4h_1^2+4h_1h_2$说明混合项使两条坐标轴的一元展开不能简单相加。

###### paragraph：二阶导数界与导数的Lipschitz性

1. 说明二阶微分为13.3.2的余项界提供常数：对$C^2$向量值映射定义$D^2F_{\bm x}[\bm h,\bm k]$（第$i$个分量为$\bm h^\top\nabla^2F_i\bm k$）及其范数$\lVert D^2F_{\bm x}\rVert$，最大值由连续函数在闭有界集上取到，标量时即Hessian的谱范数。

2. 定理`thm:multivariable-second-derivative-lipschitz`及证明：凸开集上二阶导数统一不超过$M$时Jacobian以$M$为Lipschitz常数；固定单位向量$\bm h$令$G(\bm z)=\bm J_F(\bm z)\bm h$，对$G$用积分表示并取范数，再对$\bm h$取最大值。

3. 结论：此时定理`thm:multivariable-first-order-remainder-bound`以$L=M$成立；强调这只是一种充分办法，余项估计本身只要求导数的Lipschitz界。

#### 13.4.2 多元Taylor展开与余项

1. 说明把多坐标同时改变的位移看作线段上的参数变化，沿线段用一元Taylor公式：一次项给出切平面，二次项为Hessian二次型补上弯曲；带Lagrange余项得中间点形式，再借二阶偏导数在基点的连续性得小量形式。

2. 定理`thm:multivariable-second-order-taylor`（式`eq:analysis-second-order-taylor`、`eq:analysis-second-order-local-model`）及证明：用方向导数公式两次算出$\phi'$与$\phi''=\bm h^\top\nabla^2f(\bm x+t\bm h)\bm h$，用Lagrange余项得第一式；再由中间点到基点的距离不超过$\lVert\bm h\rVert_2$、Hessian连续及$|\bm h^\top\bm B\bm h|\leq\lVert\bm B\rVert_F\lVert\bm h\rVert_2^2$得第二式。

3. 由中间点位置一般无法确定，引用一元Taylor公式的积分余项式`eq:analysis-taylor-integral-remainder`得积分形式，解释权重$1-t$使靠近起点的曲率贡献更多，它与中间点形式描述同一有限变化。

###### paragraph：局部展开与有限误差

1. 说明小量形式只是局部结论，不给出指定有限扰动的数值误差界；在线段邻域内$C^3$且三阶方向导数受$M_3\lVert\bm h\rVert_2^3$控制时，由一元Taylor公式得二阶截断误差不超过$\tfrac{M_3}6\lVert\bm h\rVert_2^3$，并指出仅凭一点处的二阶导数得不到这样的界。

2. 示例`ex:multivariable-exponential-taylor`：$e^{x+y}$在原点的二次项为$(h+k)^2$，取$h=k=0.1$时切平面误差约$0.021$、加二次项后约$0.0014$，三阶界约$0.0016$与实际误差同量级。

3. 解释二次项补上沿位移方向的弯曲，混合项$2hk$说明坐标间相互作用不能由分别展开再相加恢复，更高阶项由多线性微分作用于重复方向给出。

#### 13.4.3 驻点附近的函数形状

1. 说明Taylor公式把增量写成梯度项、Hessian二次型与高阶余项之和，因而梯度与Hessian的条件可转化为极值结论；回顾局部极值与严格局部极值的定义，限定只考察开集内部的点、不涉及约束。

###### paragraph：局部极值的一阶必要条件

1. 由过极值点的任意直线上该点仍是一元极值点及Fermat条件，几何上切平面水平；定理`thm:multivariable-extremum-first-order`（式`eq:analysis-first-order-necessary`）及证明：每个方向导数为零，取坐标方向得梯度为零。

2. 定义驻点，用$x^2-y^2$在原点沿$x$轴最低、沿$y$轴最高说明驻点未必是极值点，区分这些情形需要二阶信息。

###### paragraph：局部极值的二阶必要条件

1. 说明极小点处函数不能沿任何方向向下弯；定理`thm:multivariable-extremum-second-order`（式`eq:analysis-second-order-necessary`）及证明：沿每个方向用一元二阶必要条件，并回用Taylor定理证明中算出的$\phi''(0)$，得Hessian半正定（极大时半负定）。

2. 用$x^4$、$-x^4$、$x^3$在$0$处一、二阶导数都为零却分别为极小、极大与非极值，说明必要条件不能单独决定驻点类型，二次型为零的方向须检查更高阶项。

###### paragraph：驻点的二阶充分条件

1. 说明各非零方向二次型严格为正时函数沿所有方向向上弯，高阶余项不改变充分小扰动下增量的符号；强调需要正定而不只是半正定。

2. 定理`thm:multivariable-hessian-classification`及证明：正定时在单位球面上由极值定理（定理`thm:multivariable-extreme-value`）取得共同正下界$\lambda$（即最小特征值），再由Hessian连续性选小球使中间点Hessian与基点之差不超过$\lambda/2$，得增量不小于$\tfrac\lambda4\lVert\bm h\rVert_2^2$；负定对$-f$同理；不定时沿使二次型为正、为负的两个方向用小量形式比较符号。

3. 定义鞍点并以$x^2-y^2$的Hessian$\operatorname{diag}(2,-2)$为例；指出半定且有零方向时二阶判据可能无结论，边界点（如$x$在$[0,1]$上的最小点$0$）梯度可不为零，受约束问题需可行方向与乘子条件（交叉引用卷三约束优化与对偶章）。

4. 归纳判别两步：先解$\nabla f=\bm0$找驻点，再检查Hessian定性；示例`ex:multivariable-stationary-point-classification`：$x^3-3x+y^2$的驻点$(1,0)$为严格局部极小点、$(-1,0)$为鞍点，并由沿负$x$轴$f\to-\infty$说明局部极小不等于全局最小。

5. 图`fig:analysis-process-hessian-local-shapes`对照$x^2+2y^2$、$x^2-y^2$、$x^4+y^4$三种形状：前两者由正定与不定判定，第三者Hessian为零却严格极小，零Hessian也可能无极值（如$x^3$），说明退化不是一种确定分类。

### 13.5 矩阵映射的微分与扰动

1. 从线性层权重、协方差矩阵等矩阵参数与求逆、相乘等矩阵输出进入，说明可拉直为长向量，但保留矩阵形状能使乘法次序与迹结构更清楚；矩阵空间是有限维线性空间，故不建立新理论，而集中处理矩阵形状、乘法不交换与对称正定等结构约束三件事。

2. 交代路线：先说明矩阵变量的微分与梯度，再依次处理基本运算、求逆、行列式与对数行列式；每个函数都给出定义域与输入输出、微分、一阶响应和可用的误差界，局部条件数与余项原则直接回用13.3，能写出精确增量的运算用同一展开既证可微又给出余项。

#### 13.5.1 矩阵变量、微分与梯度

1. 说明矩阵输入、输出按固定顺序拉直后即欧氏坐标空间，8.3.2的Frobenius内积与范数正是拉直后的欧氏内积与范数；限定定义域为全矩阵空间中的开集，全部充分小的同形扰动都可使用。

2. 给出矩阵映射可微的定义（余项按输出Frobenius范数），说明它是向量值可微性按矩阵形状重排的写法，计算时记$\mathrm d\Phi=\mathrm d\Phi_{\bm X}(\mathrm d\bm X)$；指出微分拉直后是$rs\times mn$的Jacobian，一般不能写成与$\bm X$同形的矩阵。

3. 区分按矩阵运算定义的映射（如$\bm X^{-1}$、$\bm X^2$，输出元素依赖许多输入元素）与逐元素作用（微分只在对应位置相乘），并指出11.8.5沿谱构造的$f(\bm S)$属于前一类，但只是以矩阵为输入的映射中的一种，研究$\bm S\mapsto f(\bm S)$的微分时扰动一般不保持原特征方向。

###### paragraph：输入变量决定扰动的形状

1. 说明同一表达式随所选变量不同而微分输入不同：固定$\bm A$时$\bm x\mapsto\bm A\bm x$的扰动是向量，固定$\bm x$时$\bm A\mapsto\bm A\bm x$的扰动是矩阵；两者同时变化时在乘积空间取乘积范数，由精确增量中$\lVert\bm E\bm h\rVert_2\leq\tfrac12\lVert(\bm E,\bm h)\rVert^2$得联合微分$(\bm E,\bm h)\mapsto\bm A\bm h+\bm E\bm x$。

###### paragraph：标量输出与矩阵梯度

1. 说明标量输出的微分是矩阵空间上的线性泛函，由Riesz表示定理（定理`thm:ls-riesz-representation`）在Frobenius内积下唯一写成与同形矩阵的内积；给出矩阵梯度定义`def:multivariable-matrix-scalar-gradient`（式`eq:analysis-matrix-gradient-definition`），用单元素扰动说明其元素就是对相应元素的偏导数并得唯一性，在Frobenius长度下指出最快上升方向。

2. 给出求梯度的一般做法：展开微分，用迹的循环移位把扰动移到末端写成$\operatorname{tr}(\bm G^\top\mathrm d\bm X)$；强调循环移动整个因子而不能任意交换相邻矩阵，标量等于自身的迹。

3. 示例`ex:multivariable-bilinear-matrix-gradient`：$\bm a^\top\bm W\bm b$经迹的循环移位得梯度$\bm a\bm b^\top$，并逐元素核对偏导数$a_ib_j$。

###### paragraph：结构化变量的梯度

1. 说明变量限于线性子空间$\mathcal S$（如对称矩阵空间）时只允许$\mathcal S$中的扰动，在$\mathcal S$上用Riesz表示得受限梯度；由$\bm G-P_{\mathcal S}\bm G$与$\mathcal S$正交（10.5.4），受限梯度是环境梯度的正交投影；由对称与反对称矩阵Frobenius正交得对称投影$(\bm G+\bm G^\top)/2$，并指出在$\mathcal S$中沿用环境梯度时表示矩阵不唯一。

2. 由第11章的Weyl界说明对称正定矩阵组成对称子空间中的开集，讨论正定变量时邻域与扰动方向都在对称子空间内理解；矩阵输出时没有单个梯度矩阵，只能保留微分本身。

#### 13.5.2 基本矩阵运算的微分与精确余项

1. 导语说明从线性运算（余项为零）、乘法与平方（增量直接展开、余项可精确写出）到迹、Frobenius范数平方与二次型（读出梯度）的顺序；共同做法是写出对任意大小扰动成立的精确增量，从中同时读出微分与精确余项，承接本节开头“用同一个代数展开既证明可微、又给出具体余项”的安排。

###### paragraph：线性运算

1. 说明加法、数乘、转置与迹是线性映射，精确增量即作用于扰动、余项为零，微分等于运算本身；固定矩阵两侧相乘给出$\mathrm d(\bm A\bm X\bm B)=\bm A(\mathrm d\bm X)\bm B$，扰动位置不能移动，复合按13.2.2的链式法则逐步核对形状。

2. 由线性迹函数无余项读出式`eq:analysis-trace-linear-gradient`即$\nabla_{\bm X}\operatorname{tr}(\bm A^\top\bm X)=\bm A$，与向量情形$\nabla(\bm a^\top\bm x)=\bm a$对应。

###### paragraph：乘积的精确增量

1. 由分配律写出对任意大小扰动成立的式`eq:multivariable-product-increment`；说明前两项对$(\bm E,\bm H)$线性并受乘积不等式控制，取联合范数后由Frobenius次乘性得交叉项$\bm E\bm H$为二次量，从而得到联合微分$\bm A\bm H+\bm E\bm B$，$\bm E\bm H$是精确余项；只固定一个因子时交叉项不出现。

2. 令两因子相同得$\mathrm d(\bm X^2)(\bm E)=\bm X\bm E+\bm E\bm X$，余项恰为$\bm E^2$；用$\bm X=\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]$、$\bm E=\left[\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right]$说明正确一阶项为$\bm I$而$2\bm X\bm E=\operatorname{diag}(2,0)$错误，并由$(\bm X+t\bm E)^2=t\bm I$直接核对。

###### paragraph：Frobenius范数平方与二次型

1. 由精确增量$2\langle\bm X,\bm E\rangle_F+\lVert\bm E\rVert_F^2$读出$\nabla_{\bm X}\lVert\bm X\rVert_F^2=2\bm X$与余项$\lVert\bm E\rVert_F^2$。

2. 以二次型$\bm x^\top\bm A\bm x$说明同一数组在固定线性作用与可变输入两种角色下导数不同：对$\bm x$的梯度为向量$(\bm A+\bm A^\top)\bm x$，对$\bm A$的梯度为矩阵$\bm x\bm x^\top$且无余项；两者同时变化时展开，括号中各项至少含两个扰动因子，联合微分是两个单独微分之和。

#### 13.5.3 求逆的微分与扰动

1. 说明求逆定义在可逆方阵集合上、属于矩阵输出，没有单个梯度矩阵；回指8.2.8与8.3.1的逆矩阵和行列式非零的关系，约定矩阵范数取诱导范数（$\lVert\bm I\rVert=1$且满足乘积不等式）。

###### paragraph：由逆差恒等式得到微分

1. 在$q=\lVert\bm A^{-1}\rVert\lVert\bm E\rVert<1$下回用12.6.1的结论：$\bm B=\bm A+\bm E$可逆，逆差满足精确恒等式`eq:ch06-inverse-finite-perturbation`且$\lVert\bm B^{-1}\rVert\leq\lVert\bm A^{-1}\rVert/(1-q)$，可逆矩阵组成开集；把$\bm B^{-1}$拆成$\bm A^{-1}$与逆差后再用一次恒等式，得线性项$-\bm A^{-1}\bm E\bm A^{-1}$与满足式`eq:multivariable-inverse-remainder-bound`的二次余项，借范数等价得式`eq:analysis-inverse-differential`。

2. 说明先由精确恒等式确认可微后，再对$\bm X\bm X^{-1}=\bm I$求微分只作交叉核对，这种形式推导以可微为前提；$1\times1$时回到$-1/x^2$，两个逆位于扰动两侧，不能合并为$-\bm X^{-2}\mathrm d\bm X$。

3. 示例`ex:analysis-noncommuting-inverse-differential`：$\bm X=\operatorname{diag}(2,1)$、扰动为交换矩阵时正确导数为$\left[\begin{smallmatrix}0&-1/2\\-1/2&0\end{smallmatrix}\right]$，错误写法得非对称矩阵，直接对$(\bm X+t\bm E)^{-1}$求导核对；说明路径由对称可逆矩阵组成，导数必须对称，这种结构检查能发现错误。

###### paragraph：一阶预测的误差

1. 说明式`eq:multivariable-inverse-remainder-bound`同时是有限扰动下一阶预测的误差界，并由$\lVert\bm A^{-1}(t\bm E)\rVert\leq tq<1$确认整条扰动线段可逆；比较12.6.1控制的全变化与$\lVert\bm E\rVert$同阶，本段扣除一阶项后的误差与$\lVert\bm E\rVert^2$同阶，$q$接近$1$时一阶预测不再可靠。

2. 示例`ex:multivariable-inverse-first-order-check`：$\bm A=\operatorname{diag}(2,1)$、对称非对角扰动$0.1$，在谱范数下$q=0.1$，实际误差谱范数约$0.00505$，余项上界约$0.0111$，全变化约$0.0540$而全变化界约$0.111$；解释一阶预测扣除了约$0.05$的主要部分，余项界只保证误差不超过多少。

###### paragraph：求逆的条件数

1. 在无结构扰动与谱范数下，由乘积不等式得一阶响应不超过$\lVert\bm A^{-1}\rVert_2^2\lVert\bm E\rVert_2$，取最小奇异值的奇异向量（11.5）构造$\bm E=\bm u_d\bm v_d^\top$使其达到；由定理`thm:multivariable-local-condition-number`得绝对条件数$\lVert\bm A^{-1}\rVert_2^2$与相对条件数$\kappa_2(\bm A)$。

2. 说明矩阵条件数在此重现但输入是矩阵本身，与11.9.3输入为向量不同；结构化扰动须改用允许子空间上的范数；沿可微参数曲线有$\tfrac{\mathrm d}{\mathrm dt}\bm A(t)^{-1}=-\bm A^{-1}\bm A'\bm A^{-1}$；求解算法与数值稳定性仍按第12章处理。

###### paragraph：线性方程的解映射

1. 把求逆与乘法复合得解映射$\operatorname{sol}(\bm A,\bm b)=\bm A^{-1}\bm b$，定义在可逆$\bm A$与任意$\bm b$组成的开集上；联合输入取乘积范数，回用12.6.1的推导得精确式$\Delta\bm x=(\bm A+\bm E)^{-1}(\bm f-\bm E\bm x)$。

2. 把$(\bm A+\bm E)^{-1}$拆成$\bm A^{-1}$与逆差，第一项线性，第二项由逆差界与$\lVert\bm f-\bm E\bm x\rVert$的估计为联合扰动的二次量，得式`eq:multivariable-solution-map-differential`；再用乘积的联合微分与式`eq:analysis-inverse-differential`按链式法则核对，并区分12.6.1的完整误差界与这里的一阶预测，指出显式公式使可微性无须等到隐函数定理。

#### 13.5.4 行列式的微分与扰动

1. 说明行列式把方阵映为实数、绝对值是体积缩放倍数（8.3.1），按排列展开是各元素的多项式，因而在全部方阵上（含奇异矩阵）连续可微；本小节先算微分，再讨论条件数与余项。

###### paragraph：代数余子式形式

1. 利用行列式对每列线性逐列展开$\det(\bm a_1+\bm e_1,\ldots,\bm a_d+\bm e_d)$为$2^d$项：恰有一列取扰动的项按该列展开（8.3.1.4）给出$\sum_iE_{i,j}C_{i,j}$，至少两列取扰动的项是二次以上的多项式，在$\lVert\bm E\rVert_F\leq1$时受常数乘$\lVert\bm E\rVert_F^2$控制；得式`eq:multivariable-determinant-cofactor-differential`，梯度为代数余子式矩阵$\bm C$，奇异处同样成立。

2. 可逆时由古典伴随恒等式（定理`thm:ls-adjugate-identity`）得Jacobi公式$\mathrm d\det\bm X=\det\bm X\operatorname{tr}(\bm X^{-1}\mathrm d\bm X)$与梯度$\det(\bm X)\bm X^{-\top}$，解释为有向体积缩放倍数的相对变化；用乘法公式化归到$\det(\bm I+\bm X^{-1}\bm H)$核对，并说明奇异处只能用代数余子式形式。

3. 示例`ex:multivariable-determinant-near-identity`：对角扰动的一阶变化为$\varepsilon_1+\varepsilon_2=\operatorname{tr}\bm H$，剪切扰动面积不变且迹为零；解释面积的相对增量一阶上是伸长率之和。

###### paragraph：行列式的条件数

1. 由定理`thm:multivariable-local-condition-number`，局部绝对条件数是线性泛函$\bm E\mapsto\langle\bm C,\bm E\rangle_F$的对偶范数（10.3.5），Frobenius范数下由Cauchy--Schwarz得$\lVert\bm C\rVert_F$；可逆时由$\bm C=\det(\bm A)\bm A^{-\top}$得相对条件数$\lVert\bm A^{-1}\rVert_F\lVert\bm A\rVert_F$，奇异处只有绝对变化有定义。

###### paragraph：余项与接近奇异的矩阵

1. 在有界邻域$K=\{\bm A+\bm F:\lVert\bm F\rVert_F\leq1\}$上由多项式二阶偏导数有界取常数$M$，令$g(t)=\det(\bm A+t\bm E)$，由$|g''|\leq M\lVert\bm E\rVert_F^2$及一元Taylor公式得二次余项界，常数依赖所取邻域。

2. 示例`ex:ls-determinant-near-singular`：$\operatorname{diag}(1,\varepsilon)$沿$\operatorname{diag}(0,\delta)$扰动时行列式相对变化为矩阵相对变化的$1/\varepsilon$倍，微分给出同一结果且余项为零，说明越接近奇异沿该方向的相对放大越强。

3. 用$\varepsilon\bm I$说明行列式$\varepsilon^d$可以极小，而求逆的相对条件数为$1$、行列式自身的相对条件数为$d$，均不随$\varepsilon$变大；结论是行列式与逆矩阵是不同的输出，绝对与相对是不同尺度，须分别判断。

#### 13.5.5 对数行列式的微分与扰动

1. 说明$\det>0$的方阵组成开集，对数与行列式在其上复合，由$\mathrm d\log u=\mathrm du/u$得式`eq:analysis-logdet-gradient`，借式`eq:analysis-matrix-gradient-definition`读出梯度$\bm X^{-\top}$；对称时化为$\bm X^{-1}$，$1\times1$时回到$(\log x)'=1/x$。

2. 写出一阶变化$\operatorname{tr}(\bm A^{-1}\bm E)+o(\lVert\bm E\rVert_F)$，说明局部绝对条件数是相应线性泛函的对偶范数，Frobenius范数下为$\lVert\bm A^{-1}\rVert_F$；对数行列式可为零或接近零，这时应比较绝对变化。

###### paragraph：对称正定变量

1. 说明统计与优化中常见对称正定矩阵上的$\log\det$，只允许对称扰动；由13.5.1受限梯度是环境梯度$\bm A^{-1}$在对称子空间上的投影，它本身对称，故梯度为$\bm A^{-1}$。

2. 区分两个定义域：$\det>0$的方阵是全矩阵空间中的开集，对称正定矩阵是对称子空间中的开集；一般情形由连续性只知存在足够小的邻域，正定情形可用第11章的最小特征值界明确检查整条线段保持正定，下面的余项界基于这一检查。

###### paragraph：二次余项界

1. 设$\bm A$对称正定、最小特征值$m$，对称扰动满足$\lVert\bm E\rVert_2<m$，由任意单位向量上的二次型下界$\bm x^\top(\bm A+t\bm E)\bm x\geq m-\lVert\bm E\rVert_2$说明整条线段正定且最小特征值不小于$m-\lVert\bm E\rVert_2$；令$g(t)=\log\det(\bm A+t\bm E)$，由式`eq:analysis-logdet-gradient`与沿参数曲线的求逆公式算出$g''$，再用Frobenius内积的Cauchy--Schwarz与混合乘积界式`eq:matrix-analysis-mixed-submultiplicativity`估计$|g''|$，由一元Taylor公式得余项不超过$\lVert\bm E\rVert_F^2/(2(m-\lVert\bm E\rVert_2)^2)$。

2. 示例：$\operatorname{diag}(2,1)$加$\operatorname{diag}(0.1,0)$时一阶预测$0.05$、实际$\log1.05\approx0.04879$，实际误差约$0.00121$、上界约$0.00618$；说明上界不表示误差接近它，导数、正定线段与余项界要一起使用，并指出正定条件只是这一显式估计的条件，而非$\log\det$的定义条件。

### 13.6 隐函数与反函数

1. 说明前面各节对给定显式映射求微分，本节反过来从方程出发：判断方程能否在基点附近确定唯一函数并求其导数；以单位圆、物理平衡方程与梯度为零的最优参数为例，关心参数稍变时未知量是否唯一、光滑地随之改变及变化率。

2. 指出方程个数与待解变量个数相同时，关于待解变量的方阵Jacobian是否可逆决定能否局部解出；交代先建立隐函数定理，再研究特征值与特征向量随矩阵的变化，最后得到局部反函数定理。

#### 13.6.1 隐函数的存在与微分

1. 对比显式函数$y=\sqrt x$与关系$F(x,y)=0$可能有多个或没有解，给出在$(a,b)$附近确定隐函数的定义（小矩形内解集恰为一个函数的图像），说明须先证局部解分支存在唯一再求导。

2. 示例`ex:multivariable-implicit-circle`：单位圆在$(0,\pm1)$附近分别确定上、下半圆的隐函数，在$(1,0)$附近左侧两解、右侧无解，不能写成$x$的函数，此处切线竖直。

3. 示例`ex:multivariable-implicit-parabola-branches`：$y^2=x$在$(1,1)$附近可选出唯一正支，在原点两支相交且负侧无实数解，不存在含$0$的开区间上的解函数，说明还要指定起始解。

4. 指出两个例子中不能局部解出$y$的点都满足$\partial F/\partial y=0$，正是定理`thm:analysis-implicit-function`的可逆性失效之处；换被解变量后条件随之改变，单位圆在$(1,0)$处可把$x$解成$y$的函数。图`fig:vol1-add-implicit-branches`显示局部矩形内只保留正支，原点处不能局部选出可微解。

###### paragraph：存在、唯一性与微分

1. 用线性方程$\bm P\bm x+\bm Q\bm y=\bm0$说明条件落在待解变量的导数上：$\bm Q$可逆时有唯一解$-\bm Q^{-1}\bm P\bm x$，不可逆时解不存在或不唯一。

2. 用非线性方程在基点附近的线性近似说明隐函数定理的内容：$\bm D_{\bm y}F$可逆时局部像线性方程一样有唯一解，导数即$-\bm Q^{-1}\bm P$；强调这是充分条件，只要求待解变量的Jacobian为方阵。

3. 陈述隐函数定理`thm:analysis-implicit-function`（式`eq:analysis-implicit-derivative`），核对矩阵形状$m\times p$；说明唯一性只限于所选邻域，不排除远处的其他解支；已知$\varphi$可微时导数公式可由链式法则形式得到，定理真正困难在于存在、唯一与可微。

4. 用一元固定斜率的修正迭代$y_{n+1}=y_n-F(x,y_n)/F_y(a,b)$说明证明思路（类似Newton法但斜率固定），列出要检查的三件事：压缩、自映射与解随参数可微。

5. 证明前半：构造$T_{\bm x}(\bm y)=\bm y-\bm A^{-1}F(\bm x,\bm y)$，零点即不动点；由$\bm D_{\bm y}T$在基点为零与导数连续选闭球与参数邻域得一致压缩式`eq:analysis-ift-uniform-contraction`，借式`eq:analysis-operator-mean-value-bound`得压缩；缩小参数邻域使$T_{\bm x}(\bm b)$接近$\bm b$，由三角不等式得自映射且像落在球内部。

6. 证明中段：从$\bm b$出发迭代，相邻差按$q^n$衰减，由几何和得Cauchy列，借有限维完备性（定理`thm:ls-finite-dimensional-complete`）与闭性得极限，连续性使其为不动点；压缩给出不动点唯一，从而得到零点集合的局部存在与逐点唯一。

7. 证明后半：在闭有界集上取参数导数的统一界$L$，把两个不动点之差拆成“改变$\bm y$”与“改变$\bm x$”两步得$\varphi$局部Lipschitz；再对解集上两点之差作联合扰动的一阶展开，由$\lVert\bm k\rVert_2=O(\lVert\bm h\rVert_2)$控制余项，由行列式连续保证$\bm D_{\bm y}F$在邻域内可逆，左乘其逆得导数公式及其连续性。

###### paragraph：隐函数的导数

1. 说明定理成立后只需在选定分支上代入两个Jacobian；示例`ex:multivariable-implicit-branch-derivative`：$y^2-x$在$(1,1)$处$\varphi'(1)=1/2$并与$\sqrt x$直接求导一致，负支在$(1,-1)$处为$-1/2$，单位圆上半支一点处为$-x_0/y_0$而不必先解出$y$。

2. 说明导数要在选定分支上取值；$y_0\to0$时$-x_0/y_0$趋于无穷，与$(1,0)$处竖直切线及示例`ex:multivariable-implicit-circle`一致；曲线切向量$(1,-x_0/y_0)^\top$与梯度$(2x_0,2y_0)^\top$正交，回应13.1.4，梯度非零正是所需非退化条件。

3. 提醒Jacobian奇异时定理不能直接使用：既不能断言不存在可微分支，也不能默认分支仍唯一光滑，须另行分析。

###### paragraph：与线性解映射的一致性

1. 把$(\bm A,\bm b)$看作参数、$\bm x$看作未知量，令$F=\bm A\bm x-\bm b$，关于未知量的Jacobian为可逆的$\bm A$，关于参数的微分为$\bm E\bm x-\bm f$，由式`eq:analysis-implicit-derivative`得到与式`eq:multivariable-solution-map-differential`一致的微分。

2. 说明这里只是核对，线性方程有显式解公式而不需要隐函数定理；特征方程$\bm S\bm v=\lambda\bm v$一般没有显式公式，须先用隐函数定理证明局部分支存在且可微，引出下一小节。

#### 13.6.2 特征值与特征向量的局部微分

1. 说明特征值与特征向量由方程确定而非矩阵元素的显式函数，可用隐函数定理判断它们何时随矩阵可微变化。

2. 设实对称矩阵$\bm S_0$有简单特征值$\lambda_0$与单位特征向量$\bm v_0$，解释简单指代数重数为$1$、对实对称矩阵等价于特征空间一维；由$\pm\bm v_0$代表同一方向，用$\bm v_0^\top\bm v>0$选定局部分支，并指出单位长度不保证全局唯一。

3. 以上三角元素为坐标把对称矩阵作为参数，把特征方程与单位长度条件写成$d+1$个方程、$d+1$个未知量；写出关于$(\bm v,\lambda)$的导数矩阵，用$\bm v_0^\top$左乘第一行得$\eta=0$、第二行得$\bm h\perp\bm v_0$，由特征值简单推出$\bm h=\bm0$，故矩阵可逆，隐函数定理给出可微分支。

4. 对特征方程与归一化条件求微分，用$\bm v_0^\top$左乘得$\mathrm d\lambda(\bm E)=\bm v_0^\top\bm E\bm v_0$；代回后右侧与$\bm v_0$正交，由$\bm S_0-\lambda_0\bm I$在正交补上可逆唯一确定$\mathrm d\bm v(\bm E)$；强调分支的存在由隐函数定理保证，形式求导不能承担这一步。

###### paragraph：谱展开与谱隙

1. 在$\bm S_0$的标准正交特征基中把$\mathrm d\bm v(\bm E)$写成与$\bm v_i$正交的组合，逐个取内积得$\mathrm d\bm v(\bm E)=\sum_{j\neq i}\frac{\bm v_j^\top\bm E\bm v_i}{\lambda_i-\lambda_j}\bm v_j$。

2. 设$d\geq2$并定义谱隙$\gamma$，由谱范数定义得$|\mathrm d\lambda(\bm E)|\leq\lVert\bm E\rVert_2$，由Parseval等式得$\lVert\mathrm d\bm v(\bm E)\rVert_2\leq\lVert\bm E\rVert_2/\gamma$；$d=1$时特征向量分支不变、微分为零。

3. 与11.10的Weyl界与谱隙界比较：后者控制有限扰动下的整体变化，这里给出带方向的一阶响应；特征值响应只看扰动在该特征方向上的读数，特征向量响应以$\lambda_i-\lambda_j$为分母，谱隙小时可被大幅转向相邻特征方向。

###### paragraph：重特征值

1. 说明重特征值使关于未知量的导数不可逆，这条构造失效，但不断言每条特征值分支不可微，也不影响矩阵多项式或可逆点处求逆的光滑性；回指13.3.1中$\operatorname{diag}(t,-t)$排序后的特征值有有限条件数而不可微、未排序分支光滑；重特征值附近应改为考察特征子空间，其稳定性已在11.10.3处理，不重复谱扰动界。

#### 13.6.3 局部反函数与坐标变换

1. 提出反求输入的问题：已知输出能否唯一确定输入且随输出光滑变化，以由直角坐标反求极坐标为例；由线性映射可逆当且仅当方阵可逆，期待Jacobian可逆时局部可逆，并把$G(\bm x)-\bm y=\bm0$看成以输出为参数、输入为待解变量的隐函数问题，强调只得到两个邻域之间的逆。

2. 定理`thm:multivariable-inverse-function`及证明：对$H(\bm y,\bm x)=G(\bm x)-\bm y$用隐函数定理得局部解映射$\varphi$，缩小邻域使Jacobian在其中可逆，取$U_0=W\cap G^{-1}(V_0)$并验证$G:U_0\to V_0$是以$\varphi$为逆的双射，最后对$G(\varphi(\bm y))=\bm y$用链式法则得逆的Jacobian；解释逆映射的局部伸缩抵消原映射的局部伸缩。

3. 示例`ex:multivariable-polar-local-inverse`：由示例`ex:multivariable-polar-jacobian`的$\det\bm J_P=r$知$r>0$处可局部反求；在$(2,\pi/2)$即点$(0,2)$处求得逆Jacobian，解释$\mathrm dr=\mathrm dy$与$\mathrm d\theta=-\mathrm dx/2$。

4. 指出$r=0$处Jacobian行列式为零、所有$\theta$都映到原点，确实无法反求$\theta$，正是定理条件不满足之处。

###### paragraph：局部可逆与整体单射

1. 说明局部反函数定理是局部结论；示例`ex:multivariable-local-not-global-inverse`：$g(u,v)=(e^u\cos v,e^u\sin v)^\top$的Jacobian行列式$e^{2u}>0$处处可逆，但$(u,v)$与$(u,v+2\pi)$输出相同，不是单射；解释它是半径取$e^u$的极坐标映射，沿$v$方向每隔$2\pi$重复覆盖。

2. 反方向用$x^3$说明全局单射且逆连续也不保证逆可微，对应导数为零、定理条件不满足；提醒邻域、可微性与Jacobian可逆性都要逐项检查，14.3用坐标变换计算区域积分时还须检查区域上的一一对应、光滑性与边界处理，不能仅凭一点处Jacobian非零换元。

### 13.7 本章小结

1. 回顾一阶微分：偏导数和方向导数只考察固定直线，可微要求所有小扰动（含方向随步长改变者）共用一个线性近似，它由偏导数唯一确定，在标准坐标下由Jacobian表示、标量输出时为梯度与扰动的内积；梯度是全微分在所选内积下的表示向量，改变内积改变其坐标与最陡上升方向而不改变全微分。偏导数存在、全部方向导数存在或连续都不单独保证可微，偏导数连续是方便的充分条件；复合的Jacobian按计算顺序相乘，标量目标的梯度由微分的伴随传回输入端。

2. 回顾局部敏感性与预测精度：局部条件数由有限变化定义，可微时等于微分的算子范数，但有限条件数不必伴随可微（排序后的特征值）；导数的统一界控制整个有限变化，导数的Lipschitz界控制一阶预测的余项，二者估计不同对象且都要求扰动线段留在定义域内。再由Hessian、二阶Taylor公式与驻点判别区分严格极小、严格极大与鞍点，半定情形需要更高阶信息，二阶导数统一界是取得导数Lipschitz常数的一种充分办法。

3. 回顾矩阵变量：微分是矩阵空间之间的线性映射，标量输出的梯度是Frobenius内积下的表示矩阵，结构约束通过允许方向与正交投影进入，矩阵输入、矩阵输出与同形梯度不能混同；乘积与求逆的精确恒等式同时证明可微并给出余项，求逆的相对条件数为$\kappa_2(\bm A)$，行列式与对数行列式的条件数是相应泛函的对偶范数，行列式数值小不意味着求逆病态；说明谱章与方程章保留有限变化界和误差分析，本章以求逆、行列式等矩阵映射与线性解映射展示局部响应。

4. 回顾隐函数定理与反函数定理：在选定基点且相关Jacobian可逆时，方程或映射在邻域中确定可微分支，简单特征值及特征向量由此可微、响应大小受谱隙控制；强调这些是局部结论，不能替代全局唯一性，并说明下一章把局部线性化用于换元与累计。

## 第14章 多元函数积分

正文入口：[07-multivariate-integration.tex](../../tex/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/07-multivariate-integration.tex)。

1. 从一元积分沿区间累计出发，说明本章把累计范围换成区域、曲线和曲面；每换一种范围都要先确定小块的体积、长度或面积，计算功和通量时还要记录行进方向或法向。

2. 交代各节如何相连：区域积分承接一元Riemann积分，依次讨论Jordan区域上的分割和、累次积分、换元与参数积分；路径积分和曲面积分分别按弧长和面积累计，各有一类带方向的积分计算功与通量；最后引入散度、旋度与Laplace算子，用Green、Gauss、Stokes公式联系内部导数的累计与边界累计。

### 14.1 区域积分的定义与性质

1. 以不均匀金属薄片的总质量为例，说明切块、取“密度乘面积”、相加并加细的累计过程，同样适用于体密度和电荷密度；被积函数是输入$d$个坐标、输出一个待累计数的多元标量函数。

2. 给出积分的两种读法：非负函数的积分是以区域为底、以图像为顶的立体体积；除以区域面积得到平均值。

3. 说明本节路线：先确定哪些区域有体积，再用分割和定义积分，最后整理基本性质；一般可测函数与极限定理留给卷二积分章（`chap:integration`），本章不以它们为前提。

#### 14.1.1 盒体积与Jordan区域

1. 从“多元积分要把区域切成已知体积的小块”进入，定义闭坐标盒的体积为边长之积，边长为零时体积为零。

2. 说明有限可加性：沿坐标切开时边长相加不变，反复切分可知任意有限网格的小盒体积之和等于原体积，公共边界不重复计入。

3. 用含于$D$的有限盒组从内侧、覆盖$D$的有限盒组从外侧逼近有界集合，两侧差可任意小时称Jordan可测（Jordan区域）；由任一内侧总体积不超过任一外侧总体积，说明夹住的数唯一，即Jordan体积$|D|$。

4. 引出边界判别：有界集合Jordan可测当且仅当边界能被总体积任意小的有限个盒覆盖。先说明非边界点有邻域完全在$D$内或$D$外，所以同时接触$D$和$D$外的小盒必与边界相交。

5. 证明充分性：把覆盖边界的盒稍向外扩张，取足够细的网格使与边界相交的小盒都落入扩张盒，内外逼近之差只由这些小盒组成，总体积小于$\varepsilon$。

6. 证明必要性：边界含于外侧盒组减去内侧盒组内部的部分，其体积受两侧之差控制，另外至多含有限个盒的边界，仍可被任意小体积覆盖；并由此说明有界函数在边界附近的贡献可以任意小。

7. 以闭圆盘为例，用短弧与小正方形的个数、面积尺度说明圆周的覆盖面积趋于零；推广到有限片分段光滑边界，并提醒依赖有限片和规则参数化。

#### 14.1.2 多元Riemann和与可积性

1. 在包含$D$的闭坐标盒上作有限网格，定义网格大小与Riemann和；要求所有足够细的分割和所有取样方式都趋于同一极限，才称Riemann可积。

2. 因无法逐一检查取样方式，引入上和与下和：任意取样和夹在二者之间，可积当且仅当上下和之差可任意小。

3. 证明盒上连续函数可积：紧性给出一致连续，细网格上每块振幅任意小，上下和之差不超过振幅乘盒体积。

4. 用零延拓$f\mathbb I_D$定义一般Jordan区域上的积分，说明换更大的包含盒不改变结果。

5. 说明能连续延拓到闭包的函数零延拓可积：远离边界的小盒由一致连续控制振幅，靠近边界的小盒由边界覆盖控制体积；分块连续函数同理，边界上的取值不影响积分。

6. 以$\mathbb I_{\{x\geq1/2\}}$说明连续只是充分条件，只有穿过不连续直线的小盒贡献上下和差，积分为$1/2$；再以$\mathbb I_{\mathbb Q^2}$上下和之差恒为盒面积说明有界不够。

#### 14.1.3 积分的性质与累计量

1. 由有限Riemann和取极限得到线性、保序性和绝对值估计，以及内部不重叠、沿可忽略边界拼接的区域可加性。

2. 把体积、总质量、平均值和质心写成区域积分，说明向量值函数的积分按分量计算。

### 14.2 累次积分

1. 说明定义同时分割所有坐标，计算时希望逐个坐标积分，把$d$维累计化为几次一元积分；本节回答这样做的条件，以及上下限怎样由截面确定。

#### 14.2.1 长方体上的累次积分

1. 对闭矩形上的连续函数，固定$x$得到截面积分$F(x)$，由一致连续性证明$F$连续。

2. 把乘积网格上的Riemann和按列分组，内层和趋于截面积分且一致连续性同时控制各列误差，外层和趋于$\int F$；按行分组同理，得到两种次序的累次积分都等于二重积分，更多坐标重复分组。

3. 指出连续是便于核对的充分条件：一般Riemann可积函数的某些截面积分可能不存在，不能省去对内层积分的检查。

#### 14.2.2 简单区域与积分次序的选择

1. 对由连续边界函数$\alpha\leq\beta$描述的区域和闭包上的连续函数，给出先$y$后$x$的累次积分公式；用零延拓的网格分组说明边界附近格子可忽略，边界函数一致连续保证截面端点与内层积分随$x$连续，有限个这样的区域逐块相加。

2. 以三角形$0\leq y\leq x\leq1$上的$x+y$为例，分别按竖直截面和水平截面计算，两种次序都得$1/2$，说明换序时要重新求投影和截面，而不是机械交换积分号。

3. 以$0\leq y\leq\min(x,2-x)$的三角形说明换序会改变分块：先对$y$积分需在$x=1$处分块，先对$x$积分只需一块；取$f=1$核对面积为$1$。

#### 14.2.3 截断、奇点与交换次序的边界

1. 指出前面结论只针对有界区域上的有界函数；无界情形先用一族有界Jordan区域截断，逐个检查可积性，再取极限，并提醒一族截断的极限不能代表其他截断方式。

2. 取$(0,1]^2$上的$(x^2-y^2)/(x^2+y^2)^2$，用远离原点的矩形$[\varepsilon,1]\times[\varepsilon^2,1]$截断；先把下边界放宽到$y=0$，由原函数$y/(x^2+y^2)$算出内层积分$1/(1+x^2)$，外层极限为$\pi/4$。

3. 用$|f|\leq1/x^2$估计多算的窄条贡献趋于零，得到截断积分趋于$\pi/4$；交换两边截断速度并利用$f(y,x)=-f(x,y)$得到$-\pi/4$，说明不存在与截断方式无关的总量，两种次序的累次积分也分别为$\pi/4$与$-\pi/4$。

### 14.3 区域积分的换元

1. 以圆盘用半径和角度描述更简单进入，说明换坐标除了重写函数，还要校正小块体积；线性映射按行列式绝对值缩放体积，可微映射局部近似线性，换元公式累计这些局部比例。

#### 14.3.1 局部体积变化与换元公式

1. 为保证单次覆盖并便于处理边界，在开集之间取逆也为$C^1$的双射，陈述紧Jordan区域上连续函数的换元定理，权重为$|\det DT|$。

2. 概述证明思路：在紧集上写出余项一致的一阶近似，逆导数有界保证小立方体的像不被任意压扁。

3. 用线性像平行多面体外加与$\eta(\delta)\delta$同阶的薄层夹住真实像，得到局部体积比趋于$|\det DT|$；再逐项比较像区域与参数区域上的和，由一致连续、一致余项界和Jordan边界条件控制三类误差。明确这是证明思路，仅有单点线性近似不能交换整个分割和的极限。

4. 说明全局双射不可省：逆函数定理只给局部可逆，重复覆盖会重复累计；行列式取绝对值只消去定向符号，不消去覆盖次数。

#### 14.3.2 极坐标、柱坐标与球坐标

1. 平面极坐标的Jacobian行列式为$r$，以同一角宽在大半径处扫过更长的弧解释面积权重$r\,\mathrm dr\,\mathrm d\theta$，配图对照不同半径处的小块面积。

2. 说明原点处行列式为零、角度两端表示同一射线，闭参数矩形不满足定理条件；先在$r\geq\varepsilon$、$\varepsilon\leq\theta\leq2\pi-\varepsilon$上换元再取极限，用函数上界乘面积控制遗漏。

3. 用圆盘面积$\pi R^2$核对，指出角度取到$4\pi$时结果加倍，奇异被积函数不能只凭“接缝不贡献面积”跳过极限估计。

4. 柱坐标保留高度，体积权重仍含$r$，得圆柱体积$\pi R^2H$。

5. 球坐标按三个正交方向的长度比例$1$、$\rho$、$\rho\sin\varphi$得到体积权重$\rho^2\sin\varphi$，并可由Jacobian行列式验证；说明在去掉轴线和接缝后单次覆盖，经截断估计得到球体积$4\pi R^3/3$。

#### 14.3.3 线性换元与积分结果的核对

1. 用$u=x+y$、$v=x-y$把斜正方形变为$[0,2]^2$，逆变换行列式为$-1/2$、面积权重为$1/2$，算得$\int_D(x+y)=2$。

2. 用面积$2$与平均值$1$的乘积再核对一次，说明这同时检验了区域、权重和积分值。

### 14.4 参数积分

1. 以密度随时间变化时总质量成为时间的函数进入，说明判断参数积分的连续与可导需要整个区域上的统一控制，本节固定紧Jordan区域，用连续性提供这种控制。

#### 14.4.1 固定区域上的参数积分与连续性

1. 设$f$在$D\times K$上连续，由乘积紧集上的一致连续性得到关于$\bm x$的上确界差趋于零，再用绝对值估计证明参数积分连续；参数域不必整体有界，局部取小闭盒即可。

#### 14.4.2 积分号下的偏导数与全微分

1. 设$f$及各参数偏导数在$D$与参数邻域的乘积上连续，用一元中值定理把差商写成附近参数处的偏导值，由偏导数一致连续得到差商一致收敛，进而得到积分号下求偏导的公式。

2. 右侧是被积函数连续的参数积分，因而连续；由连续偏导数判据得$F\in C^1$及全微分公式，并强调整体可微来自连续偏导数，不能只验证各方向极限。

3. 以$F(t)=\int_0^1e^{tx}\,\mathrm dx$求得$F'(0)=1/2$，说明这样不必处理显式表达式$(e^t-1)/t$在$0$处的可去奇点。

#### 14.4.3 变限参数积分

1. 说明积分区间随参数变化时，变化来自被积函数的变化和端点处新添或移除的细条。

2. 在$a,b\in C^1$、$f$与$\partial_tf$连续的条件下，把积分写成固定点到上下限的积分之差，对上限用一元基本定理、对参数用积分号下求导，再由链式法则得到变限求导公式，解释两个边界项的符号。

3. 说明多参数时逐个求偏导或改用全微分，更一般的移动区域会产生沿边界的贡献，本章只在区间变限时使用这一规则。

### 14.5 路径积分

1. 以弯曲铁丝的质量和沿路线推物体做功进入，区分沿曲线累计标量函数与向量场的两类问题。

2. 说明第一类路径积分按函数值乘长度累计、与方向无关；第二类路径积分取力与有向位移的内积累计，反向时变号。

3. 交代本节先参数化曲线并计算弧长，再讨论两类积分，最后研究功何时只取决于端点；参数积分均为一元Riemann积分。

#### 14.5.1 参数路径与弧长

1. 以质点每个时刻的位置描述一次行进，导数是速度，速率乘时间是路程，速率变化时路程是速率的积分。

##### 14.5.1.1 路径的定义

###### paragraph：参数化路径

1. 说明只记下经过的点会丢失快慢、起点与重复行进的信息，因而用区间到空间的连续映射同时保留位置与先后次序；正式定义路径、起点终点、闭路径与像集。

2. 用三条像集相同的对角线路径对照：$\gamma(t)=(t,t)$、速度减半用时加倍的$\eta$、先去后回的$\rho$；前两者只差快慢，$\rho$使每个内点经过两次。说明两类积分对前两者相同，沿$\rho$按长度加倍、按有向位移抵消，所以路径积分沿一次行进定义。

###### paragraph：分段光滑路径

1. 以往返路径掉头、正方形边界转角说明这些位置没有唯一切线，正式定义分段$C^1$（分段光滑）与分段正则路径。

2. 解释闭区间上$C^1$指导数连续并可延拓到端点，相邻段的端点导数不必相同，以$\rho$两段速度为例；折点只有有限个，不影响参数积分；分段正则排除中途停住，单位切向量只在速度非零处使用。

##### 14.5.1.2 路径的长度

###### paragraph：弧长

1. 用插标杆测道路的办法说明内接折线不长于道路、加点后不变短，定义弧长为内接折线长度的上确界及可求长；指出定义只用位置。

2. 以位移约为速度乘时间、里程表累计路程为直观，陈述分段$C^1$路径的弧长等于速率积分。证明先归结到单个光滑段，再分两步：由分量基本定理与Cauchy--Schwarz不等式得弦长不超过该段速度积分，并得到向量积分的范数不等式；再用$\gamma'$的一致连续控制细分割上每段弦长与速度积分的差，得到反向不等式。

3. 用例子核对：对角线段长$\sqrt2$而非$2$，慢速路径同为$\sqrt2$，往返路径为$2\sqrt2$，圆周为$2\pi r$；说明速率减半与用时加倍抵消、弧长计入经过次数。定义累计路程$s(t)$与$\mathrm ds=\lVert\gamma'\rVert_2\,\mathrm dt$。

#### 14.5.2 第一类路径积分

1. 说明被积对象是曲线上的标量函数，每小段贡献函数值乘长度，只用路程作权重。

##### 14.5.2.1 定义与可积性

###### paragraph：按弧长的积分

1. 把铁丝切成小段，每段质量约为密度乘速率乘参数长度，相加成为$h(\gamma(t))\lVert\gamma'(t)\rVert_2$的积分和；对像集上的连续函数正式定义第一类路径积分，右侧按各光滑段的一元积分相加。

2. 给出读法：$h=1$为弧长，非负线密度给质量，除以长度得到按路程加权的平均值，并与按参数时间加权对比，说明车速不影响按路程的平均。

3. 例题沿上半单位圆放线密度为$y$的铁丝，速率为$1$，质量为$2$，平均线密度$2/\pi$；指出速率恒为$1$时两种平均一致，一般不同。

##### 14.5.2.2 积分的基本性质

1. 假设函数沿路径连续或分段连续，说明各性质由定义式代入一元积分的相应性质得到，并可用铁丝质量解读。

###### paragraph：线性

1. 给出和与数乘的积分公式，由$c=-1$得到差的积分；以两种材料叠合和密度同时放大说明含义。

###### paragraph：路径拼接

1. 定义拼接路径，由一元积分对区间的可加性得到拼接公式，作为逐段计算折线与多边形边界的依据。

2. 说明重叠部分计入两次：往返路径$\rho$的返回段经换元化为沿$\gamma$的同一积分，故沿$\rho$的积分是沿$\gamma$的两倍。

###### paragraph：重参数化与方向无关

1. 以称铁丝质量与从哪端开始、快慢无关为直观，对单调、端点相配的分段$C^1$微分同胚$\sigma$，由链式法则得新速率含$|\sigma'|$，再用一元换元证明积分不变；递减时绝对值保持权重非负，所以反向也不变。

2. 以$\eta=\gamma\circ\sigma$弧长同为$\sqrt2$举例，说明换参数不改变经过次数，往返路径$\rho$不是$\gamma$的重参数化。

###### paragraph：单调性

1. 由长度权重非负，路径上处处$h\leq k$推出积分不等式；以密度较小的铁丝质量较小解读。

###### paragraph：绝对值不等式

1. 给出$|\int h|\leq\int|h|\leq\sup_C|h|\,\ell(\gamma)$，说明连续函数在紧像集上有界故上界有限，并用半圆铁丝核对。

##### 14.5.2.3 积分的计算

1. 归纳三步：选恰好走一遍的参数化，乘速率，在参数区间上积分并在折点两侧分段。

2. 沿对角线段积分$x+y$得$\sqrt2$，平均值$1$等于中点值；指出漏掉速率会少一个因子$\sqrt2$，第一类积分也不是线段下方的平面面积。

3. 对函数图像$y=\psi(x)$以$x$为参数，得到含$\sqrt{1+\psi'^2}$的公式，用斜边长度解释根号，曲线越陡同一$\mathrm dx$的路程越长。

4. 例题计算抛物线$y=x^2$上线密度$x$的铁丝质量$(5\sqrt5-1)/12$，对照漏写根号所得的$1/2$。

#### 14.5.3 第二类路径积分

1. 以推车时力与前进方向的夹角决定功的正负进入，说明做功问题需要先说清每一点有一个力的含义。

##### 14.5.3.1 定义与可积性

###### paragraph：向量场

1. 以重力、引力与水流速度说明每个位置给出一个同维向量，正式定义向量场并解释箭头画法。

2. 给出重力常场、径向场和旋转场三个平面例子，验证旋转场与位置向量垂直。

###### paragraph：有向线积分

1. 以常力沿直线做功等于内积$\bm F^\top\Delta\bm r$说明只有沿位移方向的分量做功及功的符号；路线弯曲时切段近似，每段功约为场值与速度的内积乘参数长度，强调乘的是速度向量而非速率。

2. 对像集上的连续向量场正式定义第二类路径积分；解释$\mathrm d\bm r$为有向位移，平面中写成$\int P\,\mathrm dx+Q\,\mathrm dy$并说明各项含义；连续性保证参数积分存在。

3. 在速度非零处用单位切向量把被积量写成切向分量乘$\mathrm ds$，说明第二类积分是切向分量的第一类积分，速度为零处两侧都为零；切向分量随行进方向反转而变号。

4. 定义流速场沿闭路径的环流，以旋转场沿单位圆一周环流$2\pi$为例；配图在同一对角线段上对照常数密度按弧长累计得$\sqrt2$与常场$(1,0)$做功为$1$。

##### 14.5.3.2 积分的基本性质

1. 假设向量场在像集上连续，说明性质分三组：线性说明功对力线性，拼接、方向反转与重参数化说明功随路径的变化，最后的不等式估计功的大小。

###### paragraph：线性

1. 给出向量场之和与数乘的积分公式，以合力做功等于各力做功之和、力反向则功变号解读，并得到差的公式。

###### paragraph：路径拼接

1. 先走一段再走一段，总功为两段之和；分段路径可逐段计算，但每段须按实际行进方向参数化。

###### paragraph：方向反转

1. 定义反向路径$\gamma^-(u)=\gamma(a+b-u)$，由速度反号和一元换元证明积分变号；以顺风去、逆风回为例，对照第一类积分反向不变；往返路径上的第二类积分为零而长度加倍。

###### paragraph：重参数化

1. 对严格递增的分段$C^1$换参数，由链式法则与一元换元证明积分不变，即功只取决于经过的位置和方向，与快慢无关。

2. 对照第一类积分，这里乘$\sigma'$而非$|\sigma'|$，递减换参数等于反向因而变号；换参数不改变经过次数。

###### paragraph：绝对值不等式

1. 由三角不等式和$|\bm F^\top\bm\tau|\leq\lVert\bm F\rVert_2$得功的绝对值不超过力的大小沿路程的累计，力沿前进方向时取等号，并给出$M\ell$的上界。

##### 14.5.3.3 积分的计算

1. 归纳步骤：按行进方向参数化，场值与速度取内积，再做一元积分。

2. 常场$(1,0)$沿对角线段做功为$1$而不是长度$\sqrt2$，因为只对位移的水平分量做功。

3. 重力沿任意分段光滑平面路径的功为$-mg(y(b)-y(a))$，被积函数不含$x'$，只依赖高度差；以$1$千克下降$2$米做功约$19.6$焦为数值例，并预告路径无关一节解释其原因。

4. 给出图像路径上的第二类积分公式。

5. 例题比较从$(1,0)$到$(-1,0)$的上半圆与直径：常场在两条路线上做功都为$-2$，等于$x$的端点差；旋转场沿上半圆做功$\pi$，沿直径为$0$。

6. 总结常场的功与路线无关、旋转场的功依赖路线，绕单位圆一周旋转场做功$2\pi$；配图画出旋转场与两条路线。

#### 14.5.4 路径无关与势函数

1. 对比重力与旋转场：重力的功可写成只依赖位置的量$-mgy$在两端之差，旋转场没有这样的量；说明本小节依次讨论势函数化累计为端点差、由路径无关构造势函数、微分判别及有洞定义域的反例。

##### 14.5.4.1 势函数与路径积分

###### paragraph：势函数

1. 由重力势能$mgy$与重力等于负势能梯度引入，数学上取$\phi=-E_{\mathrm p}$，正式定义势函数、梯度场与保守场。

2. 说明梯度场指向$\phi$增大、势能减小的方向，以$x^2+y^2$与$x$为例。

3. 说明势函数相差常数仍为势函数；在路径连通开集上沿折线逐段用中值公式，证明两个势函数只差常数，对应势能零点可任选。

4. 解释“保守”的来源：对牛顿第二定律下的$C^2$运动，用乘积法则、运动方程和链式法则证明动能与势能之和守恒，并指出功率$\nabla\phi^\top\gamma'$是$\phi\circ\gamma$的导数正是下一定理的核心。

###### paragraph：路径积分基本定理

1. 由复合函数$\phi\circ\gamma$的导数是第二类积分的被积函数，以及小段增量相加时中间项抵消的直观，陈述路径积分基本定理；证明在每个光滑段上用链式法则和一元基本定理，相加后中间端点值抵消。

2. 用势能读定理：保守力做功等于势能下降量，重力做功是$\phi=-mgy$的情形；得到两个推论：梯度场的积分只依赖端点，闭路径积分为零，并与方向反转性质一致。

3. 例题对$(2x,2y)$用势函数$x^2+y^2$直接算出沿上半圆的积分为$0$，并以直接代入核对，说明场沿半径方向与切线垂直。

4. 用第二个推论否定势函数的存在：旋转场绕单位圆环流$2\pi\neq0$，故在平面上没有势函数。

##### 14.5.4.2 路径无关的等价判别

###### paragraph：路径无关

1. 说明比较不同路线需要路径连通，欧氏开集中路径连通时可选域内折线，正式定义路径无关。

2. 以物理中从参考点做功定义势能、只有功与路线无关时势能才确定为动机，陈述势函数存在、路径无关与闭路径积分为零三者等价。

3. 证明：1推2由基本定理；2推3用常值路径；3推2把两条路径拼成闭路径并用拼接与反向性质；2推1固定参考点定义$\phi$，在小球内沿坐标方向延伸一小段线段，把差商写成$F_j$在短线段上的平均值，由连续性得偏导数等于$F_j$。

4. 说明所构造的$\phi$就是从参考点出发的功，换参考点只差一个常数。

##### 14.5.4.3 势函数存在的微分判别

###### paragraph：交叉偏导相等的必要条件

1. 指出等价条件需检查所有路径而无法逐条验证，转而寻找求导即可检查的条件；对$C^1$场由$\phi\in C^2$与混合偏导可交换，陈述并证明交叉偏导相等的必要条件。

2. 在平面中条件化为$\partial_xQ=\partial_yP$，计算小正方形边界的环流约为$(\partial_xQ-\partial_yP)\delta^2$，把这个差解释为单位面积的旋转率；保守场的旋转率必须为零，精确关系留给Green公式。

3. 以$(2x,2y)$满足条件且有势函数、旋转场旋转率为$2$因而在任何非空开集上都没有势函数对照，并核对$2\pi$等于旋转率$2$乘圆盘面积$\pi$。

###### paragraph：星形域上的充分条件

1. 说明交叉偏导条件是局部的，势函数是全局的，需对定义域加条件；定义星形开集，凸集与全空间是例子，并说明沿线段从中心点做功的构造。

2. 陈述星形域上的势函数构造定理。证明先说明$\phi$是沿线段的第二类积分，线段的紧邻域保证可在积分号下求导；再用链式法则求被积函数对$x_j$的偏导，借交叉偏导条件写成$\frac{\mathrm d}{\mathrm dt}[tF_j(\bm a+t\bm z)]$，积分得$\partial_j\phi=F_j$。

3. 例题对$(2xy,x^2)$核对交叉偏导，沿线段积分得势函数$x^2y$，并算出到$(1,2)$的功为$2$；说明星形域上的构造不依赖猜测。

###### paragraph：穿孔平面上的反例

1. 引入穿孔平面上的涡旋场，说明它与旋转场同向而大小为距离的倒数；用商的求导法则验证交叉偏导处处相等，再沿单位圆积分得$2\pi$，由等价条件知没有势函数。

2. 说明与星形域定理不矛盾：穿孔平面不是星形域，问题出在原点这个洞。

3. 第一个角度：局部势函数是极角，在右半平面和去掉负半轴的平面上验证$\nabla\theta=\bm F$；在整个穿孔平面上绕一圈极角增加$2\pi$，无法连续选取；上下半圆积分分别为$\pi$与$-\pi$，相差$2\pi$；不绕原点的圆积分为零。

4. 第二个角度：用小正方形环流近似为零与公共边相消说明被围区域整个在定义域内时环流为零，精确形式是Green公式；单位圆盘含原点，无法这样填满；由环形区域的划分得绕原点一周的简单闭路径积分都是$2\pi$。

5. 说明星形域中任意闭路径可沿线段向中心收缩而不离开定义域，从几何上解释交叉偏导条件在星形域上足够。

### 14.6 曲面积分

1. 以薄壳质量和穿过渔网的水量两个问题进入，区分被积对象：前者是曲面上的标量面密度，后者是向量场，只取垂直于曲面的分量累计为通量。

2. 说明两类积分都需要面积元，通量还要规定穿越方向，所以先求面积元，再讨论定向；参数积分按有界Jordan区域上的Riemann积分理解。

#### 14.6.1 参数曲面与面积元

1. 说明弯曲曲面的面积尚无定义，以经纬度为参数化的例子，指出参数面积不等于实际面积，需要每点乘一个面积放大倍数；本小节说明怎样的参数化描述一张面，求出放大倍数，并证明面积与参数选取无关。

##### 14.6.1.1 曲面的参数化

###### paragraph：正则曲面片

1. 说明并非每个二元向量值映射都描述一张面：点只沿一个方向移动时像集可能是曲线，重复覆盖会重复累计；正式定义正则参数曲面片，参数边界允许接缝或退化。

2. 解释$\bm r_u,\bm r_v$是两条参数曲线的速度向量，线性无关即不共线并张成切平面；以$(u+v,0,0)$把正方形压成线段的例子说明正则性的作用。

3. 以单位圆柱面说明单次覆盖：$\theta\in[0,2\pi]$只在边界形成接缝，$\theta\in[0,4\pi]$使内部点被表示两次，不符合定义。

4. 引入贯穿全节的斜平面片$(u,v,u+v)$，核对它满足定义。

###### paragraph：叉积

1. 由线性近似说明参数小矩形近似映为以$\bm r_u\Delta u$、$\bm r_v\Delta v$为边的平行四边形，问题归结为由两条三维边向量求面积。

2. 指出$3\times2$矩阵没有行列式，定义叉积并以坐标单位向量为例。

3. 核对三条性质：叉积垂直于两因子并按右手规则定向；由Lagrange恒等式得叉积长度等于平行四边形面积，为零当且仅当线性相关；双线性与反对称。

4. 由性质得小曲面片面积约为$\lVert\bm r_u\times\bm r_v\rVert_2\Delta u\Delta v$，即面积放大倍数，正则性等价于叉积非零；平面情形下它就是Jacobian行列式的绝对值，与换元一节的权重一致。

##### 14.6.1.2 曲面面积的表示

###### paragraph：面积元与面积

1. 说明把放大倍数在参数域上积分取作面积定义，而不用内接多面形的上确界，以Schwarz灯笼说明后者会失败，切平面平行四边形贴着曲面。

2. 正式定义曲面面积与面积元$\mathrm dS$，说明积分存在，有限分片曲面逐片相加且接缝不重复累计。

3. 例题算斜平面片的叉积$(-1,-1,1)$与面积$\sqrt3$，用两边长度与夹角$60^\circ$的初等几何核对；配图对照参数小块与斜面小块，说明每个参数面积放大$\sqrt3$倍。

###### paragraph：重参数化

1. 例题把斜平面片的一个参数拉伸为$u=2\xi$，参数域面积减半而放大倍数加倍，面积仍为$\sqrt3$。

2. 陈述并证明重参数化定理：由链式法则与叉积的双线性、反对称性得新叉积等于$\det\bm J_T$乘原叉积，取长度后用二维换元公式得到同一面积，内部正则时先在紧子域上应用再取极限。

3. 几何上把证明读成两步面积放大，用拉伸例子说明$\det\bm J_T=2$；交换参数时行列式为$-1$，叉积反向而长度不变，面积不用这个方向，通量要用。

4. 说明双射条件不可省：柱面$\theta\in[0,4\pi]$给出$4\pi$而非$2\pi$。

###### paragraph：分片曲面

1. 以立方体表面和球面说明有些曲面需分片，规定有限分片的条件，面积逐片相加；立方体表面积为$6$，棱不另计；无界或不能有限分片的曲面需另行处理。

#### 14.6.2 第一类曲面积分

1. 回到薄壳质量问题，说明这类积分只用小片面积、不涉及方向。

##### 14.6.2.1 积分的定义和可积性

###### paragraph：按面积的积分

1. 把薄壳分片，每片质量约为面密度乘面积，相加加细得到面密度对面积的积分，电荷量与涂料用量同理；在参数域上把密度与面积权重相乘。

2. 正式定义连续函数的第一类曲面积分，解释计算顺序，说明重参数化下积分不变；取$h=1$得面积，以斜平面片上常数密度$2$得质量$2\sqrt3$。

3. 定义按面积加权的平均，以全球平均气温说明应按实际面积而非经纬度格子数平均。

4. 说明第一类积分继承线性、单调性与绝对值估计，分片曲面逐片求和；面积权重非负且与观察侧无关，所以反转曲面朝向不改变第一类积分。

##### 14.6.2.2 积分的计算

1. 归纳三步：选单次覆盖的正则参数化，与$h$复合，乘叉积长度后在参数域上积分。

2. 函数图像$z=\psi(x,y)$的叉积为$(-\psi_x,-\psi_y,1)$，自动正则且单次覆盖，得到含$\sqrt{1+\psi_x^2+\psi_y^2}$的公式。

3. 用法向与$z$轴夹角的余弦解释根号是投影面积的校正，以平面$z=ax+by+c$在单位圆盘上方的面积$\pi\sqrt{1+a^2+b^2}$为例；不能单值投影的曲面需换参数或分片。

4. 给出球面参数化及偏导向量，由两者正交、长度为$R$与$R\sin\varphi$得放大倍数$R^2\sin\varphi$，并用经线与纬线圈上的弧长直观解释；两极与接缝来自参数边界，面积为零。

5. 例题由球坐标算得球面面积$4\pi R^2$。

6. 例题求上半球面按面积的平均高度$R/2$，对照按参数矩形平均所得的$2R/\pi$；说明参数格子在北极附近对应很小的面积，按参数平均会高估。

#### 14.6.3 定向曲面与第二类曲面积分

1. 回到渔网问题，说明“穿过”需要先规定出发侧与到达侧，所以先讨论定向再定义通量。

##### 14.6.3.1 曲面的定向

###### paragraph：单位法向量

1. 说明正则点处有两个相反的单位法向，选定其一即约定正向穿越；用参数叉积定义局部单位法向，交换参数会反转它。

2. 斜平面片上它指向上方；球坐标参数下叉积是位置向量的正数倍，单位法向指向外侧；参数边界上叉积退化处不用此式，面积为零不影响通量。

###### paragraph：定向与可定向性

1. 说明逐点选法向不够，用给曲面一侧涂色解释连续选取的要求；正式定义定向、可定向曲面与分片曲面的相容条件。

2. 举出函数图像的向上法向、球面外法向、闭曲面通常取外法向（散度定理采用）以及立方体表面的相容外法向。

3. 以纸带扭转半圈粘合与蚂蚁爬行描述Möbius带；例题给出参数化，算出中线上叉积在$u=0$与$u=2\pi$处对应同一点却方向相反，再用连续函数只取$\pm1$必为常数推出矛盾，证明不可定向。

4. 说明Möbius带的面积与第一类积分仍有定义，但全局通量不适用。

##### 14.6.3.2 积分的定义和可积性

###### paragraph：通量积分

1. 从恒定流穿过平面网的斜柱体积推出单位时间穿过量为$(\bm v^\top\bm n)A$，并区分平行、垂直与逆向三种情形，说明只有法向分量起作用。

2. 例题对倾斜正方形算出单位法向与面积，竖直流的通量为$c\cos\alpha$，切向流的通量为零；说明竖直流的通量等于流速乘水平投影面积，并以倾斜屋顶接雨解释。

3. 对弯曲曲面与变化的场切片近似，得到$\bm F^\top\bm n$对面积的积分，电场、热流同理；正式定义第二类曲面积分，参数叉积须与所选法向一致，分片曲面按相容定向相加。

4. 说明单位法向的分母与面积元中的长度抵消，引入有向面积元，计算时不必先求单位法向；通量是净穿过量，与把三个分量分别做面积积分所得的向量不同。

5. 引入记号$\mathrm dy\,\mathrm dz$等，解释各分量是小片在坐标平面上的有向投影面积，以倾斜正方形核对，强调这些记号带符号；配图在法向截面内分解场值，说明通量只累计法向分量。

6. 说明连续场与连续有向面积元保证每片通量存在。

##### 14.6.3.3 积分的性质

1. 规定同一曲面、同一法向约定与连续向量场，说明线性和可加性沿用第一类积分，法向反转与重参数化需单独说明。

###### paragraph：线性

1. 由法向分量对场的线性，给出和与数乘的通量公式，以两股水流叠加与流速加倍解读，强调缩放的是场而法向约定不变。

###### paragraph：曲面分割的可加性

1. 有限分片且各片沿用原定向时通量相加，零面积接缝不贡献；某片单独反转法向就不再是整张曲面的通量。

###### paragraph：法向反转

1. 法向换成相反方向时通量变号，水流不变而计数方向改变；与第一类积分不随定向改变对照。

###### paragraph：重参数化

1. 由重参数化定理，新叉积乘$\det\bm J_T$而换元公式用$|\det\bm J_T|$；行列式为正时直接不变，为负时按定义中的符号约定校正后仍不变，通量只依赖曲面、定向和场。

##### 14.6.3.4 积分的计算

1. 归纳三步：定法向，选叉积指向该侧的参数化（否则加负号），在参数域上累计场与有向面积元的内积。

2. 图像曲面取向上法向时得到$\iint(-P\psi_x-Q\psi_y+R)$的公式，取向下法向加负号，强调不能再乘根号。

3. 例题对斜平面片与竖直单位场算得通量$1$，用面积$\sqrt3$乘法向分量$1/\sqrt3$核对，等于水平投影面积；推广到平面在单位圆盘上方的通量$\pi$，与实际面积对照。

4. 说明球面$(\varphi,\theta)$次序的叉积指向外侧，三个例子都取外法向。

5. 例题径向场$\bm x/R$穿过球面的外向通量为$4\pi R^2$，取内法向为负；说明一般只有法向分量计入，通量绝对值不超过场大小的面积积分。

6. 例题点源场$\bm x/\lVert\bm x\rVert^3$的外向通量为$4\pi$，与半径无关，用面积增大抵消场减弱解释。

7. 例题恒定场穿过球面的净通量为零，上下半球分别为$\pi R^2$与$-\pi R^2$；说明闭曲面的净通量反映内部的源与汇，包围点源的球面有正通量，并预告用散度定理核对。

### 14.7 向量场与微分算子

1. 以梯度为对照，把向量场想成流体速度场，提出净流出与绕点打转两个局部问题，分别由散度与旋度回答；Laplace算子作用于标量函数，比较一点的值与周围平均；三者都是下一节积分公式中的内部量。

#### 14.7.1 散度与局部通量

###### paragraph：小立方体的净流出

1. 回顾单位时间穿过小片的流量约为法向分量乘面积，以点$\bm a$为中心取边长为$h$的小立方体估计净流出。

2. 计算垂直于$x$轴的两面：右面流出、左面流入，合计约为$\partial_1F_1h^3$，解释$F_1$沿$x$增大时净流出为正。

3. 三对面相加除以体积得到偏导数之和；对连续可微场在小立方体上统一展开，余项贡献为$o(h^3)$，常数项抵消、线性项给出偏导数，从而得到极限，不需要Gauss公式。

4. 正式定义散度，并说明它是Jacobian矩阵的迹，非对角偏导数不进入净流出率。

###### paragraph：源的强度

1. 把散度读成源的强度，区分源、汇与平衡；不可压缩且无源汇的流体散度为零。

2. 例题算出三维径向场散度为$3$、旋转场与常场散度为$0$，说明散度为零不表示场为零。

3. 给出二维散度$P_x+Q_y$，说明平面通量公式使用它。

#### 14.7.2 旋度与局部环流

###### paragraph：小正方形上的环流

1. 以旋转场散度为零而环流不为零说明需要另一度量，用小闭路径上的环流度量旋转。

2. 计算平面小正方形四边的贡献，得到单位面积的逆时针环流约为$\partial_xQ-\partial_yP$，并解释两项的符号。

3. 在三维中把小正方形放在垂直于三个坐标轴的平面内，按逆时针取向分别得到三个环流率，用$\bm e_2\times\bm e_3=\bm e_1$等说明坐标次序；排成向量即旋度，正式定义旋度。

###### paragraph：旋转的轴与强度

1. 陈述垂直于单位向量$\bm n$的小圆周上环流除以面积的极限为$(\operatorname{curl}\bm F)^\top\bm n$，一般方向的证明放在Stokes公式之后；由Cauchy--Schwarz不等式说明旋度方向是旋转最强的转轴、长度是强度，转向按右手定则。

2. 以小桨轮解释环流与旋度分量，强调图像不代替计算。

3. 例题刚体旋转的旋度为$(0,0,2\omega)$，$\omega=1/2$时为$(0,0,1)$；径向场旋度为零。

4. 例题剪切流$(y,0,0)$流线为直线而旋度为$(0,0,-1)$，用桨轮上缘受推更多解释；对同心圆流动推导$Q_x-P_y=s(r)/r+s'(r)$，区分流线弯曲与速率差两项，刚体旋转合计$2\omega$，涡旋场$s=1/r$时两项抵消。

5. 总结旋度与流线是否弯曲是两回事，涡旋场外侧较慢的流速抵消了弯曲带来的转动倾向。

6. 说明二维场补零第三分量后，$Q_x-P_y$是旋度在$\bm e_3$上的分量；$\nabla\cdot$与$\nabla\times$只是偏导数组合的记号。配图在单位圆上对照径向场与旋转场的通量与环流。

#### 14.7.3 Laplace算子与运算关系

1. 说明梯度再取散度把各方向的二阶变化相加，出现在分部积分与热传导方程中；正式定义Laplace算子，说明输入输出都是标量函数，并是Hessian的迹，以$\lVert\bm x\rVert^2$的$\Delta=2d$为例。

2. 由混合偏导可交换得到$\operatorname{curl}(\nabla v)=\bm0$与$\operatorname{div}(\operatorname{curl}\bm F)=0$，指出由旋度为零推势函数仍须核对定义域，并区分两个等式的对象类型。

###### paragraph：与邻域平均值的差

1. 由一元$v''>0$对应低于邻点平均值进入，在各坐标方向取前后邻点作二阶Taylor展开，一阶项抵消，求和除以$2d$得到邻点平均与中心值之差为$\frac{h^2}{2d}\Delta v+o(h^2)$，据此解释$\Delta v$的符号。

2. 例题$x^2+y^2+z^2$在原点的邻点平均比中心值高$h^2$，等式精确成立；$x^2-y^2$的邻点平均恰等于中心值。

3. 说明后者两个方向的弯曲相互抵消，Laplace算子只记录弯曲的总和。

###### paragraph：热传导中的含义

1. 由Fourier定律$\bm q=-k\nabla u$与散度的含义，推出无热源时温度变化率为$\frac kc\Delta u$，即热传导方程。

2. 用邻域平均解释较冷点升温、较热点降温、温度被抹平，稳态时$\Delta u=0$；说明Fourier定律是物理模型，只用来说明$\Delta$的含义。

### 14.8 区域与边界的积分关系

1. 从一元基本定理把端点差读成带符号的边界求和、路径积分基本定理把同样关系搬到路径上进入，说明本节推广到平面区域、空间区域和曲面，分别得到Green、Gauss与Stokes公式。

2. 说明共同思路：小块上导数乘大小近似边界累计，相邻公共边界方向相反而抵消，只剩外边界；环流对应旋度，通量对应散度；先规定边界方向，再依次给出三个公式。

###### paragraph：边界的定向

1. 说明内部公共边或公共面的贡献要相消，各小块须采用相容方向，并与局部计算所用方向一致，即环流按逆时针、通量按外法向。

###### paragraph：平面区域的正向边界

1. 定义简单闭曲线与正向边界（区域在左侧），圆盘边界逆时针。

2. 有孔时外边界逆时针、孔洞边界顺时针，以圆环为例，并说明这与小块逆时针相消的结果一致。

3. 分段光滑边界逐段相接，转角不另加项；相邻小块的公共边被反向走过而抵消。

###### paragraph：区域边界的外法向

1. 规定空间区域的外法向，以球壳内外球面为例，相邻子区域公共面上外法向相反。

2. 平面区域边界的外法向由正向单位切向量顺时针转直角得到$(\tau_2,-\tau_1)$，以单位圆上一点核对。

###### paragraph：定向曲面边界的诱导方向

1. 按右手约定定义诱导方向，等价地头朝法向沿边界前进时曲面在左侧，并给出左手方向$\bm u\times\bm f$的核对方法。

2. 例题核对向上圆盘与外向上半球面在单位圆上诱导出同一个从上方看逆时针的方向，说明二者都满足曲面在左侧。

3. 说明翻转法向则诱导方向翻转，分片曲面的相容定向使公共边积分相消；配图展示小正方形公共边相消与圆环两圈边界的方向。

#### 14.8.1 Green公式与平面边界

1. 说明平面边界上可累计切向分量（环流）或外法向分量（通量），分别对应$Q_x-P_y$与散度。

##### 14.8.1.1 Green公式的环流形式

1. 由小正方形环流近似与公共边相消预期区域内旋转累计等于边界环流；陈述Green公式及区域、光滑性与正向边界条件。

2. 矩形情形的证明：先写出四条边的贡献，再对$\partial_yP$与$\partial_xQ$分别用一元基本定理和累次积分，两行恰好对应四条边；说明矩形拼接时公共边抵消，一般区域引用教材。

3. 例题旋转场在单位圆盘上两侧都为$2\pi$，顺时针时左侧变号，说明公式的符号由正向边界约定决定。

4. 例题取$Q_x-P_y\equiv1$的场得到面积公式，算出椭圆面积$\pi\alpha\beta$，并提及求积仪原理。

5. 例题涡旋场在圆环上两圈环流$2\pi$与$-2\pi$相加为零，与右侧一致；说明环流来自原点的奇点，单位圆盘含原点不满足条件。

##### 14.8.1.2 Green公式的通量形式

1. 由小正方形净流出与公共边相消预期源强度总和等于边界净流出；由外法向与切向的关系得$\bm n\,\mathrm ds=(\mathrm dy,-\mathrm dx)$。

2. 陈述平面通量公式，证明取$(P,Q)=(-F_2,F_1)$代入Green公式；说明它是二维散度公式。

3. 例题单位圆盘上径向场的通量$2\pi$与散度积分一致，旋转场通量为零而环流为$2\pi$；以流体产生与杯中搅水解释通量与环流记录不同的边界分量。

#### 14.8.2 Gauss公式与封闭曲面

1. 说明边界从曲线变为闭曲面，关系仍是内部散度积分等于边界净通量。

##### 14.8.2.1 Gauss公式

1. 以流体守恒和小立方体公共面相消预期结论，并提及静电学中的对应；陈述散度定理的区域与光滑性条件，说明接缝面积为零、两侧有限。

2. 长方体情形的证明：逐坐标用一元基本定理与累次积分，把$\partial_xF_1$的体积积分化为两张面的通量，三项相加；说明拼接时公共面抵消，一般区域引用教材，无界或不规则情形需另用版本。配图说明共同面上两份通量抵消。

3. 例题用$\bm x/R$核对球面面积$4\pi R^2$，与球坐标体积和直接参数化结果一致。

4. 例题点源场在原点外散度为零，而球面通量为$4\pi$，因球含原点不满足条件；对球壳应用定理，外内球面通量相加为零。说明通量全部来自原点的点源，并给出点电荷的Gauss定律形式。

###### paragraph：散度是通量密度

1. 用长方体上的Gauss公式把小立方体净流出除以体积写成散度的平均值，由散度连续得极限为$\operatorname{div}\bm F(\bm a)$；换成小球得到同样极限，说明散度不依赖坐标轴方向。

#### 14.8.3 Stokes公式与曲面的边界

1. 说明另一类问题只给有边界的定向曲面，比较曲面上的旋转累计与边界环流，使用旋度的法向分量。

##### 14.8.3.1 Stokes公式

1. 由平面上旋度法向分量即$Q_x-P_y$、弯曲曲面切成小平面片与公共边相消、桨轮图像预期结论；陈述Stokes定理的曲面、定向与光滑性条件，并解释两侧都是标量。

2. 在参数曲面片上归结为参数平面上的Green公式：设定参数条件，记$A=\bm F^\top\bm r_u$、$B=\bm F^\top\bm r_v$，由链式法则把边界环流化为参数平面上的路径积分。

3. 计算$\partial_uB-\partial_vA$，二阶导数项因$\bm r_{uv}=\bm r_{vu}$抵消，得到$\bm r_v^\top(\bm J_{\bm F}-\bm J_{\bm F}^\top)\bm r_u$。

4. 用反对称矩阵作用等于与旋度作叉积及混合积轮换，化为旋度与有向面积元的内积；说明参数平面Green公式适用，相容拼片使公共边相消，一般定理引用教材。

###### paragraph：旋度分量是环流密度

1. 由Stokes公式把小圆盘边界环流除以面积写成旋度法向分量的平均值，取极限得到旋度分量是环流密度，并说明这一含义不依赖坐标轴。

##### 14.8.3.2 跨接曲面的选择

1. 说明左侧只依赖有向边界，同一有向边界的两张跨接曲面上旋度通量相等，可选较简单的曲面但不能穿过奇点。

2. 用$\operatorname{div}(\operatorname{curl}\bm F)=0$与散度定理从另一角度说明两张曲面通量之差为零。

3. 例题对$(-y/2,x/2,0)$分别在向上圆盘和外向上半球面上算得旋度通量都为$\pi$，并直接计算边界环流核对；改用向下圆盘时边界方向与积分同时变号。配图比较两张曲面，强调相等的是法向分量的累计而非面积。

#### 14.8.4 积分分部与Green恒等式

1. 说明分部积分把导数转移到另一因子并留下边界项；由乘积法则$\operatorname{div}(u\bm F)=\nabla u^\top\bm F+u\operatorname{div}\bm F$与Gauss公式得到一般分部公式，边界项在$u=0$或法向分量为零时消失。

2. 回顾一元分部积分并把端点项按外法向$\pm1$拆开，列出多元推广中各项的对应关系。

3. 陈述多元分部积分定理，证明对$u\nabla v$求散度后代入Gauss公式；说明平面情形改用平面通量公式，边界项是否为零由边界条件决定。

4. 例题取$u=1$、$v=\lVert\bm x\rVert^2$在球上核对两侧都为$8\pi R^3$。

5. 例题证明Laplace方程的解由边界值唯一决定：取$u=v=w$得梯度平方积分为零，由连续非负推出梯度为零，再由连通性与边界值得$w\equiv0$；按热传导解释稳态温度由边界温度决定。

6. 交换$u,v$相减得到Green第二恒等式，说明在积分中把$\Delta$从$v$移到$u$上只差边界项。

###### paragraph：积分公式的比较

1. 说明各公式回答同一类问题且推导方式相同，用表格对照一元基本定理、路径积分基本定理、Green、Gauss、Stokes公式的内部积分与边界积分。

2. 说明Stokes公式在平面上还原为Green环流形式，Green通量形式是二维散度公式；普通标量函数的区域积分要先找到散度或旋度分量等于被积函数的场，以面积公式为例。

3. 用Stokes公式解释势函数的存在与定义域有关：闭路径若是定义域内某张曲面的边界，无旋场的环流为零；星形域中锥面落在定义域内，穿孔平面上绕原点的圆所围圆盘必含原点。

4. 总结使用条件：核对连续可微性、分片规则边界与定向，尤其是场在积分对象附近是否有定义；边界在边界积分中是累计对象，须知道场在边界上的取值与可延拓性；降低规则性需另建弱导数与边界迹的公式。

### 14.9 本章小结

1. 区域积分部分：Jordan区域的边界可被任意小体积覆盖，闭包上的连续函数可积；连续被积函数和连续边界函数下可按截面逐次积分；换元时$|\det DT|$给出局部体积缩放且须单次覆盖；连续性的一致控制允许在积分号下求导；无界情形用截断，不同截断可给出不同极限。

2. 路径与曲面积分部分：第一类积分按弧长和面积累计、与方向无关；第二类积分计算功与通量，随方向反转变号，换参数须保持方向；保守场的功只取决于端点，交叉偏导相等在星形域上保证势函数存在，在有孔区域上不够。

3. 积分关系部分：散度是单位体积的净流出，旋度分量是单位面积的环流；Green、Gauss、Stokes公式联系内部的散度或旋度累计与边界通量或环流，使用时须检查场在积分对象附近的光滑性、边界完整性与方向相容。
