# coding: utf-8
"""Teaching charts for volume three, part "processes and trajectory evolution",
chapter 1 (discrete dynamical systems).

Every curve is produced by iterating the maps stated in the text with the
recorded parameters; high-precision reference orbits use Python's decimal
module.  Pseudo-random residuals use a fixed numpy seed.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch1.py [name ...]
"""
from pathlib import Path
from decimal import Decimal, getcontext
import sys
import numpy as np
from matplotlib.patches import Ellipse
from matplotlib.colors import ListedColormap

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import (figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, STROKE,
                     BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL)

D = Path(__file__).resolve().parent
SEED = 20261030


def logistic(r, x):
    return r * x * (1 - x)


# ---------------------------------------------------------------- 1.1
def dds_temperature_trajectory():
    """x_{n+1}=0.8x_n+0.4 from several initial values; deviation |x_n-2| on a log axis."""
    fig, axes = figure(width_mm=107, height_mm=46, ncols=2)
    n = np.arange(0, 21)
    starts = [(0.0, BLUE), (3.5, GREEN), (1.0, YELLOW)]
    facts = {'map': 'x_{n+1}=0.8 x_n+0.4', 'equilibrium': 2.0, 'orbits': {}}
    for x0, col in starts:
        x = [x0]
        for _ in n[1:]:
            x.append(0.8 * x[-1] + 0.4)
        x = np.array(x)
        axes[0].plot(n, x, 'o-', color=col, ms=2.2, lw=.9, label=rf'$x_0={x0:g}$')
        axes[1].semilogy(n, np.abs(x - 2), 'o-', color=col, ms=2.2, lw=.9)
        facts['orbits'][str(x0)] = [round(float(v), 6) for v in x[:7]]
    axes[0].axhline(2, color=MUTED, lw=.6, ls='--')
    axes[0].text(0.4, 2.08, r'$x_*=2$', color=MUTED, ha='left', va='bottom', fontsize=7.5)
    axes[0].set(xlabel=r'$n$', ylabel=r'$x_n$', xlim=(0, 20), ylim=(-0.1, 3.7))
    axes[0].set_title('(a) 轨迹趋向平衡')
    axes[0].legend(loc='lower right', handlelength=1.2)
    axes[1].set(xlabel=r'$n$', ylabel=r'$|x_n-2|$', xlim=(0, 20), ylim=(5e-3, 3))
    axes[1].set_title('(b) 偏差每步乘以0.8')
    axes[1].grid(True, which='major', axis='y')
    save(fig, D/'dds-temperature-trajectory', 'figure', facts)


def dds_history_moments():
    """Exponentially weighted moments S0,S1 close a 2-D linear recursion and give a local line."""
    rng = np.random.default_rng(SEED)
    a = 0.85
    N = 60
    j = np.arange(N + 1)
    u = 0.6 + 0.03 * j + 0.5 * np.sin(j / 6.0) + 0.15 * rng.standard_normal(N + 1)
    S0 = S1 = 0.0
    for k in range(N + 1):
        S0, S1 = a * S0 + u[k], a * (S1 + S0)
    # direct check of the closed recursion against the defining sums
    lag = N - j
    S0d, S1d = np.sum(a**lag * u), np.sum(a**lag * lag * u)
    # weighted LS line u ~ c0 + c1 (j - N) with weights a^{N-j} over the infinite past (finite here)
    w = a**lag
    G = np.array([[w.sum(), -(w * lag).sum()], [-(w * lag).sum(), (w * lag**2).sum()]])
    rhs = np.array([S0d, -S1d])
    c0, c1 = np.linalg.solve(G, rhs)
    fig, ax = figure(width_mm=100, height_mm=50)
    ax.bar(j, w * 1.0, width=.8, color=BLUE_FILL, lw=0, label='指数权重')
    ax.plot(j, u, 'o', color=INK, ms=2.0, label='输入')
    jj = np.linspace(N - 18, N, 50)
    ax.plot(jj, c0 + c1 * (jj - N), color=RED, lw=1.4, label='由状态读出的局部直线')
    ax.plot([N], [c0], 's', color=RED, ms=3.5)
    ax.set(xlabel=r'$j$', ylabel='数值', xlim=(-1, N + 1))
    ax.legend(loc='upper left', handlelength=1.4)
    save(fig, D/'dds-history-moments', 'figure', {
        'a': a, 'n': N, 'input': 'u_j=0.6+0.03j+0.5 sin(j/6)+0.15 N(0,1), seed %d' % SEED,
        'recursion': 'S0_n=a S0_{n-1}+u_n, S1_n=a(S1_{n-1}+S0_{n-1})',
        'S0_recursive_vs_direct': [round(S0, 6), round(float(S0d), 6)],
        'S1_recursive_vs_direct': [round(S1, 6), round(float(S1d), 6)],
        'local_line_intercept_slope': [round(float(c0), 4), round(float(c1), 4)]})


