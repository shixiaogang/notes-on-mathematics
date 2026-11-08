# 卷二《向量、矩阵与多元微积分》第四部分：多元微积分

所属：卷二《向量、矩阵与多元微积分》第四部分“多元微积分”，本卷第21—27章。正文入口：[volume.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/volume.tex) → [part.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/part.tex)。以下按实际正文顺序记录内容提要。

## 部分主线

本部分从线性作用转到一般的多元映射，回答两类问题：怎样描述映射在一点附近的局部变化，以及怎样在区域、曲线和曲面上累计一个量。第20章以标量场与向量场为对象建立全微分、梯度、Jacobian与Hessian；第21章把同一套微分用于矩阵自变量，给出常用矩阵运算的微分公式与梯度；第22章从方程出发证明隐函数定理与局部反函数定理；第23章把前三章的微分与第9章的有限扰动界结合起来，研究指定方向的一阶响应、局部条件数与余项界，并用于矩阵运算和隐式给定的谱分支。第24章用分割和定义区域积分，并以累次积分、换元与参数积分计算它；第23、24章分别沿路径和曲面累计标量场与向量场，得到功、环流与通量；第27章用散度、旋度把局部导数与边界累计联系起来，建立Green、Gauss与Stokes公式及多元分部积分。前四章依次依赖：第21章用第20章的全微分与Riesz表示，第22章用第20章的压缩估计与第21章的求逆微分，第23章调用第21—23章的结果；后四章以第24章的区域积分为共同基础，第27章同时使用第23、24章的环流与通量。本部分依赖本卷第3章的极限、连续与有限维完备性，第4、7章的谱分解与有限扰动界，以及卷一的一元微积分。

部分导读（`\BookPartGuide`，不计入章数）：

1. 说明前三部分研究线性作用，本部分研究一般多元映射，主线是描述局部变化与在区域、曲线、曲面上累计。

2. 概述前四章的分工：多元函数微分章以标量场与向量场为对象建立全微分、梯度、Jacobian与Hessian；矩阵函数的微分章给出矩阵自变量的微分公式与梯度。

3. 续述隐函数与反函数章说明Jacobian可逆时方程在局部确定唯一可微解；微分与扰动分析章结合谱分析部分的有限扰动界，研究一阶响应、局部放大倍数与余项，并用于矩阵运算和谱分支。

4. 概述后四章：区域积分章的定义与计算方法，路径积分章与曲面积分章按长度、面积及切向、法向的两类累计，积分定理章由散度、旋度与Green、Gauss、Stokes公式联系内部与边界。

5. 提醒区分微分与其表示（梯度、矩阵），指定方向变化率、最坏方向条件数与有限步长余项，局部可逆与整体单射，非负权重的累计与依赖方向的累计，并逐项核对定义域、光滑性、覆盖次数与定向条件。

## 第20章 多元函数微分

正文入口：[01-multivariate-differentiation.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/01-multivariate-differentiation.tex)（章首）；章内依次输入[01-functions-and-fields.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/01-multivariate-differentiation/01-functions-and-fields.tex)（20.1）、[02-scalar-first-order.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/01-multivariate-differentiation/02-scalar-first-order.tex)（20.2）、[03-vector-differentiation.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/01-multivariate-differentiation/03-vector-differentiation.tex)（20.3）、[04-higher-order.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/01-multivariate-differentiation/04-higher-order.tex)（20.4）与[05-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/01-multivariate-differentiation/05-summary.tex)（20.5）。

1. 从一元导数是输出改变量与输入改变量之比的极限出发，指出平板温度、模型损失与流体速度同时依赖多个输入，需要把变化率推广到多个输入。

2. 以$f(x,y)=x^2+xy+y^2$为地形高度，说明从一点出发可以向东、向北、斜向或沿弯曲路线靠近；提出本章的问题：能否用一个线性映射统一预测所有走法下的变化、它在什么条件下成立，以及弯曲部分怎样决定驻点是谷底、山顶还是鞍点。

3. 说明第3章的极限、连续、范数等价、完备、算子范数与伴随和第2章的线性映射、多线性映射与对偶空间是本章语言；本章新增的问题是把精确变化分成线性一阶部分与更小的余项，并指出连续或有限变化有界都不保证这种分解。

4. 交代20.1、20.2的分工：先把多元函数看作标量场与向量场并回顾极限与连续，再由偏导数、方向导数判断何时组成全微分，用内积表示为梯度，并以中值估计控制有限变化。

5. 交代20.3、20.4的分工：向量输出用Jacobian记录微分、用链式法则组合并用算子范数估计增量；再把微分用于梯度得到Hessian、Taylor公式与驻点判别，定性判断用到第6章的实对称谱分解。

6. 划定范围：矩阵自变量的微分在第21章，隐式确定的函数在第22章，误差放大与有限步长下的一阶精度集中在第23章；列出所用的第1章运算与卷一一元微分（跨卷引用到章），并给出两份参考文献。

### 20.1 多元函数与场

1. 从平板温度、河水流速和金属密度等位置上的量进入，说明输入是位置坐标、输出是在该位置读出的量，微分与积分都要先确定这样的研究对象。

2. 指出`sec:multivariable-joint-limit-section`已从极限角度定义多元标量函数与向量值映射，本节改从“位置上的属性”看它们：先按输出是数还是向量区分标量场与向量场，再约定定义域、输出空间及极限与连续性的理解。

#### 20.1.1 标量场

1. 以温度计在平板不同位置的读数以及密度、压强、电势为例，说明标量场在每个位置只给出大小；给出标量场定义`def:multivariable-scalar-field`。

2. 说明作为映射它就是定义`def:multivariable-scalar-function`的多元标量函数，“场”只强调输入是位置；称多元函数还是标量场取决于讨论角度，数学内容相同。

3. 以$f(x,y)=x^2+y^2$为例给出两种画法：三维中的碗形曲面$z=x^2+y^2$，以及输入平面中的等值曲线。

4. 算出等值曲线在$c>0$时是半径$\sqrt c$的圆、$c=0$时是原点、$c<0$时为空；由$c=1,2,3,4$的半径$1,\sqrt2,\sqrt3,2$间距变小，说明离原点越远场值沿径向增长越快。

5. 指出这一观察只是定性的，度量“沿某方向增长多快”需要导数，20.2.4将以梯度描述它并说明梯度与等值曲线正交。

#### 20.1.2 向量场

1. 以流速和重力、电场中的受力为例，说明这些量有大小和方向且与位置同处一个空间；给出向量场定义`def:multivariable-vector-field`，按列矩阵书写，每个分量是标量场。

2. 举出径向场$(x,y)^\top$与绕原点逆时针的场$(-y,x)^\top$，说明第25章用它们比较沿路径的功。

3. 说明向量场是向量值函数的特例：一般向量值函数的输出维数可以不同（参数曲线、神经网络的一层），向量场要求输出与输入同维，箭头才能画在输入空间中，也才能与切向量或法向量作内积。

4. 区分矩阵值的场（每个位置给出一个$p\times q$矩阵，例如应力矩阵，元素均为标量场）与第21章研究的矩阵输入的映射（如$\bm X\mapsto\bm X^{-1}$），强调分类时要分别核对输入与输出空间。

#### 20.1.3 多元函数的极限与连续

1. 说明极限与连续已在第3章建立，这里只回顾后面要用的结论、不重复证明。

2. 回顾极限的范数定义`def:multivariable-limit`：输入进入去心小球、不论沿什么路线，输出都落在给定误差内；连续性`def:multivariable-scalar-continuity`要求极限等于函数值。

3. 说明有限维的向量或矩阵输出可逐分量判断（定理`thm:multivariable-coordinatewise-convergence`），而输入坐标不能拆开逐个检查，因为输入可以同时改变全部坐标、沿弯曲路线趋近。

4. 由此说明路径检验只能否定极限：示例`ex:multivariable-path-limits`沿$x$轴与$y=x$得到$0$与$1/2$；示例`ex:multivariable-parabola-path-limit`沿每条直线趋于$0$而沿抛物线恒为$1/2$；证明极限存在需要只依赖距离的统一误差估计。

5. 指出这一区别在微分中再现：方向导数沿固定直线取极限，全微分要求统一控制，20.2.2的反例与抛物线例子结构相同。

6. 约定定义域：微分时基点取在开集内部，积分时累计范围通常是有界闭区域，只要求被积函数连续或满足相应可积条件。

### 20.2 多元标量函数的一阶微分

1. 承接上一节回顾的极限与连续，说明本节度量函数值变化的快慢：先沿直线把多元函数化为一元函数，得到偏导数与方向导数。

2. 说明这些方向信息只描述固定直线，接着判断它们何时组成对全部小扰动有效的全微分，借对偶空间与内积把全微分表示为梯度，最后沿线段用一元中值定理把梯度大小化为有限变化的界。

3. 限定研究开集$U\subseteq\mathbb R^d$上的实值函数，说明开集保证从基点出发向任何方向走足够小的一步仍在定义域内，双侧差商因而有意义。

#### 20.2.1 偏导数与方向导数

1. 固定除$x_j$以外的坐标得到一元函数，给出偏导数定义`def:multivariable-partial-derivative`；用竖直平面截曲面所得截线的切线斜率和“向正东移动时温度的变化”解释其几何含义。

2. 说明计算时把其余坐标当作常数；示例`ex:multivariable-quadratic-partials`对$x^2+xy+y^2$求得$f_x=2x+y$、$f_y=x+2y$，在$(1,2)$处为$4,5$，并用定义和数值$f(1.01,2)=7.0401$等核对。

3. 指出每个偏导数只描述自己那条坐标切片；同时走$(0.01,0.01)$时增量约为$0.04+0.05$，像是两个偏导数贡献之和，但这种相加并非总是成立，保证它的可微性留给20.2.2。

###### paragraph：方向导数

1. 让多个坐标按固定向量比例共同移动，得到另一条直线上的一元切片，给出方向导数定义`def:multivariable-directional-derivative`，用“沿地图方向前进时脚下的坡度”解释；说明$\bm v=\bm e_j$回到偏导数，定义采用双侧极限，单侧方向导数是另一概念，边界点只能讨论指向内部的单侧差商，本章只在开集内部使用双侧定义。

2. 说明方向向量不必是单位向量，此时导数按参数$t$计量，表示每单位水平距离的变化率须取单位向量；示例`ex:multivariable-diagonal-directional-derivative`由$f(1+t,2+t)=7+9t+3t^2$得沿$(1,1)^\top$为$9$，改用同向单位向量得$9/\sqrt2$。

3. 由两个方向向量描述同一直线、只是参数速度不同，提醒比较变化率前先统一归一化；再指出$9=4\cdot1+5\cdot1$恰为偏导数按方向分量加权之和，提出这些切片变化率能否组成对所有方向乃至方向不断改变的扰动都有效的线性近似，引出下一小节。

#### 20.2.2 全微分与可微性判别

1. 从一元可微$f(a+h)=f(a)+f'(a)h+o(h)$即图像放大后像切线出发，说明两个输入时对应的是切平面；预测规则应与扰动的叠加和数乘相容，故用线性映射，遗漏的误差还须比扰动长度小得多。

2. 给出可微性与全微分定义`def:multivariable-total-differential`（式`eq:analysis-total-differentiability`）；写出余项条件，说明$\bm h\to\bm0$按`sec:multivariable-joint-limit-section`的联合极限理解，强调同一个$A$适用于全部趋零扰动，而不是按方向分别控制误差；$d=2$时解释为曲面与切平面的高度差比水平距离小得多。

3. 示例`ex:multivariable-tangent-plane-error`：取$A(h,k)=4h+5k$，在$(0.01,0.02)$处误差与步长之比约$0.031$，步长减半后约$0.016$，说明这个比值随步长缩小而趋零正是余项条件的要求。

###### paragraph：可微性的要求与判别

1. 固定开集、函数与基点，说明下面依次讨论可微必然带来什么、一个便于核查的充分条件，以及区分偏导数存在、全部双侧方向导数存在、可微和连续可微的反例。

###### paragraph：可微的必要条件

1. 说明统一线性近似限制到一条直线上必须与该直线上的一元导数相同，函数增量也必须趋零，由此联系全微分与偏导数、方向导数。

2. 定理`thm:multivariable-differentiable-necessary`：可微蕴含连续、各偏导数存在、全微分唯一，$\mathrm df_{\bm a}(\bm h)=\sum_j\partial_jf(\bm a)h_j$且$D_{\bm v}f(\bm a)=\mathrm df_{\bm a}(\bm v)$。证明先由有限和的Cauchy--Schwarz不等式得线性项趋零（即`sec:ls-matrix-norms`有限维线性映射的Lipschitz连续）从而连续，再取$\bm h=t\bm e_j$读出系数并得唯一性，最后取$\bm h=t\bm v$得方向导数公式。

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

5. 回指`sec:multivariable-joint-limit-section`示例`ex:multivariable-parabola-path-limit`：函数沿抛物线有一道坡，每条直线都避开它；说明方向导数先固定方向再取极限，全微分则要求方向随扰动改变时误差仍受同一个控制。

###### paragraph：连续与偏导数存在互不蕴含

1. 用处处Lipschitz连续的$|x|$在原点关于$x$的双侧偏导数不存在说明连续推不出偏导数存在，用示例`ex:multivariable-path-limits`中原点置零的$xy/(x^2+y^2)$说明偏导数存在推不出连续；结论是二者互不蕴含，可微同时保证二者。

###### paragraph：条件之间的蕴含关系

1. 写出“邻域内连续可微$\Rightarrow$可微$\Rightarrow$全部双侧方向导数存在$\Rightarrow$全部偏导数存在”的蕴含链，逐条指出依据（两条定理与取坐标方向），并补充可微蕴含连续、方向导数关于方向线性。

2. 区分第一行前提涉及整个邻域、其余条件只涉及基点；逐个回指示例`ex:multivariable-differentiable-not-c1`、`ex:multivariable-nonlinear-directional-derivatives`、`ex:multivariable-linear-directionals-not-differentiable`与`ex:analysis-partials-not-differentiable`说明各箭头不能反向，并提醒不满足偏导数连续时应回到定义检查余项。

#### 20.2.3 微分的运算法则

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

2. 解释内层先产生速度向量、外层全微分再作用于它；取直线回到方向导数公式，并说明20.2.4用该式证明梯度与等值曲线切向正交，一般向量值复合留给20.3.2。

###### paragraph：二次型的微分

1. 说明平方误差、能量函数含二次型结构；对$q(\bm x)=\bm x^\top\bm A\bm x$把两个$\bm x$看作两个因子，用乘积法则并利用标量等于自身转置，得到$\mathrm dq_{\bm x}(\bm h)=\bm x^\top(\bm A^\top+\bm A)\bm h$及偏导数向量式`eq:analysis-quadratic-form-gradient`。

2. 说明$\bm A$对称时化为$2\bm A\bm x$，不对称时不能这样写；用$\bm A=\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]$即$q=x_1x_2$核对$(\bm A+\bm A^\top)\bm x=(x_2,x_1)^\top$，而$2\bm A\bm x$是错的。

###### paragraph：二次型的精确增量

1. 说明乘积法则只给出一阶项，对对称$\bm S$直接写出完整增量$2\bm x^\top\bm S\bm h+\bm h^\top\bm S\bm h$；由Cauchy--Schwarz与谱范数（`sec:ls-matrix-norms`）得$|\bm h^\top\bm S\bm h|\leq\lVert\bm S\rVert_2\lVert\bm h\rVert_2^2$，余项受明确二次量控制，也独立证明了可微。

2. 以$x^2+xy+y^2$的$\bm S$特征值为$3/2,1/2$说明$\lVert\bm S\rVert_2=3/2$正是示例`ex:multivariable-quadratic-differential`中的余项常数；预告$\bm h^\top\bm S\bm h$在20.4成为Hessian二次型，梯度与余项估计将复用此例。

#### 20.2.4 梯度与内积

1. 说明全微分是$\mathbb R^d$上的线性泛函即对偶空间元素（`sec:ls-dual-spaces`），不能画成输入空间中的箭头；由`sec:ls-riesz-representation`的Riesz表示定理，选定内积后它等于与唯一向量的内积，给出梯度定义`def:multivariable-gradient`，未加说明时取标准欧氏内积。

2. 在标准内积下逐个取$\bm h=\bm e_j$，得到梯度的坐标式`eq:multivariable-gradient-coordinates`，从而$f(\bm a+\bm h)=f(\bm a)+\nabla f(\bm a)^\top\bm h+o(\lVert\bm h\rVert_2)$、$D_{\bm v}f=\nabla f^\top\bm v$；以$\nabla f(1,2)=(4,5)^\top$与一般二次型为例，说明梯度与输入同属一个空间，可画成地图平面上的箭头。

