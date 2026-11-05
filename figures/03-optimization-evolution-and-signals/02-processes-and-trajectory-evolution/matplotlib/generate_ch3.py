# coding: utf-8
"""Teaching charts for volume three, part "processes and trajectory evolution",
chapter 3 (partial differential equations).

All curves come from closed-form solutions, truncated eigenfunction series with
the stated number of modes, or the finite-difference / finite-volume schemes
recorded in each figure's facts file. No randomness is used.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch3.py [name ...]
"""
from pathlib import Path
import re
import sys
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Polygon

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import (figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, STROKE,
                     BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL)

D = Path(__file__).resolve().parent
TCOL = [BLUE, GREEN, YELLOW, RED, PURPLE]
HEAT = LinearSegmentedColormap.from_list('pde_heat', ['#FFFFFF', BLUE_FILL, BLUE, INK])

# ----------------------------------------------------------------- helpers
XQ = (np.arange(20000) + 0.5) / 20000      # midpoint nodes on (0,1)


def sine_coeffs(f, K):
    """b_k = 2 int_0^1 f(x) sin(k pi x) dx, midpoint rule with 20000 cells."""
    fx = f(XQ)
    k = np.arange(1, K + 1)
    return 2 * (np.sin(np.pi * np.outer(k, XQ)) @ fx) / XQ.size


def cosine_coeffs(f, K):
    """a_0 = int f, a_k = 2 int f cos(k pi x), k=1..K."""
    fx = f(XQ)
    k = np.arange(0, K + 1)
    a = 2 * (np.cos(np.pi * np.outer(k, XQ)) @ fx) / XQ.size
    a[0] /= 2
    return a


def heat_dirichlet(b, x, t, kappa=1.0):
    k = np.arange(1, b.size + 1)
    return (b * np.exp(-kappa * (k * np.pi) ** 2 * t)) @ np.sin(np.pi * np.outer(k, x))


def heat_neumann(a, x, t, kappa=1.0):
    k = np.arange(0, a.size)
    return (a * np.exp(-kappa * (k * np.pi) ** 2 * t)) @ np.cos(np.pi * np.outer(k, x))


def bump(x, c, w):
    return np.exp(-((x - c) / w) ** 2)


def smooth_box(x, a, b, eps=0.004):
    return 0.5 * (np.tanh((x - a) / eps) - np.tanh((x - b) / eps))


def lab(ax, s, x=0.0, y=1.02, **kw):
    """Panel label; CJK and $math$ pieces are drawn as separate, abutting texts
    because the pinned math font has no CJK glyphs."""
    parts = [q for q in re.split(r'(\$[^$]*\$)', s) if q]
    kw.setdefault('fontsize', 8)
    t = ax.text(x, y, parts[0], transform=ax.transAxes, ha='left', va='baseline', **kw)
    for q in parts[1:]:
        t = ax.annotate(q, xy=(1, 0), xycoords=t, ha='left', va='bottom', **kw)
    return t


# ----------------------------------------------------------------- 3.1
def rod_snapshots():
    """Heat equation on (0,1), Dirichlet zero, kappa=1, two-bump initial temperature."""
    u0 = lambda x: bump(x, .32, .07) + .6 * bump(x, .7, .05)
    K = 300
    b = sine_coeffs(u0, K)
    x = np.linspace(0, 1, 801)
    times = [0, .001, .004, .015]
    fig, ax = figure(width_mm=100, height_mm=46)
    for t, col in zip(times, TCOL):
        ax.plot(x, heat_dirichlet(b, x, t), color=col, lw=1.1, label=rf'$t={t:g}$')
    N = 11
    xj = np.arange(1, N + 1) / (N + 1)
    uj = heat_dirichlet(b, xj, times[2])
    ax.vlines(xj, 0, uj, color=MUTED, lw=.6)
    ax.plot(xj, uj, 'o', color=YELLOW, ms=3.2, mec=INK, mew=.5, label='网格值')
    ax.set(xlim=(0, 1), ylim=(0, 1.08), xlabel=r'$x$', ylabel=r'$u(x,t)$')
    ax.legend(loc='upper right', handlelength=1.4, ncol=1)
    save(fig, D/'pde-rod-snapshots', 'figure', {
        'equation': 'u_t=u_xx on (0,1), u(0,t)=u(1,t)=0',
        'u0': 'exp(-((x-.32)/.07)^2)+0.6*exp(-((x-.7)/.05)^2)',
        'method': f'sine series with {K} modes', 'times': times,
        'grid': {'N': N, 'h': 1 / (N + 1), 'sampled_time': times[2],
                 'values': [round(float(v), 4) for v in uj]}})


def three_mechanisms():
    """Same Gaussian bump under heat, transport and wave equations on the real line."""
    x0, s = 3.0, .25
    kappa, bspeed, c = .1, 1.0, 1.0
    u0 = lambda x: np.exp(-(x - x0) ** 2 / (2 * s ** 2))
    x = np.linspace(0, 6, 1201)
    times = [0, .5, 1.0, 1.5]
    fig, axes = figure(width_mm=150, height_mm=44, ncols=3, sharey=True)
    titles = [r'(a) 扩散 $u_t=\kappa u_{xx}$', r'(b) 输运 $u_t+bu_x=0$', r'(c) 波动 $u_{tt}=c^2u_{xx}$']
    for ax, title in zip(axes, titles):
        lab(ax, title)
        ax.set(xlim=(0, 6), ylim=(0, 1.08), xlabel=r'$x$')
    for t, col in zip(times, TCOL):
        var = s ** 2 + 2 * kappa * t
        heat = s / np.sqrt(var) * np.exp(-(x - x0) ** 2 / (2 * var))
        axes[0].plot(x, heat, color=col, label=rf'$t={t:g}$')
        axes[1].plot(x, u0(x - bspeed * t), color=col)
        axes[2].plot(x, .5 * (u0(x - c * t) + u0(x + c * t)), color=col)
    axes[0].set_ylabel(r'$u(x,t)$')
    axes[0].legend(loc='upper left', handlelength=1.2)
    save(fig, D/'pde-three-mechanisms', 'figure', {
        'u0': 'exp(-(x-3)^2/(2*0.25^2))', 'kappa': kappa, 'b': bspeed, 'c': c,
        'heat': 'exact Gaussian solution, variance s^2+2*kappa*t',
        'transport': 'u0(x-bt)', 'wave': "d'Alembert with zero initial velocity", 'times': times})


