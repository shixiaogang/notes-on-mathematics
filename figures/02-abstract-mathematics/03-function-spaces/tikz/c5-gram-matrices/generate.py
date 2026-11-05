"""第5章 5.1.2：高斯核与仿射核在五个点上的 Gram 矩阵及其特征值。

点组 x = -1, -0.5, 0, 0.5, 1；高斯核 exp(-(x-z)^2/(2*0.5^2))，仿射核 1+xz。
纯 Python 循环 Jacobi 方法求对称矩阵特征值，打印矩阵元与特征值，供 figure.tex 使用。
运行：python3 generate.py
"""
import math

xs = [-1.0, -0.5, 0.0, 0.5, 1.0]
sigma = 0.5


def jacobi_eigenvalues(a, sweeps=60):
    n = len(a)
    a = [row[:] for row in a]
    for _ in range(sweeps):
        off = sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < 1e-30:
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


gauss = [[math.exp(-(x - z) ** 2 / (2 * sigma ** 2)) for z in xs] for x in xs]
affine = [[1 + x * z for z in xs] for x in xs]
print("Gaussian Gram:")
for row in gauss:
    print(" ".join(f"{v:.4f}" for v in row))
print("Gaussian eigenvalues:", [round(v, 5) for v in jacobi_eigenvalues(gauss)])
print("Affine Gram:")
for row in affine:
    print(" ".join(f"{v:.2f}" for v in row))
print("Affine eigenvalues:", [round(v, 8) for v in jacobi_eigenvalues(affine)])
