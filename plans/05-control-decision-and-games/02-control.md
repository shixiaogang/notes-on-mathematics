# 卷5《数学准备：控制、决策与博弈》：控制大纲

正文入口：[part.tex](../../tex/05-control-decision-and-games/02-control/part.tex)。以下按实际正文顺序保留内容提要；目标细化方案另见数学基础五卷目标目录。

阅读指引：从根据观测选择行动的反馈问题进入，概述可达、可控与可观、闭环稳定、调节跟踪及约束安全；说明反馈改变演化规律，并区分可达性、稳定性和安全。

## 第2章 策略的实现与轨迹控制

正文：[02-policy-realization-and-control.tex](../../tex/05-control-decision-and-games/02-control/02-policy-realization-and-control.tex)。

### 2.1 策略的实现与可达轨迹

主要内容：在行动与观测受限的系统中比较开环和反馈策略，建立目标可达、可控与状态可区分的结构条件。

论证与表述逻辑：

1. 开环策略与反馈策略：考虑离散时间线性时不变系统$\begin{aligned} \boldsymbol{x}_{t+1}&=\boldsymbol{A}\boldsymbol{x}_t+\boldsymbol{B}\boldsymbol{u}_t,\\ \boldsymbol{y}_t&=\boldsymbol{C}\boldsymbol{x}_t, \end{aligned}$其中$\boldsymbol{x}_t\in\mathbb R^n$、$\boldsymbol{u}_t\in\mathbb R^m$和$\boldsymbol{y}_t\in\mathbb R^p$分别是状态、输入和输出；$\boldsymbol A,\boldsymbol B,\boldsymbol C$的维度依次为$n\times n,n\times m,p\times n$。
2. 目标状态的可达与可控：要判断一个终态能否由动作实现，可以把前$N$次输入对终态的贡献集中写出。
3. 观测条件下的状态可区分性：同一动作序列可能从不同初态产生不同读数。要检查读数是否足以区分初态，先从观测中扣除已知动作的贡献，留下只由初态产生的自由响应。

#### 2.1.1 开环策略与反馈策略

主要内容：考虑离散时间线性时不变系统$\begin{aligned} \boldsymbol{x}_{t+1}&=\boldsymbol{A}\boldsymbol{x}_t+\boldsymbol{B}\boldsymbol{u}_t,\\ \boldsymbol{y}_t&=\boldsymbol{C}\boldsymbol{x}_t, \end{aligned}$其中$\boldsymbol{x}_t\in\mathbb R^n$、$\boldsymbol{u}_t\in\mathbb R^m$和$\boldsymbol{y}_t\in\mathbb R^p$分别是状态、输入和输出；$\boldsymbol A,\boldsymbol B,\boldsymbol C$的维度依次为$n\times n,n\times m,p\times n$。

论证与表述逻辑：

1. 定义（开环控制与反馈控制）：若输入序列$\boldsymbol u_0,\boldsymbol u_1,\ldots$事先指定，不根据运行中实际出现的状态修正，称为开环控制（open-loop control）。状态可直接取得时，规则$\boldsymbol u_t=\kappa_t(\boldsymbol x_t)$称为状态反馈（state feedback）。仅有观测和已执行动作可用时，规则$\boldsymbol u_t=\mu_t(\boldsymbol y_0,\ldots,\boldsymbol y_t;\boldsymbol u_0,\ldots,\boldsymbol u_{t-1})$称为输出反馈（output feedback），初始控制历史按空序列处理。随机系统中，动作必须对这些允许信息可测，不能使用尚未产生的噪声。
2. 在温度例中，始终取$u_t=0.4$是一条开环策略；若直接测得状态，则可以根据$x_t-2$修正输入。若只有带噪声的$y_t$，把$x_t$写进控制公式并不会使真实状态变得可用，必须说明怎样从读数构造估计。
3. 把反馈代回状态方程后，需要确认给定初态与外部输入后，闭环轨迹存在、唯一，并覆盖任务所需时域；随机情形还要固定噪声实现。

#### 2.1.2 目标状态的可达与可控

主要内容：要判断一个终态能否由动作实现，可以把前$N$次输入对终态的贡献集中写出。

论证与表述逻辑：

