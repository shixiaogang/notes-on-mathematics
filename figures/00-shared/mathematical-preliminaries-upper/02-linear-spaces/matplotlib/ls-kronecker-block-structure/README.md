# Kronecker 积块结构

采用紧邻正文示例 ex:ls-kronecker-two-by-two 的数值。正文宽度 112 mm、导出高度 85 mm，主体字号为 8 pt。

$A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，$B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$，则
$A\otimes B=\begin{pmatrix}0&1&0&2\\1&0&2&0\\0&3&0&4\\3&0&4&0\end{pmatrix}$。

上方是两个输入矩阵，下方为四个 2×2 输出块。绿色对应 A 的左上元素 1、矩阵 B 和左上输出块，其他块用蓝色；颜色不编码数值大小。块边界是数学对象的结构，无背景网格。

运行本目录的 plots.py 可导出同名 PDF、SVG 和 PNG；numpy.kron 计算的精确数据、字体校验值和尺寸保存在 sources.json。共享样式从 figures/00-shared/academic-drawing/plot_style.py 加载。无随机采样。
