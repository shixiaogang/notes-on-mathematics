# 二次型水平集的三种情形

回应第 6 章“方程和优化”中“二次型的正定性怎样从水平集形状看出来”的读者问题。三 panel 并列，解析曲线直接求值，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-quadratic-level-sets.pdf/.png/.svg` | 正定→同心椭圆（唯一极小）；半正定→平行直线槽（极小值是一整条直线）；不定→双曲线（鞍点） | 169 mm | `figure*` |

## 图中元素含义

- (a) $f=x^2+2y^2$：四层椭圆，黄点为唯一无约束极小 $(0,0)$。
- (b) $f=x^2$：水平集退化为竖直线 $x=\pm\sqrt c$（三对）；绿线为极小值集合——整条 $y$ 轴。
- (c) $f=x^2-y^2$：双曲线 $x^2-y^2=\pm1,\pm2$；红点为鞍点 $(0,0)$，沿 $x$ 方向是谷、沿 $y$ 方向是脊。

## 关键精确值

- 正定：$f>0$（$x\neq0$），极小唯一。
- 半正定：$f\ge0$，$f=0$ 取遍 $\{(0,y):y\in\mathbb R\}$。
- 不定：$f(1,0)=1>0$，$f(0,1)=-1<0$，原点既非极小也非极大。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-quadratic-level-sets/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存各 panel 的水平集取值。
