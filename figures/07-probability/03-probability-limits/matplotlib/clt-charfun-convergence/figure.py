from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Characteristic functions of standardized sums against exp(-t^2/2).
# (a) Rademacher steps: phi_n(t) = cos(t/sqrt n)^n, n = 1, 4, 16 (real valued);
# (b) Exp(1) steps: phi_n(t) = exp(-i t sqrt n) (1 - i t/sqrt n)^(-n); real part, n = 1, 4, 16.
t = np.linspace(-6, 6, 1201)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.97, bottom=.28, wspace=.3)
COL = {1: YELLOW, 4: PURPLE, 16: GREEN}
g = np.exp(-t*t/2)
for n in (1, 4, 16):
    a.plot(t, np.cos(t/math.sqrt(n))**n, color=COL[n], lw=1.2)
for i, n in enumerate((1, 4, 16)):
    s = math.sqrt(n)
    ph = np.exp(-1j*t*s)*(1-1j*t/s)**(-n)
    b.plot(t, ph.real, color=COL[n], lw=1.2)
for ax in (a, b):
    ax.plot(t, g, color=BLUE, lw=1.5); ax.axhline(0, color=STROKE, lw=.6)
    ax.set_xlim(-6, 6); ax.set_ylim(-1.05, 1.08); ax.set_xticks([-6, -3, 0, 3, 6])
lab(a, 3.6, -.9, '$n=1$', YELLOW, ha='left'); lab(a, 4.1, .85, '$n=4$', PURPLE, ha='right'); lab(a, 1.7, .55, '$n=16$', GREEN, ha='left')
lab(b, 4.3, -.33, '$n=1$', YELLOW, ha='center'); lab(b, 2.0, .45, '$n=4$', PURPLE, ha='left')
lab(a, -2.2, .9, r'$\mathrm{e}^{-t^2/2}$', BLUE, ha='right'); lab(b, -2.2, .9, r'$\mathrm{e}^{-t^2/2}$', BLUE, ha='right')
axlab(a, '$t$', r'$\phi_{Z_n}(t)$'); axlab(b, '$t$', r'$\mathrm{Re}\,\phi_{Z_n}(t)$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'t=1': {'rad_n16': float(np.cos(1/4)**16), 'gauss': float(np.exp(-.5))}})
