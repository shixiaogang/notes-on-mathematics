# 停止准则与噪声地板

回应第 7 章“迭代到什么时候该停、继续迭代为什么不再变准”的读者问题。固定含噪递推精确数值。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-stopping-noise-floor.pdf/.png/.svg` | 误差三段：几何下降 → 噪声地板 δ/(1−q) → 触底不再下降；标停止阈值 | 169 mm | `figure*` |

## 图中元素含义

- 递推 `e_{k+1}=0.7 e_k+0.05`，`e0=1`，k=0..30；扰动为固定常数，无随机采样。
- 红虚线为稳态地板 `δ/(1−q)=0.05/0.3≈0.167`；绿点线为停止阈值 0.20。
- 早停错过收敛段，晚停撞上地板——阈值应设在曲线刚触底的位置。

## 关键精确值

- 地板 0.1667；阈值 0.20 与曲线交点约在 k=9。逐 k 误差见 `sources.json`。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-stopping-noise-floor/plots.py
```

从任意目录运行均可，不调用 LaTeX。
