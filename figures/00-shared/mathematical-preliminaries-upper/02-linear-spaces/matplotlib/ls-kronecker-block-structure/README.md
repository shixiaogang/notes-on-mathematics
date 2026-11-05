# Kronecker 积块结构

回应第 5 章“运算”中“为什么 A⊗B 的每个块正好是 a_{ij} 乘 B”的读者问题。4×4 数值由 `numpy.kron` 直接求得，是教学构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-kronecker-block-structure.pdf/.png/.svg` | $A\otimes B$ 按 $A$ 的布局把 $B$ 复制四块，色深编码数值 | 112 mm | `figure` |

## 图中元素含义

- 粗线划分 2×2 块；每块是标量 $a_{ij}$ 乘以同一个 $B$；浅色到深蓝表示数值 0→4。
- 上方给出 $A$、$B$ 的取值，块角标注 $a_{ij}B$。

## 关键精确值

- $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，$B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$。
- $A\otimes B=\begin{pmatrix}1B&2B\\3B&4B\end{pmatrix}=\begin{pmatrix}1&1&2&2\\0&1&0&2\\3&3&4&4\\0&3&0&4\end{pmatrix}$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-kronecker-block-structure/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存矩阵与块积结果。
