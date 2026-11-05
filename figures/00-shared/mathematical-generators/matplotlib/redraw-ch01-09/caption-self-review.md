# 本轮图注与局部引导的三遍作者自查

范围：4张新图N1/N2/N3/N5，1张扩展图N4，31张图的颜色或线型图注修改，以及其局部回指。原有定义、推导和章节结构是f70正文基线，本记录不重复宣称对九章全文进行了一次新的三遍独立审查。稳定定位用图key和`caption-units.json`中的`key:C-Snn`，源哈希绑定在`review-bindings.json`；各图数学含义与实际输出观察逐项见`review-observations.tsv`。脚本仅截取/编号文本及计算哈希，所有语义判断由实际阅读作出。

## 第一遍：在章节问题链中复读

N1位于第四章“多目标的最优折中”的三方案反例之后、共同下降方向之前。先由损失偏序说明Pareto，再指出加权和只能选择支撑方向；新增图仅把已给出的有限像及等值线可视化，不补造连续前沿、不将参数候选与损失向量混同。它兑现的是“某个Pareto点不能由加权和获得”，不是所有多目标算法比较。

N2位于双层求解中两步二次更新的现成例子之后、隐式局部分支条件之前。上行读取有限步算法输出，下行读取精确内层解，两条链分别给出复合目标。图注重申初始化/步长，比较的导数是3/8与1；两个算式都正确而目标不同。图后继续局部分支与全局解的条件，没有把链式求导当成误差传播定理。

N3位于第六章“坐标的转换”的两张单位圆坐标图说明之后、三图兼容关系之前。抽象定义已经出现，图把同一p±的记录变化展开；读者可先看空心漏点，再看两交叠分支。图不改变圆的连通性，也不声称存在单张全局实坐标图。

N4替换第八章分块FFT段既有重叠相加图。前一段说明完整块卷积放回全局位置，后一段算出N4循环输出及丢弃首项。并排图的左右流程分别承接这两段，图后才讨论块大小、工作区与耗时。图注对红框给不同明确动作：左框相加贡献，右框丢污染项；两个相同终值没有遮蔽拼接条件。

N5位于第九章一般袋消息递推与运行交集论证之后、固定宽度成本和循环消息限制之前。图用贯穿叶袋123/234给出四行符号表，保留z2,z3而汇总z1；ΦB只由分配一次的袋内因子组合。没有提前把一般有环图直接套树公式。查询仍须后袋组合、和积归一化或最优见证回溯，图不取代前文条件。

其余图注修改不重排章节或引入新科学对象，逐项只对当前图中颜色/线型恢复一致命名。七、八章的“输入”仅为既有数学函数/信号索引，未把它转成第十七章未指定的训练/评价对象。31处已逐图读完整图注并对照图，接受理由是具体对象和比较口径没有变化、指向的当前图元唯一。

## 第二遍：段落职责和承接

N1图注的中心是“可行有限像中，Pareto与加权和可选性不同”。开句固定三个候选及两个最小化方向，中句给∀α∈[0,1]的严格比较，接句说明辅助等值线不是新增候选，末句只收束此反例。

N2图注的中心是“同一内层问题可产生两个不同外层目标”。初始化/步长先于有限步结果，精确解随后并列；外层读取同一损失，再解释导数不同，末句就地回指这两个目标，没有空泛的“方法不同”。

N3图注的中心是“同一圆点可以有两份局部记录”。漏点和两图覆盖先交代范围，实点指向几何对象，两个角度分支说明记录转换，最后限定断点属于坐标。没有用后面的切空间或微分信息来补当前位置。

N4图注的中心是“两种分块拼接恢复同一完整线性卷积”。固定输入、核、N，先左后右对应版面；左贡献加法与右污染丢弃分别说明，尾部补零产生的多余输出只按目标长度裁去。末句保留算法差异，不另添误差/残差长表。

N5图注的中心是“叶袋压缩成接口消息表”。袋/接口/内部变量先于四行表，ΦB与⊕就地回接已有递推，未给未指定因子虚拟数值。最后说明右袋后续动作，承接紧接着的袋大小成本而不泛化为循环消息收敛。

其余改变的图注逐段对照`review-observations.tsv`对应key：例如Möbius说明左累计与右局部斜纹，Clarke分别说左有效下界与右局部最大，幂序列分别说三n函数及整体误差，基函数仍以单位系数增量比较作用范围；更换颜色没有改动条件、指标方向、定义域、点形、数组或因果强度。

## 第三遍：句子与用词

以下连续句组共同完成一个数学动作，按`caption-units.json`列出完整句ID。每个组复述的是实际意思而非标题意图。

