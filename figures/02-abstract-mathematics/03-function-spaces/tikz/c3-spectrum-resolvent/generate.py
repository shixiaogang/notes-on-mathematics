"""第3章图 c3-spectrum-resolvent 的数据：A=diag(1/n) 在 l^2 上，
实参数 lambda 不在谱中时 ||(A-lambda I)^{-1}|| = 1/dist(lambda, {1/n}∪{0})。
在 [-0.3,1.3] 上以步长 0.002、偏移 0.0007 取样（避开 1/n），把大于 1000 的值截为 1000，绘图时纵轴上限 120。"""
N = 100000
eig = [1.0 / n for n in range(1, N + 1)]
pts = []
k = 0
while True:
    lam = -0.3 + 0.0007 + 0.002 * k
    if lam > 1.3:
        break
    d = min(abs(lam), min(abs(e - lam) for e in eig[:2000]))
    v = min(1.0 / d, 1000.0)
    pts.append(f"{lam:.4f} {v:.3f}")
    k += 1
print("lambda norm"); print("\n".join(pts))
