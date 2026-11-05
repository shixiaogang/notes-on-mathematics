# coding: utf-8
"""Teaching charts for volume three, part "optimization", chapter 9
(functional optimization).

Every curve comes from a closed-form expression or a deterministic computation
recorded in the saved facts file; no random numbers are used.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/01-optimization/matplotlib/generate_c9.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import (figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED,
                     GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL)

D = Path(__file__).resolve().parent


def perturbation_family():
    """u(x)=x^2, h(x)=sin(pi x), J(u)=1/2 int u'^2;  J(u+th)=2/3-4t/pi+pi^2 t^2/4."""
    x = np.linspace(0, 1, 401)
    fig, (a1, a2) = figure(width_mm=110, height_mm=46, ncols=2)
    ts = [-0.4, -0.2, 0.0, 0.2, 0.4]
    cols = [GRID, MUTED, BLUE, MUTED, GRID]
    for t, c in zip(ts, cols):
        a1.plot(x, x**2 + t*np.sin(np.pi*x), color=c, lw=1.1 if t == 0 else .8)
    a1.text(0.36, 0.74, r'$t=0.4$', fontsize=7.5, color=MUTED)
    a1.text(0.42, -0.29, r'$t=-0.4$', fontsize=7.5, color=MUTED)
    a1.text(0.73, 0.4, r'$u$', fontsize=8, color=BLUE)
    a1.plot([0, 1], [0, 1], 'o', color=INK, ms=2.5)
    a1.set(xlim=(0, 1), ylim=(-0.3, 1.1), xlabel=r'$x$', title=r'(a) $u+th$')
    t = np.linspace(-0.6, 1.4, 401)
    J = 2/3 - 4*t/np.pi + np.pi**2*t**2/4
    a2.plot(t, J, color=BLUE)
    slope = -4/np.pi
    tt = np.linspace(-0.45, 0.45, 2)
    a2.plot(tt, 2/3 + slope*tt, color=YELLOW, lw=1.0, ls='--')
    a2.plot([0], [2/3], 'o', color=INK, ms=3)
    tmin = 8/np.pi**3
    a2.plot([tmin], [2/3 - 16/np.pi**4], 'o', color=GREEN, ms=3)
    a2.text(0.08, 1.0, r"$\varphi'(0)=-4/\pi$", fontsize=7.5, color=YELLOW)
    a2.set(xlim=(-0.6, 1.4), ylim=(0.2, 1.6), xlabel=r'$t$', title=r'(b) $\varphi(t)=J(u+th)$')
    save(fig, D/'c9-perturbation-family', 'figure', {
        'u': 'x^2', 'h': 'sin(pi x)', 'J': '1/2 int_0^1 u\'(x)^2 dx',
        'phi(t)': '2/3 - 4 t/pi + pi^2 t^2/4', 'phi_prime_0': slope,
        'curves_t': ts, 'phi_min_t': tmin, 'phi_min': 2/3 - 16/np.pi**4})


