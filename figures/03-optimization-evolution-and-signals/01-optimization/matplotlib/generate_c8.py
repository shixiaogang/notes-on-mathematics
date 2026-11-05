# coding: utf-8
"""Teaching figures for volume three, part "optimization", chapter 8
(function fitting and regularization).

Every curve comes from a closed form or a deterministic computation recorded in
the facts file next to each figure; synthetic data use the fixed numpy seed SEED
and are teaching examples, not measurements.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/01-optimization/matplotlib/generate_c8.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from numpy.polynomial import legendre as npleg

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL

D = Path(__file__).resolve().parent
SEED = 20261030


def r4(x):
    return round(float(x), 4)


# ---------------------------------------------------------------- helpers
def leg_basis(x, deg):
    """Shifted Legendre basis P_k(2x-1), k=0..deg, and its second derivative."""
    t = 2 * np.asarray(x) - 1
    V = npleg.legvander(t, deg)
    V2 = np.zeros_like(V)
    for k in range(deg + 1):
        c = np.zeros(deg + 1); c[k] = 1
        V2[:, k] = npleg.legval(t, npleg.legder(c, 2)) * 4.0
    return V, V2


def curvature_gram(deg, nq=80):
    q, w = npleg.leggauss(nq)
    x = (q + 1) / 2; w = w / 2
    _, V2 = leg_basis(x, deg)
    return V2.T @ (w[:, None] * V2)


def gauss_kernel(a, b, s=0.15):
    a = np.asarray(a)[:, None]; b = np.asarray(b)[None, :]
    return np.exp(-(a - b) ** 2 / (2 * s * s))


def noisy_data(n, sd, seed=SEED):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 1, n)
    e = rng.normal(0, sd, n)
    return x, np.sin(2 * np.pi * x) + e, e


# ---------------------------------------------------------------- 8.1
def c8_interpolation_vs_regularization():
    x, y, _ = noisy_data(15, 0.15)
    deg = 14
    V, _ = leg_basis(x, deg)
    R = curvature_gram(deg)
    a_int = np.linalg.solve(V, y)
    lam = 1e-4
    A = np.vstack([V, np.sqrt(lam) * np.linalg.cholesky(R + 1e-12 * np.eye(deg + 1)).T])
    a_reg = np.linalg.lstsq(A, np.concatenate([y, np.zeros(deg + 1)]), rcond=None)[0]
    t = np.linspace(0, 1, 600)
    Vt, _ = leg_basis(t, deg)
    fi, fr = Vt @ a_int, Vt @ a_reg
    fig, ax = figure(width_mm=100, height_mm=50)
    ax.axhline(0, color=GRID, lw=.4)
    ax.plot(t, fi, color=RED, lw=1.1, label='14次多项式插值')
    ax.plot(t, fr, color=BLUE, lw=1.1, label='曲率惩罚拟合')
    ax.plot(x, y, 'o', color=INK, ms=3.2, zorder=5, label='观测')
    ax.set(xlim=(-0.02, 1.02), ylim=(-3.2, 3.2), xlabel=r'$x$', ylabel=r'$f(x)$')
    ax.legend(loc='lower left', handlelength=1.4, ncol=1)
    curv = lambda a: float(a @ R @ a)
    save(fig, D/'c8-interpolation-vs-regularization', 'figure', {
        'data': 'x_i=i/14 (i=0..14), y_i=sin(2 pi x_i)+e_i, e_i~N(0,0.15^2), seed %d' % SEED,
        'basis': 'shifted Legendre P_k(2x-1), k=0..14',
        'regularized': 'min sum (f(x_i)-y_i)^2 + lambda int_0^1 f\'\'(x)^2 dx, lambda=1e-4',
        'max_abs_interp_on_[0,1]': r4(np.abs(fi).max()), 'max_abs_reg_on_[0,1]': r4(np.abs(fr).max()),
        'curvature_interp': r4(curv(a_int)), 'curvature_reg': r4(curv(a_reg)),
        'train_rss_reg': r4(((V @ a_reg - y) ** 2).sum())})


def c8_invisible_direction():
    t = np.linspace(0, 1, 400)
    f0 = 4 * t * (1 - t)
    p = t * (t - 0.5) * (t - 1)
    fig, ax = figure(width_mm=78, height_mm=46)
    cols = [PURPLE, GREEN, BLUE, YELLOW, RED]
    for c, col in zip([-16, -8, 0, 8, 16], cols):
        ax.plot(t, f0 + c * p, color=col, lw=1.1 if c == 0 else .9,
                label=r'$c=%d$' % c)
    ax.plot([0, .5, 1], [0, 1, 0], 'o', color=INK, ms=3.4, zorder=5)
    ax.set(xlim=(-0.02, 1.02), ylim=(-0.4, 1.6), xlabel=r'$x$', ylabel=r'$f_0+c\,p$')
    ax.legend(loc='upper right', ncol=1, handlelength=1.2, fontsize=7)
    save(fig, D/'c8-invisible-direction', 'figure', {
        'f0': '4x(1-x)', 'p': 'x(x-1/2)(x-1)', 'c': [-16, -8, 0, 8, 16],
        'observations': {'x': [0, 0.5, 1], 'y': [0, 1, 0]}})


def c8_residual_losses():
    r = np.linspace(-3, 3, 601)
    huber = np.where(np.abs(r) <= 1, r ** 2 / 2, np.abs(r) - .5)
    fig, (a, b) = figure(width_mm=112, height_mm=46, ncols=2)
    a.plot(r, r ** 2 / 2, color=BLUE, label=r'$r^2/2$')
    a.plot(r, np.abs(r), color=YELLOW, ls='--', label=r'$|r|$')
    a.plot(r, huber, color=GREEN, label='Huber')
    a.plot(r, np.log1p(r ** 2) / 2, color=RED, ls='-.', label='Cauchy')
    a.set(xlim=(-3, 3), ylim=(0, 3), xlabel=r'$r$', ylabel='代价')
    a.set_title('(a) 残差代价')
    a.legend(loc='upper center', fontsize=6.8, handlelength=1.6)
    rr = r[np.abs(r) > 1e-9]
    b.plot(r, np.ones_like(r), color=BLUE)
    b.plot(rr, 1 / np.abs(rr), color=YELLOW, ls='--')
    b.plot(r, np.minimum(1, 1 / np.maximum(np.abs(r), 1e-9)), color=GREEN)
    b.plot(r, 1 / (1 + r ** 2), color=RED, ls='-.')
    b.set(xlim=(-3, 3), ylim=(0, 1.6), xlabel=r'$r$', ylabel=r'$\psi(r)/r$')
    b.set_title('(b) 等效权重')
    save(fig, D/'c8-residual-losses', 'figure', {
        'square': 'r^2/2', 'absolute': '|r|', 'huber': 'r^2/2 if |r|<=1 else |r|-1/2',
        'cauchy': '(1/2) log(1+r^2)', 'weights': '1, 1/|r|, min(1,1/|r|), 1/(1+r^2)'})


def c8_decay_vs_l2():
    eta, lam, eps, b1, b2 = 0.1, 2.0, 1.0, 0.9, 0.999
    T = 30
    wd = [1.0]; wa = [1.0]; m = v = 0.0
    for k in range(1, T + 1):
        wd.append((1 - eta * lam) * wd[-1])
        g = lam * wa[-1]
        m = b1 * m + (1 - b1) * g; v = b2 * v + (1 - b2) * g * g
        mh = m / (1 - b1 ** k); vh = v / (1 - b2 ** k)
        wa.append(wa[-1] - eta * mh / (np.sqrt(vh) + eps))
    fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
    ks = np.arange(T + 1)
    a.plot(ks, wd, 'o-', color=BLUE, ms=2.2, lw=1.0, label='AdamW')
    a.plot(ks, wa, 's-', color=RED, ms=2.2, lw=1.0, label=r'Adam + $\frac{\lambda}{2}w^2$')
    a.set(xlim=(0, T), ylim=(-0.05, 1.05), xlabel=r'$t$', ylabel=r'$w^{(t)}$')
    a.set_title('(a) 数据梯度为零')
    a.legend(loc='upper right', handlelength=1.6)
    # panel b: fixed preconditioner, F = |w-(1,1)|^2/2, lambda=1, P=diag(1,4)
    P = np.array([1.0, 4.0]); c = np.array([1.0, 1.0]); lb = 1.0; et = 0.15
    g1, g2 = np.meshgrid(np.linspace(-0.1, 1.2, 200), np.linspace(-0.1, 1.2, 200))
    Fv = ((g1 - 1) ** 2 + (g2 - 1) ** 2) / 2
    b.contour(g1, g2, Fv, levels=[0.02, 0.08, 0.18, 0.32, 0.5, 0.72], colors=GRID, linewidths=.6)
    wc = np.zeros(2); wdc = np.zeros(2); pc = [wc.copy()]; pd = [wdc.copy()]
    for _ in range(40):
        wc = wc - et * P * ((wc - c) + lb * wc); pc.append(wc.copy())
        wdc = wdc - et * (P * (wdc - c) + lb * wdc); pd.append(wdc.copy())
    pc, pd = np.array(pc), np.array(pd)
    b.plot(pc[:, 0], pc[:, 1], '-', color=RED, lw=.9)
    b.plot(pd[:, 0], pd[:, 1], '-', color=BLUE, lw=.9)
    b.plot([.5], [.5], 's', color=RED, ms=4, label=r'$P(\nabla F+\lambda w)$')
    b.plot([.5], [.8], 'o', color=BLUE, ms=4, label=r'$P\nabla F+\lambda w$')
    b.plot([1], [1], '+', color=INK, ms=6)
    b.text(1.03, 1.03, 'F最小点', fontsize=7, color=INK)
    b.set(xlim=(-0.1, 1.2), ylim=(-0.1, 1.2), xlabel=r'$w_1$', ylabel=r'$w_2$', aspect='equal')
    b.set_title('(b) 固定预条件的不动点')
    b.legend(loc='lower right', fontsize=6.8, handlelength=1.0)
    save(fig, D/'c8-decay-vs-l2', 'figure', {
        'panel_a': {'eta': eta, 'lambda': lam, 'eps': eps, 'beta1': b1, 'beta2': b2, 'w0': 1,
                    'data_gradient': 0, 'adamw_w1': r4(wd[1]), 'adam_l2_w1': r4(wa[1]),
                    'adamw_w10': r4(wd[10]), 'adam_l2_w10': r4(wa[10]), 'adam_l2_w30': r4(wa[30])},
        'panel_b': {'F': '|w-(1,1)|^2/2', 'lambda': lb, 'P': 'diag(1,4)', 'eta': et, 'w0': [0, 0],
                    'coupled_fixed_point': [0.5, 0.5], 'decoupled_fixed_point': [0.5, 0.8],
                    'coupled_final': [r4(pc[-1, 0]), r4(pc[-1, 1])], 'decoupled_final': [r4(pd[-1, 0]), r4(pd[-1, 1])]}})


# ---------------------------------------------------------------- 8.2
def c8_ridge_filter():
    s = np.logspace(-3, 1, 400)
    fig, ax = figure(width_mm=80, height_mm=46)
    for lam, col, ls in [(1e-4, BLUE, '-'), (1e-2, GREEN, '--'), (1.0, RED, '-.')]:
        ax.semilogx(s, s ** 2 / (s ** 2 + lam), color=col, ls=ls, label=r'$\lambda=%s$' % (
            {1e-4: '10^{-4}', 1e-2: '10^{-2}', 1.0: '1'}[lam]))
        ax.plot([np.sqrt(lam)], [.5], 'o', color=col, ms=3)
    ax.axhline(.5, color=GRID, lw=.4)
    ax.set(xlim=(1e-3, 10), ylim=(-0.02, 1.05), xlabel=r'$\sigma_k$',
           ylabel=r'$\sigma_k^2/(\sigma_k^2+\lambda)$')
    ax.legend(loc='upper left', handlelength=1.6)
    save(fig, D/'c8-ridge-filter', 'figure', {
        'filter': 'sigma^2/(sigma^2+lambda)', 'lambda': [1e-4, 1e-2, 1], 'half_point': 'sigma=sqrt(lambda)'})


def irls(x, y, c, iters=50, w0=None):
    Xd = np.column_stack([np.ones_like(x), x])
    w = np.linalg.lstsq(Xd, y, rcond=None)[0] if w0 is None else w0
    for _ in range(iters):
        r = Xd @ w - y
        g = 1 / (1 + (r / c) ** 2)
        sw = np.sqrt(g)
        w = np.linalg.lstsq(sw[:, None] * Xd, sw * y, rcond=None)[0]
    r = Xd @ w - y
    return w, 1 / (1 + (r / c) ** 2)


def c8_irls_outliers():
    rng = np.random.default_rng(SEED + 1)
    x = np.linspace(0, 1, 14)
    y = 1 + 2 * x + rng.normal(0, 0.08, x.size)
    y[[10, 12]] += np.array([-2.2, -2.6])
    Xd = np.column_stack([np.ones_like(x), x])
    wls = np.linalg.lstsq(Xd, y, rcond=None)[0]
    wc, gc = irls(x, y, c=0.2)
    fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
    t = np.array([0, 1.0])
    a.plot(t, wls[0] + wls[1] * t, color=RED, ls='--', label='最小二乘')
    a.plot(t, wc[0] + wc[1] * t, color=BLUE, label='Cauchy IRLS')
    a.scatter(x, y, s=4 + 22 * gc, color=INK, zorder=5, lw=0)
    a.set(xlim=(-0.03, 1.03), ylim=(-0.5, 3.4), xlabel=r'$x$', ylabel=r'$y$')
    a.set_title('(a) 点的面积表示最终权重')
    a.legend(loc='upper left', handlelength=1.6)
    # panel b: constant fit to 0,0,10 with cauchy c=1
    yy = np.array([0, 0, 10.0])
    F = lambda s: 0.5 * np.log1p((s[:, None] - yy[None, :]) ** 2).sum(1)
    s = np.linspace(-2, 12, 800)
    gam = 1 / (1 + (0 - yy) ** 2)
    Q = F(np.array([0.0]))[0] + 0.5 * (gam[None, :] * ((s[:, None] - yy) ** 2 - (0 - yy) ** 2)).sum(1)
    b.plot(s, F(s), color=BLUE, label=r'$F(w)$')
    b.plot(s, Q, color=YELLOW, ls='--', label=r'$Q(w\mid 0)$')
    a1 = 10 / 203
    b.plot([0], F(np.array([0.0])), 'o', color=INK, ms=3)
    b.plot([a1], F(np.array([a1])), 'o', color=RED, ms=3)
    # local minimiser near 10
    aa = 10.0
    for _ in range(200):
        gg = 1 / (1 + (aa - yy) ** 2); aa = (gg * yy).sum() / gg.sum()
    ab = 0.0
    for _ in range(200):
        gg = 1 / (1 + (ab - yy) ** 2); ab = (gg * yy).sum() / gg.sum()
    b.plot([aa], F(np.array([aa])), 'v', color=PURPLE, ms=3.5)
    b.set(xlim=(-2, 12), ylim=(1.5, 6.5), xlabel=r'$w$', ylabel='目标值')
    b.set_title('(b) 常数拟合 0, 0, 10')
    b.legend(loc='upper center', handlelength=1.6, fontsize=7)
    save(fig, D/'c8-irls-outliers', 'figure', {
        'panel_a': {'data': 'x=linspace(0,1,14), y=1+2x+N(0,0.08^2), y[10]-=2.2, y[12]-=2.6, seed %d' % (SEED + 1),
                    'ls_line': [r4(wls[0]), r4(wls[1])], 'cauchy_c': 0.2, 'cauchy_line': [r4(wc[0]), r4(wc[1])],
                    'outlier_weights': [r4(gc[10]), r4(gc[12])], 'min_inlier_weight': r4(np.delete(gc, [10, 12]).min())},
        'panel_b': {'objective': 'F(a)=(1/2) sum log(1+(a-y_i)^2), y=(0,0,10)', 'first_weights': [1, 1, r4(1 / 101)],
                    'a1': '10/203', 'limit_from_0': r4(ab), 'F_limit_from_0': r4(F(np.array([ab]))[0]),
                    'limit_from_10': r4(aa), 'F_limit_from_10': r4(F(np.array([aa]))[0])}})


# ---------------------------------------------------------------- 8.3
def c8_gn_lm_scalar():
    th0 = .5; r0 = th0 ** 2 - 4; J = 2 * th0
    th = np.linspace(-0.5, 4.6, 600)
    F = (th ** 2 - 4) ** 2 / 2
    p = th - th0
    m = (r0 + J * p) ** 2 / 2
    mu = 4.0
    mlm = m + mu * p ** 2 / 2
    fig, ax = figure(width_mm=96, height_mm=52)
    ax.plot(th, F, color=BLUE, label=r'$F(\theta)=\frac{1}{2}(\theta^2-4)^2$')
    ax.plot(th, m, color=YELLOW, ls='--', label=r'$m(p)=\frac{1}{2}(r+Jp)^2$')
    ax.plot(th, mlm, color=GREEN, ls='-.', label=r'$m(p)+2p^2$')
    ax.plot([th0], [r0 ** 2 / 2], 'o', color=INK, ms=3.2)
    ax.annotate('', xy=(4.25, 11.2), xytext=(th0, 7.03 + 0.2),
                arrowprops=dict(arrowstyle='->', color=RED, lw=.8))
    ax.text(4.2, 11.6, r'$\theta=17/4,\ F\approx98.9$', ha='right', fontsize=7, color=RED)
    ax.plot([1.25], [1521 / 512], 'o', color=GREEN, ms=3.4)
    ax.annotate(r'$\theta=5/4$', xy=(1.25, 1521 / 512), xytext=(1.6, 4.6), fontsize=7, color=GREEN,
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=.7))
    ax.set(xlim=(-0.5, 4.6), ylim=(0, 12.5), xlabel=r'$\theta$', ylabel='目标值')
    ax.legend(loc='center right', fontsize=7, handlelength=1.6, bbox_to_anchor=(1.0, 0.42))
    save(fig, D/'c8-gn-lm-scalar', 'figure', {
        'residual': 'r(theta)=theta^2-4', 'theta0': 0.5, 'F0': '225/32', 'J': 1,
        'gn_step': '15/4', 'gn_F': '50625/512', 'lm_tau': 4, 'lm_step': '3/4', 'lm_F': '1521/512',
        'pred': '81/32', 'ared': '2079/512', 'ratio': '77/48'})


def c8_lm_path():
    t = np.arange(5.0)
    y = np.array([2.0, 1.1, 0.6, 0.35, 0.2])
    def res(th):
        return th[0] * np.exp(-th[1] * t) - y
    def jac(th):
        e = np.exp(-th[1] * t)
        return np.column_stack([e, -th[0] * t * e])
    th0 = np.array([0.8, 0.05])
    r0, J0 = res(th0), jac(th0)
    g0 = J0.T @ r0
    taus = np.concatenate([[0], np.logspace(-3, 3, 300)])
    path = np.array([th0 + np.linalg.solve(J0.T @ J0 + tau * np.eye(2), -g0) for tau in taus])
    A, B = np.meshgrid(np.linspace(0.4, 2.8, 260), np.linspace(-0.15, 1.05, 260))
    E = np.exp(-B[..., None] * t)
    Fv = 0.5 * ((A[..., None] * E - y) ** 2).sum(-1)
    # true minimiser by GN iterations from a good start
    th = np.array([2.0, 0.6])
    for _ in range(50):
        th = th + np.linalg.lstsq(jac(th), -res(th), rcond=None)[0]
    fig, ax = figure(width_mm=96, height_mm=62)
    ax.contour(A, B, np.log10(Fv + 1e-4), levels=np.linspace(-2.5, 1.0, 13), colors=GRID, linewidths=.6, linestyles='solid')
    ax.plot(path[:, 0], path[:, 1], color=BLUE, lw=1.1, label=r'$\theta^{(0)}+p(\tau)$')
    ax.plot(*path[0], 's', color=RED, ms=3.6, label='GN步')
    for tau in [0.1, 1, 10]:
        q = th0 + np.linalg.solve(J0.T @ J0 + tau * np.eye(2), -g0)
        ax.plot(*q, 'o', color=BLUE, ms=2.6)
        ax.text(q[0] + (0.05 if tau > 0.5 else -0.22), q[1] - (0.02 if tau > 0.5 else -0.01), r'$\tau=%g$' % tau, fontsize=7, color=BLUE)
    d = -g0 / np.linalg.norm(g0)
    ax.annotate('', xy=th0 + 0.35 * d, xytext=th0, arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.0))
    ax.text(*(th0 + 0.35 * d + np.array([0.02, 0.03])), r'$-\nabla F$', fontsize=7, color=GREEN)
    ax.plot(*th0, 'o', color=INK, ms=3.4)
    ax.text(th0[0] - 0.05, th0[1] - 0.09, r'$\theta^{(0)}$', fontsize=7.5)
    ax.plot(*th, '+', color=INK, ms=6)
    ax.text(th[0] + 0.05, th[1] + 0.02, '最小点', fontsize=7)
    ax.set(xlim=(0.4, 2.8), ylim=(-0.15, 1.05), xlabel=r'$\theta_1$', ylabel=r'$\theta_2$')
    ax.legend(loc='upper right', fontsize=7, handlelength=1.4)
    save(fig, D/'c8-lm-path', 'figure', {
        'model': 'theta1*exp(-theta2*t), t=0..4', 'y': y.tolist(), 'theta0': th0.tolist(),
        'gn_point': [r4(v) for v in path[0]], 'minimiser': [r4(v) for v in th],
        'F_theta0': r4(0.5 * (r0 ** 2).sum()), 'F_gn_point': r4(0.5 * (res(path[0]) ** 2).sum()),
        'F_min': r4(0.5 * (res(th) ** 2).sum()), 'tau_marks': [0.1, 1, 10],
        'contours': 'log10 F levels from -2.5 to 1.0'})


# ---------------------------------------------------------------- 8.4
def c8_min_kernel_fit():
    t = np.linspace(0, 1, 400)
    k1, k2 = np.minimum(t, .5), np.minimum(t, 1.0)
    f_lam = 0.8 * k1 + 0.4 * k2
    f_dag = 2 * k1
    r = 0.25 * np.sin(2 * np.pi * t)
    fig, (a, b) = figure(width_mm=112, height_mm=54, ncols=2)
    a.plot(t, k1, color=MUTED, lw=.7, ls=':')
    a.plot(t, k2, color=MUTED, lw=.7, ls=':')
    a.text(.78, .44, r'$K_{1/2}$', fontsize=7, color=MUTED)
    a.text(.76, .86, r'$K_{1}$', fontsize=7, color=MUTED, ha='right', va='center')
    a.plot(t, f_lam, color=BLUE, label=r'$\lambda=1/4$')
    a.plot(t, f_dag, color=RED, ls='--', label=r'$\lambda\downarrow0$')
    a.plot([.5, 1], [1, 1], 'o', color=INK, ms=3.2, zorder=5)
    a.set(xlim=(0, 1.02), ylim=(-0.05, 1.25), xlabel=r'$x$', ylabel=r'$f(x)$')
    a.set_title('(a) 核截面与正则化解')
    a.legend(loc='upper left', handlelength=1.6)
    b.plot(t, f_dag, color=RED, ls='--', label=r'$f^\dagger,\ \|f^\dagger\|_H^2=2$')
    b.plot(t, f_dag + r, color=PURPLE, label=r'$f^\dagger+r,\ \|\cdot\|_H^2\approx3.23$')
    b.plot(t, r, color=YELLOW, lw=.8, label=r'$r=\frac{1}{4}\sin 2\pi x$')
    b.plot([0, .5, 1], [0, 0, 0], 'o', color=YELLOW, ms=2.6, zorder=5)
    b.plot([.5, 1], [1, 1], 'o', color=INK, ms=3.2, zorder=5)
    b.axhline(0, color=GRID, lw=.4)
    b.set(xlim=(0, 1.02), ylim=(-1.25, 1.3), xlabel=r'$x$')
    b.set_title('(b) 读数相同的两个插值')
    b.legend(loc='lower left', fontsize=6.8, handlelength=1.6)
    nr = (0.25 * 2 * np.pi) ** 2 / 2
    save(fig, D/'c8-min-kernel-fit', 'figure', {
        'kernel': 'K(s,t)=min(s,t) on [0,1], ||f||_H^2=int f\'^2', 'points': [0.5, 1], 'y': [1, 1], 'n': 2,
        'lambda': 0.25, 'coeff_lambda': [0.8, 0.4], 'readings_lambda': [0.6, 0.8], 'norm2_lambda': 0.8,
        'coeff_dagger': [2, 0], 'norm2_dagger': 2, 'r': '(1/4) sin(2 pi x)', 'norm2_r': r4(nr),
        'norm2_dagger_plus_r': r4(2 + nr)})


# ---------------------------------------------------------------- 8.5
def c8_spectral_shrinkage():
    j = np.arange(1, 41)
    mu = 1 / ((j - .5) * np.pi) ** 2
    lams = [(1e-1, RED, '-.'), (1e-2, GREEN, '--'), (1e-3, BLUE, '-')]
    fig, (a, b) = figure(width_mm=112, height_mm=48, ncols=2)
    facts = {'kernel': 'min(s,t) on [0,1], Lebesgue', 'mu_j': '((j-1/2) pi)^-2',
             'target': 'y=1', 'fit': '1-cosh((1-x)/sqrt(lambda))/cosh(1/sqrt(lambda))', 'effective_dim': {}}
    x = np.linspace(0, 1, 500)
    for lam, col, ls in lams:
        lab = {1e-1: '10^{-1}', 1e-2: '10^{-2}', 1e-3: '10^{-3}'}[lam]
        a.plot(j, mu / (mu + lam), ls, color=col, marker='o', ms=1.8, lw=.8, label=r'$\lambda=%s$' % lab)
        f = 1 - np.cosh((1 - x) / np.sqrt(lam)) / np.cosh(1 / np.sqrt(lam))
        b.plot(x, f, color=col, ls=ls)
        jj = np.arange(1, 2_000_001); mm = 1 / ((jj - .5) * np.pi) ** 2
        facts['effective_dim'][str(lam)] = r4((mm / (mm + lam)).sum())
        # spectral check of the closed form at x=0.5
        wj = (jj[:20000] - .5) * np.pi; c = np.sqrt(2) / wj; bj = mm[:20000] * c / (mm[:20000] + lam)
        facts['check_x0.5_' + str(lam)] = [r4((bj * np.sqrt(2) * np.sin(wj * .5)).sum()),
                                          r4(1 - np.cosh(.5 / np.sqrt(lam)) / np.cosh(1 / np.sqrt(lam)))]
    a.set(xlim=(0, 41), ylim=(-0.03, 1.05), xlabel=r'$j$', ylabel=r'$\mu_j/(\mu_j+\lambda)$')
    a.set_title('(a) 各谱方向的保留比例')
    a.legend(loc='upper right', handlelength=1.6)
    b.plot(x, np.ones_like(x), color=INK, lw=.8, ls=':', label=r'$y=1$')
    b.set(xlim=(0, 1), ylim=(-0.03, 1.1), xlabel=r'$x$', ylabel=r'$f_\lambda(x)$')
    b.set_title('(b) 常数目标的拟合')
    b.legend(loc='lower right', handlelength=1.6)
    save(fig, D/'c8-spectral-shrinkage', 'figure', facts)


def c8_gradient_projection():
    n = 15
    g = np.linspace(0, 1, n)
    X, Y = np.meshgrid(g, g)
    s, c = np.sin, np.cos
    pi = np.pi
    gphi = np.array([pi * c(pi * X) * s(pi * Y), pi * s(pi * X) * c(pi * Y)])
    k = 0.8
    # curl psi = (psi_y, -psi_x), psi = k sin(pi x) sin(pi y)
    rot = np.array([k * pi * s(pi * X) * c(pi * Y), -k * pi * c(pi * X) * s(pi * Y)])
    v = gphi + rot
    fig, axs = figure(width_mm=112, height_mm=42, ncols=3)
    G = np.linspace(0, 1, 120); XX, YY = np.meshgrid(G, G)
    for ax, field, col, title in [(axs[0], v, INK, '(a) 给定场'),
                                  (axs[1], gphi, BLUE, '(b) 梯度投影'),
                                  (axs[2], rot, RED, '(c) 余项')]:
        if ax is axs[1]:
            ax.contourf(XX, YY, s(pi * XX) * s(pi * YY), levels=6, colors=[BLUE_FILL, '#EEF1F5', 'white', BLUE_FILL, '#DCE3EB', '#D2DBE6'], alpha=1)
            ax.contour(XX, YY, s(pi * XX) * s(pi * YY), levels=6, colors=GRID, linewidths=.4)
        ax.quiver(X, Y, field[0], field[1], color=col, scale=40, width=0.008, headwidth=3.5)
        ax.set(xlim=(-0.03, 1.03), ylim=(-0.03, 1.03), aspect='equal', xticks=[0, 1], yticks=[0, 1])
        ax.set_title(title)
    save(fig, D/'c8-gradient-projection', 'figure', {
        'domain': 'unit square', 'u': 'sin(pi x) sin(pi y) in H_0^1', 'psi': '0.8 sin(pi x) sin(pi y)',
        'v': 'grad u + (psi_y, -psi_x)', 'orthogonality': 'int (psi_y h_x - psi_x h_y) = 0 for h in H_0^1',
        'grid': '15x15 arrows'})


# ---------------------------------------------------------------- 8.6
def kr_fit(x, y, lam, t, s=0.15):
    n = x.size
    G = gauss_kernel(x, x, s)
    a = np.linalg.solve(G + n * lam * np.eye(n), y)
    return gauss_kernel(t, x, s) @ a, a, G


def c8_data_perturbation():
    x, y, _ = noisy_data(12, 0.1, SEED + 2)
    dy = np.zeros_like(y); dy[5] = 0.4
    t = np.linspace(0, 1, 500)
    fig, axs = figure(width_mm=112, height_mm=48, ncols=2, sharey=True)
    facts = {'kernel': 'Gaussian sigma=0.15', 'n': 12, 'data': 'x=linspace(0,1,12), y=sin(2 pi x)+N(0,0.1^2), seed %d' % (SEED + 2),
             'delta_y': '0.4 at the sixth point x=5/11'}
    for ax, lam, title in [(axs[0], 1e-7, r'(a) $\lambda=10^{-7}$'), (axs[1], 1e-2, r'(b) $\lambda=10^{-2}$')]:
        f1, a1, G = kr_fit(x, y, lam, t)
        f2, a2, _ = kr_fit(x, y + dy, lam, t)
        ax.fill_between(t, f1, f2, color=YELLOW_FILL, lw=0)
        ax.plot(t, f1, color=BLUE, label=r'$y$')
        ax.plot(t, f2, color=RED, ls='--', label=r'$y+\delta y$')
        ax.plot(x, y, 'o', color=INK, ms=3)
        ax.plot([x[5]], [y[5] + dy[5]], 'o', mfc='white', mec=RED, ms=3.4)
        ax.set(xlim=(0, 1), ylim=(-1.6, 1.6), xlabel=r'$x$')
        ax.set_title(title)
        da = a2 - a1
        nH = float(np.sqrt(da @ G @ da)); n = x.size
        facts[str(lam)] = {'delta_f_H': r4(nH), 'bound_1_over_2sqrt(n lambda)': r4(0.4 / (2 * np.sqrt(n * lam))),
                           'max_abs_delta_f': r4(np.abs(f2 - f1).max())}
    axs[0].set_ylabel(r'$f(x)$')
    axs[0].legend(loc='lower left', handlelength=1.6)
    save(fig, D/'c8-data-perturbation', 'figure', facts)


def c8_lcurve():
    x, y, e = noisy_data(15, 0.15, SEED + 3)
    n = x.size
    t = np.linspace(0, 1, 500)
    G = gauss_kernel(x, x)
    lams = np.logspace(-8, 0, 120)
    res, nrm = [], []
    for lam in lams:
        a = np.linalg.solve(G + n * lam * np.eye(n), y)
        res.append(np.linalg.norm(G @ a - y)); nrm.append(np.sqrt(a @ G @ a))
    res, nrm = np.array(res), np.array(nrm)
    delta = np.linalg.norm(e)
    k = np.argmin(np.abs(res - delta)); lam_d = lams[k]
    fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
    marks = [(1e-7, PURPLE, ':'), (1e-4, BLUE, '-'), (lam_d, GREEN, '--'), (1e-1, RED, '-.')]
    for lam, col, ls in marks:
        f, _, _ = kr_fit(x, y, lam, t)
        lab = r'$\lambda=%s$' % ('%.0e' % lam).replace('e-0', r'\times10^{-').replace('e-', r'\times10^{-') if False else None
        a.plot(t, f, color=col, ls=ls, lw=1.0)
    a.plot(x, y, 'o', color=INK, ms=2.8, zorder=5)
    a.set(xlim=(0, 1), ylim=(-2.0, 2.0), xlabel=r'$x$', ylabel=r'$f_\lambda(x)$')
    a.set_title('(a) 同一数据上的解族')
    b.loglog(nrm, res, color=MUTED, lw=.9)
    for lam, col, _ in marks:
        aa = np.linalg.solve(G + n * lam * np.eye(n), y)
        b.plot(np.sqrt(aa @ G @ aa), np.linalg.norm(G @ aa - y), 'o', color=col, ms=3.4)
    b.axhline(delta, color=GREEN, lw=.6, ls=':')
    b.text(nrm.min() * 1.05, delta * 1.12, r'$\|e\|_2$', fontsize=7, color=GREEN)
    b.set(xlabel=r'$\|f_\lambda\|_H$', ylabel=r'$\|Lf_\lambda-y\|_2$')
    b.set_title('(b) 残差与函数范数')
    labels = {PURPLE: r'$10^{-7}$', BLUE: r'$10^{-4}$', GREEN: r'$%.1f\times10^{%d}$' % (lam_d / 10 ** np.floor(np.log10(lam_d)), np.floor(np.log10(lam_d))), RED: r'$10^{-1}$'}
    for lam, col, _ in marks:
        aa = np.linalg.solve(G + n * lam * np.eye(n), y)
        b.text(np.sqrt(aa @ G @ aa) * 1.12, np.linalg.norm(G @ aa - y), labels[col], fontsize=7, color=col, va='center')
    save(fig, D/'c8-lcurve', 'figure', {
        'kernel': 'Gaussian sigma=0.15', 'n': n, 'data': 'x=linspace(0,1,15), y=sin(2 pi x)+e, e~N(0,0.15^2), seed %d' % (SEED + 3),
        'noise_norm': r4(delta), 'lambda_discrepancy': float('%.3g' % lam_d),
        'marks': [1e-7, 1e-4, float('%.3g' % lam_d), 1e-1],
        'residual_at_marks': [r4(np.linalg.norm(G @ np.linalg.solve(G + n * l * np.eye(n), y) - y)) for l, _, _ in marks],
        'norm_at_marks': [r4(np.sqrt((lambda q: q @ G @ q)(np.linalg.solve(G + n * l * np.eye(n), y)))) for l, _, _ in marks]})


# ---------------------------------------------------------------- 8.7
def c8_implicit_bias_gd():
    fig, ax = figure(width_mm=80, height_mm=62)
    s = np.linspace(-0.6, 1.6, 10)
    ax.plot(s, 1 - s, color=INK, lw=.9)
    ax.text(1.02, 0.08, r'$w_1+w_2=1$', fontsize=7)
    th = np.linspace(0, 2 * np.pi, 300)
    rad = np.sqrt(.5)
    ax.plot(rad * np.cos(th), rad * np.sin(th), color=BLUE, lw=.6, ls=':')
    # ellipse w^T P^{-1} w = c, P=diag(1,4): w1^2 + w2^2/4 = 1/25+16/100 = 0.2
    cst = 0.2
    ax.plot(np.sqrt(cst) * np.cos(th), 2 * np.sqrt(cst) * np.sin(th), color=RED, lw=.6, ls=':')
    X = np.array([1.0, 1.0]); y = 1.0; eta = 0.3
    for P, col, mk in [(np.array([1.0, 1.0]), BLUE, 'o'), (np.array([1.0, 4.0]), RED, 's')]:
        w = np.zeros(2); pts = [w.copy()]
        for _ in range(30):
            w = w - (0.15 if P[1] > 1 else eta) * P * X * (X @ w - y); pts.append(w.copy())
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], '-', color=col, lw=.9)
        ax.plot(pts[:6, 0], pts[:6, 1], mk, color=col, ms=2.2)
    w = np.array([1.2, -0.5]); pts = [w.copy()]
    for _ in range(30):
        w = w - eta * X * (X @ w - y); pts.append(w.copy())
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], '-', color=GREEN, lw=.9)
    ax.plot(pts[:6, 0], pts[:6, 1], '^', color=GREEN, ms=2.4)
    ax.plot([.5], [.5], 'o', color=BLUE, ms=4.2, mfc='white')
    ax.plot([.2], [.8], 's', color=RED, ms=4.2, mfc='white')
    ax.plot([1.35], [-0.35], '^', color=GREEN, ms=4.2, mfc='white')
    ax.text(.55, .5, r'$(\frac{1}{2},\frac{1}{2})$', fontsize=7, color=BLUE)
    ax.text(.26, .84, r'$(\frac{1}{5},\frac{4}{5})$', fontsize=7, color=RED)
    ax.text(1.24, -0.64, r'$w^{(0)}$', fontsize=7, color=GREEN)
    ax.plot([0], [0], 'o', color=INK, ms=2.6)
    ax.set(xlim=(-0.6, 1.6), ylim=(-0.75, 1.25), xlabel=r'$w_1$', ylabel=r'$w_2$', aspect='equal')
    save(fig, D/'c8-implicit-bias-gd', 'figure', {
        'X': [1, 1], 'y': 1, 'objective': '(w1+w2-1)^2/2', 'eta': eta,
        'P_I_limit': [0.5, 0.5], 'P_diag14_limit': [0.2, 0.8], 'nonzero_start': [1.2, -0.5],
        'nonzero_limit': [1.35, -0.35], 'eta_P_diag14': 0.15, 'level_sets': 'circle |w|^2=1/2, ellipse w1^2+w2^2/4=1/5'})


def c8_separable_direction():
    Xp = np.array([[1.0, 2.0], [2.0, 1.5], [2.5, 3.0]])
    Xn = np.array([[-1.0, -0.5], [-2.0, -2.0], [-0.5, -2.5]])
    Xs = np.vstack([Xp, Xn]); ys = np.array([1, 1, 1, -1, -1, -1.0])
    Z = ys[:, None] * Xs
    # hard-margin homogeneous SVM via projected dual ascent (small QP), checked by KKT
    Q = Z @ Z.T
    al = np.zeros(6)
    for _ in range(200000):
        al = np.maximum(0, al + 1e-3 * (1 - Q @ al))
    wh = Z.T @ al
    marg = Z @ wh
    eta = 1.0
    w = np.zeros(2)
    ts = np.unique(np.round(np.logspace(0, 6, 40)).astype(int))
    rec = []
    tcur = 0
    angs = []
    for T in ts:
        while tcur < T:
            m = Z @ w
            g = -(Z * (1 / (1 + np.exp(m)))[:, None]).mean(0)
            w = w - eta * g; tcur += 1
        ang = np.degrees(np.arccos(np.clip(w @ wh / np.linalg.norm(w) / np.linalg.norm(wh), -1, 1)))
        angs.append(ang); rec.append(w.copy())
    fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
    a.plot(Xp[:, 0], Xp[:, 1], 'o', color=BLUE, ms=3.4)
    a.plot(Xn[:, 0], Xn[:, 1], 's', color=RED, ms=3.2)
    u = np.linspace(-3.2, 3.2, 10)
    dirn = np.array([-wh[1], wh[0]])
    a.plot(u * dirn[0] / np.linalg.norm(dirn), u * dirn[1] / np.linalg.norm(dirn), color=INK, lw=.9)
    for idx, col in [(0, YELLOW), (len(ts) // 3, GREEN)]:
        wv = rec[idx]; dv = np.array([-wv[1], wv[0]])
        a.plot(u * dv[0] / np.linalg.norm(dv), u * dv[1] / np.linalg.norm(dv), color=col, lw=.8, ls='--')
    a.annotate('', xy=1.2 * wh / np.linalg.norm(wh), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=INK, lw=.9))
    a.text(*(1.25 * wh / np.linalg.norm(wh) + np.array([0.05, -0.25])), r'$\hat w$', fontsize=7.5)
    a.set(xlim=(-3, 3), ylim=(-3, 3.3), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_2$')
    a.set_title('(a) 数据与分离方向')
    b.semilogx(ts, angs, 'o-', color=BLUE, ms=2.0, lw=.9)
    b.set(xlim=(1, 1e6), ylim=(0, max(angs) * 1.1), xlabel=r'$t$', ylabel=r'$\angle(w^{(t)},\hat w)$ (°)')
    b.set_title('(b) 方向夹角')
    save(fig, D/'c8-separable-direction', 'figure', {
        'positive': Xp.tolist(), 'negative': Xn.tolist(), 'loss': 'mean log(1+exp(-y w.x))', 'eta': eta,
        'w0': [0, 0], 'hard_margin_w': [r4(v) for v in wh], 'margins_at_hat_w': [r4(v) for v in marg],
        'dashed_lines_iterations': [int(ts[0]), int(ts[len(ts) // 3])],
        'angle_deg_at': {str(int(ts[i])): r4(angs[i]) for i in [0, 10, 20, 30, len(ts) - 1]},
        'norm_w_final': r4(np.linalg.norm(rec[-1]))})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    c8_interpolation_vs_regularization, c8_invisible_direction, c8_residual_losses, c8_decay_vs_l2,
    c8_ridge_filter, c8_irls_outliers, c8_gn_lm_scalar, c8_lm_path, c8_min_kernel_fit,
    c8_spectral_shrinkage, c8_gradient_projection, c8_data_perturbation, c8_lcurve,
    c8_implicit_bias_gd, c8_separable_direction]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
