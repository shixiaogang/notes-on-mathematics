# 卷三《图》第五部分：图的矩阵与谱

所属卷三《图》第五部分，本卷第14—20章。卷入口见[volume.tex](../../../tex/03-graphs/volume.tex)，部分入口见[part.tex](../../../tex/03-graphs/05-matrices-and-spectra/part.tex)。

## 部分主线与导读

1. 用四个测点的温差和管道的进出量说明为什么要先找到边的两个端点，再把账目写成关联矩阵。第14章以运输分配和选边说明允许分数后怎样仍找到整数最优方案。
2. 第15章由一步连接转到各长度的行走计数，再用特征值恢复边数、三角形数并研究其他谱信息。
3. 第16章在四点图上把端点差加权并汇总，用无沿边变化解释连通分量。第17章计算注入电流怎样分到各支路。第18章比较组间连接少且两侧保有一定规模的切法。
4. 第19章说明删边并重分配权重后，什么时候仍能近似保留沿边变化。第20章把每步选择邻居的规则换成位置概率和平均等待时间。
5. 说明本部分通常讨论有限无向无自环图，边权非负并沿正权边判断连通性。
6. 约定$n$为顶点数、$m$为边数。在共同四点五边算例和各章实际使用处说明顶点数、加权度与函数长度。

## 第14章 关联矩阵

正文：[01-incidence-matrix.tex](../../../tex/03-graphs/05-matrices-and-spectra/01-incidence-matrix.tex)

章职责与主线：本章用同一张关联矩阵连接顶点函数空间和边空间，建立沿边差分与净流出汇总的伴随关系，导出环空间与割空间的正交直和分解、维数公式及生成森林基本基，最后由全幺模性证明网络流和二部匹配的线性松弛存在整数最优解。

1. 从四个测点读数的端点温差和管道流量的顶点净流出进入，指出两种计算共用边的尾端与头端信息，因而可由同一张关联矩阵$\bm B$组织。
2. 概括两种互逆作用：左乘$\bm B^\top$由顶点函数生成沿边差分向量，左乘$\bm B$由边流量向量生成顶点净流出向量；净流出为零的边流量构成环空间$\ker\bm B$，沿边差分向量构成割空间$\operatorname{im}\bm B^\top$，生成森林的树外边与树内边分别为两者提供基本环基和基本割基。
3. 介绍带符号关联矩阵与无符号关联矩阵的方子式性质（全幺模性），说明由此可保证最大流、最小费用流与二部图匹配在线性规划松弛下存在整数最优解。

### 14.1 图上的函数

正文：[01-graph-functions.tex](../../../tex/03-graphs/05-matrices-and-spectra/01-incidence-matrix/01-graph-functions.tex)

本节建立顶点空间$\mathbb R^V$与边空间$\mathbb R^E$的坐标、参考方向与内积，定义关联矩阵$\bm B$，并推导沿边差分算子$\bm B^\top$与净流出汇总算子$\bm B$的伴随关系。

#### 14.1.1 顶点函数

1. 引入四点五边贯穿图（$V=\{1,2,3,4\}$，$E=\{12,23,34,41,13\}$）与图`fig:incidence-running-example`，定义顶点函数$f\colon V\to\mathbb R$，区分图连接结构与附加在顶点上的读数。
2. 固定顶点编号次序后，顶点函数与列向量$\bm f\in\mathbb R^V\cong\mathbb R^n$一一对应，单点脉冲对应标准基向量$\bm e_v$，维数为$n$。
3. 定义顶点空间标准内积$\langle\bm f,\bm g\rangle_V=\sum_{v\in V}f(v)g(v)$（式`eq:incidence-vertex-inner-product`）。说明顶点重编号仅置换坐标，固定次序$1,2,3,4$后贯穿算例读数为$\bm f=(3,2,1,0)^\top$。

#### 14.1.2 边函数

1. 定义边函数$q\colon E\to\mathbb R$及其在固定边序$(12,23,34,41,13)$下的列向量表示$\bm q\in\mathbb R^E\cong\mathbb R^m$（四点图$m=5$）。
2. 引入每条无向边的参考方向$u\to v$（$u$为尾端、$v$为头端），明确定义边流量（向量）$\bm q\in\mathbb R^E$：$q_e>0$表示实际流向与参考方向一致，$q_e<0$表示实际流向与参考方向相反（以$q_{41}=-2$为例），说明参考方向只是坐标约定。
3. 对比边流量$q_e$（随参考方向反转而变号）与非负边权$w_e\geq 0$（图的结构参数，排成对角阵$\bm C=\operatorname{diag}(w_e)$，不随参考方向变号）。
4. 定义边空间标准内积$\langle\bm q,\bm r\rangle_E=\sum_{e\in E}q_e r_e$（式`eq:incidence-edge-inner-product`），并与第17章电网络加权内积区分。

#### 14.1.3 关联矩阵的作用

本小节定义带符号关联矩阵$\bm B\in\mathbb R^{n\times m}$，分别展开$\bm B^\top$的沿边取差作用与$\bm B$的按顶点汇总作用，并证明伴随恒等式。

1. 定义关联矩阵$\bm B$的第$e$列（对应$e\colon u\to v$）为$\bm B_{:,e}=\bm e_u-\bm e_v$（式`eq:incidence-oriented-column`），尾端行填$+1$、头端行填$-1$、其余填$0$。写出四点五边图的$4\times 5$矩阵$\bm B$并以第四列（边$41$）核对。

##### paragraph：沿边取差

1. 用$\bm B^\top$左乘顶点函数$\bm f$，定义边空间中的沿边差分（向量）$\bm d=\bm B^\top\bm f\in\mathbb R^E$，其第$e$个分量为$d_e=f(u)-f(v)$（式`eq:incidence-edge-difference`），明确区分边向量$\bm B^\top\bm f$与算子$\bm B^\top$。
2. 在四点五边图上对$\bm f=(3,2,1,0)^\top$逐边算出$\bm B^\top\bm f=(1,1,1,-3,2)^\top$。
3. 说明给所有顶点加同一常数$c$在每条边两端相消，常值向量$c\bm 1$的沿边差分向量为零向量$\bm 0$。

##### paragraph：按顶点汇总

1. 用$\bm B$左乘边流量向量$\bm q\in\mathbb R^E$，定义顶点$v$处的净流出量$(\bm B\bm q)_v$（式`eq:incidence-net-outflow`）与顶点空间中的净流出向量$\bm B\bm q\in\mathbb R^V$，以顶点$1$写出$(\bm B\bm q)_1=q_{12}-q_{41}+q_{13}$。
2. 以单边单位流$\bm q=(1,0,0,0,0)^\top$算出$\bm B\bm q=(1,-1,0,0)^\top$，并证明对任意边流量$\bm q$，全图所有顶点的净流出量总和$\bm 1^\top(\bm B\bm q)=0$恒为零。
3. 图`fig:incidence-matrix-actions`在同一条参考边$1\to 2$上并排对照沿边取差与按点记账。

##### paragraph：伴随恒等式

1. 将内积$\langle\bm B^\top\bm f,\bm q\rangle_E=\sum_{e\colon u\to v}(f(u)-f(v))q_e$从逐边求和改写为逐顶点归并，导出伴随恒等式$\langle\bm B^\top\bm f,\bm q\rangle_E=\langle\bm f,\bm B\bm q\rangle_V$（式`eq:incidence-adjoint-pairing`）。
2. 说明反转参考方向使$\bm B$的对应列与$q_e,d_e$同时变号，乘积相消，顶点净流出与子空间结构不依赖参考方向。

### 14.2 环空间与割空间

正文：[02-cycle-and-cut-spaces.tex](../../../tex/03-graphs/05-matrices-and-spectra/01-incidence-matrix/02-cycle-and-cut-spaces.tex)

本节定义环空间$\mathcal C(\mathcal G)=\ker\bm B$与割空间$\mathcal D(\mathcal G)=\operatorname{im}\bm B^\top$，证明边空间的正交直和分解与维数公式，并利用生成森林构造基本环基与基本割基。

#### 14.2.1 环空间

1. 在四点五边图上构造外圈四边环流$\bm c_1=(1,1,1,1,0)^\top$与三角形环流$\bm c_2=(-1,-1,0,0,1)^\top$，逐顶点核对$\bm B\bm c_1=\bm B\bm c_2=\bm 0$。
2. 计算叠加环流$\bm c_1+\bm c_2=(0,0,1,1,1)^\top$，结合图`fig:incidence-circulation-superposition`说明公共边$12,23$上的正反单位流相互抵消，合成为绕三角形$1\to 3\to 4\to 1$的单位环流。
3. 给出环流与环空间的定义`def:graph-cycle-space`（式`eq:incidence-cycle-space`）：每个顶点净流出均为零的边流量向量$\bm q\in\mathbb R^E$（$\bm B\bm q=\bm 0$）称为环流，全体实数环流构成环空间$\mathcal C(\mathcal G)=\ker\bm B$；对比实数环流叠加与模$2$边集对称差的区别。

#### 14.2.2 割空间

1. 对任意顶点子集$S\subseteq V$及其指示向量$\bm 1_S\in\mathbb R^V$，分析割向量$\bm d_S=\bm B^\top\bm 1_S\in\mathbb R^E$在跨割边（$\pm 1$）与同侧边（$0$）上的取值。
2. 以$S=\{1,2\}$、$\bar S=\{3,4\}$为例逐边算出$\bm d_S=(0,1,0,-1,1)^\top$，配图`fig:incidence-cut-vector-example`直观展示顶点划分指示读数$\bm 1_S$与生成的割向量$\bm d_S$。
3. 将一般顶点函数展开为$\bm f=\sum_{v\in V}f(v)\bm 1_{\{v\}}$，说明任意沿边差分向量都是单点割向量的线性组合，给出割空间的定义`def:graph-cut-space`（式`eq:incidence-cut-space`）：$\mathcal D(\mathcal G)=\{\bm B^\top\bm f:\bm f\in\mathbb R^V\}=\operatorname{im}\bm B^\top$。

##### paragraph：正交直和分解

1. 由伴随恒等式证明任意环流$\bm c\in\ker\bm B$与任意沿边差分$\bm d=\bm B^\top\bm f\in\operatorname{im}\bm B^\top$正交，并用沿闭合环绕行一周端点差首尾相消给出直观解释。
2. 证明与$\operatorname{im}\bm B^\top$正交的边向量$\bm q$必满足$\|\bm B\bm q\|_2^2=0$从而属于$\ker\bm B$，导出边空间的正交直和分解$\mathbb R^E=\mathcal C(\mathcal G)\oplus\mathcal D(\mathcal G)=\ker\bm B\oplus\operatorname{im}\bm B^\top$（式`eq:incidence-edge-space-decomposition`）及分解唯一性。
3. 在四点图上将$\bm q=(1,2,1,0,1)^\top$正交分解为$\bm c_1+\bm d_S$（图`fig:incidence-flow-decomposition`），并指出给定沿边差分$\bm d$后原像顶点函数$\bm f$相差$\ker\bm B^\top$中的常值分量。

#### 14.2.3 子空间维数

本小节分四步完整推导$\ker\bm B^\top$的基与维数$c$，再由秩零度定理证明关联矩阵的秩以及割空间、环空间的维数公式。

##### paragraph：第一步：同一连通分量内的顶点读数必定相等

1. 由$\bm B^\top\bm f=\bm 0\iff$每条边两端读数相等$f(u)=f(v)$，沿分量内任意路径$i=w_0,w_1,\ldots,w_s=j$逐边传递，证明同一连通分量内所有顶点读数必取同一常数。

##### paragraph：第二步：不同连通分量之间的常数可以彼此独立选取

1. 设顶点集划分为$c$个连通分量$V=V_1\cup\cdots\cup V_c$；因不同分量之间没有任何边相连，每条边的两个端点必落在同一分量$V_k$内，两端差为$\alpha_k-\alpha_k=0$，故$c$个分量上的常数$\alpha_1,\ldots,\alpha_c$互不约束、可完全独立选取（含孤立顶点分量）。

##### paragraph：第三步：用分量指示向量表示零空间$\ker\bm B^\top$

1. 定义第$k$个连通分量的指示向量$\bm 1_{V_k}\in\mathbb R^V$，逐坐标验证$\bm f\in\ker\bm B^\top\iff\bm f=\sum_{k=1}^c\alpha_k\bm 1_{V_k}$（式`eq:incidence-ker-bt-expansion`），证明$\{\bm 1_{V_1},\ldots,\bm 1_{V_c}\}$张成$\ker\bm B^\top$。

##### paragraph：第四步：证明$c$个分量指示向量线性无关

1. 令$\sum_{k=1}^c\alpha_k\bm 1_{V_k}=\bm 0$，在每个非空分量$V_k$中任取一点$v\in V_k$读取第$v$个坐标即得$\alpha_k=0$，证得$\{\bm 1_{V_1},\ldots,\bm 1_{V_c}\}$线性无关，$\dim\ker\bm B^\top=c$。
2. 以含两个连通分量$V_1=\{1,2,3\}$与$V_2=\{4,5\}$的五点图及图`fig:incidence-component-constants`核对$\bm 1_{V_1},\bm 1_{V_2}$及其线性组合。
3. 陈述并证明定理`thm:incidence-cycle-cut-dimensions`（式`eq:incidence-rank-components`、`eq:incidence-cycle-cut-dimensions`）：分别对$\bm B^\top$与$\bm B$应用秩零度定理，得出$\operatorname{rank}\bm B=n-c$、$\dim\mathcal D(\mathcal G)=n-c$与$\dim\mathcal C(\mathcal G)=m-n+c$，并核对四点五边图与森林特例。

#### 14.2.4 基本环基

1. 给出基本环向量$\bm c^{(e)}$（$e\in E\setminus F$）的一般构造规则：将非树边$e\colon u\to v$添入生成森林$F$，与连接$v,u$的唯一树路径$P_e$围成简单环$C_e$；沿$e$的参考方向绕行，在$e$上取$+1$、其余非树边取$0$、树路径$P_e$上的边按同向$+1$/反向$-1$取值。
2. 在四点五边图上取生成树$T=\{12,23,34\}$，依次添入非树边$41,13$算出$\bm c_1=(1,1,1,1,0)^\top$与$\bm c_2=(-1,-1,0,0,1)^\top$（图`fig:incidence-fundamental-cycles`），指出它们在非树边坐标$(41,13)$上构成$2\times 2$单位阵。
3. 陈述并分三步证明基本环基定理`thm:incidence-fundamental-cycle-basis`（式`eq:incidence-fundamental-cycle-expansion`）：（1）沿简单环一进一出证$\bm B\bm c^{(e)}=\bm 0$；（2）利用非树边坐标上的单位阵结构证线性无关；（3）由维数相等及剥除森林叶子的消元法证任意环流唯一展开为$\bm q=\sum_{e\in E\setminus F}q_e\bm c^{(e)}$。

#### 14.2.5 基本割基

