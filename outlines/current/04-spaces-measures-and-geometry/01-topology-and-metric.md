# 卷4《函数空间与流形》：拓扑与度量大纲

所属：卷四《函数空间与流形》第一部分“拓扑与度量”（第1—4章）。卷入口：[volume.tex](../../../tex/04-spaces-measures-and-geometry/volume.tex)；部分入口：[part.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/part.tex)。以下按 `volume.tex → part.tex → 章 → 节 → 小节 → paragraph` 的实际层级记录当前正文；章号在卷内连续，本部分为第1—4章。目标结构依据[十卷计划的本部分细纲](../../../plans/ten-volume-migration/04-spaces-measures-and-geometry/01-topology-and-metric.md)。

## 部分主线与导读

部分主线：本部分建立邻近、距离与连续变形的语言。第1章只用开集与邻域规定“附近”，定义闭包、稠密、点列收敛、连续映射、同胚与子空间、乘积、商三种构造，再集中考察分离性、可数性、可分性、连通性和紧性；第2章加入距离，用点列刻画稠密与紧性，研究完备性、完备化与Baire纲定理，并以覆盖数、打包数和度量熵量化有限精度下的空间大小；第3章研究映射怎样传递距离与误差，包括连续性的距离判据、一致与Lipschitz连续、映射列的逐点与一致收敛、等度连续、空间比较、稠密集延拓与压缩迭代；第4章由三角形边界与填实三角形的区别出发，用同伦、单纯复形、链与边界建立同调，并推广到奇异同调、证明同伦不变性。拓扑性质只依赖开集，完备性和Lipschitz常数依赖所选距离；流形与点云问题留在第四部分。

部分导读（`\BookPartGuide`）的自然段：

1. 以卷一绝对值、卷二范数描述的接近为起点，说明函数、测度与流形需要先脱离具体公式重新规定“接近”；概述全卷四个部分的分工：本部分建立邻近、距离与连续变形的语言，第二部分测量集合并累计函数，第三部分把函数当作向量研究表示、观测与逼近，第四部分研究局部像欧氏空间、整体可能弯曲的空间。

2. 说明前三章的分工：第1章只用开集与邻域定义闭包、收敛、连续与空间构造，再考察分离性、可数性、连通性与紧性；第2章加入距离，用点列刻画稠密与紧性，研究完备性、Baire纲定理与覆盖数；第3章研究映射怎样传递距离与误差，包括一致收敛、等度连续、延拓与压缩迭代。

3. 说明第4章转向连续变形保留的信息：三角形边界与填实三角形拓扑不同，同调用链、边界及线性代数中的核与像把这种差异算成数，并在同伦下不变。

4. 提示阅读时区分只依赖开集、在同胚下保持的拓扑性质，与依赖所选距离、换成拓扑等价距离可能改变的完备性、有界性和Lipschitz常数；说明例子多取自实轴与欧氏空间，以便核对定义。

## 第1章 拓扑空间

正文入口：[01-topological-spaces.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces.tex)，章内依次输入[01-topology.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/01-topology.tex)、[02-subsets.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/02-subsets.tex)、[03-convergence.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/03-convergence.tex)、[04-continuous-maps.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/04-continuous-maps.tex)、[05-constructions.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/05-constructions.tex)、[06-properties.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/06-properties.tex)、[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/07-summary.tex)。

章职责与主线：本章把“附近”从距离中分离出来，以开集族为唯一基本数据建立拓扑空间。先由实轴开集的运算规则得到拓扑，并用拓扑基、邻域与邻域基描述全体开集和一点附近；再在固定拓扑下研究子集、点列收敛与连续映射；随后用子空间、有限乘积与商空间构造新空间；最后讨论Hausdorff分离性、可数性、可分性、连通性与紧性。全章不使用距离，距离带来的判据交给第2、3章。

1. 从实轴上收敛与连续的距离定义出发，说明这些定义里要用的是“附近”的区域。

2. 指出起作用的是$x$附近的一组区域，并说明圆周、曲面、函数集合与粘合空间往往没有唯一合适的距离。

3. 说明本章以开集族为基本数据，前四节依次处理拓扑、子集、点列与映射。

4. 说明1.5用“哪些映射应当连续”确定新开集，1.6集中讨论空间本身的四类性质。

5. 划定范围：距离判据属于第2、3章，乘积为第4章同伦准备定义域，空间性质是第24章定义流形的条件。

### 1.1 拓扑的定义

正文：[01-topology.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/01-topology.tex)

1. 说明谈论“附近”要规定哪些子集围住其中每一点，本节由实轴开集总结规则，再说明生成全部开集和只看一点周围的办法。

#### 1.1.1 开集

1. 以开区间每点留有余地、闭区间端点没有余地的对比，引出开集的要求。

###### paragraph：实轴上的开集

1. 回顾实轴开集的定义，并指出半径可随点改变。

2. 对$U=(0,1)\cup(2,3)$与$x=2.9$算出半径$r=0.1$，由逐点取半径确认$U$是开集。

3. 说明$[0,1)$在$0$处失败，引用卷一“极限与连续”，转而关心开集族的整体规则。

4. 陈述并证明引理`lem:topo-real-open-rules`：空集与全集开、任意并开、有限交开，有限交取各半径的最小值。

5. 用$\bigcap_n(-1/n,1/n)=\{0\}$说明“有限”不能去掉，失效处是半径的下确界为零。

###### paragraph：拓扑

1. 指出三条规则只涉及并与交，据此作为公理。

2. 定义`def:topo-topology`：对空集与全集、任意并、有限交封闭的子集族称为拓扑，成员称为开集。

3. 用“认可区域的清单”解释拓扑，并与向量空间定义只规定运算规则作类比。

4. 约定简称，说明有限交只需验证两个集合，引入$\mathbb R$的通常拓扑。

5. 引出有限集上的核对。配图`fig:topo-finite-topologies`在三点集上画两个拓扑和一个缺少并集的非拓扑。

6. 对嵌套族逐项核对并、交封闭，说明图(c)的族缺少$\{a,b\}$因而不是拓扑。

###### paragraph：同一集合上的不同拓扑

1. 指出同一集合可配不同拓扑，先看两个极端。

2. 例`ex:topo-discrete-indiscrete`给出离散拓扑、平凡拓扑，以及两点集上“附近”不对称的拓扑。

3. 由开集多少与区分能力的关系定义更细与更粗。

4. 说明离散最细、平凡最粗，两个拓扑也可能互不包含，并给出两点集上的例子。

#### 1.1.2 拓扑基

1. 由实轴每个开集都是开区间之并，说明开区间这一小类集合决定全部开集。

2. 与线性空间的基类比，并说明类比在取并没有系数、表示不唯一、成员无独立性处失效。

3. 定义`def:topo-basis`。

4. 给出逐点判据\eqref{eq:topo-basis-pointwise}，空集情形由零个成员的并处理。

5. 论证判据的必要性与充分性，并结合图(a)说明靠近边缘的点需要更小的基本开集。

###### paragraph：由一族集合生成拓扑

1. 提出先有简单集合、再生成拓扑时需要判断的问题。

2. 陈述并证明定理`thm:topo-basis-criterion`：覆盖与交中可放下基本开集是充要条件，证明逐项检验拓扑公理。

3. 结合图(b)解释条件2。配图`fig:topo-basis-criterion`展示逐点判据、条件2与方块圆盘的相互嵌套。

4. 用$\{\{a,b\},\{b,c\}\}$的反例说明条件2不能省略。

5. 例`ex:topo-intervals-rectangles`说明开区间、开矩形生成$\mathbb R$、$\mathbb R^n$的通常拓扑，并写出开矩形交的分解。

6. 说明开圆盘与开矩形生成同一拓扑，开集不取决于度量附近的形状。

#### 1.1.3 邻域

1. 用“在$1/2$附近取正值”说明邻域不必是开集，关键是包含围住该点的开集。

2. 定义`def:topo-neighborhood`。

3. 用$[0,1]$是$1/2$而非$0$的邻域，说明邻域不必开且相对于指定点。配图`fig:topo-neighborhoods`展示这一区别与邻域基的逐层缩小。

4. 引出邻域对开集的反向刻画，陈述并证明引理`lem:topo-open-iff-neighborhood`。

5. 指出实轴开集定义是该引理的特例，以及证明开集的常用办法。

#### 1.1.4 邻域基

1. 由判断实数列极限只需检验可数个区间，引出足以代表所有邻域的子族。

2. 定义`def:topo-neighborhood-basis`。

3. 证明$\{(x-1/k,x+1/k)\}$是$x$的邻域基。

4. 对$N=(x-0.4,x+0.6)$具体计算，$k=2$不够而$k=3$已含于$N$。

5. 说明闭区间族也是邻域基，成员不必开。

###### paragraph：邻域基与拓扑基的区别

1. 比较二者代表的对象，陈述并证明引理`lem:topo-basis-to-neighborhood-basis`的两个方向。

2. 以$\mathbb R$说明可数的邻域基比开区间基更经济，引出第一可数性。

### 1.2 空间中的子集

正文：[02-subsets.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/02-subsets.tex)

1. 列举子集与环境的几种关系，并强调这些判断都相对于给定拓扑。

#### 1.2.1 闭集

1. 由“集合外每点留有余地”引出定义`def:topo-closed-set`。

2. 由De Morgan律得到闭集的三条规则。

3. 用$\bigcup_n[1/n,1]=(0,1]$说明有限并的“有限”不能去掉。

###### paragraph：实轴上的区间

1. 逐一核对闭区间、开区间与半开区间的开闭性。

###### paragraph：开与闭不是互斥的两类

1. 说明开闭是两个独立条件，给出既开又闭与既不开又不闭的例子。

2. 指出“不开”不能推出“闭”，既开又闭的子集将用于判断连通。

#### 1.2.2 内部、闭包与边界

1. 按点与集合的关系分类。配图`fig:topo-interior-closure`展示内点、外部点和属于或不属于集合的边界点。

###### paragraph：内部

1. 定义内点与内部。

2. 说明内部是含于$A$的最大开集，$A$开当且仅当$\operatorname{int}A=A$。

###### paragraph：闭包

1. 由被$A$紧贴的点引出闭包。

2. 定义`def:topo-closure`。

3. 说明只需检验开邻域或邻域基，并给出$A\subseteq\overline A$。

4. 陈述并证明定理`thm:topo-closure-smallest-closed`：闭包等于包含$A$的所有闭集之交。

5. 由补集得到式\eqref{eq:topo-closure-interior-complement}。

###### paragraph：边界

1. 定义边界式\eqref{eq:topo-boundary}，给出每个邻域同时碰到$A$与补集的判据，并得到边界对补集对称。

2. 例`ex:topo-interior-closure-examples`计算$[0,1)$在三种拓扑下与$\mathbb Q$在通常拓扑下的内部、闭包与边界。

3. 表`tab:topo-three-topologies`并列三种拓扑下的结果，说明这些概念描述集合在拓扑中的位置。

4. 在三点集拓扑上列出全部闭集。

5. 对$A=\{b\}$算出内部、闭包与边界，并解释$c$为何在闭包中。

6. 指出距离判据留到第2章。

#### 1.2.3 稠密集

1. 用闭包语言重述有理数逼近实数，引出稠密。

2. 定义`def:topo-dense`。

3. 由闭包定义转为开集的说法。

4. 陈述并证明定理`thm:topo-dense-open-criterion`。

5. 例`ex:topo-rationals-irrationals-dense`证明有理数与无理数都稠密，并在$(0.3,0.31)$上算出$31/101$。

6. 说明稠密不要求占据大部分空间。

###### paragraph：为什么不用点列定义稠密

1. 指出一般空间中点列走不到闭包中的所有点，所以闭包与稠密以邻域定义。

### 1.3 点列收敛

正文：[03-convergence.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/03-convergence.tex)

1. 把$\varepsilon$-$N$定义改写成点列最终停在邻域基的每个区间中。

2. 对$x_n=(-1)^n/n$算出$\varepsilon=0.3$与$0.12$时的进入时刻$n=4$与$n=9$。配图`fig:topo-sequence-eventual`展示点列进入两条带。

3. 引出不需要距离的定义。

4. 定义`def:topo-sequence-convergence`。

5. 说明只需检验邻域基，通常拓扑下与卷一的极限一致。

###### paragraph：拓扑决定哪些点列收敛

1. 比较离散拓扑与平凡拓扑下的收敛。

2. 说明极限唯一性留到分离性讨论。

###### paragraph：子列与闭集

1. 指出两条基本性质只用到邻域，陈述并证明定理`thm:topo-subsequence-closure`。

###### paragraph：点列不能反推闭包

1. 提出逆命题在一般空间中不成立。

2. 例`ex:topo-cocountable`建立余可数拓扑，证明只有最终恒定的点列收敛，$0\in\overline A$却不是$A$中点列的极限。

3. 解释问题出在邻域数量。

4. 证明余可数拓扑在$0$处没有可数邻域基。

5. 指出第一可数性与度量空间的序列判据在后文处理。

### 1.4 连续映射

正文：[04-continuous-maps.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/04-continuous-maps.tex)

1. 由实函数连续的含义引入开集表达。

