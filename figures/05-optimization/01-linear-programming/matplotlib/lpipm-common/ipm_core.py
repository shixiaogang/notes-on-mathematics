"""Primal-dual interior-point kernels for the examples of the LP interior-point chapter."""
import numpy as np

# Chapter running example: min x1+2x2+3x3, x1+x2+x3=1, x>=0.
A_RUN = np.array([[1., 1., 1.]])
B_RUN = np.array([1.])
C_RUN = np.array([1., 2., 3.])
X0_RUN, Y0_RUN, S0_RUN = np.ones(3) / 3, np.zeros(1), C_RUN.copy()

# Factory example of the simplex chapter, in standard form.
A_FAC = np.array([[1., 2., 1., 0., 0.], [2., 1., 0., 1., 0.], [0., 1., 0., 0., 1.]])
B_FAC = np.array([8., 10., 3.])
C_FAC = np.array([-4., -5., 0., 0., 0.])


def residuals(A, b, c, x, y, s):
    return A @ x - b, A.T @ y + s - c


def newton(A, rp, rd, rc, x, s):
    """Solve A dx=-rp, A'dy+ds=-rd, S dx+X ds=rc through the normal equations."""
    D = x / s
    M = (A * D) @ A.T
    rhs = -rp - A @ ((rc + x * rd) / s)
    dy = np.linalg.solve(M, rhs)
    ds = -rd - A.T @ dy
    dx = (rc - x * ds) / s
    return dx, dy, ds, M, rhs


def max_step(v, dv):
    neg = dv < 0
    return np.inf if not neg.any() else float(np.min(-v[neg] / dv[neg]))


def _arrays(*v):
    return [np.array(u, float) for u in v]


def path_following(A, b, c, x, y, s, sigma=.5, eta=.9, tol=1e-4, maxit=200):
    """Common-step path following; returns a list of dicts with every intermediate quantity."""
    x, y, s = _arrays(x, y, s)
    n = len(x); hist = []
    for t in range(maxit + 1):
        rp, rd = residuals(A, b, c, x, y, s)
        mu = x @ s / n
        rec = dict(t=t, x=x.copy(), y=y.copy(), s=s.copy(), mu=mu, rp=rp.copy(), rd=rd.copy())
        if (max(np.linalg.norm(rp), np.linalg.norm(rd)) <= tol and x @ s <= tol) or t == maxit:
            hist.append(rec); break
        rc = sigma * mu * np.ones(n) - x * s
        dx, dy, ds, M, rhs = newton(A, rp, rd, rc, x, s)
        amax = min(max_step(x, dx), max_step(s, ds))
        a = min(1., eta * amax)
        rec.update(rc=rc, dx=dx, dy=dy, ds=ds, M=M, rhs=rhs, amax=amax, alpha=a)
        hist.append(rec)
        x, y, s = x + a * dx, y + a * dy, s + a * ds
    return hist


def center(A, b, c, x, y, s, mu, it=200):
    """Newton iteration for the central-path equations at fixed mu, from any interior start."""
    x, y, s = _arrays(x, y, s)
    n = len(x)
    for _ in range(it):
        rp, rd = residuals(A, b, c, x, y, s)
        rc = mu * np.ones(n) - x * s
        if max(np.linalg.norm(rp), np.linalg.norm(rd), np.linalg.norm(rc)) < 1e-12 * max(1, mu):
            break
        dx, dy, ds, _, _ = newton(A, rp, rd, rc, x, s)
        a = min(1., .9 * min(max_step(x, dx), max_step(s, ds)))
        x, y, s = x + a * dx, y + a * dy, s + a * ds
    return x, y, s


def central_curve(A, b, c, x, y, s, mus):
    """Central points for a decreasing list of mu, warm-started in order."""
    out = []
    for mu in mus:
        x, y, s = center(A, b, c, x, y, s, mu)
        out.append((x.copy(), y.copy(), s.copy()))
    return out


def predictor_corrector(A, b, c, x, y, s, eta=.9, tol=1e-4, maxit=100):
    """Mehrotra-type predictor-corrector with one common step length."""
    x, y, s = _arrays(x, y, s)
    n = len(x); hist = []
    for t in range(maxit + 1):
        rp, rd = residuals(A, b, c, x, y, s)
        mu = x @ s / n
        rec = dict(t=t, x=x.copy(), y=y.copy(), s=s.copy(), mu=mu, rp=rp.copy(), rd=rd.copy())
        if (max(np.linalg.norm(rp), np.linalg.norm(rd)) <= tol and x @ s <= tol) or t == maxit:
            hist.append(rec); break
        dxa, dya, dsa, M, rhsa = newton(A, rp, rd, -x * s, x, s)
        aa = min(1., max_step(x, dxa), max_step(s, dsa))
        mua = (x + aa * dxa) @ (s + aa * dsa) / n
        sigma = (mua / mu) ** 3
        rc = sigma * mu * np.ones(n) - x * s - dxa * dsa
        dx, dy, ds, _, rhs = newton(A, rp, rd, rc, x, s)
        amax = min(max_step(x, dx), max_step(s, ds))
        a = min(1., eta * amax)
        rec.update(dxa=dxa, dya=dya, dsa=dsa, aa=aa, mua=mua, sigma=sigma, rc=rc, dx=dx, dy=dy, ds=ds,
                   M=M, rhsa=rhsa, rhs=rhs, amax=amax, alpha=a)
        hist.append(rec)
        x, y, s = x + a * dx, y + a * dy, s + a * ds
    return hist


def short_step(A, b, c, x, y, s, eps=1e-6, maxit=100000):
    """Short-step path following: sigma=1-0.4/sqrt(n), unit step."""
    x, y, s = _arrays(x, y, s)
    n = len(x); sigma = 1 - .4 / np.sqrt(n); hist = []
    for t in range(maxit):
        mu = x @ s / n
        hist.append(dict(t=t, x=x.copy(), y=y.copy(), s=s.copy(), mu=mu))
        if x @ s <= eps:
            break
        rp, rd = residuals(A, b, c, x, y, s)
        dx, dy, ds, _, _ = newton(A, rp, rd, sigma * mu * np.ones(n) - x * s, x, s)
        x, y, s = x + dx, y + dy, s + ds
    return hist


def long_step(A, b, c, x, y, s, sigma=.1, gamma=1e-3, eps=1e-6, maxit=2000):
    """Long-step path following in the one-sided neighbourhood min x_i s_i >= gamma mu."""
    x, y, s = _arrays(x, y, s)
    n = len(x); hist = []
    for t in range(maxit):
        mu = x @ s / n
        hist.append(dict(t=t, x=x.copy(), y=y.copy(), s=s.copy(), mu=mu))
        if x @ s <= eps:
            break
        rp, rd = residuals(A, b, c, x, y, s)
        dx, dy, ds, _, _ = newton(A, rp, rd, sigma * mu * np.ones(n) - x * s, x, s)
        a = min(1., .9999 * min(max_step(x, dx), max_step(s, ds)))
        while True:
            xn, sn = x + a * dx, s + a * ds
            if np.all(xn > 0) and np.all(sn > 0) and np.min(xn * sn) >= gamma * (xn @ sn) / n:
                break
            a *= .95
        x, y, s = xn, y + a * dy, sn
    return hist


def tri(x):
    """Planar coordinates of points of the unit simplex in R^3: e1 right, e2 top, e3 left."""
    x = np.asarray(x, float)
    return np.stack([x[..., 0] - x[..., 2], x[..., 1] * np.sqrt(3.)], -1)
