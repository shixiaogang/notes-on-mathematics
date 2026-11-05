# coding: utf-8
"""Teaching charts for volume three, part "optimization", chapter 4
(nonsmooth and composite optimization).

Every curve comes from a closed-form expression or from a deterministic
iteration whose parameters are recorded in the facts file next to each figure;
the only random data (the Lasso comparison) use the fixed seed SEED.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/01-optimization/matplotlib/generate_c4.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import linprog, minimize_scalar

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import (figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID,
                     BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL)

D = Path(__file__).resolve().parent
SEED = 20261030


def _axes_through_origin(ax):
    ax.axhline(0, color=GRID, lw=.6, zorder=0)
    ax.axvline(0, color=GRID, lw=.6, zorder=0)


# ---------------------------------------------------------------- 4.1
def abs_supports():
    """|x| with the family of support lines y=g x, g in [-1,1], and the set-valued map d|x|."""
    fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
    x = np.linspace(-1.5, 1.5, 301)
    ax = axes[0]
    _axes_through_origin(ax)
    for g in [-1, -.5, 0, .5, 1]:
        ax.plot(x, g*x, color=GREEN, lw=.6, ls='--')
    ax.plot(x, np.abs(x), color=BLUE, lw=1.4)
    ax.text(1.02, -.62, r'$g x,\ g\in[-1,1]$', color=GREEN, fontsize=7.5)
    ax.text(-1.0, 1.25, r'$|x|$', color=BLUE)
    x1 = 1.0
    ax.plot(x, x, color=PURPLE, lw=.9)
    ax.plot([x1], [x1], 'o', color=PURPLE, ms=3)
    ax.text(.42, 1.28, '唯一支撑', color=PURPLE, fontsize=7.5)
    ax.set(xlim=(-1.5, 1.5), ylim=(-1.0, 1.5), xlabel=r'$x$')
    ax.set_title('(a) 原点处的一族支撑线')
    ax = axes[1]
    _axes_through_origin(ax)
    ax.plot([-1.5, 0], [-1, -1], color=BLUE, lw=1.4)
    ax.plot([0, 1.5], [1, 1], color=BLUE, lw=1.4)
    ax.plot([0, 0], [-1, 1], color=BLUE, lw=2.2)
    ax.plot([0], [0], 'o', color=RED, ms=3.2)
    ax.text(.08, .05, r'$0\in\partial f(0)$', color=RED, fontsize=7.5)
    ax.text(-1.4, -.82, r'$\{-1\}$', fontsize=7.5)
    ax.text(.9, 1.1, r'$\{1\}$', fontsize=7.5)
    ax.text(.08, -.6, r'$[-1,1]$', fontsize=7.5, color=BLUE)
    ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel=r'$x$', ylabel=r'$\partial f(x)$')
    ax.set_title('(b) 次微分作为集合值映射')
    save(fig, D/'c4-abs-supports', 'figure', {
        'f': '|x|', 'support_slopes_at_0': [-1, -.5, 0, .5, 1],
        'subdifferential': {'x<0': [-1], 'x=0': '[-1,1]', 'x>0': [1]}})


def max_affine_subdiff():
    """f(x)=max{-x, x/2, 2x-3}: kinks at 0 and 2, subdifferentials [-1,1/2] and [1/2,2]."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    x = np.linspace(-2, 3.5, 400)
    pieces = [(-1, 0), (.5, 0), (2, -3)]
    f = np.max([a*x + b for a, b in pieces], axis=0)
    ax = axes[0]
    _axes_through_origin(ax)
    for (a, b), c in zip(pieces, [GREEN, YELLOW, PURPLE]):
        ax.plot(x, a*x + b, color=c, lw=.6, ls='--')
    ax.plot(x, f, color=BLUE, lw=1.4)
    for g in [-.5, 0, .25]:
        ax.plot(x, g*x, color=MUTED, lw=.5, ls=':')
    for g in [1, 1.5]:
        ax.plot(x, 1 + g*(x - 2), color=MUTED, lw=.5, ls=':')
    ax.plot([0, 2], [0, 1], 'o', color=INK, ms=3)
    ax.text(-1.9, 1.75, r'$-x$', color=GREEN, fontsize=7.5)
    ax.text(-1.2, -.95, r'$x/2$', color=YELLOW, fontsize=7.5)
    ax.text(2.55, 3.2, r'$2x-3$', color=PURPLE, fontsize=7.5)
    ax.set(xlim=(-2, 3.5), ylim=(-1.5, 4), xlabel=r'$x$')
    ax.set_title('(a) 活跃分支与支撑线')
    ax = axes[1]
    _axes_through_origin(ax)
    ax.plot([-2, 0], [-1, -1], color=BLUE, lw=1.4)
    ax.plot([0, 2], [.5, .5], color=BLUE, lw=1.4)
    ax.plot([2, 3.5], [2, 2], color=BLUE, lw=1.4)
    ax.plot([0, 0], [-1, .5], color=BLUE, lw=2.2)
    ax.plot([2, 2], [.5, 2], color=BLUE, lw=2.2)
    ax.plot([0], [0], 'o', color=RED, ms=3.2)
    ax.text(.1, -.35, r'$0\in[-1,1/2]$', color=RED, fontsize=7.5)
    ax.text(2.1, 1.1, r'$[1/2,2]$', color=BLUE, fontsize=7.5)
    ax.set(xlim=(-2, 3.5), ylim=(-1.5, 2.5), xlabel=r'$x$', ylabel=r'$\partial f(x)$')
    ax.set_title('(b) 切换点处取斜率的凸包')
    save(fig, D/'c4-max-affine-subdiff', 'figure', {
        'f': 'max{-x, x/2, 2x-3}', 'kinks': [0, 2],
        'subdifferential_at_kinks': {'0': '[-1,1/2]', '2': '[1/2,2]'}, 'minimizer': 0, 'f_star': 0})


