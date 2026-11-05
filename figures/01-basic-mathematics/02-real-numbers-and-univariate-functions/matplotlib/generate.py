# coding: utf-8
"""Analytic teaching charts for volume one, part 2 (real numbers and univariate functions).

Every curve is an explicit formula listed in the saved facts; no sampled data.
Run from any directory:  python3 figures/01-basic-mathematics/02-real-numbers-and-univariate-functions/matplotlib/generate.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL

D = Path(__file__).resolve().parent


def power_sequence_nonuniform():
    fig, ax = figure(height_mm=52)
    x = np.linspace(0, 1, 1201)
    ns = [1, 2, 5, 20, 80]
    colors = [BLUE, GREEN, YELLOW, RED, PURPLE]
    for n, c in zip(ns, colors):
        ax.plot(x, x**n, color=c, label=rf'$n={n}$')
        xc = 0.5**(1/n)
        ax.plot([xc], [0.5], 'o', color=c, ms=2.6)
    ax.plot([0, 1], [0, 0], color=MUTED, lw=2.2, alpha=.45, solid_capstyle='butt')
    ax.plot([1], [1], 'o', color=INK, ms=3.4)
    ax.plot([1], [0], 'o', mfc='white', mec=INK, ms=3.4)
    ax.axhline(0.5, color=MUTED, lw=.6, ls='--')
    ax.text(0.02, 0.53, '误差 1/2', color=MUTED, fontsize=7.5)
    ax.set(xlim=(0, 1.04), ylim=(-0.04, 1.06), xlabel=r'$x$', ylabel=r'$f_n(x)=x^n$')
    ax.set_xticks([0, .25, .5, .75, 1]); ax.set_yticks([0, .5, 1])
    ax.legend(loc='upper left', ncol=2, handlelength=1.6, columnspacing=1.2)
    save(fig, D/'power-sequence-nonuniform', 'figure', {
        'curves': 'f_n(x)=x**n on [0,1]', 'n': ns,
        'crossing_points': {str(n): 0.5**(1/n) for n in ns},
        'pointwise_limit': '0 on [0,1), 1 at x=1', 'sup_error_on_[0,1)': 1})


def geometric_partial_sums():
    fig, ax = figure(height_mm=54)
    x = np.linspace(-0.995, 0.93, 1600)
    ax.plot(x, 1/(1-x), color=INK, lw=1.3, label=r'$1/(1-x)$')
    for N, c, ls in [(2, BLUE, '-'), (5, GREEN, '-'), (10, PURPLE, '-')]:
        s = (1 - x**(N+1))/(1 - x)
        ax.plot(x, s, color=c, ls=ls, label=rf'$S_{{{N}}}(x)$')
    ax.axvline(1, color=MUTED, lw=.6, ls='--'); ax.axvline(-1, color=MUTED, lw=.6, ls='--')
    ax.set(xlim=(-1.05, 1.05), ylim=(-1, 8), xlabel=r'$x$', ylabel='函数值')
    ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_yticks([0, 2, 4, 6, 8])
    ax.legend(loc='upper left', handlelength=1.6)
    save(fig, D/'geometric-partial-sums', 'figure', {
        'partial_sums': 'S_N(x)=(1-x**(N+1))/(1-x)', 'N': [2, 5, 10], 'limit': '1/(1-x) for |x|<1',
        'error': '|x|**(N+1)/|1-x|', 'x_range': [-0.995, 0.93], 'y_clip': [-1, 8]})


def convex_chord_tangent():
    fig, ax = figure(height_mm=50)
    x = np.linspace(-2.2, 1.6, 800)
    f = lambda t: np.exp(t)/2
    ax.plot(x, f(x), color=INK, lw=1.3, label=r'$f(x)=e^x/2$')
    a, b = -1.5, 1.0
    ax.plot([a, b], [f(a), f(b)], color=GREEN, lw=1.1, label='弦')
    ax.plot([a, b], [f(a), f(b)], 'o', color=GREEN, ms=3)
    ax.plot(x, 0.5 + 0.5*x, color=BLUE, lw=1.1, ls='--', label='切线')
    ax.plot([0], [0.5], 'o', color=BLUE, ms=3)
    xs = np.linspace(a, b, 200)
    ax.fill_between(xs, f(xs), f(a) + (f(b)-f(a))/(b-a)*(xs-a), color=GREEN_FILL, lw=0)
    ax.set(xlim=(-2.2, 1.6), ylim=(-0.6, 2.4), xlabel=r'$x$', ylabel=r'$y$')
    ax.set_xticks([-2, -1.5, -1, 0, 1]); ax.set_yticks([0, 1, 2])
    ax.legend(loc='upper left', handlelength=1.8)
    save(fig, D/'convex-chord-tangent', 'figure', {
        'function': 'exp(x)/2', 'chord_endpoints': [a, b], 'tangent_point': 0,
        'tangent_line': 'y=1/2+x/2', 'shaded': 'region between graph and chord on [a,b]'})


def finite_difference_error():
    fig, ax = figure(height_mm=56)
    x0 = 1.0
    exact = np.exp(x0)
    hs = np.logspace(-15, -0.3, 300)
    fwd = np.array([abs((np.exp(x0+h)-np.exp(x0))/h - exact) for h in hs])
    cen = np.array([abs((np.exp(x0+h)-np.exp(x0-h))/(2*h) - exact) for h in hs])
    eps = np.finfo(float).eps
    ax.loglog(hs, fwd, 'o', color=BLUE, ms=1.6, label='前向差分')
    ax.loglog(hs, cen, 's', color=GREEN, ms=1.6, label='中心差分')
    ax.loglog(hs, exact*hs/2 + 2*eps*exact/hs, color=BLUE, lw=.8, ls='--')
    ax.loglog(hs, exact*hs**2/6 + eps*exact/hs, color=GREEN, lw=.8, ls='--')
    ax.set(xlim=(1e-15, 0.5), ylim=(1e-12, 10), xlabel=r'$h$', ylabel='绝对误差')
    ax.set_xticks([1e-15, 1e-12, 1e-9, 1e-6, 1e-3]); ax.set_yticks([1e-12, 1e-9, 1e-6, 1e-3, 1])
    ax.legend(loc='upper right')
    hopt_f = 2*np.sqrt(eps); hopt_c = (3*eps)**(1/3)
    save(fig, D/'finite-difference-error', 'figure', {
        'function': 'exp', 'x0': x0, 'arithmetic': 'IEEE double precision (numpy float64)',
        'h_grid': 'logspace(-15,-0.3,300)', 'machine_epsilon': eps,
        'model_forward': 'e*h/2+2*eps*e/h', 'model_central': 'e*h**2/6+eps*e/h',
        'model_optimal_h': {'forward': hopt_f, 'central': hopt_c}})


def riemann_sums():
    import matplotlib.patches as mp
    fig, axes = figure(width_mm=169, height_mm=52, ncols=2)
    x = np.linspace(0, 3, 600)
    pts = [0, 0.4, 1.0, 1.4, 2.1, 2.5, 3.0]
    tags = [0.3, 0.55, 1.3, 1.6, 2.3, 2.9]
    ax = axes[0]
    for a, b, t in zip(pts[:-1], pts[1:], tags):
        v = np.cos(t)
        c, fc = (BLUE, BLUE_FILL) if v >= 0 else (RED, '#F0E5E6')
        ax.add_patch(mp.Rectangle((a, 0), b-a, v, facecolor=fc, edgecolor=c, lw=.7))
        ax.plot([t], [v], 'o', color=INK, ms=2.6)
    ax.plot(x, np.cos(x), color=INK, lw=1.2)
    ax.axhline(0, color=MUTED, lw=.6)
    ax.set(xlim=(0, 3), ylim=(-1.1, 1.1), xlabel=r'$x$', ylabel=r'$\cos x$', title='(a) 一个黎曼和')
    ax = axes[1]
    n = 12; xs = np.linspace(0, 3, n+1)
    for a, b in zip(xs[:-1], xs[1:]):
        lo, hi = np.cos(b), np.cos(a)  # cos decreasing on [0, 3]
        ax.add_patch(mp.Rectangle((a, 0), b-a, lo, facecolor=BLUE_FILL, edgecolor=BLUE, lw=.6))
        ax.add_patch(mp.Rectangle((a, lo), b-a, hi-lo, facecolor=GREEN_FILL, edgecolor=GREEN, lw=.6))
    ax.plot(x, np.cos(x), color=INK, lw=1.2)
    ax.axhline(0, color=MUTED, lw=.6)
    ax.set(xlim=(0, 3), ylim=(-1.1, 1.1), xlabel=r'$x$', title='(b) 下和与上和')
    U = sum((xs[1]-xs[0])*np.cos(a) for a in xs[:-1]); Lw = sum((xs[1]-xs[0])*np.cos(b) for b in xs[1:])
    save(fig, D/'riemann-sums', 'figure', {
        'function': 'cos(x) on [0,3]', 'panel_a_partition': pts, 'panel_a_tags': tags,
        'panel_a_sum': float(sum((b-a)*np.cos(t) for a, b, t in zip(pts[:-1], pts[1:], tags))),
        'panel_b_equal_segments': n, 'upper_sum': float(U), 'lower_sum': float(Lw), 'U_minus_L': float(U-Lw),
        'exact_integral': float(np.sin(3))})


def narrow_spikes():
    fig, ax = figure(height_mm=50)
    for n, c in [(2, BLUE), (4, GREEN), (8, PURPLE)]:
        xs = [0, 1/n, 2/n, 1]; ys = [0, n, 0, 0]
        ax.plot(xs, ys, color=c, label=rf'$f_{{{n}}}$')
    ax.set(xlim=(0, 1), ylim=(0, 8.6), xlabel=r'$x$', ylabel=r'$f_n(x)$')
    ax.set_xticks([0, .25, .5, 1]); ax.set_yticks([0, 2, 4, 8])
    ax.legend(loc='upper right')
    save(fig, D/'narrow-spikes', 'figure', {
        'definition': 'triangle on [0,2/n] with apex (1/n,n), zero elsewhere', 'n': [2, 4, 8],
        'integral_each': 1, 'pointwise_limit': 0, 'sup_norm': 'n'})


def quadrature_rules():
    fig, axes = figure(width_mm=169, height_mm=54, ncols=2)
    ax = axes[0]
    f = lambda t: np.exp(2*t)/3
    x = np.linspace(0, 1, 400)
    ax.fill_between([0, 1], [f(.5), f(.5)], color=YELLOW_FILL, lw=0)
    ax.plot([0, 1], [f(.5), f(.5)], color=YELLOW, lw=1.1, label='中点矩形')
    ax.plot([0, 1], [f(0), f(1)], color=GREEN, lw=1.1, ls='--', label='梯形直线')
    # quadratic through the three nodes 0, 1/2, 1
    A = f(.5); C = (f(0)+f(1)-2*f(.5))/(2*.25); B = (f(1)-f(0))/1.0
    ax.plot(x, A + B*(x-.5) + C*(x-.5)**2, color=PURPLE, lw=1.1, ls='-.', label='Simpson抛物线')
    ax.plot(x, f(x), color=INK, lw=1.3, label=r'$f(x)$')
    ax.plot([0, .5, 1], [f(0), f(.5), f(1)], 'o', color=INK, ms=3)
    ax.set(xlim=(-0.02, 1.02), ylim=(0, 2.6), xlabel=r'$x$', title='(a) 一段上的近似')
    ax.set_xticks([0, .5, 1]); ax.legend(loc='upper left', fontsize=7)
    ax = axes[1]
    exact = np.e - 1
    ns = np.array([2, 4, 8, 16, 32, 64, 128, 256])
    def left(n): h = 1/n; return h*np.exp(np.arange(n)*h).sum()
    def mid(n): h = 1/n; return h*np.exp(np.arange(n)*h + h/2).sum()
    def trap(n): h = 1/n; y = np.exp(np.arange(n+1)*h); return h*(y.sum() - (y[0]+y[-1])/2)
    def simp(n): h = 1/n; y = np.exp(np.arange(n+1)*h); return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
    data = {}
    for name, rule, c, m in [('左矩形', left, BLUE, 'o'), ('中点', mid, YELLOW, 's'), ('梯形', trap, GREEN, '^'), ('Simpson', simp, PURPLE, 'D')]:
        err = np.array([abs(rule(n) - exact) for n in ns])
        ax.loglog(ns, err, marker=m, color=c, ms=3, lw=1, label=name)
        data[name] = err.tolist()
    ax.set(xlabel='段数 n', ylabel='绝对误差', title='(b) 积分误差随段数的变化')
    ax.set_xticks([2, 8, 32, 128]); ax.set_xticklabels(['2', '8', '32', '128'])
    ax.legend(loc='lower left', fontsize=7)
    save(fig, D/'quadrature-rules', 'figure', {
        'panel_a_function': 'exp(2x)/3 on [0,1]', 'panel_b_integrand': 'exp(x) on [0,1]', 'exact': exact,
        'n': ns.tolist(), 'errors': data, 'arithmetic': 'IEEE double precision'})


def quadrature_comparison():
    """Same integrand, same interval: constant, linear and quadratic local approximations."""
    from support import RED_FILL
    fig, grid = figure(width_mm=169, height_mm=92, nrows=2, ncols=3, gridspec_kw={'height_ratios': [2, 1.15]})
    axes, lower = grid[0], grid[1]
    f = lambda t: np.exp(2*t)/3
    exact = (np.exp(2) - 1)/6
    x = np.linspace(0, 1, 600)
    A = f(.5); B = f(1) - f(0); C = (f(0) + f(1) - 2*f(.5))/(2*.25)
    rules = [
        ('(a) 中点矩形：常数', np.full_like(x, f(.5)), [.5], f(.5)),
        ('(b) 梯形：直线', f(0) + (f(1) - f(0))*x, [0, 1], (f(0) + f(1))/2),
        ('(c) Simpson：抛物线', A + B*(x-.5) + C*(x-.5)**2, [0, .5, 1], (f(0) + 4*f(.5) + f(1))/6),
    ]
    facts = {'integrand': 'exp(2x)/3 on [0,1]', 'exact': float(exact), 'rules': {}}
    for k, (ax, low, (title, p, nodes, value)) in enumerate(zip(axes, lower, rules)):
        y = f(x)
        d = p - y
        low.axhline(0, color=MUTED, lw=.6)
        low.fill_between(x, 0, d, where=d > 0, interpolate=True, color=RED_FILL, lw=0)
        low.fill_between(x, d, 0, where=d < 0, interpolate=True, color=YELLOW_FILL, lw=0)
        low.plot(x, d, color=BLUE, lw=1.1)
        low.plot(nodes, np.zeros(len(nodes)), 'o', color=INK, ms=3, zorder=5)
        span = 1.15*np.abs(d).max()
        low.set(xlim=(0, 1), ylim=(-span, span), xlabel=r'$x$')
        low.set_xticks([0, .5, 1])
        if k == 0:
            low.set_ylabel('近似函数 − f(x)')
        if k > 0:
            ax.set_yticklabels([])
        facts.setdefault('max_abs_pointwise_gap', {})[title] = float(np.abs(d).max())
        ax.fill_between(x, 0, np.minimum(y, p), color=BLUE_FILL, lw=0, label='两者共有的面积')
        ax.fill_between(x, y, p, where=p > y, interpolate=True, color=RED_FILL, lw=0, label='近似多算')
        ax.fill_between(x, p, y, where=p < y, interpolate=True, color=YELLOW_FILL, lw=0, label='近似少算')
        ax.plot(x, p, color=BLUE, lw=1.1, label='近似函数')
        ax.plot(x, y, color=INK, lw=1.2, label=r'$f(x)$')
        ax.plot(nodes, f(np.array(nodes)), 'o', color=INK, ms=3, zorder=5)
        err = value - exact
        sign = '−' if err < 0 else '+'
        ax.set_title(f'{title}\n近似值 {value:.3f}，误差 {sign}{abs(err):.3f}')
        ax.set(xlim=(0, 1), ylim=(0, 2.6))
        ax.set_xticks([0, .5, 1])
        facts['rules'][title] = {'nodes': nodes, 'approximation': float(value), 'signed_error': float(err)}
    axes[0].legend(loc='upper left', handlelength=1.6)
    save(fig, D/'quadrature-comparison', 'figure', facts)


def function_properties():
    fig, axes = figure(width_mm=169, height_mm=54, ncols=3)
    # (a) monotonicity: strictly increasing f and non-decreasing g with a flat piece
    ax = axes[0]
    f = lambda t: 0.85 + 0.45*t + 0.1*np.sin(2*t)          # f' = 0.45 + 0.2 cos 2t > 0
    g = lambda t: np.piecewise(t, [t <= 1, (t > 1) & (t <= 2), t > 2],
                               [lambda s: 0.15 + 0.55*s, 0.7, lambda s: 0.7 + 0.55*(s - 2)])
    x = np.linspace(0, 3, 400)
    ax.plot(x, g(x), color=GREEN, label='单调不减 g')
    ax.plot(x, f(x), color=BLUE, label='严格递增 f')
    x1, x2 = 0.7, 2.3
    for xi in (x1, x2):
        ax.plot([xi, xi, 0], [0, f(xi), f(xi)], color=MUTED, lw=.6, ls='--')
        ax.plot([xi], [f(xi)], 'o', color=BLUE, ms=3)
    ax.set(xlim=(0, 3.1), ylim=(0, 2.5), xlabel=r'$x$', title='(a) 单调性')
    ax.set_xticks([x1, x2], [r'$x_1$', r'$x_2$'])
    ax.set_yticks([f(x1), f(x2)], [r'$f(x_1)$', r'$f(x_2)$'])
    ax.legend(loc='upper left', handlelength=1.6)
    # (b) parity: even f (symmetric about the vertical axis), odd g (symmetric about the origin)
    ax = axes[1]
    a = 1.2
    fe = lambda t: 0.35*t**2 + 0.35
    go = lambda t: 0.25*t**3
    x = np.linspace(-1.8, 1.8, 400)
    ax.axhline(0, color=MUTED, lw=.6); ax.axvline(0, color=MUTED, lw=.6)
    ax.plot(x, fe(x), color=BLUE, label='偶函数 f')
    ax.plot(x, go(x), color=GREEN, label='奇函数 g')
    ax.plot([-a, a], [fe(a), fe(a)], color=BLUE, lw=.6, ls='--')
    ax.plot([-a, a], [fe(a), fe(a)], 'o', color=BLUE, ms=3)
    ax.plot([-a, a], [go(-a), go(a)], color=GREEN, lw=.6, ls='--')
    ax.plot([-a, a], [go(-a), go(a)], 'o', color=GREEN, ms=3)
    ax.plot([0], [0], 'o', color=INK, ms=2.2)
    ax.set(xlim=(-1.9, 1.9), ylim=(-1.6, 1.7), xlabel=r'$x$', title='(b) 奇偶性')
    ax.set_xticks([-a, 0, a], [r'$-a$', r'$0$', r'$a$']); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.legend(loc='upper center', ncol=2, handlelength=1.4, columnspacing=1.0)
    # (c) periodicity with period T = 2
    ax = axes[2]
    T, x0 = 2.0, 0.25
    fp = lambda t: np.sin(np.pi*t) + 0.35*np.sin(2*np.pi*t)
    x = np.linspace(-0.3, 4.45, 800)
    ax.axvspan(x0, x0 + T, color=BLUE_FILL, lw=0)
    ax.axhline(0, color=MUTED, lw=.6)
    ax.plot(x, fp(x), color=BLUE)
    xs = [x0, x0 + T, x0 + 2*T]
    for xi in xs:
        ax.plot([xi, xi], [-1.5, fp(xi)], color=MUTED, lw=.6, ls='--')
        ax.plot([xi], [fp(xi)], 'o', color=BLUE, ms=3)
    for left in xs[:2]:
        ax.annotate('', xy=(left + T, 1.6), xytext=(left, 1.6),
                    arrowprops=dict(arrowstyle='<->', color=INK, lw=.6, shrinkA=0, shrinkB=0))
        ax.text(left + T/2, 1.68, r'$T$', ha='center', va='bottom')
    ax.set(xlim=(-0.3, 4.5), ylim=(-1.5, 2.05), xlabel=r'$x$', title='(c) 周期性')
    ax.set_xticks(xs, [r'$x_0$', r'$x_0+T$', r'$x_0+2T$']); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    save(fig, D/'function-properties', 'figure', {
        'panel_a_strict': '0.85+0.45x+0.1 sin(2x) on [0,3]',
        'panel_a_nondecreasing': 'piecewise linear: 0.15+0.55x (x<=1), 0.7 (1<=x<=2), 0.7+0.55(x-2) (x>=2)',
        'panel_a_inputs': [x1, x2], 'panel_a_values': [float(f(x1)), float(f(x2))],
        'panel_b_even': '0.35x^2+0.35', 'panel_b_odd': '0.25x^3', 'panel_b_domain': [-1.8, 1.8], 'a': a,
        'panel_c_function': 'sin(pi x)+0.35 sin(2 pi x)', 'period_T': T, 'x0': x0,
        'panel_c_marked_values': [float(fp(t)) for t in xs]})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [power_sequence_nonuniform, geometric_partial_sums, convex_chord_tangent, finite_difference_error, riemann_sums, narrow_spikes, quadrature_rules, quadrature_comparison, function_properties]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
