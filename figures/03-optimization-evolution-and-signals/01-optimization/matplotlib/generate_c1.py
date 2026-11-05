# coding: utf-8
"""Teaching charts for volume three, part "optimization", chapter 1
(optimization problems and their solutions).

Every curve, level set and marked point comes from the closed-form expression
recorded in the facts file saved next to each figure; no random numbers are used.
Chinese labels and mathtext labels are kept in separate text objects because the
mathtext font (Fira Math) has no CJK glyphs.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/01-optimization/matplotlib/generate_c1.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from matplotlib.patches import Polygon

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import (figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID,
                     BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL)

D = Path(__file__).resolve().parent
NOTE = 7.5


def label2(ax, x, y, first, second, color, ha='left', size=NOTE, box=False):
    """Two stacked labels at data point (x, y): Chinese or math first line, then second line."""
    bb = dict(fc='white', ec='none', pad=0.6) if box else None
    ax.text(x, y, first, fontsize=size, color=color, ha=ha, va='bottom', bbox=bb)
    ax.annotate(second, (x, y), xytext=(0, -1.5), textcoords='offset points',
                fontsize=size, color=color, ha=ha, va='top', bbox=bb)


# ---------------------------------------------------------------- 1.1
def resource_region():
    """Feasible polygon x1+x2<=4, 2x1+x2<=6, x>=0 and profit lines 3x1+2x2=c."""
    fig, ax = figure(width_mm=80, height_mm=66)
    verts = np.array([[0, 0], [3, 0], [2, 2], [0, 4]])
    ax.add_patch(Polygon(verts, closed=True, facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
    x = np.linspace(-0.4, 4.8, 50)
    for c in (4, 8, 10):
        ax.plot(x, (c - 3*x)/2, color=GREEN if c == 10 else MUTED,
                lw=1.0 if c == 10 else .7, ls='--' if c == 10 else ':')
        xe = (c + 0.3*2)/3  # where the line meets y=-0.3
        ax.text(xe + 0.05, -0.28, f'{c}', fontsize=7, color=GREEN if c == 10 else MUTED, va='bottom')
    ax.text(3.0, 4.3, r'$3x_1+2x_2=c$', fontsize=7, color=MUTED, ha='center')
    ax.plot([2], [2], 'o', color=GREEN, ms=4)
    ax.text(2.12, 2.12, r'$(2,2)$', fontsize=NOTE, color=INK)
    ax.annotate('', xy=(4.15, 2.75), xytext=(3.55, 2.35),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=.8))
    ax.text(3.5, 2.85, '利润增大', fontsize=NOTE, color=GREEN)
    ax.text(0.8, 1.0, r'$C$', fontsize=10, color=BLUE)
    ax.text(1.05, 3.15, r'$x_1+x_2\leq 4$', fontsize=7, color=BLUE, rotation=-45, ha='center', va='center')
    ax.text(2.95, 1.25, r'$2x_1+x_2\leq 6$', fontsize=7, color=BLUE, rotation=-63.4, ha='center', va='center')
    ax.set(xlim=(-0.4, 4.8), ylim=(-0.4, 4.6), xlabel=r'$x_1$', ylabel=r'$x_2$', aspect='equal')
    ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2, 3, 4])
    save(fig, D/'c1-resource-region', 'figure', {
        'constraints': ['x1+x2<=4', '2x1+x2<=6', 'x1>=0', 'x2>=0'],
        'vertices': verts.tolist(), 'profit': '3x1+2x2', 'vertex_profits': [0, 9, 10, 8],
        'level_lines': [4, 8, 10], 'best_vertex': [2, 2]})


def failure_modes():
    """Infeasible, unbounded below, finite infimum not attained."""
    fig, axes = figure(width_mm=150, height_mm=46, ncols=3)
    ax = axes[0]
    ax.axhline(0, color=GRID, lw=.6)
    ax.plot([-2.2, 0], [0.35, 0.35], color=BLUE, lw=2.2, solid_capstyle='butt')
    ax.plot([1, 3.2], [-0.35, -0.35], color=GREEN, lw=2.2, solid_capstyle='butt')
    ax.plot([0], [0.35], 'o', color=BLUE, ms=3.5); ax.plot([1], [-0.35], 'o', color=GREEN, ms=3.5)
    ax.text(-1.1, 0.55, r'$x\leq 0$', ha='center', color=BLUE, fontsize=NOTE)
    ax.text(2.1, -0.75, r'$x\geq 1$', ha='center', color=GREEN, fontsize=NOTE)
    ax.text(0.5, 0.95, r'$C=\varnothing$', ha='center', color=RED, fontsize=NOTE)
    ax.set(xlim=(-2.4, 3.4), ylim=(-1.2, 1.2), title='(a) 不可行', xlabel=r'$x$')
    ax.set_yticks([]); ax.spines['left'].set_visible(False)
    ax = axes[1]
    x = np.linspace(-3, 3, 50)
    ax.plot(x, x, color=BLUE)
    ax.annotate('', xy=(-3, -3), xytext=(-2.2, -2.2), arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.0))
    ax.text(-0.3, -2.0, r'$f(x)=x$', fontsize=NOTE, color=INK)
    ax.text(-0.3, -2.75, r'$f^{\ast}=-\infty$', fontsize=NOTE, color=RED)
    ax.set(xlim=(-3.2, 3.2), ylim=(-3.2, 3.2), title='(b) 无下界', xlabel=r'$x$')
    ax = axes[2]
    x = np.linspace(-5, 1.2, 200)
    ax.plot(x, np.exp(x), color=BLUE)
    ax.axhline(0, color=RED, lw=.8, ls='--')
    label2(ax, -4.9, 0.55, r'$f^{\ast}=0$', '无点取得', RED)
    ax.text(-0.9, 2.4, r'$f(x)=e^{x}$', fontsize=NOTE)
    ax.set(xlim=(-5, 1.3), ylim=(-0.4, 3.4), title='(c) 下确界有限而未达到', xlabel=r'$x$')
    save(fig, D/'c1-failure-modes', 'figure', {
        'panel_a': 'constraints x<=0 and x>=1, empty feasible set',
        'panel_b': 'f(x)=x on R, inf=-inf', 'panel_c': 'f(x)=exp(x) on R, inf=0 not attained'})


def local_global():
    """f(x)=x^4/4-x^3/3-x^2 on C=[-1.5,1.5]."""
    f = lambda x: x**4/4 - x**3/3 - x**2
    fig, ax = figure(width_mm=100, height_mm=56)
    x = np.linspace(-2.0, 2.6, 400)
    ax.axvspan(-1.5, 1.5, color=BLUE_FILL, lw=0)
    ax.plot(x, f(x), color=MUTED, lw=.8, ls='--')
    xc = np.linspace(-1.5, 1.5, 300)
    ax.plot(xc, f(xc), color=BLUE)
    ax.plot([-1], [f(-1)], 'o', color=GREEN, ms=4)
    label2(ax, -1.3, 0.75, '局部最优', r'$x=-1$', GREEN)
    ax.plot([1.5], [f(1.5)], 'o', color=RED, ms=4)
    label2(ax, 0.3, -2.75, '可行域上全局最优', r'$x=1.5$', RED)
    ax.plot([2], [f(2)], 'o', color=MUTED, ms=4)
    label2(ax, 1.62, -1.25, '可行域外更低', r'$x=2$', MUTED)
    ax.plot([0], [0], 'o', mfc='white', mec=MUTED, ms=4)
    ax.text(0.08, 0.25, '局部最大', fontsize=NOTE, color=MUTED)
    ax.text(-1.45, -3.35, r'$C=[-1.5,1.5]$', fontsize=NOTE, color=BLUE)
    ax.set(xlim=(-2.0, 2.6), ylim=(-3.5, 2.2), xlabel=r'$x$', ylabel=r'$f(x)$')
    save(fig, D/'c1-local-global', 'figure', {
        'f': 'x^4/4 - x^3/3 - x^2', 'C': [-1.5, 1.5],
        'critical_points': {'-1': f(-1), '0': 0.0, '2': f(2)},
        'endpoints': {'-1.5': f(-1.5), '1.5': f(1.5)},
        'derivative_at_1.5': 1.5**3 - 1.5**2 - 2*1.5})


def extended_value():
    """(x-2)^2 with x<=1 as indicator versus a finite penalty max(0,x-1)."""
    fig, ax = figure(width_mm=100, height_mm=52)
    x = np.linspace(-0.6, 3.0, 400)
    f = (x - 2)**2
    pen = f + np.maximum(0, x - 1)
    ax.axvspan(1, 3.0, color=RED_FILL, lw=0)
    ax.text(2.0, 3.55, r'$\iota_C(x)=+\infty$', color=RED, fontsize=NOTE, ha='center')
    xl = x[x <= 1]
    ax.plot(xl, (xl - 2)**2, color=BLUE, label=r'$f+\iota_C$')
    ax.plot(x, f, color=MUTED, lw=.7, ls=':', label=r'$f(x)=(x-2)^2$')
    ax.plot(x, pen, color=GREEN, ls='--', label=r'$f(x)+\max\{0,x-1\}$')
    ax.plot([1], [1], 'o', color=BLUE, ms=4)
    ax.plot([1.5], [0.75], 'o', color=GREEN, ms=4)
    ax.annotate(r'$x=1$', (1, 1), xytext=(1.05, 2.0), fontsize=NOTE, color=BLUE,
                arrowprops=dict(arrowstyle='-', color=BLUE, lw=.5))
    ax.annotate(r'$x=1.5$', (1.5, 0.75), xytext=(1.7, 1.6), fontsize=NOTE, color=GREEN,
                arrowprops=dict(arrowstyle='-', color=GREEN, lw=.5))
    ax.set(xlim=(-0.6, 3.0), ylim=(0, 4.2), xlabel=r'$x$')
    ax.legend(loc='lower left', fontsize=7, handlelength=1.6)
    save(fig, D/'c1-extended-value', 'figure', {
        'f': '(x-2)^2', 'C': 'x<=1', 'indicator_minimizer': [1, 1],
        'penalty': 'max(0,x-1), weight 1', 'penalty_minimizer': [1.5, 0.75]})


# ---------------------------------------------------------------- 1.2
def existence_failures():
    """Missing endpoint, escape to infinity, value jumping up at the limit."""
    fig, axes = figure(width_mm=150, height_mm=48, ncols=3)
    ax = axes[0]
    x = np.linspace(0, 1, 50)
    ax.plot(x, x, color=BLUE)
    ax.plot([0], [0], 'o', mfc='white', mec=BLUE, ms=4)
    ax.plot([1], [1], 'o', color=BLUE, ms=3)
    xs = 1/np.array([2, 4, 8, 16])
    ax.plot(xs, xs, 'o', color=GREEN, ms=2.6)
    ax.text(0.02, 0.92, r'$f(x)=x,\ C=(0,1]$', fontsize=NOTE, color=INK)
    ax.text(0.3, 0.06, r'$x^{(k)}=2^{-k}\to 0\notin C$', fontsize=NOTE, color=GREEN)
    ax.set(xlim=(-0.1, 1.1), ylim=(-0.1, 1.1), xlabel=r'$x$', title='(a) 缺失端点')
    ax = axes[1]
    x = np.linspace(1, 12, 200)
    ax.plot(x, 1/x, color=BLUE)
    ks = np.array([1, 2, 4, 8])
    ax.plot(ks, 1/ks, 'o', color=GREEN, ms=2.6)
    ax.axhline(0, color=RED, lw=.8, ls='--')
    ax.text(3.0, 0.92, r'$f(x)=1/x,\ C=[1,\infty)$', fontsize=NOTE, color=INK)
    ax.text(4.5, 0.4, r'$x^{(k)}=2^{k}\to\infty$', fontsize=NOTE, color=GREEN)
    ax.set(xlim=(0, 12.5), ylim=(-0.12, 1.1), xlabel=r'$x$', title='(b) 逃向无穷远')
    ax = axes[2]
    x = np.linspace(-1, 1, 201)
    xl, xr = x[x < 0], x[x > 0]
    ax.plot(xl, xl**2, color=BLUE); ax.plot(xr, xr**2, color=BLUE)
    ax.plot([0], [0], 'o', mfc='white', mec=BLUE, ms=4)
    ax.plot([0], [0.6], 'o', color=RED, ms=4)
    ax.text(0.08, 0.6, r'$f(0)=0.6$', fontsize=NOTE, color=RED, va='center')
    ax.text(-0.55, 1.0, r'$C=[-1,1]$', fontsize=NOTE, color=INK)
    ax.set(xlim=(-1.1, 1.1), ylim=(-0.1, 1.1), xlabel=r'$x$', title='(c) 极限处跳高')
    save(fig, D/'c1-existence-failures', 'figure', {
        'panel_a': 'f(x)=x on (0,1], inf 0, sequence 2^-k',
        'panel_b': 'f(x)=1/x on [1,inf), inf 0, sequence 2^k',
        'panel_c': 'f(x)=x^2 for x!=0, f(0)=0.6 on [-1,1], inf 0 not attained'})


def lsc_gap():
    """Two step functions differing only in the value at the jump; sublevel {f<=0.6}."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2, sharey=True)
    for ax, v0, title in [(axes[0], 0.4, '(a) 下半连续'), (axes[1], 1.0, '(b) 不下半连续')]:
        xl = np.linspace(-1, 0, 20); xr = np.linspace(0, 1.5, 40)
        ax.plot(xl, np.ones_like(xl), color=BLUE)
        ax.plot(xr, 0.4 + 0.5*xr, color=BLUE)
        ax.axhline(0.6, color=MUTED, lw=.6, ls=':')
        ax.text(-0.98, 0.64, r'$a=0.6$', fontsize=7, color=MUTED)
        ax.plot([0], [1 if v0 < 0.5 else 0.4], 'o', mfc='white', mec=BLUE, ms=3.6)
        ax.plot([0], [v0], 'o', color=BLUE, ms=3.6)
        ax.text(0.1, v0 + (0.06 if v0 > 0.5 else -0.1), rf'$f(0)={v0:g}$', fontsize=NOTE, color=BLUE)
        ax.plot([0, 0.4], [0.03, 0.03], color=GREEN, lw=2.4, solid_capstyle='butt')
        ax.plot([0.4], [0.03], 'o', color=GREEN, ms=3)
        if v0 < 0.5:
            ax.plot([0], [0.03], 'o', color=GREEN, ms=3)
            ax.text(0.5, 0.06, r'$\{f\leq a\}=[0,0.4]$', fontsize=7, color=GREEN)
        else:
            ax.plot([0], [0.03], 'o', mfc='white', mec=GREEN, ms=3)
            ax.text(0.5, 0.06, r'$\{f\leq a\}=(0,0.4]$', fontsize=7, color=GREEN)
        ax.set(xlim=(-1.05, 1.55), ylim=(-0.05, 1.3), xlabel=r'$x$', title=title)
    save(fig, D/'c1-lsc-gap', 'figure', {
        'f': '1 for x<0; 0.4+0.5x for x>0; value at 0 is 0.4 (a) or 1 (b)', 'level': 0.6,
        'sublevel_a': '[0,0.4]', 'sublevel_b': '(0,0.4]', 'inf_b': '0.4 not attained'})


