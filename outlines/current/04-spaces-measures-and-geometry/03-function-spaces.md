# 卷4《函数空间与流形》：函数空间大纲

所属：卷四《函数空间与流形》第三部分“函数空间”（第10—23章）。卷入口：[volume.tex](../../../tex/04-spaces-measures-and-geometry/volume.tex)；部分入口：[part.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/part.tex)。以下按 `volume.tex → part.tex → 章 → 节 → 小节 → paragraph` 的实际层级记录当前正文；章号在卷内连续，本部分为第10—23章。目标结构依据[十卷计划的本部分细纲](../../../plans/ten-volume-migration/04-spaces-measures-and-geometry/03-function-spaces.md)。

## 部分主线与导读

部分主线：本部分把整个函数当作无限维空间中的向量。第10—13章建立共同结构：对照有限维线性代数说明无限项展开与闭球不紧，加入范数研究完备性与Lᵖ空间，加入内积研究Hilbert空间、正交投影与正交展开，并用有限覆盖衡量函数类的大小；第14—20章研究表示与作用：Fourier与小波分别按频率和尺度给函数建立坐标，线性泛函研究标量观测及弱收敛，线性算子研究函数之间的变换、伴随、紧性与基本定理，算子谱与奇异系统给出展开，算子方程讨论可解性与稳定恢复，函数逼近在误差与表示预算下比较各种方案；第21—23章按问题选取空间：Sobolev空间控制导数与边界，Besov空间区分不同尺度上的变化，再生核Hilbert空间由离散点值观测函数。一般拓扑与度量判据回用第一部分，积分工具回用第二部分；拟合目标、正则化与优化求解归卷五。

部分导读（`\BookPartGuide`）的自然段：

1. 以信号、温度分布、回归函数与方程解为例，指出函数有无穷多个坐标、误差度量的选择影响收敛结论；说明本部分把函数当作无限维向量，研究空间结构及表示、观测、变换与逼近。

2. 说明第10—13章建立共同结构：对照有限维说明无限展开的收敛条件与闭球不紧，分别加入范数与内积研究完备性、Lᵖ空间、正交投影与展开，再问函数类能否用有限代表表覆盖、需要多少代表。

3. 说明第14—20章研究表示与作用：Fourier与小波分别按频率与尺度建立坐标，泛函研究标量观测，算子把观测推广为变换，谱与奇异系统分析算子并讨论算子方程的可解与稳定恢复，函数逼近在误差与预算下比较逼近方式。

4. 说明第21—23章按问题选空间：控制导数与边界用Sobolev空间，区分不同尺度局部变化用Besov空间，由离散点值观测用再生核Hilbert空间；交代一般判据回用第一部分、积分工具回用第二部分，拟合与优化归卷五。

## 第10章 函数作为无限维向量

正文入口：[01-functions-as-vectors.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors.tex)，章内依次输入[01-linear-operations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/01-linear-operations.tex)、[02-dimension.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/02-dimension.tex)、[03-infinite-expansions.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/03-infinite-expansions.tex)、[04-closed-ball-noncompact.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/04-closed-ball-noncompact.tex)、[05-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/05-summary.tex)。

章职责与主线：本章把函数类比为“每个输入占一个分量”的无限维向量$[\ldots,a_1,a_2,\ldots]$，让这一类比贯穿“运算—维数—展开—紧性”四步，每一步都说明对应物是什么、类比在哪里失效：逐点运算对应逐分量运算，由此得到函数空间；维数看张成需要的方向数而不是定义域点数，并以$P_2$上系数列与取值列的矩阵关系展示函数的两种“一列数”；维数无限后，代数基只允许有限组合，级数的收敛、表示范围与系数唯一性都依赖误差的选择；最后由Riesz引理证明任何无限维赋范空间的闭球都不紧，并用鼓包列和$x^n$给出两种失败方式。范数、完备性与正交展开分别留给第11、12章。

1. 章首第一段从拟合曲线、研究近似函数列需要把整个函数当作对象进入，提出要对函数做加法、缩放和量距离。

2. 第二段给出全章类比：把函数在一串输入处的取值排成长向量$[\ldots,a_1,a_2,a_3,\ldots]$，输入取遍定义域时函数就是每个输入占一个分量的向量。

3. 第三段说明本章做法：把卷二的相加、数乘、基、坐标和范数逐一搬到函数上，每次都问对应物是什么、类比在哪里失效。

4. 第四段说明四节的衔接：逐点运算对应逐分量运算，比较定义域点数与空间维数，无限维后讨论无穷和，最后处理单位球中可有无穷多彼此远离的点。

5. 第五段划定范围：本章只建立线性结构并指出困难，范数、完备性与$L^p$在第11章，内积与正交展开在第12章，函数类的有限代表在第13章。

### 10.1 函数的线性运算

正文：[01-linear-operations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/01-linear-operations.tex)

1. 以温度曲线取平均、信号放大、近似减目标得误差等操作进入，指出它们遵守向量运算的规则，原因是函数可以看成每个输入占一个分量的向量。

2. 固定全章约定：标量域$\mathbb K$为$\mathbb R$或$\mathbb C$，函数空间的元素是整个函数，用普通字母表示、不用粗体。

###### paragraph：逐点加法与数乘

1. 在四个等距点上采样$f(x)=x^2$与$g(x)=1-x$，得到两个四维向量，逐分量相加得到$[1,\tfrac79,\tfrac79,1]$。

2. 指出$h(x)=x^2-x+1$在这四点的取值就是这四个数，说明采样向量相加与函数逐点相加给出同一列数。

3. 说明结论与采样点个数无关，取遍全部输入时就得到函数的加法，并引出配图。

4. 配图`fig:fvec-pointwise-addition`：(a)四个采样点上$f$、$g$、$f+g$的分量，(b)全部输入上的曲线及固定$x$处两段高度首尾相接等于和。

5. 固定输入集合$X$与全体函数$\mathbb K^X$，对照$\mathbb K^d$的记号，用式`eq:fvec-pointwise-operations`定义逐点加法与数乘，给出零函数、负元和逐点运算的名称。

6. 以加法交换律为例说明八条规则在固定输入处的验证方法，写出数的交换律给出的等式链。

7. 指出结合律等规则同样逐点继承，$\mathbb K^X$是线性空间，这与逐分量验证$\mathbb K^d$的做法相同，并引用卷二第2章。

8. 取$X=\{1,\ldots,d\}$、$\mathbb N_+$、$[0,1]$分别得到向量、数列和区间上的函数，说明差别只在下标集合。

9. 配图`fig:fvec-index-to-function`：三种下标集合上的取值，竖线的顶点在连续下标时连成函数图像。

10. 指出类比的第一个边界：区间上的输入不可数，无法排成一列，$[\ldots,f(x),\ldots]$只是图景，但逐点定义不需要排序；并引出对应表。

11. 表`tab:fvec-dictionary`：下标与输入、分量与取值、逐分量运算与逐点运算、零元、相等的对应。

###### paragraph：线性子空间的核验

1. 由$\mathbb R^3$中过原点的平面类比，给出线性子空间的三条核验，并把通过核验的集合称为函数空间。

2. 核验$C[a,b]$与$P_m$是线性子空间。

3. 核验收敛到零的数列$c_0$与有限支撑数列$c_{00}$是线性子空间。

4. 把$\{f(0)=0\}$对应为$\mathbb R^3$的平面$x_1=0$，把$\{f(0)=1\}$对应为不过原点的平面$x_1=1$，说明后者不含零函数且不封闭。

5. 由$\mathbb R^2$两条坐标轴的并集对数乘封闭、对加法不封闭，引出单折点参数族$\mathcal R$。

6. 分段算出$\max(0,x)+\max(0,x-1)$，斜率改变两次，故不在$\mathcal R$中，说明这类族可作逼近工具但不是线性空间。

###### paragraph：函数值、函数元素与坐标

1. 把向量的下标、分量、整个向量三个层次对应到输入、函数值和函数本身，区分比较元素与比较一个位置。

2. 说明坐标依赖所选的基，把$p(x)=2-x+3x^2$相对$1,x-1,(x-1)^2$重写，用代换$x=t+1$逐步算出坐标$(4,5,3)$。

3. 说明元素不变而记录方式改变，与卷二基变换相同，并引出配图。

4. 配图`fig:fvec-two-coordinates`：同一条曲线的两种三项分解及各项高度之和。

5. 解释$p(1)=4$等于第二组首项是因为另两个基函数在$1$处为零，第一组首项等于$p(0)$而不等于$p(1)$。

6. 总结函数有取值列和系数列两种“一列数”，前者不需选基，后者随基改变。

###### paragraph：乘法与微分不是一般的内部运算

1. 对照向量的逐分量乘积，说明逐点乘法不属于线性结构，$P_m$对乘法不封闭。

2. 说明$C[0,1]$对乘法封闭而对求导不封闭，例子是$\lvert x-\tfrac12\rvert$。

3. 说明乘积和导数须单独交代定义域与值域，在$P_2$上把求导写成$3\times3$矩阵。

4. 代入$(2,-1,3)$得$(-1,6,0)$，并指出乘固定函数在采样点上是对角矩阵；这类映射是第17章的线性算子，可微性的推广由第7章的弱导数承担。

### 10.2 函数空间的维数

正文：[02-dimension.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/02-dimension.tex)

1. 重述维数是张成所需的最少方向数，提醒只有输入集合有限时点数才等于$\mathbb K^X$的维数，一般函数空间的维数可以远小于点数。

#### 10.2.1 有限维函数空间

1. 从有限输入集合进入，函数由$m$个取值确定，期望$\mathbb K^X$与$\mathbb K^m$是同一空间的两种写法。

###### paragraph：指示函数基

1. 把标准基$e_i$照搬到函数上，定义指示函数$\delta_i$。

2. 由式`eq:fvec-indicator-expansion`及逐点比较得到$\delta_i$张成$\mathbb K^X$。

3. 取值证明线性无关，得到$\dim\mathbb K^X=m$，坐标恰为函数的$m$个取值。

4. 以$X=\{0,1,2\}$上$f=(1,0,4)$与$g=(2,-1,1)$算出$2f-g=(0,1,7)$，线性运算完全变为坐标运算。

5. 配图`fig:fvec-indicator-basis`：三个指示函数与$f=\delta_0+4\delta_2$的取值。

###### paragraph：多项式基与坐标

1. 指出有限维函数空间不必来自有限输入集合，$1,x,\ldots,x^m$张成$P_m$。

2. 由多项式至多有$m$个根证线性无关，得到式`eq:fvec-polynomial-dimension`，系数是坐标。

3. 说明定义域不可数而$P_m$只有$m+1$维，维数与定义域点数无关。

4. 在$P_2$上由取值列$(2,4,12)$与系数列$(2,-1,3)$得到式`eq:fvec-vandermonde`的矩阵关系。

5. 由行列式等于$2$说明矩阵可逆，两列数互相决定，并引出配图。

6. 配图`fig:fvec-coefficient-point`：同一抛物线在系数坐标系和取值坐标系中各是一个点。

7. 构造$\ell_0,\ell_1,\ell_2$使取值列成为坐标，并验证$p=2\ell_0+4\ell_1+12\ell_2$。

#### 10.2.2 无限维函数空间

1. 由$\mathbb R^1\subset\mathbb R^2\subset\cdots$的延续类比，定义无限维，并用卷二的线性无关个数上界说明其含义。

###### paragraph：全体多项式

1. 说明$P$是线性子空间，且对每个$m$有$m+1$个线性无关元素，故为无限维。

2. 直接说明任何有限族张不成$P$：最高次数$d$之外的$x^{d+1}$落在外面。

###### paragraph：全体数列

1. 定义标准单位列$e_k$，读出各项证明线性无关，数列空间是无限维的。

2. 推广到任意无限输入集合，并指出类比的边界：$X$无限时指示函数的有限组合只在有限个点非零，取值不再是有限坐标。

###### paragraph：每个元素有限与整体无限

1. 区分每个元素只用有限个方向与整个空间没有统一的有限基，用多项式的系数列和$c_{00}$说明。

2. 由图解读多项式的系数列所占位置没有统一上限，并指出$e^x$的系数永不为零，它不是多项式。

3. 配图`fig:fvec-finite-support-grid`：三个多项式与$e^x$的系数列方格。

4. 把常数列与$e^x$并列，指出要表示它们只能借助无穷和。

### 10.3 无限展开

正文：[03-infinite-expansions.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/03-infinite-expansions.tex)

1. 对比有限维的精确表示，把无限维的问题分成有限组合覆盖什么、部分和在什么意义下收敛两个问题，用数列分开研究。

#### 10.3.1 代数基与级数表示

1. 说明把只允许有限组合的基的要求原样用于无限维，并引出定义。

2. 定义`def:fvec-algebraic-basis`：代数基。

3. 解释线性无关保证表示唯一，有限组合不涉及极限。

###### paragraph：有限支撑数列与全体数列

1. 说明$\{e_k\}$是$c_{00}$的代数基，并指出全体多项式通过系数列就是换了名字的$c_{00}$。

2. 说明同一族在全体数列空间中不再张成，常数列不是有限组合。

3. 说明一般代数基的存在要用选择公理，并建议读者查阅教材；存在性证明不给出具体的基，代数基也不能谈无穷和。

###### paragraph：级数表示需要另外核对的内容

1. 把无穷和理解为部分和的极限，指出需要先规定收敛的含义。

2. 列出收敛性、表示范围和唯一性三件需要分别核对的事。

3. 以逐项收敛的意义，引入族$u_0=e_1,u_k=e_k-e_{k+1}$作为唯一性失败的例子。

4. 逐项读取证明这族元素的任意有限个线性无关。

5. 由裂项和$\sum_{k\leq N}u_k=e_1-e_{N+1}$得到$e_1$的第二种展开，系数列分别是$(1,0,\ldots)$与$(0,1,1,\ldots)$。

6. 在有界数列与上确界距离下，构造不可数多个两两距离为$1$的$\chi_S$。

7. 假设可数族能级数表示每个有界数列，得到有理系数有限组合的可数逼近集。

8. 由半径$\tfrac12$开球两两不交导出矛盾，结论是可数级数表示要求空间可分。

#### 10.3.2 展开的收敛

1. 提出逐项比较与统一比较两种接近方式，用$N=\max\{N_1,\ldots,N_d\}$说明二者在$\mathbb K^d$中等价。

2. 指出这一步依赖分量有限，分量无穷多时$N_k$可能没有上界。

###### paragraph：常数列的截断

1. 写出$x=(1,1,\ldots)$的截断及误差形状。

2. 说明逐项收敛成立而统一误差恒为$1$，未对上的项永远存在。

###### paragraph：调和数列的截断

1. 由式`eq:fvec-harmonic-truncation`得到调和数列截断的统一误差为$1/(N+1)$，尾部变小使统一误差趋于零。

2. 配图`fig:fvec-truncation-error`：两次截断的保留项、误差项和上确界。

###### paragraph：收敛意义的选择

1. 对比两种误差下的结论，并指出统一误差下恰好$c_0$中的数列能这样展开，级数收敛必须说明误差。

2. 表`tab:fvec-truncation-compare`：两种误差对两个数列的结论。

3. 以$e^x$的系数列为函数情形的例子，写出部分和$s_N$，在$[0,1]$上把$x^k$放大到$1$估计误差。

4. 用等比级数得到式`eq:fvec-exp-truncation`的上界$2/(N+1)!$，$N=3$时为$\tfrac1{12}$。

5. 说明在$\mathbb R$上逐点收敛但每个$N$的统一误差为无穷大，二者结论不同。

6. 把逐点、一致、积分三种误差分开，指向第11、12及第20章。

### 10.4 无限维闭球不紧

正文：[04-closed-ball-noncompact.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/04-closed-ball-noncompact.tex)

1. 回顾有限维中抽收敛子列的存在性论证，提出这条路在无限维中会断。

2. 以$c_0$中$e_m$与$e_n$的距离恰为$1$给出具体现象。

3. 说明本节要证明这是所有无限维赋范空间的性质，并回顾范数与诱导距离。

4. 指向卷二第3章与第11章，说明本节只用公理和距离的语言。

###### paragraph：有限维子空间是闭集

1. 说明后续构造需要有限维子空间闭的事实，并由直线、平面的直观引入。

2. 引理`lem:fvec-finite-subspace-closed`及其证明：收敛列是柯西列，$Y$的完备性给出$Y$中的极限，极限唯一。

3. 指出证明只用$Y$自身完备，由闭性得到线外点到$Y$的距离严格为正。

###### paragraph：Riesz引理

1. 在$\mathbb R^2$中用垂线与归一化造出到$Y$距离为$1$的单位向量。

2. 说明一般赋范空间没有垂直、最近点也可能不存在，所以退而取几乎最近的点，并引出配图。

3. 配图`fig:fvec-riesz-lemma`：$\mathbb R^2$中$x_0$、$y_0$与归一化得到的$x$。

4. 由几何过程引出引理。

5. 引理`lem:fvec-riesz`及其证明，每步单列：取几乎最近的$y_0$，通分并利用子空间性质得到$\lVert x-y\rVert\geq\theta$。

6. 以$c_{00}\subset c_0$说明$Y$不闭时结论失败：每点到$Y$的距离为$0$。

7. 由有限维最近点存在引出$\theta=1$在无限维中可能失败。

8. 例`ex:fvec-riesz-theta-one`：$X=\{f(0)=0\}$、$Y=\{\int f=0\}$，用$h_n=\min(nt,1)$算出每个单位向量到$Y$的距离小于$1$。

###### paragraph：两两远离的单位向量

1. 用Riesz引理逐个构造单位向量$e_{n+1}$。

2. 说明序列线性无关，并由式`eq:fvec-separated-sequence`两两距离至少$\tfrac12$；第11章构造不等价范数还会用到它。

3. 引出闭球不紧的定理。

4. 定理`thm:fvec-closed-ball-noncompact`及其证明：半径$\tfrac14$的开球至多含一个$e_n$，闭球不全有界；一般闭球由伸缩平移得到。

5. 指出证明不用完备性，不紧的原因是有界区域装得下无穷多互相隔开的点。

6. 用体积比较得到式`eq:fvec-packing-bound`的上界$N\leq5^d$，维数无限时不再有上界。

###### paragraph：连续函数的例子

1. 说明Riesz引理给出存在性，具体函数空间可直接写出例子，在$C[0,1]$上取最大绝对值距离。

2. 配图`fig:fvec-bounded-noncompact`：$\mathbb R^2$单位圆盘内的点、鼓包$\varphi_n$与$x^n$及其逐点极限。

3. 定义鼓包$\varphi_n$，类比标准单位列。

4. 算出鼓包两两距离为$1$，它们在闭单位球内而没有收敛子列。

5. 转向$x^n$，算出相邻两项的距离不超过$1/(n+1)$，序列看似收敛。

6. 由逐点极限在$1$处不连续证明$x^n$没有一致收敛子列。

7. 对比两种失败：鼓包的逐点极限在空间内但一致距离不降，$x^n$的逐点极限跑出空间；恢复紧性的条件见第3章和第13章。

### 10.5 本章小结

正文：[05-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/01-functions-as-vectors/05-summary.tex)

1. 回应开头的问题，并引出汇总表。

2. 表`tab:fvec-summary`：线性运算、维数、取值与坐标、基、无穷和、两种收敛、有界序列在有限维与无限维的对比。

3. 总结线性运算完整保留，子空间核验，元素、取值与坐标的区分。

4. 总结维数与定义域点数无关，取值列与系数列互相决定，无限维的含义。

5. 总结两个困难：级数依赖误差，闭球不紧不需要完备。

6. 把两个困难分别指向第11章和第12章，并提醒无限维中需要额外的紧性条件或更弱的收敛概念。

## 第11章 赋范空间

正文入口：[02-normed-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces.tex)，章内依次输入[01-norms.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/01-norms.tex)、[02-banach-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/02-banach-spaces.tex)、[03-continuous-function-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/03-continuous-function-spaces.tex)、[04-lp-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/04-lp-spaces.tex)、[05-linfty-space.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/05-linfty-space.tex)、[06-convergence-of-sequences.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/06-convergence-of-sequences.tex)、[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/07-summary.tex)。

章职责与主线：本章沿用上一章把函数看作无限维向量的类比，用范数规定函数之间的距离，并研究类比在哪里失效。先把范数公理用于函数，由采样向量的最大分量和加权和得到一致范数与积分范数，说明无限维上存在不等价范数；再定义Banach空间，证明紧集上的连续函数在一致范数下完备而在积分范数下不完备；接着在几乎处处等价类上建立$L^p$与$L^\infty$，证明Young、Hölder、Minkowski不等式和完备性；最后比较逐点、一致、$L^p$与依测度收敛，用一致可积性连接依测度收敛与$L^1$收敛。内积结构、包含映射与稠密性逼近分别留给第12、17、20章。

1. 章首第一段以$x^2$近似$x$的误差给出最大误差$\tfrac14$与积分误差$\tfrac16$，说明两种误差回答不同问题，收敛要先说清用哪种误差。

2. 第二段接上一章的向量类比，说明本章把有限维的范数搬到函数上，并预告不等价范数和无极限的柯西列两处差别。

3. 第三段说明11.1规定函数的大小与收敛、11.2问柯西列的极限是否在空间内。

4. 第四段说明11.3至11.6的分工：连续函数的完备与不完备，$L^p$与$L^\infty$为积分极限找去处，比较各种收敛方式。

5. 第五段说明对第2、3、5、6章的依赖和对第12、17、20章的分工。

### 11.1 范数

正文：[01-norms.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/01-norms.tex)

1. 以给函数差规定大小引入，说明把卷二的范数公理用到整个函数上。

#### 11.1.1 函数的范数

1. 说明函数的范数衡量整个函数的大小，引出定义`def:nspace-norm`。

2. 解释三条公理对函数的含义：零元素是处处为零的函数，齐次性是整体放大，三角不等式是误差估计的基本工具。

3. 指向卷二第3章的有限维例子。

###### paragraph：两种整体大小

1. 回顾向量的最大分量与分量和，说明函数是下标连续变化的向量，分量和需要调整。

2. 用$n$个中点采样，给分量配权重$1/n$，加权和趋于积分。

3. 给出$C[0,1]$上的$\lVert\cdot\rVert_\infty$与$\lVert\cdot\rVert_1$（式`eq:nspace-two-norms`）。

4. 以$h=x-x^2$、$n=4$手算采样向量、最大分量$\tfrac{15}{64}$和加权和$\tfrac{11}{64}$。

5. 给出一般偶数$n$的两个公式，令$n\to\infty$得$\tfrac14$与$\tfrac16$。

6. 配图`fig:nspace-two-sizes`：三个子图分别画最大绝对值、曲线下面积和$n=4$的采样柱。

7. 逐点验证$\lVert\cdot\rVert_\infty$的三角不等式、齐次性和正定性。

8. 验证$\lVert\cdot\rVert_1$的公理，用连续性得到正定性。

###### paragraph：有限性与正定性要逐个空间核验

1. 只在一点非零的函数积分为零，引出半范数。

2. 指出类比的第一处差别：函数的单个点权重为零，积分看不见单个坐标。

3. 上确界可能无穷，归纳配范数须核验封闭性、有限性、正定性。

#### 11.1.2 范数与收敛

1. 由范数得到距离并验证三角不等式，说明赋范空间都是度量空间。

###### paragraph：依范数收敛与柯西列

1. 定义依范数收敛与柯西列，收敛列都是柯西列，反之取决于空间。

2. 解释一致范数收敛是一致收敛，积分范数收敛只控制面积。

3. 给出单向控制$\lVert f\rVert_1\leq\lVert f\rVert_\infty$（式`eq:nspace-sup-controls-l1`）。

###### paragraph：等价范数

1. 从互相控制引出定义`def:nspace-equivalent-norms`（式`eq:nspace-equivalent-norms`）。

2. 强调常数与$f$无关，说明等价范数给出相同的收敛、极限与完备性。

3. 给出单位球互相夹住的几何图像，以$\mathbb R^2$上$\lVert x\rVert_\infty\leq\lVert x\rVert_1\leq2\lVert x\rVert_\infty$为例。

4. 配图`fig:nspace-unit-balls`：画出菱形、正方形和放大一倍的菱形的包含关系。

5. 回用卷二有限维范数等价的结论，指出其证明依赖单位球面的紧性，无限维须另作判断。

#### 11.1.3 范数不等价

1. 用$\mathbb R^n$上平均值与最大分量的比较说明常数$n$不可改进。

2. 说明$n\to\infty$时常数无上界，等价关系可能断裂，预告一般构造与具体例子。

###### paragraph：用代数基构造

1. 取第10章的单位列，说明按方向压缩的想法。

2. 把单位列扩充为代数基，写出元素的有限表示，选择公理的证明请读者查阅集合论教材。

3. 定义压缩映射$T$，说明它线性且单射。

4. 令$N_2(x)=N_1(Tx)$，核验范数公理。

5. 比较$e_n$上的取值，否定等价下界。

6. 给出$c_0$上可具体计算的对应例子。

###### paragraph：连续函数上的一对具体范数

1. 由$x^n$的两个范数值说明$\lVert\cdot\rVert_\infty$与$\lVert\cdot\rVert_1$不等价。

2. 把$x^n$类比为向量$(1,0,\ldots,0)$，解释峰顶与面积的差别。

3. 配图`fig:nspace-xn-norms`：左图为$x^n$曲线，右图为三种范数随$n$的变化。

###### paragraph：与有限维的对照

1. 区分“存在不等价的范数”和“任意两个范数都不等价”。

2. 说明无限维中的收敛必须连同范数陈述。

### 11.2 Banach空间

正文：[02-banach-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/02-banach-spaces.tex)

1. 说明迭代与截断常只给出柯西列，需要空间中真有极限。

2. 用$\mathbb Q$中$\sqrt2$的小数近似类比，说明空缺取决于集合和范数，引出定义`def:nspace-banach`。

3. 说明定义是第2章的完备性，有限维自动成立，无限维须逐个证明。

###### paragraph：闭子空间判据

1. 借第2章的闭子集结论，引出定理`thm:nspace-closed-subspace`并给出证明。

2. 说明两个方向的分工。

###### paragraph：不闭的子空间

1. 取$e^x$的Taylor多项式作为例子。

2. 说明最大误差在$x=1$取到，手算$N=1,2,4$的误差，并给出Lagrange余项的界。

3. 用三角不等式证明Taylor多项式列是柯西列。

4. 说明它在多项式空间中没有极限。

5. 指出这等价于多项式空间在$C[0,1]$中不闭。

###### paragraph：范数与完备性是两个问题

1. 区分配范数与完备性回答的两个问题。

2. 说明抽象完备化不告诉新元素是哪类函数。

3. 说明本章采用在更大函数集合上直接定义范数的路线。

### 11.3 连续函数空间

正文：[03-continuous-function-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/03-continuous-function-spaces.tex)

1. 预告紧集上的完备性、非紧定义域的调整和积分范数下完备性的失去。

###### paragraph：紧集上的一致范数

1. 定义$C(K)$上的一致范数（式`eq:nspace-uniform-norm`），由紧性保证最大值有限。

2. 说明公理核验与$C[0,1]$相同，$K$有限时回到$\mathbb K^d$的最大分量范数。

###### paragraph：一致范数下的收敛

1. 把一致范数收敛解释为曲线落在误差带内。

2. 引导读配图中两种情形：曲线在带内和$x^n$越出带子。

3. 配图`fig:nspace-uniform-tube`：左图为带内函数，右图为$x^4,x^{12}$的越出点。

4. 计算$\lVert x^n-x^{2n}\rVert_\infty=\tfrac14$，说明$x^n$不是柯西列。

###### paragraph：完备性

1. 回用第3章的两个结论，引出定理`thm:nspace-ck-complete`并证明。

2. 说明证明中候选极限、共同阈值、连续性各有出处，紧性只保证最大值有限。

###### paragraph：非紧定义域

1. 引入有界连续函数空间$C_b(X)$（式`eq:nspace-cb`）及其范数。

2. 补充一致极限有界的一步，得到$C_b(X)$是Banach空间。

3. 用移动三角形说明逐点收敛而不依范数收敛，质量移向无穷远。

###### paragraph：积分范数下的不完备

1. 回到$C[0,1]$改用积分范数，说明集合不变而完备性失去。

2. 定义折线列$g_n$，说明它逼近阶跃函数。

3. 配图`fig:nspace-step-ramp`：左图为折线与阶跃函数，右图为$g_4,g_8$之间面积$\tfrac1{16}$。

4. 由单调性和面积算出$\lVert g_n-g_m\rVert_1=\tfrac1{2n}-\tfrac1{2m}$（式`eq:nspace-ramp-distance`），得到柯西列，以$n=4,m=8$验算。

5. 证明没有连续极限：在$[0,\tfrac12]$上为零。

6. 证明在$(\tfrac12,1]$上为一，导出矛盾。

7. 指出同一列在一致范数下不是柯西列。

8. 说明极限是阶跃函数，引出下一节扩大成员并取等价类。

### 11.4 $L^p$空间

正文：[04-lp-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/04-lp-spaces.tex)

1. 说明折线列的极限是阶跃函数，本节按$p$次幂累计偏差并取等价类。

2. 固定测度空间，说明实复情形论证相同。

###### paragraph：几乎处处相等的函数

1. 用只在一点不同的两个函数说明积分无法区分它们。

2. 定义几乎处处相等（式`eq:nspace-ae-equivalence`）与等价类，验证等价关系。

3. 定义等价类的运算，验证不依赖代表，得到线性空间。

4. 把取等价类类比为放弃读取单个分量，说明点值一般没有意义。

###### paragraph：$L^p$范数

1. 把向量$p$范数的求和换成积分，引出定义`def:nspace-lp`（式`eq:nspace-lp-norm`）。

2. 核验数值不依赖代表、正定性和齐次性。

3. 用$t^p$的凸性证明$L^p$对加法封闭，指出三角不等式要用Hölder。

###### paragraph：不同的$p$

1. 用$h_1\equiv1$与$h_2=4\cdot\mathbf 1_{[0,1/4]}$手算$L^1$与$L^2$范数，说明集中误差被放大。

2. 给出$\lVert h_2\rVert_p=4^{1-1/p}$，引出配图。

3. 配图`fig:nspace-lp-weight`：左图为两个误差，右图为范数随$p$的变化。

4. 用$x^{-1/2}$与$x^{-1/4}$说明可积性随$p$改变。

###### paragraph：数列空间

1. 计数测度下得到$\ell^p$（式`eq:nspace-ellp`），说明它是有限维$p$范数的延伸，并以$1/k$为例。

###### paragraph：Hölder与Minkowski不等式

1. 引入共轭指数。

2. 回顾有限维的乘积估计，引出Young不等式。

3. 引理`lem:nspace-young`（式`eq:nspace-young`）及其由一元函数求最小值的证明。

4. 解释面积图像，配图`fig:nspace-young-area`。

5. 用图中数字验算不等式与等号情形。

6. 定理`thm:nspace-holder`（式`eq:nspace-holder`）及归一化证明。

7. 说明归一化的作用，并用$f=x,g=x^2$与$f=1,g=x$验算。

8. 定理`thm:nspace-minkowski`（式`eq:nspace-minkowski`）及证明。

9. 说明证明中除法需要$I$有限且为正。

###### paragraph：完备性

1. 说明困难在于$L^p$范数不控制每一点。

2. 预告先抽子列、再用Fatou引理的路线。

3. 定理`thm:nspace-lp-complete`，分五步证明：快速子列、控制函数$S_m$、候选极限、子列依范数收敛、回到整列。

4. 总结五步各自的职责。

5. 用具体序列说明$S_m$的控制作用。

6. 配图`fig:nspace-fast-subsequence`：左图为子列函数，右图为控制函数。

7. 定理`thm:nspace-lp-ae-subsequence`及证明。

8. 回到折线列，取$n_k=2^k$算相邻误差，和为$\tfrac14$。

9. 控制函数逐项相消得$S=\mathbf 1_{(1/2,1]}$，核对$\lVert S\rVert_1=\tfrac12=C$。

10. 算$\lVert g_n-\mathbf 1_{(1/2,1]}\rVert_1=\tfrac1{2n}$，说明取等价类的用意，计数测度下得到$\ell^p$完备。

### 11.5 $L^\infty$空间

正文：[05-linfty-space.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/05-linfty-space.tex)

1. 由$p\to\infty$引入最大偏差，说明普通上确界对等价类没有意义。

###### paragraph：本质上确界

1. 说明合理的要求是在零测集之外有上界。

2. 定义`def:nspace-linfty`（式`eq:nspace-esssup`）。

3. 证明下确界可以达到（式`eq:nspace-esssup-attained`），并说明数值不依赖代表。

###### paragraph：与逐点上确界的比较

1. 以$f=x$改动一点为例说明两者差别。

2. 配图`fig:nspace-essential-sup`。

3. 有理点指示函数的例子。

4. 证明连续函数两者一致，并说明本质上界不控制每个代表。

5. 计数测度下得到$\ell^\infty$（式`eq:nspace-ellinfty`），说明它与第10章不可分性的联系。

###### paragraph：范数公理

1. 说明关键是合并例外集。

2. 验证正定性和齐次性。

3. 验证三角不等式与加法封闭。

###### paragraph：$L^1$与$L^\infty$的Hölder估计

1. 给出端点估计（式`eq:nspace-holder-endpoint`）。

2. 由式`eq:nspace-esssup-attained`一步证明。

3. 说明它与第16章线性泛函的联系。

###### paragraph：完备性

1. 说明与有限$p$情形的证明方式不同。

2. 定理`thm:nspace-linfty-complete`及证明：合并例外集、补集上一致柯西、极限属于$L^\infty$。

3. 对照两种完备性证明。

4. 计数测度下得到$\ell^\infty$完备。

### 11.6 函数列的收敛

正文：[06-convergence-of-sequences.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/06-convergence-of-sequences.tex)

1. 列举几种收敛并用向量语言类比。

2. 指出函数列的收敛方式只在附加条件下互推，说明与第6章的衔接。

3. 固定测度空间与函数列。

#### 11.6.1 逐点、一致与$L^p$收敛

1. 回顾三种收敛的含义。

###### paragraph：代表的选择

1. 说明逐点、一致收敛依赖代表。

2. 给出等价类上的几乎处处收敛与本质一致收敛。

3. 说明$L^p$收敛和依测度收敛只依赖等价类。

###### paragraph：一致收敛推出$L^p$收敛的条件

1. 有限测度下得到式`eq:nspace-uniform-to-lp`，以$h_n=\tfrac1n\mathbf 1_{[0,n]}$说明测度无限时失败。

2. 由Hölder不等式得到不同指数的比较（式`eq:nspace-lp-inclusion`），指向第17章。

###### paragraph：三个对照序列

1. 引导读配图和表格。

2. 配图`fig:nspace-convergence-modes`与表`tab:nspace-convergence-modes`。

3. 分析$x^n$。

4. 分析窄尖峰。

5. 例`ex:nspace-typewriter`打字机序列。

6. 写出打字机序列的几乎处处收敛子列。

#### 11.6.2 依测度收敛

1. 说明依测度收敛只问超差区域多大，并用向量语言类比。

2. 定义`def:nspace-convergence-in-measure`。

3. 以窄尖峰和打字机序列说明定义的内容。

###### paragraph：$L^p$收敛推出依测度收敛

1. 由积分下界得到Chebyshev不等式（式`eq:nspace-chebyshev`）。

2. 用三角形$h(x)=1-\lvert2x-1\rvert$手算一例。

3. 配图`fig:nspace-chebyshev`。

###### paragraph：有限测度下几乎处处收敛推出依测度收敛

1. 说明两者的含义，定理`thm:nspace-ae-to-measure`及证明。

2. 说明有限测度的作用，并给出$\mathbf 1_{[n,n+1]}$的反例。

###### paragraph：依测度收敛列的几乎处处收敛子列

1. 定理`thm:nspace-measure-subsequence`及证明。

2. 说明证明思路及其与定理`thm:nspace-lp-ae-subsequence`的关系。

#### 11.6.3 一致可积性

1. 说明窄尖峰的积分躲在小区域中，需要比共同上界更弱的条件。

2. 定义`def:nspace-uniform-integrability`（式`eq:nspace-uniform-integrability`）。

3. 说明单个可积函数总满足，一致可积要求整族同时满足。

###### paragraph：尖峰与共同上界

1. 证明窄尖峰不一致可积。

2. 算出$\sqrt n\,\mathbf 1_{(0,1/n)}$一致可积。

3. 配图`fig:nspace-uniform-integrability`。

4. 证明共同可积上界推出一致可积，窄尖峰没有这样的上界。

###### paragraph：一致的小区域控制

1. 给出式`eq:nspace-ui-small-sets`。

2. 由此得到小区域上积分一致小和$L^1$有界。

###### paragraph：从依测度收敛到$L^1$收敛

1. 说明思路，定理`thm:nspace-vitali`及证明。

2. 说明证明的两部分和有限测度的两处作用。

3. 用$\sqrt n$尖峰验证定理，并指出窄尖峰不满足条件。

###### paragraph：回到支配收敛

1. 由定理`thm:nspace-vitali`回到支配收敛定理。

2. 说明共同可积上界只是一致可积的充分条件。

3. 说明$L^1$收敛的序列一致可积，证明请读者查阅测度论教材。

### 11.7 本章小结

正文：[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/02-normed-spaces/07-summary.tex)

1. 回到章首问题，总结范数与两种整体大小。

2. 引导读表`tab:nspace-summary`。

3. 表`tab:nspace-summary`对照有限维向量与无限维函数空间。

4. 总结不等价范数。

5. 总结完备性：闭子空间判据、连续函数空间、积分范数下不完备。

6. 总结$L^p$与$L^\infty$。

7. 总结各收敛方式及其互推条件，引出配图。

8. 配图`fig:nspace-convergence-relations`：收敛方式的推出关系。

9. 说明后续章节的分工。

## 第12章 内积空间

正文入口：[03-inner-product-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces.tex)，章内依次输入[01-inner-products.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/01-inner-products.tex)、[02-hilbert-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/02-hilbert-spaces.tex)、[03-l2-space.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/03-l2-space.tex)、[04-orthogonal-projection.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/04-orthogonal-projection.tex)、[05-orthonormal-bases.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/05-orthonormal-bases.tex)、[06-orthogonal-expansions.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/06-orthogonal-expansions.tex)、[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/07-summary.tex)。

章职责与主线：本章沿用前两章“函数是无限维向量”的类比，把有限维的点积推广为内积。先由取样点积的极限得到积分内积，固定复情形约定，由Cauchy--Schwarz不等式得到诱导范数，用平行四边形恒等式判别范数是否来自内积；再定义Hilbert空间，用有限支撑数列和平方积分下的连续函数说明完备性可能失败，并以$L^2$与$\ell^2$给出实例。随后证明闭子空间上最近点存在唯一及其正交刻画，定义正交投影与正交分解，用反例说明闭性和完备性都不能去掉；定义完备正交系并与代数基对比，给出正交判据和可分空间的可数正交基；最后用内积系数写出展开，建立有限截断、Bessel不等式、级数收敛、Parseval等式与尾和误差，并说明不完备和点态收敛的边界。

1. 指出前两章已把函数看成无限维向量并规定了长度，有限维的点积还没有搬过来，而夹角、垂直、投影都依赖它。

2. 以$[-1,1]$上用常数近似$x^2$（最佳常数$\tfrac13$，误差与常数垂直）和用多项式逼近阶跃函数两个问题说明点积对函数的用处。

3. 说明结构部分：12.1推广内积并说明哪些范数不来自内积，12.2定义Hilbert空间，12.3用$L^2$与$\ell^2$给出实例。

4. 说明几何部分：12.4证明最近点存在唯一并即正交投影，12.5说明无限维中的“基”，12.6用内积系数写出无限展开。

5. 划定范围：泛函的内积表示与投影算子、三角函数系和小波的完备性、截断误差与光滑性、点值连续的函数空间分别归后面相应各章。

### 12.1 内积

正文：[01-inner-products.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/01-inner-products.tex)

1. 说明内积公理不提维数，可以搬到函数和数列上，提出函数上的内积形式、诱导长度为何是范数、哪些范数不来自内积三个待确认的问题，并指向卷二相应章。

###### paragraph：内积的公理

1. 由$\langle\mathrm ix,\mathrm ix\rangle=-\langle x,x\rangle$说明复空间不能要求双线性，由此采用共轭对称，并按卷二约定对第二个变量线性。

2. 给出内积与内积空间的定义（定义`def:ipspace-inner-product`），三条公理分别编号。

3. 由前两条写出对第一个变量的共轭线性，说明共轭对称使$\langle f,f\rangle$为实数，实情形退回卷二的三条公理。

###### paragraph：函数与数列上的内积

1. 把$[-1,1]$等分取中点，函数读成$N$维向量，点积乘步长收敛到积分（式`eq:ipspace-riemann-dot`），并说明乘步长的必要性。

2. 用$f=1+x$、$g=x$、$N=4$手算读出的两个向量、点积$1.25$和乘步长后的$0.625$。

3. 算出精确积分$\tfrac23$与$N=8,16$的值，读配图说明矩形带符号面积就是取样和。

4. 配图`fig:ipspace-sampled-dot-product`：(a)两函数在四个中点读出的分量，(b)分量乘积形成的矩形与曲线$fg$。

5. 由极限给出$C[a,b]$上的内积（式`eq:ipspace-continuous-inner-product`），线性和共轭对称来自积分的线性。

6. 用连续函数非零点附近有正下界证明正定性。

7. 指出类比失效之处：单点权重趋于零，改动一点不影响积分，离开连续函数后正定性要靠等价类恢复。

8. 说明数列是更直接的无限维向量但点积可能发散，在$c_{00}$上定义内积（式`eq:ipspace-c00-inner-product`），无穷多项非零的情形留给$\ell^2$。

9. 用$[-\pi,\pi]$上的$e^{\mathrm ix}$说明不取共轭时非零函数与自身的“内积”为零，取共轭后为$2\pi$。

10. 定义正交，说明它由乘积积分决定而与曲线交角无关，以$1$与$x$、$1$与$x^2$在$[-1,1]$上和$[0,1]$上的积分说明正交依赖区间。

###### paragraph：Cauchy--Schwarz不等式与诱导范数

1. 说明长度成为范数的关键是三角不等式，它依赖下面的不等式。

2. 用向量在直线上的投影说明不等式的几何来源，并指出证明只用内积公理。

3. 陈述Cauchy--Schwarz不等式及等号条件（定理`thm:ipspace-cauchy-schwarz`）。

4. 证明：取影子系数$\alpha=\langle g,f\rangle/\lVert g\rVert^2$使余量与$g$正交，展开余量长度平方并代入共轭，移项得不等式，再由余量为零讨论等号。

5. 在$[0,1]$上用$f=1$、$g=x$核对不等式、影子系数$\tfrac32$和余量长度平方$\tfrac14$。

6. 定义实空间中函数的夹角，算出$1$与$x$在$[0,1]$上夹角$30^\circ$、在$[-1,1]$上$90^\circ$。

7. 展开$\lVert f+g\rVert^2$并放大交叉项得三角不等式，定义诱导范数，$C[a,b]$上即平方积分大小。

8. 把差拆成两项，由不等式得内积对两个变量连续（式`eq:ipspace-inner-continuity`），说明后文在极限中保持正交都用这一点。

###### paragraph：平行四边形恒等式

1. 由平面几何引出恒等式（式`eq:ipspace-parallelogram`），展开后交叉项抵消完成验证。

2. 用$C[0,1]$一致范数下的$f=1$、$g=x$得左边$5$、右边$4$，说明恒等式不成立。

3. 用$L^1[0,1]$中两半区间指示函数得左边$2$、右边$1$，说明这两个范数都不来自内积。

4. 说明反方向成立，实情形内积由式`eq:ipspace-polarization`给出，证明篇幅较长、指向Jordan--von Neumann定理，本章只用正方向。

### 12.2 Hilbert空间

正文：[02-hilbert-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/02-hilbert-spaces.tex)

1. 说明最佳逼近和无限展开都要取极限，需要完备性。

2. 给出Hilbert空间的定义（定义`def:ipspace-hilbert`）。

3. 说明Hilbert空间即范数来自内积的Banach空间，用一致范数和$L^1$范数说明反向不成立，有内积与完备是两个独立问题。

4. 说明有限维时两个问题合并，无限维要逐个空间证明。

###### paragraph：有限支撑数列

1. 在$c_{00}$上取前$N$项调和式数列$x^{(N)}$，由尾和证明它是柯西列，并读配图(a)。

2. 由坐标不超过范数得坐标收敛，极限只能是$(1/k)$，不在$c_{00}$中，故$c_{00}$不完备。

###### paragraph：连续函数与平方积分

1. 在$C[-1,1]$上取平方积分内积，构造越来越陡的连续斜坡$g_n$，它们趋近$\operatorname{sgn}$。

2. 配图`fig:ipspace-ramp-step`：(a)$x^{(4)}$与$(1/k)$的项，(b)$g_2$、$g_8$与$\operatorname{sgn}$及差的区域。

3. 由差只在长度$2/n$的区间上且不超过$1$，证明$(g_n)$是柯西列。

4. 用反证法说明连续极限在$0$两侧分别恒为$\pm1$，不可能连续。

5. 指出两个例子都缺极限点，与有理数列逼近$\sqrt2$同类，$\ell^2$与$L^2$将把这些极限收进来。

### 12.3 $L^2$空间

正文：[03-l2-space.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/03-l2-space.tex)

1. 承接上一节缺少的极限，指出$L^2$的完备性已由第11章建立，只需定义内积并核对诱导范数。

###### paragraph：$L^2$内积

1. 由$p=q=2$的Hölder不等式保证$\bar fg$可积。

2. 定义$L^2$内积（式`eq:ipspace-l2-inner-product`），说明实情形和复值积分的约定。

3. 说明定义不依赖代表的选择。

###### paragraph：内积公理与诱导范数

1. 由积分线性得线性和共轭对称，正定性为零当且仅当几乎处处为零。

2. 说明等价类使正定性成立，它承认了单点没有权重。

3. 核对诱导范数就是$L^2$范数，引用第11章的完备性。

4. 陈述$L^2$是Hilbert空间（定理`thm:ipspace-l2-hilbert`）。

5. 计算$\lVert g_n-\operatorname{sgn}\rVert_2^2=2/(3n)$，斜坡列在$L^2$中收敛到$\operatorname{sgn}$。

###### paragraph：$\ell^2$空间

1. 取计数测度得$\ell^2$（式`eq:ipspace-ell2`），说明它是字面意义的无限维向量空间，由Hölder不等式和定理得Hilbert空间。

2. 说明$c_{00}$是其子空间、柯西列在其中收敛，有限维$\mathbb K^d$是特例。

3. 对比$\ell^2$与$L^2[-1,1]$：离散下标有权重、可读坐标，而$L^2$单点无权重、不能读点值。

###### paragraph：$L^2$中的正交

1. 读配图对照正负面积抵消与非负面积，由对称性说明偶函数与奇函数正交。

2. 配图`fig:ipspace-integral-orthogonality`：(a)$1\cdot x$带符号面积$\pm\tfrac12$，(b)$1\cdot x^2$面积$\tfrac23$。

3. 计算复指数的内积，$j=k$时为$2\pi$，$j\neq k$时由原函数周期性为零。

4. 得到$\{e^{\mathrm ikx}/\sqrt{2\pi}\}$两两正交且单位长度，其完备性留给第14章。

### 12.4 正交投影

正文：[04-orthogonal-projection.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/04-orthogonal-projection.tex)

1. 由章首问题推广到一般子空间，回顾$\mathbb R^3$点到平面的垂足。

2. 说明有限维靠闭球紧性得最近点，无限维闭球不紧，要用平行四边形恒等式、完备性和闭性替代。

###### paragraph：正交补

1. 定义正交补（式`eq:ipspace-orthogonal-complement`），以水平面和竖直线举例。

2. 由内积的线性与连续性证明$M^\perp$是闭线性子空间。

###### paragraph：最佳逼近的存在与唯一

1. 定义$f$到$M$的距离$d$（式`eq:ipspace-distance`），指出下确界能否取到是问题所在。

2. 陈述闭子空间上的最佳逼近定理（定理`thm:ipspace-best-approximation`）。

3. 说明证明想法，读配图中的平行四边形和短弦。

4. 配图`fig:ipspace-minimizing-sequence`：(a)以$f-m_j$、$f-m_k$为邻边的平行四边形及其对角线，(b)球截$M$所得短弦，半弦长$\sqrt\varepsilon$。

5. 证明分三步：平行四边形恒等式给出$\lVert m_j-m_k\rVert^2<2/j+2/k$，完备性和闭性给出极限，交替序列给出唯一性。

6. 说明平行四边形恒等式的作用，用$\mathbb R^2$最大值范数下最近点不唯一的例子说明它依赖内积。

7. 说明完备性和闭性的分工，并指出实际只需$M$自身完备。

###### paragraph：误差正交与正交投影

1. 引出用误差垂直刻画最近点。

2. 陈述正交刻画与勾股关系（定理`thm:ipspace-orthogonality-characterization`、式`eq:ipspace-pythagoras`）。

3. 证明：把$m_*+tm$代入并取$t=s\bar a$令$s\to0$得$r\perp M$；反向由勾股关系得最近性。

4. 解释勾股定理的直角三角形含义，它定量给出其他候选多出的误差。

5. 配图`fig:ipspace-projection-geometry`：平面$M$、垂足$P_Mf$、误差与另一点$m$构成直角三角形。

6. 由存在唯一性定义正交投影（定义`def:ipspace-orthogonal-projection`，式`eq:ipspace-projection`）。

###### paragraph：正交分解

1. 写出正交分解（式`eq:ipspace-orthogonal-decomposition`），类比水平与竖直分量。

2. 由同属$M$与$M^\perp$的元素只能为零证明唯一性，记为$H=M\oplus M^\perp$。

3. 由勾股定理得$\lVert P_Mf\rVert\leq\lVert f\rVert$。

4. 由正交刻画读出$P_M$的线性，作为算子的研究留给第17章。

###### paragraph：向常数投影

1. 由误差与$1$正交解出最佳常数是平均值（式`eq:ipspace-constant-projection`）。

2. 对$x^2$得投影$\tfrac13$，读配图(a)，计算距离平方$\tfrac8{45}$。

3. 由勾股关系写出任意常数的误差平方$\tfrac8{45}+2(c-\tfrac13)^2$，用$c=0$核对为$\tfrac25$。

4. 配图`fig:ipspace-constant-projection`：(a)$x^2$、投影和误差区域，(b)误差平方关于$c$的抛物线。

###### paragraph：闭性不能去掉

1. 在$\ell^2$中取$M=c_{00}$、$f=(1/k)$，由截断得距离为零。

2. 若取到下确界则$f\in c_{00}$，矛盾，最近点不存在。

###### paragraph：完备性不能去掉

1. 在$H=c_{00}$中取$M=\ker\langle a,\cdot\rangle$（$a=(1/k)$），由Cauchy--Schwarz不等式知$M$闭，提出$e_1$没有最近点。

2. 在$\ell^2$的闭子空间$N$上算出投影$p=e_1-a/\lVert a\rVert^2$，它有无穷多项非零，不在$c_{00}$中。

3. 证明$M$在$N$中稠密，距离相同，由$N$中的唯一性得矛盾。

###### paragraph：与一般闭凸集的分工

1. 指出存在唯一性的证明只用到中点和闭性，可搬到非空闭凸集。

2. 指出正交刻画用到线性子空间，闭凸集要换成变分不等式，投影也非线性，指向卷五。

### 12.5 正交基

正文：[05-orthonormal-bases.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/05-orthonormal-bases.tex)

1. 说明代数基只允许有限组合，改为要求有限组合以任意精度逼近。

###### paragraph：标准正交系

1. 把“两两垂直、长度为$1$”搬过来。

2. 给出标准正交系的定义（定义`def:ipspace-orthonormal-system`）。

3. 证明线性无关，以$\ell^2$单位列和复指数为例。

###### paragraph：Gram--Schmidt正交化

1. 给出正交化公式（式`eq:ipspace-gram-schmidt`）。

2. 验证$v_k$与之前方向正交、非零以及张成不变，每步只涉及有限维。

3. 对$1$和$x$归一化得$e_0,e_1$。

4. 处理$x^2$，余量是向常数投影的误差，得$e_2$。

5. 处理$x^3$，只减$e_1$方向分量，算出长度平方$\tfrac8{175}$，得$e_3$。

6. 说明这些是归一化Legendre多项式，读配图对比正交化前后。

7. 配图`fig:ipspace-legendre-gram-schmidt`：(a)单项式，(b)$e_0,\ldots,e_3$。

###### paragraph：完备正交系

1. 引出闭线性张成。

2. 给出完备正交系的定义（定义`def:ipspace-complete-orthonormal-system`）。

3. 区分“完备”的两种含义，引用对比表。

4. 表`tab:ipspace-basis-compare`：对比代数基和正交基的表示方式、依赖结构、坐标计算和无限维中的可得性。

5. 证明$\ell^2$单位列完备，用$(1/k)$说明它不是代数基。

###### paragraph：完备性的正交判据

1. 说明直接验证闭包难，有限维中可看是否遗漏方向。

2. 陈述判据（定理`thm:ipspace-completeness-criterion`）。

3. 证明：必要方向用连续性，充分方向用正交投影。

4. 概括两个方向用到的结构。

5. 用偶次Legendre多项式遗漏奇函数说明无穷多方向也可能不够。

6. 说明全体Legendre多项式的完备性来自第20章的两个逼近结论。

7. 把两个结论结合，用$\lVert g-p\rVert_2\leq\sqrt2\sup\lvert g-p\rvert$证明多项式在$L^2$中稠密。

###### paragraph：可分空间的可数正交基

1. 引入可分，说明它与有可数正交基等价。

2. 陈述定理（定理`thm:ipspace-separable-basis`）。

3. 证明：由稠密集筛选并正交化得可数基；由单位正交元两两距离$\sqrt2$与开球不交得可数性。

4. 证明反方向，得$\ell^2$与$L^2[-1,1]$可分。

5. 以实数集上可数支撑平方可和函数为例说明不可分空间存在，本章只处理可数情形。

### 12.6 正交展开

正文：[06-orthogonal-expansions.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/06-orthogonal-expansions.tex)

1. 回到级数的三个问题，说明用范数收敛回答。

2. 固定$H$和可数正交系，定义系数（式`eq:ipspace-coefficients`），类比坐标。

###### paragraph：有限截断是正交投影

1. 限制到有限维子空间$M_n$。

2. 陈述有限截断定理（定理`thm:ipspace-finite-truncation`、式`eq:ipspace-truncation-error`）。

3. 证明：误差与各基元素正交，由勾股定理得误差公式。

4. 说明系数是最佳选择，新增方向不改旧系数。

5. 用$L^2[0,1]$上$\{1,x\}$逼近$x^2$的Gram方程组（$a=-\tfrac16$，$b=1$）说明不正交时系数要全部重算。

###### paragraph：Bessel不等式

1. 由式`eq:ipspace-truncation-error`非负取极限。

2. 陈述Bessel不等式（定理`thm:ipspace-bessel`）。

3. 解释几何含义，得$c_j\to0$，指出不要求完备。

###### paragraph：级数的收敛与和

1. 说明平方可和系数给出收敛级数，和为投影。

2. 陈述正交展开定理（定理`thm:ipspace-orthogonal-expansion`、式`eq:ipspace-series-norm`）。

3. 证明：部分和差的范数平方等于系数尾和；和$s$与每个$e_k$的误差正交，故$s=P_Mf$。

4. 指出“当”方向需要完备，举$c_{00}$反例。

5. 说明系数唯一和求和次序无关。

###### paragraph：完备正交系：展开与Parseval等式

1. 由$M=H$引出。

2. 陈述Parseval等式（定理`thm:ipspace-parseval`，式`eq:ipspace-parseval-expansion`至`eq:ipspace-parseval-inner`）。

3. 证明展开、范数等式和内积等式。

4. 用$x^2$的两个Legendre系数核对$\tfrac29+\tfrac8{45}=\tfrac25$。

5. 说明取系数映射把$H$同构到$\ell^2$，回到无限维向量的类比。

6. 说明这与有限维同构同类，但坐标是基的系数而非函数值。

7. 写出尾和形式的截断误差（式`eq:ipspace-tail-error`）。

###### paragraph：不完备时只恢复闭张成中的部分

1. 说明展开和为$P_Mf$，Bessel的差是丢失能量。

2. 用偶部奇部分解得$P_Ef$是偶部。

3. 证明偶次Legendre多项式的闭张成恰为偶函数子空间。

4. 取$e^x$，投影$\cosh x$，丢失$\sinh x$，能量约$0.813$。

5. 配图`fig:ipspace-even-odd-projection`：$e^x$、$\cosh x$、$\sinh x$。

###### paragraph：截断误差的例子

1. 引入$\operatorname{sgn}$的Legendre展开，奇次系数、能量为$2$。

2. 手算$c_1^2=\tfrac32$、$c_3^2=\tfrac7{32}$，给出$c_5^2=\tfrac{11}{128}$。

3. 由误差公式逐项算出$0.5$、$0.28125$、约$0.195$。

4. 读配图比较$\operatorname{sgn}$与$\lvert x\rvert$的误差数值，说明一般关系归第20章。

5. 配图`fig:ipspace-legendre-truncation`：(a)部分和$s_1,s_5,s_{15}$，(b)两函数的截断误差。

###### paragraph：范数收敛不是点态收敛

1. 由一致极限连续说明部分和不一致收敛到$\operatorname{sgn}$。

2. 说明$\operatorname{sgn}$在$0$处没有确定的值，指出坐标是系数而非函数值，类比再次失效。

3. 说明点态收敛要有点值并受范数控制，指向后续各章。

### 12.7 本章小结

正文：[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/03-inner-product-spaces/07-summary.tex)

1. 回应章首问题，说明正交几何逐条保留。

2. 表`tab:ipspace-summary`：对照有限维向量与Hilbert空间的内积、完备性、最近点、投影、基、坐标、勾股定理和“够不够”的判断。

3. 总结内积公理、Cauchy--Schwarz不等式和平行四边形恒等式。

4. 总结Hilbert空间、不完备例子及$L^2$与$\ell^2$。

5. 总结闭子空间上的最近点及其三个条件的分工、正交投影与反例。

6. 总结完备正交系、判据、可分性和正交展开，以及点态收敛的边界。

7. 指出这些结构为第16、14、15、20章提供依据。

## 第13章 函数类的有限覆盖

正文入口：[04-function-class-covers.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers.tex)，章内依次输入[01-finite-cover-problem.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/01-finite-cover-problem.tex)、[02-arzela-ascoli.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/02-arzela-ascoli.tex)、[03-cover-construction.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/03-cover-construction.tex)、[04-finite-representations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/04-finite-representations.tex)、[05-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/05-summary.tex)。

章职责与主线：本章沿用第10章把函数看作无限维向量的类比，研究能否用同一份有限代表表在给定精度内覆盖一类函数，以及需要多少代表。主线是把无穷多个坐标压缩成有限个有效坐标：先用覆盖数表述问题并以立方体计数作参照，说明只限制范数不够；取值列路线用Arzelà–Ascoli判据回答能否覆盖，再在$[0,1]^d$的Lipschitz类上用网格量化给出度量熵上下界；系数列路线由有限维统一逼近构造覆盖。全章只给确定性结论，有限表示的构造留给第20章。

1. 第一段以预先造一张有限函数表、使类中每个函数都能查到最大误差不超过$0.1$的一行进入，提出是否存在、需要多少行的问题。

2. 第二段回用第10章的类比，把函数表看作有限个向量、查表看作找最近的向量，指出有限维立方体的方块数是每坐标取值数的$n$次方，坐标数趋于无穷时这个数也趋于无穷。

3. 第三段把问题改写为怎样的共同限制能把无穷多个坐标压缩成有限个，并给出两条路线：取值列上相邻坐标互相牵制，系数列上靠后的坐标足够小。

4. 第四段依次说明四节的分工，并划定本章只作确定性计数，有限表示的构造留给第20章。

### 13.1 有限覆盖问题

正文：[01-finite-cover-problem.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/01-finite-cover-problem.tex)

1. 指出函数表问题的三个要素是函数类、误差距离与精度，并说明本节依次写成覆盖数、以立方体作参照、比较两种要求、说明范数界不够。

###### paragraph：函数类与覆盖数

1. 引入函数类$\mathcal F$及其所在的度量空间$(E,\rho)$，单列一致距离与$L^1$距离两种误差标准，说明它们分别用于$C(K)$与$L^1[0,1]$。

2. 把表的一行解释为$E$中的函数，表能服务整类即每个成员落在某行的闭球内，并写出第2章覆盖数的定义式`eq:fcover-covering-number`，无有限覆盖时记为无穷。

3. 引入度量熵，用$N=1024$需要$10$位的例子说明度量熵是在精度$\varepsilon$下识别成员所需的信息量。

4. 区分行可取类外函数与行必须是类中成员两种约定，写出第2章的不等式`eq:fcover-center-change`。

5. 重述右侧不等式的机制：删去不与类相交的球、在余下的球中以成员替换中心，用三角不等式单列半径翻倍的估计，说明更换中心不增加行数。

###### paragraph：从立方体到函数

1. 在$\mathbb R^n$中单列最大分量距离，说明它是一致距离在有限下标上的版本，半径$\varepsilon$的闭球是边长$2\varepsilon$的小立方体。

2. 为覆盖$[-M,M]^n$在每个坐标上取刻度$c_k=-M+(2k-1)\varepsilon$，说明相邻小区间首尾相接、每个坐标都能选到误差不超过$\varepsilon$的刻度。

3. 由刻度任意搭配得式`eq:fcover-cube`的上界$\lceil M/\varepsilon\rceil^n$，指出度量熵的结构是坐标个数乘以每坐标信息量，这一结构贯穿全章。

4. 用$n=3$、$M=1$、$\varepsilon=1/4$的例子手算：$T=4$，至多$64$个中心，向量$(0.3,-0.6,0.9)$的最近搭配及三个坐标误差。

5. 把一致距离的闭球写成函数图像周围的管道，对应小立方体在无穷多个坐标上的样子。

6. 配图`fig:fcover-cube-tube`：(a)六个坐标上代表$g$的取值方框与成员$f$的点，(b)同一对函数的曲线与管道，以及局部越出管道的$h$。

7. 解释图：一致距离只看最坏坐标，一小段越出管道即不在球内。

8. 指出式`eq:fcover-cube`的右端随$n$趋于无穷，不能直接套用，真正的问题是无穷多个坐标能否只用有限个决定到精度$\varepsilon$。

###### paragraph：挑选近似与统一精度

1. 对单个$f\in C[0,1]$，由一致连续取$m$并连接节点值得到折线。

2. 把$f(x)-g(x)$写成两端差的凸组合，单列这一表示，得到误差不超过$\varepsilon$。

3. 指出近似由$m+1$个数决定但$m$依赖$f$，并单列“对每个$f$存在有限描述”与“存在有限集对每个$f$有近邻”两种量词次序。

4. 说明前者对$C[0,1]$总成立，有限类可列全部成员，困难出在所需节点数随成员无界的无限类。

###### paragraph：距离的选择

1. 用两个向量只在一个坐标相差$1$时最大分量差与平均分量差的对比，引入距离选择的影响。

2. 取指示函数族，单列$L^1$距离等于$\lvert t-s\rvert$，说明它就是图中矩形的面积，覆盖$\mathcal F$等同于覆盖参数区间。

3. 配图`fig:fcover-indicator-distances`：(a)$\mathbf 1_{[0,0.3]}$与$\mathbf 1_{[0,0.7]}$，(b)差的绝对值，面积$0.4$对应$L^1$距离，高度$1$对应一致距离。

4. 取中点$t_j$得到$N_{\mathcal F}(\varepsilon,\mathcal F)\leq\lceil1/(2\varepsilon)\rceil$，用$\varepsilon=0.1$的五个中心和成员$\mathbf 1_{[0,0.62]}$手算验证。

5. 改用一致距离：两两距离为$1$，半径小于$1/2$的闭球至多含一个成员，成员不可数，覆盖数为无穷。

6. 总结积分距离允许误差集中在小测度集上而一致距离不允许，这是两种答案的分界。

###### paragraph：范数界不能保证有限覆盖

1. 把范数上界读作把每个坐标限制在$[-M,M]$，回用第10章由Riesz引理得到的两两距离至少$1/2$的单位向量列。

2. 由此推出半径小于$1/4$的闭球不能有限覆盖闭单位球，并按比例推广到半径$R$的闭球。

3. 回用第10章的鼓包$\varphi_n$，单列$\lVert\varphi_n-\varphi_l\rVert_\infty=1$，说明它们在闭单位球内却没有半径小于$1/2$的有限覆盖。

4. 配图`fig:fcover-tents-on-grid`：(a)鼓包$\varphi_1$至$\varphi_{14}$与节点$j/8$，(b)放大$[0,1/8]$，$n\geq8$的鼓包在节点上全为$0$。

5. 由图说明失败原因：$n\geq m$时鼓包支撑落在$[0,1/m]$内，节点上全为零，与零函数记录相同而一致距离为$1$。

6. 指出斜率$2n(n+1)$无界，并用向量语言说明每个鼓包像标准单位向量$e_n$一样占据自己的坐标，彼此没有牵制。

7. 预告两个补救方向：13.2要求共同的连续性尺度，让相邻坐标互相牵制；13.4要求全类贴近同一有限维子空间，让靠后的坐标足够小。

### 13.2 Arzelà–Ascoli判据

正文：[02-arzela-ascoli.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/02-arzela-ascoli.tex)

1. 承接鼓包例子陈述本节判据的内容，并固定$C(K)$为实值或复值连续函数配一致距离。

###### paragraph：一致有界与等度连续

1. 用向量语言说明类中函数需要在幅度与变化两方面共同受限，引出幅度约束；紧接定义`def:fcover-uniformly-bounded`（一致有界）。

2. 指出一致有界即含于一致范数球，相当于把所有坐标限制在同一区间，回到鼓包说明仅此不够。

3. 回用第3章的等度连续及紧定义域上半径可与位置无关的结论，写出统一形式`eq:fcover-uniform-equicontinuity`。

4. 用向量语言解释该式：下标相近的坐标取值也相近，尺度对全类相同，知道一个坐标附近就大致确定。

5. 说明共同Lipschitz常数给出最常见的等度连续族，取$\delta=\varepsilon/L$。

6. 记鼓包峰值点$c_n$与半宽$w_n$，单列$\lvert\varphi_n(c_n)-\varphi_n(c_n+w_n)\rvert=1$，证明鼓包族不等度连续，并回指$x^n$在$1$处同样如此。

###### paragraph：判据与证明

1. 回忆$C(K)$完备和完备空间中相对紧等价于全有界这两件事；紧接定理`thm:fcover-arzela-ascoli`。

2. 概述证明核心是有限化：有限个位置加有限个取值块只留下有限种记录，把无穷多个坐标压缩成有限个。

3. 设定手算例子：$K=[0,1]$，$L=M=1$的Lipschitz类，五个位置和四个取值块，记录是各位置函数值所在的块号。

4. 配图`fig:fcover-finite-record`：$f(x)=x^2/2-1/4$与$g(x)=x/2-0.35$在五个位置上落在相同的块，记录都是$(2,2,2,3,3)$。

5. 由三角不等式单列记录相同的两个成员差不超过$1/8+1/2+1/8=3/4$，说明三项的来源。

6. 由至多$4^5=1024$种记录得到半径$3/4$的有限覆盖，并比较图中实际差$1/10$，引出一般证明。

7. 证明由1推出2：取$\delta$对应$\varepsilon/4$并在紧空间取有限点。

8. 把取值集合分成直径不超过$\varepsilon/4$的有限小块，实值用区间，复值用正方形。

9. 定义$f$的记录，记录种数有限，每种实际出现的记录取一个成员作代表。

10. 用三角不等式单列证明同记录成员差小于$3\varepsilon/4$，得到有限的$\varepsilon$覆盖。

11. 由2推出1的一致有界部分：取有限$1$覆盖，单列范数上界。

12. 由2推出1的等度连续部分：取$\varepsilon/3$覆盖，有限个函数共用一个$\delta$。

13. 用三角不等式单列$\lvert f(x)-f(y)\rvert<\varepsilon$，完成等度连续的证明。

14. 2与3等价由$C(K)$完备及相对紧判据得到。

15. 紧性部分：紧蕴含闭，相对紧且闭则等于闭包。

16. 解释充分性构造可以计数，结构与式`eq:fcover-cube`相同，坐标个数换成位置数$p$。

17. 解释必要性：有限个函数共用一个$\delta$，一致距离把它传给全类。

###### paragraph：相对紧性与闭性

1. 指出定理末句把紧性分成闭包紧与闭性两部分，以下各举一例。

2. $\mathcal F_{L,M}$的两个不等式在一致极限下保持，因而闭，从而紧。

3. 考察$\lvert f\rvert\leq1$、$\lvert f'\rvert\leq1$的连续可微函数类，由中值定理知其相对紧，并单列函数列$g_n$。

4. 核对$g_n$属于该类，分子有理化单列$g_n$与折线的差不超过$1/n$。

5. 得出$g_n$一致收敛到不可导的$\lvert x-1/2\rvert$，这一类闭包紧而自身不紧。

6. 配图`fig:fcover-closure-translate`：(a)$g_n$（$n=2,4,10$）收敛到$\lvert x-1/2\rvert$，(b)$\mathbb R$上的平移族。

###### paragraph：定义域紧性的作用

1. 回到证明中用有限点控制定义域这一步，用坐标语言说明紧定义域保证只有有限片彼此远离的下标区域。

2. 在$\mathbb R$上取平移族$\varphi_n(x)=\varphi(x-3n)$。

3. 全族一致有界且共用Lipschitz常数，但两两一致距离为$1$，半径小于$1/2$的闭球至多含一个成员，覆盖数为无穷。

4. 由图说明相邻坐标的牵制只在同一片区域内部起作用，管不到无穷远处。

### 13.3 有限覆盖的构造

正文：[03-cover-construction.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/03-cover-construction.tex)

1. 说明判据只回答存在，引出$[0,1]^d$上的Lipschitz类$\mathcal F^d_{L,M}$（式`eq:fcover-lipschitz-class`），并给出欧氏Lipschitz常数的换算。

2. 把总误差$\varepsilon$拆成位置离散化与取值量化两份预算，Lipschitz界控制前者，幅值界决定后者的刻度数。

#### 13.3.1 网格误差与取值误差

###### paragraph：网格与多线性插值

1. 定义网格$G_m$，说明需要把节点值连续地填满每个单元，一维连折线，高维逐坐标推广。

2. 定义局部坐标与多线性插值`eq:fcover-multilinear`，解释权重是一维折线权重的乘积，$d=1$时就是折线。

3. 用$d=2$的单元手算，$t=(1/4,1/2)$，单列四个权重。

4. 代入顶点值$1,3,2,6$得$9/4$，并用先沿上下边、再沿竖直方向的两步插值验证。

5. 配图`fig:fcover-multilinear-snake`：(a)单元顶点值、权重与插值点，(b)$m=2$、$d=2$的蛇形次序。

6. 第一条性质：权重非负且逐坐标相乘后总和为$1$，所以$(Ia)(x)$是顶点值的凸组合。

7. 第二、三条性质：节点上取值$a$，公共面上两侧公式一致，$Ia$连续。

###### paragraph：两类误差的分别控制

1. 引入节点值与$\eta$，令$T=\lceil M/\eta\rceil$，写刻度式`eq:fcover-levels`，说明量化使每个节点只剩$T$种可能。

2. 以$Iq_f$作代表，用三角不等式把误差分成网格误差与取值误差，两项各只与一种预算有关。

3. 网格误差：由单元内顶点距离不超过$1/m$和凸组合性质，单列估计$L/m$。

4. 取值误差：由权重和为$1$单列对节点值的稳定性，节点值差不超过$\eta$。紧接定理`thm:fcover-grid-cover`（含`eq:fcover-grid-general`、`eq:fcover-grid-bound`）及其证明：计数全部量化节点值，并代入$m=\lceil2L/\varepsilon\rceil$、$\eta=\varepsilon/2$。

5. 设定手算例子：$d=1$、$L=M=1$、$\varepsilon=1/2$，得$m=4$、$\eta=1/4$、$T=4$，四个刻度，上界$4^5=1024$。

6. 取$f(x)=x^2/2-1/4$，单列五个节点的函数值和量化结果，每个节点的量化误差不超过$\eta$。

7. 配图`fig:fcover-grid-quantize`：(a)Lipschitz常数$1$允许的菱形范围，(b)刻度、节点量化与代表$Iq_f$。

8. 解释图：菱形说明节点间摆动不超过$L/m$，红线说明量化误差不超过$\eta$。

9. 分三段算出$f-Iq_f$，单列最终实际误差$7/32\leq1/2$。

###### paragraph：代表取在类外

1. 说明代表未必属于类，手算例子中$Iq_f$在$[1/2,3/4]$上斜率为$2$，超过$L=1$。

2. 由式`eq:fcover-center-change`单列类内中心的换算，说明做法是以$\varepsilon/2$运行构造再替换中心，代价是精度减半。

3. $d=1$、$L=M=1$、$\varepsilon=0.1$的细精度比较：$20^{21}$与$\ln N\leq62.9$；类内中心时$40^{41}$与$\ln N\leq151.2$。

#### 13.3.2 覆盖数的维数依赖

###### paragraph：上界中的四个量

1. 取对数得式`eq:fcover-entropy-bound`，指出结构与立方体式相同，第一个因子是节点数，第二个因子是每节点信息量。

2. 分别说明维数、$L$、$M$、$\varepsilon$的位置：维数在指数上，$L$按$(L/\varepsilon)^d$起作用，$M$只在对数中，$\varepsilon$同时进入两处。

3. 类比$\mathbb R^n$中坐标数固定、度量熵按$n\log(1/\varepsilon)$增长，说明节点数随精度增长反映Lipschitz类无限维，并引出数值表。

4. 表`tab:fcover-dimension`：$L=M=1$、$\varepsilon=0.1$时节点数$21^d$、刻度数$20$、度量熵上界随$d=1,2,3$的变化。

###### paragraph：利用相邻位置的约束

1. 指出式`eq:fcover-entropy-bound`把节点当作互相独立的坐标，而Lipschitz条件牵制相邻节点，乘积计数数多了，类比在这里要修正。

2. 用逐层往返的方式构造蛇形次序，相邻两项只在一个坐标上相差$1/m$，并指向`fig:fcover-multilinear-snake`(b)。

3. 取$m=\lceil2L/\varepsilon\rceil$、$\eta=\varepsilon/2$，单列相邻量化值差不超过$3\eta$，由刻度差是$2\eta$的整数倍得只能是$-2\eta$、$0$、$2\eta$。

4. 由首项加$n-1$个“降、平、升”选择计数得式`eq:fcover-entropy-improved`，主项不再含$\log(M/\varepsilon)$因子。

5. 手算例子的相邻变化是“平、平、升、平”，比较$4\cdot3^4=324$与独立计数的$1024$；$\varepsilon=0.1$时上界从$62.9$降到$\ln20+20\ln3\approx25.0$。

###### paragraph：打包下界

1. 回用打包思路：两两距离大于$2\varepsilon$的一组成员使覆盖数不小于其个数，每个单元的符号是一个可自由选择的坐标。

2. 在$L\geq6\varepsilon$、$\varepsilon\leq M/3$下取$k=\lfloor L/(3\varepsilon)\rfloor$与单元$Q$，单列隆起$\varphi_Q$，定义$g_s=\sum_Qs_Q\varphi_Q$。

3. 核对幅度：单列高度$Lh/2\leq3\varepsilon\leq M$。

4. 核对Lipschitz界：沿线段把$[x,y]$按单元切段，逐段累加。

5. 配图`fig:fcover-bump-packing`：$d=1$、$L=1$、$k=4$时的两个符号选择，在第三格中心相差$Lh=1/4$。

6. 距离：符号不同的单元中心处差为$Lh\geq3\varepsilon>2\varepsilon$。

7. 由两两分离得下界式`eq:fcover-packing-lower`。

8. 代入$L=M=1$、$d=1$、$\varepsilon=1/12$手算：$k=4$，$16$个函数，两两距离至少$1/4$，$N\geq16$。

###### paragraph：上界与最优阶

1. 结合上下界得固定$L,M,d$时度量熵的增长阶为$\varepsilon^{-d}$，幅值只影响低阶对数项，并引Kolmogorov与Tikhomirov的系统结果。

2. 总结：网格量化给出可核验的上界，判断最优阶还需利用位置间约束和打包下界。

### 13.4 由有限表示构造覆盖

正文：[04-finite-representations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/04-finite-representations.tex)

1. 回用第10章的两种“一列数”，说明上一节截取取值列，本节截取系数列，覆盖分为先进入有限维子空间、再覆盖有限维有界集两步。

###### paragraph：统一逼近与有限维球

1. 回用第2章$n$维实赋范空间闭球的覆盖界，指出它是立方体计数的一般形式；紧接定理`thm:fcover-finite-dimensional`（式`eq:fcover-uniform-approximation`、`eq:fcover-finite-dimensional`）及证明：处理$\varepsilon_1>R$的情形，再由三角不等式得$(\varepsilon_0+\varepsilon_1)$覆盖。

2. 配图`fig:fcover-two-step`：子空间$V$中的闭球与$\varepsilon_1$网，$f$先到$g_f$再到最近网点$v_j$。

3. 解释图与两个前提：$\varepsilon_0$要求同一$V$对整类有效，$R$限定近似所在的有界区域。

4. 取对数得度量熵按$n\log(1/\varepsilon_1)$增长，$n$取代节点数；复子空间的实维数是$2n$。

###### paragraph：范数界与系数界

1. 说明范数界$R$几乎自动，但实际量化的是系数，需要系数一致有界。

2. 设$\lvert\theta_i\rvert\leq\beta$、$\Lambda=\sup_x\sum_i\lvert\varphi_i(x)\rvert$，单列$\lVert g_\theta-g_{\theta'}\rVert_\infty\leq\Lambda\max_i\lvert\theta_i-\theta_i'\rvert$，由刻度取法得代表数$\lceil\beta\Lambda/\varepsilon_1\rceil^n$。

3. 用斜坐标系类比说明基接近退化时坐标会很大，取$\varphi_1=1$、$\varphi_2=1+\delta x$并单列$x=(\varphi_2-\varphi_1)/\delta$。

4. 取$\delta=0.01$、$\varepsilon_1=0.1$手算：刻度数$2010$与基$(1,x)$下的$20$。

5. 总结按系数量化必须核对系数的一致上界，不能只看函数的范数。

###### paragraph：正弦级数类的例子

1. 定义函数类`eq:fcover-sine-class`，说明级数一致收敛，权重条件让靠后的系数整体变小。

2. 取$V_n$与部分和，单列尾项不超过$1/n$，部分和范数不超过$1$。

3. 用具体成员$\tfrac12\sin(\pi x)+\tfrac16\sin(3\pi x)$核对：$n=2$时误差$1/6\leq1/2$。

4. 代入定理得度量熵上界`eq:fcover-sine-entropy`，并算$\varepsilon=1/2$时$4\ln9$与$\varepsilon=0.1$时$20\ln41$。

5. 指出与一维Lipschitz类同为$\varepsilon^{-1}\log(1/\varepsilon)$，并由逐项求导说明$\mathcal F$含于Lipschitz类，引出两条路线的对比表。

6. 表`tab:fcover-two-lists`：取值列与系数列在下标、约束、有效坐标数、每坐标的编码与度量熵上界上的对比。

###### paragraph：从多个子空间中选择

1. 允许从$J$个候选子空间中选择时取并集，得式`eq:fcover-many-subspaces`。

2. 说明选择的自由用$\log J$支付，用$D=100$、$n=5$算$\ln J\approx18.1$与上界$n\ln D\approx23.0$。

3. 候选子空间为连续参数族时$J$无穷，并集论证失效，需另行覆盖参数；有限表示的构造是第20章的问题。

### 13.5 本章小结

正文：[05-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/04-function-class-covers/05-summary.tex)

1. 回顾能否造表与需要多少行的问题，以及两种中心约定只差把精度减半。

2. 回顾答案依赖距离和量词次序，用指示函数与单个函数近似说明。

3. 概括全章线索：度量熵等于有效坐标数乘每坐标信息量，并指出类比的边界是函数的坐标并不独立。

4. 取值列路线：Arzelà–Ascoli判据及其三个条件的作用，紧定义域不可省略。

5. 网格量化的计数：两类误差、上界改进和打包下界，增长阶为$\varepsilon^{-d}$。

6. 系数列路线：有限维统一逼近的度量熵上界，核对系数界，选择子空间要付$\log J$。

7. 强调结论是确定性的，并衔接下一章的频率表示和第20章的有限表示构造。

## 第14章 Fourier变换

正文入口：[05-fourier-transform.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform.tex)，章内依次输入[01-fourier-series.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/01-fourier-series.tex)、[02-l1-transform.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/02-l1-transform.tex)、[03-l2-transform.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/03-l2-transform.tex)、[04-operations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/04-operations.tex)、[05-discrete-representations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/05-discrete-representations.tex)、[06-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/06-summary.tex)。

章职责与主线：本章沿用第10章“函数是无限维向量”的类比，把Fourier系数讲成函数在复指数这组正交基下的坐标，并逐一核对这组坐标对哪些函数有意义、在什么意义下能还原、运算规则何时成立。先在周期区间上建立Fourier级数，以Fejér核证明完备性，再分别核对点态与一致收敛；随后下标连成整个$\mathbb R^d$，在$L^1$上定义变换、单独研究反演，再用稠密延拓推广到$L^2$，得到保持长度与内积的双射；然后把平移、缩放、微分、卷积看作频率坐标下的对角运算并核对条件；最后回到有限维的离散变换，比较三种表示及其转换。类比在每处都说明失效之处。归一化固定为周期$2\pi$与指数$e^{-2\pi\mathrm ix\cdot\xi}$，截断误差留给第20章。

1. 章首第一段回用第10章的坐标观点，指出有限维中好的基使矩阵对角，函数空间中这样的基是复指数，Fourier系数是其下的坐标。

2. 第二段说明平移、求导、卷积在频率坐标下成为对角作用，并提出三个问题：这组坐标对哪些函数有意义、在什么意义下能还原、规则何时成立。

3. 第三段说明前两节：14.1在周期函数上读坐标、证明完备并核对逐点与一致收敛；14.2下标连成实轴，在可积函数上定义变换并单独回答反演。

4. 第四段由能量关系属于$L^2$引出14.3的稠密延拓，说明14.4推导四类运算规则，14.5回到有限维向量比较三种表示。

5. 第五段固定全章归一化，并划定范围：截断误差在第20章，尺度与位置的局部表示在第15章。

### 14.1 Fourier级数

正文：[01-fourier-series.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/01-fourier-series.tex)

1. 回顾$\mathbb R^n$中标准正交基的坐标、展开与长度公式，说明第12章已把它搬到Hilbert空间，本节用于周期函数，基取复指数，坐标记录第$k$次振荡的强弱。

2. 预告先建立$L^2$展开，再问逐点与一致收敛，后两者需要正交性之外的条件。

#### 14.1.1 $L^2$中的Fourier展开

###### paragraph：周期函数与归一化内积

1. 把$2\pi$周期函数看作端点相粘的周期区间$\mathbb T$上的函数，回用第12章说明$L^2(\mathbb T)$由等价类组成且是Hilbert空间。

2. 沿用第12章对第二变量线性的约定，用式`eq:fourier-circle-inner-product`定义带因子$1/(2\pi)$的内积，并写出相应的范数与归一化$L^1$范数。

3. 记$e_k=e^{\mathrm ikx}$，分$k=j$与$k\neq j$直接积分验证标准正交，说明这是整数圈旋转正负抵消的结果。

###### paragraph：Fourier系数与部分和

1. 说明有标准正交系后，第$k$个坐标就是与$e_k$的内积，引出定义。

2. 定义`def:fourier-coefficients`：用式`eq:fourier-coefficient`给出Fourier系数，并给出Fourier级数与对称部分和式`eq:fourier-partial-sum`。

3. 指出$L^2$中系数即$\langle e_k,f\rangle$，可积即可定义且模不超过$\lVert f\rVert_1$，一个周期长度有限使$L^2(\mathbb T)\subseteq L^1(\mathbb T)$。

4. 说明函数因此对应一列坐标，并引出方波例子。

5. 例`ex:fourier-square-wave`开始：取奇的方波，指出在间断点的取值暂不规定。

6. 由奇性得$\widehat f(0)=0$，分两段积分算出奇数$k$的系数$2/(\pi\mathrm ik)$、偶数$k$的系数为零。

7. 把$\pm k$配对成$\frac4{\pi k}\sin kx$，写出$S_5f$。

8. 引出配图，对比取值与坐标两种一列数，说明三条正弦波叠加勾出方波。

9. 配图`fig:fourier-square-coordinates`：(a)方波、三个分量与$S_5f$，(b)系数模长，绿色为保留的坐标、红色为舍弃的坐标。

10. 定义三角多项式空间$\mathcal T_N$，回用第12章说明$S_Nf$是正交投影，并写出Bessel不等式。

11. 引出对照表，指出最后一行是类比失效处。

12. 表`tab:fourier-dictionary`：有限维标准正交基与复指数系在坐标、投影、Bessel、展开、成基条件上的对应。

13. 以拿掉$e_0$后仍是无穷标准正交系而丢失常数函数为例，说明无限维中正交元素的数量不保证成基，写“级数”时未断言收敛，须证明完备性。

###### paragraph：Fejér平均

1. 说明完备性的证明思路是用只依赖系数的三角多项式逼近$f$，把系数代入部分和得积分形式`eq:fourier-dirichlet-integral`并定义Dirichlet核。

2. 用几何级数与乘$e^{-\mathrm it/2}$的步骤推出闭式`eq:fourier-dirichlet-closed`。

3. 指出$D_N$权值有正有负、两侧振荡不随$N$减小，使直接估计困难，引用配图(a)。

4. 定义算术平均$\sigma_Nf$与Fejér核，说明平均使振荡的正负抵消。

5. 用积化和差与裂项相消逐步推出闭式`eq:fourier-fejer-closed`。

6. 配图`fig:fourier-kernels`：$N=8$时的$D_8$与$F_8$，同一纵轴，中央高度为$17$与$9$，$F_8$处处非负。

7. 列出$F_N$的三条性质：非负、积分为$1$、远离原点处有上界。

8. 引理`lem:fourier-fejer`：连续周期函数的Fejér平均一致收敛，$L^2$函数的Fejér平均按$L^2$收敛。

9. 证明开始：把$f(x)$写进积分得误差的积分表示。

10. 证明连续情形：用一致连续模$\omega(\delta)$与核的集中性把积分分成近、远两部分。

11. 证明$L^2$情形：以$F_N$为概率权用Cauchy--Schwarz与Tonelli，把误差化为平移误差的加权平均，归结为$L^2$平移连续性。

12. 由第7章$\mathbb R$上的$L^1$平移连续性经截断$F=f\mathbf 1_{[-2\pi,2\pi]}$得周期情形的$L^1$平移连续性。

13. 对有界函数用$\lvert\tau_hf-f\rvert^2\leq2n\lvert\tau_hf-f\rvert$得$L^2$平移连续性。

14. 对一般$L^2$函数截断取值，用三角不等式完成平移连续性的证明。

###### paragraph：完备性与Parseval关系

1. 指出$\sigma_Nf$完全由系数决定，正好用于证明完备性。

2. 定理`thm:fourier-series-l2`：复指数系完备，$S_Nf\to f$于$L^2$，并有式`eq:fourier-series-parseval`的能量与内积公式。

3. 证明：系数全零则$\sigma_Nf=0$，而$\sigma_Nf\to f$，故$f=0$；其余由第12章正交展开定理给出。

4. 解释Parseval关系是无限维勾股定理，并由正交性写出截断误差式`eq:fourier-series-truncation`。

5. 结合第12章指出系数映射是$L^2(\mathbb T)$到$\ell^2(\mathbb Z)$的保持内积的双射，“函数是一列坐标”在$L^2$意义下严格成立。

6. 用方波核对Parseval关系，算出$\sum(2j+1)^{-2}=\pi^2/8$。

7. 逐项算出前几项的平方和与$N=1,3,5$的截断误差$0.1894$、$0.0994$、$0.0669$，说明增加坐标时已算系数不必修改。

###### paragraph：实形式与一般周期

1. 由实值函数的共轭对称配对$\pm k$，写出正弦余弦形式、两套系数的关系与实形式的Parseval关系。

2. 说明两种写法是同一展开，常数来自配对，用方波核对实系数，并指出这相当于换到实的正交基。

3. 由变量替换写出一般周期$T$的系数式`eq:fourier-period-T`，频率为$k/T$，周期越长频率越密，为下一节做准备。

###### paragraph：系数描述的是等价类

1. 指出系数是积分，改变零测集上的值不改变坐标，所以坐标记录的是等价类，展开是范数等式。

2. 回到方波例子未规定间断点取值的原因，并引出点态问题需要另加条件。

#### 14.1.2 点态收敛

1. 说明$L^2$收敛不控制单点，连续性也不够（du Bois-Reymond的连续函数级数在某点发散，构造较长，可查阅教材），本小节使用分段$C^1$条件。

###### paragraph：Riemann--Lebesgue引理

1. 用高频振荡在小段上正负抵消解释高频积分趋于零，并说明它对任何可积函数成立。

2. 引理`lem:fourier-riemann-lebesgue`：可积函数的高频振荡积分趋于零，式`eq:fourier-riemann-lebesgue`，含正弦情形与周期系数情形。

3. 证明：换元半个周期并与原式相加，归结为平移积分连续性。

4. 对比$L^2$情形可由Bessel读出，指出引理的新内容是只要求可积，且不给出速度，以方波的$1/\lvert k\rvert$为例。

###### paragraph：分段$C^1$函数的Dirichlet定理

1. 定义周期函数分段$C^1$，说明每点存在单侧极限，方波是典型例子。

2. 定理`thm:fourier-dirichlet`：部分和在每点收敛到左右极限的平均，式`eq:fourier-dirichlet-limit`。

3. 证明第一步：由$D_N$偶性与积分值把误差写成$g(t)\sin((N+\tfrac12)t)$的积分，归结为$g$可积。

4. 证明第二步：在$t=0$附近用中值定理得单侧Lipschitz估计使$g$有界，在其余部分用$\sin(t/2)$的下界，再用Riemann--Lebesgue引理。

###### paragraph：连续点、跳跃点与等价类

1. 取连续点$x=\pi/2$，写出部分和的交错形式，$N=1,3,5,7$时依次约为$1.273$、$0.849$、$1.104$、$0.922$，在$1$的两侧摆动着收敛。

2. 取跳跃点$x=0$，部分和恒为$0$，等于左右极限的平均，单点赋值不进入系数或单侧极限。

3. 比较$L^2$展开，说明这里多用了单侧Lipschitz估计，收敛具有局部性，$L^2$收敛不能代替局部条件。

#### 14.1.3 一致收敛

1. 说明一致收敛要求最大误差趋于零，充分条件是坐标绝对可和，衰减速度由光滑性控制。

###### paragraph：分部积分与系数衰减

1. 分部积分得式`eq:fourier-series-derivative`，指出求导是对角矩阵$\operatorname{diag}(\mathrm ik)$，这一步依赖周期性。

2. 定理`thm:fourier-uniform`：$C^2$周期函数的系数上界式`eq:fourier-c2-coefficient`与一致误差式`eq:fourier-c2-uniform-error`。

3. 证明第一步：用式`eq:fourier-series-derivative`两次得系数估计。

4. 证明第二步：Weierstrass判别法给一致极限，与$L^2$极限几乎处处相同，由连续性处处相同。

5. 证明第三步：尾部求和用积分比较得$2/N$，得到误差估计。

6. 说明$C^2$不必要，$C^1$由Cauchy--Schwarz与$f'$的Parseval关系即可。

7. 以三角波为例算出系数，绝对可和，所以尖点不妨碍一致收敛。

8. 在$x=0$取值再次得到$\pi^2/8$，并逐项算$N=1,3,5,9$的$S_Nf(0)$。

9. 比较方波$1/\lvert k\rvert$与三角波$1/k^2$，说明函数越光滑高频坐标越小。

###### paragraph：三种误差的比较

1. 比较一致、逐点、$L^2$三种误差的控制关系。

2. 由连续函数列的一致极限连续，证明跳跃函数不能一致收敛。

3. 取$N=2n-1$，由导数定位第一个峰$x=\pi/(2n)$，用中点Riemann和算出峰值极限$\frac2\pi\int_0^\pi\frac{\sin u}u\,\mathrm du\approx1.179$，给出Gibbs现象及$N=9,25,81$的数值。

4. 配图`fig:fourier-gibbs`：(a)$N=9$的部分和与跳跃点中值，(b)放大图中$N=9,25,81$的第一个峰趋近$1.179$并靠近跳跃点。

5. 借放大图说明Gibbs现象与Dirichlet定理不矛盾，并总结方波上三种误差的不同表现。

### 14.2 $L^1$中的Fourier变换

正文：[02-l1-transform.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/02-l1-transform.tex)

1. 以周期增大时频率变密引入，下标从整数连成整个$\mathbb R^d$，求和变积分，指出类比开始不严格。

2. 预告先建立变换本身，再单独回答反演。

#### 14.2.1 Fourier变换的基本性质

###### paragraph：定义与归一化

1. 把支撑有限的函数周期化，得$Tc_k$只依赖频率$k/T$，是同一函数在格点上的取值。

2. 以方框、$T=2$、$k=1$算出$2c_1=2/\pi$，引用配图。

3. 配图`fig:fourier-series-to-transform`：$T=2,4,8$时的$Tc_k$落在同一条$\sin(\pi\xi)/(\pi\xi)$曲线上。

4. 把系数代回级数得步长$1/T$的Riemann和，形式极限是对$\xi$的积分，说明这只是启发。

5. 记内积与平面波，解释$\lvert\xi\rvert$是单位长度内的圈数。

6. 定义`def:fourier-transform-l1`：用式`eq:fourier-transform-l1`定义$L^1$上的Fourier变换。

7. 说明可积性保证积分对每个$\xi$存在且不受零测集影响，$\widehat f$有确定的逐点值。

8. 指出类比的折扣：平面波不属于$L^2$，不构成正交基，一切结论须直接证明。

9. 说明$2\pi$的约定与角频率写法的伸缩关系，常数对照在14.3末尾。

###### paragraph：有界性、连续性与高频衰减

1. 引出可积性已足够给出基本性质。

2. 定理`thm:fourier-l1-properties`：线性、有界、连续、高频衰减。

3. 证明线性与有界性。

4. 证明连续性：控制收敛定理。

5. 证明高频衰减：取$h=\xi/(2\lvert\xi\rvert^2)$换元相加，归结为平移积分连续性。

6. 总结$f\mapsto\widehat f$映到无穷远趋零的连续函数且不增范数，衰减速度留到微分规则。

###### paragraph：三个例子

1. 算方框的变换式`eq:fourier-box`，指出零点位置与前面$2c_1$一致。

2. 用调和级数说明$\widehat B$不绝对可积。

3. 算双边指数的变换式`eq:fourier-double-exponential`，用$\widehat f(0)=2$检验。

4. 引出Gauss函数自对偶，用极坐标算积分为$1$。

5. 在积分号下求导、分部积分得一阶方程，解出$\widehat G=G$，高维由Fubini。

6. 比较三对函数的光滑性与衰减，引用配图，对应周期情形的结论。

7. 配图`fig:fourier-three-pairs`：上排为方框、双边指数、Gauss函数，下排为对应变换。

###### paragraph：平移、缩放与变换的定义域

1. 以加宽的方框算出$\sin(2\pi\xi)/(\pi\xi)$，说明变换仍定义在整条实轴上，只是形状改变。

2. 对比周期情形频率集合随$T$改变，全空间频率集合总是$\mathbb R^d$。

#### 14.2.2 反演的条件

1. 由酉矩阵的逆是共轭转置提示候选，用式`eq:fourier-inverse`定义逆Fourier变换。

2. 指出直接代入后内层积分$\int e^{2\pi\mathrm i(x-y)\cdot\xi}\,\mathrm d\xi$不收敛，矩阵类比$U^*U=I$在此失效。

3. 用方框说明困难是实在的，预告先在$\widehat f$可积时反演，再讨论逐点版本。

###### paragraph：Gauss核的恒等逼近

1. 说明证明思路是在频域乘$G(t\xi)$使积分绝对收敛，引入缩放核$G_t$。

2. 用自对偶算出式`eq:fourier-gauss-kernel-inverse`，发散的内层积分被替换成集中于$z=0$的$G_t$。

3. 引理`lem:fourier-gauss-approx`：式`eq:fourier-gauss-regularized`与$f*G_t\to f$于$L^1$。

4. 证明第1条：Fubini。

5. 证明第2条：归结为平移积分连续性与控制收敛。

6. 定义恒等逼近，与磨光核比较。

7. 解释式`eq:fourier-gauss-regularized`两边，引用配图，说明$t$越小频域保留越宽、空间抹平越窄。

8. 配图`fig:fourier-gauss-smoothing`：(a)$\widehat B$、$G(t\xi)$与乘积，(b)方框与$t=0.5,0.1$的$B*G_t$。

###### paragraph：反演定理

1. 引出令$t\to0$的两侧极限。

2. 定理`thm:fourier-l1-inversion`：$f,\widehat f\in L^1$时式`eq:fourier-l1-inversion`给出连续代表，几乎处处相等，连续点处相等。

3. 证明$g$的连续性与无穷远趋零。

4. 证明左边趋于$g$。

5. 证明右边沿子列趋于$f$，两极限相等。

6. 证明连续点处的相等。

7. 解释定理三层含义：连续代表、跳跃函数变换不可积、变换是单射。

8. 对双边指数写出反演，并在$x=0$用反正切积分验证。

###### paragraph：逐点反演与对称截断

1. 用Fubini写出对称截断的积分式`eq:fourier-symmetric-truncation`，指出核扮演Dirichlet核，需要Dirichlet积分$\pi/2$。

2. 用$\frac1{2\pi}\int_0^\pi D_N=\frac12$、$\frac1{\sin(t/2)}-\frac2t$有界与Riemann--Lebesgue引理算出Dirichlet积分。

3. 定理`thm:fourier-symmetric-inversion`：局部分段$C^1$的可积函数按对称截断逐点收敛到平均值，式`eq:fourier-symmetric-inversion`。

4. 证明：把积分在$t=1$分开，写成三项。

5. 前两项的系数可积，用Riemann--Lebesgue引理趋于零。

6. 第三项换元后由Dirichlet积分得$1/2$。

7. 对方框读出结论，对应Dirichlet定理。

8. 总结变换的存在与反演是两个问题，并比较两种反演条件。

### 14.3 $L^2$中的Fourier变换

正文：[03-l2-transform.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/03-l2-transform.tex)

1. 提出希望Fourier变换像酉矩阵一样保持长度，但能量关系属于$L^2$而积分定义要求$L^1$。

2. 给出互不包含的例子$s\in L^2\setminus L^1$与$u\in L^1\setminus L^2$。

3. 用从有理数造实数作类比，说明路线是在交集上定义、证明保长、稠密延拓。

###### paragraph：截取逼近

1. 定义截取$f_n$，说明它属于$L^1\cap L^2$。

2. 用控制收敛定理证明$f_n\to f$于$L^2$。

3. 以$g=1/(1+\lvert x\rvert)$手算尾部能量$2/(1+n)$。

4. 用截取得到$L^2$平移连续性。

5. 引理`lem:fourier-gauss-l2`：$L^2$中Gauss光滑化的收敛，以及$f\in L^1\cap L^2$时的乘积公式式`eq:fourier-gauss-l2-product`。

6. 证明卷积处处有定义。

7. 证明$L^2$收敛：Cauchy--Schwarz、交换次序、平移连续性。

8. 证明乘积公式：Fubini与缩放。

9. 说明这是卷积规则的特例，因要用到而直接验证。

#### 14.3.1 等距延拓

###### paragraph：交集上的Plancherel恒等式

1. 在$D=\{f\in L^1\cap L^2:\widehat f\in L^1\}$上用反演与Fubini证明能量等式。

2. 定理`thm:fourier-plancherel-l1l2`：$L^1\cap L^2$上保持$L^2$范数，式`eq:fourier-plancherel-l1l2`。

3. 证明第一步：用$f_t=f*G_t$进入$D$。

4. 证明第二步：对$f_t$用恒等式，再用单调收敛令$t\downarrow0$。

5. 用方框读出$\int(\sin\pi\xi/(\pi\xi))^2\,\mathrm d\xi=1$，预告另行验证。

###### paragraph：延拓到$L^2$

1. 回用第3章的延拓定理，引出Plancherel定理。

2. 定理`thm:fourier-plancherel`：唯一连续线性等距延拓，以及极限式`eq:fourier-plancherel-limit`。

3. 证明存在唯一性。

4. 证明等距与线性。

5. 证明球上截取的变换收敛到$\mathcal Ff$。

6. 约定此后记号$\widehat f=\mathcal Ff$，与原定义在交集上一致。

###### paragraph：频域元素是等价类

1. 说明延拓结果是等价类，积分不必收敛，极限只在范数意义下成立。

2. 以$s$为例说明频率$\pm1/2$处的值无意义，与$L^1$情形对照。

#### 14.3.2 $L^2$反演与Parseval关系

###### paragraph：反演与内积保持

1. 引入反射$R$，验证$\mathcal FR=R\mathcal F$，逆变换的延拓即$R\mathcal F$。

2. 定理`thm:fourier-l2-inversion`：$\mathcal F$双射、$\mathcal F^{-1}=R\mathcal F$、$\mathcal F\mathcal F=R$，以及Parseval关系式`eq:fourier-l2-parseval`。

3. 证明第一步：$D$上$R\mathcal F\mathcal F=I$。

4. 证明第二步：$D$稠密，延拓到全空间。

5. 证明第三步：由$R^2=I$得双射与逆。

6. 证明第四步：用对第二变量线性的极化公式得内积保持。

7. 总结这正是酉矩阵的性质，$\mathcal F\mathcal F=R$将在14.5用$4\times4$矩阵看到。

8. 算出$\mathcal Fs=B$并得到$\int(\sin\pi x/(\pi x))^2\,\mathrm dx=1$。

###### paragraph：同一公式的不同含义

1. 指出反演公式在本章三次出现，含义各不相同，高维截断的几乎处处收敛问题本书不讨论。

2. 表`tab:fourier-inversion-meanings`：三种条件下右边的含义与等式的意义。

###### paragraph：归一化与常数

1. 说明不同约定只差伸缩与常数，但公式常数必须配套，引出对照表。

2. 表`tab:fourier-normalizations`：频率、角频率、对称归一三种约定的正反变换与能量关系。

3. 以第二行换元核对常数$(2\pi)^{-d}$，并联系周期情形把$1/(2\pi)$放进内积。

### 14.4 Fourier变换下的运算

正文：[04-operations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/04-operations.tex)

1. 由对称矩阵在特征向量基下对角作类比，算出平面波是平移与求导的公共“特征向量”，解释频率坐标好用的原因。

2. 指出平面波不在所讨论的空间内，这只是启发，每条规则先在$L^1$证明，再说明$L^2$推广。

#### 14.4.1 平移

1. 定义平移与调制，预期平移只改相位。

2. 定理`thm:fourier-translation`：平移与调制的规则，式`eq:fourier-translation`，含$L^2$情形。

3. 证明$L^1$情形：换元与合并指数。

4. 证明$L^2$情形：等距映射在稠密子空间上相等。

5. 说明两条规则方向相反，平移不改频谱大小，周期情形规则相同。

6. 以$\mathbf 1_{[0,1]}$用两种算法核对。

#### 14.4.2 缩放

1. 用单位长度内圈数解释压窄使频率放大，并预告一般线性变换。

2. 定理`thm:fourier-scaling`：线性变量替换式`eq:fourier-linear-change`及缩放特例式`eq:fourier-scaling`。

3. 证明：换元$y=\bm Ax$，Jacobian与内积的转置逆。

4. 解释频率尺度、Jacobian、转置逆三个量的来源。

5. 取$\lambda=1/2$的方框核对，解释空间变宽频域变窄、中央高度翻倍。

6. 配图`fig:fourier-scaling`：(a)$B(x)$与$B(x/2)$，(b)两者的变换，第一个零点从$\pm1$移到$\pm\frac12$。

7. 用Gauss核检验式`eq:fourier-scaling`。

8. 写出$L^2$的保范伸缩$D_\lambda$，并联系小波伸缩。

#### 14.4.3 微分

1. 回顾周期情形，指出全空间边界项与不可导点的问题，安排先后两种情形。

###### paragraph：光滑紧支撑函数

1. 分部积分逐步得$\widehat{\partial_jf}=2\pi\mathrm i\xi_j\widehat f$，与特征值一致。

###### paragraph：弱导数可积的情形

1. 回顾弱导数的测试恒等式，说明要把平面波截断成测试函数。

2. 定理`thm:fourier-derivative`：$f$与弱导数可积时的微分规则，式`eq:fourier-derivative`。

3. 证明：截断$\varphi_R$，代入测试恒等式，令$R\to\infty$，边缘项按$1/R$趋零。

4. 说明$f\in L^1$承担控制边缘项的任务，不需要逐点趋零。

###### paragraph：光滑性与衰减

1. 由微分规则与有界性得高阶弱导数对应$\lvert\xi\rvert^{-m}$衰减。

2. 对偶地由$x_jf$可积得变换可微。

3. 用双边指数的弱导数核对规则。

4. 说明方框不满足条件，形式结果对应两个点质量。

5. 说明$L^2$的频域刻画是Sobolev章的出发点。

#### 14.4.4 卷积

1. 回顾第7章的卷积定义与$L^1$上界。

2. 把卷积看作平移的加权叠加，预期频域相乘，卷积算子在频率坐标下对角。

3. 定理`thm:fourier-convolution`：$L^1$上的卷积规则，式`eq:fourier-convolution`。

4. 证明：Fubini与换元。

5. 算出$B*B=\Lambda$，引用配图中$x=0.4$的重叠长度$0.6$。

6. 由卷积规则得$\widehat\Lambda$，反演再验证$\int(\sin\pi\xi/(\pi\xi))^2=1$，解释跳跃变尖点使衰减加快。

7. 配图`fig:fourier-convolution-triangle`：(a)重叠区间，(b)$\Lambda$，(c)$\widehat B$与$\widehat\Lambda$。

###### paragraph：推广到$L^2$

1. 说明推广要确认输入、输出空间与等式意义。

2. $L^1\times L^2$：Cauchy--Schwarz得卷积上界。

3. 该情形的等式由稠密性在$L^2$中成立。

4. $L^2\times L^2$：卷积处处有定义但未必属于$L^1$或$L^2$，正确的对应是逆变换式`eq:fourier-l2-convolution`。

5. 用Parseval关系与共轭、反射规则证明。

6. 以$s*s=s$为例。

7. 指出滤波问题属于卷九信号系统章。

### 14.5 Fourier表示与离散变换

正文：[05-discrete-representations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/05-discrete-representations.tex)

1. 列出周期系数、连续变换与有限向量三种表示，指出第三种是类比的原型。

2. 预告先并列再说明转换所需的操作。

###### paragraph：离散Fourier变换

1. 说明这里“函数是向量”不再是类比，引入模$N$的下标与$N$个频率。

2. 定义`def:fourier-dft`：用式`eq:fourier-dft`定义离散Fourier变换。

3. 由几何级数证明单位根正交性式`eq:fourier-roots-orthogonality`。

4. 代入并交换有限和，得反演与能量关系式`eq:fourier-dft-inverse`。

5. 说明没有收敛问题，$N^{-1/2}\bm W$是酉矩阵，无穷维中费力建立的性质在此是矩阵性质。

6. 取$N=4$、$\bm x=(1,2,0,-1)$写出矩阵乘法，得$(2,1-3\mathrm i,0,1+3\mathrm i)$。

7. 用能量关系核对$6=6$，再作用一次得$4$倍反射$(1,-1,0,2)$，对应$\mathcal F\mathcal F=R$。

###### paragraph：三种表示的对象

1. 引出对照表，差别首先在输入。

2. 表`tab:fourier-three-representations`：三种表示的输入对象、频率集合与成立意义。

3. 说明三者不能直接互相代替，转换必须先把对象转过去，引出下面三个操作。

###### paragraph：周期化：从全空间到周期

1. 用平移叠加定义周期化式`eq:fourier-periodization`，由Tonelli说明几乎处处绝对收敛。

2. 定理`thm:fourier-periodization`：周期化的系数等于$\widehat f(k)$，式`eq:fourier-periodization-coefficient`。

3. 证明：交换求和积分并拼接区间。

4. 解释连续频率被取样，代价是原函数各段重叠，支撑不超过一个周期时无损。

5. 以双边指数读出Poisson求和公式，两边都等于约$2.1640$，并说明一般需要的正则性。

###### paragraph：取样：从周期函数到有限向量

1. 在系数绝对可和且$g$连续的条件下定义等距取样。

2. 定理`thm:fourier-sampling-aliasing`：取样向量的DFT是同余类系数之和，式`eq:fourier-aliasing`。

3. 证明：代入级数、交换有限和、用单位根正交性。

4. 定义混叠。

5. 以$\cos(6\pi x)$、$N=4$手算样本$(1,0,-1,0)$与$\widehat x[1]=\widehat x[3]=2$，与$\cos(2\pi x)$不可区分。

6. 配图`fig:fourier-aliasing`：(a)两条曲线在取样点重合，(b)频率$m=-3$按模$4$折到$k=1$。

7. 给出频带足够窄时DFT精确读取系数的条件，指出例子不满足。

###### paragraph：截断：从全空间到有限记录

1. 截断是乘方框，由$L^2$卷积对应得乘积规则式`eq:fourier-product-rule`。

2. 写出$\widehat{B_L}$，说明$L$越大越接近恒等逼近，有限时频率扩散。

3. 描述截断—周期化—取样的完整链条及其误差来源。

4. 划定范围：信号频谱、采样恢复分别属于卷九相应各章。

### 14.6 本章小结

正文：[06-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/05-fourier-transform/06-summary.tex)

1. 重述章首问题。

2. 总结周期情形：完备、Parseval、逐点与一致收敛的条件、Gibbs现象。

3. 总结全空间$L^1$理论：类比失效处、变换性质、反演的两种条件。

4. 总结$L^2$理论：稠密延拓、酉性质、等价类、反演公式的三种含义。

5. 总结四类运算规则及其条件，强调频率坐标使算子对角化。

6. 总结离散变换是真正的有限维酉变换，以及三种表示转换的代价。

7. 指出Fourier表示的全局性，引出第15章小波与第20章逼近误差。

## 第15章 小波变换

正文入口：[06-wavelet-transform.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform.tex)，章内依次输入[01-finite-haar.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/01-finite-haar.tex)、[02-scaling-detail-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/02-scaling-detail-spaces.tex)、[03-interval-haar-expansion.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/03-interval-haar-expansion.tex)、[04-wavelets-on-real-line.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/04-wavelets-on-real-line.tex)、[05-periodization-boundary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/05-periodization-boundary.tex)、[06-fourier-wavelet-comparison.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/06-fourier-wavelet-comparison.tex)、[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/07-summary.tex)。

章职责与主线：本章沿用第10章把函数看成无限维向量的类比，建立按尺度与位置组织的坐标，即把函数换到多尺度标准正交基后读出的小波系数。先在$\mathbb R^{2^J}$中用逐层平均与半差得到正交Haar变换，再放回$[0,1]$上的分段常数函数解释为换基，证明二进阶梯函数稠密，得到Haar展开、重构与Parseval等式。随后在实轴上用正交多分辨率分析、二尺度关系构造母小波并完整证明其正交基性质，以D4的二尺度系数手算消失矩与系数衰减；最后讨论周期化、周期延拓、反射延拓与边界小波，并在同一周期区间上比较Fourier系数与Haar系数。截断误差的定量刻画留给第20章，小波系数刻画正则性留给第22章。

1. 章首第一段回顾函数向量的取值坐标只知位置、Fourier坐标只知频率，说明这两种坐标各走一个极端。

2. 第二段以一段平稳、少数位置跳变的记录为对象，指出一处跳变使所有频率系数非零，提出同时带尺度和位置标号的基：先记整体水平，再逐层记左右两半的差。

3. 第三段点明小波系数是函数这条无限维向量换到多尺度标准正交基后读出的分量，提出基怎样构造、在什么意义下重构、边界如何调整三个问题。

4. 第四段说明前三节路线：15.1在$\mathbb R^{2^J}$中做正交换基，15.2放回分段常数函数说明换了哪组基函数，15.3让层数趋于无穷并证明完备。

5. 第五段说明后三节路线：15.4在实轴上建立一般多分辨率结构并讨论光滑性与消失矩，15.5处理基函数跨过端点，15.6比较Fourier坐标与小波坐标。

6. 第六段交代依赖第12章的正交投影与展开、第14章的Fourier级数，截断误差的定量结论放在第20章，Besov范数放在第22章。

### 15.1 有限Haar变换

正文：[01-finite-haar.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/01-finite-haar.tex)

1. 取$N=2^J$个等分段上的取值组成向量$\bm a$，说明这是函数向量输入有限的情形，函数就是$\mathbb R^N$中的一个点。

2. 提出把$N$个数改写成整体水平与各尺度起伏且能拼回的目标，本节全部在$\mathbb R^N$中计算。

#### 15.1.1 逐层平均与差值

###### paragraph：一对数的平均与半差

1. 把相邻取值$a,b$换成平均$s$与半差$d$（式`eq:wavelet-average-difference`），说明$s$记录共同水平、$d$记录偏离。

2. 由相加相减得$a=s+d$、$b=s-d$，说明这一步只换记法不丢信息，并指出$a=b$时$d=0$。

###### paragraph：逐层分解

1. 对长度$N=2^J$的向量两两分组得$N/2$个平均和半差，半差保存、平均继续分解，$J$步后只剩总平均。

2. 数出半差共$N-1$个，连同总平均恰为$N$个数；恢复按相反次序进行，每步只用加减，整个分解是可逆线性变换。

3. 例`ex:wavelet-four-values-average`对$(2,4,8,6)$分两步算出总平均$5$、粗层半差$-2$、细层半差$-1,1$，再逐步恢复四个取值。

4. 引出图`fig:wavelet-average-tree`，解释沿树向下平均继续传递而半差留在原地，对应“只继续处理平均”。

5. 图`fig:wavelet-average-tree`：以$(2,4,8,6)$的逐层平均与半差画成的树，蓝框为原始取值，绿框为平均，黄框为半差。

###### paragraph：差值记录的尺度与位置

1. 说明每个半差对应一个块及其左右两半：细层$-1$比较$a_0,a_1$，粗层$-2$比较前后两段的平均；块长给出尺度，块的位置给出位置。

2. 把$a_2$从$8$改成$9$重算两步，得平均$3,15/2$、细层半差$-1,3/2$、粗层半差$-9/4$、总平均$21/4$，检验只有含第$2$段的块改变，每层只影响一个系数。

#### 15.1.2 正交变换与逆变换

1. 计算$s^2+d^2=(a^2+b^2)/2$，指出平均与半差每步使平方和减半，不是标准正交基下的坐标，故两个新系数都乘以$\sqrt2$。

###### paragraph：二阶正交变换

1. 写出$\bm H_2$（式`eq:wavelet-h2`）及对应的$s,d$，说明沿用记号但比式`eq:wavelet-average-difference`中的量大$\sqrt2$倍。

2. 直接相乘核对$\bm H_2^{\top}\bm H_2=\bm I$，得到保持平方和、逆矩阵等于转置，并说明正交矩阵性质可参考卷二第4章。

###### paragraph：多层变换

1. 说明第一层对全部相邻对作用$\bm H_2$，之后只对粗系数继续作用，细节保留，共做$J$层。

2. 每层在被处理坐标上是分块对角正交矩阵、其余坐标恒等，复合仍正交；约定输出按最粗项在前、细节由粗到细排列。

3. 定义Haar变换$\bm c=\bm W_N\bm a$（式`eq:wavelet-finite-haar-isometry`），由正交性得长度不变与逆变换，并数出共$N-1$对，运算次数与$N$成正比。

4. 例`ex:wavelet-four-values-orthogonal`对$(2,4,8,6)$逐层得$(10,-4,-\sqrt2,\sqrt2)$，写出$\bm W_4$，用平方和$120$与逐分量逆变换核对。

###### paragraph：矩阵的各行就是新基

1. 指出$\bm W_4$的四行组成$\mathbb R^4$的新标准正交基，$\bm c$是$\bm a$在这组基下的坐标。

2. 逐行解释第一行读整体水平、第二行读最粗起伏、后两行读局部起伏，强调向量不变、变的是读取方式。

###### paragraph：与平均和半差的关系

1. 比较两例的系数比例$2,2,\sqrt2,\sqrt2$，一般地块长$2^m$的系数等于$2^{m/2}$乘以平均或半差。

2. 对$m$归纳验证比例因子，说明两种算法信息相同，差别只在比例因子，正交版本由此换来长度不变。

### 15.2 尺度空间与细节空间

正文：[02-scaling-detail-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/02-scaling-detail-spaces.tex)

1. 把$2^J$个取值看成在第$k$段上取常值的函数，平均与差值成为函数运算，Haar变换的各行成为基函数。

2. 固定$L^2([0,1])$的内积及对第一变量共轭线性的约定，说明本章基函数都是实值的。

#### 15.2.1 尺度空间

1. 定义第$j$层二进区间（式`eq:wavelet-dyadic-interval`），解释尺度与位置，并说明端点是零测集，不再区分$[0,1)$与$[0,1]$。

2. 用函数向量的语言解释分辨率$j$：取值向量被约束成每$2^{-j}$一段的常数块，只剩$2^j$个自由度。

3. 定义`def:wavelet-scaling-space`给出尺度空间$V_j$与归一化基函数$\varphi_{j,k}$（式`eq:wavelet-scaling-basis`）。

4. 验证支撑不交且长度为$1$，得到$V_j$的标准正交基与$\dim V_j=2^j$，有限维子空间闭故可用正交投影。

###### paragraph：嵌套

1. 由每个第$j$层区间是两个第$j+1$层区间之并，得到$V_0\subset V_1\subset\cdots$（式`eq:wavelet-interval-nesting`）。

###### paragraph：投影就是取区间平均

1. 用Cauchy--Schwarz说明区间平均有意义，再由标准正交基写出$P_jf$（式`eq:wavelet-projection-average`），说明投影在每个小区间上取平均值，是$V_j$中最近的函数。

2. 用$\mathbb R^2$中$(a,b)$投影到$(1,1)$得到两个分量都换成平均作类比，说明公式在每个小区间上做同样的事。

#### 15.2.2 细节空间

1. 由维数差$2^j$说明从$V_j$到$V_{j+1}$多出的正是每个区间左右两半的差异，用正交补把它取出。

2. 定义`def:wavelet-detail-space`给出细节空间$W_j$、母函数$\psi$与Haar函数$\psi_{j,k}$（式`eq:wavelet-haar-mother`、`eq:wavelet-haar-function`）。

3. 解释$\psi_{j,k}$在区间左半和右半的取值，写成$2^{j/2}\psi(2^jx-k)$的平移缩放形式。

4. 定理`thm:wavelet-detail-basis`给出$W_j$的标准正交基及$V_{j+1}=V_j\oplus W_j$（式`eq:wavelet-one-step-decomposition`），证明验证属于$V_{j+1}$、与$V_j$正交、标准正交及维数相等。

5. 用细区间指示函数写成$\varphi_{j,k}\pm\psi_{j,k}$的组合，说明这是平均与半差的函数版本。

###### paragraph：逐层分解

1. 反复应用定理得式`eq:wavelet-finite-decomposition`，核对维数，并指出$\{\varphi_{0,0}\}$与全部$\psi_{j,k}$是$V_J$的另一组标准正交基。

2. 用投影差$P_{j+1}-P_j$解释第$j$层细节是较粗表示中缺少的局部差异。

###### paragraph：一个可以手算的例子

1. 对$f(x)=x$写出$P_0f$、$P_1f$与细节$P_1f-P_0f$在左右两半取$\mp1/4$。

2. 用内积算出$\langle\psi_{0,0},f\rangle=-1/4$，验证两种算法一致，并引出图`fig:wavelet-projection-detail`所示各层细节同形、高度逐层减半。

3. 图`fig:wavelet-projection-detail`：$f(x)=x$在$V_0,V_1,V_2$上的投影与相邻两层投影之差。

#### 15.2.3 值向量与函数坐标

1. 计算$f$的平方积分等于取值平方和乘以$2^{-J}$，把差别归于每段的长度。

2. 与点积逼近积分要乘区间长度类比，写出$f$在基$\varphi_{J,k}$下的坐标是$2^{-J/2}\bm a$。

###### paragraph：一步变换就是一次换基

1. 写出相邻两层基函数的关系，代入后得到$c_0,c_1$换成$(c_0\pm c_1)/\sqrt2$，正是$\bm H_2$的作用。

2. 由此说明对$2^{-J/2}\bm a$作有限Haar变换得到的就是$f$在Haar基下的坐标，引出图`fig:wavelet-two-bases`对比同一函数的两套坐标。

3. 图`fig:wavelet-two-bases`：$f$取$2,4,8,6$时指示函数基的坐标$(1,2,4,3)$与Haar基的坐标$(5,-2,-1/\sqrt2,1/\sqrt2)$。

4. 例`ex:wavelet-four-values-function`由坐标向量逐层得到Haar系数，再用积分逐项核对，并以$30$核对能量，比较与欧氏系数相差因子$1/2$。

5. 说明归一化因子的用处：比较相对大小时不起作用，用系数估计$L^2$误差时必须带上。

### 15.3 区间上的Haar展开

正文：[03-interval-haar-expansion.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/03-interval-haar-expansion.tex)

1. 指出$f(x)=x$不在任何$V_J$中，要表示一般$L^2$函数须让层级无限增加。

2. 对比有限维$N$个标准正交向量自动是基，无限维须证明完备，本节先证稠密再读出系数与重构。

#### 15.3.1 尺度空间的稠密性

1. 说明要证的逼近陈述及化简路线：截去大值、换简单函数、换有限区间、端点移到二进点。

2. 定理`thm:wavelet-dyadic-dense`断言并稠密及投影列单调收敛（式`eq:wavelet-dense-convergence`）；证明按四步逼近，再由嵌套与最佳逼近得到收敛与单调性。

3. 指出证明末段只用到嵌套与投影最优，所以“并稠密”自动转化为“投影列收敛”。

4. 例`ex:wavelet-linear-projection-error`对$f(x)=x$逐段积分得$\lVert f-P_jf\rVert_2=2^{-j}/(2\sqrt3)$。

5. 说明定理不给速度，例中的速度来自$f$的光滑性，一般理论在第20章。

#### 15.3.2 系数与重构

1. 由有限层分解推广，固定$j_0\geq0$写出$V_J$从$V_{j_0}$开始的分解。

2. 定理`thm:wavelet-haar-expansion`给出标准正交基（式`eq:wavelet-haar-basis-family`）、展开（式`eq:wavelet-haar-expansion`）、Parseval（式`eq:wavelet-haar-parseval`）及部分和等于$P_Jf$；证明核对跨层正交、由稠密得完备、由投影得部分和。

3. 说明坐标是按$(j,k)$排列的数表，外层级数、内层有限和，收敛与排列无关。

4. 对$f(x)=x$算出$\langle\psi_{j,k},f\rangle=-2^{-3j/2}/4$，各层平方和加粗项得$1/3$，核对能量等式。

###### paragraph：粗项不能省略

1. 由Haar函数积分为零说明去掉粗项后只能表示区间平均为零的函数，常数函数无法表示。

2. 与$\mathbb R^4$的Haar基去掉第一行类比，并预告全实轴上情况不同。

###### paragraph：有限变换的位置

1. 说明有限Haar变换是对$V_J$的换基而非近似，对一般$f$先取$P_Jf$，截断误差由被丢掉系数的平方和给出。

###### paragraph：点态与一致收敛要另外核验

1. 指出$L^2$收敛不保证点态或一致收敛，连续函数用连续模$\omega$作为好情形。

2. 由$P_jf$是区间平均估计$\lvert P_jf-f\rvert\leq\omega(2^{-j})$，得到一致收敛。

3. 对$f=\mathbf 1_{[1/3,1)}$，每层唯一含$1/3$的区间，引入相对位置$t_j$。

4. 由$t_{j+1}=2t_j$（模$1$）得$t_j$交替，平均$c_j\in\{2/3,1/3\}$，算出一致误差恒为$2/3$、$L^2$误差平方为$\frac29 2^{-j}$，并结合图`fig:wavelet-jump-approximation`解释带宽减半而高度不变。

5. 图`fig:wavelet-jump-approximation`：跳跃函数与$P_jf$（$j=1,3,5$），浅红带为含跳跃点的区间。

6. 说明一般$L^2$函数$P_jf$几乎处处收敛需Lebesgue微分定理，不予证明，并解释平均收敛的机制。

### 15.4 实轴上的小波

正文：[04-wavelets-on-real-line.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/04-wavelets-on-real-line.tex)

1. 回看Haar由一个固定函数平移缩放，指出全实轴上$k$取遍整数，坐标表每行变成无限长。

2. 说明本节路线：抽象多分辨率、写出展开、讨论更好的小波，并固定实值约定与内积。

3. 定义$u_{j,k}$（式`eq:wavelet-dilate-translate`），由变量代换说明因子$2^{j/2}$保持范数、同层内积不依赖$j$。

#### 15.4.1 尺度函数与母小波

1. 把Haar写到实轴上，定义$\varphi,\psi$与$V_j$，$j$可取任意整数。

2. 比较区间情形：每层无限多个位置，$j$可为负对应粗区间。

###### paragraph：多分辨率的条件

1. 说明Haar的几条性质与分段常数无关，把它们抽出来；定义`def:wavelet-mra`给出嵌套、缩放、平移基、稠密与分离四条。

2. 由缩放与平移两条得$\{\varphi_{j,k}\}_k$是$V_j$的标准正交基。

3. 对Haar说明稠密性仿照区间证明，分离条件由半轴上为常数且平方可积直接验证。

###### paragraph：二尺度关系

1. 由$\varphi\in V_1$展开得二尺度关系（式`eq:wavelet-two-scale`），由Parseval得$\sum h_k^2=1$，解释其含义。

2. 指出$(h_k)$是$\varphi$在$V_1$基下的$\ell^2$坐标，写出Haar的情形。

###### paragraph：一组比Haar更长的系数

1. 由平移标准正交及$\varphi_{1,k}(\cdot-n)=\varphi_{1,k+2n}$，得到式`eq:wavelet-filter-orthogonality`。

2. 对比Haar只有$h_0^2+h_1^2=1$，给出D4系数（式`eq:wavelet-d4-filter`），引入Daubechies小波。

3. 手算核对D4的平方和为$1$、错位两位的乘积为$0$，并说明对应的$\varphi$存在且支撑在$[0,3]$上需专门著作。

4. 引出图`fig:wavelet-two-scale`，说明(b)中四片压缩片段加出$\varphi$，自相似也解释了为何没有闭式。

5. 图`fig:wavelet-two-scale`：(a)Haar二尺度关系，(b)D4的$\varphi$及四片压缩平移，(c)D4母小波，并说明数值由整数点精确值逐层加密得到。

###### paragraph：母小波

1. 定义细节空间$W_j$，希望$W_0$也由单个函数的平移张成。

2. 定理`thm:wavelet-mother-from-mra`给出$\psi$（式`eq:wavelet-mother`）及其平移在$W_0$、$W_j$中的标准正交基。

3. 称$\psi$为母小波、$\psi_{j,k}$为小波，用Haar的$g_0,g_1$验证得到Haar函数。

4. 用$\mathbb C^2$中单位向量$(u,v)$与$(\bar v,-\bar u)$正交作为证明的想法，把序列按奇偶分成两路。

5. 证明分五步：化到序列空间；奇偶两路及Parseval；由偶移位正交得$\lvert H\rvert=1$，用实值得$G_0=\overline{H_1}$、$G_1=-\overline{H_0}$；得$\{H,G\}$是$\mathbb C^2$逐点标准正交基，推出序列空间的完备标准正交系；用缩放算子$D_j$得到一般$j$。

6. 对Haar指出$H,G$是$\bm H_2$的两行，一般小波相当于让二阶正交矩阵随频率变化。

###### paragraph：不是任意的平移缩放都构成小波基

1. 用$\mathbf 1_{[0,2)}/\sqrt2$的平移不正交、$\mathbf 1_{[0,1)}$跨层不正交两个反例，说明正交性来自多分辨率结构与$g_k$的特殊选择。

#### 15.4.2 实轴上的小波展开

1. 说明有了母小波后展开与区间平行，只是坐标表两个方向都无限。

2. 定理`thm:wavelet-real-line-expansion`给出标准正交基（式`eq:wavelet-real-line-family`）与展开（式`eq:wavelet-real-line-expansion`）；证明由逐层分解和稠密条件得到完备。

###### paragraph：与区间展开的比较

1. 比较每层位置数，说明紧支撑时每层非零系数有限，个数大致与$2^j$乘以支撑长度成正比。

###### paragraph：实轴上粗项可以消失

1. 由勾股定理得$(P_jf)$在$j\to-\infty$时是Cauchy列。

2. 由极限属于$\bigcap V_i=\{0\}$得$\lVert P_{j_0}f\rVert_2\to0$，于是全部细节构成基（式`eq:wavelet-only-details`）。

3. 以Haar和$\mathbf 1_{[0,1)}$算$\lVert P_{-m}f\rVert_2^2=2^{-m}$，解释质量摊开，与区间上常数粗项保留对比。

#### 15.4.3 光滑性与消失矩

1. 指出Haar的两个局限：跳跃与只抵消常数，算出$\int x\psi=-1/4$，并用基向量与多项式正交解释消失矩。

2. 定义`def:wavelet-vanishing-moments`（式`eq:wavelet-vanishing-moments`）给出$C^s$光滑性与$r$个消失矩。

3. 说明可积性的作用，Haar恰有一个消失矩。

###### paragraph：D4的两个消失矩

1. 由二尺度关系说明消失矩等价于$\sum g_k=0$、$\sum kg_k=0$这样的系数条件。

2. 写出D4非零的$g_k$，代入逐项抵消得两个消失矩，并说明$\psi$支撑在$[-1,2]$，平移一格可取$L=3$。

###### paragraph：一般的Daubechies小波

1. 说明存在任意给定消失矩个数的紧支撑正交小波、支撑长度$2r-1$、光滑性随$r$增大，D4连续不处处可微，证明需频域细致分析。

###### paragraph：消失矩让局部多项式不留痕迹

1. 由代换后多项式次数不变，得$r$个消失矩的小波与次数小于$r$的多项式内积为零。

2. 说明系数只反映偏离多项式的部分，引出图`fig:wavelet-moment-decay`(a)(b)的正负面积对比。

3. 定理`thm:wavelet-moment-decay`（式`eq:wavelet-moment-decay`）给出系数上界；证明用Taylor展开、消失矩与$\lVert\psi_{j,k}\rVert_1$的代换。

###### paragraph：手算比较

1. 用Haar和$f(x)=x$检验定理，上界$2^{-3j/2}$，实际值$-2^{-3j/2}/4$。

2. 换成$x^2$算出$-2^{j/2}m\,h^2/2$，说明Haar抵消不了一次项，衰减阶不变。

3. 对D4由消失矩得$\langle\psi_{j,k},x^2\rangle=2^{-5j/2}m_2$，二尺度关系算出$m_2=-\sqrt3/8$，比Haar多$2^{-j}$，引出图`fig:wavelet-moment-decay`(c)。

4. 图`fig:wavelet-moment-decay`：$x\psi(x)$的正负面积，及$x^2$系数最大绝对值的对数随$j$的变化。

###### paragraph：两种性质的分工

1. 说明消失矩作用在被展开函数上，光滑性作用在重构上。

2. 区分小波的要求与$f$的正则性，刻画正则性时所需阶数在第22章固定。

### 15.5 周期化与边界处理

正文：[05-periodization-boundary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/05-periodization-boundary.tex)

1. 说明Haar从不跨端点，更长的紧支撑小波靠近端点会伸出区间。

2. 用有限向量两端无邻居类比，说明补值或改造基函数要由问题决定。

#### 15.5.1 周期化

1. 对周期对象把基函数也做成周期的，类比下标首尾相接的环，定义$L^2(\mathbb T)$。

###### paragraph：周期化的定义

1. 设定$\varphi,\psi$支撑在$[0,L]$（$L$为正整数，必要时平移），定义$\operatorname{Per}$（式`eq:wavelet-per`）。

2. 定义周期基函数（式`eq:wavelet-periodized-basis`），由$u_{j,k+2^jn}(x)=u_{j,k}(x-n)$说明每层只需$0\leq k<2^j$，$j\geq0$保证步长整除周期。

3. 引出图`fig:wavelet-periodization`，说明D4的$\psi_{2,3}$跨过$x=1$的部分被搬回$[0,1/4]$。

4. 图`fig:wavelet-periodization`：$\psi_{2,3}$在实轴上与周期化后的对比。

###### paragraph：展开公式

1. 把定义代入并交换有限和与积分，得到展开恒等式（式`eq:wavelet-unfolding`），并解释其含义。

2. 定理`thm:wavelet-periodic-basis`（式`eq:wavelet-periodic-basis`）给出$L^2(\mathbb T)$的周期小波基；证明由展开恒等式得标准正交，用$P_Jf$周期化及重叠数$2L+2$的估计得稠密，再数维数得基。

3. 说明Haar周期化后回到区间Haar展开。

###### paragraph：消失矩只部分保留

1. 由展开恒等式得零阶矩保留，计算跨接缝小波的一阶矩，指出多出一项$-\int_1^\infty\psi_{j,k}$。

2. 解释$x$作为周期函数在整数点跳回，跨接缝支撑上已不是多项式，消失矩只对不跨接缝者原样成立。

#### 15.5.2 周期延拓的边界效应

1. 写出周期延拓公式（式`eq:wavelet-periodic-extension`）。

2. 说明周期延拓是$L^2$等距同构，不要求端点取值相等。

###### paragraph：区间上光滑不等于周期光滑

1. 取$f(x)=x$，周期延拓为锯齿波，分部积分算出$\hat f(n)=\mathrm i/(2\pi n)$，只按$1/\lvert n\rvert$衰减。

2. 指出跨接缝小波看到跳跃，定理`thm:wavelet-moment-decay`不适用，只剩$2^{-j/2}$的粗略界，每层至多$L+1$个跨接缝小波。

###### paragraph：端点相容条件

1. 陈述连续和$m$次连续可微的周期延拓相容条件，逐阶核对。

2. 以$x(1-x)$为例，连续而有折角，计算$\widehat{x(1-x)}(n)=-1/(2\pi^2n^2)$，说明接缝正则性逐阶决定系数行为。

3. 图`fig:wavelet-extensions`：$x$的周期延拓、反射延拓与$x(1-x)$的周期延拓。

#### 15.5.3 区间边界的处理

1. 说明端点行为有实际意义时接缝跳跃会使系数失真，给出延拓与重建基函数两种思路。

###### paragraph：反射延拓

1. 定义反射延拓，连续函数的延拓自动连续。

2. 说明导数在端点不一定连续，需$f'(0)=0$。

3. 对$f(x)=x$算出周期$2$的三角波系数$((-1)^n-1)/(\pi^2n^2)$，指出比周期延拓快一阶，但停在$1/n^2$。

###### paragraph：边界小波

1. 说明保留内部小波、替换跨端点者为边界小波，目标是端点附近仍抵消低次多项式。

2. 列出需重新核对的正交或对偶关系、完备性、消失矩，具体实现归卷九第6章。

3. 引出表`tab:wavelet-boundary-methods`，并对比三种处理的适用对象与代价。

4. 表`tab:wavelet-boundary-methods`：周期化、反射延拓、边界小波的对比。

### 15.6 Fourier分解与小波分解的比较

正文：[06-fourier-wavelet-comparison.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/06-fourier-wavelet-comparison.tex)

1. 在$L^2(\mathbb T)$中把函数看成同一向量，提出两组标准正交基给出两套坐标。

2. 分别写出Fourier基与周期Haar基的系数。

3. 比较坐标组织方式，并引出图`fig:wavelet-coefficient-tiles`。

4. 图`fig:wavelet-coefficient-tiles`：Haar细节系数在尺度—位置方格上的分布，以及跳跃函数的Fourier系数绝对值。

###### paragraph：平滑振荡

1. 取$g=\sin2\pi x$，Fourier系数只有$\hat g(\pm1)=\mp\mathrm i/2$两个非零。

2. 由和差化积算出Haar系数（式`eq:wavelet-sine-coefficients`）。

3. 逐层读公式：$d_{0,0}=2/\pi$，第$1$层全为零，$j\geq2$时全部非零且量级约$(\pi/2)2^{-3j/2}$。

###### paragraph：局部跳跃

1. 取$f=\mathbf 1_{[1/3,1)}$，算出Fourier系数绝对值$\lvert\sin(\pi n/3)\rvert/(\pi\lvert n\rvert)$，无穷多频率非零且按$1/\lvert n\rvert$衰减。

2. 由$t_j$的两种情形得每层只有一个非零Haar系数$-2^{-j/2}/3$（式`eq:wavelet-jump-coefficients`），用$4/9+2/9=2/3$核对能量。

###### paragraph：有限项的误差

1. 说明表中保留规则与误差即被丢弃系数的平方和。

2. 表`tab:wavelet-fourier-haar-budget`：两函数在若干截断下的非零项数与平方误差。

###### paragraph：读表

1. 对跳跃函数按固定项数比较，Haar与Fourier相当，误差都与项数大致成反比。

2. 按非零系数比较，Haar用$7$项达$0.00347$而Fourier用$7$项只有$0.0227$，优势要求自适应选项。

3. 对平滑振荡结论相反，Fourier两项精确，Haar每层缩小约四倍。

4. 以$\mathbb R^N$中同一向量可在不同基下稀疏或稠密为类比，说明稀疏性是函数与基的搭配，一般刻画归第20章。

### 15.7 本章小结

正文：[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/06-wavelet-transform/07-summary.tex)

1. 重申目标：小波系数是换到多尺度标准正交基后的坐标，按$(j,k)$排成数表。

2. 总结有限Haar变换：平均半差、局部性、正交化、各行为新基。

3. 总结区间上的尺度空间、细节空间及$2^{-J/2}$归一化。

4. 总结稠密性、Haar展开与Parseval，以及粗项不可省和收敛方式的差别。

5. 总结正交多分辨率分析、二尺度关系、母小波构造的奇偶两路证明及实轴上粗项消失。

6. 总结消失矩与光滑性分工，并复述$x^2$的Haar与D4系数对比。

7. 总结周期化、周期延拓、反射延拓与边界小波的条件与局限。

8. 总结Fourier与小波比较，并指向第20章与第22章。

## 第16章 线性泛函

正文入口：[07-linear-functionals.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals.tex)，章内依次输入[01-functionals.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/01-functionals.tex)、[02-representation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/02-representation.tex)、[03-extension.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/03-extension.tex)、[04-uniform-boundedness.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/04-uniform-boundedness.tex)、[05-weak-convergence.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/05-weak-convergence.tex)、[06-ball-compactness.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/06-ball-compactness.tex)、[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/07-summary.tex)。

章职责与主线：本章沿用第10章把函数看成无限维向量的类比，研究函数空间里的“行向量”，即把函数读成一个标量的线性规则。先用有限个分量上的行向量读取引出加权积分、正交系数、点评估和平方范数，再用常数界刻画连续性并定义泛函范数；把全部连续线性读取组成完备的对偶空间，在Hilbert空间和$\sigma$有限的$L^p$（$1\leq p<\infty$）中证明内积表示与权重函数表示；一般赋范空间中用Hahn--Banach延拓得到距离泛函、范数的对偶表示与$\ell^\infty$上不来自$\ell^1$的泛函，用Baire纲定理证明一致有界原理。后半章由读取定义弱收敛与弱星收敛，给出弱收敛列的范数控制，证明对偶闭球的弱星紧性与反射空间闭球的弱紧性，并分别交代提取收敛子列所需的条件。全章逐处说明行向量类比在哪里失效。

1. 章首第一段回到第10章的无限维向量图景，指出行向量乘列向量是一次读取，本章研究函数空间里的行向量，并以区间平均、Fourier系数和点值为例。

2. 第二段对比平均值与点值在扰动下的不同表现，提出三个问题：哪些读取能由范数稳定控制，这些读取具体长什么样，子空间上的读取能否扩展到全空间。

3. 第三段说明有限维经验的保留与失效：连续读取在Hilbert空间中是内积、在$L^p$中是权重函数，但线性读取可以不连续、行向量全体可以比原空间大；Hahn--Banach定理和完备性分别提供补救和统一控制。

4. 第四段说明后半章转向读取，引出弱收敛和弱星收敛，并回指第10章的闭球不紧，列出要回答的范数界与子列问题。

5. 第五段划定范围：只讨论标量输出，算子在第17章，变分与优化由卷五承担，并列出拓扑、度量和具体函数空间的来源。

### 16.1 泛函的定义

正文：[01-functionals.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/01-functionals.tex)

1. 从温度平均、Fourier系数、点值都是输入整个函数、输出一个标量进入，给出泛函的名称，并固定标量域$\mathbb K$。

2. 定义`def:lfunc-functional`：线性空间到标量域的映射称为泛函，满足线性组合条件（式`eq:lfunc-linearity`）者为线性泛函。

3. 说明线性泛函$\ell$不带上标，与数列空间$\ell^p$靠上标区分。

4. 在$\mathbb K^d$中由$a_k=\ell(e_k)$把线性泛函写成行向量，引向卷二第5章，并指出函数空间中的新问题是线性泛函未必连续。

#### 16.1.1 常见泛函

1. 预告先用有限个分量读取、再让分量增加到无穷多，并强调每个例子须说清作用的空间。

###### paragraph：行向量读取列向量

1. 沿用第10章的数据，把$f(t)=t^2$在四个等距点上的取值写成列向量。

2. 分别用均匀权重的行向量和只取第三分量的行向量读取，算得$\tfrac7{18}$与$\tfrac49$，说明两种读取的含义。

3. 把采样点增到$n$个，均匀权重的读数为$\frac{2n-1}{6(n-1)}$，$n=4$、$n=40$时分别验算，$n\to\infty$时趋于$\int_0^1t^2\,dt=\tfrac13$。

4. 由此说明下标连成一片时行向量变成权重函数、读取变成积分，$\tfrac1n$相当于$dt$；单点权重的极限则是另一种读取，并解释配图中面积读数与单条竖线读数的差别。

5. 配图`fig:lfunc-row-readout`：同一函数$f(t)=t^2$在权重$1$、权重$t$和单点$\tfrac23$下的三个读数$\tfrac13,\tfrac14,\tfrac49$。

###### paragraph：加权积分

1. 引入共轭指数及端点约定，对$g\in L^q$定义$L_g(f)=\int fg\,d\mu$（式`eq:lfunc-weighted-integral`），指出它是行向量的连续版本。

2. 核对三件事：由Hölder不等式积分收敛，线性来自积分线性，几乎处处相等的代表给出相同读数，说明积分对零测集不敏感。

###### paragraph：正交系数

1. 在Hilbert空间中定义第$k$个系数，按第12章约定内积对第二个变量线性，故它是线性泛函，在$L^2(0,1)$中是以$\overline{e_k}$为权重的积分。

2. 取单位向量$\sqrt2\sin(\pi t)$，两次分部积分算出$f(t)=t^2$的系数$\sqrt2(\pi^2-4)/\pi^3\approx0.268$。

###### paragraph：点评估

1. 在$C(K)$中定义点评估泛函，线性来自逐点运算，它是单分量行向量的连续版本。

2. 指出类比的第一个边界：单点权重找不到函数充当，$L^p(0,1)$中$f$与$f+\mathbf 1_{\{x_0\}}$同类而点值不同，读取$x_0$处的值不是$L^p$上的映射；对比积分对零测集不敏感而点评估只看零测集。

###### paragraph：平方范数

1. 由$\lVert2f\rVert^2=4\lVert f\rVert^2$说明平方范数非线性，它是二次式而非行向量读取；非线性泛函的变分与极小化引向卷五第11章。

2. 引出汇总表。

3. 表`tab:lfunc-readouts`：四个泛函的行向量类比、定义域与是否线性。

#### 16.1.2 泛函范数

1. 由$\mathbb R^d$上的Cauchy--Schwarz不等式说明行向量都有有限放大倍数，指出无限维中行向量长度可能为无穷大，连续性不再自动成立。

2. 回用第3章的距离判据写出$\ell$在$x_0$处连续的含义。

3. 定理`thm:lfunc-continuity-bounded`：线性泛函的零点连续、处处连续与存在常数界三条等价。

4. 证明：由常数界经线性得处处连续，处处连续含零点连续；由零点连续取$\varepsilon=1$，把$x$缩放进小球再放大回去，得$C=2/\delta$。

5. 总结线性的两次作用，定义有界线性泛函，说明有界与连续同义，且这里的有界指单位球上有界。

6. 指出最小常数就是行向量长度在无限维中的替代，引出下一定义。

7. 定义`def:lfunc-functional-norm`：单位球上读数的上确界（式`eq:lfunc-functional-norm`）。

8. 由缩放得到基本不等式（式`eq:lfunc-norm-bound`），说明泛函范数是最小常数和最大放大倍数，并以行向量$[3,4]$的范数$5$验算。

###### paragraph：点评估的范数依赖空间

1. 在一致范数下由$\lvert f(0)\rvert\leq\lVert f\rVert_\infty$及$f\equiv1$得$\lVert\delta_0\rVert=1$。

2. 改配积分范数，引入尖峰$\tau_n$，算出$\lVert\tau_n\rVert_1=1/(2n)$与$\lVert\tau_n\rVert_2=1/\sqrt{3n}$。

3. 由$\tau_n(0)/\lVert\tau_n\rVert_2=\sqrt{3n}$无界得出$\delta_0$在$L^2$范数下线性、处处有定义却不连续，这在有限维不会发生。

4. 配图`fig:lfunc-spike-norm`：尖峰族，以及读数不变而两种积分范数趋于零的对数坐标对比。

###### paragraph：加权积分的范数也依赖空间

1. 在$L^2(0,1)$上取$g=\mathbf 1_{[0,1/2]}$，由Hölder上界和$f=g$取等得$\lVert L_g\rVert=1/\sqrt2$。

2. 同一规则在一致范数下由区间长度$\tfrac12$和$f\equiv1$得范数$\tfrac12$，说明稳定性依赖所选空间与范数。

### 16.2 泛函的表示

正文：[02-representation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/02-representation.tex)

1. 由逐个读取转向全部连续线性读取，预告Hilbert空间中的内积表示和$L^p$空间中的权重函数表示。

#### 16.2.1 对偶空间

1. 类比行向量全体成线性空间，说明有界线性泛函的和与数乘封闭，并由逐点估计得到三角不等式。

2. 定义`def:lfunc-dual-space`：对偶空间$X^*$与二次对偶空间$X^{**}$。

3. 解释二次对偶是读取规则的读取规则，有限维中列向量读行向量不产生新东西，无限维中$X^{**}$可以比$X$大。

###### paragraph：对偶范数可以不同于原范数

1. 在$(\mathbb R^2,\lVert\cdot\rVert_1)$上逐项估计线性泛函的读数，得到上界$\max(\lvert a_1\rvert,\lvert a_2\rvert)$。

2. 选合适的标准基向量取等，得范数公式；以$\bm a=(2,-3)$对比长度$3$与欧氏长度$\sqrt{13}$，引入对偶范数。

###### paragraph：对偶空间总是完备的

1. 提出$X^*$总完备，原因是读数取值在完备的$\mathbb K$中。

2. 定理`thm:lfunc-dual-complete`：任意赋范空间的对偶空间是Banach空间。

3. 证明：逐点取极限得线性泛函，由一致估计令$m\to\infty$，得极限有界且$\ell_n\to\ell$。

4. 以不完备的多项式空间为例，说明需要完备性的论证可以放到$X^*$上，指向一致有界与弱收敛的使用。

#### 16.2.2 Hilbert空间的泛函表示

1. 由有限维中行向量即转置，定义$\ell_h=\langle h,\cdot\rangle$，用Cauchy--Schwarz和$f=h/\lVert h\rVert$得$\lVert\ell_h\rVert=\lVert h\rVert$。

2. 提出反方向问题：每个连续线性泛函是否都是某向量的内积。

###### paragraph：零空间与法方向

1. 以$\mathbb R^2$上的$\ell(x)=3x_1+4x_2$为例，给出零空间、等值线和单位法向$w=(\tfrac35,\tfrac45)$，$\ell(w)=5$。

2. 对$f=(4,-1)$算出$\ell(f)=8$，减去$w$的倍数后落入零空间并验算，得到$h=\ell(w)w=(3,4)$，其长度$5$就是泛函范数。

3. 配图`fig:lfunc-riesz-level-sets`：零空间、等值线、表示向量、单位圆切线与$f$的投影。

4. 指出无限维中只需把找垂直方向换成正交投影定理，并由连续性证明零空间是闭的真子空间，引出定理名称。

5. 定理`thm:lfunc-riesz`：Riesz表示定理（式`eq:lfunc-riesz`），表示向量唯一且范数相等。

6. 证明：由正交投影得$w\perp N$且$\ell(w)\neq0$；用$f-\frac{\ell(f)}{\ell(w)}w\in N$解出读数，写出带共轭的表示向量；再证唯一性与范数。

7. 说明证明不要求可分；对应$\ell\mapsto h_\ell$在复空间共轭线性，对应行向量是共轭转置，实空间中$H^*$与$H$等同。

###### paragraph：$L^2$中的读取与方向

1. 写出整体平均、正交系数和$\int_0^1tf$的表示向量，算得后者范数$1/\sqrt3$，并用$\sqrt3\,t$验证取到范数。

###### paragraph：表示以连续性和完备性为前提

1. 用尖峰证明$(C([0,1]),\lVert\cdot\rVert_2)$上的点评估没有表示向量，说明单点权重不是平方可积函数。

2. 用$\int_0^{1/2}f$说明不完备时有界读取可以没有表示向量：表示函数只能是没有连续代表的指示函数。

3. 指出点评估连续的完备内积函数空间引向第23章再生核Hilbert空间。

#### 16.2.3 $L^p$空间的泛函表示

1. 说明$L^p$中无内积，候选是加权积分，这是有限维$\ell^1$与$\ell^\infty$互为对偶的推广，并提出反方向问题。

2. 定理`thm:lfunc-lp-dual`：$\sigma$有限、$1\leq p<\infty$时，每个连续线性泛函都是$L^q$权重的积分（式`eq:lfunc-lp-dual`），权重几乎处处唯一且范数相等。

3. 说明先在实值上证明、复值的处理方法，并列出证明三步。

###### paragraph：范数等式与唯一性

1. 对$1<p<\infty$取对齐输入$f=\lvert g\rvert^{q-1}\operatorname{sgn}g$，用$(q-1)p=q$算出比值等于$\lVert g\rVert_q$。

2. 对$p=1$在接近本性上确界的正测度有限集上取平均，用逼近得到范数等式。

3. 由范数等式推出权重几乎处处唯一，并说明这与$L^q$元素是等价类一致。

###### paragraph：有限测度下构造表示函数

1. 从$\ell$怎样读指示函数入手，定义集函数$\nu(E)=\ell(\mathbf 1_E)$。

2. 由线性得有限可加，由$p<\infty$时的范数收敛得可数可加，由$\lvert\nu(E)\rvert\leq\lVert\ell\rVert\mu(E)^{1/p}$得$\nu$是对$\mu$绝对连续的有限有符号测度。

3. 用第5章的Jordan分解和第8章的Radon--Nikodym定理得到$g\in L^1$，再由线性推到简单函数。

###### paragraph：表示函数属于$L^q$

1. 对$1<p<\infty$用$\lvert g\rvert\leq n$上的截断对齐输入$f_n$，说明简单函数逼近使等式对$f_n$成立。

2. 记$I_n=\int_{E_n}\lvert g\rvert^q$，由$I_n\leq\lVert\ell\rVert I_n^{1/p}$和单调收敛得$\lVert g\rVert_q\leq\lVert\ell\rVert$。

3. 对$p=1$用反证：若$g$在正测度集上超过$\lVert\ell\rVert$，取归一化指示函数得矛盾。

4. 说明简单函数在$L^p$中稠密的理由（单调逼近与控制收敛），由连续性得$\ell=L_g$。

###### paragraph：推广到$\sigma$有限测度

1. 用递增的有限测度集$A_k$限制$\ell$，得$g_k$且范数受$\lVert\ell\rVert$控制。

2. 由唯一性拼成全空间的$g$，单调收敛给出范数界，并由$f\mathbf 1_{A_k}\to f$推出$\ell=L_g$。

3. 说明$p=1$时$\sigma$有限不能去掉，$1<p<\infty$时可推广到任意测度，读者可查阅Folland。

4. 例`ex:lfunc-l3-norm`：$L^3(0,1)$上的$\int_0^1tf$，由定理得范数$(2/5)^{2/3}\approx0.543$，再用$t^{1/2}$直接验算。

5. 比较同一权重$t$在不同$L^p$上的读取，解释$p$增大时单位球变小、范数从$1$降到$\tfrac12$，$p=1$时取不到。

6. 表`tab:lfunc-lp-row`：$p=1,2,3,\infty$时的共轭指数、范数和取到范数的输入。

###### paragraph：端点$p=\infty$

1. 说明$p=\infty$时$L_g$仍是读取，但连续线性泛函不能全部写成这种形式，预告用延拓构造反例，指出“行向量全体就是共轭指数空间”在此失效。

### 16.3 泛函的延拓

正文：[03-extension.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/03-extension.tex)

1. 指出一般赋范空间没有表示定理，甚至不知$X^*$是否有足够多的元素；回顾Hilbert空间中向量被自己的内积识别，提出先在小子空间上定义再保范数扩展。

2. 类比为补全行向量的其余权重且不增大放大倍数，预告延拓及其对读出范数、区分向量的用途。

#### 16.3.1 Hahn--Banach延拓

1. 提出保范数延拓的问题，指出难点在于$M$外的取值也要满足常数不超过$\lVert\ell\rVert$的基本不等式。

2. 定理`thm:lfunc-hahn-banach`：子空间上的有界线性泛函可以保范数地延拓到全空间。

3. 给出定理名称，说明先完整证明延拓一维的步骤。

###### paragraph：延拓一维

1. 在实情形归一化，说明延拓由数$t=L(z)$决定，写出范数约束。

2. 除以$\lvert s\rvert$并换元，得到$t$的上下界约束（式`eq:lfunc-hb-interval`）。

3. 把$t$的存在化为上确界不超过下确界，由$\lVert\ell\rVert\leq1$和三角不等式验证，得到非空闭区间。

###### paragraph：一个可以手算的延拓

1. 在$\mathbb R^2$上取横轴$M$、$\ell(s,0)=s$、$z=(0,1)$，写出$L_t(\bm x)=x_1+tx_2$，准备在两种范数下计算$t$的范围。

2. 在$\lVert\cdot\rVert_1$下写出上下界函数，算得$t\in[-1,1]$，并与$\lVert L_t\rVert=\max(1,\lvert t\rvert)$对照。

3. 在欧氏范数下上下界函数只在$a\to\pm\infty$时闭合于$0$，延拓唯一。

4. 解释配图：下排是上下界函数，上排是菱形顶点处的多条支撑线与圆的唯一切线。

5. 配图`fig:lfunc-hb-support`：两种单位球的支撑线，以及两种范数下式`eq:lfunc-hb-interval`的上下界函数和$t$的可选范围。

6. 说明定理只保证存在，保持的只有$M$上的取值和范数上界。

###### paragraph：从一维到全空间

1. 可分时取可数稠密集逐个添加，再由一致连续唯一延拓到闭包，范数不变。

2. 不可分时说明Zorn引理的做法和极大元的定义域必为全空间，指明这一部分用到选择公理，读者可查阅Folland。

###### paragraph：复空间

1. 由$\operatorname{Im}\ell(m)=-u(\mathrm im)$把复线性泛函写成实部的公式，延拓实部$U$后定义$L$。

2. 验证$L(\mathrm ix)=\mathrm iL(x)$，从而$L$复线性且在$M$上等于$\ell$。

3. 用相位旋转把$\lvert L(x)\rvert$化为$U$在旋转向量上的值，得$\lVert L\rVert\leq\lVert\ell\rVert$，反向不等式来自$L$延拓$\ell$。

###### paragraph：区分向量与子空间

1. 提出用一个读取分开向量与闭子空间：在子空间上为零而读出距离。

2. 定理`thm:lfunc-distance-functional`：闭子空间外的点有范数为$1$、在子空间上为零、读出距离$d$的连续线性泛函。

3. 证明：由闭性得$d>0$；在$M\oplus\operatorname{span}\{x_0\}$上定义读取，估计范数，由极小化序列得范数为$1$，再延拓。

4. 例：$C([0,1])$中常数子空间与$x_0(t)=t$，$d=\tfrac12$，$L(f)=(f(1)-f(0))/2$，逐项验算。

###### paragraph：$\ell^\infty$上不来自$\ell^1$的泛函

1. 在收敛数列子空间上定义取极限的泛函$\lambda$，范数为$1$，延拓为$\Lambda\in(\ell^\infty)^*$。

2. 假设$\Lambda$来自$y\in\ell^1$，用$\bm e_k$得$y_k=0$，与$\Lambda(1,1,\ldots)=1$矛盾。

3. 解释$\Lambda$对每个分量的权重都是零却能读出极限，只看无穷远处的行为，这是行向量类比的又一个边界；$\Lambda$无显式公式，后面还要使用。

#### 16.3.2 范数的对偶表示

1. 回顾Hilbert空间中单位读取读出范数，提出在一般空间中用一维子空间上的规定再延拓。

2. 定理`thm:lfunc-norming`：存在单位泛函读出$\lVert x\rVert$，范数等于单位泛函读数的最大值（式`eq:lfunc-norm-dual`），全部读取能区分向量。

3. 证明：一维子空间上定义读取并延拓；由基本不等式和取等得最大值公式；对$x-y$取这样的读取区分向量。

4. 解释向量长度由全部单位读取恢复，并指出范数与对偶范数的对称。

###### paragraph：具体空间中的取范读取

1. 写出$C([0,1])$中带相位的点评估和实值$L^p$中的归一化权重，由$(p-1)q=p$验证；说明定理在写不出读取时仍保证存在。

2. 说明凸集分离与优化对偶是同一延拓思想的几何形式，引向卷五第5章。

### 16.4 泛函族的一致有界性

正文：[04-uniform-boundedness.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/04-uniform-boundedness.tex)

1. 定义逐点有界和一致有界，说明下一节需要这种统一控制。

2. 对比两者的量词次序，说明有限维只需在基上读取，无限维不再成立。

###### paragraph：不完备时可以失败

1. 在$c_{00}$上配最大值范数，取$\ell_n(x)=nx_n$，逐点有界而$\lVert\ell_n\rVert=n$，并指出$c_{00}$不完备。

###### paragraph：需要的工具

1. 由第2章Baire纲定理的稠密开集形式，用取补集得到闭集覆盖中必有一个含开球的形式。

2. 定理`thm:lfunc-uniform-boundedness`：Banach空间上逐点有界的泛函族范数一致有界（式`eq:lfunc-uniform-bound`）。

3. 给出定理名称和证明的四步顺序。

4. 证明：闭集$F_k$覆盖空间，Baire纲定理给出含开球的$F_{k_0}$，平移到原点得$2k_0$的界，缩放到单位球得$\lVert\ell_\alpha\rVert\leq2k_0/r$。

###### paragraph：完备性用在哪里

1. 在$c_{00}$例子中$F_k$覆盖空间但都不含开球，指出论证失败在Baire纲定理，说明完备性完成量词交换。

###### paragraph：能读所有平方可和序列的行向量

1. 设$\sum_ky_kx_k$对每个$x\in\ell^2$收敛，把截断读取$\ell_n$写出并算出其范数。

2. 由逐点收敛和一致有界原理得$y\in\ell^2$，即能读遍$\ell^2$的行向量本身在$\ell^2$中。

3. 取$y_k=k^{-1/2}$，构造$x_k=1/(\sqrt k\log(k+1))\in\ell^2$使级数发散，验证定理的逆否形式。

4. 说明算子版本的一致有界原理在第17章，本章把泛函情形用于弱收敛列。

### 16.5 弱收敛与弱星收敛

正文：[05-weak-convergence.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/05-weak-convergence.tex)

1. 由无限维中范数收敛要求过强，提出只要求每个固定的连续线性读取收敛。

2. 类比逐分量收敛，说明这里的分量是全部连续线性读取；区分弱收敛与弱星收敛的读取来源，预告范数控制。

#### 16.5.1 弱收敛

1. 用有限个读取的误差约束定义基本邻域（式`eq:lfunc-weak-neighborhood`）。

2. 定义`def:lfunc-weak-topology`：弱开集、弱拓扑与弱收敛。

3. 核对弱开集对并与有限交封闭。

4. 证明基本邻域本身是弱开集。

5. 定理`thm:lfunc-weak-criterion`：弱收敛等价于每个连续线性读取收敛（式`eq:lfunc-weak-criterion`），弱极限唯一。

6. 证明：两个方向分别用单个读取的邻域和有限个$N_i$取最大值；唯一性来自读取能区分向量。

7. 说明唯一性依赖Hahn--Banach定理，并写出Hilbert空间中的形式。

8. 定理`thm:lfunc-strong-implies-weak`：范数收敛推出弱收敛。

9. 证明：由基本不等式直接得到。

###### paragraph：逆向不成立

1. 以$\ell^2$的$\bm e_n$为例：两两距离$\sqrt2$，而$\langle y,\bm e_n\rangle\to0$；由Bessel不等式推广到任意标准正交序列。

2. 以$\sin(nx)$为例，用读取窗口$[0,1]$算出$(1-\cos n)/n$和范数$\sqrt\pi$，并给出$n=1,12$的数值。

3. 解释正负抵消和能量转移到高频，指明弱收敛失去的是对整体能量的控制。

4. 配图`fig:lfunc-weak-oscillation`：$\sin(12x)$与窗口内的抵消，读数绝对值与$2/n$的衰减和不变的$L^2$范数。

###### paragraph：无限维中弱邻域很大

1. 由有限个泛函的公共零空间含非零向量，推出无限维中每个弱邻域无界，弱拓扑严格弱于范数拓扑。

2. 结合配图说明一个读取给出板状区域、两个读取给出管状区域，无限维中总留下无穷多方向；对比有限维弱收敛与范数收敛一致。

3. 配图`fig:lfunc-weak-neighborhood`：$\mathbb R^3$中一个读取和两个读取的邻域与范数球。

###### paragraph：部分读取不能代替全部读取

1. 取$x_n=n\bm e_n$，坐标泛函的读数都趋于零，故若弱收敛极限只能是零。

2. 取$y=(1/k)_k$得读数恒为$1$，所以不弱收敛，说明坐标泛函虽稠密却只是部分读取。

3. 说明有统一范数界时，稠密读取集上的收敛可推到全部读取，$\ell^2$中有界且逐坐标收敛的序列弱收敛。

#### 16.5.2 弱星收敛

1. 提出变化的对象本身是读取时，只用原空间向量检验，给出基本邻域（式`eq:lfunc-weak-star-neighborhood`）。

2. 定义`def:lfunc-weak-star`：弱星拓扑与弱星收敛。

3. 说明弱星收敛等价于逐向量求值收敛，弱星极限唯一且不需要延拓定理。

4. 以$\delta_{1/n}\overset{*}{\rightharpoonup}\delta_0$为例，并由$\lVert\delta_s-\delta_t\rVert=2$说明它不按范数收敛。

###### paragraph：谁读谁

1. 比较$\sigma(X^*,X)$与$\sigma(X^*,X^{**})$，由$X$嵌入$X^{**}$得对偶空间中弱收敛推出弱星收敛（式`eq:lfunc-weak-implies-weak-star`），逆向一般不成立。

2. 配图`fig:lfunc-who-reads-whom`：三种拓扑的读取者与自然嵌入$J$。

3. 例`ex:lfunc-weak-star-not-weak`：$\ell^1$的对偶$\ell^\infty$中尾部指示序列弱星收敛到零，用$\Lambda$证明它不弱收敛。

#### 16.5.3 弱收敛列的范数控制

1. 提出把向量看成对偶空间上的读取，其范数等于向量范数。

2. 定理`thm:lfunc-weak-bounded`：弱收敛列有界且范数下半连续（式`eq:lfunc-weak-lsc`）。

3. 证明：把$x_n$看成$X^*$上的泛函$\Phi_n$，由$X^*$完备和一致有界原理得有界；对单位读取取极限再取最大值得下半连续。

4. 说明完备性用在$X^*$上，$\bm e_n$说明不等式可严格，弱极限允许能量消失。

###### paragraph：弱星收敛列

1. 在Banach前对偶上由一致有界原理得弱星收敛列有界，再由单位向量上的极限得范数下半连续。

2. 用$c_{00}$说明前对偶完备性不能省。

###### paragraph：有界只是必要条件

1. 无界序列不弱收敛；对$\sqrt n\,\bm e_n$构造只在$k=4^j$处非零的$y\in\ell^2$，读数在$0$与$1$间不收敛。

2. 用$(-1)^n\bm e_1$说明有界不能反推收敛，引出下一节的子列问题。

### 16.6 闭球的紧性

正文：[06-ball-compactness.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/06-ball-compactness.tex)

1. 由有限维闭球紧和无限维范数下不紧，提出要分清闭球所在空间、拓扑以及紧性能否转为子列，并预告本节三步。

2. 固定$B_X$与$B_{X^*}$的记号。

#### 16.6.1 对偶闭球的弱星紧性

1. 解释开集越少紧性越容易成立，引出定理。

2. 定理`thm:lfunc-banach-alaoglu`：任意赋范空间的对偶闭单位球在弱星拓扑下紧。

3. 给出定理名称，把泛函看成以$X$的元素为下标的无限长向量。

4. 结合配图说明每个下标上的竖条长度由范数限定，线性条件把选点绑在一起。

5. 配图`fig:lfunc-alaoglu-product`：$X=\mathbb R^2$中五个向量上的竖条与两个单位球内泛函的折线。

6. 把图写成论证：作闭圆盘的乘积$P$，单射放入$P$，说明弱星拓扑就是乘积拓扑的限制。

7. 证明像集在$P$中闭：每个线性条件只涉及三个坐标，且自动满足范数约束。

8. 说明一般情形还需要Tychonoff定理，它用选择公理且未证明，读者可查阅Folland；承认后定理得证，可分情形在后文完整证明。

###### paragraph：推广到任意闭球

1. 用平移缩放$T(\ell)=\ell_0+r\ell$是弱星同胚，推出任意有限半径闭球弱星紧。

###### paragraph：定理断言了什么

1. 说明定理不要求完备，断言的是$X^*$的闭球在$\sigma(X^*,X)$下紧，并用$\ell^\infty$中的$\bm e_n$说明范数下不紧。

#### 16.6.2 反射性

1. 由有限维中列向量也读行向量，引出用$x$读泛函的自然映射。

2. 定义`def:lfunc-reflexive`：自然嵌入（式`eq:lfunc-canonical-embedding`）与反射空间。

3. 验证$J(x)\in X^{**}$，由范数的对偶表示得$J$等距。

4. 说明反射空间自动完备，且定义要求特定的$J$满射，提及James的反例。

###### paragraph：Hilbert空间是反射的

1. 用共轭线性双射$R$和两次Riesz表示，把$\Phi\in H^{**}$写成$J(x)$。

###### paragraph：$L^p$空间（$1<p<\infty$）是反射的

1. 两次使用$L^p$对偶表示，把$\Phi\in(L^p)^{**}$写成$J(f)$，说明端点被排除的原因。

###### paragraph：完备而不反射

1. 把$\Lambda\in(\ell^1)^{**}$与$J(x)$比较，用$\bm e_k$得$x=0$的矛盾，证明$\ell^1$不反射。

2. 对比完备性与反射性，预告$L^1(0,1)$也不反射。

#### 16.6.3 反射空间中的弱紧性

1. 说明反射时$J$把$B_X$恰好映成$B_{X^{**}}$。

###### paragraph：两种拓扑的对应

1. 比较$\sigma(X,X^*)$与$\sigma(X^{**},X^*)$的基本邻域，用满射得它们一一对应，$J$是同胚。

2. 说明由此可把Banach--Alaoglu定理带回$X$。

3. 定理`thm:lfunc-reflexive-weak-compact`：反射空间的闭球弱紧。

4. 证明：对$X^*$应用Banach--Alaoglu定理，经同胚$J^{-1}$带回，平移缩放得任意闭球。

5. 列举Hilbert和$L^p$空间，并用$\bm e_n$说明弱紧不是范数紧。

#### 16.6.4 收敛子列的提取

1. 区分紧性与子列，引第2章的等价与互不蕴含，说明弱拓扑一般不可度量，不能直接提取子列。

###### paragraph：可分前对偶下弱星拓扑可度量

1. 由可数稠密集构造$B_X$中的稠密列$z_k$并验证稠密性。

2. 把可数个分量上的误差加权求和，定义度量（式`eq:lfunc-weak-star-metric`），验证其为度量。

3. 引理`lem:lfunc-weak-star-metric`：在$B_{X^*}$上度量拓扑与弱星拓扑相同。

4. 证明：有限项控制和尾项估计给出一个方向；用$z_{k_i}$逼近$u_i$并由单位球界控制给出另一方向。

5. 指出统一的范数界起关键作用，整个$X^*$上度量一般不能给出弱星拓扑。

6. 引出可分时的对角线构造。

7. 定理`thm:lfunc-weak-star-subsequence`：可分时$X^*$中有界序列有弱星收敛子列。

8. 证明：对角线取子列使在$z_k$上收敛，由$\varepsilon$逼近扩展到全部向量，极限是有界线性泛函。

9. 取$C=1$得$B_{X^*}$序列紧，结合度量空间中序列紧与紧的等价和引理，给出可分时Banach--Alaoglu定理的完整证明。

###### paragraph：可分性不能省

1. 在$(\ell^\infty)^*$中取坐标泛函，用符号交替的$x$说明无弱星收敛子列，紧与序列紧分开。

###### paragraph：反射空间中的弱子列

1. 陈述Eberlein--\v{S}mulian定理并说明不证，引出合并结论。

2. 定理`thm:lfunc-reflexive-subsequence`：反射空间中有界序列有弱收敛子列。

3. 证明：闭球弱闭且弱紧，反射空间是Banach空间，由Eberlein--\v{S}mulian定理得子列。

4. 列举适用空间，并用$\bm e_n$和$(-1)^n\bm e_1$说明。

###### paragraph：非反射空间中可以失败

1. 在$L^1(0,1)$中取$f_n=n\mathbf 1_{(0,1/n)}$，假设子列弱收敛，准备用两个读取得矛盾。

2. 用远离原点的读取和控制收敛得$\int_0^1f=0$。

3. 用整体积分得$\int_0^1f=1$，矛盾，所以没有弱收敛子列。

4. 结合配图解释质量向左端点集中，由逆否命题得$L^1(0,1)$不反射。

5. 配图`fig:lfunc-mass-concentration`：$f_n$的图像和三个读取的取值。

6. 说明在$C([0,1])^*$中极限以点评估$\delta_0$的形式出现，回到单点权重的含义。

### 16.7 本章小结

正文：[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/07-linear-functionals/07-summary.tex)

1. 回到开头的问题，综述泛函、定义域差异、连续性与泛函范数，以点评估说明依赖范数。

2. 综述对偶空间的完备性、Hilbert空间的内积表示及前提、$L^p$的权重表示及端点。

3. 综述Hahn--Banach延拓及其推论、$\ell^\infty$上的非序列读取和一致有界原理。

4. 综述弱收敛与弱星收敛的读取来源、与范数收敛的关系和范数控制。

5. 综述对偶闭球弱星紧、反射空间闭球弱紧和子列提取的条件，引出对比表。

6. 表`tab:lfunc-summary`：三种收敛的读取来源、单位球紧性与有界序列的子列。

7. 指向第17章，把标量输出推广为向量输出，说明本章工具在伴随与紧算子中的用途。

## 第17章 线性算子

正文入口：[08-linear-operators.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators.tex)，章内依次输入[01-operator-definition.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/01-operator-definition.tex)、[02-operator-norm.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/02-operator-norm.tex)、[03-inclusion-maps.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/03-inclusion-maps.tex)、[04-operator-convergence.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/04-operator-convergence.tex)、[05-adjoint-operators.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/05-adjoint-operators.tex)、[06-compact-operators.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/06-compact-operators.tex)、[07-fundamental-theorems.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/07-fundamental-theorems.tex)、[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/08-summary.tex)。

章职责与主线：本章把第16章的标量观测推广为函数到函数的线性变换，并沿用第10章把函数看成无限维向量的类比，把线性算子读作无限维矩阵、把积分核读作矩阵元素，同时逐处说明类比在哪里需要修正。先列出恒等、投影、乘法、积分与求导等例子并区分“公式可写”与“算子已定义”；再用统一常数定义有界性与算子范数，以差分矩阵、求导和平方可积核说明条件的作用，并给出运算的范数估计与算子空间的完备性；随后用包含映射比较同一函数在不同空间中的大小，比较算子列的范数收敛与强收敛。后三节加入结构：Hilbert空间中的伴随与像、零空间的正交关系，自伴与正算子；紧算子及其在Hilbert空间中的有限秩逼近，并证明平方可积核给出紧算子；最后在完备空间中建立一致有界原理、开映射与有界逆定理及闭图判别。全章以$[-1,1]$上$\mathrm d\mu=\mathrm dz/2$与核$1+xz$的积分算子、$\ell^2$上的对角算子$(x_n/n)$、右移和累积积分$V$作贯穿例子；谱与展开留给第18章，方程可解性留给第19章。

1. 章首第一段以投影、核积分与求导把函数变成函数进入，并与第16章把函数压成一个读数的泛函对照，确定本章的输入和输出都是函数。

2. 第二段回用第10章的$[\ldots,f(x),\ldots]$，提出向量的线性变换是矩阵、函数的线性变换就是无限维矩阵，给出线性算子这一名称的直观来源。

3. 第三段比较矩阵的按行求和与积分算子，写出式`eq:lop-matrix-integral`，说明核$k(x,y)$就是矩阵元素、$x$为行号、$y$为列号，并引出对应表。

4. 表`tab:lop-dictionary`逐行列出矩阵元素与核、求和与积分、全体输入与定义域、最大放大倍数与算子范数、共轭转置与伴随、低秩近似与有限秩逼近，并在第三列写明每项类比需要修正之处。

5. 第四段归纳有限维经验失效的三处：积分可能发散要写定义域，放大倍数可能无上界因而依赖范数，完备性开始起作用。

6. 第五段说明前四节的路线：17.1规定输入输出并举例，17.2定义有界性与算子范数，17.3把同一函数放进不同空间看成算子，17.4比较算子列的两种收敛。

7. 第六段说明后三节是矩阵其他结构的对应物：17.5的伴随对应共轭转置，17.6的紧算子对应低秩逼近，17.7在完备空间中建立三个基本定理。

8. 第七段划定范围：本章只建立算子本身的结构，$T-\lambda I$的稳定可逆、特征展开与奇异分解属于第18章，算子方程的可解性与稳定性属于第19章。

### 17.1 算子的定义

正文：[01-operator-definition.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/01-operator-definition.tex)

1. 以$L^2(0,1)$中投影到常数、对连续函数累积积分、对可导函数求导三种操作进入，指出每种操作都把函数变成函数。

2. 指出三者都保持线性组合，差别在于对输入的要求：投影与积分处处有意义，求导只对部分函数有意义，这是矩阵不会遇到而算子必须首先处理的差别。

#### 17.1.1 线性算子

1. 对比矩阵由形状确定输入输出空间、函数空间中作用规则先以公式出现，说明定义算子时必须把允许的输入集合与输出空间写进算子。

2. 定义：线性子空间$D(T)\subseteq X$上满足式`eq:lop-linearity`的$T:D(T)\to Y$称为线性算子，并按式`eq:lop-range-null`定义定义域、取值空间、像空间与零空间。

3. 解释$D(T)$须为线性子空间的理由，由线性得$T0=0$，说明像与零空间都是线性子空间。

4. 将像与零空间对应到矩阵的列空间与零空间，区分事先指定的取值空间和算子实际产生的像，二者相等时才称满射。

5. 用$Tx=Tz\Leftrightarrow x-z\in\ker T$说明零空间刻画输出中看不见的输入差别，得出单射等价于$\ker T=\{0\}$，并提醒函数空间中要在等价类意义下理解。

6. 指出秩—零化度公式没有对应物：方阵单射等价于满射，无限维中二者独立，以第17.5节的右移作预告。

7. 区分定义在整个$X$上的算子与只定义在真子空间上的算子，以求导只能作用于可导函数为例。

8. 说明两种情形要分开的原因：定义在真子空间上的算子是否有界取决于在该子空间上所配的范数。

9. 指出取值空间为标量域时线性算子就是第16章的线性泛函，相当于只有一行的矩阵，因此本章结论包含泛函情形。

#### 17.1.2 常见算子

1. 说明下面的例子在全章反复出现，逐例写出输入、输出与作用规则，核对线性并指出它相当于什么矩阵，重点是“公式可写”与“算子已定义”的差距。

###### paragraph：恒等映射与正交投影

1. 定义恒等算子并由定义核对线性，把它对应到单位矩阵，提醒复合时区分$I_X$与$I_Y$。

2. 回用第12章闭子空间上最近点与正交条件，得到正交投影$P_M:H\to H$。

3. 用“属于$M$且残差与$M$正交的元素唯一”验证$P_M$的线性，残差的线性组合单列为展示式。

4. 以$L^2(0,1)$中常函数子空间为例算出$P_Mf$是平均值，并指出这个算子的核是$k\equiv1$，每一行都把输入平均一次。

###### paragraph：固定函数相乘

1. 对$\varphi\in L^\infty(\mu)$定义乘法算子$M_\varphi f=\varphi f$，并按分量解释为对角矩阵的连续版本。

2. 逐项核对：作用对等价类有确定意义，由$\lvert\varphi f\rvert\leq\lVert\varphi\rVert_\infty\lvert f\rvert$得输出仍在$L^p(\mu)$中，线性来自分配律。

3. 用$(0,1)$上$\varphi=x^{-1}$与$f=1$说明对角元素无界时公式可写却不再给出$L^2$到$L^2$的算子。

###### paragraph：积分变换

1. 形式地写出式`eq:lop-integral-operator`，定义积分核与积分算子，按式`eq:lop-matrix-integral`说明$x$是行、$y$是列，$k(x,\cdot)$是一行的全部元素。

2. 用$[0,1]$上核$k\equiv1$说明$y^{-1/2}$可积而$y^{-1}$发散，开始说明“有意义”由核、测度和输入共同决定。

3. 把测度换成$y\,\mathrm dy$使$y^{-1}$的积分变为$1$，由此说明积分公式本身不是算子，要核对绝对收敛、可测性与输出空间，并预告17.2.1.2在平方可积核下完成检查。

4. 引入贯穿例子：$\mathrm d\mu=\mathrm dz/2$与核$1+xz$给出式`eq:lop-running-kernel`，输出总是一次函数，两个系数是输入的零阶与一阶矩。

5. 手算$f=1+x$的两个矩得$Tf=1+x/3$，并由$q=x^2-1/3$的两个矩为零得$q\in\ker T$。

6. 把$[-1,1]$四等分取中点$\pm1/4,\pm3/4$，每格测度$1/4$，写出矩阵元素$K_{ij}=1+x_ix_j$与求和近似。

7. 用输入在中点的值$(1/4,3/4,5/4,7/4)$和第一行元素算出$(Tf)(x_1)\approx49/64\approx0.766$，与准确值$0.75$对比。

8. 图`fig:lop-kernel-as-matrix`：(a)四阶矩阵、输入列与输出列，红框标第一行及其输出；(b)同一核的连续取值与$x=-3/4$的一行，展示矩阵元素如何过渡为核。

9. 解释图中(b)是格子无限加细后的样子，行变成水平切片，矩阵元素变成曲面上的点。

10. 说明类比的失效：恒等算子的矩阵集中在面积为零的对角线上，没有函数形式的核，求导相当于差分矩阵，同样没有。

###### paragraph：微分

1. 以$\lvert x-1/2\rvert$不可导说明求导不能定义在整个$C[0,1]$上。

2. 取定义域$C^1[0,1]$，得到定义在真子空间上的线性算子，并指出它也可视为从$C^1[0,1]$到$C[0,1]$的算子，两种看法的区别要到配置范数时才显现。

3. 归纳这些例子：恒等、投影与乘以有界函数定义在整个空间上，积分变换由核与测度保证定义，求导只能定义在部分函数上，由此转入范数的讨论。

### 17.2 算子范数

正文：[02-operator-norm.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/02-operator-norm.tex)

1. 由$T(x+e)=Tx+Te$说明输出误差只取决于扰动，把误差放大问题化为寻找统一常数。

2. 对比矩阵在紧的单位球上总取到最大放大倍数，算子的单位球不紧，放大倍数可能无穷，说明本节的路线。

#### 17.2.1 算子的有界性

1. 固定赋范空间与线性算子，提出用与输入无关的常数$C$控制输出，使输入误差$\lVert e\rVert$对应输出误差不超过$C\lVert e\rVert$。

2. 用式`eq:lop-bounded`定义有界线性算子与无界算子。

3. 澄清“有界”指比值有统一上界而非像集有界，并按线性缩放说明只需在单位球上检查。

4. 回用第3章的连续映射与Lipschitz映射，说明一般映射相差很远，而线性算子的情形由下面的定理统一。

5. 定理`thm:lop-bounded-continuous`：在$0$处连续、处处连续、Lipschitz与有界四条等价。

6. 证明的第一段由线性得（iv）推（iii），再依次得（iii）推（ii）、（ii）推（i）。

7. 证明的第二段开始证（i）推（iv）：取$\varepsilon=1$得到半径$\delta$的小球上输出不超过$1$。

8. 证明的第三段把任意$x$缩放到半径$\delta$，取$C=1/\delta$。

9. 指出关键在缩放，并说明有限维中线性映射总有界，无限维中要由下面两例分别看失败与成立。

##### 17.2.1.1 有界性依赖定义域范数

1. 用差分矩阵看求导：步长$h=1/n$时每行只有两个非零元素$\pm1/h$，网格加细时元素按$1/h$增大。

2. 取交错输入得到每个输出分量绝对值$2/h=2n$，以$h=1/4$时输入$(1,-1,1,-1,1)$输出$(-8,8,-8,8)$手算，并对比积分矩阵的元素带小因子$h$。

3. 回到连续情形，在定义域上用$\lVert\cdot\rVert_{C^1}$，得$\lVert Df\rVert_\infty\leq\lVert f\rVert_{C^1}$，$D$有界。

4. 在同一函数集合上只用一致范数，以$\sin(2\pi nx)$得比值$2\pi n$，$D$无界，并解释高频扰动的放大。

5. 总结求导公式与函数集合都未变，变化的是定义域范数，所以判断有界必须交代作用规则、定义域和两侧范数。

6. 指出只配一致范数的$C^1[0,1]$不完备，用$g_n=\sqrt{(x-1/2)^2+n^{-2}}$给出没有极限的柯西列。

7. 说明第17.7节的定理要求Banach空间，配$\lVert\cdot\rVert_{C^1}$后定义域完备才能使用。

##### 17.2.1.2 积分算子的有界性

1. 先看矩阵：第$i$行与输入的内积由Cauchy--Schwarz控制。

2. 对$i$求和得到Frobenius范数的估计，指出核的$L^2$范数相当于矩阵的Frobenius范数。

3. 设定$\sigma$有限测度空间、输入输出$L^2$与$k\in L^2(\mu\otimes\nu)$，指明乘积测度和Tonelli、Fubini定理见第6章。

4. 定理`thm:lop-hs-bounded`：积分几乎处处绝对收敛，$Tf$可测且属于$L^2$，并有式`eq:lop-hs-bound`。

5. 证明第一步用Tonelli定理得几乎每个截面平方可积。

6. 证明第二步用Cauchy--Schwarz得绝对收敛与逐点界，在例外零测集上令$Tf=0$。

7. 证明第三步在有限测度集上得到乘积可积，用Fubini定理与$\sigma$有限性得可测性。

8. 证明第四步把逐点界平方积分，得到范数估计。

9. 证明末段核对对等价类的良定义与线性。

10. 定义Hilbert--Schmidt积分算子，说明证明的每一步都依赖所选空间，换输入空间须重新核对。

11. 用计数测度上的单位矩阵说明平方可积只是充分条件。

#### 17.2.2 算子范数的定义

1. 说明有界性只给出常数存在，取最小常数比较放大程度，对应矩阵的最大放大倍数。

2. 用式`eq:lop-operator-norm`定义算子范数。

3. 定理`thm:lop-norm-minimal`：式`eq:lop-norm-inequality`成立，且算子范数是可取的最小非负常数。

4. 证明第一段由单位化得不等式。

5. 证明第二段由任意满足条件的$C$对单位球取上确界得最小性。

6. 由式`eq:lop-norm-inequality`和线性得式`eq:lop-lipschitz`，说明算子范数统一控制输入差造成的输出差且不能改小。

###### paragraph：求导的算子范数

1. 对配$\lVert\cdot\rVert_{C^1}$的求导，用$\sin(2\pi nx)/(2\pi n)$得$\lVert D\rVert=1$，且上确界不被取到，说明算子范数是最小统一上界而非“最大输出”。

###### paragraph：积分算子的两个范数

1. 由定理`thm:lop-hs-bounded`得式`eq:lop-hs-norm`，把两侧分别对应矩阵的最大放大倍数与元素平方和开根，引出用贯穿例子算出两个数。

2. 由$\int x\,\mathrm d\mu=0$、$\int x^2\,\mathrm d\mu=1/3$算得$\lVert k\rVert^2=10/9$。

3. 取标准正交的$e_1=1$、$e_2=\sqrt3x$，把式`eq:lop-running-kernel`写成坐标形式，说明$T$相当于$\operatorname{diag}(1,1/3)$，其余方向被送到零。

4. 用勾股定理与Bessel不等式得$\lVert T\rVert=1<\sqrt{10}/3$，说明核的$L^2$范数只是上界。

5. 用椭圆解释算子范数是最长半轴，由$f=e_1+e_2/\sqrt3$手算$\lVert f\rVert^2=4/3$、$\lVert Tf\rVert^2=28/27$，得放大倍数$\sqrt7/3\approx0.882$。

6. 图`fig:lop-norm-ellipse`：(a)输入坐标中的单位圆与归一化的$f$；(b)半轴$1$与$1/3$的椭圆，虚线圆半径$\sqrt{10}/3$，展示算子范数与核范数的差别。

###### paragraph：有界算子的矩阵

1. 在可分Hilbert空间中由标准正交基按式`eq:lop-matrix-entry`定义矩阵元素，说明此时矩阵不再只是类比。

2. 由连续性得$Tx=\lim_N\sum_{n\leq N}x_nTe_n$，再读坐标得矩阵乘法公式，指出连续性保证算子由基向量上的取值决定。

3. 给出后文反复使用的两个矩阵：对角算子$A$的矩阵及$\lVert A\rVert=1$，右移$S$的矩阵及$\lVert S\rVert=1$。

4. 用$\operatorname{diag}(1,2,3,\ldots)$说明并非每个无穷矩阵都给出有界算子。

#### 17.2.3 算子范数的性质

1. 定义算子的和、数乘与复合，把复合对应到矩阵乘法。

2. 说明运算保持线性，下面研究有界性与范数的变化，并引入记号$\mathcal B(X,Y)$。

3. 定理`thm:lop-norm-properties`：正定性、$RT$的有界性与式`eq:lop-norm-properties`，由此$\mathcal B(X,Y)$是赋范空间。

4. 证明第一段：估计先对单个输入成立再取上确界，先证正定性。

5. 证明第二段由$Y$中范数的齐次性得数乘等式。

6. 证明第三段由$Y$中的三角不等式得加法估计。

7. 证明第四段先用$R$的估计再用$T$的估计得复合估计，并指出中间范数必须匹配。

8. 解释复合估计给出多步变换的统一误差上界，以$\operatorname{diag}(1,0)$与$\operatorname{diag}(0,1)$说明上界不是等式。

###### paragraph：算子空间的完备性

1. 说明用有限秩极限构造紧算子和算子级数求和需要极限留在$\mathcal B(X,Y)$中，只要取值空间完备即可。

2. 定理`thm:lop-operator-space-complete`：$Y$是Banach空间时$\mathcal B(X,Y)$是Banach空间。

3. 证明第一段由柯西列逐点取极限得到线性的$T$。

4. 证明第二段固定$n$令$m\to\infty$，得单位球上的统一估计。

5. 证明第三段由该估计得$T$有界且$T_n\to T$按算子范数收敛。

6. 指出证明只用到$Y$的完备性，并给出绝对收敛算子级数收敛的用途，预告第18、19章的使用。

### 17.3 包含映射

正文：[03-inclusion-maps.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/03-inclusion-maps.tex)

1. 以数值方法的$L^2$误差能否推出$L^1$误差提出比较同一函数在不同范数下大小的问题。

2. 用矩阵语言说明这是输入输出相同、只换尺子的单位矩阵，算子范数衡量两把尺子的比例。

3. 定义包含映射与连续嵌入，写出式`eq:lop-embedding`，说明嵌入把误差估计搬到目标空间。

4. 区分集合包含、连续嵌入与范数等价三个逐步加强的要求。

5. 指出有限维中三者无区别，无限维中集合包含不保证连续嵌入，在$C[0,1]$上取$\lVert\cdot\rVert_1$与$\lVert\cdot\rVert_\infty$。

6. 用底为$[0,2/n]$的三角形函数算得比值$n$无界，而反方向成立，得只有单向连续嵌入。

#### 17.3.1 Lᵖ空间的包含

1. 直观说明有限测度上大指数范数控制小指数范数：大取值被更重惩罚，有限测度排除铺满无穷区域的情形。

2. 定理`thm:lop-lp-inclusion`：式`eq:lop-lp-inclusion`与包含映射的范数。

3. 证明第一段处理$p=q$与$q=\infty$。

4. 证明第二段对$p<q<\infty$用Hölder不等式得指数$pr=q$与$1/r^\prime=1-p/q$，开方得结论。

5. 证明第三段说明$\iota$是单射，并由$f=1$得范数估计不能改进。

6. 概率测度上$\lVert f\rVert_p$随$p$单调不减，以$f=x$算出$1/2$、$1/\sqrt3$、$1$，并指出$\lVert x\rVert_p=(p+1)^{-1/p}$即图中蓝线。

###### paragraph：无限测度上的失败

1. 用$f=x^{-1}\mathbf 1_{\{x\geq1\}}$说明慢衰减尾部属于$L^2$而不属于$L^1$。

2. 用$g=x^{-1/2}\mathbf 1_{(0,1)}$说明尖峰属于$L^1$而不属于$L^2$，两个方向的包含都不成立。

3. 计数测度上每点测度为$1$，推出$\lVert a\rVert_q\leq\lVert a\rVert_p$。

4. 说明包含方向反过来，图中绿线给出$(1,1/2,1/3)$的$\ell^p$范数下降，结论是指数方向由测度结构决定。

5. 图`fig:lop-lp-inclusion`：(a)$L^p[0,1]$范数随$p$上升与$\ell^p$范数随$p$下降；(b)尖峰与长尾两种失败。

#### 17.3.2 改变测度后的范数比较

1. 设$\mathrm d\nu=h\,\mathrm d\mu$，回用第8章的密度。

2. 按向量类比把密度解释为给分量换权重，提出能否用$L^p(\mu)$误差控制$L^p(\nu)$误差。

###### paragraph：等价类的对应

1. 指出两个$L^p$的元素是不同测度下的等价类，要先说明映射有意义。

2. 由$\mu(N)=0$推出$\nu(N)=0$，得映射$J$不依赖代表选取，这一步用的是绝对连续。

3. 定理`thm:lop-change-of-measure`：密度有上界$C$时有式`eq:lop-change-of-measure`。

4. 证明：由密度定义对$\lvert f\rvert^p$积分，开方得结论，线性由代表上的恒等变换得到。

###### paragraph：映射可能不是单射

1. 说明权重为零的分量不再被计入，$h$在正测度集$A$上为零时$J\mathbf 1_A=0$，$\ker J$由在$\{h>0\}$上几乎处处为零的函数组成。

2. 证明$h>0$几乎处处时两种零测集一致。

3. 此时$J$单射但可能不满射，以$h=x$与$x^{-3/4}$说明。

4. 在$0<c\leq h\leq C$下得式`eq:lop-measure-equivalence`，两个范数等价，以$h=1+x$举例。

5. 以$h=x$与$f_n=\sqrt n\,\mathbf 1_{(0,1/n)}$说明下界消失时反向控制不存在。

### 17.4 算子列的收敛

正文：[04-operator-convergence.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/04-operator-convergence.tex)

1. 以截断展开和截去积分区域引入近似算子，提出是否存在对全部单位输入同时有效的误差界。

2. 比较有限维矩阵元素收敛即整体收敛，无限维中“每列收敛”与“所有列一起收敛”不同，引出量词次序的差别。

3. 由式`eq:lop-norm-convergence`和式`eq:lop-strong-convergence`定义算子范数收敛与强算子收敛。

4. 比较统一误差与逐输入误差，由不等式得范数收敛蕴含强收敛。

5. 澄清强收敛的“逐点”是针对输入向量，不是函数在定义域各点的收敛。

###### paragraph：截断投影

1. 定义到前$n$个基向量张成空间的投影$P_n$，指出它是前$n$个对角元为$1$的对角矩阵。

2. 由Parseval等式得固定$x$时误差为收敛级数的尾部，$P_n$强收敛到$I$。

3. 由$e_{n+1}$得$\lVert I-P_n\rVert=1$，范数不收敛，矩阵上差的对角线上总还有$1$。

4. 比较系数$2^{-k/2}$与$\propto1/k$两个单位向量的衰减速度，引出图。

5. 图`fig:lop-projection-strong-norm`：(a)$P_4$保留的项与截掉的尾项；(b)三个输入的截断误差随$n$的变化。

6. 总结每个元素可被有限维子空间逼近不等于单位球可被统一逼近。

###### paragraph：有限个输入上的统一控制

1. 有限个输入取$N=\max_iN_i$即可同时控制。

2. 说明截断投影失去统一控制的原因是单位球中有无穷多正交方向，并预告一致有界原理给出的统一范数上界。

###### paragraph：函数空间中的截断

1. 按二分区间排列$I_n$，令$T_nf=(1-\mathbf 1_{I_n})f$，由积分的绝对连续性得强收敛到$I$。

2. 用$f_n=\lvert I_n\rvert^{-1/2}\mathbf 1_{I_n}$得$\lVert I-T_n\rVert=1$。

3. 取$f=1$说明输出函数在每一点都不收敛，强算子收敛与函数逐点收敛是不同概念。

### 17.5 伴随算子

正文：[05-adjoint-operators.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/05-adjoint-operators.tex)

1. 把伴随作为共轭转置的对应物引入，并从用测试方向观察输出的读数进入。

2. 由读数是输入上的线性泛函和Riesz表示，说明每个输出方向对应输入方向，本节由此定义伴随并研究看不见与够不着的方向。

3. 设定Hilbert空间、有界算子及内积对第一个变量共轭线性的约定。

#### 17.5.1 伴随的定义

1. 固定$v$，由读数有界与Riesz表示得到唯一的$w$。

2. 由式`eq:lop-adjoint`定义伴随算子。

3. 解释伴随把测试方向拉回输入空间，方向与$T$相反，它不是从输出恢复输入。

4. 定理`thm:lop-adjoint-properties`：式`eq:lop-adjoint-properties`列出和、数乘、复合、二重伴随及范数关系。

5. 证明第一段由表示的唯一性得线性。

6. 证明第二段验证和、数乘、复合公式，说明$\bar\alpha$的来源。

7. 证明第三段由$\lVert T^*v\rVert^2$的估计得$\lVert T^*\rVert\leq\lVert T\rVert$。

8. 证明第四段取共轭得$T^{**}=T$，再得反向不等式。

9. 证明第五段由复合估计和对单位向量的展开得$\lVert T^*T\rVert=\lVert T\rVert^2$。

10. 对矩阵算出伴随就是共轭转置，强调共轭来自内积约定，并给出矩阵元素$(T^*)_{mn}=\overline{A_{nm}}$。

###### paragraph：累积积分的伴随

1. 定义$V$，核为$\mathbf 1_{\{t<s\}}$，由定理`thm:lop-hs-bounded`有界，按矩阵看是下三角矩阵。

2. 交换积分次序得$(V^*g)(t)=\int_t^1g$，对应转置后的上三角矩阵。

3. 用$f=g=1$核对两边都是$1/2$。

###### paragraph：伴随不是逆

1. 算出右移的伴随是左移，矩阵上的斜线由主对角线下方移到上方。

2. 由$S^*S=I$而$SS^*\neq I$说明$S^*$只是左逆，原因是像缺少$e_1$方向。

3. 指出无限维中单射不等于满射，并用零算子说明伴随可以连左逆都不是。

#### 17.5.2 像与零空间的正交关系

1. 由定义式把输出方向与一切$Tx$正交翻译成$T^*v=0$。

2. 定理`thm:lop-range-kernel`：式`eq:lop-range-kernel`及交换$T$与$T^*$后的两式。

3. 证明第一段由内积恒等式得$(\operatorname{Ran}T)^\perp=\ker T^*$。

4. 证明第二段证明$\overline M\subseteq(M^\perp)^\perp$。

5. 证明第三段由正交分解得反向包含。

6. 写出正交分解式`eq:lop-four-subspaces`，解释看不见的输入方向、能逼近的输出方向与到不了的输出方向。

7. 把四个子空间对应矩阵的四个基本子空间，区别在于像要取闭包。

8. 图`fig:lop-four-subspaces`：$H_1$、$H_2$各分为两块，$T$与$T^*$在两块之间作用，把各自的核送到零。

###### paragraph：像稠密而不闭

1. 对角算子$A$单射自伴，由式`eq:lop-range-kernel`得像稠密。

2. $y=(1/n)$属于$\ell^2$，唯一候选$x_n=1$不平方可和，故$y$不在像中。

3. 用截断候选说明残差趋于零而输入范数$\sqrt N$趋于无穷，区分只能逼近与真正属于像。

4. 累积积分$V$由$\ker V^*=\{0\}$得像稠密。

5. 像中函数都连续，阶跃函数不在其中，所以$\operatorname{Ran}V\neq L^2(0,1)$。

6. 总结$v\perp\ker T^*$只保证$v$在像的闭包中，像闭时才等价于可解，预告第19章。

#### 17.5.3 自伴算子

1. 输入输出同空间时可比较$T$与$T^*$，由实对称与Hermite矩阵引入。

2. 用式`eq:lop-self-adjoint`定义自伴算子。

3. 由内积共轭说明自伴时二次型为实数，并指出$V$与$S$不自伴。

###### paragraph：正交投影

1. 由$z-Pz\perp M$与$Px\in M$逐步得$\langle z,Px\rangle=\langle Pz,x\rangle$，所以正交投影自伴，斜投影不自伴。

###### paragraph：积分算子的伴随核

1. 由矩阵的共轭转置引出核的变量交换和取共轭，设定平方可积核。

2. 定理`thm:lop-adjoint-kernel`：式`eq:lop-adjoint-kernel`。

3. 证明第一段由Cauchy--Schwarz与Tonelli核对三重乘积可积。

4. 证明第二段交换积分次序，并由定理`thm:lop-hs-bounded`和伴随唯一性得结论。

5. 指出核几乎处处共轭对称时积分算子自伴，实值情形就是对称核，条件只需几乎处处。

6. 贯穿例子是实对称核，累积积分的伴随核是其镜像，引出图。

7. 图`fig:lop-kernel-adjoint`：六等分方格画出$V$的下三角矩阵与$V^*$的上三角矩阵，虚线为连续极限下的边界。

#### 17.5.4 正算子

1. 自伴只保证二次型为实数，由$\langle x,T^*Tx\rangle=\lVert Tx\rVert^2$引出对应矩阵半正定的条件。

2. 用式`eq:lop-positive`定义正算子。

3. 验证正交投影与$T^*T$是正算子。

###### paragraph：自伴条件与二次型非负条件

1. 平面旋转$90^\circ$矩阵的二次型为零却不对称，说明实空间中二次型非负不推出自伴。

2. 复空间中二次型取实值迫使自伴，记$B=T-T^*$，其二次型为零。

3. 由$x+v$与$x+\mathrm iv$的展开得$\langle x,Bv\rangle=0$，故$B=0$。

4. 说明为使实复两种情形一致仍把自伴列为前提，反之自伴也不推出非负。

###### paragraph：积分算子的正性

1. 用式`eq:lop-integral-positive`检验正性，它是矩阵半正定的连续版本。

2. 贯穿例子的二次型为两个矩的平方和，是正算子；核换成$1-6xz$时取$f=x$得$-2/3$，不是正算子。

###### paragraph：核逐点非负不等于正算子

1. 两点集合上的交换矩阵逐点非负且对称。

2. 取$f=(1,-1)$得二次型$-2<0$。

3. 核$xz$有负值却给出正算子，说明正性是全部输入的二次型条件。

### 17.6 紧算子

正文：[06-compact-operators.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/06-compact-operators.tex)

1. 由低秩近似提出问题，指出有界性不保证输出能被有限多个代表近似。

2. 说明本节要求有界输入列的输出有收敛子列，路线是有限秩与恒等的比较、有限秩逼近、积分算子。

#### 17.6.1 紧算子的定义

1. 回用第1、2章的相对紧与全有界判据。

2. 定义有限秩算子并对应低秩矩阵。

3. 由有限维有界序列有收敛子列，说明有限秩算子的输出列有范数收敛子列。

4. 定义紧算子及其序列等价形式。

5. 解释两种说法等价，证明紧算子必有界，并得出有界有限秩算子紧。

###### paragraph：无限维恒等算子不紧

1. 标准正交列两两相距$\sqrt2$，恒等算子不紧；一般赋范空间回用Riesz引理。

2. 对角算子把$e_n$压成$e_n/n$，引用图(a)，单位球像满足$\lvert(Ax)_n\rvert\leq1/n$。

3. 说明紧性约束的是整个有界输入族，恒等算子对每个输入可截断、对单位球却不能。

###### paragraph：弱收敛的输入与范数收敛的输出

1. 由$e_n\rightharpoonup0$而$Ae_n\to0$提出紧算子改善收敛。

2. 区分弱收敛的对象是输入列、相对紧的对象是输出集合，引出定理。

3. 定理`thm:lop-compact-weak-strong`：式`eq:lop-compact-weak-strong`。

4. 证明第一步由有界性得输出弱收敛。

5. 证明第二步反证，由弱收敛列有界和紧性抽出输出收敛子列。

6. 证明第三步由弱极限唯一得矛盾。

7. 指出一般有界算子第二步不成立，以恒等算子说明。

#### 17.6.2 Hilbert空间中的有限秩逼近

1. 提出两个方向：有限秩极限是否紧，紧算子能否被有限秩逼近，分别在Banach取值与Hilbert空间中处理。

2. 定理`thm:lop-compact-limit`：算子范数极限保持紧性。

3. 证明第一段化为全有界。

4. 证明第二段取$T_n$的有限$\varepsilon$网。

5. 证明第三段用三角不等式把同一网搬给$T$。

6. 说明统一误差才能搬运覆盖，截断投影说明强收敛不够。

7. 例`ex:lop-diagonal-finite-rank`：$A_m$是有限秩算子，$\lVert A-A_m\rVert=1/(m+1)$，$A$紧。

8. 引用图(b)比较恒等算子与对角算子的截断误差，指出被截掉的矩阵部分本身很小。

9. 图`fig:lop-identity-orthonormal`（同时带标签`fig:lop-finite-rank-error`）：(a)$e_1,e_2,e_3$及其像；(b)三种截断误差随$m$的变化。

###### paragraph：紧算子的有限秩逼近

1. 说明思路：有限个覆盖点张成子空间，正交投影的最近点性质控制误差。

2. 定理`thm:lop-finite-rank-approx`：式`eq:lop-finite-rank-approx`。

3. 证明第一段取$\varepsilon$网并令$M$为其张成空间。

4. 证明第二段令$F=PT$，$F$是有界有限秩算子。

5. 证明第三段由最近点性质得$\lVert T-F\rVert\leq\varepsilon$。

6. 强调控制的是整个单位球上的误差，结合两定理得紧算子恰为有限秩算子的算子范数极限。

7. 指出证明用到正交投影，一般Banach空间取决于逼近性质。

8. 说明Enflo的反例存在但构造很长，读者可查专著，所以本定理不能无条件推广。

#### 17.6.3 积分算子的紧性

1. 沿用平方可积核设定，由式`eq:lop-hs-norm`得式`eq:lop-kernel-error`，把问题化为在$L^2$中逼近核。

###### paragraph：分离变量的核给出有限秩算子

1. 类比低秩矩阵的“列乘行”，有限和形式的核给出秩不超过$r$的算子，贯穿例子秩为$2$。

2. 引入可测矩形的示性函数作为最简单的分离变量核。

3. 引理`lem:lop-rectangle-approx`：有限测度上可测集可被有限个不交矩形之并逼近。

4. 证明第一段设$\mathcal E$与$\mathcal R$，核对矩形族的代数性质。

5. 证明第二段得$\mathcal E$对补封闭。

6. 证明第三段得对可数并封闭，由$\sigma$代数结论完成。

7. 定理`thm:lop-rectangle-dense`：式`eq:lop-rectangle-kernel`形式的函数在$L^2$中稠密。

8. 证明第一步截断到有限测度区域。

9. 证明第二步用简单函数逼近。

10. 证明第三步用矩形代替可测集。

11. 定理`thm:lop-hs-compact`：平方可积核给出紧算子。

12. 证明：取矩形阶梯核得有限秩算子，由式`eq:lop-kernel-error`和定理`thm:lop-compact-limit`得紧性。

13. 用矩阵类比解释元素平方和有限时切尾就是低秩近似，恒等矩阵的平方和发散因而不在此类。

###### paragraph：两种误差的具体数值

1. 区分核的$L^2$误差与算子的最坏输出误差，提出在贯穿例子上算出两者。

2. 取$n$等分格的格内平均核，得$k_n=1+\bar x\bar z$，指出它就是第17.1.2小节的矩阵，图(a)与开头的矩阵相同。

3. 写$x=\bar x+u$、$z=\bar z+v$，方差$s=1/(3n^2)$，三项两两不相关。

4. 平方平均并用总方差分解，得式`eq:lop-kernel-grid-error`。

5. 代入$n=1$与$n=4$得$1/3$与约$0.116$，大$n$下按$\sqrt2/(3n)$下降。

6. 算子误差的核为$xz-\bar x\bar z$，输出落在二维子空间，在基$(x,\bar x)$下写出$2\times2$矩阵。

7. 由迹与行列式得特征值，取绝对值最大者，得式`eq:lop-operator-grid-error`。

8. 代入$n=4$得$(1+\sqrt{61})/96\approx0.0918$，小于核误差，$n=1$时二者相等。

9. 图`fig:lop-rectangle-kernel`：(a)$4\times4$格内平均核；(b)双对数坐标下两种误差随$n$约按$1/n$下降。

10. 说明分片常数逼近不是最经济的，但对任意平方可积核可行，最经济的近似留给第18章。

### 17.7 完备空间中的基本算子定理

正文：[07-fundamental-theorems.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/07-fundamental-theorems.tex)

1. 列举逐输入有界、唯一可解、极限相容三种较弱信息。

2. 对比矩阵只有有限多列，无穷多列时统一常数要靠完备性，三个定理都建立在Baire纲定理之上。

3. 说明每个结论要核对定义域、取值空间的完备性和算子是否定义在全空间，并区分几种“好”的性质。

#### 17.7.1 一致有界原理

1. 把第16章的泛函族结论推广到算子族。

2. 定理`thm:lop-uniform-boundedness`：逐输入有界推出式`eq:lop-uniform-boundedness`。

3. 证明第一段构造闭集$F_n$，$X=\bigcup_nF_n$。

4. 证明第二段由Baire纲定理得内点，平移缩放得$\lVert T_\alpha\rVert\leq2n/r$。

5. 说明有界性、定义域完备性和线性各自的作用，取值空间完备性没有用到。

6. 在有限非零项序列空间上构造$T_nx=nx_n$，逐输入有界。

7. 但$\lVert T_n\rVert=n$无界，完备性不能去掉。

###### paragraph：强收敛极限的有界性

1. 强收敛的算子列在Banach空间上有统一范数上界，极限$T$有界，回答第17.4节留下的问题。

#### 17.7.2 开映射定理

1. 把恢复输入的要求拆成存在、唯一、稳定，方阵可逆同时满足，无限维中分离。

2. 回用第1章的开映射，引出开映射定理。

3. 定理`thm:lop-open-mapping`：式`eq:lop-open-mapping`，$T$是开映射，且每个$y$有原像满足$\lVert x\rVert\leq2\delta^{-1}\lVert y\rVert$。

4. 说明定理含义与证明两步的结构。

5. 证明第一步由满射写成可数并，用Baire纲定理得某闭包含开球。

6. 继续由差集得原点处的输出球，缩放得一族包含关系。

7. 证明第二步逐步修正残差，得$\lVert x_j\rVert<2^{1-j}$与残差估计。

8. 证明第三步由$X$的完备性求和，得式`eq:lop-open-mapping`。

9. 证明第四步验证开映射。

10. 证明末段由缩放得原像的范数估计。

11. 区分闭包只能逼近与第二步的可以达到，引出图。

12. 图`fig:lop-open-mapping`：以$T=\operatorname{diag}(1,0.7)$示意，(a)输入修正量的部分和在半径$2$的圆内收敛；(b)输出近似依次落入半径$\eta/2,\eta/4,\eta/8$的圆。

13. 由开映射定理用于双射，引出有界逆定理。

14. 定理`thm:lop-bounded-inverse`：式`eq:lop-bounded-inverse`。

15. 证明：取$0<t<\delta$由原像唯一性得$\lVert T^{-1}y\rVert<\lVert y\rVert/t$，令$t\to\delta$。

###### paragraph：代数可逆与稳定可逆

1. 对角算子$A$在像上有逆，引出条件不能省。

2. 逆相当于$\operatorname{diag}(1,2,\ldots)$，无界，原因是像稠密不闭因而不完备。

3. 总结开映射提供局部误差估计，代数可逆与稳定可逆在完备空间之间才重合。

###### paragraph：两个完备范数的比较

1. 设一个线性空间在两个范数下都完备且有单向控制。

2. 由有界逆定理得范数等价，并解释$C[0,1]$上$\lVert\cdot\rVert_1$不完备故不矛盾。

#### 17.7.3 闭图判别

1. 提出只检验极限相容的较弱条件，用式`eq:lop-graph`写出图并定义其闭性。

2. 说明$X\times Y$完备，引出闭图定理。

3. 定理`thm:lop-closed-graph`：有界当且仅当图闭。

4. 证明第一段由连续性得图闭。

5. 证明第二段说明图是Banach空间，第一坐标投影是有界双射。

6. 证明第三段由有界逆定理得范数控制。

7. 解释图闭同时考察输入与输出极限，定理的代价是定义域为整个Banach空间。

###### paragraph：处处有定义的对称算子有界

1. 由内积连续性得图闭，从而有界，反过来无界对称算子不能处处有定义。

###### paragraph：定义域只是子空间时

1. 以一致范数下的求导说明图闭：由积分表示取极限得$f\in C^1$且$f^\prime=g$。

2. 求导无界与图闭不矛盾，因为定义域在一致范数下不完备，并定义闭算子。

###### paragraph：图范数

1. 由式`eq:lop-graph-norm`定义图范数，闭算子在图范数下定义域是Banach空间且算子有界。

2. 求导的图范数正是$C^1$范数，兑现第17.2.1.1的说法。

3. 总结使用基本定理前须确认定义域完备，并指出Sobolev范数沿用同样思想。

### 17.8 本章小结

正文：[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/08-linear-operators/08-summary.tex)

1. 总结算子是无限维矩阵、核是矩阵元素，并强调定义域、取值空间和范数都写进算子，归纳几类例子的定义要求。

2. 总结有界性、算子范数及其依赖范数的表现，核范数相当于Frobenius范数并可严格大于算子范数。

3. 总结包含映射与改变测度的结论，以及算子列的两种收敛。

4. 总结伴随是共轭转置的推广，像与零空间的正交关系及像不闭的后果，自伴与正性的条件。

5. 总结紧算子相当于被低秩矩阵统一逼近的算子，平方可积核给出紧算子，核误差控制算子误差。

6. 总结完备性把弱信息升级为统一控制的三个定理及定义域完备的前提，并预告第18、19章。

## 第18章 算子谱

正文入口：[09-operator-spectra.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra.tex)，章内依次输入[01-spectrum.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/01-spectrum.tex)、[02-compact-nonzero-spectrum.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/02-compact-nonzero-spectrum.tex)、[03-compact-self-adjoint.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/03-compact-self-adjoint.tex)、[04-singular-decomposition.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/04-singular-decomposition.tex)、[05-integral-spectral-expansion.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/05-integral-spectral-expansion.tex)、[06-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/06-summary.tex)。

章职责与主线：本章沿用第10章“函数是无限维向量”的类比，把算子看成无限维矩阵，把矩阵特征值的问题推广为算子谱。从$T-\lambda I$能否在整个空间上稳定求逆定义谱，并说明无限维比矩阵多出连续谱与剩余谱：乘法算子是对角元铺满区间的“连续对角矩阵”，右移算子的谱充满圆盘而有限截断只有特征值$0$。随后逐步加入紧性、自伴性，得到离散特征值、正交特征方向与展开式；一般紧算子借$T^*T$得到奇异分解；最后把这些展开写成平方可积核的展开，以Frobenius范数与谱范数的对应区分核的$L^2$误差与算子范数误差。工具来自第17章，方程的可解条件留到第19章。

1. 章首第一段接续函数是无限维向量的类比，把线性算子读作无限维矩阵，提出算子能否沿某些方向简单伸缩的问题。

2. 第二段回顾矩阵由特征值和奇异值回答这一问题，并引出矩阵与算子的对应表。

3. 表`tab:ospec-dictionary`逐行对应向量与函数、矩阵与积分核、对角矩阵与乘法算子、特征值与谱、正交对角化与紧自伴谱分解、奇异值分解与紧算子奇异分解、Frobenius范数与核的$L^2$范数。

4. 第三段指出类比最需要当心之处：乘以$x$的算子是连续对角矩阵却没有特征函数，谱中多出连续谱和剩余谱。

5. 第四段说明路线：18.1定义一般有界算子的谱，18.2加入紧性，18.3再加入自伴性。

6. 第五段说明自伴性的局限，18.4建立奇异分解，18.5回到平方可积核并比较两种误差。

7. 第六段说明所用工具来自第17章，并划定边界：稳定恢复问题留到第19章。

### 18.1 谱

正文：[01-spectrum.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/01-spectrum.tex)

1. 回顾有限维中不可逆、不单射、不满射与存在特征值等价，其原因是维数公式，并回指卷二第6章。

2. 用$\ell^2$上的右移$S$与左移$L$说明无限维中单射与满射分离：右移单射不满，左移满而不单射。

3. 据此指出不能用特征向量刻画不可逆，必须直接从可逆性出发。

4. 固定非零复Banach空间与回到同一空间的有界算子，说明$T-\lambda I$只对这样的算子有意义。

5. 以旋转矩阵说明复数域的必要性，给出实空间的复化$T_{\mathbb C}$及Hilbert情形的复化范数与内积，规定实算子的谱指复化算子的谱。

#### 18.1.1 谱与预解集

1. 把参数$\lambda$的“好”解释为$(T-\lambda I)u=g$对每个右端存在、唯一且稳定地可解，即在整个空间上有有界逆。

2. 定义预解集、预解算子（式`eq:ospec-resolvent`）、谱、特征值与特征向量。

3. 由第17章的有界逆定理说明“逆有界”不是额外限制，写出它是强调整个空间上的稳定反解。

4. 把$\lVert R_\lambda\rVert$解释为误差放大倍数，在$\operatorname{diag}(1,3)$上算出$\lVert R_\lambda\rVert=1/\operatorname{dist}(\lambda,\{1,3\})$，取$\lambda=1.1$得放大倍数$10$。

###### paragraph：谱的有界性与闭性

1. 以一元几何级数类比，引出算子的反解工具；给出小扰动可逆引理（式`eq:ospec-neumann`），证明用复合范数估计、算子空间的完备性和部分和相乘抵消。

2. 说明几何级数的截断误差留到第19章，这里只用来确定谱的位置；给出定理：谱是有界闭集且含于半径$\lVert T\rVert$的闭圆盘（式`eq:ospec-spectrum-disk`），预解点周围半径$1/\lVert R_{\lambda_0}\rVert$的开圆盘不含谱点，证明分别提出因子$-\lambda$与$T-\lambda_0I$后用引理。

3. 把定理后一半读成放大倍数的下界（式`eq:ospec-resolvent-lower`），它是矩阵例子的一般形式。

4. 说明谱非空的结论与证明机制：谱若空，$R_\lambda$是有界的整函数并趋于零，由Liouville定理矛盾；细节不证，实空间不复化时结论失败。

#### 18.1.2 谱点与特征值

1. 说明无限维中$T-\lambda I$可以用不同方式失去可逆性，谱相应地分成几部分。

###### paragraph：谱的三种成分

1. 直观区分不单射、像稠密但不全、像不稠密三种失败方式及其对方程的影响；随后定义点谱、连续谱与剩余谱。

2. 由有界逆定理说明三种情形穷尽谱，并由矩阵的像总是闭集说明矩阵只有点谱。

###### paragraph：乘法算子：连续的对角矩阵

1. 把对角矩阵类比到$L^2(0,1)$上的$(Mf)(x)=xf(x)$，说明下标$x$上的输出只用同一下标的输入。

2. 用$n$段中点离散化得到$\bm D_n$，其特征值是中点、特征向量是归一化高台。

3. 引用图`fig:ospec-discrete-to-continuous`，说明$n$增大时特征值铺满$[0,1]$而特征向量变窄，极限下特征函数不再属于$L^2$。

4. 图`fig:ospec-discrete-to-continuous`展示$n=5$、$n=20$的对角元与特征值，以及连续极限中铺满$[0,1]$的谱。

5. 陈述结论$\sigma(M)=\sigma_{\mathrm c}(M)=[0,1]$（式`eq:ospec-multiplication-spectrum`）。

6. 对$\lambda\notin[0,1]$逐点除以$x-\lambda$得到有界逆，$\lambda\in\rho(M)$。

7. 对$\lambda\in[0,1]$由$(x-\lambda)f=0$几乎处处推出$f=0$，指出类比失效之处：对角元等于$\lambda$的下标只有一个点，测度为零。

8. 由$g=1$要求$f=1/(x-\lambda)$而其平方积分发散，得$M-\lambda I$不满射。

9. 挖去$\lambda$附近一段得到$g_n$，由控制收敛定理$g_n\to g$且$g_n$在像中，得像稠密，完成式`eq:ospec-multiplication-spectrum`的证明。

10. 取$\lambda=\frac12$、$g=1$手算$\lVert g-g_n\rVert^2=2/n$与$\lVert f_n\rVert^2=2n-4$，列出$n=10,100,1000$的数值，说明连续谱的含义是处处可近似求解而解不稳定，并引用图`fig:ospec-spike-instability`(b)。

###### paragraph：近似特征向量

1. 构造单位高台$u_n$，手算残差$\lVert(M-\frac12I)u_n\rVert=1/(2\sqrt3\,n)\to0$，说明$u_n$几乎被乘以$\frac12$。

2. 图`fig:ospec-spike-instability`展示单位高台$u_2,u_8,u_{32}$与截断解$f_4,f_{20}$。

3. 由$\langle u_n,u_{4n}\rangle=\frac12$得$\lVert u_n-u_{4n}\rVert=1$，$(u_n)$不是柯西列，极限不是$L^2$函数。

4. 过渡到一般结论：这种现象在连续谱上总会出现。

5. 给出并证明连续谱上的近似特征向量引理：若有下界则像闭，闭且稠密推出满射，矛盾。

6. 把这样的序列称为近似特征向量，说明它是有限维特征向量的替代品但不收敛。

###### paragraph：右移算子

1. 引用图`fig:ospec-shift-spectrum`(a)说明右移的作用，由保长得$\lVert S\rVert=1$，谱含于闭单位圆盘。

2. 逐分量比较$Sx=\lambda x$，分$\lambda=0$与$\lambda\neq0$证明只有零解，$S$没有特征值。

3. 对$\lvert\lambda\rvert<1$由下界得单射且像闭，计算出$y=(1,\bar\lambda,\bar\lambda^2,\ldots)$与像正交，得$\lambda$属于剩余谱。

4. 用$\lambda=\frac12$、$x=e_1$核对内积为零，指出这里解很稳定（放大倍数不超过$2$）但有方向到达不了，与连续谱对比。

5. 对$\lvert\lambda\rvert=1$由谱闭得属于谱，由与像正交推出$\lvert y_k\rvert$为常数故$y=0$，像稠密，属于连续谱；总结式`eq:ospec-shift-spectrum`。

6. 构造圆周上摊开的近似特征向量$u_n$，算出残差平方$2/n$，对比乘法算子的集中与这里的摊开。

7. 说明左移的点谱是开圆盘，由$\overline{\operatorname{Ran}(T-\lambda I)}$是$\ker(T^*-\bar\lambda I)$的正交补得剩余谱对应伴随的点谱，自伴算子没有剩余谱。

###### paragraph：有限截断看不见的谱

1. 指出$n$阶截断$\bm S_n$幂零，唯一的特征值是$0$，而$S$的谱是整个圆盘，引用图`fig:ospec-shift-spectrum`(b)(c)，说明矩阵截断不一定逼近谱。

2. 图`fig:ospec-shift-spectrum`展示右移的作用、截断的单点谱以及$S$的圆盘谱（内部剩余谱、边界连续谱）。

3. 对$\lambda=\frac12$写出$(\bm S_n-\frac12\bm I)^{-1}$的有限几何级数，第$n$行第$1$列元素$-2^n$给出放大倍数下界，说明不可逆的痕迹藏在预解范数里。

4. 总结一般有界算子的谱不能理解为特征值的集合，引出紧性条件。

### 18.2 紧算子的非零谱

正文：[02-compact-nonzero-spectrum.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/02-compact-nonzero-spectrum.tex)

1. 对比乘法算子与右移保持大小和紧算子压缩有界集，用对角算子说明紧性对应对角元趋于零，并给出两个方向的理由。

2. 预告非零谱回到矩阵情形，连续谱只剩$0$一点。

3. 设定复Banach空间上的紧算子，说明紧算子与有界算子的复合仍紧。

4. 说明Riesz引理在没有正交性时提供距离下界的替代品。

5. 给出并证明Riesz引理：取近似最近点并归一化，距离至少为$\theta$。

###### paragraph：紧算子减去非零数乘

1. 说明下面的引理是矩阵“单射推出可逆”关键部分的类比；给出单射推出下有界引理（式`eq:ospec-bounded-below`），证明用反证、紧性抽子列得到零空间中的单位向量，像闭的论证同前。

2. 用对角算子$A$说明$\mu\neq0$是必需的：$\mu=0$时单射而无正下界。

3. 给出紧算子非零谱定理：特征空间有限维、单射推出满射、模不小于$\delta$的特征值有限、无限维时$0\in\sigma(T)$。

4. 说明证明的共同思路：无限结构用Riesz引理造出彼此远离的向量，与紧性矛盾。

5. 证明四条结论：（1）在特征空间中选彼此远离的单位向量；（2）把幂写成紧算子减非零数乘，得到严格递减的闭像链并与紧性矛盾；（3）不同特征值的特征向量线性无关，在递增张成链上用Riesz引理；（4）$I=T^{-1}T$紧与无限维恒等算子不紧矛盾。

6. 解释结论（2）保留了矩阵的单射推出可逆，并由$\sigma(M)=[0,1]$不可数知$M$不紧。

7. 说明$0$是例外：总是谱点，未必是特征值，并预告连续谱待在$0$处。

###### paragraph：对角算子

1. 对$\ell^2$上的$A(x_n)=(x_n/n)$，说明每个$1/k$是一维特征空间的特征值。

2. 说明$0$不是特征值、像稠密、$0$属于连续谱，并举$y=(1/n)$不在像中。

3. 对$\lambda\notin S_A$逐分量解出有界逆，得$\sigma(A)=S_A$及$\lVert R_\lambda\rVert=1/\operatorname{dist}(\lambda,\sigma(A))$（式`eq:ospec-diagonal-resolvent`）。

4. 引用图`fig:ospec-spectrum-resolvent`，说明每个特征值附近范数趋于无穷、尖峰向$0$聚集。

5. 图`fig:ospec-spectrum-resolvent`展示$A$的谱点与实参数上的预解范数。

###### paragraph：累积积分没有特征值

1. 定义$L^2(0,1)$上的累积积分$V$，由平方可积核得紧性。

2. 由$Vf=\lambda f$推出$f$连续可导且满足$\lambda f^\prime=f$、$f(0)=0$，只有零解。

3. 由$Vf=0$说明$f$在每个区间上积分为零，由区间示性函数稠密（第15章）得$f=0$。

4. 结合定理得$\sigma(V)=\{0\}$而$V$没有特征向量，并由$\ker V^*=\{0\}$得$0$属于连续谱。

5. 离散化得到下三角矩阵$\bm V_n$，特征值只有$h\to0$，秩$n-1$使特征方向只有一个，说明无限维极限中一个也没有。

###### paragraph：五个例子的比较

1. 比较非紧的$M,S,L$与紧的$A,V$，引出五个算子的谱表。

2. 表`tab:ospec-gallery`列出$M,S,L,A,V$的谱及其点谱、连续谱、剩余谱。

3. 补充$L$在单位圆周上的判定：单射、像稠密且属于谱。

4. 用两个紧算子划出边界：紧性使非零谱离散，却不保证特征向量完备或正交，引出自伴条件。

### 18.3 紧自伴算子的谱分解

正文：[03-compact-self-adjoint.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/03-compact-self-adjoint.tex)

1. 以实对称矩阵的正交对角化为起点，比较缺乏特征结构的累积积分与具备它的对角算子，指出差别在于自伴性。

2. 预告本节得到实特征值、正交特征方向和展开式，是正交对角化在无限维的翻版。

3. 设定Hilbert空间上的紧自伴算子，说明证明不需要复化。

4. 给出紧自伴谱分解定理，三条结论分别是实特征值与正交性、非零特征值的有限性、展开式（式`eq:ospec-spectral-expansion`）。

5. 说明证明的主线：二次型读出范数、紧性找极值方向、正交补上重复。

###### paragraph：特征值与正交性

1. 由二次型等式得特征值为实数，再由自伴推出不同特征值的特征向量正交，证明结论1且未用紧性。

###### paragraph：非零特征值的有限性

1. 对一列两两正交的单位特征向量，由勾股定理得输出彼此相距至少$\sqrt2\delta$，与紧性矛盾，得结论2。

###### paragraph：二次型给出范数

1. 定义$Q$并类比对称矩阵的谱范数，由Cauchy--Schwarz得$Q\leq\lVert T\rVert$。

2. 展开$u\pm v$的二次型，用平行四边形恒等式得实部上界，取$v=Tu/\lVert Tu\rVert$得$\lVert T\rVert=Q$。

###### paragraph：紧性给出极值方向

1. 取使二次型绝对值趋于上确界的单位向量，抽子列使符号一致，得$\lambda=\pm\lVert T\rVert$，并说明不能预设$\lambda>0$；展开残差得式`eq:ospec-rayleigh-residual`，$u_n$是近似特征向量。

2. 对比乘法算子说明近似特征向量可以不收敛，紧性抽子列使其收敛到单位特征向量$e$。

3. 用$\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$计算二次型$2+\sin2\theta$、残差平方$4\sin^2(\theta-\frac\pi4)$与上界$12\sin^2(\theta-\frac\pi4)$，并在$\theta=0$核对。

4. 图`fig:ospec-rayleigh-extremal`展示二次型曲线及残差平方与上界，二者在极值方向同时为零。

###### paragraph：逐步分解与零空间

1. 证明$e_1$的正交补在$T$下不变，限制后重复得到$e_2,e_3,\ldots$，不停止时$\lambda_k\to0$。

2. 令$N$为闭张成，由$T$在$N^\perp$上的范数趋于零或按停止条件为零，得$N^\perp\subseteq\ker T$。

3. 由$\langle e_j,u\rangle=\lambda_j^{-1}\langle e_j,Tu\rangle$得反向包含，于是$N=(\ker T)^\perp$。

4. 说明每个非零特征值都已列出，结合上一节定理得非零谱恰为$\{\lambda_j\}$。

###### paragraph：展开式

1. 由正交投影与余项属于$\ker T$得第一式，把$T$作用于部分和得第二式，完成定理证明。

###### paragraph：空间的分解与有限谱截断

1. 把空间分成零空间与特征方向闭张成，类比$\bm Q\bm\Lambda\bm Q^\top$，给出式`eq:ospec-spectral-norm`。

2. 由有限秩截断的系数平方和得截断误差$\lVert T-T_m\rVert=\lvert\lambda_{m+1}\rvert$（式`eq:ospec-spectral-truncation`）。

###### paragraph：贯穿例子

1. 对核$1+xz$算出$T1=1$、$Tx=\frac13x$，写出特征展开，说明$\ker T$无限维、截断误差$\frac13$。

2. 把核换成$1-6xz$，算出特征值$-2$，说明不能只找正的最大特征值，并引用图`fig:ospec-spectral-stretch`。

3. 图`fig:ospec-spectral-stretch`展示对角算子的系数缩放与系数平面上单位圆变成翻折的椭圆。

4. 说明级数按Hilbert范数收敛，不等于逐点或一致收敛，引出第18.5节。

### 18.4 紧算子的奇异分解

正文：[04-singular-decomposition.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/04-singular-decomposition.tex)

1. 由累积积分无特征向量及输入输出空间不同的问题，引出矩阵奇异值分解（回指卷二第7章）。

2. 说明把$\bm A^\top\bm A$的做法搬到紧算子上，设定两个Hilbert空间之间的紧算子。

###### paragraph：矩阵的例子

1. 对$\left[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\right]$算出$\bm A^\top\bm A$的特征值$45,5$、右奇异向量及奇异值$3\sqrt5,\sqrt5$。

2. 算出左奇异向量并核对正交，比较特征值$3,5$与奇异值$6.71,2.24$的不同。

3. 写出秩一近似$\bm A_1$，误差谱范数为$\sqrt5$，引用图`fig:ospec-svd-geometry`解释单位圆到椭圆。

4. 图`fig:ospec-svd-geometry`展示输入单位圆与右奇异向量、输出椭圆及其半轴。

###### paragraph：从$T^*T$构造两组方向

1. 说明$T^*T$紧、自伴、正，且$\ker(T^*T)=\ker T$。

2. 用定理得$v_j$与$s_j$，令$\sigma_j=\sqrt{s_j}$、$u_j=Tv_j/\sigma_j$，验证$u_j$标准正交及$T^*u_j=\sigma_jv_j$。

3. 给出紧算子奇异分解定理（式`eq:ospec-svd`）及闭张成结论。

4. 证明：由谱分解得$x$的分解，作用$T$得展开；由展开与$u_j\in\operatorname{Ran}T$得$u_j$的闭张成；由伴随关系得$T^*$的展开。

5. 定义奇异值、右奇异向量、左奇异向量与奇异系统。

6. 把展开式解释为读系数、乘$\sigma_j$、放到输出方向三步，说明$\ker T$与$\ker T^*$的角色。

7. 比较左右方向：一般不同，对正算子相同，对自伴算子奇异值为特征值的绝对值。

8. 累积积分的奇异分解例子：由$V^*V$求导得$sf^{\prime\prime}=-f$及边界条件，解出$\omega_k$，由$V$单射得完备，得$\sigma_k$、$v_k$、$u_k$，列出前四个奇异值。

9. 说明$V$无特征向量却有完整奇异系统，奇异分解不依赖自伴性。

###### paragraph：截断奇异分解

1. 定义截断$T_m$，回指矩阵低秩逼近（卷二第18章）。

2. 给出截断误差定理（式`eq:ospec-svd-truncation`）：误差为$\sigma_{m+1}$，且任何秩不超过$m$的算子不能更好。

3. 证明：第一步由正交性与Bessel不等式计算误差；第二步在$m+1$维子空间中取$F$的零向量得下界。

4. 引用图`fig:ospec-svd-decay`，说明保留三项误差为$\sigma_4$，高频方向被积分平均掉。

5. 图`fig:ospec-svd-decay`展示奇异值衰减与前三个右奇异函数。

6. 对比对角算子，其坐标截断就是截断奇异分解。

7. 说明小奇异值利于正向逼近而不利于反向求解，引出第19章。

### 18.5 积分算子的谱展开

正文：[05-integral-spectral-expansion.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/05-integral-spectral-expansion.tex)

1. 回顾第17章平方可积核的有界紧性、伴随核与核误差控制算子误差。

2. 用矩阵分解的两种读法说明算子展开与核展开收敛意义不同，这是本节的主要问题。

3. 设定$\sigma$有限测度空间与核，定义乘积函数$a\otimes\bar b$，类比秩一矩阵。

4. 给出并证明乘积函数与核系数引理（式`eq:ospec-kernel-coefficient`），用Tonelli与Fubini定理。

5. 给出并证明核由算子唯一确定：矩形示性函数稠密。

#### 18.5.1 自伴积分算子的特征展开

1. 设定共轭对称核，类比矩阵的共轭对称，由定理得特征函数与特征值。

2. 给出定理：作用展开、核展开（式`eq:ospec-kernel-eigen-expansion`）、范数与截断误差（式`eq:ospec-kernel-eigen-norm`）。

3. 证明：由系数引理与Bessel不等式得级数收敛，由核误差控制与唯一性得$k=\tilde k$，由勾股定理得范数。

4. 把结论（3）类比Frobenius范数，并比较同一截断的算子误差与核误差。

5. 用$1+xz$核对两项展开与$\lVert k\rVert^2=10/9=1^2+(1/3)^2$，截去一项时两种误差都等于$\frac13$。

###### paragraph：收敛意义的边界

1. 说明$L^2(\mu\otimes\mu)$收敛不推出逐点或一致收敛。

2. 用$k^\prime=1+xz-10\cdot\mathbf 1_{\{x=z\}}$说明核只是几乎处处的等价类，对角线取值无意义。

3. 说明逐点或一致收敛需要连续性与正性等附加条件，属于第23章的Mercer定理。

#### 18.5.2 非自伴积分算子的特征展开

1. 说明一般非自伴紧算子可能没有特征向量，预告先讨论正规算子再改用奇异分解。

###### paragraph：正规算子

1. 类比正规矩阵定义正规算子（式`eq:ospec-normal`），举自伴与反自伴的例子，写出积分算子的正规条件。

2. 给出紧正规算子的谱分解定理（式`eq:ospec-normal-expansion`）。

3. 证明：分解$T=A+\mathrm iB$，由$AB=BA$同时对角化$A$的非零特征空间与$\ker A$上的$B$，合并后得到展开。

4. 由系数引理得正规核的特征函数展开（式`eq:ospec-normal-kernel`）。

###### paragraph：周期卷积核

1. 定义周期核$h(x-y)$，由$h(-t)=-h(t)$得$T^*=-T$，正规而不自伴。

2. 由变量替换验证$\mathrm e^{2\pi\mathrm inx}$是特征函数，算出$\mu_n=\mathrm i/(2\pi n)$，并类比离散Fourier基对角化循环卷积。

3. 由Fourier基完备写出展开，$\ker T$由常函数组成，并核对$\lVert k\rVert^2=1/12$与特征值平方和相等。

###### paragraph：一般核的奇异函数展开

1. 说明正规条件不成立或空间不同时回到奇异系统。

2. 给出平方可积核的奇异函数展开定理（式`eq:ospec-kernel-svd`、`eq:ospec-kernel-svd-error`）。

3. 证明：由系数引理得$\langle u_j,Tv_l\rangle=\sigma_l\delta_{j,l}$，其余与自伴情形相同。

4. 用累积积分核核对$\lVert k\rVert^2=\frac12$等于奇异值平方和，引出误差表。

5. 表`tab:ospec-volterra-errors`列出$m=1,\ldots,4$的算子误差与核误差。

6. 解释两种误差度量的对象：算子误差按$1/m$下降，核误差按$1/\sqrt m$下降，引用图`fig:ospec-kernel-truncation`(b)。

7. 由连续函数的一致极限仍连续说明$k_m$不一致收敛到跳跃核，引用图`fig:ospec-kernel-truncation`(a)的截面。

8. 图`fig:ospec-kernel-truncation`展示$x=\frac12$处部分和与原核的比较，以及两种误差的双对数曲线。

### 18.6 本章小结

正文：[06-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/09-operator-spectra/06-summary.tex)

1. 总结谱的定义、位置与放大倍数，说明无限维多出的连续谱和剩余谱的含义。

2. 总结乘法算子与右移算子两个例子，以及近似特征向量和矩阵截断的局限。

3. 总结紧性使非零谱回到矩阵情形，并以累积积分说明紧性不保证特征展开。

4. 总结紧自伴谱分解与截断误差，以及一般紧算子的奇异分解和截断最优性。

5. 总结核的特征函数与奇异函数展开、Frobenius范数对应、两种误差与收敛意义。

6. 指出小奇异值带来的反向困难，方程的可解性与稳定性留到第19章。

## 第19章 线性算子方程

正文入口：[10-linear-operator-equations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations.tex)，章内依次输入[01-first-kind-equations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations/01-first-kind-equations.tex)、[02-second-kind-equations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations/02-second-kind-equations.tex)、[03-stability.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations/03-stability.tex)、[04-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations/04-summary.tex)。

章职责与主线：本章沿用第10章“函数是无限维向量”的类比，把积分算子看成无限大矩阵，把算子方程看成线性方程组$\bm A\bm x=\bm b$，在Hilbert空间中回答存在、唯一与误差放大三个问题，并逐处说明类比在哪里失效。第一类方程$Kf=g$的存在与唯一由像与零空间决定，奇异系统把它们写成正交条件与Picard条件，像可以不闭；第二类方程$(I-\lambda K)u=f$因恒等项恢复有限维局面，小参数下用Neumann级数构造逆，一般参数下由Fredholm择一给出有限个相容条件；最后固定范数讨论适定性，区分离散矩阵的病态与无限维的不适定，并比较两类方程的敏感性。贯穿例子是离散累积积分$\bm A_n$、$L^2([-1,1],\mathrm dz/2)$上核为$1+xz$的秩二算子$T$与$L^2(0,1)$上的累积积分$V$，正则化参数选择与算法留给卷五。

1. 章首第一段回顾第10章的类比，指出积分算子相当于行列下标连续变化的无限大矩阵，给定输出求输入就是解线性方程组，本章把前几章正向使用的算子反过来。

2. 第二段列出方程组的三个基本问题及卷二的回答，再用三条并列项说明无限维的新现象：像可以不闭、奇异值可趋于零使误差放大无界、恒等项使这两个现象消失。

3. 第三段说明三节分工：19.1处理对应一般方程组的第一类方程，19.2说明恒等项为何恢复有限维局面，19.3单独讨论误差放大并区分病态与不适定。

4. 第四段交代三个贯穿例子，并划定范围：本章只回答何时可解与解怎样依赖数据，求解方法的设计属于卷五的正则化问题。

### 19.1 第一类算子方程

正文：[01-first-kind-equations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations/01-first-kind-equations.tex)

1. 从测量仪器给出平均或累积后的结果进入，说明从输出$g$推回$f$就是解算子方程，本节先对应到线性方程组，再分别回答有没有解与解是否唯一。

###### paragraph：从方程组到算子方程

1. 把方程组第$i$行的加权求和与积分算子对齐（式`eq:opeq-matrix-integral`），说明分量下标换成积分变量、行下标换成输出自变量、求和换成积分，核的切片对应矩阵的行与列。

2. 反向把累积积分$V$按步长$h=1/n$离散，由节点处的面积和得到元素全为$h$的下三角矩阵$\bm A_n$。

3. 取$n=4$与$f=1$逐项写出$\bm A_4\bm x=\bm b$，右端恰为$g=x$在节点上的值，并由图说明矩阵第三行与核的切片含义相同。

4. 配图`fig:opeq-matrix-kernel`并列$\bm A_4$的乘法与$V$的核，用粗框标出第三行及其输出，用粗线标出$x=3/4$的切片。

###### paragraph：方程与两个基本问题

1. 固定Hilbert空间$H_1,H_2$、有界算子$K$与数据$g$，说明复内积的约定。

2. 给出第一类算子方程的定义（`def:opeq-first-kind`、式`eq:opeq-first-kind`），并指出积分算子情形即第一类积分方程。

3. 与方程组对照，说明有解当且仅当$g\in\operatorname{Ran}K$。

4. 由两解之差属于零空间得到解集$f_0+\ker K$，唯一当且仅当$\ker K=\{0\}$，强调存在性问输出空间的集合、唯一性问输入空间的子空间。

###### paragraph：秩二积分算子的例子

1. 在$L^2([-1,1],\mathrm dz/2)$上定义核为$1+xz$的算子$T$（式`eq:opeq-rank-two`），指出输出只由两个内积决定，因而总是一次多项式。

2. 计算$\lVert1\rVert^2=1$、$\lVert x\rVert^2=1/3$、$\langle1,x\rangle=0$，由分解$f=\alpha+\beta x+h$得到$Tf=\alpha+\beta x/3$，把$T$读成对角矩阵$\operatorname{diag}(1,\frac13,0,\ldots)$。

3. 读出像是二维的$\operatorname{span}\{1,x\}$、零空间是无限维的正交补，以$x^2-\frac13$验证，指出这是与小矩阵的第一处不同。

4. 解$Tf=2+x$，比较系数得$\alpha=2$、$\beta=3$而$h$任意；$g=x^2$无解，说明被压成零的方向既丢失信息也无法产生。

###### paragraph：奇异系统下的系数关系

1. 由矩阵奇异值分解把方程组化成标量方程$\sigma_jz_j=y_j$进入，回顾第18章紧算子的奇异系统（式`eq:opeq-svd`）。

2. 列出$(v_j)$与$(u_j)$的闭张成及$\overline{\operatorname{Ran}K}=(\ker K^*)^\perp$，由图把这些子空间排在一起。

3. 配图`fig:opeq-four-subspaces`画出输入、输出空间的两部分：$\ker K$被送到$0$，$\ker K^*$到达不了，$g$可在闭包中却无原像。

4. 对方程取$u_j$的内积并移动$K$，得到系数关系$\langle v_j,f\rangle=\langle u_j,g\rangle/\sigma_j$，指出多出的要求是系数平方可和。

5. 陈述Picard可解条件与最小范数解定理（`thm:opeq-picard`、式`eq:opeq-picard`、`eq:opeq-min-norm`）。

6. 分必要性、充分性与解的结构三段证明：必要性用Bessel不等式，充分性由逐项作用得到投影，最后用勾股定理得范数最小。

7. 定义Picard条件与最小范数解，说明第一条只保证$g$在像的闭包中，第二条才保证系数拼成输入空间的元素。

8. 指出奇异值有限时第二条自动成立，并在$T$上取$g=2+x$逐项计算奇异系数，得到$f^\dagger=2+3x$，范数平方为$7$。

###### paragraph：像的闭包不等于像

1. 用$\ell^2$上的对角算子$A(x_n)=(x_n/n)$说明第一个条件对所有数据成立，Picard条件化为$\sum_nn^2\lvert g_n\rvert^2<\infty$。

2. 比较$g^{(1)}_n=1/n^2$（有解$1/n$）与$g^{(2)}_n=1/n$（形式解恒为$1$，无解），由图看出差别在除以奇异值后才显现。

3. 配图`fig:opeq-picard-coefficients`对照两组数据及其形式解系数。

4. 把$g^{(2)}$截断为有解数据，解的范数为$\sqrt N$而数据差趋于零，说明有限维子空间总闭，这一现象在有限维中不会发生。

5. 转到函数空间，回顾$V$的奇异系统与$\ker V=\ker V^*=\{0\}$，说明第一个条件对所有数据成立。

6. 取$g=1$算出$\langle u_k,1\rangle=\sqrt2\sigma_k$，形式解系数恒为$\sqrt2$，Picard条件不成立，并由输出在$0$处取零直接核对。

7. 用$f_n=n\mathbf 1_{[0,1/n]}$计算$\lVert Vf_n-1\rVert^2=1/(3n)$与$\lVert f_n\rVert^2=n$，解释输入想收缩成$L^2$中不存在的尖峰，数据只能被追到。

8. 配图`fig:opeq-range-closure`并列输入$f_n$与输出$Vf_n$趋于$1$的过程。

###### paragraph：Picard条件与求导

1. 对绝对连续、$g(0)=0$、$g'\in L^2$的数据分部积分，消去边界项得$\langle u_k,g\rangle=\sigma_k\langle v_k,g'\rangle$，复值数据分实虚部处理。

2. 由此Picard级数等于$\lVert g'\rVert^2$、$f^\dagger=g'$，再由反向论证说明$\operatorname{Ran}V$恰由这样的函数组成，解方程就是求导。

3. 用$g=x$逐项核对系数，并由$\sum_k2\sigma_k^2=1$验证Picard级数等于$\lVert1\rVert^2$。

4. 总结正交条件对$V$不提供信息，Picard条件才要求边界值与导数，奇异值衰减越快要求数据越光滑，引向稳定性一节。

### 19.2 第二类算子方程

正文：[02-second-kind-equations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations/02-second-kind-equations.tex)

1. 说明未知函数同时出现在算子内外，矩阵形式是$(\bm I-\lambda\bm A)\bm x=\bm b$，恒等项改变方程的全部性质，并预告先比较两类方程再分小参数与一般参数研究。

###### paragraph：方程与恒等项

1. 设$K$是$H$上的紧算子，说明输入输出须在同一空间。

2. 给出第二类算子方程的定义及积分形式（`def:opeq-second-kind`、式`eq:opeq-second-kind`、`eq:opeq-second-kind-integral`）。

3. 在$T$的三类方向上逐方向比较系数，得到式`eq:opeq-rank-two-second`。

4. 算出$\lambda=\frac12$时的解，说明正交补方向的乘子由$0$变为$1$，信息不再丢失，由图比较乘子。

5. 配图`fig:opeq-equation-types`并列$T$与$I-\frac12T$在五个方向上的乘子。

6. 指出例外参数$\lambda=1,3$正是特征值$1,\frac13$的倒数，对应非零解$u=1$与$u=x$。

7. 比较两类方程困难的来源，并预告下面两小节分别处理$\lambda$足够小与$\lambda$任意。

#### 19.2.1 Neumann级数

1. 由标量几何级数类比引入，并说明这里需要的是余项，而第18章只用该级数确定谱的位置。

2. 陈述Neumann级数定理（`thm:opeq-neumann`、式`eq:opeq-neumann`、`eq:opeq-neumann-remainder`）。

3. 证明部分和是Cauchy列并得到范数上界，由望远镜恒等式证明极限是逆，再逐项求和得余项界。

4. 取$S=\lambda K$得到小参数下的唯一解与范数估计（式`eq:opeq-neumann-solution`），并说明这里未用紧性。

###### paragraph：截断与迭代

1. 由余项界得到截断误差的几何衰减（式`eq:opeq-neumann-truncation`），说明$q$接近$1$时收敛变慢。

2. 写出递推（式`eq:opeq-neumann-iteration`），指出它是步长为$1$的Richardson迭代的算子形式及压缩映射。

3. 在$T$上取$\lambda=\frac12$、$f=1+x$，给出精确解与前两步迭代值。

4. 解系数递推得$a_N$、$b_N$的闭式，并以$N=2$给出具体数值。

5. 计算$N=2$的实际误差约$0.2500$，与上界$0.2887$比较，相差约$15\%$。

6. 由图说明常数方向与线性方向的收敛比分别是$\frac12$与$\frac16$，总误差由最慢方向决定。

7. 配图`fig:opeq-neumann-convergence`显示迭代直线逼近精确解，以及实际误差、上界与线性方向误差的衰减。

###### paragraph：小范数只是充分条件

1. 取$\lambda=2$，级数在常数方向发散而方程唯一可解，以$f=1+x$得$u=-1+3x$并代回核对。

2. 反方向取累积积分，写出反复积分公式，由Cauchy--Schwarz不等式得$\lVert V^n\rVert\leq1/(n-1)!$，说明级数对任意$\lambda$收敛。

3. 取$f=1$得$u=e^{\lambda x}$，在$\lambda=10$时核对，与$V$的谱只有$\{0\}$相符，并引出需要紧性的一般情形。

#### 19.2.2 Fredholm可解条件

1. 按$\lambda=0$与$\lambda\neq0$分情形，说明齐次方程有非零解当且仅当$1/\lambda$是特征值。

2. 回顾方阵的择一事实，说明它对$I-\lambda K$原样成立，并交代先看紧自伴情形再证一般情形。

###### paragraph：紧自伴情形的方向解释

1. 用$\mu_j$记非零特征值以避免符号混淆，由谱分解写出$I-\lambda K$在各方向上的乘子。

2. $\lambda$不等于任何$1/\mu_j$时乘子有正下界，逐方向相除得到有界逆（式`eq:opeq-self-adjoint-solution`）。

3. $\lambda=1/\mu_k$时乘子在有限维特征空间上为零，可解当且仅当$f$与之正交，解可加特征空间元素。

4. 在$T$上取$\lambda=1$得可解条件$a=0$与解的形式，由图说明除两个例外参数外方程唯一可解。

5. 配图`fig:opeq-fredholm-alternative`画出三个乘子随$\lambda$的变化及逆算子范数在例外参数处的爆破。

###### paragraph：Fredholm择一

1. 说明一般紧算子没有正交特征基，结论形式不变但要改用伴随方程的零空间。

2. 陈述Fredholm择一定理（`thm:opeq-fredholm`），包括零空间有限维且两侧维数相等、像闭、单射与满射等价及两种情形。

3. 定义Fredholm择一与相容条件（式`eq:opeq-compatibility`），区分非唯一与不可解的来源。

4. 强调关键是像闭，所以正交条件判断的是精确可解，并与对角算子$A$对比。

5. 引出不自伴的秩一算子$(Ku)(x)=x\int_0^1u$，取$\lambda=2$，问为何条件要看伴随的零空间。

6. 直接算出$\ker B=\operatorname{span}\{x\}$与$\ker B^*=\operatorname{span}\{1\}$。

7. 两边积分得到必要条件$\int f=0$，用$f=2x-1$与$f=1$说明条件是$f\perp1$而不是$f\perp x$。

###### paragraph：有限秩部分与小范数余项

1. 说明证明思路：有限秩部分化成方阵，余项用Neumann级数吸收，先处理$\lambda=0$的情形。

2. 证明第一步：取有限秩$F$作分解$B=C(I-G)$。

3. 把$G$写成有限个内积与基向量的组合。

4. 第二步：断言$(I-G)u=h$等价于矩阵方程$(\bm I-\bm M)\bm c=\bm d(h)$。

5. 分两个方向验证这一等价。

6. 第三步：由闭集的连续原像与$C$的同胚性得到像闭，并推出第二条结论。

7. 第四步：取$h=0$得$\dim\ker B=\dim\ker(\bm I-\bm M)$。

8. 计算$G^*$并证明$\ker(I-G^*)$与$\ker(\bm I-\bm M^{\mathsf H})$线性同构。

9. 由$B^*=(I-G^*)C^*$与方阵秩相等得到两个零空间维数相等。

10. 第五步：由维数相等与第二条得单射与满射等价，开映射定理给出逆有界。

11. 用秩一算子走一遍证明，取$F=K$、$C=I$，得到$\bm M=\lambda/2$与标量矩阵方程。

12. 分$\lambda=1$（解$u=h+2x\int h$，取$h=1$核对）与$\lambda=2$（重现相容条件）两种情形读出结论。

13. 总结紧性的作用是化到有限维，并指出定理不给迭代格式。

14. 由第三条重新得到紧算子的非零谱点都是特征值，这是一条不依赖第18章的论证路线。

### 19.3 算子方程的稳定性

正文：[03-stability.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations/03-stability.tex)

1. 从数据误差进入，说明方程组用有限的条件数回答稳定性，本节说明无限维中这个数可以变成无穷并比较两类方程。

###### paragraph：适定问题

1. 说明稳定性要在固定范数后才有确切含义。

2. 给出适定与不适定问题的定义（`def:opeq-well-posed`）。

3. 以$V:L^2\to Y$在导数范数下等距为例，说明适定性依赖范数，而实际误差多在$L^2$下小。

4. 由开映射定理说明完备空间中失去稳定性必伴随失去存在性。

###### paragraph：趋于零的奇异值

1. 取扰动$\sigma_ju_j$，数据误差趋于零而解的误差恒为$1$，说明$g\mapsto f^\dagger$无界。

2. 有限秩时由$\sigma_{\min}$得到放大上界，$T$上至多三倍，说明决定放大的是奇异值离零的距离。

3. 陈述紧算子的像不闭定理（`thm:opeq-compact-range`）。

4. 证明逆无界的第一段：若逆有界则像中有界序列有收敛子列。

5. 证明逆无界的第二段：无限维子空间的标准正交序列无收敛子列，得出矛盾。

6. 用开映射定理证明像不闭。

7. 总结不适定是无限秩紧算子第一类方程的共同性质。

###### paragraph：累积积分的误差放大

1. 给出真解$f=1$、数据$g=x$与扰动$\delta u_{20}$的具体数据。

2. 算出放大倍数约$61$、解的范数误差约$0.61$、振幅约$0.87$。

3. 配图`fig:opeq-noise-amplification`并列几乎重合的数据与带强振荡的解。

4. 把放大解释为求导的不稳定，并用$\sin(n\pi x)/n$说明求导在$L^2$下不连续。

###### paragraph：离散之后：病态与不适定

1. 写出$\bm A_n$的逆是差商，说明每个离散问题都适定。

2. 给右端加交错扰动，算出$n=4$、$\varepsilon=0.01$时的解扰动。

3. 用加权范数算出放大倍数$\sqrt{n(4n-3)}$，给出$n=4$与$n=1000$的数值。

4. 由图说明奇异值随$n$逼近$V$的奇异值，最小奇异值约$1/(2n)$，条件数约$4n/\pi$。

5. 配图`fig:opeq-discrete-singular-values`展示$\bm A_n$的奇异值与条件数增长。

6. 区分病态（定量）与不适定（定性），指出加密网格不能消除困难。

###### paragraph：有限截断与误差的两部分

1. 定义截断解$f_m^\delta$，说明截断算子范数为$1/\sigma_m$。

2. 把误差拆成舍弃部分与噪声放大两个正交部分，得到式`eq:opeq-truncation-split`。

3. 以$f=1$、$\delta=0.01$逐项计算，指出最好的上界在$m=5$附近。

4. 表`tab:opeq-truncation`列出不同$m$的舍弃项、放大项与合计。

5. 说明截断稳定但不再精确，截断位置须结合误差水平选择，并指向卷五与卷二。

###### paragraph：第二类方程与共振参数

1. 在紧自伴情形写出逆算子范数公式（式`eq:opeq-resolvent-norm`），说明零空间平凡时公式仍成立。

2. 说明靠近$1/\mu_k$时误差被放大，在$T$上写出范数并由图解读$\lambda=0.99$时放大$100$倍的例子。

3. 比较两类方程的敏感性：第二类集中在共振参数的有限个方向上，第一类无法消除。

###### paragraph：算子的扰动

1. 由$B+E=B(I+B^{-1}E)$与Neumann级数得到扰动判据与范数上界（式`eq:opeq-operator-perturbation`）。

2. 应用到有限秩近似，并比较$\lambda=\frac12$与$\lambda=0.99$时对近似精度的要求。

3. 用对角算子的截断说明第一类方程不能用同样论证，恒等项提供了可逆主部。

### 19.4 本章小结

正文：[04-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/10-linear-operator-equations/04-summary.tex)

1. 第一段回到无限大矩阵的类比，并由表引出比较。

2. 表`tab:opeq-summary`并列方程组、第一类、第二类在像、可解条件、零空间与误差放大上的差别。

3. 第二段综述第一类方程的正交条件、Picard条件、最小范数解与$V$的求导解释。

4. 第三段综述第二类方程的Neumann级数、Fredholm择一与紧性造成的闭像。

5. 第四段综述适定性、无限秩紧算子的无界逆、病态与不适定的关系、截断误差及共振敏感性。

6. 第五段划定范围，把正则化交给卷五，并引向用有限个简单函数逼近目标函数的下一章。

## 第20章 函数逼近

正文入口：[11-function-approximation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation.tex)，章内依次输入[01-integrable-function-approximation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/01-integrable-function-approximation.tex)、[02-approximation-error.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/02-approximation-error.tex)、[03-fixed-subspaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/03-fixed-subspaces.tex)、[04-best-n-term.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/04-best-n-term.tex)、[05-adaptive-piecewise.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/05-adaptive-piecewise.tex)、[06-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/06-summary.tex)。

章职责与主线：本章沿用第10章“函数是无限维向量”的类比，把函数逼近看成向量向低维替身的投影，沿“能否逼近—误差多大—怎样选择候选集合”展开。先在$L^p$中用简单、连续、光滑函数逼近可积函数，并核对测度、指数与$L^\infty$的失效；再以点到候选集合的距离定义最佳误差，比较尺子与候选集合对最近点的影响，并用Fourier截断计算丢掉坐标的代价和混叠；最后比较固定子空间、最佳$N$项与自适应分段三种替身。贯穿例子为折线$f_*(x)=\lvert x-\frac12\rvert$、$\sqrt x$与在$3/4$处跳跃的阶梯函数，正则性的系统刻画交给第21—23章。

1. 章首第一段从第10章的长向量类比和计算机只能存放有限个数出发，提出选低维替身及其距离的问题。

2. 第二段用$\mathbb R^3$中向量$(3,4,1)$到$xy$平面的垂足算出误差$1$，说明函数逼近做的是同一件事，只是平面换成函数子空间。

3. 第三段列出目标、尺子、候选集合三要素，由此提出能否趋零、给定预算的最小误差、选哪种候选集合三个问题。

4. 第四段说明20.1回答定性问题，20.2加入预算并用Fourier截断计算丢掉坐标的代价。

5. 第五段说明后三节分别对应事先固定投影平面、固定坐标轴但挑选坐标、连坐标轴也按目标调整，并交代三个贯穿例子。

6. 第六段指出有限维直觉的两处修正：单位球不紧使函数类没有共同速率，范数不等价使结论随尺子改变。

7. 第七段划定范围：正则性刻画分别由第21、22、23章承担，带误差数据的拟合属于卷五。

### 20.1 可积函数的逼近

正文：[01-integrable-function-approximation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/01-integrable-function-approximation.tex)

1. 以有理向量在$\mathbb R^n$中稠密作对照，提出不规则的可积函数能否被结构简单的函数接近。

2. 用第1、2章的稠密性与距离判据表述问题，交代依次使用简单、连续、光滑函数并核对测度、指数与范数。

#### 20.1.1 简单函数逼近

1. 写出简单函数$\sum c_i\mathbf 1_{A_i}$，类比为分量舍入到有限档位的向量，提出第5章的分层在$L^p$范数下是否收敛。

###### paragraph：截断与取值分层

1. 定义二进分层并截断的$s_n$（式`eq:fapprox-dyadic-simple`），把$\lfloor2^nf\rfloor/2^n$解释为舍入、$\min$解释为压低大分量。

2. 列出$s_n$只取有限多个值、$0\leq s_n\leq f$、在$f<n$处误差小于$2^{-n}$，得到逐点收敛。

3. 陈述定理`thm:fapprox-simple-dense`。

4. 证明第一段对非负函数用控制函数$f^p$与控制收敛定理得$L^p$收敛。

5. 证明第二段由Chebyshev不等式得到取值集合测度有限。

6. 证明第三段分正负部、实虚部后由三角不等式组合。

7. 指出$p<\infty$的两处用途，并说明定理没有给出可数稠密族。

8. 例子取$f(x)=x^{-1/3}$、$p=2$，把误差分成截断与舍入两部分。

9. 例子算出截断部分的平方误差恰为$1/n$。

10. 例子合并得$\lVert f-s_n\rVert_2^2\leq1/n+4^{-n}$，说明慢的是截断误差。

11. 例子指出$p=3$时$f\notin L^3$，定理不适用。

###### paragraph：Lebesgue区域上的可数逼近族

1. 类比有理分量，定义有理矩形与有理复系数的有限组合族$\mathcal D$，说明它可数。

2. 陈述定理`thm:fapprox-separable`。

3. 证明把问题化为用有理矩形有限并按对称差测度逼近有限测度集。

4. 第一步由Lebesgue测度的定义取可数矩形覆盖。

5. 第二步截取有限个，使对称差测度小于$2\varepsilon$。

6. 第三步把端点外移到有理数，使对称差测度小于$3\varepsilon$，并切成不交有理矩形。

###### paragraph：一般测度空间的条件

1. 指出证明只用到可数个有限测度集按测度逼近所有有限测度集这一条件。

2. 以不可数集上的计数测度为反例，单点示性函数两两距离$2^{1/p}$，故$\ell^p(I)$不可分。

###### paragraph：有界函数与本质上确界

1. 把$L^\infty$范数比作最大分量，取$\mathbf 1_{[0,t]}$两两距离为$1$，由不可数个不交球推出不可分。

2. 对本质有界函数取有界代表并分层，得$\lVert f-s_n\rVert_\infty\leq2^{-n}$，简单函数在$L^\infty$中仍稠密。

3. 解释两结论不矛盾：水平集有不可数多种，有理矩形按测度逼近集合不能控制本质上确界。

#### 20.1.2 光滑函数逼近

1. 说明需要先对连续或光滑函数推导，交代开紧逼近、平移连续、卷积磨光三步。

###### paragraph：紧支撑连续函数

1. 回用第7章的Lebesgue正则性，取$K\subseteq A\subseteq U$，提出用连续斜坡磨掉示性函数的棱角。

2. 陈述定理`thm:fapprox-cc-dense`。

3. 证明化为逼近有限测度集的示性函数，并单独处理$K$为空集。

4. 证明把$U$缩小为有紧闭包的$U'$。

5. 证明定义距离比斜坡函数$\varphi$，核对连续性、取值与紧支撑。

6. 证明说明$\mathbf 1_A-\varphi$只在$U\setminus K$上非零，得误差估计。

###### paragraph：平移的$L^p$连续性

1. 说明磨光是平移的平均，把平移比作下标错位，并由平移不变性提出$L^p$连续性问题。

2. 陈述定理`thm:fapprox-translation`。

3. 证明先对$C_c$函数用一致连续估计。

4. 证明再由稠密性和三角不等式推广到一般$f$。

5. 用$\mathbf 1_{[0,1/2]}$说明$p=\infty$时平移误差恒为$1$。

###### paragraph：磨光的$L^p$收敛

1. 回顾第7章磨光核，把磨光解释为加权滑动平均。

2. 陈述定理`thm:fapprox-mollifier`（式`eq:fapprox-mollifier-error`）。

3. 证明用$\int\rho_\varepsilon=1$把$f(x)$写进平均。

4. 证明由Hölder不等式把$p$次方移进积分。

5. 证明由Tonelli定理得平移误差的加权平均，取上确界。

6. 对$\mathbf 1_{[0,1/2]}$算出$\lVert f_\varepsilon-f\rVert_p^p=4\varepsilon\int_0^1T^p$。

7. 由此读出$L^p$误差按$\varepsilon^{1/p}$下降，$p=\infty$时误差保持$1/2$，并引出图`fig:fapprox-mollifier-norms`。

8. 图`fig:fapprox-mollifier-norms`展示跳跃函数的磨光曲线和三种范数误差随$\varepsilon$的变化。

###### paragraph：光滑紧支撑函数与局部逼近

1. 先取$g\in C_c(\Omega)$逼近$f$并延拓为零。

2. 由卷积支撑和定理`thm:fapprox-mollifier`得$C_c^\infty(\Omega)$在$L^p(\Omega)$中稠密。

3. 对局部可积函数在紧集的闭邻域上截断。

4. 说明在紧集上磨光不受截断影响，得局部收敛，代价是只在远离边界的紧集上成立。

###### paragraph：$L^\infty$中的失效

1. 对$\mathbf 1_{(0,1/2]}$，由几乎处处不等式与连续性在$x=1/2$处夹出$r\geq1/2$。

2. 总结本节结论都是定性的，要比较效率须固定参数个数。

### 20.2 逼近误差

正文：[02-approximation-error.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/02-approximation-error.tex)

1. 回到投影图景，说明本节依次定义最佳误差、比较候选集合与尺子、计算Fourier截断。

#### 20.2.1 目标、误差与表示预算

1. 规定目标$f$与预算$N$下的候选集合$\mathcal A_N$，列举维数、项数、段数三种预算。

2. 提出以最好的候选度量集合的好坏。

3. 给出定义`def:fapprox-best-error`（式`eq:fapprox-best-error`）。

4. 把最佳误差解释为点到集合的距离，重述稠密性结论。

5. 区分最佳误差与具体构造的误差。

###### paragraph：三种预算

1. 次数小于$N$的多项式是$N$维线性空间，类比固定平面。

2. 至多$N$个基向量的组合在$\mathbb R^2$中是两条坐标轴的并，不对加法封闭；可动分点的分段常数同样如此。

3. 定义非线性逼近，与固定线性空间中的逼近区分。

###### paragraph：单个函数与函数类

1. 给出函数类的最坏误差（式`eq:fapprox-worst-case`）。

2. 以Hilbert空间单位球为例，单个函数误差趋零而最坏误差恒为$1$，并与$\mathbb R^n$对照。

3. 把有限候选集的最坏误差不超过$\varepsilon$等同于闭球覆盖。

4. 给出反向论证，覆盖数描述用$N$个固定函数逼近函数类的最坏误差。

#### 20.2.2 固定空间中的最佳逼近

1. 提出有限维子空间中下确界能否取到。

2. 陈述定理`thm:fapprox-existence`并用有限维闭球的紧性证明。

3. 指出证明依赖有限维，无限维要靠第12章的完备性与平行四边形恒等式。

4. 用$\mathbb R^2$最大值范数与直线的例子说明最近点可以不唯一。

5. 引出图`fig:fapprox-nearest-point`，用吹大球的方式解释最近点个数。

6. 图`fig:fapprox-nearest-point`对比圆与正方形碰到直线的情形，并画出候选集合$\Sigma_1$。

###### paragraph：Hilbert空间中的正交投影

1. 回用第12章的正交投影，写出勾股关系（式`eq:fapprox-pythagoras`）与投影公式，指出线性性。

2. 例子把$x^2$投影到一次函数，算出$P_Vf=x-1/6$与误差平方$1/180$。

###### paragraph：不同的尺子，不同的最佳近似

1. 推导一致范数下的最佳常数（式`eq:fapprox-best-constant`）。

2. 与$L^2$平均值对比，$x^2$的两种最佳常数分别是$1/3$与$1/2$。

3. 用$x$、$-x^2$及其和说明一致逼近的最佳选择不是线性的。

#### 20.2.3 正交展开的截断误差

1. 把Fourier系数看作坐标，固定周期$1$的基与系数，由第14章和变量代换得到Parseval等式。

###### paragraph：平方误差与保留维数

1. 写出$P_K$与尾和公式（式`eq:fapprox-fourier-tail`），引出锯齿与三角波的比较。

2. 对锯齿函数分部积分，算出系数和$K=10,40$时的误差。

3. 对三角波代换、分部积分，算出系数与$K^{-3/2}$的误差。

4. 比较多变量两种截断的系数个数，$d=2,K=10$时为$441$与$317$。

###### paragraph：一致误差

1. 系数绝对可和时得到连续代表和绝对尾和界（式`eq:fapprox-uniform-tail`）。

2. 三角波的绝对尾和在$x=1/2$处取等，$K=10$时一致误差为$0.0101$。

3. 锯齿函数因跳跃而一致误差不趋零，由图`fig:fapprox-fourier-truncation`(a)说明。

4. 比较平方尾和与绝对尾和，由图`fig:fapprox-fourier-truncation`(b)读出不同速率。

5. 图`fig:fapprox-fourier-truncation`展示锯齿函数的截断和三种误差的速率。

###### paragraph：理论截断与离散计算

1. 写出离散系数，解释为只读$M$个分量。

2. 代入绝对收敛级数，由几何和得混叠公式（式`eq:fapprox-aliasing`）。

3. 三角波$M=4,k=1$时由采样值算出$\hat f_4(1)=1/8$。

4. 用混叠公式和奇数平方倒数和复算出$1/8$，并引出图`fig:fapprox-aliasing`。

5. 图`fig:fapprox-aliasing`展示两个频率的余弦采样相同，以及被叠到一起的频率。

6. 由正交性写出离散截断的误差分解（式`eq:fapprox-discrete-error`）。

7. 分别解释截断误差与离散误差，说明二者应分别预算。

#### 20.2.4 连续频带截断

1. 把频率下标改为连续的$\xi$，沿用第14章的归一化与Plancherel等式。

2. 定义$Q_W$与带限函数空间，得频域尾积分公式（式`eq:fapprox-band-tail`）。

3. 对Gauss函数估计尾积分，比较$W=1,1.5$时的实际误差与界。

4. 用平移sinc函数说明$\mathcal B_W$无限维，有限计算还需进一步离散。

### 20.3 固定子空间的选择

正文：[03-fixed-subspaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/03-fixed-subspaces.tex)

1. 把固定子空间类比事先选定投影平面。

2. 交代在一致范数下比较多项式、分段多项式和张量积。

3. 引入贯穿目标$f_*$。

#### 20.3.1 多项式逼近

1. 提出多项式能否一致逼近连续函数，并从构造中读取误差。

###### paragraph：连续模

1. 说明需要记录小尺度变化的量。

2. 给出定义`def:fapprox-modulus`（式`eq:fapprox-modulus`）。

3. 说明单调性、与一致连续的等价及Lipschitz情形。

4. 算出折线与平方根的连续模，比较$\delta$与$\sqrt\delta$。

###### paragraph：Bernstein多项式

1. 定义$B_mf$（式`eq:fapprox-bernstein`），说明它是结点值的凸组合。

2. 手算$B_4f_*(1/2)=3/16$。

3. 提出还需权重集中。

4. 陈述引理`lem:fapprox-bernstein-moments`（式`eq:fapprox-bernstein-moments`、`eq:fapprox-bernstein-variance`）。

5. 证明用组合恒等式得前两个矩。

6. 证明展开平方得方差公式。

7. 引出按远近分组估计。

8. 陈述定理`thm:fapprox-bernstein`（式`eq:fapprox-bernstein-error`）。

9. 证明写出误差并估计近邻组。

10. 证明用方差公式估计远处组。

11. 证明说明$\delta$与$m$的选取次序。

12. 称为Weierstrass逼近定理，说明推广到任意紧区间。

13. 指出$B_m$线性但不是投影，由图`fig:fapprox-bernstein`(a)读出误差约减半。

14. 图`fig:fapprox-bernstein`展示折线的Bernstein多项式及$B_{16}$与最佳二次多项式的误差曲线。

###### paragraph：附加光滑性与误差速率

1. 区分能任意逼近与给定次数下的误差。

2. 对Lipschitz函数用Cauchy--Schwarz不等式得$L/(2\sqrt m)$。

3. 对$\sqrt x$得$(4m)^{-1/4}$。

4. 由$B_m(x^2)$说明Bernstein构造不是最佳近似。

5. 例子定义$p^*$并算出误差$1/16$。

6. 例子列出五点交替取值。

7. 例子设更好的二次多项式$q$，比较$p^*-q$的符号。

8. 例子由零点个数得矛盾，最佳误差小于$B_{16}$的误差。

9. 陈述Jackson型定理（式`eq:fapprox-jackson`），说明未证及其含义。

10. 指出多项式的全局性，引出分段表示。

#### 20.3.2 固定网格上的分段逼近

1. 固定结点与网格尺寸，说明候选集合仍是固定线性空间。

###### paragraph：分段常数与分段多项式

1. 由最佳常数公式得$\omega_f(h)/2$与一阶速率，并举$f(x)=x,N=4$。

2. 用中点Taylor多项式得$h^{r+1}$，说明前提。

###### paragraph：分段线性插值

1. 定义$S_hf$（式`eq:fapprox-linear-interpolant`）及$N+1$维空间。

2. 引入帽形函数，结点值即坐标，并结合图`fig:fapprox-spline-rates`(a)对比多项式的全局性。

3. 陈述定理`thm:fapprox-linear-interpolation`（式`eq:fapprox-interpolation-modulus`、`eq:fapprox-interpolation-quadratic`）。

4. 证明连续模界。

5. 证明构造辅助函数并两次用Rolle定理。

6. 证明得误差公式与$h^2/8$的界。

7. 比较两个界的依据，并用$x^2$说明常数$1/8$不可改进。

###### paragraph：局部正则性与网格位置

1. 等距奇数网格下折线误差恰为$h/2$，结合图`fig:fapprox-spline-rates`(b)(c)比较$\sin\pi x$。

2. 图`fig:fapprox-spline-rates`展示帽形函数、折线的插值和两种目标的误差。

3. 结点含$1/2$时插值精确，说明折点位置未知是自适应的动机。

###### paragraph：拼接条件与维数

1. 连续分段线性函数维数减少而阶不变。

2. 计算$k$次样条维数$N+k$，说明样条逼近阶未证及衔接条件的代价。

###### paragraph：与全局多项式的比较

1. 比较相同维数下全局多项式利用整体光滑性、分段多项式利用局部光滑性。

#### 20.3.3 张量积表示

1. 定义一维函数的张量积。

2. 把多元函数的坐标类比为矩阵和高阶张量。

###### paragraph：网格插值与组合误差

1. 定义二维张量积插值（式`eq:fapprox-tensor-interp`），结合图`fig:fapprox-tensor-grid`(a)解释双线性插值。

2. 图`fig:fapprox-tensor-grid`展示乘积基的支撑与四个角点，以及系数个数随维数的增长。

3. 说明$I_x$不放大一致范数。

4. 逐方向拆分误差，给出$d$维误差界。

###### paragraph：成本随维数的增长

1. 由$h^2\leq8\varepsilon/d$算出$d=2,6$时的系数个数，定义维数灾难。

2. 区分存储系数、点值计算与取样次数的计数对象。

### 20.4 最佳N项逼近

正文：[04-best-n-term.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/04-best-n-term.tex)

1. 说明固定选法可能浪费预算，转为按目标挑选基向量。

2. 用$\mathbb R^5$的向量比较留前两个与留最大两个坐标，平方误差为$4.2$与$0.21$。

3. 定义$\Sigma_N$。

4. 给出定义`def:fapprox-best-n-term`（式`eq:fapprox-best-n-term`）。

5. 说明$\Sigma_N$的非线性来自支撑依赖目标，并参见图`fig:fapprox-nearest-point`(c)。

#### 20.4.1 固定截断与自适应选择

1. 写出固定截断的误差，比较自适应选择。

2. 以$f=e_{N+1}$和跳跃函数的小波系数说明差距。

3. 说明自适应选择需要知道系数，最佳误差不等于算法代价。

#### 20.4.2 最大系数选择

1. 由平方可和给出系数的非增排列。

2. 陈述定理`thm:fapprox-largest-coefficients`（式`eq:fapprox-largest-coefficients`）。

3. 证明用Parseval等式按坐标拆误差，得固定支撑的最优系数。

4. 证明比较支撑，得下界并由$g_N$达到。

5. 解释证明依赖正交性和方向与系数可分开选择，冗余字典不成立。

6. 用$1.2\varphi+\psi_{2,0}$给出一致范数下最大系数规则失效的反例。

###### paragraph：Haar展开中的选择

1. 回用第15章的Haar基，取在$3/4$处跳跃的阶梯函数。

2. 逐个算出系数$2,1,0,\sqrt2$，$j\geq2$的内积为零。

3. 写出三项展开并用Parseval等式检验。

4. 比较固定次序与最大系数选择的误差平方$2$、$1$，三项时精确。

5. 由图`fig:fapprox-best-n-term`解释跳跃位置决定应保留的细节系数。

6. 图`fig:fapprox-best-n-term`对照两种两项逼近和前四个系数。

### 20.5 自适应分段逼近

正文：[05-adaptive-piecewise.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/05-adaptive-piecewise.tex)

1. 说明固定网格的局限，把分点移动类比为按目标调整坐标轴。

2. 交代预算、范数及存在、误差、算法三个问题。

###### paragraph：候选集合与局部误差

1. 定义$\mathcal S_N$与自适应分段逼近。

2. 由最佳常数公式把问题化为最小化最大局部振幅（式`eq:fapprox-adaptive-error`）。

###### paragraph：平方根函数的比较

1. 等距网格误差为$1/(2\sqrt N)$。

2. 分点$(i/N)^2$使振幅相等，误差为$1/(2N)$，并引出图`fig:fapprox-adaptive`(a)(b)。

3. 由振幅和为$1$证明该分割最优。

4. 图`fig:fapprox-adaptive`展示$N=6$的两种分割和三种方法的误差。

###### paragraph：单调函数的误差界

1. 指出例子只用到单调性。

2. 陈述定理`thm:fapprox-monotone`（式`eq:fapprox-monotone`）。

3. 证明振幅和给出下界。

4. 证明用水平集分点构造分割。

5. 证明得到上界。

6. 解释误差依赖总变化量而不是连续模。

###### paragraph：最佳分割的存在

1. 说明局部振幅关于端点连续。

2. 由分点集的紧性得最佳分割存在，并与有限维存在定理对照。

3. 区分存在性、误差界与寻找方法。

###### paragraph：贪心细分

1. 描述按最大局部误差对半细分的算法。

2. 用$\sqrt x$跑前三步。

3. 列出四个单元的振幅，误差$0.1768$与最优$0.125$比较。

4. 由表`tab:fapprox-greedy`说明此例贪心约为最优的$\sqrt2$倍，是计算观察而非定理。

5. 表`tab:fapprox-greedy`列出等距、贪心与最优的误差。

6. 连接二进细分、Haar细节系数与第22章。

### 20.6 本章小结

正文：[06-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/11-function-approximation/06-summary.tex)

1. 回应章首的投影图景与三个问题。

2. 总结定性逼近及其在$L^\infty$的失效。

3. 总结最佳误差的定义和有限维、Hilbert、其他范数下的差别。

4. 总结Fourier截断、混叠与带限逼近。

5. 总结三种候选集合的关键结论，引出表`tab:fapprox-three-candidates`。

6. 表`tab:fapprox-three-candidates`对照三种方法的向量类比、线性与误差决定因素。

7. 说明有限维投影图景保留什么、在哪里失效。

8. 把各误差所需的正则性交给第21—23章。

## 第21章 Sobolev空间

正文入口：[12-sobolev-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces.tex)，章内依次输入[01-derivative-control.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/01-derivative-control.tex)、[02-norms-and-completeness.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/02-norms-and-completeness.tex)、[03-smooth-density.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/03-smooth-density.tex)、[04-extension.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/04-extension.tex)、[05-constrained-subspaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/05-constrained-subspaces.tex)、[06-continuous-embeddings.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/06-continuous-embeddings.tex)、[07-compact-embeddings.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/07-compact-embeddings.tex)、[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/08-summary.tex)。

章职责与主线：本章沿用第10章“函数是无限维向量”的类比，把Sobolev范数理解为对高频坐标加权的范数：在余弦坐标下$H^1(0,1)$恰好是权为$1+\pi^2n^2$的加权$\ell^2$空间，并在每处说明类比在$p\neq2$、$k\geq2$和一般区域上的边界。全章先由振荡、折点与跳跃说明为何同时控制函数与弱导数，建立范数、完备性与Hilbert结构；再研究光滑稠密、跨边界延拓、零边界与零均值约束；最后区分连续嵌入与紧嵌入，用集中序列说明二者在临界指数处的差别。章首有五个自然段：

1. 第一段回到无限维向量的看法，指出$L^2$范数对每个坐标一视同仁，看不见$\sin(2\pi nx)$振荡的快慢。

2. 第二段提出给高频坐标加权的图景，说明把求导放进范数正是这样的加权，并允许$|x-1/2|$这样的折点函数留在空间中，导数按第7章的弱导数理解。

3. 第三段说明前半路线：21.1用三类例子给出动机和加权坐标，21.2建立范数、完备性和Hilbert结构，随后三节研究逼近、延拓和约束。

4. 第四段说明后半路线：连续嵌入回答单个函数被控制到什么程度，紧嵌入回答有界函数列能否选出收敛子列，两者都由$p$与$d$的比较决定，在临界指数处有实质差别。

5. 第五段划定范围：只处理整数阶、重点在$W^{1,p}$、函数取实值；分数阶和按尺度的刻画在第22章，连续点值的Hilbert空间在第23章。

### 21.1 导数控制

正文：[01-derivative-control.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/01-derivative-control.tex)

1. 指出$L^2$只记录“有多大”，说明本节比较正弦、常数、折点和阶跃四类函数，各自暴露振荡被遗漏、高度被遗漏和不可经典求导函数的取舍问题。

#### 21.1.1 振荡函数

1. 对$f_n(x)=\sin(2\pi nx)$用半角公式算出$\lVert f_n\rVert_2=1/\sqrt2$，说明$L^2$大小与$n$无关。

2. 计算$f_n'$并得到$\lVert f_n'\rVert_2=\sqrt2\pi n$，结合图说明导数范数记录单位长度内的摆动程度。

3. 配图sobolev-oscillation：左为$f_1$与$f_4$，振幅和$L^2$长度相同；右为两种范数随$n$的变化，一条水平、一条线性增长。

###### paragraph：高频坐标上的权重

1. 把$\sqrt2\sin(2\pi nx)$看作正交的单位向量，$f_n$是沿第$n$条轴的向量，求导把它送到余弦轴并把长度乘以$2\pi n$。

2. 把长度平方改为函数平方加导数平方，第$n$条轴上出现权$1+(2\pi n)^2$，解释为把球压成沿高频方向很短的椭球。

3. 在有限维取三点取值$u$和相邻差分$D$，写出二次型$\lVert Du\rVert^2=u^\top D^\top Du$及矩阵$D^\top D$。

4. 逐个验证常向量、斜坡、锯齿是特征向量，特征值为$0,1,3$，说明形状越抖特征值越大。

5. 指出$\lVert u\rVert^2+\lVert Du\rVert^2$在这些方向上的权是$1,2,4$，用锯齿核对$\lVert Dz\rVert^2=18=3\lVert z\rVert^2$，并对比有限维权有界、无限维权无界，由此解释求导在$L^2$上不是有界算子。

###### paragraph：常数方向

1. 说明常数的导数为零，只看导数无法区分不同高度，导数度量变化、高度由函数本身记录。

2. 由此得出完整度量必须同时保留$\lVert f\rVert_2$和$\lVert f'\rVert_2$，只有排除常数方向后导数才可能单独控制函数，回指21.5.4。

#### 21.1.2 折点与跳跃

1. 指出坚持经典导数会排除$|x-1/2|$，提出用弱导数检查。

2. 在折点两侧分部积分，边界项因$f(1/2)=0$和测试函数的紧支撑而消失，得到弱导数$\operatorname{sgn}(x-1/2)$。

3. 算出$\lVert f\rVert_2^2=1/12$、$\lVert f'\rVert_2^2=1$，说明这类函数组成21.2的$H^1(0,1)$。

4. 对阶跃函数$H$算出$-\int H\varphi'=\varphi(1/2)$，说明跳跃把测试函数送到跳跃点的值。

5. 配图sobolev-kink-step：四幅小图依次为折点函数、它的弱导数、阶跃函数和阶跃对测试函数的点值作用。

6. 用测试函数判别证明这一作用不能写成局部可积函数的积分，所以$H$没有弱导数。

7. 指出$H$几乎处处导数为$0$而$0$不是弱导数，强调Sobolev空间中的导数始终指弱导数。

###### paragraph：用余弦坐标比较

1. 引入余弦正交归一基$e_n$及坐标$a_n$，说明完备性来自偶延拓后的Fourier基，选用余弦基的理由留到21.2.3。

2. 由对称性和分部积分算出折点函数的坐标：$a_0=1/4$，$a_{2m}=\sqrt2/(\pi^2m^2)$（$m$为奇数），其余为零。

3. 直接积分算出阶跃函数的坐标，奇数项绝对值为$\sqrt2/(\pi n)$，并比较折点按$1/n^2$、阶跃按$1/n$衰减。

4. 定义加权部分和$S_N$，折点函数每项为$8/(\pi^2m^2)$，用$\sum_{m\text{奇}}m^{-2}=\pi^2/8$得$S_N\to1=\lVert f'\rVert_2^2$。

5. 阶跃函数每个奇数项都是$2$，$S_N$线性发散，结合图对比两条路径。

6. 配图sobolev-cosine-coordinates：左为两函数的坐标绝对值，右为加权部分和，折点收敛到$1$、阶跃线性增长。

7. 总结Sobolev范数有限等于坐标加权后仍平方可和，并指出跳跃的按尺度度量由第22章回答。

### 21.2 Sobolev范数与完备性

正文：[02-norms-and-completeness.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/02-norms-and-completeness.tex)

1. 说明本节固定区域、阶数和指数，把函数与各阶弱导数的$L^p$大小合成范数，再证明完备性并写出$p=2$时的内积和坐标形式。

#### 21.2.1 空间的定义

1. 约定开集、多重指标和弱导数记号。

2. 用Hölder不等式说明$L^p$函数局部可积，检验弱导数总有意义。

3. 引出函数与每个导数各占一项的范数。

4. 定义$W^{k,p}(\Omega)$与Sobolev范数，分$p<\infty$和$p=\infty$两种形式。

5. 解释阶数、指数、区域的分工，并说明$W^{0,p}=L^p$及记号简写。

6. 验证范数：齐次性、对分量用$L^p$的Minkowski不等式再用$\ell^p$合并、零范数给出零等价类。

7. 得到求导映射从$W^{k,p}$到$L^p$连续的估计，并用$f_n$说明求导在$L^p$上不连续，连续性来自定义域的选择。

8. 把$f$对应到乘积空间中的长向量，Sobolev范数是长向量的范数，指出分量受测试恒等式约束，这是与独立坐标不同之处。

9. 说明元素是等价类、点值一般无意义，判断属于空间须核对积分恒等式。

10. 例子：折点函数的$W^{1,2}$范数平方为$13/12$，$W^{1,\infty}$范数为$1$，并用$\operatorname{sgn}=2H-1$证明它不属于$W^{2,p}$。

#### 21.2.2 完备性

1. 说明各分量有$L^p$极限，需证明约束在极限下保持，即长向量子集是闭的。

2. 定理：$1\leq p\leq\infty$时$W^{k,p}(\Omega)$是Banach空间。

3. 证明分三步：取各分量极限，用Hölder不等式把测试恒等式传到极限得$g_\alpha=\partial^\alpha f$，合并分量得范数收敛。

4. 指出关键是测试恒等式两边对$L^p$收敛连续，证明不涉及边界形状也不给出逐点收敛。

#### 21.2.3 Hᵏ空间

1. 定义$H^k=W^{k,2}$及内积。

2. 验证内积性质，写出$k=1$的形式$\int fg+\int\nabla f\cdot\nabla g$。

3. 说明Hilbert性依靠完备性，正交投影可用于闭子空间。

###### paragraph：一维$H^1$的加权坐标

1. 引入正弦基$s_n$及关系$e_n'=-\pi ns_n$，预告$H^1(0,1)$恰是加权$\ell^2$空间。

2. 定理：$f\in H^1(0,1)$当且仅当$\sum\pi^2n^2a_n^2<\infty$，且$\lVert f\rVert_{H^1}^2=\sum(1+\pi^2n^2)a_n^2$。

3. 证明：对绝对连续代表分部积分，$s_n$的端点零值消掉边界项，得$f'$的正弦坐标$-\pi na_n$；反向由部分和在$H^1$中的Cauchy性和完备性得到。

4. 说明余弦基不需要边界条件的原因，并用$f(x)=x$核对加权和等于$1$。

5. 引出对应表，强调加权坐标只是$p=2$、$k=1$时最干净的图景。

6. 表：对比三点差分与$H^1(0,1)$的坐标方向、权、零导数方向、$k\geq2$和$p\neq2$。

7. 解释$k\geq2$的失效：$f(x)=x$属于$H^2(0,1)$但$n^4a_n^2$不趋于零，余弦坐标只描述$f'(0)=f'(1)=0$的子空间，周期情形没有这个问题。

### 21.3 光滑函数的稠密性

正文：[03-smooth-density.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/03-smooth-density.tex)

1. 说明先证光滑函数情形再逼近的做法要求光滑函数在Sobolev范数下稠密，本节对任意开集和有限指数证明，工具是磨光和$L^p$磨光收敛。

###### paragraph：需要的两条磨光结论

1. 回用磨光核、$\Omega_\varepsilon$、磨光与弱导数交换，以及全空间上$L^p$磨光收敛。

2. 两条结论合用，得到全空间上$f*\rho_\varepsilon\to f$在$W^{k,p}$中成立。

###### paragraph：手算一次磨光

1. 用盒形核对$|x|$手算磨光，折点窗口内得到抛物线$(x^2+\varepsilon^2)/(2\varepsilon)$，窗口外不变。

2. 算出函数误差$(|x|-\varepsilon)^2/(2\varepsilon)$，上确界$\varepsilon/2$，导数误差只在宽$2\varepsilon$的窗口内。

3. 算出导数误差的$L^2$平方为$2\varepsilon/3$趋于零，而$L^\infty$误差恒为$1$，说明有限指数靠窗口变窄吸收误差，预告末尾的$p=\infty$反例。

###### paragraph：截断函数

1. 说明靠近边界允许的磨光半径变小，需要切块，因此需要截断函数。

2. 引理：紧集$K$含于开集$V$时存在取值$0$到$1$、在$K$上为$1$的$\eta\in C_c^\infty(V)$。

3. 证明：对$K$的$2\delta$邻域的指示函数做半径$\delta$的磨光。

4. 命名截断函数并说明其用途。

###### paragraph：乘积法则

1. 提出截断后是否仍在空间中取决于乘积的弱导数。

2. 引理：有界光滑函数乘Sobolev函数的乘积法则及算子有界性。

3. 证明：$k=1$用测试函数$\zeta\varphi$直接验证，高阶对$k$归纳。

###### paragraph：局部有限的单位分解

1. 定义分层开集$G_j$，说明其闭包紧、递增并穷尽$\Omega$。

2. 定义$V_j=G_{j+1}\setminus\overline{G_{j-2}}$和$K_j=\overline{G_j}\setminus G_{j-1}$，核对$K_j\subset V_j$与局部有限性。

3. 取截断函数$\eta_j$并令$S=\sum\eta_i$，说明$S\geq1$且光滑。

4. 令$\zeta_j=\eta_j/S$得到单位分解，并引向图。

5. 配图sobolev-partition-layers：$(0,1)$左半上的$\zeta_j$，以及各层允许的磨光半径。

6. 解释各层独立选半径是单位分解的任务。

7. 定理：任意开集、$1\leq p<\infty$时$C^\infty(\Omega)\cap W^{k,p}(\Omega)$在$W^{k,p}(\Omega)$中稠密。

8. 证明：分块并零延拓到全空间、逐块磨光使误差不超过$\theta2^{-j}$且支撑留在$V_j$、局部有限拼合后用单调收敛。

9. 说明定理对边界无要求，但逼近函数只在内部光滑。

10. 说明紧支撑光滑函数一般不稠密，光滑到边界需要延拓。

11. 用$|x-1/2|$和连续导数的比较严格证明$p=\infty$时距离至少为$1$。

### 21.4 跨边界延拓

正文：[04-extension.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/04-extension.tex)

1. 说明延拓到全空间的用途及其与补长向量的差别：补上的部分不能破坏弱导数，概述从反射到Lipschitz区域的路线。

###### paragraph：一维反射

1. 对绝对连续代表作$Ef(x)=f(|x|)$，说明它绝对连续，导数为$\operatorname{sgn}(x)f'(|x|)$。

2. 得到范数翻倍恒等式，用$f=1+x-x^2$手算$\lVert f\rVert_{H^1}^2=17/10$，延拓后为$17/5$。

3. 引向图，指出折点不破坏一阶弱导数。

4. 配图sobolev-reflections：同一函数的偶反射、零延拓和二阶反射。

###### paragraph：半空间上的偶反射

1. 定义半空间上光滑到边界函数的偶反射，切向偏导直接得到。

2. 对$i=d$在两侧分部积分写出两个等式，说明链式法则的符号。

3. 相加后边界项相消，得到$\partial_dEf$的公式和范数恒等式。

4. 说明一般函数的逼近：先截断，再向内平移并磨光，得到光滑到边界、支撑有界的函数。

5. 由稠密性和完备性把$E$延伸为有界线性算子。

###### paragraph：零延拓与边界相容条件

1. 定义零延拓，边界项不再抵消，常数$1$零延拓后成为阶跃函数。

2. 说明零延拓要求边界值为零，并指向迹和闭包空间。

###### paragraph：高阶延拓

1. 说明偶反射使法向导数在边界反号，$W^{2,p}$不够，高阶须让各阶法向导数相接。

2. 写出二阶反射公式，核对函数值和法向导数都相接。

3. 用$f=1+x-x^2$手算得$Ef=1+x+2x^2$，二阶导数跳跃但属于$L^p$。

4. 说明一般情形的范数估计和$k$阶的系数选取。

###### paragraph：Lipschitz区域

1. 说明局部图像条件和拉直的想法。

2. 定义Lipschitz区域。

3. 对比球、立方体、割缝圆盘，引向图。

4. 配图sobolev-lipschitz-domains：弯曲边界的局部坐标、方形角点、割缝圆盘的反例。

5. 定理：有界Lipschitz区域上存在有界线性延拓算子，延拓在固定有界集外为零。

6. 说明完整证明较长，给出构造的第一部分：有限覆盖、单位分解、内部块零延拓。

7. 给出构造的第二部分：边界块拉直、偶反射、变回，最后用固定截断函数。

8. 说明构造对高阶失效的原因，$C^k$边界可用光滑拉直，一般Lipschitz区域需要不同构造。

###### paragraph：光滑到边界的逼近

1. 指出延拓的推论是更强的逼近。

2. 定理：$C_c^\infty(\mathbb R^d)$的限制在$W^{1,p}(\Omega)$中稠密。

3. 证明：对延拓磨光再限制回$\Omega$。

4. 记为$C^\infty(\overline\Omega)$，与上一节定理比较，并预告用于边界值定义。

### 21.5 约束子空间

正文：[05-constrained-subspaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/05-constrained-subspaces.tex)

1. 说明边界是零测集、边界值不能直接读出，概述闭包定义、端点值、迹映射和导数范数四步。

#### 21.5.1 紧支撑光滑函数的闭包

1. 由紧支撑函数在边界附近为零引出定义思路。

2. 定义$W_0^{k,p}(\Omega)$，$p<\infty$。

3. 核验闭包对线性组合封闭，得闭线性子空间和Banach结构。

4. 说明定义不需边界正则性，一般是真子空间，全空间上由截断和磨光得$W_0^{k,p}=W^{k,p}$。

5. 说明定义限于$p<\infty$，$W^{1,\infty}$的闭包过小。

#### 21.5.2 端点值

1. 回用一维绝对连续代表，提出端点值是否受$H^1$范数控制。

2. 对$x$积分并用Cauchy--Schwarz，得$|\tilde v(y)|\leq\lVert v\rVert_2+\lVert v'\rVert_2\leq\sqrt2\lVert v\rVert_{H^1}$，点值是连续线性泛函。

3. 用尖峰$v_n$说明只有$L^2$控制不够，端点值靠导数项控制。

4. 配图sobolev-endpoint-spike：尖峰函数及其两种范数随$n$的变化，虚线为端点值$1$。

###### paragraph：点值作为坐标的线性泛函

1. 把读取点值写成与$(e_n(y))_n$的内积，并按权拆分。

2. 由Cauchy--Schwarz和$\sum1/(\pi^2n^2)=1/6$得常数$2/\sqrt3$，说明级数一致收敛到连续代表。

3. 对比$L^2$上$\sum e_n(y)^2$发散，说明有限维泛函都有界而无限维取决于权，预告维数升高后同样的和可能发散。

###### paragraph：零端点值

1. 由端点估计得$H_0^1(0,1)$中函数端点为零。

2. 常数$1$到紧支撑光滑函数的距离至少$1/\sqrt2$，紧支撑函数不稠密，反向包含是下一小节零迹刻画的一维情形。

#### 21.5.3 迹映射

1. 说明高维无连续代表，先在光滑函数上限制再推广。

###### paragraph：半空间上的估计

1. 固定$x'$沿法向积分，得$p=1$的估计。

2. $p>1$时对$|f|^p$的导数积分，得到含$p|f|^{p-1}|\partial_df|$的界，再用Young不等式放大。

3. 对$x'$积分得边界$L^p$估计，说明这是逐条法线上的一维机制，并给出高维尖峰$f(x,y)=v_n(y)$。

###### paragraph：Lipschitz区域上的迹

1. 定义表面测度及其因子的范围。

2. 迹定理：光滑到边界函数的迹估计及唯一有界线性算子$\operatorname{Tr}$。

3. 说明不等式的完整证明较长，给出局部拉直的思路。

4. 算子的构造：Cauchy列定义极限，交错排列证与逼近列无关，稠密性给出唯一性。

5. 说明迹是边界$L^p$中的等价类，由靠近边界的平均行为决定。

6. 零边界子空间等于零迹子空间，正向由连续性得到，反向说明思路并指向专著。

7. 用$x(1-x)\in H^2$但$f'(0)=1$说明高阶零迹需要法向导数条件。

#### 21.5.4 约束子空间中的导数范数

1. 提出排除常数方向后能否有$\lVert f\rVert_p\leq C\lVert\nabla f\rVert_p$，并命名Poincaré不等式。

###### paragraph：坐标中的常数方向

1. 在余弦坐标中指出第$0$个坐标的零权就是常数方向。

2. 零均值即$a_0=0$，余下的权至少$\pi^2$，得$\lVert f\rVert_2^2\leq\pi^{-2}\lVert f'\rVert_2^2$。

3. 零端点改用正弦坐标，边界项被零端点值消掉，得到同样的常数。

4. 说明常数$1/\pi$最优，用$x(1-x)$（比值$0.1$）和$x-1/2$（比值约$0.0833$）核对。

5. 说明此图景在$p\neq2$和一般区域上不适用，后面用积分估计。

###### paragraph：零边界情形

1. 说明零边界只需区域在一个方向上有界。

2. 定理：带状区域内$\lVert f\rVert_p\leq Lp^{-1/p}\lVert\partial_1f\rVert_p$。

3. 证明：沿$x_1$积分并用Hölder，再由闭包定义取极限。

4. 在$(0,1)$、$p=2$上比较定理常数$1/\sqrt2$和最优常数$1/\pi$。

###### paragraph：零均值情形

1. 说明零均值需要连通性，先在凸区域上证明。

2. 引理：凸区域上一点的值与平均之差受梯度与核$|x-z|^{1-d}$的积分控制。

3. 证明：沿线段积分，球坐标换元。

4. 定理：凸区域上的零均值Poincaré不等式及显式常数。

5. 证明：用Hölder和交换积分次序得核算子在$L^p$上有界，与引理合并，再由稠密性取极限。

6. 说明$W=(0,1)$时常数为$2$，比坐标结果宽松。

7. 陈述一般连通Lipschitz区域的结论及局部拼接思路，完整证明指向专著。

8. 给出由紧嵌入的反证路线。

###### paragraph：条件为什么不能少

1. 用不连通区域的分段常数和常数函数说明连通性与约束的必要性。

2. 用缩放$\psi(x/R)$说明有界方向的必要性，并解释为没有正的最小权。

###### paragraph：导数给出的等价范数

1. 写出零边界子空间上$\lVert\nabla f\rVert_p$与$W^{1,p}$范数的双侧估计并说明来源。

2. 得到等价范数和$H_0^1$上的等价内积，零均值子空间结论相同，整个空间上差别恰为常数方向。

### 21.6 连续嵌入

正文：[06-continuous-embeddings.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/06-continuous-embeddings.tex)

1. 说明一维有界而高维取决于$p$与$d$，提出本节问题。

2. 定义连续嵌入。

3. 说明区域有界和Lipschitz各自的用途。

###### paragraph：缩放决定指数

1. 设想不等式成立，用$u_\lambda$算两边的缩放指数。

2. 由指数相等得$p^*=dp/(d-p)$，以$d=3$、$p=2$、$p^*=6$核对。

3. 说明缩放只确定指数，不证明不等式，并解释维数的作用。

#### 21.6.1 更高指数的可积性

1. 引出$p<d$时的结论。

2. 定理：$\lVert f\rVert_{L^{p^*}}\leq C\lVert f\rVert_{W^{1,p}}$，较小指数由有限测度得到。

3. 说明证明分四步。

###### paragraph：第一步：p=1的全空间估计

1. 沿每个坐标方向积分，得不依赖该坐标的上界$g_i$。

2. $d=2$时相乘并分离积分，得$\lVert u\rVert_2\leq\lVert\nabla u\rVert_1$。

3. 引出分离变量的乘积估计。

4. 引理：$d$个各少一个变量的函数之积的积分不超过它们$L^{d-1}$范数之积。

5. 证明：对维数归纳，依次用Hölder、归纳假设和$d$个指数的推广Hölder。

6. 把$d$个界相乘，用引理得$\lVert u\rVert_{d/(d-1)}\leq\lVert\nabla u\rVert_1$。

###### paragraph：第二步：1<p<d

1. 把估计用于$|u|^\gamma$并用Hölder。

2. 选$\gamma=p(d-1)/(d-p)$使两侧范数相同，约去后得$\lVert u\rVert_{p^*}\leq\gamma\lVert\nabla u\rVert_p$，以$d=3$、$p=2$、$\gamma=4$核对。

###### paragraph：第三步：推广到全空间Sobolev函数

1. 由稠密性和Fatou引理推广到$W^{1,p}(\mathbb R^d)$。

###### paragraph：第四步：回到区域

1. 用延拓回到区域，得到定理。

2. 说明常数的来源及其不依赖被估计函数。

3. 例子：$|x|^{-a}$属于$L^q$和$W^{1,p}$的条件，$p^*$不能提高；取$d=3$、$p=2$、$a=0.4$逐项核对属于$W^{1,2}$和$L^6$、不属于$L^8$、在原点无界。

#### 21.6.2 临界指数下的可积性

1. 由$p\to d$时$p^*\to\infty$引出临界情形。

2. 定理：$p=d\geq2$时对每个有限$q$有估计。

3. 证明：降到$s<d$再用次临界结论。

4. 用$\ln\ln(e/|x|)$算出$\int|\nabla u|^d=|S^{d-1}|/(d-1)$有限。

5. 说明边界项趋零，$u\in W^{1,d}(B)$而在原点趋于无穷。

6. 说明不能代入$p^*=\infty$，并由$\lVert f\rVert_q\to\lVert f\rVert_\infty$证明常数$C_q$不可能一致。

#### 21.6.3 连续代表

1. 说明$p>d$的机制：核$|x-z|^{1-d}$的$p'$次幂局部可积。

2. 定理：$d<p<\infty$时有$1-d/p$阶Hölder连续代表及统一估计。

3. 证明：在两球之交上用平均估计和Hölder得振荡估计，取单位球得上确界估计，再由磨光列一致收敛传到一般函数。

4. 命名Hölder连续，说明连续代表唯一、点值是有界线性泛函。

5. 用$|x|^b$说明指数不能整体提高，以$d=2$、$p=4$、$b=0.6$核对。

6. $p=\infty$的凸区域：磨光函数的梯度有界，取极限得Lipschitz代表。

7. 一般有界Lipschitz区域：分支间用上确界，同一分支内用折线的几何事实，后者不证。

###### paragraph：一维的情形

1. $d=1$时$W^{1,1}$已有有界连续代表，$p>1$时有$1-1/p$阶Hölder代表。

2. 解释一维时路径唯一，临界反例不能照搬。

###### paragraph：高阶空间

1. 陈述$W^{k,p}$的指数比较和$k>d/2$时$H^k$的连续代表，证明指向专著。

2. 用周期坐标解释$k>d/2$：点值有界要求$\sum(1+|\xi|^2)^{-k}<\infty$，按球壳计数得$2k>d$，并指向第23章。

###### paragraph：四种情形的对照

1. 引出汇总表。

2. 表：列出$p<d$、$p=d$、$d<p<\infty$、$p=\infty$四种情形的结论和说明不能改进的例子。

### 21.7 紧嵌入

正文：[07-compact-embeddings.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/07-compact-embeddings.tex)

1. 说明连续嵌入只给有界性，无限维闭球不紧，概述本节三步。

#### 21.7.1 Lᵠ中的强收敛子列

###### paragraph：坐标中的椭球

1. 把$H^1(0,1)$的单位球写成余弦坐标下半轴$s_n=(1+\pi^2n^2)^{-1/2}$的椭球，与$L^2$单位球对比。

2. 配图sobolev-ellipsoid：$(a_1,a_2)$平面上的截面对比和半轴条形图，虚线为精度$0.1$。

3. 由半轴趋零得到截断误差的一致界$s_{N+1}^2$。

4. 数值例子：$\varepsilon=0.1$时$s_4\approx0.079$，保留前四个坐标即可，有限维有界集可有限覆盖，得全有界。

5. 说明边界：在$H^1$自身范数下球不紧，图景依赖$p=2$。

###### paragraph：一般区域与一般指数

1. 把直观换成不依赖正交结构的语言：平移差控制对应高频一致小，有限维近似对应保留低频。

2. 引理：有界Lipschitz区域上$W^{1,p}$有界列有$L^p$收敛子列。

3. 证明：延拓、平移差统一控制磨光误差、对固定尺度的磨光函数用分片常数作有限维近似、合并得全有界。

4. 说明导数统一界、区域有界和目标范数较弱各自的职责。

5. 定理：$1<p<d$、$q<p^*$时$W^{1,p}$有界列有$L^q$收敛子列。

6. 证明：$q\leq p$由有限测度，$p<q<p^*$由插值和连续嵌入。

7. 命名紧嵌入，说明是紧算子，以及$p=1$和$p\geq d$的情形。

8. 用$n^{-1}\sin(nx_1)$说明紧嵌入不给Sobolev范数下的收敛，先给出序列的设定。

9. 由Riemann--Lebesgue引理完成矛盾论证。

10. 说明与弱收敛的配合，上例弱收敛、$L^q$强收敛而$W^{1,p}$不收敛。

#### 21.7.2 临界指数处的集中现象

1. 指出$q=p^*$时嵌入连续但不紧，反例来自缩放集中。

2. 定义$f_n=n^{(d-p)/p}\varphi(n(x-x_0))$，换元逐项计算三种范数。

3. 总结范数行为，引向$d=3$、$p=2$的图。

4. 配图sobolev-concentration：径向剖面随$n$的收缩，以及各范数比值的双对数图。

5. 证明几乎处处趋零而临界范数下没有强收敛子列。

6. 说明这是一维加权坐标看不到的现象，有限维类比在“尺度”自由度上失效。

7. 算次临界$q<p^*$时$L^q$范数趋零，并用平移说明无界区域失去紧性。

#### 21.7.3 有界函数类的有限覆盖

1. 把紧嵌入转写为函数类$\mathcal F_R$。

2. 由相对紧与全有界的等价得每个精度的有限覆盖。

3. 说明只得到数量有限，增长阶需要具体构造，指向第13、22章。

4. 用集中序列说明临界连续嵌入不能代替有限覆盖。

5. 用$n^{-1}\sin(nx_1)$说明弱紧性不能代替有限覆盖。

### 21.8 本章小结

正文：[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/12-sobolev-spaces/08-summary.tex)

1. 回答开头的问题：同时控制函数与弱导数，由四类例子说明理由。

2. 用加权坐标重述，并指出它在$p=2$、$k=1$时是定理，在其余情形是帮助理解机制的图景，再总结范数、完备性和Hilbert结构。

3. 总结稠密性、延拓及其条件。

4. 总结闭包、端点值、迹和Poincaré不等式，点出去掉零权坐标的含义。

5. 总结连续嵌入按$p$与$d$的分类及其反例。

6. 总结紧嵌入的椭球图景、一般证明、临界集中和有限覆盖。

7. 指出本章的局限，引向第22章和第23章。

## 第22章 Besov空间

正文入口：[13-besov-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces.tex)，章内依次输入[01-translation-differences.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/01-translation-differences.tex)、[02-besov-norms.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/02-besov-norms.tex)、[03-wavelet-characterization.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/03-wavelet-characterization.tex)、[04-scale-truncation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/04-scale-truncation.tex)、[05-best-n-term.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/05-best-n-term.tex)、[06-covering-numbers.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/06-covering-numbers.tex)、[07-relation-to-sobolev.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/07-relation-to-sobolev.tex)、[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/08-summary.tex)。

章职责与主线：本章在单位周期上从平移差出发，补充一阶Sobolev条件缺少的两类描述：分数阶的变化规律与跨尺度的汇总方式，并沿用第10章把函数看作无限维向量的图景，把Besov范数讲成按尺度分组的坐标加权范数。先建立差分与连续模，定义Besov范数并证明完备；再用周期正交小波基证明差分范数与分组坐标范数等价；随后在坐标中研究固定尺度截断、最佳$N$项逼近与Besov球的覆盖数；最后证明$B^1_{2,2}$与周期$H^1$一致。章首有六个自然段：

1. 第一段指出弱导数这把尺子对周期阶跃没有读数，而它的平移差平方积分恰好等于$2\lvert h\rvert$，整数阶条件读不出这条规律。

2. 第二段指出上界相同的函数可能在不同尺度上表现不同，需要单独规定跨尺度汇总，本章由平移差把这两类信息写成一族函数空间。

3. 第三段给出贯穿全章的图景：坐标取小波系数，按尺度$j$分组，组内$\ell^p$、乘权重、组间$\ell^q$就是Besov范数。

4. 第四段说明$s,p,q$分管权重、组内、组间，并概述前三节如何建立这幅图景。

5. 第五段概述后四节：保留前若干组、自选最大$N$个分量、覆盖整球，三者条件各异；最后回到导数。

6. 第六段划定范围：单位周期、$L^p(\mathbb T)$、实值函数，全空间与一般区域的情形指向专著。

### 22.1 平移差

正文：[01-translation-differences.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/01-translation-differences.tex)

1. 没有可积导数时退一步，比较函数与其平移的差别如何随步长缩小。

2. 固定记号$\Delta_hf$与周期$L^p$范数，指出平移不改变范数。

#### 22.1.1 阶跃函数的平移差

1. 定义单位周期阶跃，指出它在跳跃点处没有弱导数。

2. 设$0<h\leq1/2$逐段比较$f(x)$与$f(x+h)$，写出$\Delta_hf$的分段公式。

3. 由总长$2h$的非零集得到式`eq:besov-step-difference`：$\lVert\Delta_hf\rVert_p=(2\lvert h\rvert)^{1/p}$。

4. 指出图`fig:besov-step-differences`(a)中两条窄带的总宽就是积分值。

配图`fig:besov-step-differences`：(a)阶跃、平移后函数与差异窄带（$h=1/8$）；(b)对数坐标下阶跃与正弦的$L^2$平移差，斜率$1/2$与$1$。

5. 与$\sin(2\pi x)$比较，和差化积得到$\lVert\Delta_hg\rVert_2=\sqrt2\lvert\sin\pi h\rvert$。

6. 对$C^1$周期函数由微积分基本定理与Minkowski不等式得到式`eq:besov-c1-difference`。

7. 用表`tab:besov-step-sine`的三个步长比较：步长变为四分之一时，正弦差约变为四分之一，阶跃差只变为一半。

表`tab:besov-step-sine`：$h=1/8,1/32,1/128$时两种函数的平移差。

8. 归纳：有可积导数与毫无规律之间存在以步长分数次幂表示的规律，这是本章要刻画的光滑性。

#### 22.1.2 位置分布与尺度汇总

1. 指出单一幂次不够，用有限维的$\ell^p$范数比较与求和方式选择作类比，提出位置分布和尺度汇总两件事。

###### paragraph：同一尺度内的位置分布

1. 把$\Delta_hf$在各位置的取值想成长向量，用表`tab:besov-p-position`比较$h=1/128$时阶跃与正弦在$p=1,2,\infty$下的读数。

表`tab:besov-p-position`：阶跃读数随$p$剧烈变化，正弦几乎不变。

2. 阶跃幂次为$1/p$，正弦恒为一次；$p$记录同尺度变化的位置分布，并与$W^{1,p}$中的$p$对照。

###### paragraph：不同尺度之间的汇总

1. 定义单频分量$u_j$，算出$\lVert\Delta_hu_j\rVert_2$，说明第$j$个分量在$h\approx2^{-j}$处起作用。

2. 把分量按权重$b_j$叠加成$f_b$，写出它的Fourier坐标和平移差平方和公式。

3. 将求和分成$2^jh\leq1$的递增几何级数，估计第一段。

4. 估计$2^jh>1$的第二段，两段相加得到统一上界式`eq:besov-fb-upper`。

5. 取$h=2^{-J-1}$得到下界，说明尺度$2^{-J}$处的比值至少与$b_J$同量级。

6. 比较$b_j=1$与$b_j=1/j$，同一上界下前者维持水平、后者下降，上确界看不出区别。

配图`fig:besov-scale-aggregation`：(a)两列权重；(b)$s=1/2$时比值$h^{-1/2}\lVert\Delta_hf_b\rVert_2$随尺度的变化。

7. 用前四项的$\ell^1,\ell^2,\ell^\infty$范数手算两列权重的读数。

8. 项数趋于无穷时$(1/j)$平方可和、常数列不可和，这就是在尺度下标上选$\ell^q$，由第二个指数$q$承担。

#### 22.1.3 有限差分

1. 一阶差分对光滑函数也只给出$h$的一次方，提出迭代差分，并与二阶差商对照。

2. 定义$r$阶差分，写出二项式展开式`eq:besov-finite-difference`。

3. 说明$\Delta_h^r$消去次数小于$r$的多项式，给出$x$与$x^2$的计算。

4. 局部与低阶多项式重合时差分为零，差分只读出超出局部多项式的变化。

5. 对$C^r$周期函数归纳写出$r$重积分表示。

6. 由Minkowski不等式和范数至多加倍得到式`eq:besov-difference-bounds`的两个估计，分别用于小步长和大步长。

例`ex:besov-triangle-wave`：周期三角波，$0<h\leq1/4$时计算$\lVert\Delta_hg\rVert_2^2=h^2(1-4h/3)$；二阶差分在折点前是高$2h$的三角形，$\lVert\Delta_h^2g\rVert_2=2h(4h/3)^{1/2}$；$h=1/16$时数值分别为$0.0598$、$0.0361$，一般$p$下为$1+1/p$阶。

7. 解读图`fig:besov-second-difference`：一阶差分淹没折点，二阶差分只留下两个小三角形。

配图`fig:besov-second-difference`：三角波、一阶差分与二阶差分（$h=1/16$）。

#### 22.1.4 连续模

1. 对不超过给定尺度的步长取最坏情形，引出连续模。

定义`def:besov-modulus`：式`eq:besov-modulus`给出$r$阶连续模。

2. 列出单调性、两条上界与次可加性式`eq:besov-modulus-subadditive`。

3. 写出阶跃函数与正弦函数的连续模。

###### paragraph：差分阶数为何要高于光滑阶数

1. 提出连续模增长不能慢于$t^r$的问题，给出周期$1$的Fourier系数与Parseval等式。

2. 指出平移是Fourier坐标上的对角矩阵，得到式`eq:besov-difference-fourier`。

3. 设$\omega_r(f,t)_2=o(t^r)$，保留第$k$项并令$t\to0$，推出$f$是常数。

4. 总结饱和现象，并以正弦说明$s>r$时连续模不能刻画$s$阶光滑性。

5. 定义要求$r>s$，避开$s=r$的边界，呼应三角波例子。

### 22.2 Besov范数

正文：[02-besov-norms.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/02-besov-norms.tex)

1. 回顾连续模与$p$已给出的信息，提出把尺度离散成坐标，再选权重和求和方式。

#### 22.2.1 差分范数

1. 有限维类比：先乘权重再求$\ell^q$范数，权重大的位置要求分量小。

2. 把下标对应到尺度$t=2^{-j}$，分量取连续模，权重取$2^{js}$，用$\mathrm dt/t$使各二进尺度等权。

定义`def:besov-space`：式`eq:besov-seminorm`、`eq:besov-norm`给出半范数、范数与周期Besov空间。

3. 解释只取$t\leq1$，大尺度由$\lVert f\rVert_p$记录，不同$r>s$等价的结论需要Marchaud不等式，指向专著。

4. 由连续模单调性写出每段上的上下界。

5. 积分换成二进和，得到式`eq:besov-dyadic-form`，半范数与序列的$\ell^q$范数相差有界倍数。

6. 固定$s$改变$q$，得到包含关系式`eq:besov-inclusion-q`，与$\ell^q$范数的单调性同一机制。

7. 降低$s$，用几何因子把有界序列变成可和序列，得到式`eq:besov-inclusion-s`。

#### 22.2.2 参数的作用

1. 说明$s,p,q$的分工，提出用周期阶跃检验。

2. 对任意$r$由差分范数至多加倍得到连续模的上界。

3. 在跳跃点附近只剩一项，得到下界$\omega_r(f,t)_p\geq t^{1/p}$。

4. 由两侧估计知比值与$t^{1/p-s}$同阶，代入定义化为一个幂积分。

5. 分$s<1/p$、$s=1/p$、$s>1/p$讨论，得到成员判别式`eq:besov-step-membership`。

6. 取$p=2$、$r=1$，比值序列为$\sqrt2\,2^{j(s-1/2)}$，列入表`tab:besov-step-ratios`。

表`tab:besov-step-ratios`：$s=1/4,1/2,3/4$时$j=1,\ldots,4$的比值。

7. 读表：$s$改变基准，$q$只在临界情形起决定作用。

8. 说明$f_b$在临界时大致由$(b_j)$是否属于$\ell^q$决定。

9. 读出$p$的作用：阶跃的临界阶数为$1/p$，Besov尺度给了它确切位置。

#### 22.2.3 完备性

1. 由差分线性核对齐次性。

2. 三角不等式分内外两层，与分组向量范数结构相同，$B^s_{p,q}$是线性空间。

3. 零范数只对应零等价类，$L^p$项用于排除常数。

定理`thm:besov-complete`：$B^s_{p,q}$是Banach空间。

4. 预告证明沿用先在$L^p$中取极限再保留附加条件的思路。

证明：取$L^p$极限，用差分的$L^p$连续性得到连续模的下半连续，再由Fatou引理传到半范数，最后由Cauchy条件得到收敛。

5. 与Sobolev空间的完备性比较附加条件的形式。

### 22.3 小波刻画

正文：[03-wavelet-characterization.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/03-wavelet-characterization.tex)

1. 差分范数不便于计算逼近误差，小波基提供坐标，本节把差分范数改写成坐标条件。

###### paragraph：周期小波基与系数

1. 回顾实值紧支撑正交多分辨率分析与周期基函数，省略周期化上标。

2. 固定$j_0$并要求$2^{j_0}\geq L$，写出周期标准正交基。

3. 用积分读取粗项与细节系数，写出Parseval等式。

4. 函数对应分组无限维向量，第$j$组有$2^j$个分量。

###### paragraph：贯穿后文的例子

1. 取$f=\mathbf 1_{[0,1/3)}$与Haar基，解释跳跃点选在非二进点的原因，给出$a_0$与平移差。

2. 支撑不含$1/3$时系数为零，每层只有$k_j=\lfloor2^j/3\rfloor$一个非零系数，并求出相对位置$\theta$。

3. 对$\theta=1/3,2/3$计算括号，得到$c_{j,k_j}=2^{-j/2}/3$。

4. 用Parseval等式核对平方和等于$1/3$。

#### 22.3.1 单尺度系数的大小

1. 换元得到式`eq:besov-psi-lp`，这是$L^2$归一化与$L^p$度量的换算。

2. 同层支撑至多有限重叠，一层的组合是不交拼接，这是组内$\ell^p$的来源。

引理`lem:besov-single-level`：式`eq:besov-single-level`。

证明：上界用有限和Hölder不等式，下界用正交性与Hölder不等式，再按重叠次数求和。

3. 指出上界只用到支撑重叠次数和函数有界，下一小节要用。

###### paragraph：手算：集中与分散

1. Haar时式`eq:besov-single-level`取等号，取$j=3$比较集中与分散两组$\ell^2$范数为$1$的系数。

2. 写出两组系数对应的函数，把组内范数列入表`tab:besov-concentrate-spread`。

表`tab:besov-concentrate-spread`：$p=1,2,\infty$时的因子、系数范数与函数范数。

配图`fig:besov-lp-position`：第$3$层的集中脉冲与分散方波。

3. 由图解释$L^2$、$L^\infty$、$L^1$对集中与分散的不同反应，$\ell^p$把位置汇总搬到坐标上。

4. 乘$2^{js}$对应差分范数的$t^{-s}$，粗项对应$\lVert f\rVert_p$且不能省略。

#### 22.3.2 小波等价范数

1. 把加权块按$\ell^q$汇总，定义式`eq:besov-block`的$b_j$与式`eq:besov-wavelet-norm`的系数范数。

2. 解释图`fig:besov-group-coordinates`，说明与有限维分组范数的两点不同。

配图`fig:besov-group-coordinates`：坐标按尺度分组、组内合成$b_j$、组间取$\ell^q$再加粗项的流程。

3. 手算$p=q=2$、$s=1/4$的$b_j=2^{-j/4}/3$。

4. 求几何和得到系数范数约$0.949$，并核对$s=1/2$时$b_j=1/3$与差分判别一致。

定理`thm:besov-wavelet-characterization`：式`eq:besov-wavelet-equivalence`，要求$m,M>s$。

5. 交代证明的主要步骤和三处外部事实，取$r=\lfloor s\rfloor+1$并固定记号$g_j,B_j,b_j$。

###### paragraph：由系数控制差分：正则性

1. 系数范数有限时级数在$L^p$中绝对收敛，说明其和就是$f$。

2. 单层差分小步长用导数、大步长用$2^r$，得到带$\min(1,(2^j\lvert h\rvert)^r)$的估计。

3. 对$j$求和，分$j<J$与$j\geq J$得到$\omega_r(f,2^{-J})_p$的上界。

4. 乘$2^{Js}$改写成$(b_j)$与几何序列的卷积。

5. 给出卷积不等式式`eq:besov-convolution`。

6. 两侧几何比都小于$1$恰好需要$0<s<r$，结合式`eq:besov-dyadic-form`得到右半部分。

###### paragraph：由差分控制系数：消失矩

1. 由展开公式把系数写成实轴上的积分，消失矩可以使用。

2. 减去局部多项式，用Hölder不等式得到$B_j^p$的上界。

3. $r=1$时取平均值，由Jensen不等式估计。

4. 对$x$积分并换元，得到局部差分的平均。

5. 对$k$求和，用$2m\omega_1(f,\delta)_p^p$控制。

6. 用$\omega_1(f,nt)_p\leq n\omega_1(f,t)_p$得到$B_j\leq C\omega_1(f,2^{-j})_p$，完成$0<s<1$的左半部分。

7. $r\geq2$时需Whitney估计，指向专著，并说明消失矩不足的后果。

###### paragraph：条件不能省略

1. Haar母小波是阶跃型函数，$s\geq1/2$时系数范数有限而差分范数无限或仅在$q=\infty$有限，两者不等价。

2. Haar在$p=2$、$0<s<1/2$时适用，正则性方向的增益只有$(2^j\lvert h\rvert)^{1/2}$，这是手算例子的依据。

3. 后三节固定满足定理条件的小波，把两种范数相差的倍数记入$C_0$。

### 22.4 按尺度截断的误差

正文：[04-scale-truncation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/04-scale-truncation.tex)

1. 向量图景中最直接的近似是保留前若干组，固定$p=2$，概述本节三步。

2. $p=2$时写出系数范数$\mathcal N(f)$与等价式`eq:besov-wavelet-norm-l2`。

#### 22.4.1 尺度截断

1. 定义$V_J$与投影$P_J$，在坐标上是把后面的组置零，维数$M_J=2^J$。

2. 由Parseval等式得到式`eq:besov-truncation-error`，$P_Jf$是$V_J$中的最佳元素。

3. 对贯穿例子得到$E_J=\frac{\sqrt2}{3}2^{-J/2}$，$J=3$时$E_3=1/6$。

4. 区分尺度$J$与预算$M_J$，强调$V_J$预先选定，属于固定子空间逼近。

#### 22.4.2 统一截断误差

1. 球条件给出每组统一上界，尾部几何和给出误差上界。

定理`thm:besov-uniform-truncation`：式`eq:besov-uniform-truncation`。

证明：$\ell^q$范数不小于各项，代入误差公式求几何和。

2. 用单层函数说明对$V_J$量级不能改进。

3. 结论与$q$无关，因为证明只用每组的统一上界。

#### 22.4.3 截断误差的尺度汇总

1. 提出误差能否反过来读出Besov条件，需要把各尺度的误差汇总。

定理`thm:besov-truncation-characterization`：式`eq:besov-truncation-characterization`。

证明：$b_J\leq e_J$，尾和与卷积不等式给出反向，再处理粗项。

2. $q$在逼近语言中规定放大后的误差序列的汇总方式。

例`ex:besov-one-coefficient-per-scale`：每组一个大小$2^{-js}$的分量，属于$B^s_{2,\infty}$但不属于有限$q$；$s=1/2$时$2^{J/2}E_J\equiv\sqrt2$。

3. 有限$q$要求误差比统一速率衰减更快，与$b_j=1,1/j$的对比是同一件事。

### 22.5 最佳N项逼近的误差

正文：[05-best-n-term.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/05-best-n-term.tex)

1. 固定截断浪费预算，改为跨组挑选至多$N$个分量，最优选择是最大的$N$个。

2. 写出重排与误差式`eq:besov-n-term-error`。

3. 取$0<s<1/2$，定义式`eq:besov-tau`的$\tau$，函数取自$L^2$。

#### 22.5.1 跨尺度选择

1. 单系数函数的极端比较：固定截断遗漏全部能量，一项即可精确。

2. 贯穿例子中$\sigma_N=\frac23 2^{-N/2}$。

3. $\sigma_8=1/24$是$E_3$的四分之一，图`fig:besov-haar-tiles`比较两种选择。

配图`fig:besov-haar-tiles`：固定截断与最佳$8$项在尺度--位置方格上的选择。

4. 用表`tab:besov-fixed-vs-best`和图`fig:besov-error-decay`比较：一个按项数的$-1/2$次幂下降，一个指数下降。

表`tab:besov-fixed-vs-best`：项数$1,2,4,8,16$时的两种误差。

配图`fig:besov-error-decay`：两种误差与定理上界的双对数图。

5. 更光滑的紧支撑小波仍然每层有界个非零系数，$\sigma_N$指数衰减。

6. 固定截断的误差不能比$M^{-1/2}$快一个幂次。

7. 两种方式的差别和代价：下标信息与非线性。

#### 22.5.2 最佳N项误差的上界

1. $1/\tau=s+1/2$时权重抵消，分组不再起作用。

2. 比较$A^\tau+B^\tau$的关系，得到式`eq:besov-ltau-coeff`，$B^s_{\tau,\tau}$等价于全部系数$\tau$次可和。

3. $\tau<2$的可和性比平方可和强，用集中与分散的表说明。

定理`thm:besov-n-term-upper`：式`eq:besov-n-term-upper`。

证明：重排界$c_n^*\leq n^{-1/\tau}\lVert c\rVert_{\ell^\tau}$，拆分$(c_n^*)^2$后代入。

4. 用贯穿例子核对：$\lVert c\rVert_{\ell^{4/3}}\approx0.890$，$N=8$时上界$0.529$，实际$0.0417$。

5. 解读图`fig:besov-parameter-map`：竖线$B^s_{2,q}$与绿线$B^s_{\tau,\tau}$有相同速率。

配图`fig:besov-parameter-map`：$(1/p,s)$平面上的$p=2$竖线、$\tau$线与阶跃临界线。

6. 绿线整条在阶跃临界线以下，解释阶跃函数适合自适应逼近。

#### 22.5.3 速率条件的逆向刻画

1. 提出逆向问题，答案是速率只对应更弱的条件。

定理`thm:besov-n-term-rate`：式`eq:besov-n-term-rate`。

证明：用第$N+1$到$2N$项的尾和与积分比较两个方向。

2. 定义弱$\ell^\tau$条件，用$c_n^*=n^{-1/\tau}$构造平方可和函数并得到速率。

3. 该序列不$\tau$次可和，单一速率不能反推成员资格。

#### 22.5.4 跨预算的误差汇总

1. 类比截断情形，把各二进预算的误差按$\ell^\tau$汇总。

定义`def:besov-approximation-space`：式`eq:besov-approximation-space`。

2. 二进预算的上确界等价于统一速率，$\ell^\tau$和是加强。

定理`thm:besov-approximation-equals-besov`：$A^s_\tau=B^s_{\tau,\tau}$。

证明：二进块估计、卷积不等式控制一个方向；逐块重排与$\tau s=1-\tau/2$控制另一方向。

3. 定理依赖的固定条件与失效方向。

### 22.6 Besov球的覆盖数

正文：[06-covering-numbers.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/06-covering-numbers.tex)

1. 提出为整类函数准备有限代表的问题，紧嵌入只给出有限性。

2. 分组坐标把问题变成数格点：一串有限维球，尾部舍去，逐组铺网。

#### 22.6.1 函数类、距离与精度

1. 定义$\mathcal F_R$。

2. 规定覆盖数与球心约定。

3. 引入度量熵，说明全有界性的定性论证。

#### 22.6.2 逐尺度精度分配

1. 列出尾部和每组系数的上界，构造分两部分。

###### paragraph：尾部

1. 取最小的$J$，由最小性得到式`eq:besov-cover-scale`。

###### paragraph：保留的系数

1. 粗项并入起始块，分配式`eq:besov-cover-precision`的精度。

2. 解释精度随$j$增大的理由，并核对平方和小于$\varepsilon^2/4$。

###### paragraph：合并

1. 各块中心组合成$V_J$中的函数，由正交性合并误差，得到$\varepsilon$覆盖。

#### 22.6.3 对数覆盖数的上界

1. 回用有限维球的覆盖界，第$j$块的贡献是维数乘对数比值。

定理`thm:besov-entropy-upper`：式`eq:besov-entropy-upper`。

证明：估计$2\rho_j/\delta_j$，取对数后按块求和，用几何和得到$6C_12^J$。

2. 说明估计对象是对数覆盖数以及常数和适用范围。

3. 给出教学数据$s=1,R=1,C_0=1,j_0=0,J=6$。

4. 算出$C_s$、$\varepsilon\approx0.0361$，逐块结果见表`tab:besov-cover-budget`。

表`tab:besov-cover-budget`：各块的维数、半径、精度、比值与贡献，总和约$174$。

5. 解读图`fig:besov-cover-budget`：主要计数来自接近截断尺度的几组。

配图`fig:besov-cover-budget`：半径与精度的对数图、各块的贡献条形图。

#### 22.6.4 覆盖数的下界

1. 用单尺度子类核对上界，它是真正的欧氏球。

定理`thm:besov-entropy-lower`：式`eq:besov-entropy-lower`。

证明：单组子类、投影球心、体积比较，再选择尺度。

2. 上下界同阶，增长阶由$s$决定而与$q$无关。

3. 结论依赖的固定设定及其他情形的差别。

### 22.7 与Sobolev空间的联系

正文：[07-relation-to-sobolev.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/07-relation-to-sobolev.tex)

1. 提出二者在重合处是否一致，只对照一阶平方可积弱导数。

2. 向量图景：差分与求导都是Fourier坐标上的对角矩阵，权重同阶则空间相同。

###### paragraph：定理与证明

1. 定义$H^1_{\mathrm{per}}$。

定理`thm:besov-b122-h1`：式`eq:besov-b122-h1`。

2. 预告分两步的证明。

证明：第一步用分部积分与Parseval等式刻画$H^1_{\mathrm{per}}$；第二步取$r=2$，用换元得到半范数平方与$\sum k^2\lvert\widehat f(k)\rvert^2$等价，$c_1\approx106.9$，$C_1=16\pi^2$。

###### paragraph：端点条件的作用

1. $f(x)=x$不满足端点条件，算出$k^2\lvert\widehat f(k)\rvert^2=1/(4\pi^2)$。

2. 这些数不可和，$f\notin B^1_{2,2}$，边界项正是接缝处的跳跃。

###### paragraph：二阶差分的必要性

1. 一阶连续模有正比于$t$的下界。

2. 积分发散，一阶差分写出的空间只含常数；Haar不能用于$s=1$。

###### paragraph：其他参数

1. $0<s<1$时$B^s_{2,2}$由加权Fourier条件刻画，正整数$s$时与$H^s$一致。

2. $p\neq2$时$W^{1,p}$夹在两个Besov空间之间，指向Littlewood--Paley理论。

3. 总结Besov空间在Sobolev空间之外增加的描述。

### 22.8 本章小结

正文：[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/13-besov-spaces/08-summary.tex)

1. 回应开头两处空白：平移差读出分数幂，$p$与跨尺度汇总分别规定。

2. 总结高阶差分、连续模与饱和现象。

3. 概括Besov范数即分组加权范数，阶跃分开$s$与$q$，小波等价的条件。

表`tab:besov-parameters-summary`：三个参数的差分写法、坐标写法与含义。

4. 三种任务由不同条件控制，见表。

表`tab:besov-tasks-summary`：固定截断、最佳$N$项、覆盖的函数类、结果与反方向。

5. 说明向量类比的边界：范数等价在无限组下失效，等价依赖小波性质。

6. 回顾与$H^1$的一致性和$p\neq2$的差别，并连接第23章。

## 第23章 再生核Hilbert空间

正文入口：[14-reproducing-kernel-hilbert-spaces.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces.tex)，章内依次输入[01-recovery-from-observations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/01-recovery-from-observations.tex)、[02-reproducing-relation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/02-reproducing-relation.tex)、[03-spaces-from-kernels.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/03-spaces-from-kernels.tex)、[04-kernel-constructions.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/04-kernel-constructions.tex)、[05-minimum-norm-interpolation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/05-minimum-norm-interpolation.tex)、[06-finite-subspace-approximation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/06-finite-subspace-approximation.tex)、[07-mercer-spectral-representation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/07-mercer-spectral-representation.tex)、[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/08-summary.tex)。

章职责与主线：本章沿用第10章“函数是下标取遍定义域的向量”的图景，把读取点值看成取坐标，追问这一操作何时能写成内积。点评估连续的Hilbert函数空间称为RKHS，读坐标用的向量是核截面，核是下标取遍$X\times X$的半正定“矩阵”。随后反向由正定核构造唯一的RKHS，给出特征映射、非负组合与逐点乘积三条造核规则；用观测映射、Gram矩阵与观测零空间的正交分解处理插值的相容性与最小范数解；比较核截面与一般有限特征的表示误差；最后加入全支撑测度，经积分算子与Mercer定理得到谱坐标及两种范数下的截断误差。全章以三点网格上的矩阵$\bm K=[\min(x_i,x_j)]$、仿射核与最小值核为贯穿例子，并逐处说明类比失效的位置。带损失与正则项的拟合归卷五，随机观测的统计误差归卷八。

1. 章首第一段由有限读数恢复整条函数的问题进入，指出候选空间须让“在一点取值”既有确定意义又随函数连续变化。

2. 第二段回到函数即向量的图景，把读取$f(x)$看成取第$x$个坐标，提出它能否写成内积、所用向量是什么的问题。

3. 第三段给出回答：核是下标取遍$X\times X$的矩阵，第$x$列是读坐标的向量；并说明这一类比怎样贯穿造空间、观测与Mercer展开，且每处都交代失效位置。

4. 第四段交代所用前置（Hilbert空间与投影、Riesz表示、紧自伴谱定理、完备化），并划定噪声拟合归卷五、随机观测归卷八。

### 23.1 从离散观测恢复函数

正文：[01-recovery-from-observations.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/01-recovery-from-observations.tex)

1. 以测点$0,\tfrac12,1$与读数$(0,1,0)$为例，指出抛物线$q$与正弦$s$都通过这三点。

2. 用在测点上为零的$c(x)$构造一族$q+\beta c$，在$x=\tfrac14$处比较各函数的值，说明测点之间的取值可以任意调节。

3. 用向量图景解释：三个读数只是不可数个坐标中的三个，有限点值不能确定函数，必须约束未读到的坐标。

4. 提出精确插值与带残差拟合两个问题，分别说明它们问的是什么。

5. 提出域外误差问题，划定本章处理精确插值与只依赖空间结构的域外误差，拟合归卷五，随机测点指向卷八。

#### 23.1.1 有限特征空间

1. 提出预先固定有限个特征、在其线性组合中寻找候选函数的做法，寻找函数由此变成寻找系数。

2. 定义设计矩阵，把精确插值写成方程$\bm A\bm\theta=\bm y$（式`eq:rkhs-design-equation`）。

3. 回用卷二第11章的判据：相容看列空间，唯一看列满秩，不相容时取最小二乘解，再选最短解。

4. 例`ex:rkhs-polynomial-features`在同一组数据上取三组特征：一次时无解，法方程给出常数$\tfrac13$及残差；二次时Vandermonde矩阵可逆，解出$q$；三次时零空间一维，得到插值族$q+\beta c$。

5. 总结三种情形：维数改变的是候选函数本身，存在与唯一由候选空间与测点共同决定。

6. 指出零残差不保证测点外零误差：真实函数为$\sin\pi x$时，$q$在$\tfrac14$处差约$0.043$，须加读数之外的约束。

#### 23.1.2 点值观测的稳定性

1. 提出在无限维Hilbert空间中选范数最小可行函数的思路，须先检查读数与范数是否相容。

2. 以$\mathbb R^n$中坐标不超过长度为参照，写出稳定性要求（式`eq:rkhs-stability-requirement`），说明它不成立时选范数最小者控制不了读数。

###### paragraph：$L^2$空间中点值的两个缺陷

1. 说明$L^2$元素是函数类，点值没有确定意义。

2. 用尖峰$f_k$算出$\lVert f_k\rVert_{L^2}^2=1/(3k)$而$f_k(0)=1$，比值$\sqrt{3k}$无界，点值不受$L^2$范数控制。

3. 用$N$点采样的平均范数解释来由：单个坐标只受$\sqrt N$倍的界控制，常数随坐标数爆炸，与尖峰的$\sqrt{3k}$是同一回事。

###### paragraph：Sobolev空间中的点值

1. 回用第21章：$H^1(0,1)$的元素有唯一绝对连续代表，第一个缺陷消失。

2. 由绝对连续性写出$f(x)=f(y)+\int_y^xf'$，再对$y$积分，得到点值的积分表示。

3. 估计第二项，用Cauchy--Schwarz把$L^1$换成$L^2$，得到$\lvert f(x)\rvert\leq\sqrt2\lVert f\rVert_{H^1}$（式`eq:rkhs-h1-point-bound`）。

4. 算出尖峰的$\lVert f_k'\rVert_{L^2}^2=k$，说明造高而窄的尖峰须付出范数代价，它不再是反例。

###### paragraph：候选空间与真实函数

1. 归纳候选空间的两项要求，比较$L^2$与$H^1(0,1)$。

2. 指出要求只针对候选函数：真实函数有跳跃时不属于$H^1$，空间是否贴合须结合问题判断。

### 23.2 再生关系

正文：[02-reproducing-relation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/02-reproducing-relation.tex)

1. 承接上一节的两项要求，把它们作为定义。

2. 固定数域$\mathbb K$与复内积对第一变量共轭线性的约定，说明保留复数是为了Mercer一节用复谱定理。

3. 定义`def:rkhs-rkhs`：逐点运算的Hilbert函数空间，每个点评估泛函有界即为RKHS。

4. 解释逐点运算的作用：相等即逐点相等，$L^2$不在讨论范围内。

5. 说明有界性等价于稳定性要求，且定义只要求逐点常数，统一常数留待由核的对角值读出。

#### 23.2.1 点评估界

1. 说明判断RKHS的关键是估计$\lvert f(x)\rvert/\lVert f\rVert_H$，先有限维后无限维。

###### paragraph：仿射函数空间

1. 定义$H_{\mathrm{aff}}$及系数内积，说明它与$\mathbb K^2$等距同构。

2. 由Cauchy--Schwarz得$\lvert f(x)\rvert\leq\sqrt{1+x^2}\lVert f\rVert$，常数在实轴上无界，限制到$[-1,1]$时为$\sqrt2$。

3. 推广到多项式与一切有限维函数空间，指出真正需要论证的是无限维情形。

###### paragraph：左端固定的一阶Sobolev函数

1. 定义$H_{\min}$及导数内积，核对$f(0)=0$使它成为真正的内积。

2. 由$f\mapsto f'$到$L^2(0,1)$的等距满射得到完备性。

3. 把$f(x)$写成导数累计，得$\lvert f(x)\rvert\leq\sqrt x\lVert f\rVert$（式`eq:rkhs-hmin-point-bound`），并解释常数在左端为零。

4. 归纳机制：范数控制导数平方积分，点值是导数的路径累计，Cauchy--Schwarz连接二者。

#### 23.2.2 核截面

1. 说明下一步把读数写成内积，先算清有限维情形。

###### paragraph：有限维的样板：读坐标的向量

1. 在$\mathbb R^n$上取内积矩阵$\bm A$，指出用$\bm e_i$作内积读出的是$(\bm A\bm v)_i$。

2. 解$\bm A\bm w=\bm e_i$得读坐标向量是$\bm K=\bm A^{-1}$的第$i$列（式`eq:rkhs-finite-reproducing`），$\bm K$自身是这些向量的Gram矩阵。

3. 取$x=\tfrac13,\tfrac23,1$上的$\bm K=[\min(x_i,x_j)]$与$\bm v=(\tfrac89,\tfrac89,0)^{\top}$，写出$\bm A$并逐步验证第二列读出$v_2=\tfrac89$。

4. 展开得$\bm v^{\top}\bm A\bm v=\tfrac1h\sum_i(v_i-v_{i-1})^2$（式`eq:rkhs-finite-difference-form`），它是$\int f'^2$的差分形式，预告与$H_{\min}$的联系。

###### paragraph：再生关系与再生核

1. 对点评估用Riesz表示，得到$K_x$与再生性质（式`eq:rkhs-reproducing`）。

2. 指出这是有限维式的无限维版本，定义再生核与核截面（式`eq:rkhs-kernel-definition`）。

3. 解释“再生”一词，引出对应表与图。

4. 表`tab:rkhs-dictionary`列出下标、坐标、读坐标向量、矩阵元素、列、半正定在有限维与RKHS中的对应。

5. 图`fig:rkhs-kernel-as-matrix`展示最小值核从三点矩阵到二元函数的过渡，一行读出来就是核截面$K_{2/3}$。

6. 类比失效一：无限维中通常只有$K$还是函数，$\bm A$的元素以$1/h$增长，极限是求导运算而非二元函数。

7. 类比失效二：有限长度是实在的限制，标准单位向量的对应物尖峰通常不在$H$中，这解释了$L^2$的失败。

###### paragraph：两个例子中的核截面

1. 在$H_{\mathrm{aff}}$中比较系数，得仿射核$K(t,x)=1+tx$。

2. 配合图说明读数是内积、函数在某点为零即与该点核截面垂直。

3. 图`fig:rkhs-reproducing-geometry`在系数平面画出$f=1+t$、$K_{1/2}$、$K_{-1}$及投影，并对照函数图像上的读数$1.5$与零点。

4. 把$f(x)$写成$\mathbf 1_{[0,x]}$与$f'$的积分，找到$K_x(t)=\min(t,x)$。

5. 直接核对再生性质，定义最小值核，并说明差分式的连续版本就是$\int f'^2$。

###### paragraph：再生核的基本性质

1. 说明内积性质转化为核的性质，引出定理。

2. 定理`thm:rkhs-kernel-properties`：共轭对称、正定性（式`eq:rkhs-kernel-positivity`）、点评估范数（式`eq:rkhs-kernel-norm`）、核截面稠密，证明逐条给出。

3. 定义Gram矩阵与核矩阵，指出无限矩阵的每个有限子矩阵都半正定，前两条只涉及核，留作下一节的定义。

4. 说明单位球在$x$处的取值恰好填满半径$\sqrt{K(x,x)}$的圆盘。

5. 回答统一常数问题：存在当且仅当$\sup_xK(x,x)<\infty$，并以仿射核、最小值核核对。

### 23.3 从正定核构造空间

正文：[03-spaces-from-kernels.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/03-spaces-from-kernels.tex)

1. 提出由二元函数出发问对应空间的反向问题。

2. 指出有限维答案是取逆，无限维逆通常不存在，构造必须只用$\bm K$，并陈述本节结论。

3. 预告三步构造：半内积、零长度方向、完备化。

#### 23.3.1 正定核

1. 把定理的前两条单独提出来，看成要求每个有限子矩阵半正定。

2. 定义`def:rkhs-pd-kernel`：正定核（式`eq:rkhs-pd-condition`）与严格正定核。

3. 用矩阵语言复述，说明复情形对称性自动成立、实情形须单独要求。

4. 说明“正定核”只要求半正定，严格正定决定观测能否对任意数据求解，并解释为何强调互异点。

###### paragraph：半正定但不严格正定的例子

1. 仿射核在$-1,0,1$上的Gram矩阵以$(1,-2,1)^{\top}$为零向量，对应函数组合为零，原因是空间只有二维。

###### paragraph：严格正定的例子

1. 写出高斯核，把它表示为$\mathrm e^{\mathrm i\omega u}$对正权重$p_\sigma$的积分。

2. 把二次型写成$\int\lvert g\rvert^2p_\sigma$，得到非负。

3. 积分为零推出$g\equiv0$，在$\omega=0$处逐阶求导得Vandermonde齐次方程组，系数全零，完成严格正定的证明。

4. 在两点$0,1$、$\sigma=1$上核对特征值$1\pm\mathrm e^{-1/2}$。

5. 结合图比较两种核，提醒单一点组不能代替对一切点组的论证。

6. 图`fig:rkhs-gram-matrices`给出五点上的高斯核与仿射核Gram矩阵及特征值，前者全正，后者只有两个正特征值。

#### 23.3.2 核截面的有限线性组合

1. 说明若空间存在，必含核截面且截面内积只能是$K(x,y)$，构造由此出发。

###### paragraph：有限维的样板：只用$\bm K$写内积

1. 把$\bm K\bm c$、$\bm K\bm d$代入内积，逆矩阵消掉，得到只含$\bm K$的公式$\bm c^{\top}\bm K\bm d$，奇异时同样有意义，零向量对应零长度系数方向。

###### paragraph：半内积

1. 定义$H_0$及半内积（式`eq:rkhs-h0-inner`），列出线性、共轭对称与非负。

2. 以$K_{-1}+K_1$与$2K_0$为例提出表示无关性问题。

3. 给出只依赖函数值的两种写法，得出良定义。

4. 取$f=K_x$得再生性质在$H_0$上成立（式`eq:rkhs-h0-reproducing`）。

###### paragraph：零范数方向的商

1. 把系数当对象，指出它只是半内积，$(1,-2,1)$非零而长度为零。

2. 回用零距离商，由半内积的Cauchy--Schwarz得$N$是子空间，半内积下降为内积。

3. 把系数映为函数，由$e_t$得点值估计（式`eq:rkhs-h0-point-bound`）。

4. 证明零范数系数恰好给出零函数，商空间与$H_0$一一对应。

#### 23.3.3 空间的完备化

1. 用最小值核上$m$个核截面的平均$f_m$说明$H_0$不完备，写出其导数。

2. 算出$\lVert f_m-f\rVert^2=1/(3m^2)$，极限$t-t^2/2$不是折线，引出下面的补全。

###### paragraph：完备化与点值的极限

1. 回用完备化，指出其元素还不是函数。

2. 由点值估计得Cauchy列逐点收敛，定义$J$，$J$在$H_0$上是恒等。

###### paragraph：极限元素仍可识别为函数

1. 提出不同元素给出同一函数的危险。

2. 由$H_0$稠密推出$J$单射。

3. 定理`thm:rkhs-moore-aronszajn`：正定核确定唯一RKHS，$H_0$稠密，元素是Cauchy列的逐点极限；证明分存在性与唯一性写出。

4. 命名Moore--Aronszajn定理，正定核与RKHS互相确定，引出构造示意图。

5. 图`fig:rkhs-construction-steps`以最小值核画出系数、折线、折线序列及极限、函数$t-t^2/2$四个阶段。

###### paragraph：由最小值核重建$H_{\min}$

1. 把截面内积写成导数积分，由阶梯函数稠密得到完备化后就是$H_{\min}$。

2. 说明唯一性在此的作用。

3. 指出构造不用测度或拓扑，核范数稠密不回答逼近外部函数的问题。

### 23.4 正定核的构造

正文：[04-kernel-constructions.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/04-kernel-constructions.tex)

1. 以矩阵证明半正定的三种办法（分解、相加、逐元素相乘）引出本节三条造核规则。

#### 23.4.1 特征映射构造

1. 由$\bm G=\bm\Phi\bm\Phi^{\top}$的行内积引出特征映射。

2. 定义`def:rkhs-feature-map`（式`eq:rkhs-feature-kernel`）。

3. 把二次型写成长度平方，核得正定，并写出Gram矩阵的分解形式。

4. 由规范特征映射得到“正定”与“有特征映射”等价。

###### paragraph：线性核与有限特征核

1. 给出线性核与$(1+xy)^2$的三维特征，说明有限特征核的Gram矩阵秩受特征维数限制。

###### paragraph：特征维数与RKHS

1. 以矩阵分解不唯一作类比，仿射核的二维与三维特征给出同一RKHS，特征维数不是空间的性质。

2. 由参数$w$定义$f_w$，说明$V^\perp$分量对函数无影响。

3. 定理`thm:rkhs-feature-space`：$H_K=\{f_w\}$且范数等于最短参数长度（式`eq:rkhs-feature-norm`），并给出证明。

4. 说明冗余表示中参数长度只是范数的上界。

5. 例`ex:rkhs-redundant-features`：$\Phi(x)=(x,x)$时三个参数给出同一函数，由投影得范数$\sqrt2$，再直接核对。

6. 用图说明读数只看沿$V$的分量。

7. 图`fig:rkhs-visible-parameters`在参数平面画出$V$、等值虚线与三个参数。

8. 比较仿射核两个特征映射下的最短与非最短参数。

#### 23.4.2 非负线性组合

1. 说明组合已知核可免去重新找特征，最简单的是加权求和。

2. 定理`thm:rkhs-nonnegative-combination`及逐项二次型的证明。

3. 用拼接特征解释，仿射核是常数核与线性核之和。

4. 以$xy-1$的对角负值与$\mathrm iK$说明系数不能任意改变符号或取复数。

#### 23.4.3 逐点乘积

1. 指出乘积核的Gram矩阵是逐元素乘积，正定性来自卷二第4章的Schur乘积定理。

2. 定理`thm:rkhs-pointwise-product`：用秩一分解证明正定，用张量积内积给出特征映射。

3. 用$(1,x)\otimes(1,x)$说明四维与三维特征给出同一个核。

###### paragraph：两条辅助规则

1. 函数缩放规则及其模平方证明。

2. 逐点极限规则。

###### paragraph：多项式核与高斯核

1. 由组合与乘积得多项式核正定。

2. 高斯核验证第一步：展开平方，分出缩放因子。

3. 第二、三步：指数级数部分和正定，取极限后乘缩放因子；并区分正定与严格正定。

###### paragraph：运算在核截面上的效果

1. 说明和核、乘积核的截面分别是截面之和、之积，比较$x=0.4$处的形状。

2. 图`fig:rkhs-kernel-operations`画出仿射与高斯截面及其和、积。

3. 预告核本身的谱给出另一种特征。

### 23.5 最小范数插值

正文：[05-minimum-norm-interpolation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/05-minimum-norm-interpolation.tex)

1. 回到精确插值，把候选空间取为RKHS并固定记号。

2. 分可行性与选解两步，预告同一正交分解的作用。

#### 23.5.1 观测映射

1. 定义观测映射（式`eq:rkhs-observation-map`），估计其有界性。

###### paragraph：伴随与Gram矩阵

1. 由内积换算得$S^*\bm c=\sum_ic_iK_{x_i}$。

2. 得$SS^*=\bm G$及内积公式（式`eq:rkhs-gram-calculus`）。

3. 指出$\bm G$是无限矩阵的子矩阵，并区分$\bm c^*\bm G\bm c$与$\lVert\bm c\rVert_2$。

###### paragraph：秩与线性相关

1. 由$\ker\bm G=\ker S^*$得秩等于核截面张成维数。

2. 列出奇异的三种来源：重复观测、空间维数不够、退化观测点。

3. 例`ex:rkhs-hmin-observation`：三点上$\bm G$可逆，组合是折线，写出三段斜率。

#### 23.5.2 观测零空间

1. 定义观测零空间（式`eq:rkhs-observation-null-space`）与$M$，指出两者闭。

2. 定理`thm:rkhs-observation-null-space`：互为正交补，投影保读数且不增范数，并给出证明。

3. 解释读数恰好确定$Pf$，并指出有限维中的相同关系。

4. 例`ex:rkhs-hmin-null-space`：$N$含$\sin(3k\pi x)$，由逐段积分验证正交，$Pf$是折线插值。

5. 说明这是卷五表示定理的结构依据。

#### 23.5.3 约束相容性

1. 提出可行性判定，举重复观测冲突的例子。

2. 定理`thm:rkhs-consistency`：可行当且仅当$\bm y$在$\bm G$的像中，并给出证明。

3. 分$\bm G$可逆与奇异讨论。

4. 列举三种奇异情形的相容条件。

5. 区分没有插值函数与插值函数不止一个，引出表。

6. 表`tab:rkhs-gram-vs-null`对比仿射核与$H_{\min}$，说明$\bm G$可逆与唯一性是两回事。

#### 23.5.4 最小范数解

1. 指出可行函数组成$f_0+N$，自然的选择是范数最小者。

###### paragraph：有限维的样板

1. 在三维样板中求第二坐标为$1$的最短向量，得$(\tfrac12,1,1)^{\top}$，长度平方$\tfrac32$。

2. 定理`thm:rkhs-min-norm-interpolation`：解的公式（式`eq:rkhs-min-norm-solution`）、勾股关系（式`eq:rkhs-min-norm-pythagoras`）与范数（式`eq:rkhs-min-norm-value`），并给出证明。

3. 命名最小范数插值，它是可行函数在$M$上的投影，求解只需核在观测点上的值。

###### paragraph：系数不唯一与函数唯一

1. 区分系数不唯一与函数唯一，伪逆只是选写法。

2. 仿射核算例：系数$(s,-2s,1+s)$对任意$s$给出同一函数$1+t$，范数平方恒为$2$。

3. 例`ex:rkhs-hmin-interpolation`：$q$的读数给出折线，解出$\bm c$并代回检验，算得$\lVert f^+\rVert^2=\tfrac{128}{27}$，余项范数平方$\tfrac{16}{27}$。

4. 结合图解释余项为何正交：$(f^+)'$是$q'$的逐段平均。

5. 图`fig:rkhs-min-norm-interpolation`画出$q$、$f^+$、余项及其导数。

6. 指出插值的域外误差取决于看不见的分量，引到下一节。

### 23.6 有限维子空间逼近

正文：[06-finite-subspace-approximation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/06-finite-subspace-approximation.tex)

1. 把问题从读数转为已知目标在有限子空间中的表示误差。

2. 回用投影，指出RKHS的额外结构是范数误差控制逐点误差。

3. 定理`thm:rkhs-subspace-error`：子空间的再生核与逐点误差界（式`eq:rkhs-subspace-pointwise`），并给出证明。

4. 解释两个因子各自的来源，预告两类子空间。

#### 23.6.1 核截面张成空间的逼近

1. 取$V=M_Z$，投影即最小范数插值，定义幂函数。

2. 写出幂函数公式（式`eq:rkhs-power-function`），指出它是Schur补的对角元。

###### paragraph：点集决定的稠密性

1. 提出位置受限时的稠密性问题。

2. 定理`thm:rkhs-dense-sections`及证明。

3. 连续核情形：$H$中函数连续，任意稠密点集足够。

4. 离散核反例：无限大单位矩阵对应$\ell^2([0,1])$，稠密点集不够，说明连续性的作用。

5. 例`ex:rkhs-hmin-grid`：均匀节点上误差平方$16h^2/3$，幂函数平方$ab/h$，最大值$h/4$。

###### paragraph：RKHS范数误差与其他范数下的误差

1. $\kappa<\infty$时$H$范数逼近蕴含一致逼近，反例$\sin(k\pi x)/k$说明反向不成立。

2. 讨论逼近$H$之外函数的问题，以仿射核、$H_{\min}$为例。

3. 陈述高斯核的通用性质（未证，说明所需工具），解释其含义。

4. 归纳核与点集的分工。

#### 23.6.2 有限特征表示

1. 引入显式特征，坐标预算为$m$。

###### paragraph：投影的计算

1. 由正交条件得$\bm B\bm a=\bm b$及误差（式`eq:rkhs-feature-projection-error`）。

2. 代入$K_y$得子空间的核（式`eq:rkhs-feature-subspace-kernel`）。

3. 比较一般特征与核截面的坐标来源。

4. 例`ex:rkhs-hmin-polynomial-features`：$(x,x^2)$的$\bm B$，两个坐标精确表示$q$，三个核截面误差约$0.77$。

###### paragraph：有限特征核不是原核

1. 欧氏内积给出的$\widetilde K$范数与原空间不同。

2. 求出$\bm B^{-1}$与正确的$K_V$，在$\tfrac12$处得误差系数$\tfrac14$。

3. 总结有限特征近似不等于原核的精确表示。

### 23.7 Mercer谱表示

正文：[07-mercer-spectral-representation.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/07-mercer-spectral-representation.tex)

1. 以矩阵特征分解为参照，指出不可数下标上没有现成求和。

2. 说明用测度把求和换成积分，得到积分算子与谱展开。

3. 列出标准条件：紧度量空间、连续正定核、全支撑有限Borel测度。

#### 23.7.1 核积分算子

1. 定义$T_K$（式`eq:rkhs-integral-operator`），预告核验紧、自伴、正。

###### paragraph：紧性、自伴性与像的连续性

1. 由核有界得紧性，交换积分次序得自伴。

2. 由一致连续得$T_Kg$是连续函数。

###### paragraph：积分算子的正性

1. 说明正性需要把积分切成Gram矩阵二次型的逼近论证。

2. 引理`lem:rkhs-positive-operator`（式`eq:rkhs-operator-positivity`）：先对连续$f$用有限划分逼近，再由稠密性推广，证明写细。

###### paragraph：再生关系与积分算子的区别

1. 区分核的两种角色，把测度解释为下标的权重。

2. 用仿射核算出$T_K1=1$、$T_Kx=x/3$，测度加倍则算子加倍。

#### 23.7.2 核的谱展开

1. 回用谱定理给出特征值、特征函数与算子展开。

###### paragraph：特征函数的连续代表

1. 由$\phi=\lambda^{-1}T_K\phi$取连续代表，全支撑保证唯一。

2. 以支撑不全的测度说明条件的作用。

###### paragraph：Mercer定理

1. 对比一般谱定理的$L^2$展开，引出Mercer定理。

2. 定理`thm:rkhs-mercer`（式`eq:rkhs-mercer`、`eq:rkhs-mercer-trace`）及三步证明：对角线部分和有界，固定$x$识别极限，由Dini论证得一致收敛。

3. 把迹公式解释为矩阵迹的连续版本，说明零特征方向不出现。

4. 指出类比的边界：矩阵分解无前提，逐点展开依赖紧、连续、全支撑。

###### paragraph：两个核的谱

1. 仿射核的两个特征值及迹检验。

2. 最小值核：分段写出$T_K\phi$，逐次求导。

3. 化为边值问题，解出谱（式`eq:rkhs-min-kernel-spectrum`）。

4. 零空间平凡，迹之和为$\tfrac12$。

5. 比较三种核的特征值衰减。

6. 图`fig:rkhs-mercer-spectrum`画出前三个特征函数与三种核的特征值。

#### 23.7.3 RKHS中的谱坐标

1. 由有限维的$\bm v^{\top}\bm A\bm v=\sum_ja_j^2/\lambda_j$预告同样的公式。

2. 由Mercer展开写出$\ell^2$特征映射。

3. 定理`thm:rkhs-spectral-norm`：$\{\sqrt{\lambda_j}\phi_j\}$是标准正交基，两种范数的系数公式（式`eq:rkhs-two-norms`），并给出证明。

###### paragraph：两种范数的坐标权重

1. 比较两种范数的权重与单位方向。

2. 把$H_K$单位球解释为半轴$\sqrt{\lambda_j}$的椭球。

3. 对最小值核算$f=\phi_1$与$g=\phi_1+0.1\phi_8$的两种距离。

4. 图`fig:rkhs-norm-weights`画出两条曲线与两种权重。

###### paragraph：只使用非零特征方向

1. 列出成员的两项要求。

2. 以$x^2$（仿射核）与常数$1$（最小值核）分别说明两种失败。

###### paragraph：谱坐标依赖测度，RKHS范数不依赖

1. 仿射核换测度后谱坐标与$L^2$范数改变，RKHS范数不变。

#### 23.7.4 Mercer谱特征的截断

1. 定义$V_N$与$f_N$，它同时是两种内积下的投影。

###### paragraph：两种尾和

1. 写出两种尾和（式`eq:rkhs-tail-sums`），有限秩时精确表示。

###### paragraph：单位球上的$L^2$误差

1. 得统一界$\lambda_{N+1}$（式`eq:rkhs-tail-comparison`），由$\sqrt{\lambda_{N+1}}\phi_{N+1}$说明不能改进，对应椭球半轴。

2. 同一函数说明RKHS范数下没有统一界，与无限维闭球不紧是同一现象。

###### paragraph：逐点误差与核的截断

1. 写出$K_N$与余项$R_N$，得逐点误差界与核的一致逼近。

2. 例`ex:rkhs-hmin-truncation`：$q$的谱坐标、三项截断的两种误差$0.068$与$1.07$，与折线插值比较，两种三维子空间各有所长。

3. 指出由样本构造Gram矩阵谱分解得到的不是这里的$K_N$。

### 23.8 本章小结

正文：[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/03-function-spaces/14-reproducing-kernel-hilbert-spaces/08-summary.tex)

1. 回顾候选空间的两项要求。

2. 回顾点值即取坐标、再生关系与核作为半正定矩阵。

3. 回顾由核造空间与造核规则及其矩阵对应。

4. 回顾有限观测的正交分解与最小范数插值。

5. 回顾有限表示的误差比较。

6. 回顾Mercer展开、谱坐标、椭球图景与截断误差。
