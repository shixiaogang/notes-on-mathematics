"""Dyadic simple approximations s_n = floor(2^n f)/2^n of f(x)=sin(pi x) on [0,1].
Prints const-plot coordinates (left endpoint, value) for n=2 and n=3, and sup errors."""
import math
for n in (2, 3):
    L = 2 ** n
    # breakpoints where f crosses k/L
    bps = {0.0, 1.0}
    for k in range(1, L + 1):
        y = k / L
        if y <= 1:
            x = math.asin(y) / math.pi
            bps.add(x); bps.add(1 - x)
    xs = sorted(bps)
    pts = []
    for a, b in zip(xs[:-1], xs[1:]):
        mid = (a + b) / 2
        v = math.floor(L * math.sin(math.pi * mid)) / L
        pts.append((a, v))
    pts.append((1.0, pts[-1][1]))
    print(n, " ".join(f"({a:.4f},{v:.4f})" for a, v in pts))
    # L2 error^2 numerically
    M = 200000
    e2 = sum((math.sin(math.pi*(i+.5)/M) - math.floor(L*math.sin(math.pi*(i+.5)/M))/L)**2 for i in range(M))/M
    print("  L2 error", math.sqrt(e2), "sup error <", 1 / L)