def _ls(lam, X1, X2):
    return 0.5*(X1 + X2 - 2)**2 + 0.5*lam*(X1**2 + X2**2)


def ls_sublevel():
    """f(x)=1/2(x1+x2-2)^2+lam/2||x||^2, sublevel {f<=1} for lam=0 and lam=0.5."""
    fig, axes = figure(width_mm=124, height_mm=62, ncols=2, sharey=True)
    g = np.linspace(-3, 5, 401)
    X1, X2 = np.meshgrid(g, g)
    facts = {'A': [[1, 1]], 'b': [2], 'level': 1.0, 'other_contours': [0.25, 2.25, 4, 6.25]}
    for ax, lam in zip(axes, [0.0, 0.5]):
        F = _ls(lam, X1, X2)
        ax.contourf(X1, X2, F, levels=[-1, 1.0], colors=[BLUE_FILL])
        ax.contour(X1, X2, F, levels=[0.25, 2.25, 4, 6.25], colors=[MUTED], linewidths=.5)
        ax.contour(X1, X2, F, levels=[1.0], colors=[BLUE], linewidths=1.0)
        if lam == 0:
            ax.plot(g, 2 - g, color=GREEN, lw=1.0, ls='--')
            label2(ax, 1.3, -1.3, '最小点集合', r'$x_1+x_2=2$', GREEN, box=True)
            ax.set_title(r'(a) $\lambda=0$')
        else:
            c = 2/(2 + lam)
            ax.plot([c], [c], 'o', color=GREEN, ms=3.5)
            ax.annotate(r'$\mathbf{x}^{\ast}=(0.8,0.8)$', (c, c), xytext=(1.3, 3.9), fontsize=NOTE, color=GREEN,
                        arrowprops=dict(arrowstyle='-', color=GREEN, lw=.5))
            ax.set_title(r'(b) $\lambda=0.5$')
            facts['lam_0.5_minimizer'] = [c, c]
            facts['lam_0.5_fstar'] = 0.5*lam*4/(2 + lam)
        ax.set(xlim=(-3, 5), ylim=(-3, 5), xlabel=r'$x_1$', aspect='equal')
    axes[0].set_ylabel(r'$x_2$')
    save(fig, D/'c1-ls-sublevel', 'figure', facts)


