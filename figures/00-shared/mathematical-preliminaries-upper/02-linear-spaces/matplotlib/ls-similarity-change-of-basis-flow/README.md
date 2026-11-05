# 相似换基的闭环

回应读者问题“相似 $\bm B=\bm P^{-1}\bm A\bm P$ 是怎样从换基推导出来的，闭环为什么合拢”。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-similarity-change-of-basis-flow.pdf/.png/.svg` | 旧基（蓝排）与新基（绿排）四节点交换图：上边 $\bm y=\bm A\bm x$，左边 $\bm x'=\bm P^{-1}\bm x$，下边 $\bm y'=\bm B\bm x'$，右边 $\bm y=\bm P\bm y'$ | 169 mm | `figure*` |

## 图中元素含义

- 蓝排（上）：旧基下的输入坐标 $\bm x$ 与输出坐标 $\bm y=\bm A\bm x$。
- 绿排（下）：新基下的输入坐标 $\bm x'=\bm P^{-1}\bm x$ 与输出坐标 $\bm y'=\bm B\bm x'$。
- 左箭头：输入换基 $\bm P^{-1}$；右箭头：输出回换 $\bm P$（相似两端共用同一次换基）。

## 关键精确值

- 沿上边与沿“左—下—右”的路径给出同一个 $\bm y$，闭环合拢条件即 $\bm B=\bm P^{-1}\bm A\bm P$。
- 对照图 `ls-equivalence-two-sided-bases-flow`：相似是左右两侧共用 $\bm P$ 的特例。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-similarity-change-of-basis-flow/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存交换图结构与公式记录。