1. 区分任意初态到零与任意初态到任意终态：$\boldsymbol A$可逆是零可控推出可控的充分条件，$A=B=0$说明一般逆推失败，$A=0,B=1$说明可逆性并非具体系统可控的必要条件。
2. 命题（Popov--Belevitch--Hautus（PBH）可控性判据）：矩阵对$(\boldsymbol A,\boldsymbol B)$可控，当且仅当对每个复特征值$\lambda\in\sigma(\boldsymbol A)$都有$\operatorname{rank}[\lambda\boldsymbol I-\boldsymbol A\ \boldsymbol B]=n$；等价地，不存在非零左特征向量$\boldsymbol q^\ast$同时满足$\boldsymbol q^\ast\boldsymbol A=\lambda\boldsymbol q^\ast$和$\boldsymbol q^\ast\boldsymbol B=\boldsymbol0$。
3. 推导：若存在这样的向量，则$\boldsymbol q^\ast\boldsymbol A^k\boldsymbol B=\lambda^k\boldsymbol q^\ast\boldsymbol B=\boldsymbol0$对所有$k\geq0$成立，所以可控性矩阵不可能满行秩。反之，其列空间$\boldsymbol R_{\mathrm{reach}}$若不满维，便是一个真$\boldsymbol A$不变子空间。正交补$\boldsymbol R_{\mathrm{reach}}^{\perp}$在$\boldsymbol A^\ast$下不变。
4. 终点可控仍不保证任意指定的中间状态都能实现。给定整条参考$\boldsymbol r_t$，离散系统要求每一步$\boldsymbol r_{t+1}-\boldsymbol A\boldsymbol r_t\in\operatorname{col}(\boldsymbol B)$，并且解出的输入位于允许集合；连续系统则要求参考绝对连续且$\dot{\boldsymbol r}_t-\boldsymbol A\boldsymbol r_t=\boldsymbol B\boldsymbol u_t^r$几乎处处成立。

#### 2.1.3 观测条件下的状态可区分性

主要内容：同一动作序列可能从不同初态产生不同读数。要检查读数是否足以区分初态，先从观测中扣除已知动作的贡献，留下只由初态产生的自由响应。

论证与表述逻辑：

1. 定义（可观测性）：若同一已知输入下的输出序列能够区分任意两个不同初态，称$(\boldsymbol C,\boldsymbol A)$可观测（observable）。对上述线性时不变系统，这等价于$\mathcal O(\boldsymbol C,\boldsymbol A)$满列秩。
2. 反之，若秩不足，存在$\boldsymbol v\neq\boldsymbol0$满足$\mathcal O\boldsymbol v=\boldsymbol0$，初态$\boldsymbol x_0$与$\boldsymbol x_0+\boldsymbol v$的前$n$次输出便相同。
3. 新增$\boldsymbol C=(1,1)$的两组二维系统读数图：不同衰减模态使相同首读数随后分开，并由两行观测矩阵的行列式恢复初态；相同模态只能观察坐标和，增加观测时长仍不能补出遗漏方向。
4. 温度模型的$C=1$使无噪声当前读数就能区分状态。有噪声时，同一个读数可能来自多个状态，结构可观测性并不提供单次误差上界。

### 2.2 策略的轨迹收敛与稳定

主要内容：从可稳定、可检测条件进入状态反馈、二次成本下的反馈设计与输出反馈，检查闭环误差的长期行为。

论证与表述逻辑：

1. 不可控与不可观测模式的稳定条件：反馈$\boldsymbol u=-\boldsymbol K\boldsymbol x$把状态矩阵改为$\boldsymbol A-\boldsymbol B\boldsymbol K$。
2. 状态反馈下的闭环稳定：可稳定性保证某个增益能够稳定系统；实际设计仍要给出增益，并检验相应闭环。
3. 二次成本下的稳定化反馈：稳定增益通常不唯一，较快纠偏可能需要更大的动作。以二次型分别计量状态偏差与动作幅值，便能将增益选择写成成本最小化问题；所得反馈律仍是线性的。
4. 输出反馈下的估计与闭环稳定：反馈需要状态，但传感器可能只提供状态的一部分。可以先根据模型和已执行动作预测状态，再利用当前读数与预测读数的差纠正估计。

#### 2.2.1 不可控与不可观测模式的稳定条件

主要内容：反馈$\boldsymbol u=-\boldsymbol K\boldsymbol x$把状态矩阵改为$\boldsymbol A-\boldsymbol B\boldsymbol K$。观测增益使线性估计误差按$\boldsymbol A-\boldsymbol L\boldsymbol C$传播；因此可检测性检查是否存在使误差消退的校正，而不是要求全部初态均可恢复。

