"""Quasi-Newton routines shared by the qn-* figures of chapter 5.8.

Every figure imports this module and states its own objective and parameters;
no plotted number is written by hand.
"""
import numpy as np


def strong_wolfe(fun, grad, x, d, a0=1.0, c1=1e-4, c2=.9, maxit=40):
    """Bracket-and-zoom line search for the strong Wolfe conditions."""
    phi = lambda a: fun(x+a*d)
    dphi = lambda a: float(grad(x+a*d)@d)
    p0, dp0 = phi(0.), dphi(0.)
    if dp0 >= 0:
        raise ValueError('not a descent direction')
    evals = 1

    def zoom(lo, hi, plo, dplo):
        nonlocal evals
        for _ in range(maxit):
            a = .5*(lo+hi)
            pa = phi(a); evals += 1
            if pa > p0+c1*a*dp0 or pa >= plo:
                hi = a
            else:
                da = dphi(a)
                if abs(da) <= -c2*dp0:
                    return a
                if da*(hi-lo) >= 0:
                    hi = lo
                lo, plo, dplo = a, pa, da
        return lo if lo > 0 else a

    prev, pprev, a = 0., p0, a0
    for i in range(maxit):
        pa = phi(a); evals += 1
        if pa > p0+c1*a*dp0 or (i > 0 and pa >= pprev):
            return zoom(prev, a, pprev, 0.), evals
        da = dphi(a)
        if abs(da) <= -c2*dp0:
            return a, evals
        if da >= 0:
            return zoom(a, prev, pa, da), evals
        prev, pprev, a = a, pa, 2*a
    return a, evals


def run_quasi_newton(fun, grad, x0, W0, kind='bfgs', T=200, gtol=1e-10, c2=.9):
    """Dense BFGS or DFP in inverse form.

    Returns iterates, gradient norms, inverse matrices and function evaluations.
    """
    x, W = np.array(x0, float), np.array(W0, float)
    xs, Ws, gn, evals = [x.copy()], [W.copy()], [np.linalg.norm(grad(x))], [0]
    I = np.eye(len(x))
    for _ in range(T):
        g = grad(x)
        if np.linalg.norm(g) <= gtol:
            break
        d = -W@g
        a, e = strong_wolfe(fun, grad, x, d, c2=c2)
        xn = x+a*d
        s, y = xn-x, grad(xn)-g
        sy = float(s@y)
        if sy > 1e-14*np.linalg.norm(s)*np.linalg.norm(y):
            if kind == 'bfgs':
                rho = 1/sy
                V = I-rho*np.outer(y, s)
                W = V.T@W@V+rho*np.outer(s, s)
            elif kind == 'dfp':
                Wy = W@y
                W = W-np.outer(Wy, Wy)/float(y@Wy)+np.outer(s, s)/sy
            else:
                raise ValueError(kind)
        x = xn
        xs.append(x.copy()); Ws.append(W.copy())
        gn.append(np.linalg.norm(grad(x))); evals.append(evals[-1]+e)
    return dict(x=np.array(xs), W=Ws, gnorm=np.array(gn), evals=np.array(evals))


def two_loop(g, S, Y, gamma):
    """Two-loop recursion: returns W g for pairs S[0..r-1], Y[0..r-1] (oldest first)."""
    q = g.copy()
    xi = [0.]*len(S)
    for j in range(len(S)-1, -1, -1):
        rho = 1/float(S[j]@Y[j])
        xi[j] = rho*float(S[j]@q)
        q = q-xi[j]*Y[j]
    z = gamma*q
    for j in range(len(S)):
        rho = 1/float(S[j]@Y[j])
        eta = rho*float(Y[j]@z)
        z = z+(xi[j]-eta)*S[j]
    return z


def run_lbfgs(fun, grad, x0, r, T=2000, gtol=1e-8, scale=True, c2=.9):
    """L-BFGS with memory r. scale=False keeps the initial matrix equal to I."""
    x = np.array(x0, float)
    S, Y = [], []
    gn, fs, evals = [np.linalg.norm(grad(x))], [fun(x)], [0]
    for t in range(T):
        g = grad(x)
        if np.linalg.norm(g) <= gtol:
            break
        gamma = 1.
        if S and scale:
            gamma = float(S[-1]@Y[-1])/float(Y[-1]@Y[-1])
        d = -two_loop(g, S, Y, gamma)
        a0 = 1. if (S or not scale) else min(1., 1/np.linalg.norm(g))
        a, e = strong_wolfe(fun, grad, x, d, a0=a0, c2=c2)
        xn = x+a*d
        s, y = xn-x, grad(xn)-g
        if float(s@y) > 1e-12*np.linalg.norm(s)*np.linalg.norm(y):
            S.append(s); Y.append(y)
            if len(S) > r:
                S.pop(0); Y.pop(0)
        x = xn
        gn.append(np.linalg.norm(grad(x))); fs.append(fun(x)); evals.append(evals[-1]+e)
    return dict(gnorm=np.array(gn), f=np.array(fs), evals=np.array(evals), x=x)


def rotated_logcosh(n, cmin, cmax, seed):
    """f(x)=sum_i(c_i z_i^2/2+log cosh z_i), z=Qx, with c log-spaced in [cmin,cmax].

    Strongly convex: mu=cmin, L=cmax+1, x*=0, f*=0, H*=Q^T diag(c+1) Q.
    """
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    c = np.logspace(np.log10(cmin), np.log10(cmax), n)
    fun = lambda x: float(np.sum(.5*c*(Q@x)**2+np.log(np.cosh(Q@x))))
    grad = lambda x: Q.T@(c*(Q@x)+np.tanh(Q@x))
    hstar = Q.T@np.diag(c+1)@Q
    return fun, grad, hstar, rng


def panel(fig, left, right, top, bottom, wspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position()
        fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
