# 商空间的等价类

回应读者问题“商空间 $V/N$ 到底是由哪些对象组成的”。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-quotient-equivalence-classes.pdf/.png/.svg` | 平面 $V$、子空间 $N$（x 轴）、三条平行于 $N$ 的等价类 $x+N$；商空间是这些平行线的集合 | 112 mm | `figure` |

## 图中元素含义

- 蓝线 $0+N=N$（x 轴）；绿线 $p_1+N$（$y=1$）、黄线 $p_2+N$（$y=2$）、红虚线 $p_3+N$（$y=-1$），每条都是一整条等价类。
- 绿线上两个点（实点 $p_1=(0.3,1)$、空心点 $(2.1,1)$）之间的双向箭头说明：同一平行线上任意两点之差属于 $N$，因此彼此等价。

## 关键精确值

- $N=\{(x,0)\}$；等价类 $p+N=\{(x,p_y)\}$。
- $(0.3,1)$ 与 $(2.1,1)$ 之差为 $(1.8,0)\in N$，故属同一类。
- 商空间 $V/N=\{x+N:x\in V\}$：每条平行线被当成商空间里的一个点。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-quotient-equivalence-classes/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式与代表点坐标。