#### 1.4.1 连续性的定义

1. 把$\varepsilon$-$\delta$定义改写为开集的原像开。

2. 对$f(x)=x^2$算出$(1,4)$的原像，并取$x_0=3/2$核对$\delta=1/2$。

3. 对跳跃函数算出$(3/2,5/2)$的原像$[1,3/2)$，说明跳跃表现为原像不开。配图`fig:topo-preimage`并排展示两种情形。

4. 定义`def:topo-continuous-map`。

5. 说明定义用原像的原因是原像与集合运算相容，并得到只需检验拓扑基。

###### paragraph：等价判据

1. 引出逐点与闭集两种检验方式，陈述并证明定理`thm:topo-continuity-equivalent`。

2. 说明条件2在实轴上回到$\varepsilon$-$\delta$定义，常值映射连续。

3. 例`ex:topo-continuity-depends-topology`比较恒等映射在不同拓扑下的连续性。

###### paragraph：复合与点列

1. 证明连续映射的复合连续，陈述并证明定理`thm:topo-continuous-preserves-limits`。

2. 指出余可数拓扑上任何映射都保持极限。

3. 用余可数拓扑到通常拓扑的恒等映射说明保持极限不能反推连续。

###### paragraph：原像与像

1. 用$x^2$与$\arctan$说明连续映射的像不保持开闭性。

2. 用$A=\{-1\}$、$B=\{1\}$的计算说明像与交不相容。

#### 1.4.2 开映射

1. 提出把开集映成开集的问题。

2. 定义`def:topo-open-map`。

3. 说明只需对拓扑基检验。

4. 用常值映射和到离散拓扑的恒等映射说明连续与开互不蕴含。

5. 证明投影是开映射。

6. 用双曲线说明开映射不必把闭集映成闭集。配图`fig:topo-image-openness`展示三种像的开闭性。

#### 1.4.3 同胚

1. 与线性同构类比，由开集的一一对应引出同胚。

2. 定义`def:topo-homeomorphism`。

3. 说明同胚在开集族与邻域之间建立对应。

4. 陈述并证明定理`thm:topo-homeomorphism-open`。

5. 给出连续双射不是同胚的例子，并预告绕圆映射。

###### paragraph：同胚不保持长度

1. 用仿射映射与式\eqref{eq:topo-interval-line-homeomorphism}说明同胚可以改变长度与有界性。

2. 写出逆映射并验证，确认二者连续。

3. 计算$h(1/2)=1$、$h(3/4)=3$，说明距离可被任意放大。配图`fig:topo-homeomorphism`展示$h$的图像与沿射线的对应。

4. 定义拓扑性质。

5. 用公式给出圆周与正方形边界的同胚。

6. 对$(3/5,4/5)$往返计算，说明拓扑只记录首尾相接成一圈的结构。

### 1.5 空间的构造

正文：[05-constructions.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/05-constructions.tex)

1. 说明三种构造各有自然映射，新开集按使映射连续来规定。

#### 1.5.1 子空间

1. 由圆周上的“附近”引出子空间拓扑。

2. 定义`def:topo-subspace`。

3. 验证$\mathcal T_A$是拓扑。

4. 给出相对闭集与子空间的基。

###### paragraph：相对开与在环境中开

1. 用$[0,1/2)$在$[0,1]$中相对开、在$\mathbb R$中不开作对比，并说明$A$在自身中既开又闭。

2. 说明端点处的邻域只需单侧，$\{0\}$在$A$中仍不开。

3. 说明$A$开时两种开相同，描述开闭性须说明环境。

###### paragraph：映入子空间的映射

1. 说明包含映射连续且子空间拓扑是使其连续的最粗拓扑，限制仍连续。

2. 陈述并证明引理`lem:topo-map-into-subspace`。

3. 用$p(t)$说明映入圆周的连续性可逐坐标检验。

4. 例`ex:topo-interval-to-circle`证明$[0,1)\to S^1$是连续双射但不是同胚。

5. 解释失败原因是端点只有单侧邻域。配图`fig:topo-subspace-wrap`展示相对开集与绕圆映射。

#### 1.5.2 有限乘积

1. 由成对数据引出乘积上的开集。

2. 定义`def:topo-product`。

3. 验证基的条件。

4. 说明开集一般是开矩形之并，$\mathbb R^n$的通常拓扑是乘积拓扑，并给出乘积的基。

###### paragraph：投影与分量

1. 证明投影连续且开。

2. 说明乘积拓扑是使投影连续的最粗拓扑，陈述并证明定理`thm:topo-map-into-product`。

3. 说明逐坐标判据的适用范围，并用$x_1x_2/(x_1^2+x_2^2)$说明从乘积出发的映射不能逐分量判断。

###### paragraph：空间与区间的乘积

1. 把$X\times I$的点读作某时刻的位置，$H$记录一族映射。

2. 说明基本开集同时限制位置与时刻，$H_t$连续。配图`fig:topo-product-neighborhood`展示$U\times V$与$X\times I$中的基本开邻域。

3. 验证$H(x,t)=(1-t)f(x)+tg(x)$连续。

4. 引出同伦，指出$X\times I$是其定义域。

#### 1.5.3 商空间

1. 用纸条粘合提出商空间上开集的问题。

###### paragraph：等价类与投影

1. 用等价关系描述识别并引入投影$q$。

2. 定义`def:topo-quotient`。

3. 证明商拓扑是使$q$连续的最细拓扑。

4. 解释子空间、乘积取最粗而商空间取最细的原因在于新拓扑所在的一侧。

5. 说明商空间的开集对应由完整等价类组成的开集。

6. 例`ex:topo-interval-gluing-circle`说明端点粘合后粘合点的邻域由两端小段拼成。

7. 取$\varepsilon=0.1$算出两段绕出的角度范围。配图`fig:topo-quotient-circle`展示两段拼成粘合点的开邻域。

###### paragraph：从商空间出发的映射

1. 说明商空间上的映射由$X$上的映射下降得到，陈述并证明定理`thm:topo-quotient-maps`。

2. 应用定理得到连续双射$\bar p:I/{\sim}\to S^1$。

3. 指出还需紧性与分离性才能得到同胚，粘合也可能破坏分离性。

### 1.6 空间的性质

正文：[06-properties.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/06-properties.tex)

1. 概述四类性质各自回答的问题。

#### 1.6.1 分离性

1. 用$r=(y-x)/2$在实轴上分开两点并算一例，指出平凡拓扑的缺陷。

2. 定义`def:topo-hausdorff`。

3. 证明$\mathbb R^n$与乘积保持Hausdorff性质。

4. 证明子空间保持Hausdorff性质。

###### paragraph：极限的唯一性

1. 结合图(a)说明机制，陈述并证明定理`thm:topo-hausdorff-unique-limit`。

2. 说明定理只需要邻域不交。配图`fig:topo-separation`展示分离与有两个原点的直线。

###### paragraph：商空间是否仍可分离

1. 指出商空间需要逐个检查。

2. 分开两个内部点。

3. 分开内部点与粘合点，证明$I/{\sim}$是Hausdorff空间。

4. 例`ex:topo-line-two-origins`证明两个原点不能分开，点列同时收敛到两者。

5. 说明定义流形时要单独要求Hausdorff条件。

#### 1.6.2 可数性

1. 提出邻域族与开集族能否用可数个代表描述。

2. 定义`def:topo-countability`。

3. 比较逐点与整体的条件，得到第二可数蕴含第一可数。

4. 例`ex:topo-rational-intervals`用有理端点区间证明$\mathbb R$与$\mathbb R^n$第二可数，并以$\sqrt2\in(1.4,1.5)\subseteq(1,2)$为例。

5. 指出可数性约束开集族规模而非点数。

6. 用不可数离散空间说明第一可数不推出第二可数。

7. 证明第一可数时闭包点是点列的极限。

8. 指出余可数拓扑的失效原因、度量空间的情形和第二可数在流形中的作用。

#### 1.6.3 可分性

1. 引出用可数个点接近所有点的问题。

2. 定义`def:topo-separable`。

3. 说明$\mathbb R$与$\mathbb R^n$可分。

###### paragraph：可分性取决于拓扑

1. 比较同一集合在离散、通常、平凡拓扑下的可分性。

###### paragraph：三种可数要求的区别

1. 表`tab:topo-countability`比较三种可数性要求的对象。

2. 证明第二可数推出可分。

3. 构造Sorgenfrey直线，说明它可分且第一可数。

4. 证明Sorgenfrey直线不第二可数。

5. 指出度量空间中第二可数与可分等价，留到第2章证明。

#### 1.6.4 连通性

1. 用两种思路区分连通与路径连通。

##### 1.6.4.1 连通集

1. 说明$[0,1]\cup[2,3]$的两块相对开，引出连通。

2. 定义`def:topo-connected`。

3. 用既开又闭的子集刻画连通，并检查离散与平凡拓扑。

###### paragraph：实轴上的连通集

1. 给出区间的定义。

2. 陈述并证明定理`thm:topo-connected-intervals`，用上确界排除两种情形。

3. 配图`fig:topo-connected-sup`并列证明的三种情形。

4. 列举连通与不连通的例子，指出证明依赖确界原理。

###### paragraph：连续像与介值

1. 说明连续映射不能制造分解，陈述并证明定理`thm:topo-connected-image`。

2. 得到一般形式的介值定理与同胚不变性。

###### paragraph：连通分支

1. 提出最大连通块，陈述并证明引理`lem:topo-connected-union-closure`。

2. 定义连通分支。

3. 证明连通分支构成划分且是闭集。

4. 例`ex:topo-components`计算$(0,1)\cup(2,3)$与$\mathbb Q$的连通分支，说明分支不必开。

##### 1.6.4.2 路径连通性

1. 引出用曲线连接两点。

2. 定义`def:topo-path-connected`。

3. 说明线段给出凸集的路径连通性。

###### paragraph：路径分支

1. 验证等价关系，写出路径拼接式\eqref{eq:topo-path-concatenation}。

2. 用粘接引理证明拼接连续。

3. 定义路径分支。

###### paragraph：路径连通蕴含连通

1. 由路径的像连通且有公共点推出路径连通蕴含连通。

2. 指出反方向不成立。配图`fig:topo-sine-curve`画出拓扑学家的正弦曲线及其局部放大。

3. 例`ex:topo-topologist-sine`证明$S$连通，再用$t_0=\max T$与两个振荡点证明没有路径。

4. 用$k=1$的数值解释路径无法穿过无穷多次振荡。

###### paragraph：局部路径连通

1. 定义局部路径连通，说明$\mathbb R^n$的开子集满足它。

2. 陈述并证明定理`thm:topo-locally-path-connected`。

3. 说明$\mathbb R^n$的连通开集路径连通，正弦曲线不满足条件，流形满足条件。

#### 1.6.5 紧性

1. 由闭区间上的最大值问题引出有限子覆盖。

2. 把紧性解释为把局部信息化为有限个再汇总。

##### 1.6.5.1 紧性的定义

1. 定义开覆盖与有限子覆盖。

2. 定义`def:topo-compact`。

3. 说明紧集可直接用环境空间的开集检验。

###### paragraph：某一个覆盖与所有覆盖

1. 用覆盖$\{(1/n,1)\}$证明$(0,1)$不紧，$\mathbb R$同理。

2. 说明闭区间的端点使含$0$的成员一次盖住靠近$0$的所有点。

3. 用具体覆盖选出两个成员盖住$[0,1]$。配图`fig:topo-open-covers`对比两种情形。

4. 引用卷一闭区间紧性，引出有界闭集紧，陈述并证明引理`lem:topo-closed-in-compact`。

5. 列举有限集、无限离散空间与平凡拓扑的紧性。

6. 说明紧性以开覆盖定义的原因，序列判据留到第2章。

##### 1.6.5.2 相对紧集

1. 由$(0,1)$引出闭包紧的概念。

2. 定义`def:topo-relatively-compact`。

3. 给出例子，引出Hausdorff空间中紧集的闭性，陈述引理`lem:topo-compact-closed-hausdorff`。

4. 解释证明想法是用有限子覆盖把逐点分离汇总。配图`fig:topo-compact-closed`展示$m=3$的情形。

5. 给出引理的证明。

6. 由引理得到紧集相对紧，并用平凡拓扑说明Hausdorff条件不能去掉。

###### paragraph：相对紧依赖环境空间

1. 用$(0,1)$在自身与在$\mathbb R$中的对比说明相对紧依赖环境。

##### 1.6.5.3 紧集的连续像

1. 指出最大值定理的拓扑核心。

2. 陈述并证明定理`thm:topo-compact-image`。

3. 解释证明中连续性与紧性各自的作用。

4. 陈述并证明定理`thm:topo-extreme-values`。

5. 用开区间与不连续函数说明两个条件不能去掉。

###### paragraph：同胚保持紧性

1. 由连续像得到同胚保持紧性，陈述并证明定理`thm:topo-compact-hausdorff-homeomorphism`。

2. 回到区间粘合，证明$\bar p$是同胚，并与$[0,1)\to S^1$对照。

### 1.7 本章小结

正文：[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/01-topological-spaces/07-summary.tex)