1. 给出基本割向量$\bm d^{(e)}=\bm B^\top\bm 1_{S_e}$（$e\in F$）的一般构造规则：从生成森林$F$中删去树边$e$，取含$e$尾端的子树顶点集$S_e$作沿边差分；说明$\bm d^{(e)}$在树边$e$上取$+1$、在其余树边上全取$0$、在跨割非树边上取$\pm 1$。
2. 在四点五边图路径生成树$T=\{12,23,34\}$上依次删去树边$12,23,34$，算出三个基本割向量$\bm d_1,\bm d_2,\bm d_3$（图`fig:incidence-tree-cycle-cut`），指出它们在树边坐标$(12,23,34)$上构成$3\times 3$单位阵。
3. 陈述并证明基本割基定理`thm:incidence-fundamental-cut-basis`（式`eq:incidence-fundamental-cut-expansion`）：利用树边坐标上的单位阵结构证明线性无关与唯一展开式$\bm d=\sum_{e\in F}d_e\bm d^{(e)}$。

##### paragraph：正交性的验证

1. 在四点图算例上直接验算$\bm c_1^\top\bm d_2=0$与$\bm c_2^\top\bm d_2=0$，从环路跨割一去一回成对抵消解释正交性，并说明子空间本身不依赖生成森林的选取。

### 14.3 图上优化问题的整数最优解

正文：[03-total-unimodularity.tex](../../../tex/03-graphs/05-matrices-and-spectra/01-incidence-matrix/03-total-unimodularity.tex)

本节先定义全幺模矩阵并结合卷五线性规划理论说明全幺模矩阵为何支持线性松弛的整数最优解，再分别考察带符号关联矩阵$\bm B$与无符号关联矩阵$\bm N$所对应的两类图优化问题、全幺模性成立条件及其整数最优解结论。

#### 14.3.1 全幺模矩阵

1. 用二阶矩阵$\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)$（行列式$-2$）求解整数右端$(1,0)^\top$产生分数解$1/2$，说明克莱姆法则分母$\det\bm M\neq\pm 1$是分数极点的来源，给出全幺模矩阵（TUM）的定义`def:graph-total-unimodularity`：任意阶方形子矩阵的行列式均属于$\{0,1,-1\}$。
2. 写出图优化问题的线性规划松弛（式`eq:incidence-lp-relaxation`）及引入松弛变量后的标准型（式`eq:incidence-lp-slack-matrix`），说明拼接单位分块保持全幺模性，并向后引用卷五“线性规划”章的全幺模整数顶点结论：先删除冗余等式，再在满行秩标准型中选基；当约束矩阵全幺模且右端项为整数向量时，每个可逆基矩阵行列式均为$\pm 1$，可行域的每个顶点（基本可行解）都是整数向量，在问题可行且最优值有限时存在整数最优解；据此引出后续两小节对$\bm B$和$\bm N$的分类讨论。

#### 14.3.2 带符号关联矩阵

本小节介绍以带符号关联矩阵$\bm B$为约束的网络流优化问题家族，证明$\bm B$对任意无自环图无条件全幺模，从而导出该家族的整数最优流结论。

##### paragraph：属于带符号关联约束的图优化问题

1. 归纳以$\bm B\bm q=\bm b$和$\bm 0\leq\bm q\leq\bm u$为约束的三类网络流问题：最小费用流问题、最大流问题（配图`fig:incidence-flow-integer-example`展示添加虚拟回流弧$t\to s$化为守恒环流$\bm B\bm q=\bm 0$标准型）以及最短路问题；说明最短路单位流模型的可达与无负费用环条件，负环下无容量模型可能无界，单位容量模型也可能包含负环流。

##### paragraph：全幺模性判定与整数最优流

1. 陈述并证明定理`thm:graph-signed-incidence-tu`（任意有限无自环图的带符号关联矩阵$\bm B$全幺模）：对子方阵阶数$k$归纳，按列中非零元个数分全零列（行列式$0$）、单非零元列（拉普拉斯展开降阶）和每列均一正一负（行和为零，行列式$0$）三种情形完成归纳。
2. 在三角形$\bm B_\triangle$上核对三阶行列式为$0$（情形三）与二阶子式为$1$（情形二），说明奇环不影响$\bm B$的全幺模性；结合全幺模整数顶点性质得出：在任意有向图上，在整数供需与容量、问题可行且最优值有限时，网络流松弛存在整数最优解；单位流最短路模型还要求终点可达且全图无负费用环。

#### 14.3.3 无符号关联矩阵

本小节介绍以无符号关联矩阵$\bm N$为约束的配对与覆盖优化问题家族，证明$\bm N$全幺模当且仅当图为二部图，从而阐明二部图上的整数最优解与奇环上的分数间隙。

##### paragraph：属于无符号关联约束的图优化问题

1. 定义无符号关联矩阵$\bm N$（每条边在两个端点行均填$+1$），归纳以$\bm N$或$\bm N^\top$为约束的三类问题：最大匹配与最大权匹配问题（$\bm N\bm x\leq\bm 1$）、指派问题（平衡二部图完美匹配$\bm N\bm x=\bm 1$）以及对偶的最小顶点覆盖问题（$\bm N^\top\bm y\geq\bm 1$）。

##### paragraph：全幺模性的二部图充要条件

1. 在三角形上算出$\det\bm N_\triangle=2\notin\{0,1,-1\}$，说明$\bm N$并非对任意图全幺模。
2. 陈述并证明定理`thm:graph-unsigned-incidence-tu`（简单无向图的$\bm N$全幺模当且仅当图为二部图）：充分性将二部图一侧顶点行乘$-1$化归为带符号关联矩阵；必要性取出奇环$C_\ell$的$\ell\times\ell$子方阵，证明其排列展开仅有恒等排列与$\ell$-循环置换两项非零，当$\ell$为奇数时两项同号给出$\det\bm N_{C_\ell}=1+(-1)^{\ell-1}=2$。
3. 图`fig:incidence-bipartite-signs`对比四边环（可交替分配行符号化为一正一负）与三角形（第三条边同号冲突）。

##### paragraph：二部图的整数最优解与奇环的分数间隙

1. 结合定理`thm:graph-unsigned-incidence-tu`与全幺模整数顶点性质指出：当$\mathcal G$为二部图时，二部图最大匹配、指派问题（Birkhoff--von Neumann定理）与二部图最小顶点覆盖（Kőnig定理）的线性松弛均在$\{0,1\}$整数顶点处达到最优；当$\mathcal G$含奇环时全幺模失效，图`fig:incidence-matching-comparison`对比四边环$C_4$（整数最优匹配$2$）与三角形$C_3$（$\det\bm N_\triangle=2$说明三个紧约束独立，从而验证分数极点$(1/2,1/2,1/2)^\top$，松弛最优值$3/2>1$）。

### 14.4 本章小结

正文：[04-summary.tex](../../../tex/03-graphs/05-matrices-and-spectra/01-incidence-matrix/04-summary.tex)

1. 回顾关联矩阵$\bm B$的定义及其对偶作用：$\bm B^\top$映射顶点函数为沿边差分向量，$\bm B$映射边流量为净流出向量，二者满足伴随恒等式。
2. 总结环空间$\ker\bm B$与割空间$\operatorname{im}\bm B^\top$的正交直和分解、维数公式（$m-n+c$与$n-c$）以及由生成森林构造的基本环基和基本割基。
3. 先回顾标准型线性规划的整数顶点条件，再分别总结带符号关联矩阵的网络流应用与无符号关联矩阵的二部图配对覆盖应用，分开说明各自条件。
4. 预告将差分$\bm B^\top$、边权对角阵$\bm C$与汇总$\bm B$复合为下一章的拉普拉斯矩阵$\bm L=\bm B\bm C\bm B^\top$。

## 第15章 邻接矩阵

正文：[02-adjacency-matrix.tex](../../../tex/03-graphs/05-matrices-and-spectra/02-adjacency-matrix.tex)

章职责与主线：本章建立邻接矩阵幂与图上行走计数的对应关系，直接构造典型图族的特征向量与特征值，证明一般非负加权图邻接谱的Perron性质、度界、单调性与二部图对称性，利用谱矩与极端特征值刻画边数、三角形数、直径、色数与独立数，并通过同谱图和公平划分商谱界定谱作为图不变量的能力与边界。

1. 从四点环加对角线的三阶谱矩数出两个三角形引入本章核心问题：仅凭邻接矩阵特征值能读出多少图结构信息？
2. 交代全章五节的递进脉络（邻接矩阵的谱、典型图的谱、谱的性质、图结构的谱刻画、商谱），并注明图谱理论参考文献。
3. 规定简单无向图的零一邻接矩阵$\bm A$、降序排列的实特征值$\lambda_1\ge\cdots\ge\lambda_n$（邻接谱），以及非负实对称加权邻接矩阵$\bm W=(w_{i,j})$。

### 15.1 邻接矩阵的谱

正文：[01-walks-and-spectrum.tex](../../../tex/03-graphs/05-matrices-and-spectra/02-adjacency-matrix/01-walks-and-spectrum.tex)

本节建立“行走计数—矩阵幂—迹—谱矩”的基本联系，给出谱矩的定义。

##### paragraph：两步行走计数

1. 从$(\bm A^1)_{u,v}=a_{u,v}$记录一步行走出发，在三点路径$1\text{--}2\text{--}3$上展开$(\bm A^2)_{1,3}=\sum_{z\in V}a_{1,z}a_{z,3}$，说明每个求和项对应以$z$为中间顶点的两步行走$1\to z\to 3$。
2. 图`fig:adjacency-walk-progression`在四点环加对角线$\{1,3\}$上逐步展示从起点$1$出发走$k=1,2,3$步到达各顶点的行走条数（即$\bm A^k$的第一行）。

##### paragraph：多步行走计数

1. 陈述并证明行走计数定理`thm:adjacency-walk-count`（式`eq:adjacency-walk-count`）：对步数$k$归纳，将从$u$到$v$的$k+1$步行走按倒数第二个顶点$z$分解为前$k$步行走与最后一步边$z\to v$的拼接，对应矩阵乘法$\sum_{z}(\bm A^k)_{u,z}a_{z,v}=(\bm A^{k+1})_{u,v}$。

##### paragraph：闭行走计数

1. 定义闭行走（起点与终点重合的行走），说明$(\bm A^k)_{u,u}$是以$u$为起点的$k$步闭行走条数，对全体起点求和即得全图$k$步闭行走总数等于$\operatorname{tr}(\bm A^k)$（式`eq:adjacency-closed-walk-trace`），并在路径$1\text{--}2\text{--}3$上核对$\operatorname{tr}(\bm A^2)=1+2+1=4$。
2. 强调闭行走计数的两条规则：区分不同起点与绕行方向；允许途中重复经过顶点和边（与简单环区分）。

##### paragraph：谱矩

1. 利用实对称矩阵的正交谱分解$\bm A=\bm P\bm\Lambda\bm P^\top$得$\bm A^k=\bm P\bm\Lambda^k\bm P^\top$，由迹的循环不变性导出谱矩公式$\operatorname{tr}(\bm A^k)=\sum_{i=1}^n\lambda_i^k$（式`eq:adjacency-spectral-moments`）。
2. 给出第$k$阶谱矩的定义`def:adjacency-spectrum`，并说明替换成非负加权邻接矩阵$\bm W$时谱矩汇总的是所有$k$步闭行走的边权乘积之和。

### 15.2 典型图的谱

正文：[02-standard-graph-spectra.tex](../../../tex/03-graphs/05-matrices-and-spectra/02-adjacency-matrix/02-standard-graph-spectra.tex)

本节在完全图、完全二部图、环、路径、笛卡儿积图与正则图的补图上直接通过邻接矩阵的作用构造特征向量，求出完整邻接谱。

#### 15.2.1 完全图与完全二部图

本小节分别利用全局求和与左右分块常值结构求出$K_n$与$K_{p,q}$的全部特征值。

##### paragraph：完全图

1. 将$K_n$的邻接矩阵写为$\bm A=\bm J-\bm I$（全局求和减去自身读数），在$1$维常向量$\bm 1$方向上得出特征值$n-1$，在$n-1$维零和子空间$\bm 1^\perp$上由$\bm J\bm x=\bm 0$得出特征值$-1$（重数$n-1$）。
2. 陈述完全图邻接谱定理`prop:adjacency-complete-spectrum`，并用一阶迹$0$与二阶迹$n(n-1)=2m$核对。

##### paragraph：完全二部图

1. 写出$K_{p,q}$按左右部$U,W$分块的邻接矩阵作用，先在两侧各取常值$(a,b)$导出$qb=\lambda a,pa=\lambda b$，解得$\lambda=\pm\sqrt{pq}$及同号/异号特征向量$(\sqrt q,\pm\sqrt p)$。
2. 在左侧零和（$p-1$维）且右侧零和（$q-1$维）的子空间上导出重数为$p+q-2$的零特征值，陈述定理`prop:adjacency-bipartite-complete-spectrum`，并以星图$K_{1,4}$算出谱$\{2,0,0,0,-2\}$。

#### 15.2.2 环与路径

本小节利用循环平移下的单位根模式和零边界下的正弦驻波模式分别求出$C_n$与$P_n$的谱。

##### paragraph：环

1. 在$n$点环$C_n$上代入幂模式$z_j=\omega^j$，由周期边界条件$z_n=z_0\iff\omega^n=1$选出$n$次单位根$\omega_k=\exp(2\pi\mathrm ik/n)$，算出特征值$\lambda_k=\omega_k^{-1}+\omega_k=2\cos(2\pi k/n)$（式`eq:adjacency-cycle-spectrum`）。
2. 说明不同$k$的模式正交，陈述定理`prop:adjacency-cycle-spectrum`，并以$C_4$说明共轭模式合并为实余弦与正弦特征向量。

##### paragraph：路径

1. 在路径$P_n$两端外侧引入虚拟零边界点$x_0=0,x_{n+1}=0$，使端点与内部顶点满足统一的递推式$x_{j-1}+x_{j+1}=\lambda x_j$。
2. 代入正弦模式$x_j=\sin(j\theta)$，由和差化积得$\lambda=2\cos\theta$，再由右边界条件$\sin((n+1)\theta)=0$确定$\theta_k=k\pi/(n+1)$（$k=1,\ldots,n$），陈述定理`prop:adjacency-path-spectrum`（式`eq:adjacency-path-spectrum`）。
3. 以三点路径$P_3$及图`fig:adjacency-path-sine-modes`展示含虚拟零点$0,4$的三个正弦特征模式（$\lambda_1=\sqrt 2,\lambda_2=0,\lambda_3=-\sqrt 2$）。

#### 15.2.3 笛卡儿积图

