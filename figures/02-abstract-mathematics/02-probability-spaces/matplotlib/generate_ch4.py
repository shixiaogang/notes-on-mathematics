# coding: utf-8
"""Teaching charts for volume two, part "probability spaces", chapter 4
(weak convergence, tightness and limit theorems).

Analytic curves come from closed-form expressions or scipy.stats formulas listed in
the saved facts; every simulation uses a fixed numpy seed recorded with its
sample sizes and parameters.
Run from any directory:
  python figures/02-abstract-mathematics/02-probability-spaces/matplotlib/generate_ch4.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from scipy import stats, special

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL

D = Path(__file__).resolve().parent
SEED = 20261029


def step_cdf(ax, jumps, masses, xlim, color, lw=1.1, label=None, dots=True, ls='-'):
    """Draw a right-continuous step distribution function with closed/open endpoint dots."""
    jumps = np.asarray(jumps, float)
    order = np.argsort(jumps)
    jumps, masses = jumps[order], np.asarray(masses, float)[order]
    levels = np.r_[0, np.cumsum(masses)]
    xs = np.r_[xlim[0], jumps, xlim[1]]
    for j in range(len(levels)):
        ax.plot([xs[j], xs[j + 1]], [levels[j], levels[j]], color=color, lw=lw, ls=ls,
                label=label if j == 0 else None, solid_capstyle='butt')
    if dots:
        for j, x in enumerate(jumps):
            if xlim[0] < x < xlim[1]:
                ax.plot(x, levels[j + 1], 'o', color=color, ms=2.6)
                ax.plot(x, levels[j], 'o', color=color, ms=2.6, mfc='white', mew=.7)


def wlim_point_mass_cdf():
    """Distribution functions of delta_{1/n} and delta_0; convergence fails only at 0."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    ax = axes[0]
    xl = (-0.6, 1.4)
    for n, col in [(1, YELLOW), (2, GREEN), (4, BLUE)]:
        step_cdf(ax, [1 / n], [1], xl, col, label=rf'$n={n}$')
    step_cdf(ax, [0], [1], xl, INK, lw=.9, ls='--', label=r'$F$')
    ax.set(xlim=xl, ylim=(-0.08, 1.12), xlabel=r'$x$', ylabel=r'$F_n(x)$')
    ax.set_title('(a) 点质量的分布函数')
    ax.legend(loc='center right', handlelength=1.5)
    ax = axes[1]
    n = np.arange(1, 21)
    for x0, col, mk in [(0.0, RED, 'o'), (0.25, BLUE, 's')]:
        ax.plot(n, (1 / n <= x0).astype(float), mk, color=col, ms=2.6, label=rf'$x={x0:g}$')
        ax.axhline(float(x0 >= 0), color=col, lw=.6, ls=':')
    ax.set(xlim=(0, 21), ylim=(-0.08, 1.12), xlabel=r'$n$', ylabel=r'$F_n(x)$')
    ax.set_title('(b) 固定阈值处的数列')
    ax.legend(loc='center right', handlelength=1.0)
    save(fig, D/'wlim-point-mass-cdf', 'figure', {
        'P_n': 'delta_{1/n}', 'P': 'delta_0', 'panel_a_n': [1, 2, 4],
        'panel_b_thresholds': [0, 0.25], 'F_n(0)': 0, 'F(0)': 1,
        'F_n(0.25)_becomes_1_from_n': 4})


