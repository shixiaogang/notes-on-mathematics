# coding: utf-8
"""Teaching charts for volume one, part 5, chapter 2 (random vectors and joint distributions).

Analytic curves are listed in the saved facts. Simulated panels use numpy's
default_rng with the seed, sample size and parameters recorded in each JSON file.
Run from any directory:
  python3 figures/01-basic-mathematics/05-probability-and-statistics-basics/matplotlib/generate_ch2.py [name ...]
"""
from pathlib import Path
from math import factorial, sqrt, pi, exp
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL

D = Path(__file__).resolve().parent


def phi(x, m=0.0, s=1.0):
    return np.exp(-0.5*((x-m)/s)**2)/(s*sqrt(2*pi))


def ellipse(ax, mu, cov, c, **kw):
    w, V = np.linalg.eigh(np.asarray(cov, float))
    t = np.linspace(0, 2*pi, 400)
    circ = np.vstack([np.cos(t), np.sin(t)])
    pts = (V @ np.diag(np.sqrt(w)) @ circ)*c + np.asarray(mu, float)[:, None]
    ax.plot(pts[0], pts[1], **kw)


def rvec_same_marginals():
    seed, n = 20261028, 1500
    rng = np.random.default_rng(seed)
    x_ind = rng.standard_normal(n); y_ind = rng.standard_normal(n)
    z = rng.standard_normal(n); s = rng.choice([-1.0, 1.0], size=n)
    x_dep, y_dep = z, s*z
    fig = figure(width_mm=112, height_mm=60)[0]
    fig.clf()
    gs = fig.add_gridspec(2, 4, height_ratios=[1, 3.2], width_ratios=[3.2, 1, 3.2, 1])
    bins = np.linspace(-3.5, 3.5, 29)
    grid = np.linspace(-3.5, 3.5, 300)
    for k, (x, y, title, col) in enumerate([(x_ind, y_ind, '(a) 两分量独立', BLUE), (x_dep, y_dep, '(b) 第二分量随机变号', GREEN)]):
        main = fig.add_subplot(gs[1, 2*k])
        top = fig.add_subplot(gs[0, 2*k], sharex=main)
        right = fig.add_subplot(gs[1, 2*k+1], sharey=main)
        main.scatter(x, y, s=1.6, color=col, alpha=.55, lw=0)
        main.set(xlim=(-3.5, 3.5), ylim=(-3.5, 3.5), xlabel=r'$X$', ylabel=r'$Y$')
        main.set_xticks([-3, 0, 3]); main.set_yticks([-3, 0, 3])
        main.set_aspect('equal', adjustable='box')
        top.hist(x, bins=bins, density=True, color=BLUE_FILL if k == 0 else GREEN_FILL, edgecolor=col, lw=.4)
        top.plot(grid, phi(grid), color=INK, lw=.8)
        right.hist(y, bins=bins, density=True, orientation='horizontal', color=BLUE_FILL if k == 0 else GREEN_FILL, edgecolor=col, lw=.4)
        right.plot(phi(grid), grid, color=INK, lw=.8)
        for a in (top, right):
            a.set_xticks([]); a.set_yticks([])
            for sp in a.spines.values():
                sp.set_visible(False)
        top.tick_params(labelbottom=False); right.tick_params(labelleft=False)
        top.set_title(title, fontsize=8, pad=2)
    fig.set_layout_engine('constrained')
    save(fig, D/'rvec-same-marginals', 'figure', {
        'seed': seed, 'n': n,
        'panel_a': 'X,Y independent N(0,1)', 'panel_b': 'X=Z, Y=S*Z, Z~N(0,1), S=+-1 w.p. 1/2 independent of Z',
        'marginal_curve': 'standard normal density', 'histogram_bins': bins.tolist(),
        'sample_corr_a': float(np.corrcoef(x_ind, y_ind)[0, 1]), 'sample_corr_b': float(np.corrcoef(x_dep, y_dep)[0, 1])})


