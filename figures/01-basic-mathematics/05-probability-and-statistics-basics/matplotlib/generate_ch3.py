# coding: utf-8
"""Teaching charts for volume one, part 5, chapter 3 (samples, statistics and estimation).

All data are small teaching examples written out below; every curve is an explicit
formula of these data.  No random simulation is used.
Run from any directory:
  python figures/01-basic-mathematics/05-probability-and-statistics-basics/matplotlib/generate_ch3.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from scipy import stats

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL

D = Path(__file__).resolve().parent

# Teaching data used throughout the chapter.
READINGS = np.array([9.8, 10.1, 10.0, 10.3, 10.1, 9.9, 10.4, 10.2])   # length readings in mm
DEFECTS = np.array([0, 0, 1, 0, 0, 0, 1, 0, 0, 0])                    # 1 = defective
SIGMA_KNOWN = 0.2
PRIOR_MU, PRIOR_TAU = 10.0, 0.1


def ecdf_values(x, t):
    return np.array([(x <= s).mean() for s in t])


def est_empirical_cdf():
    fig, ax = figure(width_mm=104, height_mm=52)
    xs = np.sort(READINGS)
    pts = np.unique(xs)
    t = np.linspace(9.55, 10.65, 800)
    ax.plot(t, stats.norm.cdf(t, 10.0, 0.2), color=MUTED, lw=1.0, ls='--', label=r'$F(t)$')
    lo = 9.55
    levels = [0.0] + [ecdf_values(xs, [p])[0] for p in pts]
    edges = [lo] + list(pts) + [10.65]
    for k in range(len(levels)):
        ax.plot([edges[k], edges[k+1]], [levels[k], levels[k]], color=BLUE, lw=1.3,
                label=r'$\hat F_8(t)$' if k == 0 else None)
    for k, p in enumerate(pts):
        ax.plot([p], [levels[k+1]], 'o', color=BLUE, ms=3.2)
        ax.plot([p], [levels[k]], 'o', mfc='white', mec=BLUE, ms=3.2)
    ax.annotate('', xy=(10.1, levels[4]), xytext=(10.1, levels[3]),
                arrowprops=dict(arrowstyle='<->', color=RED, lw=.8))
    ax.text(10.115, (levels[3]+levels[4])/2 - 0.02, r'$2/8$', color=RED, fontsize=7.5)
    ax.set(xlim=(9.55, 10.65), ylim=(-0.04, 1.06), xlabel=r'$t$ (mm)', ylabel='累计频率与累计概率')
    ax.set_xticks(pts); ax.set_xticklabels([f'{p:.1f}' for p in pts])
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.grid(axis='y')
    ax.legend(loc='upper left', handlelength=1.8)
    save(fig, D/'est-empirical-cdf', 'figure', {
        'data_mm': READINGS.tolist(), 'n': 8, 'distinct_values': pts.tolist(),
        'ecdf_levels': levels, 'repeated_value': 10.1, 'jump_at_repeated_value': 0.25,
        'reference_population_cdf': 'normal CDF, mean 10.0, sd 0.2 (assumed for illustration only)'})


def est_sample_quantiles():
    fig, ax = figure(width_mm=104, height_mm=54)
    xs = np.sort(READINGS); n = len(xs)
    p = np.linspace(0.001, 0.999, 2000)
    inv = np.quantile(xs, p, method='inverted_cdf')
    lin = np.quantile(xs, p, method='linear')
    ax.plot(p, inv, color=BLUE, lw=1.3, label='广义逆')
    ax.plot(p, lin, color=GREEN, lw=1.1, ls='--', label='线性插值')
    for k in range(n):
        ax.plot([(k+1)/n], [xs[k]], 'o', color=BLUE, ms=2.8)
        ax.plot([k/(n-1)], [xs[k]], 's', color=GREEN, ms=2.6)
    q = {'inverted_cdf': 9.9, 'averaged_inverted_cdf': 9.95, 'linear': 9.975}
    ax.axvline(0.25, color=MUTED, lw=.6, ls=':')
    ax.plot([0.25], [9.95], 'D', color=RED, ms=3.2, label='跳跃处取中点')
    ax.set(xlim=(0, 1), ylim=(9.72, 10.48), xlabel=r'$p$', ylabel=r'$\hat q_p$ (mm)')
    ax.set_xticks([0, .25, .5, .75, 1])
    ax.set_yticks(np.unique(xs))
    ax.grid(axis='y')
    ax.legend(loc='upper left', handlelength=1.8)
    save(fig, D/'est-sample-quantiles', 'figure', {
        'data_mm': READINGS.tolist(), 'sorted': xs.tolist(),
        'generalized_inverse': 'q_p = x_(k) for (k-1)/n < p <= k/n (numpy inverted_cdf)',
        'linear_interpolation': 'h=(n-1)p+1, q_p=x_(floor h)+(h-floor h)(x_(floor h+1)-x_(floor h)) (numpy linear)',
        'p_0.25_values': q, 'median_all_conventions': 10.1})


def est_bernoulli_loglik():
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
    p = np.linspace(0.002, 0.998, 1000)
    n = 10
    for ax, k, title in [(axes[0], 2, r'$n=10,\ k=2$'), (axes[1], 0, r'$n=10,\ k=0$')]:
        ell = k*np.log(p) + (n-k)*np.log(1-p)
        ax.plot(p, ell, color=BLUE)
        ph = k/n
        if 0 < ph < 1:
            m = k*np.log(ph) + (n-k)*np.log(1-ph)
            ax.plot([ph], [m], 'o', color=RED, ms=3.2)
            ax.axvline(ph, color=MUTED, lw=.6, ls='--')
            ax.text(ph+0.03, m-3, r'$\hat p=0.2$', color=RED, fontsize=7.5)
        else:
            ax.plot([0], [0], 'o', mfc='white', mec=RED, ms=3.4, clip_on=False)
            ax.text(0.22, -1.6, r'$\ell(p)\to 0\ (p\to 0)$', color=RED, fontsize=7.5)
        ax.set(xlim=(0, 1), ylim=(-25, 1), xlabel=r'$p$', title=title)
        ax.set_xticks([0, .2, .5, 1])
    axes[0].set_ylabel(r'$\ell(p)$')
    save(fig, D/'est-bernoulli-loglik', 'figure', {
        'log_likelihood': 'k log p + (n-k) log(1-p)', 'n': n, 'k_panels': [2, 0],
        'mle': {'k=2': 0.2, 'k=0': 'boundary p=0 (sup 0, attained only if 0 is in parameter set)'},
        'data_k2': DEFECTS.tolist(), 'y_clip': [-25, 1]})


def est_gaussian_contours():
    fig, ax = figure(width_mm=100, height_mm=62)
    x = READINGS; n = len(x)
    mu = np.linspace(9.85, 10.35, 300)
    sg = np.linspace(0.09, 0.42, 300)
    M, Sg = np.meshgrid(mu, sg)
    ss = ((x[None, None, :] - M[..., None])**2).sum(-1)
    ell = -n*np.log(Sg) - ss/(2*Sg**2) - n/2*np.log(2*np.pi)
    muh, sh = x.mean(), np.sqrt(x.var())
    lmax = -n*np.log(sh) - n/2 - n/2*np.log(2*np.pi)
    levels = lmax - np.array([8, 4, 2, 1, 0.5])
    cs = ax.contour(M, Sg, ell, levels=levels, colors=[BLUE], linewidths=.8, linestyles='solid')
    ax.clabel(cs, levels=levels[1:], fmt={lv: f'{lv-lmax:.1f}' for lv in levels}, fontsize=6.5, inline_spacing=2)
    prof = np.sqrt(((x - muh)**2).mean())
    ax.plot([muh], [sh], 'o', color=RED, ms=3.6)
    ax.text(muh+0.012, sh-0.025, r'$(\hat\mu,\hat\sigma)$', color=RED, fontsize=7.5)
    ax.axvline(muh, color=MUTED, lw=.6, ls='--')
    ax.set(xlim=(9.85, 10.35), ylim=(0.09, 0.42), xlabel=r'$\mu$ (mm)', ylabel=r'$\sigma$ (mm)')
    save(fig, D/'est-gaussian-contours', 'figure', {
        'data_mm': x.tolist(), 'log_likelihood': '-n log sigma - sum (x_i-mu)^2/(2 sigma^2) - n/2 log(2 pi)',
        'mle': {'mu': float(muh), 'sigma': float(sh), 'sigma2': float(x.var())},
        'contour_levels_relative_to_max': [-8, -4, -2, -1, -0.5], 'profile_sigma': float(prof)})


def est_unbounded_likelihood():
    fig, ax = figure(width_mm=100, height_mm=50)
    s = np.linspace(0.005, 0.6, 1200)
    same = np.array([10.0, 10.0, 10.0])
    other = np.array([9.9, 10.0, 10.1])
    for x, c, lab in [(other, BLUE, '9.9, 10.0, 10.1'), (same, RED, '10.0, 10.0, 10.0')]:
        n = len(x); m = x.mean(); ssq = ((x-m)**2).sum()
        ell = -n*np.log(s) - ssq/(2*s**2) - n/2*np.log(2*np.pi)
        ax.plot(s, ell, color=c, label=lab)
        if ssq > 0:
            sh = np.sqrt(ssq/n)
            ax.plot([sh], [-n*np.log(sh) - n/2 - n/2*np.log(2*np.pi)], 'o', color=c, ms=3.2)
    ax.set(xlim=(0, 0.6), ylim=(-6, 14), xlabel=r'$\sigma$', ylabel=r'$\ell(\bar x,\sigma)$')
    ax.legend(loc='upper right', handlelength=1.8)
    save(fig, D/'est-unbounded-likelihood', 'figure', {
        'samples': {'distinct': other.tolist(), 'all_equal': same.tolist()},
        'curve': 'profile log-likelihood at mu = sample mean: -n log s - SS/(2 s^2) - n/2 log(2 pi)',
        'distinct_max_sigma': float(np.sqrt(0.02/3)), 'all_equal': 'SS=0, ell -> +inf as s -> 0',
        'y_clip': [-6, 14]})


def est_beta_updating():
    fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
    p = np.linspace(0.0005, 0.9995, 1200)
    n, k = 10, 2
    for ax, (a, b) in zip(axes, [(1, 1), (2, 18)]):
        prior = stats.beta(a, b); post = stats.beta(a+k, b+n-k)
        lik = stats.beta(k+1, n-k+1)  # normalized likelihood
        ax.plot(p, prior.pdf(p), color=MUTED, ls='--', lw=1.0, label='先验')
        ax.plot(p, lik.pdf(p), color=GREEN, ls=':', lw=1.1, label='似然')
        ax.plot(p, post.pdf(p), color=BLUE, lw=1.3, label='后验')
        ax.set(xlim=(0, 0.7), ylim=(0, 8.5), xlabel=r'$p$')
        ax.set_title(rf'$\mathrm{{Beta}}({a},{b})\to\mathrm{{Beta}}({a+k},{b+n-k})$')
        ax.set_xticks([0, .1, .2, .4, .6])
    axes[0].set_ylabel('密度')
    axes[0].legend(loc='upper right', handlelength=1.8)
    save(fig, D/'est-beta-updating', 'figure', {
        'data': DEFECTS.tolist(), 'n': n, 'k': k,
        'panels': [{'prior': [1, 1], 'posterior': [3, 9], 'posterior_mean': 0.25},
                   {'prior': [2, 18], 'posterior': [4, 26], 'posterior_mean': 4/30}],
        'likelihood_curve': 'p**k (1-p)**(n-k) normalized to integrate to 1, i.e. Beta(k+1, n-k+1) density'})


def est_gaussian_posterior():
    fig, ax = figure(width_mm=104, height_mm=50)
    n = len(READINGS); xbar = READINGS.mean()
    prec = 1/PRIOR_TAU**2 + n/SIGMA_KNOWN**2
    pm = (PRIOR_MU/PRIOR_TAU**2 + n*xbar/SIGMA_KNOWN**2)/prec
    ps = np.sqrt(1/prec)
    ls_ = SIGMA_KNOWN/np.sqrt(n)
    m = np.linspace(9.65, 10.45, 900)
    ax.plot(m, stats.norm.pdf(m, PRIOR_MU, PRIOR_TAU), color=MUTED, ls='--', lw=1.0, label='先验')
    ax.plot(m, stats.norm.pdf(m, xbar, ls_), color=GREEN, ls=':', lw=1.1, label='似然')
    ax.plot(m, stats.norm.pdf(m, pm, ps), color=BLUE, lw=1.3, label='后验')
    for v, c in [(PRIOR_MU, MUTED), (xbar, GREEN), (pm, BLUE)]:
        ax.axvline(v, color=c, lw=.6, ls='-', alpha=.8)
    ax.set(xlim=(9.65, 10.45), ylim=(0, 7.8), xlabel=r'$\mu$ (mm)', ylabel='密度')
    ax.set_xticks([9.7, 9.9, 10.0, 10.1, 10.3])
    ax.legend(loc='upper left', handlelength=1.8)
    save(fig, D/'est-gaussian-posterior', 'figure', {
        'data_mm': READINGS.tolist(), 'known_sigma': SIGMA_KNOWN, 'prior': [PRIOR_MU, PRIOR_TAU],
        'likelihood_curve': 'normal density in mu, mean xbar=10.1, sd sigma/sqrt(n)',
        'posterior': {'mean': float(pm), 'sd': float(ps), 'precision': float(prec)}})


def est_posterior_summaries():
    fig, ax = figure(width_mm=104, height_mm=48)
    a, b = 3, 9
    d = stats.beta(a, b)
    p = np.linspace(0, 0.8, 1000)
    ax.fill_between(p, d.pdf(p), color=BLUE_FILL, lw=0)
    ax.plot(p, d.pdf(p), color=BLUE)
    mode, med, mean = (a-1)/(a+b-2), d.median(), d.mean()
    for v, c, ls, lab in [(mode, RED, '-', '众数'), (med, GREEN, '--', '中位数'), (mean, PURPLE, ':', '均值')]:
        ax.plot([v, v], [0, d.pdf(v)], color=c, ls=ls, lw=1.1, label=f'{lab} {v:.3f}')
    ax.set(xlim=(0, 0.8), ylim=(0, 3.6), xlabel=r'$p$', ylabel='后验密度')
    ax.set_xticks([0, .2, .4, .6, .8])
    ax.legend(loc='upper right', handlelength=1.8)
    save(fig, D/'est-posterior-summaries', 'figure', {
        'posterior': 'Beta(3,9)', 'mode': mode, 'median': float(med), 'mean': mean})


ALL = [est_empirical_cdf, est_sample_quantiles, est_bernoulli_loglik, est_gaussian_contours,
       est_unbounded_likelihood, est_beta_updating, est_gaussian_posterior, est_posterior_summaries]

if __name__ == '__main__':
    wanted = set(sys.argv[1:])
    for f in ALL:
        if not wanted or f.__name__ in wanted:
            f()