def wlim_halfline_sandwich():
    """Continuous ramps h_- <= 1_{(-inf,x]} <= h_+ and the resulting bracket F(x-d), F(x+d)."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    ax = axes[0]
    x0, d = 0.0, 0.5
    x = np.linspace(-1.5, 1.5, 601)
    hminus = np.clip((x0 - x) / d, 0, 1)
    hplus = np.clip((x0 + d - x) / d, 0, 1)
    ax.plot(x, hplus + 0.015, color=BLUE, label=r'$h_+$')
    ax.plot(x, hminus - 0.015, color=GREEN, label=r'$h_-$')
    ax.plot([-1.5, x0], [1, 1], color=INK, lw=.9, ls='--', label='示性函数')
    ax.plot([x0, 1.5], [0, 0], color=INK, lw=.9, ls='--')
    ax.axvspan(x0 - d, x0, color=GREEN_FILL, lw=0)
    ax.axvspan(x0, x0 + d, color=BLUE_FILL, lw=0)
    ax.set_xticks([x0 - d, x0, x0 + d])
    ax.set_xticklabels([r'$x-\delta$', r'$x$', r'$x+\delta$'])
    ax.set(xlim=(-1.5, 1.5), ylim=(-0.1, 1.15), ylabel='函数值')
    ax.set_title('(a) 两侧的连续夹逼')
    ax.legend(loc='lower left', handlelength=1.5)
    ax = axes[1]
    xs, delta = 0.5, np.linspace(0.005, 1.0, 300)
    ax.plot(delta, stats.norm.cdf(xs + delta), color=BLUE, label=r'$F(x+\delta)$')
    ax.plot(delta, stats.norm.cdf(xs - delta), color=GREEN, label=r'$F(x-\delta)$')
    ax.axhline(stats.norm.cdf(xs), color=INK, lw=.8, ls='--', label=r'$F(x)$')
    ax.fill_between(delta, stats.norm.cdf(xs - delta), stats.norm.cdf(xs + delta), color=YELLOW_FILL, lw=0)
    ax.set(xlim=(0, 1), ylim=(0.25, 1.0), xlabel=r'$\delta$', ylabel='概率')
    ax.set_title('(b) 上下界随间距收拢')
    ax.legend(loc='lower left', handlelength=1.5)
    save(fig, D/'wlim-halfline-sandwich', 'figure', {
        'panel_a_x': x0, 'panel_a_delta': d, 'panel_b_F': 'standard normal cdf',
        'panel_b_x': xs, 'F(x)': float(stats.norm.cdf(xs))})


def wlim_closed_set_portmanteau():
    """Distance ramps decreasing to the indicator of a closed set; strict Portmanteau inequalities."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    ax = axes[0]
    x = np.linspace(-2.5, 3.2, 1141)
    dist = np.maximum.reduce([np.zeros_like(x), -1 - x, x])
    for k, col in [(1, YELLOW), (2, GREEN), (4, BLUE), (16, PURPLE)]:
        ax.plot(x, np.maximum(0, 1 - k * dist), color=col, label=rf'$k={k}$')
    ax.fill_between([-1, 0], [0, 0], [1, 1], color=BLUE_FILL, lw=0)
    ax.text(-0.5, 0.45, r'$F$', ha='center', color=INK)
    ax.set(xlim=(-2.5, 3.2), ylim=(-0.05, 1.12), xlabel=r'$x$', ylabel=r'$h_k(x)$')
    ax.set_title('(a) 距离函数逼近闭集')
    ax.legend(loc='upper right', handlelength=1.3)
    ax = axes[1]
    n = np.arange(1, 16)
    ax.plot(n, np.zeros_like(n, dtype=float), 'o', color=BLUE, ms=2.8, label='闭集概率')
    ax.plot(n, np.ones_like(n, dtype=float), 's', color=GREEN, ms=2.6, label='开集概率')
    ax.axhline(1, color=BLUE, lw=.7, ls='--')
    ax.axhline(0, color=GREEN, lw=.7, ls='--')
    ax.text(15.5, 0.9, r'$P(F)=1$', ha='right', va='top', color=BLUE, fontsize=7.5)
    ax.text(15.5, 0.1, r'$P(G)=0$', ha='right', va='bottom', color=GREEN, fontsize=7.5)
    ax.set(xlim=(0, 16), ylim=(-0.12, 1.15), xlabel=r'$n$', ylabel='概率')
    ax.set_title('(b) 移动点质量的开闭集')
    ax.legend(loc='center left', handlelength=1.0)
    save(fig, D/'wlim-closed-set-portmanteau', 'figure', {
        'panel_a_closed_set': '[-1,0]', 'h_k': 'max(0, 1-k d(x,F))', 'k': [1, 2, 4, 16],
        'panel_b_P_n': 'delta_{1/n}', 'closed_set': '(-inf,0]', 'open_set': '(0,inf)',
        'P_n(F)': 0, 'P(F)': 1, 'P_n(G)': 1, 'P(G)': 0})


