# coding: utf-8
"""Teaching charts for volume one, part 5, chapter 5 (intervals, tests and prediction).

Analytic curves come from scipy.stats formulas listed in the saved facts; the only
simulation (repeated confidence intervals) uses a fixed numpy seed recorded with its
sample size and parameters. The filling-machine and advertising data are teaching data
written out in the chapter text.
Run from any directory:
  python figures/01-basic-mathematics/05-probability-and-statistics-basics/matplotlib/generate_ch5.py [name ...]
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

# Teaching data used in the chapter text.
FILL_A = np.array([501.8, 499.6, 502.4, 500.9, 503.1, 501.2, 499.9, 502.6, 501.5, 502.0])
FILL_B = np.array([500.2, 498.1, 501.9, 497.6, 499.4, 502.3, 498.8, 499.7])
AD_X = np.arange(1, 9, dtype=float)
AD_Y = np.array([3.0, 4.4, 4.2, 6.0, 5.8, 7.6, 6.9, 8.9])


def pred_coverage_simulation():
    """Fifty repeated 95% t intervals from N(500, 1.5^2) samples of size 10."""
    rng = np.random.default_rng(SEED)
    mu, sigma, n, reps = 500.0, 1.5, 10, 50
    X = rng.normal(mu, sigma, size=(reps, n))
    m, s = X.mean(1), X.std(1, ddof=1)
    h = stats.t.ppf(0.975, n - 1) * s / np.sqrt(n)
    lo, hi = m - h, m + h
    miss = (lo > mu) | (hi < mu)
    fig, ax = figure(width_mm=112, height_mm=56)
    k = np.arange(1, reps + 1)
    for i in range(reps):
        c = RED if miss[i] else BLUE
        ax.plot([k[i], k[i]], [lo[i], hi[i]], color=c, lw=1.1 if miss[i] else .9)
        ax.plot([k[i]], [m[i]], 'o', color=c, ms=1.8)
    ax.axhline(mu, color=INK, lw=.75, ls='--')
    ax.text(reps + 1.2, mu + 0.12, r'$\mu$', va='bottom', ha='center', color=INK)
    ax.set(xlim=(0, reps + 2), ylim=(497.2, 503.0), xlabel='重复抽样的序号', ylabel='区间端点')
    ax.set_xticks([1, 10, 20, 30, 40, 50])
    save(fig, D/'pred-coverage-simulation', 'figure', {
        'seed': SEED, 'population': 'Normal(500, 1.5^2)', 'n': n, 'repetitions': reps,
        'interval': 'mean +- t_{9,0.975} S/sqrt(n)', 't_quantile': float(stats.t.ppf(0.975, n - 1)),
        'misses': [int(i) for i in k[miss]], 'number_of_misses': int(miss.sum())})


def pred_proportion_coverage():
    """Exact coverage of Wald and Clopper-Pearson intervals for n = 30."""
    n, alpha = 30, 0.05
    z = stats.norm.ppf(1 - alpha / 2)
    s = np.arange(n + 1)
    ph = s / n
    w = z * np.sqrt(ph * (1 - ph) / n)
    wl, wu = ph - w, ph + w
    cl = np.where(s == 0, 0.0, stats.beta.ppf(alpha / 2, np.maximum(s, 1), n - s + 1))
    cu = np.where(s == n, 1.0, stats.beta.ppf(1 - alpha / 2, s + 1, np.maximum(n - s, 1)))
    p = np.linspace(0.005, 0.995, 991)
    pmf = stats.binom.pmf(s[None, :], n, p[:, None])
    cov_w = (pmf * ((wl[None, :] <= p[:, None]) & (p[:, None] <= wu[None, :]))).sum(1)
    cov_c = (pmf * ((cl[None, :] <= p[:, None]) & (p[:, None] <= cu[None, :]))).sum(1)
    fig, ax = figure(width_mm=112, height_mm=50)
    ax.plot(p, cov_w, color=RED, lw=.8, label='Wald')
    ax.plot(p, cov_c, color=BLUE, lw=.8, label='Clopper–Pearson')
    ax.axhline(1 - alpha, color=INK, lw=.6, ls='--')
    ax.set(xlim=(0, 1), ylim=(0.5, 1.005), xlabel=r'$p$', ylabel='实际覆盖概率')
    ax.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0])
    ax.legend(loc='lower center', ncol=2, handlelength=1.6)
    save(fig, D/'pred-proportion-coverage', 'figure', {
        'n': n, 'alpha': alpha, 'p_grid': 'linspace(0.005,0.995,991)',
        'coverage': 'sum_s binom.pmf(s;n,p) * 1{p in C(s)}, computed exactly',
        'wald_min': float(cov_w.min()), 'cp_min': float(cov_c.min()),
        'wald_at_p_0.05': float(cov_w[np.argmin(abs(p - 0.05))]),
        'cp_at_p_0.05': float(cov_c[np.argmin(abs(p - 0.05))])})


def pred_error_types():
    """Sampling distributions of the z statistic under H0 and one alternative."""
    alpha, n, d = 0.05, 10, 1 / 1.5
    c = stats.norm.ppf(1 - alpha)
    delta = np.sqrt(n) * d
    x = np.linspace(-3.5, 6, 1000)
    f0, f1 = stats.norm.pdf(x), stats.norm.pdf(x, delta)
    fig, ax = figure(width_mm=112, height_mm=50)
    ax.plot(x, f0, color=BLUE)
    ax.plot(x, f1, color=GREEN)
    ax.fill_between(x, f0, where=x >= c, color=BLUE, alpha=1, lw=0)
    ax.fill_between(x, f1, where=x <= c, color=GREEN_FILL, lw=0)
    ax.plot(x[x <= c], f1[x <= c], color=GREEN)
    ax.axvline(c, color=INK, lw=.75, ls='--')
    ax.annotate('', xy=(5.8, 0.43), xytext=(c, 0.43), arrowprops=dict(arrowstyle='->', color=INK, lw=.75))
    ax.text((c + 5.8) / 2, 0.445, '拒绝域', ha='center', color=INK)
    ax.text(-0.9, 0.36, r'$H_0:\ \mu=\mu_0$', color=BLUE, ha='right')
    ax.text(delta + 0.75, 0.36, r'$\mu=\mu_1$', color=GREEN, ha='left')
    ax.annotate(r'$\alpha$', xy=(2.0, 0.02), xytext=(2.6, 0.12), color=INK,
                arrowprops=dict(arrowstyle='-', color=INK, lw=.6))
    ax.text(1.05, 0.08, r'$\beta$', color=INK, ha='center')
    ax.set(xlim=(-3.5, 6), ylim=(0, 0.48), xlabel=r'$Z=\sqrt{n}(\bar X-\mu_0)/\sigma$', ylabel='密度')
    ax.text(c + 0.08, 0.3, r'$z_{0.95}$', ha='left', color=INK)
    save(fig, D/'pred-error-types', 'figure', {
        'test': 'one-sided z test, reject when Z > z_{0.95}', 'alpha': alpha, 'critical_value': float(c),
        'n': n, 'effect_size_d': d, 'mean_shift_sqrt_n_d': float(delta),
        'beta': float(stats.norm.cdf(c - delta)), 'power': float(stats.norm.sf(c - delta))})


def pred_power_curves():
    """Power of the one-sided z test against standardized effect size for several n."""
    alpha = 0.05
    c = stats.norm.ppf(1 - alpha)
    d = np.linspace(-0.25, 1.5, 600)
    fig, ax = figure(width_mm=112, height_mm=50)
    facts = {'test': 'one-sided z test, H0: mu<=mu0', 'alpha': alpha,
             'power': 'Phi(sqrt(n) d - z_{0.95}), d=(mu-mu0)/sigma'}
    for n, col, ls in [(5, YELLOW, '-'), (10, BLUE, '-'), (20, GREEN, '-'), (50, PURPLE, '-')]:
        pw = stats.norm.cdf(np.sqrt(n) * d - c)
        ax.plot(d, pw, color=col, ls=ls, label=rf'$n={n}$')
        facts[f'power_at_d_2/3_n={n}'] = float(stats.norm.cdf(np.sqrt(n) * 2 / 3 - c))
    ax.axhline(alpha, color=MUTED, lw=.6, ls='--')
    ax.axvline(0, color=MUTED, lw=.6)
    ax.axvline(2 / 3, color=INK, lw=.6, ls=':')
    ax.set(xlim=(-0.25, 1.5), ylim=(0, 1.02), xlabel=r'$d=(\mu-\mu_0)/\sigma$', ylabel='功效（拒绝概率）')
    ax.set_yticks([0.05, 0.25, 0.5, 0.75, 1])
    ax.legend(loc='lower right', handlelength=1.6)
    save(fig, D/'pred-power-curves', 'figure', facts)


def pred_p_value_tail():
    """Two-sided p value of machine B's t statistic as a tail area of t_7."""
    m, s, n = FILL_B.mean(), FILL_B.std(ddof=1), len(FILL_B)
    t_obs = (m - 500) / (s / np.sqrt(n))
    k = n - 1
    x = np.linspace(-4.5, 4.5, 900)
    f = stats.t.pdf(x, k)
    crit = stats.t.ppf(0.975, k)
    fig, ax = figure(width_mm=112, height_mm=46)
    ax.plot(x, f, color=BLUE)
    ax.fill_between(x, f, where=np.abs(x) >= abs(t_obs), color=BLUE_FILL, lw=0)
    ax.axvline(t_obs, color=INK, lw=.75)
    ax.axvline(-t_obs, color=INK, lw=.75, ls=':')
    for sgn in (-1, 1):
        ax.axvline(sgn * crit, color=RED, lw=.6, ls='--')
    ax.text(t_obs - 0.12, 0.405, r'$t_{\mathrm{obs}}$', ha='right', color=INK)
    ax.text(crit + 0.1, 0.25, r'$t_{7,0.975}$', ha='left', color=RED)
    ax.set(xlim=(-4.5, 4.5), ylim=(0, 0.43), xlabel=r'$t$', ylabel='密度')
    save(fig, D/'pred-p-value-tail', 'figure', {
        'data': FILL_B.tolist(), 'H0': 'mu=500, two-sided', 'mean': float(m), 'S': float(s),
        't_obs': float(t_obs), 'df': k, 'p_value': float(2 * stats.t.sf(abs(t_obs), k)),
        'critical_value_0.975': float(crit)})


