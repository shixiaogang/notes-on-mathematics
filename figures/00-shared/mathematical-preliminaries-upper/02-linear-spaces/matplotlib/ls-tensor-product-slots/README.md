# 张量积的行与列

用于卷一第8章“运算”§8.4.2“张量积”（`fig:ls-tensor-product-slots`），回答“两个向量的全部两两乘积怎样排成二阶数组，它的行与列分别是哪个因子的倍数”。数值由解析式直接求出，是教学构造。

| 文件 | 读图任务 | 原生尺寸 | 正文宽度 | 图环境 |
| --- | --- | --- | --- | --- |
| `ls-tensor-product-slots.pdf/.png/.svg` | $u\in\mathbb R^2$（竖排）与 $v\in\mathbb R^3$（横排）的张量积排成 $2\times3$ 网格，元素 $u_iv_j$；标出第2行 $=u_2v^\top$、第3列 $=v_3u$ | 112 mm × 32 mm | 112 mm（缩放 1.0） | `figure` |

## 图中元素含义

- 左：$u=(1,2)^\top$ 竖排两格（蓝），$v=(3,-1,2)^\top$ 横排三格（绿）；分量下标用同色标注。
- 右：$u\otimes v$ 的 $2\times3$ 网格，左侧标行因子 $u_i$，上方标列因子 $v_j$，格内为 $u_iv_j$。
- 蓝色实线框：第2行 $(6,-2,4)=u_2v^\top$；绿色虚线框：第3列 $(2,4)^\top=v_3u$。

## 关键精确值

- $u\otimes v=\begin{pmatrix}3&-1&2\\6&-2&4\end{pmatrix}$。$u$ 与正文示例 `ex:ls-tensor-product-two-vectors` 的 $x=(1,2)^\top$ 相同，$v$ 的前两个分量与 $y=(3,-1)^\top$ 相同。

## 样式

使用 `figures/00-shared/academic-drawing/plot_style.py`：数学标注为 Fira Math（粗斜体向量用数学字母区字形），中文为思源黑体 Normal；主标注 8 pt，下标标注 7.5 pt；蓝 `#7188A3`/`#E5EAF0` 对应 $u$ 与行，绿 `#829C8B`/`#E8EEE9` 对应 $v$ 与列。

## 运行

```bash
python figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-tensor-product-slots/plots.py
```

需要 Matplotlib（生成时为 3.11.2），不需要 numpy。从任意目录运行均可，不调用 LaTeX，无随机采样；同时重写 `sources.json`（参数、计算结果、版式与字体校验值）。

## 修订

- 2026-10-31：重绘。原图画的是 $2\times2$ 基槽位网格 $e_i\otimes f_j$ 与另一组 $u=(1,2)$、$v=(3,1)$ 的 $2\times2$ 外积，与图注所述 $u\in\mathbb R^2$、$v\in\mathbb R^3$ 的 $2\times3$ 网格不符，且标注不是数学字体、版面留白不均。现按图注结构重画，图注同步改为新数值。