def clarke_abs():
    """|x| and -|x| share the Clarke set [-1,1] at 0 although one has a min and the other a max."""
    fig, axes = figure(width_mm=112, height_mm=42, ncols=2, sharey=True)
    x = np.linspace(-1.2, 1.2, 241)
    for ax, sgn, title in [(axes[0], 1, r'(a) $f(x)=|x|$'), (axes[1], -1, r'(b) $f(x)=-|x|$')]:
        _axes_through_origin(ax)
        ax.plot(x, sgn*np.abs(x), color=BLUE, lw=1.4)
        ax.plot(x, 0*x, color=RED, lw=.9, ls='--')
        xl = np.linspace(-1.2, -.3, 10)
        xr = np.linspace(.3, 1.2, 10)
        ax.annotate('', xy=(-.15, sgn*.15), xytext=(-.7, sgn*.7),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=.8))
        ax.annotate('', xy=(.15, sgn*.15), xytext=(.7, sgn*.7),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=.8))
        ax.text(-1.0, sgn*.3, r"$f'=%d$" % (-sgn), color=GREEN, fontsize=7.5, va='center')
        ax.text(.55, sgn*.3, r"$f'=%d$" % sgn, color=GREEN, fontsize=7.5, va='center')
        ax.text(-.35, -.22 if sgn > 0 else .12, r'$g=0$', color=RED, fontsize=7.5)
        ax.set(xlim=(-1.2, 1.2), ylim=(-1.25, 1.25), xlabel=r'$x$')
        ax.set_title(title)
    save(fig, D/'c4-clarke-abs', 'figure', {
        'functions': ['|x|', '-|x|'], 'clarke_set_at_0': '[-1,1] for both',
        'convex_subdifferential_at_0': {'|x|': '[-1,1]', '-|x|': 'empty'}})


# ---------------------------------------------------------------- 4.2
def subgrad_not_descent():
    """f=|x1|+2|x2| at x=(1,0): g=(1,2) is a subgradient, -g raises f but shortens distance to 0."""
    fig, ax = figure(width_mm=80, height_mm=62)
    X, Y = np.meshgrid(np.linspace(-.6, 1.6, 300), np.linspace(-.9, .9, 300))
    F = np.abs(X) + 2*np.abs(Y)
    ax.contour(X, Y, F, levels=[.5, 1, 1.5, 2], colors=[BLUE], linewidths=.7)
    th = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.cos(th), np.sin(th), color=GREEN, lw=.8, ls='--')
    x = np.array([1., 0.])
    ax.plot(*x, 'o', color=INK, ms=3)
    ax.plot([0], [0], '*', color=RED, ms=6)
    s = .3
    ax.plot([x[0] - s, x[0] - s], [-2*s, 2*s], color=PURPLE, lw=2.0, alpha=1)
    for g, c, lab in [((1, 2), RED, r'$-\mathbf{g}$'), ((1, 0), YELLOW, None)]:
        g = np.array(g, float)
        ax.annotate('', xy=x - s*g, xytext=x, arrowprops=dict(arrowstyle='->', color=c, lw=1.1))
    ax.text(.72, -.72, r'$-(1,2)$', color=RED, fontsize=7.5)
    ax.text(.62, .06, r'$-(1,0)$', color=YELLOW, fontsize=7.5)
    ax.text(.36, .7, r'$-\partial f(\mathbf{x})$', color=PURPLE, fontsize=7.5)
    ax.text(-.55, .3, r'$f=1$', color=BLUE, fontsize=7.5)
    ax.text(1.03, .05, r'$\mathbf{x}$', fontsize=8)
    ax.text(-.25, -.95, r'$\|\mathbf{y}\|_2=1$', color=GREEN, fontsize=7.5)
    ax.text(1.12, .45, r'$f=1.5$', color=BLUE, fontsize=7.5)
    ax.set_aspect('equal')
    ax.set(xlim=(-.6, 1.6), ylim=(-1.05, .9), xlabel=r'$x_1$', ylabel=r'$x_2$')
    t = .15
    y = x - t*np.array([1, 2.])
    save(fig, D/'c4-subgrad-not-descent', 'figure', {
        'f': '|x1|+2|x2|', 'x': [1, 0], 'subdifferential': '{1} x [-2,2]', 'g': [1, 2],
        'f_along_minus_g': '1+3t for 0<t<1', 'dist2_along_minus_g': '1-2t+5t^2',
        'sample_t': t, 'f_at_sample': float(np.abs(y[0]) + 2*np.abs(y[1])),
        'dist_at_sample': float(np.linalg.norm(y))})