3. 说明处处可微时把各点梯度放在该点得到梯度场$\nabla f$，以$x^2+y^2$的梯度场$(2x,2y)^\top$与20.1.1观察到的等值圆变密相互印证，并说明哪些向量场是梯度场留给25.4。

4. 由表示向量随泛函线性变化，把20.2.3的法则改写成梯度的和、数乘、积与复合法则，以$\nabla e^{-(x^2+y^2)}$指向原点为例。

###### paragraph：偏导数向量与梯度

1. 说明偏导数全部存在时本书也用$\nabla f$记这一列偏导数，但它此时只是坐标变化率的排列：示例`ex:multivariable-nonlinear-directional-derivatives`中这一列为$(1,0)^\top$却给不出沿$(1,1)^\top$的方向导数；只有确认可微后才能用内积计算任意方向导数并解释为最快上升方向。

2. 指出列向量的排列来自所选内积与坐标：标准内积把全微分系数原样排成列向量，换用其他内积时同一全微分由另一个向量表示。

###### paragraph：改变内积时的梯度

1. 设内积为$\bm x^\top\bm G\bm y$（`sec:ls-gram-psd`说明任何内积在坐标下都是这种形式，$\bm G$为Gram矩阵），由$\bm c^\top\bm h=\bm g^\top\bm G\bm h$对所有$\bm h$成立推出$\bm G\bm g=\bm c$，得式`eq:multivariable-gradient-gram`；强调系数向量由函数决定，改变的只是表示向量。

2. 示例`ex:multivariable-weighted-gradient`：$\bm G=\operatorname{diag}(4,1)$时梯度为$(1,5)^\top$，核对它给出同一全微分$4h+5k$，并解释加权长度使第一坐标方向的同样加权距离只需更小的坐标位移；与`sec:ls-riesz-representation`“读取不变、表示随内积改变”的结论对应。

###### paragraph：最陡上升方向

1. 对所选内积诱导长度下的单位向量，由Cauchy--Schwarz不等式（定理`thm:linear-algebra-cauchy-schwarz`）得$D_{\bm u}f\leq\lVert\nabla f\rVert$，梯度非零时取其方向达到等号；结论是梯度方向上升最快、最大坡度为梯度长度、反方向下降最快，并用加权例子说明“最快”总相对某种长度而言。

###### paragraph：梯度与等值曲线

1. 由与梯度正交的方向导数为零进入；对落在等值集中、经过基点的可微曲线，用式`eq:multivariable-curve-chain-rule`求导得梯度与切向量正交。

2. 限定这里假定了这样的曲线存在，等值集在基点附近是否光滑需要第22章的隐函数定理与梯度非零条件；梯度为零只说明一阶项消失，局部形状留给20.4；图`fig:analysis-process-gradient-level-curves`对照梯度方向、等值曲线切向$(5,-4)^\top$与另一单位方向，并提醒比较前先归一化。

#### 20.2.5 中值估计与局部Lipschitz性

1. 说明微分只描述一点附近的变化，估计两点之间的有限变化要沿连接两点的线段把函数化为一元函数，前提是整条线段在定义域内；给出线段记号。

2. 定理`thm:multivariable-scalar-mean-value`及证明：令$\phi(t)=f(\bm x+t(\bm y-\bm x))$，其导数是沿$\bm y-\bm x$的方向导数，对$\phi$用一元中值定理；解释为一元“平均斜率等于某点切线斜率”的推广，并以$x^2+y^2$从原点到$(1,1)$的中值点为线段中点为例。

###### paragraph：局部Lipschitz性

1. 回指定义`def:ls-lipschitz`已给出Lipschitz与局部Lipschitz连续，说明本小节的新任务是由导数求出常数：中值公式把增量写成梯度与位移的内积，梯度长度有统一上界时即可用距离控制输出变化，并指出优化中常用这种控制。

2. 先给不依赖导数的例子：线性函数的常数是$\lVert\bm a\rVert_2$即梯度长度，欧氏范数由三角不等式以$1$为常数却在原点不可微，说明Lipschitz连续不要求处处可微。

3. 引入凸集，定理`thm:multivariable-gradient-lipschitz`：凸开集上可微函数以$L$为Lipschitz常数当且仅当梯度长度处处不超过$L$；充分性用中值公式与内积不等式，必要性沿梯度单位方向取单侧差商极限。几何上解释坡度与高度变化的关系，并以$\sin x+\cos y$的常数$\sqrt2$为例。

4. 示例`ex:multivariable-nonconvex-lipschitz-failure`：去掉负$x$轴的环形区域上极角函数梯度长度小于$1$，但负$x$轴两侧距离$2\varepsilon$的两点极角相差接近$2\pi$，不是Lipschitz函数；解释连接两点的线段穿过被去掉的部分，中值公式不能使用，故凸性不能省略。

5. 说明局部情形不需整体凸：$C^1$函数在基点附近闭球上梯度长度有界（定理`thm:multivariable-extreme-value`），在同心开球上用前述定理得局部Lipschitz；用$x^2$说明各点局部常数不一定有共同上界。

###### paragraph：三种控制的强弱

1. 比较已出现的三种结论：连续不给出趋近速度；可微给出$o(\lVert\bm h\rVert_2)$的渐近线性近似，却不说明给定有限步长的误差；梯度的统一界沿线段控制有限变化的大小，却不估计线性预测还差多少。

2. 指出估计一阶预测还差多少要结合后两者、考察导数沿线段怎样变化：20.4的Taylor公式用二阶导数描述这种变化，只用一阶导数的余项界与局部条件数集中在第23章。

### 20.3 多元向量值函数的微分

1. 从每个输入只产生一个实数转到产生$m$个输出分量的映射$F:U\subseteq\mathbb R^d\to\mathbb R^m$，关心输入稍变时输出点整体怎样移动。

2. 以极坐标映射、神经网络的一层、参数曲线与参数曲面为例说明这类映射的来源。

3. 说明可以逐个分量使用前面的结论，但每个分量仍须对全部输入方向整体扰动；本节先定义整体可微并引入Jacobian，再给出复合映射的导数，最后用导数的算子范数估计有限增量。

#### 20.3.1 Jacobian矩阵

1. 按输出分量给出多元向量值函数定义`def:multivariable-vector-function`；回用`sec:multivariable-joint-limit-section`、`sec:multivariable-continuity`的极限与连续性及20.1.3的回顾（输出点整体接近等价于各分量接近），说明本节在连续性基础上研究线性近似，并指出向量场是$m=d$的特例。

###### paragraph：微分与Jacobian矩阵

1. 说明向量输出的全微分要把输入扰动映为$m$维输出扰动，有限维线性映射由矩阵表示，每行记录一个分量的系数；给出可微性与Jacobian矩阵定义`def:multivariable-vector-differential`（式`eq:analysis-jacobian-linearization`），余项按输出欧氏范数理解。

2. 证明向量值函数可微当且仅当各分量可微：正向取向量余项的分量，反向用欧氏范数合并有限个小量余项；由此Jacobian第$i$行是$\nabla F_i^\top$，微分唯一，并定义向量值$C^k$。

3. 说明列向量约定下Jacobian为“输出维数$\times$输入维数”，$\bm J_F\bm h$与输出同形；$m=1$时Jacobian是行向量$\nabla f^\top$，与列向量梯度互为转置。

###### paragraph：Jacobian矩阵的几何意义

1. 说明按行看是各分量的梯度，按列看第$j$列是只增加第$j$个输入时输出点的移动方向，一般扰动的一阶效果是各列按$h_j$加权求和。

2. 对$d=m=2$说明小正方形的像近似为两列张成的平行四边形，由`sec:prelim-determinants`行列式的面积缩放含义得面积约$|\det\bm J_F|\varepsilon^2$，符号表示定向是否翻转。

3. 示例`ex:multivariable-polar-jacobian`：极坐标映射的Jacobian行列式为$r$，第一列是单位径向向量、第二列长度为$r$沿切向，小矩形变为面积约$r\,\mathrm dr\,\mathrm d\theta$的扇形块；说明离原点越远面积放大越多，24.3的区域积分换元用这个倍数校正面积。

4. 图`fig:analysis-process-jacobian-grid-cell`对一般非线性映射$T$对照弯边像块与线性像平行四边形，$\det J_T(a)=0.525$，说明有限块不与线性像重合，缩小扰动后才由可微余项控制差异。

5. 示例`ex:multivariable-helix-jacobian`：螺旋线的Jacobian是$3\times1$的切向量，长度$\sqrt2$表示参数每增加一单位点约移动$\sqrt2$；结论是Jacobian形状随输入输出维数改变，不能默认为方阵或有行列式，并预告20.4把梯度映射也作为向量值映射研究其微分。

###### paragraph：Jacobian矩阵的计算

1. 给出逐分量求偏导、按行排列并核对形状的做法，以$F(x,y)=(x^2+xy,y^2)^\top$在$(1,2)$处的一阶影响$(4h+k,4k)^\top$为例，按行、按列解读。

2. 引入softmax（归一化指数映射）把得分变为总和为$1$的正权重，由商法则推出式`eq:analysis-softmax-jacobian`；解释对角项为正、非对角项为负来自共同分母，$n=1$时Jacobian为零，每行和为零对应所有得分加同一常数不改变输出。

3. 示例`ex:multivariable-softmax-jacobian-check`：二维softmax在原点的Jacobian为$\tfrac14\left[\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right]$，提高$z_1$为$0.1$时线性近似$0.525$与实际$0.52498$只差约$2\times10^{-5}$，两分量增量一正一负、和为零。

#### 20.3.2 微分的运算法则

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

1. 说明上例中的转置是`sec:ls-adjoints`的伴随：输入、输出各取内积，链式法则写成线性映射的复合，依次用梯度定义与伴随定义式`eq:ls-adjoint-pairing`，由梯度唯一性得式`eq:multivariable-gradient-adjoint`。

2. 解释微分把输入扰动推向输出端、伴随把输出端梯度拉回输入端；标准内积下伴随矩阵为$\bm J_F^\top$，回到上例，加权内积下由式`eq:ls-weighted-adjoint`为$\bm M_V^{-1}\bm J_F^\top\bm M_W$，与式`eq:multivariable-gradient-gram`相容；指出矩阵函数的梯度与隐函数的导数都沿用这一规则。

#### 20.3.3 向量增量的估计

1. 说明标量中值公式不能照搬到向量值函数：各分量的中值点可能不同；以单位圆参数化走完一圈增量为零而速度长度恒为$1$为例，改为估计增量长度或把增量写成沿线段的积分。

###### paragraph：导数的算子范数

1. 说明向量输出时同一线性映射在不同方向放大倍数不同，取最大者；回用`sec:ls-matrix-norms`已定义且有限维时有限可达的算子范数，写出$\lVert\mathrm dF_{\bm a}\rVert$，两端欧氏范数时即Jacobian的谱范数，标量情形就是梯度长度；计算时先给对全部单位向量成立的上界，再找达到上界的方向。

2. 示例`ex:multivariable-diagonal-operator-norm`：由$4h_1^2+h_2^2\leq4$且$\bm e_1$取等得$\lVert\operatorname{diag}(2,1)\rVert_2=2$；补充旋转矩阵的算子范数为$1$。

3. 定理`thm:multivariable-vector-mean-value`（式`eq:analysis-operator-mean-value-bound`）及证明：在含线段的开集上连续可微时，把向量增量投影到自身单位方向得到标量函数，用链式法则与一元中值定理，再用内积不等式与谱范数的界；说明这样不再需要各分量共用中值点。

###### paragraph：向量增量的积分表示

1. 说明中值估计只给长度上界，在同样条件下逐分量用式`eq:multivariable-curve-chain-rule`与一元微积分基本定理，可精确写出式`eq:multivariable-vector-integral-increment`，各分量变化率沿整条线段累计而不需共同中间点。

2. 由积分的线性、单调性与Cauchy--Schwarz不等式证明向量积分的范数不超过范数的积分，用于积分表示再次得到式`eq:analysis-operator-mean-value-bound`；指出积分形式可先从被积函数中扣除固定线性项，第23章（23.1.2）据此估计一阶余项。

###### paragraph：Lipschitz估计与压缩

1. 说明凸开集上Jacobian谱范数有统一界$L$时映射以$L$为Lipschitz常数，局部球上得局部版本；界$q<1$时称压缩，但压缩本身不保证迭代留在球内、也不单独给出不动点，还须检查自映射并借有限维完备性（定理`thm:ls-finite-dimensional-complete`）取极限，第22章证明隐函数定理时依次核对这三点。

### 20.4 高阶微分与极值判别

1. 说明切平面看不出曲面弯向哪边，碗底、山顶和马鞍点的切平面都是水平的，切平面遗漏的部分中最先出现的是弯曲；把20.3的向量值微分用于梯度映射以研究弯曲。

2. 说明多线性映射、二次型和谱判别分别用于表示高阶导数、衡量二阶项和判断局部形状，并交代路线：先把二阶偏导数集中为Hessian并解释为二阶微分，再借一元Taylor公式建立二阶近似，最后判断驻点类型。

#### 20.4.1 二阶偏导数、Hessian与高阶微分

1. 定义记号$f_{x_ix_j}=\partial_j(\partial_if)$，解释$f_{xx}$为切片的弯曲、$f_{xy}$为曲面的扭转；以$x^2+xy+y^2$及每条坐标切片都是直线却扭曲的$xy$为例，指出一般函数混合偏导数能否交换需要额外条件。

###### paragraph：混合偏导数的交换

1. 示例`ex:multivariable-mixed-partials-differ`：$xy(x^2-y^2)/(x^2+y^2)$由$f_x(0,y)=-y$、$f_y(x,0)=x$得两个次序的混合偏导数分别为$-1$与$1$。

2. 定理`thm:multivariable-mixed-partials`及证明：混合偏导数在邻域存在并在基点连续时可交换，$C^2$函数处处可交换；证明对小矩形四顶点的二阶差分按两种方式分组，各用两次一元中值定理得到不同中间点处的两种混合偏导数，令步长趋零并用连续性；回指反例说明缺少连续性时结论可能失败。

###### paragraph：Hessian矩阵

1. 把全部二阶偏导数排成方阵，给出Hessian定义`def:multivariable-hessian`，解释第$i$行是$\partial_if$偏导数向量的转置，即“梯度的梯度”；指出二阶偏导数存在不保证梯度映射有统一线性近似，二阶可微指$\nabla f$作为向量值映射可微。

###### paragraph：Hessian是梯度映射的Jacobian

1. 对$C^2$函数由定理`thm:multivariable-continuous-partials-sufficient`逐分量得梯度映射可微，$C^2$是二阶可微的充分条件；按Jacobian约定得$\bm J_{\nabla f}=\nabla^2f$，说明Hessian既是二阶偏导数表又是梯度映射微分的矩阵，描述基点移动时梯度怎样变化，$C^2$时对称。

2. 说明沿直线求两次导数得方向二次型$\bm v^\top\nabla^2f\bm v$（依据见Taylor定理的证明），它衡量切片曲线向上或向下弯；对二次函数$\tfrac12\bm x^\top\bm A\bm x+\bm b^\top\bm x+c$说明只有对称部分$\bm H$影响函数值，由式`eq:analysis-quadratic-form-gradient`得Hessian为常数矩阵$\bm H$。

3. 用$\operatorname{diag}(2,100)$说明狭长山谷与半轴之比$\sqrt{50}$，用$\operatorname{diag}(2,-100)$说明马鞍形；回指`sec:ls-matrix-representation`的正定与半正定，补充负定、半负定与不定，对应碗形、倒扣的碗与马鞍。

4. 示例`ex:multivariable-hessian-definiteness`：配方证明$\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$正定，$\left[\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\right]$对角元为正却沿$(1,-1)^\top$为负、不定；说明判断定性须检查整个二次型，对角元只反映坐标轴方向。

###### paragraph：高阶微分的多线性形式

1. 说明Hessian可同时作用于两个方向：对固定$\bm h$把一阶变化看作基点的函数，沿$\bm k$求全微分得$D^2f_{\bm x}[\bm h,\bm k]=\bm h^\top\nabla^2f\bm k$，它是`sec:ls-linear-maps`意义下的对称双线性形式，两个方向相同时给出Taylor二次项。

