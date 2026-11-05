# 对偶基怎样把读取坐标分离

回应读者问题“对偶基怎样把线性泛函对各基向量的读数分离开”。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-dual-basis-readout.pdf/.png/.svg` | 基 $b_1,b_2$、对偶基 $b^1,b^2$、泛函 $\ell(x)=x\cdot a$ 的等值线，以及 $a=2b^1-b^2$ | 112 mm | `figure` |

## 图中元素含义

- 蓝箭头 $b_1=(2,1)$、绿箭头 $b_2=(-1,1)$；红色虚线箭头为对偶基 $b^1=(1/3,1/3)$、$b^2=(-1/3,2/3)$。
- 黄色箭头 $a=(1,0)$；灰色虚线为等值线 $\ell(x)=x\cdot a=c$，即竖直线 $x=c$：$c=-1,0,2$。$b_1$ 落在 $c=2$ 线上，$b_2$ 落在 $c=-1$ 线上。

## 关键精确值

- 对偶条件 $b^i\cdot b_j=\delta^i_j$ 解得：$b^1=(1/3,1/3)$，$b^2=(-1/3,2/3)$。
- $\ell(b_1)=a\cdot b_1=2$，$\ell(b_2)=a\cdot b_2=-1$。
- 分解验证：$a=\ell(b_1)b^1+\ell(b_2)b^2=2b^1-b^2=2(1/3,1/3)-(-1/3,2/3)=(1,0)$。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-dual-basis-readout/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存解析式、对偶向量与验证值。
