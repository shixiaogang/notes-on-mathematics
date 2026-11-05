# 诱导范数作用

回应第 5 章“运算”中“诱导范数 ‖A‖₂ 在几何上到底量什么”的读者问题。椭圆与奇异值由解析式核对，是教学构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-induced-norm-action.pdf/.png/.svg` | 单位圆被 $A$ 拉成椭圆，最长半轴即 ‖A‖₂=σmax | 169 mm | `figure*` |

## 图中元素含义

- 左 panel：单位圆 $\{x:\|x\|_2=1\}$ 与使 $\|Ax\|$ 最大的方向 $x^*$。
- 右 panel：$A$ 映射出的椭圆 $\{Ax:\|x\|_2=1\}$；红箭头为 $Ax^*$，其长度就是诱导范数 $\|A\|_2=\sigma_{max}$。

## 关键精确值

- $A=\begin{pmatrix}2&1\\0&1\end{pmatrix}$；$A^\top A=\begin{pmatrix}4&2\\2&2\end{pmatrix}$，特征值 $3\pm\sqrt5$。
- $\sigma_{max}=\sqrt{3+\sqrt5}\approx2.29$，$\sigma_{min}=\sqrt{3-\sqrt5}\approx0.87$；最优方向 $\propto(1,0.618)$，$Ax^*\approx(2.23,0.53)$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-induced-norm-action/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式与数值核对。
