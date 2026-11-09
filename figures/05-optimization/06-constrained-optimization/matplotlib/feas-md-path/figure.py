from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
M = md(T=120); P = pgd(T=120)
fig, axs = figure(width_mm=112, height_mm=50, ncols=3, gridspec_kw={'width_ratios': [1.1, .8, .8]})
ax = axs[0]; triangle(ax); contours(ax); active(ax, V[0], V[1]); path(ax, bary(P)[:7], YELLOW, lw=1.2, ms=2.8); path(ax, bary(M)[:30], GREEN, lw=1.2, ms=2.4); dot(ax, bary(XS)); off(ax, (-.08, 1.08), (-.08, .93))
ax = axs[1]; T = np.arange(0, 40); ax.semilogy(T, np.maximum(M[:40, 2], 1e-12), color=GREEN, lw=1.4); ax.semilogy(T[:3], P[:3, 2], '-o', color=YELLOW, lw=1.4, ms=2.8, mew=0)
setup(ax, (0, 40), (1e-3, 1.5), [0, 20, 40], [1e-2, 1], xl='$t$', yl='$x_3^{(t)}$')
ax = axs[2]; T = np.arange(1, 81); D0 = np.sum(XS[:2]*np.log(XS[:2]/X0[:2])); ax.semilogy(T, f(M[1:81])-FS, color=GREEN, lw=1.4); ax.semilogy(T, L*D0/T, color=PURPLE, lw=1.2, ls=(0, (4, 2)))
setup(ax, (0, 80), (1e-5, 8), [0, 40, 80], [1e-4, 1e-2, 1], xl='$t$', yl='$f-f^*$')
panels(fig, .01, .985, .985, .2, .42); tags(fig, axs)
save(fig, HERE, 'figure', {'alpha': .25, 'D0': float(D0), 'first': M[:4].tolist()})