2. 把$\bm x\mapsto\mathrm df_{\bm x}$看作取值于有限维泛函空间的映射，逐次求微分得$C^r$函数的$r$重线性形式，其系数就是$r$阶偏导数数组，与`sec:ls-linear-maps`多线性映射的坐标表示一致；以$x^2y$在$(1,2)$处的二次变化$4h_1^2+4h_1h_2$说明混合项使两条坐标轴的一元展开不能简单相加。

###### paragraph：二阶导数界与导数的Lipschitz性

1. 说明二阶微分能控制一阶导数本身变化多快，第23章估计余项时需要这种控制：对$C^2$向量值映射定义$D^2F_{\bm x}[\bm h,\bm k]$（第$i$个分量为$\bm h^\top\nabla^2F_i\bm k$）及其范数$\lVert D^2F_{\bm x}\rVert$，最大值由连续函数在闭有界集上取到，标量时即Hessian的谱范数。

2. 定理`thm:multivariable-second-derivative-lipschitz`及证明：凸开集上二阶导数统一不超过$M$时Jacobian以$M$为Lipschitz常数；固定单位向量$\bm h$令$G(\bm z)=\bm J_F(\bm z)\bm h$，对$G$用积分表示并取范数，再对$\bm h$取最大值。

3. 结论：二阶导数的统一界给出Jacobian的Lipschitz常数；预告23.1.2将证明只要Jacobian满足这种Lipschitz型界，余项就不超过$\tfrac L2\lVert\bm h\rVert_2^2$，本定理只是取得该条件的一种充分办法，那里的余项估计本身不要求二阶导数存在。

#### 20.4.2 多元Taylor展开与余项

1. 说明把多坐标同时改变的位移看作线段上的参数变化，沿线段用一元Taylor公式：一次项给出切平面，二次项为Hessian二次型补上弯曲；带Lagrange余项得中间点形式，再借二阶偏导数在基点的连续性得小量形式。

2. 定理`thm:multivariable-second-order-taylor`（式`eq:analysis-second-order-taylor`、`eq:analysis-second-order-local-model`）及证明：用方向导数公式两次算出$\phi'$与$\phi''=\bm h^\top\nabla^2f(\bm x+t\bm h)\bm h$，用Lagrange余项得第一式；再由中间点到基点的距离不超过$\lVert\bm h\rVert_2$、Hessian连续及$|\bm h^\top\bm B\bm h|\leq\lVert\bm B\rVert_F\lVert\bm h\rVert_2^2$得第二式。

3. 由中间点位置一般无法确定，写出一元Taylor公式的积分余项形式$\phi(1)=\phi(0)+\phi'(0)+\int_0^1(1-t)\phi''(t)\,\mathrm dt$，说明它由基本定理与分部积分得到（跨卷引用卷一“一元函数的积分”章）；代入$\phi',\phi''$得积分形式，解释权重$1-t$使靠近起点的曲率贡献更多，它与中间点形式描述同一有限变化。

###### paragraph：局部展开与有限误差

1. 说明小量形式只是局部结论，不给出指定有限扰动的数值误差界；在线段邻域内$C^3$且三阶方向导数受$M_3\lVert\bm h\rVert_2^3$控制时，由一元Taylor公式得二阶截断误差不超过$\tfrac{M_3}6\lVert\bm h\rVert_2^3$，并指出仅凭一点处的二阶导数得不到这样的界。

2. 示例`ex:multivariable-exponential-taylor`：$e^{x+y}$在原点的二次项为$(h+k)^2$，取$h=k=0.1$时切平面误差约$0.021$、加二次项后约$0.0014$，三阶界约$0.0016$与实际误差同量级。

3. 解释二次项补上沿位移方向的弯曲，混合项$2hk$说明坐标间相互作用不能由分别展开再相加恢复，更高阶项由多线性微分作用于重复方向给出。

#### 20.4.3 驻点的二阶判别

1. 说明Taylor公式把增量写成梯度项、Hessian二次型与高阶余项之和，因而梯度与Hessian的条件可转化为极值结论；回顾局部极值与严格局部极值的定义，限定只考察开集内部的点、不涉及约束。

###### paragraph：局部极值的一阶必要条件

1. 由过极值点的任意直线上该点仍是一元极值点及Fermat条件，几何上切平面水平；定理`thm:multivariable-extremum-first-order`（式`eq:analysis-first-order-necessary`）及证明：每个方向导数为零，取坐标方向得梯度为零。

2. 定义驻点，用$x^2-y^2$在原点沿$x$轴最低、沿$y$轴最高说明驻点未必是极值点，区分这些情形需要二阶信息。

###### paragraph：局部极值的二阶必要条件

1. 说明极小点处函数不能沿任何方向向下弯；定理`thm:multivariable-extremum-second-order`（式`eq:analysis-second-order-necessary`）及证明：沿每个方向用一元二阶必要条件，并回用Taylor定理证明中算出的$\phi''(0)$，得Hessian半正定（极大时半负定）。

2. 用$x^4$、$-x^4$、$x^3$在$0$处一、二阶导数都为零却分别为极小、极大与非极值，说明必要条件不能单独决定驻点类型，二次型为零的方向须检查更高阶项。

###### paragraph：驻点的二阶充分条件

1. 说明各非零方向二次型严格为正时函数沿所有方向向上弯，高阶余项不改变充分小扰动下增量的符号；强调需要正定而不只是半正定。

2. 定理`thm:multivariable-hessian-classification`及证明：正定时在单位球面上由极值定理（定理`thm:multivariable-extreme-value`）取得共同正下界$\lambda$，并按实对称谱分解展开说明它就是最小特征值，再由Hessian连续性选小球使中间点Hessian与基点之差不超过$\lambda/2$，得增量不小于$\tfrac\lambda4\lVert\bm h\rVert_2^2$；负定对$-f$同理；不定时沿使二次型为正、为负的两个方向用小量形式比较符号。 图`fig:analysis-process-hessian-local-shapes`对照$x^2+2y^2$、$x^2-y^2$、$x^4+y^4$三种形状：前两者由正定与不定判定，第三者Hessian为零却严格极小，零Hessian也可能无极值（如$x^3$），说明退化不是一种确定分类。图接在判别定理之后、证明之前。

3. 定义鞍点并以$x^2-y^2$的Hessian$\operatorname{diag}(2,-2)$为例；指出半定且有零方向时二阶判据可能无结论，边界点（如$x$在$[0,1]$上的最小点$0$）梯度可不为零，受约束问题需可行方向与乘子条件（交叉引用卷五约束优化与对偶章）。

4. 归纳判别两步：先解$\nabla f=\bm0$找驻点，再检查Hessian定性；示例`ex:multivariable-stationary-point-classification`：$x^3-3x+y^2$的驻点$(1,0)$为严格局部极小点、$(-1,0)$为鞍点，并由沿负$x$轴$f\to-\infty$说明局部极小不等于全局最小。

### 20.5 本章小结

1. 回顾研究对象：标量场、向量场与一般向量值函数；极限与连续按范数理解，输出可逐分量判断而输入坐标不能拆开，路径检验只能否定极限。

2. 归纳偏导数、方向导数与全微分的关系：可微要求所有小扰动共用一个线性近似并由偏导数唯一确定；偏导数存在、方向导数存在或连续都不单独保证可微，偏导数连续是充分而非必要的条件。

3. 归纳全微分与梯度：梯度是全微分在所选内积下的表示，改变内积改变梯度坐标与最陡方向；中值公式沿含于定义域的线段控制有限变化，凸开集上梯度上界即Lipschitz常数，凸性不能省略。

4. 归纳向量输出：Jacobian的行是分量梯度、列是输入坐标的推动，复合按顺序相乘，梯度由伴随传回；向量增量没有共同中值点，改用积分表示与算子范数。

5. 归纳高阶微分：混合偏导连续时可交换，Hessian对称；开集内驻点处正定、负定、不定分别给出严格极小、严格极大与鞍点，半定退化情形与边界、约束问题不在此判别范围。

6. 指出这些结论都是局部的，可微不说明给定步长下的误差；矩阵自变量的微分、隐式方程的解以及误差放大与一阶精度依次在后三章展开。

## 第21章 矩阵函数的微分

正文入口：[02-matrix-differentiation.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/02-matrix-differentiation.tex)（全章）。

1. 以线性层权重和协方差矩阵为例，说明损失是矩阵的标量函数，求逆、相乘又产生矩阵输出；提出本章问题：矩阵自变量的微分是什么形状的对象，标量输出的梯度怎样读出，常用运算的微分公式是什么、在哪里成立。

2. 说明可以拉直为长向量，但保留矩阵形状使乘法次序与迹的结构更清楚；矩阵空间有限维，本章不建新理论，只把全微分、链式法则与Riesz表示用于矩阵，集中处理形状、乘法不交换与结构约束。

3. 交代各节分工：21.1建立矩阵微分与Frobenius梯度并区分全部扰动与结构受限扰动；21.2—21.5依次处理基本运算、求逆、行列式与对数行列式，每种运算先定定义域与输入输出，再由增量的一阶项读出微分并验证可微。

4. 划定范围：本章只建立微分公式与梯度，一阶预测的精度与误差放大留到第23章；列出所用的第1章迹、行列式与逆矩阵，第3章Frobenius内积与Riesz表示，以及第17章逆矩阵的有限扰动界。

### 21.1 矩阵微分与梯度

1. 说明矩阵输入、输出按固定顺序拉直后即欧氏坐标空间，`sec:prelim-matrix-trace`的Frobenius内积与范数正是拉直后的欧氏内积与范数；限定定义域为全矩阵空间中的开集，全部充分小的同形扰动都可使用。

2. 给出矩阵映射可微的定义（余项按输出Frobenius范数），说明它是向量值可微性按矩阵形状重排的写法，计算时记$\mathrm d\Phi=\mathrm d\Phi_{\bm X}(\mathrm d\bm X)$；指出微分拉直后是$rs\times mn$的Jacobian，一般不能写成与$\bm X$同形的矩阵。

3. 区分按矩阵运算定义的映射（如$\bm X^{-1}$、$\bm X^2$，输出元素依赖许多输入元素）与逐元素作用（微分只在对应位置相乘），并指出`sec:ls-matrix-functions`沿谱构造的$f(\bm S)$属于前一类，但只是以矩阵为输入的映射中的一种，研究$\bm S\mapsto f(\bm S)$的微分时扰动一般不保持原特征方向。

###### paragraph：输入变量决定扰动的形状

1. 说明同一表达式随所选变量不同而微分输入不同：固定$\bm A$时$\bm x\mapsto\bm A\bm x$的扰动是向量，固定$\bm x$时$\bm A\mapsto\bm A\bm x$的扰动是矩阵；两者同时变化时在乘积空间取乘积范数，由精确增量中$\lVert\bm E\bm h\rVert_2\leq\tfrac12\lVert(\bm E,\bm h)\rVert^2$得联合微分$(\bm E,\bm h)\mapsto\bm A\bm h+\bm E\bm x$。

###### paragraph：标量输出与矩阵梯度

1. 说明标量输出的微分是矩阵空间上的线性泛函，由Riesz表示定理（定理`thm:ls-riesz-representation`）在Frobenius内积下唯一写成与同形矩阵的内积；给出矩阵梯度定义`def:multivariable-matrix-scalar-gradient`（式`eq:analysis-matrix-gradient-definition`），用单元素扰动说明其元素就是对相应元素的偏导数并得唯一性，在Frobenius长度下指出最快上升方向。

2. 给出求梯度的一般做法：展开微分，用迹的循环移位把扰动移到末端写成$\operatorname{tr}(\bm G^\top\mathrm d\bm X)$；强调循环移动整个因子而不能任意交换相邻矩阵，标量等于自身的迹。

3. 示例`ex:multivariable-bilinear-matrix-gradient`：$\bm a^\top\bm W\bm b$经迹的循环移位得梯度$\bm a\bm b^\top$，并逐元素核对偏导数$a_ib_j$。

###### paragraph：结构化变量的梯度

图解：`fig:v2-matrix-gradient-projection`。受限梯度是环境梯度$\bm G$到允许子空间$\mathcal S$的Frobenius正交投影。平面表示矩阵子空间，而非矩阵的二维数组；$\bm H\in\mathcal S$，故$\langle\bm G,\bm H\rangle_F=\langle P_{\mathcal S}\bm G,\bm H\rangle_F$。


1. 说明变量限于线性子空间$\mathcal S$（如对称矩阵空间）时只允许$\mathcal S$中的扰动，在$\mathcal S$上用Riesz表示得受限梯度；由$\bm G-P_{\mathcal S}\bm G$与$\mathcal S$正交（`sec:ls-orthogonal-projection`），受限梯度是环境梯度的正交投影；由对称与反对称矩阵Frobenius正交得对称投影$(\bm G+\bm G^\top)/2$，并指出在$\mathcal S$中沿用环境梯度时表示矩阵不唯一。

2. 由第~`chap:condition-and-spectral-perturbation`章的Weyl界说明对称正定矩阵组成对称子空间中的开集，讨论正定变量时邻域与扰动方向都在对称子空间内理解；矩阵输出时没有单个梯度矩阵，只能保留微分本身。

### 21.2 基本矩阵运算的微分

1. 导语说明从线性运算（余项为零）、乘法与平方（增量直接展开，余项可精确写出并据此验证可微）到迹、Frobenius范数平方与二次型（读出梯度）的顺序。

###### paragraph：线性运算

1. 说明加法、数乘、转置与迹是线性映射，精确增量即作用于扰动、余项为零，微分等于运算本身；固定矩阵两侧相乘给出$\mathrm d(\bm A\bm X\bm B)=\bm A(\mathrm d\bm X)\bm B$，扰动位置不能移动，复合按20.3.2的链式法则逐步核对形状。

2. 由线性迹函数无余项读出式`eq:analysis-trace-linear-gradient`即$\nabla_{\bm X}\operatorname{tr}(\bm A^\top\bm X)=\bm A$，与向量情形$\nabla(\bm a^\top\bm x)=\bm a$对应。

###### paragraph：乘积的精确增量

图解：`fig:v2-matrix-product-increment`。乘积增量的标量面积示意，取$A,B,E,H>0$。两条绿色边带各含一个扰动因子，黄色角块含两个扰动因子；去掉原来的蓝色面积后，留下$AH+EB+EH$。矩阵公式保留同样的项，但矩阵本身不解释为这些面积。


1. 由分配律写出对任意大小扰动成立的式`eq:multivariable-product-increment`；说明前两项对$(\bm E,\bm H)$线性并受乘积不等式控制，取联合范数后由Frobenius次乘性得交叉项$\bm E\bm H$为二次量，从而得到联合微分$\bm A\bm H+\bm E\bm B$，$\bm E\bm H$是精确余项；只固定一个因子时交叉项不出现。

2. 令两因子相同得$\mathrm d(\bm X^2)(\bm E)=\bm X\bm E+\bm E\bm X$，余项恰为$\bm E^2$；用$\bm X=\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]$、$\bm E=\left[\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right]$说明正确一阶项为$\bm I$而$2\bm X\bm E=\operatorname{diag}(2,0)$错误，并由$(\bm X+t\bm E)^2=t\bm I$直接核对。

###### paragraph：Frobenius范数平方与二次型

1. 由精确增量$2\langle\bm X,\bm E\rangle_F+\lVert\bm E\rVert_F^2$读出$\nabla_{\bm X}\lVert\bm X\rVert_F^2=2\bm X$与余项$\lVert\bm E\rVert_F^2$。

2. 以二次型$\bm x^\top\bm A\bm x$说明同一数组在固定线性作用与可变输入两种角色下导数不同：对$\bm x$的梯度为向量$(\bm A+\bm A^\top)\bm x$，对$\bm A$的梯度为矩阵$\bm x\bm x^\top$且无余项；两者同时变化时展开，括号中各项至少含两个扰动因子，联合微分是两个单独微分之和。

### 21.3 求逆的微分

1. 说明求逆定义在可逆方阵集合上、属于矩阵输出，没有单个梯度矩阵；回指`sec:prelim-inverse-matrices`与`sec:prelim-determinants`的逆矩阵和行列式非零的关系，约定矩阵范数取诱导范数（$\lVert\bm I\rVert=1$且满足乘积不等式）。

###### paragraph：由逆差恒等式得到微分

1. 在$q=\lVert\bm A^{-1}\rVert\lVert\bm E\rVert<1$下回用`sec:ls-inverse-sensitivity`的结论：$\bm B=\bm A+\bm E$可逆，逆差满足精确恒等式`eq:ch06-inverse-finite-perturbation`，且逆差范数不超过$\lVert\bm A^{-1}\rVert^2\lVert\bm E\rVert/(1-q)$；由此可逆矩阵组成开集，求逆连续。

