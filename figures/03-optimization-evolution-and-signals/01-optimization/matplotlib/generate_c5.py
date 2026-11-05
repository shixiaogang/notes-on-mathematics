# coding: utf-8
"""Teaching figures for volume three, part "optimization", chapter 5
(constrained optimization and duality).

Every curve comes from a closed-form expression or from a deterministic
iteration whose rule, start point and parameters are written to the facts
file of the figure.  No randomness is used except where a seed is recorded.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/01-optimization/matplotlib/generate_c5.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import brentq

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, \
    BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL

D = Path(__file__).resolve().parent
ARROW = dict(arrowstyle='-|>', lw=1.0, mutation_scale=8, shrinkA=0, shrinkB=0)


def arrow(ax, p, q, color, lw=1.0):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(ARROW, color=color, lw=lw))


def r(v, k=4):
    return [round(float(t), k) for t in np.atleast_1d(v)]


# ---------------------------------------------------------------- 5.1
def c5_tangency():
    """min (x1^2+4 x2^2)/2 s.t. x1+x2=1: gradient parallel to the normal at the optimum."""
    fig, ax = figure(width_mm=100, height_mm=70)
    g = np.linspace(-0.4, 1.6, 400)
    X1, X2 = np.meshgrid(g, np.linspace(-0.6, 1.2, 400))
    F = 0.5*(X1**2 + 4*X2**2)
    levels = [0.1, 0.2, 0.4, 0.8, 1.2]
    ax.contour(X1, X2, F, levels=levels, colors=MUTED, linewidths=.6)
    t = np.linspace(-0.4, 1.6, 10)
    ax.plot(t, 1-t, color=BLUE, lw=1.4)
    ax.text(1.45, -0.42, r'$x_1+x_2=1$', color=BLUE, ha='right', va='top', fontsize=7.5)
    xs = np.array([0.8, 0.2])
    ax.contour(X1, X2, F, levels=[0.4], colors=GREEN, linewidths=1.1)
    ax.plot(*xs, 'o', color=INK, ms=3.5, zorder=5)
    grad = np.array([0.8, 0.8])
    arrow(ax, xs, xs + 0.5*grad, GREEN)
    ax.text(*(xs + 0.5*grad + np.array([0.03, 0.0])), r'$\nabla f(\mathbf{x}^*)$', color=GREEN, fontsize=7.5, va='center')
    ax.text(xs[0]-0.04, xs[1]-0.06, r'$\mathbf{x}^*$', ha='right', va='top', fontsize=8)
    # a non-optimal feasible point
    xa = np.array([0.2, 0.8])
    ga = np.array([0.2, 3.2])
    tang = np.array([1, -1])/np.sqrt(2)
    gt = (ga @ tang)*tang
    gn = ga - gt
    ax.plot(*xa, 'o', color=INK, ms=3.5, zorder=5)
    s = 0.12
    arrow(ax, xa, xa + s*ga, RED)
    arrow(ax, xa, xa + s*gn, MUTED, lw=.8)
    arrow(ax, xa, xa - s*gt, BLUE, lw=1.2)
    ax.text(*(xa + s*ga + np.array([0.03, 0])), r'$\nabla f(\mathbf{x})$', color=RED, fontsize=7.5, va='center')
    ax.text(*(xa - s*gt + np.array([0.04, 0.02])), '沿约束下降', color=BLUE, fontsize=7.5, va='bottom')
    ax.text(xa[0]-0.04, xa[1]-0.02, r'$\mathbf{x}$', ha='right', va='top', fontsize=8)
    ax.set(xlim=(-0.4, 1.6), ylim=(-0.6, 1.3), xlabel=r'$x_1$', ylabel=r'$x_2$', aspect='equal')
    save(fig, D/'c5-tangency', 'figure', {
        'objective': 'f(x)=(x1^2+4*x2^2)/2', 'constraint': 'x1+x2=1',
        'optimum': [0.8, 0.2], 'grad_at_optimum': [0.8, 0.8], 'nu_star': -0.8, 'f_star': 0.4,
        'other_point': [0.2, 0.8], 'grad_other': [0.2, 3.2],
        'tangential_component': r(gt), 'normal_component': r(gn), 'arrow_scale': s,
        'contour_levels': levels})


def c5_normal_cone():
    """Projection of c onto T={x>=0, x1+x2<=2}: interior, edge and corner cases."""
    fig, axes = figure(width_mm=169, height_mm=60, ncols=3)
    cases = [((0.6, 0.8), (0.6, 0.8), '(a) 内点', []),
             ((2.0, 1.0), (1.5, 0.5), '(b) 光滑边界', [(1, 1)]),
             ((3.0, -1.0), (2.0, 0.0), '(c) 角点', [(1, 1), (0, -1)])]
    facts = {'set': 'x>=0, x1+x2<=2', 'objective': '0.5*||x-c||^2', 'cases': []}
    for ax, (c, xs, title, normals) in zip(axes, cases):
        ax.fill([0, 2, 0], [0, 0, 2], color=BLUE_FILL, lw=0)
        ax.plot([0, 2, 0, 0], [0, 0, 2, 0], color=BLUE, lw=1.0)
        c = np.array(c); xs = np.array(xs)
        for rad in [0.3, 0.6, 0.9, 1.2, 1.5]:
            th = np.linspace(0, 2*np.pi, 200)
            ax.plot(c[0]+rad*np.cos(th), c[1]+rad*np.sin(th), color=GRID, lw=.6)
        if len(normals) == 2:
            n1, n2 = np.array(normals[0], float), np.array(normals[1], float)
            ax.fill([xs[0], xs[0]+1.3*n1[0], xs[0]+1.3*n1[0], xs[0]+1.3*n2[0]],
                    [xs[1], xs[1]+1.3*n1[1], xs[1]-1.3, xs[1]+1.3*n2[1]], color=GREEN_FILL, lw=0, zorder=1)
        for nrm in normals:
            nv = np.array(nrm, float)/np.linalg.norm(nrm)
            arrow(ax, xs, xs + 0.55*nv, GREEN, lw=.8)
        ax.plot(*c, 'x', color=RED, ms=4, mew=1.1, zorder=6)
        ax.text(c[0]+0.08, c[1]+0.05, r'$\mathbf{c}$', color=RED, fontsize=8)
        ax.plot(*xs, 'o', color=INK, ms=3.5, zorder=6)
        mg = c - xs
        if np.linalg.norm(mg) > 1e-9:
            arrow(ax, xs, xs + 0.9*mg/np.linalg.norm(mg)*min(1, np.linalg.norm(mg)), RED, lw=1.1)
        if np.linalg.norm(mg) > 1e-9:
            tip = xs + 0.9*mg/np.linalg.norm(mg)*min(1, np.linalg.norm(mg))
            mid = (xs + tip)/2
            off = np.array([0.12, -0.12]) if len(normals) == 1 else np.array([-0.62, -0.3])
            ax.text(*(mid + off), r'$-\nabla f$', color=RED, fontsize=7.5, va='center')
        if len(normals) == 2:
            ax.text(2.95, 0.75, '法锥', color=GREEN, fontsize=7.5, ha='center')
        ax.set_title(title)
        ax.set(xlim=(-0.4, 3.4), ylim=(-1.5, 2.3), aspect='equal', xlabel=r'$x_1$')
        ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([-1, 0, 1, 2])
        lam = {'(a) 内点': [0, 0], '(b) 光滑边界': [0.5, 0], '(c) 角点': [1, 2]}[title]
        facts['cases'].append({'c': r(c), 'x_star': r(xs), 'minus_grad': r(mg), 'multipliers_budget_and_x2': lam})
    axes[0].set_ylabel(r'$x_2$')
    axes[0].text(0.6, 0.62, r'$\mathbf{x}^*=\mathbf{c}$', fontsize=7.5, ha='center', va='top')
    save(fig, D/'c5-normal-cone', 'figure', facts)


def c5_cusp():
    """Kuhn--Tucker cusp: x2<=(1-x1)^3, x2>=0; linearized directions vs true feasible directions."""
    fig, ax = figure(width_mm=96, height_mm=56)
    t = np.linspace(-0.2, 1.0, 300)
    ax.fill_between(t, 0, (1-t)**3, color=BLUE_FILL, lw=0)
    ax.plot(t, (1-t)**3, color=BLUE, lw=1.1)
    ax.plot([-0.2, 1.0], [0, 0], color=BLUE, lw=1.1)
    ax.plot([0.55, 1.45], [0, 0], color=YELLOW, lw=2.4, alpha=1, zorder=1, solid_capstyle='butt')
    ax.plot(1, 0, 'o', color=INK, ms=3.5, zorder=5)
    arrow(ax, (1, 0), (0.62, 0), BLUE, lw=1.2)
    arrow(ax, (1, 0), (1.38, 0), YELLOW, lw=1.2)
    arrow(ax, (1, 0.0), (1.0, 0.32), GREEN, lw=.9)
    arrow(ax, (1, 0.0), (1.0, -0.32), GREEN, lw=.9)
    ax.text(1.03, 0.3, r'$\nabla g_1$', color=GREEN, fontsize=7.5, va='center')
    ax.text(1.03, -0.3, r'$\nabla g_2$', color=GREEN, fontsize=7.5, va='center')
    ax.text(0.3, 0.12, '可行域', color=BLUE, fontsize=7.5)
    ax.text(1.42, 0.05, '线性化允许', color=YELLOW, fontsize=7.5, ha='right', va='bottom')
    ax.text(0.62, -0.06, '真实可行', color=BLUE, fontsize=7.5, ha='left', va='top')
    ax.set(xlim=(-0.2, 1.5), ylim=(-0.4, 0.8), xlabel=r'$x_1$', ylabel=r'$x_2$', aspect='equal')
    save(fig, D/'c5-cusp', 'figure', {
        'constraints': ['g1=x2-(1-x1)^3<=0', 'g2=-x2<=0'], 'point': [1, 0],
        'grad_g1': [0, 1], 'grad_g2': [0, -1], 'linearized_directions': 'd2=0, d1 any sign',
        'true_feasible_directions': 'd=(-t,0), t>=0', 'objective_example': 'f=-x1, no KKT multipliers at (1,0)'})


# ---------------------------------------------------------------- 5.2
def c5_dual_envelope():
    """min x^2 s.t. 1-x<=0: image set G and dual function as supporting-line intercept."""
    fig, axes = figure(width_mm=169, height_mm=62, ncols=2)
    ax = axes[0]
    x = np.linspace(-1.2, 2.6, 400)
    u, tt = 1-x, x**2
    # region A = G + R_+^2 (upper-right closure), drawn lightly
    uu = np.linspace(-2.0, 2.3, 400)
    p = np.where(uu < 1, (1-uu)**2, 0.0)
    ax.fill_between(uu, p, 5, color=BLUE_FILL, lw=0)
    ax.plot(u, tt, color=BLUE, lw=1.2)
    ax.axvline(0, color=MUTED, lw=.6, ls=':')
    facts = {'problem': 'min x^2 s.t. 1-x<=0', 'p_star': 1, 'lines': {}}
    for lam, col in [(1.0, YELLOW), (2.0, GREEN), (3.0, RED)]:
        q = lam - lam**2/4
        ax.plot(uu, q - lam*uu, color=col, lw=.9, ls='--')
        ax.plot(0, q, 'o', color=col, ms=3)
        facts['lines'][str(lam)] = {'q': q, 'line': f't = {q} - {lam} u', 'touch_x': lam/2}
    ax.annotate(r'$q(2)=1$', xy=(0, 1), xytext=(-1.0, 0.25), color=GREEN, fontsize=7.5, ha='right',
                arrowprops=dict(arrowstyle='-', color=GREEN, lw=.5))
    ax.annotate(r'$q(1)=q(3)=0.75$', xy=(0, 0.75), xytext=(0.25, -0.3), color=INK, fontsize=7.5,
                arrowprops=dict(arrowstyle='-', color=MUTED, lw=.5))
    ax.text(-1.95, 2.05, r'$\lambda=1$', color=YELLOW, fontsize=7)
    ax.text(-1.25, 4.2, r'$\lambda=2$', color=GREEN, fontsize=7)
    ax.text(-0.6, 4.2, r'$\lambda=3$', color=RED, fontsize=7)
    ax.text(1.55, 1.2, r'$G=\{(g(x),f(x))\}$', color=BLUE, fontsize=7.5)
    ax.set(xlim=(-2.0, 2.3), ylim=(-0.5, 4.5), xlabel=r'$u=g(x)=1-x$', ylabel=r'$t=f(x)=x^2$')
    ax.set_title('(a) 支撑直线与截距')
    ax2 = axes[1]
    lam = np.linspace(0, 4.5, 300)
    ax2.plot(lam, lam - lam**2/4, color=GREEN, lw=1.2, label=r'$q(\lambda)=\lambda-\lambda^2/4$')
    ax2.axhline(1, color=BLUE, lw=.9, ls='--', label=r'$p^*=1$')
    ax2.plot(2, 1, 'o', color=INK, ms=3.5)
    for lam0, col in [(1.0, YELLOW), (3.0, RED)]:
        ax2.plot(lam0, lam0 - lam0**2/4, 'o', color=col, ms=3)
    ax2.set(xlim=(0, 4.5), ylim=(-0.6, 1.4), xlabel=r'$\lambda$', ylabel='下界值')
    ax2.legend(loc='lower center')
    ax2.set_title('(b) 对偶函数')
    save(fig, D/'c5-dual-envelope', 'figure', facts)


def c5_conjugate():
    """Conjugate as the best intercept: x^2/2 and |x|."""
    fig, axes = figure(width_mm=169, height_mm=58, ncols=2)
    ax = axes[0]
    x = np.linspace(-1.5, 3.0, 300)
    ax.plot(x, x**2/2, color=BLUE, lw=1.2, label=r'$f(x)=x^2/2$')
    y = 1.5
    ax.plot(x, y*x, color=MUTED, lw=.8, ls=':', label=r'$yx$')
    ax.plot(x, y*x - y**2/2, color=GREEN, lw=1.0, ls='--', label=r'$yx-f^*(y)$')
    ax.plot([y, y], [y*y - y**2/2, y*y], color=RED, lw=1.1)
    ax.text(y+0.08, y*y - y**2/4, r'$f^*(y)=1.125$', color=RED, fontsize=7.5, va='center')
    ax.plot(y, y**2/2, 'o', color=INK, ms=3)
    ax.plot(0, -y**2/2, 'o', color=GREEN, ms=3)
    ax.text(0.1, -y**2/2 - 0.1, r'$-f^*(y)$', color=GREEN, fontsize=7.5, va='top')
    ax.axhline(0, color=GRID, lw=.5); ax.axvline(0, color=GRID, lw=.5)
    ax.set(xlim=(-1.5, 3.0), ylim=(-1.6, 4.0), xlabel=r'$x$')
    ax.legend(loc='upper left')
    ax.set_title(r'(a) $y=1.5$')
    ax2 = axes[1]
    x = np.linspace(-2, 2, 300)
    ax2.plot(x, np.abs(x), color=BLUE, lw=1.2, label=r'$f(x)=|x|$')
    for yy, col in [(-0.6, GREEN), (0.4, GREEN), (1.0, GREEN)]:
        ax2.plot(x, yy*x, color=col, lw=.8, ls='--')
    ax2.plot(x, 1.5*x - 0.0, color=RED, lw=.8, ls=':')
    ax2.text(1.15, 1.5*1.15, r'$y=1.5$', color=RED, fontsize=7.5, ha='right', va='bottom')
    ax2.text(1.9, 0.62, r'$|y|\leq1$', color=GREEN, fontsize=7.5, ha='right')
    ax2.axhline(0, color=GRID, lw=.5)
    ax2.set(xlim=(-2, 2), ylim=(-1.4, 2.6), xlabel=r'$x$')
    ax2.legend(loc='upper left')
    ax2.set_title(r'(b) $f^*=\iota_{[-1,1]}$')
    save(fig, D/'c5-conjugate', 'figure', {
        'panel_a': {'f': 'x^2/2', 'slope_y': y, 'f_star': y**2/2, 'touch_point': y},
        'panel_b': {'f': '|x|', 'slopes_drawn': [-0.6, 0.4, 1.0, 1.5],
                    'conjugate': 'indicator of [-1,1]', 'slope_1.5_line_exceeds_f_for_x>0': True}})


def c5_slater():
    """Value function p(u) with and without a finite supporting slope at u=0."""
    fig, axes = figure(width_mm=169, height_mm=58, ncols=2)
    ax = axes[0]
    u = np.linspace(-1.5, 2.0, 400)
    p = np.where(u < 1, (1-u)**2, 0)
    ax.fill_between(u, p, 7, color=BLUE_FILL, lw=0)
    ax.plot(u, p, color=BLUE, lw=1.2, label=r'$p(u)$')
    ax.plot(u, 1 - 2*u, color=GREEN, lw=.9, ls='--', label=r'$t=1-2u$')
    ax.plot(0, 1, 'o', color=INK, ms=3.5)
    ax.axvline(0, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(-1.5, 2.0), ylim=(-0.5, 5.5), xlabel=r'$u$')
    ax.legend(loc='upper right')
    ax.set_title(r'(a) $\min\ x^2,\ 1-x\leq u$')
    ax2 = axes[1]
    uu = np.linspace(0, 2.0, 400)
    ax2.fill_between(uu, -np.sqrt(uu), 1.0, color=BLUE_FILL, lw=0)
    ax2.plot(uu, -np.sqrt(uu), color=BLUE, lw=1.2, label=r'$p(u)=-\sqrt{u}$')
    ax2.axvline(0, color=BLUE, lw=1.2)
    facts = {'panel_a': {'problem': 'min x^2 s.t. 1-x<=u', 'p': '(1-u)^2 for u<1, 0 for u>=1',
                         'lambda_star': 2, 'support_line': 't=1-2u'},
             'panel_b': {'problem': 'min x s.t. x^2<=u', 'p': '-sqrt(u) for u>=0, +inf for u<0',
                         'q(lambda)': '-1/(4 lambda)', 'lines': []}}
    us = np.linspace(-0.5, 2.0, 50)
    for lam, col in [(0.5, YELLOW), (1.5, GREEN), (5.0, RED)]:
        q = -1/(4*lam)
        ax2.plot(us, q - lam*us, color=col, lw=.8, ls='--')
        ax2.plot(0, q, 'o', color=col, ms=3)
        facts['panel_b']['lines'].append({'lambda': lam, 'q': q})
    ax2.text(0.05, -0.62, r'$q(\lambda)=-1/(4\lambda)\uparrow0$', fontsize=7.5, color=INK)
    ax2.set(xlim=(-0.5, 2.0), ylim=(-1.6, 0.6), xlabel=r'$u$')
    ax2.legend(loc='upper right')
    ax2.set_title(r'(b) $\min\ x,\ x^2\leq u$')
    save(fig, D/'c5-slater', 'figure', facts)


# ---------------------------------------------------------------- 5.3
def c5_sensitivity():
    fig, axes = figure(width_mm=169, height_mm=58, ncols=2)
    ax = axes[0]
    tau = np.linspace(0.02, 4, 500)
    V = np.where(tau >= 3, 0, np.where(tau >= 1, (3-tau)**2/4, ((2-tau)**2+1)/2))
    lam = np.where(tau >= 3, 0, np.where(tau >= 1, (3-tau)/2, 2-tau))
    ax.plot(tau, V, color=BLUE, lw=1.2, label=r'$V(\tau)$')
    ax.plot(tau, lam, color=GREEN, lw=1.0, ls='--', label=r'$\lambda^*(\tau)$')
    t0 = 2.0
    ax.plot(tau, 0.25 - 0.5*(tau - t0), color=RED, lw=.8, ls=':', label='支撑直线')
    ax.plot(t0, 0.25, 'o', color=INK, ms=3.5)
    for v in [1, 3]:
        ax.axvline(v, color=GRID, lw=.6)
    ax.set(xlim=(0, 4), ylim=(-0.1, 2.2), xlabel=r'$\tau$')
    ax.legend(loc='upper right')
    ax.set_title('(a) 预算例')
    ax2 = axes[1]
    bb = np.linspace(-0.5, 2.5, 300)
    ax2.plot(bb, np.maximum(-bb, -1), color=BLUE, lw=1.2, label=r'$V(b)=\max\{-b,-1\}$')
    for s, col in [(-1, GREEN), (-0.5, YELLOW), (0, RED)]:
        ax2.plot(bb, -1 + s*(bb-1), color=col, lw=.8, ls='--')
    ax2.text(2.45, -1.55, r'$-\lambda_1\in[-1,0]$', fontsize=7.5, ha='right')
    ax2.plot(1, -1, 'o', color=INK, ms=3.5)
    ax2.set(xlim=(-0.5, 2.5), ylim=(-2.0, 0.7), xlabel=r'$b$')
    ax2.legend(loc='upper right')
    ax2.set_title('(b) 折点处的多重乘子')
    save(fig, D/'c5-sensitivity', 'figure', {
        'panel_a': {'problem': 'min 0.5||x-(2,1)||^2 s.t. x1+x2<=tau, x>=0',
                    'V': '0 (tau>=3); (3-tau)^2/4 (1<=tau<=3); ((2-tau)^2+1)/2 (0<tau<=1)',
                    'lambda': '0; (3-tau)/2; 2-tau', 'tau0': 2, 'V(2)': 0.25, 'slope': -0.5},
        'panel_b': {'problem': 'min -x s.t. x<=b, x<=1', 'V': 'max(-b,-1)',
                    'multipliers_at_b=1': 'lambda1 in [0,1], lambda2=1-lambda1', 'slopes_drawn': [-1, -0.5, 0]}})


# ---------------------------------------------------------------- 5.4
def c5_psd_disk():
    """Trace-one 2x2 symmetric matrices [[a,b],[b,1-a]]: PSD disk vs entrywise nonnegative strip."""
    fig, ax = figure(width_mm=100, height_mm=66)
    ax.fill_between([0, 1], 0, 0.9, color=YELLOW_FILL, lw=0)
    ax.plot([0, 0, 1, 1], [0.9, 0, 0, 0.9], color=YELLOW, lw=.9)
    th = np.linspace(0, 2*np.pi, 300)
    ax.fill(0.5+0.5*np.cos(th), 0.5*np.sin(th), color=BLUE_FILL, alpha=.85, lw=0)
    ax.plot(0.5+0.5*np.cos(th), 0.5*np.sin(th), color=BLUE, lw=1.2)
    for lev in [-0.5, -0.25, 0, 0.25, 0.5]:
        ax.axhline(lev, color=GREEN, lw=.6, ls='--')
    ax.plot(0.5, -0.5, 'o', color=INK, ms=3.5, zorder=5)
    ax.text(0.55, -0.56, r'$\mathbf{X}^*=\mathbf{v}\mathbf{v}^{\mathrm{T}}$', fontsize=7.5, va='top')
    ax.plot(0.5, 0.8, 's', color=RED, ms=3.5)
    ax.text(0.56, 0.8, '非负但不半正定', color=RED, fontsize=7.5, va='center')
    ax.plot(0.5, -0.3, '^', color=PURPLE, ms=3.8)
    ax.text(0.56, -0.3, '半正定但有负元', color=PURPLE, fontsize=7.5, va='center')
    ax.text(-0.12, 0.3, r'$\mathbf{X}\succeq\mathbf{0}$', color=BLUE, fontsize=8, ha='right')
    ax.text(1.03, 0.65, '逐元素非负', color=YELLOW, fontsize=7.5)
    ax.text(1.04, -0.18, '目标等值线', color=GREEN, fontsize=7.5, va='center')
    ax.set(xlim=(-0.45, 1.5), ylim=(-0.75, 0.95), xlabel=r'$X_{1,1}=a$', ylabel=r'$X_{1,2}=b$', aspect='equal')
    save(fig, D/'c5-psd-disk', 'figure', {
        'matrices': '[[a,b],[b,1-a]]', 'psd_condition': '(a-1/2)^2+b^2<=1/4',
        'entrywise_nonnegative': '0<=a<=1, b>=0', 'C': [[2, 1], [1, 2]],
        'objective': '<C,X> = 2+2b', 'optimum': {'a': 0.5, 'b': -0.5, 'value': 1, 'v': [0.7071, -0.7071]},
        'nonneg_not_psd_point': [0.5, 0.8], 'psd_with_negative_entry': [0.5, -0.3]})


def c5_soc():
    """Second-order cone in R^3: t >= sqrt(u1^2+u2^2)."""
    import matplotlib.pyplot as plt
    from support import configure
    configure()
    fig = plt.figure(figsize=(84/25.4, 66/25.4))
    ax = fig.add_subplot(projection='3d')
    th = np.linspace(0, 2*np.pi, 60)
    rr = np.linspace(0, 1.0, 12)
    R, TH = np.meshgrid(rr, th)
    ax.plot_surface(R*np.cos(TH), R*np.sin(TH), R, color=BLUE_FILL, edgecolor=BLUE, linewidth=.25, alpha=.75, rstride=5, cstride=2, shade=False)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 1))
        axis._axinfo['grid']['color'] = GRID
        axis._axinfo['grid']['linewidth'] = .4
    ax.plot(np.cos(th), np.sin(th), np.ones_like(th), color=BLUE, lw=1.0)
    ax.plot(0.6*np.cos(th), 0.6*np.sin(th), 0.6*np.ones_like(th), color=GREEN, lw=.9)
    ax.plot([0, 0], [0, 0], [0, 1.25], color=INK, lw=.75)
    ax.scatter([0.3], [0.2], [0.8], color=INK, s=6)
    ax.set_xlabel(r'$u_1$', labelpad=-8); ax.set_ylabel(r'$u_2$', labelpad=-8); ax.set_zlabel(r'$t$', labelpad=-8)
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_zticks([0, 0.5, 1])
    ax.tick_params(labelsize=6.5, pad=-3)
    ax.view_init(elev=18, azim=-58)
    ax.set_box_aspect((1, 1, 0.9))
    fig.subplots_adjust(left=0, right=1, bottom=0.02, top=1)
    save(fig, D/'c5-soc', 'figure', {
        'cone': 'K={(u,t): ||u||_2<=t}, u in R^2', 'height_range': [0, 1], 'slice_t': 0.6,
        'sample_point': [0.3, 0.2, 0.8], 'sample_norm': round(float(np.hypot(0.3, 0.2)), 4)})


# ---------------------------------------------------------------- 5.5
TRI = np.array([[0, 0], [2, 0], [0, 2]], float)


def _f_pg(x):
    return 0.5*((x[0]-2.5)**2 + 4*(x[1]-1)**2)


def _g_pg(x):
    return np.array([x[0]-2.5, 4*(x[1]-1)])


def _proj_tri(z):
    """Projection onto {x>=0, x1+x2<=2} by checking the KKT pieces."""
    if z[0] >= 0 and z[1] >= 0 and z.sum() <= 2:
        return z.copy()
    cands = []
    # edge x1+x2=2
    t = np.clip((z[0]-z[1]+2)/2, 0, 2); cands.append(np.array([t, 2-t]))
    cands.append(np.array([np.clip(z[0], 0, 2), 0.0]))
    cands.append(np.array([0.0, np.clip(z[1], 0, 2)]))
    return min(cands, key=lambda p: np.sum((p-z)**2))


def c5_pg_fw():
    fig, axes = figure(width_mm=169, height_mm=64, ncols=2, gridspec_kw={'width_ratios': [1.0, 1.05]})
    ax = axes[0]
    g1 = np.linspace(-0.2, 2.4, 300); g2 = np.linspace(-0.2, 2.2, 300)
    X1, X2 = np.meshgrid(g1, g2)
    F = 0.5*((X1-2.5)**2 + 4*(X2-1)**2)
    ax.fill(TRI[:, 0], TRI[:, 1], color=BLUE_FILL, lw=0)
    ax.plot([0, 2, 0, 0], [0, 0, 2, 0], color=BLUE, lw=1.0)
    ax.contour(X1, X2, F, levels=[0.1, 0.4, 1.0, 2.0, 3.5], colors=GRID, linewidths=.6)
    xs = np.array([1.3, 0.7]); fstar = _f_pg(xs)
    x = np.zeros(2); pg = [x.copy()]
    for t in range(30):
        x = _proj_tri(x - 0.25*_g_pg(x)); pg.append(x.copy())
    pg = np.array(pg)
    x = np.zeros(2); fw = [x.copy()]; gaps = []
    for t in range(200):
        g = _g_pg(x)
        s = TRI[np.argmin(TRI @ g)]
        gaps.append(float(g @ (x - s)))
        gam = 2/(t+2)
        x = x + gam*(s - x); fw.append(x.copy())
    fw = np.array(fw)
    ax.plot(pg[:8, 0], pg[:8, 1], '-o', color=GREEN, ms=2.4, lw=.9, label='投影梯度')
    ax.plot(fw[:16, 0], fw[:16, 1], '-s', color=RED, ms=2.2, lw=.7, label='条件梯度')
    ax.plot(*xs, '*', color=INK, ms=6, zorder=6)
    ax.plot(2.5, 1, 'x', color=MUTED, ms=4)
    ax.text(2.5, 1.12, '无约束最小点', fontsize=7.5, color=MUTED, ha='center')
    ax.set(xlim=(-0.2, 2.9), ylim=(-0.2, 2.2), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$')
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))
    ax.set_title('(a) 迭代路径')
    ax2 = axes[1]
    T = np.arange(1, 101)
    pgerr = np.array([_f_pg(p)-fstar for p in pg[:25]])
    k = pgerr > 1e-13
    ax2.semilogy(np.arange(25)[k], pgerr[k], '-o', color=GREEN, ms=2, lw=.9, label='投影梯度：目标差')
    fwerr = np.array([_f_pg(p)-fstar for p in fw[1:101]])
    ax2.semilogy(T, fwerr, color=RED, lw=.7, label='条件梯度：目标差')
    ax2.semilogy(T, np.minimum.accumulate(gaps[1:101]), color=RED, lw=.8, ls=':', label='条件梯度间隙（至今最小）')
    ax2.semilogy(T, 2*4*8/(T+2), color=MUTED, lw=.8, ls='--', label='理论上界')
    ax2.set(xlim=(0, 100), ylim=(1e-12, 1e2), xlabel=r'$t$')
    ax2.legend(loc='lower right', fontsize=7)
    ax2.set_title('(b) 精度随迭代')
    save(fig, D/'c5-pg-fw', 'figure', {
        'objective': '0.5*((x1-2.5)^2+4*(x2-1)^2)', 'set': 'triangle x>=0, x1+x2<=2',
        'L': 4, 'diameter_D': float(np.sqrt(8)), 'x_star': [1.3, 0.7], 'f_star': fstar, 'lambda_budget': 1.2,
        'start': [0, 0], 'pg_step': 0.25, 'pg_first_iterates': [r(p) for p in pg[:6]],
        'fw_step': '2/(t+2)', 'fw_first_iterates': [r(p) for p in fw[:6]],
        'fw_first_gaps': r(gaps[:5]), 'fw_error_at_100': float(fwerr[-1]), 'fw_best_error_by_100': float(fwerr.min()), 'fw_best_gap_by_100': float(np.min(gaps[1:101])),
        'pg_error_at_20': float(_f_pg(pg[20])-fstar)})


def _proj_simplex(z):
    u = np.sort(z)[::-1]
    css = np.cumsum(u)
    k = np.max(np.nonzero(u - (css-1)/np.arange(1, len(z)+1) > 0)[0]) + 1
    tau = (css[k-1]-1)/k
    return np.maximum(z - tau, 0)


V3 = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])


def tern(x):
    x = np.atleast_2d(x)
    return x @ V3


def c5_mirror_simplex():
    c = np.array([0.8, 0.6, -0.1])
    fig, axes = figure(width_mm=169, height_mm=62, ncols=2, gridspec_kw={'width_ratios': [1.0, 1.1]})
    ax = axes[0]
    ax.fill(V3[:, 0], V3[:, 1], color=BLUE_FILL, lw=0)
    ax.plot(*np.vstack([V3, V3[:1]]).T, color=BLUE, lw=1.0)
    # contours of f on the simplex
    n = 200
    a, b = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n))
    m = a + b <= 1
    P = np.stack([a[m], b[m], 1-a[m]-b[m]], 1)
    Fv = 0.5*np.sum((P-c)**2, 1)
    XY = tern(P)
    ax.tricontour(XY[:, 0], XY[:, 1], Fv, levels=[0.03, 0.06, 0.12, 0.2, 0.3, 0.45], colors=GRID, linewidths=.6)
    x0 = np.array([0.15, 0.15, 0.7])
    x = x0.copy(); pg = [x.copy()]
    for t in range(12):
        x = _proj_simplex(x - 0.5*(x - c)); pg.append(x.copy())
    x = x0.copy(); md = [x.copy()]
    for t in range(40):
        w = x*np.exp(-1.0*(x - c)); x = w/w.sum(); md.append(x.copy())
    pg, md = np.array(pg), np.array(md)
    ax.plot(*tern(pg[:8]).T, '-o', color=GREEN, ms=2.4, lw=.9, label='投影梯度')
    ax.plot(*tern(md[:14]).T, '-s', color=RED, ms=2.2, lw=.8, label='熵镜像下降')
    xs = np.array([0.6, 0.4, 0])
    ax.plot(*tern(xs).T, '*', color=INK, ms=6, zorder=6)
    for lab, v, off in [(r'$\mathbf{e}_1$', V3[0], (-0.05, -0.05)), (r'$\mathbf{e}_2$', V3[1], (0.05, -0.05)), (r'$\mathbf{e}_3$', V3[2], (0, 0.05))]:
        ax.text(v[0]+off[0], v[1]+off[1], lab, ha='center', va='center', fontsize=8)
    ax.text(0.5, -0.07, r'$x_3=0$', ha='center', va='top', fontsize=7.5, color=BLUE)
    ax.set(xlim=(-0.1, 1.1), ylim=(-0.15, 0.95), aspect='equal')
    ax.axis('off')
    ax.legend(loc='upper right', bbox_to_anchor=(1.08, 1.0))
    ax.set_title('(a) 单纯形上的路径')
    ax2 = axes[1]
    ax2.semilogy(np.arange(len(md)), md[:, 2], color=RED, lw=1.0, label='熵镜像下降')
    pg3 = pg[:, 2]
    ax2.semilogy(np.arange(len(pg3))[pg3 > 0], pg3[pg3 > 0], '-o', color=GREEN, ms=2.4, lw=.9, label='投影梯度')
    zero_at = int(np.argmax(pg3 <= 0))
    ax2.annotate('第3步起恰为0', xy=(zero_at-1, pg3[zero_at-1]), xytext=(zero_at+4, 3e-2), fontsize=7.5, color=GREEN,
                 arrowprops=dict(arrowstyle='-', color=GREEN, lw=.6))
    ax2.set(xlim=(0, 40), ylim=(1e-8, 1), xlabel=r'$t$')
    ax2.legend(loc='upper right')
    ax2.set_title('(b) 第三个坐标')
    ax2.set_ylabel(r'$x_3^{(t)}$')
    save(fig, D/'c5-mirror-simplex', 'figure', {
        'objective': '0.5*||x-c||^2', 'c': r(c), 'x_star': [0.6, 0.4, 0.0], 'start': [0.15, 0.15, 0.7],
        'pg_step': 0.5, 'md_step': 1.0, 'md_update': 'x_i <- x_i exp(-eta g_i)/Z',
        'pg_iterates': [r(p) for p in pg[:6]], 'md_iterates': [r(p) for p in md[:6]],
        'pg_x3_zero_from_iteration': zero_at, 'md_x3_at_40': float(md[40, 2])})


# ---------------------------------------------------------------- 5.6
def c5_penalty_path():
    fig, axes = figure(width_mm=169, height_mm=64, ncols=2)
    ax = axes[0]
    g1 = np.linspace(-0.3, 1.4, 400); g2 = np.linspace(-0.6, 1.1, 400)
    X1, X2 = np.meshgrid(g1, g2)
    rho = 20.0
    Q = 0.5*(X1**2 + 4*X2**2) + rho/2*(X1+X2-1)**2
    xr = lambda p: np.array([4*p, p])/(4+5*p)
    qmin = 0.5*(xr(rho)[0]**2 + 4*xr(rho)[1]**2) + rho/2*(xr(rho).sum()-1)**2
    ax.contour(X1, X2, Q, levels=qmin + np.array([0.02, 0.08, 0.2, 0.5, 1.0]), colors=GREEN, linewidths=.6)
    t = np.linspace(-0.3, 1.4, 10)
    ax.plot(t, 1-t, color=BLUE, lw=1.1)
    rhos = np.concatenate([[0], np.geomspace(0.05, 1e4, 300)])
    path = np.array([xr(p) for p in rhos])
    ax.plot(path[:, 0], path[:, 1], color=RED, lw=1.1, label=r'$\mathbf{x}_\rho$, $\rho\geq0$')
    for p, off in [(1, (0.0, -0.05)), (5, (0.02, -0.07))]:
        ax.plot(*xr(p), 'o', color=RED, ms=2.8)
        ax.text(xr(p)[0]+off[0], xr(p)[1]+off[1], fr'$\rho={p}$', fontsize=7, color=RED, va='top')
    ax.plot(*xr(20), 'o', color=RED, ms=2.8)
    ax.plot(0.8, 0.2, '*', color=INK, ms=6, zorder=6)
    ax.set(xlim=(-0.3, 1.4), ylim=(-0.6, 1.1), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$')
    ax.legend(loc='upper right')
    ax.set_title('(a) 罚目标等值线与解路径')
    ax2 = axes[1]
    pr = np.geomspace(0.01, 1e4, 300)
    res = 4/(4+5*pr)
    lam_max = (5+2*pr+np.sqrt(9+4*pr**2))/2
    lam_min = (5+2*pr-np.sqrt(9+4*pr**2))/2
    ax2.loglog(pr, res, color=RED, lw=1.1, label='约束违约')
    ax2.loglog(pr, lam_max/lam_min, color=BLUE, lw=1.1, label='Hessian 条件数')
    ax2.set(xlabel=r'$\rho$', xlim=(1e-2, 1e4), ylim=(1e-4, 1e5))
    ax2.legend(loc='center left')
    ax2.set_title('(b) 可行性与病态')
    kappa = lambda p: float((5+2*p+np.sqrt(9+4*p**2))/(5+2*p-np.sqrt(9+4*p**2)))
    save(fig, D/'c5-penalty-path', 'figure', {
        'problem': 'min (x1^2+4x2^2)/2 s.t. x1+x2=1', 'penalty': '(rho/2)(x1+x2-1)^2',
        'x_rho': '(4 rho, rho)/(4+5 rho)', 'residual': '-4/(4+5 rho)',
        'hessian': 'diag(1,4)+rho*11^T', 'eigs': '((5+2rho) +- sqrt(9+4rho^2))/2',
        'kappa': {str(p): round(kappa(p), 3) for p in [0, 1, 10, 100, 1000]},
        'contour_rho': rho})


def c5_exact_penalty():
    fig, axes = figure(width_mm=169, height_mm=56, ncols=2, sharey=True)
    x = np.linspace(-1.0, 2.0, 400)
    ax = axes[0]
    ax.plot(x, x, color=MUTED, lw=.8, ls=':', label=r'$f(x)=x$')
    for rho, col in [(1, YELLOW), (4, GREEN), (16, BLUE)]:
        y = x + rho/2*np.maximum(1-x, 0)**2
        ax.plot(x, y, color=col, lw=1.1, label=fr'$\rho={rho}$')
        xm = 1 - 1/rho
        ax.plot(xm, xm + 1/(2*rho), 'o', color=col, ms=3)
    ax.axvline(1, color=RED, lw=.6, ls='--')
    ax.set(xlim=(-1, 2), ylim=(-1.2, 3), xlabel=r'$x$')
    ax.legend(loc='upper left')
    ax.set_title(r'(a) $x+\frac{\rho}{2}[1-x]_+^2$')
    ax2 = axes[1]
    ax2.plot(x, x, color=MUTED, lw=.8, ls=':')
    for rho, col in [(0.5, YELLOW), (1.0, GREEN), (2.0, BLUE)]:
        ax2.plot(x, x + rho*np.maximum(1-x, 0), color=col, lw=1.1, label=fr'$\rho={rho:g}$')
    ax2.plot(1, 1, 'o', color=BLUE, ms=3)
    ax2.axvline(1, color=RED, lw=.6, ls='--')
    ax2.set(xlim=(-1, 2), xlabel=r'$x$')
    ax2.legend(loc='upper left')
    ax2.set_title(r'(b) $x+\rho[1-x]_+$')
    save(fig, D/'c5-exact-penalty', 'figure', {
        'problem': 'min x s.t. 1-x<=0', 'x_star': 1, 'lambda_star': 1,
        'quadratic_minimizer': '1-1/rho', 'quadratic_rhos': [1, 4, 16],
        'exact_rhos': [0.5, 1, 2], 'exact_behavior': 'rho<1 unbounded below; rho=1 every x<=1 minimizes; rho>1 unique minimizer x=1'})


# ---------------------------------------------------------------- 5.7
def c5_al_multiplier():
    fig, axes = figure(width_mm=169, height_mm=56, ncols=2)
    T = 12
    nus = {}
    nu = 0.0; seq = [nu]
    for t in range(T):
        x = np.array([-nu, -nu/4]); nu = nu + 0.4*(x.sum()-1); seq.append(nu)
    nus['DA'] = (np.array(seq), GREEN, '-o')
    resid = {}
    for rho, col, mk in [(1.0, BLUE, '-s'), (10.0, PURPLE, '-^')]:
        nu = 0.0; seq = [nu]; rs = []
        for t in range(T):
            rr = -(4+5*nu)/(4+5*rho)
            x = np.array([-(nu+rho*rr), -(nu+rho*rr)/4])
            rs.append(abs(x.sum()-1)); nu = nu + rho*(x.sum()-1); seq.append(nu)
        nus[f'AL{rho:g}'] = (np.array(seq), col, mk)
        resid[rho] = rs
    ax = axes[0]
    labels = {'DA': '对偶上升，η=0.4', 'AL1': '增广Lagrange，ρ=1', 'AL10': '增广Lagrange，ρ=10'}
    for lab, (s, col, mk) in nus.items():
        e = np.abs(s + 0.8)
        k = e > 1e-15
        ax.semilogy(np.arange(T+1)[k], e[k], mk, color=col, ms=2.4, lw=.9, label=labels[lab])

    ax.set(xlim=(0, T), ylim=(1e-13, 3), xlabel=r'$t$', ylabel=r'$|\nu^{(t)}-\nu^*|$')
    ax.legend(loc='lower left', title='')
    ax.set_title('(a) 乘子误差')
    ax2 = axes[1]
    pr = np.array([1, 10, 100, 1000.0])
    ax2.semilogy(np.arange(1, T+1), resid[1.0], '-s', color=BLUE, ms=2.4, lw=.9, label='增广Lagrange，ρ=1')
    ax2.semilogy(np.arange(1, T+1), resid[10.0], '-^', color=PURPLE, ms=2.4, lw=.9, label='增广Lagrange，ρ=10')
    for p in [10, 100, 1000]:
        ax2.axhline(4/(4+5*p), color=RED, lw=.6, ls='--')
        ax2.text(T-0.2, 4/(4+5*p)*1.3, fr'$\rho={p}$', fontsize=7, color=RED, ha='right')
    ax2.text(7.0, 2.0, '二次惩罚（固定罚参数）', fontsize=7, color=RED, ha='left')
    ax2.set(xlim=(0, T), ylim=(1e-13, 3), xlabel=r'$t$', ylabel='约束违约')
    ax2.legend(loc='lower left')
    ax2.set_title('(b) 约束违约')
    save(fig, D/'c5-al-multiplier', 'figure', {
        'problem': 'min (x1^2+4x2^2)/2 s.t. x1+x2=1', 'nu_star': -0.8,
        'dual_ascent': 'x(nu)=(-nu,-nu/4), nu+=nu+0.4*(x1+x2-1), error factor 0.5',
        'augmented_lagrangian': 'error factor 4/(4+5 rho)', 'factors': {'1': 4/9, '10': 4/54},
        'dual_ascent_nus': r(nus['DA'][0][:5]),
        'al_rho1_nus': r(nus['AL1'][0][:5]),
        'quadratic_penalty_residual': {str(p): 4/(4+5*p) for p in [10, 100, 1000]}})


def c5_admm():
    """ADMM for min (x-3)^2/2 + |z| s.t. x=z, rho=1, scaled dual u."""
    fig, axes = figure(width_mm=169, height_mm=64, ncols=2, gridspec_kw={'width_ratios': [1.0, 1.0]})
    ax = axes[0]
    g = np.linspace(-0.3, 3.3, 300)
    X, Z = np.meshgrid(g, g)
    F = 0.5*(X-3)**2 + np.abs(Z)
    ax.contour(X, Z, F, levels=[1.5, 2.0, 2.5, 3.0, 3.5, 4.5], colors=GRID, linewidths=.6)
    ax.plot([-0.3, 3.3], [-0.3, 3.3], color=BLUE, lw=1.1)
    ax.text(3.2, 2.95, r'$x=z$', color=BLUE, fontsize=7.5, ha='right', va='top')
    rho = 1.0
    x = 0.0; z = 0.0; u = 0.0
    pts = [(x, z)]; rs = []; ss = []; it = []
    soft = lambda v, k: np.sign(v)*max(abs(v)-k, 0)
    for t in range(25):
        x = (3 + rho*(z - u))/(1 + rho); pts.append((x, z))
        zold = z
        z = soft(x + u, 1/rho); pts.append((x, z))
        u = u + x - z
        rs.append(abs(x - z)); ss.append(abs(rho*(z - zold))); it.append((round(x, 5), round(z, 5), round(u, 5)))
    pts = np.array(pts)
    ax.plot(pts[:12, 0], pts[:12, 1], color=RED, lw=.9)
    ax.plot(pts[2:12:2, 0], pts[2:12:2, 1], 'o', color=RED, ms=2.6)
    ax.plot(2, 2, '*', color=INK, ms=6, zorder=6)
    ax.text(2.08, 1.9, r'$(2,2)$', fontsize=7.5, va='top')
    ax.set(xlim=(-0.3, 3.3), ylim=(-0.3, 3.3), aspect='equal', xlabel=r'$x$', ylabel=r'$z$')
    ax.set_title('(a) 交替的两块更新')
    ax2 = axes[1]
    errs = {}
    for rh, col, mk in [(0.5, GREEN, '-^'), (1.0, RED, '-o'), (2.0, BLUE, '-s')]:
        xx = zz = uu = 0.0; e = []
        for t in range(25):
            xx = (3 + rh*(zz - uu))/(1 + rh); zz = soft(xx + uu, 1/rh); uu = uu + xx - zz
            e.append(abs(xx - 2))
        e = np.array(e); k = e > 1e-14
        ax2.semilogy(np.arange(1, 26)[k], e[k], mk, color=col, ms=2.2, lw=.9, label=f'ρ={rh:g}')
        errs[str(rh)] = r(e[:5], 5)
    ax2.set(xlim=(0, 25), xlabel=r'$t$', ylim=(1e-10, 3))
    ax2.legend(loc='upper right')
    ax2.set_title('(b) 与解的距离')
    ax2.set_ylabel(r'$|x^{(t)}-2|$')
    save(fig, D/'c5-admm', 'figure', {
        'problem': 'min (x-3)^2/2+|z| s.t. x-z=0', 'rho': rho, 'start': 'z=0,u=0',
        'updates': 'x=(3+rho(z-u))/(1+rho); z=S_{1/rho}(x+u); u=u+x-z',
        'first_iterates_x_z_u': it[:5], 'solution': [2, 2], 'scaled_dual_limit': 1,
        'panel_b_x_errors_by_rho': errs, 'error_factor_after_u_settles': 'rho/(1+rho)'})


# ---------------------------------------------------------------- 5.8
def c5_sqp():
    fig, ax = figure(width_mm=100, height_mm=70)
    g = np.linspace(-2.2, 1.0, 300)
    X1, X2 = np.meshgrid(g, g)
    ax.contour(X1, X2, X1+X2, levels=np.arange(-4, 2, 0.5), colors=GRID, linewidths=.6)
    th = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.sqrt(2)*np.cos(th), np.sqrt(2)*np.sin(th), color=BLUE, lw=1.1)
    x = np.array([0.2, -1.6]); nu = 1.0
    path = [x.copy()]; nus = [nu]; hs = [x@x-2]
    for k in range(6):
        gr = np.array([1., 1.]); h = x@x-2; a = 2*x
        K = np.block([[2*nu*np.eye(2), a[:, None]], [a[None, :], np.zeros((1, 1))]])
        sol = np.linalg.solve(K, np.concatenate([-gr, [-h]]))
        if k == 0:
            # linearized constraint of the first subproblem: h + a.(y-x) = 0
            yy = np.linspace(-2.2, 1.0, 10)
            ax.plot(yy, x[1] + (-h - a[0]*(yy-x[0]))/a[1], color=YELLOW, lw=.9, ls='--')
        x = x + sol[:2]; nu = sol[2]
        path.append(x.copy()); nus.append(nu); hs.append(x@x-2)
    path = np.array(path)
    ax.plot(path[:, 0], path[:, 1], '-o', color=RED, ms=2.8, lw=.9)
    for i in range(2):
        ax.text(path[i, 0]+0.06, path[i, 1]+0.02, fr'$\mathbf{{x}}^{{({i})}}$', fontsize=7.5, color=RED)
    ax.plot(-1, -1, '*', color=INK, ms=6, zorder=6)
    ax.text(-1.06, -0.94, r'$\mathbf{x}^*$', ha='right', va='bottom', fontsize=8)
    ax.text(0.95, -0.95, '首个子问题的\n线性化约束', color=YELLOW, fontsize=7.5, ha='right', va='top')
    ax.set(xlim=(-2.2, 1.0), ylim=(-2.2, 1.0), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$')
    save(fig, D/'c5-sqp', 'figure', {
        'problem': 'min x1+x2 s.t. x1^2+x2^2=2', 'x_star': [-1, -1], 'nu_star': 0.5,
        'start': [0.2, -1.6], 'nu0': 1.0, 'hessian': '2*nu*I (Lagrangian Hessian)',
        'iterates': [r(p, 5) for p in path], 'nus': r(nus, 5), 'constraint_values': r(hs, 6)})


# ---------------------------------------------------------------- 5.9
def _central(c, mu):
    f = lambda y: np.sum(mu/(c - y)) - 1
    y = brentq(f, -1e6, c.min() - 1e-14)
    return mu/(c - y), y


def c5_central_path():
    c = np.array([1., 2., 3.])
    fig, ax = figure(width_mm=96, height_mm=78)
    ax.fill(V3[:, 0], V3[:, 1], color=BLUE_FILL, lw=0)
    ax.plot(*np.vstack([V3, V3[:1]]).T, color=BLUE, lw=1.0)
    n = 260
    a, b = np.meshgrid(np.linspace(1e-4, 1, n), np.linspace(1e-4, 1, n))
    m = a + b < 1 - 1e-4
    P = np.stack([a[m], b[m], 1-a[m]-b[m]], 1)
    mu0 = 0.3
    B = P @ c - mu0*np.log(P).sum(1)
    XY = tern(P)
    xc, _ = _central(c, mu0)
    Bmin = xc @ c - mu0*np.log(xc).sum()
    ax.tricontour(XY[:, 0], XY[:, 1], B, levels=Bmin + np.array([0.05, 0.15, 0.35, 0.7, 1.2]), colors=GREEN, linewidths=.6)
    mus = np.geomspace(1e3, 1e-3, 200)
    path = np.array([_central(c, m_)[0] for m_ in mus])
    ax.plot(*tern(path).T, color=RED, lw=1.2)
    marks = [10, 1, 0.3, 0.1, 0.01]
    facts_pts = {}
    for m_ in marks:
        xx, yy = _central(c, m_)
        ax.plot(*tern(xx).T, 'o', color=RED, ms=2.8)
        facts_pts[str(m_)] = {'x': r(xx), 'y': round(float(yy), 4), 'gap': round(float(c @ xx - yy), 6)}
    for m_, off in [(1, (0.035, -0.01)), (0.3, (0.03, -0.045)), (0.1, (0.0, -0.06))]:
        p = tern(_central(c, m_)[0])[0]
        ax.text(p[0]+off[0], p[1]+off[1], fr'$\mu={m_:g}$', fontsize=7, color=RED)
    ax.plot(*tern(np.ones(3)/3).T, 'x', color=INK, ms=4)
    for lab, v, off in [(r'$\mathbf{e}_1$', V3[0], (-0.05, -0.05)), (r'$\mathbf{e}_2$', V3[1], (0.05, -0.05)), (r'$\mathbf{e}_3$', V3[2], (0, 0.05))]:
        ax.text(v[0]+off[0], v[1]+off[1], lab, ha='center', va='center', fontsize=8)
    ax.set(xlim=(-0.1, 1.1), ylim=(-0.12, 0.95), aspect='equal')
    ax.axis('off')
    save(fig, D/'c5-central-path', 'figure', {
        'problem': 'min x1+2x2+3x3 s.t. x1+x2+x3=1, x>=0', 'x_star': [1, 0, 0],
        'central_point': 'x_j=mu/(c_j-y), sum x_j=1', 'contour_mu': mu0,
        'marked_points': facts_pts, 'gap_formula': 'c^T x - y = 3 mu'})


def c5_pdipm():
    A = np.array([[2, 1, 1, 0], [1, 2, 0, 1.]]); b = np.array([4, 4.]); c = np.array([-3, -2, 0, 0.])
    m, n = A.shape
    x = 2*np.ones(n); s = np.ones(n); y = np.zeros(m); sigma = 0.2
    rows = []
    for k in range(16):
        rp = A@x - b; rd = A.T@y + s - c; mu = x@s/n
        rows.append((k, float(np.linalg.norm(rp)), float(np.linalg.norm(rd)), float(x@s), float(c@x), float(b@y)))
        K = np.block([[np.zeros((n, n)), A.T, np.eye(n)], [A, np.zeros((m, m)), np.zeros((m, n))],
                      [np.diag(s), np.zeros((n, m)), np.diag(x)]])
        rhs = -np.concatenate([rd, rp, x*s - sigma*mu])
        d = np.linalg.solve(K, rhs); dx, dy, ds = d[:n], d[n:n+m], d[n+m:]

        def mstep(v, dv):
            neg = dv < 0
            return (-v[neg]/dv[neg]).min() if neg.any() else np.inf
        al = min(1.0, 0.99*min(mstep(x, dx), mstep(s, ds)))
        x = x + al*dx; y = y + al*dy; s = s + al*ds
    rows = np.array(rows)
    fig, ax = figure(width_mm=100, height_mm=56)
    keep = lambda v: np.where(v > 1e-12, v, np.nan)
    ax.semilogy(rows[:, 0], keep(rows[:, 1]), '-o', color=RED, ms=2.4, lw=.9, label=r'$\|\mathbf{A}\mathbf{x}-\mathbf{b}\|_2$')
    ax.semilogy(rows[:, 0], keep(rows[:, 2]), '-s', color=BLUE, ms=2.4, lw=.9, label=r'$\|\mathbf{A}^{\mathrm{T}}\mathbf{y}+\mathbf{s}-\mathbf{c}\|_2$')
    ax.semilogy(rows[:, 0], rows[:, 3], '-^', color=GREEN, ms=2.4, lw=.9, label=r'$\mathbf{x}^{\mathrm{T}}\mathbf{s}$')
    ax.text(2.3, 3e-11, '两项残差降至舍入误差以下', fontsize=7.5, color=MUTED)
    ax.set(xlim=(0, 15), ylim=(1e-11, 1e2), xlabel=r'$t$')
    ax.legend(loc='upper right')
    save(fig, D/'c5-pdipm', 'figure', {
        'problem': 'min -3x1-2x2 s.t. 2x1+x2+x3=4, x1+2x2+x4=4, x>=0',
        'optimum': {'x': [4/3, 4/3, 0, 0], 'y': [-4/3, -1/3], 'value': -20/3},
        'start': {'x': [2, 2, 2, 2], 's': [1, 1, 1, 1], 'y': [0, 0]}, 'sigma': sigma,
        'step_rule': 'alpha=min(1, 0.99*max step keeping x,s>0)',
        'rows_k_rp_rd_xs_cx_by': [[int(r_[0])] + [float(f'{v:.3e}') for v in r_[1:]] for r_ in rows[:10]]})


# ---------------------------------------------------------------- 5.10
def c5_sdp_rounding():
    fig, axes = figure(width_mm=169, height_mm=62, ncols=2)
    th = np.linspace(0, 2*np.pi, 200)
    # (a) C4: rank-one solution
    ax = axes[0]
    ax.plot(np.cos(th), np.sin(th), color=GRID, lw=.6)
    vec = {1: (1, 0), 3: (1, 0), 2: (-1, 0), 4: (-1, 0)}
    arrow(ax, (0, 0), (1, 0), BLUE, lw=1.2); arrow(ax, (0, 0), (-1, 0), GREEN, lw=1.2)
    ax.text(1.05, 0.08, r'$\mathbf{v}_1=\mathbf{v}_3$', color=BLUE, fontsize=7.5)
    ax.text(-1.05, 0.08, r'$\mathbf{v}_2=\mathbf{v}_4$', color=GREEN, fontsize=7.5, ha='right')
    ax.plot([0.25, -0.25], [-1.2, 1.2], color=RED, lw=.9, ls='--')
    ax.text(-0.22, 1.08, '任一超平面', color=RED, fontsize=7.5, ha='right')
    ax.set(xlim=(-1.8, 1.8), ylim=(-1.3, 1.3), aspect='equal'); ax.axis('off')
    ax.set_title('(a) 四顶点圈')
    # (b) triangle: three vectors at 120 degrees
    ax2 = axes[1]
    ax2.plot(np.cos(th), np.sin(th), color=GRID, lw=.6)
    ang = np.pi/2 + np.array([0, 2*np.pi/3, 4*np.pi/3])
    cols = [BLUE, GREEN, GREEN]
    hyper = np.pi/2 - 0.35   # normal direction of the drawn hyperplane
    nrm = np.array([np.cos(hyper), np.sin(hyper)])
    for i, a in enumerate(ang):
        v = np.array([np.cos(a), np.sin(a)])
        col = BLUE if v @ nrm >= 0 else GREEN
        arrow(ax2, (0, 0), v, col, lw=1.2)
        ax2.text(1.17*v[0], 1.17*v[1], fr'$\mathbf{{v}}_{i+1}$', color=col, fontsize=7.5, ha='center', va='center')
    dirv = np.array([-nrm[1], nrm[0]])
    ax2.plot([-1.3*dirv[0], 1.3*dirv[0]], [-1.3*dirv[1], 1.3*dirv[1]], color=RED, lw=.9, ls='--')
    arrow(ax2, (0, 0), 0.45*nrm, RED, lw=.8)
    ax2.text(0.5*nrm[0]+0.05, 0.5*nrm[1], r'$\mathbf{r}$', color=RED, fontsize=7.5)
    ax2.set(xlim=(-1.8, 1.8), ylim=(-1.3, 1.3), aspect='equal'); ax2.axis('off')
    ax2.set_title('(b) 三角形')
    save(fig, D/'c5-sdp-rounding', 'figure', {
        'panel_a': {'graph': 'cycle 1-2-3-4-1, unit weights', 'X': 'x x^T, x=(1,-1,1,-1)', 'sdp_value': 4, 'max_cut': 4},
        'panel_b': {'graph': 'triangle, unit weights', 'X_offdiag': -0.5, 'vectors': 'unit vectors at 120 degrees',
                    'sdp_value': 2.25, 'max_cut': 2, 'hyperplane_normal_angle_rad': hyper,
                    'rounding': 'x_i=sign(<r,v_i>); every hyperplane in general position separates one vector from two'}})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    c5_tangency, c5_normal_cone, c5_cusp, c5_dual_envelope, c5_conjugate, c5_slater,
    c5_sensitivity, c5_psd_disk, c5_soc, c5_pg_fw, c5_mirror_simplex, c5_penalty_path,
    c5_exact_penalty, c5_al_multiplier, c5_admm, c5_sqp, c5_central_path, c5_pdipm, c5_sdp_rounding]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
