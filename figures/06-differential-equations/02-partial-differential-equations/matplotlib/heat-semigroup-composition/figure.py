from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# G(t)*G(s)=G(t+s) by numerical convolution; two-step vs one-step on the box.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.28, bottom=.27)
xx = np.linspace(-4, 4, 8001); dx = xx[1]-xx[0]; t, s = .02, .06
Gt, Gs = gauss(xx, t), gauss(xx, s)
conv = np.convolve(Gt, Gs, mode='same')*dx
ax = axes[0]
ax.plot(xx, Gt, color=YELLOW, lw=1.3); ax.plot(xx, Gs, color=PURPLE, lw=1.3); ax.plot(xx, gauss(xx, t+s), color=BLUE, lw=1.4); ax.plot(xx[::250], conv[::250], 'o', ms=3.4, color=GREEN, mew=0, zorder=5)
lab(ax, .18, 1.6, '$G(\\cdot,0.02)$', YELLOW, ha='left'); lab(ax, .42, .72, '$G(\\cdot,0.06)$', PURPLE, ha='left')
ax.set_xlim(-1.2, 1.2); ax.set_ylim(0, 2.1); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1, 2]); axlab(ax)
ax = axes[1]
u0 = (np.abs(xx) < .5)*1.; u1 = np.convolve(u0, Gs, mode='same')*dx; u2 = np.convolve(u1, Gt, mode='same')*dx
ax.plot(xx, u0, color=RED, lw=1.3); ax.plot(xx, u1, color=PURPLE, lw=1.3); ax.plot(xx, box(xx, t+s), color=BLUE, lw=1.4); ax.plot(xx[::250], u2[::250], 'o', ms=3.4, color=GREEN, mew=0, zorder=5)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(0, 1.2); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1]); axlab(ax)
tags(fig, axes)
save(fig, HERE, 'figure', {'sup conv err': float(np.abs(conv-gauss(xx, t+s)).max()), 'sup two-step err': float(np.abs(u2-box(xx, t+s)).max())}); print(np.abs(conv-gauss(xx, t+s)).max(), np.abs(u2-box(xx, t+s)).max())
