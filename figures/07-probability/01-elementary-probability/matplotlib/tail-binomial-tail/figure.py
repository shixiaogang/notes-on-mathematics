from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'tail-common'))
from tail_fig import *
# X ~ Bin(20,1/2): (a) mass table with the tail k>=15, (b) distribution function near the atom k=15.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, wspace=.34, bottom=.28)
ax = axes[0]
for k in KB:
    tail = k >= 15
    ax.bar(k, PB[k], width=.72, color=BLUE_FILL if tail else 'white', edgecolor=BLUE, lw=.75 if not tail else 1.0)
ax.axvline(14.5, color=RED, lw=1.2)
lab(ax, 15.1, .16, r'$\{X\geq15\}$', RED)
ax.set_xlim(-.8, 20.8); ax.set_ylim(0, .19); ax.set_xticks([0, 5, 10, 15, 20]); ax.set_yticks([0, .05, .1, .15])
axlab(ax, '$k$', '$p_X(k)$')
ax = axes[1]
F = np.cumsum(PB)
xs = np.arange(13, 19)
for k in xs:
    ax.plot([k, k+1], [F[k], F[k]], color=BLUE, lw=1.4, solid_capstyle='butt')
    ax.plot([k], [F[k]], 'o', ms=3.2, color=BLUE, mew=0)
    ax.plot([k+1], [F[k]], 'o', ms=3.2, mfc='white', mec=BLUE, mew=.8)
ax.plot([15, 15], [F[14], F[15]], color=RED, lw=1.4)
lab(ax, 15.2, (F[14]+F[15])/2, r"$p_X(15)$", RED, va="center")
lab(ax, 14.5, F[14]-.002, r"$F_X(15^-)$", INK, ha="center", va="top")
lab(ax, 15.5, F[15]+.0015, r"$F_X(15)$", INK, ha="center", va="bottom")
ax.set_xlim(12.6, 19); ax.set_ylim(.93, 1.004); ax.set_xticks([13, 14, 15, 16, 17, 18]); ax.set_yticks([.94, .96, .98, 1]); ax.set_yticklabels(["0.94", "0.96", "0.98", "1"])
axlab(ax, '$x$', '$F_X(x)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'P(X>=15)': float(PB[15:].sum()), 'P(X=15)': float(PB[15]), 'F(14)': float(F[14]), 'F(15)': float(F[15])})
