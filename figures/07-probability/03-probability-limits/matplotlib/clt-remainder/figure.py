from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Remainder r(x) = |e^{ix} - 1 - ix + x^2/2| of the second-order expansion (log-log axes),
# against the two bounds |x|^3/6 (better for |x| < 6) and x^2 (better for |x| > 6).
x = np.logspace(-1, np.log10(30), 800)
r = np.abs(np.exp(1j*x)-1-1j*x+x*x/2)
fig, ax = figure(width_mm=90, height_mm=54)
ax.plot(x, x**3/6, color=PURPLE, lw=1.1, ls=DASH)
ax.plot(x, x**2, color=PURPLE, lw=1.1, ls=DOT)
ax.plot(x, r, color=BLUE, lw=1.5)
ax.axvline(6, color=RED, lw=.8, ls=DASH)
dot(ax, 6, 36, RED, ms=3.6)
ax.set_xscale('log'); ax.set_yscale('log')
lab(ax, 9, 500, r'$|x|^3/6$', PURPLE, ha='right'); lab(ax, .33, .3, r'$x^2$', PURPLE, ha='right')
lab(ax, 1.6, .06, r'$r(x)$', BLUE, ha='left'); lab(ax, 6.4, 3, r'$x=6$', RED, ha='left')
ax.set_xlim(.1, 30); ax.set_ylim(1e-4, 1e3)
logticks(ax, [-1, 0, 1], 'x'); logticks(ax, [-4, -2, 0, 2], 'y')
axlab(ax, '$x$', None)
save(fig, HERE, 'figure', {'crossing': 6, 'r(1)': float(abs(np.exp(1j)-1-1j+.5)), 'r(6)': float(abs(np.exp(6j)-1-6j+18))})