# ---------------------------------------------------------------- 1.3
def chord_tangent():
    """Convex x^2/2 versus nonconvex x^4/4-x^2: chord and tangent."""
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    f = lambda x: x**2/2
    x = np.linspace(-1.8, 2.5, 200)
    ax.plot(x, f(x), color=BLUE)
    u, v = -1.0, 2.0
    ax.plot([u, v], [f(u), f(v)], color=GREEN, marker='o', ms=3)
    x0 = 0.5
    ax.plot(x, f(x0) + x0*(x - x0), color=PURPLE, ls='--', lw=.9)
    ax.plot([x0], [f(x0)], 'o', color=PURPLE, ms=3)
    ax.text(0.15, 1.6, '弦在上方', fontsize=NOTE, color=GREEN)
    ax.text(1.0, -0.55, '切线在下方', fontsize=NOTE, color=PURPLE)
    ax.set(xlim=(-1.8, 2.5), ylim=(-1.0, 3.1), xlabel=r'$x$', title=r'(a) $f(x)=x^2/2$')
    ax = axes[1]
    g = lambda x: x**4/4 - x**2
    x = np.linspace(-2.0, 2.0, 300)
    ax.plot(x, g(x), color=BLUE)
    u, v = -1.6, 1.0
    ax.plot([u, v], [g(u), g(v)], color=RED, marker='o', ms=3)
    ax.axhline(0, color=PURPLE, ls='--', lw=.9)
    ax.plot([0], [0], 'o', color=PURPLE, ms=3)
    ax.text(-1.95, 0.25, '切线在图像上方', fontsize=NOTE, color=PURPLE)
    ax.text(-0.75, -1.25, '弦在图像下方', fontsize=NOTE, color=RED)
    ax.set(xlim=(-2.0, 2.0), ylim=(-1.5, 1.3), xlabel=r'$x$', title=r'(b) $g(x)=x^4/4-x^2$')
    save(fig, D/'c1-chord-tangent', 'figure', {
        'panel_a': {'f': 'x^2/2', 'chord': [-1, 2], 'tangent_at': 0.5},
        'panel_b': {'g': 'x^4/4-x^2', 'chord': [-1.6, 1.0], 'tangent_at': 0.0,
                    'g(-1.6)': g(-1.6), 'g(1.0)': g(1.0)}})