论证与表述逻辑：

1. 令$\boldsymbol R_{\mathrm{reach}}$为可控性矩阵的列空间，选取以其一组基为前若干列的可逆矩阵$\boldsymbol T$。
2. 定义（可检测性）：若存在$\boldsymbol L$使$\boldsymbol A-\boldsymbol L\boldsymbol C$稳定，称$(\boldsymbol C,\boldsymbol A)$可检测（detectable）。
3. $\boldsymbol C=(1,0)$看得见$1.2$模式，看不见但无需纠正$0.5$模式，所以不可观测却可检测。

#### 2.2.2 状态反馈下的闭环稳定

主要内容：可稳定性保证某个增益能够稳定系统；实际设计仍要给出增益，并检验相应闭环。取线性状态反馈后，动作与状态递推为$\boldsymbol u_t=-\boldsymbol K\boldsymbol x_t, \qquad \boldsymbol x_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol x_t$，负号只是增益约定。

论证与表述逻辑：

1. 非线性系统在不同状态处具有不同的变化方向，固定矩阵的谱一般不足以判断整个区域。可以改用一个随状态变化的标量$V$衡量偏离，再要求所选动作使它沿轨迹下降。
2. 定义（控制Lyapunov函数条件）：考虑$\dot{\boldsymbol x}_t=\boldsymbol f(\boldsymbol x_t)+\boldsymbol G(\boldsymbol x_t)\boldsymbol u_t$，目标为原点，输入属于$U$，并假设$\boldsymbol f,\boldsymbol G$在原点的某邻域内局部Lipschitz。若该邻域内的$C^1$函数$V$满足$V(\boldsymbol0)=0$、$V(\boldsymbol x)>0$（$\boldsymbol x\neq\boldsymbol0$），且有正定连续函数$W$使$\text{对每个 }\boldsymbol x\neq\boldsymbol0\text{，存在 }\boldsymbol u\in U\text{ 使} \quad\nabla V(\boldsymbol x)^\top(\boldsymbol f(\boldsymbol x)+\boldsymbol G(\boldsymbol x)\boldsymbol u) \leq-W(\boldsymbol x),$称$V$提供一个控制Lyapunov函数（control Lyapunov function, CLF）条件：每个非零状态至少应能选择一个使偏离量严格下降的动作。
3. 点态存在动作不等于已经构造出适定反馈。还须选出取值于$U$的局部Lipschitz反馈，使原点为平衡并保持严格下降；模型与反馈的规则性共同保证闭环右端$\boldsymbol f+\boldsymbol G\kappa$局部Lipschitz，补齐前章Lyapunov定理的条件后才得到局部渐近稳定。
4. 若进一步有$c_1\|\boldsymbol x\|_2^2\leq V\leq c_2\|\boldsymbol x\|_2^2$和$W\geq c_3\|\boldsymbol x\|_2^2$，便有$V_t\leq e^{-c_3t/c_2}V_0$；全局结论还需全域条件与解的延拓。三次系统的抵消算例展示下降反馈的构造，并以输入限幅说明结论的区域边界。

#### 2.2.3 二次成本下的稳定化反馈

主要内容：稳定增益通常不唯一，较快纠偏可能需要更大的动作。二次成本同时评价状态偏差与动作幅值，通过有限时域配方构造线性反馈，再讨论确定性无限时域下稳定化与成本最优如何联系。区分稳定性、衰减率、瞬态峰值和输入成本；温度模态$0.8-K$由$K=0.3$时的0.5变为$K=2$时的$-1.2$，说明增大增益可破坏稳定，再引出成本选择。新增同一初态下$K=0.3,1.6,2$的闭环解析轨迹，以模态绝对值和符号分别解释单调衰减、交替衰减及交替发散，不把增益大小视为稳定性指标。

论证与表述逻辑：