def _subgrad_run(x0, steps, T):
    x = np.array(x0, float)
    xs, fs = [x.copy()], []
    for t in range(T):
        f = abs(x[0]) + 2*abs(x[1])
        fs.append(f)
        g = np.array([np.sign(x[0]), 2*np.sign(x[1])])
        x = x - steps(t)*g
        xs.append(x.copy())
    return np.array(xs), np.array(fs)


def subgrad_steps():
    """Subgradient method on |x1|+2|x2| from (1.5,1): constant vs. diminishing steps."""
    x0 = (1.47, 0.93)
    R = float(np.linalg.norm(x0))
    G = float(np.sqrt(5))
    T = 2000
    runs = {
        r'$\eta=0.1$': (lambda t: .1, BLUE, '-'),
        r'$\eta=0.01$': (lambda t: .01, GREEN, '--'),
        r'$\eta^{(t)}=R/(G\sqrt{t+1})$': (lambda t: R/(G*np.sqrt(t + 1)), PURPLE, '-.'),
    }
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1, 1.25]})
    ax = axes[0]
    X, Y = np.meshgrid(np.linspace(-.4, 1.7, 300), np.linspace(-.5, 1.2, 300))
    ax.contour(X, Y, np.abs(X) + 2*np.abs(Y), levels=[.25, .5, 1, 1.5, 2, 2.5, 3.5], colors=[GRID], linewidths=.6)
    xs, _ = _subgrad_run(x0, lambda t: .1, 40)
    ax.plot(xs[:, 0], xs[:, 1], '-o', color=BLUE, lw=.8, ms=1.8)
    ax.plot(*x0, 'o', color=INK, ms=3)
    ax.plot([0], [0], '*', color=RED, ms=6)
    ax.set_aspect('equal')
    ax.set(xlim=(-.4, 1.7), ylim=(-.5, 1.2), xlabel=r'$x_1$', ylabel=r'$x_2$')
    ax.set_title('(a) 固定步长0.1的前40步')
    ax = axes[1]
    facts = {'f': '|x1|+2|x2|', 'x0': list(x0), 'R': R, 'G': G, 'T': T,
             'subgradient_choice': '(sign x1, 2 sign x2) with sign(0)=0', 'best_gap_at_T': {}}
    tt = np.arange(1, T + 1)
    for lab, (st, c, ls) in runs.items():
        _, fs = _subgrad_run(x0, st, T)
        best = np.minimum.accumulate(fs)
        ax.loglog(tt, best, color=c, ls=ls, lw=1.1, label=lab)
        facts['best_gap_at_T'][lab] = float(best[-1])
    ax.loglog(tt, R*G/np.sqrt(tt), color=MUTED, lw=.7, ls=':', label=r'$RG/\sqrt{T}$')
    ax.set(xlabel='迭代次数 T', ylabel='历史最佳目标差', ylim=(1e-4, 10))
    ax.legend(loc='lower left', handlelength=1.8, fontsize=7)
    ax.set_title('(b) 三种步长')
    save(fig, D/'c4-subgrad-steps', 'figure', facts)


# ---------------------------------------------------------------- 4.3
def prox_subproblem():
    """Subproblem |w|+(w-z)^2/2 for z=0.5 and z=2 (eta=1): minimizers 0 and 1."""
    fig, axes = figure(width_mm=112, height_mm=46, ncols=2, sharey=True)
    w = np.linspace(-1, 3, 401)
    for ax, z, p, title in [(axes[0], .5, 0., r'(a) $z=0.5$'), (axes[1], 2., 1., r'(b) $z=2$')]:
        _axes_through_origin(ax)
        ax.plot(w, np.abs(w), color=GREEN, lw=.9, ls='--', label=r'$|w|$')
        ax.plot(w, (w - z)**2/2, color=PURPLE, lw=.9, ls=':', label=r'$(w-z)^2/2$')
        ax.plot(w, np.abs(w) + (w - z)**2/2, color=BLUE, lw=1.4, label='子问题目标')
        ax.plot([p], [abs(p) + (p - z)**2/2], 'o', color=RED, ms=3.2)
        ax.plot([z], [0], 'v', color=INK, ms=3.2)
        ax.text(z + .05, .12, r'$z$', fontsize=8)
        ax.text(p + .06, abs(p) + (p - z)**2/2 - .38, r'$p=%g$' % p, color=RED, fontsize=7.5)
        ax.set(xlim=(-1, 3), ylim=(-.3, 3.2), xlabel=r'$w$')
        ax.set_title(title)
    axes[0].legend(loc='upper left', handlelength=1.6, fontsize=7)
    save(fig, D/'c4-prox-subproblem', 'figure', {
        'r': '|w|', 'eta': 1, 'centers': [.5, 2], 'minimizers': [0, 1],
        'balance': 'z-p in d|.|(p): 0.5 in [-1,1]; 1 = sign(1)'})