def strong_convex_gap():
    """(a) chord gap for f=x^2/2+|x-0.5| (mu=1); (b) quadratic sandwich along directions."""
    fig, axes = figure(width_mm=150, height_mm=54, ncols=2)
    ax = axes[0]
    f = lambda x: x**2/2 + np.abs(x - 0.5)
    mu = 1.0
    u, v = -1.5, 2.0
    th = np.linspace(0, 1, 200)
    xs = th*u + (1 - th)*v
    chord = th*f(u) + (1 - th)*f(v)
    gap = chord - mu/2*th*(1 - th)*(u - v)**2
    x = np.linspace(-1.9, 2.4, 300)
    ax.fill_between(xs, gap, chord, color=GREEN_FILL, lw=0)
    ax.plot(x, f(x), color=BLUE)
    ax.plot(xs, chord, color=GREEN, lw=.9)
    ax.plot(xs, gap, color=GREEN, lw=.9, ls='--')
    ax.plot([u, v], [f(u), f(v)], 'o', color=GREEN, ms=3)
    ax.text(-0.25, 3.5, '弦', fontsize=NOTE, color=GREEN)
    ax.text(-0.45, 2.45, '二次间隔', fontsize=NOTE, color=GREEN)
    ax.set(xlim=(-1.9, 2.4), ylim=(0, 4.2), xlabel=r'$x$',
           title=r'(a) $f(x)=x^2/2+|x-0.5|,\ \mu=1$')
    ax = axes[1]
    H = np.array([[2.0, 1.0], [1.0, 2.0]])
    t = np.linspace(-1.5, 1.5, 200)
    lam = np.linalg.eigvalsh(H)
    ax.fill_between(t, lam[0]/2*t**2, lam[1]/2*t**2, color=BLUE_FILL, lw=0)
    dirs = [(np.array([1, 1])/np.sqrt(2), r'$\mathbf{d}=(1,1)/\sqrt{2}$: $3t^2/2$', RED),
            (np.array([1, 0]), r'$\mathbf{d}=(1,0)$: $t^2$', YELLOW),
            (np.array([1, -1])/np.sqrt(2), r'$\mathbf{d}=(1,-1)/\sqrt{2}$: $t^2/2$', BLUE)]
    for d, lab, col in dirs:
        q = d @ H @ d
        ax.plot(t, q/2*t**2, color=col, label=lab)
    ax.set(xlim=(-1.5, 1.5), ylim=(0, 3.5), xlabel=r'$t$', ylabel=r'$f(\mathbf{x}^{\ast}+t\mathbf{d})-f^{\ast}$',
           title=r'(b) $\mu=1,\ L=3$')
    ax.legend(loc='upper center', fontsize=7, handlelength=1.4)
    save(fig, D/'c1-strong-convex-gap', 'figure', {
        'panel_a': {'f': 'x^2/2+|x-0.5|', 'mu': 1, 'u': u, 'v': v},
        'panel_b': {'H': H.tolist(), 'eigenvalues': lam.tolist(),
                    'source': 'A=[1 1], b=2, lambda=1: H=A^T A + I'}})