# ---------------------------------------------------------------- 1.2
def _ellipse_panel(ax, A, steps, title, color, extra=None, marker=None):
    t = np.linspace(0, 2 * np.pi, 400)
    circ = np.vstack([np.cos(t), np.sin(t)])
    for k, n in enumerate(steps):
        P = np.linalg.matrix_power(A, n) @ circ
        ax.plot(P[0], P[1], color=color if n else MUTED, lw=1.0 if n else .7,
                ls='-' if n else '--', alpha=1.0)
        if marker is not None:
            mark = np.linalg.matrix_power(A, n) @ np.array(marker)
            ax.plot(mark[0], mark[1], 'o', color=INK, ms=2.2)
            ax.text(mark[0], mark[1], f' {n}', fontsize=7, color=INK, va='bottom')
    if extra:
        extra(ax)
    ax.set_aspect('equal')
    ax.set(xlim=(-2.2, 2.2), ylim=(-2.2, 2.2))
    ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
    ax.axhline(0, color=GRID, lw=.4); ax.axvline(0, color=GRID, lw=.4)
    ax.set_title(title)


def dds_matrix_power_shapes():
    """Images of the unit circle under A^n for real, complex and Jordan spectra."""
    fig, axes = figure(width_mm=150, height_mm=54, ncols=3)
    V = np.array([[1.0, 1.0], [0.0, 1.0]]) / np.array([1.0, np.sqrt(2)])
    A1 = V @ np.diag([1.25, 0.6]) @ np.linalg.inv(V)
    th = np.pi / 6
    A2 = 0.85 * np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    A3 = np.array([[0.9, 0.5], [0.0, 0.9]])

    def eig_lines(ax):
        for v, c in [(V[:, 0], BLUE), (V[:, 1], GREEN)]:
            v = v / np.linalg.norm(v)
            ax.plot([-2.2 * v[0], 2.2 * v[0]], [-2.2 * v[1], 2.2 * v[1]], color=c, lw=.6, ls=':')

    def jordan_line(ax):
        ax.plot([-2.2, 2.2], [0, 0], color=YELLOW, lw=.8, ls=':')

    _ellipse_panel(axes[0], A1, [0, 1, 2, 3], '(a) 两个实特征值', BLUE, eig_lines)
    _ellipse_panel(axes[1], A2, [0, 2, 4, 6], '(b) 一对复特征值', GREEN, marker=(1.0, 0.0))
    _ellipse_panel(axes[2], A3, [0, 2, 4, 8], '(c) 二阶Jordan块', YELLOW, jordan_line, marker=(0.0, 1.0))
    save(fig, D/'dds-matrix-power-shapes', 'figure', {
        'A_real': np.round(A1, 4).tolist(), 'eigenvectors_real': np.round(V, 4).tolist(),
        'A_complex': '0.85*rotation(pi/6)', 'A_jordan': A3.tolist(),
        'steps': {'a': [0, 1, 2, 3], 'b': [0, 2, 4, 6], 'c': [0, 2, 4, 8]},
        'marker': 'image of (1,0) in panel b and of (0,1) in panel c under A^n'})


