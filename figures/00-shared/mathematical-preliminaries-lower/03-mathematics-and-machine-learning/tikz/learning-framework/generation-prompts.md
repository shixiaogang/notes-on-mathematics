# 第17章框架图生成记录

2026-10-07。内置 imagegen 生成原生带字 PNG；工具未暴露模型名称、版本、种子或原生尺寸控制。用户指定直接生成中文与数学标签，采用 LXGW WenKai 文楷字形并参照卷二图1.2；没有覆盖文字、后加排版层或上采样。字体参考由仓库 `fonts/LXGWWenKai-Regular.ttf` 的实际标签字样渲染。

旧TikZ设计草稿保留在 `drafts/`，无现行正文引用；成书只使用下列原生带字图片。

## 当前资源与事实清单

最终资源是 `static-learning-framework.png`（1649×954）和 `interactive-learning-framework.png`（1516×1037），通过同名 LaTeX 包装按169mm宽嵌入，有效分辨率分别约248dpi与228dpi。静态原文件为 `exec-5ed9f6b4-f395-4237-b8bb-bdd83cfe3560.png`；交互原文件为 `exec-864af14c-2fbb-4806-9fd5-781a965b17da.png`。原图保留在工具默认生成目录，出版使用仓库副本。

两图均为文字在上、图标在下。环境、分布、样本与观测使用浅蓝；目标、算法与策略使用浅黄；学得对象与评价使用浅红。相同对象使用同类深灰线图标。参照卷二低饱和蓝/黄/红配色、细轮廓和文楷常规字重。图像为原生栅格文字，字形经目视对照，工具不提供字体嵌入证据。

共同接口：样本集D及候选类H、损失ℓ、约束C输入完整学习算法A；A输出经验目标R̂_D和学得对象h_D。经验目标在算法上方，连接方向是A到经验目标。算法构造并求解该目标，不能把D到经验目标再到A画成唯一串行通路。

静态图：环境→P→D→A→h_D；P另采样得到D_eval，D_eval与h_D形成有限样本总体评价R̂_Deval(h_D)。统计分析连接它与真正总体风险R_P(h_D)，P到总体风险的虚线表示期望定义。

交互图：上方β→采集轨迹分布→D→A→h_D=π；下方π→评价轨迹分布→D_eval→有限样本总体评价。中间只有同一个环境与可得观测/历史I_t。β和π都依据I_t选择行动，行动进入环境更新内部状态，环境再产生新观测。两策略对应不同运行阶段。右侧学得对象分别连接执行策略与有限样本总体评价，后者明确接收学得对象及评价样本两个输入。外侧反馈表示在线更新下一轮β。样本评价通过统计分析联系理论总体风险。没有直接隐状态到策略的输入，也没有直接读取轨迹分布计算未知期望的实际运算箭头。

## 最后接口修订提示词

静态参考为重排后的 `exec-70db354d-5d53-423e-8517-88d1847a3141.png`，另提供实际文楷字样；交互参考为 `exec-fa47a4a1-192e-4ca9-a116-1d55af15110a.png`，另提供相同字样。两者此前采用过经验目标输入A的接口，该接口已由用户后续要求替代。以下修订确定现行接口。

### 静态图

```text
Edit this textbook diagram locally and preserve its composition, all unaffected arrows, all native Chinese labels, LXGW WenKai font appearance, blue/yellow/red pale palette, thin gray outlines, and icons under their text. All output labels must be generated natively, not overlays. CRITICAL interface: the complete learning algorithm A takes D and (candidate class H, loss ell, constraints C) as inputs, and OUTPUTS empirical objective R-hat_D and learned object h_D. Thus objective is a result ABOVE A, and arrow must point UP from A to objective. H/ell/C strip must feed A, never objective. Remove every D->objective arrow, every objective->A arrow and every H/ell/C->objective arrow. Retain the direct D->A and A->h_D connections. In the static reference, move the '候选类 H 损失 ell 约束 C' thin yellow strip into the empty area to the LEFT of the empirical-objective box and ABOVE the sample/D-to-A row; route a short clean elbow arrow from this strip to the TOP-LEFT edge of A. The objective box remains above A with a straight UP arrow from A. Delete old topmost strip position and the old D elbow to objective. Preserve evaluation flow P -> evaluation D_eval -> 总体评价 Rhat_Deval(h_D) -> dashed statistical analysis -> 总体风险 R_P(h_D), learned-object inputs to both evaluation boxes, and dashed P expectation definition. Do not change any of these evaluation semantics. All labels above icons. Ensure no lines collide, no residual arrows from erased connections, crisp Chinese, balanced spacing.
```