def prox_maps():
    """Three proximal maps on the line with the same parameter 1."""
    fig, ax = figure(width_mm=86, height_mm=56)
    z = np.linspace(-3, 3, 601)
    _axes_through_origin(ax)
    ax.plot(z, z, color=MUTED, lw=.6, ls=':', label='恒等')
    ax.plot(z, np.sign(z)*np.maximum(np.abs(z) - 1, 0), color=BLUE, lw=1.4, label='软阈值')
    ax.plot(z, z/2, color=GREEN, lw=1.1, ls='--', label='二次收缩')
    ax.plot(z, np.clip(z, -1, 1), color=YELLOW, lw=1.1, ls='-.', label='区间投影')
    ax.set(xlim=(-3, 3), ylim=(-2.2, 2.2), xlabel='中心 z', ylabel=r'$\mathrm{prox}(z)$')
    ax.legend(loc='upper left', handlelength=1.8, fontsize=7)
    save(fig, D/'c4-prox-maps', 'figure', {
        'eta': 1, 'soft_threshold': 'sign(z) max(|z|-1,0)', 'ridge': 'z/2',
        'projection': 'clip(z,-1,1)', 'sample_z': [3, .4, -2],
        'sample_outputs': {'soft': [2, 0, -1], 'ridge': [1.5, .2, -1], 'projection': [1, .4, -1]}})


def prox_point():
    """Proximal point (eta=1) vs subgradient (eta=1) on |x| from 2.5."""
    fig, axes = figure(width_mm=112, height_mm=46, ncols=2, gridspec_kw={'width_ratios': [1.25, 1]})
    ax = axes[0]
    _axes_through_origin(ax)
    w = np.linspace(-1, 3, 401)
    ax.plot(w, np.abs(w), color=INK, lw=1.2)
    centers = [2.5, 1.5, .5]
    cols = [BLUE, GREEN, PURPLE]
    for c, col in zip(centers, cols):
        p = np.sign(c)*max(abs(c) - 1, 0)
        ax.plot(w, np.abs(w) + (w - c)**2/2, color=col, lw=.9, ls='--')
        ax.plot([p], [abs(p) + (p - c)**2/2], 'o', color=col, ms=3)
        ax.plot([c], [abs(c)], 's', color=col, ms=2.6)
    ax.text(2.55, 2.2, r'$\mathbf{x}^{(0)}$', color=BLUE, fontsize=7.5)
    ax.set(xlim=(-1, 3), ylim=(-.2, 3.2), xlabel=r'$x$')
    ax.set_title('(a) 每轮的邻近子问题')
    ax = axes[1]
    T = 8
    pp = [2.5]
    sg = [2.5]
    for t in range(T):
        x = pp[-1]
        pp.append(np.sign(x)*max(abs(x) - 1, 0))
        x = sg[-1]
        sg.append(x - np.sign(x))
    ax.axhline(0, color=GRID, lw=.6)
    ax.plot(range(T + 1), sg, '-o', color=YELLOW, lw=.9, ms=2.6, label='次梯度法')
    ax.plot(range(T + 1), pp, '-s', color=BLUE, lw=1.1, ms=2.6, label='邻近点法')
    ax.set(xlabel=r'$t$', ylabel=r'$x^{(t)}$', ylim=(-.8, 2.8))
    ax.legend(loc='upper right', handlelength=1.6, fontsize=7)
    ax.set_title('(b) 迭代值（步长1）')
    save(fig, D/'c4-prox-point', 'figure', {
        'f': '|x|', 'eta': 1, 'x0': 2.5, 'proximal_point': [float(v) for v in pp],
        'subgradient_constant_step': [float(v) for v in sg]})


# ---------------------------------------------------------------- 4.4
Q = np.array([[2., 1.], [1., 1.]])
q = np.array([3., 1.])
LAM = 1.0
CONST = 2.5  # 0.5*||b||^2 with A=[[1,1],[1,0]], b=(1,2)


def lasso_F(x):
    return .5*x@Q@x - q@x + CONST + LAM*np.abs(x).sum()


def soft(z, k):
    return np.sign(z)*np.maximum(np.abs(z) - k, 0)


def ista(x0, eta, T, accel=False):
    x = np.array(x0, float)
    xprev = x.copy()
    y = x.copy()
    tk = 1.
    xs = [x.copy()]
    for _ in range(T):
        base = y if accel else x
        xn = soft(base - eta*(Q@base - q), eta*LAM)
        if accel:
            tn = (1 + np.sqrt(1 + 4*tk*tk))/2
            y = xn + (tk - 1)/tn*(xn - x)
            tk = tn
        xprev, x = x, xn
        xs.append(x.copy())
    return np.array(xs)