def dds_input_injection():
    """Stacked contributions a^{n-1-j} u_j of each input to x_n for x_{n+1}=0.8x_n+u_n."""
    a = 0.8
    u = np.array([1.0, 0.0, 0.0, 0.6, 0.6, 0.0, 0.0, 0.0, 1.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    N = len(u)
    n = np.arange(N + 1)
    contrib = np.zeros((N, N + 1))
    for jj in range(N):
        for k in range(jj + 1, N + 1):
            contrib[jj, k] = a**(k - 1 - jj) * u[jj]
    x = [0.0]
    for jj in range(N):
        x.append(a * x[-1] + u[jj])
    cols = [BLUE, GREEN, YELLOW, RED, PURPLE]
    fills = [BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL]
    fig, axes = figure(width_mm=107, height_mm=58, nrows=2, sharex=True,
                       gridspec_kw={'height_ratios': [1, 2.4]})
    axes[0].bar(np.arange(N), u, width=.5, color=MUTED)
    axes[0].set(ylabel=r'$u_j$', ylim=(0, 1.4))
    axes[0].set_yticks([0, 1])
    bottom = np.zeros(N + 1)
    k = 0
    for jj in range(N):
        if u[jj] == 0:
            continue
        axes[1].fill_between(n, bottom, bottom + contrib[jj], step=None, color=fills[k % 5], lw=0)
        axes[1].plot(n, bottom + contrib[jj], color=cols[k % 5], lw=.8)
        axes[1].text(jj + 1.1, bottom[jj + 1] + contrib[jj, jj + 1] * .55, rf'$u_{{{jj}}}$', fontsize=7, color=cols[k % 5])
        bottom = bottom + contrib[jj]
        k += 1
    axes[1].plot(n, x, 'o', color=INK, ms=2.2, label='递推值')
    axes[1].set(xlabel=r'$n$', ylabel=r'$x_n$', xlim=(0, N), ylim=(0, 2.2))
    axes[1].legend(loc='upper right', handlelength=1.0)
    save(fig, D/'dds-input-injection', 'figure', {
        'a': a, 'x0': 0, 'u': u.tolist(), 'x': [round(v, 5) for v in x],
        'check': 'sum of stacked contributions equals recursive x_n at every n',
        'max_abs_diff': float(np.max(np.abs(contrib.sum(0) - np.array(x))))})


# ---------------------------------------------------------------- 1.3
def _cobweb(ax, F, x0, steps, lo, hi, col):
    xs = np.linspace(lo, hi, 400)
    ax.plot(xs, F(xs), color=INK, lw=1.0)
    ax.plot([lo, hi], [lo, hi], color=MUTED, lw=.6)
    x = x0
    path_x, path_y = [x], [lo if lo > -0.5 else 0]
    path_x, path_y = [x], [x]
    for _ in range(steps):
        y = F(x)
        path_x += [x, y]
        path_y += [y, y]
        x = y
        if abs(x) > 10:
            break
    ax.plot(path_x, path_y, color=col, lw=.8)
    ax.plot([x0], [x0], 'o', color=col, ms=2.6)
    ax.set_aspect('equal')
    ax.set(xlim=(lo, hi), ylim=(lo, hi))


def dds_cobweb():
    """Cobwebs: logistic r=2.8 (converge), r=3.2 (period two), F(x)=x^2 around x=1."""
    fig, axes = figure(width_mm=150, height_mm=54, ncols=3)
    _cobweb(axes[0], lambda x: logistic(2.8, x), 0.1, 40, 0, 1, BLUE)
    axes[0].plot([1 - 1 / 2.8], [1 - 1 / 2.8], 's', color=INK, ms=2.6)
    axes[0].set_title('(a) 收敛到平衡')
    _cobweb(axes[1], lambda x: logistic(3.2, x), 0.1, 60, 0, 1, GREEN)
    d = np.sqrt(4.2 * 0.2)
    xp, xm = (4.2 + d) / 6.4, (4.2 - d) / 6.4
    axes[1].plot([xm, xp, xp, xm, xm], [xp, xp, xm, xm, xp], color=INK, lw=.9, ls='--')
    axes[1].plot([0.6875], [0.6875], 's', color=INK, ms=2.6, mfc='white')
    axes[1].set_title('(b) 趋向周期二轨道')
    sq = lambda x: x**2
    _cobweb(axes[2], sq, 1.05, 6, 0, 1.6, RED)
    _cobweb(axes[2], sq, 0.95, 12, 0, 1.6, BLUE)
    axes[2].plot([1], [1], 's', color=INK, ms=2.6, mfc='white')
    axes[2].set_title('(c) 离开不稳定平衡')
    for ax in axes:
        ax.set_xlabel(r'$x_n$')
    axes[0].set_ylabel(r'$x_{n+1}$')
    save(fig, D/'dds-cobweb', 'figure', {
        'a': 'logistic r=2.8, x0=0.1, fixed point 1-1/r=0.642857, derivative 2-r=-0.8',
        'b': 'logistic r=3.2, x0=0.1, 2-cycle (%.5f, %.5f), fixed point 0.6875 unstable' % (xm, xp),
        'c': 'F(x)=x^2, x0=1.05 (escape) and 0.95 (to 0), fixed point 1 with derivative 2'})


def dds_period_two_graph():
    """Graphs of F and F^2 for the logistic map at r=3.2."""
    r = 3.2
    xs = np.linspace(0, 1, 600)
    F = logistic(r, xs)
    F2 = logistic(r, F)
    d = np.sqrt((r + 1) * (r - 3))
    xp, xm = ((r + 1) + d) / (2 * r), ((r + 1) - d) / (2 * r)
    xf = 1 - 1 / r
    fig, ax = figure(width_mm=86, height_mm=72)
    ax.plot(xs, F, color=BLUE, lw=1.0, label=r'$F(x)$')
    ax.plot(xs, F2, color=GREEN, lw=1.2, label=r'$F^2(x)$')
    ax.plot([0, 1], [0, 1], color=MUTED, lw=.6)
    ax.plot([xm, xp], [xm, xp], 'o', color=GREEN, ms=3.2)
    ax.plot([xf], [xf], 's', color=INK, ms=3.0, mfc='white')
    ax.annotate(r'$x_-$', (xm, xm), xytext=(-12, 6), textcoords='offset points', fontsize=7.5, color=GREEN)
    ax.annotate(r'$x_+$', (xp, xp), xytext=(4, -10), textcoords='offset points', fontsize=7.5, color=GREEN)
    ax.annotate(r'$x_*$', (xf, xf), xytext=(-14, 2), textcoords='offset points', fontsize=7.5, color=INK)
    ax.set_aspect('equal')
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel=r'$x$')
    ax.legend(loc='upper left', handlelength=1.4)
    save(fig, D/'dds-period-two-graph', 'figure', {
        'r': r, 'fixed_point': xf, 'F_prime_at_fixed': 2 - r,
        'two_cycle': [xm, xp], 'multiplier': -r * r + 2 * r + 4})


def dds_transient_growth():
    """A_K=[[0.5,K],[0,0.5]]: Euclidean length of A_K^n (0,1) against rho^n."""
    fig, ax = figure(width_mm=100, height_mm=50)
    facts = {'x0': [0, 1], 'norms': {}, 'operator_norms': {}}
    n = np.arange(0, 16)
    for K, col, mk in [(0, BLUE, 'o'), (1, GREEN, 's'), (4, RED, '^')]:
        A = np.array([[0.5, K], [0, 0.5]])
        X = np.array([np.linalg.matrix_power(A, k) @ np.array([0.0, 1.0]) for k in n])
        nr = np.linalg.norm(X, axis=1)
        ax.semilogy(n, nr, mk + '-', color=col, ms=2.4, lw=.8, label=rf'$K={K}$')
        facts['norms'][str(K)] = [round(float(v), 4) for v in nr[:8]]
        facts['operator_norms'][str(K)] = [round(float(np.linalg.norm(np.linalg.matrix_power(A, k), 2)), 4) for k in n[:8]]
    ax.axhline(1, color=MUTED, lw=.6, ls=':')
    ax.set(xlabel=r'$n$', ylabel=r'$\|\mathbf{x}_n\|_2$', xlim=(0, 15))
    ax.legend(loc='lower left', handlelength=1.2)
    save(fig, D/'dds-transient-growth', 'figure', facts)


def dds_lyapunov_ellipses():
    """A=[[0.5,1],[0,0.5]]: level sets of V=x^T P x with A^T P A - P = -I and the orbit of (0,1)."""
    A = np.array([[0.5, 1.0], [0.0, 0.5]])
    P = np.array([[4 / 3, 8 / 9], [8 / 9, 116 / 27]])
    assert np.allclose(A.T @ P @ A - P, -np.eye(2))
    x = np.array([0.0, 1.0])
    orbit = [x]
    for _ in range(12):
        orbit.append(A @ orbit[-1])
    orbit = np.array(orbit)
    V = np.einsum('ij,jk,ik->i', orbit, P, orbit)
    fig, axes = figure(width_mm=107, height_mm=52, ncols=2)
    ax = axes[0]
    g = np.linspace(-1.6, 1.6, 300)
    XX, YY = np.meshgrid(g, g)
    VV = P[0, 0] * XX**2 + 2 * P[0, 1] * XX * YY + P[1, 1] * YY**2
    ax.contour(XX, YY, VV, levels=sorted(V[:6]), colors=[BLUE], linewidths=.7)
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(t), np.sin(t), color=MUTED, lw=.6, ls='--')
    ax.plot(orbit[:7, 0], orbit[:7, 1], 'o-', color=RED, ms=2.4, lw=.8)
    for k in range(3):
        ax.text(orbit[k, 0] + .05, orbit[k, 1] + .04, rf'$\mathbf{{x}}_{k}$', fontsize=7, color=RED)
    ax.set_aspect('equal')
    ax.set(xlim=(-1.3, 1.6), ylim=(-1.2, 1.3), xlabel=r'$x_1$', ylabel=r'$x_2$')
    ax.set_title('(a) 水平椭圆与单位圆')
    ax = axes[1]
    n = np.arange(len(orbit))
    ax.semilogy(n, np.sqrt(V), 'o-', color=BLUE, ms=2.4, lw=.8, label=r'$\sqrt{V(\mathbf{x}_n)}$')
    ax.semilogy(n, np.linalg.norm(orbit, axis=1), 's-', color=RED, ms=2.4, lw=.8, label=r'$\|\mathbf{x}_n\|_2$')
    ax.set(xlabel=r'$n$', xlim=(0, 12))
    ax.set_title('(b) 两种长度')
    ax.legend(loc='lower left', handlelength=1.2)
    save(fig, D/'dds-lyapunov-ellipses', 'figure', {
        'A': A.tolist(), 'P': P.tolist(), 'Q': 'I', 'V_orbit': [round(float(v), 4) for v in V[:7]],
        'euclid_orbit': [round(float(v), 4) for v in np.linalg.norm(orbit, axis=1)[:7]],
        'eigs_P': np.linalg.eigvalsh(P).tolist(), 'c_bound': 1 - 1 / np.linalg.eigvalsh(P)[-1]})