| 图key/范围 | 短引与实际意思 | 具体接受依据 |
|---|---|---|
| v1-opt-pareto-weighted-sum:C-S01, v1-opt-pareto-weighted-sum:C-S02, v1-opt-pareto-weighted-sum:C-S03, v1-opt-pareto-weighted-sum:C-S04 | “三个精确可行损失向量”；“对任意α”；“仅为…等值线”；“Pareto最优不保证…” | 候选明确为三个离散向量，两个方向均最小化；∀α比较有min≤1/2<.6的邻文证明；虚线不是可行连线。 |
| v1-opt-bilevel-target-chains:C-S01, v1-opt-bilevel-target-chains:C-S02, v1-opt-bilevel-target-chains:C-S03, v1-opt-bilevel-target-chains:C-S04 | “固定w0…步长”；“两个复合目标不同”；“各自对应自己的目标” | 所有依赖都出现在图与前文例子，有限算法导数/精确解导数的主语各自唯一，3/8与1可直接求导核算。 |
| v1-geometry-circle-chart-transition:C-S01, v1-geometry-circle-chart-transition:C-S02, v1-geometry-circle-chart-transition:C-S03, v1-geometry-circle-chart-transition:C-S04 | “各图漏掉”；“同一几何点”；“上半圆…下半圆” | χ1/χ2覆盖范围已在前文定义，p±不变；θ=0和±π不属于两图交叠，不把分支公式扩到漏点。 |
| v1-cnn-fft-blocks:C-S01, v1-cnn-fft-blocks:C-S02, v1-cnn-fft-blocks:C-S03, v1-cnn-fft-blocks:C-S04 | “均取N=4”；“放回全局位置”；“丢弃…首项”；“按目标长度截去” | 左3项块完整卷积合法补零至4，右循环卷积长4/核长2污染首项；五项目标长度来自4+2−1，尾零不是污染首项。 |
| v1-graph-theory-bag-message-interface:C-S01, v1-graph-theory-bag-message-interface:C-S02, v1-graph-theory-bag-message-interface:C-S03, v1-graph-theory-bag-message-interface:C-S04 | “仅与C…相连”；“只汇总内部变量z1”；“没有为因子虚设数值” | 叶袋没有其他入消息；四二值接口配置列尽，⊕未偷换成一般求和，ΦB因子归属规则保持前文条件。 |
| v1-cnn-fft-blocks:R-S01, v1-cnn-fft-blocks:R-S02, v1-opt-pareto-weighted-sum:R-S01, v1-opt-bilevel-target-chains:R-S01, v1-geometry-circle-chart-transition:R-S01, v1-graph-theory-bag-message-interface:R-S01 | “标出这三个方案”；“两个不同目标”；“同一圆…记录”；“右侧…并列”；“二值变量…四个接口值” | 每处回指恢复当地已有具体例子，不写空泛“如图所示”；不要求读者去后文补成立条件。 |
| 其余31key全部C句 | 源文本和当前线型/颜色对照 | 本轮改变的是g/h柱、函数/近似、几何方向、有效/不可行和新增边的图元名称；所有原数学陈述逐句读过，按各key人工观察核对关系两端、条件、指标及正负方向。 |

七门槛实际校准：G1所有保证都绑定具体有限集合或解析式；G2“最佳/最优/误差”保留候选空间、范数/目标和方向；G3新图只展开同一例子，无突发模型集合；G4先已有问题/算式后配图；G5各图当地段先恢复三向量、二次内层、单位圆、两条FFT链或叶袋；G6新公式均由紧邻明确运算产生，不把绘图设定当一般定理；G7“同一/这两条/右侧”均就地指具体对象，适用范围不从有限例子扩到一般情形。

E1/E12：没有未指定统计指标的“表现接近”；相对敏感性图明确响应扰动5e-5与系数变化，幂误差图明确L²/上确界。E2/E3：新增图无笼统“使用后果/概率频率要求”。E4：比较句直接写严格大于、保留或丢弃，不用嵌套否定。E5：N1直接列出三个候选损失向量，不让读者猜有限样本为何形成候选集合。E6：五个补充/替换各补图形机制或可核算接口值，不重复章节起因。E7：所有回指恢复当地对象，不调用未恢复的“几个问题”。E8：图注首句均为具体对象或计算链。E9：N1允许权重α范围明示，未用未指定的“最不利”。E10：没有从局部到全局分布的扩大；圆过渡和树消息保留局部/叶袋条件。E11：ΦB已由前文袋内因子分配定义，图不突然引入一般统计风险记号。这些适用性结论只覆盖本记录的图注与局部引导。