def nonlinear_directional():
    """J(a,b)=a^3/(a^2+b^2): directional derivative at 0 is cos^3(theta) on unit directions."""
    fig, (a1, a2) = figure(width_mm=110, height_mm=50, ncols=2)
    g = np.linspace(-1, 1, 301)
    A, B = np.meshgrid(g, g)
    with np.errstate(invalid='ignore', divide='ignore'):
        J = np.where(A**2 + B**2 > 0, A**3/(A**2 + B**2), 0.0)
    lev = np.linspace(-0.9, 0.9, 13)
    a1.contourf(A, B, J, levels=lev, cmap=_cmap(), extend='both')
    a1.contour(A, B, J, levels=lev, colors=[MUTED], linewidths=.3)
    for th in np.deg2rad([0, 45, 90]):
        a1.annotate('', xy=(0.85*np.cos(th), 0.85*np.sin(th)), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=INK, lw=.8))
    a1.text(0.88, -0.08, r'$(1,0)$', fontsize=7.5, ha='right', va='top')
    a1.text(0.62, 0.68, r'$(1,1)$', fontsize=7.5)
    a1.text(0.04, 0.9, r'$(0,1)$', fontsize=7.5)
    a1.set(xlim=(-1, 1), ylim=(-1, 1), xlabel=r'$a$', ylabel=r'$b$', aspect='equal',
           title='(a) 等值线')
    th = np.linspace(0, 2*np.pi, 400)
    a2.plot(th, np.cos(th)**3, color=BLUE, label=r'$\cos^3\theta$')
    a2.plot(th, np.cos(th), color=YELLOW, ls='--', lw=1.0, label=r'$\cos\theta$')
    a2.axhline(0, color=GRID, lw=.6)
    for v in [0, np.pi/4, np.pi/2]:
        a2.plot([v], [np.cos(v)**3], 'o', color=INK, ms=2.5)
    a2.text(np.pi/4 + 0.12, 0.38, r'$1/(2\sqrt{2})$', fontsize=7.5)
    a2.set(xlim=(0, 2*np.pi), ylim=(-1.15, 1.15), xlabel=r'$\theta$',
           title='(b) 单位方向上的导数')
    a2.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    a2.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    a2.legend(loc='lower left', handlelength=1.6)
    save(fig, D/'c9-nonlinear-directional', 'figure', {
        'J': 'a^3/(a^2+b^2), J(0,0)=0',
        'directional_derivative': 'h1^3/(h1^2+h2^2); on unit circle cos^3(theta)',
        'values': {'(1,0)': 1, '(0,1)': 0, '(1,1)': 0.5,
                   'unit (1,1)/sqrt2': 1/(2*np.sqrt(2))}})


def _cmap():
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list('c9div', [BLUE, BLUE_FILL, '#FFFFFF', YELLOW_FILL, YELLOW])


def gateaux_not_frechet():
    """f(a,b)=a^3 b/(a^4+b^2): zero directional derivatives, f(a,a^2)=a/2."""
    fig, (a1, a2) = figure(width_mm=110, height_mm=50, ncols=2)
    g = np.linspace(-1, 1, 401)
    A, B = np.meshgrid(g, g)
    with np.errstate(invalid='ignore', divide='ignore'):
        F = np.where(A**4 + B**2 > 0, A**3*B/(A**4 + B**2), 0.0)
    lev = np.linspace(-0.5, 0.5, 11)
    a1.contourf(A, B, F, levels=lev, cmap=_cmap(), extend='both')
    a1.contour(A, B, F, levels=lev, colors=[MUTED], linewidths=.3)
    s = np.linspace(-1, 1, 200)
    a1.plot(s, s**2, color=RED, lw=1.1)
    for th in np.deg2rad([20, 60]):
        a1.plot([0, np.cos(th)], [0, np.sin(th)], color=INK, lw=.8)
    a1.text(-0.62, 0.06, r'$b=a^2$', fontsize=7.5, color=RED)
    a1.set(xlim=(-1, 1), ylim=(-1, 1), xlabel=r'$a$', ylabel=r'$b$', aspect='equal',
           title='(a) 等值线')
    r = np.logspace(-3, 0, 200)
    for deg, c, ls in [(20, BLUE, '-'), (60, GREEN, '-')]:
        th = np.deg2rad(deg)
        a, b = r*np.cos(th), r*np.sin(th)
        a2.plot(r, a**3*b/(a**4 + b**2)/r, color=c, ls=ls, label=f'射线 {deg}°')
    aa = np.logspace(-3, 0, 200)
    nr = np.sqrt(aa**2 + aa**4)
    a2.plot(nr, (aa/2)/nr, color=RED, label=r'$b=a^2$')
    a2.axhline(0.5, color=GRID, lw=.6)
    a2.set_xscale('log')
    a2.set(xlim=(1e-3, 1), ylim=(-0.03, 0.6), xlabel=r'$\Vert(a,b)\Vert_2$',
           title=r'(b) $f(a,b)/\Vert(a,b)\Vert_2$')
    a2.legend(loc='center left', handlelength=1.6)
    save(fig, D/'c9-gateaux-not-frechet', 'figure', {
        'f': 'a^3 b/(a^4+b^2), f(0,0)=0', 'directional_derivatives_at_0': 0,
        'along_parabola': 'f(a,a^2)=a/2, ratio -> 1/2', 'rays_deg': [20, 60]})


