# coding: utf-8
"""Analytic teaching charts for volume one, part 5, chapter 1 (random variables and distributions).

Every curve is an explicit formula listed in the saved facts; no sampled data.
Run from any directory:
  python3 figures/01-basic-mathematics/05-probability-and-statistics-basics/matplotlib/generate_ch1.py [name ...]
"""
from pathlib import Path
from math import comb, exp, factorial, gamma, lgamma, log, sqrt
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL

D = Path(__file__).resolve().parent


def step_cdf(ax, xs, ps, lo, hi, color):
    """Draw a right-continuous step CDF with filled (attained) and open (left-limit) dots."""
    cum = np.cumsum(ps)
    pts = [lo] + list(xs) + [hi]
    vals = [0] + list(cum)
    for i in range(len(vals)):
        ax.plot([pts[i], pts[i+1]], [vals[i], vals[i]], color=color, lw=1.1)
    for x, a, b in zip(xs, [0] + list(cum[:-1]), cum):
        ax.plot([x], [a], 'o', mfc='white', mec=color, ms=3)
        ax.plot([x], [b], 'o', color=color, ms=3)
    return cum


def prob_cdf_three_types():
    fig, axs = figure(width_mm=160, height_mm=50, ncols=3)
    # (a) fair die
    step_cdf(axs[0], range(1, 7), [1/6]*6, -0.5, 7.5, BLUE)
    axs[0].set(xlim=(-0.5, 7.5), xticks=range(0, 8), title='(a) 离散：公平骰子点数')
    # (b) standard exponential
    x = np.linspace(-1, 6, 800)
    axs[1].plot(x, np.where(x < 0, 0, 1-np.exp(-np.clip(x, 0, None))), color=GREEN)
    axs[1].set(xlim=(-1, 6), title='(b) 有密度：等待时间')
    # (c) mixed: P(T=0)=0.3, otherwise standard exponential
    xl = np.linspace(-1, 0, 50); xr = np.linspace(0, 6, 600)
    axs[2].plot(xl, 0*xl, color=PURPLE)
    axs[2].plot(xr, 0.3+0.7*(1-np.exp(-xr)), color=PURPLE)
    axs[2].plot([0], [0], 'o', mfc='white', mec=PURPLE, ms=3)
    axs[2].plot([0], [0.3], 'o', color=PURPLE, ms=3)
    axs[2].annotate('', xy=(0.35, 0.3), xytext=(0.35, 0), arrowprops=dict(arrowstyle='<->', color=MUTED, lw=.6))
    axs[2].text(0.5, 0.12, '跳跃 0.3', color=MUTED, fontsize=7.5)
    axs[2].set(xlim=(-1, 6), title='(c) 混合：可能无须等待')
    for ax, lab in zip(axs, [r'$x$', r'$t$', r'$t$']):
        ax.set(ylim=(-0.04, 1.06), yticks=[0, .5, 1], xlabel=lab)
        ax.axhline(1, color=GRID, lw=.4, zorder=0)
    axs[0].set_ylabel(r'$F(x)$')
    save(fig, D/'prob-cdf-three-types', 'figure', {
        'panel_a': 'fair die, F(x)=floor(x)/6 for 0<=x<=6', 'panel_b': 'F(t)=1-exp(-t), t>=0',
        'panel_c': 'F(t)=0.3+0.7(1-exp(-t)), t>=0; atom 0.3 at t=0'})


def prob_pmf_cdf():
    fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
    ks = np.arange(4); ps = np.array([1, 3, 3, 1])/8
    axs[0].vlines(ks, 0, ps, color=BLUE, lw=1.1)
    axs[0].plot(ks, ps, 'o', color=BLUE, ms=3.2)
    for k, p in zip(ks, ps):
        axs[0].text(k, p+0.03, f'{int(p*8)}/8', ha='center', fontsize=7.5)
    axs[0].set(xlim=(-0.6, 3.6), ylim=(0, 0.5), xticks=ks, yticks=[0, .125, .25, .375],
               yticklabels=['0', '1/8', '2/8', '3/8'], xlabel=r'$k$', ylabel=r'$p_X(k)$', title='(a) 质量函数')
    cum = step_cdf(axs[1], ks, ps, -0.8, 3.8, BLUE)
    for k, a, b in zip(ks, [0] + list(cum[:-1]), cum):
        axs[1].annotate('', xy=(k+0.18, b), xytext=(k+0.18, a), arrowprops=dict(arrowstyle='<->', color=MUTED, lw=.6, shrinkA=0, shrinkB=0))
    axs[1].set(xlim=(-0.8, 3.8), ylim=(-0.04, 1.06), xticks=ks, yticks=[0, .125, .5, .875, 1],
               yticklabels=['0', '1/8', '4/8', '7/8', '1'], xlabel=r'$x$', ylabel=r'$F_X(x)$', title='(b) 分布函数')
    save(fig, D/'prob-pmf-cdf', 'figure', {
        'variable': 'number of heads in three fair coin tosses', 'pmf': [1/8, 3/8, 3/8, 1/8],
        'cdf_values': cum.tolist(), 'arrows': 'jump sizes equal pmf values'})


