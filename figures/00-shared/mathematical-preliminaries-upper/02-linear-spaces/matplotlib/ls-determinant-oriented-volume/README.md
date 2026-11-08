# 行列式的有向体积

按当前正文重绘为三面板，正文宽度 169 mm、导出高度 59 mm。所有面板使用相同的长度比例，主体字号为 8 pt。

- 左：单位正方形，有向面积为 1。
- 中：$A=\begin{pmatrix}2&0.5\\0&1.5\end{pmatrix}$，有向面积为 3。
- 右：$A_-=A\operatorname{diag}(-1,1)$，第一列反向，有向面积为 −3。
- 蓝、绿向量为第一、第二列；深灰弧箭头从第一列转到第二列。无背景网格。

运行本目录的 plots.py 可导出同名 PDF、SVG 和 PNG，来源与精确矩阵保存在 sources.json。
共享样式从 figures/00-shared/academic-drawing/plot_style.py 加载，使用仓库字体和统一加粗线条。数值是解析教学例，无随机采样。