def l2_h1_gradient():
    """Same differential, L2 vs H^1_0 representer: coefficient k divided by (1+k^2 pi^2)."""
    x = np.linspace(0, 1, 801)
    r = np.sin(np.pi*x) + 0.5*np.sin(15*np.pi*x)
    w = np.sin(np.pi*x)/(1 + np.pi**2) + 0.5*np.sin(15*np.pi*x)/(1 + 225*np.pi**2)
    fig, (a1, a2) = figure(width_mm=110, height_mm=44, ncols=2)
    a1.plot(x, r, color=BLUE)
    a1.set(xlim=(0, 1), ylim=(-0.6, 1.6), xlabel=r'$x$', title='(a) L² 内积下的梯度')
    a2.plot(x, w, color=GREEN)
    a2.set(xlim=(0, 1), ylim=(-0.6/(1+np.pi**2), 1.6/(1+np.pi**2)), xlabel=r'$x$',
           title='(b) H¹ 内积下的梯度')
    a2.ticklabel_format(axis='y', style='plain')
    save(fig, D/'c9-l2-h1-gradient', 'figure', {
        'r': 'sin(pi x)+0.5 sin(15 pi x)',
        'w': 'sin(pi x)/(1+pi^2)+0.5 sin(15 pi x)/(1+225 pi^2)',
        'H1_inner_product': 'int (w h + w\' h\') dx on H_0^1(0,1)',
        'damping_k1': 1/(1+np.pi**2), 'damping_k15': 1/(1+225*np.pi**2),
        'relative_high_freq_amplitude_r': 0.5,
        'relative_high_freq_amplitude_w': 0.5*(1+np.pi**2)/(1+225*np.pi**2)})


def positivity_vi():
    """Project g=sin(2 pi x) onto {u>=0} in L2: u*=max(g,0), gradient u*-g=max(-g,0)."""
    x = np.linspace(0, 1, 801)
    g = np.sin(2*np.pi*x)
    u = np.maximum(g, 0)
    fig, ax = figure(width_mm=96, height_mm=46)
    ax.axhline(0, color=GRID, lw=.6)
    ax.fill_between(x, 0, np.maximum(-g, 0), color=YELLOW_FILL, lw=0)
    ax.plot(x, g, color=MUTED, ls='--', lw=.9, label=r'$g$')
    ax.plot(x, u, color=BLUE, label=r'$u^*=\max(g,0)$')
    ax.plot(x, np.maximum(-g, 0), color=YELLOW, lw=1.0, label=r'$\nabla J(u^*)=u^*-g$')
    ax.set(xlim=(0, 1), ylim=(-1.15, 1.15), xlabel=r'$x$')
    ax.legend(loc='lower left', handlelength=1.6)
    save(fig, D/'c9-positivity-vi', 'figure', {
        'g': 'sin(2 pi x)', 'C': '{u in L2(0,1): u>=0 a.e.}',
        'J': '1/2 int (u-g)^2', 'u_star': 'max(g,0)', 'gradient': 'max(-g,0)',
        'J_u_star': 0.125, 'gradient_norm_sq': 0.25})