def prob_density_above_one():
    fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
    x = np.linspace(-0.2, 1.0, 1201)
    f = np.where((x > 0) & (x < 0.5), 2.0, 0.0)
    axs[0].plot(x, f, color=BLUE)
    xs = np.linspace(0.1, 0.3, 50)
    axs[0].fill_between(xs, 0, 2, color=BLUE_FILL, lw=0)
    axs[0].text(0.2, 0.5, '0.4', ha='center', fontsize=7.5)
    axs[0].set(xlim=(-0.2, 1.0), ylim=(0, 3.2), xlabel=r'$x$', ylabel=r'$f_X(x)$', title='(a) 区间 (0, 1/2) 上均匀')
    x = np.linspace(-0.2, 1.6, 1201)
    f = np.where(x >= 0, 3*np.exp(-3*np.clip(x, 0, None)), 0)
    axs[1].plot(x[x < 0], f[x < 0], color=GREEN); axs[1].plot(x[x >= 0], f[x >= 0], color=GREEN)
    xs = np.linspace(0, 0.2, 80)
    axs[1].fill_between(xs, 0, 3*np.exp(-3*xs), color=GREEN_FILL, lw=0)
    axs[1].text(0.1, 0.5, f'{1-exp(-0.6):.3f}', ha='center', fontsize=7.5)
    axs[1].set(xlim=(-0.2, 1.6), ylim=(0, 3.2), xlabel=r'$t$', ylabel=r'$f_T(t)$', title='(b) 率为 3 的指数密度')
    for ax in axs:
        ax.axhline(1, color=MUTED, lw=.6, ls='--')
    save(fig, D/'prob-density-above-one', 'figure', {
        'panel_a': 'f(x)=2 on (0,1/2); shaded P(0.1<X<=0.3)=0.4',
        'panel_b': 'f(t)=3exp(-3t), t>=0; shaded P(0<T<=0.2)=1-exp(-0.6)', 'value': 1-exp(-0.6),
        'reference_line': 'y=1'})


def quantile_cdf(x):
    x = np.asarray(x, float)
    return np.select([x < 0, x < 1, x < 2, x < 3], [0, 0.4*x, 0.4, 0.7+0.3*(x-2)], 1.0)


