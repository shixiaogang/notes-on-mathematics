# 线性组合张成

回应第 4 章“表示”中“线性组合能到达多大范围”的读者问题。所有点由解析式直接求出，是教学构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-linear-combination-span.pdf/.png/.svg` | 两个不共线向量的组合张成整个平面；只有一个方向的组合只停在一条直线上 | 169 mm | `figure*` |

## 图中元素含义

- 左 panel：$u=(2,1)$（蓝箭头）、$v=(1,2)$（绿箭头）；浅蓝平行四边形为 $0,u,u+v,v$；灰点是格点 $c_1u+c_2v$（$c_1,c_2\in\{-1,0,1\}$）；黄点为 $u+v=(3,3)$。
- 右 panel：红线为 $\operatorname{span}\{u\}=\{cu:c\in\mathbb R\}$，红点为 $-u,u,2u$；绿点 $v=(1,2)$ 不在这条直线上，说明仅靠 $u$ 到不了 $v$。

## 关键精确值

- $u=(2,1)$，$v=(1,2)$；$u+v=(3,3)$，$u-v=(1,-1)$。
- $v$ 不在 $\operatorname{span}\{u\}$ 上：直线 $cu$ 满足 $y=x/2$，而 $v$ 的 $y=2\neq 0.5$。
- 结论：两个不共线方向的组合 $\{c_1u+c_2v\}$ 取遍整个平面；单个方向的组合只是过原点的一条直线。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-linear-combination-span/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式、格点与精确读数。