def no_uniform_curvature():
    """Slices t -> t^2/k - t^4 of J(x)=sum x_k^2/k - sum x_k^4 along e_k."""
    t = np.linspace(0, 1.1, 400)
    fig, ax = figure(width_mm=90, height_mm=48)
    ax.axhline(0, color=GRID, lw=.6)
    for k, c in [(1, BLUE), (4, GREEN), (16, YELLOW), (64, RED)]:
        ax.plot(t, t**2/k - t**4, color=c, label=f'$k={k}$')
        ax.plot([1/np.sqrt(k)], [0], 'o', color=c, ms=2.6)
    ax.set(xlim=(0, 1.1), ylim=(-0.12, 0.27), xlabel=r'$t$', ylabel=r'$J(te_k)$')
    ax.legend(loc='upper left', ncols=2, handlelength=1.4)
    save(fig, D/'c9-no-uniform-curvature', 'figure', {
        'J': 'sum_k x_k^2/k - sum_k x_k^4 on l2', 'slice': 't^2/k - t^4',
        'zero_crossings': {str(k): 1/np.sqrt(k) for k in (1, 4, 16, 64)},
        'second_derivative_at_0_along_ek': '2/k'})


def smoothed_abs():
    """psi_eps(p)=sqrt(p^2+eps^2) and derivative p/sqrt(p^2+eps^2)."""
    p = np.linspace(-1.5, 1.5, 601)
    fig, (a1, a2) = figure(width_mm=110, height_mm=44, ncols=2)
    for e, c, ls in [(0, INK, '--'), (0.1, BLUE, '-'), (0.5, GREEN, '-'), (1.0, YELLOW, '-')]:
        lab = r'$\varepsilon=%g$' % e
        a1.plot(p, np.sqrt(p**2 + e**2), color=c, ls=ls, lw=.9 if e == 0 else 1.1, label=lab)
        if e > 0:
            a2.plot(p, p/np.sqrt(p**2 + e**2), color=c, label=lab)
        else:
            a2.plot(p[p < 0], -np.ones((p < 0).sum()), color=c, ls=ls, lw=.9)
            a2.plot(p[p > 0], np.ones((p > 0).sum()), color=c, ls=ls, lw=.9)
            a2.plot([0, 0], [-1, 1], color=c, ls=':', lw=.9)
    a1.set(xlim=(-1.5, 1.5), ylim=(0, 1.9), xlabel=r'$p$', title=r'(a) $\psi_\varepsilon(p)$')
    a1.legend(loc='upper center', ncols=2, handlelength=1.4, fontsize=7)
    a2.set(xlim=(-1.5, 1.5), ylim=(-1.15, 1.15), xlabel=r'$p$', title=r"(b) $\psi_\varepsilon'(p)$")
    save(fig, D/'c9-smoothed-abs', 'figure', {
        'psi_eps': 'sqrt(p^2+eps^2)', 'derivative': 'p/sqrt(p^2+eps^2)',
        'eps': [0, 0.1, 0.5, 1.0], 'max_slope_of_derivative': '1/eps at p=0',
        'eps0_subdifferential_at_0': '[-1,1]'})


def _quad(f, n=None):
    from scipy.integrate import quad
    return float(quad(lambda s: float(f(np.array(s))), 0, 1, limit=200)[0])


def fixed_endpoint_candidates():
    """Candidates with u(0)=0,u(1)=1: Dirichlet energy 1/2 int u'^2 and length int sqrt(1+u'^2)."""
    x = np.linspace(0, 1, 401)
    cands = [
        ('$x$', lambda s: s, lambda s: np.ones_like(s), BLUE, '-'),
        ('$x^2$', lambda s: s**2, lambda s: 2*s, GREEN, '-'),
        (r'$x+0.15\sin 2\pi x$', lambda s: s + .15*np.sin(2*np.pi*s),
         lambda s: 1 + .3*np.pi*np.cos(2*np.pi*s), YELLOW, '-'),
        (r'$\sqrt{x}$', lambda s: np.sqrt(s), lambda s: .5/np.sqrt(s), RED, '-'),
    ]
    fig, ax = figure(width_mm=100, height_mm=52)
    facts = {}
    for name, u, du, c, ls in cands:
        E = 0.5*_quad(lambda s: du(s)**2) if name != r'$\sqrt{x}$' else float('inf')
        Lg = _quad(lambda s: np.sqrt(1 + du(s)**2), 200000)
        Es = r'\infty' if np.isinf(E) else f'{E:.3f}'
        ax.plot(x, u(x), color=c, ls=ls, label=f'{name}: $J={Es}$, $\\ell={Lg:.3f}$')
        facts[name] = {'dirichlet_energy': None if np.isinf(E) else round(E, 4), 'length': round(Lg, 4)}
    ax.plot([0, 1], [0, 1], 'o', color=INK, ms=2.6)
    ax.set(xlim=(0, 1), ylim=(-0.05, 1.12), xlabel=r'$x$', ylabel=r'$u(x)$')
    ax.legend(loc='upper left', handlelength=1.4, fontsize=7)
    facts['exact'] = {'x': {'J': 0.5, 'length': np.sqrt(2)}, 'x^2': {'J': 2/3},
                      'x+0.15 sin 2pi x': {'J': 0.5 + 0.25*(0.3*np.pi)**2}}
    save(fig, D/'c9-fixed-endpoint-candidates', 'figure', facts)