2. 把恒等式右端的$\bm B^{-1}$换成$\bm A^{-1}$得到线性候选项$-\bm A^{-1}\bm E\bm A^{-1}$，替换误差为$-(\bm B^{-1}-\bm A^{-1})\bm E\bm A^{-1}$，由连续性是$o(\lVert\bm E\rVert)$，借范数等价得式`eq:analysis-inverse-differential`；说明导数以矩阵方向为输入、输出同形方阵，不能写成单个梯度矩阵，并预告23.2.2写出精确余项与二次界。

3. 说明先由精确恒等式确认可微后，再对$\bm X\bm X^{-1}=\bm I$求微分只作交叉核对，这种形式推导以可微为前提。

1. 指出$1\times1$时回到$-1/x^2$，两个逆位于扰动两侧，不能合并为$-\bm X^{-2}\mathrm d\bm X$。

2. 示例`ex:analysis-noncommuting-inverse-differential`：$\bm X=\operatorname{diag}(2,1)$、扰动为交换矩阵时正确导数为$\left[\begin{smallmatrix}0&-1/2\\-1/2&0\end{smallmatrix}\right]$，错误写法得非对称矩阵，直接对$(\bm X+t\bm E)^{-1}$求导核对；说明路径由对称可逆矩阵组成，导数必须对称，这种结构检查能发现错误。

3. 由链式法则写出可逆矩阵沿可微参数曲线变化时$\tfrac{\mathrm d}{\mathrm dt}\bm A(t)^{-1}=-\bm A^{-1}\bm A'\bm A^{-1}$，说明21.5与第23章沿扰动线段求导时会用到它。

### 21.4 行列式的微分

1. 说明行列式的绝对值是体积缩放倍数，按排列展开是元素的多项式，因而在包括奇异矩阵的全部方阵上连续可微；本节由逐列展开算出微分，再在可逆时化为迹的形式。

###### paragraph：代数余子式形式

1. 利用行列式对每列线性逐列展开$\det(\bm a_1+\bm e_1,\ldots,\bm a_d+\bm e_d)$为$2^d$项：恰有一列取扰动的项按该列展开（`sec:ls-det-cofactor-adjugate`）给出$\sum_iE_{i,j}C_{i,j}$，至少两列取扰动的项是二次以上的多项式，在$\lVert\bm E\rVert_F\leq1$时受常数乘$\lVert\bm E\rVert_F^2$控制；得式`eq:multivariable-determinant-cofactor-differential`，梯度为代数余子式矩阵$\bm C$，奇异处同样成立。

2. 可逆时由古典伴随恒等式（定理`thm:ls-adjugate-identity`）得Jacobi公式$\mathrm d\det\bm X=\det\bm X\operatorname{tr}(\bm X^{-1}\mathrm d\bm X)$与梯度$\det(\bm X)\bm X^{-\top}$，解释为有向体积缩放倍数的相对变化；用乘法公式化归到$\det(\bm I+\bm X^{-1}\bm H)$核对，并说明奇异处只能用代数余子式形式。

3. 示例`ex:multivariable-determinant-near-identity`：对角扰动的一阶变化为$\varepsilon_1+\varepsilon_2=\operatorname{tr}\bm H$，剪切扰动面积不变且迹为零；解释面积的相对增量一阶上是伸长率之和。

### 21.5 对数行列式的微分

1. 说明$\det>0$的方阵组成开集，对数与行列式在其上复合，由$\mathrm d\log u=\mathrm du/u$得式`eq:analysis-logdet-gradient`，借式`eq:analysis-matrix-gradient-definition`读出梯度$\bm X^{-\top}$；对称时化为$\bm X^{-1}$，$1\times1$时回到$(\log x)'=1/x$。

###### paragraph：对称正定变量

1. 说明统计与优化中常见对称正定矩阵上的$\log\det$，只允许对称扰动；由21.1受限梯度是环境梯度$\bm A^{-1}$在对称子空间上的投影，它本身对称，故梯度为$\bm A^{-1}$。

2. 区分两个定义域：$\det>0$的方阵是全矩阵空间中的开集，式`eq:analysis-logdet-gradient`在其上处处成立；对称正定矩阵是对称子空间中的开集。说明正定性不是可微的条件，只决定允许方向与梯度表示，并预告23.2.4估计有限扰动的余项时正定性还保证整条线段留在定义域内。

### 21.6 本章小结

1. 归纳矩阵微分的形状：标量输出时Riesz表示给出同形的Frobenius梯度，常用写成$\operatorname{tr}(\bm G^\top\mathrm d\bm X)$读出；矩阵输出时只能保留微分本身；结构子空间上受限梯度是环境梯度的正交投影，对称情形为$(\bm G+\bm G^\top)/2$。

2. 归纳各运算的公式与条件：线性运算的微分是运算本身；乘积的微分是只变一个因子的两项之和，平方的微分不是$2\bm X\mathrm d\bm X$；求逆在可逆开集上可微，扰动夹在两个逆之间；行列式在全部方阵上可微，由代数余子式给出，可逆时化为Jacobi公式；对数行列式在$\det>0$的开集上可微，梯度为$\bm X^{-\top}$。

3. 强调所有公式先由一阶项识别、再由余项验证可微，对恒等式形式求导只作核对；精确余项在本章只用于证明可微，第23章再用这些公式估计条件数与有限扰动下的预测误差。

## 第22章 隐函数与反函数

正文入口：[03-implicit-inverse-functions.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/03-implicit-inverse-functions.tex)（全章）。

1. 说明前面各章对显式映射求微分，本章反过来从方程出发，判断方程能否在基点附近确定唯一函数并求其导数。

2. 以单位圆、力的平衡方程与梯度为零的最优参数为例，提出参数稍变时未知量是否唯一、光滑地随之改变以及变化率是多少的问题。

3. 说明方程组用向量值映射表示，方程数与待解变量数相同时关于待解变量的方阵Jacobian是否可逆决定能否局部解出；交代22.1先用例子说明起始解与导数条件，再用压缩迭代证明存在、唯一与可微并给出导数公式，22.2由隐函数定理得到局部反函数定理并说明局部可逆不推出整体单射。

4. 列出所用的第20章链式法则、向量值中值估计与压缩，以及第3章有限维完备性；指出隐式给定的谱分支对扰动的响应在第23章用本章定理分析。

### 22.1 隐函数的存在与微分

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

2. 说明导数要在选定分支上取值；$y_0\to0$时$-x_0/y_0$趋于无穷，与$(1,0)$处竖直切线及示例`ex:multivariable-implicit-circle`一致；曲线切向量$(1,-x_0/y_0)^\top$与梯度$(2x_0,2y_0)^\top$正交，回应20.2.4，梯度非零正是所需非退化条件。

3. 提醒Jacobian奇异时定理不能直接使用：既不能断言不存在可微分支，也不能默认分支仍唯一光滑，须另行分析。

###### paragraph：与线性解映射的一致性

1. 在有显式解的线性方程上核对：把$(\bm A,\bm b)$看作参数、$\bm x$看作未知量，令$F=\bm A\bm x-\bm b$，关于未知量的Jacobian为可逆的$\bm A$，关于参数的微分为$\bm E\bm x-\bm f$，由式`eq:analysis-implicit-derivative`得$(\bm E,\bm f)\mapsto\bm A^{-1}(\bm f-\bm E\bm x)$；再对显式解$\bm A^{-1}\bm b$用乘积法则与求逆的微分`eq:analysis-inverse-differential`算出同一结果。

2. 说明这里只是核对，线性方程的可微性由显式公式直接得到；特征方程$\bm S\bm v=\lambda\bm v$一般没有显式公式，须先用隐函数定理证明局部分支存在且可微，引出23.3。

### 22.2 反函数的局部存在与微分

1. 提出反求输入的问题：已知输出能否唯一确定输入且随输出光滑变化，以由直角坐标反求极坐标为例；由线性映射可逆当且仅当方阵可逆，期待Jacobian可逆时局部可逆，并把$G(\bm x)-\bm y=\bm0$看成以输出为参数、输入为待解变量的隐函数问题，强调只得到两个邻域之间的逆。

2. 定理`thm:multivariable-inverse-function`及证明：对$H(\bm y,\bm x)=G(\bm x)-\bm y$用隐函数定理得局部解映射$\varphi$，缩小邻域使Jacobian在其中可逆，取$U_0=W\cap G^{-1}(V_0)$并验证$G:U_0\to V_0$是以$\varphi$为逆的双射，最后对$G(\varphi(\bm y))=\bm y$用链式法则得逆的Jacobian；解释逆映射的局部伸缩抵消原映射的局部伸缩。

3. 示例`ex:multivariable-polar-local-inverse`：由示例`ex:multivariable-polar-jacobian`的$\det\bm J_P=r$知$r>0$处可局部反求；在$(2,\pi/2)$即点$(0,2)$处求得逆Jacobian，解释$\mathrm dr=\mathrm dy$与$\mathrm d\theta=-\mathrm dx/2$。

4. 指出$r=0$处Jacobian行列式为零、所有$\theta$都映到原点，确实无法反求$\theta$，正是定理条件不满足之处。

###### paragraph：局部可逆与整体单射

图解：`fig:v2-local-inverse-covering`。映射$g(u,v)=(e^u\cos v,e^u\sin v)$的重复覆盖。左侧蓝、绿矩形具有相同的$u$范围，$v$范围相差$2\pi$；右侧表示它们共同的扇环像。位置与宽度为示意，不按两边的坐标比例绘制。处处非奇异的Jacobian保证局部可逆，却不消除周期造成的整体多对一。


1. 说明局部反函数定理是局部结论；示例`ex:multivariable-local-not-global-inverse`：$g(u,v)=(e^u\cos v,e^u\sin v)^\top$的Jacobian行列式$e^{2u}>0$处处可逆，但$(u,v)$与$(u,v+2\pi)$输出相同，不是单射；解释它是半径取$e^u$的极坐标映射，沿$v$方向每隔$2\pi$重复覆盖。

2. 反方向用$x^3$说明全局单射且逆连续也不保证逆可微，对应导数为零、定理条件不满足；提醒邻域、可微性与Jacobian可逆性都要逐项检查，24.3用坐标变换计算区域积分时还须检查区域上的一一对应、光滑性与边界处理，不能仅凭一点处Jacobian非零换元。

### 22.3 本章小结

1. 归纳隐式解的两个前提：指定起始解，检查关于待解变量的Jacobian可逆；线性方程说明条件的来源；隐函数定理在连续可微与Jacobian可逆下给出唯一的连续可微局部解分支与导数$-(\bm D_{\bm y}F)^{-1}\bm D_{\bm x}F$。

2. 回顾证明把解方程改写为固定斜率的修正迭代并依次核对压缩、自映射与随参数可微；强调存在与唯一是定理的困难部分，形式求导只在分支已知可微时给出导数。

3. 说明反函数定理是同一机制的特例，Jacobian可逆时局部可逆、逆的Jacobian为原Jacobian的逆；可逆Jacobian在两类问题中都保证线性近似可唯一反解。

4. 强调结论的局部性：唯一性只限于邻域，Jacobian处处可逆仍可能不整体单射，Jacobian奇异时定理不作结论；换元还须检查整个区域的一一对应；解分支的响应大小与一阶近似可靠性由下一章讨论。

## 第23章 微分与扰动分析

正文入口：[04-differential-perturbation-analysis.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/04-differential-perturbation-analysis.tex)（章首）；章内依次输入[01-general-maps.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/04-differential-perturbation-analysis/01-general-maps.tex)（23.1）、[02-matrix-operations.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/04-differential-perturbation-analysis/02-matrix-operations.tex)（23.2）、[03-eigen-differentials.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/04-differential-perturbation-analysis/03-eigen-differentials.tex)（23.3）与[04-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/04-differential-perturbation-analysis/04-summary.tex)（23.4）。

1. 以测量、舍入与数据误差进入，回顾第9章不借助微分直接比较精确变化、对一切方向取最坏情形的条件数与有限扰动界，又指出前三章的微分把变化分成一阶响应与余项；提出三个问题：指定方向的一阶响应、最坏方向的放大倍数、有限步长下线性预测的误差。

2. 交代23.1对一般可微映射回答后两个问题：局部条件数由有限变化定义、可微时等于微分在允许子空间上的算子范数；余项界需要导数沿整条线段的变化；这一节建立不依赖具体运算的方法。

3. 交代23.2调用第21章的微分与精确增量逐个估计矩阵运算的响应、条件数与余项并检查线段留在定义域内，23.3用第22章隐函数定理处理没有显式公式的谱分支并说明一阶近似何时可靠。

4. 划定范围：有限扰动界以第9章为准，逆矩阵与方程解的完整误差分析以第17章为准；本章只补充指定方向的一阶响应及其有限步长精度，不重复稳定性证明，也不评价算法。

### 23.1 一般映射的扰动分析

1. 以输入误差引起的输出偏离进入，写出$\Delta F=\mathrm dF_{\bm x}(\bm h)+R_{\bm x}(\bm h)$，提出最坏方向的一阶放大与有限步长下的预测误差两个问题；前者由微分的算子范数回答，后者要控制导数沿扰动线段的变化。

2. 说明输入、输出取有限维赋范空间（如某种范数下的$\mathbb R^d$或按元素排成坐标的矩阵空间），由范数等价（定理`thm:ls-norm-equivalence`）可微与否不依赖范数，只有算子范数的数值依赖。

#### 23.1.1 局部条件数与导数范数

1. 回顾第9章的结论：固定矩阵的线性作用中误差比只依赖方向，取上确界得到放大倍数$\lVert\bm A\rVert$，相对误差的最坏放大不超过$\kappa(\bm A)$（`sec:ls-perturbation-conditioning`），对任意大小的扰动都成立。

2. 说明一般映射的误差比随扰动大小变化，所以先在半径$\delta$内取最坏情形再令半径缩小。

3. 给出局部条件数定义`def:multivariable-local-condition-number`，说明内层上确界随$\delta$减小而不增，极限在$[0,\infty]$中存在；定义只用有限变化、不要求可微，也不同于沿某个给定方向的响应。

4. 定理`thm:multivariable-local-condition-number`及证明：可微时局部条件数等于微分限制在$\mathcal E$上的算子范数；记余项比的上确界为$\eta(\delta)\to0$，用三角不等式得上界$N+\eta(\delta)$，取达到算子范数的单位方向（`sec:ls-matrix-norms`）并用反向三角不等式得下界$N-\eta(\delta)$，夹逼得结论。说明结构化扰动时最坏方向限于允许子空间，数值一般不大于无结构情形。

###### paragraph：相对条件数

1. 在参照量非零时乘以输入尺度、除以输出尺度定义相对条件数，衡量相对扰动在一阶上的放大倍数。

2. 对线性作用$\bm A\bm x$说明余项为零，绝对条件数为$\lVert\bm A\rVert$，相对条件数$\lVert\bm A\rVert\lVert\bm x\rVert/\lVert\bm A\bm x\rVert$在可逆时不超过$\kappa(\bm A)$，回到`sec:ls-matrix-condition-number`的精确结论。

3. 区分三个易混的量：矩阵条件数$\kappa(\bm A)$是对全部输入的统一上界，固定输入处的相对条件数只涉及这一点，矩阵函数（如求逆）以矩阵为输入的条件数留给第21章计算；指出它们都描述问题本身的敏感性，与算法稳定性的分工见`sec:ls-numerical-stability`。

###### paragraph：有限条件数而不可微

图解：`fig:v2-ordered-eigenvalue-kink`。$\bm S(t)=\operatorname{diag}(t,-t)$。左图为未排序分支$t$与$-t$，右图为最大特征值$|t|$。两侧斜率在零点不同，但函数仍为$1$-Lipschitz，零点的局部绝对条件数仍为$1$。


1. 反例：$\bm S(t)=\operatorname{diag}(t,-t)$排序后的最大特征值为$|t|$，由Weyl界（定理`thm:ls-weyl-eigenvalue`）有限变化受控，在$0$处局部条件数为$1$，却没有双侧导数；解释失去可微性的是“排序取最大”这一步，未排序的分支$t,-t$光滑并在$0$处相交，23.3将在特征值简单时证明所选局部分支可微。

2. 反方向说明局部条件数为零不表示输出不变：$t^2$在$0$处条件数为$0$，有限步长仍有变化$t^2$，被一阶分析遗漏的部分留给下一小节的余项界。

#### 23.1.2 一阶近似的余项界

1. 说明可微只保证余项为$o(\lVert\bm h\rVert)$，得到有限扰动的数值误差界需要知道导数沿线段怎样变化；约定本小节输入输出取欧氏范数、矩阵空间取Frobenius范数、导数用谱范数，其他范数借范数等价改变常数。

