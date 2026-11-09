from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# MGDA on f1=(x1^2+9x2^2)/2, f2=||x-(4,3)||^2/2 with backtracking (c=1/2,beta=1/2).
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .07, .985, .985, .21, .26)
ax = axes[0]; setup(ax, (-.4, 5.4), (-.4, 3.4), range(0, 6), range(0, 4), '$x_1$', '$x_2$', equal=True)
X, Y = np.meshgrid(np.linspace(-.5, 5.5, 400), np.linspace(-.5, 3.5, 400)); F = fm(np.stack([X, Y], -1))
ax.contour(X, Y, F[0], levels=[1, 4, 9, 16, 25], colors=BLUE, linewidths=.7); ax.contour(X, Y, F[1], levels=[.5, 2, 4.5, 8], colors=BLUE, linewidths=.7, linestyles=[(0, (3, 2))])
w = np.linspace(0, 1, 400); C = xm(w); ax.plot(C[:, 0], C[:, 1], color=RED, lw=2, zorder=3)
starts = [(1, 1), (0, 2), (5, 1), (4, 0)]; out = {}
axb = axes[1]; setup(axb, (0, 26), (0, 9.5), range(0, 26, 5), range(0, 10, 2))
Fc = fm(xm(np.linspace(0, 1, 800))); axb.plot(Fc[0], Fc[1], color=RED, lw=2, zorder=3)
for s in starts:
    P, R, A_, T_ = mgda(s, 80); out[str(s)] = P[-1].tolist()
    col = GREEN; ax.plot(P[:, 0], P[:, 1], '-', color=col, lw=1.1, zorder=4); ax.plot(P[:6, 0], P[:6, 1], 'o', color=col, ms=2.6, zorder=5); dot(ax, P[-1], RED, ms=4.6, z=6); hollow(ax, s, GREEN, ms=4.2, z=6)
    V = fm(P).T; axb.plot(V[:, 0], V[:, 1], '-', color=col, lw=1.1, zorder=4); axb.plot(V[:6, 0], V[:6, 1], 'o', color=col, ms=2.6, zorder=5); dot(axb, V[-1], RED, ms=4.6, z=6); hollow(axb, V[0], GREEN, ms=4.2, z=6)
ax.text(.42, 1.14, '$x^{(0)}$', color=INK, fontsize=7.5)
axes[0].set_ylim(-.4, 3.4); tags(fig, axes)
save(fig, HERE, 'figure', {'limits': out}); print(out)
