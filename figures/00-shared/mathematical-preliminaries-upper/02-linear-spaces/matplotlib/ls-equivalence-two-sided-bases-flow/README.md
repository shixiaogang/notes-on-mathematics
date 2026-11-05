# 相抵两端换基的闭环

回应读者问题“相抵 $\bm B=\bm Q^{-1}\bm A\bm P$ 的两次换基为什么彼此独立、闭环怎样合拢”。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-equivalence-two-sided-bases-flow.pdf/.png/.svg` | 两端各自选基的四节点交换图：上边 $\bm y=\bm A\bm x$，左边输入换基 $\bm P^{-1}$，下边 $\bm y'=\bm B\bm x'$，右边输出回换 $\bm Q$ | 169 mm | `figure*` |

## 图中元素含义

- 蓝排（上）：输入、输出在旧坐标下的记录 $\bm x$ 与 $\bm y=\bm A\bm x$。
- 绿排（下）：输入端新坐标 $\bm x'=\bm P^{-1}\bm x$、输出端新坐标 $\bm y'=\bm B\bm x'$。
- 左箭头：输入换基 $\bm P^{-1}$（$\bm P$ 为 $d\times d$ 可逆矩阵）；右箭头：输出回换 $\bm Q$（$\bm Q$ 为 $m\times m$ 可逆矩阵）；二者彼此独立。

## 关键精确值

- 闭环合拢条件即 $\bm B=\bm Q^{-1}\bm A\bm P$。
- 与 `ls-similarity-change-of-basis-flow` 对照：相似两端共用 $\bm P$，相抵两端各自取独立的 $\bm P$ 与 $\bm Q$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-equivalence-two-sided-bases-flow/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存交换图结构与公式记录。
