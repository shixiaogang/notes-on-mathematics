from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
x = E3; g = grad(x); s = np.eye(3)[1]; d = s-x
A_ = np.linspace(0, 1, 200); phi = f(x+A_[:, None]*d); up = f(x)+A_*(g@d)+.5*L*A_**2*(d@d)
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
ax = axs[0]; ax.plot(A_, phi, color=BLUE, lw=1.4); ax.plot(A_, up, color=YELLOW, lw=1.4)
for a, m in ((1, 's'), (.75, 'o'), (.5625, '^')):
    v = f(x+a*d); ax.plot([a], [v], m, color=GREEN, ms=4.6, mew=0, zorder=6); ax.plot([a, a], [0, v], color=MUTED, lw=.75, ls=(0, (1, 1.5)))
ax.text(.26, 1.92, '上界', color=YELLOW, fontsize=7.5, ha='right'); ax.text(.3, .62, '$\\phi(\\alpha)$', color=BLUE, fontsize=8)
setup(ax, (0, 1.03), (0, 2.5), [0, .5625, .75, 1], [0, 1, 2], xl='$\\alpha$'); ax.set_xticklabels(['0', '.56', '.75', '1'])
ax = axs[1]; T = np.arange(1, 1001)
for r, c, ls in (('open', GREEN, '-'), ('exact', YELLOW, '-'), ('smooth', PURPLE, '-')):
    X, *_ = fw(T=1000, rule=r); e = f(X[1:])-FS; ax.loglog(T, np.minimum.accumulate(e), color=c, lw=1.4, ls=ls)
ax.loglog(T, 2*L*2/(T+2), color=RED, lw=1.1, ls=(0, (4, 2)))
setup(ax, (1, 1000), (1e-7, 20), [1, 10, 100, 1000], [1e-6, 1e-3, 1], xl='$T$', yl='$\\min_{t\\leq T} f(x^{(t)})-f^*$')
panels(fig, .07, .985, .98, .2, .5); tags(fig, axs)
save(fig, HERE, 'figure', {'segment': 'e3 to e2', 'bound': '16/(T+2)'})
