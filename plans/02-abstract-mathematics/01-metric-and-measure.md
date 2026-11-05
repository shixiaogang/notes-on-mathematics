# 卷2《数学准备：抽象数学》：度量与测度大纲

正文入口：[part.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/part.tex)。以下按实际正文顺序保留内容提要；目标细化方案另见[数学基础五卷目标目录](../mathematical-foundations/02-spaces-and-analysis/06-metric-and-measure.md)。本部分已按目标大纲的四章结构实施到正文。

阅读指引从绝对值的误差语言进入，说明第1章用距离规则建立邻近、收敛、完备与紧致，研究连续映射、空间比较与压缩迭代；第2章规定可测集合与测度，构造Lebesgue测度，研究可测映射传递质量以及测度的比较与分解；第3章由简单函数定义积分，比较求和与经典积分，按条件组织极限交换、累次积分、换元与含参积分，并讨论积分恢复增量；第4章在测度与积分已建立后研究密度的存在、计算与换测度。指引最后说明条件期望、概率收敛与分布距离留给后续的概率空间与概率分布部分。

## 第1章 度量空间

正文入口：[01-metric-spaces.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces.tex)。

本章研究带距离的集合及其间的映射，回答如何判断邻近、收敛与极限存在，以及怎样通过迭代构造极限。前置知识为集合与映射、可数性、实数极限与有限维范数；不依赖一般拓扑、函数空间与测度。

1. 从迭代$x^{(t+1)}=x^{(t)}/2+1$与有理数逼近$\sqrt2$两个例子进入，指出“相邻项越来越近”与“极限存在”是两件事，后者取决于空间本身。
2. 指出二进制串、图顶点等对象不能相减却仍需比较远近，提出学习目标：从距离的共同规则出发建立不依赖坐标的邻近、收敛与连续语言，并弄清每个结论的条件。
3. 按依赖关系解释路线：先定义距离及其构造，再由开球得到邻近结构，由点列收敛、完备与紧致研究极限的存在，由连续映射与空间比较研究误差在空间之间的传递，最后在压缩映射定理中汇合。

### 1.1 度量与度量空间

正文：[01-metrics.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces/01-metrics.tex)

1. 列举绝对值、范数、二进制串的逐位比较和图的最短路，指出它们遵守共同规则；预告本节由此定义度量，再研究限制、组合与识别对象时怎样得到新度量。

#### 1.1.1 度量的定义

1. 从$|x-y|$与欧氏距离的共同性质进入，给出度量与度量空间的定义（`def:metric-space`），陪域$[0,\infty)$包含非负性与有限性。
2. 逐条说明非负性、分离性、对称性与三角不等式分别排除什么；强调三角不等式使难估计的距离可以拆段估计。

###### paragraph：反向三角不等式

1. 由三角不等式交换角色推出$|d(x,z)-d(y,z)|\leq d(x,y)$（`eq:metric-reverse-triangle`），解释为移动比较点时到固定点的距离至多改变移动量；配图`fig:metric-triangle`。

###### paragraph：集合与度量一起给出

1. 以$\mathbb R$上通常距离与离散距离下$1/n$与$0$的距离对比，说明度量空间是集合与度量的对，邻近、收敛、连续都须先说明所用度量。

#### 1.1.2 常见度量

1. 指出度量既可以来自范数，也可以来自计数与路径长度，不要求对象能相减。

###### paragraph：由范数诱导的度量

1. 跨卷引用卷一赋范空间章，逐条由范数公理验证$d(\bm x,\bm y)=\lVert\bm x-\bm y\rVert$是度量，写出$d_1,d_2,d_\infty$并说明偏差累计方式的差异。
2. 例`ex:metric-three-distances`：$\bm p=(0,0)$、$\bm q=(4,0)$、$\bm r=(3,3)$，三种度量下$\bm q$距离均为$4$，$\bm r$的距离为$6$、$3\sqrt2$、$3$，“更近”的结论随度量改变；配图`fig:metric-three-distances`。

###### paragraph：不需要减法的度量

1. 定义离散度量并分情形验证三角不等式，说明它只区分相同与不同，常用于反例。
2. 定义等长二进制串的Hamming距离，算例$d_H(10110,11100)=2$，逐位论证三角不等式。
3. 定义无权无向连通图的最短路距离（跨卷引用卷一图上的组合优化章），由路径反向与拼接验证公理；指出不连通时跨分量为$+\infty$，须限制到一个连通分量。

#### 1.1.3 子空间度量

1. 由只研究部分对象的需要进入，定义子空间度量（`def:metric-subspace`），说明公理直接继承、距离数值不变、变化的是可取点的范围。

###### paragraph：区间与圆周

1. 对$[0,1]$与单位圆周$S^1$检查限制后的距离：圆周上的子空间距离是弦长$2\sin(\theta/2)$，弧长$\theta$是重新规定的度量（对径点弦长$2$、弧长$\pi$），由此区分限制定义域与重新规定距离。

#### 1.1.4 有限乘积度量

1. 定义有限乘积上的$\rho_1$与$\rho_\infty$（`def:metric-product`），用逐坐标三角不等式验证。
2. 引入正权重$w_i$，说明零权重使分离性失败、得到伪度量。

###### paragraph：两种乘积度量的比较

1. 证明$\rho_\infty\leq\rho_1\leq m\rho_\infty$（`eq:metric-product-bounds`）及$d_i\leq\rho_\infty$，作为逐坐标收敛、连续与完备判断的依据；指出常数$m$随坐标数增长，不能推广到无限乘积。

#### 1.1.5 伪度量与商度量

1. 以只比较横坐标的$p(\bm x,\bm y)=|x_1-y_1|$进入，区分“原对象相同”与“当前规则无法区分”，定义伪度量（`def:metric-pseudometric`）。

###### paragraph：零距离等价类

1. 定义$x\sim y\Leftrightarrow p(x,y)=0$，用三角不等式证明传递性，得到商集$X/{\sim}$；跨卷引用卷一集合、关系与映射章。

###### paragraph：商度量

1. 用三角不等式证明$\bar p([x],[y])=p(x,y)$与代表元无关，再说明其余公理继承、分离性恢复，得到商度量。
2. 例`ex:metric-quotient-projection`：横坐标伪度量的等价类是竖直线，商空间即带通常距离的实轴；预告几乎处处相等函数的识别是同一构造。配图`fig:metric-pseudometric-quotient`。

### 1.2 开闭集与邻近关系

正文：[02-open-closed-sets.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces/02-open-closed-sets.tex)

1. 说明本节把两点间数值组织为关于集合的判断：开球、开闭集、内部闭包边界、稠密与可分，全节固定$(X,d)$。

#### 1.2.1 开球与邻域

1. 由实轴区间推广，定义开球与邻域（`def:metric-open-ball`）；以$[0,1]$是$1/2$而非$0$的邻域说明邻域要求留有一个球的余量。

###### paragraph：球的形状由度量决定

1. 比较$d_1,d_2,d_\infty$下的单位球（菱形、圆盘、正方形），由范数不等式说明嵌套顺序，并指出离散度量下小球只含中心；配图`fig:metric-unit-balls`。

###### paragraph：球内每点都有更小的球

1. 取$\rho=r-d(y,a)$，由三角不等式证明$B(y,\rho)\subseteq B(a,r)$（`eq:metric-ball-inside-ball`），为开球是开集作准备。

###### paragraph：相对开球

1. 证明$B_A(a,r)=A\cap B_X(a,r)$（`eq:metric-relative-ball`），以$A=[0,1]$中$B_A(0,r)=[0,r)$说明邻域相对当前空间判断；配图`fig:metric-relative-ball`。

#### 1.2.2 开集与闭集

1. 从每点能否保留一个小球出发，定义开集与闭集（`def:metric-open-closed`），说明半径可随点变化，开球、空集与全空间均开。
2. 定理`thm:metric-open-operations`：任意并与有限交保持开，任意交与有限并保持闭；证明中有限性保证最小半径为正。
3. 用$\bigcap(-1/n,1/n)=\{0\}$与$\bigcup[1/n,1]=(0,1]$说明“有限”不能换成“任意”。

###### paragraph：开与闭不是互斥的两类

1. 以全空间、空集既开又闭和$[0,1)$既不开也不闭说明开闭并非二分。

###### paragraph：子空间中的开集与闭集

1. 引理`lem:metric-relative-open`：子空间开集即环境开集与$A$的交，闭集同理；用开球之并构造环境开集，闭集由补集得到。
2. 以$A=[0,1]$中的$[0,1/2)$、$(1/2,1]$与$[0,1/2]$为例，说明开闭性依赖所在空间。

#### 1.2.3 内部、闭包与边界

1. 用“存在一球留在集合内”“每球都碰到集合”“每球同时碰到两侧”定义内部、闭包、边界（`def:metric-closure`），强调量词区别与$A^\circ\subseteq A\subseteq\overline A$；配图`fig:metric-interior-closure-boundary`。

###### paragraph：边界等于闭包去掉内部

1. 由“非内点即每球碰到补集”推出$\partial A=\overline A\setminus A^\circ$（`eq:metric-boundary`），计算$(0,1)$、$[0,1]$与$\mathbb Q$的内部、闭包与边界。

###### paragraph：闭包是闭集

1. 用小球论证闭包的补集开，得到$A$闭当且仅当$A=\overline A$，并给出内部的对称结论。

###### paragraph：点到集合的距离

1. 定义$d(x,A)=\inf_{a\in A}d(x,a)$并记下下确界的逼近性质。
2. 引理`lem:metric-distance-closure`：$x\in\overline A$当且仅当$d(x,A)=0$。
3. 用$d(0,(0,1))=0$与$d(2,(0,1))=1$说明距离为零不保证属于集合、下确界不保证达到，最近点问题留到1.5.4。

#### 1.2.4 稠密集与可分空间

1. 以有理数逼近实数进入，定义稠密集与可分空间（`def:metric-separable`），将$\overline D=X$与每个球都遇到$D$联系，强调可分要求一套可数代表服务所有位置与精度；跨卷引用卷一基数章。

###### paragraph：实轴与离散空间

1. 证明$\mathbb Q$在$\mathbb R$、$\mathbb Q^d$在$(\mathbb R^d,d_2)$中稠密；不可数离散空间中单点集是开球，稠密集只能是全空间，不可分。说明可分不等于可数，且依赖度量。
2. 承上启下，指出邻近结构由度量和所在空间共同决定，引出点列。

### 1.3 点列收敛与完备性

正文：[03-convergence-completeness.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces/03-convergence-completeness.tex)

1. 区分“已有候选极限时检查收敛”与“不知道极限时判断存在”两类问题，预告收敛、闭集判据、柯西列与完备化。

#### 1.3.1 点列的收敛

1. 定义$x_n\to x$（`def:metric-convergence`），用开球解释，跨卷引用卷一极限与连续章；强调极限必须属于当前空间。

###### paragraph：极限的基本性质

1. 由三角不等式证明极限唯一、收敛列有界、子列保持原极限，分别说明控制的量。

###### paragraph：有限乘积中的收敛

1. 回用`eq:metric-product-bounds`证明整体收敛与逐坐标收敛等价，并推出$\mathbb R^d$上三种度量的收敛都等价于逐坐标收敛。

###### paragraph：极限可能不在当前空间中

1. 用$(0,1)$中的$1/(n+1)$说明点列在环境实轴中收敛、在子空间中没有极限。

#### 1.3.2 闭包与闭集的序列判据

1. 引理`lem:metric-sequential-closure`：在每个$B(x,1/n)$中取点构造逼近列，反向由收敛定义得到闭包点。
2. 推出闭集的序列判据，以$(0,1]$中$1/n\to0$为反例。
3. 指出判据只保留已经存在的极限，以$\mathbb Q$在自身中闭为例引出完备性。

#### 1.3.3 柯西列与完备性

1. 以逐次逼近为动机，定义柯西列与完备空间（`def:metric-complete`），证明收敛列是柯西列。
2. 例`ex:metric-rational-cauchy`：$\sqrt2$的十进制截断在$\mathbb Q$中是柯西列（$0\leq q_m-q_n<10^{-n}$）却无极限，$\mathbb Q$不完备；配图`fig:metric-rational-cauchy`。

###### paragraph：实数与欧氏空间的完备性

1. 回接实数的柯西收敛准则，再逐坐标推出$\mathbb R^d$在$d_1,d_2,d_\infty$下完备。

###### paragraph：完备子集与闭子集

1. 定理`thm:metric-complete-closed`：完备空间的闭子集完备；任意度量空间中的完备子集闭。前者用环境极限与闭集判据，后者用极限唯一。
2. 以$[0,1]$完备、$(0,1)$不完备、$\mathbb Q$闭于自身却不完备说明各条件的作用。

###### paragraph：有限乘积的完备性

1. 由逐坐标柯西判据证明有限个完备空间之积完备，$\mathbb R^d$为其特例。

#### 1.3.4 度量空间的完备化

1. 以$\mathbb Q$与$\mathbb R$为动机，提出用柯西列补入缺失极限，并指出构造要用到1.1.5的商度量。

###### paragraph：用柯西列代表新点

1. 用两次反向三角不等式证明$d(x_n,y_n)$是实数柯西列，借实数完备性定义伪度量$D$，以$(1/n)$与$(-1/n)$说明$D$可为零，商化得到$(\widehat X,\hat d)$。

###### paragraph：原空间的等距嵌入

1. 常值列给出保距嵌入$\iota$，并证明$\iota(X)$稠密。
2. 定理`thm:metric-completion`：逐步选取原空间近似点$x_k$，证明$(x_k)$为柯西列并代表$\xi_k$的极限，得到$\widehat X$完备。
3. 说明$\widehat{\mathbb Q}$与$\mathbb R$之间有保距双射、完备空间的完备化不增加新点；完备化唯一性需映射延拓，不展开。

### 1.4 紧致性

正文：[04-compactness.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces/04-compactness.tex)

1. 以闭区间上收敛子列与最值的存在进入，说明紧致性的核心是任意精度下的有限控制。

#### 1.4.1 有界集与全有界集

1. 定义有界集与直径（`def:metric-bounded`），证明两种刻画等价。
2. 以无限离散空间说明有界不控制细尺度，定义全有界与有限$\varepsilon$网（`def:metric-totally-bounded`），说明代表点可以随精度改变；配图`fig:metric-epsilon-net`。

###### paragraph：全有界推出有界与可分

1. 由有限$1$网推出有界，由一列$1/n$网的可数并推出可分。

###### paragraph：三个要求的区别

1. 以无限离散空间（有界不全有界）与$\mathbb R$（可分不全有界）区分总体范围、可数代表与每个尺度的有限代表。

#### 1.4.2 开覆盖与紧致集

1. 以“给定一族开集”与“自选球”的区别进入，定义开覆盖与紧致（`def:metric-compact`），用引理`lem:metric-relative-open`说明子集情形可用环境开集表述，强调有限子覆盖只能从给定覆盖中选。

###### paragraph：紧致集全有界且闭

1. 代入同半径球覆盖证明紧致推出全有界；用紧集与外点之间的有限球覆盖证明紧集在环境空间中闭。
2. 例`ex:metric-open-interval-cover`：$(0,1)$全有界，但覆盖$U_n=(1/n,1)$无有限子覆盖；配图`fig:metric-open-cover-interval`。
3. 无限离散空间闭且有界却不紧致，说明一般度量空间中闭有界不够。

#### 1.4.3 紧致性的序列刻画

1. 定义序列紧致（`def:metric-sequentially-compact`）。
2. 定理`thm:metric-compact-sequential`正向：反证得到每个邻域含无穷多项的点，再按半径$1/k$选取下标递增的子列。
3. 反向：先由两两相距$\varepsilon$的点列排除非全有界，再反证得到Lebesgue数$\delta$，最后用有限$\delta$网选出有限成员。
4. 解释Lebesgue数的含义，说明证明处处用到距离，等价性限于度量空间。

