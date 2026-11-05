"""第5章 5.3：高斯核 RKHS 中的观测投影、余项与幂函数。

核 K(x,z)=exp(-(x-z)^2/(2*0.15^2))，区间 [0,1]。
目标 f = K_{0.2} - 0.8 K_{0.5} + 0.9 K_{0.8}（属于 H_K）；观测点 Z={0.1,0.35,0.6,0.9}。
求 G a = b（b_i=f(x_i)）得投影 Pf=sum a_j K_{x_j}；余项 r=f-Pf。
幂函数 P_Z(t)=sqrt(K(t,t)-k_Z(t)^T G^{-1} k_Z(t))，满足 |r(t)|<=P_Z(t)||r||_H。
输出：data.dat（t f Pf r）到本目录，power.dat（t PZ absr bound）到 ../c5-power-function/。
运行：python3 generate.py
"""
import math
from pathlib import Path

here = Path(__file__).resolve().parent
sigma = 0.15
centers_f = [0.2, 0.5, 0.8]
coef_f = [1.0, -0.8, 0.9]
Z = [0.1, 0.35, 0.6, 0.9]


def K(x, z):
    return math.exp(-(x - z) ** 2 / (2 * sigma ** 2))


def solve(A, b):
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c:
                fac = M[r][c] / M[c][c]
                for k in range(c, n + 1):
                    M[r][k] -= fac * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]


def f(t):
    return sum(c * K(t, x) for c, x in zip(coef_f, centers_f))


G = [[K(x, z) for z in Z] for x in Z]
b = [f(x) for x in Z]
a = solve(G, b)


def Pf(t):
    return sum(aj * K(t, xj) for aj, xj in zip(a, Z))


norm_f2 = sum(ci * cj * K(xi, xj) for ci, xi in zip(coef_f, centers_f) for cj, xj in zip(coef_f, centers_f))
norm_Pf2 = sum(ai * bi for ai, bi in zip(a, b))
norm_r = math.sqrt(norm_f2 - norm_Pf2)
print("b =", [round(v, 4) for v in b])
print("a =", [round(v, 4) for v in a])
print("||f||^2 =", round(norm_f2, 4), " ||Pf||^2 =", round(norm_Pf2, 4), " ||r|| =", round(norm_r, 4))


def power(t):
    k = [K(t, x) for x in Z]
    c = solve(G, k)
    v = K(t, t) - sum(ci * ki for ci, ki in zip(c, k))
    return math.sqrt(max(v, 0.0))


ts = [i / 200 for i in range(201)]
with open(here / "data.dat", "w") as out:
    out.write("t f Pf r\n")
    for t in ts:
        out.write(f"{t:.4f} {f(t):.5f} {Pf(t):.5f} {f(t) - Pf(t):.5f}\n")
mx = 0
with open(here.parent / "c5-power-function" / "power.dat", "w") as out:
    out.write("t PZ absr bound\n")
    for t in ts:
        p = power(t)
        r = abs(f(t) - Pf(t))
        assert r <= p * norm_r + 1e-9
        mx = max(mx, r)
        out.write(f"{t:.4f} {p:.5f} {r:.5f} {p * norm_r:.5f}\n")
print("max |r| =", round(mx, 4), " max P_Z =", round(max(power(t) for t in ts), 4))
print("f(0.25), Pf(0.25):", round(f(0.25), 4), round(Pf(0.25), 4))