1. 在有限时域期望二次成本之前说明风险中性：确定成本10与等概率成本0或20打平。评价只看期望，并非否认波动；随后用终端价值反向配方得到Riccati递推，再说明无限时域稳定化所需条件。
2. 无限时域定理之前先用$\boldsymbol x^\top\boldsymbol Q\boldsymbol x=\|\boldsymbol Q^{1/2}\boldsymbol x\|_2^2$解释成本输出。成本可检测要求沿动态始终不被该输出辨认的模式自行衰减，不能把瞬时零成本方向等同于不可观测模式，也不能用传感器输出的可检测条件替换。
3. 命题（无限时域LQR的稳定化解）：在确定性、时不变、无折扣条件下，设$\boldsymbol Q\succeq\boldsymbol0$、$\boldsymbol R\succ\boldsymbol0$，$(\boldsymbol A,\boldsymbol B)$可稳定且$(\boldsymbol Q^{1/2},\boldsymbol A)$可检测。DARE存在唯一半正定稳定化解，相应反馈使闭环渐近稳定，并在所有允许控制序列中给出二次总成本的最优值$V(\boldsymbol x)=\boldsymbol x^\top\boldsymbol P\boldsymbol x$。
4. 推导：由零终端代价有限问题的价值矩阵单调性与稳定反馈提供的上界构造DARE解，再以闭环谱与成本可检测性证明稳定。对任意有限成本控制，先证明状态及终端项趋零，再对累加配方取极限，得到成本最优性与稳定化解唯一性。
5. $Q=0$的标量反例说明缺少成本可检测时，成本最优可能选择不稳定反馈；持续非零噪声下的无折扣总期望成本通常发散，不能直接沿用确定性定理。
6. 连续时间借用CARE稳定化解的标准存在性结论，并直接核验闭环谱；连续有限时域Riccati与价值最优性留给后章，不写成此处已经证明。

#### 2.2.4 输出反馈下的估计与闭环稳定

主要内容：反馈需要状态，但传感器可能只提供状态的一部分。可以先根据模型和已执行动作预测状态，再利用当前读数与预测读数的差纠正估计。随机部分区分预测协方差与更新后协方差，在独立零均值噪声及有限初态二阶矩的设定下分析线性滤波误差；联合高斯时再把估计解释为精确条件均值。先以无噪声、不完全观测推导Luenberger谱分离；有噪声时显式写$y=Cx+v$。残差是观测空间向量，校正由增益$L$映回状态空间，正残差上调只用于正测量与正增益的标量例。

论证与表述逻辑：

1. 确定性Luenberger观测器合并模型预测与读数残差校正，负责更新下一时刻的估计；控制器单独按尚未使用当前读数的估计选择当前动作。联合矩阵的上三角分块给出谱分离，说明状态反馈与估计误差可以分别作稳定设计。
2. 命题（稳态预测滤波的充分条件）：若$(\boldsymbol C,\boldsymbol A)$可检测、$(\boldsymbol A,\boldsymbol\Sigma_{\mathrm w}^{1/2})$可稳定，且$\boldsymbol\Sigma_{\mathrm v}\succ\boldsymbol0$，预测协方差方程有唯一半正定稳定化解。从任意有限$\boldsymbol\Pi_0\succeq\boldsymbol0$出发的递推收敛到$\boldsymbol\Pi$，稳态$\boldsymbol L=\boldsymbol A\boldsymbol M$使$\boldsymbol A-\boldsymbol L\boldsymbol C$稳定。
3. 推导：对偶代换给出稳态解的存在、唯一与稳定性；固定增益配方给出$\Phi(\boldsymbol X)\preceq\Psi_{\boldsymbol L}(\boldsymbol X)$。在$\boldsymbol X\succeq\boldsymbol Y$时选取在$\boldsymbol X$处取等号的增益，依次用固定增益保序与任意增益上界，展开$\Phi(\boldsymbol X)\succeq\Psi_{\boldsymbol L_{\boldsymbol X}}(\boldsymbol Y)\succeq\Phi(\boldsymbol Y)$，再以零初值和稳态增益两端夹逼一般初始协方差。
4. 转用当前观测更新后的$\widehat{\boldsymbol x}_{t|t}$控制时，先写残差校正式与更新误差，明确时序改为先用当前读数更新、再确定动作。稳态联合矩阵仍可分块检查；持续噪声下的二阶矩有界与协方差收敛不能解释为路径趋零，也不能仅凭谱分离推出成本最优。

### 2.3 策略的调节与跟踪

主要内容：将固定设定值与运动参考转成误差系统，先检查参考可实现性，再讨论反馈和扰动下的调节跟踪。

论证与表述逻辑：

1. 先求出维持目标状态或参考轨迹所需的输入，避免误差方程保留未处理的漂移。
2. 随后用闭环误差分析分别讨论固定调节与运动跟踪，并检查持续扰动和模型误差。

