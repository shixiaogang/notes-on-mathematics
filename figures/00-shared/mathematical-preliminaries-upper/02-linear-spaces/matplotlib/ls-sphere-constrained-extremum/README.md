# 单位圆约束下的极值落在特征方向

回应第 6 章“方程和优化”中“为什么 $\max_{\|x\|=1}x^\top Ax$ 一定在特征方向取到”的读者问题。固定对称矩阵，特征值由精确对角化求出，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-sphere-constrained-extremum.pdf/.png/.svg` | 椭圆 $x^\top Ax=\lambda_1$ 在 $\pm v_1$ 处与单位圆相切（最大），$x^\top Ax=\lambda_2$ 在 $\pm v_2$ 处相切（最小）；子空间约束直线上也标出两个极值点 | 112 mm | `figure` |

## 图中元素含义

- $A=\begin{bmatrix}2&0.5\\0.5&1\end{bmatrix}$；灰圆为单位约束 $\|x\|=1$。
- 蓝椭圆 $x^\top Ax=\lambda_1\approx2.21$：沿 $v_1$ 方向恰为单位圆半径 1，故在 $\pm v_1$ 相切——$v_1$ 是最大方向。
- 绿椭圆 $x^\top Ax=\lambda_2\approx0.793$：在 $\pm v_2$ 处与单位圆相切——$v_2$ 是最小方向。
- 黄色虚线为子空间约束（过原点直线 $y=-0.6x$），黄点是该直线与单位圆的交点，即约束在子空间上的两个极值。

## 关键精确值

- 特征值 $\lambda_{1,2}=\dfrac{3\pm\sqrt2}{2}\approx2.207,\ 0.793$。
- $\max_{\|x\|=1}x^\top Ax=\lambda_1$，$\min=\lambda_2$（Rayleigh 商极值定理）。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-sphere-constrained-extremum/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存特征值与特征向量。