### 交互图

```text
Edit this textbook diagram locally and preserve its composition, all unaffected arrows, all native Chinese labels, LXGW WenKai font appearance, blue/yellow/red pale palette, thin gray outlines, and icons under their text. All output labels must be generated natively, not overlays. CRITICAL interface: the complete learning algorithm A takes D and (candidate class H, loss ell, constraints C) as inputs, and OUTPUTS empirical objective R-hat_D and learned object h_D. Thus objective is a result ABOVE A, and arrow must point UP from A to objective. H/ell/C strip must feed A, never objective. Remove every D->objective arrow, every objective->A arrow and every H/ell/C->objective arrow. Retain the direct D->A and A->h_D connections. In the interactive reference, keep the top row β -> collection trajectory P_E^β -> D -> A -> learned h_D=π; middle one shared environment E and observed/history I_t; bottom row π -> evaluation trajectory P_E^π -> D_eval -> 总体评价 Rhat_Deval(π). Keep both action arrows to SAME E, E internal state update then produces observations, E -> I_t, I_t -> β, I_t -> π; keep outer learned π deployment loop and outer next β update. Move H/ell/C strip into empty middle-right space BELOW A, around the level immediately below the top row, with a clean short UP arrow into A bottom. Empirical objective remains ABOVE A, with UP arrow A->Rhat_D. Delete old metadata strip at upper-left and its old objective-directed edge. Keep theoretical 总体风险 R_M(π) and dashed statistical-analysis arrow from sample evaluation. Do not add a second environment or direct state-to-policy links. No direct objective-to-A arrows.
```

生成稿的经验目标短连线仍误向下，局部直线修订也未消除错误；最终改为从A上方经空白区域折回、从左侧进入经验目标。下述提示词对应输出连线修订稿，其余节点与关系保持；最终图随后再补评价对象输入。

```text
Correct exactly the empirical-objective output connection in this diagram. Preserve ALL boxes, text, native WenKai typography, icons and other arrows. The very short vertical arrow between 经验目标 and 学习算法 currently points downward, incorrectly. DELETE that entire short vertical connector, leaving clear white space between the bottom of objective and top of algorithm. Do not draw ANY connector in that short gap. Instead use this precise new elbow route, ending with a RIGHT-POINTING arrowhead into the LEFT SIDE of the upper 经验目标 box: start at TOP-LEFT PORT of 学习算法 A (around x1000,y261); move up slightly to y248; turn LEFT through white space to x865; turn UP to y170; turn RIGHT into LEFT BORDER of 经验目标 (around x928,y170). Place the ONLY triangle arrowhead at the objective left border pointing RIGHT into objective. No arrowhead near A. This route unambiguously means A -> empirical objective. It stays entirely in empty white space above the sample row and to the left of the objective, never inside D. Add the short Chinese label '构造' above the final horizontal segment if it fits. Keep metadata H/ell/C -> A upward connector below algorithm and the direct D -> A -> learned object main row unchanged. Do not redesign anything else, do not add D -> objective or objective -> A. The objective is an OUTPUT from A; it is not an input. The old downward connector MUST completely disappear.
```

最终补充学得对象到有限样本评价的输入边，参考为 `exec-aa4d1297-2747-4189-b78b-a770958aaa42.png`，生成最终交互原文件：