def boundary_conditions():
    """-u''=1 on (0,1), u(1)=0, left end Dirichlet, Robin u'(0)=alpha u(0), Neumann."""
    x = np.linspace(0, 1, 401)
    fig, ax = figure(width_mm=100, height_mm=48)
    cases = [(np.inf, BLUE, r'Dirichlet $u(0)=0$'), (2.0, GREEN, r"Robin $u'(0)=2u(0)$"),
             (0.0, YELLOW, r"Neumann $u'(0)=0$")]
    facts = {'equation': "-u''=1 on (0,1), u(1)=0", 'cases': {}}
    for alpha, col, name in cases:
        if np.isinf(alpha):
            A, B = .5, 0.0
        else:
            B = 1 / (2 * (1 + alpha)); A = alpha * B
        u = -x ** 2 / 2 + A * x + B
        ax.plot(x, u, color=col, label=name)
        # tangent segment at the left end
        xs = np.array([0, .16])
        ax.plot(xs, B + A * xs, color=col, lw=.6, ls=(0, (3, 2)))
        ax.plot([0], [B], 'o', color=col, ms=3, mec=INK, mew=.4)
        facts['cases'][str(alpha)] = {'u': f'-x^2/2+{A:.4f}x+{B:.4f}', 'u(0)': B, "u'(0)": A}
    ax.set(xlim=(0, 1), ylim=(0, .56), xlabel=r'$x$', ylabel=r'$u(x)$')
    ax.legend(loc='upper right', handlelength=1.4)
    ax.text(.04, .34, '虚线：左端切线', fontsize=7.5, color=MUTED)
    save(fig, D/'pde-boundary-conditions', 'figure', facts)


# ----------------------------------------------------------------- 3.2
def weak_form_test():
    """u = 1/2-|x-1/2| (kink), test bump phi on (0.2,0.8); compare int u' phi and -int u phi'."""
    x = np.linspace(0, 1, 40001)
    u = .5 - np.abs(x - .5)
    up = np.where(x < .5, 1.0, -1.0)
    a, b = .22, .82
    def phi_f(z):
        out = np.zeros_like(z)
        m = (z > a) & (z < b)
        s = (2 * z[m] - a - b) / (b - a)
        out[m] = np.exp(1 - 1 / (1 - s ** 2))
        return out
    phi = phi_f(x)
    sx = (2 * x - a - b) / (b - a)
    inside = np.abs(sx) < 1
    phip = np.zeros_like(x)
    phip[inside] = phi[inside] * (-2 * sx[inside] / (1 - sx[inside] ** 2) ** 2) * 2 / (b - a)
    I1 = float(np.trapezoid(up * phi, x))
    I2 = float(-np.trapezoid(u * phip, x))
    fig, axes = figure(width_mm=105, height_mm=44, ncols=2)
    ax = axes[0]
    lab(ax, r'(a) 带尖点的 $u$ 与测试函数 $\varphi$')
    ax.plot(x, u, color=BLUE, label=r'$u$')
    ax.plot(x, .45 * phi, color=GREEN, label=r'$0.45\,\varphi$')
    ax.set(xlim=(0, 1), ylim=(-0.02, .6), xlabel=r'$x$')
    ax.legend(loc='upper left', handlelength=1.2)
    ax = axes[1]
    lab(ax, r'(b) 两个被积函数')
    ax.fill_between(x, 0, up * phi, color=BLUE_FILL, lw=0)
    ax.plot(x, up * phi, color=BLUE, label=r"$u'\varphi$")
    ax.plot(x, -u * phip, color=GREEN, label=r"$-u\varphi'$")
    ax.axhline(0, color=GRID, lw=.6)
    ax.set(xlim=(0, 1), xlabel=r'$x$')
    ax.legend(loc='lower left', handlelength=1.2)
    save(fig, D/'pde-weak-form-test', 'figure', {
        'u': '1/2-|x-1/2|', "u'": 'sign step', 'phi': 'exp(1-1/(1-s^2)), s=(2x-a-b)/(b-a), a=.22, b=.82',
        'int_u_prime_phi': round(I1, 5), 'minus_int_u_phi_prime': round(I2, 5)})


def poisson_energy():
    """(a) -u''=f with zero Dirichlet data for three loads of unit total; (b) J(u+s w)."""
    x = np.linspace(0, 1, 801)
    G = lambda xx, y: np.where(xx <= y, xx * (1 - y), y * (1 - xx))
    u1 = x * (1 - x) / 2
    # f = 2 on [1/4,3/4]: u = int G(x,y) f(y) dy computed numerically
    yq = np.linspace(.25, .75, 4001)
    u2 = 2 * np.trapezoid(G(x[:, None], yq[None, :]), yq, axis=1)
    u3 = G(x, .5)
    fig, axes = figure(width_mm=105, height_mm=46, ncols=2)
    ax = axes[0]
    lab(ax, r'(a) 三种总量为 $1$ 的源')
    ax.plot(x, u1, color=BLUE, label=r'$f=1$')
    ax.plot(x, u2, color=GREEN, label=r'$f=2\cdot\mathbf{1}_{[1/4,3/4]}$')
    ax.plot(x, u3, color=YELLOW, label=r'$f=\delta_{1/2}$')
    ax.set(xlim=(0, 1), ylim=(0, .29), xlabel=r'$x$', ylabel=r'$u(x)$')
    ax.legend(loc='upper left', handlelength=1.2, fontsize=7)
    ax = axes[1]
    lab(ax, r'(b) $J(u+sw)$，$f=1$')
    s = np.linspace(-.06, .06, 401)
    J0 = -1 / 24
    for k, col in [(1, BLUE), (3, GREEN)]:
        ax.plot(s, J0 + s ** 2 * (k * np.pi) ** 2 / 4, color=col, label=rf'$w=\sin({k}\pi x)$' if k > 1 else r'$w=\sin(\pi x)$')
    ax.axhline(J0, color=MUTED, lw=.6, ls=(0, (3, 2)))
    ax.text(-.058, J0 + .0007, r'$J(u)=-1/24$', fontsize=7.5, color=MUTED)
    ax.set(xlim=(-.06, .06), ylim=(J0 - .002, J0 + .03), xlabel=r'$s$')
    ax.legend(loc='upper center', handlelength=1.2)
    save(fig, D/'pde-poisson-energy', 'figure', {
        'equation': "-u''=f, u(0)=u(1)=0", 'green': 'G(x,y)=min(x,y)(1-max(x,y))',
        'max_u': {'f=1': .125, 'f=2 on [1/4,3/4]': round(float(u2.max()), 5), 'delta_1/2': .25},
        'energy': "J(v)=1/2 int (v')^2 - int f v; J(u)=-1/24; J(u+s sin(k pi x))=J(u)+s^2 k^2 pi^2/4"})