1. 回到章首问题，总结开集族、拓扑基与邻域基的作用。

2. 总结子集关系与点列收敛，强调点列不能反推闭包。

3. 总结连续映射、开映射与同胚。

4. 总结三种空间构造及其连续性判据。

5. 总结分离性与三种可数性。

6. 总结连通性、路径连通性与紧性。

7. 划定距离章节的分工，并指向同调。

## 第2章 度量空间

正文入口：[02-metric-spaces.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces.tex)，章内依次输入[01-metrics.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/01-metrics.tex)、[02-constructions.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/02-constructions.tex)、[03-convergence.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/03-convergence.tex)、[04-completeness.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/04-completeness.tex)、[05-compactness.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/05-compactness.tex)、[06-finite-covers.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/06-finite-covers.tex)、[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/07-summary.tex)。

章职责与主线：本章在第1章拓扑语言的基础上加入距离，使邻近变成可以计算的误差。先由度量公理和开球得到度量拓扑，讨论距离带来的有界性与“可分等价于第二可数”；再构造子空间、有限乘积与零距离识别后的空间。随后以点列为中心：收敛等价于距离趋零，闭包由点列极限刻画；柯西列与完备性回答极限是否存在，并给出闭子空间判据、完备化与Baire纲定理。紧性的度量判据把开覆盖换成收敛子列，再拆成完备与全有界。最后用覆盖数、打包数和度量熵计数有限精度下的代表，并用体积估计有限维球的覆盖数。连续映射、范数结构与函数类覆盖分别留给第3、11、13章。

1. 章首第一段以有理截断逼近$\sqrt2$和有限格点代表平面区域两个定量说法进入，指出第1章的拓扑说不出误差多大。

2. 第二段说明距离补上这层信息，并提出全章围绕的两个问题：后项相互接近的点列是否有极限，给定精度需要多少代表。

3. 第三段概述前半路线：度量公理、开球拓扑、三种构造、点列收敛与闭包判据。

4. 第四段概述后半路线：完备性、完备化、Baire纲定理、紧性的拆分与有限精度的计数。

5. 第五段划定范围：本章只研究单个度量空间，映射、范数和函数类覆盖分别在第3、11、13章。

### 2.1 度量

正文：[01-metrics.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/01-metrics.tex)

1. 以直线飞行、按较慢坐标方向调整、只判断是否相同三种距离规则进入。

2. 说明本节先提炼公理得到度量，再用开球得到拓扑，然后讨论有界性与可分性。

#### 2.1.1 度量的定义

1. 写出欧氏距离、最大值距离和离散距离的公式（式`eq:metric-three-plane-distances`）并命名。

2. 对$\bm p=(0,0)$、$\bm q=(3,4)$单列算出三种距离$5,4,1$，指出“谁离$\bm p$近”的判断不同，并引出配图。

3. 配图`fig:metric-unit-balls`：到原点距离小于$1$的点分别构成圆盘、正方形与单点。

4. 归纳三种规则的共同之处：非负且只有相同点距离为零、对称、绕道不更近，提出作为公理。

5. 给出度量与度量空间的定义（定义`def:metric-metric`），三条公理为零距离判定、对称性与三角不等式。

6. 逐条解释公理的作用，以单行道说明对称性的含义，以绕道说明三角不等式。

7. 强调度量空间由集合与度量共同确定，同一$\mathbb R^2$配三种距离是三个不同的空间。

8. 由三角不等式移项并交换角色，单列推出反向三角不等式（式`eq:metric-reverse-triangle`），说明点移动多少、到固定点的距离至多变化多少。

9. 示例`ex:metric-three-metrics`逐坐标核对最大值距离的三角不等式，分情形核对离散距离；指出欧氏距离的三角不等式是Minkowski不等式，范数都给出度量。

10. 引出卷二“赋范空间”章和第11章作为范数的参考。

11. 定义二进制串上的Hamming距离，算出$d_H(0110,0011)=2$。

12. 按位置计数证明Hamming距离的三角不等式。

13. 以$e(x,y)=(x-y)^2$为反例，单列$e(0,2)=4>e(0,1)+e(1,2)=2$，解释平方放大大差异使分两步“更近”，其平方根才是度量。

#### 2.1.2 度量拓扑

1. 说明“$x$附近”最自然的含义是距离小于某正数的点，提出先命名这类集合再说明它们生成拓扑。

2. 给出开球与闭球的定义（定义`def:metric-balls`，式`eq:metric-balls`）。

3. 用离散度量说明闭球不一定是开球的闭包。

4. 以开区间端点两侧留有余地类比，提出球内每点都被小球包住。

5. 引理`lem:metric-ball-inside-ball`及其一行三角不等式证明。

6. 说明半径$s$是到边界的余量，并引出配图。

7. 配图`fig:metric-ball-inside-hausdorff`：(a)球内小球的半径选取，(b)半径取距离一半时两球不交。

8. 由引理过渡到开球生成拓扑。

9. 定理`thm:metric-balls-base`：开球构成拓扑基，开集的球判据；证明依次核对覆盖、两球之交含小球，再证球判据的两个方向。

10. 命名度量拓扑，约定今后开集、闭集、邻域、收敛、连续都指这个拓扑。

11. 由定理得邻域的球判据，$B(x,1/n)$构成可数邻域基。

###### paragraph：点的分离

12. 引用配图(b)，单列推导半径为距离一半的两球不交，得到Hausdorff条件。

13. 由分离性得出并非每个拓扑来自度量，以两点集的平凡拓扑为例。

14. 推出单点集是闭集。

###### paragraph：用球判断子集的位置

15. 用列表把内点、闭包、边界翻译成球的语言，说明它们来自开球构成邻域基。

16. 证明闭球是闭集，单列三角不等式给出球在补集中。

17. 示例`ex:metric-open-closed-interval`：$[0,1)$在通常度量下的内部、闭包和边界单列给出，换成离散度量时任意子集既开又闭，说明开闭性取决于度量。

18. 由平方和比较单列$d_\infty\leq d_2\leq\sqrt2\,d_\infty$。

19. 把不等式翻译成球的包含（式`eq:metric-ball-nesting`），引出配图并得出两者开集相同。

20. 配图`fig:metric-ball-nesting`：(a)圆盘夹在两个同心正方形之间，(b)乘积度量的菱形夹在两个正方形之间。

21. 指出离散度量给出不同拓扑，什么时候两个度量“一样好”留到第3章。

#### 2.1.3 有界集

1. 说明拓扑不回答集合整体多大，距离可以回答能否被有限半径的球装下。

2. 定义有界集与直径（定义`def:metric-bounded`，式`eq:metric-diameter`）。

3. 指出空集有界，并用三角不等式说明换球心只需加两球心的距离。

4. 单列估计证明非空集有界当且仅当直径有限。

5. 以$(0,1)$、$\mathbb Z$、$[0,1]$说明有界性与开闭性互不决定。

6. 定义截断度量$d'=\min\{d,1\}$并分情形核对三角不等式。

7. 说明小球相同所以拓扑相同，而整条实轴在$d'$下有界，有界性依赖度量。

#### 2.1.4 可分性的判据

1. 回顾第1章的局部可数、第二可数和可分，提出度量空间中前者总成立、后两者等价。

2. 说明局部可数不能推出全局可数基，因为可数个球合起来在点数不可数时不再可数。

3. 以离散$\mathbb R$为例，每个单点集都必须是基元素，基不可数。

4. 用有理坐标的“地图”类比可数稠密集与有理半径的作用。

5. 定理`thm:metric-separable-second-countable`：可分当且仅当有可数基；证明按有理半径球族、取近邻点、由基元素取代表点分步写出。

6. 说明有理半径是为可数，第二步在一般拓扑中仍成立，第一步依赖距离。

7. 示例`ex:metric-rn-separable`逐坐标取有理逼近证明$\mathbb Q^n$稠密，并说明离散$\mathbb R$不可分。

8. 推出可分度量空间的子集仍可分，依据可数基与子集之交，回指子空间拓扑。

9. 以平面曲线和无理数集为例说明推论的用途。

### 2.2 度量的构造

正文：[02-constructions.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/02-constructions.tex)

1. 回顾第1章的三种构造，提出直接写出新距离并使拓扑与那里一致。

2. 分述子空间、乘积、零距离识别三种构造，说明前两种普遍可行，第三种只适用于由距离决定的识别。

#### 2.2.1 子空间

1. 提出保留两点距离、限制点的做法。

2. 定义子空间度量（定义`def:metric-subspace-metric`）。

3. 说明公理继承，子空间开球是环境开球与$A$的交。

4. 定理`thm:metric-subspace-topology`：诱导拓扑等于子空间拓扑，两个方向分别构造开集$U$和取球。

5. 说明第1章结论可用，开闭性相对于$A$判断，并引出配图。

6. 配图`fig:metric-subspace-chord-arc`：(a)$0$的球限制到$[0,1]$成为$[0,1/2)$，(b)单位圆周上弦长$2$与半圆弧长$\pi$。

7. 解释$[0,1/2)$在$A$中开而在$\mathbb R$中不开，再举$(0,1]$说明环境决定开闭。

8. 指出子空间只保留环境距离，圆周上弦长$2$不是弧长$\pi$。

9. 说明弧长是另一度量、拓扑相同，路径长度在第27章建立。

#### 2.2.2 有限乘积空间

1. 定义求和与取最大两种乘积度量（式`eq:metric-product-metrics`）。

2. 核对公理：零距离判定与对称性逐坐标，三角不等式从单坐标不等式出发，分别相加和取最大。

3. 单列$\rho_\infty\leq\rho_1\leq m\rho_\infty$，引配图`fig:metric-ball-nesting`(b)说明开球嵌套、拓扑相同。

4. 定理`thm:metric-product-topology`：两种度量诱导有限乘积拓扑，由开球是基元素及基元素中可放小球证明。

5. 示例`ex:metric-product-two-coordinates`：实数与Hamming坐标算出$\rho_1=1.3$、$\rho_\infty=1$，并描述半径$1/2$的球。

6. 总结乘积距离小要求每个坐标接近。

#### 2.2.3 伪度量

1. 由只看横坐标的比较（式`eq:metric-first-coordinate-pseudometric`）说明不同点可以距离为零，只缺零距离判定的一半。

2. 定义伪度量（定义`def:metric-pseudometric`）。

3. 说明伪度量来自忽略信息，举半范数和积分比较函数的例子。

4. 说明开球拓扑论证不用零距离判定，因而伪度量也生成拓扑。

5. 算出横坐标开球是竖直带形，说明零距离的点互在对方的所有邻域中。

6. 推出非Hausdorff且极限不唯一，以常值点列趋于两点为例。

7. 配图`fig:metric-pseudometric-quotient`：带形开球、等价类竖线及商映射压成实轴。

#### 2.2.4 零距离等价类上的度量

1. 提出把零距离的点识别，并验证它是第1章的商空间。

2. 定义等价关系并核对传递性，记商映射。

3. 定理`thm:metric-quotient-metric`：$\hat d$不依赖代表元、是度量，诱导商拓扑；证明分定义合理、公理、拓扑两个方向。

4. 回到横坐标例子，识别后得到带通常距离的实轴，并回指配图。

5. 说明构造依赖等价关系由$p$给出，提出$x-y\in\mathbb Q$的反例。

6. 证明该商拓扑平凡，任何度量都不能诱导。

### 2.3 点列收敛

正文：[03-convergence.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/03-convergence.tex)

1. 回顾第1章的邻域收敛，提出换成实数列的极限。

2. 说明本节路线，指出序列判据反向依赖可数邻域基。

3. 定理`thm:metric-convergence-distance`：收敛当且仅当距离趋零，两个方向分别证明。

4. 用$x_n=(\cos n/n,\sin n/n)$说明判据把运动压缩成实数列$1/n$。

5. 取$\varepsilon=1/5$算出$N=6$，并引出配图。

6. 配图`fig:metric-sequence-tail`：(a)平面点列与球，(b)距离数列与$\varepsilon$、$N$。

7. 说明乘积空间中收敛就是逐坐标收敛。

8. 说明离散度量下收敛点列从某项起恒等于极限。

#### 2.3.1 收敛点列的性质

1. 由三角不等式证明极限唯一，指出依赖零距离判定，伪度量失效。

2. 定理`thm:metric-convergent-bounded`：收敛点列有界，取有限项的最大距离放大半径。

3. 定义子列，说明严格递增保证$n_k\geq k$。

4. 证明收敛点列的每个子列收敛到同一极限。

5. 以$(-1)^n$说明有收敛子列不推出整列收敛。

6. 指出第5节紧性判据只要求存在收敛子列。

#### 2.3.2 闭包与闭集的序列判据

1. 提出用下确界度量点到集合的距离。

2. 定义点到集合的距离（定义`def:metric-point-set-distance`，式`eq:metric-point-set-distance`）。

3. 在$(0,1)$上单列$d(2,A)=1$、$d(1,A)=0$，说明距离为零不意味着属于集合。

4. 定理`thm:metric-closure-sequential`：距离为零、属于闭包、存在点列三者等价，按(1)推(3)、(3)推(2)、(2)推(1)分段证明。

