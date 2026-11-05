# coding: utf-8
"""Teaching figures for volume three, part "optimization", chapter 7
(multiobjective, minimax and bilevel optimization).

Every number comes from a closed-form expression or a deterministic iteration
recorded in the facts file of the figure; no randomness is used.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/01-optimization/matplotlib/generate_c7.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import (figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID,
                     BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL)

D = Path(__file__).resolve().parent

# Common finite example: (latency f1, error f2) of six candidate schemes.
CANDS = {'A': (1.0, 5.0), 'B': (2.0, 2.5), 'C': (3.5, 2.2),
         'D': (5.0, 1.0), 'E': (4.0, 4.0), 'F': (6.0, 1.0)}
PARETO = ['A', 'B', 'C', 'D']


def _cands_axes(ax, labels=True, colors=None):
    colors = colors or {}
    for k, (u, v) in CANDS.items():
        if k in PARETO:
            ax.plot(u, v, 'o', ms=4.2, color=colors.get(k, BLUE), zorder=4)
        elif k == 'F':
            ax.plot(u, v, 's', ms=3.8, mfc='white', mec=YELLOW, mew=1.0, zorder=4)
        else:
            ax.plot(u, v, 'o', ms=3.8, mfc='white', mec=MUTED, mew=.9, zorder=4)
        if labels:
            ax.annotate(k, (u, v), xytext=(4, 3), textcoords='offset points', fontsize=7.5, color=INK)
    ax.set(xlim=(0, 7), ylim=(0, 6), xlabel=r'$f_1$', ylabel=r'$f_2$')
    ax.set_xticks(range(0, 8)); ax.set_yticks(range(0, 7))


def pareto_candidates():
    fig, ax = figure(width_mm=92, height_mm=66)
    # dominated region of B (closed upper-right quadrant minus B)
    ax.fill_between([2, 7], 2.5, 6, color=BLUE_FILL, lw=0, zorder=0)
    ax.fill_between([5, 7], 1, 6, color=YELLOW_FILL, lw=0, zorder=0)
    ax.fill_between([5, 7], 2.5, 6, color=GREEN_FILL, lw=0, zorder=0)
    ax.plot([2, 7], [2.5, 2.5], color=BLUE, lw=.6, ls='--'); ax.plot([2, 2], [2.5, 6], color=BLUE, lw=.6, ls='--')
    ax.plot([5, 7], [1, 1], color=YELLOW, lw=.6, ls='--'); ax.plot([5, 5], [1, 6], color=YELLOW, lw=.6, ls='--')
    xs = [CANDS[k][0] for k in PARETO]; ys = [CANDS[k][1] for k in PARETO]
    ax.step(xs + [7], ys + [ys[-1]], where='post', color=BLUE, lw=.8, alpha=.0)
    ax.plot(xs, ys, color=BLUE, lw=.9, ls=':')
    _cands_axes(ax)
    ax.text(2.2, 5.55, '被 B 支配', fontsize=7.5, color=BLUE)
    ax.text(5.2, 1.55, '被 D 支配', fontsize=7.5, color=YELLOW)
    save(fig, D/'c7-pareto-candidates', 'figure', {
        'candidates (f1 latency, f2 error)': CANDS,
        'pareto_optimal': PARETO, 'dominated': {'E': 'by B and C', 'F': 'by D'},
        'weak_pareto_only': ['F'],
        'shaded': 'B + R^2_{>=0} (blue), D + R^2_{>=0} (yellow), overlap (green)'})


def pareto_set_front():
    fig, (a1, a2) = figure(width_mm=150, height_mm=62, ncols=2)
    s = np.linspace(-2.2, 2.2, 401)
    X, Y = np.meshgrid(s, s)
    F1 = ((X-1)**2 + Y**2)/2; F2 = ((X+1)**2 + Y**2)/2
    lv = [0.125, 0.5, 1.0, 1.5, 2.25]
    a1.contour(X, Y, F1, levels=lv, colors=BLUE, linewidths=.6)
    a1.contour(X, Y, F2, levels=lv, colors=GREEN, linewidths=.6, linestyles='--')
    a1.plot([-1, 1], [0, 0], color=INK, lw=2.0, solid_capstyle='butt')
    a1.plot([1], [0], 'o', color=BLUE, ms=3.6); a1.plot([-1], [0], 'o', color=GREEN, ms=3.6)
    a1.annotate(r'$\mathbf{a}$', (1, 0), xytext=(3, -10), textcoords='offset points', color=BLUE)
    a1.annotate(r'$\mathbf{b}$', (-1, 0), xytext=(-9, -10), textcoords='offset points', color=GREEN)
    a1.plot([0], [1], 'o', color=RED, ms=3.6); a1.annotate(r'$\mathbf{p}$', (0, 1), xytext=(4, 2), textcoords='offset points', color=RED)
    a1.plot([0], [0], 'o', mfc='white', mec=INK, ms=3.6)
    a1.annotate('', xy=(0, 0.06), xytext=(0, 0.94), arrowprops=dict(arrowstyle='->', color=RED, lw=.8))
    a1.text(-0.62, -0.42, 'Pareto 集合', fontsize=7.5, color=INK)
    a1.set(xlim=(-2.2, 2.2), ylim=(-2.2, 2.2), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$', title='(a) 参数空间')
    # objective space: image of the plane is {f1+f2 >= 1 + (f1-f2)^2/4}
    g = np.linspace(0, 4.5, 500)
    U, V = np.meshgrid(g, g)
    region = (U + V >= 1 + (U - V)**2/4)
    a2.contourf(U, V, region.astype(float), levels=[.5, 1.5], colors=[BLUE_FILL])
    t = np.linspace(-2.2, 2.2, 400)
    a2.plot((t-1)**2/2, (t+1)**2/2, color=MUTED, lw=.7)
    tt = np.linspace(-1, 1, 200)
    a2.plot((tt-1)**2/2, (tt+1)**2/2, color=INK, lw=2.0)
    a2.plot([0], [2], 'o', color=BLUE, ms=3.6); a2.plot([2], [0], 'o', color=GREEN, ms=3.6)
    a2.annotate(r'$\mathbf{f}(\mathbf{a})$', (0, 2), xytext=(4, 3), textcoords='offset points', color=BLUE, fontsize=7.5, bbox=dict(fc='white', ec='none', pad=.6))
    a2.annotate(r'$\mathbf{f}(\mathbf{b})$', (2, 0), xytext=(2, 4), textcoords='offset points', color=GREEN, fontsize=7.5)
    a2.plot([1], [1], 'o', color=RED, ms=3.6); a2.annotate(r'$\mathbf{f}(\mathbf{p})$', (1, 1), xytext=(4, 2), textcoords='offset points', color=RED, fontsize=7.5)
    a2.plot([.5], [.5], 'o', mfc='white', mec=INK, ms=3.6)
    a2.annotate('', xy=(.54, .54), xytext=(.96, .96), arrowprops=dict(arrowstyle='->', color=RED, lw=.8))
    a2.text(2.3, 3.4, '可达集合', fontsize=7.5, color=BLUE)
    a2.text(0.62, 0.02, 'Pareto 前沿', fontsize=7.5, color=INK, rotation=-38)
    a2.set(xlim=(0, 4.5), ylim=(0, 4.5), aspect='equal', xlabel=r'$f_1$', ylabel=r'$f_2$', title='(b) 目标空间')
    save(fig, D/'c7-pareto-set-front', 'figure', {
        'objectives': 'f1=||x-a||^2/2, f2=||x-b||^2/2, a=(1,0), b=(-1,0)',
        'pareto_set': 'segment {(s,0): -1<=s<=1}',
        'front': '(f1,f2)=((s-1)^2/2,(s+1)^2/2), -1<=s<=1',
        'attainable_set': 'f1+f2 >= 1 + (f1-f2)^2/4',
        'point_p': {'x': [0, 1], 'f': [1, 1], 'improved_to': {'x': [0, 0], 'f': [0.5, 0.5]}},
        'contour_levels': lv})


def _dented_front(n=1201):
    u = np.linspace(0, 1, n)
    v = (1-u)**2 + 0.12*np.exp(-((u-0.45)/0.12)**2)
    return u, v


def _lower_hull(u, v):
    pts = sorted(zip(u, v))
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            if (x2-x1)*(p[1]-y1) - (y2-y1)*(p[0]-x1) <= 0:
                hull.pop()
            else:
                break
        hull.append(p)
    return np.array(hull)


def _dent_interval(u, v):
    hull = _lower_hull(u, v)
    hv = np.interp(u, hull[:, 0], hull[:, 1])
    gap = v - hv
    idx = np.where(gap > 1e-6)[0]
    return u[idx[0]], u[idx[-1]], hull


def weighted_sum():
    u, v = _dented_front()
    assert np.all(np.diff(v) < 0)
    lo, hi, hull = _dent_interval(u, v)
    fig, (a1, a2) = figure(width_mm=150, height_mm=62, ncols=2)
    a1.fill_between(u, v, 1.35, color=BLUE_FILL, lw=0)
    a1.plot(u, v, color=INK, lw=1.1)
    m = (u > lo) & (u < hi)
    a1.plot(u[m], v[m], color=RED, lw=2.0)
    a1.plot(hull[:, 0], hull[:, 1], color=MUTED, lw=.6, ls=':')
    facts_lines = []
    for alpha, col in [(0.62, GREEN), (0.5, YELLOW), (0.3, PURPLE)]:
        val = alpha*u + (1-alpha)*v
        k = int(np.argmin(val)); c = val[k]
        xx = np.linspace(-0.05, 1.05, 10)
        a1.plot(xx, (c - alpha*xx)/(1-alpha), color=col, lw=.8, ls='--')
        a1.plot(u[k], v[k], 'o', color=col, ms=3.8, zorder=5)
        facts_lines.append({'alpha': alpha, 'argmin_u': round(float(u[k]), 4), 'argmin_v': round(float(v[k]), 4)})
    a1.text(0.47, 0.62, '凹陷段', color=RED, fontsize=7.5)
    a1.set(xlim=(0, 1.05), ylim=(0, 1.3), xlabel=r'$f_1$', ylabel=r'$f_2$', title='(a) 支撑线只碰到凸包上的点')
    # (b) finite candidates and three supporting lines
    _cands_axes(a2)
    for alpha, col, name in [(0.2, GREEN, 'D'), (0.5, YELLOW, 'B'), (0.85, PURPLE, 'A')]:
        vals = {k: alpha*p[0] + (1-alpha)*p[1] for k, p in CANDS.items()}
        best = min(vals.values())
        xx = np.linspace(0, 7, 10)
        a2.plot(xx, (best - alpha*xx)/(1-alpha), color=col, lw=.8, ls='--')
    a2.plot([2, 5], [2.5, 1], color=MUTED, lw=.6, ls=':')
    a2.set_title('(b) 有限候选：C 不会被选中')
    save(fig, D/'c7-weighted-sum', 'figure', {
        'panel_a_front': 'v=(1-u)^2+0.12*exp(-((u-0.45)/0.12)^2), 0<=u<=1 (strictly decreasing, checked)',
        'panel_a_unsupported_interval_u': [round(float(lo), 4), round(float(hi), 4)],
        'panel_a_lines': facts_lines,
        'panel_b_candidates': CANDS,
        'panel_b_lines': {'alpha=0.2': 'D (value 1.8)', 'alpha=0.5': 'B (value 2.25)', 'alpha=0.85': 'A (value 1.6)'},
        'C_never_selected': 'C<B needs alpha<1/6, C<D needs alpha>4/9'})


def threshold():
    u, v = _dented_front()
    lo, hi, hull = _dent_interval(u, v)
    fig, (a1, a2) = figure(width_mm=150, height_mm=62, ncols=2)
    a1.fill_between(u, v, 1.35, color=BLUE_FILL, lw=0)
    a1.plot(u, v, color=INK, lw=1.1)
    m = (u > lo) & (u < hi)
    a1.plot(u[m], v[m], color=RED, lw=2.0)
    taus = [0.2, 0.4, 0.55, 0.8]
    sel = []
    for tau in taus:
        a1.axvline(tau, color=GREEN, lw=.6, ls='--')
        k = np.searchsorted(u, tau, side='right') - 1
        a1.plot(u[k], v[k], 'o', color=GREEN, ms=3.8, zorder=5)
        sel.append({'tau': tau, 'f2': round(float(v[k]), 4)})
        a1.text(tau+0.01, 1.22, rf'$\tau={tau:g}$', fontsize=7, color=GREEN)
    a1.set(xlim=(0, 1.05), ylim=(0, 1.3), xlabel=r'$f_1$', ylabel=r'$f_2$', title='(a) 阈值约束扫过整条前沿')
    # (b) selections: weighted sum vs threshold on the finite example
    order = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5}
    al = np.linspace(0, 1, 1001)
    pick_w = []
    for a in al:
        vals = {k: a*p[0] + (1-a)*p[1] for k, p in CANDS.items()}
        best = min(vals.values())
        ks = [k for k in vals if abs(vals[k]-best) < 1e-12]
        pick_w.append(order[sorted(ks)[0]])
    tau = np.linspace(1, 7, 1201)
    pick_t = []
    for t in tau:
        feas = {k: p[1] for k, p in CANDS.items() if p[0] <= t}
        best = min(feas.values())
        ks = sorted([k for k in feas if feas[k] == best])
        pick_t.append(order[ks[0]])
    ax2 = a2
    ax2.step(al, pick_w, where='post', color=BLUE, lw=1.1, label='加权和（横轴为 α）')
    ax2.step((tau-1)/6, pick_t, where='post', color=GREEN, lw=1.1, ls='--', label='阈值法（横轴为 (τ−1)/6）')
    ax2.set_yticks([1, 2, 3, 4]); ax2.set_yticklabels(['A', 'B', 'C', 'D'])
    ax2.set(xlim=(0, 1), ylim=(0.5, 5.0), xlabel=r'参数（归一化）', ylabel='返回的候选', title='(b) 两种标量化的选择')
    ax2.legend(loc='upper right', fontsize=7)
    save(fig, D/'c7-threshold', 'figure', {
        'panel_a_front': 'same as c7-weighted-sum panel a', 'panel_a_selections': sel,
        'panel_a_unsupported_interval_u': [round(float(lo), 4), round(float(hi), 4)],
        'panel_b_weighted': 'alpha in [0,1/3): D (alpha=0 ties D,F), (1/3,5/7): B, (5/7,1]: A; ties broken alphabetically',
        'panel_b_threshold': 'tau in [1,2): A, [2,3.5): B, [3.5,5): C, [5,inf): D (tau>=6 ties D,F)',
        'candidates': CANDS})


def _mgda_dir(g1, g2):
    d = g1 - g2
    den = d @ d
    a = 0.5 if den == 0 else float(np.clip(-(g2 @ d)/den, 0, 1))
    return a*g1 + (1-a)*g2, a


def common_descent():
    a = np.array([1.0, 0.0]); b = np.array([-1.0, 0.0])
    fig, (a1, a2) = figure(width_mm=150, height_mm=64, ncols=2)
    p = np.array([0.0, 1.0])
    th = np.linspace(0, 2*np.pi, 400); r = np.sqrt(2)
    c1 = a + r*np.c_[np.cos(th), np.sin(th)]; c2 = b + r*np.c_[np.cos(th), np.sin(th)]
    # lens where both objectives are smaller than at p
    s = np.linspace(-1.5, 1.5, 500); X, Y = np.meshgrid(s, s)
    lens = (((X-1)**2+Y**2) < 2) & (((X+1)**2+Y**2) < 2)
    a1.contourf(X, Y, lens.astype(float), levels=[.5, 1.5], colors=[YELLOW_FILL])
    a1.plot(c1[:, 0], c1[:, 1], color=BLUE, lw=.7); a1.plot(c2[:, 0], c2[:, 1], color=GREEN, lw=.7, ls='--')
    g1 = p - a; g2 = p - b
    gbar, al = _mgda_dir(g1, g2)
    sc = 0.5
    for g, col, lab, off in [(g1, BLUE, r'$\nabla f_1$', (-22, 2)), (g2, GREEN, r'$\nabla f_2$', (3, 2))]:
        a1.annotate('', xy=p+sc*g, xytext=p, arrowprops=dict(arrowstyle='->', color=col, lw=1.0))
        a1.annotate(lab, p+sc*g, xytext=off, textcoords='offset points', color=col, fontsize=7.5)
    a1.plot([p[0]+sc*g1[0], p[0]+sc*g2[0]], [p[1]+sc*g1[1], p[1]+sc*g2[1]], color=INK, lw=.8, ls=':')
    a1.annotate('', xy=p+sc*gbar, xytext=p, arrowprops=dict(arrowstyle='->', color=INK, lw=1.0))
    a1.annotate(r'$\bar{\mathbf{g}}$', p+sc*gbar, xytext=(2, 3), textcoords='offset points', color=INK, fontsize=7.5)
    # common descent cone {d: d2 < -|d1|}
    cone = np.array([p, p+0.75*np.array([-1, -1]), p+0.75*np.array([1, -1])])
    a1.fill(cone[:, 0], cone[:, 1], color=RED_FILL, lw=0, alpha=1, zorder=1)
    a1.annotate('', xy=p-1.0*gbar, xytext=p, arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    a1.annotate(r'$-\bar{\mathbf{g}}$', p-1.0*gbar, xytext=(5, 4), textcoords='offset points', color=RED, fontsize=7.5)
    a1.plot(*p, 'o', color=INK, ms=3.4, zorder=6)
    a1.annotate(r'$\mathbf{p}$', p, xytext=(-11, 3), textcoords='offset points', fontsize=7.5)
    a1.plot([-1, 1], [0, 0], color=INK, lw=1.6)
    a1.set(xlim=(-1.6, 1.6), ylim=(-1.0, 1.8), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$', title='(a) 点 p=(0,1) 处')
    # (b) MGDA paths with fixed step eta=0.5
    eta = 0.5
    starts = [np.array([0.0, 1.5]), np.array([1.9, 1.2]), np.array([-1.8, -1.2]), np.array([1.6, -1.4])]
    paths = []
    for x0 in starts:
        x = x0.copy(); P = [x.copy()]
        for t in range(25):
            gb, _ = _mgda_dir(x-a, x-b)
            if np.linalg.norm(gb) < 1e-10:
                break
            x = x - eta*gb; P.append(x.copy())
        P = np.array(P); paths.append(P)
        a2.plot(P[:, 0], P[:, 1], '-o', color=PURPLE, ms=1.8, lw=.8)
        a2.plot(*P[0], 'o', mfc='white', mec=PURPLE, ms=3.6)
    s2 = np.linspace(-2.2, 2.2, 300); X2, Y2 = np.meshgrid(s2, s2)
    a2.contour(X2, Y2, ((X2-1)**2+Y2**2)/2, levels=[0.5, 1.5, 3], colors=BLUE, linewidths=.5)
    a2.contour(X2, Y2, ((X2+1)**2+Y2**2)/2, levels=[0.5, 1.5, 3], colors=GREEN, linewidths=.5, linestyles='--')
    a2.plot([-1, 1], [0, 0], color=INK, lw=2.0)
    a2.set(xlim=(-2.2, 2.2), ylim=(-1.8, 1.8), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$', title='(b) 共同下降迭代，η=1/2')
    save(fig, D/'c7-common-descent', 'figure', {
        'objectives': 'f1=||x-a||^2/2, f2=||x-b||^2/2, a=(1,0), b=(-1,0)',
        'point_p': [0, 1], 'grad_f1': g1.tolist(), 'grad_f2': g2.tolist(),
        'min_norm_weight_on_f1': al, 'g_bar': gbar.tolist(),
        'common_descent_cone': 'd2 < -|d1|',
        'lens': 'both objectives below their values at p (radius sqrt(2) discs)',
        'arrows_scaled_by': sc, 'mgda_step': eta,
        'paths_end': [P[-1].round(4).tolist() for P in paths], 'path_lengths': [len(P)-1 for P in paths]})


def worst_case_envelope():
    fig, ax = figure(width_mm=96, height_mm=62)
    x = np.linspace(-2, 2, 401)
    for y in [-1, -0.5, 0, 0.5, 1]:
        ax.plot(x, (x-y)**2, color=MUTED, lw=.6)
    ax.plot(x, (np.abs(x)+1)**2, color=BLUE, lw=1.4, label=r'$\bar{\phi}(x)=(|x|+1)^2$')
    ax.plot(x, (np.abs(x)+0.5)**2, color=GREEN, lw=1.1, ls='--', label='只查 y=±1/2')
    ax.plot([0], [1], 'o', color=BLUE, ms=3.8); ax.plot([0], [0.25], 'o', color=GREEN, ms=3.6)
    ax.annotate('最坏值 1', (0, 1), xytext=(6, 4), textcoords='offset points', color=BLUE, fontsize=7.5, bbox=dict(fc='white', ec='none', pad=.6))
    ax.annotate('低估为 1/4', (0, 0.25), xytext=(-52, -2), textcoords='offset points', color=GREEN, fontsize=7.5, bbox=dict(fc='white', ec='none', pad=.6))
    ax.set(xlim=(-2, 2), ylim=(0, 5), xlabel=r'$x$', ylabel='损失')
    ax.legend(loc='upper center', fontsize=7)
    save(fig, D/'c7-worst-case-envelope', 'figure', {
        'phi': '(x-y)^2, x in [-2,2] shown, y in [-1,1]',
        'upper_envelope': '(|x|+1)^2, min 1 at x=0',
        'finite_inner_candidates': '{-1/2,1/2} gives (|x|+1/2)^2, min 1/4 at x=0',
        'max_min': 0})


def saddle_surfaces():
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(150/25.4, 64/25.4))
    from support import configure
    configure()
    s = np.linspace(-1, 1, 41); X, Y = np.meshgrid(s, s)
    specs = [('(a) 极小极大鞍点', X**2 - Y**2), ('(b) 仅为微分鞍点', Y**2 - X**2)]
    for i, (title, Z) in enumerate(specs):
        ax = fig.add_subplot(1, 2, i+1, projection='3d', computed_zorder=False)
        ax.plot_surface(X, Y, Z, color=BLUE_FILL, edgecolor=BLUE, linewidth=.25, rstride=4, cstride=4, shade=False, zorder=1)
        ax.plot(s, 0*s, s**2 if i == 0 else -s**2, color=GREEN, lw=1.6, zorder=5)
        ax.plot(0*s, s, -s**2 if i == 0 else s**2, color=RED, lw=1.6, zorder=5)
        ax.scatter([0], [0], [0], color=INK, s=10, zorder=6)
        ax.set_xlabel(r'$x$', labelpad=-4); ax.set_ylabel(r'$y$', labelpad=-4)
        ax.set_zlabel(r'$\phi$', labelpad=-6)
        ax.tick_params(labelsize=6.5, pad=-2)
        ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_zticks([-1, 0, 1])
        ax.view_init(elev=24, azim=-58)
        ax.set_title(title, fontsize=8, pad=0)
    fig.subplots_adjust(left=0.0, right=0.97, bottom=0.04, top=0.92, wspace=0.08)
    save(fig, D/'c7-saddle-surfaces', 'figure', {
        'panel_a': 'phi=x^2-y^2 on [-1,1]^2; x minimizes (green section x^2), y maximizes (red section -y^2); (0,0) is a minimax saddle',
        'panel_b': 'phi=y^2-x^2; (0,0) is a stationary point with indefinite Hessian but for fixed y=0, x=0 maximizes; not a minimax saddle'})


def gda_bilinear():
    eta = 0.5; T = 16; u0 = np.array([0.5, 0.0])
    def sim(u):
        x, y = u; return np.array([x - eta*y, y + eta*x])
    def alt(u):
        x, y = u; x2 = x - eta*y; return np.array([x2, y + eta*x2])
    def eg(u):
        x, y = u; xb, yb = x - eta*y, y + eta*x
        return np.array([x - eta*yb, y + eta*xb])
    runs = {}
    for name, f in [('sim', sim), ('alt', alt), ('eg', eg)]:
        u = u0.copy(); P = [u.copy()]
        for t in range(T):
            u = f(u); P.append(u.copy())
        runs[name] = np.array(P)
    fig, (a1, a2) = figure(width_mm=150, height_mm=64, ncols=2)
    a1.add_patch(__import__('matplotlib').patches.Rectangle((-1, -1), 2, 2, fill=False, ec=GRID, lw=.8))
    sty = {'sim': (BLUE, '同时下降—上升'), 'alt': (YELLOW, '交替下降—上升'), 'eg': (GREEN, '外梯度')}
    for k, (col, lab) in sty.items():
        P = runs[k]
        a1.plot(P[:, 0], P[:, 1], '-o', color=col, ms=1.8, lw=.9, label=lab)
    a1.plot([0], [0], '*', color=INK, ms=6)
    a1.plot(*u0, 'o', mfc='white', mec=INK, ms=3.6)
    a1.set(xlim=(-3.2, 3.2), ylim=(-3.2, 3.2), aspect='equal', xlabel=r'$x$', ylabel=r'$y$', title='(a) 迭代轨迹')
    a1.legend(loc='lower left', fontsize=7)
    t = np.arange(T+1)
    for k, (col, lab) in sty.items():
        P = runs[k]
        a2.semilogy(t, (P**2).sum(1), '-o', color=col, ms=1.8, lw=.9, label=lab)
    a2.set(xlabel=r'$t$', ylabel=r'$x^2+y^2$', title=r'(b) 到鞍点距离的平方')
    a2.grid(True, which='major')
    save(fig, D/'c7-gda-bilinear', 'figure', {
        'phi': 'x*y, unconstrained updates (box [-1,1]^2 drawn for reference)', 'eta': eta, 'T': T, 'u0': u0.tolist(),
        'factor_sim': 1+eta**2, 'factor_eg': 1-eta**2+eta**4, 'alt_matrix': '[[1,-eta],[eta,1-eta^2]], det 1',
        'final_sq_norm': {k: float((v[-1]**2).sum()) for k, v in runs.items()},
        'eg_inside_box': bool(np.all(np.abs(runs['eg']) <= 1))})


def inner_selection():
    fig, ax = figure(width_mm=88, height_mm=70)
    s = np.linspace(-0.5, 2.5, 10)
    ax.plot(s, 2-s, color=BLUE, lw=1.4)
    ax.text(1.72, 0.0, r'$x_1+x_2=2$', color=BLUE, fontsize=7.5, bbox=dict(fc='white', ec='none', pad=.6))
    th = np.concatenate([np.linspace(0, 10, 400), [1e3]])
    c = 2/(2+th)
    ax.plot(c, c, color=GREEN, lw=1.1)
    for tv in [0.5, 2, 6]:
        cc = 2/(2+tv); ax.plot(cc, cc, 'o', color=GREEN, ms=2.8)
        ax.annotate(rf'$\theta={tv:g}$', (cc, cc), xytext=(-30, 2), textcoords='offset points', fontsize=7, color=GREEN)
    ax.plot([1], [1], 'o', color=INK, ms=4)
    ax.annotate('最小范数解 (1,1)', (1, 1), xytext=(6, 4), textcoords='offset points', fontsize=7.5)
    ax.plot([1.5], [0.5], 's', color=RED, ms=3.8)
    ax.annotate(r'$\mathbf{c}$', (1.5, 0.5), xytext=(6, -3), textcoords='offset points', fontsize=7.5, color=RED)
    ax.plot([0], [0], 'o', mfc='white', mec=INK, ms=3.4)
    ax.annotate(r'$\mathbf{x}^{(0)}=\mathbf{0}$', (0, 0), xytext=(4, -9), textcoords='offset points', fontsize=7.5)
    ax.set(xlim=(-0.5, 2.6), ylim=(-0.5, 2.6), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$')
    save(fig, D/'c7-inner-selection', 'figure', {
        'inner': 'L_in(x,theta)=0.5*(x1+x2-2)^2 + theta/2*||x||^2, theta>=0',
        'solution_theta_pos': 'x=(2/(2+theta))*(1,1)', 'solution_set_theta0': 'x1+x2=2',
        'outer': 'L_out=0.5*||x-c||^2, c=(1.5,0.5)',
        'optimistic_at_0': 'x=c, value 0', 'gd_from_zero_at_0': 'x=(1,1), value 0.25',
        'limit_theta_to_0': '(1,1), value 0.25', 'pessimistic_at_0': '+inf (unbounded line)'})


def _unroll(theta, T, a=3.0, eta=0.5, x0=0.0):
    x = x0; Dv = 0.0; xs = [x]; As = []; Bs = []
    for t in range(T):
        A = 1 - eta*(1+theta); B = x
        Dv = A*Dv - eta*B
        As.append(A); Bs.append(B)
        x = A*x + eta*a
        xs.append(x)
    return x, Dv, xs, As, Bs


def unroll_vs_implicit():
    a, b, eta = 3.0, 1.0, 0.5
    fig, (a1, a2) = figure(width_mm=150, height_mm=62, ncols=2)
    th = np.linspace(0, 2.8, 501)
    cols = {1: MUTED, 2: YELLOW, 4: GREEN, 8: PURPLE}
    for T, col in cols.items():
        xT = [_unroll(t, T)[0] for t in th]
        a1.plot(th, xT, color=col, lw=1.0, label=rf'$x^{{({T})}}$')
    a1.plot(th, a/(1+th), color=BLUE, lw=1.5, label=r'$x^*$')
    a1.axhline(b, color=RED, lw=.8, ls='--')
    a1.text(0.05, b+0.06, '外层目标值 b=1', color=RED, fontsize=7.5)
    a1.plot([2], [1], 'o', color=BLUE, ms=3.6); a1.plot([5/3], [1], 'o', color=YELLOW, ms=3.4)
    a1.set(xlim=(0, 2.8), ylim=(0, 3.2), xlabel=r'$\theta$', ylabel='内层输出', title='(a) 内层输出随外层参数变化')
    a1.legend(loc='upper right', fontsize=7, ncol=2)
    Ts = np.arange(1, 21)
    full = [(_unroll(0.0, T)[0]-b)*_unroll(0.0, T)[1] for T in Ts]
    # truncated backprop at T=20 keeping last ell steps
    T = 20
    xT, DT, xs, As, Bs = _unroll(0.0, T)
    q = xT - b
    trunc = []
    for ell in Ts:
        g = 0.0; qq = q
        for t in range(T-1, T-1-ell, -1):
            g += qq*(-eta*Bs[t]); qq = qq*As[t]
        trunc.append(g)
    a2.plot(Ts, full, '-o', color=PURPLE, ms=2.2, lw=.9, label='完整展开（横轴为 T）')
    a2.plot(Ts, trunc, '-s', color=GREEN, ms=2.0, lw=.9, label='T=20 截断反传（横轴为 ℓ）')
    a2.axhline(-6, color=BLUE, lw=1.1, ls='--', label='隐式微分：−6')
    a2.set(xlim=(0, 21), ylim=(-6.6, 0.4), xlabel=r'步数', ylabel='θ=0 处的超梯度', title='(b) 超梯度')
    a2.legend(loc='upper right', fontsize=7)
    save(fig, D/'c7-unroll-vs-implicit', 'figure', {
        'inner': 'L_in=0.5*(x-a)^2+theta/2*x^2, a=3', 'outer': 'L_out=0.5*(x-b)^2, b=1',
        'gd': 'x^{(0)}=0, eta=0.5, stable for theta<3', 'exact': 'x*=a/(1+theta), argmin J at theta=2, J(0)=2',
        'J2': 'x2=9/4-3theta/4, J2=0.5*(5/4-3theta/4)^2, argmin theta=5/3', 'J1': 'x1=3/2, constant 1/8',
        'theta_range': [0, 2.8],
        'full_unroll_hypergrad_theta0': [round(v, 6) for v in full],
        'truncated_T20_by_ell': [round(v, 6) for v in trunc], 'implicit': -6.0})


def _cubic_branch(theta, start):
    x = start
    for _ in range(80):
        x -= (x**3 - x + theta)/(3*x**2 - 1)
    return x


def branch_switch():
    thf = 2/(3*np.sqrt(3))
    fig, (a1, a2) = figure(width_mm=150, height_mm=62, ncols=2)
    thR = np.linspace(-0.6, thf-1e-4, 500); xR = np.array([_cubic_branch(t, 1.3) for t in thR])
    thL = np.linspace(-thf+1e-4, 0.6, 500); xL = np.array([_cubic_branch(t, -1.3) for t in thL])
    a1.plot(thR[thR <= 0], xR[thR <= 0], color=BLUE, lw=1.6)
    a1.plot(thR[thR >= 0], xR[thR >= 0], color=BLUE, lw=1.0, ls='--')
    a1.plot(thL[thL >= 0], xL[thL >= 0], color=GREEN, lw=1.6)
    a1.plot(thL[thL <= 0], xL[thL <= 0], color=GREEN, lw=1.0, ls='--')
    a1.plot([thf, -thf], [1/np.sqrt(3), -1/np.sqrt(3)], 'o', mfc='white', mec=RED, ms=3.6)
    a1.annotate('折点', (thf, 1/np.sqrt(3)), xytext=(-8, -12), textcoords='offset points', fontsize=7.5, color=RED)
    a1.axvline(0, color=GRID, lw=.6)
    a1.set(xlim=(-0.6, 0.6), ylim=(-1.6, 1.6), xlabel=r'$\theta$', ylabel=r'$x$', title='(a) 两条极小点分支')
    a1.text(-0.55, 1.35, '实线：全局极小', fontsize=7, color=INK); a1.text(-0.55, 1.12, '虚线：仅局部极小', fontsize=7, color=MUTED)
    JR = 0.5*(xR-1)**2; JL = 0.5*(xL-1)**2
    a2.plot(thR, JR, color=BLUE, lw=1.0, ls='--', label='沿右分支')
    m1 = thR < 0; m2 = thL > 0
    a2.plot(thR[m1], JR[m1], color=INK, lw=1.6, label='沿全局选解')
    a2.plot(thL[m2], JL[m2], color=INK, lw=1.6)
    a2.plot([0], [0], 'o', color=INK, ms=3.6); a2.plot([0], [2], 'o', mfc='white', mec=INK, ms=3.6)
    a2.annotate('乐观：J(0)=0', (0, 0), xytext=(5, 6), textcoords='offset points', fontsize=7.5)
    a2.annotate('悲观：J(0)=2', (0, 2), xytext=(-62, 5), textcoords='offset points', fontsize=7.5)
    a2.set(xlim=(-0.6, 0.6), ylim=(-0.1, 2.6), xlabel=r'$\theta$', ylabel=r'$J$', title='(b) 外层目标')
    a2.legend(loc='center left', fontsize=7)
    save(fig, D/'c7-branch-switch', 'figure', {
        'inner': 'L_in(x,theta)=x^4/4-x^2/2+theta*x, stationarity x^3-x+theta=0',
        'fold': {'theta': round(float(thf), 6), 'x': round(1/np.sqrt(3), 6)},
        'global_selection': 'right branch for theta<0, left branch for theta>0, tie {-1,1} at theta=0',
        'outer': '0.5*(x-1)^2', 'implicit_derivative': 'dx/dtheta=-1/(3x^2-1)',
        'right_branch_at_0': 1.0, 'left_branch_at_0': -1.0})


ALL = {'pareto-candidates': pareto_candidates, 'pareto-set-front': pareto_set_front,
       'weighted-sum': weighted_sum, 'threshold': threshold, 'common-descent': common_descent,
       'worst-case-envelope': worst_case_envelope, 'saddle-surfaces': saddle_surfaces,
       'gda-bilinear': gda_bilinear, 'inner-selection': inner_selection,
       'unroll-vs-implicit': unroll_vs_implicit, 'branch-switch': branch_switch}

if __name__ == '__main__':
    names = sys.argv[1:] or list(ALL)
    for n in names:
        ALL[n.removeprefix('c7-')]()
        print('done', n)