def neumann():
    """(a) Neumann solutions u=cos(pi x)+c for f=pi^2 cos(pi x); (b) u_t=u_xx+1+pi^2 cos(pi x)."""
    x = np.linspace(0, 1, 401)
    fig, axes = figure(width_mm=105, height_mm=46, ncols=2)
    ax = axes[0]
    lab(ax, r'(a) $\int f=0$：解差一个常数')
    for c, col in [(-.5, GREEN), (0, BLUE), (.5, YELLOW)]:
        ax.plot(x, np.cos(np.pi * x) + c, color=col, label=rf'$c={c:g}$')
    ax.set(xlim=(0, 1), ylim=(-1.6, 1.6), xlabel=r'$x$', ylabel=r'$u=\cos(\pi x)+c$')
    ax.legend(loc='lower left', handlelength=1.2)
    ax = axes[1]
    lab(ax, r'(b) $\int f=1$：热量持续增加')
    for t, col in zip([.05, .2, .5, 1.0], TCOL):
        u = t + (1 - np.exp(-np.pi ** 2 * t)) * np.cos(np.pi * x)
        ax.plot(x, u, color=col, label=rf'$t={t:g}$')
    ax.set(xlim=(0, 1), ylim=(-1.1, 3.0), xlabel=r'$x$', ylabel=r'$u(x,t)$')
    ax.legend(loc='upper right', handlelength=1.2, ncol=2, columnspacing=.8)
    save(fig, D/'pde-neumann', 'figure', {
        'a': "-u''=pi^2 cos(pi x), u'(0)=u'(1)=0, solutions cos(pi x)+c",
        'b': 'u_t=u_xx+1+pi^2 cos(pi x), Neumann zero, u(x,0)=0; exact u=t+(1-exp(-pi^2 t))cos(pi x)'})


# ----------------------------------------------------------------- 3.3
def heat_modes():
    """(a) u0=sin(pi x)+0.5 sin(4 pi x) under u_t=u_xx; (b) mode amplitudes exp(-k^2 pi^2 t)."""
    x = np.linspace(0, 1, 401)
    fig, axes = figure(width_mm=105, height_mm=46, ncols=2)
    ax = axes[0]
    lab(ax, r'(a) 两个模式的叠加')
    for t, col in zip([0, .004, .015, .05], TCOL):
        u = np.exp(-np.pi ** 2 * t) * np.sin(np.pi * x) + .5 * np.exp(-16 * np.pi ** 2 * t) * np.sin(4 * np.pi * x)
        ax.plot(x, u, color=col, label=rf'$t={t:g}$')
    ax.set(xlim=(0, 1), ylim=(-.5, 2.2), xlabel=r'$x$', ylabel=r'$u(x,t)$')
    ax.legend(loc='upper center', handlelength=1.2, ncol=2, columnspacing=.8)
    ax = axes[1]
    lab(ax, r'(b) 模式振幅 $e^{-k^2\pi^2t}$')
    t = np.linspace(0, .15, 301)
    for k, col in zip([1, 2, 3, 4], TCOL):
        ax.semilogy(t, np.exp(-(k * np.pi) ** 2 * t), color=col, label=rf'$k={k}$')
    ax.set(xlim=(0, .15), ylim=(1e-6, 1.5), xlabel=r'$t$')
    ax.legend(loc='lower left', handlelength=1.2)
    save(fig, D/'pde-heat-modes', 'figure', {
        'equation': 'u_t=u_xx, Dirichlet zero on (0,1)', 'u0': 'sin(pi x)+0.5 sin(4 pi x)',
        'decay_rates': {k: round((k * np.pi) ** 2, 3) for k in range(1, 5)},
        'half_lives': {k: round(np.log(2) / (k * np.pi) ** 2, 5) for k in range(1, 5)}})


U0_STEP = lambda x: smooth_box(x, .15, .45) + .5 * smooth_box(x, .6, .8)


def heat_heatmap():
    """Space-time temperature for Dirichlet zero and Neumann zero boundaries."""
    K = 400
    b = sine_coeffs(U0_STEP, K)
    a = cosine_coeffs(U0_STEP, K)
    x = np.linspace(0, 1, 301)
    t = np.linspace(0, .1, 241)
    UD = np.array([heat_dirichlet(b, x, tt) for tt in t])
    UN = np.array([heat_neumann(a, x, tt) for tt in t])
    fig, axes = figure(width_mm=107, height_mm=50, ncols=2, sharey=True)
    for ax, U, title in [(axes[0], UD, r'(a) Dirichlet：$u=0$'), (axes[1], UN, r'(b) Neumann：$u_x=0$')]:
        im = ax.pcolormesh(x, t, U, cmap=HEAT, vmin=0, vmax=1, shading='auto', rasterized=True)
        lab(ax, title)
        ax.set(xlabel=r'$x$')
    axes[0].set_ylabel(r'$t$')
    cb = fig.colorbar(im, ax=axes, shrink=.85, pad=.02)
    cb.set_label(r'$u$')
    cb.outline.set_linewidth(.5)
    save(fig, D/'pde-heat-heatmap', 'figure', {
        'u0': '1 on [0.15,0.45], 0.5 on [0.6,0.8] (tanh-smoothed edges, width 0.004)', 'kappa': 1,
        'method': f'{K}-mode sine / cosine series', 'mean_u0': round(float(a[0]), 4),
        'final_time': .1, 'max_dirichlet_final': round(float(UD[-1].max()), 4),
        'neumann_final_range': [round(float(UN[-1].min()), 4), round(float(UN[-1].max()), 4)]})