#### 1.4.4 完备与全有界判据

1. 定理`thm:metric-compact-complete-tb`：紧致推出完备（柯西列有收敛子列则整体收敛）；完备且全有界时逐级用更细有限球覆盖抽取柯西子列，再用序列刻画得紧致。
2. 用判据重看$(0,1)$、无限离散空间与$[0,1]$。

###### paragraph：欧氏空间中的闭有界集

1. 定理`thm:metric-heine-borel`：$\mathbb R^d$中紧致当且仅当闭且有界；用边长$h<\varepsilon/\sqrt d$的网格给出有限网，用闭子集完备性得到完备。
2. 指出有限维体现在网格计数$s^d$上，闭区间的性质是特例，一般度量空间须回到“完备且全有界”。

### 1.5 连续映射

正文：[05-continuous-maps.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces/05-continuous-maps.tex)

1. 固定$f:D\subseteq X\to Y$，预告连续性、一致连续与Lipschitz的误差控制强度，以及紧致定义域带来的结论。

#### 1.5.1 极限与连续性

1. 定义聚点，给出函数极限（`def:metric-function-limit`），说明极限不看基点处取值，由聚点条件证明唯一，非聚点处不谈极限。
2. 定义连续性（`def:metric-continuous`），说明聚点处连续等价于极限等于函数值，孤立点处由$x=a$本身自动连续。

###### paragraph：序列判据

1. 定理`thm:metric-sequential-continuity`：连续当且仅当保持收敛到该点的点列极限，反向取$\delta=1/n$构造反例点列。

###### paragraph：开集原像判据与复合

1. 定理`thm:metric-open-preimage`：连续当且仅当开集原像开，复合保持连续。
2. 比较三种刻画的用途，指出原像判据是第二章可测映射的参照。

#### 1.5.2 一致连续

1. 以$x^2$在$a=1,3$处$\varepsilon=1$时$\delta(a)=\sqrt{a^2+1}-|a|$的变化引出统一容差，定义一致连续（`def:metric-uniform-continuity`），比较量词次序；配图`fig:metric-uniform-continuity`(a)。
2. 例`ex:metric-square-uniform`：$x^2$在$\mathbb R$上取$n$与$n+1/n$说明不一致连续，在$[-M,M]$上由$|x+y|\leq2M$一致连续。

###### paragraph：一致连续映射保持柯西列

1. 证明一致连续把柯西列映为柯西列；以$1/x$说明逐点连续不够，以$(0,1)$上的恒等映射说明输出未必在陪域中有极限。

#### 1.5.3 Lipschitz映射

1. 由“输出误差不超过输入误差的固定倍数”进入，定义全局与局部Lipschitz（`def:metric-lipschitz`），证明前者推出一致连续、后者推出连续；证明$d(\cdot,z)$与$d(\cdot,A)$是$1$-Lipschitz的。

###### paragraph：三种条件的区分

1. 用$\sqrt x$在$[0,1]$上（$|\sqrt x-\sqrt y|\leq\sqrt{|x-y|}$，割线斜率$1/\sqrt t$无界）区分一致连续与Lipschitz，用$x^2$在$\mathbb R$上区分局部Lipschitz与一致连续；配图`fig:metric-uniform-continuity`(b)。总结蕴含关系，强调针对固定定义域与度量。

#### 1.5.4 紧致集上的连续映射

1. 说明本小节结合1.4与1.5回答最值、最近点与一致连续问题，不以同胚为前提。
2. 定理`thm:metric-compact-image`：拉回开覆盖证明连续像紧致，由闭有界与上确界逼近得到最值存在。

###### paragraph：最近点的存在

1. 由$a\mapsto d(x,a)$的连续性在非空紧集上取得最小值，回应1.2.3：$(0,1)$中下确界不达到，$[0,1]$中最近点存在；以原点与单位圆周说明不唯一。

###### paragraph：连续升级为一致连续

1. 回顾$x^2$在$\mathbb R$上缺统一容差的原因，定理`thm:metric-compact-uniform`：反证构造距离趋零而输出分离的点对，抽取共同极限得到矛盾。
2. 指出结论只给统一容差，不给Lipschitz常数（$\sqrt x$），并回解释例`ex:metric-square-uniform`。

### 1.6 度量空间的比较

正文：[06-comparison.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces/06-comparison.tex)

1. 说明本节用映射比较空间，区分控制距离数值的等距、双Lipschitz映射与只要求双向连续的同胚，并把同一底集上的两个度量纳入比较。

#### 1.6.1 等距与双Lipschitz映射

1. 以平移旋转和完备化嵌入进入，定义双Lipschitz与等距映射（`def:metric-bilipschitz`，`eq:metric-bilipschitz`），说明上界控制正向误差，下界推出单射且逆映射在实际像上为$1/c$-Lipschitz。
2. 例`ex:metric-identity-bilipschitz`：由Cauchy--Schwarz不等式得$\lVert\bm x\rVert_2\leq\lVert\bm x\rVert_1\leq\sqrt d\lVert\bm x\rVert_2$，$\bm x=(1,1)$说明常数$\sqrt2$不能改小。

###### paragraph：双Lipschitz映射保留的性质

1. 证明柯西列、收敛、完备性与全有界性（$\varepsilon$网对应$C\varepsilon$网与$\varepsilon/c$网）在$D$与实际像$f(D)$之间对应，非满射时不涉及陪域其余部分；配图`fig:metric-bilipschitz-homeo`(a)。

#### 1.6.2 同胚与度量的比较

1. 以只关心收敛与开集的问题进入，定义同胚（`def:metric-homeomorphism`），由原像判据和序列判据说明它保留开集与收敛；双Lipschitz双射必为同胚。

###### paragraph：同一底集上的两种度量

1. 定义拓扑等价与强等价，指出$d_1,d_2$及$\rho_1,\rho_\infty$强等价，通常距离与离散度量不拓扑等价；只讨论度量诱导的拓扑。
2. 例`ex:metric-logit`：logit映射是$(0,1)$与$\mathbb R$之间的同胚，$(0,1)$不完备而$\mathbb R$完备；柯西列$1/(n+1)$的像$-\ln n$满足$|h(x_{2n})-h(x_n)|=\ln2$，不是柯西列；配图`fig:metric-bilipschitz-homeo`(b)。
3. 用$d'(s,t)=|\sigma(s)-\sigma(t)|$说明与通常距离拓扑等价的度量可以不完备，强调完备性、全有界与压缩条件须指明度量。

### 1.7 压缩映射与不动点

正文：[07-contraction.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces/07-contraction.tex)

1. 回到章首迭代，说明本节综合距离控制、柯西列、完备性与连续性构造方程的解，并讨论停止条件与执行误差；约定迭代上标$x^{(t)}$。

#### 1.7.1 压缩映射定理

1. 定义不动点与压缩映射（`def:metric-contraction`），说明自映射与统一常数$q<1$的作用。
2. 定理`thm:metric-contraction`：相邻差几何衰减，几何尾和（`eq:metric-contraction-tail`）给出柯西列，完备性给出极限，连续性验证不动点，压缩不等式给出唯一性。
3. 以$T(x)=x/2+1$计算不动点$2$与误差$2^{1-t}$；配图`fig:metric-contraction`(a)蛛网图。

###### paragraph：各条件的职责

1. 用$(0,1)$上的$x/2$（缺极限）、平移$x+1$（常数为$1$）与调和部分和（相邻差趋零而发散）逐项说明非空、自映射、完备与统一严格压缩的职责。

#### 1.7.2 迭代误差与停止条件

1. 说明需要在不知道$x^\star$时判断精度。

###### paragraph：先验与后验误差界

1. 在尾和中令$s\to\infty$得到先验界（`eq:metric-a-priori`），以第$t-1$步为初值得到后验界（`eq:metric-a-posteriori`），区分所用的初始差与当前相邻差。
2. 例`ex:metric-contraction-stop`：$T(x)=x/2+1$下误差$10^{-3}$需$t=11$（$x^{(11)}=1.9990234375$）；$t=5$时后验界与实际误差均为$0.0625$。

###### paragraph：收缩缓慢时的停止判断

1. 以$T(x)=0.99x+1$说明$q/(1-q)$的放大：$t=459$时相邻差约$0.00992$，而$x^{(460)}$误差约$0.982$；先验界要求约$1146$步。区分收敛保证与实际步数。

#### 1.7.3 带误差的压缩迭代

1. 设$d(x^{(t+1)},T(x^{(t)}))\leq\eta_t$且近似点留在$X$中。

###### paragraph：误差递推

1. 推出$e_{t+1}\leq qe_t+\eta_t$与展开式（`eq:metric-inexact-error`），识别初始误差衰减与各步误差传播。
2. 定理`thm:metric-inexact-contraction`：统一误差上界时$\limsup e_t\leq\eta/(1-q)$；$\eta_t\to0$时把和式分段证明$e_t\to0$。
3. 例`ex:metric-inexact-example`：每步加$0.1$时迭代收敛到$2.2$，偏差恰为界$0.2$；配图`fig:metric-contraction`(b)。

###### paragraph：带误差时的停止判断

1. 由$d(x,x^\star)\leq d(x,T(x))/(1-q)$推出$e_t\leq(d(x^{(t+1)},x^{(t)})+\eta_t)/(1-q)$，说明相邻差的停止判断须连同执行误差；具体线性求解与最优化算法留给相应部分。

### 1.8 本章小结

正文：[08-summary.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/01-metric-spaces/08-summary.tex)

1. 回到实数、向量、串与图的比较，梳理距离依次提供的邻近结构、点列收敛与映射连续三层语言。
2. 区分有界、可分、全有界、完备与紧致各自控制的对象，汇总紧致的三种等价刻画与$\mathbb R^d$中的闭有界判据，以及紧致定义域、双Lipschitz映射与同胚分别保留的性质。
3. 以压缩迭代重新串联“误差缩小—柯西列—极限存在—方程验证—唯一性”，说明局部数值现象不足以保证全局结论。
4. 预告下一章：开集生成Borel集合族，但距离不决定集合的测度。

## 第2章 测度

章入口为 `tex/02-abstract-mathematics/01-metric-and-measure/02-measures.tex`，依次输入 `02-measures/01-size-and-additivity` 至 `09-summary` 九个节文件。本章研究怎样测量集合、怎样经映射传递质量、怎样比较与分解测度，只用集合运算、可数性与级数，不依赖积分。

1. 章首从计数、长度、重量共同的“不交相加”规则进入，指出有理点集、Cantor集一类复杂集合无法靠有限个区间可靠测量，提出把相加规则推广到可数分割的学习目标，并列出三个问题：测量集合、传递质量、比较与分解测度。
2. 第二段说明前五节的路线：2.1由计数、长度与Jordan测量提出可数运算的要求；2.2把可测范围与赋值分开，建立$\sigma$代数、Borel集、测度与零测集；2.3用外测度构造Lebesgue测度与Lebesgue--Stieltjes测度，并给出延拓的存在唯一性；2.4用原像定义可测映射与可测函数；2.5研究推前测度。
3. 第三段说明后四节在同一可测空间上比较测度：2.6用零测集刻画绝对连续与相互奇异，2.7建立有符号测度的Hahn分解、Jordan分解与总变差，2.8给出Lebesgue分解及实轴上的三元分解，2.9小结；并交代积分在第3章建立、密度表示在第4章讨论。

### 2.1 集合大小与可加性

本节从计数与长度提取不交相加规则，用有限区间逼近定义Jordan测量，以有理点集说明有限覆盖的局限，提出对可数运算封闭与可数可加的要求。

#### 2.1.1 计数与长度

###### paragraph：计数与加权计数

1. 用有限集合的元素个数与非负权重之和说明不交集合合并时大小相加；权重全为一即计数。
2. 以五点权重$0.5,1,2,0.5,1$、分组$A=\{1,2,3\}$与$B=\{4,5\}$复算个数$3+2=5$与权重$3.5+1.5=5$，引用 `fig:measure-count-length`(a) 说明两种大小遵守同一规则。

###### paragraph：区间长度

1. 定义区间长度$b-a$（与端点归属无关），引卷一基数章说明非退化区间等势而长度不同，长度度量占据范围而非元素多少，计数只是一种测度。

###### paragraph：有限个不交区间的长度

1. 定义有限个不交区间之并的长度为各段长度和，用共同细分与增量逐项相消证明结果与分割方式无关。
2. 以$E=[0,2)\cup[3,4)$的两种分割复算总长度均为$3$，引用 `fig:measure-count-length`(b) 展示共同细分切点。

###### paragraph：有限的含义

1. 区分“有限个区间”与“区间中有限个点”；把$[0,1]$看成不可数个单点之并时有限可加性不适用，预告测度只允许可数分割。

#### 2.1.2 Jordan测量

1. 定义初等集合（有限个有界区间之并），由有限可加推出长度的单调性与有限次可加性，作为后续比较的依据。
2. 给出Jordan内、外测量与Jordan可测的定义（`def:measure-jordan`），说明$J_*\le J^*$，并与卷一一元积分中用有限分割的上和、下和夹逼作类比。

###### paragraph：Jordan可测集的例子

1. 区间与有限个区间之并Jordan可测；再用$\{1/n\}$说明有限个区间可覆盖无限个聚集点，其Jordan测量为零。

###### paragraph：有理点集的反例

1. 证明$\mathbb Q\cap[0,1]$的内测量为$0$；任一外部初等集合取闭包后因稠密性覆盖$[0,1]$，长度不小于$1$，故外测量为$1$，不Jordan可测。
2. 枚举有理点并用长度$\varepsilon2^{-k}$的区间覆盖，总长为$\varepsilon$，引用 `fig:measure-jordan-rationals` 对比有限覆盖与可数覆盖，引出可数覆盖下有理点集应为零。

###### paragraph：对可数运算的要求

1. 指出单点Jordan可测而其可数并不可测，Jordan可测族对可数并不封闭；提出可测族对补、可数并、可数交封闭及可数可加两项要求，把构造留给2.3。

### 2.2 测度空间

本节把“哪些集合可测”与“怎样赋值”分开：建立$\sigma$代数及生成、迹与子$\sigma$代数，用开集生成Borel集并给出实轴生成族，定义测度与有限性条件，证明基本性质，最后讨论零测集与完备化。

#### 2.2.1 $\sigma$代数

###### paragraph：能够区分哪些集合

1. 以四点集合上的幂集与两组分组对比区分能力，提出对补集和可数并封闭的要求。
2. 定义$\sigma$代数、可测空间与可测集合（`def:measure-sigma-algebra`），由De Morgan律推出空集、有限并、可数交与差的封闭性，并核对开头两个集合族。

###### paragraph：生成的$\sigma$代数

1. 定义$\sigma(\mathcal C)$为所有包含$\mathcal C$的$\sigma$代数之交，逐条核对其为最小$\sigma$代数。
2. 例 `ex:measure-partition-sigma`：$\{\{1\},\{2\}\}$生成由三组之并构成的$8$个集合，一般$k$组得$2^k$个，引用 `fig:measure-partition-sigma`。
3. 证明$\mathbb R$上单点生成的$\sigma$代数含于“可数或补集可数”族，因而不含$[0,1]$，说明生成族中必须直接放入区间或开集。

###### paragraph：迹$\sigma$代数与子$\sigma$代数

1. 定义迹$\sigma$代数（缩小底集）与子$\sigma$代数（底集不变、可测集变少），并验证迹族为$\sigma$代数。
2. 用四点集合对比二者：迹丢掉点但保留区分能力，子$\sigma$代数保留点而降低分辨率，为后文“部分信息”预留对象。

#### 2.2.2 Borel $\sigma$代数

###### paragraph：由开集生成

1. 回指第1章开集，定义$\mathcal B(X)$（`def:measure-borel`），举$\mathbb Q$与$[0,1)$为例说明闭集及可数运算所得集合为Borel集，强调Borel结构不规定任何大小。