## 修订后闭环与边界

已从各新增位置前一段连续读到后续段落，并逐图对照当前数值/拓扑。N1最终标签与虚线/图例分开；N2导数脚注上移；N3循环变量改名后原生编译无缺字；基函数刻度右留白；割线移到容量标签下层。两处配色未完全落地（连续性输出邻域、Frobenius点）已修源、再输出、再看；图注按最后输出命名。当前图源/实际输出接受为作者自查，最终书页字号/分页及根任务独立复核另列，不以本记录代替。

## 改色/线型31图的句定位

下面仅列稳定定位；每一行的具体对象、关系和实际接受依据由review-observations.tsv同key人工记录与上面三遍复读共同给出。未改变的图注只被机械编号，不被这份作者记录宣称新增全文审查。

- v1-comb-mobius-cumulative-local：v1-comb-mobius-cumulative-local:C-S01, v1-comb-mobius-cumulative-local:C-S02, v1-comb-mobius-cumulative-local:C-S03。
- v1-combinatorics-growth-patterns：v1-combinatorics-growth-patterns:C-S01, v1-combinatorics-growth-patterns:C-S02, v1-combinatorics-growth-patterns:C-S03。
- v1-ds-six-cycle：v1-ds-six-cycle:C-S01, v1-ds-six-cycle:C-S02, v1-ds-six-cycle:C-S03。
- v1-comb-fat-margin-output-square：v1-comb-fat-margin-output-square:C-S01, v1-comb-fat-margin-output-square:C-S02, v1-comb-fat-margin-output-square:C-S03, v1-comb-fat-margin-output-square:C-S04。
- v1-prelim-perturbed-recurrence：v1-prelim-perturbed-recurrence:C-S01, v1-prelim-perturbed-recurrence:C-S02, v1-prelim-perturbed-recurrence:C-S03。
- v1-analysis-derivative-orders：v1-analysis-derivative-orders:C-S01, v1-analysis-derivative-orders:C-S02, v1-analysis-derivative-orders:C-S03, v1-analysis-derivative-orders:C-S04, v1-analysis-derivative-orders:C-S05。
- v1-analysis-clarke-stationarity-boundary：v1-analysis-clarke-stationarity-boundary:C-S01, v1-analysis-clarke-stationarity-boundary:C-S02, v1-analysis-clarke-stationarity-boundary:C-S03, v1-analysis-clarke-stationarity-boundary:C-S04。
- v1-analysis-power-convergence-scales：v1-analysis-power-convergence-scales:C-S01, v1-analysis-power-convergence-scales:C-S02, v1-analysis-power-convergence-scales:C-S03, v1-analysis-power-convergence-scales:C-S04。
- v1-opt-convex-chord-tangent：v1-opt-convex-chord-tangent:C-S01, v1-opt-convex-chord-tangent:C-S02, v1-opt-convex-chord-tangent:C-S03, v1-opt-convex-chord-tangent:C-S04。
- v1-opt-preconditioned-paths：v1-opt-preconditioned-paths:C-S01, v1-opt-preconditioned-paths:C-S02, v1-opt-preconditioned-paths:C-S03。
- v1-opt-conjugate-affine-envelope：v1-opt-conjugate-affine-envelope:C-S01, v1-opt-conjugate-affine-envelope:C-S02, v1-opt-conjugate-affine-envelope:C-S03, v1-opt-conjugate-affine-envelope:C-S04。
- v1-opt-majorizer-versus-tangent：v1-opt-majorizer-versus-tangent:C-S01, v1-opt-majorizer-versus-tangent:C-S02, v1-opt-majorizer-versus-tangent:C-S03, v1-opt-majorizer-versus-tangent:C-S04。
- v1-matrix-analysis-svd-geometry：v1-matrix-analysis-svd-geometry:C-S01, v1-matrix-analysis-svd-geometry:C-S02, v1-matrix-analysis-svd-geometry:C-S03, v1-matrix-analysis-svd-geometry:C-S04。
- v1-ch06-error-rank-curves：v1-ch06-error-rank-curves:C-S01, v1-ch06-error-rank-curves:C-S02, v1-ch06-error-rank-curves:C-S03, v1-ch06-error-rank-curves:C-S04。
- v1-matrix-analysis-coefficient-sensitivity：v1-matrix-analysis-coefficient-sensitivity:C-S01, v1-matrix-analysis-coefficient-sensitivity:C-S02, v1-matrix-analysis-coefficient-sensitivity:C-S03。
- v1-geometry-circle-distances：v1-geometry-circle-distances:C-S01, v1-geometry-circle-distances:C-S02, v1-geometry-circle-distances:C-S03, v1-geometry-circle-distances:C-S04。
- v1-geometry-sphere-parallel-transport：v1-geometry-sphere-parallel-transport:C-S01, v1-geometry-sphere-parallel-transport:C-S02, v1-geometry-sphere-parallel-transport:C-S03, v1-geometry-sphere-parallel-transport:C-S04, v1-geometry-sphere-parallel-transport:C-S05。
- v1-geometry-sphere-retraction：v1-geometry-sphere-retraction:C-S01, v1-geometry-sphere-retraction:C-S02, v1-geometry-sphere-retraction:C-S03, v1-geometry-sphere-retraction:C-S04, v1-geometry-sphere-retraction:C-S05, v1-geometry-sphere-retraction:C-S06。
- v1-functional-affine-point-readout：v1-functional-affine-point-readout:C-S01, v1-functional-affine-point-readout:C-S02, v1-functional-affine-point-readout:C-S03, v1-functional-affine-point-readout:C-S04, v1-functional-affine-point-readout:C-S05。
- v1-functional-spectral-shrinkage：v1-functional-spectral-shrinkage:C-S01, v1-functional-spectral-shrinkage:C-S02, v1-functional-spectral-shrinkage:C-S03。
- v1-functional-point-evaluation：v1-functional-point-evaluation:C-S01, v1-functional-point-evaluation:C-S02, v1-functional-point-evaluation:C-S03。
- v1-functional-basis-locality：v1-functional-basis-locality:C-S01, v1-functional-basis-locality:C-S02, v1-functional-basis-locality:C-S03。
- v1-signal-basic-operations：v1-signal-basic-operations:C-S01, v1-signal-basic-operations:C-S02, v1-signal-basic-operations:C-S03。
- v1-reader-continuous-convolution-overlap：v1-reader-continuous-convolution-overlap:C-S01, v1-reader-continuous-convolution-overlap:C-S02, v1-reader-continuous-convolution-overlap:C-S03, v1-reader-continuous-convolution-overlap:C-S04。
- v1-signal-convolution-boundaries：v1-signal-convolution-boundaries:C-S01, v1-signal-convolution-boundaries:C-S02, v1-signal-convolution-boundaries:C-S03。
- v1-signal-aliasing-curves：v1-signal-aliasing-curves:C-S01, v1-signal-aliasing-curves:C-S02, v1-signal-aliasing-curves:C-S03。
- v1-graph-theory-ancestor-moral-query：v1-graph-theory-ancestor-moral-query:C-S01, v1-graph-theory-ancestor-moral-query:C-S02, v1-graph-theory-ancestor-moral-query:C-S03, v1-graph-theory-ancestor-moral-query:C-S04。
- v1-graph-theory-elimination-fill：v1-graph-theory-elimination-fill:C-S01, v1-graph-theory-elimination-fill:C-S02, v1-graph-theory-elimination-fill:C-S03, v1-graph-theory-elimination-fill:C-S04。
- v1-graph-theory-flow-cut-certificate：v1-graph-theory-flow-cut-certificate:C-S01, v1-graph-theory-flow-cut-certificate:C-S02, v1-graph-theory-flow-cut-certificate:C-S03, v1-graph-theory-flow-cut-certificate:C-S04。
- v1-graph-theory-spectral-coordinates：v1-graph-theory-spectral-coordinates:C-S01, v1-graph-theory-spectral-coordinates:C-S02, v1-graph-theory-spectral-coordinates:C-S03, v1-graph-theory-spectral-coordinates:C-S04。
- v1-graph-theory-polynomial-locality：v1-graph-theory-polynomial-locality:C-S01, v1-graph-theory-polynomial-locality:C-S02, v1-graph-theory-polynomial-locality:C-S03, v1-graph-theory-polynomial-locality:C-S04, v1-graph-theory-polynomial-locality:C-S05。

独立复核后闭环：A10字面模式集、A05纯白画布、A20邻文颜色及A56竖线图注四项见 independent-findings-closure.json。原作者全图注记中A10/A05/A56接受措辞过宽已更正；不把作者初查当独立通过。A20与A56两处句子修后按上文章→段→句顺序及连续上下文复读。

第二批独立发现 A79/A52/A35/A48 已集中修复，先按章节问题和数学条件核对位置，再连续复读图前、图注、图后，最后逐句核对主语、符号对象、范围和比较口径。具体含义、接受依据和原句/新句在 independent-findings-closure.json；初始295句索引增为297句，是A79及A35拆开解释，不以计数代替语义审查。四图科学源及图资产未改变。