def pred_binomial_test():
    """Exact Bin(40,0.05) null distribution, rejection region and normal approximation."""
    n, p0, s_obs = 40, 0.05, 6
    k = np.arange(0, 11)
    pmf = stats.binom.pmf(k, n, p0)
    fig, ax = figure(width_mm=112, height_mm=48)
    rej = k >= 5
    ax.bar(k[~rej], pmf[~rej], width=.7, color=BLUE_FILL, edgecolor=BLUE, lw=.5, label='不拒绝')
    ax.bar(k[rej], pmf[rej], width=.7, color=RED_FILL, edgecolor=RED, lw=.5, label='拒绝域')
    xx = np.linspace(-0.5, 10.5, 600)
    mu, sd = n * p0, np.sqrt(n * p0 * (1 - p0))
    ax.plot(xx, stats.norm.pdf(xx, mu, sd), color=INK, lw=.8, ls='--', label='正态近似')
    ax.annotate(r'$s=6$', xy=(s_obs, pmf[s_obs] + 0.004), xytext=(s_obs + 1.4, 0.09), color=INK,
                arrowprops=dict(arrowstyle='->', color=INK, lw=.6))
    ax.set(xlim=(-0.6, 10.6), ylim=(0, 0.3), xlabel=r'$s$', ylabel='概率')
    ax.set_xticks(k)
    ax.legend(loc='upper right', handlelength=1.4)
    save(fig, D/'pred-binomial-test', 'figure', {
        'null': 'Bin(40,0.05)', 'rejection_region': 's>=5', 'size': float(stats.binom.sf(4, n, p0)),
        'size_if_s>=4': float(stats.binom.sf(3, n, p0)), 's_obs': s_obs,
        'exact_p': float(stats.binom.sf(s_obs - 1, n, p0)),
        'normal_approx': {'mean': mu, 'sd': float(sd), 'z': float((s_obs - mu) / sd),
                          'p': float(stats.norm.sf((s_obs - mu) / sd))}})