def rvec_correlation():
    seed, n = 20261029, 400
    rng = np.random.default_rng(seed)
    fig, axes = figure(width_mm=112, height_mm=34, ncols=4)
    facts = {'seed': seed, 'n': n, 'panels': []}
    specs = [(0.9, BLUE), (-0.6, GREEN), (0.0, YELLOW)]
    for ax, (rho, col) in zip(axes[:3], specs):
        z1 = rng.standard_normal(n); z2 = rng.standard_normal(n)
        x = z1; y = rho*z1 + sqrt(1-rho**2)*z2
        ax.scatter(x, y, s=1.6, color=col, alpha=.7, lw=0)
        ax.set_title(rf'$\rho={rho:g}$', fontsize=8, pad=2)
        facts['panels'].append({'model': f'X=Z1, Y={rho}*Z1+sqrt(1-{rho}^2)*Z2', 'rho': rho, 'sample_corr': float(np.corrcoef(x, y)[0, 1])})
    x = rng.uniform(-1, 1, n)*sqrt(3)
    y = x**2 - 1 + 0.15*rng.standard_normal(n)
    axes[3].scatter(x, y, s=1.6, color=RED, alpha=.7, lw=0)
    axes[3].set_title(r'$Y=X^2-1+\varepsilon$', fontsize=8, pad=2)
    facts['panels'].append({'model': 'X ~ U(-sqrt3,sqrt3), Y=X^2-1+0.15*N(0,1)', 'rho': 0.0, 'sample_corr': float(np.corrcoef(x, y)[0, 1])})
    for ax in axes:
        ax.set(xlim=(-3.2, 3.2), ylim=(-3.2, 3.2))
        ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlabel(r'$X$', labelpad=1)
    axes[0].set_ylabel(r'$Y$', labelpad=1)
    for ax in axes[1:]:
        ax.tick_params(labelleft=False)
    save(fig, D/'rvec-correlation', 'figure', facts)


def rvec_total_variance():
    seed, n_per = 20261030, 60
    rng = np.random.default_rng(seed)
    means = [1.0, 3.0, 5.0]
    cols = [BLUE, GREEN, YELLOW]
    fig, ax = figure(width_mm=112, height_mm=46)
    allv = []
    for k, (m, c) in enumerate(zip(means, cols)):
        v = m + rng.standard_normal(n_per)
        allv.append(v)
        yj = k + 1 + rng.uniform(-0.18, 0.18, n_per)
        ax.scatter(v, yj, s=3, color=c, alpha=.75, lw=0)
        ax.plot([m, m], [k+0.68, k+1.32], color=c, lw=1.6)
        ax.annotate('', xy=(m+1, k+1.42), xytext=(m-1, k+1.42), arrowprops=dict(arrowstyle='<->', color=c, lw=.7, shrinkA=0, shrinkB=0))
    allv = np.concatenate(allv)
    ax.axvline(3.0, color=INK, lw=.8, ls='--')
    ax.text(3.08, 3.72, r'$\mu_Y=3$', color=INK, fontsize=7.5)
    ax.set_yticks([1, 2, 3]); ax.set_yticklabels([r'$X=1$', r'$X=2$', r'$X=3$'])
    ax.set(xlim=(-2.2, 8.2), ylim=(0.45, 3.95), xlabel=r'$Y$')
    ax.spines['left'].set_visible(False); ax.tick_params(axis='y', length=0)
    save(fig, D/'rvec-total-variance', 'figure', {
        'seed': seed, 'n_per_group': n_per, 'model': 'X uniform on {1,2,3}; Y|X=k ~ N(m_k,1), m=(1,3,5)',
        'within_variance': 1.0, 'between_variance': 8/3, 'total_variance': 11/3,
        'arrows': 'group mean +- 1 (one conditional standard deviation)',
        'sample_total_variance': float(np.var(allv))})


