# 最小二乘残差垂直于列空间

回应第 6 章“方程和优化”中“为什么最小二乘解处的残差垂直于整个列空间”的读者问题。三维透视示意，所有点由解析式直接求出，是教学构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-least-squares-residual.pdf/.png/.svg` | 列空间平面上的投影 $A\hat x$ 离 $b$ 最近，残差 $r=b-A\hat x$ 与列空间的两条列向量都垂直 | 112 mm | `figure` |

## 图中元素含义

- $A=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$，列 $a_1=(1,0,1)$（蓝箭头）、$a_2=(0,1,1)$（绿箭头），浅蓝平面即 $\mathrm{Col}(A)$。
- 蓝点 $b=(2,3,2)$；绿点 $A\hat x=a_1+2a_2=(1,2,3)$ 在平面上；红色箭头为残差 $r=b-A\hat x=(1,1,-1)$。
- 视角 elev=18°、azim=−62°，仅为看清平面与残差的透视。

## 关键精确值

- $\hat x=(1,2)$ 是最小二乘解：$A^\top r=0$ 等价于 $r\cdot a_1=0$、$r\cdot a_2=0$。
- 验证：$r\cdot a_1=1+0-1=0$，$r\cdot a_2=0+1-1=0$；$\|r\|=\sqrt3\approx1.73$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-least-squares-residual/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存点坐标与内积验证。
