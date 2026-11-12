"""(a) Product density f_X(x) f_Y(y) = 1/(4 sqrt(y)) on [-1,1]x(0,1] for X ~ Unif(-1,1), Y = X^2 (white-to-blue),
with the band |y - x^2| <= 0.05 (red outline); the joint law puts mass 1 on the curve y = x^2 (blue).
(b) q_eps = (P_X x P_Y)(|y - x^2| <= eps) and the binary-label KL ln(1/q_eps) as eps decreases."""
from pathlib import Path
import sys, math
from matplotlib.colors import LinearSegmentedColormap
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

cmap = LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE_FILL, BLUE])
xs = np.linspace(-1, 1, 401); ys = np.linspace(0.002, 1, 400)
Xg, Yg = np.meshgrid(xs, ys)
D = 1/(4*np.sqrt(Yg))
fig, axs = figure(width_mm=110, height_mm=48, ncols=2)
ax = axs[0]
ax.pcolormesh(xs, ys, np.minimum(D, 1.0), cmap=cmap, shading="auto", vmin=0, vmax=1.0, rasterized=True)
eps = .05
ax.plot(xs, xs**2, color=BLUE, lw=1.4)
ax.plot(xs, xs**2+eps, color=RED, lw=.8, ls='--'); ax.plot(xs, np.maximum(xs**2-eps, 0), color=RED, lw=.8, ls='--')
ax.set_xlim(-1, 1); ax.set_ylim(0, 1); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, .5, 1])
ax.set_xlabel('$x$', labelpad=0); ax.set_ylabel('$y$', labelpad=3); gfmt(ax)
ax.set_box_aspect(.85)
tag(ax, '(a)', y=-.3)
xx, ww = grid_x(200000)
Fy = lambda t: np.sqrt(np.clip(t, 0, 1))
E = np.logspace(-4, 0, 60)
q = np.array([(ww*(Fy(xx**2+e)-Fy(xx**2-e))).sum() for e in E])
ax = axs[1]
ax.plot(E, np.log(1/q), color=BLUE, lw=1.4)
for e in (.1, .05, .01):
    qq = float((ww*(Fy(xx**2+e)-Fy(xx**2-e))).sum())
    ax.plot([e], [math.log(1/qq)], 'o', color=RED, ms=3)
ax.set_xscale('log'); ax.invert_xaxis()
ax.set_xlabel('$\\varepsilon$', labelpad=0); ax.set_ylabel('$\\ln(1/q_{\\varepsilon})$', labelpad=1)
ax.set_xticks([1, 1e-1, 1e-2, 1e-3, 1e-4]); ax.set_ylim(0, 5.2)
ax.set_box_aspect(.85)
tag(ax, '(b)', y=-.3)
qs = {str(e): float((ww*(Fy(xx**2+e)-Fy(xx**2-e))).sum()) for e in (.1, .05, .01, 1e-4)}
save(fig, HERE, 'figure', {'band_eps': eps, 'q_eps': qs, 'ln_inv_q': {k: math.log(1/v) for k, v in qs.items()}})
