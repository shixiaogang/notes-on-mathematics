# 行列式的有向体积

回应第 5 章“运算”中“行列式的正负号在图上标记了什么”的读者问题。平行四边形与行列式由解析式核对，是教学构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-determinant-oriented-volume.pdf/.png/.svg` | 单位正方形被 $A$ 变成平行四边形，面积为 |det A|，符号标记取向 | 169 mm | `figure*` |

## 图中元素含义

- 灰点线为原单位正方形；蓝平行四边形为像；蓝箭头 $a_1$、绿箭头 $a_2$ 是 $A$ 的两列。
- 红弧箭头：panel (a) 从 $a_1$ 扫到 $a_2$ 为逆时针，$\det A>0$；panel (b) 交换两列后翻为顺时针，$\det A<0$，面积大小不变。

## 关键精确值

- $A_+=\begin{pmatrix}1.5&0.5\\0.3&1.2\end{pmatrix}$，$\det A_+=1.5\cdot1.2-0.5\cdot0.3=1.65>0$。
- $A_-=\begin{pmatrix}0.5&1.5\\1.2&0.3\end{pmatrix}$，$\det A_-=-1.65<0$；两像面积均为 $1.65$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-determinant-oriented-volume/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存矩阵、列向量与行列式。