def lasso_path():
    """Proximal gradient path on a 2-D Lasso with A=[[1,1],[1,0]], b=(1,2), lambda=1,
    compared with plain gradient descent on the smooth part alone."""
    fig, ax = figure(width_mm=100, height_mm=74)
    X, Y = np.meshgrid(np.linspace(-1.4, 2.5, 400), np.linspace(-1.3, 2.3, 400))
    Z = .5*(2*X*X + 2*X*Y + Y*Y) - 3*X - Y + CONST + LAM*(np.abs(X) + np.abs(Y))
    ax.contour(X, Y, Z, levels=[1.6, 1.8, 2.2, 2.8, 3.6, 4.6, 6, 7.5], colors=[GRID], linewidths=.6)
    ax.axhline(0, color=MUTED, lw=.6, ls=':')
    ax.axvline(0, color=MUTED, lw=.6, ls=':')
    eta = .25
    x0 = np.array([-1., 2.])
    P = ista(x0, eta, 30)
    G = [x0.copy()]
    for _ in range(30):
        G.append(G[-1] - eta*(Q@G[-1] - q))
    G = np.array(G)
    ax.plot(G[:, 0], G[:, 1], '--', color=YELLOW, lw=.9, label='只对光滑项的梯度下降')
    ax.plot(G[:, 0], G[:, 1], 'o', color=YELLOW, ms=1.6)
    ax.plot(P[:, 0], P[:, 1], '-o', color=BLUE, lw=.9, ms=2.2, label='邻近梯度')
    on_axis = np.abs(P[:, 1]) < 1e-15
    ax.plot(P[on_axis, 0], P[on_axis, 1], 'o', color=RED, ms=2.6)
    c = x0 - eta*(Q@x0 - q)
    ax.annotate('', xy=c, xytext=x0, arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.0))
    ax.annotate('', xy=P[1], xytext=c, arrowprops=dict(arrowstyle='->', color=RED, lw=1.0))
    ax.text(x0[0] - .3, x0[1] + .1, r'$\mathbf{x}^{(0)}$', fontsize=8)
    ax.text(-.72, 2.08, '梯度步', color=PURPLE, fontsize=7.5)
    ax.text(c[0] + .1, c[1] + .02, '软阈值', color=RED, fontsize=7.5)
    ax.plot([1], [0], '*', color=RED, ms=7)
    ax.text(.92, -.25, '(1,0)', color=RED, fontsize=7.5)
    ax.plot([2], [-1], 'P', color=YELLOW, ms=4)
    ax.text(2.07, -1.05, '(2,-1)', color=YELLOW, fontsize=7.5)
    ax.set_aspect('equal')
    ax.set(xlim=(-1.4, 2.5), ylim=(-1.3, 2.3), xlabel=r'$x_1$', ylabel=r'$x_2$')
    ax.legend(loc='upper right', handlelength=1.6, fontsize=7)
    Fs = [lasso_F(x) for x in P]
    first_zero = int(np.argmax(on_axis)) if np.any(on_axis) else None
    save(fig, D/'c4-lasso-path', 'figure', {
        'objective': '0.5*||Ax-b||^2 + ||x||_1, A=[[1,1],[1,0]], b=(1,2)',
        'Q=A^T A': Q.tolist(), 'A^T b': q.tolist(), 'lambda': LAM, 'L': float(np.linalg.eigvalsh(Q).max()),
        'eta': eta, 'x0': x0.tolist(), 'center0': c.tolist(),
        'prox_grad_first8': [[round(float(v), 6) for v in x] for x in P[:9]],
        'x_star': [1, 0], 'F_star': 1.5, 'prox_grad_first_iter_with_x2_zero': first_zero,
        'prox_grad_F_first9': [round(v, 5) for v in Fs[:9]], 'prox_grad_x_30': P[30].tolist(),
        'smooth_only_minimizer': [2, -1], 'smooth_only_x_30': G[30].tolist()})


def ista_fista():
    """Objective gaps of proximal gradient vs FISTA on a seeded Lasso instance."""
    rng = np.random.default_rng(SEED)
    n, d = 60, 100
    A = rng.standard_normal((n, d))
    A[:, 1::2] = .9*A[:, ::2] + .45*rng.standard_normal((n, d//2))   # correlated columns
    xtrue = np.zeros(d)
    xtrue[rng.choice(d, 8, replace=False)] = rng.standard_normal(8)*2
    b = A@xtrue + .1*rng.standard_normal(n)
    lam = .1*np.abs(A.T@b).max()
    L = float(np.linalg.eigvalsh(A.T@A).max())
    eta = 1/L

    def F(x):
        r = A@x - b
        return .5*r@r + lam*np.abs(x).sum()

    def run(T, accel):
        x = np.zeros(d); y = x.copy(); tk = 1.; vals = [F(x)]
        for _ in range(T):
            base = y if accel else x
            xn = soft(base - eta*(A.T@(A@base - b)), eta*lam)
            if accel:
                tn = (1 + np.sqrt(1 + 4*tk*tk))/2
                y = xn + (tk - 1)/tn*(xn - x)
                tk = tn
            x = xn
            vals.append(F(x))
        return np.array(vals), x
    _, xref = run(30000, True)
    Fstar = F(xref)
    T = 600
    vi, _ = run(T, False)
    va, _ = run(T, True)
    R2 = float(np.sum(xref**2))
    t = np.arange(1, T + 1)
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1.3, 1]})
    ax = axes[0]
    ax.loglog(t, vi[1:] - Fstar, color=BLUE, lw=1.1, label='邻近梯度')
    ax.loglog(t, va[1:] - Fstar, color=GREEN, lw=1.1, label='加速邻近梯度')
    ax.loglog(t, L*R2/(2*t), color=BLUE, lw=.6, ls=':', label=r'$LR^2/(2t)$')
    ax.loglog(t, 2*L*R2/(t + 1)**2, color=GREEN, lw=.6, ls=':', label=r'$2LR^2/(t+1)^2$')
    ax.set(xlabel='迭代次数 t', ylabel='目标差', ylim=(1e-8, 1e5))
    ax.legend(loc='lower left', fontsize=6.8, handlelength=1.6)
    ax.set_title('(a) 目标差与保证界')
    ax = axes[1]
    lo, hi = 80, 260
    ax.semilogy(np.arange(lo, hi), va[lo:hi] - Fstar, color=GREEN, lw=1.1)
    ax.semilogy(np.arange(lo, hi), vi[lo:hi] - Fstar, color=BLUE, lw=1.1)
    ax.set(xlabel='迭代次数 t')
    ax.set_title('(b) 局部放大')
    inc = int(np.sum(np.diff(va) > 0))
    save(fig, D/'c4-ista-fista', 'figure', {
        'seed': SEED, 'n': n, 'd': d, 'design': 'standard normal, odd columns = 0.9*even + 0.45*noise',
        'sparsity_true': 8, 'noise_sd': .1, 'lambda': float(lam), 'L': L, 'eta': eta,
        'x0': 'zeros', 'reference_iterations': 30000, 'F_star_estimate': float(Fstar),
        'R2=||x0-xref||^2': R2, 'T': T, 'fista_increase_count': inc,
        'gap_at_T': {'prox_grad': float(vi[-1] - Fstar), 'fista': float(va[-1] - Fstar)},
        'gap_at_100': {'prox_grad': float(vi[100] - Fstar), 'fista': float(va[100] - Fstar)}})


