"""Bernstein weights w_{m,j}(x)=C(m,j)x^j(1-x)^{m-j} at m=50, x=0.3, delta=0.15.
Writes near.dat / far.dat (node j/m, weight) and prints near/far weight sums and the bound 1/(4 m delta^2)."""
from math import comb
from pathlib import Path
here = Path(__file__).resolve().parent
m, x, d = 50, 0.3, 0.15
w = [(j / m, comb(m, j) * x**j * (1 - x)**(m - j)) for j in range(m + 1)]
near = [(t, v) for t, v in w if abs(t - x) <= d + 1e-12]
far = [(t, v) for t, v in w if abs(t - x) > d + 1e-12]
(here / "near.dat").write_text("t w\n" + "\n".join(f"{t:.3f} {v:.5f}" for t, v in near) + "\n")
(here / "far.dat").write_text("t w\n" + "\n".join(f"{t:.3f} {v:.6f}" for t, v in far) + "\n")
print("near sum", sum(v for _, v in near), "far sum", sum(v for _, v in far))
print("second moment", sum((t - x)**2 * v for t, v in w), "x(1-x)/m", x * (1 - x) / m)
print("bound 1/(4 m d^2)", 1 / (4 * m * d * d), " x(1-x)/(m d^2)", x*(1-x)/(m*d*d))
print("max weight", max(v for _, v in w))
