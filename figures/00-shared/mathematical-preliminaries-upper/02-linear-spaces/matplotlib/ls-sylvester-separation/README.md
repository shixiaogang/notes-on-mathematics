# Sylvester 方程的特征值分离条件

回应第 6 章“方程和优化”中“Sylvester 方程 $AX+XB=C$ 什么时候对任意 $C$ 都有唯一解”的读者问题。只用一条实轴画两个实数集合的距离，不引入复数对象；解析式构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-sylvester-separation.pdf/.png/.svg` | $A$ 的特征值集合 $\{1,2\}$ 与 $-B$ 的特征值集合 $\{3,4\}$ 分居实轴两侧，间距 $\mathrm{sep}(A,-B)=1>0$，两集合不相交即可解 | 112 mm | `figure` |

## 图中元素含义

- 蓝点为 $A=\mathrm{diag}(1,2)$ 的特征值 $\{1,2\}$；绿点为 $-B$（$B=\mathrm{diag}(-3,-4)$）的特征值 $\{3,4\}$。
- 红色双向箭头标出最近的一对 $\lambda=2$ 与 $\mu=3$，间距即 $\mathrm{sep}(A,-B)=1$。

## 关键精确值

- 条件：$\sigma(A)\cap\sigma(-B)=\varnothing$，即对所有 $i,j$，$\lambda_i(A)+\mu_j(B)\neq0$。
- 本例：$\{1,2\}\cap\{3,4\}=\varnothing$，$\mathrm{sep}=|2-3|=1>0$，故 $AX+XB=C$ 对任意 $C$ 有唯一解。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-sylvester-separation/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存所有成对距离。