###### paragraph：实轴上的生成族

1. 引理 `lem:measure-open-rational-intervals`：开集是有理端点开区间的可数并，由有理数稠密与$\mathbb Q\times\mathbb Q$可数证明。
2. 定理 `thm:measure-borel-generators`：开区间、两类半直线、左开右闭区间都生成$\mathcal B(\mathbb R)$，有理端点半直线已足够；用可数并、差与补集逐一互相表示证明。

###### paragraph：开集的不交区间分解

1. 用“两点间闭区间含于$U$”的等价关系把开集分成两两不交的开区间分量，每个分量选一个有理数得到至多可数性。
2. 以$U=(0,1)\cup(1,2)\cup(2.5,4)$为例，引用 `fig:measure-open-set-components` 对比重叠表示与不交分量，为由区间控制开集作准备。

###### paragraph：离散空间

1. 有限或可数且单点闭的空间中每个子集是可数个闭单点之并，Borel结构为幂集，为第3章“离散积分即求和”作准备。

#### 2.2.3 测度的定义

1. 说明取值允许$+\infty$及其运算约定，定义测度、测度空间与可数可加性（`def:measure-measure`）。

###### paragraph：计数测度、Dirac测度与加权点测度

1. 分情形核对计数测度的可数可加性。
2. 定义$\delta_x(A)=\mathbf 1_A(x)$并核对可加性，用分组$\sigma$代数说明不要求单点可测。
3. 有限个加权点测度是加权计数的推广，可数情形留到2.2.4的加权和引理。

###### paragraph：有限性条件

1. 定义有限、概率与$\sigma$有限测度（`def:measure-finiteness`）。
2. $\mathbb N$上计数测度总量无限但$\sigma$有限；$\mathbb R$上计数测度因$\mathbb R$不可数而非$\sigma$有限；声明$\sigma$有限只在需要处单独假设。

#### 2.2.4 测度的性质

1. 定理 `thm:measure-basic-properties`：有限可加、单调与差公式、可数次可加、从下连续、首项有限时从上连续；分别用不交差集、不交化、相邻差集与取补证明。
2. 用$\mathbb N$上计数测度的尾集说明从上连续的有限性条件不能省略，并指出证明失效于$+\infty-+\infty$。

###### paragraph：限制与加权和

1. 区分限制到可测子集（改变质量所在/底集）与限制到子$\sigma$代数（改变可测范围）两种操作。
2. 引理 `lem:measure-weighted-sum`：可数非负加权和仍是测度，用有限截断与上确界证明非负二重级数换序，并说明$0\cdot(+\infty)=0$约定的作用。
3. 例：$\sum_n2^{-n}\delta_n$为概率测度，偶数集测度$1/3$、奇数集$2/3$。

#### 2.2.5 零测集

###### paragraph：零测集与几乎处处

1. 定义零测集与几乎处处（`def:measure-null-set`），解释“包含于零测集”的写法，并用$\delta_0$、$\delta_1$说明几乎处处依赖测度。
2. 由可数次可加性合并可数个零测例外，指出不可数并不适用，回指2.3.2中$[0,1]$由不可数个零测单点组成。

###### paragraph：完备性与完备化

1. 用三点空间上$\delta_1$的零测集$\{2,3\}$含不可测子集引出完备性定义（`def:measure-complete`），并与度量完备性区分。
2. 定理 `thm:measure-completion`：完备化的构造，依次证明赋值与表示无关、$\sigma$代数、可数可加与完备性；回到例子得到幂集上的$\delta_1$。

### 2.3 测度的构造

本节把可数覆盖做成外测度并用Carathéodory判据筛选可测集，构造Lebesgue测度、计算可数集与Cantor集，证明正则性与完备化关系，简述多维情形，抽象出预测度延拓与$\pi$--$\lambda$唯一性，最后构造Lebesgue--Stieltjes测度。

#### 2.3.1 外测度

###### paragraph：覆盖的总代价

1. 定义外测度（`def:measure-outer`）。
2. 引理 `lem:measure-cover-outer`：由覆盖族与代价函数取下确界得到外测度，用$\varepsilon2^{-n}$选覆盖证明可数次可加性。
3. 两点空间上只允许整体覆盖的例子说明外测度对不交集合不可加。

###### paragraph：Carathéodory可测性

1. 用测试集合的分割直观引出Carathéodory可测定义（`def:measure-caratheodory-measurable`），说明只需验证“$\ge$”。
2. 定理 `thm:measure-caratheodory-criterion`（完整证明）：补集与有限并、可数不交并的归纳与式 `eq:measure-caratheodory-chain`、不交化及零外测度集，得到完备测度。
3. 指出定理不保证可测族含所需集合，引出对长度的具体验证。

#### 2.3.2 Lebesgue测度

###### paragraph：区间覆盖与Lebesgue外测度

1. 用开区间覆盖定义Lebesgue外测度，引用 `fig:measure-outer-cover`（覆盖总长$1.4$，外测度$1$）说明下确界的含义，列出需验证的两件事。

###### paragraph：区间的外测度

1. 引理 `lem:measure-finite-cover`：单调函数增量形式的闭区间有限开覆盖不等式，对区间个数归纳证明，供2.3.5复用。
2. 引理 `lem:measure-interval-outer`：由Heine--Borel紧性化为有限覆盖，证明闭区间外测度等于长度，再推广到一般与无界区间。

###### paragraph：区间满足Carathéodory判据

1. 引理 `lem:measure-halfline-measurable`：覆盖区间被点$a$切成两段，长度和不变，得到半直线的Carathéodory可测性。
2. 定义 `def:measure-lebesgue`：Lebesgue可测集$\mathcal L$与Lebesgue测度，说明$\mathcal B(\mathbb R)\subseteq\mathcal L$、区间测度为长度及平移不变性。

###### paragraph：可数集的测度

1. 单点与可数集测度为零，有理点集测度为零、无理数集测度为一，对比Jordan外测量，并兑现不可数并的说明。

###### paragraph：Cantor集

1. 例 `ex:measure-cantor-set`：构造Cantor集，由$(2/3)^n\to0$得测度为零，引用 `fig:measure-cantor-set`。
2. 用只含数字0、2的三进制展开构造$0$--$1$序列到Cantor集的单射并估计差值$\ge3^{-k}$，由对角线方法得不可数，区分零测性与可数性。

#### 2.3.3 Lebesgue测度的逼近与推广

###### paragraph：开集外逼近与紧集内逼近

1. 定理 `thm:measure-lebesgue-regularity`：开集外逼近（先有限测度，再分片），闭集内逼近（对补集），有限测度时紧集内逼近（截断与从上连续）。
2. 以$E=[0,1]\setminus\{1/2\}$、$\varepsilon=0.25$复算外差$0.1$、内差$0.2$，引用 `fig:measure-inner-outer-approx`。

###### paragraph：Lebesgue可测集与Borel集

1. 由开集列之交得到与可测集只差零测集的Borel集。
2. 定理 `thm:measure-lebesgue-completion`：Lebesgue测度是Borel上Lebesgue测度的完备化，两向证明。
3. 区分$\mathcal B(\mathbb R)\subsetneq\mathcal L\subsetneq\mathcal P(\mathbb R)$：前者借Cantor集子集的基数比较、后者借Vitali构造，二者均只作边界说明不证明。

###### paragraph：多维Lebesgue测度

1. 以开矩形与体积替换区间与长度，逐项说明网格化有限覆盖、超平面切割半空间、有理顶点矩形生成Borel集等对应步骤；与乘积测度的一致性留到第3章 `sec:integral-iterated`。

#### 2.3.4 测度延拓的存在性和唯一性

###### paragraph：从预测度延拓

1. 定义集合代数与预测度（`def:measure-algebra-premeasure`），以左开右闭区间的有限不交并为例。
2. 定理 `thm:measure-caratheodory`（Carathéodory延拓定理）：证明外测度在代数上等于预测度、代数中集合可测，从而延拓存在；$\sigma$有限时唯一性由 `thm:measure-uniqueness` 给出，并解释局部化的作用。

###### paragraph：$\pi$系统与$\lambda$系统

1. 说明“取值相等的集合族”对一般并不封闭，引出$\pi$系统与$\lambda$系统（`def:measure-pi-lambda-systems`），证明二者兼具即$\sigma$代数。
2. 定理 `thm:measure-pi-lambda`（完整证明）：用$\mathcal D_A$两次最小性论证说明最小$\lambda$系统对交封闭。

###### paragraph：测度的唯一性

1. 定理 `thm:measure-uniqueness`：同有限总量时在生成$\pi$系统上一致即处处一致；$\sigma$有限版本要求取自$\pi$系统的公共有限覆盖片，逐片应用后拼接。
2. 反例：有理点计数测度$\mu$与$2\mu$都$\sigma$有限、在全部$(a,b]$上都为$+\infty$却在$\{0\}$上不同，说明条件不可替换；应用于Lebesgue测度的唯一性。

#### 2.3.5 Lebesgue--Stieltjes测度

###### paragraph：用单调函数的增量赋值

1. 从长度即$x\mapsto x$的增量过渡到一般单调函数增量。
2. 定理 `thm:measure-stieltjes`：在区间代数上用共同细分定义赋值，用右连续性挪动端点、紧性与 `lem:measure-finite-cover` 证明可数可加，再处理无界区间，由延拓定理得唯一Borel测度。
3. 从测度从上连续的角度解释右连续性的必要性。

###### paragraph：点质量与例子

1. 由递减区间得$\mu_F(\{x\})=F(x)-F(x-)$；$F(x)=x$给出$\lambda$，阶跃函数给出$\delta_0$，加常数不改变测度。
2. 例 `ex:measure-stieltjes-mixture`：$F$在$[0,1)$斜率$1/2$、在$1$处跳$1/2$，得$\tfrac12\lambda|_{[0,1]}+\tfrac12\delta_1$，复算$\mu_F((0.5,1])=0.75$，引用 `fig:measure-stieltjes-jump`。
3. 指出连续$F$无点质量但仍可能奇异（指向2.8），密度问题留到第4章。

### 2.4 可测映射与可测函数

本节用原像定义可测映射，给出生成族判据、复合与连续映射的可测性，专门化为实值可测函数并证明运算与可数极限保持可测，讨论零测修改与不可数运算的边界。

#### 2.4.1 原像判据与可测复合

###### paragraph：可测映射的定义

1. 引卷一集合映射章说明原像不要求可逆，定义可测映射（`def:measure-measurable-map`）。
2. 用四点分组空间上的$f$可测、$g$不可测，以及把目标$\sigma$代数换成平凡族后$g$变可测，说明可测性依赖两端集合族。

###### paragraph：生成族判据

1. 引理 `lem:measure-generator-criterion`：原像保持补与可数并，故只需检查生成族；引用 `fig:measure-preimage-criterion`。

###### paragraph：复合与连续映射

1. 由复合原像公式证明可测复合，并指出中间空间须用同一$\sigma$代数。
2. 连续映射在两端取Borel结构时可测；说明两端取Lebesgue可测集时连续函数可能不可测（只陈述，不构造）。

#### 2.4.2 可测函数的运算

###### paragraph：阈值判据

1. 定义可测函数、扩展实值可测函数与Borel可测函数（`def:measure-measurable-function`）。
2. 引理 `lem:measure-threshold`：只需有理阈值集合可测；再由可数运算得到其他阈值集合。

###### paragraph：示性函数与简单函数

1. 指示函数可测当且仅当集合可测，以$\mathbf 1_{\mathbb Q}$回应Jordan反例。
2. 定义简单函数（`def:measure-simple-function`），给出标准写法与表示不唯一的例子，积分与逼近留给第3章。

###### paragraph：代数运算

1. 定理 `thm:measure-function-operations`：连续复合、用有理数分拆证明和的可测性，由平方恒等式、绝对值公式得积、最大最小值，分母非零时得商。
2. 扩展实值时须先排除$+\infty-\infty$等无定义点。

#### 2.4.3 函数列的可测性

###### paragraph：可数极限

1. 定理 `thm:measure-limits`：上下确界、上下极限与逐点极限可测，说明这不涉及极限与积分交换。

###### paragraph：零测修改

1. 完备空间中零测修改保持可测；用三点空间$\delta_1$的例子说明不完备时失败，并给出选可测代表或完备化的处理。

###### paragraph：不可数运算的边界

1. 对非Borel集$S$，单点示性函数族的上确界为$\mathbf 1_S$而不可测，说明证明只对可数指标成立。

### 2.5 推前测度

本节用原像累计质量定义推前测度，证明测度性、总量保持与复合规则，讨论保测映射和$\sigma$有限性的丢失，再计算多对一合并与坐标投影产生的边缘测度。

#### 2.5.1 推前测度的定义与性质

###### paragraph：用原像累计质量

1. 定义推前测度（`def:measure-pushforward`）。
2. 定理 `thm:measure-pushforward-properties`：原像保持不交并得测度性与总量保持，复合原像公式得$(S\circ T)_\#\mu=S_\#(T_\#\mu)$。

###### paragraph：保持测度的映射

1. 定义保持测度，循环移位保持计数测度，平移保持$\lambda$。
2. 伸缩$T(x)=2x$：在区间上复算并用唯一性定理得$T_\#\lambda=\tfrac12\lambda$。

###### paragraph：$\sigma$有限性一般不保持

1. $\mathbb N$上计数测度经常值映射推到单点得到非$\sigma$有限测度，提醒使用唯一性或分解定理时单独核对。

#### 2.5.2 合并与投影产生的测度

###### paragraph：多对一映射合并质量

1. 权重$0.1,0.2,0.3,0.4$经$T(1)=T(3)=a$、$T(2)=T(4)=b$推前得$0.4\delta_a+0.6\delta_b$。
2. $\lambda|_{[0,1]}$经常值映射得点质量，经$\lfloor2x\rfloor$得$\tfrac12\delta_0+\tfrac12\delta_1$，引用 `fig:measure-pushforward-merge`。

###### paragraph：坐标投影与边缘测度

1. 由$\pi^{-1}(B)=B\times\mathbb R^{d-k}$定义边缘测度，联系卷一随机向量章的边缘分布。
2. 例 `ex:measure-projection-marginal`：三点质量的两个边缘，以及单位正方形面积测度的边缘经区间比较与唯一性得到$\lambda|_{[0,1]}$，引用 `fig:measure-projection-marginal`。
3. 平面$\lambda_2$的边缘在每个非退化区间上无限，说明$\sigma$有限性可能丢失；推前积分公式留到第3章，边缘密度留到第4章，不预设输出有密度。

### 2.6 测度之间的关系

正文：[06-relations.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/02-measures/06-relations.tex)

1. 回顾前几节在同一可测空间上出现的长度、点质量、计数、加权和与推前测度，提出比较两种赋值的问题；固定$(X,\mathcal A)$及非负测度$\mu,\nu$，本节只问零测集是否一同被忽略、质量能否分别集中在不交区域，两者只读取集合质量，不用积分或密度。

#### 2.6.1 绝对连续与等价测度

1. 承接2.2中“可忽略总相对于某个测度”，说明比较两个测度最基本的信息是零测集族的包含关系。

###### paragraph：零测集的包含关系

1. 从“凡$\mu$忽略的集合$\nu$也忽略，则$\mu$-几乎处处的结论对$\nu$同样成立”引出定义`def:measure-absolutely-continuous`：$\nu\ll\mu$及等价测度$\mu\sim\nu$。
2. 说明记号方向（参考测度写在右边）以及定义只比较“是否为零”。
3. 例：$X=\{0,1\}$，$\mu=\delta_0+\delta_1$，$\nu=\delta_0$；$\mu$的零测集只有空集，故$\nu\ll\mu$；$\nu(\{1\})=0\ne\mu(\{1\})$，反向不成立。配图`fig:measure-absolute-continuity`(a)。
4. 同一例中取$\rho=2\delta_0+5\delta_1$，与$\mu$零测集相同而质量不同，说明等价不意味着质量相同。