5. 说明(1)推(3)用可数半径，一般拓扑中反方向失败，引余可数拓扑。

6. 由三角不等式取下确界，推出点到集合距离的Lipschitz不等式（式`eq:metric-distance-to-set-lipschitz`）。

7. 给出稠密集的序列判据。

8. 给出闭集的序列判据。

9. 示例`ex:metric-sequential-criteria`：有理数稠密、$[0,1]$闭、$(0,1]$不闭，以及换环境后的情形。

10. 指出环境是否缺少极限是下一节的问题。

### 2.4 完备性

正文：[04-completeness.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/04-completeness.tex)

1. 以逼近未知对象时只能看到近似值进入，提出只用点列内部距离的条件。

2. 说明本节路线：柯西列与完备、子空间完备、完备化、Baire纲定理。

#### 2.4.1 完备空间

1. 由收敛点列后项彼此接近提出不提极限的条件。

2. 定义柯西列（定义`def:metric-cauchy`）。

3. 比较收敛与柯西列的量词，前者要知道极限，后者只用点列自身。

4. 引理`lem:metric-cauchy-basic`：收敛点列是柯西列、柯西列有界、有收敛子列的柯西列收敛，分三段证明。

5. 解释第(3)条：抓住部分的极限，整列被带过去。

6. 列出$\sqrt2$的十进制截断并单列$\lvert q_m-q_n\rvert<10^{-n}$，证明它是$\mathbb Q$中的柯西列。

7. 由极限唯一得出它在$\mathbb Q$中无极限，称为“洞”。

8. 引出配图说明逐层放大。

9. 配图`fig:metric-rational-cauchy`：三行逐层放大，$q_n$与空心圆$\sqrt2$。

10. 定义完备度量空间（定义`def:metric-complete`）。

11. 实轴完备，引卷一“极限与连续”章。

12. 由实轴推出$(\mathbb R^n,\rho_\infty)$完备，离散空间完备。

13. 给出$\mathbb Q$与$(0,1)$的不完备例子。

14. 区分两种缺口，并指出完备性依赖度量，引第3章。

#### 2.4.2 闭子空间的完备性

1. 说明子空间是否完备取决于是否保留极限。

2. 定理`thm:metric-closed-complete`：闭子空间与完备子空间的关系，两条结论分别证明。

3. 举$[0,1]$、$\mathbb Z$、$\mathbb Q$的例子。

4. 以$\mathbb Q\cap[0,2]$和$(0,1/2]$说明环境完备性不能省略。

5. 总结闭是相对环境的性质，完备是空间自身的性质。

#### 2.4.3 完备化

1. 说明只能通过柯西列指认缺失的极限，提出把柯西列当作新点。

2. 指出同一缺失点有多种指认方式，以$\sqrt2$的两种逼近演示。

3. 定义牛顿迭代$y_n$，并引表与配图说明两列差值趋零。

4. 表`tab:metric-completion-sequences`：$q_n$、$y_n$与差值。

5. 配图`fig:metric-completion-sequences`：两列有理数趋向$\sqrt2$。

6. 由$z_n=q_n+1$说明逐项距离的极限给出新点的距离，引出识别。

7. 对一般度量空间证明$d(x_n,y_n)$是实柯西列，定义式`eq:metric-completion-pseudometric`。

8. 说明$p$是伪度量而不是度量，举$(1/n)$与常值列为例。

9. 按零距离识别得到$(\hat X,\hat d)$，定义嵌入$\iota$。

10. 定理`thm:metric-completion`：保持距离、稠密、完备，分段证明；完备性用稠密性选代表点列。

11. 命名完备化，说明完备空间的完备化不加新点。

12. 陈述唯一性，证明留到第3章的延拓。

13. 指出$\mathbb Q$、$(0,1)$的完备化，构造用到实轴完备性，不能用来构造实数。

#### 2.4.4 Baire纲定理

1. 证明两个稠密开集的交稠密开，有限个同理。

2. 以$\mathbb Q$上去掉一个点的可数交为空说明可数情形失败，引出定理名称。

3. 定理`thm:metric-baire`：非空完备空间中可数个稠密开集的交稠密。

4. 说明证明思路是选嵌套闭球，并提出先算$\mathbb R$上的例子。

5. 示例`ex:metric-baire-nested-intervals`：$W=(0,1)$、避开$1/2,1/4,5/16$时选三步闭区间，逐步列出中心和半径。

6. 引出配图说明缩向一点。

7. 配图`fig:metric-baire-nested`：三行放大各步的闭区间、球心与红叉。

8. 过渡到一般证明。

9. 定理的证明：第一步选球、归纳选球、球心为柯西列、极限留在每个球内。

10. 说明闭球、半径减半、完备性各自的作用，$\mathbb Q$失败在最后一步。

11. 给出无处稠密闭集的等价形式。

12. 推出$\mathbb R$不可数，对照$\mathbb Q$。

13. 提出由逐点有界到某球上统一有界的用法。

14. 定理`thm:metric-baire-pointwise-bound`及其证明，用闭集$F_k$与Baire纲定理。

15. 指出只用度量与完备性，线性结构下得到一致有界原理，引第17章。

### 2.5 紧性的度量判据

正文：[05-compactness.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/05-compactness.tex)

1. 回顾开覆盖定义的难处，提出两种检验。

2. 说明本节路线：序列判据、全有界、拆分、相对紧。

#### 2.5.1 紧性的序列判据

1. 由闭区间事实提出一般条件。

2. 定义序列紧致（定义`def:metric-sequentially-compact`）。

3. 提出反方向需要联系开覆盖与小球，给出$[0,1]$上的覆盖$[0,0.6)$、$(0.4,1]$。

4. 计算$\delta\leq0.1$可行、$\delta>0.1$失败。

5. 称它为最小分辨尺度，引向引理。

6. 引理`lem:metric-lebesgue-number`：序列紧致空间的开覆盖有Lebesgue数，反证法证明。

7. 以$(0,1)$上的覆盖$(1/n,1)$说明缺少序列紧致时尺度不存在。

8. 定理`thm:metric-compact-sequential`：紧致当且仅当序列紧致；正方向由有限子覆盖得矛盾，反方向由Lebesgue数和贪心选点。

9. 用$[0,1]$的振荡点列说明判据比较的是整个空间。

10. 用$(0,1]$说明一个特定点列收敛不能代替紧性。

11. 说明一般拓扑中两个方向的反例及其查阅方式，并指出证明中距离的两处用途。

#### 2.5.2 全有界性

1. 由证明中出现的条件引出有限精度下有限代表的问题。

2. 定义全有界（定义`def:metric-totally-bounded`）。

3. 说明球心约定在第6节处理。

4. 证明全有界蕴含有界。

5. 以可数无限离散空间说明逆向不成立，区分有界、可分与全有界。

6. 证明$\mathbb R$中有界集都全有界。

7. 证明全有界空间可分，并说明可分不能反推。

8. 提出全有界的序列刻画，并提示先用具体点列演示。

9. 给出$n\sqrt2$小数部分点列的前几项，说明每个小区间含无穷多项。

10. 三轮逐次取子列，列出下标序列。

11. 沿对角线得到下标$2,9,16$，单列对应点，说明对角线子列是柯西列。

12. 配图`fig:metric-diagonal-subsequence`：三轮下标表与对角线圆圈。

13. 定理`thm:metric-totally-bounded-cauchy`：全有界当且仅当每个点列有柯西子列，证明说明对角线下标严格递增，反方向用贪心选点。

#### 2.5.3 完备性与全有界性

1. 把序列判据拆为选柯西子列与取极限两步。

2. 定理`thm:metric-compact-complete-totally-bounded`及其证明。

3. 引出表说明两个条件缺一不可。

4. 表`tab:metric-compact-examples`：四个空间的完备、全有界、紧致情况。

5. 提出欧氏判据的来源。

6. 定理`thm:metric-heine-borel`：$\mathbb R^n$的非空子集紧致当且仅当有界闭；反方向用小立方体构造有限覆盖。

7. 说明结论对欧氏距离成立，并以离散空间说明不能推广。

8. 与有限维直觉对照：$k^n$有限依赖维数，无限维闭球不紧，引第11章。

#### 2.5.4 相对紧性的判据

1. 回顾相对紧集及其在Hausdorff空间中的等价说法。

2. 定理`thm:metric-relatively-compact-sequential`：相对紧的序列判据，反方向用逼近点列。

3. 说明极限不必属于$A$，且相对紧依赖环境，举$(0,1)$在$\mathbb R$和在自身中的情形。

4. 定理`thm:metric-relatively-compact-totally-bounded`：完备空间中相对紧等价于全有界，两个方向分别调整球心与半径。

5. 说明证明的前后两半，以$\mathbb Q\cap[0,2]$说明环境完备性不能省略。

6. 说明无环境完备性时全有界只保证闭包的完备化紧致，并引第13章。

### 2.6 有限覆盖

正文：[06-finite-covers.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/06-finite-covers.tex)

1. 提出全有界只回答能否，需要回答多少。

2. 说明本节计数覆盖与打包，统一用闭球，最后用体积估计。

#### 2.6.1 覆盖数

1. 提出球心约定问题。

2. 定义覆盖数（定义`def:metric-covering-number`，式`eq:metric-covering-number`）与$\varepsilon$网。

3. 说明覆盖数对精度和集合的单调性，以及两种约定只差一倍半径。

4. 定理`thm:metric-covering-centers`（式`eq:metric-covering-centers`）及其证明。

5. 说明全有界不依赖球心约定，以及开球闭球只差一个尺度。

6. 以$A=\{-1,1\}$说明数量可能不同。

7. 用$[0,1]$、$\varepsilon=1/(2m)$的等分覆盖给出上界$m$。

#### 2.6.2 打包数

1. 说明打包从相反方向计数，每个小球至多照顾一个点。

2. 定义分离集与打包数（定义`def:metric-packing-number`，式`eq:metric-packing-number`）。

3. 说明覆盖与打包互相约束。

4. 定理`thm:metric-covering-packing`（式`eq:metric-covering-packing`）及其证明。

5. 说明极大分离集就是网，给出贪心构造。

6. 用矩形$[0,3]\times[0,2]$、$\varepsilon=1$列出九个点并验证分离与极大。

7. 解释配图的两半对应定理的两个不等式。

8. 配图`fig:metric-net-packing`：(a)半径$\varepsilon$的圆覆盖矩形，(b)半径$\varepsilon/2$的圆互不相交。

9. 完成区间的例子，得到覆盖数恰为$m$。

10. 把两个定理连成链，说明三种计数互相控制，以及全有界的打包数判据。

#### 2.6.3 度量熵

1. 提出取对数比较增长速度。

2. 定义度量熵（定义`def:metric-entropy`，式`eq:metric-entropy`）。

3. 指出来源，以给球心编号解释度量熵是描述精度下的信息量。

4. 由全有界判断有限性，算出区间的度量熵。

5. 把论证用于$[0,1]^n$，单列$N=m^n$与$H=n\log m$。

6. 举$n=3,m=4$的数值，说明维数作为系数；离散空间的度量熵为无穷。

7. 区分存在性判断与数量估计，指向第13章。

#### 2.6.4 有限维球的覆盖

1. 说明一般范数球不贴合坐标网格，引入体积工具，定义闭球$B_R$。

2. 第一条事实：单位球体积正且有限。

3. 第二条事实：平移不变，伸缩乘$r^n$，引卷二换元公式。

4. 定理`thm:metric-finite-dim-ball-cover`（式`eq:metric-finite-dim-ball-cover`）及其证明：不交小球比较体积，单列体积不等式和结果。

5. 用$n=2,R=2,\varepsilon=1$的$19$个点检验上界$25$和面积比较。

6. 配图`fig:metric-volume-packing`：$B_R$内$19$个点、不交小圆与外圆。

7. 给出度量熵的双边估计，并以$n=1$的数值说明上下界的精度。

8. 说明指数是实维数，复空间取$2n$，证明依赖线性结构和有限维。

9. 指出无限维单位球不全有界，引第11章。

### 2.7 本章小结

正文：[07-summary.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/02-metric-spaces/07-summary.tex)

1. 第一个回答：距离把邻近变成可算的误差，度量公理保证开球拓扑、Hausdorff和可数邻域基。

2. 用球和点列判断闭包与收敛，可分与第二可数等价。

3. 第二个回答：区分拓扑看不出的性质，有界性与完备性依赖度量，子空间完备判据和完备化。

4. Baire纲定理及其由逐点有界到局部一致有界的用法。

5. 第三个回答：紧性拆为序列紧致、完备且全有界，以及相对紧的判据。

6. 最后把全有界细化为覆盖、打包与度量熵，有限维球的覆盖数指数是实维数。

7. 指向第3章的映射和第13章的函数类覆盖。

## 第3章 度量空间上的映射

正文入口：[03-metric-space-maps.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps.tex)，章内依次输入[01-continuity-criteria.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/01-continuity-criteria.tex)、[02-uniform-lipschitz.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/02-uniform-lipschitz.tex)、[03-map-sequences.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/03-map-sequences.tex)、[04-equicontinuity.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/04-equicontinuity.tex)、[05-comparison.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/05-comparison.tex)、[06-extension.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/06-extension.tex)、[07-contraction.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/07-contraction.tex)、[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/08-summary.tex)。