def dds_basin_estimate():
    """F(x1,x2)=(0.5x1+x2, 0.5x2+x1^2): numerical basin of 0 and certified sublevel set of V."""
    A = np.array([[0.5, 1.0], [0.0, 0.5]])
    P = np.array([[4 / 3, 8 / 9], [8 / 9, 116 / 27]])

    def F(x1, x2):
        return 0.5 * x1 + x2, 0.5 * x2 + x1**2

    def V(x1, x2):
        return P[0, 0] * x1**2 + 2 * P[0, 1] * x1 * x2 + P[1, 1] * x2**2

    g1 = np.linspace(-2.0, 1.5, 700)
    g2 = np.linspace(-1.6, 1.2, 560)
    X1, X2 = np.meshgrid(g1, g2)
    y1, y2 = X1.copy(), X2.copy()
    alive = np.ones_like(X1, bool)
    for _ in range(200):
        y1, y2 = F(y1, y2)
        bad = (np.abs(y1) > 1e3) | (np.abs(y2) > 1e3)
        alive &= ~bad
        y1 = np.where(bad, 1e3, y1); y2 = np.where(bad, 1e3, y2)
    conv = alive & (np.hypot(y1, y2) < 1e-6)
    # certified level: smallest V among grid points (not too close to 0) where Delta V >= 0
    h1 = np.linspace(-2.5, 2.5, 1601)
    H1, H2 = np.meshgrid(h1, h1)
    f1, f2 = F(H1, H2)
    dV = V(f1, f2) - V(H1, H2)
    mask = (dV >= 0) & (np.hypot(H1, H2) > 1e-3)
    cstar = float(V(H1, H2)[mask].min())
    c = 0.95 * cstar
    fig, ax = figure(width_mm=100, height_mm=70)
    ax.contourf(X1, X2, conv.astype(float), levels=[-.5, .5, 1.5], colors=['white', BLUE_FILL])
    ax.contour(X1, X2, V(X1, X2), levels=[c], colors=[BLUE], linewidths=1.1)
    ax.contour(H1, H2, dV, levels=[0], colors=[RED], linewidths=.7, linestyles='--')
    for x0, col in [((0.3, -0.15), GREEN), ((0.7, -0.75), YELLOW), ((0.2, 0.3), RED)]:
        o = [np.array(x0)]
        for _ in range(14):
            nx = np.array(F(*o[-1]))
            o.append(nx)
            if np.hypot(*nx) > 2.5:
                break
        o = np.array(o)
        ax.plot(o[:, 0], o[:, 1], 'o-', color=col, ms=2.2, lw=.7)
    ax.plot([0], [0], 's', color=INK, ms=3)
    ax.set_aspect('equal')
    ax.set(xlim=(-1.2, 1.5), ylim=(-1.1, 1.0), xlabel=r'$x_1$', ylabel=r'$x_2$')
    save(fig, D/'dds-basin-estimate', 'figure', {
        'map': 'F(x1,x2)=(0.5x1+x2, 0.5x2+x1^2)', 'V': 'x^T P x, P from A^T P A-P=-I',
        'grid_basin': '700x560 grid, 200 iterations, converged if |x|<1e-6',
        'certified_level_grid_estimate': cstar, 'drawn_level': c,
        'orbits_x0': {'inside_certified': (0.3, -0.15), 'in_basin_outside_certified': (0.7, -0.75),
                      'escaping': (0.2, 0.3)}})


