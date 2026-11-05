"""Generate exact breakpoints of the piecewise-linear Cantor approximations F_n.

F_n rises by 2^{-n} linearly on each of the 2^n closed intervals of C_n and is
constant elsewhere on [0,1].  Output: pgfplots coordinate strings for the figure
sources c2-cantor-function and c2-three-part-decomposition.
Run from the repository root: python3 <this file>
"""
from fractions import Fraction as Fr


def intervals(n):
    iv = [(Fr(0), Fr(1))]
    for _ in range(n):
        new = []
        for a, b in iv:
            L = (b - a) / 3
            new += [(a, a + L), (b - L, b)]
        iv = new
    return iv


def breakpoints(n):
    pts = []
    for k, (a, b) in enumerate(intervals(n)):
        pts += [(a, Fr(k, 2**n)), (b, Fr(k + 1, 2**n))]
    return pts


def coords(pts, f=lambda x, y: (x, y)):
    return " ".join(f"({float(x):.5f},{float(y):.5f})" for x, y in (f(x, y) for x, y in pts))


def value(n, x):
    pts = breakpoints(n)
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            return y0 if x1 == x0 else y0 + (y1 - y0) * (x - x0) / (x1 - x0)


if __name__ == "__main__":
    for n in (1, 2, 7):
        print(f"F_{n}:", coords(breakpoints(n)))
    print("F_n(1/4), n=0..4:", [str(Fr(1, 4))] + [str(value(n, Fr(1, 4))) for n in range(1, 5)])
    # three-part example: G = x/2 + (1/4)1[x>=1/2] + F/4 on [0,1]; F approximated by F_7
    left = [(x, y) for x, y in breakpoints(7) if x < Fr(1, 2)]
    right = [(x, y) for x, y in breakpoints(7) if x > Fr(1, 2)]
    g = lambda x, y: (x, x / 2 + y / 4)
    print("G left:", coords(left + [(Fr(1, 2), Fr(1, 2))], g))
    print("G right:", coords([(Fr(1, 2), Fr(1, 2))] + right, lambda x, y: (x, x / 2 + Fr(1, 4) + y / 4)))
    print("F/4:", coords(breakpoints(7), lambda x, y: (x, y / 4)))