2. 在含线段的开集上连续可微时，从式`eq:multivariable-vector-integral-increment`中扣除常向量$\bm J_F(\bm x)\bm h$，得余项的精确积分表示式`eq:multivariable-remainder-integral`；对照完整增量由导数大小控制、余项由导数相对基点的变化控制，说明导数大而变化慢时增量大而一阶预测仍准确。

3. 定理`thm:multivariable-first-order-remainder-bound`及证明：Jacobian相对基点满足$L$倍的Lipschitz型界时，对积分表示取范数得余项不超过$\tfrac L2\lVert\bm h\rVert_2^2$；指出定理不以二阶导数存在为前提，凸邻域内Jacobian以$L$为Lipschitz常数即满足假设，20.4将说明二阶导数统一界是取得$L$的一种充分办法。

4. 说明上界正比于步长平方只表示所保证误差的量级，实际误差可能远小于上界；以对称二次型为例，定理给出的$\lVert\bm S\rVert_2\lVert\bm h\rVert_2^2$与20.2.3由精确增量得到的界一致。

###### paragraph：三种保证的分工

1. 归纳可微给出步长趋零时的$o(\lVert\bm h\rVert)$，导数的Lipschitz界给出带明确常数的二次余项，20.3.3的导数界控制整个有限变化。

2. 提醒使用后两者前须检查扰动线段留在定义域内、可逆或正定等结构条件在整条线段上保持、常数在该范围内统一成立；矩阵映射的检查可借第9章的Weyl界与奇异值扰动界、`sec:ls-inverse-sensitivity`的逆矩阵有限界完成，基点条件数不能代替这些检查，并引出下一节对各矩阵运算逐一完成它们。

### 23.2 矩阵运算的扰动分析

1. 说明第21章已求出微分并验证可微，本节回到误差问题：矩阵数据带扰动时线性预测在有限步长下有多准、误差在最坏方向上放大多少。

2. 列出每种运算要同时检查的三件事（输出类型与误差尺度、扰动结构、线段是否留在定义域内），并约定矩阵范数取满足乘积不等式的范数，求逆时取诱导范数。

#### 23.2.1 基本矩阵运算的增量与余项

1. 说明21.2的精确增量都是扰动的多项式，余项直接从增量中读出，再用范数控制大小。

###### paragraph：线性运算

1. 说明加法、数乘、转置、迹与$\bm X\mapsto\bm A\bm X\bm B$的余项恒为零，线性预测在任意步长下精确，由定理`thm:multivariable-local-condition-number`局部绝对条件数就是运算本身的算子范数且与基点无关。

2. 举例：Frobenius范数下转置的条件数为$1$；由$|\operatorname{tr}\bm E|\leq\sqrt d\lVert\bm E\rVert_F$且$\bm E=\bm I/\sqrt d$取等号，迹的条件数为$\sqrt d$，对角元误差同号时会累加。

###### paragraph：乘积与平方

1. 由式`eq:multivariable-product-increment`写出乘积的余项$\bm E\bm H$，给出一阶项不超过$\lVert\bm A\rVert\lVert\bm H\rVert+\lVert\bm E\rVert\lVert\bm B\rVert$、余项不超过$\lVert\bm E\rVert\lVert\bm H\rVert$，说明扰动不超过$\rho$时一阶项至多与$\rho$同阶、余项至多$\rho^2$；平方的余项恰为$\bm E^2$。

2. 把这些界用作误差预算：绝对误差不超过$\tau$时，两个扰动同样大小的步长不超过$\sqrt\tau$即可；若要求余项不超过一阶项的比例，还要知道一阶项在所取方向上的大小。

3. 示例`ex:multivariable-square-first-order-check`：$\bm X=\operatorname{diag}(2,1)$、$\bm E=\varepsilon\bm K$（$\bm K$为交换矩阵）时一阶项谱范数$3\varepsilon$、余项$\varepsilon^2$，$\varepsilon=0.1$时余项约为一阶项的$3\%$，要求不超过$1\%$则须$\varepsilon\leq0.03$。

###### paragraph：Frobenius范数平方与二次型

1. 说明Frobenius范数平方的余项恰为$\lVert\bm E\rVert_F^2$，而一阶项$2\langle\bm X,\bm E\rangle_F$可为零，此时线性预测说没有变化而实际变化为$\lVert\bm E\rVert_F^2$，应直接给出绝对误差预算。

2. 给出二次型在矩阵与向量同时扰动时余项的谱范数上界，指出每项含两个扰动因子，交叉项还乘基点大小$\lVert\bm x\rVert_2$。

3. 比较线性运算的零余项与多项式运算可精确写出的高次余项，说明误差预算由高次项决定可用步长，导数大小只决定一阶项。

#### 23.2.2 求逆的扰动

1. 说明21.3只用到余项为$o(\lVert\bm E\rVert)$，本节精确写出余项、给出二次界，再计算条件数并联系线性方程的解映射。

###### paragraph：精确余项与可逆邻域

1. 在$q<1$下由逆差恒等式代入两次得到一阶预测$-\bm A^{-1}\bm E\bm A^{-1}$与精确余项$\bm B^{-1}\bm E\bm A^{-1}\bm E\bm A^{-1}$，由$\lVert\bm B^{-1}\rVert\leq\lVert\bm A^{-1}\rVert/(1-q)$得二次界`eq:multivariable-inverse-remainder-bound`。

2. 借第10章的Neumann级数另证：写$\bm B=\bm A(\bm I-\bm T)$、$\bm T=-\bm A^{-1}\bm E$，由定理`thm:ls-neumann`展开$\bm B^{-1}$，前两项即一阶预测，截断误差界`eq:ls-neumann-tail`取$N=1$给出同一余项界，并说明余项依次由二次、三次……项组成。

###### paragraph：一阶预测的误差

1. 说明式`eq:multivariable-inverse-remainder-bound`同时是有限扰动下一阶预测的误差界，并由$\lVert\bm A^{-1}(t\bm E)\rVert\leq tq<1$确认整条扰动线段可逆；比较`sec:ls-inverse-sensitivity`控制的全变化与$\lVert\bm E\rVert$同阶，本段扣除一阶项后的误差与$\lVert\bm E\rVert^2$同阶，$q$接近$1$时一阶预测不再可靠。

2. 示例`ex:multivariable-inverse-first-order-check`：$\bm A=\operatorname{diag}(2,1)$、对称非对角扰动$0.1$，在谱范数下$q=0.1$，实际误差谱范数约$0.00505$，余项上界约$0.0111$，全变化约$0.0540$而全变化界约$0.111$；解释一阶预测扣除了约$0.05$的主要部分，余项界只保证误差不超过多少。

###### paragraph：求逆的条件数

1. 在无结构扰动与谱范数下，由乘积不等式得一阶响应不超过$\lVert\bm A^{-1}\rVert_2^2\lVert\bm E\rVert_2$，取最小奇异值的奇异向量（`sec:ls-svd`）构造$\bm E=\bm u_d\bm v_d^\top$使其达到；由定理`thm:multivariable-local-condition-number`得绝对条件数$\lVert\bm A^{-1}\rVert_2^2$与相对条件数$\kappa_2(\bm A)$。

2. 说明矩阵条件数在此重现但输入是矩阵本身，与`sec:ls-matrix-condition-number`输入为向量不同；结构化扰动须改用允许子空间上的范数；求解算法与数值稳定性仍按第17章处理。

###### paragraph：线性方程的解映射

1. 把求逆与乘法复合得解映射$\operatorname{sol}(\bm A,\bm b)=\bm A^{-1}\bm b$，定义在可逆$\bm A$与任意$\bm b$组成的开集上；联合输入取乘积范数，回用`sec:ls-equation-sensitivity`的推导得精确式$\Delta\bm x=(\bm A+\bm E)^{-1}(\bm f-\bm E\bm x)$。

2. 把$(\bm A+\bm E)^{-1}$拆成$\bm A^{-1}$与逆差，第一项线性，第二项由逆差界与$\lVert\bm f-\bm E\bm x\rVert$的估计为联合扰动的二次量，得式`eq:multivariable-solution-map-differential`；再用乘积的联合微分与式`eq:analysis-inverse-differential`按链式法则核对，并回指22.1已用隐函数公式核对同一结果。

3. 区分`sec:ls-equation-sensitivity`控制完整解误差与这里的一阶预测，指出预测误差是联合扰动的二次量；数据误差、残差与算法稳定性的完整分析仍以第17章为准。

#### 23.2.3 行列式的扰动

1. 说明21.4逐列展开中至少含两列扰动的高阶项就是线性预测的误差，对包括奇异矩阵在内的全部方阵有意义，故先讨论绝对误差、再在可逆时讨论相对误差。

###### paragraph：绝对变化的余项

1. 在有界邻域$K=\{\bm A+\bm F:\lVert\bm F\rVert_F\leq1\}$上由多项式二阶偏导数有界取常数$M$，令$g(t)=\det(\bm A+t\bm E)$，由$|g''|\leq M\lVert\bm E\rVert_F^2$及一元Taylor公式得二次余项界，常数依赖所取邻域。

2. 在二阶情形精确写出$\det(\bm A+\bm E)=\det\bm A+\langle\bm C,\bm E\rangle_F+\det\bm E$，由$|ab|\leq(a^2+b^2)/2$得余项$|\det\bm E|\leq\lVert\bm E\rVert_F^2/2$，与基点无关，奇异的$\bm A$也适用。

###### paragraph：条件数与相对变化

1. 由定理`thm:multivariable-local-condition-number`，局部绝对条件数是线性泛函$\bm E\mapsto\langle\bm C,\bm E\rangle_F$的对偶范数（`sec:ls-dual-norms`），Frobenius范数下由Cauchy--Schwarz得$\lVert\bm C\rVert_F$；可逆时由$\bm C=\det(\bm A)\bm A^{-\top}$得相对条件数$\lVert\bm A^{-1}\rVert_F\lVert\bm A\rVert_F$，奇异处只有绝对变化有定义。

2. 示例`ex:ls-determinant-near-singular`：$\operatorname{diag}(1,\varepsilon)$沿$\operatorname{diag}(0,\delta)$扰动时行列式相对变化为矩阵相对变化的$1/\varepsilon$倍，微分给出同一结果且余项为零，说明越接近奇异沿该方向的相对放大越强。

3. 用$\varepsilon\bm I$说明行列式$\varepsilon^d$可以极小，而求逆的相对条件数为$1$、行列式自身的相对条件数为$d$，均不随$\varepsilon$变大；结论是行列式与逆矩阵是不同的输出，绝对与相对是不同尺度，须分别判断。

#### 23.2.4 对数行列式的扰动

1. 回指21.5的微分，写出一阶变化$\operatorname{tr}(\bm A^{-1}\bm E)+o(\lVert\bm E\rVert_F)$，说明局部绝对条件数是相应线性泛函的对偶范数，Frobenius范数下为$\lVert\bm A^{-1}\rVert_F$；对数行列式可为零或接近零，这时应比较绝对变化。

###### paragraph：整条线段的定义域

1. 说明把一阶预测用于有限扰动前须保证整条线段$\bm A+t\bm E$留在定义域内：一般正行列式矩阵由连续性只知存在足够小的邻域而不知其大小，正定情形可用第4、7章的最小特征值界明确检查，下面的余项界基于这一检查。

###### paragraph：二次余项界

1. 设$\bm A$对称正定、最小特征值$m$，对称扰动满足$\lVert\bm E\rVert_2<m$，由任意单位向量上的二次型下界$\bm x^\top(\bm A+t\bm E)\bm x\geq m-\lVert\bm E\rVert_2$说明整条线段正定且最小特征值不小于$m-\lVert\bm E\rVert_2$；令$g(t)=\log\det(\bm A+t\bm E)$，由式`eq:analysis-logdet-gradient`与沿参数曲线的求逆公式算出$g''$，再用Frobenius内积的Cauchy--Schwarz与混合乘积界式`eq:matrix-analysis-mixed-submultiplicativity`估计$|g''|$，由一元Taylor公式得余项不超过$\lVert\bm E\rVert_F^2/(2(m-\lVert\bm E\rVert_2)^2)$。

2. 示例：$\operatorname{diag}(2,1)$加$\operatorname{diag}(0.1,0)$时一阶预测$0.05$、实际$\log1.05\approx0.04879$，实际误差约$0.00121$、上界约$0.00618$；说明上界不表示误差接近它，导数、正定线段与余项界要一起使用，并指出正定条件只是这一显式估计的条件，而非$\log\det$的定义条件。

3. 解释分母$m-\lVert\bm E\rVert_2$是到奇异边界的余量：$\bm A$接近奇异时条件数$\lVert\bm A^{-1}\rVert_F\geq1/m$变大、余项界按$1/(m-\lVert\bm E\rVert_2)^2$放大，步长须小于$m$；以$\operatorname{diag}(1,\varepsilon)$加$\operatorname{diag}(0,\delta)$为例，精确变化$\log(1+\delta/\varepsilon)$与预测$\delta/\varepsilon$在$\delta$与$\varepsilon$同阶时相差显著。

### 23.3 特征值与特征向量的微分

1. 说明特征值与特征向量不是矩阵元素的显式函数；回顾第9章的有限扰动界（Weyl界`thm:ls-weyl-eigenvalue`与`sec:ls-subspace-sensitivity`的子空间偏转界）对一切方向取最坏情形。

2. 提出本节问题：沿指定方向的变化率是多少、在多大范围内可用于预测；交代先用第22章隐函数定理证明简单特征值分支可微，再分别求特征值与特征向量的微分，最后说明一阶近似的适用条件。

#### 23.3.1 特征值与特征向量的可微性

1. 设实对称矩阵$\bm S_0$有简单特征值$\lambda_0$与单位特征向量$\bm v_0$，解释简单指代数重数为$1$、对实对称矩阵等价于特征空间一维；由$\pm\bm v_0$代表同一方向，用$\bm v_0^\top\bm v>0$选定局部分支，并指出单位长度不保证全局唯一。

2. 以上三角元素为坐标把对称矩阵作为参数，把特征方程与单位长度条件写成$d+1$个方程、$d+1$个未知量；写出关于$(\bm v,\lambda)$的导数矩阵，用$\bm v_0^\top$左乘第一行得$\eta=0$、第二行得$\bm h\perp\bm v_0$，由特征值简单推出$\bm h=\bm0$，故矩阵可逆，隐函数定理给出可微分支。

3. 说明固定符号不可省略：不选定符号时沿路径任意切换$\pm\bm v_0$会使特征向量看似不连续，这是表示的不唯一而非方向的变化；选定$\bm v_0^\top\bm v>0$后分支在邻域内唯一，可微性才有确定含义。

#### 23.3.2 特征值的微分

1. 对特征方程与归一化条件求微分，用$\bm v_0^\top$左乘得$\mathrm d\lambda(\bm E)=\bm v_0^\top\bm E\bm v_0$；强调分支的存在由上一小节的隐函数定理保证，形式求导不能承担这一步。

2. 解释变化率只看扰动在特征方向上的读数，由$|\mathrm d\lambda(\bm E)|\leq\lVert\bm E\rVert_2$且$\bm E=\bm v_0\bm v_0^\top$时取等号，简单特征值分支的局部绝对条件数为$1$；满足$\bm E\bm v_0=\bm0$的扰动一阶上不改变该特征值。

3. 示例`ex:multivariable-eigenvalue-direction-check`：$\bm S_0=\operatorname{diag}(2,1)$，沿$\bm e_1\bm e_1^\top$特征值为$2+t$；沿交换矩阵方向公式给出零变化率，直接计算较大特征值为$2+t^2+O(t^4)$；两方向的Weyl界都只给$|t|$。

4. 比较两类结论：Weyl界是对一切方向、任意步长成立的最坏偏差，微分是指定方向的变化率，可远小于最坏情形但只在步长足够小时描述实际变化；用于有限扰动还须估计余项，引向23.3.4。

#### 23.3.3 特征向量的微分

1. 把$\mathrm d\lambda$代回后右侧与$\bm v_0$正交，由特征值简单，$\bm S_0-\lambda_0\bm I$在正交补上可逆，归一化条件选出唯一的$\mathrm d\bm v(\bm E)$。

###### paragraph：谱展开与谱隙

1. 在$\bm S_0$的标准正交特征基中把$\mathrm d\bm v(\bm E)$写成与$\bm v_i$正交的组合，逐个取内积得$\mathrm d\bm v(\bm E)=\sum_{j\neq i}\frac{\bm v_j^\top\bm E\bm v_i}{\lambda_i-\lambda_j}\bm v_j$。

