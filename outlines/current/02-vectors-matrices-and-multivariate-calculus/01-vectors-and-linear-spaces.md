# 卷二《向量、矩阵与多元微积分》第一部分：向量与线性空间

所属：卷二《向量、矩阵与多元微积分》第一部分“向量与线性空间”，本卷第1—3章。正文入口：[volume.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/volume.tex) → [part.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/part.tex)。以下按实际正文顺序记录内容提要。

## 部分主线

本部分回答怎样表示线性对象、怎样对它们实施运算，以及怎样在它们所在的空间中度量大小、接近与垂直。第1章把数据记成向量、矩阵与多轴数组，按索引个数建立具体运算，逐项核对形状条件、输出形状与运算规则；第2章把数组与它记录的对象分开，用线性空间、基与坐标、线性映射的矩阵和对偶空间说明哪些量依赖表示、哪些量与基无关；第3章给线性空间补上范数与内积，建立有限维的收敛、完备性、算子范数、正交投影与伴随。三章依次依赖：第2章用第1章的矩阵运算记录映射，第3章在第2章的空间与坐标上加入度量。本部分依赖卷一的实数与复数、映射与等价关系、有限求和及一元极限与最值定理，为后面的谱分析、线性方程与优化和多元微积分提供共同语言。

部分导读（`\BookPartGuide`，不计入章数）：

1. 说明本部分研究线性对象的表示、运算与空间几何，并列出所依赖的卷一内容：实数与复数、映射与等价关系、有限求和、一元分析中的极限、确界与最值定理。

2. 说明第1章按索引个数建立向量、矩阵与多轴数组的运算，每种运算核对形状条件、输出形状与规则；行列式、迹与Frobenius内积把矩阵变成一个数，张量积与缩约统一处理多重索引。

3. 说明第2章把数组与它记录的对象分开：线性空间规定可作线性组合的对象，基与坐标把对象记成一列数，线性映射在两端的基下记成矩阵，对偶空间研究读取规则；换基改变坐标与矩阵而不改变对象与映射，核、像、秩与基无关。

4. 说明第3章给线性空间补上度量：范数规定大小并定义收敛、极限与连续，在有限维中证明范数等价与完备性；内积再规定夹角与正交，得到正交分解、标准正交基、正交投影与伴随。

5. 提醒区分三组东西：数组与它记录的对象；矩阵乘法、逐项乘积与张量积这几种“乘积”对索引的不同处理；只依赖线性运算的结论（线性无关、维数、秩）与随范数或内积改变的结论（误差大小、夹角、最近点）。并说明这些内容是后面谱分析、线性方程与多元微积分共同使用的语言。

## 第1章 向量、矩阵与张量的运算

正文入口：[01-operations.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/01-operations.tex)，章内依次输入[01-vectors.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-operations/01-vectors.tex)、[02-matrices.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-operations/02-matrices.tex)、[03a-matrix-scalar-readouts.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-operations/03a-matrix-scalar-readouts.tex)、[04-tensors.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-operations/04-tensors.tex)、[05-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-operations/05-summary.tex)。

1. 从数据常是一组数进入：一列观测、一张特征表、带通道和像素位置的图像数组；指出三类数组的区别在于定位一个数所需的索引个数（一个、两个、更多）。

2. 列出最先遇到的计算需要：对一列数，要合并、配对并衡量误差大小；对一张表，要一次算出许多加权和、合成两次计算、撤销或重复一次计算，并知道方阵把面积放大多少倍；对多轴数组，要重排、组合并沿指定轴汇总。

3. 按定位一个数所需的索引个数说明前两节的分工：向量一节建立线性组合，并用坐标内积、长度与距离把配对、大小与差异变成一个数；矩阵一节由“接连两次加权求和”得到矩阵乘法，再用乘法表达可撤销的行变换、逆矩阵与矩阵的幂。

4. 说明后两节的分工：行列式、迹与Frobenius内积把矩阵变成一个数，其中行列式回答方阵把有向体积放大多少倍；张量一节把前面的运算统一为对索引的重排、组合与缩约。并说明每种运算都核对输入形状条件、输出形状与运算规则。

5. 限定范围与依赖：只在有限维实数组层面讨论，只用实数的四则运算、绝对值与平方根以及有限和可交换次序、重新分组的规则，跨卷注明可参考卷一“实数、复数与函数”一章（`chap:real-complex-functions`）；数组记录什么对象、矩阵怎样记录线性映射留给第~`chap:linear-representation`章，内积与范数的一般性质及一般空间中的长度、夹角与正交留给第~`chap:normed-inner-product-spaces`章。

### 1.1 向量

1. 从观测输入、输出与误差都是一串数进入，定义向量为按固定次序排列的一串实数，并说明本节的三类运算：加法与数乘合成向量，内积把两个向量配成一个数，长度和范数衡量向量的大小。

#### 1.1.1 向量的表示

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

#### 1.1.2 加法、数乘与线性组合

1. 以两列预测取平均、预测减观测为例，说明本小节要定义加法、数乘及由它们组成的线性组合，并整理运算规则。

##### 1.1.2.1 加法与数乘

1. 给出逐坐标加减与数乘的公式，引出$0\bm x=\bm0$与相反向量，指出结果的每个坐标只由输入的同一坐标决定、维数不变。

2. 示例`ex:ls-vector-addition-scaling`逐坐标计算一组二维向量的加法、减法与数乘。

3. 说明相加的两个条件：维数相同，否则无法逐位置配对；位置含义相同，否则算得出数却没有意义。

##### 1.1.2.2 线性组合

1. 把加法和数乘结合起来，定义线性组合与系数，说明结果的每个坐标是各向量在同一位置上的加权和，系数不要求非负或和为$1$。

2. 示例`ex:ls-residual-vector`把三次观测的残差$\bm r=w\bm x-\bm y$写成以$w,-1$为系数的线性组合，并在$w=1$时算出$\bm r=(1,-2,-3)^\top$。

3. 贯穿例`ex:ls-nearly-collinear-features`给出特征取值向量$\bm c_1$、$\bm c_2$与$\bm q$，逐坐标验证$\bm c_2=\bm c_1+\varepsilon\bm q$；随后一句说明方向“几乎相同”须等第~`sec:ls-inner-product-definition`节定义夹角后说明。

##### 1.1.2.3 加法与数乘的性质

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

#### 1.1.3 内积、长度与距离

1. 从加法与数乘的结果仍是向量过渡：数据分析还要把两个向量配成一个数、用一个数衡量向量大小；本小节只给坐标公式，一般性质在第~`chap:normed-inner-product-spaces`章证明。

##### 1.1.3.1 内积

1. 由线性预测的加权和引出欧氏内积$\langle\bm x,\bm y\rangle=\sum_jx_jy_j=\bm x^\top\bm y$，说明输入两个同维向量、输出标量，并预告它是$1\times d$与$d\times1$矩阵的乘积。

2. 定义内积为零即正交；示例`ex:ls-inner-product-orthogonality`计算三对平面向量的内积，第一对为$2$不正交，后两对为$0$正交。

3. 指出平面上正交就是垂直，一般维数下的理解须等第~`sec:ls-inner-product-definition`节定义夹角。

##### 1.1.3.2 长度与距离

1. 由$\langle\bm x,\bm x\rangle$是平方和而非负，定义长度（式`eq:linear-algebra-inner-product-norm`）与欧氏范数$\lVert\bm x\rVert_2$，说明它推广了勾股定理。

2. 定义单位向量，说明非零向量除以自身长度得到同方向的单位向量。

3. 定义欧氏距离为差向量的长度；示例`ex:ls-length-distance`算出残差长度平方$14$（即平方误差总和）与两点距离$5$。最后提醒比较实际数据前应统一各坐标的单位和尺度。

##### 1.1.3.3 范数

1. 从欧氏长度先平方再相加出发，说明还可以累加绝对值或只看最大绝对值，这些大小度量统称范数。

2. 给出$p$范数与$\infty$范数的公式并解释$p=1,2,\infty$的含义；示例`ex:ls-p-norms`在$(3,-4)^\top$上得到$7,5,4$。

3. 用图`fig:ls-norm-unit-balls`比较三种单位球的形状，并说明非负性、正定性与齐次性可从公式看出，三角不等式见定理`thm:linear-algebra-minkowski`。

4. 本节收束：概括三类运算，并说明把若干向量并排得到矩阵。

### 1.2 矩阵

1. 从样本特征表上用同一组权重求加权和进入，说明矩阵就是这样的数表，矩阵乘法一次写出这些加权和。

2. 说明本节先规定写法、再逐个讨论运算，每种运算先定义后整理性质；重点是矩阵乘法保留结合律与分配律而失去交换律与消去律；最后三小节用乘法回答怎样用可撤销步骤化简、怎样撤销一次乘法、怎样记录反复作用。

#### 1.2.1 矩阵的表示与常见矩阵

1. 指出数表中的一个数需要行、列两个索引定位。

###### paragraph：矩阵、元素与形状

1. 定义$m\times d$矩阵、元素$\bm A_{i,j}$、形状及行列记号$\bm A_{i,:}$、$\bm A_{:,j}$，以一个$2\times3$矩阵举例。

2. 规定矩阵相等，并说明行向量与列向量是矩阵的特例。

###### paragraph：设计矩阵

约定行对应样本、列对应特征，把示例`ex:ls-nearly-collinear-features`的$\bm c_1,\bm c_2$并排为贯穿例$\bm X_\varepsilon=[\bm c_1\ \bm c_2]$（式`eq:linear-algebra-nearly-collinear-design`），说明后面各章用它考察两列几乎相同时的问题。

##### 1.2.1.1 常见矩阵

1. 从元素分布的固定模式（大部分位置为零或关于主对角线对称）进入，说明下面逐类定义并举例；它们在乘法下的固定模式在1.2.5.3（`sec:ls-common-matrix-products`）中随乘法讨论，依赖内积的正交矩阵与正定矩阵留到第~`chap:normed-inner-product-spaces`章。

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

#### 1.2.2 加法与数乘

1. 说明加法与数乘沿用向量的逐项规则，给出同形矩阵逐项加减与数乘的元素公式，指出结果形状不变；示例`ex:ls-matrix-addition-scaling`对一组二阶矩阵逐项计算，以$(2,1)$元核对。

2. 说明相加要求形状相同、对应位置含义相同；以$2\times3$与$3\times2$矩阵说明元素个数相同也不能相加，并指出同形矩阵的线性组合按同样方式定义。

##### 1.2.2.1 加法与数乘的性质

1. 由逐项运算说明向量的八条规则在每个位置上照样成立，列出同形矩阵的八条规则，并指出每条都可在任一位置上用实数运算验证。

#### 1.2.3 转置

1. 用$(\bm A^\top)_{j,i}=\bm A_{i,j}$定义转置，说明形状交换而数值不变、第$i$行成为第$i$列，并与向量的转置一致；示例`ex:ls-transpose-two-by-three`转置一个$2\times3$矩阵。

##### 1.2.3.1 转置的性质

1. 说明转置只改变元素位置，本小节只给出它与加法、数乘的关系及转置两次的结果；与矩阵乘积的关系待定义乘法后在1.2.5.2讨论。

###### paragraph：与加法、数乘交换

说明转置只搬动元素，因而$(\bm A+\bm B)^\top=\bm A^\top+\bm B^\top$、$(c\bm A)^\top=c\bm A^\top$。

###### paragraph：转置的转置

列出$(\bm A^\top)^\top=\bm A$：$(i,j)$元先搬到$(j,i)$再搬回。

#### 1.2.4 矩阵与向量的乘积

1. 由$n$次观测共用一组权重的加权和引出$\bm A\bm u$，给出元素定义（式`eq:prelim-matrix-prediction`），要求矩阵列数等于向量维数。

2. 说明按行（各行与$\bm u$的内积）与按列（各列以$u_j$为系数的线性组合）两种算法结果相同；由按列算法得$\bm A\bm e_j=\bm A_{:,j}$，并指出贯穿例$\bm X_\varepsilon\bm w=w_1\bm c_1+w_2\bm c_2$。示例`ex:ls-matrix-vector-rows-columns`核对两种算法。

3. 示例`ex:ls-affine-predictions`在$x=1,2,3$处计算$ax+b$，说明全$1$列给出截距；再写出残差$\bm X\bm w-\bm y$与平方误差总和$\lVert\bm X\bm w-\bm y\rVert_2^2$，并把结论推广到$n$个样本、$d$个特征。

#### 1.2.5 矩阵乘法

1. 由两次加权求和$\bm y=\bm B\bm x$、$\bm z=\bm A\bm y$出发，说明这是两个映射的复合：前一映射的输出落在后一映射的定义域$\mathbb R^d$中；映射复合的一般定义跨卷注明可参考卷一“集合、关系与映射”一章（`chap:sets-relations-maps`）。

2. 逐坐标代入并交换有限求和次序（式`eq:linear-algebra-matrix-product`），说明$\bm z$仍是$\bm x$的加权和，括号中的系数排成的表就是乘积。

3. 给出元素公式（式`eq:prelim-matrix-composition`）与形状条件，指出被求和的公共维数就是中间结果的维数，并说明矩阵乘向量与内积（$1\times1$矩阵与其元素等同）是特例。

4. 以$2\times3$乘$3\times2$的非方阵算例说明左矩阵列数须等于右矩阵行数、输出保留左矩阵的行数与右矩阵的列数。

##### 1.2.5.1 矩阵乘法的性质

1. 说明矩阵乘法保留结合律和分配律、一般不满足交换律和消去律，逐条核对并检查形状要求。依次给出单位乘、零乘、结合律、分配律与分块乘法，再说明交换律与消去律不成立；乘积的转置与常见矩阵的乘法模式分别放在其后两小节。

###### paragraph：单位乘

