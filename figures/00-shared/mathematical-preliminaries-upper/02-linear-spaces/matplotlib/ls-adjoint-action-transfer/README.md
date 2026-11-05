# 伴随的作用转移

回应第 5 章“运算”中“伴随矩阵把内积里的作用搬到了哪里”的读者问题。本图为关系示意，不涉及数值计算。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-adjoint-action-transfer.pdf/.png/.svg` | $\langle Ax,y\rangle=\langle x,A^\top y\rangle$ 的两条作用路径 | 112 mm | `figure` |

## 图中元素含义

- 左方框 $V$、右方框 $W$；$x\in V$、$y\in W$。
- 蓝路径：先对 $x$ 作用 $A$ 得 $Ax\in W$，再与 $y$ 取内积；绿路径：先对 $y$ 作用 $A^\top$ 得 $A^\top y\in V$，再与 $x$ 取内积；两路径恒等。

## 关键精确值

- 恒等式：$\langle Ax,y\rangle_W=\langle x,A^\top y\rangle_V$ 对一切 $x\in V,y\in W$ 成立。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-adjoint-action-transfer/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 记录构图参数。