def prob_quantile_inverse():
    fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axs[0]
    for a, b in [(-0.5, 2), (2, 3.6)]:
        xx = np.linspace(a, b, 400, endpoint=False)
        ax.plot(xx, quantile_cdf(xx), color=BLUE)
    ax.plot([2], [0.4], 'o', mfc='white', mec=BLUE, ms=3); ax.plot([2], [0.7], 'o', color=BLUE, ms=3)
    ax.plot([1, 2], [0.4, 0.4], color=YELLOW, lw=2.2, alpha=.8, solid_capstyle='butt')
    ax.text(1.5, 0.47, '平台', ha='center', fontsize=7.5, color=MUTED)
    ax.text(2.12, 0.58, '跳跃', va='bottom', fontsize=7.5, color=MUTED)
    ax.axhline(0.55, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(-0.5, 3.6), ylim=(-0.04, 1.06), xticks=[0, 1, 2, 3], yticks=[0, .4, .55, .7, 1],
           xlabel=r'$x$', ylabel=r'$F(x)$', title='(a) 分布函数')
    ax = axs[1]
    p1 = np.linspace(0.001, 0.4, 200); p2 = np.linspace(0.4, 0.7, 50); p3 = np.linspace(0.7, 0.999, 200)
    ax.plot(p1, 2.5*p1, color=PURPLE)
    ax.plot(p2, 0*p2+2, color=PURPLE)
    ax.plot(p3, 2+(p3-0.7)/0.3, color=PURPLE)
    ax.plot([0.4], [1], 'o', color=PURPLE, ms=3); ax.plot([0.4], [2], 'o', mfc='white', mec=PURPLE, ms=3)
    ax.plot([0.4, 0.7], [2, 2], color=YELLOW, lw=2.2, alpha=.8, solid_capstyle='butt')
    ax.plot([0.55], [2], 'o', color=INK, ms=3)
    ax.set(xlim=(0, 1), ylim=(-0.1, 3.2), xticks=[0, .4, .55, .7, 1], yticks=[0, 1, 2, 3],
           xlabel=r'$p$', ylabel=r'$Q(p)$', title='(b) 分位数函数')
    save(fig, D/'prob-quantile-inverse', 'figure', {
        'distribution': 'mass 0.4 uniform on [0,1], atom 0.3 at x=2, mass 0.3 uniform on [2,3]',
        'cdf': '0.4x on [0,1); 0.4 on [1,2); 0.7+0.3(x-2) on [2,3); 1 after',
        'quantile': 'Q(p)=2.5p for p<=0.4; 2 for 0.4<p<=0.7; 2+(p-0.7)/0.3 for p>0.7',
        'marked_level': 0.55, 'Q(0.55)': 2})


def prob_skewed_locations():
    fig, ax = figure(width_mm=112, height_mm=46)
    x = np.linspace(0, 8, 800)
    ax.plot(x, x*np.exp(-x), color=BLUE)
    ax.fill_between(x, 0, x*np.exp(-x), color=BLUE_FILL, lw=0)
    med = 1.6783469900166625
    for v, c, ls, lab in [(1, GREEN, '-', '众数 1'), (med, YELLOW, '--', '中位数 1.68'), (2, RED, '-.', '均值 2')]:
        ax.plot([v, v], [0, v*exp(-v)], color=c, ls=ls, lw=1.1, label=lab)
    ax.set(xlim=(0, 8), ylim=(0, 0.42), xlabel=r'$x$', ylabel=r'$f(x)=x e^{-x}$')
    ax.legend(loc='upper right')
    save(fig, D/'prob-skewed-locations', 'figure', {
        'density': 'f(x)=x exp(-x), x>0 (Gamma(2,1))', 'mode': 1, 'median': med, 'mean': 2,
        'median_equation': '1-(1+m)exp(-m)=1/2'})


def prob_discrete_pmfs():
    fig, axs = figure(width_mm=160, height_mm=50, ncols=4)
    ax = axs[0]
    pi = [0.6, 0.3, 0.1]
    ax.bar([1, 2, 3], pi, width=0.5, color=BLUE_FILL, edgecolor=BLUE, lw=.75)
    ax.set(xticks=[1, 2, 3], xlim=(0.4, 3.6), title='(a) 类别分布')
    ax.set_xticklabels(['晴', '雨', '雪'])
    def stems(ax, k, p, color):
        ax.vlines(k, 0, p, color=color, lw=1.1); ax.plot(k, p, 'o', color=color, ms=2.6)
    k = np.arange(0, 11); p = [comb(10, i)*0.3**i*0.7**(10-i) for i in k]
    stems(axs[1], k, p, GREEN); axs[1].set(title='(b) 二项 Bin(10, 0.3)', xticks=[0, 5, 10])
    k = np.arange(1, 16); pg = [0.7**(i-1)*0.3 for i in k]
    stems(axs[2], k, pg, YELLOW); axs[2].set(title='(c) 几何 Geom(0.3)', xticks=[1, 5, 10, 15])
    k = np.arange(0, 13); pp = [exp(-3)*3**i/factorial(i) for i in k]
    stems(axs[3], k, pp, PURPLE); axs[3].set(title='(d) Poisson(3)', xticks=[0, 3, 6, 9, 12])
    for ax in axs:
        ax.set(ylim=(0, 0.65), yticks=[0, .2, .4, .6])
    for ax in axs[1:]:
        ax.set_xlabel(r'$k$')
    axs[0].set_ylabel('概率')
    save(fig, D/'prob-discrete-pmfs', 'figure', {
        'categorical': pi, 'binomial': {'n': 10, 'p': 0.3, 'mean': 3, 'var': 2.1},
        'geometric': {'p': 0.3, 'support': '1..15 shown', 'mean': 1/0.3}, 'poisson': {'lambda': 3, 'support': '0..12 shown'}})