###### paragraph：只检查单点为什么不够

1. $\delta_0$相对于$\lambda$不绝对连续可由单点看出；但$\lambda|_{[0,1]}$与$\lambda|_{[2,3]}$在每个单点上都为零，却在$[0,1]$上分别为$1$与$0$，互不绝对连续。原因是不可数集的质量不能拆成单点质量之和，定义要求检查每个可测集。配图`fig:measure-absolute-continuity`(b)。

###### paragraph：小质量控制

1. 从“绝对连续”名称引出“参考测度小推出目标测度小”的加强说法，并指出需要目标测度有限。
2. 定理`thm:measure-ac-epsilon-delta`：$\nu$有限时，$\nu\ll\mu$当且仅当$\varepsilon$–$\delta$小质量条件成立。
3. 证明充分性：$\mu(A)=0$时对每个$\varepsilon$都有$\nu(A)<\varepsilon$。
4. 证明必要性（反证）：取$\mu(A_n)<2^{-n}$、$\nu(A_n)\ge\varepsilon$，尾并$B_k$满足$\mu(B_k)\le2^{1-k}$、$\nu(B_k)\ge\varepsilon$。
5. 对递减的$B_k$取交得$\mu(B)=0$，由$\nu$有限及从上连续性得$\nu(B)\ge\varepsilon$，矛盾。
6. 反例说明有限性不能去掉：$I_k=(2^{-k},2^{1-k}]$，$\nu=\sum_k2^k\lambda|_{I_k}$（2.2中的可数加权和）满足$\nu\ll\lambda$，但$\lambda(I_k)\to0$而$\nu(I_k)=1$；$\nu$总质量无限，与定理不矛盾。配图`fig:measure-absolute-continuity-blocks`。

#### 2.6.2 相互奇异

1. 把相互奇异作为与绝对连续相对的另一极端引入：两种质量各自待在对方忽略的区域。

###### paragraph：质量集中在不交的可测区域

1. 定义“$\nu$集中在$N$上”，再给出定义`def:measure-singular`：存在$N$使$\mu(N)=0$、$\nu(X\setminus N)=0$，记$\mu\perp\nu$。
2. 用补集$N'=X\setminus N$说明关系对称，并给出“$X$分成两个区域分别承载两种质量”的直观。
3. 例：$\lambda|_{[0,1]}$与$\tfrac12\delta_{1/2}$相互奇异，$N=\{1/2\}$位于区间内部，说明相互奇异不要求位置分开。配图`fig:measure-mutually-singular`(a)。
4. 证明$\nu\ll\mu$与$\nu\perp\mu$同时成立时$\nu=0$，预告2.8唯一性证明会用到。

###### paragraph：可测分离不等于距离分离

1. 构造$\mu=\sum_n2^{-n}\delta_{q_n}$（$q_n$列举有理数）与$\nu=\sum_n2^{-n}\delta_{q_n+\sqrt2}$；由$\sqrt2$无理，$\mathbb Q$与$\mathbb Q+\sqrt2$不交，取$N=\mathbb Q+\sqrt2$得$\mu\perp\nu$。
2. 两个点集都稠密，故两种测度在每个非空开区间上都有正质量；相互奇异是可测集合层面的分离，与第1章距离结构无关；顺带指出两者都与$\lambda$相互奇异。配图`fig:measure-mutually-singular`(b)。

### 2.7 测度的差

正文：[07-signed-measures.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/02-measures/07-signed-measures.tex)

1. 从“两种测度在每个集合上差多少”进入，对有限测度作差得到可正可负的赋值；本节研究其正负区域、唯一的正负部分与变化总量，不讨论有符号测度的积分。

#### 2.7.1 有限有符号测度

###### paragraph：从测度之差到有符号赋值

1. 对有限测度$\nu,\mu$验证$\eta=\nu-\mu$保持可数可加性（两个收敛级数相减），引出定义`def:measure-signed`：取有限实值、$\eta(\varnothing)=0$、可数可加。
2. 说明不交并与次序无关，故级数在任意重排下收敛、因而绝对收敛；本章只用“通项趋于零”。
3. 区分对集合赋予实数的有符号测度与在点上取负值的函数；限于有限值以避免$+\infty-\infty$。
4. 例`ex:measure-signed-weights`：四点集上权重$2,-1,1,-2$，写成$\nu-\mu$；计算$\eta(X)=0$、$\eta(\{1,2\})=1$、$\eta(\{1,3\})=3$、$\eta(\{2,4\})=-3$，说明全空间值为零不代表各处都小。配图`fig:measure-signed-weights`。
5. 指出同一$\eta$还可写成$(\nu+\delta_1)-(\mu+\delta_1)$，差表示不唯一，引出寻找由$\eta$本身确定的表示。

#### 2.7.2 Hahn分解与Jordan分解

1. 从四点例中$\{1,3\}$与$\{2,4\}$的符号分割提出一般问题：能否把$X$切成正、负两个区域。

###### paragraph：正集与负集

1. 用$\eta(\{1,2\})\ge0$而子集$\{2\}$为负说明只看整体取值不够，给出定义`def:measure-positive-set`（正集、负集）。
2. 证明正集的可测子集及可数并仍是正集（不交化后逐项非负）。

###### paragraph：两条准备性质

1. 说明构造需要取值有界（最小集合才可能存在）和单调连续性。
2. 引理`lem:measure-signed-bounded`：用“无界集”反复二分，构造两两不交且$|\eta(B_n)|\ge1$的集合列，与级数通项趋零矛盾。
3. 引理`lem:measure-signed-continuity`：递增列用相邻差集与部分和，递减列取在$A_1$中的补；指出递减情形无需额外有限性假设。

###### paragraph：Hahn分解

1. 说明思路：寻找使$\eta$最小的集合，最小集合自然为负集、补集为正集；难点是证明最小值可达。
2. 定理`thm:measure-hahn`：存在正集$P$使$X\setminus P$为负集；两组分解之差的每个可测子集上$\eta$为零。
3. 证明第一步：$m=\inf\eta$有限；由$\eta(A\cap B)\le\eta(A)+\eta(B)-m$归纳控制有限交$C_{n,k}$，得$\eta(C_{n,k})<m+2^{1-n}$。
4. 证明第二步：对$k$取递减交、对$n$取递增并，借单调连续性得$\eta(D)=m$。
5. 证明第三步：从$D$中去掉正值子集或向$D$添入负值集合都会低于$m$，故$D$为负集、补集为正集；最后说明两组分解之差同时为正集与负集的子集。
6. 指出证明只用集合运算与单调连续性；以$\eta=\lambda|_{[0,1]}-\lambda|_{[2,3]}$为例，$P_1=(-\infty,3/2)$与$P_2=(-\infty,2)$都是正区域，或只差一个零长度单点。配图`fig:measure-hahn-decomposition`。

###### paragraph：Jordan分解

1. 说明区域不唯一但限制到区域上的质量唯一。
2. 定理`thm:measure-jordan`：$\eta^+(A)=\eta(A\cap P)$、$\eta^-(A)=-\eta(A\cap N)$为相互奇异的有限测度且$\eta=\eta^+-\eta^-$，与Hahn分解无关；相互奇异的差表示唯一。
3. 证明非负性、可数可加性与相互奇异。
4. 证明与Hahn分解无关：利用两组分解之差上$\eta$为零。
5. 证明唯一性：相互奇异的$\alpha,\beta$给出的分离集本身就是一组Hahn分解。
6. 反例：$\alpha=\lambda|_{[0,3]}$、$\beta=\lambda|_{[1,2]}+2\lambda|_{[2,3]}$逐段核对得$\alpha-\beta=\eta$，但二者重叠、总质量各为$3$，而$\eta^\pm$总质量为$1$。配图`fig:measure-jordan-decomposition`。
7. 证明极小性$\eta^+\le\alpha$、$\eta^-\le\beta$，并由此得到$\eta^+(A)=\sup\{\eta(E):E\subseteq A\}$。

#### 2.7.3 总变差测度

1. 从$|\eta(A)|$允许抵消引出累计正负质量的需要。

###### paragraph：定义与分割刻画

1. 定义`def:measure-total-variation`：$|\eta|=\eta^++\eta^-$，说明它是有限非负测度。
2. 定理`thm:measure-total-variation-partition`：$|\eta|(A)$等于有限可测分割上$\sum_i|\eta(A_i)|$的上确界；先用正负部分给上界，再用Hahn区域分割取得。
3. 回到四点例：不分割得$0$，相邻配对得$2$，按符号分组得$6$，任何细分不超过单点绝对值之和$6$，故$|\eta|(X)=6$。配图`fig:measure-total-variation-partition`。

###### paragraph：净值与总量

1. 由平凡分割得$|\eta(A)|\le|\eta|(A)$，并说明$|\eta|(A)=0$当且仅当$\eta$在$A$的每个子集上为零，“几乎处处”对有符号测度相对于$|\eta|$理解。
2. 对概率测度$P,Q$，由$\eta(X)=0$与正部分的上确界读法得$\tfrac12|P-Q|(X)=\sup_A(P(A)-Q(A))$，指出它在比较概率分布时称为全变差距离，进一步比较留到后续讨论概率分布的部分；预告第3章用$|\eta|$规定有符号测度积分的绝对可积条件，第4章研究$\eta$的函数表示。

### 2.8 测度的分解

正文：[08-decompositions.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/02-measures/08-decompositions.tex)

1. 指出绝对连续与相互奇异是两个极端，一般测度介于其间；本节先相对于参考测度把$\sigma$有限测度唯一分成两部分，再在实轴上把奇异部分分为点质量与奇异连续质量并用Cantor集构造后者；只用测度，不要求密度。

#### 2.8.1 Lebesgue分解

###### paragraph：分解的陈述

1. 以“$\mu$看不见的质量”与“$\mu$看得见的质量”引出定理`thm:measure-lebesgue-decomposition`：$\mu$任意、$\nu$为$\sigma$有限时唯一分解$\nu=\nu_{\mathrm{ac}}+\nu_{\mathrm{s}}$，且存在$\mu$零测集$N$使两部分分别为$\nu$在$N$与其补上的限制。
2. 例：$\nu=\lambda|_{[0,1]}+\delta_2$以$\lambda$为参考时$\nu_{\mathrm s}=\delta_2$，以$\delta_2$为参考时角色互换，说明分解依赖参考测度。配图`fig:measure-lebesgue-decomposition`。

###### paragraph：有限情形：选取承载最多质量的零测集

1. 说明构造思想：把所有仍有$\nu$质量的$\mu$零测集并入$N$，用上确界实现。
2. 证明（$\nu$有限）：令$M=\sup\{\nu(A):\mu(A)=0\}$，取$\nu(N_k)>M-1/k$，并集$N$满足$\mu(N)=0$、$\nu(N)=M$。
3. 定义$\nu_{\mathrm s},\nu_{\mathrm{ac}}$为$\nu$在$N$及其补上的限制，验证$\nu_{\mathrm s}\perp\mu$。
4. 若$\mu(A)=0$，则$N\cup(A\setminus N)$仍为$\mu$零测集，得$M+\nu(A\setminus N)\le M$，消去有限的$M$得绝对连续性。
5. 指出“消去”正是需要$\nu$有限之处。

###### paragraph：$\sigma$有限情形与唯一性

1. 说明把$\sigma$有限测度切成有限片后逐片构造。
2. 存在性证明：取不交有限片$X_j$，在各片取$N_j\subseteq X_j$，合并为$N$，逐片求和验证绝对连续。
3. 唯一性证明：取两个奇异部分分离集的并$T$，在$A\cap T$上绝对连续部分为零、在$A\setminus T$上奇异部分为零，分别读取$\nu$得两组分解相同；指出论证不做减法，全程不用积分、Hahn分解或Radon–Nikodym定理。
4. 反例：$[0,1]$上$\nu$为计数测度、$\mu=\lambda$时，任一点$x\notin N$都迫使$\nu(\{x\})=0$，说明存在性中的$\sigma$有限条件不能随意去掉。
5. 预告第4章在积分建立后回答绝对连续部分何时能写成加权形式，本节分解不依赖它。

#### 2.8.2 实轴上的三元分解

1. 以$\lambda$为参考时单点都是零测集，点质量必属奇异部分；提出奇异部分是否只有点质量的问题。

###### paragraph：点质量至多可数

1. 定义原子；引理`lem:measure-atoms-countable`：按质量下界$1/k$分组，每组至多$k\rho(\mathbb R)$个点，故原子至多可数。
2. 定义离散部分$\rho_{\mathrm d}(B)=\sum_{x\in A\cap B}\rho(\{x\})$与无原子的余部$\rho_{\mathrm c}$。
3. 定理`thm:measure-three-part`：有限Borel测度唯一分为离散、绝对连续与奇异连续三部分，并定义奇异连续测度。
4. 证明存在性：对$\rho_{\mathrm c}$关于$\lambda$作Lebesgue分解，奇异部分无原子。
5. 证明唯一性：其余两项无原子，故原子质量全由离散项承担，离散项被确定；余下两项由Lebesgue分解唯一性确定。
6. 说明离散部分也与$\lambda$相互奇异，Lebesgue奇异部分为$\rho_{\mathrm d}+\rho_{\mathrm{sc}}$；三项是同一测度的成分而非互斥类别。
7. 由从下连续性得累计函数跳跃$G(x)-G(x-)=\rho(\{x\})$，与2.3的Lebesgue–Stieltjes单点质量公式一致；累计函数连续只能排除离散部分，不能排除奇异连续部分。

###### paragraph：Cantor函数

1. 回到2.3的Cantor集（引用`fig:measure-cantor-set`），说明目标是构造只在$C$上增长的连续单调函数。
2. 递归构造分段线性的$F_n$：在$C_n$的每个区间上增长$2^{-n}$，下一步把区间三等分，左右段各增长$2^{-n-1}$、中段取常数。
3. 计算$\sup|F_{n+1}-F_n|=2^{-n}/6$，得一致Cauchy性与$\sup|F-F_n|\le2^{-n}/3$。
4. 例：$F_n(1/4)$依次为$3/8,5/16,11/32,21/64$，交替逼近$F(1/4)=1/3$，并用三进制$0.0202\ldots$到二进制$0.0101\ldots$核对。配图`fig:measure-cantor-function`。
5. 列出$F$的四条性质：单调且$F(0)=0$、$F(1)=1$；用$\varepsilon/3$论证连续；在删去的开区间上为常数；在$C_n$每个区间上增长$2^{-n}$。

###### paragraph：Cantor测度

1. 将$F$延拓到实轴，用2.3的Lebesgue–Stieltjes构造得到$\mu_C$。
2. 核对总质量为$1$、无原子，并用从下连续性证明$\mu_C$在每个删去的开区间及两条半直线上为零，故集中在$C$上；结合$\lambda(C)=0$得$\mu_C\perp\lambda$。
3. 计算$\mu_C(C_n)=1$而$\lambda(C_n)=(2/3)^n\to0$，说明$\mu_C$是非零奇异连续测度；预告第3章3.8复用Cantor函数检验增量恢复公式。配图`fig:measure-cantor-mass-length`。

###### paragraph：三类成分的混合

1. 构造$\rho=\tfrac12\lambda|_{[0,1]}+\tfrac14\delta_{1/2}+\tfrac14\mu_C$，写出累计函数$G$，计算$G(1/2-)=3/8$、$G(1/2)=5/8$、$G(1/4)=5/24$。
2. 按定理`thm:measure-three-part`的步骤得到$\rho_{\mathrm d}=\tfrac14\delta_{1/2}$、$\rho_{\mathrm{ac}}=\tfrac12\lambda|_{[0,1]}$、$\rho_{\mathrm{sc}}=\tfrac14\mu_C$；指出从$G$只能直接读出跳跃，连续增长中两种成分无法凭连续性区分，第4章用Radon–Nikodym定理说明哪一部分可由密度表示。配图`fig:measure-three-part-decomposition`。

