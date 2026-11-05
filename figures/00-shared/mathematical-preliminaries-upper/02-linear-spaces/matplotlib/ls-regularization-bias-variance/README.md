# 正则化的偏差—方差权衡（L 曲线）

回应第 6 章“方程和优化”中“正则参数 λ 调大调小分别引入什么误差”的读者问题。固定 2×2 例子与固定 λ 网格，无随机采样。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-regularization-bias-variance.pdf/.png/.svg` | 左：L 曲线——参数范数小、残差大（偏差）与参数范数大、残差小（过拟合）两端；右：残差随 λ 上升、参数范数随 λ 下降 | 169 mm | `figure*` |

## 图中元素含义

- $A=\mathrm{diag}(2,1)$，$b=(4,1)$；岭回归解 $x(\lambda)=\big(\tfrac{8}{4+\lambda},\tfrac{1}{1+\lambda}\big)$。
- 左 panel：横轴 $\|x(\lambda)\|$、纵轴 $\|Ax-b\|$，黄点标出 $\lambda=0.02,1,8$；右端（λ 小）过拟合/方差大，左端（λ 大）偏差大。
- 右 panel：横轴 λ；红曲线残差 $\|Ax-b\|$ 随 λ 增大，绿曲线参数范数 $\|x(\lambda)\|$ 随 λ 减小，灰色虚线标出折衷区。

## 关键精确值

- $\lambda=0$：$x=(2,1)$，$\|x\|=\sqrt5\approx2.24$，残差 $0$。
- $\lambda=8$：$x=(2/3,1/9)$，$\|x\|\approx0.67$，残差约 $2.80$。
- λ 网格为 `linspace(0.02, 8, 41)`，固定复算。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-regularization-bias-variance/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存端点处的精确数值。
