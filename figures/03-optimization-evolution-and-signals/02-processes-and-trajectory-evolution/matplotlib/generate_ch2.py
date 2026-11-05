# coding: utf-8
"""Teaching charts for volume three, part "processes and trajectory evolution",
chapter 2 (ordinary differential equations).

Exact curves come from closed-form solutions recorded in each facts file;
reference trajectories for nonlinear equations use scipy's solve_ivp with
rtol=atol=1e-11.  No random numbers are used.
Run from any directory:
  python figures/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/matplotlib/generate_ch2.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib.patches import Polygon, Rectangle
from matplotlib.lines import Line2D

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import (figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, STROKE,
                     BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL)

D = Path(__file__).resolve().parent
TOL = dict(rtol=1e-11, atol=1e-11)


def r(v, k=4):
    return float(np.round(v, k))


def ref_solve(f, t_span, y0, t_eval=None):
    sol = solve_ivp(f, t_span, y0, method='DOP853', t_eval=t_eval, **TOL)
    return sol.t, sol.y


def arrow_on(ax, x, y, i, color, size=7):
    ax.annotate('', xy=(x[i+1], y[i+1]), xytext=(x[i], y[i]),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=size))


# ---------------------------------------------------------------- 2.1
def ode_slope_field():
    """(a) slope field of x'=-0.2x+0.4 with solutions; (b) damped pendulum field."""
    fig, axes = figure(width_mm=150, height_mm=58, ncols=2)
    lam, u = 0.2, 0.4
    ax = axes[0]
    T, X = np.meshgrid(np.linspace(0, 20, 17), np.linspace(-0.5, 4.0, 13))
    S = -lam*X + u
    L = np.sqrt(1 + (S*20/4.5*0.55)**2)
    ax.quiver(T, X, 1/L, S/L, angles='xy', color=MUTED, width=0.0028, headwidth=0, headlength=0,
              headaxislength=0, pivot='middle', scale=28)
    t = np.linspace(0, 20, 300)
    for x0, col in [(0, BLUE), (1, BLUE), (3.5, GREEN), (-0.4, BLUE)]:
        ax.plot(t, 2 + (x0-2)*np.exp(-lam*t), color=col, lw=1.1)
        ax.plot([0], [x0], 'o', color=col, ms=2.6)
    ax.axhline(2, color=YELLOW, lw=0.8, ls='--')
    ax.text(19.6, 2.08, r'$x=u/\lambda=2$', ha='right', va='bottom', fontsize=7.5, color=INK)
    ax.set(xlim=(0, 20), ylim=(-0.5, 4.0), xlabel=r'$t$', ylabel=r'$x$')
    ax.set_title('(a) 温度模型的斜率场与解曲线')
    ax = axes[1]
    c = 0.3
    Q, P = np.meshgrid(np.linspace(-3.6, 3.6, 25), np.linspace(-2.6, 2.6, 19))
    U, V = P, -np.sin(Q) - c*P
    N = np.hypot(U, V) + 1e-12
    ax.quiver(Q, P, U/N, V/N, color=MUTED, width=0.0028, scale=40, headwidth=3.5, headlength=4, headaxislength=3.5)
    facts_traj = []
    for z0, col in [((-2.8, 0.0), BLUE), ((0.0, 2.4), GREEN), ((1.0, -1.0), BLUE)]:
        ts, ys = ref_solve(lambda t, z: [z[1], -np.sin(z[0]) - c*z[1]], (0, 25), z0,
                           t_eval=np.linspace(0, 25, 2000))
        ax.plot(ys[0], ys[1], color=col, lw=1.1)
        ax.plot([z0[0]], [z0[1]], 'o', color=col, ms=2.6)
        arrow_on(ax, ys[0], ys[1], 40, col)
        facts_traj.append({'z0': z0, 'z(25)': [r(ys[0, -1]), r(ys[1, -1])]})
    ax.set(xlim=(-3.6, 3.6), ylim=(-2.6, 2.6), xlabel=r'$q$', ylabel=r'$p$')
    ax.set_title('(b) 阻尼摆的向量场与轨迹')
    save(fig, D/'ode-slope-field', 'figure', {
        'panel_a': 'x(t)=2+(x0-2)exp(-0.2t), x0 in {-0.4,0,1,3.5}',
        'panel_b': {'damping': c, 'trajectories': facts_traj}})


# ---------------------------------------------------------------- 2.2
def ode_picard():
    """(a) Picard box for x'=1+x^2, x(0)=0, a=1,b=1; (b) Picard iterates for x'=x."""
    fig, axes = figure(width_mm=150, height_mm=56, ncols=2)
    ax = axes[0]
    a, b, M = 1.0, 1.0, 2.0
    h = min(a, b/M)
    ax.add_patch(Rectangle((-a, -b), 2*a, 2*b, fc=BLUE_FILL, ec=BLUE, lw=0.75))
    ax.add_patch(Polygon([[-h, M*h], [0, 0], [h, M*h], [h, -M*h], [0, 0], [-h, -M*h]], closed=False,
                         fc=GREEN_FILL, ec='none'))
    tt = np.linspace(-1.15, 1.15, 10)
    ax.plot(tt, M*tt, color=GREEN, lw=0.6, ls='--')
    ax.plot(tt, -M*tt, color=GREEN, lw=0.6, ls='--')
    t = np.linspace(-1.4, 1.4, 600)
    ax.plot(t, np.tan(t), color=MUTED, lw=0.8)
    tin = np.linspace(-h, h, 200)
    ax.plot(tin, np.tan(tin), color=RED, lw=1.3)
    for x in (-h, h):
        ax.axvline(x, color=GREEN, lw=0.6)
    ax.text(0.95, -0.95, r'$D$', ha='right', va='bottom', fontsize=8, color=BLUE)
    ax.text(h, -2.5, r'$h$', fontsize=7.5, color=INK, ha='left', va='bottom')
    ax.text(-h, -2.5, r'$-h$', fontsize=7.5, color=INK, ha='right', va='bottom')
    ax.text(0.0, 2.3, r'$|x|\leq M|t|$', fontsize=7.5, color=GREEN, ha='center', va='center')
    ax.text(1.14, 1.2, r'$\tan t$', fontsize=7.5, color=MUTED, ha='left')
    ax.set(xlim=(-1.4, 1.4), ylim=(-2.6, 2.6), xlabel=r'$t$', ylabel=r'$x$')
    ax.set_title('(a) 解在短区间内留在盒中')
    ax = axes[1]
    t = np.linspace(0, 2, 300)
    cols = [MUTED, YELLOW, GREEN, PURPLE, BLUE]
    poly = np.ones_like(t)
    term = np.ones_like(t)
    vals = {}
    ax.plot(t, np.exp(t), color=INK, lw=1.6, label=r'$e^t$')
    for k in range(5):
        if k > 0:
            term = term*t/k
            poly = poly + term
        ax.plot(t, poly, color=cols[k], lw=1.0, ls='--' if k < 4 else '-', label=rf'$x^{{({k})}}$')
        vals[f'x^({k})(2)'] = r(poly[-1])
    vals['e^2'] = r(np.e**2)
    ax.set(xlim=(0, 2), ylim=(0, 7.6), xlabel=r'$t$', ylabel=r'$x$')
    ax.set_title('(b) Picard迭代逐次逼近')
    ax.legend(loc='upper left', handlelength=1.6, ncols=2)
    save(fig, D/'ode-picard', 'figure', {'panel_a': {'f': '1+x^2', 'a': a, 'b': b, 'M': M, 'h': h,
                                                     'tan(0.5)': r(np.tan(0.5))}, 'panel_b': vals})