### 2.9 本章小结

正文：[09-summary.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/02-measures/09-summary.tex)

1. 回顾2.1至2.5：从计数、长度和Jordan测量的局限出发要求对可数运算封闭；$\sigma$代数与测度分别规定可测范围与赋值；外测度、Carathéodory条件和延拓定理构造Lebesgue测度与Lebesgue–Stieltjes测度，$\pi$–$\lambda$定理保证唯一；Cantor集区分零测与可数；可测映射与推前测度处理质量的传递。
2. 回顾2.6至2.8：同一Borel结构上可放不同测度；绝对连续与相互奇异只读集合质量；Hahn、Jordan分解与总变差处理测度之差；Lebesgue分解与实轴三元分解相对于参考测度分出不同质量成分，Cantor测度给出奇异连续例子；概括三种分解各自回答的问题。
3. 说明进入第3章时已具备的对象（可测集合、测度、可测函数与简单函数、有符号测度的总变差），第3章从简单函数积分建立一般积分，第4章研究密度表示与换测度；强调测度分解并未证明绝对连续部分一定有密度。

## 第3章 积分

正文入口：[03-integration.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/03-integration.tex)。

本章研究如何依据测度累计函数的取值，并在什么条件下交换积分与极限、累次求积、换元和求导。先从简单函数建立积分，构造简单函数逼近，推广到非负、实值、复值函数与有符号测度；再建立运算性质，对照经典积分，研究极限交换；后五节处理累次积分、换元、含参积分、积分与微分及小结。只依赖第2章的测度、可测函数与有符号测度，不以密度为前提。

1. 从细杆总质量、加权平均与函数列的累计三个问题进入，指出共同对象是测度空间上的可测函数，所求的数在示性函数时退化为测度，一般情形按“函数值乘以所占测度”累计；交代本章建立定义、运算及与极限、累次求积、换元、求导的交换条件。

2. 说明前四节建立积分本身：3.1由简单函数与二进分层逼近定义各类积分；3.2先证单调收敛定理再推广运算；3.3对照离散求和、黎曼积分与反常积分；3.4按递增、非负、可积控制、绝对积分可和、有限测度上一致收敛五类条件研究极限交换。

3. 说明后五节的分工：3.5乘积测度与Tonelli、Fubini定理；3.6可测映射与光滑可逆变换下的换元；3.7含参积分的连续与可导；3.8绝对连续函数、恢复公式及Cantor函数边界；3.9小结。声明全章只用第2章材料，密度表示留给第4章。

### 3.1 积分的定义

正文：[01-definition.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/03-integration/01-definition.tex)

1. 从测度已能累计区域大小、现在让各位置带上函数值贡献进入，指出一般函数在区域内不断改变取值的困难；交代路线：常值块的精确累计、按函数值分层的逼近、上确界定义、扩展被积函数取值范围、有符号测度；固定测度空间并约定$0\cdot(+\infty)=0$。

#### 3.1.1 简单函数的积分

###### paragraph：有限个常值块的累计

1. 回用第2章简单函数的定义及其按取值的标准写法，解释每层贡献为“高度乘以测度”，给出定义`def:integral-simple`（不交表示、可取$+\infty$、区域积分$\int_Es=\int s\mathbf 1_E$）。

2. 说明积分直接使用已有测度称重；用$\mathbf 1_{\mathbb R}$说明积分可为无穷，用补零项的两种写法说明约定$0\cdot\infty=0$的作用。

3. 以$[0,3]$上在$A_1=[0,1)\cup[2,2.5)$取2、在$A_2=[1,2)\cup[2.5,3]$取0.5的函数计算积分$3.75$，强调同值块合并成层、层不必是区间。配图`fig:integral-simple-height-measure`。

###### paragraph：与表示方式无关

1. 用$\mathbf 1_{[0,2]}$的两种写法引出良定性问题，陈述引理`lem:integral-simple-properties`：与表示无关、加法与非负数乘、单调性、$E\mapsto\int_Es$为测度。

2. 证明：补零层化为两个分割，在共同细分上用有限可加性逐项比较；加法、单调性在共同细分上逐项验证；区域累计是有限个测度$\mu(A_i\cap\cdot)$的非负组合，由第2章加权和引理为测度。

3. 说明第4条为区域间比较累计值服务，单调收敛定理证明中将用其从下连续性。

#### 3.1.2 简单函数逼近

###### paragraph：按函数值分层

1. 对比黎曼积分对定义域的分割，指出一般测度空间没有小区间、可测函数可剧烈振荡；改为切分函数值，层是阈值集合之差，总可测。配图`fig:integral-riemann-lebesgue-partitions`，指出层$\{f\ge1.5\}$由两段区间组成。

2. 陈述并证明引理`lem:integral-simple-approx`：$s_n=2^{-n}\lfloor2^n\min(f,n)\rfloor$是简单函数（写出层集合）、递增（用$2\lfloor y\rfloor\le\lfloor2y\rfloor$）、不超过$f$、逐点收敛（含$f=+\infty$），$f$有界时一致收敛。

3. 以$[0,2]$上的$x^2$说明$s_1$、$s_2$的断点与截断高度，解释细分与截断两个方向的改进，断点由$f$决定。配图`fig:integral-dyadic-approximation`。

###### paragraph：取正负值的函数

1. 指出下取整对负值不适用，给出正部、负部定义`def:integral-positive-negative-parts`及$f=f^+-f^-$、$|f|=f^++f^-$，说明每点至多一部分非零。配图`fig:integral-positive-negative-parts`（$\sin x$）。

2. 分别逼近两部分得$\varphi_n=s_n^+-s_n^-\to f$且$|\varphi_n|\le|f|$，有界时一致；说明积分是否随逼近收敛需在定义后讨论。

#### 3.1.3 非负可测函数的积分

###### paragraph：下方逼近的上确界

1. 说明下方简单函数给出偏小估计，取上确界不需指定逼近列；给出定义`def:integral-nonnegative`（允许$+\infty$、区域积分、称Lebesgue积分并写$\int f(x)\,\mathrm dx$）。

2. 用简单函数单调性说明与简单函数积分一致；沿逼近列取极限留到单调收敛定理。

3. 例`ex:integral-identity-on-unit`：用$2^n$段上的下方阶梯$s_n$与上方阶梯$t_n$夹逼，得$\int_{[0,1]}x\,\mathrm dx=1/2$，说明上方简单函数控制全部候选；指出一般计算留待与黎曼积分的关系。

###### paragraph：单调性与零测集

1. 陈述并证明引理`lem:integral-nonnegative-basic`：对函数单调；$a\mu(\{f\ge a\})\le\int f$；几乎处处相等则积分相等（候选$s\mathbf 1_{X\setminus N}$）；积分为零当且仅当几乎处处为零（用$\{f\ge1/n\}$与可数次可加性）；积分有限则几乎处处有限。

2. 用$\mathbf 1_{[0,1]}+\infty\cdot\mathbf 1_{\mathbb Q\cap[0,1]}$说明零测集上的无穷值不影响积分，交代各条在后文的用途。

3. 提醒零测修改后的可测性取决于完备性，对比$(\mathbb R,\mathcal L,\lambda)$与Borel结构。

#### 3.1.4 实值与复值函数的积分

###### paragraph：正负贡献分别累计

1. 给出定义`def:integral-integrable`：积分存在（至少一部分有限）、Lebesgue可积（$\int|f|<\infty$）、复值可积及其积分、记号$L^1(\mu)$与区域积分。

2. 由$f^\pm\le|f|$说明可积时积分为有限实数且函数几乎处处有限；两部分有限推出可积要用加法，留到3.2.3。

3. 用$2\mathbf 1_{[0,1)}-\mathbf 1_{[1,3)}$（积分0）、$\mathbf 1_{[0,1]}-\mathbf 1_{(1,\infty)}$（积分$-\infty$）、$\mathbf 1_{[0,\infty)}-\mathbf 1_{(-\infty,0)}$（无定义）区分三种情形。

###### paragraph：复值函数

1. 说明$|f|$可测且$|u|,|v|\le|f|$保证实部、虚部可积；以$\mathrm i\mathbf 1_{[0,1]}+(1-\mathrm i)\mathbf 1_{(1,2]}$计算$\int|f|=1+\sqrt2$、$\int f=1$；等价性留到3.2.3。

2. 指出本小节改变被积函数取值范围，下一小节改变测度的取值范围。

#### 3.1.5 有符号测度的积分

###### paragraph：分别对正负质量积分

1. 回用Jordan分解与总变差，陈述并证明引理`lem:integral-measure-monotone`（测度逐集合较小则非负积分较小，先简单函数后上确界），由$\eta^\pm\le|\eta|$推出对总变差绝对可积蕴含对两部分可积。

2. 给出定义`def:integral-signed-measure`；由Jordan分解唯一说明定义不依赖Hahn区域选取，并核对$\int\mathbf 1_A\,\mathrm d\eta=\eta(A)$；指出只调用第2章分解与已有积分。

3. 例`ex:integral-signed-measure-points`：$\eta=2\delta_a-3\delta_b+\delta_c$与$f=(1,2,-4)$，算得$\int f\,\mathrm d\eta^+=-2$、$\int f\,\mathrm d\eta^-=6$、$\int f\,\mathrm d\eta=-8$、绝对贡献12。

4. 区分负贡献来自测度符号（点$b$）与函数符号（点$c$）；线性规则与总变差估计留到3.2.4。配图`fig:integral-signed-measure-masses`。

### 3.2 积分的基本性质

正文：[02-basic-properties.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/03-integration/02-basic-properties.tex)

1. 指出上确界定义下加法不明显（候选之和只是$f+g$下方的一部分），交代路线：先证单调收敛定理，再推广非负运算、有符号与复值运算、有符号测度积分。

#### 3.2.1 单调收敛定理

###### paragraph：定理与证明

1. 陈述定理`thm:integral-monotone-convergence`，允许两边为无穷；证明先由单调性得$L\le\int f$，再固定简单函数$s\le f$与$c\in(0,1)$，构造可测递增集$E_n=\{f_n\ge cs\}$并说明其填满$X$，用$E\mapsto\int_Es$的从下连续性得$L\ge c\int s$，令$c\uparrow1$并取上确界。

2. 解释缩小因子的作用（无$c$时在$f=s$处可能永不进入$E_n$），以$f_n=x^{1/n}$、$s=0.8\cdot\mathbf 1_{(0,1]}$、$c=0.9$说明$E_n=[0.72^n,1]$逐步覆盖$(0,1]$。配图`fig:integral-monotone-convergence-sets`。

3. 说明定理不要求可积，并给出几乎处处版本：合并零测例外后应用，需$f$可测。

###### paragraph：与简单函数逼近的衔接

1. 将定理用于二进逼近列，得到任一递增简单逼近列的积分极限都等于上确界，从而简单函数的运算可以传递；计算性使用集中在3.4.1。

#### 3.2.2 非负积分的运算性质

###### paragraph：加法与数乘

1. 陈述并证明定理`thm:integral-nonnegative-linear`：逼近列相加、简单函数加法、三次单调收敛；说明不出现无穷相减与$0\cdot\infty$约定，例$\int_{[0,1]}(x+3)\,\mathrm dx=7/2$。

###### paragraph：比较、区域与上下界

1. 由单调性与加法推出有限个不交区域的可加性、区域包含时的比较、$m\mu(E)\le\int_Ef\le M\mu(E)$。

2. 以$[0,2]$上分段函数计算$3/2$并用上下界核对；可数区域留到3.4.1。

#### 3.2.3 有符号积分的运算性质

1. 声明“有符号”指被积函数，测度非负，复值按分量处理。

###### paragraph：可积性与线性

1. 由$\int|f|=\int f^++\int f^-$得实值可积等价于两部分有限；由$|f|\le|u|+|v|$得复值可积等价于实部虚部可积；可积扩展实值函数几乎处处有限，可改为实值。

2. 陈述并证明定理`thm:integral-linear`：可积性由三角不等式；实值加法用$h^++f^-+g^-=h^-+f^++g^+$；数乘按系数符号；复值按实部虚部展开。说明由线性得可积函数的比较。

###### paragraph：绝对值估计

1. 陈述并证明定理`thm:integral-abs-bound`：实值用$-|f|\le f\le|f|$；复值把积分旋转到实轴后估计实部。用$\mathbf 1_{[0,1)}-\mathbf 1_{[1,2)}$说明不等式可严格，区分实值比较与复值模长估计。

###### paragraph：用可积函数控制

1. 由$|f|\le g$可积推出$f$可积，有限测度上有界可测函数可积，例$\sin(1/x)$在$(0,1]$上可积且积分绝对值不超过1。

2. 警示允许单侧无穷的积分：$\mathbf 1_{[0,\infty)}$与$-\mathbf 1_{[0,\infty)}$之和的积分为0而$\int f+\int g$无定义。

#### 3.2.4 有符号测度积分的运算性质

###### paragraph：测度相加时的积分

1. 陈述并证明引理`lem:integral-sum-of-measures`：先简单函数，再对三个测度用单调收敛，可积情形拆正负部与实虚部。

2. 陈述并证明定理`thm:integral-signed-measure-rules`：对总变差可积函数的线性组合仍可积且线性；$|\int f\,\mathrm d\eta|\le\int|f|\,\mathrm d|\eta|$。

3. 用Hahn分解上的$\mathbf 1_P-\mathbf 1_N$说明等号可达，并解释3.1.5例中$8<12$的原因。

###### paragraph：保序性不再成立

1. 在$\eta=\delta_a-\delta_b$上，$0\le\mathbf 1_{\{b\}}$而积分为$-1$，说明有符号测度积分无一般保序性，比较时须回到$\eta^\pm$。

### 3.3 与经典积分的关系

正文：[03-classical-integrals.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/03-integration/03-classical-integrals.tex)

1. 交代将一般积分与离散求和、黎曼积分、反常积分逐一对照；跨卷引用卷1“一元函数的积分”章，说明所用的Darboux判据、反常积分截断定义与$\sin x/x$反常积分收敛性。

#### 3.3.1 与离散求和的关系

###### paragraph：非负加权和

1. 设可数集上全部子集可测、权重$w$定义的测度（计数测度为$w\equiv1$），说明非负和与次序无关。

2. 陈述并证明定理`thm:integral-discrete-sum`：单点函数积分（含值$+\infty$）、枚举后截断函数递增、单调收敛；实值与复值由绝对可和刻画，绝对收敛级数可拆分重排。

3. 例：计数测度下$\sum2^{-k}=1$，权重$2^{-k}$下$\sum k2^{-k}=2$。配图`fig:integral-counting-measure-series`。

###### paragraph：条件收敛级数不对应积分

1. 以交错调和级数说明条件收敛而不可积，正负部积分均为无穷（其按原次序之和在3.4.3求出）。

2. 解释原因：测度积分对集合赋值不依赖次序，而条件收敛级数重排可收敛到任意值（回指卷1的重排讨论）。

#### 3.3.2 与黎曼积分的关系

###### paragraph：区间与阶梯函数

1. 区间示性函数与阶梯函数的两种积分相等，端点为零测集；指出上下和即阶梯函数积分。

###### paragraph：Lebesgue判据

1. 定义振幅并证明连续当且仅当振幅为零，写出$D_f=\bigcup_m\{\omega_f\ge1/m\}$。

2. 陈述定理`thm:integral-riemann-lebesgue`：有界函数黎曼可积当且仅当$D_f$零测，此时Lebesgue可测、可积且两积分相等。

3. 证明第一步：取逐次加细的分割，上下阶梯函数$\varphi_k\uparrow\varphi$、$\psi_k\downarrow\psi$夹住$f$，$\int(\psi-\varphi)=0$，由完备性得$f$可测，单调收敛（平移$M$）得两积分相等。

4. 证明第二步：在可数分点集外$\omega_f\le\psi_k-\varphi_k$，故$D_f$零测。