# ---------------------------------------------------------------- 1.4
def stationary_types():
    """Contours near the origin; red fill marks f<f(0)=0."""
    fig, axes = figure(width_mm=160, height_mm=46, ncols=4)
    g = np.linspace(-1, 1, 301)
    X, Y = np.meshgrid(g, g)
    cases = [(X**2 + Y**2, '(a) $x^2+y^2$'), (X**2 - Y**2, '(b) $x^2-y^2$'),
             (X**2 + Y**4, '(c) $x^2+y^4$'), (X**2 + Y**3, '(d) $x^2+y^3$')]
    for ax, (F, title) in zip(axes, cases):
        ax.contourf(X, Y, F, levels=[-10, 0], colors=[RED_FILL])
        ax.contour(X, Y, F, levels=np.linspace(-0.9, 1.8, 10), colors=[MUTED], linewidths=.45)
        ax.contour(X, Y, F, levels=[0], colors=[RED], linewidths=.8)
        ax.plot([0], [0], 'o', color=INK, ms=3)
        ax.set(xlim=(-1, 1), ylim=(-1, 1), aspect='equal', title=title, xlabel=r'$x$')
        ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
    axes[0].set_ylabel(r'$y$')
    save(fig, D/'c1-stationary-types', 'figure', {
        'functions': ['x^2+y^2', 'x^2-y^2', 'x^2+y^4', 'x^2+y^3'],
        'hessians_at_0': [[[2, 0], [0, 2]], [[2, 0], [0, -2]], [[2, 0], [0, 0]], [[2, 0], [0, 0]]],
        'contour_levels': np.linspace(-0.9, 1.8, 10).round(2).tolist(),
        'red_fill': 'region where f < f(0) = 0'})


