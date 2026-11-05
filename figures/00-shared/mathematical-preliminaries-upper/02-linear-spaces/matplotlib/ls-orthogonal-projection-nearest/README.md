# 子空间最近点：正交投影

回应第 6 章“方程和优化”中“子空间上离给定点最近的点为什么是正交投影”的读者问题。所有点由解析式直接求出，是教学构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-orthogonal-projection-nearest.pdf/.png/.svg` | 直线子空间 $U$ 上离点 $y$ 最近的点是正交投影 $P_Uy$，误差 $y-P_Uy$ 垂直于 $U$；非正交候选点距离更长 | 112 mm | `figure` |

## 图中元素含义

- 蓝线为子空间 $U$（过原点、方向 $d=(2,1)$ 的直线）；蓝点为给定点 $y=(1,3)$。
- 绿点 $P_Uy=(2,1)$ 在 $U$ 上；绿色箭头为误差 $y-P_Uy=(-1,2)$，直角小方块表示它与 $U$ 垂直。
- 黄点 $Q=(4,2)$ 是 $U$ 上另一个候选点；黄色虚线是 $y$ 到 $Q$ 的距离，明显长于绿色误差线段。

## 关键精确值

- $P_Uy=\dfrac{y\cdot d}{d\cdot d}d=\dfrac{2+3}{5}(2,1)=(2,1)$；误差 $(-1,2)$ 与 $d=(2,1)$ 的内积为 $0$。
- $\|y-P_Uy\|=\sqrt5\approx2.24$（最短）；$\|y-Q\|=\sqrt{10}\approx3.16$。
- 结论：投影定理——子空间上最近点唯一，且连接向量与子空间正交。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-orthogonal-projection-nearest/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式与精确读数。