def boundary_conditions():
    """J(u)=int_0^1 (u'^2/2 - u) dx; fixed: u=x(1-x)/2; free right end: u=x-x^2/2."""
    x = np.linspace(0, 1, 401)
    fig, ax = figure(width_mm=96, height_mm=48)
    ax.plot(x, x*(1 - x)/2, color=BLUE, label='两端固定')
    ax.plot(x, x - x**2/2, color=GREEN, label='右端自由')
    ax.plot([1, 1], [0, 0.5], color=GRID, lw=.6)
    ax.plot([0.82, 1.0], [0.5, 0.5], color=GREEN, ls='--', lw=.8)
    ax.text(0.83, 0.44, r"$u'(1)=0$", fontsize=7.5, color=GREEN)
    ax.plot([0, 1], [0, 0], 'o', color=BLUE, ms=2.6)
    ax.set(xlim=(0, 1.05), ylim=(-0.03, 0.62), xlabel=r'$x$', ylabel=r'$u(x)$')
    ax.legend(loc='upper left', handlelength=1.4)
    save(fig, D/'c9-boundary-conditions', 'figure', {
        'J': 'int_0^1 (u\'^2/2 - u) dx', 'fixed': 'x(1-x)/2, J=-1/24',
        'free_right': 'x - x^2/2, J=-1/6', 'euler_lagrange': '-u\'\'=1'})


def bolza_sawtooth():
    """Sawtooth u_n: slopes +-1, n teeth, J(u)=int ((u'^2-1)^2+u^2) = 1/(12 n^2)."""
    x = np.linspace(0, 1, 4001)
    fig, (a1, a2) = figure(width_mm=110, height_mm=44, ncols=2)
    for n, c in [(2, BLUE), (4, GREEN), (8, YELLOW)]:
        s = (x*n) % 1.0
        u = np.minimum(s, 1 - s)/n
        a1.plot(x, u, color=c, label=f'$n={n}$')
    a1.set(xlim=(0, 1), ylim=(0, 0.34), xlabel=r'$x$', title=r'(a) $u_n$')
    a1.legend(loc='upper right', ncols=3, handlelength=1.2, columnspacing=.8)
    n = 4
    s = (x*n) % 1.0
    du = np.where(s < 0.5, 1.0, -1.0)
    a2.plot(x, du, color=GREEN, lw=.9, drawstyle='steps-post')
    a2.axhline(0, color=GRID, lw=.6)
    a2.set(xlim=(0, 1), ylim=(-1.3, 1.3), xlabel=r'$x$', title=r"(b) $u_4'=\pm1$")
    save(fig, D/'c9-bolza-sawtooth', 'figure', {
        'J': 'int_0^1 ((u\'^2-1)^2 + u^2) dx on W_0^{1,4}(0,1)',
        'u_n': 'distance to nearest multiple of 1/n, amplitude 1/(2n)',
        'J_u_n': {str(k): 1/(12*k**2) for k in (2, 4, 8)}, 'J_0': 1})


