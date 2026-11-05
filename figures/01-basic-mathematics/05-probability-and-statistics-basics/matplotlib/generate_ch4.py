# coding: utf-8
"""Teaching charts for volume one, part 5, chapter 4 (sampling distributions and estimation error).

Analytic curves come from scipy.stats formulas listed in the saved facts; every
simulation uses a fixed numpy seed recorded together with sample sizes and parameters.
Run from any directory:
  python figures/01-basic-mathematics/05-probability-and-statistics-basics/matplotlib/generate_ch4.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from scipy import stats

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL

D = Path(__file__).resolve().parent
SEED = 20261028


def samp_sample_proportion():
    """Histogram of repeated sample proportions with the exact binomial pmf."""
    rng = np.random.default_rng(SEED)
    p, reps = 0.3, 10000
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=False)
    facts = {'seed': SEED, 'population': 'Bernoulli(0.3)', 'repetitions': reps}
    for ax, n, tag in zip(axes, [20, 80], ['(a)', '(b)']):
        s = rng.binomial(n, p, size=reps)
        k = np.arange(n + 1)
        freq = np.bincount(s, minlength=n + 1) / reps
        ax.bar(k / n, freq, width=0.8 / n, color=BLUE_FILL, edgecolor=BLUE, lw=.5, label='模拟频率')
        ax.plot(k / n, stats.binom.pmf(k, n, p), 'o', color=INK, ms=2.0, label='二项概率')
        ax.axvline(p, color=RED, lw=.8, ls='--')
        ax.set(xlim=(0, 0.75), xlabel=r'$\hat p$')
        ax.set_title(f'{tag} n = {n}')
        ax.set_xticks([0, .15, .3, .45, .6, .75])
        facts[f'n={n}'] = {'empirical_mean': float(s.mean() / n), 'empirical_sd': float((s / n).std()),
                           'exact_sd': float(np.sqrt(p * (1 - p) / n))}
    axes[0].set_ylabel('概率或频率')
    axes[0].legend(loc='upper right', handlelength=1.2)
    save(fig, D/'samp-sample-proportion', 'figure', facts)


def samp_three_distributions():
    """Population density, one empirical CDF and the sampling distribution of the mean."""
    rng = np.random.default_rng(SEED)
    n, reps = 25, 10000
    fig, axes = figure(width_mm=150, height_mm=48, ncols=3)
    x = np.linspace(0, 6, 600)
    ax = axes[0]
    ax.plot(x, np.exp(-x), color=BLUE)
    ax.fill_between(x, np.exp(-x), color=BLUE_FILL, lw=0)
    ax.axvline(1, color=RED, lw=.8, ls='--')
    ax.set(xlim=(0, 6), ylim=(0, 1.05), xlabel=r'$x$', ylabel=r'$f(x)$')
    ax.set_title('(a) 总体分布')
    ax = axes[1]
    sample = rng.exponential(1.0, size=n)
    xs = np.sort(sample)
    ax.plot(x, 1 - np.exp(-x), color=MUTED, lw=.8, ls='--', label='总体')
    ax.step(np.r_[0, xs, 6], np.r_[0, np.arange(1, n + 1) / n, 1], where='post', color=GREEN, label='经验')
    ax.plot(xs, np.zeros(n) + 0.02, '|', color=INK, ms=4)
    ax.set(xlim=(0, 6), ylim=(0, 1.05), xlabel=r'$x$', ylabel=r'$\hat F_{25}(x)$')
    ax.set_title('(b) 一组样本的经验分布')
    ax.legend(loc='lower right', handlelength=1.4)
    ax = axes[2]
    means = rng.exponential(1.0, size=(reps, n)).mean(axis=1)
    ax.hist(means, bins=np.linspace(0.3, 1.9, 49), density=True, color=YELLOW_FILL, edgecolor=YELLOW, lw=.4)
    m = np.linspace(0.3, 1.9, 400)
    ax.plot(m, stats.gamma.pdf(m, a=n, scale=1 / n), color=INK, lw=1.0)
    ax.axvline(1, color=RED, lw=.8, ls='--')
    ax.set(xlim=(0.3, 1.9), xlabel=r'$\bar x_{25}$', ylabel='密度')
    ax.set_title('(c) 样本均值的抽样分布')
    save(fig, D/'samp-three-distributions', 'figure', {
        'seed': SEED, 'population': 'Exponential(rate=1)', 'n': n, 'repetitions_for_panel_c': reps,
        'panel_b_sample_mean': float(sample.mean()), 'panel_b_sample_max': float(xs[-1]), 'panel_c_mean_of_means': float(means.mean()),
        'panel_c_sd_of_means': float(means.std()), 'exact_sampling_law': 'Gamma(shape=25, rate=25), sd=0.2'})


def samp_shrinkage_mse():
    """Sampling densities of the mean and a shrunken mean, and their MSE curves."""
    n, sigma2, c, mu0 = 10, 1.0, 0.8, 0.5
    v = sigma2 / n
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    x = np.linspace(-0.6, 1.6, 600)
    ax.plot(x, stats.norm.pdf(x, mu0, np.sqrt(v)), color=BLUE, label=r'$\bar X$')
    ax.plot(x, stats.norm.pdf(x, c * mu0, c * np.sqrt(v)), color=GREEN, label=r'$0.8\bar X$')
    ax.axvline(mu0, color=RED, lw=.8, ls='--')
    ax.text(mu0 + 0.04, 1.75, r'$\mu=0.5$', color=RED, fontsize=7.5)
    ax.set(xlim=(-0.6, 1.6), ylim=(0, 1.9), xlabel='估计值', ylabel='密度')
    ax.set_title('(a) 两个估计量的抽样分布')
    ax.legend(loc='upper left', handlelength=1.4)
    ax = axes[1]
    mu = np.linspace(-1.6, 1.6, 400)
    ax.plot(mu, np.full_like(mu, v), color=BLUE, label=r'$\bar X$')
    ax.plot(mu, c**2 * v + (1 - c)**2 * mu**2, color=GREEN, label=r'$0.8\bar X$')
    cross = np.sqrt((v - c**2 * v) / (1 - c)**2)
    for s in (-cross, cross):
        ax.axvline(s, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(-1.6, 1.6), ylim=(0, 0.18), xlabel=r'$\mu$', ylabel='均方误差')
    ax.set_title('(b) 均方误差随参数变化')
    ax.legend(loc='upper center', handlelength=1.4)
    save(fig, D/'samp-shrinkage-mse', 'figure', {
        'model': 'X_i iid N(mu,1), n=10', 'estimators': ['mean', '0.8*mean'],
        'panel_a_mu': mu0, 'mse_mean': v, 'mse_shrunk': '0.064+0.04*mu**2', 'crossing_abs_mu': float(cross)})


def samp_chi_square_densities():
    fig, ax = figure(width_mm=100, height_mm=48)
    x = np.linspace(0.001, 20, 1000)
    for k, col in zip([1, 2, 3, 5, 10], [BLUE, GREEN, YELLOW, RED, PURPLE]):
        ax.plot(x, stats.chi2.pdf(x, k), color=col, label=rf'$k={k}$')
    ax.set(xlim=(0, 20), ylim=(0, 0.5), xlabel=r'$q$', ylabel='密度')
    ax.legend(loc='upper right', handlelength=1.6)
    save(fig, D/'samp-chi-square-densities', 'figure', {
        'densities': 'chi-square with k degrees of freedom', 'k': [1, 2, 3, 5, 10], 'means': [1, 2, 3, 5, 10]})


def samp_t_normal_tails():
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    x = np.linspace(-5, 5, 800)
    ax.plot(x, stats.norm.pdf(x), color=INK, lw=1.2, label=r'$\mathcal{N}(0,1)$')
    tail = {}
    for k, col, ls in [(1, RED, '-'), (3, YELLOW, '-'), (10, BLUE, '--')]:
        ax.plot(x, stats.t.pdf(x, k), color=col, ls=ls, label=rf'$t_{{{k}}}$')
    ax.set(xlim=(-5, 5), ylim=(0, 0.42), xlabel=r'$t$', ylabel='密度')
    ax.set_title('(a) 密度')
    ax.legend(loc='upper left', handlelength=1.6)
    ax = axes[1]
    c = np.linspace(0, 6, 400)
    ax.semilogy(c, 2 * stats.norm.sf(c), color=INK, lw=1.2, label=r'$\mathcal{N}(0,1)$')
    for k, col, ls in [(1, RED, '-'), (3, YELLOW, '-'), (10, BLUE, '--')]:
        ax.semilogy(c, 2 * stats.t.sf(c, k), color=col, ls=ls, label=rf'$t_{{{k}}}$')
        tail[k] = float(2 * stats.t.sf(3, k))
    ax.set(xlim=(0, 6), ylim=(1e-8, 1.2), xlabel=r'$c$', ylabel='尾概率')
    ax.set_title('(b) 双侧尾概率')
    tail['normal'] = float(2 * stats.norm.sf(3))
    save(fig, D/'samp-t-normal-tails', 'figure', {
        'densities': 'standard normal and Student t with k=1,3,10', 'two_sided_tail_at_3': tail})


def samp_f_densities():
    fig, ax = figure(width_mm=100, height_mm=46)
    x = np.linspace(0.001, 4, 800)
    pairs = [(3, 10), (9, 15), (20, 20), (40, 60)]
    for (a, b), col in zip(pairs, [BLUE, GREEN, YELLOW, PURPLE]):
        ax.plot(x, stats.f.pdf(x, a, b), color=col, label=rf'$F_{{{a},{b}}}$')
    ax.axvline(1, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(0, 4), ylim=(0, 1.6), xlabel=r'$r$', ylabel='密度')
    ax.legend(loc='upper right', handlelength=1.6)
    save(fig, D/'samp-f-densities', 'figure', {'densities': 'F distribution', 'pairs': pairs,
                                                'F_9_15_upper_0.05_quantile': float(stats.f.ppf(.95, 9, 15))})


def samp_markov_chebyshev():
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    a = np.linspace(0.5, 8, 400)
    ax.semilogy(a, np.minimum(1, 1 / a), color=BLUE, label='Markov上界')
    ax.semilogy(a, np.exp(-a), color=INK, lw=1.2, label='真实尾概率')
    ax.set(xlim=(0.5, 8), ylim=(1e-4, 1.3), xlabel=r'$a$', ylabel='尾概率')
    ax.set_title('(a) 指数分布')
    ax.legend(loc='lower left', handlelength=1.6)
    ax = axes[1]
    t = np.linspace(1, 5, 400)
    ax.semilogy(t, 1 / t**2, color=GREEN, label='Chebyshev上界')
    ax.semilogy(t, 2 * stats.norm.sf(t), color=INK, lw=1.2, label='真实尾概率')
    ax.set(xlim=(1, 5), ylim=(1e-7, 1.3), xlabel=r'$k$', ylabel='尾概率')
    ax.set_title('(b) 标准正态分布')
    ax.legend(loc='lower left', handlelength=1.6)
    save(fig, D/'samp-markov-chebyshev', 'figure', {
        'panel_a': 'X~Exponential(1); Markov bound min(1,1/a); exact exp(-a)',
        'panel_b': 'Z~N(0,1); Chebyshev 1/k**2; exact 2*(1-Phi(k))',
        'values': {'a=3': [1/3, float(np.exp(-3))], 'k=2': [0.25, float(2*stats.norm.sf(2))],
                   'k=3': [1/9, float(2*stats.norm.sf(3))]}})


def tail_prob(n, p=0.5, eps=0.05):
    k = np.arange(n + 1)
    mask = np.abs(k / n - p) >= eps - 1e-12
    return stats.binom.pmf(k, n, p)[mask].sum()


def samp_chebyshev_sample_size():
    fig, ax = figure(width_mm=100, height_mm=48)
    ns = np.arange(50, 2401, 5)
    exact = np.array([tail_prob(n) for n in ns])
    ax.semilogy(ns, np.minimum(1, 100 / ns), color=GREEN, label='Chebyshev上界')
    ax.semilogy(ns, exact, color=INK, lw=1.0, label='二项精确概率')
    ax.axhline(0.05, color=RED, lw=.7, ls='--')
    for v in (401, 2000):
        ax.axvline(v, color=MUTED, lw=.6, ls=':')
    ax.set(xlim=(50, 2400), ylim=(1e-6, 1.3), xlabel='样本量 n')
    ax.set_ylabel('失败概率')
    ax.legend(loc='lower left', handlelength=1.6)
    save(fig, D/'samp-chebyshev-sample-size', 'figure', {
        'model': 'Bernoulli(0.5), eps=0.05', 'chebyshev_bound': '1/(4 n eps^2)=100/n',
        'chebyshev_required_n_for_0.05': 2000, 'exact_tail_le_0.05_for_all_n_from': 401,
        'exact_at_400': float(tail_prob(400)), 'exact_at_2000': float(tail_prob(2000))})


def samp_running_means():
    rng = np.random.default_rng(SEED)
    N, paths = 5000, 6
    n = np.arange(1, N + 1)
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    cols = [BLUE, GREEN, YELLOW, RED, PURPLE, INK]
    ax = axes[0]
    ax.fill_between(n, 0.25, 0.35, color=GREEN_FILL, lw=0)
    finals = []
    for c in cols:
        x = rng.binomial(1, 0.3, size=N)
        r = np.cumsum(x) / n
        finals.append(float(r[-1]))
        ax.plot(n, r, color=c, lw=.7)
    ax.axhline(0.3, color=INK, lw=.6, ls='--')
    ax.set_xscale('log')
    ax.set(xlim=(1, N), ylim=(0, 1), xlabel=r'$n$', ylabel=r'$\bar X_n$')
    ax.set_title('(a) Bernoulli(0.3)')
    ax = axes[1]
    finals_c = []
    for c in cols:
        x = rng.standard_cauchy(size=N)
        r = np.cumsum(x) / n
        finals_c.append(float(r[-1]))
        ax.plot(n, r, color=c, lw=.7)
    ax.axhline(0, color=INK, lw=.6, ls='--')
    ax.set_xscale('log')
    ax.set(xlim=(1, N), ylim=(-6, 6), xlabel=r'$n$', ylabel=r'$\bar X_n$')
    ax.set_title('(b) 标准Cauchy')
    save(fig, D/'samp-running-means', 'figure', {
        'seed': SEED, 'paths_per_panel': paths, 'max_n': N, 'panel_a': 'Bernoulli(0.3), band 0.3+-0.05',
        'panel_b': 'standard Cauchy (no mean)', 'final_means_a': finals, 'final_means_b': finals_c,
        'panel_b_ylim_clipped': [-6, 6]})


def samp_bernoulli_clt():
    p = 0.3
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
    z = np.linspace(-3.5, 3.5, 600)
    gaps = {}
    for ax, n, tag in zip(axes, [10, 100], ['(a)', '(b)']):
        k = np.arange(n + 1)
        zk = (k - n * p) / np.sqrt(n * p * (1 - p))
        cdf = stats.binom.cdf(k, n, p)
        xs = np.r_[-3.5, zk, 3.5]
        ys = np.r_[0, cdf, 1]
        ax.step(xs, ys, where='post', color=BLUE, label=r'$F_{Z_n}$')
        ax.plot(z, stats.norm.cdf(z), color=INK, lw=.9, ls='--', label=r'$\Phi$')
        ax.set(xlim=(-3.5, 3.5), ylim=(-0.02, 1.02), xlabel=r'$z$')
        ax.set_title(f'{tag} n = {n}')
        grid = np.linspace(-3.5, 3.5, 7001)
        Fn = stats.binom.cdf(np.floor(n * p + grid * np.sqrt(n * p * (1 - p)) + 1e-9), n, p)
        gaps[n] = float(np.max(np.abs(Fn - stats.norm.cdf(grid))))
    axes[0].legend(loc='upper left', handlelength=1.6)
    save(fig, D/'samp-bernoulli-clt', 'figure', {
        'model': 'S_n~Bin(n,0.3), Z_n=(S_n-0.3n)/sqrt(0.21n)', 'n': [10, 100],
        'max_cdf_gap_on_grid': gaps})


def samp_normal_approximation_range():
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    ax = axes[0]
    z = np.linspace(-3.5, 4, 800)
    ax.plot(z, stats.norm.pdf(z), color=INK, lw=1.2, ls='--', label=r'$\varphi$')
    for n, col in [(1, RED), (5, YELLOW), (30, BLUE)]:
        # Z=(Xbar-1)*sqrt(n), Xbar ~ Gamma(n, rate n)
        xbar = 1 + z / np.sqrt(n)
        dens = np.where(xbar > 0, stats.gamma.pdf(np.maximum(xbar, 1e-12), a=n, scale=1 / n) / np.sqrt(n), 0)
        if n == 1:
            dens = np.where(xbar > 0, dens, np.nan)  # jump at z=-1 drawn as a gap
        ax.plot(z, dens, color=col, label=rf'$n={n}$')
    ax.set(xlim=(-3.5, 4), ylim=(0, 0.75), xlabel=r'$z$', ylabel='密度')
    ax.set_title('(a) 指数总体的标准化均值')
    ax.legend(loc='upper right', handlelength=1.6)
    ax = axes[1]
    n, p = 100, 0.02
    k = np.arange(0, 9)
    exact = stats.binom.cdf(k, n, p)
    sd = np.sqrt(n * p * (1 - p))
    plain = stats.norm.cdf((k - n * p) / sd)
    corr = stats.norm.cdf((k + 0.5 - n * p) / sd)
    ax.plot(k, exact, 'o', color=INK, ms=3, label='精确')
    ax.plot(k, plain, 's', color=RED, ms=2.6, mfc='white', label='未修正')
    ax.plot(k, corr, '^', color=BLUE, ms=2.8, mfc='white', label='连续性修正')
    ax.set(xlim=(-0.5, 8.5), ylim=(0, 1.05), xlabel=r'$k$', ylabel='累积概率')
    ax.set_title('(b) Bin(100, 0.02)')
    ax.legend(loc='lower right', handlelength=1.2)
    save(fig, D/'samp-normal-approximation-range', 'figure', {
        'panel_a': 'standardized mean of n iid Exponential(1); exact density from Gamma(n, rate n)',
        'panel_a_n': [1, 5, 30], 'panel_b': 'S~Bin(100,0.02), normal approx with/without continuity correction',
        'panel_b_exact': exact.tolist(), 'panel_b_plain': plain.tolist(), 'panel_b_corrected': corr.tolist()})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    samp_sample_proportion, samp_three_distributions, samp_shrinkage_mse, samp_chi_square_densities,
    samp_t_normal_tails, samp_f_densities, samp_markov_chebyshev, samp_chebyshev_sample_size,
    samp_running_means, samp_bernoulli_clt, samp_normal_approximation_range]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
