# 第三章“偏微分方程”图像

正文：`tex/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/03-partial-differential-equations/`。

## 重放

```sh
python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch3.py [函数名 ...]
python3 figures/00-shared/academic-drawing/render_tikz.py figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/tikz/pde-domain-boundary/figure.tex
```

Matplotlib 生成器需要 numpy 与 matplotlib，复用 `figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py` 的字体与色板；不使用随机数。每幅图的 `figure.json` 记录解析式、级数项数、格式与关键数值。

## 图目录

| 图 | 方法 | 生成函数 | 正文位置 |
|---|---|---|---|
| `pde-rod-snapshots` | Matplotlib | `rod_snapshots` | 3.1.1 一根细棒上的温度 |
| `pde-three-mechanisms` | Matplotlib | `three_mechanisms` | 3.1.1 三种变化机制 |
| `pde-domain-boundary` | TikZ | — | 3.1.2 边界上规定什么 |
| `pde-boundary-conditions` | Matplotlib | `boundary_conditions` | 3.1.2 例：左端点三种边界条件 |
| `pde-weak-form-test` | Matplotlib | `weak_form_test` | 3.2.1 用测试函数检验方程 |
| `pde-poisson-energy` | Matplotlib | `poisson_energy` | 3.2.1 Green函数与能量极小 |
| `pde-neumann` | Matplotlib | `neumann` | 3.2.3 相容条件与常数方向 |
| `pde-heat-modes` | Matplotlib | `heat_modes` | 3.3.1 模式衰减 |
| `pde-heat-heatmap` | Matplotlib | `heat_heatmap` | 3.3.1 常量模式；3.3.3 长期行为 |
| `pde-heat-energy-max` | Matplotlib | `heat_energy_max` | 3.3.3 能量、热量与最大值原理 |
| `pde-characteristics` | Matplotlib | `characteristics` | 3.4.1 特征线 |
| `pde-transport-vs-continuity` | Matplotlib | `transport_vs_continuity` | 3.4.2 搬运数值与搬运质量 |
| `pde-burgers` | Matplotlib | `burgers` | 3.4.2 特征线交叉与激波 |
| `pde-dalembert` | Matplotlib | `dalembert` | 3.5.1 d'Alembert公式与传播速度 |
| `pde-standing-waves` | Matplotlib | `standing_waves` | 3.5.1 驻波 |
| `pde-energy-compare` | Matplotlib | `energy_compare` | 3.5.2 阻尼与耗散 |
| `pde-fd-stencil-sparsity` | Matplotlib | `fd_stencil_sparsity` | 3.6.1 网格方程与稀疏结构 |
| `pde-fem-hats` | Matplotlib | `fem_hats` | 3.6.2 帽函数与Galerkin解 |
| `pde-convergence` | Matplotlib | `convergence` | 3.6.1、3.6.2 收敛阶 |
| `pde-explicit-stability` | Matplotlib | `explicit_stability` | 3.6.3 扩散步长条件 |
| `pde-error-plateau` | Matplotlib | `error_plateau` | 3.6.3 误差分配 |

正文引用宽度：单栏图 100–107mm（与导出宽度一致，不缩放）；`pde-three-mechanisms`、`pde-fd-stencil-sparsity`、`pde-explicit-stability` 为 150mm 跨栏图；`pde-domain-boundary` 为 124.5mm 跨栏图。