def transition_width():
    """u_delta: linear rise over width delta centred at 1/2; int|u'|=1, int u'^2=1/delta."""
    x = np.linspace(0, 1, 2001)
    fig, (a1, a2) = figure(width_mm=110, height_mm=44, ncols=2)
    for d, c in [(0.5, BLUE), (0.2, GREEN), (0.05, YELLOW)]:
        u = np.clip((x - 0.5 + d/2)/d, 0, 1)
        a1.plot(x, u, color=c, label=r'$\delta=%g$' % d)
    a1.set(xlim=(0, 1), ylim=(-0.05, 1.1), xlabel=r'$x$', title=r'(a) $u_\delta$')
    a1.legend(loc='upper left', handlelength=1.2)
    d = np.logspace(-2, 0, 100)
    a2.plot(d, np.ones_like(d), color=BLUE, label=r"$\int|u_\delta'|$")
    a2.plot(d, 1/d, color=YELLOW, label=r"$\int|u_\delta'|^2$")
    a2.set_xscale('log'); a2.set_yscale('log')
    a2.set(xlim=(1e-2, 1), ylim=(0.5, 150), xlabel=r'$\delta$', title='(b) 两种导数积分')
    a2.legend(loc='upper right', handlelength=1.4)
    save(fig, D/'c9-transition-width', 'figure', {
        'u_delta': 'clip((x-1/2+delta/2)/delta,0,1) on [0,1], u(0)=0,u(1)=1',
        'int_abs_derivative': 1, 'int_sq_derivative': '1/delta', 'deltas': [0.5, 0.2, 0.05]})


def _ritz(N):
    """Linear hats on uniform mesh for min int (u'^2/2 - f u), f=pi^2 sin(pi x), u(0)=u(1)=0."""
    h = 1.0/N
    nodes = np.linspace(0, 1, N + 1)
    K = (np.diag(2*np.ones(N - 1)) - np.diag(np.ones(N - 2), 1) - np.diag(np.ones(N - 2), -1))/h
    # exact load b_j = int f phi_j = pi^2 * int sin(pi x) phi_j = sin(pi x_j) * 2(1-cos(pi h))/h
    b = np.sin(np.pi*nodes[1:-1])*2*(1 - np.cos(np.pi*h))/h
    a = np.linalg.solve(K, b)
    return nodes, np.concatenate([[0], a, [0]])


def _ritz_errors(N, m=200):
    nodes, a = _ritz(N)
    h = 1.0/N
    eL2, eH1 = 0.0, 0.0
    gx, gw = np.polynomial.legendre.leggauss(6)
    for i in range(N):
        xs = nodes[i] + (gx + 1)/2*h
        w = gw*h/2
        uh = a[i] + (a[i+1] - a[i])*(xs - nodes[i])/h
        duh = (a[i+1] - a[i])/h
        eL2 += np.sum(w*(np.sin(np.pi*xs) - uh)**2)
        eH1 += np.sum(w*(np.pi*np.cos(np.pi*xs) - duh)**2)
    return np.sqrt(eL2), np.sqrt(eH1)


