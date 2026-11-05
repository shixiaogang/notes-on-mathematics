# CG 与 GMRES 的搜索空间

回应第 7 章“CG 和 GMRES 各自在什么空间里找解、为什么步数有上界”的读者问题。固定二次目标与固定 Krylov 仿射空间构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-cg-gmres-search-spaces.pdf/.png/.svg` | 左：CG 沿 D-共轭方向两步到达极小点；右：GMRES 在仿射空间 x0+K_k 上最小化残差 | 169 mm | `figure*` |

## 图中元素含义

- 左 panel：`f(x)=x^T D x`，D=diag(4,1)，等高线为椭圆；`x0=(1.3,-1)`，两步精确线搜索到原点。
- 右 panel：同心圆为残差范数 `‖r‖`；绿线为 `K_1=x0+span{r0}`，绿点 `x_1` 是原点到直线的垂足（K₁ 上残差最小点）；原点墨点为解 x（残差为零）；二维下 `K_2=R²`，两步内残差可取 0。

## 关键精确值

- CG：`x1≈(-0.036,-0.743)`，`x2≈0`（浮点误差内）。
- GMRES：`x_1≈(0.833,-0.263)`，残差范数≈0.874。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-cg-gmres-search-spaces/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。