def ode_nonunique():
    """x'=sqrt|x|, x(0)=0: waiting solutions."""
    fig, ax = figure(width_mm=100, height_mm=52)
    t = np.linspace(0, 4, 400)
    ax.plot(t, np.zeros_like(t), color=INK, lw=1.4, label=r'$x\equiv0$')
    for c, col in [(0, BLUE), (1, GREEN), (2, YELLOW), (3, RED)]:
        x = np.where(t > c, (t-c)**2/4, 0.0)
        ax.plot(t[t >= c], x[t >= c], color=col, lw=1.1, label=rf'$c={c}$')
        ax.plot([c], [0], 'o', color=col, ms=2.8)
    ax.set(xlim=(0, 4), ylim=(-0.15, 4.2), xlabel=r'$t$', ylabel=r'$x$')
    ax.legend(loc='upper left', handlelength=1.5)
    save(fig, D/'ode-nonunique', 'figure', {'family': 'x_c(t)=0 (t<=c), (t-c)^2/4 (t>c)', 'c': [0, 1, 2, 3]})


def ode_blowup():
    """x'=x^2 versus x'=x from several initial values."""
    fig, axes = figure(width_mm=150, height_mm=54, ncols=2)
    ax = axes[0]
    for x0, col in [(0.5, BLUE), (1.0, GREEN), (2.0, RED)]:
        tb = 1/x0
        t = np.linspace(0, tb*0.995, 600)
        ax.plot(t, x0/(1-x0*t), color=col, lw=1.1, label=rf'$x_0={x0:g},\ t^\ast={tb:g}$')
        ax.axvline(tb, color=col, lw=0.6, ls=':')
    t = np.linspace(0, 2.2, 300)
    ax.plot(t, np.exp(t), color=MUTED, lw=1.0, ls='--', label=r'$\dot x=x,\ x_0=1$')
    ax.set(xlim=(0, 2.2), ylim=(0, 10), xlabel=r'$t$', ylabel=r'$x$')
    ax.set_title('(a) 有限时间爆炸')
    ax.legend(loc='upper left', bbox_to_anchor=(0.44, 1.0), handlelength=1.5)
    ax = axes[1]
    k = np.arange(0, 8)
    t_sq = 1/(2*2.0**k)
    ax.bar(k-0.18, t_sq, width=0.34, color=RED_FILL, ec=RED, lw=0.6, label=r'$\dot x=x^2$')
    ax.bar(k+0.18, np.full_like(t_sq, np.log(2)), width=0.34, color=BLUE_FILL, ec=BLUE, lw=0.6,
           label=r'$\dot x=x$')
    ax.set(xlim=(-0.6, 7.6), ylim=(0, 0.9), xlabel=r'$k$', ylabel='翻倍所需时间')
    ax.set_xticks(k)
    ax.set_title('(b) 第k次翻倍所需时间')
    ax.legend(loc='upper right', handlelength=1.2)
    save(fig, D/'ode-blowup', 'figure', {'x^2 solution': 'x0/(1-x0 t)', 'x0': [0.5, 1, 2],
                                         'doubling_times_x2': [r(v, 5) for v in t_sq],
                                         'sum_doubling_times_x2_from_1': 1.0, 'doubling_time_x': r(np.log(2))})


def ode_trajectory_tube():
    """Pendulum q'=p, p'=-sin q: bundle from a small disk and the Gronwall envelope."""
    fig, axes = figure(width_mm=150, height_mm=56, ncols=2)
    f = lambda t, z: [z[1], -np.sin(z[0])]
    delta = 0.05
    T = 8.0
    te = np.linspace(0, T, 801)
    facts = {'L': 1.0, 'delta': delta, 'T': T}
    ax = axes[0]
    qq = np.linspace(-3.4, 3.4, 400)
    for E in [0.5, 1.0, 1.5, 2.0, 2.6]:
        pp2 = 2*(E - (1 - np.cos(qq)))
        m = pp2 >= 0
        ax.plot(qq[m], np.sqrt(pp2[m]), color=GRID, lw=0.6)
        ax.plot(qq[m], -np.sqrt(pp2[m]), color=GRID, lw=0.6)
    out = {}
    for center, col, name in [((0.0, 1.2), BLUE, 'far'), ((0.0, 1.9), RED, 'near_separatrix')]:
        ang = np.linspace(0, 2*np.pi, 24, endpoint=False)
        maxdev = np.zeros_like(te)
        _, yc = ref_solve(f, (0, T), center, t_eval=te)
        for a_ in ang:
            z0 = (center[0] + delta*np.cos(a_), center[1] + delta*np.sin(a_))
            _, y = ref_solve(f, (0, T), z0, t_eval=te)
            ax.plot(y[0], y[1], color=col, lw=0.35, alpha=1.0)
            maxdev = np.maximum(maxdev, np.hypot(y[0]-yc[0], y[1]-yc[1]))
        ax.plot([center[0]], [center[1]], 'o', color=INK, ms=2.2)
        out[name] = maxdev
        facts[name] = {'center': center, 'maxdev_at_T': r(maxdev[-1]), 'bound_at_T': r(delta*np.exp(T))}
    ax.set(xlim=(-3.4, 3.4), ylim=(-2.4, 2.4), xlabel=r'$q$', ylabel=r'$p$')
    ax.set_title('(a) 两个初值小圆的轨迹束')
    ax = axes[1]
    ax.semilogy(te, delta*np.exp(te), color=INK, lw=1.0, ls='--', label=r'$0.05e^{t}$')
    ax.semilogy(te, out['far'], color=BLUE, lw=1.1, label=r'$(0,1.2)$')
    ax.semilogy(te, out['near_separatrix'], color=RED, lw=1.1, label=r'$(0,1.9)$')
    ax.set(xlim=(0, T), ylim=(0.03, 200), xlabel=r'$t$', ylabel='最大偏差')
    ax.set_title('(b) 实际偏差与Grönwall上界')
    ax.legend(loc='upper left', handlelength=1.6)
    save(fig, D/'ode-trajectory-tube', 'figure', facts)