def rvec_convolution():
    seed, n = 20261031, 20000
    rng = np.random.default_rng(seed)
    fig, (a, b) = figure(width_mm=112, height_mm=44, ncols=2)
    s = rng.uniform(size=n) + rng.uniform(size=n)
    a.hist(s, bins=np.linspace(0, 2, 41), density=True, color=BLUE_FILL, edgecolor=BLUE, lw=.4)
    g = np.linspace(-0.1, 2.1, 400)
    tri = np.clip(np.where(g <= 1, g, 2-g), 0, None)
    a.plot(g, tri, color=INK, lw=1.1)
    a.set(xlim=(-0.1, 2.1), ylim=(0, 1.15), xlabel=r'$s$', ylabel=r'$f_{U_1+U_2}(s)$')
    a.set_xticks([0, 1, 2]); a.set_yticks([0, .5, 1])
    a.set_title('(a) 两个独立均匀之和', fontsize=8, pad=2)
    x = np.linspace(0, 8, 600)
    lam = 1.0
    for k, c in zip([1, 2, 3], [BLUE, GREEN, RED]):
        f = lam**k*x**(k-1)*np.exp(-lam*x)/factorial(k-1)
        b.plot(x, f, color=c, label=rf'$k={k}$')
    b.set(xlim=(0, 8), ylim=(0, 1.05), xlabel=r'$s$', ylabel=r'$f_{S_k}(s)$')
    b.set_xticks([0, 2, 4, 6, 8]); b.set_yticks([0, .5, 1])
    b.legend(loc='upper right', handlelength=1.6)
    b.set_title('(b) 同率指数之和', fontsize=8, pad=2)
    save(fig, D/'rvec-convolution', 'figure', {
        'panel_a': {'seed': seed, 'n': n, 'model': 'U1+U2, Ui iid U(0,1)', 'density': 's on [0,1], 2-s on [1,2]'},
        'panel_b': {'model': 'S_k = sum of k iid Exp(1)', 'density': 's^(k-1) e^(-s)/(k-1)!', 'k': [1, 2, 3]}})


def rvec_whitening():
    seed, n = 20261101, 800
    rng = np.random.default_rng(seed)
    mu = np.array([1.0, 2.0]); Sig = np.array([[4.0, 2.0], [2.0, 2.0]])
    L = np.linalg.cholesky(Sig); Linv = np.linalg.inv(L)
    Z = rng.standard_normal((2, n)); X = mu[:, None] + L @ Z
    W = Linv @ (X - mu[:, None])
    w, V = np.linalg.eigh(Sig); root = V @ np.diag(np.sqrt(w)) @ V.T
    U = rng.uniform(-sqrt(3), sqrt(3), (2, n)); Xu = mu[:, None] + root @ U
    Wu = Linv @ (Xu - mu[:, None])
    fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
    axes[0].scatter(X[0], X[1], s=1.4, color=BLUE, alpha=.6, lw=0)
    ellipse(axes[0], mu, Sig, 2.0, color=INK, lw=.8)
    axes[0].set(xlim=(-6, 8), ylim=(-5, 9), xlabel=r'$x_1$', ylabel=r'$x_2$')
    axes[0].set_title('(a) 原始高斯样本', fontsize=8, pad=2)
    axes[1].scatter(W[0], W[1], s=1.4, color=GREEN, alpha=.6, lw=0)
    ellipse(axes[1], [0, 0], np.eye(2), 2.0, color=INK, lw=.8)
    axes[1].set(xlim=(-4, 4), ylim=(-4, 4), xlabel=r'$z_1$', ylabel=r'$z_2$')
    axes[1].set_title('(b) 高斯样本白化后', fontsize=8, pad=2)
    axes[2].scatter(Wu[0], Wu[1], s=1.4, color=RED, alpha=.6, lw=0)
    sq = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]]).T*sqrt(3)
    edge = Linv @ root @ sq
    axes[2].plot(edge[0], edge[1], color=INK, lw=.8)
    axes[2].set(xlim=(-4, 4), ylim=(-4, 4), xlabel=r'$z_1$', ylabel=r'$z_2$')
    axes[2].set_title('(c) 均匀样本白化后', fontsize=8, pad=2)
    for ax in axes:
        ax.set_aspect('equal', adjustable='box')
    save(fig, D/'rvec-whitening', 'figure', {
        'seed': seed, 'n': n, 'mu': mu.tolist(), 'Sigma': Sig.tolist(), 'cholesky_L': L.tolist(),
        'whitening': 'z = L^{-1}(x - mu)', 'panel_a_ellipse': 'Mahalanobis radius 2',
        'panel_c_source': 'x = mu + Sigma^{1/2} u, u uniform on [-sqrt3,sqrt3]^2 (unit covariance)',
        'panel_c_map': 'L^{-1} Sigma^{1/2} is orthogonal, so whitened support is a rotated square',
        'rotation_matrix': (Linv @ root).tolist(),
        'sample_cov_b': np.cov(W).tolist(), 'sample_cov_c': np.cov(Wu).tolist()})