1. 用$\bm I_m$的第$i$行是$\bm e_i^\top$说明$\bm I_m\bm A=\bm A=\bm A\bm I_d$，单位矩阵相当于数$1$。

###### paragraph：零乘

1. 给出$\bm0\bm A=\bm0$与$\bm A\bm0=\bm0$，说明一个因子全为零时乘积为零，零矩阵的形状由另一个因子决定。

2. 指出逆命题不成立：示例`ex:ls-zero-product-nonzero-factors`给出两个非零矩阵的乘积为零。

3. 按列解释原因：$\bm A\bm B$的第$j$列是$\bm A$乘$\bm B$的第$j$列，$\bm A\bm B=\bm0$恰好意味着$\bm B$的每一列都被$\bm A$清零；回到示例说明两列如何被清零。

###### paragraph：结合律

1. 展开两边元素都为$\sum_k\sum_l a_{i,k}b_{k,l}c_{l,j}$，指出这是映射复合结合律的矩阵形式（先合并哪两步，得到的都是同一个映射）；取$\bm C$为列向量回到引出乘法定义的计算，并说明连乘可省略括号。

###### paragraph：分配律与数乘相容

1. 逐项展开有限和得到两条分配律与数乘相容，并以右因子取列向量得到矩阵与向量的乘积保持线性组合（式`eq:prelim-matrix-linearity`）。

2. 由此说明$\bm u\mapsto\bm A\bm u$由它在$\bm e_1,\ldots,\bm e_d$上的输出即$\bm A$的各列完全确定，并说明第~`chap:linear-representation`章将这样的函数称为线性映射。

###### paragraph：分块乘法

1. 以$2\times2$分块写出块乘公式，给出块尺寸相容的条件，并用中间索引的求和可按列块分段说明理由；指出块的次序不能交换。

2. 把块分到最细，得到按列、按行与“列乘行之和”（式`eq:ls-product-outer-sum`）三种特例，说明后者是第~`chap:matrix-approximation`章低秩近似的出发点；示例`ex:ls-product-as-outer-sum`把一个二阶乘积写成两个“列乘行”矩阵之和，与逐项计算的结果核对。

###### paragraph：交换律不成立

1. 说明形状不同时两种次序未必都有定义，同阶方阵的两种乘积也可能不同；示例`ex:ls-noncommuting-pair`用“只保留第一个坐标”与“交换两个坐标”说明两种作用次序结果不同，并约定作用顺序从右向左。

###### paragraph：消去律不成立

1. 由$\bm A\bm B=\bm A\bm C$等价于$\bm A(\bm B-\bm C)=\bm0$，借零乘的反例说明非零左因子不能消去；示例`ex:ls-cancellation-fails`给出具体反例。

2. 回指第~`sec:prelim-inverse-matrices`节，说明左因子可逆时两边左乘逆矩阵即可消去。

##### 1.2.5.2 转置与乘积

1. 回指1.2.3.1的转置性质只涉及加法、数乘与转置本身，说明乘法把行与列配对求和、转置交换行与列，因此需要单独考察乘积转置后因子的排列；本小节先给出规则，再给出内积与对称性两个推论。

###### paragraph：乘积的转置

逐元素推出$(\bm A\bm B)^\top=\bm B^\top\bm A^\top$，并推广到多个因子时次序整体反转。

###### paragraph：内积中的转置

由乘积的转置得到$\langle\bm A\bm x,\bm y\rangle=\langle\bm x,\bm A^\top\bm y\rangle$，说明作用在左侧向量上的$\bm A$可改写为作用在右侧向量上的$\bm A^\top$。

###### paragraph：$\bm A^\top\bm A$对称

由乘积的转置证明$\bm A^\top\bm A$与$\bm A\bm A^\top$总是对称矩阵，示例`ex:ls-gram-product-symmetric`对一个$2\times3$矩阵算出$\bm A\bm A^\top$，其两个非对角元都是两行的内积。

##### 1.2.5.3 常见矩阵的乘法

1. 回指1.2.1.1的常见矩阵，说明它们参与乘法时结果有固定模式，下面逐类说明；对称矩阵一类要用到上一小节的乘积转置规则。

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

#### 1.2.6 矩阵的逐项乘积

1. 与对公共索引求和的矩阵乘法对照，定义只在同一位置相乘的Hadamard积（式`eq:ls-hadamard`），并推广到同维向量和同形数组。

2. 示例`ex:ls-hadamard-vs-matrix-product`对同一对矩阵分别计算两种乘积，结果在每个位置都不同；最后说明固定掩码$\bm M$时$\bm X\mapsto\bm M\odot\bm X$适合表达挑选或调制另一个数组。

##### 1.2.6.1 逐项乘积的性质

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

#### 1.2.7 初等行变换

1. 从解方程和求逆需要把矩阵逐步化简、且每步可撤销进入，引出三种初等行变换；约定$r_i$表示第$i$行，取同一个$3\times2$矩阵$\bm A$作演示，并定义初等矩阵：对单位矩阵执行同一变换所得的$\bm E$满足$\bm E\bm A$即变换结果。

2. 交换两行$r_i\leftrightarrow r_k$：只改变行的先后，图`fig:ls-row-swap`交换第$1$、$3$行，初等矩阵是相应的置换矩阵；再交换一次即复原，逆就是自身。

3. 一行乘以非零数$r_i\leftarrow cr_i$：图`fig:ls-row-scale`把第$2$行乘以$2$，初等矩阵为$\operatorname{diag}(1,2,1)$；乘以$1/c$即可撤销，并说明$c=0$会抹去整行而无法恢复。

4. 一行加上另一行的倍数$r_i\leftarrow r_i+cr_k$（$i\neq k$）：图`fig:ls-row-replace`把第$3$行加上第$1$行的$-5$倍，使首元化为零，指出消元正用这种变换；初等矩阵只在$(3,1)$位置为$-5$，因提供倍数的行不变，可加回$5$倍撤销。

5. 总结三种逆操作仍是初等行变换，对应初等矩阵的逆，故初等矩阵可逆；接连若干次变换等于左乘这些初等矩阵之积，仍可逆。

6. 指出化为阶梯形、解线性方程组与求逆的具体做法放在第~`sec:ls-gaussian-elimination`节（第10章）与求解方法一起讨论。

#### 1.2.8 矩阵的逆

1. 以“撤销一次矩阵乘法”引出可逆与逆矩阵的定义（两侧乘积都等于$\bm I_n$）。

2. 证明可逆时方程$\bm A\bm x=\bm y$有唯一解$\bm A^{-1}\bm y$：左乘逆矩阵得唯一性，代回得存在性。

3. 由结合律证明逆矩阵唯一，因而记号$\bm A^{-1}$无歧义；随后一句说明求逆方法取决于矩阵结构，先给出对角矩阵与二阶方阵的逆，再说明一般方阵的求逆归结为解方程。

###### paragraph：对角矩阵的逆

对角元全非零时逐个取倒数得到逆；某个对角元为零时，左乘后乘积有一行为零，不可能等于$\bm I_n$，因而不可逆。

###### paragraph：二阶方阵的逆

给出$ad-bc\neq0$时的二阶求逆公式，以左上与右上元素核对乘积为单位矩阵，并指出分母是下一节的二阶行列式。

###### paragraph：一般方阵的逆

由$\bm A\bm A^{-1}=\bm I_n$按列看，$\bm A^{-1}$的第$j$列是$\bm A\bm x=\bm e_j$的解，说明求逆就是解$n$个系数矩阵相同的方程；用初等行变换一并求解、化简失败为何不可逆留到第~`sec:ls-gaussian-elimination`节，方阵何时可逆留到第~`chap:linear-solution-selection`章，并指出只解一个方程时不必先求逆。

###### paragraph：单侧逆

1. 定义矩形矩阵的左逆与右逆。

2. 说明有左逆时方程若有解则只能是$\bm L\bm y$，有右逆时$\bm R\bm y$总是一个解。

3. 指出单侧逆一般不唯一，示例`ex:ls-left-inverse-not-unique`给出无穷多个左逆。

##### 1.2.8.1 矩阵逆的性质

回到可逆方阵，指出求逆常与乘积、数乘和转置一起出现，下面四条规则说明可逆性在乘积、求逆、数乘与转置下保持，并给出逆的表达式。

###### paragraph：乘积的逆

1. 定理`thm:ls-inverse-product`陈述可逆方阵之积可逆且$(\bm A\bm B)^{-1}=\bm B^{-1}\bm A^{-1}$（式`eq:ls-inverse-product`），证明用结合律验证两侧乘积并引用逆的唯一性。

2. 用作用次序解释次序反转：先作用$\bm B$后作用$\bm A$，撤销时先撤销$\bm A$。

###### paragraph：逆的逆

由定义中$\bm A$与$\bm A^{-1}$地位对称得到$(\bm A^{-1})^{-1}=\bm A$。

###### paragraph：数乘的逆

直接相乘验证$(c\bm A)^{-1}=c^{-1}\bm A^{-1}$（$c\neq0$）。

###### paragraph：转置的逆

由乘积的转置验证$(\bm A^\top)^{-1}=(\bm A^{-1})^\top$。

#### 1.2.9 矩阵的幂

1. 以同一方阵反复作用引出正整数幂、$\bm A^0=\bm I_d$与可逆时的负幂，并说明非方阵没有幂。

2. 示例`ex:ls-matrix-square-shear`说明矩阵平方不是逐元素平方。

3. 定义幂等矩阵与幂零矩阵；示例`ex:ls-idempotent-nilpotent`用$\operatorname{diag}(1,0)$与右上元为$1$、其余元素为$0$的二阶矩阵$\bm N$各举一例，从作用和直接相乘两方面验证。

##### 1.2.9.1 幂的性质

说明同一矩阵的幂满足与实数相同的指数法则，并给出指数的取值范围（可逆时可取任意整数）。

###### paragraph：同底幂相乘

1. 由结合律与相邻$\bm A\bm A^{-1}$逐对消去得到$\bm A^m\bm A^n=\bm A^{m+n}$，并指出同一矩阵的不同次幂可交换。

2. 与之对照，不同矩阵一般不交换，故$(\bm A+\bm B)^2$的中间两项只有在$\bm A\bm B=\bm B\bm A$时才能合并。

###### paragraph：幂的幂

由结合律去括号得到$(\bm A^m)^n=\bm A^{mn}$。

###### paragraph：负幂与逆相容

对$k$个相同因子反复使用式`eq:ls-inverse-product`得到$(\bm A^k)^{-1}=(\bm A^{-1})^k=\bm A^{-k}$。

### 1.3 行列式、迹与元素内积

1. 说明本节讨论三种把矩阵变成一个数的运算：行列式衡量有向体积的缩放，迹累加主对角元，Frobenius内积配对两个同形矩阵的对应元素；三者回答的问题不同，单凭一个数无法恢复矩阵。

#### 1.3.1 行列式

1. 用一句说明本小节的顺序：计算公式、几何意义、性质，最后由代数余子式构造古典伴随并证明方阵的单侧逆即逆。

##### 1.3.1.1 行列式的定义

1. 定义排列、逆序对数与符号，给出排列公式定义`def:ls-determinant`，解释每项从每行每列各取一个元素，行列式是元素的多项式。

2. 把每项按列号重排并用$\operatorname{sgn}(\pi^{-1})=\operatorname{sgn}(\pi)$得到按列的写法（式`eq:ls-det-column-form`）。

3. 由两个排列得到二阶公式$ad-bc$；由六个排列的奇偶得到三阶公式，示例`ex:ls-det-three-by-three`代入计算得$7$，并指出高阶时借助性质与消元计算。

##### 1.3.1.2 行列式的几何意义

1. 说明排列公式看不出度量什么，本小节从平行四边形面积与平行六面体体积满足的几何规则出发推出同一公式。

###### paragraph：有向面积

1. 按转向给平行四边形面积配符号，定义有向面积$S(\bm u,\bm v)$，给出三条规则：以一边为底、有向高是另一边在法方向上的分量，故对每边线性；交换两边变号，共线时为零；单位正方形面积为$1$。

2. 把两边按坐标展开成四项，用三条规则得到$u_1v_2-u_2v_1$，即二阶行列式。

3. 示例`ex:ls-oriented-area`用三组向量对说明交换次序变号、共线时面积为零。

###### paragraph：有向体积

1. 按右手系定义平行六面体的有向体积$V(\bm u,\bm v,\bm w)$，以底面积乘有向高说明对每条棱线性，交换两棱变号，单位立方体体积为$1$。

2. 展开成$27$项，说明下标重复的项因“交换相同向量既不变又变号”而为零。

3. 其余六项对应排列，每次相邻交换使逆序对数减一，故系数为$\operatorname{sgn}(\sigma)$，得到三阶行列式。

###### paragraph：一般维数

1. 指出展开只用到对每个向量线性与交换变号两条规则，得到式`eq:ls-det-volume`：满足两条规则的函数$D$等于$D(\bm e_1,\ldots,\bm e_d)$乘以行列式；反过来验证排列公式满足两条规则，故行列式是满足规则且在单位矩阵处取$1$的那个函数。

2. 取$D$为$d$维有向体积、代入$\bm a_j=\bm A\bm e_j$，说明$\det\bm A$是$\bm A$作用下有向体积的放大倍数：绝对值是体积比，符号表示定向；图`fig:ls-determinant-oriented-volume`展示平面上保定向与反定向两种情形。

##### 1.3.1.3 行列式的性质

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

##### 1.3.1.4 代数余子式与古典伴随

1. 说明按行分组把排列公式化为低阶行列式，再把这些低阶行列式排成与$\bm A$相乘得$(\det\bm A)\bm I_d$的矩阵。

###### paragraph：按行（列）展开

定义子矩阵$\bm A^{(i,j)}$与代数余子式，按第$i$行所取的列分类得到展开公式；示例`ex:ls-det-cofactor-expansion`沿第一行展开示例`ex:ls-det-three-by-three`的矩阵，结果一致。