def pred_test_interval_duality():
    """p value function of the two-sided t test for the filling data."""
    m, s, n = FILL_A.mean(), FILL_A.std(ddof=1), len(FILL_A)
    se = s / np.sqrt(n)
    mu0 = np.linspace(499.3, 503.7, 900)
    pv = 2 * stats.t.sf(np.abs(m - mu0) / se, n - 1)
    h = stats.t.ppf(0.975, n - 1) * se
    fig, ax = figure(width_mm=112, height_mm=48)
    ax.plot(mu0, pv, color=BLUE)
    ax.axhline(0.05, color=RED, lw=.6, ls='--')
    ax.fill_between([m - h, m + h], 0, 0.05, color=BLUE_FILL, lw=0)
    ax.plot([m - h, m + h], [0, 0], color=BLUE, lw=2.2, solid_capstyle='butt')
    p500 = 2 * stats.t.sf(abs(m - 500) / se, n - 1)
    ax.plot([500], [p500], 'o', color=RED, ms=3)
    ax.annotate(r'$\mu_0=500$', xy=(500, p500), xytext=(499.5, 0.3), color=RED,
                arrowprops=dict(arrowstyle='->', color=RED, lw=.6))
    ax.text(503.6, 0.065, r'$\alpha=0.05$', ha='right', color=RED)
    ax.set(xlim=(499.3, 503.7), ylim=(0, 1.04), xlabel=r'$\mu_0$', ylabel='p 值')
    save(fig, D/'pred-test-interval-duality', 'figure', {
        'data': FILL_A.tolist(), 'mean': float(m), 'S': float(s), 'se': float(se),
        'p_function': '2*(1-F_{t_9}(|xbar-mu0|/se))', 'interval_95': [float(m - h), float(m + h)],
        'p_at_500': float(p500)})


