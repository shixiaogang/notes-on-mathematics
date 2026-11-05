# 范数单位球

回应第 5 章“运算”中“单位向量为什么依赖范数”的读者问题。所有单位球与交点由解析式直接求出，是教学构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-norm-unit-balls.pdf/.png/.svg` | 同一条射线方向上，四种范数的“单位向量”落点不同 | 169 mm | `figure*` |

## 图中元素含义

- 四个 panel 依次为 $\ell_1$ 菱形、$\ell_2$ 单位圆、$\ell_\infty$ 方盒、加权 $M$-范数椭圆 $x^2/4+y^2/0.64=1$。
- 灰色虚线为公共射线 $(1,1)$ 方向；黄点为该射线与单位球的交点，即该范数下的“单位向量”，落点随范数移动。

## 关键精确值

- 交点：$\ell_1$ 为 $(0.5,0.5)$；$\ell_2$ 为 $(1/\sqrt2,1/\sqrt2)\approx(0.71,0.71)$；$\ell_\infty$ 为 $(1,1)$；椭圆交点 $\approx(0.74,0.74)$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-norm-unit-balls/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式与交点数值。