2. 设$d\geq2$并定义谱隙$\gamma$，由Parseval等式得$\lVert\mathrm d\bm v(\bm E)\rVert_2\leq\lVert\bm E\rVert_2/\gamma$；$d=1$时特征向量分支不变、微分为零。

3. 把23.3.2的特征值导数界$|\mathrm d\lambda(\bm E)|\leq\lVert\bm E\rVert_2$与这里的特征向量导数界一起与`sec:ls-spectral-sensitivity`的Weyl界与谱隙界比较：后者控制有限扰动下的整体变化，这里给出带方向的一阶响应；特征值响应只看扰动在该特征方向上的读数，特征向量响应以$\lambda_i-\lambda_j$为分母，谱隙小时可被大幅转向相邻特征方向。

1. 示例`ex:multivariable-eigenvector-gap-check`：延续上例，沿交换矩阵方向得$\mathrm d\bm v=\bm e_2$，与直接算出的特征向量方向$(1,t+O(t^3))^\top$一致；基点换为$\operatorname{diag}(1+\gamma,1)$时响应为$\bm e_2/\gamma$，谱隙缩小几倍转向速率就放大几倍。

2. 说明有限扰动下的角度、投影距离与偏转界以第9章为准，定理`thm:ls-davis-kahan`给出$\sin\theta\leq\lVert\bm E\rVert_2/\gamma$型的界（谱隙按该定理在原矩阵与扰动后矩阵之间度量），与导数界形式相同，说明谱隙同时控制无穷小转向与有限偏转。

#### 23.3.4 一阶近似的适用条件

图解：`fig:v2-spectral-linear-range`。对$\left[\begin{smallmatrix}1+\gamma&t\\t&1\end{smallmatrix}\right]$且$\gamma>0$，较大特征值方向的转角为$\theta=\tfrac12\arctan(2t/\gamma)$，一阶预测为$t/\gamma$。横轴将扰动与谱隙同时纳入尺度；转角用弧度表示。


1. 说明前两小节的公式只在简单特征值附近、步长趋零时成立，用于有限扰动需要扰动相对谱隙足够小，并以上例的第二个基点精确计算。

2. 对$\begin{bmatrix}1+\gamma&t\\t&1\end{bmatrix}$算出特征向量夹角满足$\tan2\theta=2t/\gamma$，而一阶预测为$t/\gamma$：$|t|\ll\gamma$时一致，$t=\gamma/2$时实际为$\pi/8\approx0.39$而预测为$0.5$，固定$t$令$\gamma\to0$时实际趋于$\pi/4$而预测趋于无穷。

3. 对较大特征值$1+\gamma/2+\sqrt{\gamma^2/4+t^2}\approx1+\gamma+t^2/\gamma$指出一阶项为零、二阶系数$1/\gamma$随谱隙缩小而增大，得出一阶预测可靠的条件是扰动相对谱隙小。

4. 说明重特征值使关于未知量的导数不可逆，这条构造失效，但不断言每条特征值分支不可微，也不影响矩阵多项式或可逆点处求逆的光滑性；回指23.1.1的$\operatorname{diag}(t,-t)$排序后的特征值有有限条件数而不可微、未排序分支光滑；重特征值附近应改为考察特征子空间，其稳定性已在`sec:ls-subspace-sensitivity`处理。

5. 总结本节只界定简单谱分支何时可微、微分公式何时可作一阶近似，重根附近把相邻特征值合成隔离特征簇并直接使用第9章的子空间比较。

### 23.4 本章小结

1. 归纳一阶响应、局部条件数与余项分别回答的问题，指出条件数只描述无穷小扰动、可以有限而不可微或为零而有限变化不为零，余项界需要导数沿线段的Lipschitz型控制，二阶导数界是取得它的充分办法。

2. 比较显式矩阵运算与隐式谱分支共同的分析步骤：确定输出与误差尺度、限定扰动结构、检查线段留在定义域内，再读出响应与条件数并估计余项。

3. 逐项归纳矩阵运算的结论：线性运算零余项，乘积、平方、二次型的余项是可精确写出的高次项，求逆的余项界与相对条件数$\kappa_2(\bm A)$，行列式在奇异处也有绝对余项控制而相对条件数只在可逆时有意义，对数行列式在正定情形下借最小特征值保证线段正定且余项界随到边界的余量缩小而放大。

4. 归纳谱分支：由隐函数定理在简单特征值处可微，特征值变化率为$\bm v^\top\bm E\bm v$，特征向量变化率以特征值之差为分母，一阶预测可靠的条件是扰动相对谱隙小，重根附近改为比较特征子空间。

5. 对照第9章的稳定性保证与第17章的求解误差评价，说明本章补充指定方向的响应与有限步长精度，并强调保留定义域、结构、谱隙与相对尺度条件。

## 第24章 区域积分

正文入口：[05-region-integrals.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/05-region-integrals.tex)（章首）；章内依次输入[01-regional.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/05-region-integrals/01-regional.tex)（24.1—24.4）与[02-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/05-region-integrals/02-summary.tex)（24.5）。

1. 从一元积分沿区间累计进入，以薄板质量、体积与平均降雨量说明分布在区域上的总量；提出本章问题：怎样的区域有体积、怎样的函数可以累计，怎样实际计算，换坐标或带参数时哪些操作合法。

2. 交代24.1以坐标盒内外逼近得到Jordan区域与积分并整理性质，24.2在连续性条件下化为逐坐标积分，上下限由截面决定、换序要重新描述区域，无界情形须截断且结果可能依赖截断方式。

3. 交代24.3用Jacobian行列式绝对值修正局部体积并要求单次覆盖、截去奇异坐标点，24.4研究参数积分的极限、积分号下求导与变限积分的边界贡献。

4. 列出所用的第20章Jacobian、链式法则与连续偏导数判据，第3章一致连续性，以及卷一一元Riemann积分与基本定理（跨卷引用到章）；说明区域积分是后面各章的共同基础。

### 24.1 区域积分的定义与性质

1. 以不均匀金属薄片的总质量为例，说明切块、取“密度乘面积”、相加并加细的累计过程，同样适用于体密度和电荷密度；被积函数是输入$d$个坐标、输出一个待累计数的多元标量函数。

2. 给出积分的两种读法：非负函数的积分是以区域为底、以图像为顶的立体体积；除以区域面积得到平均值。

3. 说明本节路线：先确定哪些区域有体积，再用分割和定义积分，最后整理基本性质；一般可测函数与极限定理在卷四中建立（跨卷引用卷四“积分”章，计划标签`chap:integration`），本章不以它们为前提。

#### 24.1.1 盒体积与Jordan可测性

1. 从“多元积分要把区域切成已知体积的小块”进入，定义闭坐标盒的体积为边长之积，边长为零时体积为零。

2. 说明有限可加性：沿坐标切开时边长相加不变，反复切分可知任意有限网格的小盒体积之和等于原体积，公共边界不重复计入。

3. 用含于$D$的有限盒组从内侧、覆盖$D$的有限盒组从外侧逼近有界集合，两侧差可任意小时称Jordan可测（Jordan区域）；由任一内侧总体积不超过任一外侧总体积，说明夹住的数唯一，即Jordan体积$|D|$。

4. 引出边界判别：有界集合Jordan可测当且仅当边界能被总体积任意小的有限个盒覆盖。先说明非边界点有邻域完全在$D$内或$D$外，所以同时接触$D$和$D$外的小盒必与边界相交。

5. 证明充分性：把覆盖边界的盒稍向外扩张，取足够细的网格使与边界相交的小盒都落入扩张盒，内外逼近之差只由这些小盒组成，总体积小于$\varepsilon$。

6. 证明必要性：边界含于外侧盒组减去内侧盒组内部的部分，其体积受两侧之差控制，另外至多含有限个盒的边界，仍可被任意小体积覆盖；并由此说明有界函数在边界附近的贡献可以任意小。

7. 以闭圆盘为例，用短弧与小正方形的个数、面积尺度说明圆周的覆盖面积趋于零；推广到有限片分段光滑边界，并提醒依赖有限片和规则参数化。

#### 24.1.2 多元Riemann和与可积性

1. 在包含$D$的闭坐标盒上作有限网格，定义网格大小与Riemann和；要求所有足够细的分割和所有取样方式都趋于同一极限，才称Riemann可积。

2. 因无法逐一检查取样方式，引入上和与下和：任意取样和夹在二者之间，可积当且仅当上下和之差可任意小。

3. 证明盒上连续函数可积：紧性给出一致连续，细网格上每块振幅任意小，上下和之差不超过振幅乘盒体积。

4. 用零延拓$f\mathbb I_D$定义一般Jordan区域上的积分，说明换更大的包含盒不改变结果。

5. 说明能连续延拓到闭包的函数零延拓可积：远离边界的小盒由一致连续控制振幅，靠近边界的小盒由边界覆盖控制体积；分块连续函数同理，边界上的取值不影响积分。

6. 以$\mathbb I_{\{x\geq1/2\}}$说明连续只是充分条件，只有穿过不连续直线的小盒贡献上下和差，积分为$1/2$；再以$\mathbb I_{\mathbb Q^2}$上下和之差恒为盒面积说明有界不够。

#### 24.1.3 积分的基本性质

1. 由有限Riemann和取极限得到线性、保序性和绝对值估计，以及内部不重叠、沿可忽略边界拼接的区域可加性。

2. 把体积、总质量、平均值和质心写成区域积分，说明向量值函数的积分按分量计算。

### 24.2 累次积分

1. 说明定义同时分割所有坐标，计算时希望逐个坐标积分，把$d$维累计化为几次一元积分；本节回答这样做的条件，以及上下限怎样由截面确定。

#### 24.2.1 长方体上的累次积分

1. 对闭矩形上的连续函数，固定$x$得到截面积分$F(x)$，由一致连续性证明$F$连续。

2. 把乘积网格上的Riemann和按列分组，内层和趋于截面积分且一致连续性同时控制各列误差，外层和趋于$\int F$；按行分组同理，得到两种次序的累次积分都等于二重积分，更多坐标重复分组。

3. 指出连续是便于核对的充分条件：一般Riemann可积函数的某些截面积分可能不存在，不能省去对内层积分的检查。

#### 24.2.2 简单区域上的累次积分

图解：`fig:v2-integration-slices`。区域$D=\{0\leq y\leq x\leq1\}$的两种切片。左图固定$x$，绿色线段从$y=0$到$y=x$；右图固定$y$，绿色线段从$x=y$到$x=1$。两种积分次序覆盖同一片区域。


1. 对由连续边界函数$\alpha\leq\beta$描述的区域和闭包上的连续函数，给出先$y$后$x$的累次积分公式；用零延拓的网格分组说明边界附近格子可忽略，边界函数一致连续保证截面端点与内层积分随$x$连续，有限个这样的区域逐块相加。

2. 以三角形$0\leq y\leq x\leq1$上的$x+y$为例，分别按竖直截面和水平截面计算，两种次序都得$1/2$，说明换序时要重新求投影和截面，而不是机械交换积分号。

3. 以$0\leq y\leq\min(x,2-x)$的三角形说明换序会改变分块：先对$y$积分需在$x=1$处分块，先对$x$积分只需一块；取$f=1$核对面积为$1$。

#### 24.2.3 反常重积分与积分次序

1. 指出前面结论只针对有界区域上的有界函数；无界情形先用一族有界Jordan区域截断，逐个检查可积性，再取极限，并提醒一族截断的极限不能代表其他截断方式。

2. 取$(0,1]^2$上的$(x^2-y^2)/(x^2+y^2)^2$，用远离原点的矩形$[\varepsilon,1]\times[\varepsilon^2,1]$截断；先把下边界放宽到$y=0$，由原函数$y/(x^2+y^2)$算出内层积分$1/(1+x^2)$，外层极限为$\pi/4$。

3. 用$|f|\leq1/x^2$估计多算的窄条贡献趋于零，得到截断积分趋于$\pi/4$；交换两边截断速度并利用$f(y,x)=-f(x,y)$得到$-\pi/4$，说明不存在与截断方式无关的总量，两种次序的累次积分也分别为$\pi/4$与$-\pi/4$。

### 24.3 区域积分的换元

1. 以圆盘用半径和角度描述更简单进入，说明换坐标除了重写函数，还要校正小块体积；线性映射按行列式绝对值缩放体积，可微映射局部近似线性，换元公式累计这些局部比例。

#### 24.3.1 积分换元公式

1. 为保证单次覆盖并便于处理边界，在开集之间取逆也为$C^1$的双射，陈述紧Jordan区域上连续函数的换元定理`thm:classical-change-of-variables`，权重为$|\det DT|$。

2. 概述证明思路：在紧集上写出余项一致的一阶近似，逆导数有界保证小立方体的像不被任意压扁。

3. 用线性像平行多面体外加与$\eta(\delta)\delta$同阶的薄层夹住真实像，得到局部体积比趋于$|\det DT|$；再逐项比较像区域与参数区域上的和，由一致连续、一致余项界和Jordan边界条件控制三类误差。明确这是证明思路，仅有单点线性近似不能交换整个分割和的极限。

4. 说明全局双射不可省：逆函数定理只给局部可逆，重复覆盖会重复累计；行列式取绝对值只消去定向符号，不消去覆盖次数。

#### 24.3.2 极坐标、柱坐标与球坐标

1. 平面极坐标的Jacobian行列式为$r$，以同一角宽在大半径处扫过更长的弧解释面积权重$r\,\mathrm dr\,\mathrm d\theta$，配图对照不同半径处的小块面积。

2. 说明原点处行列式为零、角度两端表示同一射线，闭参数矩形不满足定理条件；先在$r\geq\varepsilon$、$\varepsilon\leq\theta\leq2\pi-\varepsilon$上换元再取极限，用函数上界乘面积控制遗漏。

3. 用圆盘面积$\pi R^2$核对，指出角度取到$4\pi$时结果加倍，奇异被积函数不能只凭“接缝不贡献面积”跳过极限估计。

4. 柱坐标保留高度，体积权重仍含$r$，得圆柱体积$\pi R^2H$。

5. 球坐标按三个正交方向的长度比例$1$、$\rho$、$\rho\sin\varphi$得到体积权重$\rho^2\sin\varphi$，并可由Jacobian行列式验证；说明在去掉轴线和接缝后单次覆盖，经截断估计得到球体积$4\pi R^3/3$。

#### 24.3.3 线性换元

1. 用$u=x+y$、$v=x-y$把斜正方形变为$[0,2]^2$，逆变换行列式为$-1/2$、面积权重为$1/2$，算得$\int_D(x+y)=2$。

2. 用面积$2$与平均值$1$的乘积再核对一次，说明这同时检验了区域、权重和积分值。

### 24.4 参数积分

1. 以密度随时间变化时总质量成为时间的函数进入，说明判断参数积分的连续与可导需要整个区域上的统一控制，本节固定紧Jordan区域，用连续性提供这种控制。

#### 24.4.1 参数积分的连续性

1. 设$f$在$D\times K$上连续，由乘积紧集上的一致连续性得到关于$\bm x$的上确界差趋于零，再用绝对值估计证明参数积分连续；参数域不必整体有界，局部取小闭盒即可。

#### 24.4.2 积分号下求导

1. 设$f$及各参数偏导数在$D$与参数邻域的乘积上连续，用一元中值定理把差商写成附近参数处的偏导值，由偏导数一致连续得到差商一致收敛，进而得到积分号下求偏导的公式。

2. 右侧是被积函数连续的参数积分，因而连续；由连续偏导数判据得$F\in C^1$及全微分公式，并强调整体可微来自连续偏导数，不能只验证各方向极限。

3. 以$F(t)=\int_0^1e^{tx}\,\mathrm dx$求得$F'(0)=1/2$，说明这样不必处理显式表达式$(e^t-1)/t$在$0$处的可去奇点。

#### 24.4.3 变限参数积分

1. 说明积分区间随参数变化时，变化来自被积函数的变化和端点处新添或移除的细条。

2. 在$a,b\in C^1$、$f$与$\partial_tf$连续的条件下，把积分写成固定点到上下限的积分之差，对上限用一元基本定理、对参数用积分号下求导，再由链式法则得到变限求导公式，解释两个边界项的符号。

3. 说明多参数时逐个求偏导或改用全微分，更一般的移动区域会产生沿边界的贡献，本章只在区间变限时使用这一规则。

### 24.5 本章小结

1. 归纳Jordan区域的两种刻画与边界可忽略的原因，说明闭包上连续与分块连续的有界函数可积而有界不够，并列出线性、保序、绝对值估计、可加性及体积、质量、平均值与质心。

