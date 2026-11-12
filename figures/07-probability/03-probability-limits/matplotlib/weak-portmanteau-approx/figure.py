from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Continuous approximations of indicators: closed F=[1,2]: f_k=max(0,1-k dist(x,F)) decreases to 1_F;
# open G=(1,2): g_k=min(1,k dist(x,G^c)) increases to 1_G.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.07, wspace=.25, bottom=.28)
x = np.linspace(-.2, 3.2, 1500)
dF = np.maximum(0, np.maximum(1-x, x-2)); dGc = np.maximum(0, np.minimum(x-1, 2-x))
shades = [YELLOW, GREEN, PURPLE, STROKE]
ax = axes[0]
for k, c in zip((1, 2, 4, 8), shades): ax.plot(x, np.maximum(0, 1-k*dF), color=c, lw=1.0)
ax.plot([1, 2], [1, 1], color=BLUE, lw=2.2, solid_capstyle='butt'); dot(ax, 1, 1, BLUE, ms=3.6); dot(ax, 2, 1, BLUE, ms=3.6)
ax.plot([-.2, 1], [0, 0], color=BLUE, lw=2.2); ax.plot([2, 3.2], [0, 0], color=BLUE, lw=2.2)
lab(ax, .05, .55, r'$k=1$', YELLOW); lab(ax, 1.5, 1.08, r'$F=[1,2]$', BLUE, ha='center')
ax.set_xlim(-.2, 3.2); ax.set_ylim(-.08, 1.25); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1])
ax = axes[1]
for k, c in zip((2, 4, 8, 16), shades): ax.plot(x, np.minimum(1, k*dGc), color=c, lw=1.0)
ax.plot([1, 2], [1, 1], color=BLUE, lw=2.2, solid_capstyle='butt')
ax.plot([-.2, 1], [0, 0], color=BLUE, lw=2.2); ax.plot([2, 3.2], [0, 0], color=BLUE, lw=2.2)
ax.plot([1, 2], [1, 1], 'o', ms=3.6, mfc='white', mec=BLUE, mew=1.0, zorder=7)
lab(ax, 1.5, .42, r'$k=2$', YELLOW, ha='center'); lab(ax, 1.5, 1.08, r'$G=(1,2)$', BLUE, ha='center')
ax.set_xlim(-.2, 3.2); ax.set_ylim(-.08, 1.25); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1])
for a in axes: axlab(a, r'$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'closed_k': [1, 2, 4, 8], 'open_k': [2, 4, 8, 16]})
