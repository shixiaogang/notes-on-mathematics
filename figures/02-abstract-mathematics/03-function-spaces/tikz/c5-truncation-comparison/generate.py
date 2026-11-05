"""第5章 5.4.3：最小值核 K(x,z)=min(x,z)（[0,1]、Lebesgue 测度）下谱截断与中心投影的比较。

特征对：lambda_j=1/omega_j^2，psi_j=sqrt2 sin(omega_j x)，omega_j=(j-1/2)pi。
目标 f=4x(1-x)（f(0)=0，||f||_H^2=||f'||^2=16/3）。谱系数解析式
  b_j = 4 sqrt2 (2/omega^3 - s/omega^2)，s=sin(omega_j)=(-1)^(j+1)。
谱截断 f_3=sum_{j<=3} b_j psi_j；中心 Z={1/3,2/3,1} 的投影 = 过 (0,0) 与各中心读数的分段线性插值。
对角余项：R_3(x)=x-sum_{j<=3} lambda_j psi_j(x)^2；P_Z(x)^2=(x-x_{k-1})(x_k-x)/h（x_0=0）。
输出 data.dat：x f f3 Pf R3 PZ2；打印各种误差。运行：python3 generate.py
"""
import math
from pathlib import Path

here = Path(__file__).resolve().parent
m = 3
J = 4000  # 计算尾和所用项数


def omega(j):
    return (j - 0.5) * math.pi


def b(j):
    w = omega(j)
    s = (-1) ** (j + 1)
    return 4 * math.sqrt(2) * (2 / w ** 3 - s / w ** 2)


def f(x):
    return 4 * x * (1 - x)


def f3(x):
    return sum(b(j) * math.sqrt(2) * math.sin(omega(j) * x) for j in range(1, m + 1))


Z = [0.0, 1 / 3, 2 / 3, 1.0]


def Pf(x):
    for k in range(1, 4):
        if x <= Z[k] + 1e-12:
            x0, x1 = Z[k - 1], Z[k]
            return f(x0) + (f(x1) - f(x0)) * (x - x0) / (x1 - x0)
    return f(1.0)


def R3(x):
    return x - sum(2 * math.sin(omega(j) * x) ** 2 / omega(j) ** 2 for j in range(1, m + 1))


def PZ2(x):
    for k in range(1, 4):
        if x <= Z[k] + 1e-12:
            x0, x1 = Z[k - 1], Z[k]
            return (x - x0) * (x1 - x) / (x1 - x0)
    return 0.0


print("check ||f||_H^2 = sum b_j^2 omega_j^2:", sum(b(j) ** 2 * omega(j) ** 2 for j in range(1, J)), "vs", 16 / 3)
print("check ||f||_L2^2 = sum b_j^2:", sum(b(j) ** 2 for j in range(1, J)), "vs", 8 / 15)
print("b_1..b_5:", [round(b(j), 5) for j in range(1, 6)])
# 尾和用精确总和减去前 m 项：||f||_L2^2=8/15，||f||_H^2=16/3
l2tail = 8 / 15 - sum(b(j) ** 2 for j in range(1, m + 1))
htail = 16 / 3 - sum(b(j) ** 2 * omega(j) ** 2 for j in range(1, m + 1))
print("spectral: ||f-f3||_L2 =", math.sqrt(l2tail), " ||f-f3||_H =", math.sqrt(htail))
N = 20000
xs = [(i + 0.5) / N for i in range(N)]
l2P = math.sqrt(sum((f(x) - Pf(x)) ** 2 for x in xs) / N)
hP = math.sqrt(16 / 3 - 128 / 27)
print("center: ||f-Pf||_L2 =", l2P, " ||f-Pf||_H =", hP)
grid = [i / 3000 for i in range(3001)]
print("sup|f-f3| =", max(abs(f(x) - f3(x)) for x in grid), " sup|f-Pf| =", max(abs(f(x) - Pf(x)) for x in grid))
print("int R3 =", sum(R3(x) for x in xs) / N, " int PZ2 =", sum(PZ2(x) for x in xs) / N)
print("sup R3 =", max(R3(x) for x in grid), " sup PZ2 =", max(PZ2(x) for x in grid))
with open(here / "data.dat", "w") as out:
    out.write("x f f3 Pf R3 PZ2\n")
    for i in range(301):
        x = i / 300
        out.write(f"{x:.5f} {f(x):.5f} {f3(x):.5f} {Pf(x):.5f} {R3(x):.6f} {PZ2(x):.6f}\n")