def ode_flow_deformation():
    """Flow map carries a disk of initial values: pendulum vs damped pendulum."""
    fig, axes = figure(width_mm=150, height_mm=58, ncols=2, sharey=True)
    center, rad = np.array([-1.0, 0.0]), 0.35
    ang = np.linspace(0, 2*np.pi, 400)
    pts0 = center[:, None] + rad*np.vstack([np.cos(ang), np.sin(ang)])
    times = [0, 1.5, 3.0, 4.5]
    cols = [BLUE, GREEN, YELLOW, RED]
    fills = [BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL]
    facts = {'disk_center': center.tolist(), 'radius': rad, 'times': times}
    for ax, c, title in [(axes[0], 0.0, '(a) 无阻尼摆'), (axes[1], 0.4, '(b) 阻尼摆')]:
        f = lambda t, z: [z[1], -np.sin(z[0]) - c*z[1]]
        areas = []
        for tk, col, fl in zip(times, cols, fills):
            if tk == 0:
                P = pts0
            else:
                P = np.array([ref_solve(f, (0, tk), p)[1][:, -1] for p in pts0.T]).T
            x, y = P
            area = 0.5*abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))
            areas.append(r(area))
            ax.fill(x, y, color=fl, ec=col, lw=0.8)
            ax.text(x.mean(), y.max()+0.08, rf'$t={tk:g}$', color=col, fontsize=7.5, ha='center', va='bottom')
        _, yc = ref_solve(f, (0, 4.5), center, t_eval=np.linspace(0, 4.5, 300))
        ax.plot(yc[0], yc[1], color=MUTED, lw=0.6, ls=':')
        ax.set(xlim=(-1.8, 1.9), ylim=(-1.6, 1.6), xlabel=r'$q$')
        ax.set_title(title)
        facts[f'areas_c={c}'] = areas
        facts[f'predicted_area_c={c}'] = [r(np.pi*rad**2*np.exp(-c*tk)) for tk in times]
    axes[0].set_ylabel(r'$p$')
    save(fig, D/'ode-flow-deformation', 'figure', facts)


# ---------------------------------------------------------------- 2.3
def ode_phase_portraits():
    """Linear phase portraits classified by eigenvalues."""
    cases = [
        (r'(a) 稳定结点', np.array([[0, 1], [-1, -2.5]]), r'$\lambda=-0.5,-2$'),
        (r'(b) 鞍点', np.array([[0, 1], [1, 0]]), r'$\lambda=\pm1$'),
        (r'(c) 稳定焦点', np.array([[0, 1], [-1, -0.5]]), r'$\lambda=-0.25\pm0.97\mathrm{i}$'),
        (r'(d) 中心', np.array([[0, 1], [-1, 0]]), r'$\lambda=\pm\mathrm{i}$'),
        (r'(e) 不稳定焦点', np.array([[0, 1], [-1, 0.5]]), r'$\lambda=0.25\pm0.97\mathrm{i}$'),
        (r'(f) 退化结点（Jordan块）', np.array([[0, 1], [-1, -2]]), r'$\lambda=-1,-1$'),
    ]
    fig, axes = figure(width_mm=150, height_mm=100, ncols=3, nrows=2)
    g = np.linspace(-2, 2, 41)
    X, Y = np.meshgrid(g, g)
    facts = {}
    for ax, (title, A, lab) in zip(axes.ravel(), cases):
        U = A[0, 0]*X + A[0, 1]*Y
        V = A[1, 0]*X + A[1, 1]*Y
        ax.streamplot(X, Y, U, V, color=BLUE, linewidth=0.55, density=0.85, arrowsize=0.6, arrowstyle='-|>')
        ev = np.linalg.eigvals(A)
        if np.all(np.abs(ev.imag) < 1e-6):
            w, Vec = np.linalg.eig(A)
            for i in range(2):
                v = Vec[:, i].real
                ax.plot([-3*v[0], 3*v[0]], [-3*v[1], 3*v[1]], color=RED, lw=0.8, ls='--')
                if abs(w[0]-w[1]) < 1e-6:
                    break
        ax.plot([0], [0], 'o', color=INK, ms=2.4)
        ax.set(xlim=(-2, 2), ylim=(-2, 2), xticks=[-2, 0, 2], yticks=[-2, 0, 2])
        ax.set_aspect('equal')
        ax.set_title(title)
        ax.text(0.0, -1.88, lab, ha='center', va='bottom', fontsize=7.5, color=INK,
                bbox=dict(fc='white', ec='none', pad=0.6))
        facts[title] = {'A': A.tolist(), 'eigenvalues': [str(np.round(e, 4)) for e in ev]}
    save(fig, D/'ode-phase-portraits', 'figure', facts)