def wlim_spike_mean():
    """Spike distributions converge weakly to delta_0 while their means stay at one."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    ax = axes[0]
    for n, col, off in [(10, BLUE, -0.5), (40, RED, 0.5)]:
        ax.vlines([off, n], 0, [1 - 1 / n, 1 / n], color=col, lw=1.4, label=rf'$n={n}$')
        ax.plot([off, n], [1 - 1 / n, 1 / n], 'o', color=col, ms=2.6)
    ax.text(10, 0.16, r'$0.1$', ha='center', color=BLUE, fontsize=7.5)
    ax.text(40, 0.09, r'$0.025$', ha='center', color=RED, fontsize=7.5)
    ax.set(xlim=(-3, 45), ylim=(0, 1.08), xlabel=r'$x$', ylabel='点质量')
    ax.set_title('(a) 尖峰分布')
    ax.legend(loc='upper right', handlelength=1.0)
    ax = axes[1]
    n = np.arange(1, 81)
    ax.plot(n, np.ones_like(n, dtype=float), color=RED, label='均值')
    for M, col in [(5, BLUE), (20, GREEN)]:
        trunc = np.minimum(n, M) / n
        ax.plot(n, trunc, color=col, label=rf'$M={M}$')
    ax.axhline(0, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(0, 80), ylim=(-0.05, 1.15), xlabel=r'$n$', ylabel='积分值')
    ax.set_title('(b) 截断均值与均值')
    ax.legend(loc='center right', handlelength=1.4)
    save(fig, D/'wlim-spike-mean', 'figure', {
        'P_n': '(1-1/n) delta_0 + (1/n) delta_n', 'mean': 1,
        'truncated_mean': 'int min(x,M) dP_n = min(n,M)/n', 'M': [5, 20]})


def wlim_escape_tight():
    """Uniform tail function sup_n P_n(|x|>R) for escaping and tight families."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    ax = axes[0]
    R = np.linspace(0, 8, 801)
    ax.plot(R, np.ones_like(R), color=RED, label=r'$\delta_n$')
    ax.plot(R, 1 / (np.floor(R) + 1), color=YELLOW, label='尖峰分布')
    ax.plot(R, 2 * stats.norm.sf(R / np.sqrt(2)), color=BLUE, label='方差不超过2的正态')
    ax.set(xlim=(0, 8), ylim=(-0.03, 1.08), xlabel=r'$R$', ylabel='族内最大外部概率')
    ax.set_title('(a) 外部质量的一致上界')
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, 0.93), handlelength=1.4)
    ax = axes[1]
    Rw = 3
    ax.axvspan(-Rw, Rw, color=BLUE_FILL, lw=0)
    for n in range(1, 9):
        col = BLUE if n <= Rw else RED
        ax.vlines(n, 0, 1, color=col, lw=1.2)
        ax.plot(n, 1, 'o', color=col, ms=2.6)
    ax.text(0, 1.08, r'$[-R,R]$', ha='center', color=BLUE, fontsize=7.5)
    ax.set(xlim=(-4, 9), ylim=(0, 1.2), xlabel=r'$x$', ylabel='点质量')
    ax.set_xticks([-3, 0, 3, 6, 9])
    ax.set_title('(b) 逃离固定窗口的点质量')
    save(fig, D/'wlim-escape-tight', 'figure', {
        'families': {'delta_n': 'sup tail = 1 for every R',
                     'spike (1-1/n)delta_0+(1/n)delta_n': 'sup tail = 1/(floor(R)+1)',
                     'N(0,1+1/n)': 'sup tail = P(|N(0,2)|>R)'},
        'panel_b_R': Rw})