###### paragraph：古典伴随恒等式

1. 定义古典伴随$\operatorname{adj}(\bm A)=\bm C^\top$，定理`thm:ls-adjugate-identity`给出$\bm A\operatorname{adj}(\bm A)=\operatorname{adj}(\bm A)\bm A=(\det\bm A)\bm I_d$，证明区分$i=k$的展开与$i\neq k$时换行后两行相同。

2. 指出二阶情形就是二阶求逆公式。

3. 区分古典伴随与第~`sec:ls-adjoints`节由内积定义的伴随，说明其阶乘级代价使它主要作为证明工具，并列出它在单侧逆、线性方程的可逆判据（第~`sec:ls-determinant-invertibility`节）与Cayley--Hamilton定理（第~`sec:ls-characteristic-polynomial`节）中的用途。

###### paragraph：方阵的单侧逆即逆

1. 回指第~`sec:prelim-inverse-matrices`节要求两侧乘积为单位矩阵，定理`thm:ls-square-one-sided-inverse`说明方阵只需一侧；证明由乘法性得$\det\bm A\neq0$，用古典伴随构造逆，再用结合律说明单侧逆等于它。

2. 指出检验方阵的逆只需一侧乘积，并与矩形矩阵单侧逆可能只存在一侧或不唯一（示例`ex:ls-left-inverse-not-unique`）对照。

#### 1.3.2 迹

1. 与用到全部元素的行列式对照，定义方阵的迹为主对角元之和，以二阶例子区分迹与全部元素之和。

##### 1.3.2.1 迹的性质

1. 说明前两条可直接看出，循环性最常用。

###### paragraph：线性

由有限和的线性得到迹的线性。

###### paragraph：转置不变

转置不改变对角元。

###### paragraph：循环性

1. 用交换双重求和次序证明$\operatorname{tr}(\bm A\bm B)=\operatorname{tr}(\bm B\bm A)$（式`eq:linear-algebra-trace-cyclic`），强调两个乘积可以不同阶；示例`ex:ls-trace-cyclic-different-sizes`以$1\times1$与$3\times3$乘积核对。

2. 说明三个因子时只能整体循环移动，并解释两个等号各把哪两部分看作因子；示例`ex:ls-trace-adjacent-swap`给出交换相邻因子改变迹的反例。

#### 1.3.3 矩阵的元素内积

1. 说明行列式与迹只用到一个方阵，比较两个同形矩阵时可像向量内积那样配对全部对应元素。

##### 1.3.3.1 Frobenius内积

1. 把$mn$个元素看作坐标照搬欧氏内积，定义Frobenius内积并指出它等于$\bm A\odot\bm B$的元素和；示例`ex:ls-frobenius-inner-product`沿用逐项乘积一例的矩阵得到$5$。

###### paragraph：Frobenius内积的迹表示

由$\bm A^\top\bm B$的对角元证明$\langle\bm A,\bm B\rangle_{\mathrm F}=\operatorname{tr}(\bm A^\top\bm B)$与$\lVert\bm A\rVert_{\mathrm F}^2=\operatorname{tr}(\bm A^\top\bm A)$；反过来说明计算$\operatorname{tr}(\bm A\bm B)$不必先求乘积，比较$mn$与$m^2n$次乘法的代价。

##### 1.3.3.2 Frobenius范数

1. 由Frobenius内积定义Frobenius范数并举例，说明它是元素排成一列后的$2$范数，范数性质见第~`sec:ls-normed-space-definition`节。

2. 从作用解释$\lVert\bm A\rVert_{\mathrm F}^2=\sum_j\lVert\bm A\bm e_j\rVert_2^2$，区分它与最坏输入的放大倍数，后者在第~`sec:ls-matrix-norms`节讨论。

3. 简述按组汇总的混合范数$\lVert\bm A\rVert_{p,q}$。

### 1.4 张量

1. 从图像、文本数组需要三个以上索引进入，说明本节先给记法，再按对轴的作用讨论三类运算（重排、张量积与Kronecker积、缩约）并各自整理性质，最后指出内积、矩阵乘法与迹都是缩约。

#### 1.4.1 张量的表示

1. 由多路索引引出机器学习中所说的张量。

2. 说明数学中的张量还有不依赖坐标的定义（多线性映射或张量积空间的元素），本节只采用坐标数组的口径，数组与多线性映射的联系在第~`sec:ls-multilinear-maps`节选定基以后说明；随后给出多维数值数组的定义`def:linear-algebra-multidimensional-array`（轴、阶、形状），说明向量、矩阵、标量分别是一、二、零阶数组，轴长不改变阶。

3. 以$\bm X\in\mathbb R^{b\times\ell\times d}$说明三个索引与切片，图`fig:ls-scalar-vector-matrix-tensor`并排比较四类数组。

4. 说明同形数组逐项加法与数乘照旧，并强调须先说清每条轴的含义，否则汇总会落在错误的轴上。

#### 1.4.2 张量的重排

1. 转入第一类运算：轴置换与形状重整只改变元素位置，不改变数值、不求和；先分别讨论两种重排，再整理共同性质。

##### 1.4.2.1 轴置换

1. 定义维度重排（轴置换），以交换后两条轴为例写出$y_{i,k,j}=x_{i,j,k}$，指出每个样本切片被转置；示例`ex:ls-axis-swap`给出具体小数组。

2. 指出两条轴时唯一不平凡的轴置换就是转置，并说明轴的含义跟着轴走。

##### 1.4.2.2 形状重整与向量化

1. 定义形状重整为“按遍历顺序读出、再按同序装入”，只要求元素总数不变；示例`ex:ls-reshape-vs-transpose`比较按行重整与转置，图`fig:vol1-add-linear-transpose-reshape`并排展示，说明重整须给出遍历顺序。

2. 定义按列堆叠的向量化及元素$a_{i,j}$的位置$i+(j-1)m$，以示例矩阵核对。

3. 说明矩阵展开把部分轴合并为行、其余合并为列，所选的轴决定形状与后续汇总的轴。

##### 1.4.2.3 重排的性质

1. 用一句概括三条性质：不丢失信息、与逐项运算可交换、一般重整与矩阵乘法不相容。

###### paragraph：可逆性

说明固定形状与遍历顺序后重排一一对应、可由逆操作恢复，给出$\operatorname{vec}^{-1}$的装回方式。

###### paragraph：线性

说明向量化、轴置换与形状重整都保持线性组合，因为它们只搬动元素。

###### paragraph：与矩阵乘法的关系

对照转置与乘法的规则，说明一般重整改变每行每列汇集的元素；示例`ex:ls-reshape-breaks-product`把重整结果误当转置，两个乘积的迹分别为$91$与$86$，并指出把存储格式改变误当计算变换是常见错误。

#### 1.4.3 张量积

1. 转入第二类运算，定义两个向量的张量积$(\bm x\otimes\bm y)_{i,j}=x_iy_j=\bm x\bm y^\top$，联系“列乘行”（式`eq:ls-product-outer-sum`），引入槽位并推广到多个因子；示例`ex:ls-tensor-product-two-vectors`计算二维例，说明各行、各列分别成比例。

2. 图`fig:ls-tensor-product-slots`用长度不同的两个因子展示行轴与列轴的槽位。

3. 给出任意数组的张量积定义，说明输出有$k+\ell$条轴、不求和，交换输入会交换两组轴的次序。

4. 定义简单张量，示例`ex:ls-identity-not-simple`证明$\bm I_2$不是简单张量；再说明每个二阶数组都是简单张量$\bm e_i\otimes\bm f_j$的和。

5. 说明张量积的用处：双线性函数$B(\bm x,\bm y)=\langle\bm G,\bm x\otimes\bm y\rangle_{\mathrm F}$由系数表$\bm G$决定且对$\bm x\otimes\bm y$线性，以欧氏内积$\bm G=\bm I$为例。

6. 指出二阶张量与矩阵是同一组数的两种看法。

##### 1.4.3.1 张量积的性质

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

#### 1.4.4 Kronecker积

1. 由两个矩阵分别作用在两条轴上的联合作用引出Kronecker积（式`eq:linear-algebra-kronecker-product`），说明把每个元素替换为块；示例`ex:ls-kronecker-two-by-two`计算二阶例，图`fig:ls-kronecker-block-structure`展示分块结构。

2. 说明Kronecker积与张量积共用记号$\otimes$、记录同一组数而排法不同：两个列向量的Kronecker积是$\bm x\otimes\bm y$按行读出的结果，以$(3,-1,6,-2)^\top$核对；一般矩阵时张量积保留四条轴而Kronecker积排成两条，须按上下文和输出形状区分。

##### 1.4.4.1 Kronecker积的性质

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

2. 说明它把关于未知矩阵的方程化为普通线性方程组，第~`chap:matrix-equations`章求解矩阵方程时将用到。

#### 1.4.5 指标缩约

1. 与保留全部槽位的张量积对照，说明缩约沿指定的轴求和、减少轴的个数。

2. 给出计算规则：选定长度相同的轴对、共用求和索引、逐项相乘后求和，被求和的轴消失、其余轴按原次序保留，写出索引即可检查；示例`ex:ls-contraction-shapes`给出消去两对轴得$m\times n$矩阵、消去一对轴得$b\times\ell\times h$数组两种情形。

3. 图`fig:ls-tensor-contraction`展示沿列轴求和，并说明这也是与全$1$向量的缩约。

4. 逐项说明内积、矩阵乘法、迹与Frobenius内积都是缩约，指出各自消去哪些轴。

##### 1.4.5.1 缩约的性质

1. 说明缩约只由有限次乘法与求和组成，因此满足以下规则。

###### paragraph：线性

以示例`ex:ls-contraction-shapes`（2）为例展开，说明固定配对数组后缩约对被作用数组线性，一般情形中每个输出元素都是固定系数的加权和。

###### paragraph：求和次序可交换

说明多对轴的缩约与先消去哪一对无关，以$c_{i,j}$两种求和次序为例。

###### paragraph：简单张量系数可分离

证明系数为简单张量时三重求和分离为三个内积之积（式`eq:linear-algebra-rank-one-contraction`），计算量从$mnp$降到$m+n+p$；示例`ex:ls-rank-one-contraction-check`数值核对得$8$。

###### paragraph：非线性操作不是缩约

由缩约满足$\mathcal C(2\bm X)=2\mathcal C(\bm X)$，用逐元素平方说明逐元素非线性操作与$\operatorname{softmax}$不是缩约，并指出由缩约与非线性操作交替组成的模型不能因每步缩约线性就推出整体线性。

### 1.5 本章小结

1. 回顾本章按索引个数组织，并对每种运算交代输入条件、输出形状与规则。

2. 概括向量部分：逐坐标的加法与数乘组成线性组合，内积配对、长度与$p$范数衡量大小，一般性质留到第~`chap:normed-inner-product-spaces`章。

3. 概括矩阵部分：乘法来自复合，满足结合律与分配律而不满足交换律与消去律；初等行变换可撤销，每种都等于左乘可逆的初等矩阵；逆撤销一次乘法，对角矩阵与二阶方阵有直接公式，一般方阵的求逆归结为解$n$个方程、算法留到第~`sec:ls-gaussian-elimination`节；幂记录反复作用。

4. 概括行列式、迹与Frobenius内积：行列式是有向体积的缩放倍数且非零恰对应可逆，由古典伴随得到方阵单侧逆即逆；迹累加对角元并有循环性；Frobenius内积配对全部元素并给出Frobenius范数。

5. 概括张量部分：重排只改位置，张量积与Kronecker积保留全部轴，缩约沿指定轴求和，内积、矩阵乘法与迹都是缩约。

6. 按对索引的处理（配对求和、同位置相乘、全部保留）区分各种乘积，表`tab:linear-algebra-products-and-shapes`汇总形状条件与索引作用，并给出遇到乘积记号时的检查顺序。

7. 说明后续章节的分工：第~`chap:linear-representation`章讨论数组记录的对象与线性映射，第~`chap:normed-inner-product-spaces`章讨论一般空间的大小、夹角与正交；矩阵反复作用的长期行为见第~`chap:linear-recurrence-stability`章，误差经一次矩阵作用的放大见第~`chap:condition-and-spectral-perturbation`章，方程的解与求解方法从第~`chap:linear-solution-selection`章开始。

## 第2章 线性空间、映射与坐标

正文入口：[02-linear-spaces.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-linear-spaces.tex)，章内依次输入[01-vector-spaces.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-linear-spaces/01-vector-spaces.tex)、[02-bases-dimension-coordinates.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-linear-spaces/02-bases-dimension-coordinates.tex)、[03-linear-maps.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-linear-spaces/03-linear-maps.tex)、[04-dual-spaces.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-linear-spaces/04-dual-spaces.tex)、[05-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/02-linear-spaces/05-summary.tex)。

1. 指出第~`chap:linear-operations`章没有区分数组与它记录的对象：以仿射函数$f_{a,b}(t)=a+bt$为例，函数本身可以相加缩放，选定$1$与$t$后才记成$(a,b)^\top$，换一组基本函数则记录改变而函数不变。

2. 再以设计矩阵$\bm X_\varepsilon$（式`eq:linear-algebra-nearly-collinear-design`）说明矩阵既是数表，也记录从两个系数到三个拟合值的作用，由此提出本章任务：把对象与记录对象的数分开。

3. 说明前两节的分工与依赖：记录之前先确定线性组合的范围，第~`sec:ls-vector-spaces`节统一出线性空间并研究子空间与商空间；第~`sec:ls-bases-dimension-coordinates`节选基，用张成与线性无关保证坐标唯一，由基的个数得维数，换基时坐标按可逆矩阵换算而对象不变。

