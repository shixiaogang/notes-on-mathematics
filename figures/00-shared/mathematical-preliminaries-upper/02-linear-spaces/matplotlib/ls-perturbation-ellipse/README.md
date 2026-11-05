# 对称矩阵微扰

回应第 7 章“对称矩阵加小扰动，特征值与特征向量会变多少”的读者问题。固定谱与固定扰动构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-perturbation-ellipse.pdf/.png/.svg` | A（实线椭圆）与 A+E（虚线椭圆）：轴微旋、半轴微变；Weyl 界与谱隙 γ | 112 mm | `figure` |

## 图中元素含义

- 椭圆 `{x: x^T M x≤1}` 的半轴长 `1/√λ`；A 的特征值 2 与 0.5，主轴方向 20°。
- `E=[[0.1,0.15],[0.15,-0.05]]`，`‖E‖₂≈0.193`；Weyl 界 `|Δλ_i|≤‖E‖₂`。
- 谱隙 `γ=λ1−λ2=1.5`：隙越大，特征向量方向越不易被微扰转动。

## 关键精确值

- `‖E‖₂≈0.1927`；`A+E` 的特征值约 2.18 与 0.37（与 A 相差 0.18、0.13，均小于 `‖E‖₂`，符合 Weyl）。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-perturbation-ellipse/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。
