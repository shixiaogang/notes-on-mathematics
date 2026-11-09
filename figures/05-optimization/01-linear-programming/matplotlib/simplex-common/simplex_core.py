"""Exact (rational) simplex kernels shared by the figures of the simplex chapter.

Problems are in standard form: min c'x, Ax=b, x>=0. Column indices are 1-based,
as in the text. Every function returns the per-round data that the figures draw.
"""
from fractions import Fraction as F


def to_frac(rows):
    return [[F(v) for v in r] for r in rows]


def col(A, j):
    return [row[j - 1] for row in A]


def solve(M, rhs):
    """Gauss-Jordan on exact rationals."""
    n = len(M)
    T = [list(M[i]) + [rhs[i]] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if T[i][k] != 0)
        T[k], T[p] = T[p], T[k]
        T[k] = [v / T[k][k] for v in T[k]]
        for i in range(n):
            if i != k and T[i][k] != 0:
                f = T[i][k]
                T[i] = [a - f * b for a, b in zip(T[i], T[k])]
    return [T[i][n] for i in range(n)]


def basis_matrix(A, B):
    return [[A[i][j - 1] for j in B] for i in range(len(A))]


def transpose(M):
    return [list(r) for r in zip(*M)]


def round_data(A, b, c, B):
    AB = basis_matrix(A, B)
    xB = solve(AB, b)
    y = solve(transpose(AB), [c[j - 1] for j in B])
    n = len(c)
    s = [c[j] - sum(A[i][j] * y[i] for i in range(len(A))) for j in range(n)]
    return AB, xB, y, s


def simplex(A, b, c, B, rule='dantzig', max_rounds=200, leave_tie='lowest', stop_on_repeat=False):
    """Primal simplex from feasible basis B. Returns (status, trace, x)."""
    A, b, c = to_frac(A), [F(v) for v in b], [F(v) for v in c]
    B = list(B)
    n, m = len(c), len(A)
    trace = []
    seen = set()
    for t in range(max_rounds):
        AB, xB, y, s = round_data(A, b, c, B)
        x = [F(0)] * n
        for pos, j in enumerate(B):
            x[j - 1] = xB[pos]
        f = sum(ci * xi for ci, xi in zip(c, x))
        rec = dict(t=t, B=list(B), xB=xB, x=x, y=y, s=s, f=f)
        trace.append(rec)
        key = tuple(sorted(B))
        if stop_on_repeat and key in seen:
            rec['repeat'] = True
            return 'cycle', trace, x
        seen.add(key)
        N = [j for j in range(1, n + 1) if j not in B]
        neg = [j for j in N if s[j - 1] < 0]
        if not neg:
            return 'optimal', trace, x
        if rule == 'dantzig':
            enter = min(neg, key=lambda j: (s[j - 1], j))
        else:
            enter = min(neg)
        u = solve(AB, col(A, enter))
        rec.update(enter=enter, u=u)
        cand = [(xB[i] / u[i], B[i], i) for i in range(m) if u[i] > 0]
        if not cand:
            rec['unbounded'] = True
            return 'unbounded', trace, x
        alpha = min(v for v, _, _ in cand)
        ties = [(jb, i) for v, jb, i in cand if v == alpha]
        rec['ratios'] = [(B[i], xB[i] / u[i] if u[i] > 0 else None) for i in range(m)]
        if leave_tie == 'lowest':
            leave, r = min(ties)
        elif leave_tie == 'highest':
            leave, r = max(ties)
        else:
            leave, r = leave_tie(ties)
        rec.update(leave=leave, r=r, alpha=alpha, ties=ties)
        B[r] = enter
    return 'limit', trace, None


def dual_simplex(A, b, c, B, max_rounds=100):
    """Dual simplex from a dual-feasible basis, leaving = most negative x_B (lowest index on ties)."""
    A, b, c = to_frac(A), [F(v) for v in b], [F(v) for v in c]
    B = list(B)
    n, m = len(c), len(A)
    trace = []
    for t in range(max_rounds):
        AB, xB, y, s = round_data(A, b, c, B)
        x = [F(0)] * n
        for pos, j in enumerate(B):
            x[j - 1] = xB[pos]
        rec = dict(t=t, B=list(B), xB=xB, x=x, y=y, s=s, f=sum(a * v for a, v in zip(c, x)))
        trace.append(rec)
        if min(xB) >= 0:
            return 'optimal', trace
        r = min((i for i in range(m) if xB[i] < 0), key=lambda i: (xB[i], B[i]))
        e_r = [F(int(i == r)) for i in range(m)]
        v = solve(transpose(AB), e_r)
        abar = [sum(v[i] * A[i][j] for i in range(m)) for j in range(n)]
        N = [j for j in range(1, n + 1) if j not in B]
        cand = [j for j in N if abar[j - 1] < 0]
        rec.update(leave=B[r], r=r, v=v, abar=abar)
        if not cand:
            return 'infeasible', trace
        tau = min(s[j - 1] / (-abar[j - 1]) for j in cand)
        enter = min(j for j in cand if s[j - 1] / (-abar[j - 1]) == tau)
        rec.update(enter=enter, tau=tau, ratios={j: s[j - 1] / (-abar[j - 1]) for j in cand})
        u = solve(AB, col(A, enter))
        rec.update(u=u, alpha=xB[r] / abar[enter - 1])
        B[r] = enter
    return 'limit', trace


def klee_minty(n):
    """max sum 2^(n-j) x_j, sum_{j<i} 2^(i-j+1) x_j + x_i <= 5^i, in standard form."""
    A, b = [], []
    for i in range(1, n + 1):
        row = [0] * (2 * n)
        for j in range(1, i):
            row[j - 1] = 2 ** (i - j + 1)
        row[i - 1] = 1
        row[n + i - 1] = 1
        A.append(row)
        b.append(5 ** i)
    c = [-(2 ** (n - j)) for j in range(1, n + 1)] + [0] * n
    return A, b, c, list(range(n + 1, 2 * n + 1))
