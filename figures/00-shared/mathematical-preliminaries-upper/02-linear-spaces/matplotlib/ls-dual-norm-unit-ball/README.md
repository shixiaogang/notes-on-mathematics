# 对偶范数单位球

回应第 5 章“运算”中“对偶范数的单位球和原单位球是什么关系”的读者问题。交点与支撑线由解析式直接求出，是教学构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-dual-norm-unit-ball.pdf/.png/.svg` | ℓ₁ 菱形与 ℓ∞ 方盒互为对偶，支撑超平面切于对偶球 | 112 mm | `figure` |

## 图中元素含义

- 蓝色菱形为原范数 $B$（$\ell_1$），绿色虚线方盒为对偶球 $B^*$（$\ell_\infty$）。
- 蓝点 $x=(0.5,0.5)$ 在菱形边上；红线为支撑超平面 $\{z:z\cdot x=1\}$（即 $z_1+z_2=2$），恰好切到方盒顶点 $(1,1)$。

## 关键精确值

- $\ell_1$ 的对偶是 $\ell_\infty$：$\|z\|_*=\sup_{\|x\|_1\le1}z\cdot x=\|z\|_\infty$。
- 支撑线 $0.5z_1+0.5z_2=1$ 与方盒 $[-1,1]^2$ 相切于 $(1,1)$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-dual-norm-unit-ball/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式与切点。
