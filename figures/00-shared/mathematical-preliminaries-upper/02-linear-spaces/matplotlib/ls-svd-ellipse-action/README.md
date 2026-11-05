# 最小二乘的行图像与列图像

回应第 6 章“方程和优化”中“最小二乘解 $\hat x$ 在自变量空间与像空间分别是什么位置”的读者问题。本图刻意与 tikz 旧图 `matrix-analysis-svd-geometry`（单位圆→椭圆的奇异值几何）互补：这里从行图像与列图像两侧看最小二乘解。所有曲线由解析式直接求出，是教学构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-svd-ellipse-action.pdf/.png/.svg` | 左：两条方程直线交于 $\hat x=(1,1)$，残差二次型的水平集是以 $\hat x$ 为中心的同心椭圆；右：$b=a_1+a_2$ 恰落在列空间内，残差为零 | 169 mm | `figure*` |

## 图中元素含义

- $A=\begin{bmatrix}2&1\\0.5&1.5\end{bmatrix}$，$b=(3,2)$。因 $A$ 可逆，恰有解 $\hat x=(1,1)$。
- 左 panel（行图像）：蓝线 $2x_1+x_2=3$、绿线 $0.5x_1+1.5x_2=2$；灰色点线是 $f(x)=\|Ax-b\|^2=(x-\hat x)^\top A^\top A(x-\hat x)$ 的水平集 $f(x)=c$，中心即交点 $\hat x$。
- 右 panel（列图像）：蓝箭头 $a_1=(2,0.5)$、绿箭头 $a_2=(1,1.5)$；浅蓝平行四边形张成列空间；黄点 $b=a_1+a_2=(3,2)$，残差 $r=b-A\hat x=0$。

## 关键精确值

- $A\hat x=A(1,1)=(3,2)=b$，故残差为 $0$。
- $A^\top A=\begin{bmatrix}4.25&2.5\\2.5&3.25\end{bmatrix}$，特征值约 $6.30$ 与 $1.20$，决定水平椭圆的轴比。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-svd-ellipse-action/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存 $A^\top A$ 的精确分解与椭圆水平集。