```text
Make ONE additive connection to this final Chinese textbook diagram. Preserve all existing pixels/design: all boxes, Chinese WenKai text, icons, colors, correct A-to-objective elbow output arrow, shared environment/observation/action loops, top and bottom row connections. Need the learned object h_D=π to be an explicit second input to finite-sample evaluation, in addition to D_eval. The existing deployment wire exits the bottom/right area of learned-object box and runs DOWN the outer RIGHT MARGIN, then around the bottom into 执行策略π. Add ONE horizontal LEFT-POINTING arrow branch from that right-margin vertical deployment wire into the RIGHT BORDER of the bottom pale-red 总体评价 Rhat_Deval(π) box. Use the SAME grey thin stroke and triangular arrow style. At the right vertical wire put a small filled junction dot, around y=880, and run a straight horizontal line LEFT to the evaluation box's right edge around x=1234,y=880; the arrowhead ends AT that box border, facing LEFT into evaluation. Route above the existing edge label '使用学得对象' so no text is crossed. The branch must clearly come from the learned h_D=π deployment line, NOT from metadata H/ell/C or true-risk box. This makes learned candidate and D_eval jointly input sample evaluation. No additional label needed. Preserve the wire continuing down into executionπ, the D_eval->evaluation arrow from LEFT and the dashed statistical-analysis arrow UP from evaluation. Do not change any existing connection. Do not add any environment-to-distribution arrows. Exactly one added branch and junction, native raster output.
```

## 排布草稿提示词（接口已被上述修订覆盖）

以下记录用于追溯行列布局，不代表最终A接口。最终边清单以上面的事实清单为准。

```text
Redraw FIRST static-learning diagram with the corrected algorithm interface; SECOND image is exact LXGW WenKai typography reference. Keep identical grey flat line icons, pale blue/cream/red role colors, regular WenKai native labels, mathematical style, TEXT ABOVE ICON in every node. White canvas, landscape width~1900 and height~1100, legible at169mm.
Main learning row EXACTLY FIVE boxes, evenly spaced left-to-right: "环境 𝓔" window icon; "观测分布 P" curve icon; "样本集 D" three-card icon; "学习算法 A" two-arrow gear; "学得对象 h_D" network icon. Arrows consecutive, BUT D→A DIRECTLY (solid); there is NO empirical-objective box between D and A. P→D solid arrow labeled "采样 Γ_n".
Above A place a separate cream box "经验目标 R̂_D" hollow-bars icon. R̂_D BOTTOM→A TOP solid arrow. D TOP→R̂_D LEFT solid elbow routed cleanly above the main row. A now has TWO main inputs: empirical objective AND sample set. Above/beside empirical objective put a small source strip "候选类 𝓗  损失 ℓ  约束 𝓒", dashed into empirical-objective ONLY.
Lower evaluation row exactly three boxes: blue "评价样本集 D_eval" three-card icon; pale red "总体评价 R̂_{D_eval}(h_D)" clipboard/check icon; pale red "总体风险 R_P(h_D)" clipboard/check icon. Keep all node labels top, icon below, matching style/size. P→D_eval SOLID separate sampling route labeled "评价采样 Γ_eval"; D_eval→sampled total-evaluation solid arrow. Learned h_D→sampled total-evaluation solid clean elbow, showing fixed learned object is evaluated. Sampled total-evaluation→population-risk DASHED arrow labeled "统计分析". P→population-risk separate outer dashed definition route labeled "期望定义". Evaluation D_eval is separate from top D; no D→D_eval. The "总体评价" box is a FINITE-SAMPLE RISK ESTIMATE (has hat), "总体风险" is theoretical reference (no hat). Ensure clean ports, no connectors through boxes, avoid crossing where practical. Do not add further nodes or decorate. This new arrangement must make D→A and R̂_D→A separately unmistakable.
```