# ---------------------------------------------------------------- 4.5
def smooth_max():
    """|x| vs log-sum-exp smoothing and Huber (Moreau envelope), nu=0.5, with derivatives."""
    nu = .5
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    x = np.linspace(-2, 2, 801)
    lse = nu*np.logaddexp(x/nu, -x/nu)
    hub = np.where(np.abs(x) <= nu, x*x/(2*nu), np.abs(x) - nu/2)
    ax = axes[0]
    _axes_through_origin(ax)
    ax.plot(x, np.abs(x), color=INK, lw=1.2, label=r'$|x|$')
    ax.plot(x, lse, color=BLUE, lw=1.1, ls='--', label='对数和指数')
    ax.plot(x, hub, color=GREEN, lw=1.1, ls='-.', label='Huber')
    ax.annotate('', xy=(0, nu*np.log(2)), xytext=(0, 0), arrowprops=dict(arrowstyle='<->', color=BLUE, lw=.7))
    ax.text(.07, .1, r'$\nu\log2$', color=BLUE, fontsize=7.5)
    ax.set(xlim=(-2, 2), ylim=(-.3, 2.1), xlabel=r'$x$')
    ax.legend(loc='upper center', fontsize=7, handlelength=1.6)
    ax.set_title('(a) 函数值（ν=0.5）')
    ax = axes[1]
    _axes_through_origin(ax)
    ax.plot(x, np.sign(x), color=INK, lw=1.2)
    ax.plot(x, np.tanh(x/nu), color=BLUE, lw=1.1, ls='--')
    ax.plot(x, np.clip(x/nu, -1, 1), color=GREEN, lw=1.1, ls='-.')
    ax.text(.55, -.55, '斜率 1/ν', color=GREEN, fontsize=7.5)
    ax.set(xlim=(-2, 2), ylim=(-1.3, 1.3), xlabel=r'$x$')
    ax.set_title('(b) 导数')
    save(fig, D/'c4-smooth-max', 'figure', {
        'nu': nu, 'lse': 'nu*log(exp(x/nu)+exp(-x/nu))', 'lse_gap_max': float(nu*np.log(2)),
        'huber': 'x^2/(2nu) if |x|<=nu else |x|-nu/2', 'huber_gap_max': nu/2,
        'derivatives': {'lse': 'tanh(x/nu)', 'huber': 'clip(x/nu,-1,1)'}, 'max_curvature': 1/nu})


ANG = np.deg2rad([0, 72, 144, 216, 288])
AMAT = np.stack([np.cos(ANG), np.sin(ANG)], 1)
BVEC = np.array([0., .3, -.2, .5, .1])


def _pmax(x):
    return np.max(AMAT@x + BVEC)


def _lse(x, nu):
    v = (AMAT@x + BVEC)/nu
    m = v.max()
    w = np.exp(v - m)
    return nu*(m + np.log(w.sum())), (w/w.sum())@AMAT


