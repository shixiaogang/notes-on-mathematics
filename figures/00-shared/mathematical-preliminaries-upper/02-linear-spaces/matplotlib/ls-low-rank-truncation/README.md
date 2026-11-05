# 低秩截断（秩一近似）的几何与误差

回应第 6 章“方程和优化”中“截断小奇异值在几何上把椭圆变成了什么”的读者问题。固定对称矩阵，SVD 由精确对角化求出，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-low-rank-truncation.pdf/.png/.svg` | 左：单位圆经 $A$ 变成椭圆，秩一近似把它压扁成主轴方向的一条线段；右：奇异值条形图，保留 $\sigma_1$、舍弃 $\sigma_2$ | 169 mm | `figure*` |

## 图中元素含义

- $A=\begin{bmatrix}2&0.5\\0.5&1\end{bmatrix}$；灰圆为单位圆，蓝椭圆为 $A$ 作用后的像。
- 黄粗线段为秩一近似 $A_1=\sigma_1v_1v_1^\top$ 的像：单位圆被压成长度 $2\sigma_1$ 的线段，误差即椭圆与线段之差。
- 右 panel：$\sigma_1\approx2.21$（保留，蓝）、$\sigma_2\approx0.79$（舍弃，灰），算子范数误差 $\|A-A_1\|_2=\sigma_2$。

## 关键精确值

- $\sigma_1=\dfrac{3+\sqrt2}{2}\approx2.207$，$\sigma_2=\dfrac{3-\sqrt2}{2}\approx0.793$。
- $\|A-A_1\|_2=\sigma_2\approx0.793$，即截断后仍有的最大方向误差。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-low-rank-truncation/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存奇异值与误差。