5. 证明第三步：$\{\omega_f\ge\varepsilon\}$为零测紧集，用有限个总长小于$\varepsilon$的开区间覆盖，余下闭区间上由紧性取一致的$\delta$，构造分割使$U-L<\varepsilon(b-a)+2M\varepsilon$，由Darboux判据得可积。

6. 总结第一步说明共同范围内一致，第二、三步说明障碍是不连续点占据正长度，并指出完备性的作用。

###### paragraph：Dirichlet函数

1. 计算$\int_{[0,1]}\mathbf 1_{\mathbb Q}\,\mathrm d\lambda=0$，振幅处处为1，故不黎曼可积，与卷1上下和计算一致。配图`fig:integral-dirichlet-function`。

2. 区分稠密与零测；以Cantor集示性函数说明不连续点集不可数却零测、黎曼可积且积分为0，结论是决定黎曼可积性的是不连续点集的测度。

#### 3.3.3 与反常积分的关系

###### paragraph：截断与单调收敛

1. 陈述并证明定理`thm:integral-improper`：局部黎曼可积函数非负时Lebesgue积分等于截断极限；一般函数Lebesgue可积当且仅当反常积分绝对收敛，值相等；证明用可测性、单调收敛与$f^\pm=(|f|\pm f)/2$。

2. 例：$\int_0^1x^{-1/2}=2$、$\int_1^\infty x^{-2}=1$、$\int_0^\infty\mathrm e^{-x}=1$；复值按实虚部。

###### paragraph：条件收敛的反常积分

1. $\sin x/x$在$[1,\infty)$上反常积分收敛，但逐瓣下界$2/((k+1)\pi)$使$\int|f|=\infty$，且正负部积分都无穷，Lebesgue积分不存在。配图`fig:integral-sinc-improper`。

2. 解释正负瓣按次序抵消，与条件收敛级数情形相同。

###### paragraph：Cauchy主值

1. $1/x$在$[-1,1]$上对称截断主值为0，非对称截断得$-\log2$；通常反常积分发散，Lebesgue积分不存在；主值只是额外指定的抵消规则。

### 3.4 积分与极限

正文：[04-limits.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/03-integration/04-limits.tex)

1. 指出逐点收敛不保证积分收敛，交代按五类可核查条件组织，测度本身变化时的收敛留待后文。

#### 3.4.1 非负递增条件下的极限交换

###### paragraph：递增列

1. 回用单调收敛定理，说明只需核查非负与递增、不需可积。

2. 陈述并证明定理`thm:integral-series-nonnegative`：非负级数逐项积分、递增区域积分极限、$E\mapsto\int_Ef$为测度；指出该测度在零测集上为零，其逆问题属第4章。

###### paragraph：两个计算

1. $\int_0^1-\log(1-x)/x\,\mathrm dx=\sum1/k^2\le2$；$\int_{[1,n]}x^{-2}\to1$；几何级数在$[0,1)$上逐项积分两边同为无穷。

#### 3.4.2 非负条件下的积分下界

###### paragraph：Fatou引理

1. 由尾部下确界$g_n$递增到下极限，陈述并证明引理`lem:integral-fatou`；说明不要求收敛与可积，只给下界。

###### paragraph：丢失的积分质量

1. $\mathbf 1_{[n,n+1]}$逐点趋于0而积分为1，不等式严格；质量平移到远处。配图`fig:integral-escaping-mass`(a)。

2. 换成$-f_n$说明非负性不可去，引出统一控制条件。

#### 3.4.3 可积控制条件下的极限交换

###### paragraph：控制收敛定理

1. 陈述定理`thm:integral-dominated-convergence`；证明合并可数个例外零测集（含$\{g=\infty\}$），得$f$可积，对$2g-|f_n-f|$用Fatou引理并消去有限的$\int2g$，得$\int|f_n-f|\to0$与积分收敛。

2. 说明$g$可积用于消去步骤，积分绝对误差在此只是一个数，$L^1$空间留到后文。

###### paragraph：一个可控与一个不可控的例子

1. $(1-x/n)^n\mathbf 1_{[0,n]}$受$\mathrm e^{-x}$控制，积分趋于1，与精确值$n/(n+1)$核对。

2. $n\mathbf 1_{(0,1/n)}$积分恒为1、逐点趋于0；上包络$h\ge1/x-1$不可积，故无控制函数；与$x^n$受常数1控制对照。配图`fig:integral-dominating-envelope`。

###### paragraph：函数项级数

1. 说明需控制部分和而非单项，以$\frac1k\mathbf 1_{[0,1]}$为反例。

2. 交错几何级数部分和受2控制，逐项积分得$\sum(-1)^k/(k+1)=\log2$，回答3.3.1的遗留；指出其绝对积分不可和，下一小节条件不适用。

#### 3.4.4 绝对积分可和条件下的逐项积分

###### paragraph：逐项检查的条件

1. 陈述并证明定理`thm:integral-absolute-series`：由3.4.1得$G=\sum|f_n|$可积并几乎处处有限，级数几乎处处绝对收敛，部分和受$G$控制，用控制收敛；给出余项估计。

2. 说明条件同时提供绝对收敛、控制函数与误差上界。

###### paragraph：一个带误差的计算

1. $\int_0^1\log(1+x)/x\,\mathrm dx=\sum(-1)^{n+1}/n^2$，截断误差不超过$1/N$。

#### 3.4.5 有限测度与一致收敛条件下的极限交换

###### paragraph：统一误差乘以总测度

1. 联系卷1闭区间上的一致收敛逐项积分，陈述并证明定理`thm:integral-uniform-finite`：由$|f|\le|f_N|+1$得可积，误差不超过$\mu(X)\sup|f_n-f|$。

2. 说明各项可积的必要性，并以$\sum_{k\le n}x^k/k!$求$\int_0^1\mathrm e^x=\mathrm e-1$。

###### paragraph：无限测度上的反例

1. $n^{-1}\mathbf 1_{[0,n]}$一致收敛到0而积分恒为1，质量摊平到无限测度上。配图`fig:integral-escaping-mass`(b)。

2. 综合五类条件的用途与适用范围，并把反例归为逃逸到远处、摊平到无限测度、集中到窄峰三种失效方式。

### 3.5 累次积分

正文：`tex/02-abstract-mathematics/01-metric-and-measure/03-integration/05-iterated-integrals.tex`（`sec:integral-iterated`）

1. 从矩形面积等于边长之积、区域总量可先竖切再横加进入，提出两个问题：乘积空间上的“面积”怎样由两侧测度确定；分别对两个坐标累计何时等于整体累计、两种次序何时相同。预告依次建立乘积结构与乘积测度、非负与绝对可积两个换序定理，再用于多重积分与截面计算。

#### 3.5.1 乘积可测结构与乘积测度

###### paragraph：可测矩形与乘积$\sigma$代数

1. 说明$A\times B$的大小应为$\mu(A)\nu(B)$，但圆盘等集合不是矩形，故定义可测矩形与它们生成的乘积$\sigma$代数（`def:integral-product-sigma-algebra`）。

2. 指出可测矩形对有限交封闭、构成$\pi$系统，为后面用$\pi$–$\lambda$定理比较测度作准备；以`fig:integral-product-rectangles`展示由两段区间组成的矩形，以及四分之一圆盘由逐层加细的矩形不交并内逼近。

###### paragraph：截面

1. 定义集合截面$E_x,E^y$与截面函数$f_x,f^y$，用`fig:integral-sections`说明同一区域沿两个方向的截面形状不同（一段区间与两段区间）。

2. 由截面与补、可数并可交换以及矩形截面的形式，证明乘积可测集与乘积可测函数的每个截面可测（`lem:integral-section-measurable`），证明用“截面可测的集合构成$\sigma$代数”论证。

###### paragraph：乘积测度的构造

1. 提出用截面测度累计构造乘积测度，引入$\sigma$有限条件；先在$\nu$有限时用$\pi$–$\lambda$定理证明$x\mapsto\nu(E_x)$可测，再用有限测度片的递增极限推广到$\sigma$有限（`lem:integral-section-measure-measurable`）。

2. 证明存在唯一性定理（`thm:integral-product-measure-exists`）：截面积分在两种次序下各定义一个测度，均满足矩形规则；两者在矩形$\pi$系统上一致且可被有限测度矩形可数覆盖，由唯一性相等。随后定义乘积测度（`def:integral-product-measure`），说明矩形规则本身不是对所有集合的定义，也可经Carathéodory延拓得到同一测度。

3. 以两点乘三点的有限网格（例`ex:integral-finite-product`）按竖线与横线两种方式算出同一集合的乘积测度$12$，具体核对截面公式。

###### paragraph：完备化与截面

1. 借第二章不可测集的存在，构造$\{0\}\times N$：它是零测矩形的子集，属于完备化，但$x=0$处的截面不可测；由此说明完备化后截面性质只能在零测例外之外成立，并预告Fubini小节的“几乎每个截面”版本。

#### 3.5.2 Tonelli定理

1. 引入累次积分术语，陈述Tonelli定理（`thm:analysis-tonelli-fubini`）：$\sigma$有限测度空间上非负乘积可测函数的内层积分可测，整体积分等于两种次序的累次积分，允许同为无穷。证明按矩形示性函数、一般可测集示性函数（$\pi$–$\lambda$论证）、非负简单函数（线性性）、非负可测函数（单调收敛三次）推进。

2. 指出定理可用于判断乘积空间上非负函数是否可积：任选一种方便的次序计算。

###### paragraph：$\sigma$有限条件

1. 以$[0,1]$上Lebesgue测度与计数测度的乘积及对角线$D$为例：$D$可写成可测矩形的可数交并；两种次序分别得$1$与$0$，说明计数测度不$\sigma$有限导致唯一性论证失效。

###### paragraph：非负双重级数

1. 两侧取自然数上的计数测度，Tonelli定理即非负双重级数可任意换序；以$a_{i,j}=2^{-i}\mathbf 1\{j\le i\}$换序算出$\sum_ii2^{-i}=2$。

2. 一侧取计数测度时得到非负函数项级数逐项积分，回接3.4节；强调两者都是非负质量的累计，尚不需要绝对可积性。

#### 3.5.3 Fubini定理

1. 说明可正可负时两种次序可能以不同方式抵消，先用Tonelli控制绝对值。陈述并证明Fubini定理（`thm:integral-fubini`）：绝对可积时截面几乎处处可积，例外集上内层积分取零后可积；对正部、负部分别用Tonelli后相减，复值对实部与虚部处理。

2. 给出使用顺序：先对$|f|$任选一种次序计算非负累次积分，有限后才可对$f$换序；只算出两个累次积分不构成检查。

###### paragraph：完备化后的截面

1. 对完备的$\mu,\nu$及乘积测度的完备化，由完备化定义使关于完备化可测的$f$与某个乘积可测$g$只在乘积可测零测集$M$内不同，对$\mathbf 1_M$用Tonelli得几乎每个截面零测，$\nu$完备保证截面可测；由此Tonelli与Fubini定理对完备化成立，截面结论改为几乎每个坐标成立，3.5.1的例子说明不能去掉“几乎”。

###### paragraph：缺少绝对可积时的反例

1. 用无穷矩阵$a_{i,j}=\mathbf 1\{j=i\}-\mathbf 1\{j=i+1\}$算出行和全为$0$、列和依次为$1,0,\ldots$，两种累次和为$0$与$1$；借`fig:integral-fubini-counterexample`解释逐行与逐列的配对方式不同，绝对和无穷。

2. 在$(0,1)^2$上对$f=(x^2-y^2)/(x^2+y^2)^2$用原函数$y/(x^2+y^2)$算出两种次序为$\pi/4$与$-\pi/4$；用$\int_0^1|f|\,\mathrm dy\ge1/(2x)$和Tonelli证明绝对积分发散，再以极坐标$|f|=|\cos2\theta|/r^2$解释原点附近正负部各自无穷。

#### 3.5.4 多重积分与截面计算

###### paragraph：有限乘积与Lebesgue测度

1. 说明有限乘积可逐次组成，三重矩形生成同一$\sigma$代数并由唯一性得到与括号无关的乘积测度，多重积分可在非负或绝对可积条件下按任意坐标次序逐次计算；无限乘积与随机过程分布留给概率与过程部分。

2. 证明`thm:integral-lebesgue-product`：$\mathcal B(\mathbb R^p)\otimes\mathcal B(\mathbb R^q)=\mathcal B(\mathbb R^{p+q})$（开集是有理开盒可数并；投影连续），且$\lambda_{p+q}$与$\lambda_p\otimes\lambda_q$在半开盒$\pi$系统上一致，由唯一性在Borel集上相等。

3. 说明Lebesgue可测结构是其完备化，需用“几乎每个截面”版本；跨卷说明卷一多元积分中连续函数在长方体、简单区域上的累次积分是Fubini定理的特例。

###### paragraph：区域积分与切片

1. 用$f\mathbf 1_E$定义区域积分，内层积分范围即截面$E_x$，换序须按另一方向重读截面。

2. 例`ex:integral-order-swap`：三角形上的$\int_0^1\int_x^1e^{y^2}\,\mathrm dy\,\mathrm dx$按非负性换序为$\int_0^1ye^{y^2}\,\mathrm dy=(e-1)/2$，说明换序产生的截面长度因子使外层可求原函数。

###### paragraph：层饼公式

1. 对$\sigma$有限空间上的非负可测$f$，用有理数把图像下区域$\Gamma$写成可数个可测矩形之并，证明层饼公式$\int f\,\mathrm d\mu=\int_0^\infty\mu\{f>t\}\,\mathrm dt$（`thm:integral-layer-cake`）：竖截面长$f(x)$，横截面为超水平集。

2. 以$f=e^{-x}$核对两侧均为$1$，借`fig:integral-layer-cake`对照两种切法，说明右侧只需各高度以上集合的大小，与3.1节按取值分层的思路一致。

### 3.6 积分换元

正文：`tex/02-abstract-mathematics/01-metric-and-measure/03-integration/06-change-of-variables.tex`（`sec:integral-change-of-variables`）

1. 区分累次积分（保留坐标、改变次序）与换元（经映射搬到另一个空间）；按映射条件逐层具体化：一般可测映射用推前测度，可逆光滑变换用Jacobian行列式，分支可逆变换逐支累计；强调这是两个空间之间的变量替换，与第四章同一空间上的换测度不同。

#### 3.6.1 可测映射下的换元