# ---------------------------------------------------------------- 1.4
def dds_newton_basins():
    """Basins of the three roots of z^3=1 under Newton's map N(z)=(2z^3+1)/(3z^2)."""
    re = np.linspace(-1.6, 1.6, 900)
    im = np.linspace(-1.2, 1.2, 675)
    Z = re[None, :] + 1j * im[:, None]
    roots = np.exp(2j * np.pi * np.arange(3) / 3)
    with np.errstate(all='ignore'):
        for _ in range(60):
            Z = (2 * Z**3 + 1) / (3 * Z**2)
    idx = np.full(Z.shape, 3)
    for k, rt in enumerate(roots):
        idx[np.abs(Z - rt) < 1e-6] = k
    cmap = ListedColormap([BLUE, GREEN, YELLOW, 'white'])
    fig, ax = figure(width_mm=100, height_mm=76)
    ax.imshow(idx, extent=(re[0], re[-1], im[0], im[-1]), origin='lower', cmap=cmap, vmin=-.5, vmax=3.5,
              interpolation='nearest')
    for k, (rt, col) in enumerate(zip(roots, [BLUE, GREEN, YELLOW])):
        ax.plot(rt.real, rt.imag, 'o', color='white', ms=4, mec=INK, mew=.6)
    z = 0.35 + 0.45j
    path = [z]
    for _ in range(6):
        z = (2 * z**3 + 1) / (3 * z**2)
        path.append(z)
    path = np.array(path)
    ax.plot(path.real, path.imag, 'o-', color='white', ms=2.0, lw=.7)
    ax.set_aspect('equal')
    ax.set(xlabel=r'$\mathrm{Re}\,z$', ylabel=r'$\mathrm{Im}\,z$')
    frac = [float(np.mean(idx == k)) for k in range(4)]
    save(fig, D/'dds-newton-basins', 'figure', {
        'map': 'N(z)=(2z^3+1)/(3z^2)', 'grid': '900x675 on [-1.6,1.6]x[-1.2,1.2]',
        'iterations': 60, 'tolerance': 1e-6, 'area_fractions_roots_and_undecided': frac,
        'sample_orbit_start': '0.35+0.45i'})