def saddle_curvature():
    """Wireframe of x^2-y^2 and its restrictions along three directions."""
    fig, axes = figure(width_mm=150, height_mm=58, ncols=2)
    pos = axes[0].get_subplotspec()
    axes[0].remove()
    ax = fig.add_subplot(pos, projection='3d')
    g = np.linspace(-1, 1, 21)
    X, Y = np.meshgrid(g, g)
    ax.plot_wireframe(X, Y, X**2 - Y**2, color=BLUE, linewidth=.35, alpha=.55)
    s = np.linspace(-1, 1, 60)
    ax.plot(s, 0*s, s**2, color=GREEN, lw=1.6)
    ax.plot(0*s, s, -s**2, color=RED, lw=1.6)
    ax.scatter([0], [0], [0], color=INK, s=8, depthshade=False)
    ax.set_xlabel(r'$x$', labelpad=-8); ax.set_ylabel(r'$y$', labelpad=-8)
    ax.set_zlabel(r'$f$', labelpad=-8)
    ax.tick_params(labelsize=6, pad=-3)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 0))
    ax.view_init(elev=24, azim=-55)
    ax.set_title(r'(a) $f(x,y)=x^2-y^2$', y=0.98)
    ax2 = axes[1]
    t = np.linspace(-1, 1, 100)
    ax2.plot(t, t**2, color=GREEN, label=r'$\mathbf{d}=(1,0)$: $\mathbf{d}^{\mathrm{T}}\mathbf{H}\mathbf{d}=2$')
    ax2.plot(t, 0*t, color=YELLOW, label=r'$\mathbf{d}=(1,1)/\sqrt{2}$: $0$')
    ax2.plot(t, -t**2, color=RED, label=r'$\mathbf{d}=(0,1)$: $-2$')
    ax2.set(xlim=(-1, 1), ylim=(-1.15, 1.15), xlabel=r'$t$', ylabel=r'$f(t\mathbf{d})-f(\mathbf{0})$',
            title='(b) 沿方向的一元限制')
    ax2.legend(loc='lower left', fontsize=7, handlelength=1.4)
    save(fig, D/'c1-saddle-curvature', 'figure', {
        'f': 'x^2-y^2', 'H': [[2, 0], [0, -2]],
        'restrictions': {'(1,0)': 't^2', '(1,1)/sqrt2': '0', '(0,1)': '-t^2'}})