章职责与主线：本章研究度量空间之间的映射怎样传递距离、极限与误差。先把第1章的开集原像连续性翻译成$\varepsilon$-$\delta$与点列判据，再加强为对整个定义域有效的均匀连续与Lipschitz连续，并证明紧定义域上连续即均匀连续。随后研究映射列的逐点与一致收敛、一致极限的连续性和一致柯西列的极限，得到有界（连续）映射空间的完备性，再定义映射族的等度连续性。接着比较度量空间：等距映射、同胚与同一集合上三种强弱不同的度量等价。最后把映射条件与完备性结合，完成稠密子集上的延拓（并证明完备化唯一）和压缩映射定理及其误差界。函数类的紧性判据留到第13章，函数空间的范数结构留到第11章。

1. 第一段以测量误差的传递、局部放大、逼近函数的连续性能否传给极限、反复代入何时收敛何时停止四个问题进入本章。

2. 第二段说明这些问题都在研究映射怎样传递距离、极限和误差：第1章的连续性只回答“附近映到附近”，第2章的距离使“误差变成多大”可以回答。

3. 第三段交代前半章路线：距离与点列判据，均匀连续与Lipschitz连续，映射列的两种收敛与映射族的等度连续。

4. 第四段交代后半章路线：等距、同胚与度量等价的比较，再把映射条件与完备性结合，得到稠密延拓和压缩迭代。

5. 第五段指向卷一“极限与连续”的实轴情形，并说明函数空间的范数结构在第11章、等度连续族的紧性判据与覆盖估计在第13章。

### 3.1 连续性的判据

正文：[01-continuity-criteria.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/01-continuity-criteria.tex)

1. 回顾第1章用开集原像和邻域定义的连续，说明在度量空间中邻域换成球后，得到输入误差与输出误差之间的一句保证。

2. 预告本节先证明这句保证与开集定义一致，再用点列检验连续性，并区分度量空间与一般拓扑空间。

3. 固定本章记号：$(X,d_X)$、$(Y,d_Y)$为度量空间，$f:X\to Y$，不致混淆时度量都写作$d$。

#### 3.1.1 连续性的距离判据

1. 以$f(x)=x^2$在$x=1$处为例，因式分解$\lvert x'^2-1\rvert=\lvert x'-1\rvert\lvert x'+1\rvert$，为后面估计第二个因子作准备。

2. 约定$\lvert x'-1\rvert<1$，得到第二个因子小于$3$，于是输出误差小于$3\lvert x'-1\rvert$。

3. 对$\varepsilon=0.1$算出$\delta=\min\{1,0.1/3\}=1/30$，并指出一般$\varepsilon$可取$\min\{1,\varepsilon/3\}$，这是下面保证的实例。

4. 用图说明这句保证的读法：输出端先给定球，再在输入端找足够小的球，使其整个像落在输出球内。

5. 配图`fig:mmap-epsilon-delta`：左右两个空间中的球$B(x,\delta)$与$B(f(x),\varepsilon)$，以及落在输出球内的像$f(B(x,\delta))$，像本身不必是球。

6. 说明把$f(U)\subseteq V$中的邻域都换成球就得到$\varepsilon$-$\delta$条件，引出定理。

7. 定理`thm:mmap-epsilon-delta`：一点连续当且仅当满足式`eq:mmap-epsilon-delta`；证明在邻域与球之间往返，分别写出$f(U)$的包含关系。

8. 解释$\delta$可依赖$x$与$\varepsilon$，并回到$x^2$的例子说明换一点公式就要改变。

9. 指出每一点都满足这句保证恰好就是第1章的连续映射，引出下一定理。

10. 定理`thm:mmap-pointwise-open-preimage`：处处满足距离条件当且仅当开集原像为开集；双向用球与原像的包含关系证明。

11. 由补集关系得到闭集原像判据，以$g(\bm x)=x_1^2+x_2^2$说明单位圆周$S^1=g^{-1}(\{1\})$与圆盘$g^{-1}((-\infty,4])$是闭集。

12. 以$x^2$把$(-1,1)$映成$[0,1)$、$e^x$把$\mathbb R$映成$(0,\infty)$说明连续映射不保持像的开闭，并指出开映射是另一概念。

13. 由三角不等式推出到固定点的距离函数满足$\lvert d(x,z)-d(x',z)\rvert\leq d(x,x')$。

14. 对非空集合$A$，由每个$a\in A$的不等式取下确界，得到到集合的距离函数的同样估计。

15. 说明这两个函数可取$\delta=\varepsilon$且对所有点通用，其零点集给出单点集与闭包的闭性。

#### 3.1.2 连续性的序列判据

1. 说明逐个找$\delta$不如看点列方便，度量空间中收敛点列足以探测连续性。

2. 定理`thm:mmap-sequential-continuity`：一点连续当且仅当保持趋于该点的点列极限；反方向取$\delta=1/n$构造反例点列。

3. 给出否定连续的函数$f(\bm x)=x_1x_2/(x_1^2+x_2^2)$，$f(\bm 0)=0$。

4. 沿$(1/n,1/n)$算出函数值恒为$1/2$，得到在原点不连续，并提醒只看坐标轴方向会得出错误结论。

5. 用序列判据证明复合映射在相应点连续，并与第1章的开集原像证明对照。

6. 说明一般拓扑空间中连续仍保持点列极限，用原像邻域逐步论证。

7. 说明反方向依赖可数邻域基，回指第1章余可数拓扑中保持收敛点列却不连续的映射。

### 3.2 均匀连续与Lipschitz连续

正文：[02-uniform-lipschitz.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/02-uniform-lipschitz.tex)

1. 说明处理柯西列、延拓与迭代误差时需要对整个定义域有效的阈值和固定放大倍数。

2. 概述本节依次加强条件，并预告紧定义域上连续升级为均匀连续而不升级为Lipschitz连续。

#### 3.2.1 均匀连续

1. 对$x^2$取$\varepsilon=1$，由向右先触线算出对称区间的最大半径$\delta(x_0)=\sqrt{x_0^2+1}-x_0$（式`eq:mmap-parabola-delta`）。

2. 代入$x_0=1,2,4$，得到$\delta\approx0.414,0.236,0.123$。

3. 说明$\delta(x_0)$约为$1/(2x_0)$并趋于零，引导读者从图中看同样高度的输出带对应越来越窄的输入带。

4. 配图`fig:mmap-uniform-parabola`：抛物线在$x_0=1,2,4$处的绿色输出带与蓝色输入带，数值与前文相同。

5. 对比$[0,1]$上$\lvert x'+x\rvert\leq2$，$\delta=\varepsilon/2$对所有点有效，而$\mathbb R$上$\delta(x_0)$的下确界为零。

6. 定义`def:mmap-uniform-continuity`：均匀连续，式`eq:mmap-uniform-continuity`，注明卷一称一致连续。

7. 对比量词次序：逐点连续的$\delta$可以看着$x$选，均匀连续的$\delta$要在看到$x$之前选好。

8. 给出否定均匀连续的点对序列判据：点对距离趋于零而像的距离不小于某个$\varepsilon$。

9. 用$x_n=n$、$x_n'=n+1/n$算出像差$2+1/n^2\geq2$，说明$x^2$在$\mathbb R$上不均匀连续。

10. 引出均匀连续保持柯西列这一用途。

11. 定理`thm:mmap-uniform-cauchy-image`：均匀连续映射把柯西列送到柯西列，由取阈值再取$N$证明。

12. 以$1/x$在$(0,1)$上说明仅连续不够，并指出稠密延拓依靠这一定理。

#### 3.2.2 Lipschitz连续

1. 说明均匀连续不给$\delta$与$\varepsilon$的数量关系，由此需要固定倍数的条件。

2. 定义`def:mmap-lipschitz`：Lipschitz连续（式`eq:mmap-lipschitz`）与最小常数$\operatorname{Lip}(f)$（式`eq:mmap-lip-constant`）。

3. 给出双锥直观：过图像上任一点作斜率$\pm L$的两条直线，图像留在双锥之内。

4. 以$x^2$在$[0,1]$上$L=2$、顶点$(1/2,1/4)$为例，指向图的(a)。

5. 配图`fig:mmap-lipschitz-cone`：(a) $x^2$留在双锥内，(b) $\sqrt x$从原点到$x=1,1/4,1/25,1/100$的弦斜率$1,2,5,10$。

6. 说明Lipschitz连续蕴含均匀连续，并给出误差放大界$L\eta$。

7. 由两次定义推出复合的放大倍数相乘，式`eq:mmap-lip-composition`。

8. 列举常见Lipschitz映射：距离函数常数不超过$1$，导数有界的实函数由中值定理，$x^2$在$[0,1]$上$L=2$，并引卷一“一元函数的微分”。

9. 矩阵线性映射由诱导算子范数控制，引卷二“赋范空间”。

10. 引出$\sqrt x$在$[0,1]$上是均匀连续而不Lipschitz的反例。

11. 由$(\sqrt y+\sqrt{x-y})^2\geq x$推出$\sqrt x-\sqrt y\leq\sqrt{x-y}$，取$\delta=\varepsilon^2$证明均匀连续。

12. 由比值$1/\sqrt x$无界证明不Lipschitz，并对照图中斜率说明放大倍数$1/\sqrt\eta$无上界。

13. 指出$L<1$的自映射是压缩迭代的出发点。

#### 3.2.3 紧空间上的均匀连续性

1. 指出反例$x^2$与$1/x$的定义域都不紧，紧性排除点跑到无穷远或缺失端点的情形。

2. 定理`thm:mmap-compact-uniform`：紧致度量空间上的连续映射均匀连续；反证，用序列紧致取子列，配对点趋于同一点，由序列判据矛盾。

3. 用开覆盖给出第二种证明的前半：对每点取$\delta_x$，由第2章Lebesgue数引理得公共半径。

4. 完成第二种证明，并比较两种证明分别靠收敛子列与Lebesgue数把逐点阈值汇总。

5. 说明紧性只是充分条件（$\mathbb R$上的恒等映射），且定理不给Lipschitz常数（$\sqrt x$）。

6. 引出比较表，说明$\delta(\varepsilon)$与固定倍数的差别。

7. 表`tab:mmap-continuity-strength`：连续、均匀连续、Lipschitz连续的$\delta$选取方式及正反例。

### 3.3 映射列的收敛

正文：[03-map-sequences.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/03-map-sequences.tex)

1. 说明逼近映射得到映射列，“趋于”有逐点与全部输入共用序号两种要求，差别决定极限能否继承连续。

2. 固定本节记号，概述定义两种收敛、一致极限的连续性和一致柯西列的极限。

3. 用长表类比映射：逐点收敛逐行比较，一致收敛要求同一序号之后整张表都达到精度。

#### 3.3.1 逐点收敛与一致收敛

1. 指出两种收敛的区别在于所需序号能否随输入改变。

2. 定义`def:mmap-pointwise-uniform`：逐点收敛与一致收敛，后者写成式`eq:mmap-uniform-convergence`。

3. 算出$x^n$在$[0,1]$上的逐点极限，在$x=1$处跳跃。

4. 计算使$x^n<0.01$所需的序号：$x=0.9$时$n\geq44$，$x=0.99$时$n\geq459$。

5. 用图和上确界$\sup_{0\leq x<1}x^n=1$说明不存在对全部$x$有效的$N$。

6. 配图`fig:mmap-xn-pointwise`：(a) 若干$x^n$及跳跃的逐点极限，(b) 所需序号$N(x)$在$x\to1^-$时趋于无穷。

7. 限制到$[0,1/2]$上算出$\sup=2^{-n}\to0$，说明一致收敛依赖定义域。

8. 引入上确界距离$d_\infty$（式`eq:mmap-uniform-distance`），说明一致收敛等价于$d_\infty\to0$，并以$x$与$0$说明它可能取$\infty$。

9. 限制到有界映射$B(X,Y)$，由三角不等式证明$d_\infty$有限。

10. 逐点取上确界验证三角不等式与零距离，得到一致度量；说明一般映射上仍用$\varepsilon$-$N$表述。

11. 给出管道图景，并用$f(x)=x$、$f_5(x)=x+\sin(8\pi x)/5$算出$d_\infty=1/5$，落在半径$1/4$的管道内。

12. 配图`fig:mmap-uniform-tube`：(a) 管道与$f_N$，(b) 三段误差①②③，后者供下一小节使用。

#### 3.3.2 一致极限的连续性

1. 回到$x^n$的跳跃，说明一致收敛用图中三段误差排除这种情形。

2. 定理`thm:mmap-uniform-limit-continuous`：连续映射的一致极限连续；取定$N$与开集$U$，把距离拆成三段各小于$\varepsilon/3$。

3. 说明首尾两段由一致收敛控制、中间一段由单个$f_N$的连续性控制，逐点收敛为何失败。

4. 说明定义域不需紧、目标空间不需完备，一致收敛只是充分条件（$x^n$在$[0,1)$上）。

#### 3.3.3 一致柯西列的极限