def heat_energy_max():
    """(a) energy and total heat; (b) max/min of u0=sin(pi x)+sin(5 pi x) under heat flow."""
    K = 400
    b = sine_coeffs(U0_STEP, K)
    a = cosine_coeffs(U0_STEP, K)
    t = np.linspace(0, .2, 201)
    k = np.arange(1, K + 1)
    ED = np.array([.25 * np.sum(b ** 2 * np.exp(-2 * (k * np.pi) ** 2 * tt)) for tt in t])
    QD = np.array([np.sum(b * np.exp(-(k * np.pi) ** 2 * tt) * (1 - np.cos(k * np.pi)) / (k * np.pi)) for tt in t])
    QN = np.full_like(t, a[0])
    fig, axes = figure(width_mm=105, height_mm=46, ncols=2)
    ax = axes[0]
    lab(ax, r'(a) Dirichlet 能量与热量')
    ax.semilogy(t, ED / ED[0], color=BLUE, label=r'$E(t)/E(0)$')
    ax.semilogy(t, np.exp(-2 * np.pi ** 2 * t), color=BLUE, lw=.6, ls=(0, (3, 2)), label=r'$e^{-2\pi^2t}$')
    ax.semilogy(t, QD / QD[0], color=GREEN, label=r'$Q(t)/Q(0)$')
    ax.set(xlim=(0, .2), ylim=(1e-2, 1.3), xlabel=r'$t$')
    ax.legend(loc='lower left', handlelength=1.4)
    ax = axes[1]
    lab(ax, r'(b) 最大值与最小值')
    u0 = lambda z: np.sin(np.pi * z) + np.sin(5 * np.pi * z)
    x = np.linspace(0, 1, 801)
    tt = np.linspace(0, .03, 241)
    U = np.array([np.exp(-np.pi ** 2 * s) * np.sin(np.pi * x) + np.exp(-25 * np.pi ** 2 * s) * np.sin(5 * np.pi * x) for s in tt])
    ax.plot(tt, U.max(axis=1), color=RED, label=r'$M(t)=\max_x u$')
    ax.plot(tt, U.min(axis=1), color=PURPLE, label=r'$m(t)=\min_x u$')
    ax.axhline(0, color=GRID, lw=.6)
    ax.set(xlim=(0, .03), ylim=(-.4, 2.1), xlabel=r'$t$')
    ax.legend(loc='upper right', handlelength=1.4)
    save(fig, D/'pde-heat-energy-max', 'figure', {
        'a': {'u0': 'same as pde-heat-heatmap', 'E': '1/2 ||u||^2', 'Q': 'int u', 'Q_neumann_constant': round(float(a[0]), 4),
              'E_ratio_at_0.2': float(ED[-1] / ED[0]), 'Q_ratio_at_0.2': float(QD[-1] / QD[0])},
        'b': {'u0': 'sin(pi x)+sin(5 pi x)', 'max0': round(float(U[0].max()), 4), 'min0': round(float(U[0].min()), 4)}})


# ----------------------------------------------------------------- 3.4
def characteristics():
    """(a) constant speed b=0.6; (b) b(x)=0.6+0.4 sin(pi x) on [0,2], inflow value 0 at x=0."""
    u0 = lambda z: bump(z, .5, .15)
    bfun = lambda z: .6 + .4 * np.sin(np.pi * z)
    T = 2.0
    x = np.linspace(0, 2, 321)
    t = np.linspace(0, T, 241)
    fig, axes = figure(width_mm=107, height_mm=52, ncols=2, sharey=True)
    # (a)
    X, Tm = np.meshgrid(x, t)
    Ua = np.where(X - .6 * Tm >= 0, u0(X - .6 * Tm), 0.0)
    ax = axes[0]
    ax.pcolormesh(x, t, Ua, cmap=HEAT, vmin=0, vmax=1.15, shading='auto', rasterized=True)
    for y0 in np.arange(0, 2.01, .2):
        ax.plot(y0 + .6 * t, t, color=STROKE, lw=.5)
    for s0 in np.arange(.4, 2.01, .4):
        ax.plot(.6 * (t - s0), t, color=STROKE, lw=.5, ls=(0, (2, 2)))
    lab(ax, r'(a) 常速度 $b=0.6$')
    ax.set(xlim=(0, 2), ylim=(0, T), xlabel=r'$x$', ylabel=r'$t$')
    # (b) backward tracing with RK4
    def trace(xs, tau, sign):
        z = np.array(xs, dtype=float)
        n = 200
        h = sign * tau / n
        for _ in range(n):
            k1 = bfun(z); k2 = bfun(z + h * k1 / 2); k3 = bfun(z + h * k2 / 2); k4 = bfun(z + h * k3)
            z = z + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return z
    Ub = np.zeros_like(X)
    for i, tt in enumerate(t):
        y = trace(x, tt, -1)
        Ub[i] = np.where(y >= 0, u0(np.maximum(y, 0)), 0.0)
    ax = axes[1]
    ax.pcolormesh(x, t, Ub, cmap=HEAT, vmin=0, vmax=1.15, shading='auto', rasterized=True)
    for y0 in np.arange(0, 2.01, .2):
        path = [y0]
        z = np.array([y0])
        for k in range(1, t.size):
            z = trace(z, t[k] - t[k - 1], 1)
            path.append(z[0])
        ax.plot(path, t, color=STROKE, lw=.5)
    lab(ax, r'(b) $b(x)=0.6+0.4\sin(\pi x)$')
    ax.set(xlim=(0, 2), ylim=(0, T), xlabel=r'$x$')
    save(fig, D/'pde-characteristics', 'figure', {
        'u0': 'exp(-((x-0.5)/0.15)^2)', 'inflow_data': 'u(0,t)=0',
        'a': 'b=0.6, characteristics x=y+0.6t (solid from t=0, dashed from inflow boundary)',
        'b': 'b(x)=0.6+0.4 sin(pi x); RK4 tracing, 200 substeps'})