def ode_zoh_euler():
    """Piecewise-constant heating: exact solution, ZOH samples, Euler samples (h=1 and 2)."""
    lam = 0.2
    fig, ax = figure(width_mm=107, height_mm=56)
    def u_of(t):
        return np.where(t < 10, 0.4, 0.0)
    # exact continuous solution
    t = np.linspace(0, 20, 2001)
    x = np.where(t < 10, 2*(1-np.exp(-lam*t)), 2*(1-np.exp(-lam*10))*np.exp(-lam*(t-10)))
    ax.plot(t, x, color=INK, lw=1.2, label='连续解')
    ax.axvspan(0, 10, color=YELLOW_FILL, lw=0)
    ax.text(5, 0.08, '持续加热', ha='center', fontsize=7.5, color=INK)
    ax.text(15, 0.08, '停止加热', ha='center', fontsize=7.5, color=INK)
    facts = {'lambda': lam, 'input': 'u=0.4 on [0,10), 0 after', 'x(10)': r(2*(1-np.exp(-2)))}
    for h, mk, col, name in [(2.0, 'o', BLUE, '精确离散'), (2.0, 's', RED, 'Euler')]:
        n = int(20/h)
        xs = [0.0]
        if name == '精确离散':
            a, b = np.exp(-lam*h), (1-np.exp(-lam*h))/lam
        else:
            a, b = 1-lam*h, h
        for k in range(n):
            xs.append(a*xs[-1] + b*float(u_of(np.array(k*h))))
        tk = np.arange(n+1)*h
        ax.plot(tk, xs, mk, color=col, ms=3.2, mfc='white' if name == 'Euler' else col, mew=0.8,
                label=name)
        facts[f'{name}_h={h}'] = {'a': r(a), 'b': r(b), 'x_at_10': r(xs[int(10/h)]), 'x_at_20': r(xs[-1])}
    facts['exact_x_at_20'] = r(2*(1-np.exp(-2))*np.exp(-2))
    ax.set(xlim=(0, 20), ylim=(0, 2.0), xlabel=r'$t$', ylabel=r'$x$')
    ax.legend(loc='upper right', handlelength=1.2)
    save(fig, D/'ode-zoh-euler', 'figure', facts)


# ---------------------------------------------------------------- 2.4
def ode_transient_growth():
    """A=[[-1,K],[0,-2]]: norm of e^{tA}(0,1) and phase trajectories."""
    fig, axes = figure(width_mm=150, height_mm=54, ncols=2)
    t = np.linspace(0, 6, 600)
    facts = {}
    for K, col in [(0, BLUE), (8, GREEN), (20, RED)]:
        x1 = K*(np.exp(-t) - np.exp(-2*t))
        x2 = np.exp(-2*t)
        nrm = np.hypot(x1, x2)
        axes[0].plot(t, nrm, color=col, lw=1.1, label=rf'$K={K}$')
        axes[1].plot(x1, x2, color=col, lw=1.1)
        i = int(np.argmax(nrm))
        facts[f'K={K}'] = {'peak_norm': r(nrm[i]), 't_peak': r(t[i], 3),
                           'sym_part_max_eig': r((-3 + np.sqrt(1 + K**2))/2)}
        if K > 0:
            arrow_on(axes[1], x1, x2, 30, col)
    axes[0].axhline(1, color=MUTED, lw=0.6, ls='--')
    axes[0].set(xlim=(0, 6), ylim=(0, 5.6), xlabel=r'$t$', ylabel=r'$\|\bm{x}(t)\|_2$'.replace(r'\bm', r'\mathbf'))
    axes[0].set_title('(a) 状态范数先增后减')
    axes[0].legend(loc='upper right', handlelength=1.5)
    th = np.linspace(0, np.pi/2, 100)
    axes[1].plot(np.cos(th), np.sin(th), color=MUTED, lw=0.6, ls='--')
    axes[1].plot([0], [1], 'o', color=INK, ms=2.6)
    axes[1].set(xlim=(-0.2, 5.6), ylim=(-0.05, 1.1), xlabel=r'$x_1$', ylabel=r'$x_2$')
    axes[1].set_title('(b) 相平面中的轨迹')
    save(fig, D/'ode-transient-growth', 'figure', {'A': '[[-1,K],[0,-2]]', 'x0': [0, 1],
                                                   'x1(t)': 'K(e^-t - e^-2t)', 'x2(t)': 'e^-2t', **facts})


def ode_lyapunov_levels():
    """(a) quadratic Lyapunov ellipses for A=[[0,1],[-2,-3]]; (b) damped pendulum energy and zero set."""
    fig, axes = figure(width_mm=150, height_mm=60, ncols=2)
    ax = axes[0]
    A = np.array([[0, 1], [-2, -3]])
    P = np.array([[1.25, 0.25], [0.25, 0.25]])
    g = np.linspace(-2.2, 2.2, 300)
    X, Y = np.meshgrid(g, g)
    Vq = P[0, 0]*X**2 + 2*P[0, 1]*X*Y + P[1, 1]*Y**2
    ax.contour(X, Y, Vq, levels=[0.1, 0.3, 0.6, 1.0, 1.5, 2.1], colors=[YELLOW], linewidths=0.6)
    facts = {'A': A.tolist(), 'P': P.tolist(), 'Q': 'I'}
    for z0 in [(-1.8, 1.4), (1.6, 1.8), (1.9, -1.0), (-1.2, -1.9)]:
        tt = np.linspace(0, 8, 800)
        Z = np.array([np.linalg.matrix_power(np.eye(2), 0) for _ in range(0)])
        _, y = ref_solve(lambda t, z: A@z, (0, 8), z0, t_eval=tt)
        ax.plot(y[0], y[1], color=BLUE, lw=1.0)
        ax.plot([z0[0]], [z0[1]], 'o', color=BLUE, ms=2.4)
        arrow_on(ax, y[0], y[1], 25, BLUE)
    ax.set(xlim=(-2.2, 2.2), ylim=(-2.2, 2.2), xlabel=r'$x_1$', ylabel=r'$x_2$')
    ax.set_aspect('equal')
    ax.set_title('(a) 二次型等值线与线性轨迹')
    ax = axes[1]
    c = 0.5
    gq = np.linspace(-np.pi, np.pi, 300)
    gp = np.linspace(-2.2, 2.2, 300)
    Qg, Pg = np.meshgrid(gq, gp)
    E = Pg**2/2 + 1 - np.cos(Qg)
    ax.contour(Qg, Pg, E, levels=[0.1, 0.4, 0.8, 1.3, 1.8], colors=[YELLOW], linewidths=0.6)
    ax.axhline(0, color=RED, lw=0.8, ls='--')
    ax.text(-3.05, 0.07, r'$\dot V=0$', color=RED, fontsize=7.5, va='bottom')
    tt = np.linspace(0, 30, 3000)
    z0 = (2.4, 0.0)
    _, y = ref_solve(lambda t, z: [z[1], -np.sin(z[0]) - c*z[1]], (0, 30), z0, t_eval=tt)
    ax.plot(y[0], y[1], color=BLUE, lw=1.0)
    ax.plot([z0[0]], [z0[1]], 'o', color=BLUE, ms=2.4)
    arrow_on(ax, y[0], y[1], 60, BLUE)
    Hs = y[1]**2/2 + 1 - np.cos(y[0])
    facts['pendulum'] = {'c': c, 'z0': z0, 'V0': r(Hs[0]), 'V(30)': r(Hs[-1], 6)}
    ax.set(xlim=(-np.pi, np.pi), ylim=(-2.2, 2.2), xlabel=r'$q$', ylabel=r'$p$')
    ax.set_title('(b) 阻尼摆的能量与零导数集')
    save(fig, D/'ode-lyapunov-levels', 'figure', facts)


