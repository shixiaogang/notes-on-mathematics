# coding: utf-8
"""Teaching charts for volume three, part "processes and trajectory evolution",
chapter 4 (stochastic processes and sample paths).

Analytic curves (moments, covariances, beta-binomial and Dirichlet weights)
come from the formulas recorded in each facts file; every simulation uses a
fixed numpy seed recorded together with sample sizes and parameters.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch4.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from scipy import stats, special
from matplotlib.colors import LinearSegmentedColormap

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import (figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID,
                     BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL)

D = Path(__file__).resolve().parent
SEED = 20261030
HEAT = LinearSegmentedColormap.from_list('book_blue', ['#FFFFFF', BLUE_FILL, BLUE])


def rng(k):
    return np.random.default_rng(SEED + k)


def spp_two_views():
    """Gaussian random walk S_n=sum xi_i, xi_i~N(0,1): paths and two time slices."""
    r = rng(1)
    n_paths, n_steps, t1, t2 = 2000, 40, 10, 30
    steps = r.standard_normal((n_paths, n_steps))
    S = np.concatenate([np.zeros((n_paths, 1)), np.cumsum(steps, axis=1)], axis=1)
    n = np.arange(n_steps + 1)
    fig, axes = figure(width_mm=107, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [2.1, 1]})
    ax = axes[0]
    for i in range(1, 25):
        ax.plot(n, S[i], color=GRID, lw=.6)
    ax.plot(n, S[0], color=BLUE, lw=1.2, label='一条固定路径')
    for t, col in [(t1, GREEN), (t2, YELLOW)]:
        ax.axvline(t, color=col, lw=.9, ls='--')
        ax.plot(np.full(25, t), S[:25, t], 'o', color=col, ms=2.2)
    ax.text(t1 + .6, -15.5, r'$n=10$', color=GREEN, fontsize=7.5)
    ax.text(t2 + .6, -15.5, r'$n=30$', color=YELLOW, fontsize=7.5)
    ax.set(xlim=(0, n_steps), ylim=(-17, 17), xlabel=r'$n$', ylabel=r'$S_n(\omega)$')
    ax.set_title('(a) 横看：一条路径；竖看：一个随机变量')
    ax.legend(loc='upper left', handlelength=1.4)
    ax = axes[1]
    grid = np.linspace(-17, 17, 300)
    for t, col, fill in [(t1, GREEN, GREEN_FILL), (t2, YELLOW, YELLOW_FILL)]:
        ax.hist(S[:, t], bins=np.arange(-17, 17.1, 1.4), orientation='horizontal', density=True,
                color=fill, edgecolor=col, lw=.5)
        ax.plot(stats.norm.pdf(grid, scale=np.sqrt(t)), grid, color=col, lw=1.1, label=rf'$N(0,{t})$')
    ax.set(ylim=(-17, 17), xlabel='密度')
    ax.set_yticklabels([])
    ax.set_title(f'(b) {n_paths} 条路径的竖切片')
    ax.legend(loc='upper right', handlelength=1.2)
    save(fig, D/'spp-two-views', 'figure', {
        'seed': SEED + 1, 'model': 'S_0=0, S_n=sum_{i<=n} xi_i, xi_i iid N(0,1)', 'n_paths': n_paths,
        'gray_paths_shown': 24, 'slices': [t1, t2],
        'empirical_var_at_slices': [round(float(S[:, t1].var()), 3), round(float(S[:, t2].var()), 3)],
        'exact_var_at_slices': [t1, t2], 'histogram_bin_width': 1.4})


def spp_taxonomy():
    """Index (discrete/continuous) x state/path type: four standard examples."""
    r = rng(2)
    fig, axes = figure(width_mm=107, height_mm=72, nrows=2, ncols=2)
    # (a) simple random walk
    ax = axes[0, 0]
    xi = r.choice([-1, 1], size=30)
    S = np.concatenate([[0], np.cumsum(xi)])
    ax.plot(np.arange(31), S, 'o', color=BLUE, ms=2.4)
    ax.vlines(np.arange(31), 0, S, color=GRID, lw=.5)
    ax.set(xlim=(-0.5, 30.5), xlabel=r'$n$', ylabel=r'$S_n$')
    ax.set_title('(a) 离散时间、离散状态')
    # (b) AR(1) real-valued
    ax = axes[0, 1]
    rho, Y = 0.8, [r.standard_normal()]
    for _ in range(30):
        Y.append(rho * Y[-1] + np.sqrt(1 - rho**2) * r.standard_normal())
    ax.plot(np.arange(31), Y, 'o', color=GREEN, ms=2.4)
    ax.plot(np.arange(31), Y, color=GREEN, lw=.4, alpha=1)
    ax.set(xlim=(-0.5, 30.5), xlabel=r'$n$', ylabel=r'$Y_n$')
    ax.set_title('(b) 离散时间、连续状态')
    # (c) Poisson counting path
    ax = axes[1, 0]
    lam, T = 1.0, 10.0
    arr = np.cumsum(r.exponential(1 / lam, size=40))
    arr = arr[arr < T]
    tt = np.concatenate([[0], arr, [T]])
    vals = np.arange(len(arr) + 1)
    for k in range(len(arr) + 1):
        ax.plot([tt[k], tt[k + 1]], [vals[k], vals[k]], color=YELLOW, lw=1.2)
    ax.plot(arr, vals[1:], 'o', color=YELLOW, ms=2.6)
    ax.plot(arr, vals[:-1], 'o', mfc='white', mec=YELLOW, ms=2.6, mew=.7)
    ax.set(xlim=(0, T), xlabel=r'$t$', ylabel=r'$N_t$')
    ax.set_title('(c) 连续时间、跳跃路径')
    # (d) Brownian path
    ax = axes[1, 1]
    m = 4000
    t = np.linspace(0, T, m + 1)
    B = np.concatenate([[0], np.cumsum(r.standard_normal(m) * np.sqrt(T / m))])
    ax.plot(t, B, color=RED, lw=.8)
    ax.set(xlim=(0, T), xlabel=r'$t$', ylabel=r'$B_t$')
    ax.set_title('(d) 连续时间、连续路径')
    save(fig, D/'spp-taxonomy', 'figure', {
        'seed': SEED + 2,
        'a': 'simple symmetric random walk, 30 steps of +-1',
        'b': 'stationary AR(1), rho=0.8, Y_0~N(0,1), innovations N(0,1-rho^2)',
        'c': 'Poisson counting process, rate 1, right-continuous, on [0,10]; filled dot = value at jump time',
        'd': 'Brownian path approximated on 4000 equal steps on [0,10]',
        'arrivals_c': [round(float(a), 3) for a in arr]})


def spp_same_marginals():
    """Three N(0,1)-marginal sequences: iid, AR(1) rho=0.8, shared background rho=0.8."""
    r = rng(3)
    rho, N = 0.8, 60
    n = np.arange(N)

    def iid():
        return r.standard_normal(N)

    def ar():
        y = [r.standard_normal()]
        for _ in range(N - 1):
            y.append(rho * y[-1] + np.sqrt(1 - rho**2) * r.standard_normal())
        return np.array(y)

    def shared():
        return np.sqrt(rho) * r.standard_normal() + np.sqrt(1 - rho) * r.standard_normal(N)

    fig, axes = figure(width_mm=150, height_mm=46, ncols=4, gridspec_kw={'width_ratios': [1, 1, 1, 1.05]})
    cols = [BLUE, GREEN, YELLOW]
    names = ['(a) 独立读数', '(b) AR(1)', '(c) 共享背景']
    for ax, gen, col, title in zip(axes[:3], [iid, ar, shared], cols, names):
        ax.axhspan(-2, 2, color=BLUE_FILL, lw=0)
        for j, shade in enumerate([col, MUTED, INK]):
            ax.plot(n, gen(), color=shade, lw=.8 if j else 1.1, alpha=1)
        ax.set(xlim=(0, N - 1), ylim=(-3.6, 3.6), xlabel=r'$n$')
        ax.set_title(title)
    axes[0].set_ylabel('读数')
    ax = axes[3]
    lags = np.arange(0, 11)
    ax.plot(lags, (lags == 0).astype(float), 'o-', color=BLUE, ms=2.6, lw=.9, label='独立')
    ax.plot(lags, rho**lags, 's-', color=GREEN, ms=2.6, lw=.9, label='AR(1)')
    ax.plot(lags, np.where(lags == 0, 1.0, rho), '^-', color=YELLOW, ms=2.8, lw=.9, label='共享背景')
    ax.set(xlim=(-0.3, 10.3), ylim=(-0.05, 1.08), xlabel=r'$k$', ylabel=r'$\mathrm{Corr}(X_n,X_{n+k})$')
    ax.set_title('(d) 相关随间隔的变化')
    ax.legend(loc='center right', handlelength=1.4)
    m = 100
    var_ar = (m + 2 * sum((m - k) * rho**k for k in range(1, m))) / m**2
    save(fig, D/'spp-same-marginals', 'figure', {
        'seed': SEED + 3, 'rho': rho, 'length': N,
        'iid': 'X_n iid N(0,1)', 'ar1': 'Y_0~N(0,1), Y_{n+1}=rho Y_n + sqrt(1-rho^2) eps',
        'shared': 'Z_n = sqrt(rho) Theta + sqrt(1-rho) eps_n',
        'band': '+-2, the central 95.4 percent of N(0,1)',
        'variance_of_mean_of_100': {'iid': 0.01, 'ar1_exact': round(var_ar, 4), 'shared_exact': rho + (1 - rho) / m}})


def spp_cylinder():
    """Cylinder event {x(t1) in B1, x(t2) in B2, x(t3) in B3} for Gaussian random walk paths."""
    r = rng(4)
    n_paths, N = 60, 30
    S = np.concatenate([np.zeros((n_paths, 1)), np.cumsum(r.standard_normal((n_paths, N)), axis=1)], axis=1)
    gates = [(8, (-1.0, 3.0)), (16, (0.0, 5.0)), (24, (-2.0, 2.0))]
    ok = np.ones(n_paths, bool)
    for t, (lo, hi) in gates:
        ok &= (S[:, t] >= lo) & (S[:, t] <= hi)
    fig, ax = figure(width_mm=100, height_mm=46)
    for i in range(n_paths):
        if not ok[i]:
            ax.plot(np.arange(N + 1), S[i], color=GRID, lw=.6)
    for i in range(n_paths):
        if ok[i]:
            ax.plot(np.arange(N + 1), S[i], color=BLUE, lw=1.0)
    for k, (t, (lo, hi)) in enumerate(gates, 1):
        ax.plot([t, t], [lo, hi], color=RED, lw=2.6, solid_capstyle='butt')
        ax.text(t + .4, hi + .3, rf'$B_{k}$', color=RED, fontsize=7.5)
    ax.set(xlim=(0, N), ylim=(-12, 12), xlabel=r'$n$', ylabel=r'$x(n)$')
    ax.set_xticks([0, 8, 16, 24, 30])
    ax.set_xticklabels(['0', r'$t_1$', r'$t_2$', r'$t_3$', '30'])
    save(fig, D/'spp-cylinder', 'figure', {
        'seed': SEED + 4, 'model': 'Gaussian random walk, N(0,1) steps', 'n_paths': n_paths,
        'gates': [{'time': t, 'interval': list(b)} for t, b in gates], 'paths_in_cylinder': int(ok.sum())})


def spp_stopping_vs_peak():
    """First hitting of level 3 (stopping time) versus time of the overall maximum (not a stopping time)."""
    fig, axes = figure(width_mm=107, height_mm=48, ncols=2)
    # (a) a fixed teaching path of +-1 steps
    steps_a = [1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1]
    S = np.concatenate([[0], np.cumsum(steps_a)])
    tau = int(np.argmax(S >= 3))
    ax = axes[0]
    ax.axhline(3, color=RED, lw=.8, ls='--')
    ax.plot(np.arange(tau + 1), S[:tau + 1], 'o-', color=BLUE, ms=2.4, lw=1.0)
    ax.plot(np.arange(tau, len(S)), S[tau:], 'o-', color=GRID, ms=2.0, lw=.8)
    ax.plot([tau], [S[tau]], 'o', color=RED, ms=4)
    ax.text(tau + .5, 3.35, r'$\tau=%d$' % tau, color=RED, fontsize=7.5)
    ax.text(12.5, 3.35, r'$a=3$', color=RED, fontsize=7.5)
    ax.set(xlim=(0, 20), ylim=(-3.5, 4.5), xlabel=r'$n$', ylabel=r'$S_n$')
    ax.set_title('(a) 首次达到阈值：当场可判定')
    # (b) two continuations of the same history up to n=6
    common = [1, 1, -1, 1, 1, -1]
    lower = common + [-1, -1, 1, -1, -1, 1, -1, -1]
    higher = common + [-1, 1, 1, 1, -1, 1, 1, -1]
    Sl = np.concatenate([[0], np.cumsum(lower)])
    Sh = np.concatenate([[0], np.cumsum(higher)])
    ax = axes[1]
    ax.axvspan(0, 6, color=BLUE_FILL, lw=0)
    ax.plot(np.arange(len(Sl)), Sl, 'o-', color=GREEN, ms=2.2, lw=.9, label='后续走低')
    ax.plot(np.arange(len(Sh)), Sh, 's-', color=YELLOW, ms=2.2, lw=.9, label='后续走高')
    ax.plot(np.arange(7), Sl[:7], 'o-', color=BLUE, ms=2.4, lw=1.1)
    ax.plot([5], [Sl[5]], 'o', color=RED, ms=4)
    ax.text(0.3, 4.6, '已观测部分', color=BLUE, fontsize=7.5)
    ax.set(xlim=(0, 14), ylim=(-3.5, 5.5), xlabel=r'$n$', ylabel=r'$S_n$')
    ax.set_title('(b) 全程最高点：要看未来')
    ax.legend(loc='lower left', handlelength=1.4)
    save(fig, D/'spp-stopping-vs-peak', 'figure', {
        'a_steps': steps_a, 'a_tau_first_hit_of_3': tau,
        'b_common_history': common, 'b_lower_continuation': lower, 'b_higher_continuation': higher,
        'b_time_of_running_max_at_n6': 5,
        'b_global_argmax_lower': int(np.argmax(Sl)), 'b_global_argmax_higher': int(np.argmax(Sh))})


def spp_spike():
    """X_t = 1{t=U}: versions that differ from Y_t=0 only at a random location."""
    r = rng(5)
    U = np.sort(r.uniform(size=5))
    t0 = 0.5
    fig, ax = figure(width_mm=100, height_mm=44)
    for k, u in enumerate(U):
        base = 1.6 * k
        ax.plot([0, 1], [base, base], color=BLUE, lw=1.0)
        ax.plot([u, u], [base, base + 1], color=RED, lw=1.0)
        ax.plot([u], [base + 1], 'o', color=RED, ms=2.6)
        ax.plot([u], [base], 'o', mfc='white', mec=BLUE, ms=2.6, mew=.7)
        ax.text(1.02, base, rf'$\omega_{k + 1}$', va='center', fontsize=7.5, color=MUTED)
    ax.axvline(t0, color=GREEN, lw=.9, ls='--')
    ax.text(t0 + .01, 1.6 * 5 - .2, r'$t=t_0$', color=GREEN, fontsize=7.5)
    ax.set(xlim=(0, 1.08), ylim=(-.4, 1.6 * 5 + .2), xlabel=r'$t$')
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    save(fig, D/'spp-spike', 'figure', {
        'seed': SEED + 5, 'model': 'U~Unif(0,1), X_t=1{t=U}, Y_t=0', 'U_values': [round(float(u), 4) for u in U],
        't0': t0, 'vertical_offset_between_realizations': 1.6})


def spp_increment_moments():
    """E|X_{t+h}-X_t|^p versus h: Brownian (p=2,4) and Poisson rate 1 (p=2,4)."""
    r = rng(6)
    h = np.logspace(-3, 0, 200)
    hs = np.logspace(-3, 0, 7)
    M = 200000
    fig, ax = figure(width_mm=100, height_mm=56)
    ax.loglog(h, h + h**2, color=YELLOW, lw=2.4, label=r'Poisson, $p=2$')
    ax.loglog(h, h + 7 * h**2 + 6 * h**3 + h**4, color=YELLOW, lw=1.1, ls='--', label=r'Poisson, $p=4$')
    ax.loglog(h, h, color=BLUE, lw=1.0, label=r'Brownian, $p=2$')
    ax.loglog(h, 3 * h**2, color=BLUE, lw=1.1, ls='--', label=r'Brownian, $p=4$')
    facts = {'seed': SEED + 6, 'mc_samples_per_h': M, 'h_mc': [float(x) for x in hs], 'mc': {}}
    for p, mk in [(2, 'o'), (4, 's')]:
        b = [np.mean(np.abs(np.sqrt(x) * r.standard_normal(M))**p) for x in hs]
        q = [np.mean(r.poisson(x, M).astype(float)**p) for x in hs]
        ax.loglog(hs, b, mk, color=BLUE, ms=3, mfc='white', mew=.7)
        ax.loglog(hs, q, mk, color=YELLOW, ms=3, mfc='white', mew=.7)
        facts['mc'][f'brownian_p{p}'] = [float(f'{v:.4g}') for v in b]
        facts['mc'][f'poisson_p{p}'] = [float(f'{v:.4g}') for v in q]
    ax.set(xlim=(1e-3, 1), ylim=(1e-7, 20), xlabel=r'$h$', ylabel='增量的 p 阶矩')
    ax.legend(loc='lower right', handlelength=1.8)
    facts['exact'] = {'brownian_p2': 'h', 'brownian_p4': '3h^2', 'poisson_p2': 'h+h^2',
                      'poisson_p4': 'h+7h^2+6h^3+h^4', 'poisson_rate': 1}
    save(fig, D/'spp-increment-moments', 'figure', facts)


def _kernels():
    return [
        ('(a) 平方指数核', lambda s, t: np.exp(-(s - t)**2 / (2 * 0.1**2)), r'$\ell=0.1$'),
        ('(b) 指数核', lambda s, t: np.exp(-np.abs(s - t) / 0.2), r'$\ell=0.2$'),
        ('(c) 周期核', lambda s, t: np.exp(-2 * np.sin(np.pi * np.abs(s - t) / 0.5)**2 / 1.0**2), r'$p=0.5,\ \ell=1$'),
        ('(d) Brownian 核', lambda s, t: np.minimum(s, t), r'$\min(s,t)$'),
    ]


def spp_gp_kernels():
    """Covariance heat maps and three sample paths for four kernels on [0,1]."""
    r = rng(7)
    x = np.linspace(0, 1, 301)
    S, T = np.meshgrid(x, x, indexing='ij')
    fig, axes = figure(width_mm=150, height_mm=74, nrows=2, ncols=4, gridspec_kw={'height_ratios': [1, 1]})
    facts = {'seed': SEED + 7, 'grid_points': len(x), 'sampling': 'symmetric eigendecomposition, negative eigenvalues clipped to 0', 'kernels': {}}
    Z = r.standard_normal((len(x), 3))
    for j, (title, k, param) in enumerate(_kernels()):
        K = k(S, T)
        ax = axes[0, j]
        ax.imshow(K, origin='lower', extent=(0, 1, 0, 1), cmap=HEAT, vmin=0, vmax=1, interpolation='nearest')
        ax.set_title(title)
        ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
        ax.set_xlabel(r'$s$', labelpad=1)
        if j == 0:
            ax.set_ylabel(r'$t$', labelpad=1)
        ax.text(0.04, 0.9, param, transform=ax.transAxes, fontsize=7.5, color=INK)
        w, V = np.linalg.eigh(K)
        A = V * np.sqrt(np.clip(w, 0, None))
        paths = A @ Z
        ax = axes[1, j]
        for i, col in enumerate([BLUE, GREEN, YELLOW]):
            ax.plot(x, paths[:, i], color=col, lw=.9)
        ax.set(xlim=(0, 1), ylim=(-3, 3), xlabel=r'$x$')
        if j == 0:
            ax.set_ylabel(r'$F(x)$')
        facts['kernels'][title] = {'param': param, 'min_eigenvalue': float(w.min())}
    save(fig, D/'spp-gp-kernels', 'figure', facts)


def spp_kl_expansion():
    """Partial sums of W(t)=sum_k Z_k sqrt2 sin((k-1/2) pi t)/((k-1/2) pi)."""
    r = rng(8)
    K = 1024
    Z = r.standard_normal(K)
    t = np.linspace(0, 1, 2001)
    fig, ax = figure(width_mm=100, height_mm=50)
    facts = {'seed': SEED + 8, 'basis': 'e_k(t)=sqrt(2) sin((k-1/2) pi t)/((k-1/2) pi)', 'terms': []}
    for m, col, lw in [(1, YELLOW, 1.0), (4, GREEN, 1.0), (16, BLUE, .9), (1024, INK, .6)]:
        k = np.arange(1, m + 1) - 0.5
        W = (np.sqrt(2) * np.sin(np.outer(t, k) * np.pi) / (k * np.pi)) @ Z[:m]
        ax.plot(t, W, color=col, lw=lw, label=rf'$m={m}$')
        facts['terms'].append(m)
    ax.set(xlim=(0, 1), xlabel=r'$t$', ylabel=r'$W^{(m)}(t)$')
    ax.legend(loc='best', handlelength=1.4, ncols=2)
    save(fig, D/'spp-kl-expansion', 'figure', facts)


def spp_rkhs_vs_path():
    """Dyadic quadratic sums of a Brownian path and of an H_min function; H_min norm of truncated expansions."""
    r = rng(9)
    L = 16
    m = 2**L
    t = np.linspace(0, 1, m + 1)
    W = np.concatenate([[0], np.cumsum(r.standard_normal(m) / np.sqrt(m))])
    f = 0.8 * np.sin(np.pi * t / 2)
    levels = np.arange(1, L + 1)
    qw = [float(np.sum(np.diff(W[::2**(L - n)])**2)) for n in levels]
    qf = [float(np.sum(np.diff(f[::2**(L - n)])**2)) for n in levels]
    fig, axes = figure(width_mm=107, height_mm=48, ncols=2)
    ax = axes[0]
    ax.semilogy(levels, qw, 'o-', color=RED, ms=2.6, lw=.9, label='Brownian 路径')
    ax.semilogy(levels, qf, 's-', color=BLUE, ms=2.6, lw=.9, label=r'$f\in H_{\min}$')
    norm_f = 0.8**2 * (np.pi / 2)**2 * 0.5
    ax.semilogy(levels, norm_f * 2.0**(-levels), color=INK, lw=.7, ls='--', label=r'$\|f\|^2 2^{-n}$', zorder=5)
    ax.set(xlabel=r'$n$', ylabel=r'$\sum_i (\Delta_i)^2$')
    ax.set_title('(a) 二进平方增量和')
    ax.legend(loc='lower left', handlelength=1.6)
    ax = axes[1]
    mm = np.arange(1, 401)
    for i, col in enumerate([RED, YELLOW, GREEN]):
        Z = r.standard_normal(400)
        ax.plot(mm, np.cumsum(Z**2), color=col, lw=.9)
    ax.plot(mm, mm, color=MUTED, lw=.6, ls='--', label=r'$m$')
    ax.set(xlim=(0, 400), ylim=(0, 450), xlabel=r'$m$', ylabel=r'$\sum_{k\leq m} Z_k^2$')
    ax.set_title('(b) 截断展开的范数平方')
    ax.legend(loc='upper left', handlelength=1.6)
    save(fig, D/'spp-rkhs-vs-path', 'figure', {
        'seed': SEED + 9, 'brownian_grid': m, 'f': '0.8 sin(pi t/2)', 'f_Hmin_norm_squared': float(norm_f),
        'brownian_quadratic_sums': [round(v, 4) for v in qw], 'f_quadratic_sums': [float(f'{v:.4g}') for v in qf]})


def spp_beta_binomial():
    """Number of successes among 10: Binomial(10,1/2) versus Beta(2,2) mixture (beta-binomial)."""
    n = 10
    k = np.arange(n + 1)
    binom = stats.binom.pmf(k, n, .5)
    bb = stats.betabinom.pmf(k, n, 2, 2)
    fig, ax = figure(width_mm=100, height_mm=46)
    w = .38
    ax.bar(k - w / 2, binom, width=w, color=BLUE_FILL, edgecolor=BLUE, lw=.6, label=r'$\Theta\equiv 1/2$')
    ax.bar(k + w / 2, bb, width=w, color=YELLOW_FILL, edgecolor=YELLOW, lw=.6, label=r'$\Theta\sim\mathrm{Beta}(2,2)$')
    ax.set(xlabel=r'$S_{10}$', ylabel='概率', xticks=k)
    ax.legend(loc='upper left', handlelength=1.4)
    save(fig, D/'spp-beta-binomial', 'figure', {
        'binomial_pmf': [round(float(v), 4) for v in binom], 'beta_binomial_pmf': [round(float(v), 4) for v in bb],
        'variances': {'binomial': 2.5, 'beta_binomial': float(stats.betabinom.var(n, 2, 2))}})


def spp_polya_frequencies():
    """Running frequencies: iid Bernoulli(1/2) versus Polya urn (a=b=1) and the law of the urn limits."""
    r = rng(10)
    n, paths, many = 2000, 20, 4000
    idx = np.arange(1, n + 1)

    def urn(count):
        ones = np.ones(count)
        tot = np.full(count, 2.0)
        out = np.empty((count, n))
        for i in range(n):
            x = r.uniform(size=count) < ones / tot
            ones += x
            tot += 1
            out[:, i] = x
        return out

    fig, axes = figure(width_mm=150, height_mm=46, ncols=3, gridspec_kw={'width_ratios': [1, 1, .8]})
    iid = r.uniform(size=(paths, n)) < .5
    for i in range(paths):
        axes[0].semilogx(idx, np.cumsum(iid[i]) / idx, color=BLUE if i else INK, lw=.6 if i else .9)
    axes[0].set(ylim=(0, 1), xlabel=r'$n$', ylabel=r'$\bar X_n$')
    axes[0].set_title('(a) 独立 Bernoulli(1/2)')
    U = urn(paths)
    for i in range(paths):
        axes[1].semilogx(idx, np.cumsum(U[i]) / idx, color=YELLOW if i else INK, lw=.6 if i else .9)
    axes[1].set(ylim=(0, 1), xlabel=r'$n$')
    axes[1].set_title('(b) Pólya 罐：各自收敛')
    lim = urn(many)[:, :].mean(axis=1)
    ax = axes[2]
    ax.hist(lim, bins=np.linspace(0, 1, 21), density=True, color=YELLOW_FILL, edgecolor=YELLOW, lw=.5)
    ax.plot([0, 1], [1, 1], color=INK, lw=1.0, label=r'$\mathrm{Beta}(1,1)$')
    ax.set(xlim=(0, 1), ylim=(0, 1.6), xlabel=r'$\bar X_{2000}$', ylabel='密度')
    ax.set_title(f'(c) {many} 个罐的频率')
    ax.legend(loc='upper center', handlelength=1.4)
    save(fig, D/'spp-polya-frequencies', 'figure', {
        'seed': SEED + 10, 'n': n, 'paths_shown': paths, 'urns_for_histogram': many,
        'urn': 'start with one 1-ball and one 0-ball; draw, return with one extra ball of the same colour',
        'histogram_mean': round(float(lim.mean()), 4), 'histogram_var': round(float(lim.var()), 4),
        'beta11_var': 1 / 12})


def _stick(r, alpha, K):
    V = r.beta(1, alpha, size=K)
    w = V * np.concatenate([[1], np.cumprod(1 - V)[:-1]])
    return w


def spp_random_measure_partition():
    """One random discrete measure on [0,1] (stick-breaking, alpha=5, G0=Unif) and its partition masses."""
    r = rng(11)
    w = _stick(r, 5.0, 400)
    xi = r.uniform(size=400)
    edges = [0, .3, .6, 1]
    masses = [float(w[(xi >= a) & (xi < b)].sum()) for a, b in zip(edges[:-1], edges[1:])]
    fig, axes = figure(width_mm=107, height_mm=46, ncols=2, gridspec_kw={'width_ratios': [1.7, 1]})
    ax = axes[0]
    fills = [BLUE_FILL, GREEN_FILL, YELLOW_FILL]
    for (a, b), fill, lab in zip(zip(edges[:-1], edges[1:]), fills, ['$A_1$', '$A_2$', '$A_3$']):
        ax.axvspan(a, b, color=fill, lw=0)
        ax.text((a + b) / 2, .47, lab, ha='center', fontsize=7.5)
    keep = w > 1e-3
    ax.vlines(xi[keep], 0, w[keep], color=INK, lw=.7)
    ax.plot(xi[keep], w[keep], 'o', color=INK, ms=1.8)
    ax.set(xlim=(0, 1), ylim=(0, .5), xlabel=r'$\xi_k$', ylabel=r'$w_k$')
    ax.set_title('(a) 一次实现：随机原子与随机权重')
    ax = axes[1]
    ax.bar([0, 1, 2], masses, color=fills, edgecolor=[BLUE, GREEN, YELLOW], lw=.6, width=.6)
    ax.bar([3.2], [masses[1] + masses[2]], color=PURPLE_FILL, edgecolor=PURPLE, lw=.6, width=.6)
    ax.set_xticks([0, 1, 2, 3.2])
    ax.set_xticklabels(['$A_1$', '$A_2$', '$A_3$', r'$A_2\cup A_3$'])
    for xpos, v in zip([0, 1, 2, 3.2], masses + [masses[1] + masses[2]]):
        ax.text(xpos, v + .015, f'{v:.2f}', ha='center', fontsize=7.5)
    ax.set(ylim=(0, max(masses[1] + masses[2], max(masses)) + .12), ylabel=r'$G(A)$')
    ax.set_title('(b) 分割质量与合并')
    save(fig, D/'spp-random-measure-partition', 'figure', {
        'seed': SEED + 11, 'construction': 'stick-breaking, V_k~Beta(1,5), atoms iid Unif(0,1), 400 atoms',
        'atoms_drawn_with_weight_above': 1e-3, 'partition': edges, 'masses': [round(m, 4) for m in masses],
        'truncation_remaining_mass': float(1 - w.sum())})


def spp_stick_breaking():
    """Stick-breaking pieces for alpha = 1, 5, 20 and expected weights E w_k."""
    r = rng(12)
    alphas = [1, 5, 20]
    fig, axes = figure(width_mm=107, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1.25, 1]})
    ax = axes[0]
    palette = [BLUE, GREEN, YELLOW, RED, PURPLE]
    facts = {'seed': SEED + 12, 'alphas': alphas, 'first_weights': {}}
    for row, a in enumerate(alphas):
        w = _stick(r, a, 3000)
        left = 0.0
        for k in range(40):
            ax.barh(row, w[k], left=left, height=.6, color=palette[k % 5], edgecolor='white', lw=.3)
            left += w[k]
        ax.barh(row, 1 - left, left=left, height=.6, color=GRID, lw=0)
        facts['first_weights'][str(a)] = [round(float(v), 4) for v in w[:6]]
    ax.set_yticks(range(3))
    ax.set_yticklabels([rf'$\alpha={a}$' for a in alphas])
    ax.invert_yaxis()
    ax.set(xlim=(0, 1), xlabel='累计质量')
    ax.set_title('(a) 前 40 段折棒（灰色为剩余）')
    ax = axes[1]
    k = np.arange(1, 61)
    for a, col, mk in zip(alphas, [BLUE, GREEN, YELLOW], ['o', 's', '^']):
        ax.semilogy(k, (1 / (1 + a)) * (a / (1 + a))**(k - 1), color=col, lw=1.0, label=rf'$\alpha={a}$')
    ax.set(xlim=(1, 60), ylim=(1e-5, 1), xlabel=r'$k$', ylabel='期望权重')
    ax.set_title('(b) 期望权重的几何衰减')
    ax.legend(loc='lower left', handlelength=1.4)
    save(fig, D/'spp-stick-breaking', 'figure', facts)


def spp_dp_samples():
    """Random CDFs of DP(alpha, N(0,1)) for alpha = 1, 10, 100 versus the base CDF."""
    r = rng(13)
    x = np.linspace(-3.2, 3.2, 1200)
    fig, axes = figure(width_mm=150, height_mm=46, ncols=3, sharey=True)
    facts = {'seed': SEED + 13, 'base': 'N(0,1)', 'truncation_atoms': 6000, 'samples_per_alpha': 4, 'remaining_mass_max': 0.0}
    for ax, a in zip(axes, [1, 10, 100]):
        for i, col in enumerate([BLUE, GREEN, YELLOW, RED]):
            w = _stick(r, a, 6000)
            xi = r.standard_normal(6000)
            cdf = np.array([w[xi <= v].sum() for v in x])
            ax.plot(x, cdf, color=col, lw=.8, drawstyle='steps-post')
            facts['remaining_mass_max'] = max(facts['remaining_mass_max'], float(1 - w.sum()))
        ax.plot(x, stats.norm.cdf(x), color=INK, lw=1.1, ls='--', label=r'$G_0$')
        ax.set(xlim=(-3.2, 3.2), ylim=(-0.02, 1.02), xlabel=r'$x$')
        ax.set_title(rf'$\alpha={a}$')
    axes[0].set_ylabel(r'$G((-\infty,x])$')
    axes[0].legend(loc='upper left', handlelength=1.6)
    save(fig, D/'spp-dp-samples', 'figure', facts)


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    spp_two_views, spp_taxonomy, spp_same_marginals, spp_cylinder, spp_stopping_vs_peak, spp_spike,
    spp_increment_moments, spp_gp_kernels, spp_kl_expansion, spp_rkhs_vs_path, spp_beta_binomial,
    spp_polya_frequencies, spp_random_measure_partition, spp_stick_breaking, spp_dp_samples]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