def smoothing_budget():
    """Gradient descent on the log-sum-exp smoothing of a 5-piece max in the plane."""
    res = linprog(c=[0, 0, 1], A_ub=np.hstack([AMAT, -np.ones((5, 1))]), b_ub=-BVEC,
                  bounds=[(None, None)]*3, method='highs')
    Fstar = float(res.fun)
    x0 = np.array([3., 2.])
    T = 3000
    fig, ax = figure(width_mm=100, height_mm=56)
    facts = {'pieces_a': AMAT.round(6).tolist(), 'pieces_b': BVEC.tolist(), 'm': 5,
             'F_star_LP': Fstar, 'x_star_LP': res.x[:2].tolist(), 'x0': x0.tolist(), 'T': T,
             'step': 'eta=nu (L_nu<=max||a_i||^2/nu=1/nu)', 'runs': {}}
    cols = {1.: BLUE, .1: GREEN, .01: PURPLE}
    t = np.arange(T + 1)
    for nu, c in cols.items():
        x = x0.copy(); gaps = []; surr = []
        for _ in range(T + 1):
            Fn, g = _lse(x, nu)
            gaps.append(_pmax(x) - Fstar); surr.append(Fn)
            x = x - nu*g
        gaps = np.array(gaps)
        ax.loglog(t[1:], gaps[1:], color=c, lw=1.1, label=r'$\nu=%g$' % nu)
        ax.axhline(nu*np.log(5), color=c, lw=.6, ls=':')
        facts['runs'][str(nu)] = {'bias_bound': float(nu*np.log(5)), 'gap_at_10': float(gaps[10]),
                                  'gap_at_100': float(gaps[100]), 'gap_at_T': float(gaps[-1])}
    ax.set(xlabel='迭代次数 t', ylabel='目标差', ylim=(1e-3, 6))
    ax.legend(loc='lower left', fontsize=7, handlelength=1.6)
    # search for a step where the surrogate decreases but the original objective increases
    nu = 1.
    x = x0.copy(); found = None
    for k in range(T):
        Fn, g = _lse(x, nu)
        xn = x - nu*g
        if _lse(xn, nu)[0] < Fn and _pmax(xn) > _pmax(x) + 1e-12:
            found = {'iter': k, 'x': x.tolist(), 'x_next': xn.tolist(), 'F': _pmax(x), 'F_next': _pmax(xn),
                     'F_nu': Fn, 'F_nu_next': _lse(xn, nu)[0]}
            break
    facts['surrogate_down_original_up_nu1'] = found
    save(fig, D/'c4-smoothing-budget', 'figure', facts)


# ---------------------------------------------------------------- 4.6
def _cauchy(w, ys=(0., 0., 10.)):
    return .5*sum(np.log1p((w - y)**2) for y in ys)


def mm_surrogates():
    """(a) Majorizer vs tangent for x^2/2 at 1; (b) IRLS/MM surrogates for the Cauchy fit of 0,0,10."""
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1, 1.3]})
    ax = axes[0]
    _axes_through_origin(ax)
    x = np.linspace(-1, 2.2, 300)
    ax.plot(x, x*x/2, color=BLUE, lw=1.4, label=r'$F=x^2/2$')
    ax.plot(x, (x - .5)**2 + .25, color=GREEN, lw=1.1, ls='--', label='主化代理')
    ax.plot(x, x - .5, color=PURPLE, lw=1.0, ls=':', label='切线')
    ax.plot([1], [.5], 'o', color=INK, ms=3)
    ax.plot([.5], [.25], 'o', color=GREEN, ms=3)
    ax.plot([.5], [.125], 'o', color=BLUE, ms=3)
    ax.set(xlim=(-1, 2.2), ylim=(-1, 2.5), xlabel=r'$x$')
    ax.legend(loc='upper left', fontsize=7, handlelength=1.6)
    ax.set_title('(a) 当前点 x=1')
    ax = axes[1]
    ys = np.array([0., 0., 10.])
    w = np.linspace(-3, 12, 800)
    ax.plot(w, _cauchy(w), color=BLUE, lw=1.4)
    wt = 4.
    its = [wt]
    cols = [GREEN, PURPLE, YELLOW]
    facts_it = []
    for k in range(3):
        a = 1/(1 + (wt - ys)**2)
        Fw = _cauchy(wt)
        Qw = Fw + .5*np.sum(a*((w[:, None] - ys)**2 - (wt - ys)**2), axis=1)
        wn = float(a@ys/a.sum())
        ax.plot(w, Qw, color=cols[k], lw=.9, ls='--')
        ax.plot([wt], [Fw], 'o', color=cols[k], ms=3)
        facts_it.append({'w': wt, 'weights': a.round(6).tolist(), 'w_next': wn, 'F': float(Fw)})
        wt = wn
        its.append(wt)
    ax.plot(its, [_cauchy(v) for v in its], 'k|', ms=5)
    for k, v in enumerate(its[:3]):
        ax.text(v + .15, _cauchy(v) + .2, r'$w^{(%d)}$' % k, fontsize=7.5, color=cols[k])
    ax.set(xlim=(-3, 12), ylim=(0, 6.5), xlabel=r'$w$')
    ax.set_title('(b) Cauchy拟合，初值4')
    # local minima of the Cauchy objective
    mins = []
    for a_, b_ in [(-1, 2), (8, 12)]:
        r = minimize_scalar(_cauchy, bounds=(a_, b_), method='bounded', options={'xatol': 1e-10})
        mins.append({'w': float(r.x), 'F': float(r.fun)})
    w8 = 8.; seq8 = [w8]
    for _ in range(30):
        a = 1/(1 + (w8 - ys)**2); w8 = float(a@ys/a.sum()); seq8.append(w8)
    w0 = 0.; a = 1/(1 + (w0 - ys)**2)
    save(fig, D/'c4-mm-surrogates', 'figure', {
        'panel_a': {'F': 'x^2/2', 'majorizer': '(x-1/2)^2+1/4', 'tangent': 'x-1/2'},
        'panel_b': {'F': '0.5*sum log(1+(w-y_i)^2)', 'data': ys.tolist(),
                    'surrogate': 'F(w_t)+0.5*sum a_i((w-y_i)^2-(w_t-y_i)^2), a_i=1/(1+(w_t-y_i)^2)',
                    'iterations_from_4': facts_it, 'local_minima': mins,
                    'iterations_from_8_last': seq8[-1], 'first_step_from_0': float(a@ys/a.sum())}})