2. 归纳累次积分的条件与换序方法，强调无界区域或无界函数须先截断再取极限，不同截断方式与积分次序可给出不同结果。

3. 归纳换元公式的来源与条件：$C^1$双射及$C^1$逆，绝对值消去定向符号而不消去覆盖次数；列出极、柱、球坐标的权重并说明原点、轴线与接缝须先截去。

4. 归纳参数积分依赖紧区域上的统一控制，联合连续时积分连续、偏导联合连续时可在积分号下求导并得全微分，变限时还要计入端点细条的贡献；引向下一章沿曲线的累计。

## 第25章 路径积分

正文入口：[06-path-integrals.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/06-path-integrals.tex)（全章）。

1. 以弯曲铁丝的质量和沿路线推物体做功进入，说明后者还取决于力与前进方向的夹角。

2. 区分两类被积对象：线密度是标量场，力是向量场（回指20.1），提出本章问题：怎样按长度累计标量场、怎样沿行进方向累计向量场，以及后者何时只取决于端点。

3. 交代各节分工：25.1用参数路径区分像、快慢、方向与重复覆盖并计算弧长，25.2按弧长累计标量场，25.3累计切向分量使方向进入结果，25.4研究功只依赖端点的情形、交叉偏导条件以及定义域中的洞使其失效。

4. 说明参数积分都是一元Riemann积分，路径无关的判别用到第20章的链式法则与混合偏导交换以及第24章的积分号下求导，并给出参考文献。

### 25.1 参数路径与弧长

1. 以质点每个时刻的位置描述一次行进，导数是速度，速率乘时间是路程，速率变化时路程是速率的积分。

#### 25.1.1 路径的定义

###### paragraph：参数化路径

1. 说明只记下经过的点会丢失快慢、起点与重复行进的信息，因而用区间到空间的连续映射同时保留位置与先后次序；正式定义路径、起点终点、闭路径与像集。

2. 用三条像集相同的对角线路径对照：$\gamma(t)=(t,t)$、速度减半用时加倍的$\eta$、先去后回的$\rho$；前两者只差快慢，$\rho$使每个内点经过两次。说明两类积分对前两者相同，沿$\rho$按长度加倍、按有向位移抵消，所以路径积分沿一次行进定义。

###### paragraph：分段光滑路径

1. 以往返路径掉头、正方形边界转角说明这些位置没有唯一切线，正式定义分段$C^1$（分段光滑）与分段正则路径。

2. 解释闭区间上$C^1$指导数连续并可延拓到端点，相邻段的端点导数不必相同，以$\rho$两段速度为例；折点只有有限个，不影响参数积分；分段正则排除中途停住，单位切向量只在速度非零处使用。

#### 25.1.2 路径的长度

###### paragraph：弧长

1. 用插标杆测道路的办法说明内接折线不长于道路、加点后不变短，定义弧长为内接折线长度的上确界及可求长；指出定义只用位置。

2. 以位移约为速度乘时间、里程表累计路程为直观，陈述分段$C^1$路径的弧长等于速率积分。证明先归结到单个光滑段，再分两步：由分量基本定理与Cauchy--Schwarz不等式得弦长不超过该段速度积分，并得到向量积分的范数不等式；再用$\gamma'$的一致连续控制细分割上每段弦长与速度积分的差，得到反向不等式。

3. 用例子核对：对角线段长$\sqrt2$而非$2$，慢速路径同为$\sqrt2$，往返路径为$2\sqrt2$，圆周为$2\pi r$；说明速率减半与用时加倍抵消、弧长计入经过次数。定义累计路程$s(t)$与$\mathrm ds=\lVert\gamma'\rVert_2\,\mathrm dt$。

### 25.2 第一类路径积分

1. 说明被积对象是曲线上的标量函数，每小段贡献函数值乘长度，只用路程作权重。

#### 25.2.1 定义与可积性

###### paragraph：按弧长的积分

1. 把铁丝切成小段，每段质量约为密度乘速率乘参数长度，相加成为$h(\gamma(t))\lVert\gamma'(t)\rVert_2$的积分和；对像集上的连续函数正式定义第一类路径积分，右侧按各光滑段的一元积分相加。

2. 给出读法：$h=1$为弧长，非负线密度给质量，除以长度得到按路程加权的平均值，并与按参数时间加权对比，说明车速不影响按路程的平均。

3. 例题沿上半单位圆放线密度为$y$的铁丝，速率为$1$，质量为$2$，平均线密度$2/\pi$；指出速率恒为$1$时两种平均一致，一般不同。

#### 25.2.2 积分的基本性质

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

#### 25.2.3 积分的计算

1. 归纳三步：选恰好走一遍的参数化，乘速率，在参数区间上积分并在折点两侧分段。

2. 沿对角线段积分$x+y$得$\sqrt2$，平均值$1$等于中点值；指出漏掉速率会少一个因子$\sqrt2$，第一类积分也不是线段下方的平面面积。

