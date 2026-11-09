from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
def kl(x, c): return np.sum(np.where(x > 0, x*np.log(np.where(x > 0, x, 1)/c), 0), axis=-1)
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
for ax, c, r in zip(axs, (np.array([.34, .33, .33]), np.array([.47, .47, .06])), (.05, .05)):
    triangle(ax); off(ax, (-.08, 1.08), (-.12, .95))
    xs = np.linspace(-.1, 1.1, 800); ys = np.linspace(-.05, .95, 800); X, Y = np.meshgrid(xs, ys); x1, x2, x3 = unbary(X, Y); M = np.stack([x1, x2, x3], -1)
    Z = kl(np.clip(M, 0, None), c); Z = np.ma.masked_where((x1 < -1e-9) | (x2 < -1e-9) | (x3 < -1e-9), Z)
    ax.contour(X, Y, Z, levels=[r], colors=GREEN, linewidths=1.4, zorder=4)
    E = .5*np.sum((M-c)**2, -1); E = np.ma.masked_where((x1 < -1e-9) | (x2 < -1e-9) | (x3 < -1e-9), E)
    ax.contour(X, Y, E, levels=[r/2], colors=YELLOW, linewidths=1.2, linestyles=[(0, (3, 2))], zorder=3)
    dot(ax, bary(c), INK, ms=4.2)
panels(fig, .01, .99, .99, .1, .03); tags(fig, axs)
save(fig, HERE, 'figure', {'KL_radius': .05, 'Euclid': '||x-c||^2/2=.025'})