def rvec_inverse_transform():
    fig, (a, b) = figure(width_mm=112, height_mm=46, ncols=2)
    lam = 2.0
    x = np.linspace(0, 2.2, 400)
    a.plot(x, 1-np.exp(-lam*x), color=BLUE)
    for u, c, ty in [(0.3, GREEN, 0.14), (0.7, RED, 0.04)]:
        xq = -np.log(1-u)/lam
        a.plot([0, xq], [u, u], color=c, lw=.7, ls='--')
        a.annotate('', xy=(xq, 0), xytext=(xq, u), arrowprops=dict(arrowstyle='->', color=c, lw=.7, shrinkA=0, shrinkB=0))
        a.plot([0], [u], 'o', color=c, ms=2.6)
        a.text(xq+0.04, ty, f'{xq:.3f}', color=c, fontsize=7.5)
    a.set(xlim=(0, 2.2), ylim=(0, 1.04), xlabel=r'$x$', ylabel=r'$F(x)=1-e^{-2x}$')
    a.set_xticks([0, 1, 2]); a.set_yticks([0, .3, .7, 1])
    a.set_title('(a) 指数分布', fontsize=8, pad=2)
    ps = [0.2, 0.5, 0.3]; cum = np.cumsum(ps)
    pts = [0.4, 1, 2, 3, 3.6]; vals = [0, *cum]
    for i in range(4):
        b.plot([pts[i], pts[i+1]], [vals[i], vals[i]], color=BLUE)
    for xk, lo, hi in zip([1, 2, 3], [0, *cum[:-1]], cum):
        b.plot([xk, xk], [lo, hi], color=BLUE, lw=.5, ls=':')
        b.plot([xk], [lo], 'o', mfc='white', mec=BLUE, ms=3)
        b.plot([xk], [hi], 'o', color=BLUE, ms=3)
    for u, c in [(0.15, GREEN), (0.55, RED), (0.9, YELLOW)]:
        k = int(np.searchsorted(cum, u)) + 1
        b.plot([0.4, k], [u, u], color=c, lw=.7, ls='--')
        b.annotate('', xy=(k, 0), xytext=(k, u), arrowprops=dict(arrowstyle='->', color=c, lw=.7, shrinkA=0, shrinkB=0))
        b.plot([0.4], [u], 'o', color=c, ms=2.6)
    b.set(xlim=(0.4, 3.6), ylim=(0, 1.04), xlabel=r'$x$', ylabel=r'$F(x)$')
    b.set_xticks([1, 2, 3]); b.set_yticks([0, .2, .7, 1])
    b.set_title('(b) 类别分布', fontsize=8, pad=2)
    save(fig, D/'rvec-inverse-transform', 'figure', {
        'panel_a': {'cdf': '1-exp(-2x)', 'u': [0.3, 0.7], 'x': [-np.log(0.7)/2, -np.log(0.3)/2]},
        'panel_b': {'pmf': {'1': .2, '2': .5, '3': .3}, 'cdf_levels': cum.tolist(), 'u': [0.15, 0.55, 0.9], 'x': [1, 2, 3]}})