def transport_vs_continuity():
    """b(x)=-x: advected value u=u0(x e^t) versus density rho=e^t rho0(x e^t)."""
    x = np.linspace(-2.5, 2.5, 801)
    g = lambda z: np.exp(-z ** 2 / (2 * .6 ** 2))
    fig, axes = figure(width_mm=105, height_mm=46, ncols=2, sharey=True)
    for t, col in zip([0, .5, 1.0], TCOL):
        axes[0].plot(x, g(x * np.exp(t)), color=col, label=rf'$t={t:g}$')
        axes[1].plot(x, np.exp(t) * g(x * np.exp(t)), color=col)
    lab(axes[0], r'(a) $u_t-xu_x=0$：数值不变')
    lab(axes[1], r'(b) $\rho_t-(x\rho)_x=0$：质量不变')
    axes[0].set(xlim=(-2.5, 2.5), ylim=(0, 2.9), xlabel=r'$x$')
    axes[1].set(xlim=(-2.5, 2.5), xlabel=r'$x$')
    axes[0].legend(loc='upper left', handlelength=1.2)
    mass = [float(np.trapezoid(np.exp(t) * g(x * np.exp(t)), x)) for t in [0, .5, 1.0]]
    save(fig, D/'pde-transport-vs-continuity', 'figure', {
        'velocity': 'b(x)=-x', 'flow': 'X(t)=y e^{-t}', 'u0=rho0': 'exp(-x^2/(2*0.36))',
        'peak_rho': [1, round(np.exp(.5), 4), round(np.e, 4)], 'mass': [round(m, 4) for m in mass]})


def burgers():
    """Burgers u_t+(u^2/2)_x=0, u0=exp(-x^2): characteristics and shock vs multivalued profile."""
    u0 = lambda z: np.exp(-z ** 2)
    tstar = 1 / (np.sqrt(2) * np.exp(-.5))
    ystar = 1 / np.sqrt(2)
    fig, axes = figure(width_mm=107, height_mm=50, ncols=2)
    ax = axes[0]
    t = np.linspace(0, 3, 50)
    for y in np.arange(-2.5, 3.01, .25):
        ax.plot(y + u0(y) * t, t, color=BLUE if y < 0 else STROKE, lw=.55)
    xs = ystar + u0(ystar) * tstar
    ax.axhline(tstar, color=RED, lw=.6, ls=(0, (3, 2)))
    ax.plot([xs], [tstar], 'o', color=RED, ms=3.2)
    ax.text(-2.4, tstar + .08, rf'$t_*\approx{tstar:.3f}$', color=RED, fontsize=7.5,
            bbox=dict(fc='white', ec='none', pad=.6))
    lab(ax, r'(a) 特征线 $x=y+u_0(y)t$')
    ax.set(xlim=(-2.5, 4), ylim=(0, 3), xlabel=r'$x$', ylabel=r'$t$')
    # (b) Godunov scheme for the entropy solution
    L, R, N = -4.0, 6.0, 4000
    dx = (R - L) / N
    xc = L + (np.arange(N) + .5) * dx
    # cell averages of u0
    sub = (np.arange(8) + .5) / 8
    U = u0(xc[:, None] - dx / 2 + dx * sub[None, :]).mean(axis=1)
    T = 2.5
    tt = 0.0
    f = lambda q: q ** 2 / 2
    def godunov_flux(ul, ur):
        fl, fr = f(ul), f(ur)
        shock = ul > ur
        flux = np.where(ul <= ur, np.where(ul > 0, fl, np.where(ur < 0, fr, 0.0)), np.maximum(fl, fr))
        return np.where(shock, np.maximum(fl, fr), flux)
    while tt < T - 1e-12:
        dt = min(.45 * dx / max(np.abs(U).max(), 1e-9), T - tt)
        Ue = np.concatenate([[U[0]], U, [U[-1]]])
        F = godunov_flux(Ue[:-1], Ue[1:])
        U = U - dt / dx * (F[1:] - F[:-1])
        tt += dt
    ax = axes[1]
    y = np.linspace(-3, 4, 3001)
    ax.plot(y + u0(y) * T, u0(y), color=MUTED, lw=.8, ls=(0, (3, 2)), label='沿特征线的多值曲线')
    ax.plot(xc, U, color=BLUE, label='熵解（含激波）')
    ax.plot(xc, u0(xc), color=GRID, lw=.8, label=r'$u_0$')
    lab(ax, rf'(b) $t={T:g}$ 的剖面')
    ax.set(xlim=(-2.5, 4), ylim=(-.02, 1.6), xlabel=r'$x$', ylabel=r'$u$')
    ax.legend(loc='upper left', handlelength=1.4, fontsize=7)
    jump = int(np.argmax(-np.diff(U)))
    save(fig, D/'pde-burgers', 'figure', {
        'equation': 'u_t+(u^2/2)_x=0', 'u0': 'exp(-x^2)', 't_star': round(tstar, 4), 'x_star': round(float(xs), 4),
        'scheme': f'Godunov finite volume, N={N} cells on [{L},{R}], CFL 0.45', 'T': T,
        'shock_location_T': round(float(xc[jump]), 3)})


# ----------------------------------------------------------------- 3.5
def dalembert():
    """(a) bump splitting, c=1; (b) characteristics, domain of dependence and region of influence."""
    u0 = lambda z: bump(z, 0, .35)
    x = np.linspace(-4, 4, 801)
    fig, axes = figure(width_mm=107, height_mm=52, ncols=2)
    ax = axes[0]
    lab(ax, r'(a) 初始鼓包分成两半')
    times = [0, .75, 1.5, 2.25, 3.0]
    for i, (t, col) in enumerate(zip(times, TCOL)):
        off = .55 * i
        ax.fill_between(x, off, off + .5 * (u0(x - t) + u0(x + t)), color='white', lw=0, zorder=2 + i)
        ax.plot(x, off + .5 * (u0(x - t) + u0(x + t)), color=col, zorder=3 + i)
        ax.text(5.3, off + .05, rf'$t={t:g}$', ha='right', fontsize=7.5, color=col, zorder=10)
    ax.set(xlim=(-4, 5.3), ylim=(0, 3.4), xlabel=r'$x$', yticks=[])
    ax.spines['left'].set_visible(False)
    ax = axes[1]
    lab(ax, r'(b) 依赖区间与影响区域')
    xp, tp = .8, 1.6
    ax.add_patch(Polygon([[xp - tp, 0], [xp + tp, 0], [xp, tp]], closed=True, fc=BLUE_FILL, ec=BLUE, lw=.75))
    a, b = -2.8, -2.2
    ax.add_patch(Polygon([[a, 0], [b, 0], [b + 2.0, 2.0], [a - 2.0, 2.0]], closed=True, fc=YELLOW_FILL, ec=YELLOW, lw=.75))
    ax.plot([xp], [tp], 'o', color=BLUE, ms=3)
    ax.text(xp + .1, tp + .07, r'$(x,t)$', fontsize=7.5, color=BLUE)
    ax.text(xp, .1, r'$[x-ct,x+ct]$', ha='center', fontsize=7.5, color=BLUE)
    ax.plot([a, b], [0, 0], color=YELLOW, lw=2.2)
    ax.text(a - .9, 1.55, '影响区域', fontsize=7.5, color=STROKE)
    ax.text((a + b) / 2, .1, r'$[a,b]$', ha='center', fontsize=7.5, color=STROKE)
    ax.set(xlim=(-4, 4), ylim=(0, 2), xlabel=r'$x$', ylabel=r'$t$')
    save(fig, D/'pde-dalembert', 'figure', {
        'u0': 'exp(-(x/0.35)^2)', 'u1': 0, 'c': 1, 'times': times,
        'dependence_point': [xp, tp], 'influence_support': [a, b]})