def dds_bifurcation_branches():
    """Saddle-node branches of x+mu-x^2 and logistic fixed point / 2-cycle branches."""
    fig, axes = figure(width_mm=107, height_mm=50, ncols=2)
    ax = axes[0]
    mu = np.linspace(0, 1, 200)
    ax.plot(mu, np.sqrt(mu), color=BLUE, lw=1.2, label='稳定')
    ax.plot(mu, -np.sqrt(mu), color=RED, lw=1.0, ls='--', label='不稳定')
    ax.plot([0], [0], 'o', color=INK, ms=2.6)
    ax.axvspan(-0.5, 0, color=GRID, alpha=.35, lw=0)
    ax.text(-0.25, 0.55, '无平衡点', ha='center', fontsize=7.5, color=MUTED)
    ax.set(xlim=(-0.5, 1), ylim=(-1.1, 1.1), xlabel=r'$\mu$', ylabel=r'$x_*$')
    ax.set_title(r'(a) $F_\mu(x)=x+\mu-x^2$')
    ax.legend(loc='lower left', handlelength=1.4)
    ax = axes[1]
    r1 = np.linspace(2.5, 3.0, 100)
    r2 = np.linspace(3.0, 3.6, 150)
    ax.plot(r1, 1 - 1 / r1, color=BLUE, lw=1.2)
    ax.plot(r2, 1 - 1 / r2, color=RED, lw=1.0, ls='--')
    rs = np.linspace(3.0, 1 + np.sqrt(6), 150)
    ru = np.linspace(1 + np.sqrt(6), 3.6, 60)
    for rr, col, ls in [(rs, GREEN, '-'), (ru, RED, '--')]:
        d = np.sqrt((rr + 1) * (rr - 3))
        ax.plot(rr, ((rr + 1) + d) / (2 * rr), color=col, ls=ls, lw=1.1)
        ax.plot(rr, ((rr + 1) - d) / (2 * rr), color=col, ls=ls, lw=1.1)
    ax.axvline(3, color=GRID, lw=.6)
    ax.axvline(1 + np.sqrt(6), color=GRID, lw=.6)
    ax.text(3.0, 0.38, r'$r=3$', fontsize=7, color=MUTED, ha='right')
    ax.text(1 + np.sqrt(6) - 0.02, 0.38, r'$1+\sqrt{6}$', fontsize=7, color=MUTED, ha='right')
    ax.set(xlim=(2.5, 3.6), ylim=(0.35, 0.95), xlabel=r'$r$', ylabel=r'$x$')
    ax.set_title('(b) Logistic：平衡与周期二')
    save(fig, D/'dds-bifurcation-branches', 'figure', {
        'a': 'fixed points +-sqrt(mu), F\'=1-+2sqrt(mu)',
        'b': 'fixed point 1-1/r stable on (1,3); 2-cycle ((r+1)+-sqrt((r+1)(r-3)))/(2r) stable on (3,1+sqrt6)'})


def dds_logistic_bifurcation():
    """Orbit diagram of the logistic map and the finite-time Lyapunov exponent."""
    rs = np.linspace(2.5, 4.0, 1500)
    x = np.full_like(rs, 0.2)
    for _ in range(1000):
        x = logistic(rs, x)
    pts_r, pts_x = [], []
    lyap = np.zeros_like(rs)
    M = 400
    for _ in range(M):
        x = logistic(rs, x)
        lyap += np.log(np.abs(rs * (1 - 2 * x)) + 1e-300)
        pts_r.append(rs.copy()); pts_x.append(x.copy())
    lyap /= M
    fig, axes = figure(width_mm=150, height_mm=78, nrows=2, sharex=True,
                       gridspec_kw={'height_ratios': [2, 1]})
    axes[0].plot(np.concatenate(pts_r), np.concatenate(pts_x), ',', color=BLUE, alpha=.35, rasterized=True)
    for rv in [3.0, 1 + np.sqrt(6), 3.544090, 3.569946]:
        axes[0].axvline(rv, color=GRID, lw=.5)
    axes[0].set(ylabel=r'$x_n$', ylim=(0, 1))
    axes[1].plot(rs, lyap, color=INK, lw=.6)
    axes[1].axhline(0, color=MUTED, lw=.6)
    axes[1].axhline(np.log(2), color=RED, lw=.6, ls=':')
    axes[1].text(2.52, np.log(2) + 0.05, r'$\ln 2$', color=RED, fontsize=7)
    axes[1].set(xlabel=r'$r$', ylabel=r'$\lambda_{400}$', ylim=(-1.6, 1.0), xlim=(2.5, 4.0))
    save(fig, D/'dds-logistic-bifurcation', 'figure', {
        'r_grid': '1500 values on [2.5,4]', 'x0': 0.2, 'transient': 1000, 'plotted': M,
        'lyapunov': 'mean of log|r(1-2x_n)| over the plotted 400 steps',
        'reference_lines_r': [3.0, 1 + np.sqrt(6), 3.544090, 3.569946],
        'lambda_at_r4': float(lyap[-1])})


