from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Densities and two-sided tails of N(0,1), t_3, Cauchy (t_1). t_3 tail by numerical integration.
import math
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.27)
ax = axes[0]; x = np.linspace(-6, 6, 800)
ax.plot(x, phi(x), color=BLUE, lw=1.4); ax.plot(x, t_pdf(x, 3), color=YELLOW, lw=1.5); ax.plot(x, t_pdf(x, 1), color=PURPLE, lw=1.4)
lab(ax, .7, .37, '$\\mathcal{N}(0,1)$', BLUE, ha='left'); lab(ax, 2.0, .12, '$\\nu=3$', YELLOW, ha='left'); lab(ax, 3.2, .04, 'Cauchy', PURPLE, ha='left')
ax.set_xlim(-6, 6); ax.set_ylim(0, .45); ax.set_xticks([-4, 0, 4]); ax.set_yticks([0, .2, .4]); axlab(ax, '$t$')
ax = axes[1]; t = np.linspace(.01, 20, 600)
gx = np.linspace(0, 400, 400001); dx = gx[1]-gx[0]; pdf3 = t_pdf(gx, 3)
cum = np.concatenate([[0], np.cumsum((pdf3[1:]+pdf3[:-1])/2*dx)]); tail3 = 2*(.5-np.interp(t, gx, cum))
tailn = np.array([math.erfc(v/np.sqrt(2)) for v in t]); tailc = 1-2/pi*np.arctan(t)
ax.semilogy(t, tailn, color=BLUE, lw=1.4); ax.semilogy(t, tail3, color=YELLOW, lw=1.5); ax.semilogy(t, tailc, color=PURPLE, lw=1.4)
ax.semilogy(t[t > 1], 2/(pi*t[t > 1]), color=MUTED, lw=.9, ls=DASH)
ax.set_xlim(0, 20); ax.set_ylim(1e-5, 1.5); ax.set_xticks([0, 5, 10, 15, 20]); axlab(ax, '$t$')
tags(fig, axes)
save(fig, HERE, 'figure', {'tail t3 at 10': float(np.interp(10, t, tail3)), 'tail cauchy at 10': float(1-2/pi*np.arctan(10))})
