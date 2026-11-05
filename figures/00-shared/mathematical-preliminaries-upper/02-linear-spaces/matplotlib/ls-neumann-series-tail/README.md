# Neumann 级数尾界

回应第 7 章“Neumann 级数截断后误差有多大、尾界紧不紧”的读者问题。固定 2×2 例精确部分和。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-neumann-series-tail.pdf/.png/.svg` | 尾界 `q^{n+1}/(1−q)`（红虚线）与真实残差（蓝线）随 n 几何衰减 | 112 mm | `figure` |

## 图中元素含义

- `T=[[0.7,0.6],[0,0.1]]`，`q=‖T‖₂≈0.92<1`；`(I−T)^{-1}=Σ T^k`。
- 真实残差 `R_n=(I−T)^{-1}−S_n=T^{n+1}(I−T)^{-1}`；尾界 `‖R_n‖≤q^{n+1}/(1−q)`。
- n=0..15，半对数纵轴。

## 关键精确值

- `q≈0.9243`；残差从 n=0 的 3.22 降到 n=15 的 0.016，尾界在其上方保持同斜率。逐点值见 `sources.json`。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-neumann-series-tail/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。