def _bundle_F(x):
    return np.abs(x - 1) + x*x/4


def _bundle_g(x):
    return x/2 + (1. if x >= 1 else -1.)


def _bundle_step(cuts, center, tau):
    """Exact minimizer of max_j(cut_j) + (x-center)^2/(2 tau) in one dimension."""
    cands = [center - tau*g for _, _, g in cuts]
    for i in range(len(cuts)):
        for j in range(i + 1, len(cuts)):
            yi, fi, gi = cuts[i]; yj, fj, gj = cuts[j]
            if abs(gi - gj) > 1e-14:
                cands.append(((fj - gj*yj) - (fi - gi*yi))/(gi - gj))
    model = lambda x: max(fy + g*(x - y) for y, fy, g in cuts)
    obj = lambda x: model(x) + (x - center)**2/(2*tau)
    best = min(cands, key=obj)
    return float(best), float(model(best))


def bundle_model():
    """Proximal bundle method on F(x)=|x-1|+x^2/4 with tau=1, beta=1/2, starting at -2."""
    tau, beta = 1., .5
    center = -2.
    cuts = [(center, float(_bundle_F(center)), _bundle_g(center))]
    log, snaps = [], []
    for k in range(6):
        cand, mval = _bundle_step(cuts, center, tau)
        delta = float(_bundle_F(center)) - mval
        Fc = float(_bundle_F(cand))
        serious = float(_bundle_F(center)) - Fc >= beta*delta
        s = (center - cand)/tau
        log.append({'k': k, 'center': center, 'candidate': round(cand, 6), 'model_at_cand': round(mval, 6),
                    'pred_decrease': round(delta, 6), 'F_center': round(float(_bundle_F(center)), 6),
                    'F_cand': round(Fc, 6), 'serious': bool(serious), 's': round(s, 6),
                    'e': round(delta - tau*s*s, 6), 'cut_slope_at_cand': _bundle_g(cand)})
        snaps.append((list(cuts), center, cand, mval, serious))
        cuts.append((cand, Fc, _bundle_g(cand)))
        if serious:
            center = cand
        if delta < 1e-9:
            break
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    specs = [(axes[0], 1, '(a) 第2次查询：实质步', (-2.5, 2.5), (-1.2, 4.5)),
             (axes[1], 2, '(b) 第3次查询：空步（局部放大）', (.3, 1.5), (-.05, .75))]
    for ax, k, title, xl, yl in specs:
        cuts_k, c, cand, mval, ser = snaps[k]
        xx = np.linspace(*xl, 600)
        _axes_through_origin(ax)
        ax.plot(xx, _bundle_F(xx), color=BLUE, lw=1.4)
        model = np.max([fy + g*(xx - y) for y, fy, g in cuts_k], axis=0)
        ax.plot(xx, model, color=GREEN, lw=1.0, ls='--')
        ax.plot(xx, model + (xx - c)**2/(2*tau), color=PURPLE, lw=.8, ls=':')
        for y, fy, g in cuts_k:
            ax.plot([y], [fy], 'o', color=GREEN, ms=2.6)
        ax.axhline(float(_bundle_F(c)), color=MUTED, lw=.5, ls=':')
        ax.plot([c], [_bundle_F(c)], 's', color=INK, ms=3.4)
        ax.plot([cand], [mval], 'x', color=RED, ms=4.5)
        ax.plot([cand], [_bundle_F(cand)], 'o', color=RED, ms=3.6)
        ax.set(xlim=xl, ylim=yl, xlabel=r'$x$')
        ax.set_title(title)
    axes[0].text(-2.3, 3.6, r'$F$', color=BLUE)
    axes[0].text(-1.3, -.9, '割平面模型', color=GREEN, fontsize=7.5)
    axes[0].text(1.3, 1.25, '模型加距离项', color=PURPLE, fontsize=7.5)
    axes[0].text(-.35, 1.25, '中心', fontsize=7.5)
    axes[1].text(.93, .33, r'$F(0.9)$', color=RED, fontsize=7.5)
    axes[1].text(.75, .02, '模型值', color=RED, fontsize=7.5)
    axes[1].text(1.03, .2, '中心', fontsize=7.5)
    save(fig, D/'c4-bundle-model', 'figure', {
        'F': '|x-1|+x^2/4', 'subgradient_oracle': 'x/2+1 if x>=1 else x/2-1', 'tau': tau, 'beta': beta,
        'x0': -2, 'x_star': 1, 'F_star': .25,
        'panels': {'a': 'cuts at -2,0; center 0; candidate 1', 'b': 'cuts at -2,0,1; center 1; candidate 0.9'},
        'log': log})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    abs_supports, max_affine_subdiff, clarke_abs, subgrad_not_descent, subgrad_steps,
    prox_subproblem, prox_maps, prox_point, lasso_path, ista_fista, smooth_max,
    smoothing_budget, mm_surrogates, bundle_model]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
