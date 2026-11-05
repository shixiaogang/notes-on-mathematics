# coding: utf-8
"""Teaching charts for volume two, part "probability spaces", chapter 3
(convergence of random variables and limits of expectations).

Analytic curves are computed from the closed forms recorded in each facts
record; every simulation uses a fixed numpy seed stored with its parameters.
Run from any directory:
  python figures/02-abstract-mathematics/02-probability-spaces/matplotlib/generate_ch3.py [name ...]
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


def dyadic_interval(n):
    """Return (k, j, left, right) for n = 2**k + j, 0 <= j < 2**k."""
    k = int(np.floor(np.log2(n)))
    j = n - 2**k
    return k, j, j / 2**k, (j + 1) / 2**k


def dyadic_value(n, u):
    _, _, a, b = dyadic_interval(n)
    return 1.0 if a <= u < b else 0.0


def conv_dyadic_sweep():
    """Dyadic sweeping indicators: the intervals and one sample path."""
    u = 0.3
    fig, axes = figure(width_mm=150, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [1, 1.35]})
    ax = axes[0]
    hits = []
    for n in range(1, 16):
        k, j, a, b = dyadic_interval(n)
        hit = a <= u < b
        if hit:
            hits.append(n)
        ax.plot([a, b], [n, n], color=RED if hit else BLUE, lw=2.2 if hit else 1.6, solid_capstyle='butt')
    for k in range(1, 4):
        ax.axhline(2**k - 0.5, color=GRID, lw=.6)
    ax.axvline(u, color=MUTED, lw=.6, ls='--')
    ax.text(u + 0.02, 15.6, r'$u=0.3$', color=MUTED, fontsize=7.5)
    ax.set(xlim=(0, 1), ylim=(16.2, 0.3), xlabel=r'$u$', ylabel=r'$n$')
    ax.set_yticks([1, 2, 4, 8, 15])
    ax.set_title('(a) 第n项取1的区间')
    ax = axes[1]
    ns = np.arange(1, 64)
    x = np.array([dyadic_value(n, u) for n in ns])
    p = np.array([2.0**-dyadic_interval(n)[0] for n in ns])
    ax.step(ns, p, where='mid', color=GREEN, lw=1.1, label='取1的概率')
    ax.plot(ns[x == 0], x[x == 0], 'o', color=BLUE, ms=2.0, label='样本值为0')
    ax.plot(ns[x == 1], x[x == 1], 'o', color=RED, ms=3.2, label='样本值为1')
    for k in range(1, 6):
        ax.axvline(2**k - 0.5, color=GRID, lw=.6)
    ax.set(xlim=(0, 64), ylim=(-0.08, 1.12), xlabel=r'$n$')
    ax.set_xticks([1, 4, 8, 16, 32, 63])
    ax.set_title('(b) 样本u=0.3的路径')
    ax.legend(loc='center right', handlelength=1.4)
    path_hits = [int(n) for n in ns[x == 1]]
    save(fig, D/'conv-dyadic-sweep', 'figure', {
        'definition': 'X_n = I{U in [j/2^k,(j+1)/2^k)}, n = 2^k + j', 'u': u,
        'hits_n_le_15': hits, 'hits_n_le_63': path_hits,
        'probability_of_one': '2^-k on round k'})


def conv_spike():
    """Spikes n*I(0<U<1/n): graphs and the constant expectation."""
    fig, axes = figure(width_mm=150, height_mm=50, ncols=2)
    ax = axes[0]
    cols = [BLUE, GREEN, YELLOW, RED]
    for n, c in zip([1, 2, 4, 8], cols):
        ax.fill_between([0, 1 / n], [n, n], color=c, alpha=0.18, lw=0, step='pre')
        ax.plot([0, 0, 1 / n, 1 / n, 1], [0, n, n, 0, 0], color=c, lw=1.1, label=rf'$n={n}$')
    ax.set(xlim=(-0.02, 1.02), ylim=(0, 8.8), xlabel=r'$u$', ylabel=r'$x_n(u)$')
    ax.set_title('(a) 每条曲线下的面积都是1')
    ax.legend(loc='upper right', handlelength=1.4)
    ax = axes[1]
    ns = np.arange(1, 201)
    ax.semilogx(ns, np.ones_like(ns, dtype=float), color=RED, lw=1.1, label='期望')
    ax.semilogx(ns, 1 / ns, color=BLUE, lw=1.1, label='取非零值的概率')
    u = 0.3
    vals = np.where(u < 1 / ns, ns, 0)
    ax.semilogx(ns, vals, 'o', color=GREEN, ms=1.8, label=r'$x_n(0.3)$')
    ax.set(xlim=(1, 200), ylim=(-0.1, 3.4), xlabel=r'$n$')
    ax.set_title('(b) 期望不随几乎处处极限变化')
    ax.legend(loc='upper right', handlelength=1.4)
    save(fig, D/'conv-spike', 'figure', {
        'definition': 'X_n = n I{0<U<1/n}, U ~ Unif[0,1)', 'expectation': 1, 'P(X_n != 0)': '1/n',
        'path_u_0.3_nonzero_n': [int(n) for n in ns[vals > 0]]})


def conv_borel_cantelli():
    """Occurrence counts of independent events with summable and divergent probabilities."""
    rng = np.random.default_rng(SEED)
    N, paths = 10000, 8
    ns = np.arange(1, N + 1)
    fig, axes = figure(width_mm=150, height_mm=50, ncols=2, sharey=False)
    facts = {'seed': SEED, 'n_max': N, 'paths': paths}
    for ax, (p, lab, tag) in zip(axes, [(1 / ns**2, 'p_n=1/n^2', '(a)'), (1 / ns, 'p_n=1/n', '(b)')]):
        finals = []
        for i in range(paths):
            occ = rng.random(N) < p
            cnt = np.cumsum(occ)
            ax.step(ns, cnt, where='post', color=BLUE if tag == '(a)' else GREEN, lw=.8, alpha=.85)
            finals.append(int(cnt[-1]))
        ax.semilogx(ns, np.cumsum(p), color=INK, lw=1.1, ls='--', label='期望次数')
        ax.set(xlim=(1, N), xlabel=r'$n$')
        facts[lab] = {'final_counts': finals, 'expected_count_at_n_max': float(np.sum(p))}
    axes[0].set_ylabel('前n个事件中发生的次数')
    axes[0].set(ylim=(0, 4.5))
    axes[0].set_title(r'(a) $p_n=1/n^2$')
    axes[1].set_title(r'(b) $p_n=1/n$')
    axes[1].set(ylim=(0, 18))
    axes[0].legend(loc='upper left', handlelength=1.6)
    save(fig, D/'conv-borel-cantelli', 'figure', facts)


def conv_subsequence():
    """Dyadic sweep: one path with the subsequence n_k=2^k, and cumulative bad probabilities."""
    u = 0.3
    fig, axes = figure(width_mm=150, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1.3, 1]})
    ax = axes[0]
    ns = np.arange(1, 128)
    x = np.array([dyadic_value(n, u) for n in ns])
    ax.plot(ns, x, 'o', color=MUTED, ms=1.6, label='全序列')
    sub = 2**np.arange(0, 7)
    xs = np.array([dyadic_value(n, u) for n in sub])
    ax.plot(sub, xs, 's', color=RED, ms=3.4, mfc='none', mew=.9, label='子列')
    for k in range(1, 7):
        ax.axvline(2**k - 0.5, color=GRID, lw=.6)
    ax.set(xlim=(0, 128), ylim=(-0.1, 1.15), xlabel=r'$n$', ylabel=r'$x_n(0.3)$')
    ax.set_xticks([1, 8, 16, 32, 64, 127])
    ax.set_title('(a) 一条样本路径上的子列')
    ax.legend(loc='center right', handlelength=1.2)
    ax = axes[1]
    nmax = 2**12
    nn = np.arange(1, nmax + 1)
    pfull = np.array([2.0**-int(np.floor(np.log2(n))) for n in nn])
    ax.semilogx(nn, np.cumsum(pfull), color=BLUE, lw=1.1, label='全序列')
    ks = np.arange(0, 13)
    ax.semilogx(2.0**ks, np.cumsum(2.0**-ks), 'o-', color=RED, ms=2.4, lw=1.0, label='子列')
    ax.axhline(2, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(1, nmax), ylim=(0, 13.5), xlabel=r'$n$', ylabel='坏事件概率的累计和')
    ax.set_title('(b) 求和是否有限')
    ax.legend(loc='upper left', handlelength=1.4)
    save(fig, D/'conv-subsequence', 'figure', {
        'u': u, 'subsequence': 'n_k = 2^k, X_{n_k} = I{U < 2^-k}', 'subsequence_values_k0_to_6': xs.tolist(),
        'full_cumulative_at_2^12': float(np.cumsum(pfull)[-1]), 'sub_cumulative_limit': 2})


def conv_ui_tails():
    """Uniform tail integrals for the spike family and a family with bounded second moments."""
    fig, axes = figure(width_mm=150, height_mm=50, ncols=2)
    ax = axes[0]
    K = np.linspace(0, 25, 2501)
    spike = np.ones_like(K)
    sq = 1 / np.sqrt(np.floor(K**2) + 1)
    ax.plot(K, spike, color=RED, lw=1.1, label='尖峰族')
    ax.plot(K, sq, color=BLUE, lw=1.1, label='平方根尖峰族')
    ax.plot(K[K >= 1], 1 / K[K >= 1], color=MUTED, lw=.8, ls='--', label=r'$K^{-1}$')
    ax.set(xlim=(0, 12), ylim=(0, 1.15), xlabel=r'$K$', ylabel='全族尾部积分的上确界')
    ax.set_title('(a) 同一阈值控制全族')
    ax.legend(loc='center right', handlelength=1.6)
    ax = axes[1]
    for n, c in zip([2, 5, 10, 20], [BLUE, GREEN, YELLOW, RED]):
        ax.step(K, np.where(K < n, 1.0, 0.0), where='post', color=c, lw=1.1, label=rf'$n={n}$')
    ax.set(xlim=(0, 25), ylim=(-0.05, 1.15), xlabel=r'$K$', ylabel='单项尾部积分')
    ax.set_title('(b) 尖峰族逐项的尾部')
    ax.legend(loc='center right', handlelength=1.4)
    save(fig, D/'conv-ui-tails', 'figure', {
        'spike_tail': 'E[X_n I(X_n>K)] = I(n>K), sup_n = 1',
        'sqrt_spike_tail': 'E[X_n I(X_n>K)] = n^-1/2 I(sqrt n > K), sup_n = (floor(K^2)+1)^-1/2',
        'second_moment_bound': 'E[X_n I(X_n>K)] <= E X_n^2 / K = 1/K'})


def conv_kolmogorov_maximal():
    """Simple random walk partial sums: first crossings and the maximal inequality."""
    rng = np.random.default_rng(SEED + 1)
    n, a = 100, 12
    fig, axes = figure(width_mm=150, height_mm=52, ncols=2)
    ax = axes[0]
    k = np.arange(0, n + 1)
    cols = [BLUE, GREEN, YELLOW, RED, PURPLE, MUTED]
    crossings = []
    for c in cols:
        s = np.r_[0, np.cumsum(rng.choice([-1, 1], size=n))]
        ax.plot(k, s, color=c, lw=.8)
        idx = np.nonzero(np.abs(s) >= a)[0]
        if idx.size:
            ax.plot(idx[0], s[idx[0]], 'o', color=c, ms=3.4, mfc='white', mew=1.0)
            crossings.append({'first_k': int(idx[0]), 'S_n': int(s[-1])})
        else:
            crossings.append({'first_k': None, 'S_n': int(s[-1])})
    for y in (a, -a):
        ax.axhline(y, color=INK, lw=.6, ls='--')
    ax.set(xlim=(0, n), ylim=(-28, 28), xlabel=r'$k$', ylabel=r'$S_k$')
    ax.set_title('(a) 部分和路径与第一次越过')
    ax = axes[1]
    reps = 20000
    steps = rng.choice([-1, 1], size=(reps, n)).astype(np.int16)
    S = np.cumsum(steps, axis=1)
    M = np.abs(S).max(axis=1)
    E = np.abs(S[:, -1])
    aa = np.arange(4, 41)
    pm = np.array([(M >= t).mean() for t in aa])
    pe = np.array([(E >= t).mean() for t in aa])
    ax.plot(aa, np.minimum(1, n / aa**2), color=INK, lw=1.0, ls='--', label='最大不等式上界')
    ax.plot(aa, pm, color=RED, lw=1.1, label='全程最大偏差')
    ax.plot(aa, pe, color=BLUE, lw=1.1, label='终点偏差')
    ax.set(xlim=(4, 40), ylim=(0, 1.05), xlabel=r'$a$', ylabel='超过阈值的概率')
    ax.set_title('(b) 概率与上界')
    ax.legend(loc='upper right', handlelength=1.6)
    ia = int(np.nonzero(aa == a)[0][0])
    save(fig, D/'conv-kolmogorov-maximal', 'figure', {
        'seed': SEED + 1, 'steps': 'iid +-1 with probability 1/2', 'n': n, 'threshold_panel_a': a,
        'panel_a_paths': crossings, 'repetitions_panel_b': reps,
        'at_threshold': {'a': a, 'P_max': float(pm[ia]), 'P_end': float(pe[ia]), 'bound': n / a**2}})


def conv_random_harmonic():
    """Random signs weighted by 1/k (variance summable) and by 1/sqrt(k) (not summable)."""
    rng = np.random.default_rng(SEED + 2)
    N, paths = 5000, 6
    k = np.arange(1, N + 1)
    fig, axes = figure(width_mm=150, height_mm=50, ncols=2)
    cols = [BLUE, GREEN, YELLOW, RED, PURPLE, MUTED]
    eps = rng.choice([-1.0, 1.0], size=(paths, N))
    limits = []
    for e, c in zip(eps, cols):
        s = np.cumsum(e / k)
        axes[0].semilogx(k, s, color=c, lw=.8)
        limits.append(float(s[-1]))
        axes[1].semilogx(k, np.cumsum(e / np.sqrt(k)), color=c, lw=.8)
    env = np.sqrt(np.cumsum(1 / k))
    for sgn in (1, -1):
        axes[1].semilogx(k, 2 * sgn * env, color=INK, lw=.8, ls='--')
    axes[0].set(xlim=(1, N), ylim=(-3, 3), xlabel=r'$n$', ylabel=r'$\sum_{k\leq n}\varepsilon_k/k$')
    axes[0].set_title('(a) 方差和有限')
    axes[1].set(xlim=(1, N), ylim=(-9, 9), xlabel=r'$n$', ylabel=r'$\sum_{k\leq n}\varepsilon_k/\sqrt{k}$')
    axes[1].set_title('(b) 方差和发散')
    save(fig, D/'conv-random-harmonic', 'figure', {
        'seed': SEED + 2, 'signs': 'iid Rademacher', 'n_max': N, 'paths': paths,
        'panel_a_values_at_n_max': limits, 'panel_a_variance_sum': float(np.pi**2 / 6),
        'panel_b_envelope': '+-2 sqrt(H_n), H_n = sum_{k<=n} 1/k'})


def conv_kronecker():
    """Abel summation identity on one path: a_n = b_n - (1/n) sum_{k<n} b_k."""
    rng = np.random.default_rng(SEED + 2)
    N = 5000
    k = np.arange(1, N + 1)
    e = rng.choice([-1.0, 1.0], size=(6, N))[0]
    b = np.cumsum(e / k)
    c = np.r_[0, np.cumsum(b)[:-1]] / k
    a = np.cumsum(e) / k
    fig, ax = figure(width_mm=112, height_mm=52)
    ax.semilogx(k, b, color=BLUE, lw=1.1, label=r'$b_n$')
    ax.semilogx(k, c, color=GREEN, lw=1.1, ls='--', label=r'$\frac{1}{n}\sum_{k<n}b_k$')
    ax.semilogx(k, a, color=RED, lw=.9, label=r'$\frac{1}{n}\sum_{k\leq n}z_k$')
    ax.axhline(0, color=MUTED, lw=.5)
    ax.set(xlim=(1, N), ylim=(-1.1, 1.6), xlabel=r'$n$')
    ax.legend(loc='lower right', handlelength=1.6)
    assert np.allclose(a, b - c)
    save(fig, D/'conv-kronecker', 'figure', {
        'seed': SEED + 2, 'z_k': 'first path of conv-random-harmonic signs', 'b_n_at_n_max': float(b[-1]),
        'cesaro_at_n_max': float(c[-1]), 'mean_at_n_max': float(a[-1]), 'identity_checked': True})


def conv_chebyshev_nonsummable():
    """Chebyshev bound versus exact error probability for Bernoulli(1/2) sample means."""
    eps = 0.1
    ns = np.arange(1, 2001)
    exact = []
    for n in ns:
        s = np.arange(n + 1)
        bad = 5 * np.abs(2 * s - n) >= n
        exact.append(stats.binom.pmf(s[bad], n, 0.5).sum())
    exact = np.array(exact)
    bound = np.minimum(1, 0.25 / (ns * eps**2))
    fig, axes = figure(width_mm=150, height_mm=50, ncols=2)
    ax = axes[0]
    ax.loglog(ns, bound, color=INK, lw=1.0, ls='--', label='Chebyshev上界')
    ax.loglog(ns, np.maximum(exact, 1e-30), color=BLUE, lw=1.1, label='精确概率')
    ax.set(xlim=(1, 2000), ylim=(1e-12, 2), xlabel=r'$n$', ylabel='误差不小于0.1的概率')
    ax.set_title('(a) 逐项比较')
    ax.legend(loc='lower left', handlelength=1.6)
    ax = axes[1]
    ax.semilogx(ns, np.cumsum(bound), color=INK, lw=1.0, ls='--', label='上界的累计和')
    ax.semilogx(ns, np.cumsum(exact), color=BLUE, lw=1.1, label='精确概率的累计和')
    ax.set(xlim=(1, 2000), ylim=(0, 200), xlabel=r'$n$')
    ax.set_title('(b) 累计和')
    ax.legend(loc='upper left', handlelength=1.6)
    save(fig, D/'conv-chebyshev-nonsummable', 'figure', {
        'model': 'X_i iid Bernoulli(1/2), event |mean - 1/2| >= 0.1', 'bound': 'min(1, 25/n)',
        'exact_at_n': {str(n): float(exact[n - 1]) for n in (10, 50, 100, 500, 1000)},
        'cum_bound_2000': float(np.cumsum(bound)[-1]), 'cum_exact_2000': float(np.cumsum(exact)[-1])})


def conv_slln_paths():
    """Running means for finite variance, finite mean only, and infinite mean."""
    rng = np.random.default_rng(SEED + 3)
    N, paths = 100000, 5
    k = np.arange(1, N + 1)
    fig, axes = figure(width_mm=150, height_mm=50, ncols=3)
    cols = [BLUE, GREEN, YELLOW, RED, PURPLE]
    facts = {'seed': SEED + 3, 'n_max': N, 'paths': paths}
    specs = [('(a) 指数分布', lambda: rng.exponential(1.0, N), 1.0, (0, 2.5), 'exponential(1)'),
             ('(b) Pareto分布，指数1.5', lambda: rng.random(N)**(-1 / 1.5), 3.0, (0, 8), 'Pareto(1.5,x_m=1)'),
             ('(c) Pareto分布，指数0.8', lambda: rng.random(N)**(-1 / 0.8), None, (1, 1e4), 'Pareto(0.8,x_m=1)')]
    for ax, (title, draw, mu, ylim, name) in zip(axes, specs):
        finals = []
        for c in cols:
            m = np.cumsum(draw()) / k
            if mu is None:
                ax.loglog(k, m, color=c, lw=.8)
            else:
                ax.semilogx(k, m, color=c, lw=.8)
            finals.append(float(m[-1]))
        if mu is not None:
            ax.axhline(mu, color=INK, lw=.7, ls='--')
        ax.set(xlim=(1, N), ylim=ylim, xlabel=r'$n$')
        ax.set_title(title)
        facts[name] = {'final_means': finals, 'mean': mu}
    axes[0].set_ylabel(r'$\bar X_n$')
    save(fig, D/'conv-slln-paths', 'figure', facts)


def conv_truncation():
    """Truncation Y_n = X_n I(|X_n|<=n) for a Pareto(1.5) sample."""
    rng = np.random.default_rng(SEED + 26)
    N = 100000
    k = np.arange(1, N + 1)
    x = rng.random(N)**(-1 / 1.5)
    big = x > k
    y = np.where(big, 0.0, x)
    diff = np.cumsum(x - y) / k
    fig, axes = figure(width_mm=150, height_mm=50, ncols=2)
    ax = axes[0]
    show = k <= 2000
    ax.loglog(k[show & ~big], x[show & ~big], '.', color=BLUE, ms=1.2, alpha=.6)
    ax.loglog(k[big], x[big], 'o', color=RED, ms=3.2, mfc='none', mew=.9, label=r'$|X_n|>n$')
    ax.loglog(k[show], k[show], color=INK, lw=.8, ls='--', label=r'$x=n$')
    ax.set(xlim=(1, 2000), ylim=(0.8, 3000), xlabel=r'$n$', ylabel=r'$X_n$')
    ax.set_title('(a) 被截断的项')
    ax.legend(loc='upper left', handlelength=1.4)
    ax = axes[1]
    ax.loglog(k, np.maximum(diff, 1e-12), color=RED, lw=1.1, label=r'$\bar X_n-\bar Y_n$')
    tot = float((x - y).sum())
    ax.loglog(k, tot / k, color=MUTED, lw=.7, ls=':', label='常数/n')
    ax.set(xlim=(1, N), ylim=(1e-5, 10), xlabel=r'$n$')
    ax.set_title('(b) 两种样本平均之差')
    ax.legend(loc='upper right', handlelength=1.4)
    save(fig, D/'conv-truncation', 'figure', {
        'seed': SEED + 26, 'law': 'Pareto alpha=1.5, x_m=1, X=U^(-1/1.5)', 'n_max': N,
        'truncated_indices': [int(i) for i in k[big]], 'expected_number': 'sum_n n^-1.5 = zeta(1.5) ~ 2.612',
        'total_removed': tot})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    conv_dyadic_sweep, conv_spike, conv_borel_cantelli, conv_subsequence, conv_ui_tails,
    conv_kolmogorov_maximal, conv_random_harmonic, conv_kronecker, conv_chebyshev_nonsummable,
    conv_slln_paths, conv_truncation]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
