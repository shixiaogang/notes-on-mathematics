from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Bimodal target pi = 0.7 N(-2,0.6^2) + 0.3 N(2,0.6^2) (blue); candidate q = N(-2,0.6^2) (yellow).
# (b) integrands of D(Q||Pi)=int q ln(q/pi) (yellow) and D(Pi||Q)=int pi ln(pi/q) (blue), quadrature on [-8,8].
x = np.linspace(-8, 8, 16001); dx = x[1]-x[0]
pi = mix_pdf(x); q = npdf(x, -M_MIX, S_MIX)
rv = q*np.log(q/pi); fw = pi*np.log(pi/q)
Drev = float(np.sum(rv)*dx); Dfwd = float(np.sum(fw)*dx)
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.27, wspace=.28)
ax = axs[0]
ax.plot(x, pi, color=BLUE, lw=1.4); ax.plot(x, q, color=YELLOW, lw=1.6)
lab(ax, 2.5, .24, r'$\pi$', BLUE); lab(ax, -1.1, .55, r'$q$', YELLOW)
ax.set_xlim(-4.5, 4.5); ax.set_ylim(0, .72); axlab(ax, '$x$', None)
ax = axs[1]
ax.plot(x, fw, color=BLUE, lw=1.4); ax.plot(x, rv, color=YELLOW, lw=1.6)
ax.axhline(0, color=STROKE, lw=.85)
lab(ax, 2.7, 3.6, r'$\pi\ln(\pi/q)$', BLUE); lab(ax, -4.3, .7, r'$q\ln(q/\pi)$', YELLOW)
ax.set_xlim(-4.5, 4.5); ax.set_ylim(-.5, 5.2); axlab(ax, '$x$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'D(Q||Pi)': Drev, 'D(Pi||Q)': Dfwd, '-ln 0.7': -math.log(.7)})