1. 定义笛卡儿积图$\mathcal G\square\mathcal H$（每次仅沿一个因子图移动一步），用图`fig:adjacency-cartesian-edge-directions`展示$K_2\square K_2=C_4$，并写出Kronecker积表达式$\bm A_{\mathcal G\square\mathcal H}=\bm A_{\mathcal G}\otimes\bm I_q+\bm I_p\otimes\bm A_{\mathcal H}$（式`eq:adjacency-cartesian-product`）。
2. 验证张量积特征向量$\bm x_i\otimes\bm y_j$对应的特征值为$\lambda_i+\mu_j$，陈述定理`thm:adjacency-cartesian-product-spectrum`，并由此算出$d$维超立方体$Q_d=(K_2)^{\square d}$的特征值$d-2j$（重数$\binom{d}{j}$）。

#### 15.2.4 正则图的补图

1. 定义$d$正则图（定义`def:regular-graph`），说明常向量$\bm 1$满足$\bm A\bm 1=d\bm 1$，且零和子空间$\bm 1^\perp$为$\bm A$的不变子空间。
2. 陈述并证明正则图的补图谱定理`thm:adjacency-regular-complement`：由$\bm A_{\overline{\mathcal G}}=\bm J-\bm I-\bm A_{\mathcal G}$（式`eq:adjacency-complement-matrix`），在$\bm 1$方向得$n-1-d$、在$\bm 1^\perp$方向得$-1-\lambda_i$；以$C_4$的补图$K_2\sqcup K_2$核对，并说明非正则图为何不适用。

### 15.3 谱的性质

正文：[03-spectral-properties.tex](../../../tex/03-graphs/05-matrices-and-spectra/02-adjacency-matrix/03-spectral-properties.tex)

本节在非负实对称加权邻接矩阵$\bm W=(w_{i,j})$的统一框架下，依次建立连通图Perron定理、平均度与最大度上下界、子图谱单调性以及二部图谱对称判别。

#### 15.3.1 连通图的Perron定理

1. 从单位球面上的Rayleigh商极大刻画$\lambda_1=\max_{\|\bm x\|_2=1}\bm x^\top\bm W\bm x$出发，将二次型按无向边展开为$2\sum_{\{i,j\}\in E}w_{i,j}x_i x_j$；说明将分量取绝对值$|\bm x|$保持单位长度不变，同时消除异号端点的负边贡献，使$|\bm x|^\top\bm W|\bm x|\geq\bm x^\top\bm W\bm x$。
2. 图`fig:adjacency-perron-absolute-value`在三点路径$1\!-\!2\!-\!3$上对比取绝对值前后：$\bm x=(1,-1,1)^\top$时两条边乘积均为$-1$，二次型为$\bm x^\top\bm A\bm x=-4$；取绝对值$(1,1,1)^\top$后二次型升为$+4$。
3. 给出加权矩阵$\bm W$的正权支撑$\mathcal G_+=(V,E_+)$（其中$E_+=\{\{i,j\}:w_{i,j}>0\}$，式`eq:positive-weight-support`）的正式定义`def:positive-weight-support`，说明零权边在矩阵乘法中不传递数值，只有正权支撑连通才能将非零分量沿正权路径传遍全图。
4. 陈述并分三步证明连通图的Perron定理`thm:adjacency-perron`：（1）对最大化向量取绝对值得到非负特征向量$\bm p$，由$\lambda_1 p_i=\sum_j w_{i,j}p_j$及正权路径传播证明$p_i>0$（$\forall i$）；（2）若存在正交于$\bm p$的单位最大特征向量$\bm y$，由$|y_i|>0$及每条正权边$y_i y_j=|y_i||y_j|>0$推出$\bm y$全分量同号，与$\langle\bm p,\bm y\rangle=0$矛盾，故$\lambda_1$重数为$1$；（3）由$|\lambda|=|\bm z^\top\bm W\bm z|\leq|\bm z|^\top\bm W|\bm z|\leq\lambda_1$证明谱半径等于$\lambda_1$。
5. 定义Perron向量，并指出$\lambda_n=-\lambda_1$何时出现将在15.3.4节解答。

#### 15.3.2 谱的上下界

本小节证明最大特征值夹在平均度与最大度之间：$\overline d\leq\lambda_1\leq d_{\max}$。

##### paragraph：下界：用全一常向量测试Rayleigh商

1. 展开邻接矩阵对全一向量$\bm 1$的乘法$(\bm W\bm 1)_i=\sum_{j=1}^n w_{i,j}\cdot 1=d_i$，再与$\bm 1^\top$作内积得$\bm 1^\top\bm W\bm 1=\sum_{i=1}^n d_i$，除以$\bm 1^\top\bm 1=n$得出全一向量的Rayleigh商等于平均度$\overline d$，故$\lambda_1\geq\overline d$。

##### paragraph：上界：在Perron向量的最大分量处放缩

1. 取非负特征向量$\bm p$的最大分量顶点$i^\star$（$p_{i^\star}=\max_j p_j>0$），在特征方程第$i^\star$行中将每个$p_j$放大为$p_{i^\star}$，导出$\lambda_1 p_{i^\star}\leq d_{i^\star}p_{i^\star}\leq d_{\max}p_{i^\star}$，同除以$p_{i^\star}$得$\lambda_1\leq d_{\max}$。
2. 陈述最大邻接特征值的度界定理`prop:adjacency-degree-bounds`（式`eq:adjacency-degree-spectral-bounds`）。

##### paragraph：取等条件

1. 在正权支撑连通图上分别追踪上界取等（最大分量沿正权边传遍全图且各点度均为$d_{\max}$）与下界取等（常向量$\bm 1$为特征向量，各点度均为$\overline d$），证明两端取等当且仅当图为正则图，并以$P_3$（$4/3<\sqrt 2<2$）和$C_4$（$2=2=2$）核对。

#### 15.3.3 子图的谱单调性

