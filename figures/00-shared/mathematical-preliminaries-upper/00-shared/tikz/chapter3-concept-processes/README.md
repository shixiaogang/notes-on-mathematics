# 第三章概念与过程图

用于补充极限、微分、积分及边界公式的几何解释。图内只保留必要坐标、变量、方向，条件与解释放在正文图注；有限图像不代替收敛或可微性的证明。

在任务工作区根目录运行：

```sh
python3 figures/00-shared/mathematical-preliminaries-upper/00-shared/tikz/chapter3-concept-processes/generate.py
```

简单几何图由 TikZ 绘制；每幅保留独立可编辑源。 每幅保留矢量 PDF、360 dpi PNG、解析参数与字体校验记录 JSON；完整参数见对应 JSON 和生成器。配色遵循 specs/figures.md，字体使用仓库固定文件及许可证。112 mm 为正文宽，169 mm 为跨栏宽；TikZ 记录实际边界与接入后的字号缩放。

| 图源 | 用途与解释边界 |
| --- | --- |
| `finite-open-cover` | 用闭区间的有限开覆盖与开区间的U_n=(1/n,1)对照；最大下标留下未覆盖区间，说明有限子覆盖与定义域边界的联系。 |
| `cantor-deletion` | 增加康托尔删除过程图，区分每个有限阶段的正长度与交集的零测度，说明零测不等于空集。 |
| `chain-rule-types` | 增加前向类型与反向梯度的简图，按2→3→1核对Jacobian转置的形状，区分梯度传递和求逆映射。 |
| `product-measure-grid` | 增加按边权重等比例绘制的有限乘积测度格表，以格面积体现乘法、格求和体现累计，并保留一般联合分布未必乘积分解的边界。 |
| `line-density-work` | 增加同一路径的标量密度累计与向量场做功对照，弧长√2和水平投影累计1分别核对，明确两类积分的对象与局部权重。 |
| `normal-projection` | 增加局部法向截面上的正交分解图，区分有符号法向标量和法向投影向量；翻转n使前者变号而后者不变，说明通量朝向规则。 |
| `boundary-orientation-cancellation` | 增加四块公共边抵消与圆环内外边界方向图，说明相容方向的机制并回接Green与Stokes的拼接。 |
| `gauss-shared-face` | 增加相邻立方体的公共面通量图，固定常向量场和相反外法向核对±1抵消，保留特殊机制与一般Gauss定理的论证边界。 |

验收范围为本次新增图及其接入，不追认历史图像。逐图核验记录见同名 `.review.json`。
