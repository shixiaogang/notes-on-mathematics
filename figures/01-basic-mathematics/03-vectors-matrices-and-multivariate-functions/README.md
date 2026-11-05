# 卷一第3部分“向量、矩阵与多元函数”图像

本目录保存第3部分独用的图像。现有图都属于第12章“线性方程与矩阵方程”，图名前缀 `c5-` 表示本部分第5章。图中数值来自正文算例或解析式，已按正文复算。本部分其余图仍位于 `figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/`。

TikZ 图每幅一个目录，`figure.tex` 为可编辑图源；在项目根目录运行下面的命令，导出 `figure.pdf/png/svg` 与 `figure.render.json`：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/01-basic-mathematics/03-vectors-matrices-and-multivariate-functions/tikz/<图名>/figure.tex
```

`c5-cg-steepest-descent-paths/data.py` 与 `c5-kaczmarz-projection-path/data.py` 只用标准库，以有理数计算迭代点，并写出图源读入的数据文件。

Matplotlib 图的目录中，`plots.py` 使用 `figures/00-shared/academic-drawing/plot_style.py`，在目录内运行 `python plots.py` 即可重新导出。依赖 Matplotlib 与 NumPy。

| 图名 | 方法 | 引用位置（05-linear-matrix-equations/） | 物理尺寸（mm） |
| --- | --- | --- | --- |
| `c5-triangular-substitution-order` | TikZ | 02-direct-factorizations.tex（LU：前代与回代的依赖） | 109.100×44.383 |
| `c5-block-elimination-schur` | TikZ | 02-direct-factorizations.tex（分块消元到Schur补系统） | 99.547×36.551 |
| `c5-householder-reflection` | TikZ | 03-orthogonal-direct-methods.tex（Householder反射的几何） | 98.940×49.195 |
| `c5-svd-solve-coordinates` | TikZ | 03-orthogonal-direct-methods.tex（SVD求解的坐标变换） | 95.652×41.109 |
| `c5-stationary-iteration-paths` | Matplotlib | 04-stationary-iterations.tex（定常迭代的轨迹与误差） | 108×54 |
| `c5-cg-steepest-descent-paths` | TikZ | 05-krylov-methods.tex（CG与最速下降的路径） | 72.873×64.897 |
| `c5-arnoldi-relation-shapes` | TikZ | 05-krylov-methods.tex（Arnoldi关系的矩阵形状） | 89.098×38.555 |
| `c5-golub-kahan-bidiagonal` | TikZ | 06-krylov-least-squares.tex（Golub--Kahan双对角化） | 109.343×80.913 |
| `c5-preconditioned-spectrum` | Matplotlib | 06-krylov-least-squares.tex（对角预条件前后的特征值） | 100×34 |
| `c5-kaczmarz-projection-path` | TikZ | 07-row-projection-methods.tex（Kaczmarz的投影路径） | 44.810×64.830 |
| `c5-ridge-tsvd-filter-factors` | Matplotlib | 09-regularization.tex（岭回归与截断SVD的滤波因子） | 112×60 |
| `c5-bartels-stewart-column-order` | TikZ | 11-matrix-equations.tex（Bartels--Stewart的逐列求解顺序） | 109.626×41.099 |
