from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Noise levels (1, 2, 5) and total power P from 0 to 12.
# (a) water-filling powers P_1, P_2, P_3 (blue, purple, yellow) against P; breakpoints P = 1 and P = 7 (dotted).
# (b) total rate: water filling (blue), equal split P/3 (yellow), all power on the quietest component (purple);
#     red dots at P = 5: 1.5 and 1.352 bit per vector use.
s = np.array([1., 2., 5.])
Ps = np.linspace(0, 12, 601)
alloc = np.array([waterfill(s, P)[1] for P in Ps])
cw = (.5*np.log2(1+alloc/s)).sum(1)
ce = (.5*np.log2(1+(Ps[:, None]/3)/s)).sum(1)
c1 = .5*np.log2(1+Ps/s[0])
fig, axs = figure(width_mm=110, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.3, wspace=.3)
ax = axs[0]
for j, col in enumerate((BLUE, PURPLE, YELLOW)):
    ax.plot(Ps, alloc[:, j], color=col, lw=1.5 if col == YELLOW else 1.4)
for b in (1, 7):
    ax.axvline(b, color=STROKE, lw=.8, ls=DOT)
ax.set_xlim(0, 12); ax.set_ylim(0, 6.5); ax.set_xticks([0, 1, 5, 7, 12]); ax.set_yticks([0, 2, 4, 6])
ax.set_xlabel(r'$P$', labelpad=1); ax.set_ylabel(r'$P_j$', labelpad=1)
lab(ax, 9.2, 5.9, r'$P_1$', BLUE); lab(ax, 10.2, 3.9, r'$P_2$', PURPLE); lab(ax, 10.2, .55, r'$P_3$', YELLOW)
ax = axs[1]
ax.plot(Ps, c1, color=PURPLE, lw=1.3)
ax.plot(Ps, ce, color=YELLOW, lw=1.5)
ax.plot(Ps, cw, color=BLUE, lw=1.4)
i5 = np.argmin(abs(Ps-5))
dot(ax, 5, cw[i5]); dot(ax, 5, ce[i5])
ax.set_xlim(0, 12); ax.set_ylim(0, 2.6); ax.set_xticks([0, 5, 12]); ax.set_yticks([0, 1, 2])
ax.set_xlabel(r'$P$', labelpad=1); ax.set_ylabel('bit/次', labelpad=2)
lab(ax, 7.2, 2.25, '注水', BLUE); lab(ax, 8.8, 1.35, '平分', YELLOW); lab(ax, 8.8, .95, '只用分量1', PURPLE)
tags(fig, axs)
save(fig, HERE, 'figure', {'C_wf(5)': float(cw[i5]), 'C_equal(5)': float(ce[i5]), 'C_single(5)': float(c1[i5])})
