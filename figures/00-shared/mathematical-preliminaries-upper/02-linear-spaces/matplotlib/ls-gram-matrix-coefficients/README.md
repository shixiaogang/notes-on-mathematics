# Gram 矩阵系数

回应第 5 章“运算”中“斜基下 Gram 矩阵到底度量了什么”的读者问题。所有向量与投影由解析式直接求出，是教学构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-gram-matrix-coefficients.pdf/.png/.svg` | $G_{ii}$ 是基向量长度平方，$G_{ij}$（$i\ne j$）是一基在另一基方向上的投影内积 | 112 mm | `figure` |

## 图中元素含义

- 蓝箭头 $b_1=(2,0)$、绿箭头 $b_2=(1,1.5)$；灰点为 $b_2$ 到 $b_1$ 轴的投影足 $(1,0)$，灰色虚线为投影线。
- $G_{11}=\langle b_1,b_1\rangle=\|b_1\|^2=4$、$G_{22}=\|b_2\|^2=3.25$ 是长度项；$G_{12}=\langle b_1,b_2\rangle=2$ 是交叉项，等于投影段长度乘以 $\|b_1\|$。

## 关键精确值

- $b_1=(2,0)$，$b_2=(1,1.5)$；$G_{11}=4$，$G_{22}=1^2+1.5^2=3.25$，$G_{12}=2\cdot1+0=2$。
- 投影足：$\frac{\langle b_1,b_2\rangle}{\langle b_1,b_1\rangle}b_1=\frac{2}{4}(2,0)=(1,0)$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-gram-matrix-coefficients/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式与精确读数。
