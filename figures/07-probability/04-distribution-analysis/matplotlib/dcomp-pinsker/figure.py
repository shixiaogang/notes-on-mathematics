from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# (a) P=Bern(t), Q=Bern(1/2): d_TV=|t-1/2| (blue) and Pinsker bound sqrt(D_KL(P||Q)/2) (purple).
# (b) P=N(0,1), Q=N(D,1): d_TV = 2Phi(D/2)-1 (blue); d_H^2 = 1-exp(-D^2/8) (purple, lower);
#     d_H sqrt(2-d_H^2) (purple dashed, upper); Pinsker sqrt(KL/2) = D/2 (yellow).
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.26, wspace=.28)
ax = axs[0]
t = np.linspace(1e-6, 1-1e-6, 600)
D = t*np.log(2*t)+(1-t)*np.log(2*(1-t))
ax.plot(t, np.abs(t-.5), color=BLUE, lw=1.4)
ax.plot(t, np.sqrt(D/2), color=PURPLE, lw=1.4)
lab(ax, .64, .04, r'$d_{\mathrm{TV}}$', BLUE, ha='left')
lab(ax, .5, .5, r'$\sqrt{D_{\mathrm{KL}}/2}$', PURPLE, ha='center')
ax.set_xlim(0, 1); ax.set_ylim(0, .65); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .2, .4, .6])
axlab(ax, '$t$', None)
ax = axs[1]
d = np.linspace(0, 5, 500)
tv = 2*Phi(d/2)-1
h2 = 1-np.exp(-d*d/8)
ax.plot(d, tv, color=BLUE, lw=1.4)
ax.plot(d, h2, color=PURPLE, lw=1.3)
ax.plot(d, np.sqrt(h2)*np.sqrt(2-h2), color=PURPLE, lw=1.3, ls=DASH)
ax.plot(d, d/2, color=YELLOW, lw=1.6)
lab(ax, 2.0, 1.12, r'$\Delta/2$', YELLOW, ha='left')
lab(ax, 4.95, .9, r'$d_{\mathrm{TV}}$', BLUE, ha='right', va='top')
lab(ax, 2.85, .36, r'$d_{\mathrm{H}}^2$', PURPLE, ha='left')
lab(ax, 3.7, 1.07, r'$d_{\mathrm{H}}\sqrt{2-d_{\mathrm{H}}^2}$', PURPLE, ha='center')
ax.set_xlim(0, 5); ax.set_ylim(0, 1.3); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$\Delta$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'Delta=1': {'tv': float(2*Phi(.5)-1), 'h2': 1-math.exp(-1/8)}})