# ---------------------------------------------------------------- 1.5
def flat_gradient():
    """(a) equal slopes, unequal errors; (b) ill-conditioned ridge LS with x_hat=(11,-9)."""
    fig, axes = figure(width_mm=150, height_mm=58, ncols=2)
    ax = axes[0]
    x = np.linspace(-12, 12, 400)
    ax.plot(x, 0.01*x**2/2, color=BLUE, label=r'$f_1(x)=0.01x^2/2$')
    ax.plot(x, x**2/2, color=GREEN, label=r'$f_2(x)=x^2/2$')
    ax.plot([10], [0.5], 'o', color=BLUE, ms=3.5)
    ax.plot([0.1], [0.005], 'o', color=GREEN, ms=3.5)
    ax.vlines(10, 0, 0.5, color=BLUE, lw=.6, ls=':')
    ax.annotate('', xy=(0, 0.04), xytext=(10, 0.04),
                arrowprops=dict(arrowstyle='<->', color=BLUE, lw=.6))
    ax.text(5, 0.07, r'$|x-x^{\ast}|=10$', fontsize=7, color=BLUE, ha='center')
    ax.text(9.6, 0.25, r'$f_1-f_1^{\ast}=0.5$', fontsize=7, color=BLUE, ha='right', va='center')
    ax.text(7.2, 0.62, r'$f_1^{\prime}(10)=0.1$', fontsize=7, color=BLUE)
    ax.text(-11.5, 1.0, r'$f_2^{\prime}(0.1)=0.1$', fontsize=7, color=GREEN)
    ax.text(-11.5, 0.9, r'$f_2-f_2^{\ast}=0.005$', fontsize=7, color=GREEN)
    ax.set(xlim=(-12, 12), ylim=(0, 1.25), xlabel=r'$x$', title='(a) 同样的梯度，不同的误差')
    ax.legend(loc='upper right', fontsize=7, handlelength=1.4)
    ax = axes[1]
    lam = 0.01
    g = np.linspace(-14, 16, 401)
    X1, X2 = np.meshgrid(g, g)
    F = _ls(lam, X1, X2)
    c = 2/(2 + lam)
    fstar = 0.5*lam*4/(2 + lam)
    levels = [0.1, 0.5, 1.0, 2.0]
    ax.contour(X1, X2, F - fstar, levels=levels, colors=[MUTED], linewidths=.5)
    ax.plot(g, 2 - g, color=GREEN, lw=.8, ls='--')
    xh = np.array([11.0, -9.0])
    ax.plot([c], [c], 'o', color=GREEN, ms=3.5)
    ax.plot([xh[0]], [xh[1]], 'o', color=RED, ms=3.5)
    ax.text(c + 1.0, c + 1.2, r'$\mathbf{x}^{\ast}$', fontsize=NOTE, color=GREEN)
    ax.text(xh[0] - 2.0, xh[1] - 1.0, r'$\hat{\mathbf{x}}=(11,-9)$', fontsize=NOTE, color=RED, ha='right')
    ax.text(-13, -12.5, r'$x_1+x_2=2$', fontsize=7, color=GREEN)
    ax.set(xlim=(-14, 16), ylim=(-14, 16), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$',
           title=r'(b) $\lambda=0.01$')
    gr = np.array([1, 1])*(xh.sum() - 2) + lam*xh
    save(fig, D/'c1-flat-gradient', 'figure', {
        'panel_a': {'f1': '0.01x^2/2 at x=10', 'f2': 'x^2/2 at x=0.1', 'slope': 0.1,
                    'gaps': [0.5, 0.005], 'distances': [10, 0.1]},
        'panel_b': {'A': [[1, 1]], 'b': [2], 'lambda': lam, 'x_star': [c, c], 'f_star': fstar,
                    'x_hat': xh.tolist(), 'f_hat': float(_ls(lam, xh[0], xh[1])),
                    'gap': float(_ls(lam, xh[0], xh[1]) - fstar), 'grad': gr.tolist(),
                    'grad_norm': float(np.linalg.norm(gr)),
                    'distance': float(np.linalg.norm(xh - c)),
                    'contour_levels_of_f_minus_fstar': levels}})


