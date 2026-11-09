from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Level sets of the barrier objective of the running example for two parameters.
fig, axs = figure(width_mm=112, height_mm=58, ncols=2)
pth = np.array([c for _, c in central_path(np.logspace(3, -4, 300))])
lim = (-2.3, 2.3, -.2, 4.3)
u, v = np.meshgrid(np.linspace(-2.3, 2.3, 500), np.linspace(-.2, 4.3, 500))
for ax, m, t, lv in zip(axs, (1., .1), ('(a)', '(b)'), ([2.8, 3.5, 4.5, 6, 8.5, 12], [1.9, 2.4, 3, 4, 6, 9, 13])):
    with np.errstate(all='ignore'):
        Z = .5*((u-3)**2+v**2) - m*(np.log(v-u**2)+np.log(4-v))
    Z = np.ma.masked_invalid(Z)
    region(ax); ax.contour(u, v, Z, levels=lv, colors=BLUE, linewidths=.75, zorder=1)
    ax.plot(pth[:, 0], pth[:, 1], color=GREEN, lw=1.4, zorder=3)
    c, _ = center(m, [0, 2]); ax.plot(*c, 'o', color=GREEN, ms=4.5, zorder=6); ax.plot(*XSTAR, 'o', color=RED, ms=4.5, zorder=6)
    ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3]); ax.set_aspect('equal'); tag(ax, '$x_1$', t)
axs[0].set_ylabel('$x_2$', labelpad=1)
save(fig, OUT, 'figure', {'mu': [1, .1], 'centers': [center(1., [0, 2])[0].tolist(), center(.1, [0, 2])[0].tolist()]})