def prob_binomial_poisson():
    fig, ax = figure(width_mm=112, height_mm=50)
    k = np.arange(0, 11)
    pois = np.array([exp(-3)*3**i/factorial(i) for i in k])
    ax.bar(k, pois, width=0.7, color=GRID, edgecolor=MUTED, lw=.5, label='Poisson(3)')
    facts = {'poisson_lambda': 3, 'k': k.tolist(), 'poisson': pois.round(5).tolist()}
    for n, c, m, dx in [(6, RED, 's', -0.22), (15, YELLOW, '^', 0), (60, BLUE, 'o', 0.22)]:
        b = np.array([comb(n, i)*(3/n)**i*(1-3/n)**(n-i) if i <= n else 0 for i in k])
        ax.plot(k+dx, b, m, color=c, ms=3.2, label=rf'$\mathrm{{Bin}}({n},\,3/{n})$')
        facts[f'binomial_n{n}'] = b.round(5).tolist()
        facts[f'sum_abs_diff_n{n}'] = float(sum(abs(comb(n, i)*(3/n)**i*(1-3/n)**(n-i) - exp(-3)*3**i/factorial(i)) for i in range(0, n+1)) + sum(exp(-3)*3**i/factorial(i) for i in range(n+1, 150)))
    ax.set(xlim=(-0.6, 10.6), ylim=(0, 0.34), xticks=k, xlabel=r'$k$', ylabel='概率')
    ax.legend(loc='upper right')
    save(fig, D/'prob-binomial-poisson', 'figure', facts)


def prob_continuous_densities():
    fig, axs = figure(width_mm=160, height_mm=92, nrows=2, ncols=2)
    ax = axs[0, 0]; x = np.linspace(0, 5, 600)
    for lam, c in [(0.5, BLUE), (1, GREEN), (2, PURPLE)]:
        ax.plot(x, lam*np.exp(-lam*x), color=c, label=rf'$\lambda={lam:g}$')
    ax.set(title='(a) 指数分布', xlim=(0, 5), ylim=(0, 2.1), xlabel=r'$x$')
    ax = axs[0, 1]; x = np.linspace(-6, 6, 800)
    for mu, s, c, ls in [(0, 1, BLUE, '-'), (1.5, 0.5, GREEN, '-'), (0, 2, PURPLE, '--')]:
        ax.plot(x, np.exp(-(x-mu)**2/(2*s*s))/sqrt(2*np.pi*s*s), color=c, ls=ls, label=rf'$\mu={mu:g},\ \sigma={s:g}$')
    ax.set(title='(b) 高斯分布', xlim=(-6, 6), ylim=(0, 0.95), xlabel=r'$x$')
    ax = axs[1, 0]; x = np.linspace(0.005, 10, 1200)
    for a, c, ls in [(0.5, RED, '-'), (1, BLUE, '-'), (2, GREEN, '-'), (5, PURPLE, '--')]:
        ax.plot(x, x**(a-1)*np.exp(-x)/gamma(a), color=c, ls=ls, label=rf'$\alpha={a:g}$')
    ax.set(title='(c) Gamma 分布，率 β=1', xlim=(0, 10), ylim=(0, 1.1), xlabel=r'$x$')
    ax = axs[1, 1]; x = np.linspace(0.002, 0.998, 1200)
    for a, b, c, ls in [(1, 1, MUTED, ':'), (2, 2, BLUE, '-'), (2, 5, GREEN, '-'), (5, 2, PURPLE, '--'), (0.5, 0.5, RED, '-')]:
        B = exp(lgamma(a)+lgamma(b)-lgamma(a+b))
        ax.plot(x, x**(a-1)*(1-x)**(b-1)/B, color=c, ls=ls, label=rf'$a={a:g},\ b={b:g}$')
    ax.set(title='(d) Beta 分布', xlim=(0, 1), ylim=(0, 5.0), xlabel=r'$x$')
    axs[0, 0].legend(loc='upper right', handlelength=1.6)
    axs[0, 1].legend(loc='upper left', handlelength=1.6)
    axs[1, 0].legend(loc='upper right', handlelength=1.6)
    axs[1, 1].legend(loc='upper center', ncol=2, handlelength=1.6, columnspacing=1.0)
    for ax in axs[:, 0]:
        ax.set_ylabel('密度')
    save(fig, D/'prob-continuous-densities', 'figure', {
        'exponential_rates': [0.5, 1, 2], 'gaussian_mu_sigma': [[0, 1], [1.5, 0.5], [0, 2]],
        'gamma_shape_rate1': [0.5, 1, 2, 5], 'gamma_note': 'alpha=0.5 density unbounded near 0, clipped at 1.1',
        'beta_ab': [[1, 1], [2, 2], [2, 5], [5, 2], [0.5, 0.5]], 'beta_note': 'a=b=0.5 clipped at 5'})


