# 非正规矩阵的瞬态放大

回应第 7 章“ρ(J)=0.5<1，为什么 ‖J^k‖ 不单调下降”的读者问题。聚焦 Jordan 块本身的可复算曲线，与旧图 `ch06-transient-growth`（连乘瞬态）叙事不重复。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-nonnormal-power-transient.pdf/.png/.svg` | 非正规 Jordan 块 `‖J^k‖` 先升到峰值 1.207（k=1）再衰减，正规对照 `ρ^k` 单调下降 | 169 mm | `figure*` |

## 图中元素含义

- `J=[[0.5,1],[0,0.5]]=λI+N`，`J^k=λ^k I+k λ^{k-1}N`；k=0..25 精确计算 `‖J^k‖₂`。
- 黄点为峰值 `‖J^1‖₂≈1.207`；红虚线为正规对照 `0.5^k`。
- 旁注：`ρ(J)=0.5<1`，但范数先升后降——谱半径小于 1 不能排除先放大。

## 关键精确值

- 峰值位置 k=1，峰值 1.2071；k=0 为 1.0。逐 k 范数见 `sources.json`。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-nonnormal-power-transient/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。