def ode_limit_cycle_bifurcation():
    """(a) van der Pol limit cycle, mu=1; (b) pitchfork diagram for x'=mu x - x^3."""
    fig, axes = figure(width_mm=150, height_mm=56, ncols=2)
    ax = axes[0]
    mu = 1.0
    f = lambda t, z: [z[1], mu*(1 - z[0]**2)*z[1] - z[0]]
    tt = np.linspace(0, 30, 4000)
    for z0, col in [((0.1, 0.0), BLUE), ((3.0, 3.0), GREEN), ((-3.5, -1.0), GREEN)]:
        _, y = ref_solve(f, (0, 30), z0, t_eval=tt)
        ax.plot(y[0], y[1], color=col, lw=0.9)
        ax.plot([z0[0]], [z0[1]], 'o', color=col, ms=2.4)
        arrow_on(ax, y[0], y[1], 80, col)
    _, yc = ref_solve(f, (0, 60), (2.0, 0.0), t_eval=np.linspace(40, 60, 3000))
    ax.plot(yc[0], yc[1], color=RED, lw=1.4)
    ax.set(xlim=(-4, 4), ylim=(-4, 4), xlabel=r'$x$', ylabel=r'$y$')
    ax.set_aspect('equal')
    ax.set_title('(a) van der Pol方程的极限环')
    ax = axes[1]
    m1 = np.linspace(-1, 0, 50)
    m2 = np.linspace(0, 1, 50)
    ax.plot(m1, 0*m1, color=BLUE, lw=1.4)
    ax.plot(m2, 0*m2, color=BLUE, lw=1.1, ls='--')
    ax.plot(m2, np.sqrt(m2), color=BLUE, lw=1.4)
    ax.plot(m2, -np.sqrt(m2), color=BLUE, lw=1.4)
    for mm in [-0.6, 0.5]:
        for x0 in np.linspace(-1.1, 1.1, 9):
            eq = [0.0] if mm < 0 else [-np.sqrt(mm), 0.0, np.sqrt(mm)]
            if any(abs(x0 - e) < 0.08 for e in eq):
                continue
            target = min(eq if mm < 0 else [-np.sqrt(mm), np.sqrt(mm)], key=lambda e: abs(e - x0)) if mm > 0 else 0.0
            if mm > 0:
                target = np.sqrt(mm) if x0 > 0 else -np.sqrt(mm)
            ax.annotate('', xy=(mm, x0 + 0.55*(target - x0)), xytext=(mm, x0),
                        arrowprops=dict(arrowstyle='-|>', color=MUTED, lw=0.6, mutation_scale=6))
    ax.set(xlim=(-1, 1), ylim=(-1.2, 1.2), xlabel=r'$\mu$', ylabel=r'平衡点 $x^\ast$'.replace('平衡点 ', ''))
    ax.set_title('(b) 叉形分岔')
    save(fig, D/'ode-limit-cycle-bifurcation', 'figure', {'van_der_pol_mu': mu,
         'pitchfork': "x'=mu x - x^3; stable branches solid, unstable dashed"})


def ode_input_response():
    """Temperature model with oscillating input: two initial values and the variation-of-constants band."""
    lam, w = 0.2, 0.5
    fig, ax = figure(width_mm=107, height_mm=56)
    t = np.linspace(0, 40, 2000)
    u = lambda s: 0.4 + 0.2*np.sin(w*s)
    amp = 0.2/np.hypot(lam, w)
    phi = np.arctan2(w, lam)
    xs = lambda s: 2 + amp*np.sin(w*s - phi)
    facts = {'lambda': lam, 'input': 'u=0.4+0.2 sin(0.5 t)', 'forced_amplitude': r(amp), 'phase_lag': r(phi)}
    for x0, col in [(0.0, BLUE), (4.0, GREEN)]:
        C = x0 - xs(0)
        x = xs(t) + C*np.exp(-lam*t)
        ax.plot(t, x, color=col, lw=1.1, label=rf'$x_0={x0:g}$')
        bound_hi = 2 + np.exp(-lam*t)*abs(x0 - 2) + (0.2/lam)*(1 - np.exp(-lam*t))
        bound_lo = 2 - np.exp(-lam*t)*abs(x0 - 2) - (0.2/lam)*(1 - np.exp(-lam*t))
        ax.plot(t, bound_hi, color=col, lw=0.6, ls=':')
        ax.plot(t, bound_lo, color=col, lw=0.6, ls=':')
    ax.axhspan(2 - amp, 2 + amp, color=YELLOW_FILL, lw=0)
    ax.axhline(2, color=MUTED, lw=0.6, ls='--')
    ax.set(xlim=(0, 40), ylim=(-0.4, 4.4), xlabel=r'$t$', ylabel=r'$x$')
    ax.legend(loc='upper right', handlelength=1.5)
    save(fig, D/'ode-input-response', 'figure', facts)


# ---------------------------------------------------------------- 2.5
def _euler(f, t0, x0, h, n):
    x = np.array(x0, float); t = t0
    for _ in range(n):
        x = x + h*f(t, x); t += h
    return x


def _rk2(f, t0, x0, h, n):
    x = np.array(x0, float); t = t0
    for _ in range(n):
        k1 = f(t, x); k2 = f(t + h/2, x + h/2*k1)
        x = x + h*k2; t += h
    return x


