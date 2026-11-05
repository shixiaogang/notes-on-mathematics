# coding: utf-8
"""Teaching charts for volume two, part "probability spaces", chapter 1
(general probability models and random objects).

Every curve comes from an explicit formula recorded in the saved facts; the only
simulation (none at present) would use the fixed seed below.
Run from any directory:
  python3 figures/02-abstract-mathematics/02-probability-spaces/matplotlib/generate_ch1.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL

D = Path(__file__).resolve().parent
SEED = 20261029


def pmod_almost_sure_limit():
    """X_n(omega)=omega**n on [0,1]: limit 0 except at the null point omega=1."""
    fig, ax = figure(width_mm=100, height_mm=50)
    w = np.linspace(0, 1, 801)
    cols = [BLUE, GREEN, YELLOW, RED, PURPLE]
    for n, c in zip([1, 2, 5, 20, 100], cols):
        ax.plot(w, w**n, color=c, lw=.9, label=rf'$n={n}$')
    ax.plot([0, 1], [0, 0], color=INK, lw=1.4, ls='--')
    ax.plot([1], [1], 'o', color=INK, ms=3.5)
    ax.plot([1], [0], 'o', mfc='white', mec=INK, ms=3.5)
    ax.annotate('极限函数', xy=(0.55, 0.0), xytext=(0.42, 0.18), color=INK, fontsize=7.5,
                arrowprops=dict(arrowstyle='-', color=MUTED, lw=.6))
    ax.annotate('例外点', xy=(0.995, 0.98), xytext=(0.76, 0.86), color=INK, fontsize=7.5,
                arrowprops=dict(arrowstyle='-', color=MUTED, lw=.6))
    ax.set(xlim=(0, 1.04), ylim=(-0.04, 1.06))
    ax.set_xlabel(r'$\omega$')
    ax.set_ylabel(r'$X_n(\omega)=\omega^n$')
    ax.legend(loc='upper left', handlelength=1.4)
    save(fig, D/'pmod-almost-sure-limit', 'figure', {
        'model': 'Omega=[0,1], P=Lebesgue; X_n(omega)=omega**n', 'n_shown': [1, 2, 5, 20, 100],
        'limit': '0 for omega<1, 1 at omega=1', 'exception_set': '{1}', 'P_exception': 0})


def pmod_pushforward_exponential():
    """X(omega)=-log(1-omega) moves uniform mass on [0,1) to the Exp(1) law."""
    a, b = 1.0, 2.0
    lo, hi = 1 - np.exp(-a), 1 - np.exp(-b)
    mass = np.exp(-a) - np.exp(-b)
    fig, axes = figure(width_mm=120, height_mm=52, ncols=2)
    ax = axes[0]
    w = np.linspace(0, 0.985, 600)
    ax.plot(w, -np.log(1 - w), color=BLUE)
    ax.axhspan(a, b, color=YELLOW_FILL, lw=0)
    ax.axvspan(lo, hi, color=BLUE_FILL, lw=0)
    for v in (lo, hi):
        ax.plot([v, v], [0, -np.log(1 - v)], color=MUTED, lw=.6, ls=':')
        ax.plot([0, v], [-np.log(1 - v)] * 2, color=MUTED, lw=.6, ls=':')
    ax.text(0.03, 1.5, r'$B=[1,2]$', color=INK, fontsize=7.5, va='center')
    ax.text((lo + hi) / 2, 3.55, r'$X^{-1}(B)$', color=INK, fontsize=7.5, ha='center')
    ax.set(xlim=(0, 1), ylim=(0, 4))
    ax.set_xlabel(r'$\omega$')
    ax.set_ylabel(r'$X(\omega)$')
    ax.set_title('(a) 样本空间上的映射')
    ax = axes[1]
    x = np.linspace(0, 4, 600)
    ax.plot(x, np.exp(-x), color=BLUE)
    xs = np.linspace(a, b, 200)
    ax.fill_between(xs, np.exp(-xs), color=YELLOW_FILL, lw=0)
    ax.text(1.5, 0.08, rf'${mass:.3f}$', color=INK, fontsize=7.5, ha='center')
    ax.set(xlim=(0, 4), ylim=(0, 1.05))
    ax.set_xlabel(r'$x$')
    ax.set_ylabel('密度')
    ax.set_title('(b) 取值空间上的分布')
    save(fig, D/'pmod-pushforward-exponential', 'figure', {
        'model': 'Omega=[0,1) uniform, X(omega)=-log(1-omega)', 'B': [a, b],
        'preimage': [float(lo), float(hi)], 'P(X in B)': float(mass), 'law': 'Exp(1), density exp(-x)'})


def pmod_reflection_uniform():
    """X(omega)=omega and Y(omega)=1-omega: same law, different values."""
    fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
    ax = axes[0]
    w = np.linspace(0, 1, 200)
    ax.plot(w, w, color=BLUE, label=r'$X(\omega)=\omega$')
    ax.plot(w, 1 - w, color=GREEN, label=r'$Y(\omega)=1-\omega$')
    w0 = 0.25
    ax.plot([w0, w0], [w0, 1 - w0], color=RED, lw=.8)
    ax.plot([w0, w0], [w0, 1 - w0], 'o', color=RED, ms=2.5)
    ax.text(w0 - 0.03, 0.5, rf'$|X-Y|={abs(1 - 2 * w0):g}$', color=RED, fontsize=7.5, va='center', ha='right')
    ax.set(xlim=(0, 1), ylim=(0, 1.0))
    ax.set_xlabel(r'$\omega$')
    ax.set_title('(a) 同一样本点上的取值')
    ax.legend(loc='upper center', handlelength=1.4, bbox_to_anchor=(0.5, -0.2), ncols=2)
    ax = axes[1]
    x = np.linspace(0, 1, 200)
    ax.plot(x, x, color=BLUE, lw=2.2, label=r'$F_X$')
    ax.plot(x, x, color=GREEN, lw=1.0, ls='--', label=r'$F_Y$')
    ax.set(xlim=(0, 1), ylim=(0, 1.0))
    ax.set_xlabel(r'$x$')
    ax.set_ylabel('分布函数')
    ax.set_title('(b) 两者的分布函数')
    ax.legend(loc='upper left', handlelength=1.6)
    save(fig, D/'pmod-reflection-uniform', 'figure', {
        'model': 'Omega=[0,1] uniform; X=omega; Y=1-omega', 'P(X=Y)': 0,
        'E|X-Y|': 0.5, 'shown_point': w0, 'distribution_functions': 'F_X(x)=F_Y(x)=x on [0,1]'})


def pmod_alternating_paths():
    """X_n=Z versus Y_n alternating between Z and 1-Z, for both values of Z."""
    n = np.arange(1, 11)
    fig, axes = figure(width_mm=112, height_mm=54, ncols=2, sharey=True)
    for ax, z, tag in zip(axes, [0, 1], ['(a)', '(b)']):
        x = np.full_like(n, z)
        y = np.where(n % 2 == 1, z, 1 - z)
        ax.plot(n, x + 0.04, 'o-', color=BLUE, ms=3, lw=.8, label=r'$X_n=Z$')
        ax.plot(n, y - 0.04, 's--', color=GREEN, ms=3, lw=.8, label=r'$Y_n$')
        ax.set(xlim=(0.5, 10.5), ylim=(-0.3, 1.3))
        ax.set_xticks(n)
        ax.set_yticks([0, 1])
        ax.set_xlabel(r'$n$')
        ax.set_title(f'{tag} Z = {z}')
    axes[0].set_ylabel('取值')
    fig.legend(*axes[0].get_legend_handles_labels(), loc='outside lower center', ncols=2, handlelength=1.8)
    save(fig, D/'pmod-alternating-paths', 'figure', {
        'model': 'Z~Bernoulli(1/2); X_n=Z; Y_n=Z for odd n, 1-Z for even n',
        'marginals': 'every X_n and Y_n ~ Bernoulli(1/2)', 'P(Y_1=Y_2)': 0, 'P(X_1=X_2)': 1,
        'vertical_offset_for_visibility': 0.04})


def pmod_mixed_expectation():
    """Point mass 0.4 at 0 plus 0.6*Exp(1): distribution function and E exp(-X)."""
    p0 = 0.4
    fig, axes = figure(width_mm=120, height_mm=52, ncols=2)
    ax = axes[0]
    x = np.linspace(0, 5, 500)
    ax.plot([-1, 0], [0, 0], color=BLUE)
    ax.plot(x, p0 + (1 - p0) * (1 - np.exp(-x)), color=BLUE)
    ax.plot([0], [0], 'o', mfc='white', mec=BLUE, ms=3.5)
    ax.plot([0], [p0], 'o', color=BLUE, ms=3.5)
    ax.annotate('', xy=(0.25, p0), xytext=(0.25, 0), arrowprops=dict(arrowstyle='<->', color=RED, lw=.7))
    ax.text(0.35, 0.2, r'$0.4$', color=RED, fontsize=7.5, va='center')
    ax.set(xlim=(-1, 5), ylim=(-0.03, 1.05))
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$F_X(x)$')
    ax.set_title('(a) 分布函数的跳跃')
    ax = axes[1]
    xs = np.linspace(0, 5, 500)
    ax.plot(xs, (1 - p0) * np.exp(-xs), color=BLUE, lw=.9, ls='--', label='连续部分密度')
    ax.fill_between(xs, np.exp(-xs) * (1 - p0) * np.exp(-xs), color=GREEN_FILL, lw=0)
    ax.plot(xs, np.exp(-xs) * (1 - p0) * np.exp(-xs), color=GREEN, lw=.9, label='被积贡献')
    ax.vlines(0, 0, p0, color=RED, lw=1.6)
    ax.plot([0], [p0], 'o', color=RED, ms=3.5, label='点质量贡献')
    ax.text(0.7, 0.13, r'$0.3$', color=GREEN, fontsize=7.5)
    ax.text(-0.1, 0.40, r'$0.4$', color=RED, fontsize=7.5, ha='right', va='center')
    ax.set(xlim=(-0.6, 5), ylim=(0, 0.65))
    ax.set_xlabel(r'$x$')
    ax.set_title('(b) 两部分贡献')
    ax.legend(loc='upper right', handlelength=1.6)
    save(fig, D/'pmod-mixed-expectation', 'figure', {
        'law': '0.4*delta_0 + 0.6*Exp(1)', 'g': 'exp(-x)', 'point_part': 0.4,
        'continuous_part': 0.6 * 0.5, 'E g(X)': 0.7, 'E X': 0.6, 'E X^2': 1.2})


def pmod_moment_tails():
    """Pareto tails P(X>t)=t**-alpha and truncated p-th moments."""
    alphas = [1.5, 2.5, 4.0]
    cols = [RED, YELLOW, BLUE]
    fig, axes = figure(width_mm=120, height_mm=52, ncols=2)
    ax = axes[0]
    t = np.logspace(0, 3, 300)
    for a, c in zip(alphas, cols):
        ax.loglog(t, t**-a, color=c, label=rf'$\alpha={a:g}$')
    ax.set(xlim=(1, 1e3), ylim=(1e-12, 1.5))
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$ℙ(X>t)$')
    ax.set_title('(a) 尾概率')
    ax.legend(loc='lower left', handlelength=1.6)
    ax = axes[1]
    T = np.logspace(0, 4, 300)
    facts = {}
    p = 2.0
    for a, c in zip(alphas, cols):
        # E[min(X,T)^p] = 1 + int_1^T p t^{p-1} t^{-a} dt
        if abs(a - p) < 1e-12:
            m = 1 + p * np.log(T)
        else:
            m = 1 + p * (T**(p - a) - 1) / (p - a)
        ax.semilogx(T, m, color=c, label=rf'$\alpha={a:g}$')
        facts[f'alpha={a}'] = {'E X^p (p<alpha)': {str(q): (a / (a - q) if q < a else 'infinite') for q in (1, 2, 3)},
                               'truncated_second_moment_at_T=1e4': float(m[-1])}
    ax.set(xlim=(1, 1e4), ylim=(0, 12))
    ax.set_xlabel(r'$T$')
    ax.set_ylabel(r'$m_2(T)$')
    ax.set_title('(b) 截断二阶矩')
    save(fig, D/'pmod-moment-tails', 'figure', {
        'law': 'Pareto: P(X>t)=t^{-alpha} for t>=1', 'alphas': alphas,
        'moment_formula': 'E X^p = alpha/(alpha-p) for p<alpha, infinite otherwise',
        'panel_b': 'E[min(X,T)^2] = 1 + 2 (T^{2-alpha}-1)/(2-alpha)', **facts})


def pmod_markov_bounds():
    """Pareto(alpha=3) tail versus moment bounds E X^p / t^p."""
    a = 3.0
    fig, ax = figure(width_mm=100, height_mm=52)
    t = np.logspace(0, 2, 300)
    ax.loglog(t, t**-a, color=INK, lw=1.3, label='真实尾概率')
    cols = [BLUE, GREEN, YELLOW]
    vals = {}
    for p, c in zip([1.0, 2.0, 2.5], cols):
        mp = a / (a - p)
        ax.loglog(t, np.minimum(1, mp / t**p), color=c, ls='--', label=rf'$p={p:g}$')
        vals[f'p={p}'] = {'E X^p': mp, 'bound_at_t=2': mp / 2**p, 'bound_at_t=10': mp / 10**p, 'bound_at_t=100': mp / 100**p}
    ax.set(xlim=(1, 100), ylim=(1e-6, 1.5))
    ax.set_xlabel(r'$t$')
    ax.set_ylabel('尾概率或上界')
    ax.legend(loc='lower left', handlelength=1.8)
    save(fig, D/'pmod-markov-bounds', 'figure', {
        'law': 'Pareto alpha=3: P(X>=t)=t^-3, t>=1', 'bounds': 'min(1, E X^p / t^p)',
        'true_at_t=2,10,100': [2**-a, 10**-a, 100**-a], **vals})


def pmod_jensen_support():
    """Three-point law, convex phi(x)=exp(x), and the support line at E X."""
    xs = np.array([-1.0, 0.5, 2.0])
    ps = np.array([0.3, 0.5, 0.2])
    m = float(xs @ ps)
    Ephi = float(np.exp(xs) @ ps)
    fig, ax = figure(width_mm=100, height_mm=56)
    x = np.linspace(-1.5, 2.4, 400)
    ax.plot(x, np.exp(x), color=BLUE, label=r'$\varphi(x)=e^x$')
    ax.plot(x, np.exp(m) + np.exp(m) * (x - m), color=GREEN, lw=.9, ls='--', label='支撑直线')
    ax.plot(xs, np.exp(xs), 'o', color=BLUE, ms=3.5)
    ax.plot(xs, np.exp(m) + np.exp(m) * (xs - m), 'o', mfc='white', mec=GREEN, ms=3.5)
    for xi in xs:
        ax.plot([xi, xi], [np.exp(m) + np.exp(m) * (xi - m), np.exp(xi)], color=MUTED, lw=.6, ls=':')
    ax.plot([m], [np.exp(m)], 's', color=RED, ms=3.5)
    ax.plot([m], [Ephi], 'D', color=YELLOW, ms=3.5)
    ax.plot([m, m], [np.exp(m), Ephi], color=RED, lw=.8)
    ax.text(m + 0.06, np.exp(m) - 0.35, r'$\varphi(\mu)$', color=RED, fontsize=7.5)
    ax.text(m + 0.06, Ephi + 0.15, r'$\mu_\varphi$', color=INK, fontsize=7.5)
    ax.set(xlim=(-1.5, 2.4), ylim=(-0.9, 8))
    ax.set_xlabel(r'$x$')
    ax.legend(loc='upper left', handlelength=1.8)
    save(fig, D/'pmod-jensen-support', 'figure', {
        'law': 'P(X=-1)=0.3, P(X=0.5)=0.5, P(X=2)=0.2', 'E X': m, 'phi(E X)': float(np.exp(m)),
        'E phi(X)': Ephi, 'support_line': 'e^m + e^m (x-m)'})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [
    pmod_almost_sure_limit, pmod_pushforward_exponential, pmod_reflection_uniform,
    pmod_alternating_paths, pmod_mixed_expectation, pmod_moment_tails,
    pmod_markov_bounds, pmod_jensen_support]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