def convergence_cost():
    """Model error sequences: 1/(t+1), 0.9^t, e_{t+1}=e_t^2 from 0.5; cost per round 1 and 40."""
    fig, axes = figure(width_mm=150, height_mm=54, ncols=2, sharey=True)
    T = 300
    t = np.arange(T + 1)
    sub = 1/(t + 1)
    lin = 0.9**t
    quad = [0.5]
    for _ in range(8):
        quad.append(quad[-1]**2)
    quad = np.array(quad)
    ax = axes[0]
    ax.semilogy(t, sub, color=YELLOW, label=r'$1/(t+1)$')
    ax.semilogy(t, lin, color=BLUE, label=r'$0.9^{t}$')
    ax.semilogy(np.arange(len(quad)), quad, color=RED, marker='o', ms=2.6, label=r'$e^{(t+1)}=(e^{(t)})^2$')
    ax.axhline(1e-8, color=MUTED, lw=.6, ls=':')
    ax.text(200, 2e-2, '次线性', fontsize=NOTE, color=YELLOW)
    ax.text(150, 1e-5, '线性', fontsize=NOTE, color=BLUE)
    ax.text(12, 1e-12, '二次', fontsize=NOTE, color=RED)
    ax.set(xlim=(0, 300), ylim=(1e-14, 2), xlabel=r'$t$', ylabel=r'$e^{(t)}$', title='(a) 按轮数比较')
    ax.legend(loc='lower right', fontsize=7, handlelength=1.4)
    ax = axes[1]
    ax.semilogy(t*1, lin, color=BLUE, label='线性序列，每轮代价1')
    ax.semilogy(np.arange(len(quad))*40, quad, color=RED, marker='o', ms=2.6, label='二次序列，每轮代价40')
    ax.axhline(1e-8, color=MUTED, lw=.6, ls=':')
    ax.text(5, 2.2e-8, r'$\varepsilon=10^{-8}$', fontsize=7, color=MUTED)
    ax.set(xlim=(0, 300), xlabel='累计代价', title='(b) 按总代价比较')
    ax.legend(loc='lower left', fontsize=7, handlelength=1.4)
    tl = int(np.ceil(np.log(1e8)/np.log(1/0.9)))
    tq = int(np.argmax(quad <= 1e-8))
    tl12 = int(np.ceil(np.log(1e12)/np.log(1/0.9)))
    tq12 = int(np.argmax(quad <= 1e-12))
    save(fig, D/'c1-convergence-cost', 'figure', {
        'sequences': {'sublinear': '1/(t+1)', 'linear': '0.9^t', 'quadratic': 'e0=0.5, e_{t+1}=e_t^2'},
        'cost_per_round': {'linear': 1, 'quadratic': 40},
        'rounds_to_1e-8': {'linear': tl, 'quadratic': tq, 'sublinear': int(1e8 - 1)},
        'cost_to_1e-8': {'linear': tl, 'quadratic': 40*tq},
        'rounds_to_1e-12': {'linear': tl12, 'quadratic': tq12},
        'cost_to_1e-12': {'linear': tl12, 'quadratic': 40*tq12},
        'note': 'model sequences generated by formulas, not measured algorithm runs'})


ALL = {f.__name__: f for f in [resource_region, failure_modes, local_global, extended_value,
                               existence_failures, lsc_gap, ls_sublevel, chord_tangent,
                               strong_convex_gap, stationary_types, saddle_curvature,
                               flat_gradient, convergence_cost]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(ALL)
    for n in names:
        ALL[n.replace('-', '_')]()
        print('saved', n)