def standing_waves():
    """Modes sin(k pi x) cos(k pi t), k=1,2,3, at several phases."""
    x = np.linspace(0, 1, 401)
    fig, axes = figure(width_mm=105, height_mm=34, ncols=3, sharey=True)
    for ax, k in zip(axes, [1, 2, 3]):
        for ph, col in zip(np.linspace(0, np.pi, 7), [BLUE, BLUE, GREEN, GREEN, GREEN, BLUE, BLUE]):
            ax.plot(x, np.sin(k * np.pi * x) * np.cos(ph), color=MUTED if 0 < ph < np.pi else BLUE, lw=.6 if 0 < ph < np.pi else 1.1)
        nodes = np.arange(0, k + 1) / k
        ax.plot(nodes, 0 * nodes, 'o', color=RED, ms=2.6)
        lab(ax, rf'$k={k}$，频率 ${k}\pi c$' if k > 1 else r'$k=1$，频率 $\pi c$')
        ax.set(xlim=(0, 1), ylim=(-1.15, 1.15), xlabel=r'$x$', xticks=[0, .5, 1])
    save(fig, D/'pde-standing-waves', 'figure', {
        'modes': 'sin(k pi x) cos(k pi c t), c=1', 'phases': 'k pi c t in {0, pi/6, ..., pi}', 'nodes': 'x=j/k'})


def energy_compare():
    """Normalized energies: undamped wave, damped wave (gamma=0.5), heat (kappa=0.05)."""
    t = np.linspace(0, 6, 1201)
    modes = [(1, 1.0), (3, .5)]
    c, gamma, kappa = 1.0, .5, .05
    E_w = np.ones_like(t)
    def damped(k, A):
        w = k * np.pi * c
        mu = np.sqrt(w ** 2 - gamma ** 2 / 4)
        a = A * np.exp(-gamma * t / 2) * (np.cos(mu * t) + gamma / (2 * mu) * np.sin(mu * t))
        ad = -A * np.exp(-gamma * t / 2) * (w ** 2 / mu) * np.sin(mu * t)
        return .25 * (ad ** 2 + w ** 2 * a ** 2)
    Ed = sum(damped(k, A) for k, A in modes)
    Ed = Ed / Ed[0]
    Eh = sum(.25 * A ** 2 * np.exp(-2 * kappa * (k * np.pi) ** 2 * t) for k, A in modes)
    Eh = Eh / Eh[0]
    fig, ax = figure(width_mm=100, height_mm=44)
    ax.plot(t, E_w, color=BLUE, label='波动')
    ax.plot(t, Ed, color=GREEN, label='阻尼波动')
    ax.plot(t, np.exp(-gamma * t), color=GREEN, lw=.6, ls=(0, (3, 2)), label=r'$e^{-0.5t}$')
    ax.plot(t, Eh, color=RED, label='热方程')
    ax.set(xlim=(0, 6), ylim=(0, 1.32), xlabel=r'$t$', ylabel='能量 / 初始能量')
    ax.legend(loc='upper right', handlelength=1.4, ncol=4, columnspacing=1.0)
    save(fig, D/'pde-energy-compare', 'figure', {
        'u0': 'sin(pi x)+0.5 sin(3 pi x)', 'u1': 0, 'boundary': 'Dirichlet zero on (0,1)',
        'wave_energy': '1/2 int (u_t^2+u_x^2)', 'heat_energy': '1/2 int u^2',
        'gamma': gamma, 'kappa': kappa, 'method': 'exact modal solutions'})


# ----------------------------------------------------------------- 3.6
def fd_stencil_sparsity():
    """(a) 1D grid and 3-point stencil; (b) sparsity of 1D A_h, N=12; (c) 2D 5-point, 6x6 grid."""
    fig, axes = figure(width_mm=150, height_mm=48, ncols=3, gridspec_kw={'width_ratios': [1.5, 1, 1]})
    ax = axes[0]
    N = 7
    xj = np.arange(N + 2)
    ax.plot([0, N + 1], [0, 0], color=STROKE, lw=.75)
    ax.plot(xj[1:-1], 0 * xj[1:-1], 'o', color=BLUE, ms=4)
    ax.plot([0, N + 1], [0, 0], 's', color=YELLOW, ms=4, mec=INK, mew=.4)
    for j, w in [(3, '$-1$'), (4, '$2$'), (5, '$-1$')]:
        ax.text(j, .28, w, ha='center', fontsize=8, color=RED)
    ax.annotate('', xy=(3, .14), xytext=(5, .14), arrowprops=dict(arrowstyle='-', color=RED, lw=.8))
    for j in [0, 3, 4, 5, N + 1]:
        lbl = {0: '$x_0$', 3: '$x_{j-1}$', 4: '$x_j$', 5: '$x_{j+1}$', N + 1: '$x_{N+1}$'}[j]
        ax.text(j, -.3, lbl, ha='center', fontsize=7.5)
    ax.text(0, -.6, '边界值', ha='center', fontsize=7.5, color=MUTED)
    ax.text(N + 1, -.6, '边界值', ha='center', fontsize=7.5, color=MUTED)
    ax.text(4, .62, r'$\times\,1/h^2$', ha='center', fontsize=7.5, color=RED)
    ax.annotate('', xy=(1, -.85), xytext=(2, -.85), arrowprops=dict(arrowstyle='<->', color=MUTED, lw=.6))
    ax.text(1.5, -1.1, '$h$', ha='center', fontsize=7.5, color=MUTED)
    ax.set(xlim=(-.6, N + 1.6), ylim=(-1.3, .95))
    ax.axis('off')
    lab(ax, '(a) 三点差分模板', y=1.06)
    n1 = 12
    A1 = 2 * np.eye(n1) - np.eye(n1, k=1) - np.eye(n1, k=-1)
    ax = axes[1]
    ax.spy(A1, markersize=3.0, color=BLUE)
    lab(ax, rf'(b) 一维 $A_h$，$N={n1}$', y=1.1)
    ax.set(xticks=[], yticks=[])
    m = 6
    T = 2 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1)
    A2 = np.kron(np.eye(m), T) + np.kron(T, np.eye(m))
    ax = axes[2]
    ax.spy(A2, markersize=1.2, color=GREEN)
    lab(ax, rf'(c) 二维五点格式，${m}\times{m}$ 网格', y=1.1)
    ax.set(xticks=[], yticks=[])
    save(fig, D/'pde-fd-stencil-sparsity', 'figure', {
        '1D': {'N': n1, 'nonzeros': int(np.count_nonzero(A1))},
        '2D': {'grid': [m, m], 'unknowns': m * m, 'nonzeros': int(np.count_nonzero(A2))}})