#### 2.3.1 固定目标下的轨迹调节

主要内容：先求维持固定设定值的平衡状态与输入，再设计误差反馈，并检查持续扰动下的调节。

论证与表述逻辑：

1. 确认目标可实现后，以实际状态减去目标建立误差系统，避免漏掉维持目标的前馈输入。
2. 利用闭环稳定讨论偏差消退，再分析持续扰动和补偿机制对稳态误差的影响。

##### 2.3.1.1 目标平衡与可行输入

主要内容：设定值（setpoint）是希望状态或输出最终保持的常数。调节（regulation）要求偏离该常数的误差趋于零；它不只要求在某一时刻经过目标。

论证与表述逻辑：

1. 定义（目标平衡与调节误差）：对$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t+\boldsymbol B\boldsymbol u_t$，若状态设定值$\boldsymbol r$与常值输入$\boldsymbol u^r$满足$(\boldsymbol I-\boldsymbol A)\boldsymbol r=\boldsymbol B\boldsymbol u^r$，则称$(\boldsymbol r,\boldsymbol u^r)$构成目标平衡。状态调节误差为$\boldsymbol e_t=\boldsymbol x_t-\boldsymbol r$。若只指定输出设定值$\boldsymbol q$，还需寻找平衡状态$\boldsymbol r$使$\boldsymbol C\boldsymbol r=\boldsymbol q$，输出误差为$\boldsymbol e_t^y=\boldsymbol C\boldsymbol x_t-\boldsymbol q$。有输入、状态限制时，目标平衡还须满足$\boldsymbol u^r\in U,\boldsymbol r\in S$。
2. 对只指定输出的任务，可解联立方程$\begin{bmatrix}\boldsymbol I-\boldsymbol A&-\boldsymbol B\\\boldsymbol C&\boldsymbol0\end{bmatrix} \begin{bmatrix}\boldsymbol r\\\boldsymbol u^r\end{bmatrix} =\begin{bmatrix}\boldsymbol0\\\boldsymbol q\end{bmatrix}$。方程可能无解或有多个解；输出达到设定值也不自动要求所有内部状态相同。
3. 示例（非零温度需要维持输入）：在无噪声温度模型中，设定值$r=2$要求$2=0.8\times2+u^r$，所以$u^r=0.4$。若直接使用$u_t=-0.3(x_t-2)$，在$x_t=2$处输入变成零，下一步温差便降为$1.6$，因而$2$不是闭环平衡。

##### 2.3.1.2 基于误差反馈的轨迹调节

主要内容：目标平衡方程给出了在目标处仍需持续施加的输入。在这个输入上叠加误差反馈，才使控制器在目标处停止纠偏而继续维持平衡：$\boldsymbol u_t=\boldsymbol u^r-\boldsymbol K(\boldsymbol x_t-\boldsymbol r), \qquad \boldsymbol e_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol e_t$，第二式由原动态减去平衡方程得到。

论证与表述逻辑：

1. 温度反馈的完整计算为$u_t=0.4-0.3(x_t-2), \qquad e_{t+1}=0.5e_t,\quad e_t=0.5^t(x_0-2)$。从$x_0=0$出发，状态依次为$0,1,1.5,1.75,\ldots$，输入依次为$1,0.7,0.55,0.475,\ldots$。
2. 若改用估计状态$\widehat{\boldsymbol x}_t$，令$\boldsymbol e_t^{\mathrm o}=\boldsymbol x_t-\widehat{\boldsymbol x}_t$，则调节误差成为$\boldsymbol e_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol e_t+\boldsymbol B\boldsymbol K\boldsymbol e_t^{\mathrm o}$。

##### 2.3.1.3 持续扰动下的轨迹调节

主要内容：持续扰动在名义误差系统中形成受迫项。先由误差方程区分常值偏差、有界时变扰动与随机噪声，再通过累积输出误差的积分状态讨论常值偏差补偿及其可实现条件。

论证与表述逻辑：

