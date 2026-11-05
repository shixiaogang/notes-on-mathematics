"""Fixed-width Gaussian sections K(x,c)=exp(-(x-c)^2/(2 s^2)), s=0.15, on [0,1].
(a) interpolate f*(x)=|x-1/2| at M equispaced centers c_l=(l-1)/(M-1), M=5,9,13,17 (figure uses 5 and 9); writes gauss-M{M}.dat,
    prints sup error on a 2001-point grid and max |a_l|.
(b) centre difference: (K(x,1/2+h)-K(x,1/2))/h for h=0.1,0.02 vs d/dc K(x,c)|_{c=1/2}=(x-1/2)/s^2 K(x,1/2);
    writes diff-h{h}.dat and prints sup deviations."""
from math import exp
from pathlib import Path
here = Path(__file__).resolve().parent
s = 0.15
K = lambda x, c: exp(-(x - c)**2 / (2 * s * s))
f = lambda x: abs(x - 0.5)
def solve(A, b):
    n = len(b); M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            t = M[r][c] / M[c][c]
            for k in range(c, n + 1): M[r][k] -= t * M[c][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (M[r][n] - sum(M[r][k] * x[k] for k in range(r + 1, n))) / M[r][r]
    return x
grid = [i / 2000 for i in range(2001)]
for Mc in (5, 9, 13, 17):
    cs = [l / (Mc - 1) for l in range(Mc)]
    a = solve([[K(ci, cj) for cj in cs] for ci in cs], [f(c) for c in cs])
    g = lambda x: sum(al * K(x, cl) for al, cl in zip(a, cs))
    (here / f"gauss-M{Mc}.dat").write_text("x y\n" + "\n".join(f"{x:.4f} {g(x):.5f}" for x in [i / 200 for i in range(201)]) + "\n")
    print("M", Mc, "sup err", round(max(abs(g(x) - f(x)) for x in grid), 4), "max|a|", round(max(abs(t) for t in a), 2))
d = lambda x: (x - 0.5) / s**2 * K(x, 0.5)
for h in (0.1, 0.02):
    q = lambda x: (K(x, 0.5 + h) - K(x, 0.5)) / h
    (here / f"diff-h{h}.dat").write_text("x y\n" + "\n".join(f"{x:.4f} {q(x):.5f}" for x in [i / 200 for i in range(201)]) + "\n")
    print("h", h, "sup |diff - deriv|", round(max(abs(q(x) - d(x)) for x in grid), 4), "max|deriv|", round(max(abs(d(x)) for x in grid), 4))
