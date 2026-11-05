"""Bernstein polynomials of f*(x)=|x-1/2| on [0,1] for m=4,16,64.
Writes bernstein-m{m}.dat (x, B_m f*(x)) and prints sup errors (on a 2001-point grid)."""
from math import comb
from pathlib import Path
here = Path(__file__).resolve().parent
f = lambda x: abs(x - 0.5)
def B(m, x):
    return sum(f(j / m) * comb(m, j) * x**j * (1 - x)**(m - j) for j in range(m + 1))
for m in (4, 16, 64):
    xs = [i / 200 for i in range(201)]
    (here / f"bernstein-m{m}.dat").write_text("x y\n" + "\n".join(f"{x:.4f} {B(m,x):.5f}" for x in xs) + "\n")
    grid = [i / 2000 for i in range(2001)]
    err = max(abs(B(m, x) - f(x)) for x in grid)
    arg = max(grid, key=lambda x: abs(B(m, x) - f(x)))
    print(m, "sup err", round(err, 5), "at", arg, "1/(2sqrt m)=", round(0.5 / m**0.5, 5))
