# 与全 1 向量的缩约

与当前正文的矩阵行和解释一致。正文宽度 112 mm、导出高度 51 mm，主体字号为 8 pt。

$A=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}$，$\mathbf1=(1,1)^\top$，
$c_i=\sum_{j=1}^2 A_{ij}1_j$，得到 $c=(3,7,11)^\top$。

列索引 j 被消去，行索引 i 保留，每行对应一个输出。蓝色突出第二行和输出 7，绿色表示全 1 向量。颜色不编码数值大小，无背景网格。

运行本目录的 plots.py 可导出同名 PDF、SVG 和 PNG；numpy.einsum 的精确输入输出、字体校验值和尺寸保存在 sources.json。共享样式从 figures/00-shared/academic-drawing/plot_style.py 加载。无随机采样。