def wlim_helly_selection():
    """Helly selection: a proper subsequential limit, a defective one, and two limits for delta_{+-1}."""
    fig, axes = figure(width_mm=150, height_mm=48, ncols=3)
    x = np.linspace(-4, 4, 801)
    ax = axes[0]
    means = np.sin(np.arange(1, 400))
    for n in range(1, 31):
        ax.plot(x, stats.norm.cdf(x - means[n - 1]), color=GRID, lw=.6)
    picks, tol = [], 0.5
    for n in range(1, 400):
        if abs(means[n - 1] - 0.5) < tol and len(picks) < 4:
            picks.append(n); tol /= 3
    for n, col in zip(picks, [YELLOW, GREEN, BLUE, PURPLE]):
        ax.plot(x, stats.norm.cdf(x - means[n - 1]), color=col, lw=.9, label=rf'$n={n}$')
    ax.plot(x, stats.norm.cdf(x - 0.5), color=INK, lw=.9, ls='--', label=r'$G$')
    ax.set(xlim=(-4, 4), ylim=(-0.03, 1.05), xlabel=r'$x$', ylabel=r'$F_n(x)$')
    ax.set_title('(a) 选出的收敛子列')
    ax.legend(loc='upper left', handlelength=1.3, fontsize=7)
    ax = axes[1]
    xb = np.linspace(-4, 12, 1601)
    for n, col in [(2, YELLOW), (5, GREEN), (10, BLUE)]:
        ax.plot(xb, 0.5 * stats.norm.cdf(xb) + 0.5 * (xb >= n), color=col, lw=.9, label=rf'$n={n}$')
    ax.plot(xb, 0.5 * stats.norm.cdf(xb), color=INK, lw=.9, ls='--', label=r'$G$')
    ax.axhline(1, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(-4, 12), ylim=(-0.03, 1.05), xlabel=r'$x$')
    ax.set_title('(b) 质量逃逸后的亏损极限')
    ax.legend(loc='upper left', handlelength=1.3, fontsize=7)
    ax = axes[2]
    xl = (-2.5, 2.5)
    step_cdf(ax, [1], [1], xl, BLUE, label='偶数项')
    step_cdf(ax, [-1], [1], xl, RED, ls='--', label='奇数项')
    ax.set(xlim=xl, ylim=(-0.08, 1.12), xlabel=r'$x$')
    ax.set_title('(c) 两个不同的子列极限')
    ax.legend(loc='center right', handlelength=1.5)
    save(fig, D/'wlim-helly-selection', 'figure', {
        'panel_a': 'P_n = N(sin n, 1), n=1..30 in grey; highlighted n with |sin n - 0.5| below 0.5/3^j',
        'panel_a_highlighted_n': picks, 'panel_a_highlighted_means': [float(means[n - 1]) for n in picks],
        'panel_b': 'P_n = 0.5 N(0,1) + 0.5 delta_n; limit G = 0.5 Phi with G(+inf)=0.5',
        'panel_c': 'P_n = delta_{(-1)^n}'})