4. 说明后两节的分工：对象记录清楚后，第~`sec:ls-linear-maps`节把保持线性组合的作用在两端的基下记成矩阵，用核与像描述消去的输入与可达的输出，由换基得到相抵与相似；第~`sec:ls-dual-spaces`节讨论把向量读成一个数的线性泛函，并说明转置记录“把输出端的读取传回输入端”。

5. 交代范围：在实数域上展开，涉及复数另作说明；只用加法和数乘，所需矩阵运算来自第~`chap:linear-operations`章，长度、收敛与正交留给第~`chap:normed-inner-product-spaces`章。

### 2.1 线性空间与子空间

1. 承接章首，说明记录对象之前要先确定线性组合的范围；本节先定义线性空间，再讨论对线性组合封闭的部分（子空间）以及子空间的比较、合并与商空间。

#### 2.1.1 线性空间的定义与示例

1. 从数组、位移、信号与多项式都满足第~`sec:ls-vector-operation-rules`节的八条规则出发，指出后续关于分解、方程的解和维数的结论只依赖这些规则。

2. 据此统称带有这样加法与数乘的集合为线性空间，“向量”从此指可作线性组合的对象，不再要求是一列数。

3. 给出实线性空间定义`def:ls-real-vector-space`，区分封闭与运算规则两层要求，并说明有了这些规则，有限线性组合有确定意义，与数组的线性组合一致。

4. 简述复线性空间：规则相同而数乘允许复数；以$\mathbb C$在复数与实数数乘下分别需要一个与两个方向，说明标量范围改变线性结构，并说明本章其余推导在实数域中进行。

5. 以$\mathbb R^d$、全体$m\times d$矩阵与次数不超过$k$的多项式空间$P_k$为正例，指出章首的仿射函数全体就是$P_1$。

6. 示例`ex:ls-non-vector-space-sets`以$x_1=1$的集合（加法不封闭、不含零向量）与非负向量集合（数乘不封闭）为反例，结论是判断须逐项检查封闭与规则，不能只看形状。

#### 2.1.2 子空间、和与直和

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

3. 把交与联立两组齐次方程对应，例如$\{x_1=0\}\cap\{x_2=0\}$，说明求交可用第~`sec:ls-elementary-row-operations`节的消元完成，解集的系统讨论留给第~`chap:linear-solution-selection`章。

###### paragraph：和

1. 定义和空间$U+W$，证明它对线性组合封闭，且是同时包含二者的最小子空间。

2. 说明并集虽是包含二者的最小集合，但一般对加法不封闭；示例`ex:ls-union-not-subspace`以两条坐标轴之并不含$\bm e_1+\bm e_2$为例，结论是和空间补入了必需的线性组合。

###### paragraph：直和与补空间

1. 从平面上两条不平行直线给出唯一分解的直观，指出唯一与否由两个子空间的交决定。

2. 定理`thm:ls-direct-sum-uniqueness`（和的分解唯一的条件）：$U+W$中分解唯一当且仅当$U\cap W=\{\bm0\}$；证明分充分性（两种分解之差落在交中）与必要性（交中非零向量给出零向量的两种分解）。

3. 定义直和$U\oplus W$，强调唯一分解不要求垂直。

4. 定义补空间，以平面直线说明补空间不唯一；存在性留到下一节用基扩充证明（`sec:ls-dimension`）。

#### 2.1.3 商空间