def fem_hats():
    """(a) hat basis on 5 interior nodes; (b) Galerkin solution for u=sin(pi x)+0.3 sin(3 pi x), h=1/6."""
    x = np.linspace(0, 1, 1201)
    n = 6
    nodes = np.arange(n + 1) / n
    hat = lambda j: np.maximum(0, 1 - np.abs(x - nodes[j]) * n)
    fig, axes = figure(width_mm=105, height_mm=46, ncols=2)
    ax = axes[0]
    for j in range(1, n):
        ax.plot(x, hat(j), color=BLUE if j == 3 else MUTED, lw=1.1 if j == 3 else .6)
    ax.fill_between(x, 0, hat(3), color=BLUE_FILL, lw=0)
    ax.plot(nodes, 0 * nodes, 'o', color=INK, ms=2.4)
    ax.text(nodes[3], 1.05, r'$\varphi_3$', ha='center', fontsize=8, color=BLUE)
    lab(ax, r'(a) 帽函数基，$h=1/6$')
    ax.set(xlim=(0, 1), ylim=(0, 1.25), xlabel=r'$x$')
    ax = axes[1]
    uex = lambda z: np.sin(np.pi * z) + .3 * np.sin(3 * np.pi * z)
    # assemble stiffness and exact load (high-order quadrature)
    K = (2 * np.eye(n - 1) - np.eye(n - 1, k=1) - np.eye(n - 1, k=-1)) * n
    fq = lambda z: np.pi ** 2 * np.sin(np.pi * z) + .3 * 9 * np.pi ** 2 * np.sin(3 * np.pi * z)
    xx = np.linspace(0, 1, 60001)
    F = np.array([np.trapezoid(fq(xx) * np.maximum(0, 1 - np.abs(xx - nodes[j]) * n), xx) for j in range(1, n)])
    c = np.linalg.solve(K, F)
    uh = np.concatenate([[0], c, [0]])
    ax.plot(x, uex(x), color=BLUE, label='精确解')
    ax.plot(nodes, uh, color=YELLOW, marker='o', ms=3, mec=INK, mew=.4, label=r'Galerkin $u_h$')
    lab(ax, r'(b) 分片线性逼近')
    ax.set(xlim=(0, 1), ylim=(-.05, 1.45), xlabel=r'$x$')
    ax.legend(loc='upper right', handlelength=1.4)
    save(fig, D/'pde-fem-hats', 'figure', {
        'equation': "-u''=f, u(0)=u(1)=0, exact u=sin(pi x)+0.3 sin(3 pi x)", 'h': 1 / n,
        'stiffness': '(1/h) tridiag(-1,2,-1)', 'load': 'exact integrals of f*phi_j (trapezoid, 60001 points)',
        'max_nodal_error': float(np.abs(uh - uex(nodes)).max())})


def convergence():
    """Errors for -u''=pi^2 sin(pi x): FD max-norm, FEM H1-seminorm and L2."""
    hs, efd, eh1, el2 = [], [], [], []
    u = lambda z: np.sin(np.pi * z)
    up = lambda z: np.pi * np.cos(np.pi * z)
    gl, gw = np.polynomial.legendre.leggauss(8)
    for N in [4, 8, 16, 32, 64, 128, 256]:
        h = 1 / (N + 1)
        xj = np.arange(1, N + 1) * h
        A = (2 * np.eye(N) - np.eye(N, k=1) - np.eye(N, k=-1)) / h ** 2
        U = np.linalg.solve(A, np.pi ** 2 * np.sin(np.pi * xj))
        efd.append(np.abs(U - u(xj)).max())
        # FEM with exact load: nodal values exact, so u_h = I_h u
        nodes = np.arange(N + 2) * h
        s1 = s2 = 0.0
        for a, b in zip(nodes[:-1], nodes[1:]):
            q = (a + b) / 2 + (b - a) / 2 * gl
            w = (b - a) / 2 * gw
            ih = u(a) + (u(b) - u(a)) * (q - a) / (b - a)
            s2 += np.sum(w * (u(q) - ih) ** 2)
            s1 += np.sum(w * (up(q) - (u(b) - u(a)) / (b - a)) ** 2)
        eh1.append(np.sqrt(s1)); el2.append(np.sqrt(s2)); hs.append(h)
    hs = np.array(hs)
    fig, ax = figure(width_mm=100, height_mm=50)
    ax.loglog(hs, efd, 'o-', color=BLUE, ms=3, label=r'$\max_j|u(x_j)-U_j|$')
    ax.loglog(hs, eh1, 's-', color=GREEN, ms=3, label=r"$\|(u-u_h)'\|_{L^2}$")
    ax.loglog(hs, el2, '^-', color=YELLOW, ms=3, label=r'$\|u-u_h\|_{L^2}$')
    ax.loglog(hs, 1.6 * hs, color=MUTED, lw=.6, ls=(0, (3, 2)))
    ax.loglog(hs, .5 * hs ** 2, color=MUTED, lw=.6, ls=(0, (1, 1.5)))
    ax.text(hs[1], 1.6 * hs[1] * 1.6, '斜率 1', fontsize=7.5, color=MUTED)
    ax.text(hs[2], .5 * hs[2] ** 2 / 3.2, '斜率 2', fontsize=7.5, color=MUTED)
    ax.set(xlabel=r'$h$', ylabel='误差')
    ax.legend(loc='upper left', handlelength=1.6, fontsize=7)
    ax.grid(True, which='major', lw=.4)
    p = lambda e: float(np.polyfit(np.log(hs[-4:]), np.log(np.array(e)[-4:]), 1)[0])
    save(fig, D/'pde-convergence', 'figure', {
        'u': 'sin(pi x)', 'N': [4, 8, 16, 32, 64, 128, 256],
        'fd_max': [float(e) for e in efd], 'fem_h1': [float(e) for e in eh1], 'fem_l2': [float(e) for e in el2],
        'fitted_slopes_last4': {'fd': p(efd), 'h1': p(eh1), 'l2': p(el2)},
        'fd_bound': 'pi^4 h^2/96'})