1. 积分调节累积的是指定输出误差$\boldsymbol C\boldsymbol e_t$。增广闭环稳定且扰动为常值时，积分方程强制平衡输出误差为零，不要求全部状态误差为零，也不保证任意时变扰动下零误差。
2. 积分器自身带有特征值$1$，不能不经核验就加到控制器上。设计增益前应检查增广对$\left( \begin{bmatrix}\boldsymbol A&\boldsymbol0\\\boldsymbol C&\boldsymbol I\end{bmatrix}, \begin{bmatrix}\boldsymbol B\\\boldsymbol0\end{bmatrix}\right)$可稳定。
3. 输入饱和后，真实误差不再服从上述线性增广方程，积分状态却可能继续累积，造成解除饱和后的大幅动作。限制或回退积分累积是常见的抗积分饱和处理，但处理后的闭环仍需重新验证。

#### 2.3.2 运动参考下的轨迹跟踪

主要内容：先检查参考运动是否符合系统动力学，再结合前馈与反馈控制跟踪误差。

论证与表述逻辑：

1. 给定参考轨迹及其变化，求出可实现它的参考输入。
2. 把实际与参考之差写成误差动态，再检查扰动与模型偏差下能够维持何种跟踪精度。

##### 2.3.2.1 参考轨迹与可实现条件

主要内容：跟踪（tracking）以随时间变化的状态$\boldsymbol r_t$或输出$\boldsymbol q_t$为目标，要求$\boldsymbol x_t-\boldsymbol r_t$或$\boldsymbol C\boldsymbol x_t-\boldsymbol q_t$趋零或保持在规定范围内。

论证与表述逻辑：

1. 定义（可实现参考）：离散线性系统的参考状态、参考输入为$(\boldsymbol r_t,\boldsymbol u_t^r)$。若每一步满足$\boldsymbol r_{t+1}=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r, \qquad \boldsymbol q_t=\boldsymbol C\boldsymbol r_t,$且参考状态、输入满足所声明的约束，称它为可实现参考。精确从首时刻跟踪还要求$\boldsymbol x_0=\boldsymbol r_0$。连续时间则要求$\boldsymbol r_t$绝对连续，并有$\dot{\boldsymbol r}_t=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r$几乎处处成立。
2. 若只给输出曲线，需要先找与其一致的内部状态和输入；不同实现可能具有不同内部行为。有输入变化率、采样周期或执行器动态限制时，也必须把这些约束加入可实现性检查。
3. 温度参考的前馈输入由系统方程直接给出：$u_t^r=r_{t+1}-0.8r_t$。前馈（feedforward）是由已知目标运动与模型预先计算的动作，不靠当前误差产生。

##### 2.3.2.2 基于前馈与反馈的轨迹跟踪

主要内容：前馈按参考轨迹计算，没有使用实际偏差；从错误初态出发时，它不会额外纠偏。

论证与表述逻辑：

1. 温度例使用$u_t=r_{t+1}-0.8r_t-0.3(x_t-r_t)$，得到$e_{t+1}=0.5e_t$。
2. 误差趋零、误差有界与始终不超过某阈值仍有区别。无扰动时，$|e_t|=0.5^t|e_0|$既给出收敛，也给出从首步起的范围；一般多维稳定矩阵可能先放大误差，需要使用$M\rho^t$而不能省掉$M$。

##### 2.3.2.3 扰动与模型偏差下的轨迹跟踪

主要内容：将模型矩阵偏差、参考实现残差与外扰写入完整误差方程，再用Lyapunov加权范数建立名义收缩和受迫误差界，说明持续修正对跟踪结论的影响。

论证与表述逻辑：

1. 真实动态与参考规划常有偏差。设实际系统为$\boldsymbol x_{t+1}=(\boldsymbol A+\Delta\boldsymbol A)\boldsymbol x_t+ (\boldsymbol B+\Delta\boldsymbol B)\boldsymbol u_t+\boldsymbol d_t$，名义参考的实现残差为$\boldsymbol\eta_t=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r-\boldsymbol r_{t+1}$。
2. 对稳定的$\boldsymbol F$，先解$\boldsymbol P_{\mathrm F}-\boldsymbol F^\top\boldsymbol P_{\mathrm F}\boldsymbol F=\boldsymbol I$，由$\boldsymbol P_{\mathrm F}\succ\boldsymbol0$构造加权向量范数及其诱导矩阵范数，使$\|\boldsymbol F\|<1$。随后在同一范数下检查$\|\boldsymbol F\|\leq\rho<1$、$\|\Delta\boldsymbol A-\Delta\boldsymbol B\boldsymbol K\|\leq\varepsilon$及$q:=\rho+\varepsilon<1$，展开几何级数得到误差界；这不要求欧氏范数中的名义矩阵也一步收缩。
3. 在精确温度模型中，若$|d_t|\leq0.1$，则$|e_t|\leq0.5^t|e_0|+0.2(1-0.5^t)$。
4. 如果安全控制器把名义动作改为$\boldsymbol u_t=\boldsymbol u_t^r-\boldsymbol K\boldsymbol e_t+\Delta\boldsymbol u_t^{\mathrm s}$，精确模型的误差方程还多出$\boldsymbol B\Delta\boldsymbol u_t^{\mathrm s}$。