1. 说明实际中往往只见后项彼此接近，需要由此推出极限存在。

2. 定义`def:mmap-uniform-cauchy`：一致柯西列，式`eq:mmap-uniform-cauchy`。

3. 定理`thm:mmap-uniform-cauchy-limit`：目标空间完备时一致柯西列有一致极限；先逐点取极限，再令$m\to\infty$把统一估计传给$f$。

4. 强调证明顺序，并以取值于$\mathbb Q$的常值映射列说明完备性不可省略。

5. 引出把两小节合起来的结论。

6. 定理`thm:mmap-bounded-maps-complete`：$(B(X,Y),d_\infty)$完备，$C_b(X,Y)$闭因而完备；分步证明极限有界与连续。

7. 说明紧定义域上$C_b=C$，$C([0,1],\mathbb R)$在一致度量下完备。

8. 给出级数$s_n(x)=\sum_{k=1}^nx^k/k^2$。

9. 裂项算出$\lvert s_m-s_n\rvert<1/n$。

10. 说明上界与$x$无关，得到一致收敛于连续函数，并指出第11章反复使用这一模式。

### 3.4 等度连续性

正文：[04-equicontinuity.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/04-equicontinuity.tex)

1. 从一整族映射的规整程度出发，以越来越陡的函数族说明需要成员共用阈值。

2. 对比均匀连续的“与位置无关”和等度连续的“与成员无关”，预告紧定义域上两者可同时实现。

###### paragraph：等度连续的定义

1. 考察$\{x^n\}$在$x_0=1$处，取$\varepsilon=1/2$，用$x=1-\delta/2$说明没有对全族有效的$\delta$。

2. 在$x_0=1/2$处取$\varepsilon=1/10$，限制$\lvert x-1/2\rvert<1/4$后由$(3/4)^9\approx0.075$处理$n\geq9$的成员。

3. 对$n=1,\ldots,8$用中值定理，系数$n(3/4)^{n-1}$的最大值为$27/16$。

4. 算出只需$\lvert x-x'\rvert<8/135$，取全族共用的$\delta=1/17$并验算。

5. 定义`def:mmap-equicontinuous`：一点等度连续、在$X$上等度连续与一致等度连续，式`eq:mmap-equicontinuous`。

6. 说明$\{x^n\}$在每个$x_0\in[0,1)$处等度连续，在$x_0=1$处不等度连续。

7. 说明等度连续要求各成员的$\delta_f$有正下界，有限族总满足，无限族可能不满足。

###### paragraph：等度连续的例子

1. 共同Lipschitz常数给出一致等度连续，以平移族$\sin(x+c)$为例。

2. $\{\sin(nx)\}$在$0$处不等度连续：取$n>\pi/(2\delta)$与$x'=\pi/(2n)$。

3. 用图并排比较这两族在窗口内的行为。

4. 配图`fig:mmap-equicontinuity`：(a) 平移族在窗口内共同缓慢变化，(b) $\sin(nx)$首次到达$1$的位置进入任何窗口。

###### paragraph：紧定义域上的统一半径

1. 引出映射族也有“紧定义域上逐点升级为一致”的结论。

2. 定理`thm:mmap-compact-uniform-equicontinuous`：紧空间上等度连续族一致等度连续；反证，取子列，在极限点用等度连续。

3. 与定理`thm:mmap-compact-uniform`比较，并以$\{x^n\}$在$[0,1)$上说明紧性不可省略。

4. 说明等度连续与有界性合起来用于相对紧判据，判据及覆盖数估计在第13章。

### 3.5 度量空间的比较

正文：[05-comparison.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/05-comparison.tex)

1. 说明“一样”取决于要保留什么：距离、开集与收敛，或柯西列与误差尺度。

2. 概述本节依次讨论等距映射、同胚与三种度量等价。

#### 3.5.1 等距映射

1. 引出最强的比较：距离完全不变。

2. 定义`def:mmap-isometry`：等距映射与等距嵌入（式`eq:mmap-isometry`），满射时称两空间等距。

3. 说明等距映射是单射、$1$-Lipschitz，保持柯西列与收敛。

4. 说明逆也是等距映射，于是完备性、紧致性经等距映射原样搬运。

5. 用平面旋转平移、$t\mapsto(t,0)$与完备化的$\iota$区分满射与嵌入。

6. 以$n\mapsto n+1$说明无限空间可等距嵌入真子集，互相嵌入不能推出等距。

#### 3.5.2 同胚与度量性质

1. 回顾同胚保持开集性质，写出$h:\mathbb R\to(-1,1)$及其逆（式`eq:mmap-homeo-h`）。

2. 用图说明$h$把等距的整数点压向端点。

3. 配图`fig:mmap-homeo-line`：$h$把整数点映到开区间内，上方间距恒为$1$，下方越来越挤。

4. 由$y_n=1-1/n$及$h^{-1}(y_n)=n-1$说明柯西性、完备性、有界性与全有界性都不是拓扑性质。

5. 在$\mathbb R$上定义$d_h$，它使$\mathbb R$不完备。

6. 说明$d_h$与通常度量拓扑相同，这正是第2章预告的度量。

7. 说明紧致度量空间之间不出现这种差别，差别只在非紧空间。

#### 3.5.3 同一集合上的度量等价

1. 把比较化为恒等映射的条件，引出三种等价。

2. 定义`def:mmap-metric-equivalence`：拓扑等价、一致等价、强等价（式`eq:mmap-strong-equivalence`）。

3. 说明强弱蕴含关系，并指向汇总表。

4. 表`tab:mmap-metric-equivalence`：三种等价保留的性质与不保留的例子。

5. 拓扑等价保留收敛、紧致与可分，不保留柯西列（$\lvert\cdot\rvert$与$d_h$）。

6. 一致等价保留柯西列与完备性。

7. 一致等价保留全有界性，由球的包含关系论证。

8. 以$\lvert x-y\rvert$与$\min\{\lvert x-y\rvert,1\}$说明一致等价不保留有界性。

9. 强等价给出球的夹逼（式`eq:mmap-ball-sandwich`）与覆盖数的尺度关系。

10. 给出$\mathbb R^n$上$\rho_\infty$与$d_2$的不等式。

11. 取$n=2$，算出$c=1/\sqrt2$、$C=1$，代入夹逼得到圆盘、正方形、大圆盘的包含关系。

12. 配图`fig:mmap-balls`：$\mathbb R^2$上$d_2$单位球、$\rho_\infty$单位球和$d_2$半径$\sqrt2$的球的嵌套。

13. 说明有限维范数都强等价，常数可能依赖维数，无限维时不再成立，指向第11章。

14. 说明文献中“等价度量”的多义性及本书的处理。

### 3.6 稠密子集上的映射延拓

正文：[06-extension.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/06-extension.tex)

1. 以有理数上定义运算、网格测量说明只在稠密子集上知道映射值的情形。

2. 给出用逼近列定义新值的办法，说明需要极限存在与不依赖逼近列，由完备性和均匀连续分别保证。

#### 3.6.1 延拓的构造

1. 指向对比图，待定义点是$1/\sqrt2$。

2. 配图`fig:mmap-extension`：有理点上的$q^2$与阶跃函数，两侧逼近列的像，前者趋于同一值，后者依赖方向。

3. 解释(a)均匀连续、(b)局部常值却不均匀连续，这就是全部区别。

4. 定理`thm:mmap-extension`：完备目标空间上均匀连续映射唯一连续延拓；分定义$F$、与逼近列无关（交错点列）、延拓、连续性与唯一性四步证明。

5. 说明唯一性只需稠密与连续，存在性两个条件都要用。

6. 以$\mathbb Q$上恒等映射说明目标空间完备不可省略。

7. 以$\mathbb Q\cap[0,1]$上的阶跃函数说明均匀连续不可省略，对应图的(b)。

#### 3.6.2 延拓后的误差控制

1. 说明延拓继承原映射在$D$上的误差控制。

2. 定理`thm:mmap-extension-control`：阈值保持（式`eq:mmap-extension-control`）、$F$均匀连续、Lipschitz常数保持；由距离的连续性取极限证明。

3. 回答哪些函数可由稠密观测唯一确定，以有理点上的多项式为例，分区间延拓后由唯一性拼接。

4. 说明只知连续时有理点值足以确定函数，可以不连续时什么也确定不了。

5. 引出延拓定理完成完备化的唯一性。

6. 定理`thm:mmap-completion-unique`：完备化在等距意义下唯一；延拓$\phi$，取极限证明保距，由闭性与稠密性证明满射。

### 3.7 压缩映射

正文：[07-contraction.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/07-contraction.tex)

1. 把方程写成$x=T(x)$，引入不动点与反复代入，以$x=(x+2)/3$的迭代$2/3,8/9,26/27$起步。

2. 概述成功的三个条件以及结论包括存在唯一和误差界。

3. 用蛛网图解释竖线走到曲线、横线走回对角线，曲线斜率$1/3$时误差按比例缩小。

4. 配图`fig:mmap-cobweb`：(a) $T(x)=(x+2)/3$的蛛网图，(b) $T(x)=\cos x$的实际误差、后验界、先验界。

5. 定义`def:mmap-contraction`：压缩映射与压缩常数，式`eq:mmap-contraction`。

6. 解释定义中的三个要求，并指出压缩映射连续。

7. 定理`thm:mmap-banach-fixed-point`：压缩映射定理，先验界式`eq:mmap-contraction-apriori`与后验界式`eq:mmap-contraction-aposteriori`。

8. 预告后面三个小节的证明顺序。

#### 3.7.1 迭代收敛

1. 由压缩条件反复使用，得相邻迭代差不超过$q^k d(x^{(1)},x^{(0)})$。

2. 沿途用三角不等式与几何级数求和，得到式`eq:mmap-contraction-cauchy`，迭代列是柯西列。

3. 由完备性取极限，再由$T$连续证明极限是不动点，并说明三个要求各起什么作用。

#### 3.7.2 不动点的唯一性

1. 对两个不动点应用压缩条件，写出距离不等式。

2. 移项得距离为零，说明唯一性只用$q<1$，不需要完备性。

3. 结合收敛性说明所有迭代趋于同一点，并直接算出$q^k d(x^{(0)},x^\ast)$的界，指出它含未知的$x^\ast$。

#### 3.7.3 迭代误差界

1. 说明两个界把未知误差换成可算量。

2. 由式`eq:mmap-contraction-cauchy`令$m\to\infty$得到先验界，并称先验误差界。

3. 由先验界反解迭代次数$k$，取对数时不等号翻转。

4. 由三角不等式与压缩条件推出后验界，并称后验误差界。

5. 给出一般点的残差界$d(x,x^\ast)\leq d(x,T(x))/(1-q)$，说明后验界可作停止判据。

6. 说明因子$1/(1-q)$在$q$接近$1$时很大，并以$q=0.99$说明收敛慢。

7. 用调和级数提醒不知道$q$时步长小说明不了问题。

#### 3.7.4 算例与反例

1. 引出可手算的例子。

2. 例`ex:mmap-linear-iteration`：$T(x)=(x+2)/3$，算出$q=1/3$、不动点$1$、前几项、$x^{(k)}=1-3^{-k}$，核对两个界取等，并求出误差不超过$10^{-6}$需要$k=13$。

3. 说明线性例子两个界重合，引出非线性例子。

4. 例`ex:mmap-cosine-iteration`：$T(x)=\cos x$在$[0,1]$上，验证映入自身与$q=\sin1$，给出不动点$0.7391$并指向数值表。

5. 表`tab:mmap-cosine-bounds`：$k=1,5,10,20$时实际误差、先验界、后验界。

6. 解释后验界比先验界紧的原因：实际衰减率趋于$\sin x^\ast\approx0.67$，并对比两种界的用途。

7. 引出三个反例，说明不动点是曲线与对角线的交点。

8. 配图`fig:mmap-contraction-failures`：$x/2$、$x+1$、$x+1/x$与对角线的关系。

9. $(0,1)$上$x/2$说明缺少完备性时极限不在空间中。

10. $\mathbb R$上$x+1$说明压缩常数等于$1$时几何级数不收敛。

11. $[1,\infty)$上$x+1/x$说明没有统一$q<1$时结论失败，用中值定理算出系数$1-1/\xi^2$。

12. $[0,1/2]$上$(x+2)/3$说明必须映回自身，并给出实际使用时先找不变闭集的做法。

13. 指出定常迭代中$\lVert\bm G\rVert<1$是压缩映射，引卷二“定常迭代法”。

14. 指出Picard迭代在连续函数空间中验证压缩条件，引卷六，并回指有界连续函数空间。

### 3.8 本章小结

正文：[08-summary.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/03-metric-space-maps/08-summary.tex)

1. 重述本章开头的三个问题。

2. 连续性本身：距离与点列判据，原像与像的区别，序列判据的适用范围。

3. 统一的误差控制：均匀连续、Lipschitz连续及其反例，紧性的作用与限度。

4. 映射列与映射族：两种收敛、一致极限的连续性、一致柯西列与完备性、等度连续。

5. 度量空间的比较：等距、同胚与三种度量等价各保留什么。

6. 稠密延拓与完备化唯一，压缩映射定理的四个环节与两种误差界。