def pred_interval_widths():
    """Half widths of the known-sigma mean interval and prediction interval versus n."""
    sigma, z = 1.5, stats.norm.ppf(0.975)
    n = np.arange(2, 201)
    fig, ax = figure(width_mm=112, height_mm=48)
    ax.plot(n, z * sigma / np.sqrt(n), color=BLUE, label=r'$z_{0.975}\sigma/\sqrt{n}$')
    ax.plot(n, z * sigma * np.sqrt(1 + 1 / n), color=GREEN, ls='--', label=r'$z_{0.975}\sigma\sqrt{1+1/n}$')
    ax.axhline(z * sigma, color=MUTED, lw=.6, ls=':')
    ax.axvline(10, color=MUTED, lw=.6)
    ax.set_xscale('log')
    ax.set(xlim=(2, 200), ylim=(0, 3.8), xlabel=r'$n$', ylabel='半宽')
    ax.set_xticks([2, 5, 10, 20, 50, 100, 200]); ax.set_xticklabels(['2', '5', '10', '20', '50', '100', '200'])
    ax.legend(loc='center right', handlelength=1.8)
    save(fig, D/'pred-interval-widths', 'figure', {
        'sigma': sigma, 'z': float(z), 'mean_half_width': 'z*sigma/sqrt(n)',
        'prediction_half_width': 'z*sigma*sqrt(1+1/n)', 'limit': float(z * sigma),
        'at_n_10': [float(z * sigma / np.sqrt(10)), float(z * sigma * np.sqrt(1.1))]})


def pred_posterior_predictive():
    """Prior, posterior of mu and posterior predictive for the filling data (sigma known)."""
    sigma2, mu0, tau0 = 2.25, 500.0, 1.0
    n, m = len(FILL_A), FILL_A.mean()
    prec = 1 / tau0**2 + n / sigma2
    tn2 = 1 / prec
    mn = tn2 * (mu0 / tau0**2 + n * m / sigma2)
    x = np.linspace(495, 507, 1200)
    fig, ax = figure(width_mm=112, height_mm=50)
    ax.plot(x, stats.norm.pdf(x, mu0, tau0), color=MUTED, ls=':', label='先验')
    ax.plot(x, stats.norm.pdf(x, mn, np.sqrt(tn2)), color=BLUE, label='后验')
    ax.plot(x, stats.norm.pdf(x, mn, np.sqrt(sigma2 + tn2)), color=GREEN, ls='--', label='后验预测')
    ax.plot(FILL_A, np.full_like(FILL_A, 0.02), '|', color=INK, ms=6)
    ax.set(xlim=(495, 507), ylim=(0, 1.0), xlabel=r'$\mu,\ x_{\mathrm{new}}$', ylabel='密度')
    ax.legend(loc='upper right', handlelength=1.8)
    save(fig, D/'pred-posterior-predictive', 'figure', {
        'data': FILL_A.tolist(), 'sigma2_known': sigma2, 'prior': [mu0, tau0**2],
        'posterior_mean': float(mn), 'posterior_var': float(tn2),
        'predictive_var': float(sigma2 + tn2), 'rug': 'observations at y=0.02'})


