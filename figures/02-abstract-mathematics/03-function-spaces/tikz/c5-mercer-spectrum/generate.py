"""第5章 5.4.1：核积分算子的特征值衰减。

(1) 最小值核 min(x,z)，[0,1] 上 Lebesgue 测度：解析特征值 1/((j-1/2)^2 pi^2)。
(2) 高斯核 exp(-(x-z)^2/(2*0.5^2))，[-1,1] 上 dz/2：用 40 点 Gauss-Legendre 求积离散，
    求对称矩阵 W^{1/2} K W^{1/2} 的特征值（Jacobi 方法）。与 60 点结果比较以确认前若干个特征值的有效位数。
(3) 仿射核 1+xz，[-1,1] 上 dz/2：解析特征值 1、1/3。
打印 pgfplots 坐标。运行：python3 generate.py
"""
import math


def legendre_nodes(n):
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-15:
                break
        nodes.append(x)
        weights.append(2 / ((1 - x * x) * dp * dp))
    return nodes, weights


def jacobi_eigenvalues(a, sweeps=80):
    n = len(a)
    a = [row[:] for row in a]
    for _ in range(sweeps):
        off = sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < 1e-32:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2 * a[p][q])
                t = (1 if theta >= 0 else -1) / (abs(theta) + math.sqrt(theta * theta + 1))
                c = 1 / math.sqrt(t * t + 1)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p] = c * akp - s * akq
                    a[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k] = c * apk - s * aqk
                    a[q][k] = s * apk + c * aqk
    return sorted((a[i][i] for i in range(n)), reverse=True)


def gauss_eigs(n, sigma=0.5):
    x, w = legendre_nodes(n)
    w = [wi / 2 for wi in w]  # measure dz/2
    A = [[math.sqrt(w[i] * w[j]) * math.exp(-(x[i] - x[j]) ** 2 / (2 * sigma ** 2)) for j in range(n)] for i in range(n)]
    return jacobi_eigenvalues(A)


g40 = gauss_eigs(40)
g60 = gauss_eigs(60)
print("Gaussian trace (should be 1):", sum(g40))
for j in range(12):
    print(j + 1, f"{g40[j]:.6e}", f"{g60[j]:.6e}")
brown = [1 / (((j - 0.5) * math.pi) ** 2) for j in range(1, 13)]
print("Brownian:", " ".join(f"({j+1},{v:.6e})" for j, v in enumerate(brown)))
print("Brownian partial trace 3:", sum(brown[:3]), "tail:", 0.5 - sum(brown[:3]))
print("Gaussian coords:", " ".join(f"({j+1},{g40[j]:.6e})" for j in range(12) if g40[j] > 1e-12 and abs(g40[j] - g60[j]) < 1e-3 * g40[j]))