## 第4章 同调

正文入口：[04-homology.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology.tex)，章内依次输入[01-homotopy.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/01-homotopy.tex)、[02-simplicial-complexes.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/02-simplicial-complexes.tex)、[03-simplicial-homology.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/03-simplicial-homology.tex)、[04-singular-homology.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/04-singular-homology.tex)、[05-summary.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/05-summary.tex)。

章职责与主线：本章从三角形框与三角形纸片、圆周与环带两组对比出发，研究怎样用可计算的代数量辨认路径连接与孔洞，以及这些量在哪些连续变形下不变。先用同伦、同伦等价与形变收缩描述连续变形；再用有限单纯复形记录点、边与填充并给出几何实现；然后在实数系数下把链看作向量、边界映射看作矩阵，以零空间模去列空间得到单纯同调，计算归结为秩，并以包含诱导的映射比较复形；最后在任意空间上建立奇异同调，说明它与有限复形的计算一致，并用棱柱构造证明同伦不变性。

1. 章首第一段以三角形框与填满的纸片有相同的点和边、只记录邻接的图分不出二者为例，说明框有洞而纸片没有。

2. 第二段以环带与圆周不同胚却可沿半径压扁、洞始终存在为对照，提出本章问题：用可计算的代数量辨认洞，并说明这些量在哪些连续变形下不变。

3. 第三段说明前两节的路线：同伦、同伦等价与形变收缩说明环带为何与圆周“有同样的洞”，有限单纯复形把点、边和填充记录下来并实现为空间。

4. 第四段说明后两节的路线：单纯同调把链看作向量、边界映射看作矩阵，把闭合与被填掉化为零空间与列空间；奇异同调把构造搬到任意空间并证明同伦不变，由此算出圆周、环带、圆盘和球面的同调，看清同调相同不意味着同胚。

5. 第五段划定范围：拓扑语言来自第1章，链、核、像与商空间回用有限维线性代数；同调在流形上的意义留给第24章，点云同调恢复与持久同调留给第31章。

### 4.1 同伦

正文：[01-homotopy.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/01-homotopy.tex)

1. 指出同胚要求点一一对应、双向连续，常把“形状相同”的空间分开；给出单位圆周$S^1$与环带$A$的定义。

2. 说明二者围着同一个洞却不同胚，区分办法是比较去掉两点后剩下的部分，并引导读者看配图。

3. 配图展示圆周去掉两点断成两段开弧，环带去掉两点后两点仍可沿圆弧、射线、圆弧连接。

4. 说明$S^1$去掉两点不连通，$A$去掉任意两点仍路径连通，后者的理由在下两段给出。

5. 构造连接$\bm p,\bm q$的路径的第一步：在半径$\lVert\bm p\rVert_2$附近取圆$r_p$避开去掉的点，对$\bm q$同样取$r_q$。

6. 第二步取避开去掉点的射线，把两段短线段、两段圆弧与射线段首尾相接得到路径。

7. 由同胚把“去掉两点”对应为“去掉两点”并保持连通性，得出$S^1$与$A$不同胚。

8. 指出环带能沿半径压到圆周上而洞始终存在，需要比同胚宽松、只要求能用连续变形相互转化的比较。

#### 4.1.1 同伦等价

1. 把环带压向圆周想成随时间$t$播放的动画，每一帧是一个映射，“不跳帧”要求点的位置也随时间连续。

2. 说明把时间当作额外坐标，两种连续性就合成乘积空间上的一个连续映射。

3. 定义同伦：乘积空间$X\times[0,1]$上的连续映射$H$，使$H(\cdot,0)=f$、$H(\cdot,1)=g$，记为$f\simeq g$。

4. 引入$h_t=H(\cdot,t)$，说明同伦既是一族映射，也是每个点的轨迹，并引导读者看配图的横线与竖线。

5. 配图展示矩形$X\times[0,1]$经$H$映到平面，水平线对应$f$、$h_{1/2}$、$g$，竖线对应轨迹。

6. 用“$h_0$为恒等、$t>0$时恒取$0$”的例子说明每帧连续不足以推出整体连续。

7. 给出直线同伦$H(x,t)=(1-t)f(x)+tg(x)$，由凸性留在$Y$中，由算术运算连续，说明进入凸集的映射两两同伦，并都同伦于常值映射。

###### paragraph：同伦关系的性质

1. 说明要把同伦的映射视为同一类，需先确认同伦是等价关系且与复合相容。

2. 引理：同伦是等价关系，并且复合保持同伦。

3. 证明：自反性取静止的同伦，对称性把时间倒过来，传递性把两段同伦各用一半时间接起来；用闭集判断接合映射连续；用$K(x,t)=G(H(x,t),t)$给出复合的同伦。

###### paragraph：同伦等价与可缩空间

1. 把同胚的“恰好回到原处”放宽为“能连续变回原处”，引出下面的定义。

2. 定义同伦等价、同伦逆与可缩空间。

3. 说明同胚是同伦等价，并用复合相容性写出两个同伦等价之复合的同伦逆计算，得出同伦等价是等价关系。

4. 证明可缩判据的一个方向：$X$可缩时，取同伦逆$g(p)=x_0$，$g\circ f$是同伦于恒等映射的常值映射。

5. 证明另一方向：恒等映射同伦于常值映射时，取$f,g$即得同伦等价，$f\circ g$自动为恒等映射。

6. 例子：圆盘经直线同伦$H(\bm x,t)=(1-t)\bm x$可缩，用点$(1,0)$的位置手算验证，并推广到一切非空凸集。

7. 指出直接证明环带不可缩需要排除所有可能的连续变形，这是同调要解决的问题，留到同伦不变性一节。

###### paragraph：同伦等价与同胚的区别

1. 以单点与区间、区间与圆盘为例说明同伦等价比同胚宽松，前者连双射都没有。

2. 用去掉一点后的连通性区分区间与圆盘，写出圆盘去掉一点仍路径连通的具体论证。

3. 比较表列出同胚与同伦等价在所需映射、点的对应、保持的信息和两组例子上的差别。

4. 解释比较表，指出同伦等价忽略维数和点的多少，“洞的个数”要等同调来说清楚。

#### 4.1.2 形变收缩

1. 从环带压向圆周时圆周上的点始终不动出发，引出把空间收回子空间、子空间不受扰动的变形。

2. 把这个过程拆成结果（收回子空间的映射）与过程（连接恒等映射的同伦）两部分。

3. 定义回缩与形变收缩，子空间记为$Y$，以避免与环带$A$混淆。

4. 解释两条要求的分工，由此得到回缩$r$与从$\operatorname{id}_X$到$i\circ r$的同伦。

5. 例子：写出$H(\bm x,t)=(1-t)\bm x+t\bm x/\lVert\bm x\rVert_2$，验证连续性与长度留在$[1,2]$内，并手算点$(0,2)$在$t=1/2,1$的位置，说明这是环带到圆周的形变收缩。

6. 配图展示环带在$t=0,1/2,1$的三帧，圆周上的点不动，外缘绿点的半径依次变化。

7. 把例子提升为定理的引子，指出形变收缩给出同伦等价所需的一对映射。

8. 定理：形变收缩的包含映射$i$是同伦等价，$r$是其同伦逆。

9. 证明：一侧$r\circ i=\operatorname{id}_Y$严格成立，另一侧$H$本身就是所需同伦。

10. 由例子与定理得$A\simeq S^1$，这正是开头“有同样的洞”的精确说法。

###### paragraph：回缩本身不够

1. 用两点离散空间与单点子空间的常值回缩说明回缩不足以推出同伦等价：点$1$无路可走。

2. 概括回缩只说结果、形变收缩还要求过程。

3. 说明定义中固定条件比同伦等价所需的略强，允许$Y$内部移动时结论不变，保留固定条件是因为它描述的具体过程在第31章的点云邻域收回中使用。

4. 指出同伦等价保留什么代数信息要等同调建立后回答，转入下一节的有限数据。

### 4.2 有限单纯复形

正文：[02-simplicial-complexes.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/02-simplicial-complexes.tex)

1. 指出图能用顶点和边记录连接，但框与纸片有同一张图，图中的环在两者上含义不同。

2. 提出把“填充”也记下来，先建立有限组合对象，再实现为欧氏空间中的子集。

#### 4.2.1 单纯复形的定义

1. 说明填充由顶点子集确定，填入三角形时边和顶点也要在记录之中，这引出对取面封闭。

2. 定义抽象单纯复形、单纯形、面与维数。

3. 解释对取面封闭，列出$0$到$3$维单纯形分别是什么。

4. 说明一维单纯复形就是简单无向图，复形是图向高维的推广。

5. 引入记号$n_k$、子复形与骨架。

6. 例子：写出$\mathcal T_1$、$\mathcal T_2$，记录单纯形个数；指出二者一维骨架相同，并给出缺少三条边的集合族作为不是复形的反例。

7. 说明图中的环未必对应复形中的洞，判断要看环能否被高维单纯形填掉，由下一节边界映射精确化。

8. 配图并列$\mathcal T_1$、$\mathcal T_2$、不封闭的集合族与空心四面体表面$\mathcal S$。

9. 例子：写出四面体表面$\mathcal S$的单纯形个数，说明它围住一个二维的洞，加入$V$得实心四面体。

#### 4.2.2 几何实现

1. 指出抽象复形只是集合族，要谈同伦需要把它变成拓扑空间：每个单纯形换成一块实心几何对象，再沿公共面粘合。

###### paragraph：标准单纯形

1. 定义标准单纯形$\Delta^k$，说明它是标准基向量的凸包，有界闭因而紧。

2. 列举$\Delta^0$到$\Delta^3$，把坐标读作基向量的权重，并以$(\frac12,\frac14,\frac14)$和$\Delta^2$的面为例说明面就是把某些坐标取零。

3. 配图展示$\Delta^1$、$\Delta^2$（含点$(\frac12,\frac14,\frac14)$和$t_0=0$的面）与$\Delta^3$。

###### paragraph：沿公共面粘合

1. 对每个单纯形取一份以其顶点为坐标编号的几何单纯形$\Delta^\sigma$。

2. 把各份放在互不相交的位置得到紧集$W$，说明$\Delta^\tau$是$\Delta^\sigma$的面。

3. 在$W$上定义等价关系，商空间$W/{\sim}$把公共面粘成一份，并引导读者看配图的前两幅。

4. 配图展示两个三角形沿公共边粘合，以及纸上的交叉与加入新顶点后的细分。

5. 把商空间放进欧氏空间，写出几何实现$\lvert\mathcal K\rvert$的凸包并。

6. 定义重心坐标与支撑，解释它们分别告诉我们点是哪些顶点的加权平均、落在哪块单纯形内部。

7. 引理：几何单纯形只在公共面上相交，每个点的支撑是单纯形。

8. 证明：用支撑包含于$\sigma$刻画点属于凸包，再得到相交部分与支撑的结论。

9. 构造连续满射$\Phi:W\to\lvert\mathcal K\rvert$。

10. 用支撑说明$\Phi$恰好粘合等价的点，得到连续双射$\bar\Phi$。

11. 说明同胚还需要逆映射连续，下面的引理把它化成紧性。

12. 引理：紧空间到Hausdorff空间的连续双射是同胚。

13. 证明：连续双射把闭集映为闭集，分两步写出紧像是紧的、Hausdorff空间中的紧集是闭集。

14. 由引理得$\bar\Phi$是同胚，定义几何实现与三角剖分。

###### paragraph：抽象顶点、坐标与空间

1. 区分抽象顶点、坐标表示与空间本身三个层次。

2. 说明换一种坐标实现得到同胚的空间，并类比线性代数中向量与坐标的区别。

3. 例子：用径向投影证明三角形边线同胚于圆周；用半平面表示和规范函数$p$写出填实三角形到圆盘的同胚；四面体表面同理同胚于球面。

4. 给出把两条边画成对角线的复形，并指出纸上有交叉。

5. 由公共面引理说明实现中两条边不相交，交叉点不是复形中的点，相遇必须靠新顶点和细分。

### 4.3 单纯同调

正文：[03-simplicial-homology.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/03-simplicial-homology.tex)

1. 比较$\mathcal T_1$与$\mathcal T_2$中的环：都是闭合的，差别在于是否是填充三角形的边界，提出要能给单纯形做加法和取边界。

2. 给出总体类比：链是向量，边界映射是矩阵，闭合是零空间，被填掉是列空间，同调是前者模去后者。

3. 说明计算归结为矩阵的核、像与秩，回用卷二线性代数，本节固定实数系数。

#### 4.3.1 边界映射

1. 说明端点要带符号才能让闭合表现为边界为零，因此先定向再取边界。

###### paragraph：定向与链空间

1. 引入有向单纯形，用边和三角形的绕向说明定向，写出置换符号规则。

2. 由规则得出交换两个顶点改变符号，单纯形有两种定向。

3. 定义链空间$C_k(\mathcal K)$。

4. 说明$C_k\cong\mathbb R^{n_k}$，选全序只影响基向量的符号。

5. 把链看作带符号的流量，举例说明系数的含义。

###### paragraph：边界映射的定义

