"""Exact Lindeberg quantities for the three running triangular arrays of chapter 7.15.

A: X_k ~ Unif(-k, k), k = 1..n            (Lindeberg holds)
B: X_k ~ N(0, 2^k),  k = 1..n             (Lindeberg fails, row sum still exactly Gaussian)
C: X_{n,k} = B_{n,k} - 1/n, B ~ Bern(1/n)  (Lindeberg fails, Poisson limit)
For every term the function returns its variance and its truncated second moment
E[X^2; |X| > eps * s_n].
"""
import math
import numpy as np

_erfc = np.vectorize(math.erfc)


def terms(kind, n, eps):
    k = np.arange(1, n+1, dtype=float)
    if kind == 'A':
        var = k*k/3; s = math.sqrt(var.sum()); c = eps*s
        tail = np.where(k > c, (k**3-np.minimum(c, k)**3)/(3*k), 0.0)
    elif kind == 'B':
        var = 2.0**k; s = math.sqrt(var.sum()); c = eps*s
        u = c/np.sqrt(var)
        tail = var*(_erfc(u/math.sqrt(2)) + 2*u*np.exp(-u*u/2)/math.sqrt(2*math.pi))
    else:
        p = 1/n; var = np.full(n, p*(1-p)); s = math.sqrt(var.sum()); c = eps*s
        big, small = 1-p, p
        tail = np.full(n, (p*big**2 if big > c else 0.0) + ((1-p)*small**2 if small > c else 0.0))
    return var, tail, s


def lindeberg_ratio(kind, n, eps):
    var, tail, s = terms(kind, n, eps)
    return float(tail.sum()/s**2)


def max_share(kind, n):
    var, _, s = terms(kind, n, .5)
    return float(var.max()/s**2)
