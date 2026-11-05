"""第12章（本部分第5章）图 c5-kaczmarz-projection-path 的数据。

贯穿例 A=[[4,1],[1,3]]，b=(1,2)，x0=0，循环顺序 1,2,1,2,...
每步 x <- x + (b_i - a_i^T x)/||a_i||^2 a_i，用有理数精确计算前 6 步，
输出 path.dat（x_0..x_6）。精确解 x*=(1/11,7/11)。
只用标准库；从任意目录运行：python3 data.py
"""
from fractions import Fraction as F
from pathlib import Path
import math

HERE = Path(__file__).resolve().parent
A = [[F(4), F(1)], [F(1), F(3)]]
b = [F(1), F(2)]
XS = [F(1, 11), F(7, 11)]
x = [F(0), F(0)]
path = [x]
for k in range(6):
    i = k % 2
    a = A[i]
    t = (b[i] - a[0] * x[0] - a[1] * x[1]) / (a[0] ** 2 + a[1] ** 2)
    x = [x[0] + t * a[0], x[1] + t * a[1]]
    path.append(x)
    print(k + 1, "row", i + 1, "t =", t, "x =", [str(v) for v in x],
          f"err={math.hypot(float(x[0]-XS[0]), float(x[1]-XS[1])):.4f}")
with (HERE / "path.dat").open("w") as f:
    f.write("x1 x2\n")
    for p in path:
        f.write(f"{float(p[0]):.6f} {float(p[1]):.6f}\n")
