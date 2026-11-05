# 核、像与秩零度定理

回应读者问题“被映到 0 的向量（核）与实际用到的输出方向（像），维度为什么相加等于定义域维数”。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-kernel-image-rank-nullity.pdf/.png/.svg` | T:R²→R² 的核是 y 轴、像是 x 轴（1+1=2）；T:R³→R² 的核是 z 轴、像是 xy 平面（1+2=3） | 169 mm | `figure*` |

## 图中元素含义

- 左 panel：$T(x,y)=(x,0)$。红直线为 $\ker T=y$ 轴（所有被映成 0 的向量），蓝直线为 $\operatorname{im}T=x$ 轴（所有可能的输出）；样本 $v=(2,1)$（深箭头）被映到 $T(v)=(2,0)$（蓝点，虚线为投影）。
- 右 panel：$T(x,y,z)=(x,y)$。红直线为 $\ker T=z$ 轴；浅蓝平面为 $\operatorname{im}T=xy$ 平面；样本 $p=(1,1,1)$ 被映到平面上的 $(1,1,0)$（虚线）。

## 关键精确值

- 左 panel：$\dim\ker T=1$，$\dim\operatorname{im}T=1$，$1+1=2$。
- 右 panel：$\dim\ker T=1$，$\dim\operatorname{im}T=2$，$1+2=3$。
- 秩零度定理：$\dim\ker T+\dim\operatorname{im}T=\dim$ 定义域。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-kernel-image-rank-nullity/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式与精确读数。