1. 引入用交错符号依次去掉顶点的边界构造。

2. 定义边界映射$\partial_k$。

3. 写出边的边界，再分两步写出三角形边界并化为绕行一周的三条有向边。

4. 引导读者看配图，说明交错符号使三条边同向绕行，再取一次边界后每个顶点的贡献抵消。

5. 配图对比边的边界、三角形的边界与二次取边界的抵消。

6. 提出边界定义需要与定向规则相容，并把检查化为相邻对换。

7. 逐项检查交换$v_j,v_{j+1}$后右端变为相反数，$\partial_k$良好定义。

###### paragraph：边界矩阵

1. 说明$\partial_k$在基下由$n_{k-1}\times n_k$矩阵$\bm D_k$表示，每列有$k+1$个$\pm1$。

2. 例子：对$\mathcal T_1$算出$\bm D_1$，对$\mathcal T_2$算出$\bm D_2$，并逐分量验证$\bm D_1\bm D_2=\bm 0$。

3. 说明$\bm D_1$是卷三关联矩阵的相反数，二维以上的边界矩阵才记录填充。

###### paragraph：两次取边界为零

1. 由$\bm D_1\bm D_2=\bm 0$的例子提出一般结论。

2. 定理：$\partial_{k-1}\circ\partial_k=0$。

3. 证明：每个$(k-2)$维面出现两次，先去掉$v_b$与先去掉$v_a$两种次序的系数互为相反数。

4. 定义链复形，写出链的序列，并说明任何链的边界都是闭合的。

#### 4.3.2 同调空间

1. 说明闭合是边界为零，被填掉是高一维边界的像，前者包含后者，要除去后者。

2. 定义闭链$Z_k$、边界链$B_k$、同调$H_k$与Betti数$\beta_k$。

3. 解释同调类与“两个闭链相差一块填充”的含义。

4. 把商空间类比为$\mathbb R^2$模去一条直线得到平行线族。

5. 指出类比的差别：一般子空间没有包含关系，$B_k\subseteq Z_k$来自$\partial\partial=0$。

6. 例子：两个三角形共边、只填一个的复形，写出$\bm D_1$，解$\bm D_1\bm x=\bm 0$逐步得到$Z_1$的基$\bm z_a,\bm z_b$，验证外圈$\bm z_c=\bm z_a+\bm z_b$，得出$[\bm z_c]=[\bm z_b]$，并用坐标$(\alpha,\beta)$说明$\beta_1=1$。

7. 配图：左图为复形与两个闭链，右图为$Z_1$平面中$B_1$与平行的同调类。

8. 由秩零度定理写出$\dim Z_k$、$\dim B_k$，得到Betti数公式，并用上例验证。

9. 例子：算出$\mathcal T_1$与$\mathcal T_2$的闭链和边界链，得出$\beta_1=1$与$\beta_1=0$，零维都是$1$。

10. 把例子概括为：两个复形闭链空间相同，差别全在$B_1$，这就是开头区别的代数形式。

###### paragraph：零维同调与连通分量

1. 说明$\beta_0$的含义：零维闭链是所有点，边界链把同一条边的两端等同。

2. 定理：$H_0$以每个连通分量取一个顶点的类为基。

3. 证明：先用路径上边界求和证明张成，再用分量上系数和函数证明线性无关。

4. 由定理得$\operatorname{rank}\bm D_1=n_0-m$，并用例子核对。

###### paragraph：二维的洞

1. 说明同样的计算在高维记录被围住的空腔。

2. 例子：写出$\mathcal S$的$\bm D_2$，解零空间得闭链$\bm w=f_0-f_1+f_2-f_3$，结合每边属于两个三角形解释，再算出$\beta_2=1$、$\beta_1=0$，并说明加入实心四面体后$\beta_2$变为零。

###### paragraph：用单纯形个数核对Betti数

1. 说明Betti数的交错和只依赖单纯形个数，可用来核对手算。

2. 定理：Euler示性数等于Betti数的交错和。

3. 证明：写出$n_k$与$\beta_k$关于秩的两式，相减后交错求和，相邻项相消。

4. 用$\mathcal T_1$、$\mathcal T_2$、$\mathcal S$三个例子核对，并说明Euler示性数可省去一次求秩。

###### paragraph：同调记录了什么，没有记录什么

1. 说明$\beta_0,\beta_1,\beta_2$分别计数什么，“独立”是线性代数意义的。

2. 用单点与$\mathcal T_2$、$\mathcal T_2$与线段说明同调相同不足以判定同胚，同调不记录维数与精细形状。

3. 说明实数系数看不到“某个倍数才能填掉”的现象：除以倍数后闭链本身就是边界。

#### 4.3.3 包含诱导的同调映射

1. 指出要表达“原来的环被填掉”需要把小复形的类送入大复形。

###### paragraph：链映射

1. 由子复形的基向量得到单射$i_k$。

2. 由取面封闭得到边界与包含交换，引出链映射。

3. 定义链映射。

4. 解释交换关系的含义：先送过去再取边界等于先取边界再送过去。

5. 引理：链映射诱导同调映射。

6. 证明：分两步写出闭链映为闭链、边界链映为边界链，得出良好定义与线性性。

7. 定义包含诱导映射并说明恒等映射与复合的性质。

8. 例子：$\mathcal T_1\subseteq\mathcal T_2$上$i_*$把$[\bm z]$送到零，零维上是同构。

###### paragraph：为什么要记录映射

1. 构造$\mathcal T_2$加空心三角形和一条边的复形$\mathcal K$。

2. 由连通性、单纯形个数和Euler示性数算出$\beta_1=1$，说明$H_1(\mathcal K)$由新环$\bm z'$张成。

3. 配图并列$\mathcal T_1$、$\mathcal T_2$与$\mathcal K$，指示$\bm z$被填掉与$\bm z'$的位置。

4. 指出$\mathcal T_1$与$\mathcal K$的Betti数相同，但$i_*$把原环送到零，单看Betti数看不出。

5. 对比去掉$s$的$\mathcal K'$：$\beta_1=2$，$i_*$单射，原环保留下来。

6. 总结比较复形时要同时记录同调空间与映射，并指向第31章的持久同调。

### 4.4 奇异同调

正文：[04-singular-homology.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/04-singular-homology.tex)

1. 指出单纯同调依赖三角剖分，圆周、环带本身没有指定剖分，也无法直接比较两个不相干的复形。

2. 给出办法：允许单纯形是连续映射，同调直接定义在空间上，代价是链空间极大、无法直接求秩。

#### 4.4.1 奇异同调的构造

1. 把有向边对应为路径、三角形对应为$\Delta^2$到空间的连续映射，指出它可以被压扁或退化。

2. 定义奇异单形与奇异链。

3. 配图展示路径、弯曲三角形与压扁到曲线上的二维奇异单形。

4. 说明$S_k(X)$通常无穷维，但每个奇异链有限，操作都是有限的。

###### paragraph：奇异边界

1. 定义插零映射$\delta_i$，把标准单纯形放到第$i$个面上。

2. 定义奇异边界，说明路径的边界仍是终点减起点。

3. 例子：对$\sigma(t_0,t_1,t_2)=(t_1,t_2)$逐个写出三个面，说明奇异边界仍是沿三角形绕行一周的三段路径。

4. 引理：$\delta_j\circ\delta_i=\delta_i\circ\delta_{j-1}$，因而$\partial\partial=0$。

5. 证明：先验证面映射的恒等式，再按$i<j$与$i\geq j$分组，两组逐项相消。

6. 说明这与单纯情形同一机制，$(S_k(X),\partial_k)$是链复形。

7. 定义奇异同调。

8. 比较表列出单纯同调与奇异同调在输入、基向量、取边界、可否求秩和是否依赖选择上的差别。

9. 说明二者优缺点互补，下一小节把它们接起来。

###### paragraph：零维同调与路径分支

1. 说明零维奇异同调的计算与图情形平行。

2. 定理：$H_0(X)$以每个路径分支取一点的类为基。

3. 证明张成：同一路径分支的两点相差路径的边界。

4. 证明线性无关：用路径分支上的系数和函数在边界链上为零。

###### paragraph：连续映射诱导的同调映射

1. 说明连续映射能直接作用在链上，这是单纯同调做不到的。

2. 定理：$f_\#$是链映射，诱导$f_*$，并满足恒等与复合的性质。

3. 证明：由复合可交换得链映射，在链层面验证恒等与复合性质。

4. 由定理得同胚诱导同构，Betti数是拓扑不变量。

#### 4.4.2 单纯同调与奇异同调

1. 指出二者各有长处，需要在有限复形上比较两种链。

###### paragraph：比较映射

1. 把单纯形线性地看作奇异单形，定义比较映射$\theta$。

2. 说明$\theta$只对递增排列定义，其他排列是$S_k$中的另一基向量，故先固定定向。

3. 验证$\theta$是链映射，得到$\theta_*$。

4. 定理：$\theta_*$是同构。

5. 说明证明需要相对同调长正合列、重心细分与五引理，篇幅较长，可查阅代数拓扑教材，这里说明含义与机制。

6. 用逐块搭建复形解释两种同调的变化相同，重心细分把奇异单形切小。

7. 说明逐步比较保持同构，归纳得到全部结论。

###### paragraph：零维情形的核对

1. 说明一维骨架同一分量中的顶点在几何实现中路径连通，每个路径分支都含顶点。

2. 设$C$是分量，把$\lvert\mathcal K\rvert$写成子复形实现的不交并。

3. 用有限闭集划分说明路径只能落在其中一块，不同分量的顶点不在同一路径分支中。

4. 由此两种零维同调都以每个分量取一个顶点为基，$\theta_*$是同构。

###### paragraph：用三角剖分计算连续空间的同调

1. 说明定理与拓扑不变性合起来给出计算方法，同一空间的不同剖分给出同构的同调。

2. 例子：由三角形边界、填实三角形和四面体表面的计算得出圆周、圆盘、球面的Betti数。

3. 指出这些结论单从奇异同调定义很难得到，定理把问题化为三条边、三个顶点的矩阵计算。

#### 4.4.3 同伦不变性

1. 说明本节要证明同伦映射诱导相同同调映射，兑现第一节的直观。

###### paragraph：棱柱构造

1. 说明同伦把闭链扫成柱面，顶减底恰好是柱面的边界。

2. 配图展示$\Delta^1\times[0,1]$、$\Delta^2\times[0,1]$的切分与同伦扫出的柱面。

3. 引入棱柱顶点$\bm a_i,\bm b_i$，要把柱面写成奇异链。

4. 定义线性映射记号与棱柱算子$P$。

5. 解释第$i$个单纯形的路线：底面前$i+1$个顶点、爬上顶面、走完其余顶点。

6. 例子：$k=0$时$P\sigma$是轨迹；$k=1$时写出两个三角形，分别展开边界，对角线相消，得到$\partial P\sigma=g_\#\sigma-f_\#\sigma-P\partial\sigma$。

7. 说明该恒等式对一般$k$成立并指示配图。

8. 引理：棱柱恒等式$\partial P+P\partial=g_\#-f_\#$。

9. 证明：写出$\partial P\sigma$的两组，先处理$i=j$的相消，留下$g\circ\sigma$与$-f\circ\sigma$；再把$i\neq j$的项识别为$P\partial\sigma$的相反数。

10. 解释恒等式的几何含义：柱面边界等于顶减底再减侧面。

11. 定理：同伦的映射诱导相同的同调映射，同伦等价诱导同构。

12. 证明：对闭链应用恒等式得差为边界，再对同伦逆用复合性质。

13. 命名同伦不变性，并说明同伦等价保留全部Betti数。

###### paragraph：单点与可缩空间

1. 写出单点的奇异单形及其边界，由$\partial_k$交替为零和同构，算出单点同调，推出可缩空间同调与单点相同。

###### paragraph：环带与圆周

1. 由形变收缩和同伦不变性得$H_1(A)\cong H_1(S^1)\cong\mathbb R$，解释环带多出的厚度不产生新类。

2. 由$H_1(A)\neq0$得环带不可缩，兑现前文。

3. 用同样的论证证明圆盘不能回缩到边界圆周。

###### paragraph：同调不能判定什么

1. 说明圆盘与单点同调相同却不同胚。

2. 用环面与两个圆周加一个球面的楔为例说明同调相同也不能推出同伦等价，并总结同调是检验“不同”的工具。

### 4.5 本章小结

正文：[05-summary.tex](../../../tex/04-spaces-measures-and-geometry/01-topology-and-metric/04-homology/05-summary.tex)

1. 回答章首两个问题分别由单纯同调和同伦不变性解决。

2. 总结同伦、同伦等价、可缩、形变收缩及回缩不够的反例。

3. 总结有限单纯复形、几何实现和“纸上交叉不是点”。

4. 总结单纯同调的链、边界、闭链、边界链与Betti数公式，以及Euler示性数与诱导映射。

5. 总结奇异同调的定义与性质，以及比较定理的作用和本章的证明范围。

6. 总结棱柱构造、同伦不变性与环带、圆盘的结论，说明同调的使用方向。

7. 指出同调在第24章和第31章的后续使用，并转向第5章的测度。
