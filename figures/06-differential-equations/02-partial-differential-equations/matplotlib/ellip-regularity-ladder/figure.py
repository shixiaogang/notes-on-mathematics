from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# f=1 on (1/2,1): -u''=f, u(0)=u(1)=0.
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.075, wspace=.5, bottom=.28, right=.985)
ax = axes[0]
ax.plot(X[X < .5], 0*X[X < .5], color=BLUE, lw=1.4); ax.plot(X[X > .5], 1+0*X[X > .5], color=BLUE, lw=1.4); hollow(ax, .5, 0, BLUE, 3.6); dot(ax, .5, 1, BLUE, 3.8)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.1, 1.25); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1]); hat01(ax, yl='$f$')
up = 1/8-np.maximum(X-.5, 0)
ax = axes[1]
ax.axhline(0, color=STROKE, lw=.6); ax.plot(X, up, color=BLUE, lw=1.4); dot(ax, .5, 1/8, RED, 4)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.42, .22); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([-.25, 0, .125]); ax.set_yticklabels(['-1/4', '0', '1/8']); hat01(ax, yl="$u'$")
u = np.where(X <= .5, X/8, 1/16+(X-.5)/8-(X-.5)**2/2)
ax = axes[2]
ax.plot(X, u, color=BLUE, lw=1.4); dot(ax, 0, 0, RED, 4); dot(ax, 1, 0, RED, 4)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.005, .1); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1/16]); ax.set_yticklabels(['0', '1/16']); hat01(ax, yl='$u$')
tags(fig, axes)
save(fig, HERE, 'figure', {'u': 'x/8 for x<=1/2; 1/16+(x-1/2)/8-(x-1/2)^2/2 else', 'u(1)': float(u[-1])})