def _logistic_decimal(x0, r, n, prec=120):
    getcontext().prec = prec
    x = Decimal(x0); r = Decimal(r)
    out = [x]
    for _ in range(n):
        x = r * x * (1 - x)
        out.append(x)
    return out


def dds_sensitive_separation():
    """Two orbits of the r=4 logistic map from 0.2 and 0.2+1e-10 (computed at 120 digits)."""
    N = 50
    a = _logistic_decimal('0.2', 4, N)
    b = _logistic_decimal('0.2000000001', 4, N)
    n = np.arange(N + 1)
    xa = np.array([float(v) for v in a]); xb = np.array([float(v) for v in b])
    diff = np.array([float(abs(p - q)) for p, q in zip(a, b)])
    fig, axes = figure(width_mm=107, height_mm=62, nrows=2, sharex=True)
    axes[0].plot(n, xa, 'o-', color=BLUE, ms=1.8, lw=.6, label=r'$x_0=0.2$')
    axes[0].plot(n, xb, 's-', color=RED, ms=1.6, lw=.6, label=r'$x_0=0.2+10^{-10}$')
    axes[0].set(ylabel=r'$x_n$', ylim=(-0.05, 1.05))
    axes[0].legend(loc='upper left', ncols=2, handlelength=1.2, bbox_to_anchor=(0, 1.25))
    axes[1].semilogy(n, diff, 'o-', color=INK, ms=1.8, lw=.6, label='两轨道距离')
    axes[1].semilogy(n, 1e-10 * 2.0**n, color=GREEN, lw=.8, ls='--', label=r'$10^{-10}\cdot 2^n$')
    axes[1].set(xlabel=r'$n$', ylabel='距离', ylim=(1e-11, 3), xlim=(0, N))
    axes[1].legend(loc='lower right', handlelength=1.4)
    first = int(np.argmax(diff > 0.1))
    save(fig, D/'dds-sensitive-separation', 'figure', {
        'map': 'x_{n+1}=4x_n(1-x_n)', 'precision_digits': 120, 'x0': ['0.2', '0.2000000001'],
        'first_step_distance_exceeds_0.1': first, 'diff_first_10': [float(v) for v in diff[:10]]})


def dds_rounding_divergence():
    """Logistic r=4 from x0=0.2 in float32 and float64 against a 120-digit reference."""
    N = 80
    ref = np.array([float(v) for v in _logistic_decimal('0.2', 4, N)])
    out = {}
    for dt, name in [(np.float32, 'float32'), (np.float64, 'float64')]:
        x = dt(0.2); r = dt(4); one = dt(1)
        seq = [x]
        for _ in range(N):
            x = r * x * (one - x)
            seq.append(x)
        out[name] = np.array(seq, dtype=float)
    n = np.arange(N + 1)
    fig, ax = figure(width_mm=100, height_mm=50)
    for name, col, mk in [('float32', RED, 's'), ('float64', BLUE, 'o')]:
        err = np.abs(out[name] - ref)
        err = np.maximum(err, 1e-18)
        ax.semilogy(n, err, mk + '-', color=col, ms=1.6, lw=.6, label=name)
    ax.semilogy(n, 1.1e-16 * 2.0**n, color=GREEN, lw=.8, ls='--', label=r'$1.1\times10^{-16}\cdot2^n$')
    ax.set(xlabel=r'$n$', ylabel=r'$|\hat{x}_n-x_n|$', ylim=(1e-18, 3), xlim=(0, N))
    ax.legend(loc='lower right', handlelength=1.4)
    first = {k: int(np.argmax(np.abs(v - ref) > 0.1)) for k, v in out.items()}
    save(fig, D/'dds-rounding-divergence', 'figure', {
        'map': 'x_{n+1}=4x_n(1-x_n)', 'x0': 0.2, 'reference': 'decimal, 120 digits',
        'first_step_error_exceeds_0.1': first, 'floor_for_plot': 1e-18})


