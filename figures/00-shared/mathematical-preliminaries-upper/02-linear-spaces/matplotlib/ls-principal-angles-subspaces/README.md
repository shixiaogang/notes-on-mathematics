# 子空间主夹角

回应第 7 章“两个过原点的子空间到底有多近、投影后还剩多少”的读者问题。固定角度三角构造，无随机采样。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-principal-angles-subspaces.pdf/.png/.svg` | 两直线子空间主夹角 θ；v 在 U 上的投影 p 与残差 `‖v‖sinθ` | 112 mm | `figure` |

## 图中元素含义

- 蓝线为 `U=span{(1,0)}`，绿线为 `V=span{v}`，`v=(cos40°,sin40°)`；红弧为主夹角 `θ=40°`。
- 黄点 `p=(v·û)û` 是 v 在 U 上的正交投影；灰色虚线为投影垂线（带直角标记）。
- 标注 `cosθ=|⟨u,v⟩|/(‖u‖‖v‖)`，`‖v‖sinθ` 为投影不掉的残差长度。

## 关键精确值

- `cos40°≈0.7660`，`sin40°≈0.6428`；`p=(0.7660, 0)`。

## 运行

```bash
python3 figures/00-shared/mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-principal-angles-subspaces/plots.py
```

从任意目录运行均可，不调用 LaTeX。`sources.json` 保存角度、投影点与残差长度。
