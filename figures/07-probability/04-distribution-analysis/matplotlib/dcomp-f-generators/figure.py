from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Convex generators with f(1)=0 on t in [0,4]:
#   KL: t ln t;  TV: |t-1|/2;  squared Hellinger: (sqrt t - 1)^2/2;
#   reverse KL: -ln t.  Slopes at infinity: inf, 1/2, 1/2, 0; values at 0: 0, 1/2, 1/2, +inf.
fig, ax = figure(width_mm=84, height_mm=56)
t = np.linspace(1e-6, 4, 800)
kl = t*np.log(t)
tv = np.abs(t-1)/2
he = (np.sqrt(t)-1)**2/2
rk = -np.log(t)
ax.axhline(0, color=STROKE, lw=.85)
ax.plot(t, kl, color=BLUE, lw=1.4)
ax.plot(t, tv, color=PURPLE, lw=1.4)
ax.plot(t, he, color=YELLOW, lw=1.6)
ax.plot(t, rk, color=RED, lw=1.4, ls=DASH)
dot(ax, 1, 0, STROKE, ms=4)
lab(ax, 3.3, 3.55, r'$t\ln t$', BLUE, ha='center')
lab(ax, 3.92, 1.68, r'$\frac{1}{2}|t-1|$', PURPLE, ha='right')
lab(ax, 3.92, .62, r'$\frac{1}{2}(\sqrt{t}-1)^2$', YELLOW, ha='right', va='top')
lab(ax, .12, 3.3, r'$-\ln t$', RED, ha='left')
ax.set_xlim(0, 4); ax.set_ylim(-.5, 4.2)
ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2, 3, 4])
axlab(ax, '$t$', '$f(t)$')
save(fig, HERE, 'figure', {'f_at_0': {'KL': 0, 'TV': .5, 'H2': .5, 'revKL': 'inf'}})
