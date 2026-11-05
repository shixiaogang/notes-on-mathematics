# Givens 旋转与 Householder 反射

回应第 6 章中“怎样用一个初等正交变换把向量打到坐标轴上”的读者问题。所有点由解析式直接求出，是教学构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-givens-householder-elimination.pdf/.png/.svg` | 左：Givens 旋转把 $(a,b)=(2,1)$ 旋到 $(r,0)$；右：Householder 反射把 $(a,b)$ 映到 $(r,0)$，反射轴为角平分线 | 169 mm | `figure*` |

## 图中元素含义

- 两幅中蓝箭头都是原向量 $(a,b)=(2,1)$，绿箭头都是像 $(r,0)$，$r=\|(a,b)\|=\sqrt5\approx2.24$。
- 左 panel：灰色点弧线标示旋转路径，旋转角 $\theta=\arctan(1/2)\approx26.6°$；Givens 矩阵 $G=\begin{bmatrix}c&s\\-s&c\end{bmatrix}$，$c=a/r$，$s=b/r$。
- 右 panel：灰色虚线为反射轴（过原点、与 $x$ 轴夹角 $\theta/2\approx13.3°$）；Householder 反射 $H=I-2vv^\top/v^\top v$，$v=(a,b)-(r,0)$。

## 关键精确值

- $r=\sqrt5\approx2.236$，$c=2/\sqrt5\approx0.894$，$s=1/\sqrt5\approx0.447$。
- $G(a,b)^\top=(r,0)$；$H(a,b)^\top=(r,0)$；$\det G=1$（旋转），$H$ 为对称正交阵（反射）。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-givens-householder-elimination/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存两个正交矩阵与角度的精确值。