def rvec_mixture():
    seed, n = 20261102, 4000
    rng = np.random.default_rng(seed)
    w = np.array([0.25, 0.75]); m = np.array([-1.0, 1.0])
    z = rng.choice(2, size=n, p=w)
    x = m[z] + rng.standard_normal(n)
    fig, ax = figure(width_mm=112, height_mm=46)
    ax.hist(x, bins=np.linspace(-4.5, 4.5, 46), density=True, color=BLUE_FILL, edgecolor=BLUE, lw=.4)
    g = np.linspace(-4.5, 4.5, 500)
    ax.plot(g, w[0]*phi(g, -1), color=GREEN, ls='--', label=r'$\frac{1}{4}\varphi(x+1)$')
    ax.plot(g, w[1]*phi(g, 1), color=YELLOW, ls='--', label=r'$\frac{3}{4}\varphi(x-1)$')
    ax.plot(g, w[0]*phi(g, -1)+w[1]*phi(g, 1), color=INK, label=r'$f_X(x)$')
    ax.set(xlim=(-4.5, 4.5), ylim=(0, 0.36), xlabel=r'$x$', ylabel='密度')
    ax.set_xticks([-4, -2, -1, 0, 1, 2, 4]); ax.set_yticks([0, .1, .2, .3])
    ax.legend(loc='upper left', handlelength=1.8)
    save(fig, D/'rvec-mixture', 'figure', {
        'seed': seed, 'n': n, 'weights': w.tolist(), 'components': ['N(-1,1)', 'N(1,1)'],
        'generation': 'Z ~ Cat(1/4,3/4); X|Z ~ N(m_Z,1)', 'mean': 0.5, 'variance': 1.75,
        'sample_mean': float(x.mean()), 'sample_variance': float(x.var())})


def rvec_gaussian_conditional():
    mu = np.array([1.0, 2.0]); Sig = np.array([[4.0, 2.0], [2.0, 2.0]])
    fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1.15, 1]})
    for c, col in zip([1, 2, 3], [BLUE, BLUE, BLUE]):
        ellipse(a, mu, Sig, c, color=col, lw=.8, alpha=[1, .75, .5][c-1])
    xs = np.linspace(-6, 8, 50)
    a.plot(xs, 2 + (xs-1)/2, color=RED, lw=1.1, label=r'$m(x_1)=2+(x_1-1)/2$')
    a.axvline(5, color=GREEN, lw=.8, ls='--')
    a.plot([5], [4], 'o', color=GREEN, ms=3)
    a.text(5.25, -2.4, r'$x_1=5$', color=GREEN, fontsize=7.5)
    a.set(xlim=(-6, 8), ylim=(-3.2, 7.2), xlabel=r'$x_1$', ylabel=r'$x_2$')
    a.set_aspect('equal', adjustable='box')
    a.legend(loc='upper left', handlelength=1.6)
    g = np.linspace(-3, 8, 500)
    b.plot(g, phi(g, 2, sqrt(2)), color=BLUE, label=r'$\mathcal{N}(2,2)$')
    b.plot(g, phi(g, 4, 1), color=GREEN, label=r'$\mathcal{N}(4,1)$')
    gg = g[g >= 3]
    b.fill_between(gg, phi(gg, 4, 1), color=GREEN_FILL, lw=0)
    b.axvline(3, color=MUTED, lw=.6, ls=':')
    b.set(xlim=(-3, 8), ylim=(0, 0.45), xlabel=r'$x_2$', ylabel='密度')
    b.set_xticks([-2, 0, 2, 3, 4, 6, 8]); b.set_yticks([0, .2, .4])
    b.legend(loc='upper left', handlelength=1.6)
    save(fig, D/'rvec-gaussian-conditional', 'figure', {
        'mu': mu.tolist(), 'Sigma': Sig.tolist(), 'ellipses': 'Mahalanobis radius 1,2,3',
        'conditional_mean_line': 'x2 = 2 + (x1 - 1)/2', 'conditional_variance': 1.0,
        'slice': 'x1 = 5 -> N(4,1)', 'marginal_X2': 'N(2,2)',
        'P(X2>3)': 0.23975, 'P(X2>3|X1=5)': 0.84134})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    rvec_same_marginals, rvec_correlation, rvec_total_variance, rvec_convolution,
    rvec_whitening, rvec_inverse_transform, rvec_mixture, rvec_gaussian_conditional]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
