from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Phase-one problem of the running example: min rho s.t. g_i(x)<=rho.
fig, ax = figure(width_mm=84, height_mm=62)
u, v = np.meshgrid(np.linspace(-3.2, 3.2, 700), np.linspace(-1.6, 6.8, 700)); G = np.maximum(u**2-v, v-4)
ax.contourf(u, v, G, levels=[-10, 0], colors=[BLUE_FILL], zorder=0)
cs = ax.contour(u, v, G, levels=[-1, 1, 2], colors=BLUE, linewidths=.75, linestyles='solid', zorder=1)
ax.contour(u, v, G, levels=[0], colors=EDGE, linewidths=1.7, zorder=2)
for r, xx, yy in ((2, 0, 6.12), (1, 0, 5.12), (0, 0, 4.14), (-1, -.55, 3.1)):
    ax.text(xx, yy, f'$\\rho={r:g}$', fontsize=7.5, ha='center', zorder=7)
# barrier path for min rho - mu sum log(rho-g_i)
def F(z, m):
    r = z[2]-g(z[:2])
    return np.inf if np.any(r <= 0) else z[2]-m*np.log(r).sum()
def GH(z, m):
    r = z[2]-g(z[:2]); Jg = J(z[:2]); A = np.c_[-Jg, np.ones(2)]
    gr = np.array([0, 0, 1.]) - m*A.T@(1/r)
    H = m*(A.T@np.diag(1/r**2)@A + np.diag([2/r[0], 0, 0])) + 1e-10*np.eye(3)
    return gr, H
z = np.array([2., 1., 4.]); P = [z.copy()]
m = 1.
while m > 1e-4:
    for _ in range(60):
        gr, H = GH(z, m); d = -np.linalg.solve(H, gr); dec = -gr@d
        if dec/2 < 1e-9: break
        a = 1.
        while a > 1e-12 and F(z+a*d, m) > F(z, m)-.25*a*dec: a *= .5
        z = z+a*d; P.append(z.copy())
    m *= .3
P = np.array(P)
ax.plot(P[:, 0], P[:, 1], color=GREEN, lw=1.4, marker='o', ms=2.4, zorder=5)
ax.plot([0], [2], 'o', color=RED, ms=5, zorder=6); ax.text(.15, 2.15, '$(0,2)$', fontsize=7.5, zorder=7); ax.text(2.1, .62, '$x^{(0)}$', fontsize=7.5, zorder=7)
ax.set_xlim(-3.2, 3.2); ax.set_ylim(-1.6, 6.8); ax.set_aspect('equal'); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
save(fig, OUT, 'figure', {'final': P[-1].tolist(), 'steps': len(P)-1})