def ritz_hat():
    x = np.linspace(0, 1, 401)
    fig, (a1, a2) = figure(width_mm=110, height_mm=48, ncols=2)
    N = 4
    nodes = np.linspace(0, 1, N + 1)
    for j in range(1, N):
        phi = np.maximum(0, 1 - np.abs(x - nodes[j])*N)
        a1.plot(x, 0.25*phi, color=GRID, lw=.8)
    a1.plot(x, np.sin(np.pi*x), color=INK, lw=.9, ls='--', label=r'$\sin\pi x$')
    for N, c in [(4, YELLOW), (8, BLUE)]:
        nd, a = _ritz(N)
        a1.plot(nd, a, color=c, marker='o', ms=2.2, label=f'$N={N}$')
    a1.text(0.5, 0.28, r'$0.25\varphi_j$', fontsize=7.5, color=MUTED, ha='center')
    a1.set(xlim=(0, 1), ylim=(0, 1.15), xlabel=r'$x$', title='(a) 帽函数与 Ritz 近似')
    a1.legend(loc='upper right', handlelength=1.4, fontsize=7)
    Ns = np.array([4, 8, 16, 32, 64, 128])
    errs = np.array([_ritz_errors(n) for n in Ns])
    a2.loglog(1/Ns, errs[:, 1], 'o-', color=BLUE, ms=2.6, label=r"$\Vert(u-u_N)'\Vert_{L^2}$")
    a2.loglog(1/Ns, errs[:, 0], 's-', color=GREEN, ms=2.6, label=r'$\Vert u-u_N\Vert_{L^2}$')
    a2.set(xlabel='网格宽度 1/N', title='(b) 误差随网格加密')
    a2.legend(loc='lower right', handlelength=1.4, fontsize=7)
    rates = np.log(errs[:-1]/errs[1:])/np.log(2)
    save(fig, D/'c9-ritz-hat', 'figure', {
        'problem': 'min int_0^1 (u\'^2/2 - f u), f=pi^2 sin(pi x), u(0)=u(1)=0, exact u=sin(pi x)',
        'trial_space': 'piecewise-linear hats on uniform mesh, N cells',
        'load': 'exact: b_j = sin(pi x_j) 2(1-cos(pi h))/h',
        'N': Ns.tolist(), 'L2_error': errs[:, 0].round(6).tolist(),
        'H1_semi_error': errs[:, 1].round(6).tolist(),
        'observed_rate_L2': rates[:, 0].round(3).tolist(),
        'observed_rate_H1semi': rates[:, 1].round(3).tolist(),
        'quadrature': '6-point Gauss-Legendre per cell'})


def energy_consistency():
    """E_N(sin pi x) = N^2 sin^2(pi/(2N)) -> pi^2/4."""
    Ns = np.array([2, 4, 8, 16, 32, 64, 128])
    E = Ns**2*np.sin(np.pi/(2*Ns))**2
    err = np.pi**2/4 - E
    fig, (a1, a2) = figure(width_mm=110, height_mm=44, ncols=2)
    a1.plot(Ns, E, 'o-', color=BLUE, ms=2.6)
    a1.axhline(np.pi**2/4, color=YELLOW, ls='--', lw=.9)
    a1.text(40, np.pi**2/4 - 0.12, r'$\pi^2/4$', fontsize=7.5, color=YELLOW)
    a1.set_xscale('log', base=2)
    a1.set(xlabel=r'$N$', title=r'(a) $E_N(u)$', ylim=(1.9, 2.55))
    a2.loglog(Ns, err, 'o-', color=BLUE, ms=2.6, label=r'$\pi^2/4-E_N$')
    a2.loglog(Ns, np.pi**4/(48*Ns**2), color=MUTED, ls='--', lw=.8, label=r'$\pi^4/(48N^2)$')
    a2.set_xscale('log', base=2)
    a2.set(xlabel=r'$N$', title='(b) 能量值误差')
    a2.legend(loc='upper right', handlelength=1.4)
    save(fig, D/'c9-energy-consistency', 'figure', {
        'u': 'sin(pi x)', 'E_N': 'sum_i (u(x_{i+1})-u(x_i))^2/(2 dx) = N^2 sin^2(pi/(2N))',
        'limit': np.pi**2/4, 'N': Ns.tolist(), 'E_N_values': E.round(6).tolist(),
        'errors': err.round(6).tolist()})


ALL = {f.__name__: f for f in [perturbation_family, nonlinear_directional, gateaux_not_frechet,
                               l2_h1_gradient, positivity_vi, no_uniform_curvature, smoothed_abs,
                               fixed_endpoint_candidates, boundary_conditions, bolza_sawtooth,
                               transition_width, ritz_hat, energy_consistency]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(ALL)
    for n in names:
        ALL[n.replace('-', '_')]()
        print('drew', n)