def wlim_characteristic_functions():
    """Characteristic functions of symmetric laws and of Bernoulli(0.3)."""
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    t = np.linspace(-12, 12, 1201)
    ax.plot(t, np.cos(t), color=YELLOW, label='Rademacher')
    ax.plot(t, np.sinc(t / np.pi), color=GREEN, label=r'$\mathrm{Unif}[-1,1]$')
    ax.plot(t, np.exp(-t**2 / 2), color=BLUE, label=r'$N(0,1)$')
    ax.axhline(0, color=MUTED, lw=.5)
    ax.set(xlim=(-12, 12), ylim=(-1.1, 1.75), xlabel=r'$t$', ylabel=r'$\varphi(t)$')
    ax.set_title('(a) 对称分布')
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.legend(loc='upper center', handlelength=1.0, ncol=3, fontsize=6.8, columnspacing=0.7)
    ax = axes[1]
    p = 0.3
    t = np.linspace(-2 * np.pi, 2 * np.pi, 1201)
    phi = 1 - p + p * np.exp(1j * t)
    ax.plot(t, phi.real, color=BLUE, label='实部')
    ax.plot(t, phi.imag, color=RED, label='虚部')
    ax.plot(t, np.abs(phi), color=INK, lw=.9, ls='--', label='模')
    ax.axhline(0, color=MUTED, lw=.5)
    ax.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    ax.set_xticklabels([r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
    ax.set(xlim=(-2 * np.pi, 2 * np.pi), ylim=(-0.5, 1.35), xlabel=r'$t$')
    ax.set_title('(b) Bernoulli(0.3)')
    ax.legend(loc='upper right', handlelength=1.3, ncol=3, fontsize=7)
    save(fig, D/'wlim-characteristic-functions', 'figure', {
        'panel_a': {'Rademacher': 'cos t', 'Unif[-1,1]': 'sin t / t', 'N(0,1)': 'exp(-t^2/2)'},
        'panel_b': '1-p+p e^{it}, p=0.3', 'min_modulus': abs(1 - 2 * p)})


def dirichlet_S(y):
    return special.sici(y)[0]


def wlim_inversion_atom():
    """Truncated inversion kernel and integrals for Bernoulli(0.3)."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    ax = axes[0]
    a, b = 0.0, 1.0
    x = np.linspace(-1, 2, 1501)
    for T, col in [(10, YELLOW), (40, BLUE)]:
        J = (dirichlet_S(T * (x - a)) - dirichlet_S(T * (x - b))) / np.pi
        ax.plot(x, J, color=col, lw=.9, label=rf'$T={T}$')
    ax.plot([a, b], [0.5, 0.5], 'o', color=RED, ms=3, zorder=5)
    ax.set_xticks([-1, 0, 1, 2])
    ax.set(xlim=(-1, 2), ylim=(-0.15, 1.2), xlabel=r'$x$', ylabel=r'$J_T(x)$')
    ax.set_title('(a) 区间 (0,1) 的截断核')
    ax.legend(loc='upper right', handlelength=1.3)
    ax = axes[1]
    p = 0.3
    T = np.linspace(0.5, 60, 1200)
    facts = {}
    for (lo, hi), col, lim in [((0, 1), BLUE, 0.5), ((-0.5, 0.5), GREEN, 0.7), ((0, 2), RED, 0.65)]:
        def J(xx):
            return (dirichlet_S(T * (xx - lo)) - dirichlet_S(T * (xx - hi))) / np.pi
        I = (1 - p) * J(0.0) + p * J(1.0)
        ax.plot(T, I, color=col, lw=.9, label=f'({lo:g}, {hi:g})')
        ax.axhline(lim, color=col, lw=.6, ls='--')
        facts[f'({lo},{hi})'] = {'limit': lim, 'I_T_at_T=60': float(I[-1])}
    ax.set(xlim=(0, 60), ylim=(0.2, 0.95), xlabel=r'$T$', ylabel=r'$I_T$')
    ax.set_title('(b) Bernoulli(0.3) 的反演积分')
    ax.legend(loc='lower right', handlelength=1.3, ncol=1, fontsize=7)
    save(fig, D/'wlim-inversion-atom', 'figure', {
        'kernel': 'J_T(x) = (S(T(x-a)) - S(T(x-b)))/pi, S = sine integral',
        'panel_a_interval': [a, b], 'panel_b_law': 'Bernoulli(0.3) on {0,1}', 'panel_b': facts})


def wlim_levy_counterexample():
    """N(0,n): characteristic functions tend to the indicator of t=0; cdfs flatten to 1/2."""
    fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
    t = np.linspace(-3, 3, 1201)
    x = np.linspace(-10, 10, 801)
    cols = [YELLOW, GREEN, BLUE, PURPLE]
    for n, col in zip([1, 4, 16, 64], cols):
        axes[0].plot(t, np.exp(-n * t**2 / 2), color=col, lw=.9, label=rf'$n={n}$')
        axes[1].plot(x, stats.norm.cdf(x / np.sqrt(n)), color=col, lw=.9, label=rf'$n={n}$')
    axes[0].plot(0, 1, 'o', color=RED, ms=3)
    axes[0].set(xlim=(-3, 3), ylim=(-0.05, 1.1), xlabel=r'$t$', ylabel=r'$\varphi_n(t)$')
    axes[0].set_title('(a) 特征函数')
    axes[0].legend(loc='upper right', handlelength=1.3, fontsize=7)
    axes[1].axhline(0.5, color=INK, lw=.8, ls='--')
    axes[1].set(xlim=(-10, 10), ylim=(-0.03, 1.05), xlabel=r'$x$', ylabel=r'$F_n(x)$')
    axes[1].set_title('(b) 分布函数')
    axes[1].legend(loc='upper left', handlelength=1.3, fontsize=7)
    save(fig, D/'wlim-levy-counterexample', 'figure', {
        'P_n': 'N(0,n)', 'phi_n': 'exp(-n t^2/2)', 'pointwise_limit': '1 at t=0, 0 elsewhere',
        'cdf_limit': 0.5, 'n': [1, 4, 16, 64]})


def wlim_studentized_shift():
    """Studentized means of Exp(1) samples; a 1/sqrt(n) shift is a unit shift on the sqrt(n) scale."""
    rng = np.random.default_rng(SEED)
    reps = 20000
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    z = np.linspace(-4, 3, 701)
    ax.plot(z, stats.norm.cdf(z), color=INK, lw=.9, ls='--', label=r'$\Phi$')
    facts = {'seed': SEED, 'population': 'Exponential(1)', 'repetitions': reps}
    for n, col in [(5, RED), (20, YELLOW), (100, BLUE)]:
        s = rng.exponential(1.0, size=(reps, n))
        tstat = np.sqrt(n) * (s.mean(axis=1) - 1) / s.std(axis=1, ddof=1)
        ts = np.sort(tstat)
        ax.plot(ts, np.arange(1, reps + 1) / reps, color=col, lw=.9, label=rf'$n={n}$')
        ecdf = np.searchsorted(ts, z, side='right') / reps
        facts[f'n={n}'] = {'sup_abs_diff_on_grid': float(np.max(np.abs(ecdf - stats.norm.cdf(z))))}
    ax.set(xlim=(-4, 3), ylim=(-0.02, 1.02), xlabel=r'$x$', ylabel='累积概率')
    ax.set_title('(a) 学生化均值')
    ax.legend(loc='upper left', handlelength=1.3, fontsize=7)
    ax = axes[1]
    n = 100
    s = rng.exponential(1.0, size=(reps, n))
    Tn = np.sqrt(n) * (s.mean(axis=1) - 1)
    Tt = np.sqrt(n) * (s.mean(axis=1) + 1 / np.sqrt(n) - 1)
    for arr, col, lab in [(Tn, BLUE, '原统计量'), (Tt, RED, '平移后')]:
        a = np.sort(arr)
        ax.plot(a, np.arange(1, reps + 1) / reps, color=col, lw=.9, label=lab)
    ax.plot(z, stats.norm.cdf(z), color=INK, lw=.7, ls='--')
    ax.plot(z, stats.norm.cdf(z - 1), color=INK, lw=.7, ls=':')
    ax.set(xlim=(-4, 4), ylim=(-0.02, 1.02), xlabel=r'$x$')
    ax.set_title('(b) 放大尺度上的平移')
    ax.legend(loc='upper left', handlelength=1.3, fontsize=7)
    facts['panel_b'] = {'n': n, 'shift_original_scale': 1 / np.sqrt(n), 'shift_sqrt_n_scale': 1.0,
                        'mean_Tn': float(Tn.mean()), 'mean_shifted': float(Tt.mean())}
    save(fig, D/'wlim-studentized-shift', 'figure', facts)


def wlim_clt_convergence():
    """Exact cdfs of standardized Exp(1) sums, Kolmogorov distances, and characteristic functions."""
    fig, axes = figure(width_mm=150, height_mm=50, ncols=3)
    ax = axes[0]
    z = np.linspace(-3.5, 3.5, 701)
    ax.plot(z, stats.norm.cdf(z), color=INK, lw=.9, ls='--', label=r'$\Phi$')
    for n, col in [(1, RED), (4, YELLOW), (16, GREEN), (64, BLUE)]:
        ax.plot(z, stats.gamma.cdf(n + z * np.sqrt(n), a=n), color=col, lw=.9, label=rf'$n={n}$')
    ax.set(xlim=(-3.5, 3.5), ylim=(-0.02, 1.02), xlabel=r'$x$', ylabel='累积概率')
    ax.set_title('(a) 指数和的分布函数')
    ax.legend(loc='upper left', handlelength=1.3, fontsize=7)
    ax = axes[1]
    ns = np.unique(np.round(np.logspace(0, 3, 25)).astype(int))
    zz = np.linspace(-8, 8, 16001)
    dexp, dber = [], []
    for n in ns:
        dexp.append(np.max(np.abs(stats.gamma.cdf(n + zz * np.sqrt(n), a=n) - stats.norm.cdf(zz))))
        p = 0.2
        k = np.arange(n + 1)
        F = stats.binom.cdf(k, n, p)
        xk = (k - n * p) / np.sqrt(n * p * (1 - p))
        # sup over x of |F_n(x)-Phi(x)| attained at jump points (left or right limits)
        Fl = np.r_[0, F[:-1]]
        dber.append(np.max(np.maximum(np.abs(F - stats.norm.cdf(xk)), np.abs(Fl - stats.norm.cdf(xk)))))
    ax.loglog(ns, dexp, 'o', color=BLUE, ms=2.4, label='指数')
    ax.loglog(ns, dber, 's', color=RED, ms=2.2, mfc='white', label='Bernoulli(0.2)')
    ax.loglog(ns, 0.2 / np.sqrt(ns), color=MUTED, lw=.6, ls=':')
    ax.set(xlabel=r'$n$', ylabel='最大分布函数差')
    ax.set_title('(b) 分布函数的最大偏差')
    ax.legend(loc='lower left', handlelength=1.0, fontsize=7)
    ax = axes[2]
    t = np.linspace(-5, 5, 1001)
    ax.plot(t, np.exp(-t**2 / 2), color=INK, lw=.9, ls='--', label=r'$e^{-t^2/2}$')
    for n, col in [(1, RED), (4, YELLOW), (16, GREEN), (64, BLUE)]:
        u = t / np.sqrt(n)
        phi = (np.exp(-1j * u) / (1 - 1j * u))**n
        ax.plot(t, phi.real, color=col, lw=.9, label=rf'$n={n}$')
    ax.set(xlim=(-5, 5), ylim=(-0.45, 1.1), xlabel=r'$t$', ylabel='实部')
    ax.set_title('(c) 标准化和的特征函数')
    ax.legend(loc='upper left', handlelength=1.3, fontsize=6.8)
    save(fig, D/'wlim-clt-convergence', 'figure', {
        'panel_a': 'T_n = (S_n - n)/sqrt(n), S_n ~ Gamma(n,1) for Exp(1) summands',
        'panel_b_n': ns.tolist(), 'panel_b_exp': [float(v) for v in dexp], 'panel_b_bernoulli_0.2': [float(v) for v in dber],
        'panel_b_reference': '0.2/sqrt(n)',
        'panel_c': 'Re [phi_Y(t/sqrt n)]^n, phi_Y(u) = exp(-iu)/(1-iu) for Y = Exp(1)-1'})


def wlim_lindeberg_triangular():
    """Unequal weights k versus one dominant summand: variance shares and row-sum distributions."""
    rng = np.random.default_rng(SEED)
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    n = np.arange(2, 401)
    sA = n * (n + 1) * (2 * n + 1) / 6
    ax.plot(n, n**2 / sA, color=BLUE, label='权重随序号增长')
    ax.plot(n, np.full_like(n, 0.8, dtype=float), color=RED, label='首项占五分之四')
    ax.set(xlim=(0, 400), ylim=(0, 1.0), xlabel=r'$n$', ylabel='最大方差占比')
    ax.set_title('(a) 单项方差占比')
    ax.legend(loc='center right', handlelength=1.3, fontsize=7)
    ax = axes[1]
    m, reps = 200, 20000
    R = rng.choice([-1.0, 1.0], size=(reps, m))
    w = np.arange(1, m + 1)
    TA = R @ w / np.sqrt((w**2).sum())
    TB = (2 * R[:, 0] + R[:, 1:].sum(axis=1) / np.sqrt(m - 1)) / np.sqrt(5)
    z = np.linspace(-3.5, 3.5, 701)
    bins = np.linspace(-3.5, 3.5, 57)
    for arr, col, lab in [(TA, BLUE, '递增权重'), (TB, RED, '主导首项')]:
        ax.hist(arr, bins=bins, density=True, histtype='step', color=col, lw=.8, label=lab)
    ax.plot(z, stats.norm.pdf(z), color=INK, lw=.8, ls='--', label=r'$N(0,1)$')
    sd = 1 / np.sqrt(5)
    mix = 0.5 * stats.norm.pdf(z, 2 / np.sqrt(5), sd) + 0.5 * stats.norm.pdf(z, -2 / np.sqrt(5), sd)
    ax.plot(z, mix, color=RED, lw=.8)
    ax.set(xlim=(-3.5, 3.5), ylim=(0, 0.75), xlabel=r'$x$', ylabel='密度')
    ax.set_title('(b) 行和的分布')
    ax.legend(loc='upper left', handlelength=1.3, fontsize=7)
    save(fig, D/'wlim-lindeberg-triangular', 'figure', {
        'seed': SEED, 'scheme_A': 'X_{n,k} = k R_k, R_k Rademacher, s_n^2 = n(n+1)(2n+1)/6',
        'scheme_B': 'X_{n,1} = 2 sqrt(n-1) R_1, X_{n,k} = R_k for k>=2, s_n^2 = 5(n-1), first share 4/5',
        'scheme_B_limit': '(2R + N(0,1))/sqrt 5: mixture 0.5 N(+-2/sqrt5, 1/5)',
        'n_panel_b': m, 'repetitions': reps,
        'scheme_A_share_n=200': float(200**2 / (200 * 201 * 401 / 6))})


def ellipse(Sigma, q=stats.chi2.ppf(0.95, 2), num=400):
    vals, vecs = np.linalg.eigh(Sigma)
    th = np.linspace(0, 2 * np.pi, num)
    circ = np.vstack([np.cos(th), np.sin(th)])
    return vecs @ (np.sqrt(np.maximum(vals, 0) * q)[:, None] * circ)


def wlim_clt_vector():
    """Bivariate CLT for (xi, xi^2), projections, and a singular covariance."""
    rng = np.random.default_rng(SEED)
    n, reps = 200, 1500
    fig, axes = figure(width_mm=150, height_mm=52, ncols=3)
    xi = rng.exponential(1.0, size=(reps, n))
    W = np.sqrt(n) * np.stack([xi.mean(axis=1) - 1, (xi**2).mean(axis=1) - 2], axis=1)
    Sigma = np.array([[1.0, 4.0], [4.0, 20.0]])
    ax = axes[0]
    ax.scatter(W[:, 0], W[:, 1], s=1.5, color=BLUE, alpha=1, lw=0)
    e = ellipse(Sigma)
    ax.plot(e[0], e[1], color=INK, lw=.9)
    ax.set(xlim=(-4, 4), ylim=(-16, 22), xlabel=r'$W_1$', ylabel=r'$W_2$')
    ax.set_title('(a) 均值与二阶矩的联合波动')
    ax = axes[1]
    facts = {}
    dirs = [((1.0, 0.0), BLUE), ((1.0, -0.2), GREEN)]
    for (a1, a2), col in dirs:
        proj = a1 * W[:, 0] + a2 * W[:, 1]
        v = a1**2 * Sigma[0, 0] + 2 * a1 * a2 * Sigma[0, 1] + a2**2 * Sigma[1, 1]
        ax.hist(proj, bins=np.linspace(-4, 4, 41), density=True, histtype='step', color=col, lw=.8)
        g = np.linspace(-4, 4, 401)
        ax.plot(g, stats.norm.pdf(g, scale=np.sqrt(v)), color=col, lw=.9,
                label=rf'$a=({a1:g},{a2:g})$')
        facts[f'a=({a1},{a2})'] = {'limit_variance': float(v), 'sample_variance': float(proj.var())}
    ax.set(xlim=(-4, 4), xlabel=r"$\langle a,W\rangle$", ylabel='密度')
    ax.set_title('(b) 两个方向的投影')
    ax.legend(loc='upper right', handlelength=1.2, fontsize=7)
    ax = axes[2]
    V = np.sqrt(n) * np.stack([xi.mean(axis=1) - 1, -2 * (xi.mean(axis=1) - 1)], axis=1)
    g = np.linspace(-4, 4, 3)
    ax.plot(g, -2 * g, color=MUTED, lw=.5, ls=':', zorder=1)
    ax.scatter(V[:, 0], V[:, 1], s=4, color=GREEN, lw=0, zorder=2)
    ax.set(xlim=(-4, 4), ylim=(-8, 8), xlabel=r'$V_1$', ylabel=r'$V_2$')
    ax.set_title('(c) 奇异协方差')
    save(fig, D/'wlim-clt-vector', 'figure', {
        'seed': SEED, 'n': n, 'repetitions': reps,
        'panel_a': 'W = sqrt(n)(mean(xi)-1, mean(xi^2)-2), xi ~ Exp(1); Sigma = [[1,4],[4,20]]; 95% ellipse of N(0,Sigma)',
        'panel_a_sample_cov': np.cov(W.T).tolist(), 'panel_b': facts,
        'panel_c': 'X_k = (xi_k, 3 - 2 xi_k), Sigma = [[1,-2],[-2,4]], rank 1; points on V_2 = -2 V_1'})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    wlim_point_mass_cdf, wlim_halfline_sandwich, wlim_closed_set_portmanteau, wlim_spike_mean,
    wlim_escape_tight, wlim_helly_selection, wlim_characteristic_functions, wlim_inversion_atom,
    wlim_levy_counterexample, wlim_studentized_shift, wlim_clt_convergence,
    wlim_lindeberg_triangular, wlim_clt_vector]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