3. 对函数图像$y=\psi(x)$以$x$为参数，得到含$\sqrt{1+\psi'^2}$的公式，用斜边长度解释根号，曲线越陡同一$\mathrm dx$的路程越长。

4. 例题计算抛物线$y=x^2$上线密度$x$的铁丝质量$(5\sqrt5-1)/12$，对照漏写根号所得的$1/2$。

### 25.3 第二类路径积分

1. 以推车时力与前进方向的夹角决定功的正负进入，说明做功问题需要先说清每一点有一个力的含义。

#### 25.3.1 定义与可积性

###### paragraph：向量场

1. 以重力、引力与水流速度说明每个位置给出一个同维向量，回指定义`def:multivariable-vector-field`而不重新定义，解释箭头画法，并说明输出与位置同维才能与速度向量作内积。

2. 给出本章反复使用的重力常场、径向场和旋转场三个平面例子，验证旋转场与位置向量垂直。

###### paragraph：有向线积分

1. 以常力沿直线做功等于内积$\bm F^\top\Delta\bm r$说明只有沿位移方向的分量做功及功的符号；路线弯曲时切段近似，每段功约为场值与速度的内积乘参数长度，强调乘的是速度向量而非速率。

2. 对像集上的连续向量场正式定义第二类路径积分；解释$\mathrm d\bm r$为有向位移，平面中写成$\int P\,\mathrm dx+Q\,\mathrm dy$并说明各项含义；连续性保证参数积分存在。

3. 在速度非零处用单位切向量把被积量写成切向分量乘$\mathrm ds$，说明第二类积分是切向分量的第一类积分，速度为零处两侧都为零；切向分量随行进方向反转而变号。

4. 定义流速场沿闭路径的环流，以旋转场沿单位圆一周环流$2\pi$为例；配图在同一对角线段上对照常数密度按弧长累计得$\sqrt2$与常场$(1,0)$做功为$1$。

#### 25.3.2 积分的基本性质

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

#### 25.3.3 积分的计算

1. 归纳步骤：按行进方向参数化，场值与速度取内积，再做一元积分。

2. 常场$(1,0)$沿对角线段做功为$1$而不是长度$\sqrt2$，因为只对位移的水平分量做功。

3. 重力沿任意分段光滑平面路径的功为$-mg(y(b)-y(a))$，被积函数不含$x'$，只依赖高度差；以$1$千克下降$2$米做功约$19.6$焦为数值例，并预告路径无关一节解释其原因。

4. 给出图像路径上的第二类积分公式。

5. 例题比较从$(1,0)$到$(-1,0)$的上半圆与直径：常场在两条路线上做功都为$-2$，等于$x$的端点差；旋转场沿上半圆做功$\pi$，沿直径为$0$。

6. 总结常场的功与路线无关、旋转场的功依赖路线，绕单位圆一周旋转场做功$2\pi$；配图画出旋转场与两条路线。

### 25.4 路径无关与势函数

1. 对比重力与旋转场：重力的功可写成只依赖位置的量$-mgy$在两端之差，旋转场没有这样的量；说明本节依次讨论势函数化累计为端点差、由路径无关构造势函数、微分判别及有洞定义域的反例。

#### 25.4.1 势函数与路径积分

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

#### 25.4.2 路径无关的等价判别

###### paragraph：路径无关

1. 说明比较不同路线需要路径连通，欧氏开集中路径连通时可选域内折线，正式定义路径无关。

2. 以物理中从参考点做功定义势能、只有功与路线无关时势能才确定为动机，陈述势函数存在、路径无关与闭路径积分为零三者等价。

3. 证明：1推2由基本定理；2推3用常值路径；3推2把两条路径拼成闭路径并用拼接与反向性质；2推1固定参考点定义$\phi$，在小球内沿坐标方向延伸一小段线段，把差商写成$F_j$在短线段上的平均值，由连续性得偏导数等于$F_j$。

4. 说明所构造的$\phi$就是从参考点出发的功，换参考点只差一个常数。

#### 25.4.3 势函数存在的微分判别

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

### 25.5 本章小结

1. 强调路径积分沿一次行进定义：参数路径记录位置、次序与经过次数；分段光滑路径的弧长是折线长度上确界并等于速率积分，一一换参数不改弧长而重复行进重复累计。

2. 比较两类积分：第一类以$\mathrm ds$为非负权重，与方向和快慢无关；第二类累计场与有向位移的内积，等于切向分量的第一类积分，保向换参数不变、反向变号、往返抵消，闭路径上称为环流。

3. 归纳路径连通开集上势函数存在、路径无关与闭路径积分为零的等价，路径积分基本定理把功化为端点差；连续可微场的交叉偏导相等是必要条件，在星形域上也充分。

4. 强调定义域条件：穿孔平面涡旋场满足交叉偏导条件而绕原点环流为$2\pi$，局部势函数是极角；小正方形相消推理只在被围区域整个落在定义域内成立，其精确形式是第27章的Green公式。

## 第26章 曲面积分

正文入口：[07-surface-integrals.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/07-surface-integrals.tex)（全章）。

1. 从路径积分沿细线累计过渡到薄片，提出薄壳质量与穿过渔网水量两个问题。

2. 区分被积对象：前者是曲面上的标量面密度，后者是向量场，只取法向分量累计为通量。

3. 提出本章问题：怎样度量一小片面积、怎样按面积累计面密度、怎样在规定穿越方向后累计通量。

4. 交代26.1求面积元并证明面积不依赖参数，26.2按面积累计且与定向无关，26.3先讨论定向再定义通量，并说明法向反转、参数次序与分片相容；指出这些积分为第27章的Gauss与Stokes公式准备边界累计。

5. 说明以三维曲面为主，使用第24章区域积分与换元、第20章偏导数与Jacobian，参数积分按有界Jordan区域上的Riemann积分理解，并给出参考文献。

### 26.1 参数曲面与面积元

1. 说明平面区域的面积是Jordan面积，而弯曲曲面不能不经伸缩地摊平，面积尚无定义。

2. 以经纬度为参数化的例子，说明用两个参数把曲面上的累计转回参数域，但参数面积不等于实际面积，需要每点乘一个面积放大倍数；本节说明怎样的参数化描述一张面，求出放大倍数，并证明面积与参数选取无关。

#### 26.1.1 曲面的参数化

###### paragraph：正则曲面片

1. 说明并非每个二元向量值映射都描述一张面：点只沿一个方向移动时像集可能是曲线，重复覆盖会重复累计；正式定义正则参数曲面片，参数边界允许接缝或退化。

2. 解释$\bm r_u,\bm r_v$是两条参数曲线的速度向量，线性无关即不共线并张成切平面；以$(u+v,0,0)$把正方形压成线段的例子说明正则性的作用。

3. 以单位圆柱面说明单次覆盖：$\theta\in[0,2\pi]$只在边界形成接缝，$\theta\in[0,4\pi]$使内部点被表示两次，不符合定义。

4. 引入贯穿全节的斜平面片$(u,v,u+v)$，核对它满足定义。

###### paragraph：叉积

1. 由线性近似说明参数小矩形近似映为以$\bm r_u\Delta u$、$\bm r_v\Delta v$为边的平行四边形，问题归结为由两条三维边向量求面积。

2. 指出$3\times2$矩阵没有行列式，定义叉积并以坐标单位向量为例。

3. 核对三条性质：叉积垂直于两因子并按右手规则定向；由Lagrange恒等式得叉积长度等于平行四边形面积，为零当且仅当线性相关；双线性与反对称。

4. 指出Lagrange恒等式右端是两条边的Gram行列式，所以面积也等于Gram行列式的平方根，这种写法只用内积，也适用于高维中两个向量张成的平行四边形。

5. 由性质得小曲面片面积约为$\lVert\bm r_u\times\bm r_v\rVert_2\Delta u\Delta v$，即面积放大倍数，正则性等价于叉积非零；平面情形下它就是Jacobian行列式的绝对值，与换元一节的权重一致。

#### 26.1.2 曲面面积的表示

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

### 26.2 第一类曲面积分

1. 回到薄壳质量问题，说明这类积分只用小片面积、不涉及方向。

#### 26.2.1 积分的定义和可积性

###### paragraph：按面积的积分

1. 把薄壳分片，每片质量约为面密度乘面积，相加加细得到面密度对面积的积分，电荷量与涂料用量同理；在参数域上把密度与面积权重相乘。

2. 正式定义连续函数的第一类曲面积分，解释计算顺序，说明重参数化下积分不变；取$h=1$得面积，以斜平面片上常数密度$2$得质量$2\sqrt3$。

3. 定义按面积加权的平均，以全球平均气温说明应按实际面积而非经纬度格子数平均。

4. 说明第一类积分继承线性、单调性与绝对值估计，分片曲面逐片求和；面积权重非负且与观察侧无关，所以反转曲面朝向不改变第一类积分。

#### 26.2.2 积分的计算

1. 归纳三步：选单次覆盖的正则参数化，与$h$复合，乘叉积长度后在参数域上积分。

2. 函数图像$z=\psi(x,y)$的叉积为$(-\psi_x,-\psi_y,1)$，自动正则且单次覆盖，得到含$\sqrt{1+\psi_x^2+\psi_y^2}$的公式。

3. 用法向与$z$轴夹角的余弦解释根号是投影面积的校正，以平面$z=ax+by+c$在单位圆盘上方的面积$\pi\sqrt{1+a^2+b^2}$为例；不能单值投影的曲面需换参数或分片。

4. 给出球面参数化及偏导向量，由两者正交、长度为$R$与$R\sin\varphi$得放大倍数$R^2\sin\varphi$，并用经线与纬线圈上的弧长直观解释；两极与接缝来自参数边界，面积为零。

5. 例题由球坐标算得球面面积$4\pi R^2$。

6. 例题求上半球面按面积的平均高度$R/2$，对照按参数矩形平均所得的$2R/\pi$；说明参数格子在北极附近对应很小的面积，按参数平均会高估。

### 26.3 第二类曲面积分

1. 回到渔网问题，说明“穿过”需要先规定出发侧与到达侧，所以先讨论定向再定义通量。

#### 26.3.1 曲面的定向

###### paragraph：单位法向量

1. 说明正则点处有两个相反的单位法向，选定其一即约定正向穿越；用参数叉积定义局部单位法向，交换参数会反转它。

2. 斜平面片上它指向上方；球坐标参数下叉积是位置向量的正数倍，单位法向指向外侧；参数边界上叉积退化处不用此式，面积为零不影响通量。

###### paragraph：定向与可定向性

1. 说明逐点选法向不够，用给曲面一侧涂色解释连续选取的要求；正式定义定向、可定向曲面与分片曲面的相容条件。

2. 举出函数图像的向上法向、球面外法向、闭曲面通常取外法向（散度定理采用）以及立方体表面的相容外法向。

3. 以纸带扭转半圈粘合与蚂蚁爬行描述Möbius带；例题给出参数化，算出中线上叉积在$u=0$与$u=2\pi$处对应同一点却方向相反，再用连续函数只取$\pm1$必为常数推出矛盾，证明不可定向。

4. 说明Möbius带的面积与第一类积分仍有定义，但全局通量不适用。

#### 26.3.2 积分的定义和可积性

###### paragraph：通量积分

1. 从恒定流穿过平面网的斜柱体积推出单位时间穿过量为$(\bm v^\top\bm n)A$，并区分平行、垂直与逆向三种情形，说明只有法向分量起作用。

2. 例题对倾斜正方形算出单位法向与面积，竖直流的通量为$c\cos\alpha$，切向流的通量为零；说明竖直流的通量等于流速乘水平投影面积，并以倾斜屋顶接雨解释。

3. 对弯曲曲面与变化的场切片近似，得到$\bm F^\top\bm n$对面积的积分，电场、热流同理；正式定义第二类曲面积分，参数叉积须与所选法向一致，分片曲面按相容定向相加。

4. 说明单位法向的分母与面积元中的长度抵消，引入有向面积元，计算时不必先求单位法向；通量是净穿过量，与把三个分量分别做面积积分所得的向量不同。

5. 引入记号$\mathrm dy\,\mathrm dz$等，解释各分量是小片在坐标平面上的有向投影面积，以倾斜正方形核对，强调这些记号带符号；配图在法向截面内分解场值，说明通量只累计法向分量。

6. 说明连续场与连续有向面积元保证每片通量存在。

#### 26.3.3 积分的性质

1. 规定同一曲面、同一法向约定与连续向量场，说明线性和可加性沿用第一类积分，法向反转与重参数化需单独说明。

###### paragraph：线性

1. 由法向分量对场的线性，给出和与数乘的通量公式，以两股水流叠加与流速加倍解读，强调缩放的是场而法向约定不变。

###### paragraph：曲面分割的可加性

1. 有限分片且各片沿用原定向时通量相加，零面积接缝不贡献；某片单独反转法向就不再是整张曲面的通量。

###### paragraph：法向反转

1. 法向换成相反方向时通量变号，水流不变而计数方向改变；与第一类积分不随定向改变对照。

###### paragraph：重参数化

1. 由重参数化定理，新叉积乘$\det\bm J_T$而换元公式用$|\det\bm J_T|$；行列式为正时直接不变，为负时按定义中的符号约定校正后仍不变，通量只依赖曲面、定向和场。

#### 26.3.4 积分的计算

1. 归纳三步：定法向，选叉积指向该侧的参数化（否则加负号），在参数域上累计场与有向面积元的内积。

2. 图像曲面取向上法向时得到$\iint(-P\psi_x-Q\psi_y+R)$的公式，取向下法向加负号，强调不能再乘根号。

3. 例题对斜平面片与竖直单位场算得通量$1$，用面积$\sqrt3$乘法向分量$1/\sqrt3$核对，等于水平投影面积；推广到平面在单位圆盘上方的通量$\pi$，与实际面积对照。

4. 说明球面$(\varphi,\theta)$次序的叉积指向外侧，三个例子都取外法向。

5. 例题径向场$\bm x/R$穿过球面的外向通量为$4\pi R^2$，取内法向为负；说明一般只有法向分量计入，通量绝对值不超过场大小的面积积分。

6. 例题点源场$\bm x/\lVert\bm x\rVert^3$的外向通量为$4\pi$，与半径无关，用面积增大抵消场减弱解释。

7. 例题恒定场穿过球面的净通量为零，上下半球分别为$\pi R^2$与$-\pi R^2$；说明闭曲面的净通量反映内部的源与汇，包围点源的球面有正通量，并预告用散度定理核对。

### 26.4 本章小结

1. 归纳面积的度量：切向量张成切平面，面积放大倍数是叉积长度或Gram行列式平方根，面积直接定义为其参数积分；正则性与单次覆盖分别排除压扁与重复计数，换参数使叉积乘$\det\bm J_T$而面积不变，参数边界上的接缝与退化点是参数的奇异而非曲面的奇异。

2. 归纳第一类积分的非负权重及其与参数化、定向无关，比较按面积平均与按参数平均（上半球面平均高度$R/2$与$2R/\pi$），列出图像与球面的面积元。

3. 归纳第二类积分：先连续选定单位法向，Möbius带不可定向；有向面积元的方向须与法向一致，交换参数次序反转叉积，法向反转使通量变号，分片须相容，闭曲面通常取外法向。

4. 以点源场通量与半径无关、恒定场穿过闭球面净通量为零说明闭曲面通量反映内部源与汇，引向第27章的Gauss公式，并说明有边界曲面通过诱导方向与边界环流联系、由Stokes公式表达。

## 第27章 积分定理

正文入口：[08-integral-theorems.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/08-integral-theorems.tex)（章首）；章内依次输入[01-relations.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/08-integral-theorems/01-relations.tex)（27.1—27.2）与[02-summary.tex](../../../tex/02-vectors-matrices-and-multivariate-calculus/04-multivariate-calculus/08-integral-theorems/02-summary.tex)（27.3）。

1. 从一元基本定理“内部变化率的累计只剩端点信息”进入，回顾前两章得到的环流与通量，提出本章问题：对平面区域、空间区域与有边界曲面，内部的哪种导数累计恰等于边界上的环流或通量，条件是什么、能做什么。

2. 交代27.1以流体速度场解释散度与旋度，并由收缩小立方体、小正方形上的通量与环流取极限得到；Laplace算子比较一点值与周围平均，并与微分恒等式一起为分部积分准备材料。

3. 交代27.2的拼接机制：小块上导数乘大小近似边界累计，公共边界方向相反而抵消，依次得到Green、Gauss、Stokes公式，再由Gauss公式推出多元分部积分与Green恒等式。

4. 提醒区分正向、外法向与诱导方向，检查场在积分对象附近连续可微、边界项能否消失；列出所用的第24章区域与累次积分、第25章环流与势函数、第26章通量与定向及第20章Jacobian、Hessian与混合偏导交换。

### 27.1 局部微分算子

1. 以梯度的坐标式为对照，把向量场想成流体速度场。

2. 提出净流出与绕点打转两个局部问题，分别由散度与旋度回答。

3. 说明Laplace算子作用于标量函数、比较一点的值与周围平均，三者都是下一节积分公式中的内部量。

#### 27.1.1 散度与局部通量

###### paragraph：小立方体的净流出

1. 回顾单位时间穿过小片的流量约为法向分量乘面积，以点$\bm a$为中心取边长为$h$的小立方体估计净流出。

2. 计算垂直于$x$轴的两面：右面流出、左面流入，合计约为$\partial_1F_1h^3$，解释$F_1$沿$x$增大时净流出为正。

3. 三对面相加除以体积得到偏导数之和；对连续可微场在小立方体上统一展开，余项贡献为$o(h^3)$，常数项抵消、线性项给出偏导数，从而得到极限，不需要Gauss公式。

4. 正式定义散度，并说明它是Jacobian矩阵的迹，非对角偏导数不进入净流出率。

###### paragraph：源的强度

1. 把散度读成源的强度，区分源、汇与平衡；不可压缩且无源汇的流体散度为零。

2. 例题算出三维径向场散度为$3$、旋转场与常场散度为$0$，说明散度为零不表示场为零。

3. 给出二维散度$P_x+Q_y$，说明平面通量公式使用它。

#### 27.1.2 旋度与局部环流

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

#### 27.1.3 Laplace算子与微分恒等式

1. 说明梯度再取散度把各方向的二阶变化相加，出现在分部积分与热传导方程中；正式定义Laplace算子，说明输入输出都是标量函数，并是Hessian的迹，以$\lVert\bm x\rVert^2$的$\Delta=2d$为例。

2. 由混合偏导可交换得到$\operatorname{curl}(\nabla v)=\bm0$与$\operatorname{div}(\operatorname{curl}\bm F)=0$，指出由旋度为零推势函数仍须核对定义域，并区分两个等式的对象类型。

###### paragraph：与邻域平均值的差

1. 由一元$v''>0$对应低于邻点平均值进入，在各坐标方向取前后邻点作二阶Taylor展开，一阶项抵消，求和除以$2d$得到邻点平均与中心值之差为$\frac{h^2}{2d}\Delta v+o(h^2)$，据此解释$\Delta v$的符号。

2. 例题$x^2+y^2+z^2$在原点的邻点平均比中心值高$h^2$，等式精确成立；$x^2-y^2$的邻点平均恰等于中心值。

3. 说明后者两个方向的弯曲相互抵消，Laplace算子只记录弯曲的总和。

###### paragraph：热传导中的含义

1. 由Fourier定律$\bm q=-k\nabla u$与散度的含义，推出无热源时温度变化率为$\frac kc\Delta u$，即热传导方程。

2. 用邻域平均解释较冷点升温、较热点降温、温度被抹平，稳态时$\Delta u=0$；说明Fourier定律是物理模型，只用来说明$\Delta$的含义。

### 27.2 区域与边界的积分关系

1. 从一元基本定理把端点差读成带符号的边界求和、路径积分基本定理把同样关系搬到路径上进入，说明本节推广到平面区域、空间区域和曲面，分别得到Green、Gauss与Stokes公式。

2. 说明共同思路：小块上导数乘大小近似边界累计，相邻公共边界方向相反而抵消，只剩外边界；环流对应旋度，通量对应散度。

3. 说明本节先规定边界方向，再依次给出三个公式，最后由Gauss公式推出多元分部积分与Green恒等式。

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

#### 27.2.1 Green公式与平面边界

1. 说明平面边界上可累计切向分量（环流）或外法向分量（通量），分别对应$Q_x-P_y$与散度。

##### 27.2.1.1 Green公式的环流形式

1. 由小正方形环流近似与公共边相消预期区域内旋转累计等于边界环流；陈述Green公式及区域、光滑性与正向边界条件。

2. 矩形情形的证明：先写出四条边的贡献，再对$\partial_yP$与$\partial_xQ$分别用一元基本定理和累次积分，两行恰好对应四条边；说明矩形拼接时公共边抵消，一般区域引用教材。

3. 例题旋转场在单位圆盘上两侧都为$2\pi$，顺时针时左侧变号，说明公式的符号由正向边界约定决定。

4. 例题取$Q_x-P_y\equiv1$的场得到面积公式，算出椭圆面积$\pi\alpha\beta$，并提及求积仪原理。

5. 例题涡旋场在圆环上两圈环流$2\pi$与$-2\pi$相加为零，与右侧一致；说明环流来自原点的奇点，单位圆盘含原点不满足条件。

##### 27.2.1.2 Green公式的通量形式

1. 由小正方形净流出与公共边相消预期源强度总和等于边界净流出；由外法向与切向的关系得$\bm n\,\mathrm ds=(\mathrm dy,-\mathrm dx)$。

2. 陈述平面通量公式，证明取$(P,Q)=(-F_2,F_1)$代入Green公式；说明它是二维散度公式。

3. 例题单位圆盘上径向场的通量$2\pi$与散度积分一致，旋转场通量为零而环流为$2\pi$；以流体产生与杯中搅水解释通量与环流记录不同的边界分量。

#### 27.2.2 Gauss公式与封闭曲面

1. 说明边界从曲线变为闭曲面，关系仍是内部散度积分等于边界净通量。

##### 27.2.2.1 Gauss公式

1. 以流体守恒和小立方体公共面相消预期结论，并提及静电学中的对应；陈述散度定理的区域与光滑性条件，说明接缝面积为零、两侧有限。

2. 长方体情形的证明：逐坐标用一元基本定理与累次积分，把$\partial_xF_1$的体积积分化为两张面的通量，三项相加；说明拼接时公共面抵消，一般区域引用教材，无界或不规则情形需另用版本。配图说明共同面上两份通量抵消。

3. 例题用$\bm x/R$核对球面面积$4\pi R^2$，与球坐标体积和直接参数化结果一致。

4. 例题点源场在原点外散度为零，而球面通量为$4\pi$，因球含原点不满足条件；对球壳应用定理，外内球面通量相加为零。说明通量全部来自原点的点源，并给出点电荷的Gauss定律形式。

###### paragraph：散度是通量密度

1. 用长方体上的Gauss公式把小立方体净流出除以体积写成散度的平均值，由散度连续得极限为$\operatorname{div}\bm F(\bm a)$；换成小球得到同样极限，说明散度不依赖坐标轴方向。

#### 27.2.3 Stokes公式与曲面的边界

1. 说明另一类问题只给有边界的定向曲面，比较曲面上的旋转累计与边界环流，使用旋度的法向分量。

##### 27.2.3.1 Stokes公式

1. 由平面上旋度法向分量即$Q_x-P_y$、弯曲曲面切成小平面片与公共边相消、桨轮图像预期结论；陈述Stokes定理的曲面、定向与光滑性条件，并解释两侧都是标量。

2. 在参数曲面片上归结为参数平面上的Green公式：设定参数条件，记$A=\bm F^\top\bm r_u$、$B=\bm F^\top\bm r_v$，由链式法则把边界环流化为参数平面上的路径积分。

3. 计算$\partial_uB-\partial_vA$，二阶导数项因$\bm r_{uv}=\bm r_{vu}$抵消，得到$\bm r_v^\top(\bm J_{\bm F}-\bm J_{\bm F}^\top)\bm r_u$。

4. 用反对称矩阵作用等于与旋度作叉积及混合积轮换，化为旋度与有向面积元的内积；说明参数平面Green公式适用，相容拼片使公共边相消，一般定理引用教材。

###### paragraph：旋度分量是环流密度

1. 由Stokes公式把小圆盘边界环流除以面积写成旋度法向分量的平均值，取极限得到旋度分量是环流密度，并说明这一含义不依赖坐标轴。

##### 27.2.3.2 跨接曲面的选择

1. 说明左侧只依赖有向边界，同一有向边界的两张跨接曲面上旋度通量相等，可选较简单的曲面但不能穿过奇点。

2. 用$\operatorname{div}(\operatorname{curl}\bm F)=0$与散度定理从另一角度说明两张曲面通量之差为零。

3. 例题对$(-y/2,x/2,0)$分别在向上圆盘和外向上半球面上算得旋度通量都为$\pi$，并直接计算边界环流核对；改用向下圆盘时边界方向与积分同时变号。配图比较两张曲面，强调相等的是法向分量的累计而非面积。

#### 27.2.4 分部积分与Green恒等式

1. 说明分部积分把导数转移到另一因子并留下边界项；由乘积法则$\operatorname{div}(u\bm F)=\nabla u^\top\bm F+u\operatorname{div}\bm F$与Gauss公式得到一般分部公式，边界项在$u=0$或法向分量为零时消失。

2. 回顾一元分部积分$\int_a^bu\,w'=[uw]_a^b-\int_a^bu'w$（跨卷引用卷一“一元函数的积分”章），取$w=v'$并把端点项按外法向$\pm1$拆开，列出多元推广中各项的对应关系。

3. 陈述多元分部积分定理，证明对$u\nabla v$求散度后代入Gauss公式；说明平面情形改用平面通量公式，边界项是否为零由边界条件决定。

4. 例题取$u=1$、$v=\lVert\bm x\rVert^2$在球上核对两侧都为$8\pi R^3$。

5. 例题证明Laplace方程的解由边界值唯一决定：取$u=v=w$得梯度平方积分为零，由连续非负推出梯度为零，再由连通性与边界值得$w\equiv0$；按热传导解释稳态温度由边界温度决定。

6. 交换$u,v$相减得到Green第二恒等式，说明在积分中把$\Delta$从$v$移到$u$上只差边界项。

###### paragraph：积分公式的比较

1. 说明各公式回答同一类问题且推导方式相同，用表格对照一元基本定理、路径积分基本定理、Green、Gauss、Stokes公式的内部积分与边界积分。

2. 说明Stokes公式在平面上还原为Green环流形式，Green通量形式是二维散度公式；普通标量函数的区域积分要先找到散度或旋度分量等于被积函数的场，以面积公式为例。

3. 用Stokes公式解释势函数的存在与定义域有关：闭路径若是定义域内某张曲面的边界，无旋场的环流为零；星形域中锥面落在定义域内，穿孔平面上绕原点的圆所围圆盘必含原点。

4. 总结使用条件：核对连续可微性、分片规则边界与定向，尤其是场在积分对象附近是否有定义；边界在边界积分中是累计对象，须知道场在边界上的取值与可延拓性；降低规则性需另建弱导数与边界迹的公式。

### 27.3 本章小结

1. 归纳散度是单位体积外向净通量的极限、也是Jacobian的迹，正负对应源与汇，零散度不表示零场。

2. 归纳旋度分量是垂直方向上单位面积环流的极限，平面对应$Q_x-P_y$，并以剪切流与涡旋场说明旋度与流线弯曲无关。

3. 归纳Laplace算子是Hessian的迹并度量与邻域平均之差，以及来自混合偏导交换的两条恒等式。

4. 归纳三个公式共同的相消机制，以及Green公式的环流与通量形式和正向边界约定。

5. 归纳Gauss与Stokes公式，说明同一有向边界的两张曲面给出相同旋度通量的前提。

6. 区分闭曲面的外向通量与有边界曲面的环流，归纳多元分部积分、Green第二恒等式及边界项消失时Laplace方程解的唯一性。

7. 强调使用条件：场在积分对象闭包附近连续可微、边界规则、方向相容，涡旋场与点源场说明不能越过奇点推断；放宽光滑性须另建弱导数理论。