```text
Completely REARRANGE FIRST diagram to the author's exact requested three-layer composition. SECOND image is actual LXGW WenKai font reference. Keep the SAME grey line icons, pale blue/cream/red fills, WenKai regular Chinese glyphs, mathematical typography. ALL nodes TEXT ON TOP and ICON BELOW. White landscape canvas about1900×1300, large readable native labels at169mm. No title/legend/caption.
UPPER main row EXACTLY FIVE boxes left-to-right, around y300–500:
1 "采集策略 β" cream network icon at x100–330.
2 "采集轨迹分布 P_𝓔^β" blue curve icon at x480–760.
3 "样本集 D" blue three-card icon at x880–1100.
4 "学习算法 A" cream iteration gear at x1230–1450.
5 "学得对象 h_D=π" pale red network at x1600–1820.
Connect consecutive boxes; β→P_𝓔^β is thin dashed definition arrow, P_𝓔^β→D SOLID labeled "采样 Γ_n", D→A DIRECT SOLID, A→h_D SOLID. NO empirical objective between sample and algorithm.
ABOVE A, around x1230–1450,y50–220: separate cream "经验目标 R̂_D" hollow-bars icon. R̂_D→A solid downward arrow. D→R̂_D solid elbow upward then right into its LEFT/BOTTOM port, separate from direct D→A. Small strip to its left "候选类 𝓗  损失 ℓ  约束 𝓒", dashed to empirical objective only. A's TWO inputs are D and empirical objective.
MIDDLE row around y650–870:
- ONE shared blue environment at x100–330. Text top "环境 𝓔", then "状态更新 s_t→s_{t+1}", downward internal arrow, then "产生新观测"; window icon at bottom.
- ONE blue information box at x480–760: "可得观测 / 历史 I_t", eye/history icon. E→I_t SOLID rightward labeled "新观测".
- β→E SOLID downward action connector using x170 between top β bottom and E top, labeled "采集行动". β does not read state.
- I_t→β SOLID observation elbow: from I_t TOP to whitespace y~570, left to x280, up into β BOTTOM x280. Keep separate from β action at x170.
LOWER main row EXACTLY FOUR boxes left-to-right around y1020–1220, aligned with upper row columns:
1 "执行策略 π" cream network at x100–330.
2 "评价轨迹分布 P_𝓔^π" blue curve at x480–760.
3 "评价样本集 D_eval" blue three-card at x880–1100.
4 "总体评价 R̂_{D_eval}(π)" pale red clipboard/check at x1230–1550.
π→P_𝓔^π dashed definition; P_𝓔^π→D_eval SOLID labeled "采样 Γ_eval"; D_eval→sampled total-evaluation SOLID. Total evaluation here is the FINITE-SAMPLE risk estimate (with hat), not the inaccessible true expectation.
- π→E SOLID UPWARD action connector using x170 from π TOP to E BOTTOM, labeled "执行行动".
- I_t→π SOLID observation elbow: from I_t BOTTOM to whitespace y~940, left to x280, down into π TOP x280, separate from the x170 action.
Thus both β and π ONLY access observation/history I_t, and both act on SAME E. No direct state/E→policy observation line.
- h_D=π→lower execution π via a SOLID outer margin route (outside right and bottom rows, ending into π LEFT), label "使用学得对象"; optional h_D→next β outer top loop labeled "据 π 更新采集策略", avoid empirical-objective box.
In empty middle-right whitespace (x~1230–1550,y~700–800), add only a small pale red THEORY REFERENCE strip "总体风险 R_𝓜(π)" (no full icon box necessary). Sampled bottom total-evaluation→this strip is DASHED upward, labeled "统计分析". Do NOT make a direct actual-computation edge from evaluation law to true risk.
No direct E→trajectory-law connectors are necessary: the E/policy observation-action loops plus the law's subscript show shared E; do NOT add extra edges that clutter the three layers. Environment/policy jointly determine each law, but only I_t is policy input. No training-law→evaluation-sample edge, no direct action→law. Preserve native WenKai text, grey icons, crisp flat colors, correct arrowheads. Exact scientific topology and clear row organization take priority.
```