def prob_square_transform():
    fig, axs = figure(width_mm=160, height_mm=54, ncols=2)
    ax = axs[0]
    x = np.linspace(-1.3, 2.3, 600)
    ax.plot(x, x**2, color=INK, lw=1.1)
    ax.axvspan(-1, 2, color=BLUE_FILL, lw=0, zorder=0)
    for y0, c, yb in [(0.49, GREEN, 0.0), (2.25, PURPLE, -0.16)]:
        r = sqrt(y0); left = max(-r, -1)
        ax.axhline(y0, color=c, lw=.6, ls='--')
        ax.plot([left, r], [yb, yb], color=c, lw=3, solid_capstyle='butt', zorder=3)
        for xx in ([-r, r] if r <= 1 else [r]):
            ax.plot([xx, xx], [0, y0], color=c, lw=.6, ls=':')
    ax.text(-1.25, 0.66, r'$y=0.49$', color=GREEN, fontsize=7.5)
    ax.text(-1.25, 2.42, r'$y=2.25$', color=PURPLE, fontsize=7.5)
    ax.set(xlim=(-1.3, 2.3), ylim=(-0.3, 4.4), xticks=[-1, -0.7, 0, 0.7, 1, 1.5, 2], xticklabels=['-1', '-0.7', '0', '0.7', '1', '1.5', '2'], yticks=[0, 1, 2, 3, 4],
           xlabel=r'$x$', ylabel=r'$y=x^2$', title='(a) 事件的逆像')
    ax = axs[1]
    y1 = np.linspace(0.01, 1, 400, endpoint=False); y2 = np.linspace(1, 4, 400)
    ax.fill_between(y1, 0, 1/(3*np.sqrt(y1)), color=BLUE_FILL, lw=0)
    ax.fill_between(y2, 0, 1/(6*np.sqrt(y2)), color=BLUE_FILL, lw=0)
    ax.plot(y1, 1/(3*np.sqrt(y1)), color=BLUE, label='两支相加')
    ax.plot(y2, 1/(6*np.sqrt(y2)), color=BLUE)
    yy = np.linspace(0.01, 4, 600)
    ax.plot(yy, 1/(6*np.sqrt(yy)), color=RED, ls='--', label='漏掉负支')
    ax.plot([1], [1/3], 'o', mfc='white', mec=BLUE, ms=3)
    ax.set(xlim=(0, 4.2), ylim=(0, 1.6), xticks=[0, 1, 2, 3, 4], xlabel=r'$y$', ylabel=r'$f_Y(y)$', title='(b) 平方后的密度')
    ax.legend(loc='upper right')
    save(fig, D/'prob-square-transform', 'figure', {
        'input': 'X ~ U(-1,2)', 'map': 'Y=X^2, support [0,4)',
        'density': '1/(3 sqrt y) on (0,1); 1/(6 sqrt y) on (1,4)', 'masses': {'(0,1)': 2/3, '(1,4)': 1/3},
        'wrong_one_branch': '1/(6 sqrt y) on (0,4), total mass 2/3',
        'panel_a_levels': {'0.49': 'two preimages [-0.7,0.7]', '2.25': 'one preimage branch, X in [-1,1.5]'}})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    prob_cdf_three_types, prob_pmf_cdf, prob_density_above_one, prob_quantile_inverse,
    prob_skewed_locations, prob_discrete_pmfs, prob_binomial_poisson, prob_continuous_densities,
    prob_square_transform]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
