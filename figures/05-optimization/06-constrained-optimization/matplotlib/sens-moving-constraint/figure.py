from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# min .5(x1-1-theta)^2+.5(x2-1)^2 s.t. theta*x1+x2<=2. Budget line rotates about (0,2), target moves. Active branch for .618<theta<2.
fig, ax = figure(width_mm=90, height_mm=62)
def sol(th):
    lam = (th**2+th-1)/(1+th**2)
    return np.array([1+th-lam*th, 1-lam]), lam
for th, ls, lw, col in [(.8, '--', .95, ACTIVE), (1, '-', 1.6, ACTIVE), (1.3, ':', 1.05, ACTIVE)]:
    xs = np.array([0, 2/th]); ax.plot(xs, 2-th*xs, color=col, lw=lw, ls=ls, zorder=3)
    c = (1+th, 1); ax.plot(*c, marker='x', color=BLUE, ms=4.2, mew=1.1, ls='none', zorder=6)
    ax.plot([c[0], sol(th)[0][0]], [c[1], sol(th)[0][1]], color=MUTED, lw=.7, zorder=2)
T = np.linspace(.8, 1.3, 101); P = np.array([sol(t)[0] for t in T])
ax.plot(P[:, 0], P[:, 1], color=GREEN, lw=1.8, zorder=5)
for th in (.8, 1.3): ax.plot(*sol(th)[0], 'o', color=GREEN, ms=3.4, zorder=6)
opt_point(ax, sol(1)[0])
ax.text(.42, 1.86, r'$\theta=0.8$', fontsize=7.5, color=MUTED)
ax.text(.05, 1.28, r'$\theta=1$', fontsize=7.5)
ax.text(.05, .84, r'$\theta=1.3$', fontsize=7.5, color=MUTED)
ax.set_aspect('equal'); clean(ax, (-.05, 2.6), (-.05, 2.15), xlabel='$x_1$', ylabel='$x_2$')
ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
save(fig, Path(__file__).resolve().parent, 'figure', {'x(1)': list(sol(1)[0]), 'lam(1)': sol(1)[1]})