def explicit_stability():
    """Explicit Euler for u_t=u_xx, h=1/20, u0=sin(pi x)+0.01(-1)^j, r=0.48 and r=0.52."""
    N = 19
    h = 1 / (N + 1)
    xj = np.arange(1, N + 1) * h
    U0 = np.sin(np.pi * xj) + .01 * (-1.0) ** np.arange(1, N + 1)
    fig, axes = figure(width_mm=150, height_mm=46, ncols=3)
    facts = {'h': h, 'u0': 'sin(pi x_j)+0.01(-1)^j', 'steps_shown': [0, 30, 60]}
    for ax, r, title in [(axes[0], .48, r'(a) $r=0.48$'), (axes[1], .52, r'(b) $r=0.52$')]:
        U = U0.copy()
        for n in range(61):
            if n in (0, 30, 60):
                col = {0: BLUE, 30: GREEN, 60: RED}[n]
                ax.plot(np.r_[0, xj, 1], np.r_[0, U, 0], color=col, marker='o', ms=1.8, lw=.9, label=rf'$n={n}$')
                tt = n * r * h ** 2
                ax.plot(np.linspace(0, 1, 201), np.exp(-np.pi ** 2 * tt) * np.sin(np.pi * np.linspace(0, 1, 201)), color=col, lw=.5, ls=(0, (3, 2)))
            if n < 60:
                U = U + r * (np.r_[U[1:], 0] - 2 * U + np.r_[0, U[:-1]])
        lab(ax, title)
        ax.set(xlim=(0, 1), ylim=(-.6, 1.25), xlabel=r'$x$')
        facts[f'r={r}'] = {'max_abs_after_60_steps': float(np.abs(U).max())}
    axes[0].legend(loc='lower center', handlelength=1.2, ncol=3, columnspacing=.8)
    ax = axes[2]
    th = np.linspace(0, np.pi, 301)
    ax.axhspan(-1, 1, color=BLUE_FILL, lw=0)
    for r, col in [(.48, BLUE), (.52, RED)]:
        ax.plot(th, 1 - 4 * r * np.sin(th / 2) ** 2, color=col, label=rf'$r={r}$')
    lab(ax, r'(c) 放大因子 $g=1-4r\sin^2(\theta/2)$')
    ax.set(xlim=(0, np.pi), ylim=(-1.25, 1.1), xlabel=r'$\theta=k\pi h$', xticks=[0, np.pi / 2, np.pi], xticklabels=['$0$', r'$\pi/2$', r'$\pi$'])
    ax.legend(loc='lower left', handlelength=1.2)
    save(fig, D/'pde-explicit-stability', 'figure', facts)


def error_plateau():
    """Heat u_t=u_xx, u0=sin(pi x), T=0.1: max error of BE / CN versus dt for several h."""
    T = .1
    exact = np.exp(-np.pi ** 2 * T)
    dts = np.logspace(-5, -1.3, 25)
    fig, ax = figure(width_mm=100, height_mm=50)
    facts = {'T': T, 'u0': 'sin(pi x)', 'note': 'sin(pi x_j) is an eigenvector of A_h, errors are scalar'}
    for N, col in [(9, BLUE), (19, GREEN), (39, YELLOW)]:
        h = 1 / (N + 1)
        lam = 4 / h ** 2 * np.sin(np.pi * h / 2) ** 2
        eBE, eCN = [], []
        for dt in dts:
            n = int(round(T / dt)); dt_ = T / n
            eBE.append(abs((1 + dt_ * lam) ** (-n) - exact))
            eCN.append(abs(((1 - dt_ * lam / 2) / (1 + dt_ * lam / 2)) ** n - exact))
        ax.loglog(dts, eBE, color=col, label=rf'$h=1/{N+1}$')
        ax.loglog(dts, eCN, color=col, lw=.7, ls=(0, (3, 2)))
        semi = abs(np.exp(-lam * T) - exact)
        ax.axhline(semi, color=col, lw=.4, ls=(0, (1, 1.5)))
        facts[f'h=1/{N+1}'] = {'spatial_error': float(semi)}
    ax.plot([], [], color=MUTED, lw=1.1, label='后向Euler')
    ax.plot([], [], color=MUTED, lw=.7, ls=(0, (3, 2)), label='梯形法')
    ax.set(xlabel=r'$\Delta t$', ylabel='最大误差', ylim=(1e-7, 2e-1))
    ax.legend(loc='lower left', handlelength=1.6, fontsize=7, ncol=2)
    ax.grid(True, which='major', lw=.4)
    save(fig, D/'pde-error-plateau', 'figure', facts)


ALL = {f.__name__: f for f in [rod_snapshots, three_mechanisms, boundary_conditions, weak_form_test,
       poisson_energy, neumann, heat_modes, heat_heatmap, heat_energy_max, characteristics,
       transport_vs_continuity, burgers, dalembert, standing_waves, energy_compare,
       fd_stencil_sparsity, fem_hats, convergence, explicit_stability, error_plateau]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(ALL)
    for name in names:
        ALL[name.replace('-', '_')]()
        print('done', name)