def _rk4(f, t0, x0, h, n):
    x = np.array(x0, float); t = t0
    for _ in range(n):
        k1 = f(t, x); k2 = f(t + h/2, x + h/2*k1); k3 = f(t + h/2, x + h/2*k2); k4 = f(t + h, x + h*k3)
        x = x + h/6*(k1 + 2*k2 + 2*k3 + k4); t += h
    return x


def ode_convergence_orders():
    """Global error at T=5 for x'=x cos t (smooth) and for switched heating (kink at t=pi)."""
    fig, axes = figure(width_mm=150, height_mm=58, ncols=2)
    T = 5.0
    f = lambda t, x: x*np.cos(t)
    exact = np.exp(np.sin(T))
    ks = np.arange(2, 13)
    hs = T/2.0**ks
    facts = {'problem': "x'=x cos t, x(0)=1, T=5, exact exp(sin 5)", 'h': [r(h, 6) for h in hs]}
    for name, m, ev, col, mk in [('Euler', _euler, 1, RED, 's'), ('RK2', _rk2, 2, YELLOW, '^'), ('RK4', _rk4, 4, BLUE, 'o')]:
        err = np.array([abs(m(f, 0.0, 1.0, h, int(round(T/h))) - exact) for h in hs])
        mask = err > 1e-13
        axes[0].loglog(hs[mask], err[mask], mk+'-', color=col, ms=2.8, lw=1.0, label=name)
        axes[1].loglog((T/hs*ev)[mask], err[mask], mk+'-', color=col, ms=2.8, lw=1.0, label=name)
        facts[name] = [float(f'{e:.3e}') for e in err]
        sl = np.polyfit(np.log(hs[mask][:6]), np.log(err[mask][:6]), 1)[0]
        facts[name+'_slope'] = r(sl, 2)
    # RK4 on the switched heating problem
    lam, ts = 0.2, np.pi
    g = lambda t, x: -lam*x + (0.4 if t < ts else 0.0)
    xs = 2*(1 - np.exp(-lam*ts))*np.exp(-lam*(T - ts))
    err = np.array([abs(_rk4(g, 0.0, 0.0, h, int(round(T/h))) - xs) for h in hs])
    axes[0].loglog(hs, err, 'o--', color=GREEN, ms=2.8, lw=1.0, mfc='white', label='RK4，有折点')
    facts['RK4_switched'] = [float(f'{e:.3e}') for e in err]
    facts['RK4_switched_slope'] = r(np.polyfit(np.log(hs), np.log(err), 1)[0], 2)
    for p, yref in [(4, 1.5e-4)]:
        hh = np.array([hs[0], hs[-1]])
        axes[0].loglog(hh, yref*(hh/hh[0])**p, color=MUTED, lw=0.6, ls=':')
    axes[0].text(1.3e-3, 2e-14, '斜率4', fontsize=7.5, color=MUTED, ha='left', va='bottom')
    axes[0].set(xlabel=r'$h$', ylabel=r'$|\widehat x_N-x(5)|$')
    axes[0].set_title('(a) 终点误差与步长')
    axes[0].legend(loc='lower right', handlelength=1.6)
    axes[1].set(xlabel='向量场调用次数', ylabel=r'$|\widehat x_N-x(5)|$')
    axes[1].set_title('(b) 终点误差与计算量')
    axes[1].legend(loc='lower left', handlelength=1.6)
    save(fig, D/'ode-convergence-orders', 'figure', facts)


def ode_stiff():
    """x'=-50(x-cos t): explicit Euler near its step limit, backward Euler and trapezoid with h=0.2."""
    k = 50.0
    exact = lambda t: (2500*np.cos(t) + 50*np.sin(t))/2501 - 2500/2501*np.exp(-k*t)
    fig, axes = figure(width_mm=150, height_mm=56, ncols=2, sharey=True)
    tt = np.linspace(0, 3, 1500)
    facts = {'k': k, 'exact': '(2500cos t+50 sin t)/2501 - (2500/2501)e^{-50t}'}
    ax = axes[0]
    ax.plot(tt, exact(tt), color=INK, lw=1.2, label='精确解')
    for h, col, mk in [(0.038, BLUE, 'o'), (0.042, RED, 's')]:
        n = int(3/h); x = [0.0]
        for i in range(n):
            x.append(x[-1] + h*(-k*(x[-1] - np.cos(i*h))))
        tk = np.arange(n+1)*h
        x = np.array(x)
        keep = np.arange(len(x)) <= (np.argmax(np.abs(x) > 3) if (h > 0.04 and (np.abs(x) > 3).any()) else len(x))
        ax.plot(tk[keep], x[keep], mk+'-', color=col, ms=2.0, lw=0.6, label=rf'$h={h}$')
        facts[f'euler_h={h}'] = {'amplification': r(1 - k*h), 'x_final': r(x[-1])}
    ax.set(xlim=(0, 3), ylim=(-2.2, 2.2), xlabel=r'$t$', ylabel=r'$x$')
    ax.set_title('(a) 显式Euler')
    ax.legend(loc='lower left', handlelength=1.5)
    ax = axes[1]
    ax.plot(tt, exact(tt), color=INK, lw=1.2, label='精确解')
    h = 0.2; n = int(3/h)
    xb, xt = [0.0], [0.0]
    for i in range(n):
        t1 = (i+1)*h
        xb.append((xb[-1] + h*k*np.cos(t1))/(1 + h*k))
        xt.append(((1 - h*k/2)*xt[-1] + h*k/2*(np.cos(i*h) + np.cos(t1)))/(1 + h*k/2))
    tk = np.arange(n+1)*h
    ax.plot(tk, xb, 'o-', color=GREEN, ms=2.4, lw=0.7, label='后向Euler')
    ax.plot(tk, xt, '^-', color=PURPLE, ms=2.4, lw=0.7, label='梯形法')
    facts['implicit_h'] = h
    facts['R_backward'] = r(1/(1 + h*k)); facts['R_trapezoid'] = r((1 - h*k/2)/(1 + h*k/2))
    facts['backward_err_max'] = r(np.max(np.abs(np.array(xb) - exact(tk))))
    facts['trap_x1'] = r(xt[1]); facts['exact_x1'] = r(exact(h))
    ax.set(xlim=(0, 3), xlabel=r'$t$')
    ax.set_title(r'(b) 隐式方法，$h=0.2$'.replace(r'，$h=0.2$', ''))
    ax.legend(loc='lower left', handlelength=1.5)
    save(fig, D/'ode-stiff', 'figure', facts)