# ---------------------------------------------------------------- 1.5
def dds_error_bound():
    """Discrete Gronwall bound vs actual error: cos map with residuals, logistic r=4 in float64."""
    rng = np.random.default_rng(SEED)
    fig, axes = figure(width_mm=107, height_mm=50, ncols=2)
    # (a) contraction: x_{n+1}=cos x_n, perturbed iterate with |r_n|<=eta
    L, eta, N = 0.85, 1e-3, 40
    x, xh = 0.2, 0.3
    err = [abs(xh - x)]
    for _ in range(N):
        x = np.cos(x)
        xh = np.cos(xh) + eta * rng.choice([-1.0, 1.0]) * rng.uniform(0.5, 1.0)
        err.append(abs(xh - x))
    n = np.arange(N + 1)
    bound = L**n * 0.1 + eta * (1 - L**n) / (1 - L)
    ax = axes[0]
    ax.semilogy(n, err, 'o-', color=BLUE, ms=1.8, lw=.6, label='实际误差')
    ax.semilogy(n, bound, color=RED, lw=1.0, ls='--', label='递推上界')
    ax.axhline(eta / (1 - L), color=MUTED, lw=.6, ls=':')
    ax.set(xlabel=r'$n$', ylabel=r'$|\hat{x}_n-x_n|$', xlim=(0, N), ylim=(1e-5, 0.3))
    ax.set_title('(a) 收缩映射')
    ax.legend(loc='upper right', handlelength=1.4)
    # (b) expanding: logistic r=4 in float64 vs reference, bound with L=4, eta=2^-53*... per step
    N2 = 40
    ref = np.array([float(v) for v in _logistic_decimal('0.2', 4, N2)])
    xf = 0.2; seq = [xf]
    for _ in range(N2):
        xf = 4.0 * xf * (1.0 - xf); seq.append(xf)
    e2 = np.maximum(np.abs(np.array(seq) - ref), 1e-18)
    m = np.arange(N2 + 1)
    eta2 = 2.0**-52
    e02 = float(abs(Decimal(0.2) - Decimal('0.2')))
    b2 = 4.0**m * e02 + eta2 * (4.0**m - 1) / 3
    ax = axes[1]
    ax.semilogy(m, e2, 'o-', color=BLUE, ms=1.8, lw=.6, label='实际误差')
    ax.semilogy(m, np.minimum(b2, 1e3), color=RED, lw=1.0, ls='--', label='递推上界')
    ax.semilogy(m, 1.1e-16 * 2.0**m, color=GREEN, lw=.8, ls=':', label=r'$\propto 2^n$')
    ax.set(xlabel=r'$n$', xlim=(0, N2), ylim=(1e-18, 10))
    ax.set_title('(b) 扩张映射')
    ax.legend(loc='lower right', handlelength=1.4)
    save(fig, D/'dds-error-bound', 'figure', {
        'a': {'map': 'cos', 'x0': 0.2, 'xhat0': 0.3, 'L_used': L, 'eta': eta,
              'residuals': 'eta*sign*U(0.5,1), seed %d' % SEED, 'limit_bound': eta / (1 - L)},
        'b': {'map': '4x(1-x)', 'x0': 0.2, 'reference': 'decimal 120 digits',
              'eta_per_step': eta2, 'e0': e02, 'bound': '4^n e0 + eta*(4^n-1)/3'}})


def dds_forced_response():
    """x_{n+1}=0.8x_n+u_n: nominal input 0.4, biased 0.45, decaying perturbation 0.4+0.3*0.7^n."""
    N = 30
    n = np.arange(N + 1)

    def run(x0, uf):
        x = [x0]
        for k in range(N):
            x.append(0.8 * x[-1] + uf(k))
        return np.array(x)

    nom = run(0.0, lambda k: 0.4)
    biased = run(1.0, lambda k: 0.45)
    decay = run(1.0, lambda k: 0.4 + 0.3 * 0.7**k)
    fig, axes = figure(width_mm=107, height_mm=48, ncols=2)
    ax = axes[0]
    ax.plot(n, nom, 'o-', color=BLUE, ms=1.8, lw=.7, label=r'$u_n=0.4,\ x_0=0$')
    ax.plot(n, biased, 's-', color=RED, ms=1.8, lw=.7, label=r'$u_n=0.45,\ x_0=1$')
    ax.plot(n, decay, '^-', color=GREEN, ms=1.8, lw=.7, label=r'$u_n=0.4+0.3\cdot0.7^n,\ x_0=1$')
    ax.set(xlabel=r'$n$', ylabel=r'$x_n$', xlim=(0, N), ylim=(0, 3.2))
    ax.set_title('(a) 三条轨迹')
    ax.legend(loc='lower right', handlelength=1.2, fontsize=7)
    ax = axes[1]
    ax.plot(n, biased - nom, 's-', color=RED, ms=1.8, lw=.7, label='持续偏差')
    ax.plot(n, decay - nom, '^-', color=GREEN, ms=1.8, lw=.7, label='衰减扰动')
    ax.axhline(0.25, color=MUTED, lw=.6, ls=':')
    ax.text(N, 0.21, r'$0.05/(1-0.8)=0.25$', ha='right', va='top', fontsize=7, color=MUTED)
    ax.set(xlabel=r'$n$', ylabel='与标称轨迹之差', xlim=(0, N), ylim=(0, 1.5))
    ax.set_title('(b) 状态差')
    ax.legend(loc='upper right', handlelength=1.2)
    save(fig, D/'dds-forced-response', 'figure', {
        'map': 'x_{n+1}=0.8x_n+u_n', 'final_differences': [round(float((biased - nom)[-1]), 5),
                                                          round(float((decay - nom)[-1]), 5)]})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    dds_temperature_trajectory, dds_history_moments, dds_matrix_power_shapes, dds_input_injection,
    dds_cobweb, dds_period_two_graph, dds_transient_growth, dds_lyapunov_ellipses, dds_basin_estimate,
    dds_newton_basins, dds_bifurcation_branches, dds_logistic_bifurcation, dds_sensitive_separation,
    dds_rounding_divergence, dds_error_bound, dds_forced_response]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
