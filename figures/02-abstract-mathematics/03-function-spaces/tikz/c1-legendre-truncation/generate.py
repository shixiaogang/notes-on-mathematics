"""Legendre expansions of sign(x) and |x| on [-1,1] (Lebesgue measure).

Exact rational arithmetic for coefficients; prints
  * squared coefficients c_n^2 and tail errors ||f-s_m||^2 = ||f||^2 - sum_{n<=m} c_n^2,
  * sampled partial sums s_1, s_5, s_15 of sign(x) for the TikZ figure.
Normalised basis e_n = sqrt((2n+1)/2) P_n, so c_n^2 = (2n+1)/2 * (int f P_n)^2.
"""
from fractions import Fraction as Fr
import math

N = 41
P = [[Fr(1)], [Fr(0), Fr(1)]]          # coefficient lists, P[n][k] = coeff of x^k
for n in range(1, N):
    a = [Fr(0)] + [Fr(2 * n + 1) * c for c in P[n]]
    b = P[n - 1] + [Fr(0)] * (len(a) - len(P[n - 1]))
    P.append([(x - Fr(n) * y) / (n + 1) for x, y in zip(a, b)])

def int01(poly, shift=0):
    """int_0^1 x^shift * poly(x) dx"""
    return sum(c / (k + shift + 1) for k, c in enumerate(poly))

def coeff_sq(n, kind):
    if kind == "sign":
        if n % 2 == 0:
            return Fr(0)
        I = 2 * int01(P[n])
    else:  # abs
        if n % 2 == 1:
            return Fr(0)
        I = 2 * int01(P[n], shift=1)
    return Fr(2 * n + 1, 2) * I * I

norms = {"sign": Fr(2), "abs": Fr(2, 3)}
for kind in ("sign", "abs"):
    print(f"== {kind}: ||f||^2 = {norms[kind]}")
    acc = Fr(0)
    tails = []
    for m in range(N + 1):
        acc += coeff_sq(m, kind)
        tails.append(float(norms[kind] - acc))
    for m in range(0, N + 1):
        print(m, float(coeff_sq(m, kind)), tails[m])

def peval(n, x):
    return sum(float(c) * x ** k for k, c in enumerate(P[n]))

def partial_sign(m, x):
    s = 0.0
    for n in range(m + 1):
        if n % 2 == 1:
            I = 2 * float(int01(P[n]))
            s += (2 * n + 1) / 2 * I * peval(n, x)
    return s

print("== partial sums of sign")
for m in (1, 5, 15):
    pts = []
    for i in range(0, 201):
        x = -1 + i / 100
        pts.append(f"({x:.2f},{partial_sign(m, x):.4f})")
    print(m, " ".join(pts))