### 2.4 策略的约束与安全

主要内容：以安全区域和一步可行动作为基础，讨论反馈修正，以及扰动和离散执行下逐轨迹安全保证的条件。

论证与表述逻辑：

1. 状态约束下的安全区域：一个制动系统最终停下，仍可能在停下之前越过位置边界；平均成本很小的随机系统，也可能有不可接受的少数路径。安全集合（safe set）直接规定允许出现的状态。
2. 安全条件下的可行动作：函数$h$只用符号区分安全与否，不必等于几何距离。
3. 可行约束下的反馈修正：调节或跟踪已经提出名义动作$\boldsymbol u_{\mathrm{nom}}$，但该动作可能违反安全条件。
4. 扰动与离散执行下的安全保证：名义屏障条件只计算模型给出的变化率。真实连续动态多出加性扰动时，安全函数的导数还多出$\nabla h(\boldsymbol x)^\top\boldsymbol d_t$。

#### 2.4.1 状态约束下的安全区域

主要内容：一个制动系统最终停下，仍可能在停下之前越过位置边界；平均成本很小的随机系统，也可能有不可接受的少数路径。安全集合（safe set）直接规定允许出现的状态。

论证与表述逻辑：

1. 定义（正向不变集）：若任意$\boldsymbol x_0\in S$所产生的闭环解，在其存在的全部未来时刻均位于$S$，称$S$对该闭环正向不变（forward invariant）。
2. 若边界$\partial S=\{h=0\}$光滑且其上$\nabla h\neq\boldsymbol0$，内侧对应$h$增大的方向。在闭集、正则边界与适定闭环等条件下，以闭环速度朝内或相切给出Nagumo边界判据。
3. 用$h(x)=x^3$表示同一半轴却在零点丢失梯度方向的反例，引出由集合内邻近点逼近速度方向的切锥。半轴的$T_S(0)=[0,\infty)$排除负速度；在已声明的正则边界条件下，切锥简化为梯度半空间。退化边界的方向检查与下一节沿轨迹的CBF比较证明分别处理。

#### 2.4.2 安全条件下的可行动作

主要内容：函数$h$只用符号区分安全与否，不必等于几何距离。从边界上的$\dot h\geq0$出发，先用$\dot h\geq-\gamma h$、$\gamma>0$限制内部安全余量的下降，再推广为扩展类$\mathcal K$函数；内部可下降、接近边界时下降限额趋零的机制引出CBF。

论证与表述逻辑：

1. 命题（CBF条件保证正向不变）：在已声明的动态与安全函数正则条件下，若反馈$\boldsymbol u=\kappa(\boldsymbol x)$局部Lipschitz，并在包含$S$的开区域$D$中始终满足$\kappa(\boldsymbol x)\in K_{\mathrm{cbf}}(\boldsymbol x)$，则$S$在相应闭环解存在的时间区间内正向不变。
2. 推导：沿任意闭环解记$r_t=h(\boldsymbol x_t)$，链式法则和CBF约束给出$\dot r_t\geq-\alpha(r_t)$。考虑比较系统$\dot z_t=-\alpha(z_t),\qquad z_0=r_0\geq0$；$\alpha$局部Lipschitz，比较系统局部解唯一，且$z=0$是平衡解，从非负初值出发的解不能穿过零点。又因$\alpha$严格递增且$\alpha(0)=0$，$z_t$留在$[0,z_0]$内，所以比较解在任意有限时间存在。
3. 回到离散温度系统，令$S=[0,3],U=[0,1]$且无噪声。下一步安全要求$0\leq0.8x+u\leq3$，因此精确的一步安全动作集合为$K_{\mathrm{safe}}(x) =[\,\max\{0,-0.8x\},\ \min\{1,3-0.8x\}\,]$；对$x\in[0,3]$，下端为$0$，上端至少为$0.6$，所以每个安全状态都有可行动作。