def ode_stability_regions():
    """Absolute stability regions |R(z)|<=1."""
    fig, axes = figure(width_mm=150, height_mm=62, ncols=2, sharey=True)
    xr = np.linspace(-5, 3, 600); yr = np.linspace(-3.5, 3.5, 600)
    Xg, Yg = np.meshgrid(xr, yr); Z = Xg + 1j*Yg
    R = {'Euler': 1 + Z, 'RK2': 1 + Z + Z**2/2, 'RK4': 1 + Z + Z**2/2 + Z**3/6 + Z**4/24,
         '后向Euler': 1/(1 - Z), '梯形法': (1 + Z/2)/(1 - Z/2)}
    ax = axes[0]
    for name, col, ls in [('RK4', BLUE, '-'), ('RK2', YELLOW, '-'), ('Euler', RED, '-')]:
        ax.contourf(Xg, Yg, np.abs(R[name]), levels=[0, 1], colors=[{BLUE: BLUE_FILL, YELLOW: YELLOW_FILL, RED: RED_FILL}[col]])
        ax.contour(Xg, Yg, np.abs(R[name]), levels=[1], colors=[col], linewidths=0.9)
    handles = [Line2D([], [], color=c, lw=0.9) for c in (RED, YELLOW, BLUE)]
    ax.legend(handles, ['Euler', 'RK2', 'RK4'], loc='upper left', handlelength=1.5)
    ax.set_title('(a) 显式方法')
    ax = axes[1]
    ax.contourf(Xg, Yg, np.abs(R['后向Euler']), levels=[0, 1], colors=[GREEN_FILL])
    ax.contour(Xg, Yg, np.abs(R['后向Euler']), levels=[1], colors=[GREEN], linewidths=0.9)
    ax.axvline(0, color=PURPLE, lw=1.1, ls='--')
    ax.legend([Line2D([], [], color=GREEN, lw=0.9), Line2D([], [], color=PURPLE, lw=1.1, ls='--')],
              ['后向Euler', '梯形法边界'], loc='upper left', handlelength=1.5)
    ax.set_title('(b) 隐式方法')
    for ax in axes:
        ax.axhline(0, color=GRID, lw=0.5); ax.axvline(0, color=GRID, lw=0.5)
        ax.plot([-2.1], [0], 'x', color=INK, ms=4)
        ax.set(xlim=(-5, 3), ylim=(-3.5, 3.5), xlabel=r'$\mathrm{Re}\,z$')
        ax.set_aspect('equal')
    axes[0].set_ylabel(r'$\mathrm{Im}\,z$')
    real_ext = {}
    for name in ['Euler', 'RK2', 'RK4']:
        zs = np.linspace(-4, 0, 400001)
        Rr = {'Euler': 1 + zs, 'RK2': 1 + zs + zs**2/2, 'RK4': 1 + zs + zs**2/2 + zs**3/6 + zs**4/24}[name]
        real_ext[name] = r(zs[np.abs(Rr) <= 1].min(), 4)
    ys = np.linspace(0, 4, 400001)
    R4i = np.abs(1 + 1j*ys + (1j*ys)**2/2 + (1j*ys)**3/6 + (1j*ys)**4/24)
    real_ext['RK4_imag_extent'] = r(ys[R4i <= 1 + 1e-12].max(), 4)
    save(fig, D/'ode-stability-regions', 'figure', {'R': {'Euler': '1+z', 'RK2': '1+z+z^2/2',
         'RK4': '1+z+z^2/2+z^3/6+z^4/24', 'backward Euler': '1/(1-z)', 'trapezoid': '(1+z/2)/(1-z/2)'},
         'real_axis_left_endpoint': real_ext, 'marked_point': -2.1})


def ode_error_fan():
    """Euler h=0.5 on x'=x and x'=-x with exact solutions launched from each numerical point."""
    fig, axes = figure(width_mm=150, height_mm=56, ncols=2)
    h, T = 0.5, 2.5
    facts = {'h': h, 'T': T}
    for ax, lam, title in [(axes[0], 1.0, r'(a) $\dot x=x$'), (axes[1], -1.0, r'(b) $\dot x=-x$')]:
        n = int(T/h)
        xs = [1.0]
        for _ in range(n):
            xs.append(xs[-1]*(1 + h*lam))
        tk = np.arange(n+1)*h
        for i in range(n+1):
            tt = np.linspace(tk[i], T, 200)
            ax.plot(tt, xs[i]*np.exp(lam*(tt - tk[i])), color=BLUE if i == 0 else GREEN, lw=1.2 if i == 0 else 0.7)
            if i < n:
                ax.plot([tk[i+1], tk[i+1]], [xs[i+1], xs[i]*np.exp(lam*h)], color=RED, lw=1.2)
        ax.plot(tk, xs, 's-', color=INK, ms=2.8, lw=0.7)
        ax.set(xlim=(0, T*1.02), xlabel=r'$t$', ylabel=r'$x$')
        ax.set_title(title.replace(r'$\dot x=x$', '指数增长').replace(r'$\dot x=-x$', '指数衰减'))
        facts[f'lambda={lam}'] = {'euler': [r(v) for v in xs], 'exact_T': r(np.exp(lam*T)),
                                  'global_error': r(np.exp(lam*T) - xs[-1]),
                                  'local_errors': [r(xs[i]*(np.exp(lam*h) - 1 - lam*h)) for i in range(n)]}
    save(fig, D/'ode-error-fan', 'figure', facts)


