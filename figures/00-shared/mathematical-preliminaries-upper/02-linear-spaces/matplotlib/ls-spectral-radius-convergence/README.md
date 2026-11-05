# 谱半径决定收敛

回应第 7 章“为什么迭代收敛当且仅当 ρ(T)<1”的读者问题。三个固定标量迭代矩阵在 k=0..20 上的精确误差曲线。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-spectral-radius-convergence.pdf/.png/.svg` | ρ=0.5 快收敛、ρ=0.9 慢收敛、ρ=1.1 发散，半对数坐标下为三条直线 | 169 mm | `figure*` |

## 图中元素含义

- 递推 `e_{k+1}=Te_k`，`‖e0‖=1`；正规 T=ρI 时 `‖e_k‖=ρ^k`。
- 蓝线 ρ=0.5 约 14 步降到 1e-4；绿线 ρ=0.9 只缓慢下降；红线 ρ=1.1 指数上升。

## 关键精确值

- `‖e_k‖=ρ^k`，k=0..20，逐点值见 `sources.json`。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-spectral-radius-convergence/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。
