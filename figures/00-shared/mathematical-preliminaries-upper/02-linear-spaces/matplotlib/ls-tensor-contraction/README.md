# 张量缩约

回应第 5 章“运算”中“缩约消去哪些槽位、怎样配对相加”的读者问题。2×2×2 数值与求和由解析式直接求出，是教学构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-tensor-contraction.pdf/.png/.svg` | 沿槽位 $(i,j)$ 把 $T[i,i,k]$ 配对求和，消去两个槽位 | 112 mm | `figure` |

## 图中元素含义

- 两个 $k$ 切片各为 2×2；黄色红框格为对角槽位 $T[i,i,k]$，红箭头把同一切片内两个对角格求和为 $C_k$。
- 非对角槽位不参与；结果 $C=(C_0,C_1)$ 是保留槽 $k$ 上的向量。

## 关键精确值

- $T[:,:,0]=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，$T[:,:,1]=\begin{pmatrix}5&6\\7&8\end{pmatrix}$。
- $C_0=T[0,0,0]+T[1,1,0]=1+4=5$；$C_1=5+8=13$，即 $C=(5,13)$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-tensor-contraction/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存切片数值与求和结果。