1. 对满足$0\leq w'_{i,j}\leq w_{i,j}$的子图矩阵$\bm W'$，取其非负单位最大化向量$\bm x\geq\bm 0$代入$\bm W$比较，证明$\lambda_1(\bm W')=\bm x^\top\bm W'\bm x\leq\bm x^\top\bm W\bm x\leq\lambda_1(\bm W)$。
2. 证明当原图正权支撑连通且确实减小了至少一条正权边权重（或删去顶点）时，由原图Perron向量的严格正性迫使不等式严格成立：$\lambda_1(\bm W')<\lambda_1(\bm W)$；对比连通图$C_n\to P_n$严格下降与不连通图$C_4\sqcup K_2$删去$K_2$边最大值不变。

#### 15.3.4 二部图的谱对称性

1. 对二部图$V=X\cup Y$构造对角符号矩阵$\bm S$（$X$侧取$+1$、$Y$侧取$-1$），验证反对易关系$\bm S\bm W\bm S=-\bm W$（式`eq:adjacency-bipartite-anticommute`），说明若$\bm W\bm x=\lambda\bm x$则$\bm W(\bm S\bm x)=-\lambda(\bm S\bm x)$，配图`fig:adjacency-bipartite-sign-flip`在$C_4$上直观展示这一翻转。
2. 陈述并证明二部图的谱对称性定理`thm:adjacency-bipartite-spectral-symmetry`：（1）谱关于零对称蕴含所有奇数阶迹$\operatorname{tr}(\bm W^k)=0$，而正权奇环会产生无法被非负项抵消的正权重奇闭行走，故正权支撑不含奇环；（2）正权支撑连通且$\lambda_n=-\lambda_1$时，对最小特征向量$\bm x$取绝对值$|\bm x|$迫使$|\bm x|$成为严格正Perron向量且每条正权边满足$x_i x_j=-|x_i||x_j|<0$，按$\bm x$的正负号即分出二部划分。
3. 对比$C_4$、$C_3$与不连通反例$C_3\sqcup K_{3,3}$（说明不连通时仅凭$\lambda_n=-\lambda_1$不足以排除奇环，但完整谱对称判别依然有效）。

### 15.4 图结构的谱刻画

正文：[04-structural-bounds.tex](../../../tex/03-graphs/05-matrices-and-spectra/02-adjacency-matrix/04-structural-bounds.tex)

本节利用低阶谱矩精确读出边数与三角形数，再结合顶点度数计算四环数，利用特征值个数限制图的直径，再结合主子矩阵交错性质、相位消去和中心化向量导出色数与独立数的谱界，最后通过同谱图总结完整谱的信息边界。

#### 15.4.1 局部结构

本小节分析二阶、三阶与四阶谱矩所计数的闭行走与局部子图结构。

##### paragraph：边数

1. 说明每条无向边$\{u,v\}$恰贡献$u\to v\to u$和$v\to u\to v$两条两步闭行走（图`fig:adjacency-edge-triangle-walks`(a)(b)），对角元$(\bm A^2)_{u,u}=d_u$，故$\operatorname{tr}(\bm A^2)=\sum_{i=1}^n\lambda_i^2=2m$。

##### paragraph：三角形数

1. 说明简单图无自环，三步闭行走必经过三个互异且两两相邻的顶点（即三角形），每个三角形有$3$个起点、$2$个绕行方向共贡献$6$条闭行走（图`fig:adjacency-edge-triangle-walks`(c)(d)），给出$m=\frac12\operatorname{tr}(\bm A^2)$与$t_3=\frac16\operatorname{tr}(\bm A^3)$（式`eq:adjacency-edge-triangle-counts`）。
2. 在四点五边图上写出$\bm A,\bm A^2$并算出$\operatorname{tr}(\bm A^2)=10\implies m=5$与$\operatorname{tr}(\bm A^3)=12\implies t_3=2$。

##### paragraph：四环数

1. 按途中访问的不同顶点个数（$2,3,4$个）将四步闭行走分为单边往返（$2m$条）、相邻两边星形往返（$4\sum_{v}\binom{d_v}{2}$条）和简单四元环绕行（$8t_4$条）三类（图`fig:adjacency-four-step-walks`），导出式`eq:adjacency-four-cycle-count`，并在四点五边图上核对$10+32+8=50$。

#### 15.4.2 直径的谱界

1. 在长为直径$D$的最短路径$u_0\to u_1\to\cdots\to u_D$上，证明前缀点对满足$\operatorname{dist}(u_0,u_k)=k$，从而当$j<k$时$(\bm A^j)_{u_0,u_k}=0$且$(\bm A^k)_{u_0,u_k}\geq 1>0$（式`eq:adjacency-diameter-echelon-entries`）。
2. 陈述并分两步证明直径谱界定理`thm:adjacency-diameter-bound`（$r\geq D+1$，式`eq:adjacency-diameter-bound`）：先由$(u_0,u_k)$处的阶梯状非零元素证明$\bm I,\bm A,\ldots,\bm A^D$线性无关；再以$r$个不同特征值构造$r$次零化多项式$p(\bm A)=\bm 0$，证明$\bm I,\bm A,\ldots,\bm A^r$线性相关，故必有$r\geq D+1$。
3. 在完全图$K_n$（$D=1,r=2$）和路径$P_n$（$D=n-1,r=n$）上核对等号成立。

#### 15.4.3 色数的谱界

1. 说明删去顶点得到导出子图$\mathcal G'$对应截取邻接矩阵的主子矩阵$\bm A_0$，引用卷二Cauchy交错定理（并配图`fig:adjacency-interlacing-path`展示$P_3\to K_2$特征值交错）说明任意导出子图满足$\lambda_1(\mathcal G')\leq\lambda_1(\mathcal G)$。
2. 陈述并分两步证明色数的谱上下界定理`thm:adjacency-chromatic-bounds`（$1-\lambda_1/\lambda_n\leq\chi(\mathcal G)\leq 1+\lfloor\lambda_1\rfloor$，式`eq:adjacency-chromatic-bounds`）：上界利用任意导出子图最小度$\delta(\mathcal G')\leq\overline d(\mathcal G')\leq\lambda_1(\mathcal G')\leq\lambda_1$构造删点序列并逆序贪心着色；下界对$k=\chi(\mathcal G)$着色赋予$k$次单位根相位对角阵$\bm U$，由异色端点几何级数相消得$\sum_{j=0}^{k-1}\bm U^{-j}\bm A\bm U^j=\bm 0$（式`eq:adjacency-chromatic-phase-cancellation`），再夹乘$\lambda_1$的单位特征向量并用$\lambda_n$下界其余$k-1$项导出$0\geq\lambda_1+(k-1)\lambda_n$。
3. 在完全图$K_n$（上下界同为$n$）和五元环$C_5$（$\sqrt 5\leq\chi(C_5)\leq 3\implies\chi(C_5)=3$）上核对。

#### 15.4.4 独立数的谱界

1. 说明正常着色的每个色类都是独立集（$\chi(\mathcal G)\geq n/\alpha(\mathcal G)$），指出独立集指示向量$\bm 1_S$满足$\bm 1_S^\top\bm A\bm 1_S=0$，需通过减去全图均值构造正交于$\bm 1$的中心化向量$\bm x=\bm 1_S-\frac{s}{n}\bm 1$。
2. 陈述并证明$d$正则图独立数的Hoffman界定理`thm:adjacency-hoffman-independence`（$\alpha(\mathcal G)\leq n\frac{-\lambda_n}{d-\lambda_n}$，式`eq:adjacency-hoffman-independence`）：算出$\|\bm x\|_2^2=s(1-s/n)$，并由$\bm 1_S^\top\bm A\bm 1_S=0$与$\bm A\bm 1=d\bm 1$算出$\bm x^\top\bm A\bm x=-ds^2/n$，代入$\bm x^\top\bm A\bm x\geq\lambda_n\|\bm x\|_2^2$即解得上界。
3. 说明结合$\chi(\mathcal G)\geq n/\alpha(\mathcal G)$可在正则图上回推出Hoffman色数下界，并在$C_{2r},K_{r,r},C_5$上核对。

#### 15.4.5 同谱图

本小节总结完整邻接谱能唯一确定的图不变量，并通过同谱非同构图反例剖析谱丢失的信息与闭行走补偿机制。

##### paragraph：邻接谱确定的图不变量

1. 归纳完整邻接谱唯一确定的四类信息：顶点数$n$、边数$m$、三角形数$t_3$及各阶闭行走总数；是否正则图（$\lambda_1=\frac1n\sum\lambda_i^2$）；是否二部图（谱关于零对称）；直径、色数与独立数的谱界。

##### paragraph：同谱非同构图

1. 定义同谱图，给出五顶点同谱非同构反例$K_{1,4}$与$C_4\sqcup K_1$（图`fig:adjacency-cospectral-pair`，谱同为$\{2,0,0,0,-2\}$），指出邻接谱不能确定连通性、度序列与四元环个数$t_4$。

##### paragraph：闭行走的补偿机制

1. 拆解两图的四阶谱矩$\operatorname{tr}(\bm A^4)=32$：$K_{1,4}$由中心度$4$多出的$8$条星形三点折返行走（$8+24+0=32$），恰好被$C_4\sqcup K_1$的$1$个四元环绕行（$8+16+8=32$）在取迹求和时抵消。

### 15.5 商谱

正文：[05-spectrum-as-invariant.tex](../../../tex/03-graphs/05-matrices-and-spectra/02-adjacency-matrix/05-spectrum-as-invariant.tex)

本节定义等价划分、商矩阵与商谱，证明从统一初色出发的颜色细化稳定划分是最粗的等价划分（公平划分），并建立商矩阵实谱性、交织恒等式与商谱精确嵌入完整邻接谱的定理体系。

#### 15.5.1 商矩阵

1. 在四点五边图上对$C_1=\{1,3\}$赋$a$、对$C_2=\{2,4\}$赋$b$（图`fig:adjacency-quotient-block-values`），验证$\bm A$作用后同块顶点保持相同输出$a+2b$与$2a$，可由$2\times 2$小矩阵$\bm Q=\bigl[\begin{smallmatrix}1&2\\2&0\end{smallmatrix}\bigr]$描述。
2. 给出等价划分、商矩阵$\bm Q=(q_{i,j})$与商谱$\operatorname{spec}(\bm Q)$的定义`def:adjacency-equitable-partition`，算出四点五边图的商谱为$\{(1\pm\sqrt{17})/2\}$。

#### 15.5.2 公平划分

1. 从顶点着色视角给出公平划分的定义`def:fair-partition`（色类$C_i$中任意顶点在$C_j$中的邻居数恒为常数$b_{i,j}$），说明公平划分与等价划分条件完全一致，重点在于它可由颜色细化算法自动生成。

##### 15.5.2.1 颜色细化的稳定划分

1. 阐述从统一初色出发的颜色细化迭代过程，结合图`fig:adjacency-color-refinement-steps`演示四点五边图经两轮迭代稳定于$\{\{1,3\},\{2,4\}\}$，并对比$C_6$始终保持单一色类。
2. 陈述并证明定理`thm:stable-is-equitable`：颜色细化达到稳定时，同色类顶点在下一轮不被拆开意味着它们对每个色类的邻居计数均相等，故稳定划分必为公平划分。

##### 15.5.2.2 最粗等价划分

1. 给出划分细化偏序关系的定义`def:partition-refinement`（$\mathcal P$的每块完整包含于$\mathcal P'$的某块中），以四点集划分例子说明细化与非细化的区别。
2. 陈述并证明定理`thm:color-refinement-coarsest`（从统一初色出发得到的公平划分$\mathcal P_{\mathrm{stable}}$是最粗的等价划分）：对细化轮数$t$归纳，利用当前色类是任意等价划分$\mathcal P$若干块的并集，证明同一$\mathcal P$块中的顶点对任意当前色类的邻居总数恒相等、永不分裂，故$\mathcal P$必为$\mathcal P_{\mathrm{stable}}$的细化；最后说明如何在两图不交并上同步运行颜色细化比较商矩阵。

#### 15.5.3 公平划分的性质

本小节通过三个形式化定理严格建立商矩阵的实谱性质、块常值不变子空间交织关系以及商谱嵌入与剩余谱的正交分解。

##### 15.5.3.1 商矩阵的实谱

1. 说明从统一初色出发得到的稳定划分作为最粗等价划分唯一确定，其商矩阵$\bm Q$在块置换下唯一；以三点路径$P_3$的$\bm Q=\bigl[\begin{smallmatrix}0&1\\2&0\end{smallmatrix}\bigr]$说明商矩阵一般不对称。
2. 陈述并证明商矩阵的实谱性质定理`thm:quotient-matrix-real-spectrum`：通过从$C_i$与$C_j$两侧双向计数跨块边数证得$|C_i|b_{i,j}=|C_j|b_{j,i}$即$\bm D_C\bm Q=\bm Q^\top\bm D_C$（式`eq:adjacency-quotient-symmetry`），进而证明$\widetilde{\bm Q}=\bm D_C^{1/2}\bm Q\bm D_C^{-1/2}$是实对称矩阵，故$\bm Q$在$\mathbb R$上可对角化且特征值全为实数。

##### 15.5.3.2 商谱嵌入

1. 定义$n\times k$块指示矩阵$\bm S$（$\bm S^\top\bm S=\bm D_C$）、$k$维块常值子空间$\mathcal W=\operatorname{col}(\bm S)$以及$n-k$维块内零和正交补空间$\mathcal W^\perp=\ker(\bm S^\top)$。
2. 陈述并证明商矩阵的交织恒等式定理`thm:quotient-intertwining`：逐项比对$(\bm A\bm S)_{u,j}=|N(u)\cap C_j|$与$(\bm S\bm Q)_{u,j}=b_{i,j}$证明公平划分充要条件为$\bm A\bm S=\bm S\bm Q$（式`eq:adjacency-quotient-intertwining`），并由此证明$\mathcal W$与$\mathcal W^\perp$均为$\bm A$的不变子空间。
3. 陈述并证明商谱嵌入定理`thm:quotient-spectrum-inclusion`：若$\bm Q\bm y=\lambda\bm y$则$\bm A(\bm S\bm y)=\lambda(\bm S\bm y)$；完整邻接谱按重数分解为商谱$\operatorname{spec}(\bm Q)$与$\mathcal W^\perp$上的剩余谱$\operatorname{spec}(\bm A|_{\mathcal W^\perp})$之并；且由Perron非负特征向量在$\mathcal W$上的非零正交投影证明最大特征值$\lambda_1(\bm A)\in\operatorname{spec}(\bm Q)$。
4. 在四点五边图上完整算出$\mathcal W$中的商谱$\{(1\pm\sqrt{17})/2\}$与$\mathcal W^\perp$中两个反对称基向量$\bm z_1=(1,0,-1,0)^\top$（特征值$-1$）、$\bm z_2=(0,1,0,-1)^\top$（$\bm A\bm z_2=\bm 0$，特征值$0$）对应的剩余谱。

##### 15.5.3.3 商谱的局限

1. 从正交直和分解$\mathbb R^n=\mathcal W\oplus\mathcal W^\perp$剖析商谱为何丢失信息：商矩阵$\bm Q=(b_{i,j})$仅记录色类之间与色类内部的平均连接次数，完全决定块常值子空间$\mathcal W$上的商谱（含$\lambda_1(\bm A)$），但任何保持各点对各色类邻居数$b_{i,j}$不变的块内重连都只改变零和正交补空间$\mathcal W^\perp$上的作用与剩余谱$\operatorname{spec}(\bm A|_{\mathcal W^\perp})$。
2. 以图`fig:adjacency-c6-vs-2c3-quotient`对比六点环$C_6$与两个不交三角形$2C_3=C_3\sqcup C_3$：两图均为$6$顶点$2$正则图，公平划分均退化为单一色类$C_1=V$、商矩阵同为$\bm Q=(2)$、商谱同为$\{2\}$，但在$5$维零和子空间$\mathcal W^\perp=\bm 1^\perp$上的剩余谱分别为$\{1,1,-1,-1,-2\}$与$\{2,-1,-1,-1,-1\}$（后者在$\bm x_{\mathrm{diff}}=(1,1,1,-1,-1,-1)^\top\in\mathcal W^\perp$上给出第二个特征值$2$），完整邻接谱能立刻区分两图而商谱不能。
3. 结合$C_6$与$2C_3$（颜色细化无法区分、完整谱通过$\mathcal W^\perp$区分）以及五顶点同谱对$K_{1,4}$与$C_4\sqcup K_1$（完整谱相同、颜色细化第一轮按度划分即区分），说明颜色细化（公平划分）与完整邻接谱是两种互不蕴含的图同构必要条件，而商谱则是两者共同捕获的块间宏观谱信息。

### 15.6 本章小结

正文：[06-summary.tex](../../../tex/03-graphs/05-matrices-and-spectra/02-adjacency-matrix/06-summary.tex)

1. 回顾矩阵幂行走计数定理与闭行走迹、谱矩公式，以及完全图、完全二部图、环、路径、笛卡儿积图与正则补图的显式谱。
2. 总结非负加权邻接谱的Perron定理、度上下界、子图单调性与二部图谱对称判别，以及边数、三角形数、直径、色数和独立数的谱刻画。
3. 总结同谱图反例（$K_{1,4}$与$C_4\sqcup K_1$）与公平划分商谱分解（$\mathbb R^n=\mathcal W\oplus\mathcal W^\perp$，$C_6$与$2C_3$对比），引出下一章能由零空间直接揭示连通分量的拉普拉斯矩阵。

## 第16章 拉普拉斯矩阵

正文：[03-laplacian-matrix.tex](../../../tex/03-graphs/05-matrices-and-spectra/03-laplacian-matrix.tex)

章职责与主线：把沿边差分、加权与汇总合成顶点空间上的矩阵，依次从逐点表达和二次型解释连通性，从约化行列式读出生成树，再以特征值比较变化尺度。度归一化消除整体边权尺度，并把邻域加权平均和对称谱分析联系起来。

章首引言的自然段：

1. 固定四点环加边$13$和默认单位权，并说明本章处理的非负权图。
2. 代入图中的读数，计算顶点$1$与三个邻居之差的总和为六，再把逐点计算概括为输入顶点读数、输出顶点偏离的线性变换。
3. 为防止有符号差相消，逐边平方并乘权求和。将这个量与拉普拉斯二次型和图的连通分量相连。
4. 由删去同一个顶点的行列提出生成树计数，再以特征值比较等长读数的能量，最后按度重新计量长度。

### 16.1 组合拉普拉斯

正文：[01-combinatorial-laplacian.tex](../../../tex/03-graphs/05-matrices-and-spectra/03-laplacian-matrix/01-combinatorial-laplacian.tex)

本节建立加权度与度矩阵、组合拉普拉斯矩阵的逐点定义以及它与带符号关联矩阵的分解关系。

#### 16.1.1 加权度与度矩阵

1. 重申$\bm W$的尺寸、非负对称边权和无边位置取零的约定，展开$\bm W\bm x$的单行并用四点图实算邻居读数总和。
2. 定义加权度$d_i=\sum_j w_{i,j}$及度矩阵$\bm D$，说明$d_i=0$当且仅当顶点$i$是正权支撑$\mathcal G_+$中的孤立顶点。
3. 在四点图上分别计算单位权与对角边权加倍时的度向量，固定后文算例仍取单位权。

#### 16.1.2 组合拉普拉斯的定义

1. 从顶点相对于各邻居读数的带权偏离总和定义组合拉普拉斯矩阵$\bm L=\bm D-\bm W$（定义`def:graph-combinatorial-laplacian`），并说明正度顶点处的输出等于$d_i$乘以本点读数相对邻居加权平均值的偏离。
2. 按边分三步（$\bm B^\top$沿边取差、$\bm C$乘边权、$\bm B$按顶点汇总）导出关联矩阵分解$\bm L=\sum_{e\in E}w_e\bm b_e\bm b_e^\top=\bm B\bm C\bm B^\top$（式`eq:graph-laplacian-incidence-factorization`），配图`fig:laplacian-readings-aggregation`演示四点算例，并写出$4\times 4$矩阵$\bm L$。

### 16.2 拉普拉斯二次型

正文：[01-combinatorial-laplacian.tex](../../../tex/03-graphs/05-matrices-and-spectra/03-laplacian-matrix/01-combinatorial-laplacian.tex)

本节定义组合拉普拉斯矩阵$\bm L$所对应的二次型，证明$\bm L$的半正定性、平移不变性与边权可加性，阐述二次型与顶点读数沿边平滑程度及子集割边代价的关系，并简介其在图分割与图信号去噪中的应用。

#### 16.2.1 拉普拉斯二次型的定义

1. 对比逐点线性输出$(\bm L\bm x)_i$中正负邻边差可相消的现象（如三点路径上$(0,1,2)^\top$在中间点输出$0$），利用关联分解$\bm L=\bm B\bm C\bm B^\top$将$\bm x^\top\bm L\bm x$转写到边空间，给出拉普拉斯二次型与沿边变化能量的定义`def:graph-dirichlet-energy`（式`eq:graph-laplacian-energy`）。

#### 16.2.2 拉普拉斯二次型的性质

1. 陈述并证明定理`prop:graph-laplacian-quadratic-form`：（1）$\bm L$为实对称半正定矩阵（$\bm x^\top\bm L\bm x\geq 0$），且$\bm x^\top\bm L\bm x=0\iff$每条正权边两端取值相等；（2）常数平移不变性$(\bm x+c\bm 1)^\top\bm L(\bm x+c\bm 1)=\bm x^\top\bm L\bm x$；（3）关于边权叠加的线性可加性与非减单调性。

#### 16.2.3 二次型与图结构

1. 说明对一般实向量$\bm x\in\mathbb R^n$，相连顶点取值越相近则$\bm x^\top\bm L\bm x$越小，从而度量顶点函数沿图结构的平滑度；在四点五边图上对比平滑赋值与交替反号赋值的二次型大小。
2. 证明当$\bm x=\bm 1_S$取为子集$0$–$1$指示向量时，二次型$\bm 1_S^\top\bm L\bm 1_S=c(S,V\setminus S)$（式`eq:graph-laplacian-cut-energy`）精确等于跨子集边界被切断的边的总权重（$\pm 1$二分向量则为$4\,c(S,V\setminus S)$），并在四点五边图上用$\bm 1_{\{1,3\}}$与$\bm e_1=\bm 1_{\{1\}}$核对（图`fig:laplacian-edge-energy`）。

#### 16.2.4 在图问题中的应用

1. 简要介绍拉普拉斯二次型的两类代表性应用：一是图分割，将离散割边代价$\bm 1_S^\top\bm L\bm 1_S$松弛为连续实向量上的二次型最小化（衔接第18章谱划分）；二是图信号处理中的去噪与半监督平滑，以$\min_{\bm x}\{\lVert\bm x-\bm y\rVert_2^2+\gamma\bm x^\top\bm L\bm x\}$（式`eq:graph-laplacian-denoising`）对应的线性系统$(\bm I+\gamma\bm L)\bm x=\bm y$滤除沿边高频毛刺（衔接第17章电网络能量最小化）。

### 16.3 拉普拉斯谱

正文：[03-laplacian-eigenvalues.tex](../../../tex/03-graphs/05-matrices-and-spectra/03-laplacian-matrix/03-laplacian-eigenvalues.tex)

本节介绍组合拉普拉斯矩阵$\bm L$的特征值与正交谱分解，证明零特征值重数等于正权支撑的连通分量个数，分别建立特征值的上下界与加边单调性，并按图族求出完全图、环、路径、星图与补图的拉普拉斯谱。

#### 16.3.1 特征值

1. 给出实对称半正定矩阵$\bm L$的升序特征值$0=\lambda_1\leq\lambda_2\leq\cdots\leq\lambda_n$（拉普拉斯谱）与正交谱分解$\bm L=\bm U\bm\Lambda\bm U^\top$（式`eq:graph-laplacian-spectral-energy`），写出瑞利商变分刻画与迹恒等式$\sum_{i=1}^n\lambda_i=\operatorname{tr}\bm L=\sum_{i=1}^n d_i=2\sum_{e\in E}w_e$。
2. 在四点五边单位权图上具体计算四个正交特征向量与特征值$0,2,4,4$（图`fig:laplacian-four-modes`），并用度数总和$10$核对迹恒等式。

#### 16.3.2 零特征值

1. 陈述并证明定理`thm:graph-laplacian-components`（式`eq:graph-laplacian-kernel-components`）：由$\bm x^\top\bm L\bm x=0\iff$每条正权边两端相等，沿正权路径传递证得$\ker\bm L=\operatorname{span}\{\bm 1_{V_1},\ldots,\bm 1_{V_c}\}$、$\operatorname{rank}\bm L=n-c$，且零特征值重数等于正权支撑连通分量个数$c$（图连通当且仅当$\lambda_2>0$）。
2. 在两条不交边與四点五边图上核对零空间维数，并指出连通图在$\bm 1^\perp$上严格正定。

#### 16.3.3 特征值的上下界

1. 陈述并证明定理`prop:graph-laplacian-eigenvalue-bounds`：由$(x_i-x_j)^2\leq 2(x_i^2+x_j^2)$导出最大度上界$0\leq\lambda_i\leq 2d_{\max}$（式`eq:graph-laplacian-spectrum-bound`），并由迹恒等式导出平均度界$\lambda_2\leq\frac{n}{n-1}d_{\mathrm{avg}}\leq\lambda_n$。

#### 16.3.4 特征值的单调性

1. 陈述并证明定理`thm:graph-laplacian-monotonicity`：在固定顶点集上加边或增权增加半正定秩一项$a\bm b_e\bm b_e^\top$，结合Courant–Fischer定理证得逐个特征值单调不减$\lambda_i(\bm L')\geq\lambda_i(\bm L)$（式`eq:graph-laplacian-edge-monotonicity`）。
2. 以四点环$C_4$（谱$0,2,2,4$）添入对角边$13$变为四点五边图（谱$0,2,4,4$）核对各特征方向的变化，并说明删点不适用该单调性。

#### 16.3.5 典型图的拉普拉斯谱

说明简单无权$d$正则图满足$\bm L=d\bm I-\bm A$，特征值由邻接特征值换算为$d-\alpha$，进而分五个小节求出典型图族的拉普拉斯谱。

##### 16.3.5.1 完全图

1. 陈述并证明定理`prop:graph-typical-laplacian-spectra`：利用$n-1$正则图关系或$\bm L(K_n)=n\bm I-\bm 1\bm 1^\top$求出$K_n$的拉普拉斯谱为$0$（重数$1$）和$n$（重数$n-1$）。

##### 16.3.5.2 环

1. 陈述并证明定理`thm:graph-cycle-laplacian-spectra`：由$2$正则图的邻接特征值换算得出$C_n$的拉普拉斯特征值$\lambda_k^{(C)}=2-2\cos(2\pi k/n)$（式`eq:graph-cycle-laplacian-spectrum`）。

##### 16.3.5.3 路径

1. 陈述并证明定理`thm:graph-path-laplacian-spectra`：在路径$P_n$两端外侧引入等值虚拟边界$x_0=x_1,x_{n+1}=x_n$，代入半格偏移余弦模式$\cos((i-1/2)\theta)$求出特征值$\lambda_k^{(P)}=2-2\cos(k\pi/n)$（式`eq:graph-path-laplacian-spectrum`）。

##### 16.3.5.4 星图

1. 陈述并证明定理`thm:graph-star-laplacian-spectrum`：按叶顶点零和子空间、常向量与中心反号向量求出星图$K_{1,n-1}$的拉普拉斯谱为$0$（重数$1$）、$1$（重数$n-2$）和$n$（重数$1$），并对比$K_{1,3}$与$P_4$的谱。

##### 16.3.5.5 补图

1. 由$\bm L(\overline{\mathcal G})=n\bm I-\bm 1\bm 1^\top-\bm L(\mathcal G)$（式`eq:graph-complement-laplacian`）导出一般简单无权图的补图拉普拉斯谱$0,n-\lambda_n,\ldots,n-\lambda_2$，并由此说明简单无权图恒有$\lambda_n\leq n$且取等号当且仅当补图不连通。

### 16.4 拉普拉斯谱与生成树

正文：[02-matrix-tree-theorem.tex](../../../tex/03-graphs/05-matrices-and-spectra/03-laplacian-matrix/02-matrix-tree-theorem.tex)

本节将组合拉普拉斯矩阵的主余子式与去掉一个零特征值后的其余特征值应用于图的生成树计数，依次通过约化关联子式、矩阵树定理与特征多项式系数建立生成树计数的拉普拉斯谱公式，并导出完全图的Cayley公式。

#### 16.4.1 生成树的关联子式

1. 固定根顶点$r$删去第$r$行得到约化关联矩阵$\overline{\bm B}$，陈述并证明引理`lem:graph-tree-incidence-minors`：若$n-1$元边集$S$含环则环上列线性相关、行列式为$0$；若$S$无环则必构成生成树，沿非根叶所在行递归拉普拉斯展开证得$\det(\overline{\bm B}_{:,S})\in\{\pm 1\}$。
2. 在四点算例中对比生成树路径$\{12,23,34\}$（下三角阵行列式$1$）与三角形$\{12,23,13\}$（行列式$0$）（图`fig:laplacian-tree-minors`）。

#### 16.4.2 生成树的代数余子式计数

1. 令$\bm M=\overline{\bm B}\bm C^{1/2}$使$\overline{\bm L}=\bm M\bm M^\top$，陈述并证明矩阵树定理`thm:graph-matrix-tree`（式`eq:graph-matrix-tree`）：应用卷二“向量、矩阵与张量的运算”章的Cauchy–Binet公式与引理`lem:graph-tree-incidence-minors`及行和为零性质，证得$\bm L$在任意位置$(i,j)$处的代数余子式$(-1)^{i+j}\det\bm L^{(i,j)}$（含主余子式$\det\overline{\bm L}$）均等于$\sum_{T\in\mathcal T}\prod_{e\in T}w_e$。
2. 在四点五边图上展开$3\times 3$约化行列式算出$\det\overline{\bm L}=8$，与$\binom{5}{3}=10$组三元边集中剔除$2$个三角形后剩余的$8$棵生成树核对，并验证边$13$权重改为$2$时的加权树和$12$。

#### 16.4.3 生成树的拉普拉斯谱公式

1. 陈述并证明定理`cor:graph-tree-count-spectrum`：比较$\det(t\bm I+\bm L)=t\prod_{i=2}^n(t+\lambda_i)$在$t$的一次项上的谱展开系数与按列拉普拉斯展开的$n$个主余子式之和，证得生成树权和的谱公式$\sum_{T\in\mathcal T}\prod_{e\in T}w_e=\frac1n\prod_{i=2}^n\lambda_i$（式`eq:graph-tree-count-from-spectrum`）。
2. 用第16.3.1小节求出的四点五边图特征值$0,2,4,4$核对$(2\cdot 4\cdot 4)/4=8$，并检验边权缩放的齐次性。

#### 16.4.4 完全图的Cayley公式

1. 陈述并证明定理`thm:graph-cayley-formula`：将第16.3.5.1小节求出的完全图$K_n$拉普拉斯谱代入谱计数公式，导出标号树总数公式$|\mathcal T(K_n)|=n^{n-2}$（式`eq:graph-cayley-count`），并在约化矩阵$\overline{\bm L}$与星图$K_{1,n-1}$上核对。

### 16.5 归一化拉普拉斯

正文：[04-normalized-laplacian.tex](../../../tex/03-graphs/05-matrices-and-spectra/03-laplacian-matrix/04-normalized-laplacian.tex)

区分$-\bm L$生成的连续时间扩散与$\bm P$表示的每步转移，归一化消除整体边权倍数而非任意局部重加权；二次型的平方根是半范数。

本节分段阐述双团哑铃图（桥端点跨团转移概率被稀释为$1/m$）与含超级节点的网络中随机游走扩散速度的两个典型例子（配图`fig:laplacian-diffusion-bottleneck`），说明未归一化的组合拉普拉斯谱受局部度数尺度干扰、无法直接刻画扩散速度，进而引入度加权内积、对称归一化拉普拉斯$\mathcal L$与随机游走拉普拉斯$\bm L_{\mathrm{rw}}$，对比两种归一化矩阵并证明归一化拉普拉斯谱的性质。

#### 16.5.1 度加权内积

1. 在正度顶点集$V_+$上定义度加权内积$\langle\bm x,\bm y\rangle_{\bm D}=\bm x^\top\bm D\bm y$（式`eq:graph-degree-weighted-inner-product`），验证任意正度顶点单位脉冲的能量与度加权范数平方之比恒为$1$。
2. 将子集指示向量的度加权范数平方定义为集合体积$\operatorname{vol}(S)=\sum_{i\in S}d_i=\lVert\bm 1_S\rVert_{\bm D}^2$（式`eq:graph-laplacian-vertex-volume`），说明度加权Rayleigh商$\frac{\bm 1_S^\top\bm L\bm 1_S}{\bm 1_S^\top\bm D\bm 1_S}=\frac{c(S,V\setminus S)}{\operatorname{vol}(S)}$直接度量跨割边权占子集连接体积的比例，并说明孤点在全空间中的处理。

#### 16.5.2 对称归一化拉普拉斯

1. 通过可逆坐标缩放$\bm y=\bm D^{1/2}\bm x$将广义Rayleigh商$\frac{\bm x^\top\bm L\bm x}{\bm x^\top\bm D\bm x}$转化为普通欧氏Rayleigh商，给出对称归一化拉普拉斯$\mathcal L=\bm D^{-1/2}\bm L\bm D^{-1/2}=\bm I-\bm D^{-1/2}\bm W\bm D^{-1/2}$的定义`def:graph-symmetric-normalized-laplacian`（式`eq:graph-symmetric-normalized-laplacian`）。
2. 说明缩放坐标下的零方向变为$\bm D^{1/2}\bm 1_{V_a}$（图`fig:laplacian-degree-coordinates`），并核对含孤点时的零行零列约定。

#### 16.5.3 随机游走拉普拉斯

1. 定义邻域加权平均算子$\bm P=\bm D^{-1}\bm W$（式`eq:graph-random-walk-neighbor-average`）与随机游走拉普拉斯$\bm L_{\mathrm{rw}}=\bm I-\bm P=\bm D^{-1}\bm L$（定义`def:graph-random-walk-laplacian`，式`eq:graph-random-walk-laplacian`），在四点图上逐点核对$\bm L_{\mathrm{rw}}(1,0,1,0)^\top$。
2. 证明$\bm P$与$\bm L_{\mathrm{rw}}$在度加权内积下自伴，并联系第20章的随机游走一步转移概率。

#### 16.5.4 两种归一化拉普拉斯的对比

本小节从相似关系、对称性与应用场景三个方面对比$\mathcal L$与$\bm L_{\mathrm{rw}}$。

##### paragraph：相似关系

1. 由正度空间上的相似变换$\mathcal L=\bm D^{1/2}\bm L_{\mathrm{rw}}\bm D^{-1/2}$（式`eq:graph-normalized-laplacian-similarity`）证明两者特征值完全相同，且特征向量按$\bm y=\bm D^{1/2}\bm x$换算（零特征向量分别为$\bm 1_{V_a}$与$\bm D^{1/2}\bm 1_{V_a}$）。

##### paragraph：对称性

1. 说明$\mathcal L$在标准欧氏内积下实对称、可选取标准正交特征基，而$\bm L_{\mathrm{rw}}$对称当且仅当每条正权边两端度数相等；它在度加权内积下自伴，可选取关于$\bm D$正交的特征基。

##### paragraph：应用场景

1. 说明$\mathcal L$适合对称谱分解与谱划分（第18章）、谱稀疏化（第19章），$\bm L_{\mathrm{rw}}=\bm I-\bm P$适合局部邻域平均与马尔可夫链随机游走演化（第20章），并在正度$d$正则图下统一为$\bm L/d$。

#### 16.5.5 归一化拉普拉斯谱的性质

1. 陈述并证明定理`prop:graph-normalized-spectrum-bound`（式`eq:graph-normalized-spectrum-bound`）：利用恒等式$2\bm x^\top\bm D\bm x-\bm x^\top\bm L\bm x=\sum_{\{i,j\}\in E}w_{i,j}(x_i+x_j)^2\geq 0$证明全部归一化特征值满足$0\leq\mu\leq 2$，零特征值重数为$c$，且最大特征值达到$\mu=2$当且仅当正权支撑含有至少一条边的二部连通分量。
2. 在四点环$C_4$与四点五边图上核对$\mu=2$的存在性，并说明边权整体缩放不变性。

### 16.6 本章小结

正文：[05-summary.tex](../../../tex/03-graphs/05-matrices-and-spectra/03-laplacian-matrix/05-summary.tex)

1. 回顾组合拉普拉斯$\bm L=\bm D-\bm W=\bm B\bm C\bm B^\top$及其二次型$\bm x^\top\bm L\bm x$的定义、半正定等性质、平滑度与割边代价含义以及在图分割与去噪中的应用。
2. 总结拉普拉斯谱的迹恒等式、零特征值与连通分量的对应、度数上下界、加边单调性、典型图族显式谱，以及矩阵树定理、生成树谱计数公式与Cayley公式。
3. 总结区分连续时间扩散与离散逐步转移后引入的度加权内积、对称归一化拉普拉斯$\mathcal L$与随机游走拉普拉斯$\bm L_{\mathrm{rw}}$的对比及归一化谱在$[0,2]$上的性质，并预告后续三章的应用。

## 第17章 电网络

正文：[04-electrical-networks.tex](../../../tex/03-graphs/05-matrices-and-spectra/04-electrical-networks.tex)

章职责与主线：给定顶点注入后，研究怎样求出支路电流、电势差和点对有效电阻。组合拉普拉斯把电势变为注入，能量原理将同一解刻画为最小耗散流，批量近似将电阻查询变为低维距离计算。

1. 以四点环加对角边为贯穿算例，从对角线一端注入、另一端引出，提出怎样分流以及需要多大压降的问题。
2. 分开逐边写电势与电流的关系以及逐点汇总流出和流入，再联立得到以电势为未知量的组合拉普拉斯方程，求解后逐边恢复电流。
3. 将不同分流方案放在一起比较耗散，由单位分流所需的端点压降引出有效电阻，并指出它在稀疏化与往返时间计算中的用途。

### 17.1 电网络的基本定律

正文：[01-network-laws.tex](../../../tex/03-graphs/05-matrices-and-spectra/04-electrical-networks/01-network-laws.tex)

本节将正权无向图解释为电阻电网络，依次建立边的电导与电阻、接点电流守恒与闭环压降守恒的Kirchhoff定律，以及连接单边压降与电流的Ohm定律。

#### 17.1.1 电导与电阻

1. 定义边的电导$c_e=w_e>0$与电阻$r_e=1/c_e$，说明零电导边不传流、正权支撑即有效导电网络。
2. 约定有向参考边$e\colon i\to j$上的带符号电流向量$\bm f\in\mathbb R^m$，并由顶点电势$\bm v\in\mathbb R^n$定义沿边压降向量$\Delta\bm v=\bm B^\top\bm v$。

#### 17.1.2 Kirchhoff定律

本小节分别建立接点上的Kirchhoff电流定律与闭合回路上的Kirchhoff电压定律。

##### paragraph：Kirchhoff电流定律

1. 用关联矩阵$\bm B$的第$i$行汇总接点$i$的净流出量$(\bm B\bm f)_i$，结合外部注入$b_i$给出Kirchhoff电流定律$\bm B\bm f=\bm b$（式`eq:electrical-current-conservation`，图`fig:electrical-local-current-balance`）。
2. 将全部顶点守恒式相加消去内部边电流，导出全图（以及每个正权连通分量）外部注入总和必须为零（$\bm 1^\top\bm b=0$）的必要条件。

##### paragraph：Kirchhoff电压定律

1. 沿任意闭环绕行一周累加电势降，顶点电势逐项相消为零，给出Kirchhoff电压定律（图`fig:electrical-ohm-and-kvl`(b)）。
2. 用第14章割空间$\operatorname{im}\bm B^\top$与环空间$\ker\bm B$的正交性$\bm c^\top(\bm B^\top\bm v)=(\bm B\bm c)^\top\bm v=0$解释闭环压降和为零的充要性。

#### 17.1.3 Ohm定律

1. 给出单边与全图Ohm定律$\bm f=\bm C\bm B^\top\bm v$（式`eq:electrical-ohm-law`，图`fig:electrical-ohm-and-kvl`(a)），说明电势整体平移常数不改变压降和电流。

### 17.2 拉普拉斯方程的求解

正文：[02-laplacian-solve.tex](../../../tex/03-graphs/05-matrices-and-spectra/04-electrical-networks/02-laplacian-solve.tex)

本节在节首分“沿边取压降$\bm B^\top\bm v$—乘电导得电流$\bm C\bm B^\top\bm v$—代入守恒式$\bm B\bm f=\bm b$”三步联立导出电网络拉普拉斯方程$\bm L\bm v=\bm b$（式`eq:electrical-laplacian-system`），进而依次建立可解性充要条件、接地唯一解、一般网络的数值求解以及树网络上的两遍线性时间求解算法。

#### 17.2.1 拉普拉斯方程的可解性

1. 陈述并证明定理`thm:electrical-laplacian-solvability`：（1）连通网络上$\bm L\bm v=\bm b$有解当且仅当外部注入总和为零$\bm 1^\top\bm b=0$（式`eq:electrical-zero-sum-condition`）；（2）通解相差常数平移$c\bm 1$，且诱导边电流$\bm f=\bm C\bm B^\top\bm v$唯一；（3）零均值子空间$\bm 1^\perp$内的唯一解为$\bm v_{\mathrm{zm}}=\bm L^\dagger\bm b$。
2. 说明非连通网络在每个连通分量内独立满足注入总和为零与常数平移。

#### 17.2.2 接地与唯一解

1. 定义在参考顶点$q$处接地（$v_q=0$），说明删去$\bm L$的第$q$行与第$q$列得到$(n-1)$阶约化系统$\overline{\bm L}\,\overline{\bm v}=\overline{\bm b}$（式`eq:electrical-grounded-system`），并强调连向接地点$q$的边电导仍保留在$\overline{\bm L}$的对角元中。
2. 陈述并证明定理`prop:electrical-grounded-system`：证明$\overline{\bm L}$对称正定、约化方程存在唯一解$\overline{\bm v}=\overline{\bm L}^{-1}\overline{\bm b}$，且补入$v_q=0$后由$\bm 1^\top(\bm L\bm v-\bm b)=0$自动满足第$q$行守恒式。
3. 在四点单位电导网络上完整演算例`ex:electrical-four-vertex-network`（在顶点$3$接地，分三步解出$\bm v=(1/2,1/4,0,1/4)^\top$与边电流$\bm f=(1/4,1/4,-1/4,-1/4,1/2)^\top$，配图`fig:electrical-grounded-matrix`、`fig:electrical-grounding-overview`与`fig:electrical-current-split`）。

#### 17.2.3 一般网络的数值求解

1. 说明接地约化系统$\overline{\bm L}\,\overline{\bm v}=\overline{\bm b}$与零均值系统可直接调用卷二第三部分“线性方程与优化”中的求解方法：直接分解法（LU、Cholesky、分块$\bm L\bm D\bm L^\top$分解，结合图`fig:electrical-cholesky-fill-in`说明稀疏图消元填充现象）、定常迭代法（Richardson、Jacobi、Gauss–Seidel、SOR/SSOR）与行列投影法（Kaczmarz），以及Krylov子空间法与预条件技术（CG、MINRES、PCG，给出$O(n+m)$边扫描乘法与误差界`eq:electrical-cg-error`）。

#### 17.2.4 树上的线性时间求解

1. 利用树中删去任意边$e_i\colon i\to p(i)$即隔离子树$T_i$的性质，对$T_i$内守恒方程求和导出边电流等于子树注入总和$s_i=\sum_{u\in T_i}b_u=b_i+\sum_{j:p(j)=i}s_j$（式`eq:electrical-subtree-injection`），再由Ohm定律导出电势递推式$v_i=v_{p(i)}+r_{i,p(i)}s_i$（式`eq:electrical-tree-voltage`）。
2. 分三个阶段完整写出$O(n)$求解算法流程：第一阶段定根并构建从根到叶的父子遍历序列；第二阶段按逆序（子节点先于父节点）汇总子树注入求得全部边电流$s_i$并检验根处总和$s_q=0$；第三阶段固定$v_q=0$并按正序（父节点先于子节点）逐层累加压降恢复全部顶点电势$v_i$。
3. 在五顶点单位电阻树上配合图`fig:electrical-tree-two-pass`逐步演示两遍遍历的计算结果。

### 17.3 能量最小原理

电流二次型在物理量上表示耗散功率；只有共用两端电势的并联支路才按电导成比例分流，一般网络的某些边可能电流为零。

正文：[03-minimum-energy.tex](../../../tex/03-graphs/05-matrices-and-spectra/04-electrical-networks/03-minimum-energy.tex)

本节首先阐明电阻耗散的物理与数学含义，进而证明真实电网络电流在所有满足Kirchhoff电流守恒的候选流中使总耗散最小（Thomson原理）。

#### 17.3.1 电阻耗散

1. 从电荷通过电阻损失电势能转化为热能出发，由焦耳定律给出单边耗散功率$P_e=f_e\Delta v_e=r_e f_e^2=f_e^2/c_e$，并给出全网络流总耗散$\mathcal E(\bm f)=\sum_{e\in E}r_e f_e^2=\bm f^\top\bm C^{-1}\bm f$的定义`def:electrical-dissipation`（式`eq:electrical-dissipation`），说明真实Ohm流的总耗散恰好等于拉普拉斯二次型$\bm v^\top\bm L\bm v$。
2. 在四点单位电阻网络上对比同一单位注入下的三种守恒分流方案（图`fig:electrical-distribution-dissipation`）：独走对角边（$\mathcal E=1$）、平分到对角边与上路（$\mathcal E=3/4$）、真实Ohm分流（$\mathcal E=1/2$），说明二次平方惩罚促使电流向多条通路分散。

#### 17.3.2 Thomson原理

1. 陈述并证明定理`thm:electrical-thomson`（Thomson原理）：将任意守恒流写为$\bm f=\bm f_\star+\bm z$（其中$\bm z\in\ker\bm B$为环流），利用割空间与环空间正交性证得交叉项$\bm f_\star^\top\bm C^{-1}\bm z=\bm v^\top\bm B\bm z=0$，导出正交分解$\mathcal E(\bm f)=\mathcal E(\bm f_\star)+\mathcal E(\bm z)$（式`eq:electrical-dissipation-decomposition`）及最小耗散公式$\mathcal E(\bm f_\star)=\bm b^\top\bm L^\dagger\bm b$（式`eq:electrical-minimum-dissipation`）。
2. 在四点网络上配合图`fig:electrical-thomson-orthogonality`验证在$\bm f_\star$上叠加外圈环流$\frac14\bm c_1$后总耗散等于$1/2+1/4=3/4$，并与带容量约束的线性最小费用流作对比。

### 17.4 有效电阻

正文：[04-effective-resistance.tex](../../../tex/03-graphs/05-matrices-and-spectra/04-electrical-networks/04-effective-resistance.tex)

本节定义两点之间的有效电阻，系统介绍简单结构、小规模“死结”结构与中等规模网络上有效电阻的精确计算方法，以及大规模网络上的三种近似计算方法，最后证明有效电阻的度量性质与单调性。

#### 17.4.1 有效电阻的定义

1. 定义单位偶极注入$\bm b_{a,b}=\bm e_a-\bm e_b$下的两端电势差$R_{a,b}=v_a-v_b$为有效电阻（定义`def:graph-effective-resistance`，式`eq:electrical-resistance-definition`），说明其与接地点无关且将整张网络对端口$a,b$的作用等效为单个阻值$R_{a,b}$。
2. 导出有效电阻的伪逆二次型表达$R_{a,b}=\bm b_{a,b}^\top\bm L^\dagger\bm b_{a,b}=L^\dagger_{a,a}+L^\dagger_{b,b}-2L^\dagger_{a,b}$（式`eq:electrical-resistance-pseudoinverse`）与Thomson最小耗散表达$R_{a,b}=\min_{\bm B\bm f=\bm e_a-\bm e_b}\bm f^\top\bm C^{-1}\bm f$（式`eq:electrical-resistance-energy`）。

#### 17.4.2 有效电阻的计算

本小节按网络结构从简到繁介绍有效电阻的三类精确计算方法。

##### 17.4.2.1 简单结构：串联、并联与悬空支路

1. 导出度为$2$无源中间顶点的串联公式$r_{\mathrm{series}}=r_1+r_2$（式`eq:electrical-series`）、同端点多支路的并联公式$c_{\mathrm{parallel}}=\sum_i c_i$（式`eq:electrical-parallel`）以及无源悬空叶支路的剪除规则。
2. 在四点五边单位电阻图上分串联、并联两步算出$R_{1,3}=1/2$（图`fig:electrical-series-parallel-reduction`）。

##### 17.4.2.2 小规模桥式结构：星-三角变换

1. 说明查询四点五边图的$R_{2,4}$时两个内部顶点度均为$3$，单靠串并联不能消去它们，陈述并证明定理`thm:electrical-wye-delta`（星-三角$\text{Y--}\Delta$等效变换，式`eq:electrical-y-to-delta`与`eq:electrical-delta-to-y`）：通过消去无源度$3$中心顶点$w$证明星形与三角形子网端口等效。
2. 配合图`fig:electrical-wye-delta-bridge`在四点五边图上对三角形$\{1,3,4\}$作$\Delta\to\text{Y}$变换（星形支路阻值$1/3$），展示另一种等效归约并由串并联算出$R_{1,2}=5/8$。

##### 17.4.2.3 中等规模网络：求解拉普拉斯方程

1. 说明对一般中等规模网络可直接固定$v_b=0$求解正定线性方程组$\overline{\bm L}\,\overline{\bm v}=\overline{\bm e}_a$读取$R_{a,b}=v_a$。
2. 在四点单位电阻图上令$v_2=0$，分三步解出$\bm L\bm v=\bm e_1-\bm e_2$的电势$\bm v=(5/8,0,3/8,1/2)^\top$与各支路分流（图`fig:electrical-r12-potential-flow`），核对$R_{1,2}=5/8>R_{1,3}=1/2$。

#### 17.4.3 有效电阻的近似计算

本小节介绍大规模图上快速近似计算有效电阻的三种常见方法。

##### 17.4.3.1 欧氏嵌入与随机投影降维

1. 构造$m\times n$精确欧氏嵌入矩阵$\bm Z=\bm C^{1/2}\bm B^\top\bm L^\dagger$（式`eq:electrical-resistance-embedding`），证明$\bm Z^\top\bm Z=\bm L^\dagger$从而$R_{a,b}=\lVert\bm Z(\bm e_a-\bm e_b)\rVert_2^2$，并在四点图上核对$R_{1,3}$与$R_{1,2}$。
2. 引入$k\times m$随机高斯投影矩阵$\bm Q$构造低维坐标$\bm Y=\bm Q\bm Z$，通过求解$k=O(\varepsilon^{-2}\log n)$个拉普拉斯系统$\bm L\bm y_j=\bm B\bm C^{1/2}\bm q_j$（式`eq:electrical-projection-systems`）直接生成$\bm Y$（图`fig:electrical-resistance-coordinate-projection`），陈述并证明定理`thm:electrical-jl-resistance`（式`eq:electrical-projection-dimension`、`eq:electrical-projection-guarantee`），并给出迭代近似求解时的误差控制界（式`eq:electrical-resistance-total-error`）。

##### 17.4.3.2 谱展开与低频主模态截断

1. 由伪逆谱分解导出有效电阻的谱展开式$R_{a,b}=\sum_{i=2}^n\frac{1}{\lambda_i}(u_{i,a}-u_{i,b})^2$（式`eq:electrical-resistance-spectral-sum`），提出保留前$r$个最小非零特征模态的低秩截断近似$R_{a,b}^{(r)}$对$r\leq n-2$给出截断误差上界$2/\lambda_{r+2}$，保留全部$n-1$项时精确，在四点图上用三个非零特征模态核对$R_{1,2}=1/4+1/8+1/4=5/8$。

##### 17.4.3.3 随机游走与生成树蒙特卡洛估计

1. 给出基于随机游走逃逸概率的关系式$R_{a,b}=1/\bigl(d_a\mathbb P_a(\tau_b<\tau_a^+)\bigr)$（式`eq:electrical-resistance-escape`）与基于随机生成树包含概率的关系式$\mathbb P(e\in T)=c_e R_{a,b}$（式`eq:electrical-resistance-tree-probability`），说明随机树边包含频率除以电导可无偏估计边有效电阻；逃逸频率的倒数一般有偏且可能无定义，Wilson的运行成本依赖图上的首达时间。

#### 17.4.4 有效电阻的基本性质

1. 陈述并证明定理`thm:electrical-resistance-metric`（有效电阻的度量性质）：证明有效电阻在正权连通分量上满足非负非退化性、对称性与三角不等式$R_{a,c}\leq R_{a,b}+R_{b,c}$（式`eq:electrical-resistance-triangle`，利用无源顶点电势等于邻居加权平均推出引出端$b$达到最低电势$v_b\leq v_c$）。
2. 陈述并证明定理`thm:electrical-resistance-monotonicity`（有效电阻的Rayleigh单调性）：利用Thomson最小耗散原理证明增大电导或添边时有效电阻单调不增，并在四点图上对比添入对角边$13$（$R_{1,3}$从$1$降至$1/2$）与添入等势边$24$（$R_{1,3}$保持$1/2$不变）的例子。

#### 17.4.5 有效电阻与图结构

本小节利用单条边的电导与有效电阻之积$c_e R_e$刻画该边在图连通结构中的不可替代性，建立其与随机生成树包含概率的恒等式及Foster定理。

##### 17.4.5.1 生成树的边包含概率

1. 定义加权生成树分布$\mathbb P(T)\propto\prod_{e\in T}c_e$，利用矩阵树定理与秩一行列式微扰证明生成树边包含概率定理`thm:graph-tree-edge-probability`（$\mathbb P(e\in T)=c_e R_e$），并在四点五边图的$8$棵生成树上核对。

##### 17.4.5.2 Foster定理

1. 分别用生成树边数期望与拉普拉斯伪逆投影迹证明Foster定理`thm:graph-foster-theorem`（$\sum_{e\in E}c_e R_e=n-1$，对$k$个连通分量为$n-k$）。

### 17.5 本章小结

正文：[05-summary.tex](../../../tex/03-graphs/05-matrices-and-spectra/04-electrical-networks/05-summary.tex)

1. 回顾电网络的Ohm定律与Kirchhoff电流/电压定律，总结拉普拉斯方程$\bm L\bm v=\bm b$的导出、零和可解条件、接地正定系统、一般网络数值求解与树上两遍线性时间算法。
2. 回顾焦耳热耗散$\mathcal E(\bm f)=\bm f^\top\bm C^{-1}\bm f$与Thomson最小能量原理的正交分解。
3. 总结有效电阻的定义、精确计算（串并联、星-三角变换、解拉普拉斯方程）、大规模近似计算（随机投影、谱截断、蒙特卡洛采样）及度量单调性质，并预告其在第19章谱稀疏化与第20章随机游走往返时间中的应用。

## 第18章 图的谱划分

正文：[05-spectral-partition.tex](../../../tex/03-graphs/05-matrices-and-spectra/05-spectral-partition.tex)

章职责与主线：本章从连通度的几何图像与点、边连通度与割的规模信息之间的区别出发，引入组合拉普拉斯代数连通度$\lambda_2$与Fiedler向量$\bm v_2$，建立归一化谱的Cheeger不等式，并展开RatioCut与NCut两种谱划分算法。

### 18.1 代数连通度

正文：[01-algebraic-connectivity.tex](../../../tex/03-graphs/05-matrices-and-spectra/05-spectral-partition/01-algebraic-connectivity.tex)

本节通过四类典型图建立瓶颈与稀疏割的几何图像，比较点、边连通度与归一化稀疏割的计算困境，进而定义代数连通度$\lambda_2$并阐明Fiedler向量$\bm v_2$的物理意义与节域连通性。

#### 18.1.1 连通度的几何意义

1. 区分“是否连通”与“连通程度”，对比链状图（删边即断开）、杠铃图（单桥连接两团）、网格图（中间切口跨越多条边）与完全图（割边数为$s(n-s)$），提炼“瓶颈/稀疏割”的几何图像。

#### 18.1.2 连通度的度量

1. 定义点连通度$\kappa(\mathcal G)$、边连通度$\lambda(\mathcal G)$与最小度数$\delta(\mathcal G)$，说明点、边连通度是全局最小量但不记录分隔两侧规模；区分无权拓扑、加权最小割的连续性与可微性，再引入等周数$h(\mathcal G)$和RatioCut的一般精确计算困难，引出寻找连续可算替代品的动机。

#### 18.1.3 代数连通度

1. 给出代数连通度$\lambda_2(\mathcal G)$的Courant–Fischer变分定义与基本性质，并核对单桥连接两个$K_m$的杠铃图满足$\lambda_2=\Theta(m^{-1})$，对简单无权连通非完全图证明$\lambda_2(\mathcal G)\leq\kappa(\mathcal G)\leq\lambda(\mathcal G)\leq\delta(\mathcal G)$及全局稀疏割下界$\lambda_2(\mathcal G)/2\leq h(\mathcal G)$。

#### 18.1.4 Fiedler向量

1. 阐明$\lambda_2$对应特征向量$\bm v_2$的一维弹簧最小势能嵌入、振动基频模态与热扩散最慢衰减模态物理意义，并证明含零坐标的Fiedler节域连通性定理，说明该结论不保证最优割；振动角频率为$\sqrt{\lambda_2}$，重特征值对应多个同速扩散方向。

### 18.2 Cheeger不等式

正文：[02-cheeger-inequality.tex](../../../tex/03-graphs/05-matrices-and-spectra/05-spectral-partition/02-cheeger-inequality.tex)

明确对称归一化特征向量$\bm z$与广义特征向量$\bm f=\bm D^{-1/2}\bm z$的区别，阈值扫描使用后者；度加权中位数允许位于恰好等分体积的两个相邻读数之间。

本节以集合体积替代顶点数引入度数归一化的导通率$\phi_*$，并利用对称归一化拉普拉斯的第二小特征值$\mu_2$建立双向夹逼的Cheeger不等式$\mu_2/2\leq\phi_*\leq\sqrt{2\mu_2}$。

#### 18.2.1 导通率

1. 对比跨海单桥与末梢单叶说明按度体积衡量规模的必要性，定义割权$c(S,\bar S)$、集合体积$\operatorname{vol}(S)$与导通率$\phi(S)$，并在四点路径上对比中间割（$\phi=1/3$）与端点割（$\phi=1$）。
2. 将导通率与对称归一化拉普拉斯$\mathcal L$的广义Rayleigh商$\mu_2$对接，陈述Cheeger不等式并阐明下界（无瓶颈谱证书）与上界（阈值扫描构造性算法）的含义。

#### 18.2.2 下界：指示向量的Rayleigh商

1. 对任意割$(S,\bar S)$构造度加权零和的两值试探向量$\bm f=\bm 1_S-\frac{a}{a+b}\bm 1$，分步算出分子$\bm f^\top\bm L\bm f=c(S,\bar S)$与分母$\bm f^\top\bm D\bm f=\frac{ab}{a+b}$，代入变分最小性质导出下界$\mu_2/2\leq\phi_*$。

#### 18.2.3 上界：扫描阈值

1. 分三步证明构造性上界$\phi_*\leq\sqrt{2\mu_2}$：先按度加权中位数平移并截取支撑体积不超过半图的非负向量$\bm g$；再将水平集$S_t=\{i:g_i^2>t\}$的割权与体积对阈值$t$积分，由积分平均原理定位合格阈值；最后用平方差分解与Cauchy–Schwarz不等式完成放缩，并在四点路径上核对排序前缀扫描。

#### 18.2.4 两端的紧性

1. 剖析Cheeger不等式下界一次方$\Theta(\mu_2)$与上界平方根$\Theta(\sqrt{\mu_2})$各自不可改进的几何原因：在超立方体$Q_d$上连续特征向量呈跨割两值突变，下界$\phi_*=\mu_2/2=1/d$精确取等；在长偶数环$C_n$上，余弦向量的能量分子为$\Theta(n^{-1})$、度加权长度平方为$n$，故归一化后$\mu_2=\Theta(n^{-2})$而$\phi_*=2/n=\Theta(\sqrt{\mu_2})$。

#### 18.2.5 扩展图与混合引理

1. 从兼具常数度稀疏性与一致正导通率/谱隙的需求引出扩展图（expander graph）与$(n,d,\lambda)$-图的定义，通过沿常值主特征向量与正交补空间$\bm 1^\perp$分解子集指示向量，证明扩展图混合引理$\bigl|e(S,T)-\frac{d}{n}|S||T|\bigr|\le\lambda\sqrt{|S||T|(1-|S|/n)(1-|T|/n)}$，并导出割边数夹逼界与使用双侧谱界的独立数上界，并与使用最小特征值的Hoffman界区分；说明均匀基准矩阵不等同于无自环随机简单图的期望，区分Ramanujan图排除$\pm d$的约定与本节双侧参数，并区分对数级混合时间和访问全部顶点的遍历时间。

### 18.3 RatioCut谱划分

正文：[03-ratio-cut.tex](../../../tex/03-graphs/05-matrices-and-spectra/05-spectral-partition/03-ratio-cut.tex)

本节从最小割（MinCut）易切出孤立末梢节点的退化解困境出发，引入以节点个数作为惩罚分母的RatioCut目标，通过四步推导将其松弛为组合拉普拉斯的Fiedler向量问题并给出阈值扫描实现。

#### 18.3.1 RatioCut的谱松弛

1. 定义RatioCut目标$c(A,B)\bigl(\frac{1}{|A|}+\frac{1}{|B|}\bigr)$，分四步完成谱松弛推导：（1）构造两值指示向量$f_i=\sqrt{|B|/|A|}$（$i\in A$）与$-\sqrt{|A|/|B|}$（$i\in B$）；（2）代入二次型分子得$\bm f^\top\bm L\bm f=n\operatorname{RatioCut}(A,B)$；（3）验证零和正交条件$\bm f\perp\bm 1$与分母$\bm f^\top\bm f=n$；（4）放宽两值限制得到Rayleigh商最小值$\lambda_2(\bm L)$及最优解Fiedler向量$\bm v_2$。

#### 18.3.2 算法实现

1. 阐述谱嵌入与离散化还原的主要思路，给出“构建未归一化拉普拉斯矩阵—求解特征向量—构建特征矩阵—离散化还原（阈值扫描）”四步流程及算法`alg:graph-ratiocut-sweep`，并在四点路径上核对。

#### 18.3.3 算法分析

1. 给出松弛下界与扫描上界构成的夹逼区间$\lambda_2(\bm L)\leq\operatorname{OPT}_R\leq\operatorname{RatioCut}(A_R,B_R)$与$O(n\log n+m)$扫描复杂度，并指出度数不均时缺乏独立于最大度的Cheeger保证。

### 18.4 NCut谱划分

正文：[04-normalized-cut.tex](../../../tex/03-graphs/05-matrices-and-spectra/05-spectral-partition/04-normalized-cut.tex)

要求正度顶点集非空，只扫描两侧体积均正的候选；孤立点在扫描后分配。仅有孤立点时不存在本节定义下的合法切分。

本节针对“节点个数多不代表内部联系紧密”的问题，将分母替换为子图度数之和（体积$\operatorname{vol}(A)$）以衡量跨割连接占两侧总连接量的比例，说明体积不等同于内部边权或内部密度，导出NCut谱划分算法及Cheeger目标值上界。

#### 18.4.1 NCut的谱松弛

1. 定义NCut目标$c(A,B)\bigl(\frac{1}{\operatorname{vol}(A)}+\frac{1}{\operatorname{vol}(B)}\bigr)$，分四步推导其谱松弛：构造按体积加权的两值向量$f_i=\sqrt{\operatorname{vol}(B)/\operatorname{vol}(A)}$（$i\in A$）与$-\sqrt{\operatorname{vol}(A)/\operatorname{vol}(B)}$（$i\in B$），算出分子$\bm f^\top\bm L\bm f=\operatorname{vol}(V)\operatorname{NCut}(A,B)$、度加权正交条件$\bm f^\top\bm D\bm 1=0$与分母$\bm f^\top\bm D\bm f=\operatorname{vol}(V)$，再经$\bm z=\bm D^{1/2}\bm f$变换松弛为对称归一化拉普拉斯特征值$\mu_2(\mathcal L)$。

#### 18.4.2 算法实现

1. 给出“构建归一化拉普拉斯矩阵$\mathcal L$—求解特征向量$\bm z_2$—坐标逆缩放$\bm f=\bm D^{-1/2}\bm z_2$与构建特征矩阵—离散化还原”四步流程及算法`alg:graph-ncut-sweep`，并通过图示阐明为什么必须按还原后的坐标$f_i$排序。

#### 18.4.3 算法分析

1. 从目标函数等价性（$\phi(S)\leq\operatorname{NCut}(S,\bar S)\leq 2\phi(S)$）、松弛算子$\mu_2(\mathcal L)$一致性与扫描向量$\bm f=\bm D^{-1/2}\bm z_2$一致性三个层面，由Cheeger不等式导出$\mu_2\leq\operatorname{OPT}_N\leq\operatorname{NCut}(S_N)\leq 2\sqrt{2\mu_2}\leq 2\sqrt{2\operatorname{OPT}_N}$的平方根目标值保证，说明对应近似因子依赖最优值；排序扫描成本不包含特征向量求解。

### 18.5 谱划分方法的比较

正文：[05-comparison.tex](../../../tex/03-graphs/05-matrices-and-spectra/05-spectral-partition/05-comparison.tex)

1. 列表对比RatioCut与NCut在均衡目标、两值指示向量、松弛算子与Cheeger保证上的对应关系，通过边权为$1,2,1$的加权路径算例展示RatioCut偏好低度端点割（$4/3$）而NCut偏好体积均衡中间割（$1$）的分歧，补列内部单点割以穷尽五类二分，说明正则图目标成比例，但一致的算法输出还需相同特征方向和并列规则；两类目标均不强制等分。

### 18.6 本章小结

正文：[06-summary.tex](../../../tex/03-graphs/05-matrices-and-spectra/05-spectral-partition/06-summary.tex)

1. 回顾从连通度几何图像、代数连通度与Fiedler向量、Cheeger不等式到RatioCut与NCut谱划分算法的完整主线，引向下一章图的谱稀疏化。

## 第19章 图的稀疏化

正文：[06-graph-sparsification.tex](../../../tex/03-graphs/05-matrices-and-spectra/06-graph-sparsification.tex)

章职责与主线：本章研究如何用原图的一部分边构造同一顶点集上的稀疏重加权近似图，依次建立割近似与谱近似的定义及性质，利用第17章的有效电阻与生成树理论给出按有效电阻抽样的稀疏图构造算法与矩阵Chernoff界保证，最后将稀疏图作为预条件子加速原图拉普拉斯方程求解。

### 19.1 割近似与谱近似

正文：[01-approximation.tex](../../../tex/03-graphs/05-matrices-and-spectra/06-graph-sparsification/01-approximation.tex)

本节对比保持离散二分割权的割近似与保持全体实向量二次型能量的谱近似，阐明为何必须使用谱近似，并分三小节证明谱近似保持特征值、有效电阻与方程解的性质。

#### 19.1.1 割近似

1. 定义所有子集割的$1\pm\varepsilon$相对误差条件（定义`def:graph-cut-approximation`），并证明割近似保持最小割、RatioCut、集合体积、导通率与NCut（定理`prop:graph-cut-approximation-preservation`，采用乘法不等式兼容零割权）。

#### 19.1.2 谱近似的定义

1. 从连续实值向量应用场景、边端差值平方放大效应以及算子预条件需求三个层面阐明为何使用谱近似而非割近似，给出谱近似$(1-\varepsilon)\bm L_G\preceq\bm L_H\preceq(1+\varepsilon)\bm L_G$的定义`def:graph-spectral-approximation`，并通过三顶点反例`ex:graph-cut-not-spectral`证明$\varepsilon$割近似不必是相同误差参数下的$\varepsilon$谱近似。

#### 19.1.3 谱近似的性质

本小节分别证明谱近似在特征值、伪逆与有效电阻、以及拉普拉斯线性方程组解上的三项保持性质。

##### 19.1.3.1 特征值保持

1. 利用Courant–Fischer极小极大定理证明定理`thm:graph-spectral-approximation-consequences`：谱近似保持全部拉普拉斯特征值的$1\pm\varepsilon$相对误差。

##### 19.1.3.2 伪逆与有效电阻保持

1. 在$\bm 1^\perp$上通过原图能量坐标变换$\bm A=\bm L_G^{-1/2}\bm L_H\bm L_G^{-1/2}$与特征值取倒数，证明定理`thm:graph-sparsification-resistance`：伪逆满足$\frac{1}{1+\varepsilon}\bm L_G^\dagger\preceq\bm L_H^\dagger\preceq\frac{1}{1-\varepsilon}\bm L_G^\dagger$，且全图任意两点有效电阻满足$\frac{R_G(u,v)}{1+\varepsilon}\leq R_H(u,v)\leq\frac{R_G(u,v)}{1-\varepsilon}$。

##### 19.1.3.3 拉普拉斯方程解保持

1. 证明定理`thm:graph-sparsification-solution`：对任意相容右端$\bm b\in\bm 1^\perp$，两图零均值解在原图能量范数下满足$\lVert\bm x_H-\bm x_G\rVert_{\bm L_G}\leq\frac{\varepsilon}{1-\varepsilon}\lVert\bm x_G\rVert_{\bm L_G}$。

### 19.2 稀疏图的构造

正文：[03-resistance-sampling.tex](../../../tex/03-graphs/05-matrices-and-spectra/06-graph-sparsification/03-resistance-sampling.tex)

一般失败概率$\delta$下，抽样次数为$O(n\log(n/\delta)/\varepsilon^2)$。近似电阻估计的失败概率另行合并；边数界不等同于构造时间界，后者还包括电阻估计与拉普拉斯求解。

本节直接利用第17.4.5小节的生成树包含概率与Foster定理，给出按有效电阻抽样构造谱稀疏化子图的算法，并用矩阵Chernoff界证明$O(n\log n/\varepsilon^2)$条边的谱近似保证。

#### 19.2.1 抽样分布的选择

1. 用杠铃图唯一桥边说明均匀抽样的风险，调用生成树包含概率$\mathbb P(e\in T)=c_e R_e$与Foster定理$\sum_{e\in E}c_e R_e=n-1$定义抽样分布$p_e=c_e R_e/(n-1)$及重加权规则$c_e/(qp_e)$，并证明无偏性$\mathbb E[\bm L_H]=\bm L_G$与单次算子范数界$\lVert\bm X_j\rVert_2=(n-1)/q$（引理`lem:graph-resistance-sampling-moments`）。

#### 19.2.2 算法实现

1. 给出按有效电阻独立有放回抽样的算法`alg:graph-resistance-sampling`，并在四点五边图上演示$q=6$次抽取的区间定位与权重累加过程（例`ex:graph-resistance-sampling`）。

#### 19.2.3 算法分析

1. 引入矩阵Chernoff界（定理`thm:graph-matrix-chernoff`），证明抽取$q=O(n\log n/\varepsilon^2)$次边即可以高概率输出$\varepsilon$谱近似图（定理`thm:graph-resistance-sparsification`），并说明近似有效电阻的误差补偿。

### 19.3 稀疏图作为预条件

正文：[04-sparse-preconditioning.tex](../../../tex/03-graphs/05-matrices-and-spectra/06-graph-sparsification/04-sparse-preconditioning.tex)

1. 以$\varepsilon$谱近似图的拉普拉斯矩阵$\bm M=\bm L_H$作为预条件子，证明预条件算子条件数满足$\kappa_2(\bm A)\leq\frac{1+\varepsilon}{1-\varepsilon}$及预条件共轭梯度法的收敛率（定理`prop:graph-sparse-preconditioner`），并在四点五边图上用四元环预条件演示一轮迭代。

### 19.4 本章小结

正文：[05-summary.tex](../../../tex/03-graphs/05-matrices-and-spectra/06-graph-sparsification/05-summary.tex)

1. 总结割近似与谱近似的层次关系、基于有效电阻抽样的稀疏图构造原理以及稀疏预条件求解的分工与加速机制。

## 第20章 图上的行走

正文：[07-graph-walks.tex](../../../tex/03-graphs/05-matrices-and-spectra/07-graph-walks.tex)

章职责与主线：本章研究图上随机游走的位置分布演化、首达与遍历等待时间以及有向图PageRank与局部探索，将转移矩阵幂、归一化拉普拉斯谱、Cheeger导通率、接地拉普拉斯系统与有效电阻融会贯通。

### 20.1 随机游走

正文：[01-random-walk.tex](../../../tex/03-graphs/05-matrices-and-spectra/07-graph-walks/01-random-walk.tex)

本节建立一步转移规则与转移矩阵$\bm P=\bm D^{-1}\bm W$的多步分布公式，并利用详细平衡与拉普拉斯零空间证明无向连通图平稳分布的存在唯一性。

#### 20.1.1 转移规则

1. 从四点路径算例引入按邻边权重比例选择下一步的随机游走规则（定义`def:graph-random-walk`），写出单条轨迹的概率乘法公式`eq:graph-walk-path-probability`。

#### 20.1.2 多步分布

1. 定义行随机转移矩阵$\bm P=\bm D^{-1}\bm W$，导出多步分布递推式$\bm\nu^{(t)}=\bm\nu^{(0)}\bm P^t$，并在四点路径上演示前三步分布演化。

#### 20.1.3 平稳分布

1. 定义平稳分布$\bm\pi\bm P=\bm\pi$（定义`def:graph-walk-stationary`），验证度数比例分布$\pi_i=d_i/\operatorname{vol}(V)$满足逐边详细平衡，并利用连通图组合拉普拉斯零空间证明其唯一性（定理`thm:graph-walk-stationary-uniqueness`）。

### 20.2 收敛速度

正文：[03-convergence-rate.tex](../../../tex/03-graphs/05-matrices-and-spectra/07-graph-walks/03-convergence-rate.tex)

本节通过度平方根相似变换将转移矩阵对称化，导出多步分布收敛的充要条件、总变差指数衰减界与惰性游走谱隙，并对比典型图族的混合速度。

#### 20.2.1 转移矩阵的对称化

1. 利用相似变换$\bm S=\bm D^{1/2}\bm P\bm D^{-1/2}=\bm I-\mathcal L$建立转移矩阵特征值$\theta_i=1-\mu_i$与对称归一化拉普拉斯特征值$\mu_i$的一一对应。

#### 20.2.2 收敛条件

1. 在$\bm S$的标准正交特征基下展开分布偏差（式`eq:graph-walk-spectral-evolution`），证明无向连通图随机游走从任意初态收敛于$\bm\pi$当且仅当图不是二部图（定理`thm:graph-walk-convergence`）。

#### 20.2.3 收敛速度

1. 证明$\pi^{-1}$-范数与总变差距离的几何衰减界（定理`prop:graph-walk-tv-bound`），明确混合时间的最坏初态定义、误差范围、向上取整及对最小平稳概率的依赖，并引入惰性游走$\bm Q=(\bm I+\bm P)/2$消除负特征值振荡，使收敛率由谱隙$\gamma=\mu_2/2$决定。

#### 20.2.4 典型图的收敛速度

1. 结合Cheeger不等式导出$\phi_*^2/4\leq\gamma\leq\phi_*$，在固定总变差误差下，对比完全图（$\Theta(1)$）、超立方体（$\Theta(d\log d)$）、路径与环（$\Theta(n^2)$）以及杠铃图（细腰瓶颈拖慢至$\Omega(n^2)$）的混合速度。

### 20.3 首达时间

正文：[04-hitting-time.tex](../../../tex/03-graphs/05-matrices-and-spectra/07-graph-walks/04-hitting-time.tex)

本节研究随机游走首次命中目标顶点的平均步数，先给出六类典型图的首达时间，再建立接地拉普拉斯方程、有效电阻往返时间公式以及简单单位权图上的三次方上界。

#### 20.3.1 典型图的首达时间

1. 推导并对比六类典型图的首达期望：完全图$K_n$（$n-1$）、星图$K_{1,n-1}$（$h_{u,c}=1,h_{c,v}=2n-3$）、路径$P_n$（端点出发为$(n-1)^2$、最坏起点为$\Theta(n^2)$）、环$C_n$（$k(n-k)$）、超立方体$Q_d$（异点首达为$\Theta(n)$）以及棒棒糖图（$\Theta(n^3)$）。

#### 20.3.2 首达时间期望的方程

1. 证明首达期望有限且满足一阶递推与接地拉普拉斯线性系统$\bm L_{-j,-j}\bm h_{-j,j}=\bm d_{-j}$（定理`prop:graph-walk-hitting-system`），并在四点路径上核对。

#### 20.3.3 往返时间

1. 证明单向首达期望的拉普拉斯伪逆表示与往返时间恒等式$h_{i,j}+h_{j,i}=\operatorname{vol}(V)R_{i,j}$（定理`thm:graph-walk-commute-resistance`），并据此复核星图、环与棒棒糖图的首达时间。

#### 20.3.4 首达时间的上界

1. 在连通简单单位权图上，利用有效电阻的三角不等式与单调性证明相邻点往返界$h_{u,v}+h_{v,u}\leq 2m$与任意点对的通用上界$h_{i,j}<2m\,\operatorname{dist}(i,j)\leq 2m(n-1)<n^3$（定理`thm:graph-walk-hitting-upper-bound`）。

### 20.4 遍历时间

正文：[05-cover-time.tex](../../../tex/03-graphs/05-matrices-and-spectra/07-graph-walks/05-cover-time.tex)

本节研究随机游走访问遍全图所有顶点的期望步数，依次介绍典型图的遍历时间、连接遍历时间与首达时间的Matthews定理以及生成树有效电阻上界。

#### 20.4.1 典型图的遍历时间

1. 推导完全图$K_n$（优惠券收集$(n-1)H_{n-1}\sim n\ln n$）、星图（$\sim 2n\ln n$）、路径$P_n$（端点出发为$(n-1)^2$、最坏起点为$\Theta(n^2)$）、环$C_n$（$n(n-1)/2$）与棒棒糖图（$\Theta(n^3)$）的遍历时间。

#### 20.4.2 遍历时间与首达时间：Matthews定理

1. 利用独立随机排列和强Markov性质证明Matthews定理，区分未访问事件的无条件概率$1/k$与停时历史下带事件指示函数的条件期望`thm:graph-walk-matthews`：遍历时间满足上界$C\leq h_{\max}H_{n-1}$与子集下界$C\geq h_{\min}(K)H_{|K|-1}$，并在完全图与星图上验证紧性。

#### 20.4.3 遍历时间的生成树界

1. 利用生成树深度优先巡游与往返时间公式证明定理`thm:graph-walk-cover-tree-bound`：$C_u\leq\operatorname{vol}(V)\sum_{e\in T}R_e\leq\operatorname{vol}(V)\sum_{e\in T}1/w_e$；简单单位权图进一步有$C\leq2m(n-1)<n^3$，路径图由此去掉对数因子。

### 20.5 PageRank

正文：[06-pagerank.tex](../../../tex/03-graphs/05-matrices-and-spectra/07-graph-walks/06-pagerank.tex)

区分重启前普通跳转次数的期望$\alpha/(1-\alpha)$与包含重启一步的间隔期望$1/(1-\alpha)$；全矩阵谱半径仍为$1$，非平稳特征值模长至多为$\alpha$，实际绝对谱隙至少为$1-\alpha$。

本节阐述PageRank处理有向图死胡同、闭合类与周期性的核心思想，给出稀疏幂法实现，并证明平稳分布存在唯一性及第二大特征值模长界$|\lambda_2(\bm G)|\leq\alpha$。

#### 20.5.1 背景与核心思想

1. 剖析有向图随机游走的“死胡同（悬挂节点漏失质量）”与“闭合类与周期性”问题，介绍死胡同修补$\widetilde{\bm P}$与引入阻尼系数$\alpha\in(0,1)$全局随机跳转构造Google矩阵$\bm G=\alpha\widetilde{\bm P}+(1-\alpha)\bm 1\bm s$的思想，给出PageRank定义`def:graph-pagerank`。

#### 20.5.2 算法实现

1. 将每轮幂法拆解为沿有向边稀疏传播、死胡同质量汇总补偿与全局随机跳转三步$O(n+m)$操作（算法`alg:graph-pagerank-iteration`），并在四顶点有向图上逐步核对。

#### 20.5.3 算法分析

1. 证明PageRank平稳分布存在唯一；在跳转分布各分量为正时，得$\bm p\geq(1-\alpha)\bm s>\bm 0$（定理`thm:graph-pagerank-uniqueness`），证明Google矩阵的第二大特征值模长恒不超过阻尼系数$|\lambda_2(\bm G)|\leq\alpha$（定理`thm:pagerank-second-eigenvalue`），并导出几何收敛界$2\alpha^t$与后验残差停止准则。

### 20.6 个性化PageRank

正文：[07-personalized-pagerank.tex](../../../tex/03-graphs/05-matrices-and-spectra/07-graph-walks/07-personalized-pagerank.tex)

假定邻接表能常数时间读取度数且全图体积已给定，局部扫描的割权和体积须按原图计算，不能删去通向支撑集外的边；排除全图前缀。逐点逼近不自动给出低导通率保证，原文的精确PageRank扫描与PageRank-Nibble定理还要求种子、精度、体积尺度和目标导通率满足相应条件。

本节介绍将重启分布集中于种子节点的个性化PageRank，阐述局部推送（Local Push）算法的核心思想、实现步骤、依赖$\alpha,\varepsilon$和种子支撑的局部工作量界及局部谱划分分析。

#### 20.6.1 背景与主要思想

1. 说明从全局权威转向种子局部亲密度与超大图局部社区发现的动机，阐述维护“已确认分数$\bm p$+待处理余量$\bm r$”守恒不变量$\mathcal R(\bm s)=\bm p+\mathcal R(\bm r)$并仅对$r_i/d_i>\varepsilon$活跃节点执行局部推送的思想。

#### 20.6.2 算法实现

1. 给出个性化PageRank局部推送算法`alg:graph-personalized-pagerank-push`，并在四点路径上逐步演示三次推送过程。

#### 20.6.3 算法分析

1. 证明局部推送算法的推送工作量为$O(\frac{1}{\alpha\varepsilon})$，另计种子支撑初始化；参数随规模变化时不自动保证亚线性，并证明逐点误差保证$0\leq\mathcal R(\bm s)_i-p_i\leq\varepsilon d_i$与总质量守恒（定理`thm:graph-pagerank-push-guarantee`），说明按$p_i/d_i$阈值扫描实现局部社区切分的原理。

2. 按扫描方法、杠铃图算例、一般质量保证的条件依次分段说明，区分精确PageRank扫描与PageRank-Nibble的结论。

### 20.7 本章小结

正文：[08-summary.tex](../../../tex/03-graphs/05-matrices-and-spectra/07-graph-walks/08-summary.tex)

1. 总结随机游走的位置分布与谱隙收敛率、首达与遍历时间的拉普拉斯及有效电阻刻画，以及PageRank与个性化局部推送的核心机制。