def pred_regression_bands():
    """Teaching regression data: fit, 95% mean band, 95% prediction band, residuals."""
    x, y = AD_X, AD_Y
    n = len(x)
    xb, yb = x.mean(), y.mean()
    Sxx = ((x - xb)**2).sum(); Sxy = ((x - xb) * (y - yb)).sum()
    b1 = Sxy / Sxx; b0 = yb - b1 * xb
    r = y - (b0 + b1 * x)
    s = np.sqrt((r**2).sum() / (n - 2))
    t = stats.t.ppf(0.975, n - 2)
    g = np.linspace(0, 10, 500)
    mu = b0 + b1 * g
    hm = t * s * np.sqrt(1 / n + (g - xb)**2 / Sxx)
    hp = t * s * np.sqrt(1 + 1 / n + (g - xb)**2 / Sxx)
    fig, axes = figure(width_mm=160, height_mm=56, ncols=2, gridspec_kw={'width_ratios': [1.6, 1]})
    ax = axes[0]
    ax.axvspan(8, 10, color='#F4F5F7', lw=0)
    ax.axvspan(0, 1, color='#F4F5F7', lw=0)
    ax.fill_between(g, mu - hp, mu + hp, color=GREEN_FILL, lw=0, label='95% 预测带')
    ax.fill_between(g, mu - hm, mu + hm, color=BLUE_FILL, lw=0, label='95% 均值置信带')
    ax.plot(g, mu - hp, color=GREEN, lw=.6, ls='--'); ax.plot(g, mu + hp, color=GREEN, lw=.6, ls='--')
    ax.plot(g, mu, color=BLUE, label='拟合直线')
    ax.plot(x, y, 'o', color=INK, ms=3)
    ax.axvline(xb, color=MUTED, lw=.6, ls=':')
    ax.text(9, 1.0, '外推', ha='center', color=MUTED, fontsize=7.5)
    ax.set(xlim=(0, 10), ylim=(0, 13), xlabel='广告投入（万元）', ylabel='销量（百件）', title='(a) 拟合与两种区间带')
    ax.legend(loc='upper left', handlelength=1.6)
    ax = axes[1]
    ax.axhline(0, color=MUTED, lw=.6)
    ax.plot(x, r, 'o', color=BLUE, ms=3)
    for xi, ri in zip(x, r):
        ax.plot([xi, xi], [0, ri], color=BLUE, lw=.6)
    ax.set(xlim=(0.3, 8.7), ylim=(-1.1, 1.1), xlabel='广告投入（万元）', ylabel='残差', title='(b) 残差')
    ax.set_xticks(range(1, 9))
    save(fig, D/'pred-regression-bands', 'figure', {
        'x': x.tolist(), 'y': y.tolist(), 'b0': float(b0), 'b1': float(b1), 's': float(s), 't_6_0.975': float(t),
        'mean_band': 'b0+b1 x0 +- t s sqrt(1/n+(x0-xbar)^2/Sxx)',
        'prediction_band': 'b0+b1 x0 +- t s sqrt(1+1/n+(x0-xbar)^2/Sxx)',
        'extrapolation_region': [[0, 1], [8, 10]], 'residuals': r.round(4).tolist()})


def pred_exponential_coverage():
    """Facts only (no chart): simulated coverage of nominal 95% t and chi-square intervals
    for Exponential(1) samples, quoted in the chapter text."""
    import json
    rng = np.random.default_rng(SEED)
    reps, out = 200000, {}
    for n in [5, 10, 30, 100]:
        X = rng.exponential(1.0, size=(reps, n))
        m, s = X.mean(1), X.std(1, ddof=1)
        h = stats.t.ppf(0.975, n - 1) * s / np.sqrt(n)
        ss = ((X - m[:, None])**2).sum(1)
        lo, hi = ss / stats.chi2.ppf(0.975, n - 1), ss / stats.chi2.ppf(0.025, n - 1)
        out[str(n)] = {'t_mean_coverage': float(np.mean(np.abs(m - 1) <= h)),
                       'mu_above_upper': float(np.mean(m + h < 1)), 'mu_below_lower': float(np.mean(m - h > 1)),
                       'chi2_variance_coverage': float(np.mean((lo <= 1) & (1 <= hi)))}
    out['chi2_asymptotic_coverage'] = float(2 * stats.norm.cdf(stats.norm.ppf(0.975) / 2) - 1)
    d = D/'pred-exponential-coverage'; d.mkdir(exist_ok=True)
    (d/'facts.json').write_text(json.dumps({'seed': SEED, 'population': 'Exponential(rate 1), mean 1, variance 1',
        'repetitions': reps, 'results': out}, indent=2) + '\n')


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    pred_coverage_simulation, pred_proportion_coverage, pred_error_types, pred_power_curves,
    pred_p_value_tail, pred_binomial_test, pred_test_interval_duality, pred_interval_widths,
    pred_posterior_predictive, pred_regression_bands, pred_exponential_coverage]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
