# coding: utf-8
"""Figures for volume three, part "optimization", chapter 6
(stochastic and block optimization).

Every figure is computed from closed-form expressions or from small,
reproducible problems (ridge least squares, ridge logistic regression,
explicit quadratics) with a fixed numpy seed.  Each saved figure.json
records the formulas, parameters, seeds and key numbers quoted in the text.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/01-optimization/matplotlib/generate_c6.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
import re
import matplotlib.pyplot as plt
from support import (figure as _figure, save as _save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID,
                     BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL)
from matplotlib.colors import LinearSegmentedColormap

D = Path(__file__).resolve().parent
SEED = 20261030
CJK_FAMILY = 'Volume One Source Han Sans Normal'   # private alias registered by support.configure()


def figure(*args, **kwargs):
    fig_axes = _figure(*args, **kwargs)
    # Fira Math lacks \star and blackboard letters; let mathtext fall back to STIX for those glyphs only.
    plt.rcParams['mathtext.fallback'] = 'stix'
    return fig_axes


def save(fig, directory, name, facts):
    # mathtext renders the non-math part of a mixed string with the text's own family; strings that
    # combine Chinese with $...$ therefore need the CJK face (which also carries Latin glyphs).
    for tx in fig.findobj(lambda o: hasattr(o, 'get_text') and hasattr(o, 'set_fontfamily')):
        s = tx.get_text()
        if '$' in s and re.search(r'[\u3000-\u9fff\uff00-\uffef]', s):
            tx.set_fontfamily(CJK_FAMILY)
    return _save(fig, directory, name, facts)


# ---------------------------------------------------------------- problems
def ls2d(seed=SEED, n=40, scales=(2.0, 0.5), lam=0.05, noise=0.6):
    """Ridge least squares f(x)=1/(2n)||Ax-b||^2+lam/2||x||^2, d=2."""
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, 2)) * np.array(scales)
    xt = np.array([1.0, -0.5])
    b = A @ xt + noise * rng.normal(size=n)
    H = A.T @ A / n + lam * np.eye(2)
    xs = np.linalg.solve(H, A.T @ b / n)
    ev = np.linalg.eigvalsh(H)
    Li = (A ** 2).sum(1) + lam
    gstar = A * (A @ xs - b)[:, None] + lam * xs
    sig2 = float((gstar ** 2).sum(1).mean())
    f = lambda x: 0.5 * np.mean((A @ x - b) ** 2) + 0.5 * lam * x @ x
    return dict(A=A, b=b, lam=lam, n=n, H=H, xs=xs, mu=ev[0], L=ev[1], Lmax=Li.max(),
                Lbar=Li.mean(), Li=Li, sig2=sig2, f=f, fs=f(xs), seed=seed)


def fgrid(P, xr, yr, m=240):
    X, Y = np.meshgrid(np.linspace(*xr, m), np.linspace(*yr, m))
    pts = np.stack([X.ravel(), Y.ravel()], 1)
    r = pts @ P['A'].T - P['b']
    Z = 0.5 * (r ** 2).mean(1) + 0.5 * P['lam'] * (pts ** 2).sum(1)
    return X, Y, Z.reshape(X.shape) - P['fs']


def contours(ax, X, Y, Z, levels):
    ax.contour(X, Y, Z, levels=levels, colors=GRID, linewidths=.6)


def sgd_runs(P, eta_fn, T, R, x0, seed, batch=1, sampler=None, weights=None):
    """R independent SGD runs vectorised; returns iterates (T+1, R, 2)."""
    rng = np.random.default_rng(seed)
    A, b, lam, n = P['A'], P['b'], P['lam'], P['n']
    X = np.tile(x0, (R, 1)).astype(float)
    out = np.empty((T + 1, R, 2)); out[0] = X
    for t in range(T):
        if sampler is None:
            idx = rng.integers(0, n, size=(R, batch))
        else:
            idx = rng.choice(n, size=(R, batch), p=sampler)
        a = A[idx]                                  # R,b,2
        res = np.einsum('rbk,rk->rb', a, X) - b[idx]
        gi = a * res[..., None]                     # R,b,2
        if weights is not None:
            gi = gi * weights[idx][..., None]
        g = gi.mean(1) + lam * X
        X = X - eta_fn(t) * g
        out[t + 1] = X
    return out


# ---------------------------------------------------------------- 6.2
def c6_gradient_fan():
    """Per-sample descent directions -grad f_i at one point and their mean."""
    P = ls2d(seed=SEED + 1, n=10, scales=(1.6, 0.8), lam=0.05, noise=0.8)
    xs = P['xs']; x = xs + np.array([1.2, 0.9])
    A, b, lam = P['A'], P['b'], P['lam']
    G = A * (A @ x - b)[:, None] + lam * x
    gbar = G.mean(0)
    fig, ax = figure(width_mm=100, height_mm=62)
    X, Y, Z = fgrid(P, (xs[0] - 2.2, xs[0] + 3.6), (xs[1] - 1.6, xs[1] + 2.6))
    contours(ax, X, Y, Z, levels=[0.05, 0.2, 0.5, 1, 1.6, 2.4, 3.4])
    s = 0.35
    ascent = 0
    for gi in G:
        up = gi @ gbar < 0
        ascent += int(up)
        ax.annotate('', xy=x - s * gi, xytext=x,
                    arrowprops=dict(arrowstyle='-|>', color=RED if up else MUTED,
                                    lw=.8, shrinkA=0, shrinkB=0, mutation_scale=7))
    ax.annotate('', xy=x - s * gbar, xytext=x,
                arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.8, shrinkA=0, shrinkB=0, mutation_scale=9))
    ax.plot(*x, 'o', color=INK, ms=3.5, zorder=5)
    ax.plot(*xs, '*', color=GREEN, ms=8, zorder=5)
    ax.text(x[0] + .1, x[1] + .18, r'$x$', color=INK)
    ax.text(xs[0] + .1, xs[1] - .35, r'$x^\star$', color=GREEN)
    ax.plot([], [], color=MUTED, lw=.8, label=r'$-\nabla f_i(x)$')
    ax.plot([], [], color=RED, lw=.8, label=r'$-\nabla f_i$ 与 $-\nabla f$ 夹角为钝角')
    ax.plot([], [], color=BLUE, lw=1.8, label=r'平均 $-\nabla f(x)$')
    ax.legend(loc='lower right', handlelength=1.4)
    ax.set(xlabel=r'$x_1$', ylabel=r'$x_2$', aspect='equal')
    ax.set_xlim(X.min(), X.max()); ax.set_ylim(Y.min(), Y.max())
    save(fig, D/'c6-gradient-fan', 'figure', {
        'problem': 'f(x)=1/(2n)||Ax-b||^2+lam/2||x||^2, A rows N(0,diag(1.6,0.8)^2)', 'n': 10,
        'lam': 0.05, 'seed': SEED + 1, 'x_star': xs.round(4).tolist(), 'x': x.round(4).tolist(),
        'arrow_scale': s, 'num_obtuse_readings': ascent,
        'full_gradient': gbar.round(4).tolist()})


def c6_sgd_noise_ball():
    P = ls2d()
    xs = P['xs']; x0 = xs + np.array([-2.6, 2.2])
    T, R = 1500, 400
    etas = [1 / (2 * P['Lmax']), 1 / (4 * P['Lmax']), 1 / (8 * P['Lmax'])]
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=60, ncols=2)
    X, Y, Z = fgrid(P, (xs[0] - 3.4, xs[0] + 1.4), (xs[1] - 1.5, xs[1] + 2.6))
    contours(ax1, X, Y, Z, levels=[0.02, 0.1, .3, .7, 1.4, 2.5, 4, 6])
    # GD path
    xg = x0.copy(); path = [xg.copy()]
    for t in range(60):
        xg = xg - (1 / P['L']) * (P['H'] @ (xg - xs)); path.append(xg.copy())
    path = np.array(path)
    ax1.plot(path[:, 0], path[:, 1], '-', color=BLUE, lw=1.1, label='梯度下降')
    runs = sgd_runs(P, lambda t: etas[0], 300, 1, x0, SEED + 2)
    ax1.plot(runs[:, 0, 0], runs[:, 0, 1], '-', color=YELLOW, lw=.6, label=r'随机梯度，$\eta=1/(2L_{\max})$')
    cloud = sgd_runs(P, lambda t: etas[0], 400, 300, xs, SEED + 3)[-1]
    ax1.plot(cloud[:, 0], cloud[:, 1], '.', color=RED, ms=1.6, alpha=.8, label='300 次运行的第 400 步')
    ax1.plot(*xs, '*', color=GREEN, ms=8, zorder=5)
    ax1.set(xlabel=r'$x_1$', ylabel=r'$x_2$', aspect='equal', title='(a) 路径与终点分布')
    ax1.set_xlim(X.min(), X.max()); ax1.set_ylim(Y.min(), Y.max())
    ax1.legend(loc='lower left', fontsize=6.8, handlelength=1.2, borderaxespad=0.2)
    facts = {'problem': 'ridge least squares d=2', 'n': P['n'], 'lam': P['lam'], 'seed': SEED,
             'mu': round(P['mu'], 4), 'L': round(P['L'], 4), 'Lmax': round(P['Lmax'], 4),
             'sigma_star_sq': round(P['sig2'], 4), 'x0_minus_xstar': [-2.6, 2.2], 'runs': R, 'T': T,
             'bound': 'E||x_t-x*||^2 <= (1-eta mu)^t D0^2 + 2 eta sigma*^2/mu'}
    cols = [BLUE, GREEN, PURPLE]
    D0 = float(((x0 - xs) ** 2).sum())
    for eta, c, lab in zip(etas, cols, ['1/(2L_{\\max})', '1/(4L_{\\max})', '1/(8L_{\\max})']):
        it = sgd_runs(P, lambda t, e=eta: e, T, R, x0, SEED + 4)
        err = ((it - xs) ** 2).sum(2).mean(1)
        t = np.arange(T + 1)
        ax2.semilogy(t, err, color=c, lw=1.1, label=rf'$\eta={lab}$')
        floor = 2 * eta * P['sig2'] / P['mu']
        ax2.semilogy(t, (1 - eta * P['mu']) ** t * D0 + floor, color=c, lw=.6, ls='--')
        facts[f'eta={eta:.4f}'] = {'bound_floor': round(floor, 5), 'empirical_mean_last100': float(err[-100:].mean().round(5))}
    ax2.set(xlabel=r'迭代 $t$', ylabel=r'$\mathbb{E}\Vert x^{(t)}-x^\star\Vert_2^2$', title='(b) 平均误差与界（虚线）')
    ax2.set_ylim(1e-3, 30)
    ax2.legend(loc='upper right', handlelength=1.4)
    save(fig, D/'c6-sgd-noise-ball', 'figure', facts)


def c6_step_schedules():
    P = ls2d()
    xs = P['xs']; x0 = xs + np.array([-2.6, 2.2])
    T, R = 3000, 400
    mu, Lm = P['mu'], P['Lmax']
    eta0 = 1 / (2 * Lm); t0 = 4 * Lm / mu
    K = 500
    sched = {
        '常数': (lambda t: eta0, BLUE),
        r'递减 $2/(\mu(t+t_0))$': (lambda t: 2 / (mu * (t + t0)), GREEN),
        '分段减半（每 500 步）': (lambda t: eta0 * 0.5 ** (t // K), PURPLE),
    }
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=56, ncols=2)
    t = np.arange(T)
    facts = {'problem': 'ridge least squares d=2 (same as c6-sgd-noise-ball)', 'seed': SEED + 5, 'runs': R,
             'eta0': round(eta0, 5), 't0': round(t0, 3), 'K': K, 'mu': round(mu, 4), 'Lmax': round(Lm, 4)}
    for name, (fn, c) in sched.items():
        ax1.plot(t, [fn(s) for s in t], color=c, lw=1.1, label=name)
        it = sgd_runs(P, fn, T, R, x0, SEED + 5)
        err = ((it - xs) ** 2).sum(2).mean(1)
        ax2.loglog(np.arange(1, T + 1), err[1:], color=c, lw=1.1, label=name)
        facts[name] = {'err_t=500': float(err[500].round(5)), 'err_t=3000': float(err[-1].round(6))}
    D0 = float(((x0 - xs) ** 2).sum())
    nu = max(t0 * D0, 8 * P['sig2'] / mu ** 2)
    tt = np.arange(1, T + 1)
    ax2.loglog(tt, nu / (tt + t0), color=GREEN, lw=.6, ls='--', label=r'界 $\nu/(t+t_0)$')
    facts['nu'] = round(nu, 3)
    ax1.set(xlabel=r'迭代 $t$', ylabel=r'步长 $\eta^{(t)}$', title='(a) 三种调度')
    ax1.legend(loc='upper right', handlelength=1.4)
    ax2.set(xlabel=r'迭代 $t$', ylabel=r'$\mathbb{E}\Vert x^{(t)}-x^\star\Vert_2^2$', title='(b) 平均误差')
    ax2.legend(loc='lower left', handlelength=1.4, fontsize=7)
    save(fig, D/'c6-step-schedules', 'figure', facts)


def c6_return_points():
    P = ls2d()
    xs = P['xs']; x0 = xs + np.array([-2.6, 2.2])
    T, R = 4000, 300
    eta = 1 / (2 * P['Lmax'])
    it = sgd_runs(P, lambda t: eta, T, R, x0, SEED + 6)
    f = lambda Xs: 0.5 * (((Xs @ P['A'].T) - P['b']) ** 2).mean(-1) + 0.5 * P['lam'] * (Xs ** 2).sum(-1) - P['fs']
    last = f(it)                     # T+1, R
    avg = np.cumsum(it, 0) / np.arange(1, T + 2)[:, None, None]
    favg = f(avg)
    tail = np.empty_like(it)
    for s in range(T + 1):
        h = s // 2
        tail[s] = it[h:s + 1].mean(0)
    ftail = f(tail)
    t = np.arange(1, T + 2)
    fig, ax = figure(width_mm=105, height_mm=58)
    ax.loglog(t, last[:, 0], color=GRID, lw=.5, label='最后一点（单次运行）')
    ax.loglog(t, last.mean(1), color=BLUE, lw=1.1, label='最后一点（平均）')
    ax.loglog(t, favg.mean(1), color=GREEN, lw=1.1, label='全程平均点')
    ax.loglog(t, ftail.mean(1), color=PURPLE, lw=1.1, label='后半程平均点')
    ax.set(xlabel=r'迭代 $t$', ylabel=r'$\mathbb{E}f(\cdot)-f^\star$')
    ax.set_ylim(1e-5, 10)
    ax.legend(loc='lower left', handlelength=1.4, fontsize=7)
    save(fig, D/'c6-return-points', 'figure', {
        'problem': 'ridge least squares d=2', 'eta': round(eta, 5), 'runs': R, 'seed': SEED + 6,
        'last_iterate_mean_gap_last500': float(last[-500:].mean().round(6)),
        'running_average_gap_T': float(favg[-1].mean().round(7)),
        'tail_average_gap_T': float(ftail[-1].mean().round(7)),
        'note': 'quadratic objective: E x_{t+1}=E x_t-eta H(E x_t-x*), averages remove the noise floor'})


# ---------------------------------------------------------------- 6.3
def c6_importance_sampling():
    rng = np.random.default_rng(SEED + 7)
    n = 40
    A = rng.normal(size=(n, 2)) * np.array([1.0, 0.6])
    big = np.arange(4)
    A[big] *= 6.0
    xt = np.array([1.0, -0.5]); b = A @ xt + 0.5 * rng.normal(size=n)
    lam = 0.05
    H = A.T @ A / n + lam * np.eye(2)
    xs = np.linalg.solve(H, A.T @ b / n)
    Li = (A ** 2).sum(1)
    p = Li / Li.sum()
    P = dict(A=A, b=b, lam=lam, n=n, xs=xs)
    x0 = xs + np.array([-2.0, 2.0])
    T, R = 3000, 300
    Lmax_u = Li.max() + lam
    Lmax_p = Li.mean() + lam          # max_i L_i/(n p_i) = mean L_i when p_i is proportional to L_i
    mu = np.linalg.eigvalsh(H)[0]
    t0u, t0p = 4 * Lmax_u / mu, 4 * Lmax_p / mu
    eta_u = lambda t: 2 / (mu * (t + t0u))
    eta_p = lambda t: 2 / (mu * (t + t0p))
    w = 1 / (n * p)
    u = sgd_runs(P, eta_u, T, R, x0, SEED + 8)
    s_rw = sgd_runs(P, eta_p, T, R, x0, SEED + 8, sampler=p, weights=w)
    s_nw = sgd_runs(P, eta_u, T, R, x0, SEED + 8, sampler=p)
    # minimiser of the un-reweighted (biased) mean direction: sum p_i a_i(a_i^T x - b_i) + lam x = 0
    Hb = (A * p[:, None]).T @ A + lam * np.eye(2)
    xb = np.linalg.solve(Hb, (A * p[:, None]).T @ b)
    gl = A * (A @ xs - b)[:, None]
    sig_u = float((gl ** 2).sum(1).mean())
    sig_p = float(((gl ** 2).sum(1) / p).sum() / n ** 2)
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [1, 1.35]})
    order = np.arange(n)
    ax1.bar(order, p, color=BLUE_FILL, edgecolor=BLUE, lw=.5, label=r'$p_i\propto\Vert a_i\Vert_2^2$')
    ax1.axhline(1 / n, color=GREEN, lw=1.1, label=r'均匀 $1/n$')
    ax1.set(xlabel=r'样本序号 $i$', ylabel='抽样概率', title='(a) 抽样分布')
    ax1.legend(loc='upper right', handlelength=1.4)
    t = np.arange(1, T + 2)
    for it, c, lab in [(u, BLUE, '均匀抽样'), (s_rw, GREEN, r'按 $p_i$ 抽样并乘 $1/(np_i)$'),
                       (s_nw, RED, r'按 $p_i$ 抽样但不重加权')]:
        ax2.loglog(t, ((it - xs) ** 2).sum(2).mean(1), color=c, lw=1.1, label=lab)
    ax2.axhline(float(((xb - xs) ** 2).sum()), color=RED, lw=.6, ls='--')
    ax2.set(xlabel=r'迭代 $t$', ylabel=r'$\mathbb{E}\Vert x^{(t)}-x^\star\Vert_2^2$', title=r'(b) 误差，$\eta^{(t)}=2/(\mu(t+t_0))$')
    ax2.legend(loc='lower left', handlelength=1.4, fontsize=7)
    errs = {k: float(((it[-200:] - xs) ** 2).sum(2).mean().round(5)) for k, it in
            [('uniform', u), ('importance_reweighted', s_rw), ('importance_unweighted', s_nw)]}
    save(fig, D/'c6-importance-sampling', 'figure', {
        'problem': 'ridge least squares d=2, first 4 rows scaled by 6', 'n': n, 'lam': lam, 'seed': SEED + 7,
        'Lmax': round(float(Lmax_u), 3), 'Lbar': round(float(Lmax_p), 3),
        'mu': round(float(mu), 4), 't0_uniform': round(float(t0u), 1), 't0_importance': round(float(t0p), 1),
        'sigma_star_sq_uniform': round(sig_u, 3), 'sigma_star_sq_importance': round(sig_p, 3),
        'schedule': 'eta_t=2/(mu(t+t0)), t0=4 Lmax_eff/mu; unweighted run uses uniform schedule',
        'biased_limit_distance_sq': round(float(((xb - xs) ** 2).sum()), 4),
        'mean_sq_error_last200': errs})


def c6_minibatch_variance():
    rng = np.random.default_rng(SEED + 9)
    n, d = 200, 5
    A = rng.normal(size=(n, d)); b = A @ rng.normal(size=d) + rng.normal(size=n)
    x = np.zeros(d)
    G = A * (A @ x - b)[:, None]
    gbar = G.mean(0)
    sig2 = float(((G - gbar) ** 2).sum(1).mean())
    bs = np.array([1, 2, 4, 8, 16, 32, 64, 100, 150, 200])
    M = 4000
    emp_w, emp_wo = [], []
    for bb in bs:
        idx = rng.integers(0, n, size=(M, bb))
        emp_w.append(((G[idx].mean(1) - gbar) ** 2).sum(1).mean())
        idx2 = np.argsort(rng.random((M, n)), 1)[:, :bb]
        emp_wo.append(((G[idx2].mean(1) - gbar) ** 2).sum(1).mean())
    fig, ax = figure(width_mm=100, height_mm=58)
    bb = np.linspace(1, n, 400)
    ax.loglog(bb, sig2 / bb, color=BLUE, lw=1.1, label=r'有放回：$\sigma^2/b$')
    ax.loglog(bb[bb < n], (sig2 / bb * (n - bb) / (n - 1))[bb < n], color=GREEN, lw=1.1,
              label=r'无放回：$\frac{\sigma^2}{b}\cdot\frac{n-b}{n-1}$')
    ax.loglog(bs, emp_w, 'o', color=BLUE, ms=3)
    ax.loglog(bs[:-1], emp_wo[:-1], 's', color=GREEN, ms=3)
    ax.set(xlabel=r'批量 $b$', ylabel=r'$\mathbb{E}\Vert \bar g-\nabla f\Vert_2^2$')
    ax.legend(loc='lower left', handlelength=1.4)
    save(fig, D/'c6-minibatch-variance', 'figure', {
        'problem': 'least squares n=200,d=5 at x=0, A,b ~ N(0,1)', 'seed': SEED + 9, 'draws_per_b': M,
        'sigma_sq': round(sig2, 3), 'batch_sizes': bs.tolist(),
        'empirical_with_replacement': np.round(emp_w, 4).tolist(),
        'empirical_without_replacement': np.round(emp_wo, 5).tolist(),
        'note': 'without replacement and b=n the variance is exactly 0 (not drawn on log axis)'})


def logistic_problem(seed=SEED + 10, n=200, d=10, lam=5e-2):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, d)) * np.linspace(1.5, 0.3, d)
    w = rng.normal(size=d)
    y = np.where(rng.random(n) < 1 / (1 + np.exp(-A @ w)), 1.0, -1.0)
    Z = A * y[:, None]

    def gi(x, i):
        z = Z[i]; s = 1 / (1 + np.exp(z @ x))
        return -s[..., None] * z + lam * x if np.ndim(i) else -s * z + lam * x

    def full(x):
        s = 1 / (1 + np.exp(Z @ x)); return -(Z * s[:, None]).mean(0) + lam * x

    def allg(x):
        s = 1 / (1 + np.exp(Z @ x)); return -Z * s[:, None] + lam * x

    def f(x):
        return np.mean(np.logaddexp(0, -Z @ x)) + 0.5 * lam * x @ x
    x = np.zeros(d)
    for _ in range(50):
        s = 1 / (1 + np.exp(Z @ x))
        Hs = (Z * (s * (1 - s))[:, None]).T @ Z / n + lam * np.eye(d)
        x = x - np.linalg.solve(Hs, full(x))
    Lmax = float(((Z ** 2).sum(1)).max() / 4 + lam)
    L = float(np.linalg.eigvalsh(Z.T @ Z / (4 * n)).max() + lam)
    return dict(Z=Z, gi=gi, full=full, allg=allg, f=f, xs=x, fs=f(x), n=n, d=d, lam=lam, Lmax=Lmax, L=L)


def c6_variance_reduction():
    P = logistic_problem()
    n, d, Lm = P['n'], P['d'], P['Lmax']
    passes = 30
    budget = passes * n
    seeds = range(8)
    curves = {}

    def record(store, reads, x, var):
        store.append((reads / n, P['f'](x) - P['fs'], var))

    for name in ['GD', 'SGD', 'SGD-dec', 'SVRG', 'SAGA']:
        runs = []
        for sd in seeds:
            rng = np.random.default_rng(SEED + 11 + sd)
            x = np.zeros(d); reads = 0; rec = []
            if name == 'GD':
                while reads <= budget:
                    record(rec, reads, x, 0.0)
                    x = x - (1 / P['L']) * P['full'](x)
                    reads += n
            elif name in ('SGD', 'SGD-dec'):
                t = 0
                while reads <= budget:
                    if reads % (n // 4) == 0:
                        G = P['allg'](x); var = float(((G - G.mean(0)) ** 2).sum(1).mean())
                        record(rec, reads, x, var)
                    eta = 1 / (2 * Lm) if name == 'SGD' else 1 / (2 * Lm) / (1 + t / (2 * n))
                    i = rng.integers(n); x = x - eta * P['gi'](x, i); reads += 1; t += 1
            elif name == 'SVRG':
                m = 2 * n; eta = 1 / (3 * Lm)
                while reads <= budget:
                    xt = x.copy(); Gt = P['allg'](xt); mu = Gt.mean(0); reads += n
                    for k in range(m):
                        if reads % (n // 4) == 0:
                            G = P['allg'](x); V = G - Gt + mu
                            var = float(((V - V.mean(0)) ** 2).sum(1).mean())
                            record(rec, reads, x, var)
                        i = rng.integers(n)
                        v = P['gi'](x, i) - Gt[i] + mu
                        x = x - eta * v; reads += 2
                        if reads > budget: break
            elif name == 'SAGA':
                eta = 1 / (3 * Lm)
                phi = P['allg'](x); mean = phi.mean(0); reads += n
                while reads <= budget:
                    if reads % (n // 4) == 0:
                        G = P['allg'](x); V = G - phi + mean
                        var = float(((V - V.mean(0)) ** 2).sum(1).mean())
                        record(rec, reads, x, var)
                    i = rng.integers(n); gnew = P['gi'](x, i)
                    v = gnew - phi[i] + mean
                    mean = mean + (gnew - phi[i]) / n; phi[i] = gnew
                    x = x - eta * v; reads += 1
            runs.append(np.array(rec))
        k = min(len(r) for r in runs)
        arr = np.stack([r[:k] for r in runs])
        curves[name] = arr.mean(0)
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=58, ncols=2)
    style = {'GD': (INK, '梯度下降'), 'SGD': (YELLOW, '随机梯度（常数步长）'),
             'SGD-dec': (RED, '随机梯度（递减步长）'), 'SVRG': (BLUE, 'SVRG'), 'SAGA': (GREEN, 'SAGA')}
    facts = {'problem': 'ridge logistic regression n=200,d=10,lam=5e-2', 'L': round(P['L'], 4), 'seeds': [SEED + 11 + s for s in seeds],
             'Lmax': round(Lm, 4), 'steps': {'GD': '1/L', 'SGD': '1/(2Lmax)', 'SGD-dec': '1/(2Lmax)/(1+t/(2n))',
                                              'SVRG': '1/(3Lmax), m=2n', 'SAGA': '1/(3Lmax)'},
             'reads': 'GD n per step; SGD 1; SVRG n per snapshot + 2 per inner step; SAGA n initial + 1 per step',
             'gap_at_30_passes': {}}
    for name, arr in curves.items():
        c, lab = style[name]
        ax1.semilogy(arr[:, 0], np.maximum(arr[:, 1], 1e-16), color=c, lw=1.1, label=lab,
                     marker='o' if name == 'GD' else None, ms=1.6)
        if name != 'GD':
            ax2.semilogy(arr[:, 0], np.maximum(arr[:, 2], 1e-30), color=c, lw=1.1, label=lab)
        facts['gap_at_30_passes'][name] = float('%.3g' % arr[-1, 1])
    ax1.set(xlabel='读取量（全数据遍历次数）', ylabel=r'$f(x)-f^\star$', title='(a) 目标差')
    ax1.set_ylim(1e-12, 1)
    ax1.legend(loc='lower left', handlelength=1.4, fontsize=7)
    ax2.set(xlabel='读取量（全数据遍历次数）', ylabel=r'$\mathbb{E}[\Vert v-\nabla f(x)\Vert_2^2\mid x]$', title='(b) 方向的条件方差')
    ax2.set_ylim(1e-10, 10)
    save(fig, D/'c6-variance-reduction', 'figure', facts)


# ---------------------------------------------------------------- 6.4
def _adaptive_runs(Hm, x0, T):
    grad = lambda x: Hm @ x
    out = {}
    x = x0.copy(); p = [x.copy()]
    for t in range(T):
        x = x - (1 / np.linalg.eigvalsh(Hm).max()) * grad(x); p.append(x.copy())
    out['GD'] = np.array(p)
    x = x0.copy(); v = np.zeros(2); p = [x.copy()]
    for t in range(T):
        g = grad(x); v += g * g; x = x - 1.0 * g / (np.sqrt(v) + 1e-8); p.append(x.copy())
    out['AdaGrad'] = np.array(p)
    x = x0.copy(); m = np.zeros(2); v = np.zeros(2); p = [x.copy()]; b1, b2 = 0.9, 0.999
    for t in range(T):
        g = grad(x); m = b1 * m + (1 - b1) * g; v = b2 * v + (1 - b2) * g * g
        mh = m / (1 - b1 ** (t + 1)); vh = v / (1 - b2 ** (t + 1))
        x = x - 0.3 * mh / (np.sqrt(vh) + 1e-8); p.append(x.copy())
    out['Adam'] = np.array(p)
    return out


def c6_adaptive_paths():
    """Deterministic gradients on f=1/2 x^T H x, H=diag(1,25) and the same H rotated by 45 degrees."""
    T = 60
    Ha = np.diag([1.0, 25.0])
    c, s_ = np.cos(np.pi / 4), np.sin(np.pi / 4)
    Q = np.array([[c, -s_], [s_, c]])
    Hr = Q @ Ha @ Q.T
    x0 = np.array([-4.0, 1.0])
    pa = _adaptive_runs(Ha, x0, T)
    pr = _adaptive_runs(Hr, Q @ x0, T)
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=56, ncols=2, gridspec_kw={'width_ratios': [1.5, 1]})
    X, Y = np.meshgrid(np.linspace(-4.6, 1.6, 300), np.linspace(-1.4, 1.4, 300))
    Z = 0.5 * (X ** 2 + 25 * Y ** 2)
    ax1.contour(X, Y, Z, levels=[0.1, 0.5, 1.5, 3, 5, 8, 12, 17], colors=GRID, linewidths=.6)
    sty = {'GD': (BLUE, r'梯度下降 $\eta=1/L$'), 'AdaGrad': (GREEN, r'AdaGrad $\eta=1$'),
           'Adam': (PURPLE, r'Adam $\eta=0.3$')}
    fval = lambda Hm, P: 0.5 * np.einsum('ti,ij,tj->t', P, Hm, P)
    facts = {'objective': 'f(x)=1/2 x^T H x, exact gradients; aligned H=diag(1,25); rotated Q H Q^T, Q=rotation 45 deg',
             'x0_aligned': x0.tolist(), 'x0_rotated': 'Q x0', 'T': T,
             'GD': 'eta=1/25', 'AdaGrad': 'eta=1, eps=1e-8 outside sqrt', 'Adam': 'eta=0.3,beta1=0.9,beta2=0.999,eps=1e-8',
             'f_at_T_aligned': {}, 'f_at_T_rotated': {}, 'adagrad_first_step_aligned': (pa['AdaGrad'][1] - x0).tolist()}
    for k in pa:
        col, lab = sty[k]
        pth = pa[k]
        ax1.plot(pth[:25, 0], pth[:25, 1], '-o', color=col, lw=.9, ms=1.8, label=lab)
        ax2.semilogy(np.arange(T + 1), fval(Ha, pa[k]), color=col, lw=1.1)
        ax2.semilogy(np.arange(T + 1), fval(Hr, pr[k]), color=col, lw=1.0, ls='--')
        facts['f_at_T_aligned'][k] = float('%.3g' % fval(Ha, pa[k])[-1])
        facts['f_at_T_rotated'][k] = float('%.3g' % fval(Hr, pr[k])[-1])
    ax2.plot([], [], color=MUTED, lw=1.1, label='主轴与坐标轴对齐')
    ax2.plot([], [], color=MUTED, lw=1.0, ls='--', label='旋转 45°')
    ax1.plot(0, 0, '*', color=INK, ms=7)
    ax1.set(xlabel=r'$x_1$', ylabel=r'$x_2$', aspect='equal', title='(a) 对齐情形的前 25 步')
    ax1.legend(loc='lower right', fontsize=7, handlelength=1.2)
    ax2.set(xlabel=r'迭代 $t$', ylabel=r'$f(x^{(t)})$', title='(b) 目标值')
    ax2.legend(loc='lower left', handlelength=1.6, fontsize=7)
    save(fig, D/'c6-adaptive-paths', 'figure', facts)


def c6_adafactor():
    rng = np.random.default_rng(SEED + 12)
    m, d, T = 6, 8, 40
    r = np.linspace(2.0, 0.5, m); c = np.linspace(0.4, 1.6, d)
    V = np.zeros((m, d))
    for t in range(T):
        G = np.outer(r * rng.normal(size=m), c) + 0.6 * rng.normal(size=(m, d))
        V += G * G
    V /= T
    R = V.sum(1); C = V.sum(0)
    Vh = np.outer(R, C) / V.sum()
    rel = np.abs(Vh - V) / V
    cmap = LinearSegmentedColormap.from_list('b', ['#FFFFFF', BLUE_FILL, BLUE, '#4F6580'])
    cmap2 = LinearSegmentedColormap.from_list('r', ['#FFFFFF', RED_FILL, RED])
    fig, axes = figure(width_mm=160, height_mm=46, ncols=3)
    vmax = max(V.max(), Vh.max())
    for ax, M, title, cm, vm in [(axes[0], V, r'(a) 完整统计 $V$（48 个数）', cmap, vmax),
                                 (axes[1], Vh, r'(b) 行列重建 $\hat V$（14 个数）', cmap, vmax),
                                 (axes[2], rel, r'(c) 相对误差 $|\hat V-V|/V$', cmap2, rel.max())]:
        im = ax.imshow(M, cmap=cm, vmin=0, vmax=vm)
        ax.set_title(title)
        ax.set_xticks([]); ax.set_yticks([])
        fig.colorbar(im, ax=ax, shrink=.8, pad=.02)
    save(fig, D/'c6-adafactor', 'figure', {
        'model': 'G_t = outer(r*N(0,1), c) + 0.6 N(0,1), r=linspace(2,.5,6), c=linspace(.4,1.6,8)',
        'T': T, 'seed': SEED + 12, 'V': 'mean of G_t*G_t', 'reconstruction': 'outer(row sums, col sums)/total',
        'max_rel_error': round(float(rel.max()), 3), 'mean_rel_error': round(float(rel.mean()), 3),
        'stored_numbers': {'full': m * d, 'factored': m + d}})


def c6_lion_muon():
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=56, ncols=2, gridspec_kw={'width_ratios': [1, 1.4]})
    g1 = np.array([0.2, 0.05]); g2 = np.array([4.0, 1.0]); g3 = np.array([3.0, -0.4])
    sc = 0.45
    arrow = lambda v, c, lw=1.0, ls='-': ax1.annotate('', xy=v, xytext=(0, 0), arrowprops=dict(
        arrowstyle='-|>', color=c, lw=lw, ls=ls, mutation_scale=8, shrinkA=0, shrinkB=0))
    arrow(-sc * g1, BLUE); arrow(-sc * g2, GREEN); arrow(-sc * g3, PURPLE)
    ax1.text(-sc * g1[0] + .02, -sc * g1[1] + .1, r'$-0.45g_{\mathrm{a}}$', color=BLUE, fontsize=7, ha='left')
    ax1.text(-sc * g2[0] - .05, -sc * g2[1] - .2, r'$-0.45g_{\mathrm{b}}$', color=GREEN, fontsize=7, ha='center')
    ax1.text(-sc * g3[0] - .05, -sc * g3[1] + .1, r'$-0.45g_{\mathrm{c}}$', color=PURPLE, fontsize=7, ha='center')
    arrow(np.array([-1, -1]), INK, 1.5)
    arrow(np.array([-1, 1]), PURPLE, 1.5, '--')
    ax1.text(-1.0, -1.22, r'$-\mathrm{sign}(g_{\mathrm{a}})=-\mathrm{sign}(g_{\mathrm{b}})$', ha='center', fontsize=7, color=INK)
    ax1.text(-1.0, 1.08, r'$-\mathrm{sign}(g_{\mathrm{c}})$', ha='center', fontsize=7, color=PURPLE)
    ax1.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color=GRID, lw=.6)
    ax1.set(xlim=(-2.3, 1.2), ylim=(-1.45, 1.4), aspect='equal', title='(a) 符号方向')
    ax1.axhline(0, color=GRID, lw=.4); ax1.axvline(0, color=GRID, lw=.4)
    ax1.set_xticks([-1, 0, 1]); ax1.set_yticks([-1, 0, 1])
    # Muon polynomial maps
    s = np.logspace(-3, 0, 600)
    a, b, c = 3.4445, -4.7750, 2.0315
    q = s.copy()
    for _ in range(5):
        q = a * q + b * q ** 3 + c * q ** 5
    cub = s.copy()
    for _ in range(5):
        cub = 1.5 * cub - 0.5 * cub ** 3
    ax2.semilogx(s, np.ones_like(s), color=INK, lw=.8, ls='--', label='理想极因子：奇异值变为 1')
    ax2.semilogx(s, q, color=BLUE, lw=1.1, label='五次多项式迭代 5 次')
    ax2.semilogx(s, cub, color=GREEN, lw=1.1, label='三次 Newton–Schulz 迭代 5 次')
    ax2.set(xlabel=r'归一化后的奇异值 $s$', ylabel='输出奇异值', title='(b) Muon 的奇异值映射', ylim=(0, 1.3))
    ax2.legend(loc='lower right', handlelength=1.4, fontsize=7)
    mask = s > 0.02
    save(fig, D/'c6-lion-muon', 'figure', {
        'lion_readings': {'g_a': g1.tolist(), 'g_b': g2.tolist(), 'g_c': g3.tolist()}, 'arrow_scale': sc,
        'muon_quintic': [a, b, c], 'iterations': 5,
        'quintic_range_for_s_in_[0.02,1]': [round(float(q[mask].min()), 3), round(float(q[mask].max()), 3)],
        'cubic_at_s=0.01': round(float(cub[np.argmin(abs(s - 0.01))]), 4),
        'quintic_at_s=0.01': round(float(q[np.argmin(abs(s - 0.01))]), 4),
        'cubic_at_s=0.1': round(float(cub[np.argmin(abs(s - 0.1))]), 4)})


# ---------------------------------------------------------------- 6.5
def c6_coordinate_descent():
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=64, ncols=2)
    Phi = lambda u, v: 0.5 * (u - v) ** 2 + 0.5 * (u - 1) ** 2
    U, V = np.meshgrid(np.linspace(-2.2, 2.2, 300), np.linspace(-2.2, 2.6, 300))
    ax1.contour(U, V, Phi(U, V), levels=[0.02, 0.1, 0.3, 0.7, 1.3, 2.2, 3.5, 5], colors=GRID, linewidths=.6)
    u, v = -2.0, 2.4
    path = [(u, v)]
    for t in range(6):
        u = (v + 1) / 2; path.append((u, v))
        v = u; path.append((u, v))
    path = np.array(path)
    ax1.plot(path[:, 0], path[:, 1], '-o', color=BLUE, lw=1.0, ms=2.2, label='循环坐标下降（逐块精确）')
    Hm = np.array([[2.0, -1.0], [-1.0, 1.0]]); Lh = np.linalg.eigvalsh(Hm).max()
    x = np.array([-2.0, 2.4]); gp = [x.copy()]
    for t in range(12):
        g = np.array([(x[0] - x[1]) + (x[0] - 1), -(x[0] - x[1])]); x = x - g / Lh; gp.append(x.copy())
    gp = np.array(gp)
    ax1.plot(gp[:, 0], gp[:, 1], '-o', color=GREEN, lw=.9, ms=1.8, label=r'梯度下降 $\eta=1/L$')
    ax1.plot(1, 1, '*', color=INK, ms=7)
    ax1.set(xlabel=r'$u$', ylabel=r'$v$', aspect='equal', title=r'(a) $\frac{1}{2}(u-v)^2+\frac{1}{2}(u-1)^2$')
    ax1.legend(loc='lower right', fontsize=7, handlelength=1.2)
    F = lambda u, v: 2 * np.abs(u - v) + np.abs(u + v - 2)
    U, V = np.meshgrid(np.linspace(-1.2, 2.2, 400), np.linspace(-1.2, 2.2, 400))
    ax2.contour(U, V, F(U, V), levels=[0.5, 1, 1.5, 2, 3, 4, 5], colors=GRID, linewidths=.6)
    cs = ax2.contour(U, V, F(U, V), levels=[2], colors=[YELLOW], linewidths=1.0)
    ax2.axhline(0, color=RED, lw=.8, ls='--'); ax2.axvline(0, color=RED, lw=.8, ls='--')
    ax2.plot(0, 0, 'o', color=RED, ms=4); ax2.plot(1, 1, '*', color=INK, ms=7)
    ax2.text(0.06, -0.22, r'$(0,0)$：$F=2$', color=RED, fontsize=7)
    ax2.text(1.06, 1.12, r'$(1,1)$：$F=0$', color=INK, fontsize=7)
    ax2.set(xlabel=r'$u$', ylabel=r'$v$', aspect='equal', title=r'(b) $2|u-v|+|u+v-2|$')
    save(fig, D/'c6-coordinate-descent', 'figure', {
        'panel_a': 'Phi=1/2(u-v)^2+1/2(u-1)^2, start (-2,2.4); CD: u=(v+1)/2 then v=u; GD eta=1/L, L=%.4f' % Lh,
        'cd_v_values': path[::2, 1].round(4).tolist(),
        'panel_b': 'F=2|u-v|+|u+v-2|, (0,0) unique minimiser along both axes, F(0,0)=2, F(1,1)=0',
        'yellow_level': 2})


def c6_alternating():
    rho = 0.05
    Phi = lambda u, v: 0.5 * (u * v - 1) ** 2 + 0.5 * rho * (u ** 2 + v ** 2)
    U, V = np.meshgrid(np.linspace(-0.6, 3.4, 400), np.linspace(-0.6, 2.4, 400))
    fig, ax = figure(width_mm=105, height_mm=72)
    ax.contour(U, V, Phi(U, V), levels=[0.05, 0.1, 0.2, 0.35, 0.5, 0.8, 1.2, 2, 3], colors=GRID, linewidths=.6)
    u, v = 3.0, 0.1
    path = [(u, v)]; vals = [Phi(u, v)]
    for t in range(8):
        u = v / (v ** 2 + rho); path.append((u, v)); vals.append(Phi(u, v))
        v = u / (u ** 2 + rho); path.append((u, v)); vals.append(Phi(u, v))
    path = np.array(path)
    ax.plot(path[:, 0], path[:, 1], '-o', color=BLUE, lw=1.0, ms=2.2, label=r'从 $(3,0.1)$ 交替精确最小化')
    us = np.sqrt(1 - rho)
    ax.plot(us, us, '*', color=GREEN, ms=8, label=r'最小点 $u=v=\sqrt{1-\rho}$')
    ax.plot(0, 0, 'o', color=RED, ms=4, label=r'从 $(0,0)$ 出发：停在驻点')
    ax.set(xlabel=r'$u$', ylabel=r'$v$', aspect='equal')
    ax.legend(loc='upper right', fontsize=7, handlelength=1.2)
    save(fig, D/'c6-alternating', 'figure', {
        'objective': 'Phi(u,v)=1/2(uv-1)^2+rho/2(u^2+v^2)', 'rho': rho,
        'updates': 'u=v/(v^2+rho), v=u/(u^2+rho)', 'path': path.round(4).tolist(),
        'objective_values': np.round(vals, 5).tolist(), 'minimum': round(float(us), 4),
        'Phi_at_min': round(float(Phi(us, us)), 5), 'Phi_at_origin': 0.5})


# ---------------------------------------------------------------- 6.6
def c6_clipping():
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=58, ncols=2)
    g = np.array([3.0, 4.0])
    th = np.linspace(0, 2 * np.pi, 200)
    ax1.plot(np.cos(th), np.sin(th), color=GREEN, lw=.8)
    ax1.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color=YELLOW, lw=.8)
    for vec, c, lab in [(g, MUTED, r'$g=(3,4)$'), (np.array([1, 1]), YELLOW, r'逐坐标 $(1,1)$'),
                        (g / 5, GREEN, r'按范数 $(0.6,0.8)$')]:
        ax1.annotate('', xy=vec, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.3, mutation_scale=9, shrinkA=0, shrinkB=0))
    ax1.text(3.05, 4.0, r'$g=(3,4)$', color=MUTED, fontsize=7, va='center')
    ax1.text(1.08, 1.12, r'逐坐标 $(1,1)$', color=YELLOW, fontsize=7)
    ax1.text(-0.15, 1.15, r'按范数 $(0.6,0.8)$', color=GREEN, fontsize=7, ha='right')
    ax1.set(xlim=(-2.6, 4.6), ylim=(-1.3, 4.5), aspect='equal', xlabel=r'$g_1$', ylabel=r'$g_2$', title=r'(a) 两种裁剪，$c=1$')
    ax1.axhline(0, color=GRID, lw=.4); ax1.axvline(0, color=GRID, lw=.4)
    cs = np.linspace(0.01, 4, 400)
    two = np.array([0.5 * np.clip(2, -c, c) + 0.5 * np.clip(-1, -c, c) for c in cs])
    # skewed continuous reading: g = -1 + Exp(scale 1.5), mean 0.5
    xx = np.linspace(-1, 40, 400001); dens = np.exp(-(xx + 1) / 1.5) / 1.5; dx = xx[1] - xx[0]
    cont = np.array([np.sum(np.clip(xx, -c, c) * dens) * dx for c in cs])
    ax2.plot(cs, two, color=BLUE, lw=1.1, label=r'两点读数 $2,-1$（各 $1/2$）')
    ax2.plot(cs, cont, color=PURPLE, lw=1.1, label=r'偏斜读数 $-1+\mathrm{Exp}(1.5)$')
    ax2.axhline(0.5, color=INK, lw=.7, ls='--', label=r'未裁剪均值 $1/2$')
    ax2.set(xlabel=r'裁剪阈值 $c$', ylabel=r'$\mathbb{E}\,\mathrm{clip}_c(g)$', title='(b) 裁剪后的平均', ylim=(-0.05, 0.62))
    ax2.legend(loc='lower right', handlelength=1.4, fontsize=7)
    save(fig, D/'c6-clipping', 'figure', {
        'vector': [3, 4], 'c': 1, 'elementwise': [1, 1], 'norm_clip': [0.6, 0.8],
        'two_point_clipped_mean': 'c<1: 0; 1<=c<2: (c-1)/2; c>=2: 1/2',
        'skewed': 'g=-1+Exp(scale 1.5), mean 0.5, clipped mean at c=1: %.4f, c=3: %.4f' % (
            cont[np.argmin(abs(cs - 1))], cont[np.argmin(abs(cs - 3))])})


def c6_ste():
    fig, ax = figure(width_mm=105, height_mm=56)
    w = np.linspace(-0.45, 1.45, 2000)
    q = np.round(w)
    for a, c, lab in [(1.0, BLUE, r'$a=1$'), (0.4, GREEN, r'$a=0.4$')]:
        F = 0.5 * (q - a) ** 2
        Fm = F.copy(); Fm[np.abs(np.diff(np.r_[F[0], F])) > 1e-9] = np.nan
        ax.plot(w, Fm, color=c, lw=1.1, label=rf'$F(w)=\frac{{1}}{{2}}(\mathrm{{round}}(w)-{a:g})^2$')
    pts = [(1.0, 0.4, BLUE), (0.4, 1.0, GREEN)]
    for a, eta, c in pts:
        w0 = 0.2; g = np.round(w0) - a; w1 = w0 - eta * g
        F0 = 0.5 * (np.round(w0) - a) ** 2; F1 = 0.5 * (np.round(w1) - a) ** 2
        ax.plot([w0], [F0], 'o', color=c, ms=3.5)
        ax.plot([w1], [F1], 's', color=c, ms=3.5)
        ax.annotate('', xy=(w1, F1), xytext=(w0, F0), arrowprops=dict(arrowstyle='-|>', color=c, lw=.8, ls='--', connectionstyle='arc3,rad=-0.25', mutation_scale=8))
    ax.axvline(0.5, color=GRID, lw=.6, ls=':')
    ax.text(0.52, 0.36, '取整阈值', color=MUTED, fontsize=7)
    ax.set(xlabel=r'$w$', ylabel=r'$F(w)$', ylim=(-0.03, 0.62))
    ax.legend(loc='upper right', handlelength=1.4, fontsize=7)
    save(fig, D/'c6-ste', 'figure', {
        'a=1': 'w=0.2, STE direction round(w)-a=-1, eta=0.4 -> w=0.6, F: 0.5 -> 0',
        'a=0.4': 'w=0.2, STE direction -0.4, eta=1 -> w=0.6, F: 0.08 -> 0.18'})


# ---------------------------------------------------------------- 6.7
def c6_perturbation():
    P = ls2d()
    xs, H = P['xs'], P['H']
    fig, (ax1, ax2) = figure(width_mm=160, height_mm=60, ncols=2)
    T, R = 1500, 300
    x0 = xs + np.array([-2.6, 2.2])
    bias = np.array([0.25, 0.0])
    s = 0.5
    facts = {'problem': 'ridge least squares d=2, readings grad f + bias + noise/sqrt(batch), noise N(0,s^2 I)',
             's': s, 'bias': bias.tolist(), 'runs': R, 'seed': SEED + 13, 'eta0': 0.4}
    configs = [('仅噪声，$\\eta_0$', 0.4, 1, 0, BLUE, '-'), ('仅噪声，$\\eta_0/4$', 0.1, 1, 0, BLUE, '--'),
               ('仅噪声，$\\eta_0$，批量 4', 0.4, 4, 0, GREEN, '-'),
               ('仅偏差，$\\eta_0$', 0.4, 1, 1, RED, '-'), ('仅偏差，$\\eta_0/4$', 0.1, 1, 1, RED, '--')]
    for lab, eta, bsz, use_b, c, ls in configs:
        rng = np.random.default_rng(SEED + 13)
        X = np.tile(x0, (R, 1)); err = [((X - xs) ** 2).sum(1).mean()]
        for t in range(T):
            noise = 0 if use_b else s * rng.normal(size=(R, 2)) / np.sqrt(bsz)
            g = (X - xs) @ H.T + (bias if use_b else 0) + noise
            X = X - eta * g; err.append(((X - xs) ** 2).sum(1).mean())
        ax1.semilogy(err, color=c, ls=ls, lw=1.1, label=lab)
        facts[lab] = round(float(np.mean(err[-200:])), 5)
    off = np.linalg.solve(H, bias)
    ax1.axhline(float(off @ off), color=RED, lw=.6, ls=':')
    facts['bias_offset_sq'] = round(float(off @ off), 5)
    ax1.set(xlabel=r'迭代 $t$', ylabel=r'$\mathbb{E}\Vert x^{(t)}-x^\star\Vert_2^2$', title='(a) 噪声与偏差')
    ax1.set_ylim(3e-3, 300)
    ax1.legend(loc='upper right', handlelength=1.6, fontsize=6.8, ncols=2, columnspacing=0.8)
    # stability: replace sample 0
    A, b, lam, n = P['A'], P['b'], P['lam'], P['n']
    rng = np.random.default_rng(SEED + 14)
    A2 = A.copy(); b2 = b.copy()
    A2[0] = rng.normal(size=2) * np.array([2.0, 0.5]); b2[0] = A2[0] @ np.array([1.0, -0.5]) + 0.6 * rng.normal()
    L = max(((A ** 2).sum(1) + lam).max(), ((A2 ** 2).sum(1) + lam).max())
    eta = 1.0 / L
    T2, R2 = 800, 2000
    X = np.zeros((R2, 2)); Y = X.copy()
    dist = [0.0]; G = 0.0
    for t in range(T2):
        g0x = A[0] * (X @ A[0] - b[0])[:, None] + lam * X
        g0y = A2[0] * (Y @ A2[0] - b2[0])[:, None] + lam * Y
        G = max(G, np.linalg.norm(g0x, axis=1).max(), np.linalg.norm(g0y, axis=1).max())
        i = rng.integers(0, n, size=R2)
        gx = A[i] * ((A[i] * X).sum(1) - b[i])[:, None] + lam * X
        gy = A2[i] * ((A2[i] * Y).sum(1) - b2[i])[:, None] + lam * Y
        X = X - eta * gx; Y = Y - eta * gy
        dist.append(np.linalg.norm(X - Y, axis=1).mean())
    t = np.arange(T2 + 1)
    lin = 2 * G * eta * t / n
    con = 2 * G / (n * lam) * (1 - (1 - eta * lam) ** t)
    ax2.semilogy(t[1:], dist[1:], color=BLUE, lw=1.1, label=r'$\mathbb{E}\Vert x^{(t)}-\tilde x^{(t)}\Vert_2$（经验）')
    ax2.semilogy(t[1:], lin[1:], color=MUTED, lw=.8, ls='--', label=r'非扩张界 $2G\eta t/n$')
    ax2.semilogy(t[1:], con[1:], color=GREEN, lw=.9, ls='-.', label=r'压缩界 $\frac{2G}{n\lambda}(1-(1-\eta\lambda)^t)$')
    ax2.set(xlabel=r'迭代 $t$', ylabel='参数距离', title='(b) 替换一个样本', ylim=(3e-3, 100))
    ax2.legend(loc='center right', bbox_to_anchor=(1.0, 0.42), handlelength=1.6, fontsize=7)
    facts['stability'] = {'eta': round(eta, 5), 'L': round(L, 4), 'G_replaced_terms': round(float(G), 3), 'runs': R2,
                          'seed': SEED + 14, 'mean_distance_T': round(float(dist[-1]), 4),
                          'mean_distance_t=20': round(float(dist[20]), 4), 'linear_bound_t=20': round(float(lin[20]), 4),
                          'linear_bound_T': round(float(lin[-1]), 3), 'contraction_bound_T': round(float(con[-1]), 3),
                          'replaced_row_old': A[0].round(4).tolist(), 'replaced_row_new': A2[0].round(4).tolist()}
    save(fig, D/'c6-perturbation', 'figure', facts)


# ---------------------------------------------------------------- 6.8
def c6_batch_cost():
    """Exact expected error of minibatch SGD (sampling with replacement) on ridge least squares.

    With e = x - x*, B_i = a_i a_i^T + lam I and g_i* = grad f_i(x*), the first and second moments
    m = E e, M = E e e^T obey exactly
      m+ = (I - eta H) m,
      M+ = M - eta(HM+MH) + eta^2 [HMH + (S(M)-HMH)/b] + eta^2 Sigma*/b + eta^2/b (K(m)+K(m)^T),
    S(M) = mean_i B_i M B_i, Sigma* = mean_i g_i* g_i*^T, K(m) = mean_i B_i m g_i*^T,
    and E f(x) - f* = tr(H M)/2.  For each batch size the step is chosen from a grid to minimise the
    number of sample reads needed to reach E f - f* <= eps."""
    rng = np.random.default_rng(SEED + 15)
    n, d, lam, eps = 10000, 5, 1e-2, 1e-3
    A = rng.normal(size=(n, d)) * np.linspace(1.0, 0.2, d)
    b = A @ rng.normal(size=d) + 1.0 * rng.normal(size=n)
    H = A.T @ A / n + lam * np.eye(d); xs = np.linalg.solve(H, A.T @ b / n)
    gs = A * (A @ xs - b)[:, None] + lam * xs
    Sig = gs.T @ gs / n
    Bm = np.einsum('ip,iq->ipq', A, A) + lam * np.eye(d)
    Sop = np.einsum('ipr,isq->pqrs', Bm, Bm).reshape(d * d, d * d) / n
    K = np.einsum('ipr,iq->prq', Bm, gs) / n
    ev = np.linalg.eigvalsh(H); L, mu = ev[-1], ev[0]
    e0 = -xs
    etas = np.geomspace(1e-3, 1.9 / L, 80)
    bs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    reads, best = [], []
    with np.errstate(over='ignore', invalid='ignore'):
        for bb in bs:
            E = len(etas)
            m = np.tile(e0, (E, 1)); M = np.tile(np.outer(e0, e0), (E, 1, 1)); t = 0
            while True:
                gap = 0.5 * np.einsum('pq,eqp->e', H, M)
                hit = np.where(gap <= eps)[0]
                if hit.size:
                    reads.append(t * bb); best.append(float(etas[hit].min())); break
                et = etas[:, None, None]
                HM = H @ M; MH = M @ H; HMH = H @ M @ H
                SM = (M.reshape(E, -1) @ Sop.T).reshape(E, d, d)
                Km = np.einsum('prq,er->epq', K, m)
                M = M - et * (HM + MH) + et ** 2 * (HMH + (SM - HMH) / bb) + et ** 2 * Sig / bb \
                    + et ** 2 / bb * (Km + Km.transpose(0, 2, 1))
                m = m - etas[:, None] * (m @ H.T)
                t += 1
    x = np.zeros(d); it = 0
    while 0.5 * (x - xs) @ H @ (x - xs) > eps:
        x = x - (1 / L) * (H @ (x - xs)); it += 1
    fig, ax = figure(width_mm=100, height_mm=58)
    ax.loglog(bs, reads, '-o', color=BLUE, lw=1.1, ms=3, label=r'小批量随机梯度（每个 $b$ 取最优常数步长）')
    ax.axhline(it * n, color=GREEN, lw=1.0, ls='--', label=r'梯度下降（每步读 $n$ 项）')
    ax.set(xlabel=r'批量 $b$', ylabel=r'读取量（达到 $\mathbb{E}f-f^\star\leq10^{-3}$）')
    ax.set_ylim(2e4, 2e6)
    ax.legend(loc='upper left', handlelength=1.4, fontsize=7)
    save(fig, D/'c6-batch-cost', 'figure', {
        'problem': 'ridge least squares n=10000,d=5,lam=1e-2, A columns scaled linspace(1,0.2,5), noise 1.0',
        'seed': SEED + 15, 'eps': eps, 'method': 'exact first/second-moment recursion (see docstring)',
        'step_grid': 'geomspace(1e-3, 1.9/L, 80)', 'L': round(float(L), 4), 'mu': round(float(mu), 4),
        'trace_Sigma_star': round(float(np.trace(Sig)), 4), 'x0': 'zeros',
        'batch_sizes': bs, 'reads_needed': [int(r) for r in reads], 'best_eta': [round(e, 4) for e in best],
        'gd_iterations': it, 'gd_reads': it * n})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    c6_gradient_fan, c6_sgd_noise_ball, c6_step_schedules, c6_return_points, c6_importance_sampling,
    c6_minibatch_variance, c6_variance_reduction, c6_adaptive_paths, c6_adafactor, c6_lion_muon,
    c6_coordinate_descent, c6_alternating, c6_clipping, c6_ste, c6_perturbation, c6_batch_cost]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