#### 2.4.3 可行约束下的反馈修正

主要内容：调节或跟踪已经提出名义动作$\boldsymbol u_{\mathrm{nom}}$，但该动作可能违反安全条件。

论证与表述逻辑：

1. 示例（一维积分器上的安全投影）：考虑$\dot x_t=u_t$、$S=[0,\infty)$、$h(x)=x$及$\alpha(h)=\gamma h$。
2. 固定状态时，正定二次目标的强制性阻止最小化序列逃向无穷，非空闭可行域保证取到最小值，凸性与严格凸性保证唯一。约束$xu\geq|x|^{3/2}$下唯一最优动作在零点为零、非零处为$\operatorname{sgn}(x)\sqrt{|x|}$，仍非局部Lipschitz；约束梯度在零退化，说明调用闭环不变性前必须另验反馈规则性。
3. 对无噪声温度模型，先命名状态相关的安全动作界$\underline u_{\mathrm{safe}}(x)=\max\{0,-0.8x\}$与$\overline u_{\mathrm{safe}}(x)=\min\{1,3-0.8x\}$，再把名义动作投影到已核验非空的安全区间。正弦跟踪的首步投影给出$x_1=1$，而不是无约束的$1.153$；此时$e_1=1-[2+0.4\sin(\pi/8)]\approx-1.153$，不再等于$0.5e_0=-1$。投影保证该区间内的逐步安全，跟踪误差须保留安全修正项重新分析。

#### 2.4.4 扰动与离散执行下的安全保证

主要内容：名义屏障条件只计算模型给出的变化率。真实连续动态多出加性扰动时，安全函数的导数还多出$\nabla h(\boldsymbol x)^\top\boldsymbol d_t$。以余距和速度的制动相图展示二阶约束：最大加速度2时，负速度状态需有余距至少v²/4；同速度的两个起点分别能在边界前停下和必然越界。这一解析可保持域不等同于一般高阶CBF可行集。

论证与表述逻辑：

1. 离散温度系统若$|w_{t+1}|\leq\delta$，最坏扰动下的安全动作集合为$K_{\mathrm{safe}}^\delta(x) =[\,\max\{0,\delta-0.8x\},\ \min\{1,3-\delta-0.8x\}\,]$；当$0\leq\delta\leq0.6$，该集合对所有$x\in[0,3]$非空：下端不超过$1$，未截断区间宽度$3-2\delta$非负，且上端在$x=3$也不小于零。
2. 采样点满足连续CBF条件不自动保证采样间安全；在有效的速度界与Lipschitz区域中预留保持动作所需的裕量，或另以离散屏障作逐步归纳，再检查连续采样间轨迹。
3. 双积分器的位置约束先显示一阶导数没有动作、二阶导数才出现输入，再命名相对阶。高阶屏障还要求初态同时满足位置与新增速度条件、约束始终可行且闭环适定；制动距离反例说明安全位置不等于可避免后续越界。
4. CBF还要求用于计算约束的状态信息可靠。若只有估计值，应先给估计误差集合界或概率模型，再收紧安全集合或构造输出反馈屏障。

### 2.5 本章小结

主要内容：区分可实施性、系统结构、闭环稳定、调节跟踪与安全，说明存在一条可达轨迹不足以保证固定反馈的行为。

论证与表述逻辑：

1. 一个可实施策略既要遵守信息时序，也要符合执行器能够改变的方向。可控、可观测要求处理全部状态方向；可稳定只要求不可控模式自行衰减，可检测只要求不可观测模式自行衰减。结构条件仍需由实际闭环矩阵、误差动态或Lyapunov不等式完成行为核验。
2. 在同一温度模型中，固定目标$2$需要平衡输入$0.4$，再加误差反馈才得到$e_{t+1}=0.5e_t$。运动参考改用$u_t^r=r_{t+1}-0.8r_t$抵消参考变化，同一个稳定误差系统便能服务于跟踪。
3. Riccati方法在特定二次成本下选择反馈。有限时域的逐步配方保持二次形式；确定性无折扣无限时域还需可稳定、成本可检测及权重条件，才能同时得到稳定化与成本最优性。
4. 安全性约束全过程。对无噪声温度系统，固定目标反馈已经保持$0\leq u\leq1,0\leq x\leq3$；同一增益的运动参考却可能在初始纠偏时要求过大输入。
