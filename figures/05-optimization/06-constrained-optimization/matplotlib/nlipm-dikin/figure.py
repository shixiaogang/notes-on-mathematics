from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Dikin ellipsoids of the barrier of the running example.
fig, ax = figure(width_mm=78, height_mm=62)
region(ax)
th = np.linspace(0, 2*np.pi, 300); circ = np.c_[np.cos(th), np.sin(th)].T
facts = {}
for x in ([0., 2.], [.8, 1.6], [-1., 2.2], [.9, .9]):
    x = np.array(x); gg = -g(x); JJ = J(x); H = np.diag([2/gg[0], 0.])+JJ.T@np.diag(1/gg**2)@JJ
    L = np.linalg.cholesky(H); E = np.linalg.solve(L.T, circ)
    P = x[:, None]+E
    ax.fill(P[0], P[1], color=GREEN_FILL, zorder=3); ax.plot(P[0], P[1], color=GREEN, lw=1.2, zorder=4); ax.plot(*x, 'o', color=GREEN, ms=3.2, zorder=5)
    facts[str(x.tolist())] = float((np.c_[P[1]-P[0]**2, 4-P[1]].min()))
ax.set_xlim(-2.3, 2.3); ax.set_ylim(-.2, 4.3); ax.set_aspect('equal'); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
save(fig, OUT, 'figure', {'min_slack_on_ellipse_boundary': facts})