def ode_adaptive_step():
    """Heun-Euler 2(1) pair with step control on van der Pol mu=3."""
    mu = 3.0
    f = lambda t, z: np.array([z[1], mu*(1 - z[0]**2)*z[1] - z[0]])
    tol, T = 1e-4, 20.0
    t, z, h = 0.0, np.array([2.0, 0.0]), 0.05
    acc_t, acc_x, acc_h, rej_t, rej_h = [0.0], [2.0], [], [], []
    nf = 0
    while t < T - 1e-12:
        h = min(h, T - t)
        k1 = f(t, z); k2 = f(t + h, z + h*k1); nf += 2
        low = z + h*k1
        high = z + h/2*(k1 + k2)
        est = np.linalg.norm(high - low, np.inf)
        fac = 0.9*(tol/max(est, 1e-16))**0.5
        if est <= tol:
            t += h; z = high
            acc_t.append(t); acc_x.append(z[0]); acc_h.append(h)
            h = h*min(2.0, max(0.2, fac))
        else:
            rej_t.append(t); rej_h.append(h)
            h = h*min(1.0, max(0.2, fac))
    _, yr = ref_solve(lambda s, y: f(s, y), (0, T), [2.0, 0.0], t_eval=[T])
    fig, axes = figure(width_mm=107, height_mm=72, nrows=2, sharex=True)
    tt = np.linspace(0, T, 2000)
    _, yy = ref_solve(lambda s, y: f(s, y), (0, T), [2.0, 0.0], t_eval=tt)
    axes[0].plot(tt, yy[0], color=INK, lw=1.0)
    axes[0].plot(acc_t, acc_x, 'o', color=BLUE, ms=1.4)
    axes[0].set(ylabel=r'$x$', ylim=(-2.6, 2.6))
    axes[1].semilogy(acc_t[1:], acc_h, 'o-', color=BLUE, ms=1.4, lw=0.6, label='接受')
    axes[1].semilogy(rej_t, rej_h, 'x', color=RED, ms=3.0, label='拒绝')
    axes[1].set(xlabel=r'$t$', ylabel=r'$h$', xlim=(0, T), ylim=(5e-4, 0.4))
    axes[1].legend(loc='upper right', handlelength=1.2, ncols=2)
    save(fig, D/'ode-adaptive-step', 'figure', {'mu': mu, 'tol': tol, 'pair': 'Heun-Euler 2(1)',
         'accepted': len(acc_h), 'rejected': len(rej_h), 'f_evals': nf,
         'h_min': float(f'{min(acc_h):.3e}'), 'h_max': r(max(acc_h)),
         'global_error_x(20)': float(f'{abs(acc_x[-1] - yr[0, -1]):.3e}'),
         'uniform_steps_for_hmin': int(np.ceil(T/min(acc_h)))})


# ---------------------------------------------------------------- 2.6
def ode_symplectic_energy():
    """(a) oscillator: explicit Euler, symplectic Euler, leapfrog; (b) pendulum energy error, h=0.5."""
    fig, axes = figure(width_mm=150, height_mm=60, ncols=2)
    ax = axes[0]
    h, n = 0.1, 120
    th = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(th), np.sin(th), color=MUTED, lw=0.8, ls='--')
    facts = {'oscillator': {'h': h, 'steps': n}}
    for name, M, col in [('显式Euler', np.array([[1, h], [-h, 1]]), RED),
                         ('辛Euler', np.array([[1 - h**2, h], [-h, 1]]), GREEN),
                         ('Leapfrog', np.array([[1 - h**2/2, h], [-h + h**3/4, 1 - h**2/2]]), BLUE)]:
        z = np.array([1.0, 0.0]); Zs = [z]
        for _ in range(n):
            z = M@z; Zs.append(z)
        Zs = np.array(Zs)
        ax.plot(Zs[:, 0], Zs[:, 1], color=col, lw=0.8 if name != '显式Euler' else 0.7, label=name)
        facts['oscillator'][name] = {'det': r(np.linalg.det(M), 8), 'energy_ratio_final': r((Zs[-1]**2).sum())}
    ax.plot([1], [0], 'o', color=INK, ms=2.4)
    ax.set(xlim=(-2.0, 3.8), ylim=(-2.2, 2.2), xlabel=r'$q$', ylabel=r'$p$')
    ax.set_aspect('equal')
    ax.set_title('(a) 谐振子，前120步')
    ax.legend(loc='upper right', handlelength=1.4)
    ax = axes[1]
    f = lambda z: np.array([z[1], -np.sin(z[0])])
    H = lambda z: z[1]**2/2 + 1 - np.cos(z[0])
    hp, T = 0.5, 400.0
    N = int(T/hp)
    def run(step):
        z = np.array([2.0, 0.0]); H0 = H(z); E = [0.0]
        for _ in range(N):
            z = step(z); E.append(H(z) - H0)
        return np.array(E)
    def eu(z): return z + hp*f(z)
    def rk4(z):
        k1 = f(z); k2 = f(z + hp/2*k1); k3 = f(z + hp/2*k2); k4 = f(z + hp*k3)
        return z + hp/6*(k1 + 2*k2 + 2*k3 + k4)
    def lf(z):
        q, p = z; p = p - hp/2*np.sin(q); q = q + hp*p; p = p - hp/2*np.sin(q); return np.array([q, p])
    tk = np.arange(N+1)*hp
    pend = {'h': hp, 'T': T, 'q0': 2.0, 'p0': 0.0, 'H0': r(1 - np.cos(2.0))}
    for name, st, col in [('显式Euler', eu, RED), ('RK4', rk4, YELLOW), ('Leapfrog', lf, BLUE)]:
        E = run(st)
        m = np.abs(E) < 1.0
        idx = np.argmax(~m) if (~m).any() else len(E)
        ax.plot(tk[:idx], E[:idx], color=col, lw=0.6 if name == 'Leapfrog' else 1.0, label=name)
        pend[name] = {'final': r(E[idx-1]), 'min': r(E[:idx].min()), 'max': r(E[:idx].max()),
                      'time_reaching_|dH|=1': r(tk[idx]) if idx < len(E) else None}
    ax.axhline(0, color=MUTED, lw=0.5)
    ax.set(xlim=(0, T), ylim=(-0.16, 0.12), xlabel=r'$t$', ylabel=r'$H-H_0$')
    ax.set_title('(b) 单摆能量误差，h=0.5')
    ax.legend(loc='lower left', handlelength=1.4, ncols=3)
    facts['pendulum'] = pend
    save(fig, D/'ode-symplectic-energy', 'figure', facts)


DRAWERS = {}


def register(*fs):
    for f in fs:
        DRAWERS[f.__name__.replace('_', '-')] = f


register(ode_slope_field, ode_picard, ode_nonunique, ode_blowup, ode_trajectory_tube,
         ode_flow_deformation, ode_phase_portraits, ode_zoh_euler, ode_transient_growth,
         ode_lyapunov_levels, ode_limit_cycle_bifurcation, ode_input_response, ode_convergence_orders,
         ode_stiff, ode_stability_regions, ode_error_fan, ode_adaptive_step, ode_symplectic_energy)

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