1. 与和、直和相反，提出有意忽略某个子空间内差别的需要：只关心截距时，$f_{a,b}$与$f_{a,b'}$之差落在$\{st\}$中而无区别。

2. 再以非齐次约束$x_1=1$的解集是特解加齐次解子空间为例，归纳共同点：相差某个子空间中的向量即视为相同。

3. 把这一点写成关系$\bm x\sim\bm y\iff\bm x-\bm y\in U$，说明等价关系即满足自反、对称、传递的关系（跨卷注明可参考卷一“集合、关系与映射”一章，`chap:sets-relations-maps`），再逐条验证三条性质。

4. 写出等价类$\bm x+U$即$U$的平移，说明类相等只要求代表元之差在$U$中，全部类划分$V$；图`fig:ls-quotient-equivalence-classes`以平面中平行于$x$轴的直线展示这种划分。

5. 借代表元定义类的加法与数乘，给出商空间定义`def:linear-algebra-quotient-space`。

6. 验证运算与代表元选取无关，再说明零类、相反类与其余规则的继承，得出$V/U$是线性空间；回到图例说明商空间只记录高度。

7. 强调商空间的元素是整条平行线而不是挑出的代表点：在每条线上取与$y$轴的交点作代表，等于另选补空间，换一条过原点的非水平直线代表点就变而类不变，所以商空间不依赖代表元或补空间的选择。

8. 示例`ex:ls-quotient-intercept`计算$P_1$对$\{st\}$的商：每个类只依赖截距，类相等当且仅当截距相等，运算即截距的相加缩放，$f_{a,b}+U\mapsto a$是保持运算的双射。

9. 指出商空间的维数在下一节计算（`sec:ls-dimension`），与线性映射的联系见第~`sec:ls-kernel-image`节。

### 2.2 基、维数与坐标

1. 说明本节用有限个数记录对象：先用张成与线性无关判断系数的存在与唯一，二者同时成立即为基，基的向量个数是维数；最后定义坐标并推导换基时的换算。

#### 2.2.1 张成与线性无关

###### paragraph：张成

1. 由平面上一个方向与两个不共线方向能到达范围的对比，定义张成空间（式`eq:ls-span`）。

2. 证明张成空间是子空间且是包含该组向量的最小子空间，定义生成组。

3. 在$\mathbb R^m$中按列读法把张成空间写成$\{\bm V\bm a\}$，指出它即后文的列空间；图`fig:ls-linear-combination-span`对比两个方向张成平面与一个方向只得直线。

###### paragraph：线性无关

1. 指出张成不管表示方法有几种，以$\bm u=(1,0)^\top$、$\bm v=(1,1)^\top$、$\bm w=(2,1)^\top$为例：目标$(3,2)^\top$既是$\bm u+2\bm v$又是$\bm v+\bm w$，原因是$\bm w=\bm u+\bm v$没有带来新方向。

2. 两种写法相减得$\bm u+\bm v-\bm w=\bm0$，说明一般规律：表示不唯一与零向量有系数不全为零的表示互相推出，因此判断冗余只需看能否非平凡地组合出零向量。

3. 给出线性无关与线性相关的定义（式`eq:linear-algebra-independence-relation`），并用“谁也不能被其余向量凑出来”作直观说明。

4. 说明线性相关时取非零系数移项即得某个向量是其余向量的组合（如$\bm w=\bm u+\bm v$），反之亦然，故线性相关就是有向量多余、删去不改变张成空间。

5. 补充含零向量的组必相关、两个向量相关当且仅当共线；在$\mathbb R^m$中线性无关即$\bm V\bm a=\bm0$只有零解，上例矩阵有非零解$(1,1,-1)^\top$。

6. 示例`ex:ls-nearly-collinear-independence`说明近共线不能凭观感判断，先验证$\bm c_1,\bm q$线性无关，再得出$\varepsilon\neq0$时贯穿例两列线性无关、$\varepsilon=0$时相关。

7. 据此区分线性无关这一只答“是”或“否”的判断与两列接近程度的描述，后者要用夹角等度量另行刻画。

###### paragraph：表示的存在与唯一

1. 说明张成管表示是否存在、线性无关管表示是否唯一；示例`ex:ls-redundant-spanning-set`在$\mathbb R^2$中对照足够且无冗余、不够、足够但冗余（$\bm v_3=\bm v_1+\bm v_2$）三种方向组，图`fig:vol1-add-linear-redundant-directions`画出冗余情形下同一目标的两种表示。

2. 概括：张成保证表示存在，线性无关保证表示唯一，且由上一段唯一性反推线性无关，这是定义坐标的依据。

#### 2.2.2 基与维数

1. 定义同时张成且线性无关的向量组为基，说明它可充当整个空间的“尺子”。

2. 验证$\mathbb R^d$的标准基与$P_k$的基$1,t,\ldots,t^k$。

3. 示例`ex:ls-solution-plane-basis`以$x_2,x_3$为自由系数，求出方程$x_1+2x_2+3x_3=0$解平面的一组基$\bm n_1,\bm n_2$，并核对张成与无关。

###### paragraph：基的抽取与扩充

1. 定义有限维空间，并限定本章只讨论有限维情形。

2. 抽取：从有限生成组反复删去可由其余向量表示的成员，张成范围不变，最终得到基。

3. 扩充：从线性无关组逐次加入张成空间之外的向量，证明新组仍线性无关。

4. 说明扩充不会无限进行：借交换引理`thm:ls-exchange-lemma`（线性无关组不长于生成组）保证有限步内停止，停止时得到基。

5. 概括抽取压缩生成组、扩充补足无关组，并指出后面的证明常用扩充。

###### paragraph：维数

1. 说明用基的向量个数度量空间大小的前提是个数与基无关，给出交换引理`thm:ls-exchange-lemma`。

2. 证明交换引理：逐步把$\bm u_i$换入生成组、换出一个系数非零的$\bm v_j$而保持张成，若$r>s$则$\bm u_{s+1}$落入前$s$个$\bm u$的张成，矛盾。

3. 互换无关组与生成组的角色得任意两组基个数相同，定义维数$\dim V$，零空间维数为$0$。

4. 给出$\dim\mathbb R^d=d$、$\dim P_k=k+1$、解平面维数$2$、过原点直线维数$1$，并说明论证依赖有限生成组，不能直接用于无限维函数展开。

#### 2.2.3 子空间的维数与分解

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

#### 2.2.4 坐标与坐标变换

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

2. 解释两个大系数在几乎同向的基向量上大部分抵消，不能据此判断对象很大；用条件数定量讨论留给第~`chap:condition-and-spectral-perturbation`章，并引出建立换基一般公式的需要。

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

### 2.3 线性与多线性映射

1. 从单个空间的记录转向对象之间保持线性组合的作用，概述本节：矩阵表示及运算对应，核与像、秩零度与可逆判据，相抵与相似两种换基关系，最后简述多线性映射。

#### 2.3.1 线性映射及其矩阵表示

1. 以设计矩阵、求导、读取坐标三种作用的共同性质（先加权相加再作用与先作用再加权相加结果相同）引出线性映射的定义（式`eq:ls-linear-map-def`），说明这一性质使作用可以逐个基向量计算。

2. 由定义得$T\bm0=\bm0$，并指出乘矩阵都是线性映射；示例`ex:ls-linear-map-checks`验证平面映射$T$与求导$D$线性、平移$\tau(x)=x+1$不线性。

3. 定义线性算子并举例，说明算子的两点不同：输出可再作为输入，故可定义$T^k$；两端可用同一组基，决定其换基规律（第~`sec:ls-similarity`节）。

4. 过渡段（标签`sec:ls-map-representation`）：定义域有无穷多个元素，选定基后有限个数即可记录；概述映射与矩阵一一对应、运算对应运算，矩阵由此是线性映射在坐标下的记录。

##### 2.3.1.1 矩阵表示

1. 由线性性说明映射由基向量的像决定，以像的坐标为列定义$[T]_{\mathcal C\leftarrow\mathcal B}$，推出$[T\bm v]_{\mathcal C}=[T]_{\mathcal C\leftarrow\mathcal B}[\bm v]_{\mathcal B}$（式`eq:linear-algebra-map-matrix-representation`）。

2. 说明行列数分别是输出、输入维数，下标的读法，以及算子两端用同一组基的记号$[T]_{\mathcal B}$。

3. 示例`ex:ls-plane-operator-matrix`由基向量的像写出平面映射的矩阵；示例`ex:ls-derivative-matrix`写出$P_2$上求导$D$的矩阵并核对它作用于系数列的结果。

4. 由两个“先有映射再写矩阵”的例子转到反方向，证明对应定理`thm:ls-map-matrix-correspondence`（单射与满射两部分），并提醒对应依赖基的选取，变化规律留给第~`sec:ls-coordinates-change-of-basis`节。

5. 把$\bm X_\varepsilon$读成从两个系数到三个拟合值的映射记录，输入与输出不在同一空间；图`fig:ch06-object-coordinate-map`显示先作用再取坐标与先取坐标再乘矩阵结果相同。

##### 2.3.1.2 基于矩阵的映射运算

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

4. 提醒原输入只取末坐标为$1$的向量，不能据此说原映射线性；仿射解集的几何见第~`chap:linear-solution-selection`章。

##### 2.3.1.3 矩阵基本子空间

1. 对$\bm A$与$\bm A^\top$两个方向各问哪些输出可达、哪些输入被送到零。

2. 由列读法定义列空间，指出$\bm A\bm x=\bm b$有解当且仅当$\bm b\in\operatorname{range}(\bm A)$；定义零空间。

3. 对$\bm A^\top$定义行空间与左零空间，汇总为四个基本子空间（式`eq:ls-four-fundamental-subspaces`）。

4. 说明四个子空间所在的端，以及零空间、行空间、左零空间分别收集被消去的输入方向、读取输出分量的方向、对可达输出读数恒为零的加权方式。

5. 示例`ex:ls-rank-one-four-subspaces`对$\bm A=\left[\begin{smallmatrix}1&2&3\\2&4&6\end{smallmatrix}\right]$求出四个子空间，观察维数相同与互补的规律及逐项相乘再相加得零的现象；一般证明留给第~`sec:ls-kernel-image`节，垂直关系留给第~`sec:ls-orthogonality`节。

#### 2.3.2 核、像与秩

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

2. 证明行秩等于列秩（定理`thm:ls-row-rank-column-rank`）：先用列空间的基按列读出分解$\bm A=\bm C\bm R$，再按行读这个乘积，得到每行都是$\bm R$的$r$行的组合，从而行秩不超过列秩，对转置重复得等号。

3. 得到四个基本子空间的维数全由$m,d,r$决定（式`eq:ls-four-subspace-dimensions`）。

4. 回到示例`ex:ls-rank-one-four-subspaces`核对并写出$\bm A=\bm C\bm R$，指出垂直关系见第~`sec:ls-orthogonality`节，另一证明见第~`sec:ls-dual-map`节。

#### 2.3.3 单射、满射与可逆性

1. 把由输出唯一还原输入分成单射与满射两个条件。

2. 证明单射等价于核为零、满射等价于像为全空间，并用秩零度定理换成维数条件。

3. 说明维数相等时单射、满射、双射等价；维数不同时不可能满射或不可能单射，故只有等维映射才可能可逆。

4. 汇总方阵可逆、零空间为零、秩为$n$、列（行）线性无关的等价链，预告行列式判据（第~`sec:ls-determinant-invertibility`节）。

5. 据此不借行列式再证方阵单侧逆即逆（第~`sec:ls-square-one-sided-inverse`节），并证明方阵乘积可逆时两因子都可逆。

6. 示例`ex:ls-kernel-invertibility`用核判断对角矩阵与$\left[\begin{smallmatrix}2&1\\0&3\end{smallmatrix}\right]$的可逆性。

###### paragraph：单侧逆

1. 维数不同时构造单射的左逆（像上读回、补空间上任意规定）与满射的右逆（为输出基选原输入再延拓），说明它们一般不唯一。

2. 证明矩阵有左逆当且仅当满列秩、有右逆当且仅当满行秩，以$(1,0)^\top$有无穷多个左逆为例，代表的选择留给第~`chap:linear-solution-selection`章。

#### 2.3.4 换基、矩阵等价与相似

1. 类比坐标随基改变，说明映射的矩阵也随基改变，本小节写出这种变化并判断两个矩阵何时记录同一映射。

2. 说明先讨论两端各自换基的一般映射（相抵），再讨论两端同时换基的算子（相似）；约束减少自由度，相似需要更多不变量。

3. 观察换基矩阵就是恒等映射在两组基下的矩阵，连续换基公式即复合公式的特例。

##### 2.3.4.1 一般线性映射的换基与相抵

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

4. 证明相抵判据`thm:ls-equivalence-criterion`，说明秩是固定形状下相抵的完整不变量；化到标准形可用初等行变换配合初等列变换，数值消元算法留给第~`chap:direct-linear-solvers`章。

##### 2.3.4.2 线性算子的换基与相似

1. 说明算子两端必须换成同一组新基，本小节由此得到相似关系，讨论不变量与判定。

###### paragraph：换基过程

1. 在三步推导中取$\bm Q=\bm P$，得到$\bm B=\bm P^{-1}\bm A\bm P$（式`eq:linear-algebra-similarity-change-basis`），即式`eq:ls-equivalence-transform`的特例。

###### paragraph：相似的定义

1. 定义矩阵相似`def:ls-matrix-similarity`，证明相似矩阵正是同一算子在两组基下的记录。

2. 说明相似只要求换基矩阵可逆，相似必相抵而反之不然（预告示例`ex:ls-equivalent-not-similar`）。

3. 示例`ex:ls-similarity-diagonal`把$T(x_1,x_2)=(2x_1+x_2,3x_2)$换到基$(\bm e_1,\bm e_1+\bm e_2)$后化为$\operatorname{diag}(2,3)$；说明两个新基方向只被伸缩、不被转向；图`fig:ls-similarity-change-of-basis-flow`对比标准基下的斜切与新基下沿基方向的伸缩。

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

#### 2.3.5 多线性映射

1. 以元素内积、外积有两个输入且对每个输入分别线性引出槽位的概念。

2. 定义多线性映射与双线性映射，举例$\bm x\bm y^\top$。

3. 以$f(x,y)=xy$说明分别线性不等于整体线性。

4. 选定基后，双线性函数由基向量配对值$b_{i,j}$确定，写出$B(\bm x,\bm y)=\sum x_iy_jb_{i,j}$；换基改变系数而不改变映射，并说明右端正是系数表与两列坐标的张量积$[\bm x]\otimes[\bm y]$的Frobenius配对（第~`sec:ls-tensor-products`节），但重排存放次序不等于换基，换基改变的是系数表本身。

### 2.4 对偶空间

1. 以多项式取值、信号取样、加权和与坐标为例引出把对象读成一个数的作用，说明没有内积时需把读取规则本身当作研究对象。

2. 概述本节：全部线性读取组成对偶空间，坐标读取给出它的基；输出端读取传回输入端在坐标下是转置；读取的大小留给下一章。

#### 2.4.1 线性泛函与对偶基

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

#### 2.4.2 对偶映射

1. 由“先作用再读取”定义对偶映射$T'f=f\circ T$（式`eq:ls-dual-map-def`），证明它线性、方向与$T$相反且$(S\circ T)'=T'\circ S'$，强调它不是求逆。

###### paragraph：对偶映射的矩阵是转置

1. 在两组对偶基下计算$(T'f)(\bm b_j)$，证明对偶映射的矩阵是$\bm A^\top$，转置的乘积规则即复合反序的坐标记录。

2. 示例`ex:ls-dual-map-first-component`对$T(x_1,x_2)=(2x_1+x_2,3x_2)$核对两种算法，说明读取输出第$i$分量传回得到$\bm A$的第$i$行，$T'$的像在坐标下就是行空间。

###### paragraph：再证行秩等于列秩

1. 说明$\ker T'$由在像上读数恒为零的读取组成，在坐标下即左零空间。

2. 取像的基扩充为输出空间的基，用对偶基算出$\dim\ker T'=m-r$。

3. 对$T'$用秩零度定理得$\operatorname{rank}\bm A^\top=\operatorname{rank}\bm A$。

4. 指出读取的大小由第~`sec:ls-dual-norms`节的对偶范数回答，读取写成与固定向量的内积由第~`sec:ls-riesz-representation`节回答。

### 2.5 本章小结

1. 回应章首的区分：线性空间与子空间规定线性组合的范围，交、和、直和描述子空间的比较与唯一分解，商空间把相差子空间向量的对象视为相同。

2. 基保证坐标唯一，维数与基无关，扩充给出和、补空间与商空间的维数；换基改变坐标而不改变向量，接近退化的基会产生大坐标。

3. 线性映射选基后记成矩阵，运算对应运算；核、像与秩零度定理给出单射、满射与可逆的判据；相抵以秩完全分类，相似在秩、行列式与迹相同时仍可能不成立。

4. 对偶空间由线性泛函组成，对偶基是坐标读取，对偶映射在对偶基下是转置并再次给出行秩等于列秩。

5. 回到章首的问题，区分依赖基的记录（坐标、矩阵、读取系数按可逆矩阵换算）与对象或映射本身的性质（张成、线性无关、维数、核与像的维数、秩、相似矩阵的行列式与迹）。

6. 指出这些结构尚未规定大小与夹角，近共线基下大坐标的含义还无法定量回答，第~`chap:normed-inner-product-spaces`章引入范数与内积。

## 第3章 赋范空间与内积空间

正文入口：[03-normed-inner-product.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/03-normed-inner-product.tex)，章内依次输入[01-normed-spaces.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/03-normed-inner-product/01-normed-spaces.tex)、[02-inner-product-spaces.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/03-normed-inner-product/02-inner-product-spaces.tex)与[03-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/01-vectors-and-linear-spaces/03-normed-inner-product/03-summary.tex)。

1. 从上一章只有加法和数乘的局限进入：能判断线性表示是否存在、是否唯一，却无法回答两个向量相差多少、近似序列是否收敛、两个方向是否垂直。由此说明本章先用范数规定大小，再用内积规定角度。

2. 说明前两节只用范数：第~`sec:ls-normed-spaces`节给出范数公理与例子并显式比较坐标范数，说明误差数值依赖所选范数；第~`sec:multivariable-limits-continuity`节定义向量列、矩阵列的收敛与映射的联合极限、连续性，并证明闭有界集上的连续函数取到最值、一致连续。

3. 说明第~`sec:ls-finite-dimensional-normed-properties`节借最值定理证明有限维范数等价、完备性与绝对收敛级数收敛，再用矩阵范数、对偶范数与商范数度量映射、读取与等价类；指出第~`chap:linear-recurrence-stability`章的矩阵幂与Neumann级数、第~`chap:stationary-iterations`章的迭代与第~`chap:multivariate-differentiation`章的微分都使用这套分析基础。

4. 以一般范数没有角度、最近点可能不唯一承接内积：第~`sec:ls-inner-product-spaces`节建立长度、夹角、Cauchy--Schwarz不等式与Gram矩阵；第~`sec:ls-orthogonality-and-projection`节研究正交分解、标准正交基并证明正交投影是唯一最近点；第~`sec:ls-adjoints`节把线性泛函表示为内积，并把对偶映射改写成内积空间之间的伴随。

5. 交代依赖与范围：依赖前两章的线性运算、基与坐标，以及一元分析中的数列极限、确界与最值定理；只讨论有限维空间，收敛与连续性适用于一般映射；指出无限维函数空间中范数等价、完备性与最近点存在都可能失败，跨卷注明可参考卷四“函数空间”一章（`chap:functional-analysis-and-approximation`）。

### 3.1 范数与距离

1. 从多项式近似的误差与迭代近似的收敛进入，说明需要先规定向量的大小，并把第1章$\mathbb R^d$上的范数推广到一般线性空间。

2. 用两三句交代本节路线：先给范数公理与例子，再用显式不等式比较常用坐标范数；只用线性运算与标量不等式，收敛、范数等价与完备性在后两节。说明本章只讨论有限维空间。

#### 3.1.1 范数的定义与示例

本小节给出范数公理，检验$p$范数，举出其他空间上的范数与半范数。

###### paragraph：范数的定义

1. 从$\ell_1,\ell_2,\ell_\infty$范数的共同性质（非负、只有零向量为零、齐次、和的大小不超过大小之和）进入，说明它们只涉及线性运算，给出赋范空间定义`def:ls-normed-space`。

2. 说明范数诱导的距离满足度量空间对距离的四条要求且与平移、缩放相容，因而赋范空间是特殊的度量空间；一般度量空间跨卷注明可参考卷四“度量空间”一章（`chap:metric-spaces`）。

3. 把三角不等式用于$\bm x=(\bm x-\bm y)+\bm y$并交换角色，得到反向三角不等式（式`eq:ls-reverse-triangle`），解释为两向量的长度之差不超过差向量的长度，下一节用它说明范数随向量收敛。

###### paragraph：坐标范数的公理检验

1. 指出$p$范数的非负性、正定性与齐次性可直接读出，只需证明三角不等式；$p=1,\infty$逐坐标由实数三角不等式得到，$1<p<\infty$需要先建立Hölder不等式。

###### paragraph：Hölder不等式

1. 说明Hölder不等式用共轭指数$1/p+1/q=1$的两个范数控制逐坐标乘积之和，陈述定理`thm:linear-algebra-holder`。分三步证明$1<p<\infty$的情形：换元$t=v/u^{p-1}$求一元函数最小值得Young不等式，对归一化坐标求和，再恢复尺度；零向量与端点直接处理。

2. 指出$p=q=2$给出$|\bm x^\top\bm y|\leq\lVert\bm x\rVert_2\lVert\bm y\rVert_2$，对任一内积的同形不等式（Cauchy--Schwarz）在3.4.1只用公理证明。

###### paragraph：Minkowski不等式

1. 说明证明思路是把$|x_j+y_j|^p$拆成两个乘积之和再分别用Hölder不等式，陈述定理`thm:linear-algebra-minkowski`；证明先处理$p=1,\infty$，再利用配对向量$\bm s$的$q$范数恰为$\lVert\bm x+\bm y\rVert_p^{p-1}$约去公因子。

2. 结论：每个$p$范数都满足范数定义，特别是欧氏长度满足三角不等式。

###### paragraph：其他空间上的范数

1. 回指Frobenius范数是元素排成向量后的$2$范数、诱导矩阵范数在3.3.4验证。

2. 说明借坐标映射可在一般空间上定义范数，也可直接用对象性质定义；示例`ex:ls-polynomial-norms`在$P_k$上给出系数最大绝对值与一致范数$\max_{[0,1]}|p(t)|$，后者的正定性来自非零多项式根数有限。

3. 作为对照，去掉正定性得到半范数；示例`ex:ls-seminorm-first-coordinate`中$|x_1|$满足其余要求却把$(0,0)^\top$与$(0,1)^\top$判为距离零，提醒使用半范数须说明忽略了哪些差别。

#### 3.1.2 常用坐标范数的比较

1. 从误差估计常需在不同范数之间换算进入，陈述定理`thm:ls-coordinate-norm-comparison`：$1\leq p\leq q\leq\infty$时$\lVert\bm x\rVert_q\leq\lVert\bm x\rVert_p\leq d^{1/p-1/q}\lVert\bm x\rVert_q$。左侧对归一化向量逐项比较$|u_j|^q\leq|u_j|^p$；右侧$q=\infty$直接估计，$p<q<\infty$对$(|x_j|^p)$与全$1$向量用指数$q/p$的Hölder不等式。

2. 分行列出$\ell_\infty,\ell_2,\ell_1$之间的三组比较；示例`ex:ls-norm-comparison-check`在$(3,-4)^\top$上核对前两组，说明同一误差在三种范数下读出$4,5,7$。

3. 示例`ex:ls-l1-linf-constants`以$\bm e_1$与全$1$向量说明两侧取等、常数不能改进；指出常数随维数增长，不能当作对所有维数一致的界；任意有限维范数的等价定理`thm:ls-norm-equivalence`放在3.3.1。

### 3.2 收敛、极限与连续性

1. 说明本节用范数描述“接近”，许多结论可逐坐标归结为一元结果，列出所用的一元结论（数列极限运算法则、Bolzano--Weierstrass定理与最值定理、一致连续性、柯西收敛准则），跨卷注明可参考卷一“极限与连续”一章（`chap:limits-continuity`），并约定本章用到时只说明结论与条件。

2. 说明本节固定欧氏范数与Frobenius范数建立逐坐标判据、映射的极限与连续性及闭有界集上的基本结论；换用任意范数留到下一节，以免在范数等价的证明中循环使用结论；这些概念适用于一般映射。

#### 3.2.1 向量列与矩阵列的收敛

1. 回顾一元数列的误差趋零，定义`def:multivariable-sequence-convergence`：向量列按$\lVert\cdot\rVert_2$、同形矩阵列按$\lVert\cdot\rVert_{\mathrm F}$收敛；说明维数、形状固定，复向量与复矩阵拆成实部、虚部处理。

###### paragraph：逐坐标判据

1. 由$\max_j|x_{k,j}-x_j|\leq\lVert\bm x_k-\bm x\rVert_2\leq\sqrt d\max_j|x_{k,j}-x_j|$证明定理`thm:multivariable-coordinatewise-convergence`：收敛等价于逐坐标收敛，矩阵经向量化得逐元素判据。

2. 说明取$N=\max_jN_j$依赖坐标有限，换用范数或基的问题留到3.3.1。

###### paragraph：极限的唯一性与运算

1. 由三角不等式证明极限唯一、收敛列有界，由反向三角不等式得范数随之收敛。

2. 说明加法、数乘、内积与形状相容的矩阵乘法保持极限：结果的每个元素是有限个标量数列的和与积，由一元运算法则与逐坐标判据得到。

#### 3.2.2 开集、闭集与有界集

1. 说明讨论极限与连续前须先描述输入所在的集合：基点周围有无移动余地、是否包含边界点、是否伸向无穷远，分别由开集、闭集与有界集回答；矩阵空间按Frobenius范数同样定义。

###### paragraph：开球与开集

1. 定义开球$B(\bm a,r)$并在$d=1,2$时解释，定义含某个开球的集合为该点的邻域并说明“某点附近”的含义，给出定义`def:multivariable-open-closed-bounded`（开集、闭集为补集开、有界）。

2. 解释开集中每点向任何方向走一小步仍在集合内，这是后面在开集上求双侧差商的依据，半径随点而变。

3. 说明开与闭不对立：$\mathbb R^d$与空集既开又闭，半开带$\{0\leq x<1\}$既不开也不闭；有界性与中心选取无关。

###### paragraph：聚点、孤立点与边界点

1. 定义聚点（可以不属于$D$，是讨论极限的前提）与孤立点。

2. 定义边界点，以开圆盘的边界圆说明边界点可以是不属于集合的聚点。

###### paragraph：闭集的序列判据

1. 证明闭集的序列判据`lem:multivariable-closed-sequence`，与实轴上闭集的序列刻画对应，解释为闭集包含自己的全部边界点。

2. 示例`ex:multivariable-open-closed-sets`：开圆盘开而不闭、边界点是聚点，闭圆盘与$\{\lVert\bm X-\bm I_2\rVert_{\mathrm F}\leq1/2\}$闭且有界，说明可以在不属于定义域的边界点处讨论极限。

3. 定义闭包$\overline K$为$K$中序列全部可能极限组成的集合，说明它是$K$与全部聚点的并；用“逐项取近似点”与序列判据证明闭包是闭集，再由任何含$K$的闭集都含这些极限得出闭包是包含$K$的最小闭集、$K$闭当且仅当$\overline K=K$，以开圆盘的闭包是闭圆盘为例。

4. 用一句比较邻域、边界点与闭包分别描述的对象：一点周围、同时贴近集合与补集的点、补齐边界后的集合。

#### 3.2.3 映射的联合极限

1. 说明本小节与下一小节研究$F:D\subseteq V\to W$，$V,W$取欧氏或Frobenius范数的坐标空间；标量输出、向量值映射与矩阵的函数都是特例，例子多取标量输出。

###### paragraph：多元标量函数

1. 用曲面图像说明多元标量函数，给出定义`def:multivariable-scalar-function`。

2. 以$x^2+xy+y^2$为例介绍切片和等值曲线两种观察方法，指出切片只看一条直线，由此转向在整个空间中趋近基点时函数值的变化。

##### 3.2.3.1 极限的定义

1. 说明一元只能从两侧靠近，平面中可沿直线、抛物线、螺旋线趋近，定义须用一个只依赖距离的条件控制全部输入。

2. 把一元的去心区间换成去心球，要求基点为聚点，输出误差用输出空间的范数度量，给出映射的极限定义`def:multivariable-limit`。

3. 解释$\delta$只依赖$\varepsilon$、不依赖方向，任何趋近方式都由同一个$\delta$覆盖；称之为联合极限，以区别于沿路径或逐个坐标的极限。

##### 3.2.3.2 极限的判据

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

#### 3.2.4 连续性

##### 3.2.4.1 连续性的定义

1. 由联合极限引出连续，给出映射连续性定义`def:multivariable-scalar-continuity`（条件允许$\bm x=\bm a$），说明聚点与孤立点情形、几何含义、连续等价于各输出分量连续，并指出连续函数的坐标切片连续而逆向不成立。

##### 3.2.4.2 连续性的性质

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

###### paragraph：逆映射

1. 由古典伴随公式`thm:ls-adjugate-identity`写出$\bm X^{-1}=\operatorname{adj}(\bm X)/\det\bm X$，分子各元素与分母都是多项式，分母在可逆矩阵集合上非零，故求逆在可逆矩阵上连续。

2. 说明这里只建立连续性，逆矩阵差的精确误差界与求逆的微分分别在第12、13章讨论。

##### 3.2.4.3 一致连续与Lipschitz连续

1. 给出定义`def:ls-lipschitz`：一致连续（$\delta$不依赖基点）、Lipschitz连续与局部Lipschitz连续。

2. 说明Lipschitz蕴含一致连续，以$\sqrt x$在$[0,1]$上一致连续却在零点没有Lipschitz常数作区分；范数由反向三角不等式是常数为$1$的例子；导数求常数留到第~`chap:multivariate-differentiation`章。

#### 3.2.5 闭有界集上的连续函数

1. 从“求最小点须先保证最小值存在”进入，回顾一元极值定理依赖子列性质，说明本小节先推广子列性质，再得极值定理与一致连续性；矩阵空间经向量化结论相同。

###### paragraph：有限维闭有界集的收敛子列

1. 说明逐坐标使用Bolzano--Weierstrass定理，有界性给出收敛子列，闭性保证极限在集合内；给出定理`thm:multivariable-bolzano-weierstrass`及逐坐标抽取子列的证明，极限由逐坐标判据与闭集序列判据得到。

2. 指出有限维闭有界集具有与闭区间相同的子列性质，一般度量空间中紧致与序列紧致的关系属于度量空间的一般理论，不展开。

###### paragraph：有界性与极值达到

1. 说明趋近确界的序列可能跑向无穷远或趋向集合外的边界点，闭有界性同时排除二者；给出闭有界集上的极值定理`thm:multivariable-extreme-value`，说明一元最值定理的证明只用子列性质与连续性，故逐字适用，并写出最大值情形的关键步骤。

2. 示例`ex:multivariable-extreme-value-failures`：开圆盘、整个平面和边界不连续的闭圆盘，分别说明删去闭性、有界性或连续性时最值可能取不到。

3. 指出单位球面是闭有界集，下一节在其上比较范数。

###### paragraph：一致连续性

1. 回用定义`def:ls-lipschitz`，对照一元闭区间上连续函数一致连续的结论，陈述并反证定理`thm:multivariable-uniform-continuity`：构造距离趋零而输出差保持$\varepsilon_0$的两列点，取收敛子列得同一极限，与连续性矛盾。

2. 说明第~`chap:region-integrals`章的Riemann和、参数积分与换元需要在整个区域上统一控制误差。

### 3.3 有限维赋范空间的性质

说明本节研究范数与有限维线性结构结合后的分析性质：先证明范数等价与完备性，使向量与矩阵级数有统一依据；再以算子范数度量线性映射、以对偶范数度量线性泛函；最后建立商范数与一般范数下最近点的存在；每一步回用上一节的收敛与连续性。

#### 3.3.1 有限维范数等价

1. 从上一节固定欧氏与Frobenius范数、而误差分析常用$\ell_1$、$\ell_\infty$与诱导范数进入，提出换用范数是否改变收敛与连续性。

2. 陈述定理`thm:ls-norm-equivalence`；零维单独处理，固定基后以坐标欧氏长度$\lVert\cdot\rVert_c$为参照，由三角不等式、齐次性与Hölder不等式得上界$C_p$，由反向三角不等式得$p$关于坐标连续。

3. 下界：在坐标单位球面上由极值定理`thm:multivariable-extreme-value`取到最小值（锚点`thm:ls-extreme-value`），由正定性知其为正，合成式`eq:linear-algebra-finite-norm-equivalence`后比较两个范数。

4. 回指示例`ex:ls-l1-linf-constants`说明常数不能改进，指出真正依赖有限维的是下界。

###### paragraph：收敛与连续性不依赖范数

1. 说明换用范数只把误差乘以有界正因子，收敛、极限、映射的极限与连续性（两端范数可分别更换）以及开集、闭集与有界集都与范数无关。

2. 换基后坐标的欧氏长度也是范数，故逐坐标判据与基无关；矩阵序列在任意矩阵范数下收敛等价于逐元素收敛；子列抽取与极值定理可在任何范数下使用。

3. 提醒数值误差与比较常数仍依赖范数与维数，范数等价不给出衰减速度。

#### 3.3.2 完备性

1. 从迭代与级数截断只给出彼此接近的近似、事先不知极限进入，说明一元分析用柯西条件处理这一问题，本小节推广到赋范空间。

###### paragraph：Cauchy列与完备性

1. 定义柯西列，说明收敛序列都是柯西列，有限维中柯西性与范数无关，柯西列是否收敛取决于空间中有无极限；定义完备与Banach空间，指出实数的完备性就是实数列的柯西收敛准则。

2. 陈述定理`thm:ls-finite-dimensional-complete`：借式`eq:linear-algebra-finite-norm-equivalence`把柯西列化为各坐标的实柯西数列，由实数完备性逐坐标构造极限；子空间与矩阵空间同样完备。

3. 指出证明依赖坐标有限、无限维空间是否完备取决于空间与范数，属于章首提到的无限维理论；说明完备性使下一小节的级数、第~`chap:linear-recurrence-stability`章的矩阵幂与第~`chap:stationary-iterations`章的迭代只需证明柯西性即可断定极限存在。

###### paragraph：子空间的闭性

1. 从“点与子空间任意接近能否推出属于子空间”进入，陈述并证明定理`thm:ls-subspace-closed`：扩充基后补充方向的坐标恒为零，逐坐标收敛保持为零。

2. 与完备性相互印证；定义点到子空间的距离$d(\bm x,U)$，取距离趋零的子空间序列并由闭性得$d(\bm x,U)=0$当且仅当$\bm x\in U$，供商范数使用。

#### 3.3.3 向量与矩阵级数的收敛

1. 从矩阵幂之和与逐步累积的误差进入，回顾一元分析用部分和的极限定义实数级数的和。

###### paragraph：部分和与收敛

1. 用部分和在固定有限维空间中的收敛定义向量、矩阵级数的收敛；由逐坐标判据，收敛等价于各坐标级数收敛；由$u_N=S_N-S_{N-1}$说明通项趋零。

###### paragraph：绝对收敛

1. 用$\sum_k\lVert u_k\rVert<\infty$定义绝对收敛，由范数等价说明它与范数无关。

2. 陈述并证明定理`thm:ls-absolute-series-convergence`：三角不等式把部分和之差控制为标量尾和，得柯西列，由完备性收敛，令$M\to\infty$得尾和估计$\lVert S-S_N\rVert\leq\sum_{k>N}\lVert u_k\rVert$；说明完备性使人不必先知道和。

3. 示例`ex:ls-matrix-geometric-series`对$\left[\begin{smallmatrix}1/2&1\\0&1/2\end{smallmatrix}\right]$写出$\bm A^k$，逐元素与按Frobenius范数绝对收敛，和为$\left[\begin{smallmatrix}2&4\\0&2\end{smallmatrix}\right]=(\bm I-\bm A)^{-1}$，预告第~`chap:linear-recurrence-stability`章对一般方阵说明的Neumann级数（第~`sec:ls-matrix-series-exponential`节）。

###### paragraph：级数的运算

1. 说明收敛级数可逐项相加、数乘，固定矩阵可移入求和号（部分和关系加矩阵乘积保持极限），并指出下一小节可把它看作线性映射连续性的推论；一般级数乘积与重排不需要。

#### 3.3.4 矩阵范数

1. 对照第1章衡量元素总体大小的Frobenius范数，引出把矩阵看作映射、问最大放大倍数的口径。

###### paragraph：诱导矩阵范数

1. 对任意输入、输出范数定义诱导矩阵范数`def:matrix-analysis-induced-norm`为单位球上的上确界，由齐次性说明它等于非零输入比值的上确界，零空间上取零；预告下面先证明它有限。

##### 3.3.4.1 线性作用的连续性

1. 陈述并证明定理`thm:ls-linear-map-continuity`：按列展开并用范数等价得诱导范数有限且$\lVert\bm A\bm x\rVert_\beta\leq\lVert\bm A\rVert_{\alpha\to\beta}\lVert\bm x\rVert_\alpha$；用于$\bm x-\bm y$得Lipschitz连续；单位球闭且有界，由极值定理`thm:multivariable-extreme-value`得上确界可达。

2. 解释三条结论：诱导范数是放大界中最小的常数，按`def:ls-lipschitz`读作误差放大上界，$\sup$可写成$\max$。

###### paragraph：线性映射的算子范数

1. 对有限维线性映射定义算子范数，把$V,W$的范数搬到坐标空间后它等于表示矩阵的诱导范数，由定理得有限、可达，有限维线性映射都Lipschitz连续；说明换基保持原范数时数值不变，在坐标上另指定范数则改变计量规则。

##### 3.3.4.2 常用的诱导范数

1. 写出最大绝对列和、最大绝对行和两个公式（推导在3.3.4.3），说明谱范数是欧氏诱导范数、等于最大奇异值（第~`chap:singular-value-decomposition`章）。

2. 示例`ex:ls-matrix-norms-shear`在$\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$上算出$\lVert\bm A\rVert_1=\lVert\bm A\rVert_\infty=2$、$\lVert\bm A\rVert_{\mathrm F}=\sqrt3$；图`fig:ls-induced-norm-action`把单位圆像的最长半轴读作谱范数。

##### 3.3.4.3 矩阵范数的性质

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

#### 3.3.5 对偶范数

1. 从线性泛函是对向量的读取、误差只知落在范数球内时一次读取$\bm z^\top\bm r$最多变化多少进入，定义对偶范数`def:linear-algebra-dual-norm`（式`eq:linear-algebra-dual-norm-definition`）。

2. 指出它是输出取$\mathbb R$时的诱导范数，所以上确界有限并可取到。

3. 逐条验证对偶范数满足范数要求：正定性（取$\bm e_j/\lVert\bm e_j\rVert$）、三角不等式与齐次性；图`fig:ls-dual-norm-unit-ball`把最大值画成支撑线最后接触单位球的位置。

4. 对$\ell_p$由Hölder不等式得上界并逐类构造达到上界的$\bm r$，得到单行写出的式`eq:linear-algebra-lp-duality`与按预算缩放的式`eq:linear-algebra-linear-perturbation-duality`。

5. 示例`ex:ls-dual-norm-three-budgets`对$\bm z=(2,-1)^\top$算出$\ell_1,\ell_2,\ell_\infty$单位球上的最大值$2,\sqrt5,3$及预算$0.01$下的$0.03$；图`fig:linear-algebra-dual-unit-balls`画出最坏方向。

6. 归纳：$\ell_\infty$预算对应$\ell_1$计量、$\ell_2$对应$\ell_2$。

6. 示例`ex:ls-weighted-dual-norm`对加权$\ell_1$范数$\sum_jw_j|r_j|$换元$s_j=w_jr_j$化回$\ell_1$情形，得$\lVert\bm z\rVert_*=\max_j|z_j|/w_j$；以$\bm z=(2,-1)^\top$在权重$(1,1)$与$(4,1)$下分别得$2$与$1$，说明读取的代数表达不变而大小随原范数改变。

7. 结论：讨论误差放大必须先说明所用范数；内积范数下的对偶范数在3.6.1由表示向量得到；一般有限维空间上的$\lVert\varphi\rVert_*$即取$W=\mathbb R$的算子范数，无限维代数对偶与连续对偶之别留给函数空间章。

#### 3.3.6 商范数

1. 承接子空间闭性，回指商空间只有线性结构；说明类中各点到$U$的距离不依赖代表元，据此定义商范数$\lVert\bm x+U\rVert_{V/U}=d(\bm x,U)$。

2. 验证三角不等式（取任意接近两侧下确界的代表元）与齐次性，正定性由$d(\bm x,U)=0\iff\bm x\in U$得到；指出子空间不闭的更一般空间中公式可能只给出半范数。

###### paragraph：一般范数下的最近点

1. 陈述定理`thm:multivariable-nearest-point-existence`：取距离逼近下确界的子空间点列，由$\lVert\bm u_k\rVert\leq\lVert\bm x\rVert+\lVert\bm x-\bm u_k\rVert$知有界，取收敛子列，由子空间闭性与范数连续性得最近点存在。

2. 示例`ex:ls-linf-nonunique-nearest`算出$\ell_\infty$范数下$(0,1)^\top$到横轴的距离为$1$，全部$(t,0)^\top$、$|t|\leq1$都是最近点；说明存在性不保证唯一性，3.5.4加入内积后证明正交投影给出唯一最近点。

### 3.4 内积空间

1. 从范数没有角度、最近点可能不唯一进入，说明本节提取欧氏内积的共同规则，在一般线性空间上定义内积。

2. 交代本节先由公理推出长度、夹角与基本不等式，再用Gram矩阵记录两两内积；正交投影与伴随留给后两节。

#### 3.4.1 内积与内积诱导的范数

本小节先给出内积公理与例子，再由内积定义长度、正交与夹角，最后从三角不等式出发说明内积诱导的长度是范数并给出距离；平行四边形恒等式说明并非每个范数都来自内积。

##### 3.4.1.1 内积的定义

1. 从欧氏内积的双线性、对称性与正定性只涉及线性运算进入，给出内积空间定义`def:functional-inner-product-space`。

###### paragraph：内积的例子

1. 逐条检验欧氏内积满足三条公理。

2. 说明Frobenius内积就是把元素看作坐标的欧氏内积，因而一般结论对它同样成立。

3. 示例`ex:ls-two-point-inner-product`在$P_1$上规定只看两点取值的内积并验证公理，以$\langle1,t\rangle=1$而系数向量欧氏内积为零说明它与系数内积不同；后面的算例反复使用它。

###### paragraph：复内积的约定

1. 说明复空间中两个变量都线性会破坏正定性，因而采用第一变量共轭线性、第二变量线性与共轭对称的约定，标准例子为$\bm x^*\bm y$。

2. 说明后面的Cauchy--Schwarz不等式与诱导范数在复内积下同样成立，但下一小节的余弦公式不能照搬；下文证明继续使用实内积。

##### 3.4.1.2 由内积定义的夹角

###### paragraph：长度与正交

1. 由内积定义长度（是否为范数留到下一小节检验）与正交，展开$\lVert\bm x+\bm y\rVert^2$消去交叉项得勾股定理。

###### paragraph：Cauchy--Schwarz不等式

1. 为了反过来用$\langle\bm x,\bm y\rangle=\lVert\bm x\rVert\lVert\bm y\rVert\cos\theta$定义夹角，需要比值落在$[-1,1]$中；陈述定理`thm:linear-algebra-cauchy-schwarz`（式`eq:prelim-cauchy-schwarz`），由$\lVert\bm x-s\bm y\rVert^2\geq0$的二次函数在顶点处的最小值得出不等式与等号条件。

2. 指出证明只用公理，标准内积下即$p=q=2$的Hölder不等式，对Frobenius内积同样成立。

###### paragraph：夹角

1. 定义夹角并写成两个单位向量的内积，说明夹角只比较方向、正交对应直角、共线对应$\cos\theta=\pm1$，且分子分母须来自同一内积。

2. 示例`ex:ls-nearly-collinear-angle`对贯穿例两列算得式`eq:linear-algebra-nearly-collinear-angle`（$\varepsilon=0.1$时约$4.7^\circ$）。

3. 据此定义近共线，说明“近”指作为$\mathbb R^3$中向量的夹角小，且夹角依赖所用内积。

##### 3.4.1.3 由内积定义的距离

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

1. 由内积诱导范数与3.3.2的有限维完备性引出Hilbert空间的名称，说明有限维内积空间都是Hilbert空间。

2. 指出后面的正交分解与投影由有限维代数构造得到，不依赖完备性；无限维中完备性与子空间闭性需另行检查，无限正交级数、闭子空间投影与连续泛函的表示属于章首提到的无限维理论。

#### 3.4.2 Gram矩阵

1. 交代本小节先引入正定与半正定矩阵并定义加权内积，再定义Gram矩阵，说明Gram矩阵恰为全部半正定矩阵、可读出线性无关与正交；借这一刻画证明逐元素乘积保持半正定，最后写出坐标下的内积。

##### 3.4.2.1 正定与半正定

1. 定义对称矩阵的二次型，定义正定、半正定以及$\bm M\succeq\bm N$，强调比较的是二次型而非元素。

2. 示例`ex:ls-pd-psd-completing-square`用配方区分正定的$\left[\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\right]$与仅半正定的$\left[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right]$。

3. 说明对角矩阵正定当且仅当对角元全为正；反例`ex:ls-positive-entries-not-pd`说明元素全为正的对称矩阵可以不定。

###### paragraph：加权内积

1. 说明正定矩阵可在$\mathbb R^d$上定义标准内积以外的内积，给出加权内积与距离（式`eq:linear-algebra-mahalanobis-pseudodistance`），逐条核对公理并指出协方差逆给出Mahalanobis距离。

2. 示例`ex:ls-weighted-length`以$\operatorname{diag}(4,1)$下$(1,1)^\top$的加权长度$\sqrt5$与欧氏长度$\sqrt2$对照，并预告本小节最后说明任一内积选基后都是这种形式。

##### 3.4.2.2 Gram矩阵的定义

1. 从一组向量有$r^2$个内积值、需要一次记录进入，定义Gram矩阵`def:linear-algebra-gram-matrix`及其在欧氏、加权内积下的矩阵形式，说明对称性。

2. 说明正交性写在非对角元里：对角对应两两正交，单位矩阵对应标准正交。图`fig:ls-gram-matrix-coefficients`把两个向量的内积排成数表。

##### 3.4.2.3 Gram矩阵与半正定矩阵

###### paragraph：Gram矩阵的半正定性

1. 由二次型等于线性组合的长度平方，说明Gram矩阵半正定，且正定当且仅当向量线性无关；正定时可逆。

2. 示例`ex:ls-nearly-collinear-gram`说明贯穿例两列的Gram矩阵正定，但系数$(1,-1)^\top$使二次型只有$2\varepsilon^2$，即“正定但几乎退化”。

###### paragraph：Gram因子定理

1. 提出反问题：每个半正定矩阵是否都是Gram矩阵；关键是写成欧氏平方和。对阶数归纳证明定理`thm:ls-gram-factor`：对角元全为零时推出$\bm M=\bm0$，否则置换出正对角元、对第一个变量配方，余项仍半正定，用分块上三角因子拼回；正定时写出该因子的分块逆。

2. 示例`ex:ls-gram-factor-two-by-two`按证明步骤得$\bm L=\left[\begin{smallmatrix}2&1\\0&1\end{smallmatrix}\right]$；说明加权长度即$\lVert\bm L\bm x\rVert_2$，配方即Cholesky分解的雏形。

###### paragraph：半正定矩阵是Gram矩阵

1. 由因子定理回答反问题：半正定矩阵就是$\bm L$各列的Gram矩阵，两者说的是同一件事。

##### 3.4.2.4 Gram矩阵的逐元素乘法

1. 说明“半正定矩阵就是Gram矩阵”可用来判断逐元素乘积是否保持半正定：只需找到一组向量，其两两内积恰为两个Gram矩阵对应元素之积；引出Schur乘积定理。

2. 陈述定理`thm:ls-schur-product`：两个对称半正定矩阵的逐元素乘积仍对称半正定。证明由定理`thm:ls-gram-factor`把两者写成$\bm u_i$、$\bm v_i$的Gram矩阵，借张量积在Frobenius内积下配对的分离性（`sec:ls-tensor-product-properties`），把逐元素乘积写成$\bm u_i\otimes\bm v_i$的Gram矩阵。

3. 示例`ex:ls-schur-product`用配方核对二阶例子，并指出该定理是核矩阵逐元素乘积仍合法的依据。

##### 3.4.2.5 基的Gram矩阵与内积

1. 选定基后按双线性展开得$\langle\bm v,\bm w\rangle=[\bm v]^\top\bm G[\bm w]$，并由基线性无关与上一小节得$\bm G$对称正定。

2. 说明在坐标下任一内积都是以基的Gram矩阵为权重的加权内积，反过来每个对称正定矩阵给出一个加权内积，故$\mathbb R^d$上的内积与对称正定矩阵一一对应。

3. 示例`ex:ls-two-point-inner-product-coordinates`在两点内积与基$(1,t)$下按定义与按坐标算得同一内积值$-1$，并指出标准正交基使$\bm G=\bm I$。

###### paragraph：合同变换

1. 说明换基$\bm x=\bm C\widetilde{\bm x}$时两个坐标都改变，Gram矩阵按合同变换$\bm C^\top\bm G\bm C$变化，它保持同一个内积与二次型，与记录算子换基的相似变换用途不同。

##### 3.4.2.6 复空间中的Gram矩阵

1. 沿用复内积第一变量共轭线性的约定，定义$G_{i,j}=\langle\bm b_i,\bm b_j\rangle$，说明本小节比较与实情形的异同。

###### paragraph：自共轭代替对称

1. 由交换变量取共轭得$\bm G^*=\bm G$，定义自共轭矩阵（与3.6.2的自伴矩阵相同），说明对角元为实数、非对角元一般为复数、$\bm G$一般不对称，实Gram矩阵是其特例。

###### paragraph：半正定性照样成立

1. 由$\bm c^*\bm G\bm c=\lVert\sum_jc_j\bm b_j\rVert^2\geq0$说明复Gram矩阵半正定，指出自共轭矩阵的二次型总是实数。

###### paragraph：正定与线性无关的关系照样成立

1. 由同一等式得正定当且仅当向量组在复数域上线性无关；以$\mathbb C$中的$1,\mathrm i$（实系数无关、复系数相关，Gram矩阵行列式为零）说明系数域的作用。

2. 说明逐步配方证明照样成立，得$\bm G=\bm L^*\bm L$，每个半正定自共轭矩阵都是Gram矩阵，不借用谱定理。

###### paragraph：坐标下的内积与换基

1. 说明复内积在坐标下为$\bm x^*\bm G\bm y$，换基时Gram矩阵变为$\bm C^*\bm G\bm C$。

2. 示例`ex:ls-complex-gram`对$(1,\mathrm i)^\top$与$(1,1)^\top$算出$\bm G=\left[\begin{smallmatrix}2&1-\mathrm i\\1+\mathrm i&2\end{smallmatrix}\right]$，不对称但自共轭；由两向量在复数域上线性无关（比较坐标得$c=1$与$c=\mathrm i$矛盾）推出$\bm G$正定，并以$\bm c=(1,-1)^\top$核对$\bm c^*\bm G\bm c=\lVert\bm b_1-\bm b_2\rVert^2=2>0$。

### 3.5 正交与投影

1. 说明本节把正交从两个向量推广到向量与子空间，给出正交分解；再引入标准正交基并用Gram--Schmidt正交化构造它，最后写出正交投影并证明它是唯一最近点。

#### 3.5.1 正交补与正交分解

1. 交代本小节由向量与整个子空间的正交得到唯一确定的补空间，并证明四个基本子空间的垂直关系。

###### paragraph：正交补

1. 从补空间一般不唯一进入，定义正交补$U^\perp$，由双线性说明它是子空间，并指出只需检查与$U$的一组基逐个正交。

###### paragraph：正交直和

1. 借正定可逆的Gram矩阵解出分量系数，证明正交直和引理`lem:ls-orthogonal-decomposition`与分解唯一，得$\dim U^\perp=\dim V-\dim U$。

2. 示例`ex:ls-orthogonal-decomposition-line`把$\bm y=(1,1.1,0.9)^\top$分解为$\bm c_1$与余量$(0,0.1,-0.1)^\top$；最近点性质留到3.5.4。

3. 由包含且同维证明$(U^\perp)^\perp=U$。

###### paragraph：四个基本子空间的正交关系

1. 由$\langle\bm A\bm x,\bm y\rangle=\langle\bm x,\bm A^\top\bm y\rangle$证明定理`thm:ls-four-subspaces-orthogonality`（式`eq:ls-four-subspaces-orthogonality`、`eq:ls-four-subspaces-decomposition`）。

2. 再取正交补得另两式，解释输入端分成被消去的零空间与影响输出的行空间，输出端分成可达的列空间与不可达的左零空间。

3. 与秩零度定理比较再得行秩等于列秩，回扣第2章四个子空间的算例；指出由此得到的有解判据（$\bm b$与左零空间正交）供第~`chap:linear-solution-selection`章使用。

#### 3.5.2 标准正交基

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

1. 说明转置条件只给出左逆，借方阵的单侧逆即逆（第~`sec:ls-square-one-sided-inverse`节用行列式、第~`sec:ls-injective-surjective-invertible`节用核为零各给过证明）得$\bm Q^{-1}=\bm Q^\top$与$\bm Q\bm Q^\top=\bm I_n$，从而各行也标准正交，且$\bm Q^{-1}$仍正交。

###### paragraph：正交矩阵的行列式

1. 由$\det(\bm Q^\top\bm Q)=1$与转置不变得$\det\bm Q=\pm1$，以旋转与交换坐标分别说明保定向与反定向。

###### paragraph：标准正交基之间的换基

1. 证明两组标准正交基之间的换基矩阵满足$\bm S^\top\bm S=\bm I$，反向换基只需转置，不会出现除以小数$\varepsilon$的放大。

2. 说明对算子相似关系变为$\bm B=\bm P^\top\bm A\bm P$，谱定理在这种受限换基下化简对称矩阵。

###### paragraph：正交不变性

1. 由正交矩阵保持欧氏长度，得到$\lVert\bm Q\rVert_2=1$，左乘正交矩阵不改变Frobenius范数与谱范数。

#### 3.5.3 Gram--Schmidt正交化

1. 说明本小节把任意线性无关组改造成标准正交组：思路来自正交分解，依次扣除已得方向上的分量再归一化；随后写成QR分解，并处理列相关的情形。

##### 3.5.3.1 Gram--Schmidt正交化

1. 写出Gram--Schmidt正交化的递推（式`eq:ls-gram-schmidt`），说明$\bm u_j$是正交分解中的剩余分量。

2. 对$j$归纳证明定理`thm:ls-gram-schmidt`：$\bm u_j$与前面方向正交，$\bm u_j\neq\bm0$由线性无关保证，前$j$个新旧方向张成同一子空间。

3. 推出每个有限维内积空间都有标准正交基，任何标准正交组都能扩充为标准正交基；说明张成空间逐段相等意味着正交化只在每一段内部换基。

###### paragraph：算例

1. 指出两点内积下$\langle1,t\rangle=1\neq0$；示例`ex:ls-gram-schmidt-two-point`对基$(1,t)$逐步正交化：归一化得$q_1=1/\sqrt2$，扣除分量得$t-\tfrac12$（扣除的是两点取值的平均），再归一化得$q_2=\sqrt2(t-\tfrac12)$；随后核对正交与单位长度，读出$1+t$的坐标并验证Parseval恒等式。

2. 与系数欧氏内积下$1,t$本已正交对照，说明标准正交基依赖内积。

##### 3.5.3.2 QR分解

1. 在$\mathbb R^m$中把正交化反写为$\bm a_j=\sum_{i\leq j}r_{i,j}\bm q_i$，合写为经济型QR分解（式`eq:ls-qr-factorization`），说明$\bm Q$的列是列空间的标准正交基、$\bm R$上三角且可逆。

2. 图`fig:vol1-add-linear-qr-columns`给出二维情形；说明列空间计算可改在$\bm Q$上进行，第~`chap:linear-solution-selection`章与第~`chap:direct-linear-solvers`章解方程与最小二乘时使用。

##### 3.5.3.3 列相关时的处理

1. 说明出现$\bm u_j=\bm0$恰表示该列没有新方向，应跳过并只在$\bm R$中记下系数；处理完后$\bm Q$的列数等于秩，$\bm R$为$r\times d$阶梯形。

2. 示例`ex:ls-qr-dependent-columns`以共线两列$(1,0)^\top,(2,0)^\top$演示；指出有限精度下怎样判断余量为零、怎样减少正交性损失留到数值敏感性一节（`sec:ls-numerical-sensitivity`）。

#### 3.5.4 正交投影

1. 说明本小节把标准正交基下逐个读出的分量合成正交投影，证明它是最近点，再写成矩阵并给出判别方法。

###### paragraph：向子空间的正交分解

1. 在子空间的标准正交基下Gram方程直接给出系数，写出正交投影（式`eq:ls-orthonormal-projection`），由勾股定理得部分系数平方和不超过总长度平方、等号恰在$\bm x\in U$时成立。

2. 把$\bm x-\bm v$拆成$U^\perp$与$U$中两部分，由勾股定理证明投影是唯一最近点；说明非标准正交基可先解Gram方程。

3. 指出唯一性来自内积：回用3.3.6中一般范数下最近点存在的结论与示例`ex:ls-linf-nonunique-nearest`的非唯一最近点，与欧氏范数下只有原点对照。

4. 示例`ex:ls-orthonormal-projection-line`不解Gram方程重算前面的正交分解。

###### paragraph：投影矩阵

1. 由正交分解的唯一性说明投影随原向量线性变化，因而是线性映射。

2. 在欧氏内积下写出$\bm P_U=\bm Q\bm Q^\top$（式`eq:linear-algebra-orthogonal-projector`），验证幂等与对称并解释其含义，指出像为$U$、$\bm Q$非方阵时$\bm P_U$不是单位矩阵。

###### paragraph：正交投影、斜投影与幂等

1. 提出怎样判断一个矩阵是否为正交投影；说明一般幂等矩阵把向量分成像与零空间中的两部分，但两部分不必正交，称为斜投影。

2. 示例`ex:ls-oblique-projection`以$\left[\begin{smallmatrix}1&-1\\0&0\end{smallmatrix}\right]$说明幂等而不对称的投影不给出最近点。

3. 证明幂等且对称时残差与像正交，由正交分解的唯一性得到正交投影；归纳为“先验幂等、再验对称”两步。

### 3.6 线性泛函的内积表示与伴随

1. 从对偶空间中的读取与被读取向量不在同一空间进入，说明有了内积，读取可写成与固定向量的内积，对偶映射随之成为伴随；回指四个基本子空间的证明已用到伴随在欧氏内积下的形式。

#### 3.6.1 线性泛函的内积表示

1. 从欧氏内积下读取即与系数向量的内积进入，借标准正交基构造表示向量并证明唯一，得到有限维Riesz表示定理`thm:ls-riesz-representation`。

2. 说明表示对应是$V^*$到$V$的线性双射，标准正交基的对偶基就是自身，图`fig:ls-dual-basis-readout`中的红色箭头即对偶读取的表示向量。

3. 说明表示向量依赖内积而读取本身不依赖：加权内积下为$\bm M^{-1}\bm a$；示例`ex:ls-riesz-integral-two-point`中积分读取在两点内积下对应常数$\tfrac12$（梯形公式对一次函数精确）。

4. 由Cauchy--Schwarz不等式证明单位球上读取的最大值$\lVert\varphi\rVert_*=\lVert\bm v_\varphi\rVert$，欧氏内积下即$\ell_2$范数自对偶。

#### 3.6.2 伴随与特殊线性算子

1. 从对偶映射把读取$f$传回为$f\circ T$、再把读取换成表示向量进入，给出伴随定义`def:linear-algebra-adjoint`（式`eq:ls-adjoint-pairing`）。

2. 由Riesz表示定理证明伴随存在、唯一且线性；用对偶映射的语言说明伴随就是借内积把读取换成向量后的对偶映射。

3. 在两端的基下用Gram矩阵$\bm M_V,\bm M_W$推出伴随矩阵$\bm M_V^{-1}\bm A^\top\bm M_W$（式`eq:ls-weighted-adjoint`），标准正交基下退化为$\bm A^\top$。

4. 示例`ex:ls-weighted-adjoint`在$\operatorname{diag}(4,1)$加权内积下算出伴随矩阵$\left[\begin{smallmatrix}0&0\\4&0\end{smallmatrix}\right]\neq\bm A^\top$并直接核对；说明差别来自读取与向量的对应随内积改变，并把四个基本子空间的正交关系推广为$\ker T^\star=(\operatorname{im}T)^\perp$、$\ker T=(\operatorname{im}T^\star)^\perp$。

###### paragraph：伴随的运算规则

1. 由配对定义推出伴随对加法、数乘、复合（次序反转）与二次伴随的规则，图`fig:ls-adjoint-action-transfer`示意配对从输出端搬回输入端。

2. 示例`ex:ls-adjoint-not-inverse`以$2\operatorname{id}$的伴随为自身而逆为$\tfrac12\operatorname{id}$说明伴随不是逆。

###### paragraph：自伴、正交与正规算子

1. 说明下面四类算子都由$T$与$T^\star$之间的一个等式规定。

2. 定义自伴算子（标准正交基下对应对称矩阵）与反自伴算子（对应反对称矩阵），由$\langle T\bm x,\bm x\rangle=-\langle T\bm x,\bm x\rangle$说明反自伴算子把每个向量送到与它正交的方向，以平面上旋转直角的矩阵为例。

3. 由$Q^\star Q=\operatorname{id}$定义保持内积的正交算子，对应正交矩阵，并由方阵单侧逆即逆得$Q^{-1}=Q^\star$。

4. 定义正规算子$TT^\star=T^\star T$，说明自伴、反自伴与正交算子都正规，以示例`ex:ls-weighted-adjoint`中的$\bm A$在欧氏内积下不正规为反例；谱性质留到第~`chap:eigen-spectral-decomposition`章。

###### paragraph：复空间中的泛函表示与伴随

1. 按复内积约定把线性泛函写成$\langle\bm v,\bm x\rangle$，给出标准正交基下的表示向量$\sum_j\overline{\varphi(\bm q_j)}\bm q_j$，说明表示对应共轭线性。

2. 以$\mathbb C$上$\varphi(z)=(1+\mathrm i)z$对应$v=1-\mathrm i$核验，说明共轭来自内积约定。

3. 给出复伴随在标准正交基下为$\bm A^*$、一般基下为$\bm M_V^{-1}\bm A^*\bm M_W$，与代数对偶映射的$\bm A^\top$区分，并定义Hermitian（自伴）矩阵与酉矩阵。

### 3.7 本章小结

1. 回应章首三个问题：相差多少与是否收敛由范数回答，是否垂直需要内积。

2. 回顾范数部分：坐标范数的显式比较及其依赖维数的常数，同一误差在不同范数下读数不同。

3. 回顾收敛与连续：收敛等价于逐坐标收敛，联合极限要求所有趋近方式一致、路径检验只能否定，闭有界集上的连续函数取到最值并一致连续，三个条件缺一不可。

4. 回顾有限维性质：范数等价使收敛、连续与柯西性质不依赖范数而常数会改变；完备性、子空间闭性、绝对收敛级数及尾和估计；矩阵范数与线性映射的Lipschitz连续、对偶范数、商范数，以及一般范数下最近点存在但未必唯一。

5. 回顾内积部分：内积给出长度、夹角与正交，并非每个范数来自内积（平行四边形恒等式），有限维内积空间是Hilbert空间；Gram矩阵与半正定矩阵的对应及其推出的逐元素乘积保持半正定。

6. 回顾正交与伴随：正交分解与唯一最近点，正交投影即幂等且对称的矩阵；标准正交基、Gram--Schmidt正交化与QR分解；泛函表示与伴随连接代数对偶与几何结构，标准正交基下伴随即转置，一般基下要计入Gram矩阵。

7. 指出这些结论依赖有限维，并说明后续用途：第~`chap:eigen-spectral-decomposition`章在正交换基下寻找线性作用的简单表示；矩阵幂和级数使用收敛与次乘性，迭代使用完备性和误差估计，多元微分用算子范数控制余项。