1. 回用推前测度定义，先对示性函数核对$\mathbf 1_B\circ T=\mathbf 1_{T^{-1}(B)}$；陈述并证明推前测度换元（`thm:integral-pushforward-change`）：非负可测$h$经简单函数与单调收敛得到$\int h\,\mathrm d(T_\#\mu)=\int h\circ T\,\mathrm d\mu$；实值、复值时对$|h|$用非负结论得可积性等价，再按正负部或实虚部处理。

2. 强调定理不要求可逆、可微或距离。以四点质量$k/10$、映射到两点的例子（`ex:integral-pushforward-finite`）两侧都算出$3.8$，借`fig:integral-pushforward-change`说明多对一映射如何把质量汇到同一输出点，且不预设输出密度；最后由推前的复合规则说明换元可逐级使用。

#### 3.6.2 可逆光滑变换下的换元

1. 说明对$\lambda_d$推前时还需识别输出测度的形式，局部线性化给出体积比例。

###### paragraph：Jacobian换元公式

1. 定义$C^1$微分同胚，由$DT^{-1}(T(\bm x))DT(\bm x)=\bm I$得Jacobian行列式处处非零；回顾卷一紧Jordan区域上连续函数的经典换元公式。

2. 陈述并证明`thm:integral-jacobian-change`：构造$\rho(B)=\int_U\mathbf 1_B\circ T\,|\det DT|$并证明是测度；对含于$V$的闭盒，原像是紧Jordan区域，用经典公式得$\rho=\lambda_d$；闭盒构成生成Borel结构的$\pi$系统，由唯一性推广到Borel集，再经简单函数与单调收敛推广到非负Borel函数；最后用完备化及“零测集原像零测”推广到Lebesgue可测函数，可积情形对$|h|$与分量处理。

3. 说明$C^1$条件提供局部体积比例、双射条件保证单次覆盖，重叠留给下一小节。

###### paragraph：线性变换与体积比例

1. 对仿射变换取$h=\mathbf 1_{T(E)}$得$\lambda_d(\bm AE+\bm b)=|\det\bm A|\lambda_d(E)$，以`fig:integral-jacobian-cell`中面积$1.25$的平行四边形说明行列式绝对值是固定体积比例、平移比例为一，并回到一般微分同胚的局部比例。

2. 例`ex:integral-polar-gauss`：极坐标去掉零测射线后是微分同胚，$\det DT=r$，算出$\int e^{-(x^2+y^2)}=\pi$并由Tonelli得$\int e^{-x^2}=\sqrt\pi$。

3. 说明Jacobian公式是在通用推前换元中进一步识别体积变化；不可逆或降维映射不满足条件，曲面测度与余面积公式留给几何内容。

#### 3.6.3 分支可逆变换下的换元

1. 以$x^2$为例说明整体不可逆但可分段可逆；陈述并证明`thm:integral-branch-change`：去掉零测集后输入域分为可数个不交开分支，零测集不影响积分，非负级数逐项积分，再对每支用逆映射$T_k^{-1}$的Jacobian换元；可积情形对$|f|$得绝对收敛。

2. 说明输出分支可以重叠，代入$f=h\circ T$可见每个输出点的权重是所有原像分支体积比例之和，只选一个逆分支会漏掉质量；未纳入分支的正测度部分须另行计算；单个微分同胚无需这两项检查。

3. 例`ex:integral-square-branches`：$T(x)=x^2$在$(-1,1)$上两个逆分支$\pm\sqrt y$，导数绝对值均为$1/(2\sqrt y)$，得$\int_{-1}^1f=\int_0^1[f(\sqrt y)+f(-\sqrt y)]/(2\sqrt y)\,\mathrm dy$；取$f=1$两侧为$2$、取$f=x^2$两侧为$2/3$，只用一支只得$1$；原点放入零测例外。配图`fig:integral-branch-inverse`。第四章再用同一变换计算输出密度。

### 3.7 含参积分

正文：`tex/02-abstract-mathematics/01-metric-and-measure/03-integration/07-parametric-integrals.tex`（`sec:integral-parametric`）

1. 定义含参积分$F(t)=\int_Xf(t,x)\,\mathrm d\mu(x)$：测度与区域固定，每个截面$f(t,\cdot)$可测，参数变化体现在被积函数上；提出连续性与可微性问题，说明答案来自控制收敛定理，关键是一族参数上的统一可积控制。

#### 3.7.1 积分关于参数的连续性

1. 指出逐点连续看不到质量向无穷远或集中的变化。陈述并证明`thm:integral-parametric-continuity`：在$t_0$处几乎处处连续、在邻域内每个参数被同一可积函数几乎处处控制时，沿任意$t_n\to t_0$合并可数个例外集后用控制收敛，再用序列判据得连续。说明控制条件的例外集可随参数变化，而连续性的例外集固定。

2. 例`ex:integral-parametric-local`：$\int_0^\infty e^{-tx}\,\mathrm dx=1/t$在$(0,\infty)$上无统一控制，但每个$t_0$在$(t_0/2,\infty)$上有可积包络$e^{-t_0x/2}$，故处处连续；局部控制已足够。

###### paragraph：控制失效的情形

1. 以$f(t,x)=te^{-tx}$、$f(0,x)=0$说明$F(t)=1$（$t>0$）而$F(0)=0$；用一半质量位于$x\ge(\ln2)/t$说明质量逃向无穷，配图`fig:integral-parameter-continuity`。

2. 计算上包络$\sup_{0<t<\delta}te^{-tx}=1/(ex)$在无穷远处不可积，说明$t=0$的任何邻域都没有可积控制，结论只适用于已核对条件的范围。

#### 3.7.2 积分号下求导

1. 把$F'(t)$写成差商积分的极限，说明这是又一次极限交换；对实值函数用中值定理把差商控制归结为偏导数控制。陈述并证明`thm:integral-differentiate-under-integral`：在开区间上对几乎所有$x$可微且偏导被同一可积函数控制、某个基准参数处可积；先由中值定理得各参数处可积，再由可测差商的逐点极限得到偏导的可测性（在共同零测集上取零），用控制收敛与序列判据得导数公式。

2. 说明共同零测集与控制函数不能随参数改变（参数不可数），复值函数按实虚部处理，条件只是充分条件。

3. 例`ex:integral-differentiate-exponential`：在$(t_0/2,3t_0/2)$上以$xe^{-t_0x/2}$控制，得$\int_0^\infty xe^{-tx}\,\mathrm dx=1/t^2$；逐阶重新核对$x^{k+1}e^{-t_0x/2}$的控制，得到$\int_0^\infty x^ke^{-tx}\,\mathrm dx=k!/t^{k+1}$，强调高阶导数须按阶检查。

###### paragraph：偏导存在不等于可以交换

1. 以$f(t,x)=tx/(x^2+t^2)$说明$t=0$处右偏导$1/x$处处存在但不可积，直接积分得$F(t)/t=\frac12\ln(1+t^{-2})\to\infty$，$F$无有限右导数；差商在$x=t$处峰值$1/(2t)$无界，找不到统一控制。

### 3.8 积分与微分

正文：`tex/02-abstract-mathematics/01-metric-and-measure/03-integration/08-integration-and-differentiation.tex`（`sec:integral-differentiation`）

1. 回顾卷一连续情形下微积分基本定理的两个方向，提出在可积被积函数与几乎处处导数下重新回答：积分函数的导数是否回到原函数，哪些函数能由导数恢复；以Cantor函数说明连续加几乎处处可导不够。预告依次建立绝对连续、有界变差与几乎处处可导、积分函数求导、恢复公式和Cantor边界，全部只用一元区间论证，不用第四章相对密度。

#### 3.8.1 绝对连续函数

###### paragraph：从单个区间到多个区间

1. 比较一致连续对单个短区间的控制与多个不交短区间上总增量的控制，定义绝对连续函数（`def:integral-absolutely-continuous-function`），说明取一个区间即得一致连续，区间个数不受限制。

2. 借`fig:integral-absolute-continuity-intervals`中$\sqrt x$上总长$1.2$的四段区间与总增量约$0.562$，说明绝对连续要求总长趋零时总增量一致趋零。

###### paragraph：基本例子与性质

1. 证明Lipschitz函数（含闭区间上连续可导函数）绝对连续，有限线性组合保持绝对连续；指出$\sqrt x$绝对连续而非Lipschitz，留到3.8.3验证。

2. 区分函数的绝对连续与第二章测度的绝对连续，二者联系留到第四章。

#### 3.8.2 有界变差与几乎处处可导

###### paragraph：全变差

1. 定义全变差与有界变差函数（`def:integral-bounded-variation`），区分函数的全变差与总变差测度；说明单调函数的全变差等于端点增量，并由插入分点证明全变差对区间可加。

2. 证明绝对连续函数有界变差（`lem:integral-ac-bv`）：对$\varepsilon=1$取$\delta$，把区间等分为长度小于$\delta$的$K$段，每段变差不超过$1$。

3. 以$x\sin(1/x)$在点$1/((k+\frac12)\pi)$处的交错取值说明一致连续不推出有界变差，因而也不绝对连续。

4. 定义变差函数$V$，由$V(y)-V(x)\ge|F(y)-F(x)|$得$V$与$V-F$单调不减，$F=V-(V-F)$；全程只用函数，不构造测度。

###### paragraph：单调函数的可导性

1. 定义Vitali覆盖，陈述并证明Vitali覆盖引理（`lem:integral-vitali`）：在有限测度开集内逐次选取长度超过剩余上确界一半的不交区间，长度总和有限；截取有限项后，未覆盖点都落在尾部区间的五倍放大中，借`fig:integral-vitali-cover`说明放大论证。

2. 引入四个Dini导数。陈述`thm:integral-monotone-differentiable`：单调不减函数几乎处处有有限导数，导数可积且积分不超过端点增量。证明的第一部分作为补充阅读，对有理数$u<v$两次使用Vitali引理得到$v s\le u s$从而$\{D_-F<u<v<D^+F\}$零测，再用反射$-F(-x)$得到四个Dini导数几乎处处相等。

3. 证明第二部分：令$q_n=n(F(x+1/n)-F(x))$，由Fatou引理与平移不变性得$\int_a^bF'\le F(b)-F(a)$，从而导数几乎处处有限。由两单调函数之差推出有界变差函数、进而绝对连续函数几乎处处可导且导数可积。

###### paragraph：还没有得到的结论

1. 以阶跃函数$\mathbf 1_{[1/2,1]}$说明不等式可以严格，导数读不到跳跃；强调有界变差与导数可积只给出存在与上界，恢复公式必须用绝对连续性，不能预先引用待证定理。

#### 3.8.3 积分函数的绝对连续性与导数

1. 对可积$g$定义$G(x)=\int_a^xg$，提出证明$G$绝对连续且$G'=g$几乎处处。

###### paragraph：积分函数绝对连续

1. 证明积分的绝对连续性（`lem:integral-small-sets`）：把$|g|$分为截断$\min(|g|,n)$与由单调收敛控制的小尾部，取$\delta=\varepsilon/(2n)$。

2. 把不交区间的增量和控制为$|g|$在区间并上的积分，得到$G$绝对连续；以$g=1/(2\sqrt t)$得$G=\sqrt x$，验证$\sqrt x$绝对连续。

###### paragraph：Lebesgue微分定理

1. 说明卷一结论只在连续点成立，以有理数示性函数说明“几乎处处”是准确答案。

2. 证明区间积分全为零的函数几乎处处为零（`lem:integral-vanishing-intervals`）：积分为零的Borel集构成包含半开区间$\pi$系统的$\lambda$系统，由$\pi$–$\lambda$定理推广到全部Borel集，再取$\{g>0\}$与$\{g<0\}$。

3. 陈述并证明Lebesgue微分定理（`thm:integral-lebesgue-differentiation`）：有界非负时用有界差商的控制收敛与平移得$\int_a^c(G'-g)=0$，再用上一引理；一般非负时用截断$g_n$得$G'\ge g$，再与单调函数的积分上界比较得等号；最后改写为局部平均恢复函数值。

4. 说明常见的最大函数弱型估计证法，本节改用单调可导性与区间引理，均为一元区间论证，不依赖函数空间完备性与第四章相对密度定理。

#### 3.8.4 微积分基本定理

1. 对绝对连续$F$令$G=F(a)+\int_a^xF'$，由前两小节得$H=F-G$绝对连续且$H'=0$几乎处处，把恢复公式归结为零导数引理。

###### paragraph：零导数引理

1. 证明`lem:integral-zero-derivative`：在导数为零点取增量不超过$\varepsilon$倍长度的小闭区间组成Vitali覆盖，选出有限个不交区间使间隙总长小于$\delta$；端点增量分为选中区间（导数控制）与间隙（绝对连续控制），得$|H(c)-H(a)|\le\varepsilon(c-a+1)$。

###### paragraph：恢复公式与双向刻画

1. 陈述并证明Lebesgue微积分基本定理（`thm:integral-ftc`）：绝对连续与“可积函数的不定积分加常数”等价，且$F'=g$几乎处处、$F(x)-F(a)=\int_a^xF'$；证明不使用Radon–Nikodym定理。

2. 说明连续可导与Lipschitz函数（如$|x|$）都包含在内。

###### paragraph：分部积分

1. 证明绝对连续函数的分部积分（`thm:integral-integration-by-parts`）：由有界性得乘积绝对连续，几乎处处用乘积求导，再用恢复公式移项；以$F=\sqrt x$、$G=x$在$[0,1]$上两侧均为$1/3$核对无界导数情形。

#### 3.8.5 Cantor函数与恢复公式的边界

1. 回用2.8节已构造的Cantor函数$c$，只列出所需性质：连续单调、删去区间上为常值、第$n$步$2^n$个长$3^{-n}$的保留区间各增$2^{-n}$；借`fig:integral-cantor-function`展示$c_1,c_2,c_6$与第二步四个保留区间。

###### paragraph：导数读不到的增量

1. 由Cantor集零测得$c'=0$几乎处处，$\int_0^1c'=0\ne1$，恢复公式失败，故$c$不绝对连续；再由保留区间总长$(2/3)^n\to0$而增量和恒为$1$直接验证绝对连续条件对$\varepsilon=1$失败。

###### paragraph：几种性质的比较

1. 总结$\text{Lipschitz}\Rightarrow$绝对连续$\Rightarrow$连续且有界变差$\Rightarrow$几乎处处可导，三个箭头的反例依次为$\sqrt x$、Cantor函数与阶跃函数；另以$x\sin(1/x)$说明一致连续不推出有界变差。

2. 指出Cantor函数中导数读不到的增量对应第二章的奇异连续质量，有界变差函数的增量可分为导数积分、跳跃与奇异连续三部分，第四章用相对密度重新解释。

### 3.9 本章小结

正文：`tex/02-abstract-mathematics/01-metric-and-measure/03-integration/09-summary.tex`（`sec:integral-summary`）

1. 回看积分的构造：简单函数分块累计、非负函数的上确界定义与二进制分层、正负部与实虚部分解及绝对可积条件、有符号测度沿Jordan分解积分；强调构造不需要密度；再提单调收敛传递运算规则及离散求和、Riemann积分、反常积分作为特例（3.1–3.3）。

2. 按运算归纳交换条件：非负递增支持递增累计，共同可积控制支持极限交换，绝对可积支持换序；换元按可测映射、微分同胚、分支逐层具体化；含参积分需参数点附近的统一控制。用表`tab:integral-summary-conditions`列出运算、条件、依据与反例（3.4–3.7）。

3. 收束积分与微分：不定积分绝对连续且几乎处处导数为原函数，绝对连续函数恰为导数的不定积分加常数；区分导数可积与能由导数恢复，以阶跃函数和Cantor函数为界（3.8）。

4. 引向第四章：给定两个测度，能否找到函数使其相对参考测度的积分恢复目标测度；本章的积分定义、单调收敛与基本运算为密度的存在、计算与换测度提供依据。

## 第4章 密度与换测度

正文入口：[04-densities-and-change-of-measure.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/04-densities-and-change-of-measure.tex)。

本章在第2章的测度关系、分解与Hahn分解和第3章的积分已经可用时，研究能否用逐点权重把参考测度换算成目标测度，密度何时存在、怎样计算并用于转换积分。

1. 从同一空间上同时出现两种测度的情形（骰子的计数参考与概率参考、实轴误差的长度参考）进入，回顾第2章的绝对连续与Lebesgue分解只涉及集合质量，提出能否用一个逐点权重函数完成换算的问题。

2. 说明第3章的积分使问题有准确说法，给出密度的直观表述，列出本章三个问题（是什么、何时存在、怎样计算与使用）和学习目标：判断存在性、在σ有限条件下证明存在与唯一、换测度、对三类测度写出密度。

3. 按节交代路线：4.1由质量之比定义密度、正向构造与几乎处处版本；4.2证明Radon–Nikodym定理并接到Lebesgue分解与有符号测度；4.3换测度、线性组合、链式规则与倒数；4.4离散测度、增量测度与推前测度；积分理论直接引用第3章。

### 4.1 相对密度

正文：[01-relative-density.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/04-densities-and-change-of-measure/01-relative-density.tex)

1. 说明本节固定参考测度与目标测度，从有限点集上的质量之比进入，再用积分推广；随后讲加权构造与几乎处处版本。

#### 4.1.1 参考测度与密度的定义

###### paragraph：有限点集上的质量之比

1. 在$\{a,b,c\}$上取目标质量$(0.2,0.5,0.3)$，参考为计数测度时乘数即目标质量，参考改为$(2,1,1)$时点$a$的乘数变为$0.1$；一般乘数为$p_i/m_i$，并核对$\nu(\{a,b\})=0.7$。

2. 结合图`fig:density-mass-ratio`指出目标测度不变而参考改变时密度随之改变，密度是相对于参考的换算比例。

###### paragraph：一般测度上的密度

1. 说明长度测度下单点质量为零，逐点相除成为$0/0$；保留“每个集合上参考质量乘权重累计得到目标质量”，累计用第3章积分完成。给出定义`def:density-density`（式`eq:density-definition`），引入相对密度、Radon–Nikodym密度与参考测度。

2. 说明定义中的“一个”密度及记号$\mathrm d\nu/\mathrm d\mu$指任一版本，等式理解为几乎处处；记号不是对坐标求导。

###### paragraph：概率质量函数与概率密度函数

1. 把卷一的概率质量函数解释为相对于计数测度的密度（对计数测度积分即求和），概率密度函数解释为相对于Lebesgue测度的密度。

2. 指出一般密度总积分等于$\nu(X)$而不必为一（例$2\lambda|_{[0,1]}$），概率密度在一点的值可大于一，因其不是单点概率。

#### 4.1.2 由密度构造测度

1. 提出反向问题：任给参考测度与非负权重，积分是否总产生测度；陈述定理`thm:density-weighted-measure`，用积分有限可加性与单调收敛证明可数可加，并由零测集上积分为零得$\nu_h\ll\mu$。

2. 说明正向构造不要求任何有限性，$\nu_h$甚至可以不σ有限；凡有密度的测度都绝对连续。

###### paragraph：分块加权

1. 对简单函数密度写出$\nu_h(E)=\sum_ic_i\mu(E\cap A_i)$，以$[0,1]$上$h=\tfrac32\mathbf 1_{[0,1/2)}+\tfrac12\mathbf 1_{[1/2,1]}$计算总质量$1$与$\nu_h([1/4,3/4])=1/2$，配图`fig:density-weighted-measure`(a)。

###### paragraph：两个方向

1. 区分“给定权重产生测度”（已解决）与“给定两个测度寻找权重”（$\nu\ll\mu$为必要条件，充分性留给4.2）。

#### 4.1.3 密度的几乎处处版本

###### paragraph：改动零测集不改变测度

1. 由几乎处处相等的非负函数积分相同，推出它们产生同一测度；以$h=1$与$g=1+\mathbf 1_{\mathbb Q\cap[0,1]}$为例，配图`fig:density-weighted-measure`(b)。

2. 说明密度的版本观念：关于密度的逐点断言只在几乎处处意义下成立。

###### paragraph：正向结论与唯一性

1. 区分正向结论与唯一性，用$\mu(\{0\})=+\infty$的单点空间说明常数$1$与$2$产生同一测度，唯一性需要有限性条件，留待4.2在σ有限下证明。

### 4.2 密度的存在性

正文：[02-existence.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/04-densities-and-change-of-measure/02-existence.tex)

1. 说明本节证明σ有限时绝对连续也是充分条件，并接到Lebesgue分解和有符号测度。

#### 4.2.1 Radon–Nikodym定理

1. 指出绝对连续只是零测集条件，反求权重需同时满足所有集合上的等式；陈述定理`thm:density-radon-nikodym`（σ有限、$\nu\ll\mu$，存在有限值密度且几乎处处唯一），与定理`thm:density-weighted-measure`对照得出σ有限范围内“有密度”等价于“绝对连续”。

###### paragraph：有限情形：候选权重取最大

1. 说明在所有“不超过$\nu$”的权重中取最大者的思路，陈述引理`lem:density-rn-finite`。

2. 证明第一步：候选集合对取最大值封闭（按$\{g_1\ge g_2\}$分割集合）。

3. 证明第二步：上确界$s\le\nu(X)<\infty$，取逐次最大值得到递增候选列，由单调收敛得极限候选达到上确界，并把取$+\infty$的零测集改为$0$。

4. 证明第三步：剩余测度$r$为有限且$r\ll\mu$；反设$r(X)>0$，取$\varepsilon=r(X)/(2\mu(X))$，对有限有符号测度$r-\varepsilon\mu$用Hahn分解得正集$P$，证明$\mu(P)>0$且$h+\varepsilon\mathbf 1_P$仍是候选，与上确界矛盾。

5. 用图`fig:density-rn-candidate`（事后已知密度$f=1.2+0.6\sin 2\pi x$、候选$\min(f,1)$、$\varepsilon=0.25$）解释剩余质量与加高步骤。

###### paragraph：$\sigma$有限情形与唯一性

1. 指出有限情形在何处用到$\nu(X)<\infty$与$\mu(X)<\infty$；把空间切成两测度都有限的可数块$A_i\cap B_j$，在各块用引理并以单调收敛拼接，核对对限制测度的积分等于乘示性函数后的积分。

2. 唯一性：在有限块上两密度可积，比较$\{h>g\}$上的积分得其为零测集，可数并后得几乎处处唯一。说明证明只用测度运算、Hahn分解、积分基本性质和单调收敛，并读出“密度是不超过$\nu$的最大权重”的刻画。

#### 4.2.2 密度表示与测度分解

1. 回用定理`thm:measure-lebesgue-decomposition`，陈述并证明推论`thm:density-lebesgue-form`：$\nu(A)=\int_Ah\,\mathrm d\mu+\nu_{\mathrm s}(A)$，两项唯一，且有密度当且仅当奇异部分为零。

2. 说明两个定理的分工：分解只用测度分开可见与不可见质量，Radon–Nikodym为前者找权重；奇异部分集中在零测集上，任何密度都表示不了。

###### paragraph：实轴上的三种质量

1. 以$\nu=\tfrac12\lambda|_{[0,1]}+\tfrac14\delta_{1/2}+\tfrac14\mu_C$为例写出密度形式，配图`fig:density-lebesgue-form`。

2. 说明整体有Lebesgue密度当且仅当点质量与奇异连续部分都为零；累计函数连续只排除点质量，Cantor函数连续却无密度，判断应检查绝对连续性，并预告4.4.2从函数一侧回到这一点。

###### paragraph：有限性条件不能随意去掉

1. 在$[0,1]$上以计数测度$c$为参考：$\lambda\ll c$，但单点比较迫使密度处处为零，与$\lambda([0,1])=1$矛盾；指出失败原因是$c$不σ有限，而Lebesgue分解对$\lambda$照常成立，失败的只是找函数这一步。配图`fig:density-counting-counterexample`。

2. 用$\delta_0$相对于$c$有密度$\mathbf 1_{\{0\}}$说明σ有限只是充分条件，不是必要条件。

#### 4.2.3 有符号测度的密度

1. 陈述并证明定理`thm:density-signed`：μ σ有限、η有限有符号时，$|\eta|\ll\mu$当且仅当存在可积实值密度；必要性对Jordan两部分分别用Radon–Nikodym定理再相减，充分性以$\{h\ge0\},\{h<0\}$为Hahn分解得到$\eta^\pm=\int h^\pm$与$|\eta|=\int|h|$；唯一性由可积性直接得到。

2. 说明集合层面的正负分解对应函数的正负部分，有限总变差且绝对连续对应密度绝对可积。

###### paragraph：抵消与总变差

1. 以$h(x)=1-2x$为例计算$\eta([0,1])=0$、$\eta^\pm([0,1])=1/4$、$|\eta|([0,1])=1/2$，说明总变差记录被抵消的变化，预告用于增量测度。

### 4.3 密度的运算规则

正文：[03-rules.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/04-densities-and-change-of-measure/03-rules.tex)

1. 说明本节建立换参考测度的各项规则，并注明测度关系和几乎处处范围。

#### 4.3.1 换测度公式

1. 指出密度定义只对示性函数成立，沿积分构造路线推广；陈述并证明定理`thm:density-change-of-measure`：示性函数、非负简单函数、单调逼近，再对$|f|$得到可积性等价，实值与复值情形分别处理。

2. 以密度$2x$下$\int x\,\mathrm d\nu=2/3$为例，引入换测度公式一词，指出它就是用概率密度计算期望，且不需要有限性条件。

###### paragraph：与推前换元的区别

1. 对照定理`thm:integral-pushforward-change`：推前改变空间并复合被积函数，换测度留在同一空间只乘权重；二者可接连使用，预告4.4.3。

#### 4.3.2 密度的线性组合

###### paragraph：共同参考测度下的加法

1. 由积分线性性证明非负组合的密度是密度的同系数组合，强调必须相对于同一参考测度。

###### paragraph：差与有限性

1. 有限测度之差用可积密度相减，与定理`thm:density-signed`一致；以$\nu_1=\nu_2=\lambda$在$\mathbb R$上说明无限测度相减出现$\infty-\infty$，不能形式相减。

###### paragraph：混合测度的统一表示

1. 取$\mu=\lambda|_{[0,1]}+\delta_0$，核对$\mathbf 1_{(0,1]}$与$\mathbf 1_{\{0\}}$分别是两分量的密度，得$a\lambda|_{[0,1]}+b\delta_0$的密度与总质量$a+b$；$b>0$时无Lebesgue密度却可在共同参考下统一表示。配图`fig:density-mixed-reference`（$a=3/4,b=1/4$）。

2. 指出原点处的密度值有意义，因为它在$\mu$下有正质量；取值是否有意义取决于参考测度。

#### 4.3.3 密度的链式规则

1. 为避免记号冲突用$\rho$表示底层参考；陈述并证明定理`thm:density-chain-rule`：两次换测度得$gk$是密度，再由唯一性得$\rho$-几乎处处等式。

2. 引入“密度的链式规则”一词，说明依据是质量换算而非坐标求导；以$2x\cdot\tfrac32x=3x^2$为例核对总质量，配图`fig:density-chain-rule`。

###### paragraph：版本的选择

1. 证明$\mathrm d\nu/\mathrm d\mu$的不同版本只在$\mu$零测集$M$上不同，而$k$在$M$上$\rho$-几乎处处为零，故乘积不受版本影响。

#### 4.3.4 等价测度与密度的倒数

1. 陈述并证明推论`thm:density-inverse`：等价σ有限测度下$0<h<\infty$几乎处处，由换测度公式直接验证$1/h$是反向密度；也可由链式规则读出。以密度$2x$与反向密度$1/(2x)$为例。

###### paragraph：单向绝对连续时的信息丢失

1. 以$\mu=\lambda|_{[0,2]}$、$\nu=\lambda|_{[0,1]}$说明$h$在$(1,2]$为零，$\nu$看不见这部分质量，反向密度不存在，倒数公式只限于等价测度。配图`fig:density-one-sided-loss`。

### 4.4 密度的计算与表示

正文：[04-computation.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/04-densities-and-change-of-measure/04-computation.tex)

1. 说明依次计算离散质量、增量质量与推前质量的密度，每例先定参考测度，再核对能否恢复集合质量。

#### 4.4.1 离散测度的密度

###### paragraph：逐点相除

1. 在可数集上写出两离散测度，说明σ有限；绝对连续当且仅当$m_i=0$蕴含$p_i=0$；在$m_i>0$处取$p_i/m_i$、$m_i=0$处任取，用加权求和核对恢复所有子集质量，回连4.1.1与4.1.3。

###### paragraph：同一分布换两种参考

1. 以Poisson(1)为目标、几何权重$2^{-(k+1)}$为参考算出$h(k)=2^{k+1}\mathrm e^{-1}/k!$及前几项数值，核对$\nu(\{0,1\})$，并用链式规则联系相对计数测度的密度。配图`fig:density-discrete`。

###### paragraph：总质量

1. 以几何参考下计数测度的密度$2^{k+1}$说明总质量可为无穷，只有概率测度才要求归一化。

#### 4.4.2 增量测度的密度

1. 说明把第3章的函数增量转成集合质量，再问何时有Lebesgue密度。

###### paragraph：由增量产生的有符号测度

1. 对写成两个右连续单调函数之差的$F$（右连续有界变差函数可如此分解，变差函数的右连续性引用Folland第3.5节），延拓后用Stieltjes构造定义增量测度$\eta_F$，满足$\eta_F((s,t])=F(t)-F(s)$；说明左开右闭与右连续的配合及$F(a)$单独记录。

2. 用Jordan分解把两个有限有符号测度化为两个有限测度，借π-λ定理证明区间上相等则全相等，从而$\eta_F$不依赖分解选择。

###### paragraph：绝对连续函数的增量测度

1. 陈述并证明定理`thm:density-increment`：$F$绝对连续时用微积分基本定理给出单调分解，并由区间唯一性得$\mathrm d\eta_F/\mathrm d\lambda=F'$；反之$|\eta_F|\ll\lambda$时由定理`thm:density-signed`得可积密度，$F$为不定积分因而绝对连续。

2. 说明函数的绝对连续与测度的绝对连续在增量测度上合一，恢复公式即“密度是导数”。

###### paragraph：一般情形：保留奇异增量

1. 对Jordan两部分作Lebesgue分解，写成可积密度积分加奇异增量。

2. 以$F=x/2+\tfrac14\mathbf 1_{[1/2,1]}+\tfrac14C$计算$\eta_F=\tfrac12\lambda+\tfrac14\delta_{1/2}+\tfrac14\mu_C$，$F'=1/2$几乎处处，导数积分$1/2$而总增量$1$，差额由跳跃与Cantor增长各$1/4$承担。配图`fig:density-increment`。

3. 指出连续、有界变差、几乎处处可导都不足以保证密度存在，必须绝对连续。

#### 4.4.3 推前测度的密度

1. 从随机变量变换的分布进入，说明调用第3章光滑换元公式计算输出密度，不重证Jacobian公式。

###### paragraph：可逆光滑变换

1. 陈述并证明定理`thm:density-pushforward`：对$T^{-1}$用定理`thm:integral-jacobian-change`，得$q(\bm y)=p(T^{-1}\bm y)|\det DT^{-1}(\bm y)|$。

2. 解释Jacobian因子为体积伸缩倍数；以$-\ln x$把均匀分布变成指数分布为例并核对总质量，给出仿射变换公式。

###### paragraph：分支相加

1. 在定义域分支两两不交、余部零测、各支为微分同胚的条件下，逐支计算并用单调收敛交换求和与积分，得到各分支贡献之和；强调像可重叠、须累加全部原像分支。

###### paragraph：平方变换

1. 以$[-1,1]$上均匀概率经$x^2$为例，两分支相加得$q(y)=1/(2\sqrt y)$，核对总质量$1$与$B=[0.36,0.49]$质量$0.1$，指出只取一支只得总质量$1/2$。

2. 说明$q$无界但可积，原点原像零测故无点质量；若输入在$0$处有点质量$\tfrac12$，输出相应出现点质量。配图`fig:density-square-branches`。

### 4.5 本章小结

正文：[05-summary.tex](../../tex/02-abstract-mathematics/01-metric-and-measure/04-densities-and-change-of-measure/05-summary.tex)

1. 回看主线：绝对连续只是零测集关系，Radon–Nikodym定理在σ有限下把它提升为几乎处处唯一的函数表示（候选取最大、Hahn分解排除残差）；正向加权无需有限性；换测度公式把表示用于积分；Lebesgue分解保留密度之外的奇异质量。

2. 汇总使用密度时须说明的三件事：参考测度（不同参考下密度不同、共同参考统一混合质量）、成立条件（σ有限及计数测度反例、有符号情形的绝对可积、倒数需等价）、几乎处处（链式规则与倒数均为几乎处处等式）。

3. 总结三种计算入口（离散逐点相除、增量测度密度即导数、推前密度含Jacobian并累加分支），并简短前瞻后续概率空间部分用子σ代数上的密度定义条件期望，以及概率分布比较从共同参考下的密度出发。

