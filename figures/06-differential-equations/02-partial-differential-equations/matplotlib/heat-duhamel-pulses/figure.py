from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Duhamel on the line: f=1 on |x|<.25, 0<s<.5. Five pulses, sum, exact at t=.5.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.27, bottom=.27)
xx = np.linspace(-2, 2, 500); ds = .1; t = .5
ss = np.arange(.05, .5, ds); cc = shades(len(ss))[::-1]
resp = [ds*box(xx, t-s, .25) for s in ss]
ax = axes[0]
for s, r, c in zip(ss, resp, cc[::-1]): ax.plot(xx, r, color=c, lw=1.3)
lab(ax, .3, .05, r'$s=0.45$', cc[0], ha='left'); lab(ax, 1.05, .028, r'$s=0.05$', cc[-1], ha='left')
ax.set_xlim(-2, 2); ax.set_ylim(0, .1); ax.set_xticks([-2, 0, 2]); ax.set_yticks([0, .05, .1]); ax.set_yticklabels(['0', '0.05', '0.1']); axlab(ax)
ax = axes[1]; S = np.linspace(.0005, .4995, 500); dS = S[1]-S[0]
ex = sum(dS*box(xx, t-s, .25) for s in S)
ax.plot(xx, ex, color=BLUE, lw=1.4); ax.plot(xx[::20], sum(resp)[::20], 'o', ms=3.2, color=GREEN, mew=0)
ax.set_xlim(-2, 2); ax.set_ylim(0, .24); ax.set_xticks([-2, 0, 2]); ax.set_yticks([0, .1, .2]); axlab(ax, yl='$u(x,0.5)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'max exact': float(ex.max()), 'max sum': float(sum(resp).max())}); print(ex.max(), sum(resp).max())
