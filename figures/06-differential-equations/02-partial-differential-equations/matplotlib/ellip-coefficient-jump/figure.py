from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# -(a u')'=1, a=1 (x<1/2), a=4 (x>1/2), u(0)=u(1)=0.
C = -7/20
a = np.where(X < .5, 1., 4.)
up = -(X+C)/a
uL = -(X**2/2+C*X)
uR = ((1+2*C*1)-(X**2+2*C*X))/8
u = np.where(X < .5, uL, uR)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.105, wspace=.3, bottom=.27)
ax = axes[0]
ax.axvspan(.5, 1.02, color=BLUE_FILL, lw=0)
ax.plot(X, u, color=BLUE, lw=1.4)
lab(ax, .25, .012, '$a=1$', MUTED, ha='center', va='bottom'); lab(ax, .75, .012, '$a=4$', MUTED, ha='center', va='bottom')
ax.set_xlim(-.02, 1.02); ax.set_ylim(0, .09); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, .05]); hat01(ax, yl='$u$')
ax = axes[1]
ax.axvspan(.5, 1.02, color=BLUE_FILL, lw=0)
ax.axhline(0, color=STROKE, lw=.6)
ax.plot(X[X < .5], up[X < .5], color=YELLOW, lw=1.5); ax.plot(X[X >= .5], up[X >= .5], color=YELLOW, lw=1.5)
q = X+C
ax.plot(X, q, color=BLUE, lw=1.4)
lab(ax, .22, .24, r"$u'$", YELLOW); lab(ax, .8, .54, r"$q=-a\,u'$", BLUE, ha='right')
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.45, .72); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([-.4, 0, .4]); hat01(ax)
tags(fig, axes)
i = 500
save(fig, HERE, 'figure', {'C': C, 'u(1/2)': float(u[i]), 'jump': [float(up[i-1]), float(up[i+1])]})
print(u[i], uR[i], uL[i], up[i-1], up[i+1])
