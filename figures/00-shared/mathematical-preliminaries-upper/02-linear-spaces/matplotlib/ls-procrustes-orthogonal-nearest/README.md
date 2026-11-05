# 正交 Procrustes：最优旋转贴合两组点

回应第 6 章“方程和优化”中“两组点之间的最优正交映射为什么是旋转而不是反射”的读者问题。固定点集与旋转角，解析式构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-procrustes-orthogonal-nearest.pdf/.png/.svg` | 蓝三角形 $\{x_i\}$ 经最优旋转 $R$（45°，$\det R=+1$）贴到绿三角形 $\{y_i\}$；黄色虚线三角形是反射备选（$\det=-1$），距离更大 | 112 mm | `figure` |

## 图中元素含义

- 点集 $X=\{(1.2,0),(0,1),(-1,0.3)\}$（蓝三角形）。
- 绿三角形为 $Y=RX$，$R=\frac{\sqrt2}{2}\begin{bmatrix}1&-1\\1&1\end{bmatrix}$（45° 旋转，$\det R=+1$）；灰点线为对应点之间的连线。
- 黄虚线三角形为反射备选 $\mathrm{diag}(1,-1)X$（$\det=-1$），各点到目标的距离明显更大，不是最优。

## 关键精确值

- $\det R=+1$；反射备选行列式为 $-1$。
- 最优解 $R^*=UV^\top$（$X^\top Y$ 的 SVD）：本图中即 45° 旋转；若最优解落在反射分支上则距离会变大。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-procrustes-orthogonal-nearest/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存点坐标与矩阵行列式。
