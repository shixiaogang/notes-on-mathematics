# coding: utf-8
"""Teaching charts for volume two, part "probability spaces", chapter 2
(conditional expectation and conditional distribution).

Exact group averages, conditional means and posterior curves come from the
formulas recorded in each saved facts file; every simulation uses a fixed numpy
seed recorded together with sample sizes and parameters.
Run from any directory:
  python figures/02-abstract-mathematics/02-probability-spaces/matplotlib/generate_ch2.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from scipy import stats

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL

D = Path(__file__).resolve().parent
SEED = 20261029


def cond_four_points():
    """Four equally likely points, X(omega)=omega, averaged within {0,2} and {4,6}."""
    fig, ax = figure(width_mm=100, height_mm=46)
    omega = np.array([0, 2, 4, 6])
    groups = [([0, 2], BLUE_FILL, BLUE), ([4, 6], GREEN_FILL, GREEN)]
    for pts, fill, col in groups:
        lo, hi = min(pts) - 0.8, max(pts) + 0.8
        ax.axvspan(lo, hi, color=fill, lw=0)
        m = float(np.mean(pts))
        ax.plot([lo + 0.15, hi - 0.15], [m, m], color=col, lw=2.0)
        ax.text(hi - 0.2, m + 0.35, f'{m:g}', color=col, ha='right', va='bottom', fontsize=7.5)
    ax.vlines(omega, 0, omega, color=MUTED, lw=.6)
    ax.plot(omega, omega, 'o', color=INK, ms=3.2, label=r'$X(\omega)$')
    ax.plot([], [], color=INK, lw=2.0, label='组内平均')
    ax.set(xlim=(-1.2, 7.2), ylim=(0, 7), xlabel=r'$\omega$', ylabel='数值')
    ax.set_xticks(omega)
    ax.text(1, 6.4, r'$A_1=\{0,2\}$', ha='center', fontsize=7.5, color=BLUE)
    ax.text(5, 6.4, r'$A_2=\{4,6\}$', ha='center', fontsize=7.5, color=GREEN)
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 0.86), handlelength=1.4)
    save(fig, D/'cond-four-points', 'figure', {
        'Omega': [0, 2, 4, 6], 'probabilities': [0.25] * 4, 'X': 'X(omega)=omega',
        'partition': [[0, 2], [4, 6]], 'group_means': [1, 5], 'overall_mean': 3})


def _block_means(x, fx, edges):
    out = np.empty_like(fx)
    means = []
    for a, b in zip(edges[:-1], edges[1:]):
        mask = (x >= a) & (x < b)
        m = float(fx[mask].mean())
        out[mask] = m
        means.append(m)
    return out, means


def cond_information_layers():
    """Conditional averages of X(w)=2w+sin(2 pi w) on [0,1) under four information levels."""
    x = (np.arange(200000) + 0.5) / 200000
    fx = 2 * x + np.sin(2 * np.pi * x)
    fig, axes = figure(width_mm=150, height_mm=44, ncols=4, sharey=True)
    specs = [('(a) 平凡信息', [0, 1]), ('(b) 两块', [0, .5, 1]),
             ('(c) 四块', [0, .25, .5, .75, 1]), ('(d) 完全信息', None)]
    facts = {'Omega': '[0,1) with Lebesgue probability', 'X': '2*w+sin(2*pi*w)',
             'integration': 'midpoint rule, 200000 cells'}
    for ax, (title, edges) in zip(axes, specs):
        ax.plot(x, fx, color=MUTED, lw=.7)
        if edges is None:
            ax.plot(x, fx, color=BLUE, lw=1.2)
        else:
            avg, means = _block_means(x, fx, np.array(edges))
            for a, b, m in zip(edges[:-1], edges[1:], means):
                ax.plot([a, b], [m, m], color=BLUE, lw=1.4)
            for e in edges[1:-1]:
                ax.axvline(e, color=GRID, lw=.6)
            facts[title] = {'edges': edges, 'block_means': [round(m, 4) for m in means]}
        ax.set(xlim=(0, 1), ylim=(-0.6, 2.6), xlabel=r'$\omega$')
        ax.set_xticks([0, .5, 1])
        ax.set_title(title)
    axes[0].set_ylabel('数值')
    save(fig, D/'cond-information-layers', 'figure', facts)


def cond_regression_scatter():
    """Scatter of (Y,X) with X=Y^2+eps, bin averages, and h(y)=y^2."""
    rng = np.random.default_rng(SEED)
    n, sigma = 600, 0.5
    y = rng.standard_normal(n)
    xv = y**2 + sigma * rng.standard_normal(n)
    fig, ax = figure(width_mm=100, height_mm=56)
    ax.plot(y, xv, 'o', ms=2.0, mec=BLUE, mew=.3, mfc=BLUE_FILL, label='样本点')
    edges = np.arange(-2.5, 2.51, 0.5)
    bin_means = []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (y >= a) & (y < b)
        if m.sum() >= 5:
            mu = xv[m].mean()
            ax.plot([a, b], [mu, mu], color=GREEN, lw=1.6)
            bin_means.append([float(a), float(b), int(m.sum()), round(float(mu), 3)])
    ax.plot([], [], color=GREEN, lw=1.6, label='组内平均')
    t = np.linspace(-2.6, 2.6, 400)
    ax.plot(t, t**2, color=RED, lw=1.1, label=r'$h(y)=y^2$')
    ax.set(xlim=(-2.6, 2.6), ylim=(-1.5, 8.2), xlabel=r'$y$', ylabel=r'$X$')
    ax.legend(loc='upper center', handlelength=1.4, ncols=3)
    save(fig, D/'cond-regression-scatter', 'figure', {
        'seed': SEED, 'n': n, 'model': 'Y~N(0,1), eps~N(0,0.25) independent, X=Y^2+eps',
        'exact_conditional_mean': 'h(y)=y^2', 'bins_width': 0.5, 'bins_with_at_least_5_points': bin_means})


def cond_jensen():
    """phi(x)=x^2 on the two groups of the four-point example."""
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    phi = lambda v: v**2
    facts = {'phi': 'x^2', 'groups': {}}
    for ax, pts, col, fill, tag in [(axes[0], [0, 2], BLUE, BLUE_FILL, '(a) 第一组 {0, 2}'),
                                    (axes[1], [4, 6], GREEN, GREEN_FILL, '(b) 第二组 {4, 6}')]:
        a, b = pts
        m = (a + b) / 2
        xs = np.linspace(a - 0.8, b + 0.8, 300)
        ax.plot(xs, phi(xs), color=INK, lw=1.1)
        ax.plot([a, b], [phi(a), phi(b)], color=col, lw=.9, ls='--')
        ax.plot([a, b], [phi(a), phi(b)], 'o', color=col, ms=3)
        mean_phi = (phi(a) + phi(b)) / 2
        ax.plot([m], [mean_phi], 's', color=col, ms=3.5)
        ax.plot([m], [phi(m)], 'o', color=RED, ms=3.5)
        ax.plot(xs, phi(m) + 2 * m * (xs - m), color=RED, lw=.7, ls=':')
        span = phi(b + 0.8) - phi(max(a - 0.8, 0) if a > 0 else 0)
        ax.text(m - 0.1, mean_phi + 0.02 * span, f'组内平均 {mean_phi:g}', color=col, fontsize=7.5, ha='right', va='bottom')
        ax.text(m + 0.1, phi(m) - 0.03 * span, f'函数值 {phi(m):g}', color=RED, fontsize=7.5, ha='left', va='top')
        ax.set(xlim=(a - 0.8, b + 0.8), xlabel=r'$x$')
        ax.set_title(tag)
        facts['groups'][str(pts)] = {'conditional_mean': m, 'phi_of_mean': phi(m), 'mean_of_phi': mean_phi}
    axes[0].set_ylabel(r'$\varphi(x)=x^2$')
    save(fig, D/'cond-jensen', 'figure', facts)


def cond_mse_decomposition():
    """E(X-Z)^2 = E(X-M)^2 + E(M-Z)^2 for X=Y^2+eps and four sigma(Y)-measurable predictors."""
    rng = np.random.default_rng(SEED)
    n, sigma2 = 400000, 0.25
    y = rng.standard_normal(n)
    xv = y**2 + np.sqrt(sigma2) * rng.standard_normal(n)
    M = y**2
    preds = [('常数 1', np.ones(n), 2.0), (r'$|Y|$', np.abs(y), 4 - 4 * np.sqrt(2 / np.pi)),
             (r'$0.8\,Y^2$', 0.8 * y**2, 0.12), (r'$M=Y^2$', M, 0.0)]
    fig, ax = figure(width_mm=100, height_mm=52)
    labels, mc = [], {}
    for i, (lab, z, exact_gap) in enumerate(preds):
        ax.bar(i, sigma2, color=BLUE_FILL, edgecolor=BLUE, lw=.6, width=.55)
        ax.bar(i, exact_gap, bottom=sigma2, color=YELLOW_FILL, edgecolor=YELLOW, lw=.6, width=.55)
        total_mc = float(np.mean((xv - z)**2))
        ax.plot(i, total_mc, 'D', color=INK, ms=3)
        ax.text(i, sigma2 + exact_gap + 0.06, f'{sigma2 + exact_gap:.3f}', ha='center', fontsize=7.5)
        labels.append(lab)
        mc[lab] = {'exact_total': sigma2 + exact_gap, 'exact_gap_E(M-Z)^2': exact_gap, 'monte_carlo_total': round(total_mc, 4)}
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    handles = [Patch(facecolor=BLUE_FILL, edgecolor=BLUE, lw=.6, label='不可消除部分'),
               Patch(facecolor=YELLOW_FILL, edgecolor=YELLOW, lw=.6, label='与条件平均的差距'),
               Line2D([], [], marker='D', ls='none', color=INK, ms=3, label='模拟均方误差')]
    ax.set_xticks(range(len(preds)), labels)
    ax.set(ylim=(0, 2.6), ylabel='均方误差', xlabel='预测量')
    ax.legend(handles=handles, loc='upper right', handlelength=1.2)
    save(fig, D/'cond-mse-decomposition', 'figure', {
        'seed': SEED, 'n': n, 'model': 'Y~N(0,1), eps~N(0,0.25) independent, X=Y^2+eps, M=E[X|Y]=Y^2',
        'predictors': mc})


def cond_kernel_types():
    """Rows K(s,.) of a deterministic kernel delta_{f(s)} and a density kernel N(f(s),0.15^2), f(s)=s."""
    fig, axes = figure(width_mm=112, height_mm=52, ncols=2, sharey=True)
    s_vals = [0, .25, .5, .75, 1]
    t = np.linspace(-0.4, 1.4, 600)
    sd = 0.15
    scale = 0.18 / stats.norm.pdf(0, scale=sd)
    for s in s_vals:
        axes[0].axhline(s, color=GRID, lw=.4)
        axes[0].annotate('', xy=(s, s + 0.2), xytext=(s, s),
                         arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.0, mutation_scale=6))
        axes[1].axhline(s, color=GRID, lw=.4)
        dens = stats.norm.pdf(t, loc=s, scale=sd) * scale
        axes[1].fill_between(t, s, s + dens, color=GREEN_FILL, lw=0)
        axes[1].plot(t, s + dens, color=GREEN, lw=1.0)
    for ax, title in zip(axes, ['(a) 确定性核', '(b) 密度核']):
        ax.set(xlim=(-0.4, 1.4), ylim=(-0.1, 1.3), xlabel=r'$t$')
        ax.set_title(title)
    axes[0].set_ylabel(r'$s$')
    axes[0].set_yticks(s_vals)
    save(fig, D/'cond-kernel-types', 'figure', {
        'f': 'f(s)=s', 'inputs_drawn': s_vals, 'panel_a': 'K(s,.)=point mass at f(s), drawn as arrow',
        'panel_b': 'K(s,dt)=N(s,0.15^2) density, curves scaled to common peak height 0.18 for display'})


def cond_cdf_rationals():
    """Conditional CDF of X=max(Z,0), Z|Y=y~N(y-0.5,0.5^2), evaluated on dyadic rationals and regularized."""
    fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
    F = lambda x, y: np.where(x < 0, 0.0, stats.norm.cdf((x - (y - 0.5)) / 0.5))
    ax = axes[0]
    grid = np.arange(-8, 17) / 8
    xs = np.linspace(-1, 2, 600)
    facts = {'model': 'X=max(Z,0), Z given Y=y ~ N(y-0.5, 0.5^2)', 'panel_a_y': [0.2, 0.5, 0.8],
             'panel_a_rationals': 'k/8, k=-8..16'}
    for y, col in [(0.2, BLUE), (0.5, GREEN), (0.8, YELLOW)]:
        left = xs[xs < 0]
        right = xs[xs >= 0]
        ax.plot(left, F(left, y), color=col, lw=1.0)
        ax.plot(right, F(right, y), color=col, lw=1.0, label=rf'$y={y}$')
        ax.plot(grid, F(grid, y), 'o', color=col, ms=2.0)
        facts[f'jump_at_0_y={y}'] = round(float(F(np.array(0.0), y)), 4)
    ax.set(xlim=(-1, 2), ylim=(-0.03, 1.03), xlabel=r'$x$', ylabel=r'$F(x\mid y)$')
    ax.set_title('(a) 有理点上的取值')
    ax.legend(loc='lower right', handlelength=1.2)
    ax = axes[1]
    y = 0.5
    r = np.array([1/2, 1/4, 1/8, 1/16, 1/32])
    xs2 = np.linspace(-0.3, 0.6, 400)
    ax.plot(xs2[xs2 < 0], 0 * xs2[xs2 < 0], color=GREEN, lw=1.0)
    ax.plot(xs2[xs2 >= 0], F(xs2[xs2 >= 0], y), color=GREEN, lw=1.0)
    ax.plot(r, F(r, y), 'o', color=INK, ms=2.6)
    for k, rv in enumerate(r[:3]):
        ax.annotate(f'$r={rv:g}$', (rv, F(np.array(rv), y)), xytext=(4, -9), textcoords='offset points', fontsize=7)
    f0 = float(F(np.array(0.0), y))
    ax.plot([0], [f0], 'o', color=GREEN, ms=3.6)
    ax.plot([0], [0], 'o', color=GREEN, ms=3.6, mfc='white')
    ax.annotate(r'$F(0\mid y)=\inf_{r>0}F(r\mid y)$', xy=(0.012, f0 - 0.01), xytext=(0.06, f0 - 0.22),
                fontsize=7.5, color=MUTED, arrowprops=dict(arrowstyle='->', color=MUTED, lw=.6))
    ax.set(xlim=(-0.3, 0.6), ylim=(-0.03, 1.03), xlabel=r'$x$')
    ax.set_title('(b) 从右侧逼近零点')
    facts['panel_b'] = {'y': y, 'rationals': r.tolist(), 'values': [round(float(v), 4) for v in F(r, y)], 'F(0|y)': round(f0, 4)}
    save(fig, D/'cond-cdf-rationals', 'figure', facts)


def cond_mixture_two_stage():
    """Two-component normal mixture: weighted components and P(X>Y) computed condition-then-average."""
    rng = np.random.default_rng(SEED)
    w = {1: 0.4, 2: 0.6}
    m = {1: 0.0, 2: 3.0}
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    x = np.linspace(-3.5, 6.5, 800)
    comp1 = w[1] * stats.norm.pdf(x, m[1])
    comp2 = w[2] * stats.norm.pdf(x, m[2])
    ax.fill_between(x[x > 1], comp1[x > 1], color=BLUE_FILL, lw=0)
    ax.fill_between(x[x > 2], comp2[x > 2], color=GREEN_FILL, lw=0)
    ax.plot(x, comp1, color=BLUE, lw=1.0, label=r'$0.4\,\varphi(x)$')
    ax.plot(x, comp2, color=GREEN, lw=1.0, label=r'$0.6\,\varphi(x-3)$')
    ax.plot(x, comp1 + comp2, color=INK, lw=1.1, ls='--', label='混合密度')
    ax.set(xlim=(-3.5, 6.5), ylim=(0, 0.3), xlabel=r'$x$', ylabel='密度')
    ax.set_title('(a) 加权的条件密度')
    ax.legend(loc='upper left', handlelength=1.4)
    ax = axes[1]
    p1, p2 = stats.norm.sf(1, m[1]), stats.norm.sf(2, m[2])
    total = w[1] * p1 + w[2] * p2
    n = 200000
    yy = np.where(rng.random(n) < w[1], 1, 2)
    xx = np.where(yy == 1, m[1], m[2]) + rng.standard_normal(n)
    mc = float(np.mean(xx > yy))
    ax.bar([0, 1], [p1, p2], color=[BLUE_FILL, GREEN_FILL], edgecolor=[BLUE, GREEN], lw=.6, width=.5)
    for i, p in enumerate([p1, p2]):
        ax.text(i, p + 0.03, f'{p:.3f}', ha='center', fontsize=7.5)
    ax.axhline(total, color=RED, lw=.8, ls='--')
    ax.text(-0.45, total + 0.03, f'加权平均 {total:.3f}', color=RED, fontsize=7.5, ha='left')
    ax.set_xticks([0, 1], [r'$y=1$', r'$y=2$'])
    ax.set(xlim=(-0.5, 1.5), ylim=(0, 1.0), ylabel=r'$ℙ(X>y\mid Y=y)$')
    ax.set_title('(b) 先条件、后平均')
    save(fig, D/'cond-mixture-two-stage', 'figure', {
        'seed': SEED, 'model': 'P(Y=1)=0.4, P(Y=2)=0.6; X|Y=1~N(0,1), X|Y=2~N(3,1)', 'h': 'indicator{x>y}',
        'conditional': [round(float(p1), 4), round(float(p2), 4)], 'average': round(float(total), 4),
        'monte_carlo_n': n, 'monte_carlo_P(X>Y)': round(mc, 4)})


def cond_bayes_posterior():
    """Class X in {0,1}, Y|X=x ~ N(2x-1,1); weighted likelihoods and posterior P(X=1|Y=y)."""
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    y = np.linspace(-4, 4, 600)
    pi = 0.3
    l0, l1 = stats.norm.pdf(y, -1), stats.norm.pdf(y, 1)
    ax = axes[0]
    ax.plot(y, (1 - pi) * l0, color=BLUE, lw=1.0, label=r'$0.7\,\ell(y\mid 0)$')
    ax.plot(y, pi * l1, color=GREEN, lw=1.0, label=r'$0.3\,\ell(y\mid 1)$')
    ax.plot(y, (1 - pi) * l0 + pi * l1, color=INK, lw=1.1, ls='--', label=r'$q(y)$')
    ax.axvline(1, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(-4, 4), ylim=(0, 0.42), xlabel=r'$y$', ylabel='密度')
    ax.set_title('(a) 先验加权的似然')
    ax.legend(loc='upper right', handlelength=1.4)
    ax = axes[1]
    facts = {'likelihoods': 'l(y|0)=N(-1,1) density, l(y|1)=N(1,1) density', 'posterior_at_y=1': {}}
    for p, col in [(0.3, GREEN), (0.5, PURPLE)]:
        post = p * l1 / (p * l1 + (1 - p) * l0)
        ax.plot(y, post, color=col, lw=1.1, label=rf'$ℙ(X=1)={p}$')
        v = 1 / (1 + (1 - p) / p * np.exp(-2))
        ax.plot([1], [v], 'o', color=col, ms=3)
        facts['posterior_at_y=1'][str(p)] = round(float(v), 4)
    ax.axvline(1, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(-4, 4), ylim=(-0.02, 1.02), xlabel=r'$y$', ylabel=r'$ℙ(X=1\mid Y=y)$')
    ax.set_title('(b) 后验概率')
    ax.legend(loc='upper left', handlelength=1.4)
    save(fig, D/'cond-bayes-posterior', 'figure', facts)


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    cond_four_points, cond_information_layers, cond_regression_scatter, cond_jensen,
    cond_mse_decomposition, cond_kernel_types, cond_cdf_rationals, cond_mixture_two_stage,
    cond_bayes_posterior]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
