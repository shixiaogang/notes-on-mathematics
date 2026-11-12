"""Families N(theta^3,1) (blue) and N(theta^2,1) (yellow). (a) mean map; dashed line m=0.5 hits theta^3 once, theta^2 twice.
(b) Fisher information G=9 theta^4 and 4 theta^2; both vanish at theta=0 (red)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2)
t = np.linspace(-1.3, 1.3, 400)
a.axhline(0, color=STROKE, lw=0.6); a.axvline(0, color=STROKE, lw=0.6)
a.plot(t, t**3, color=BLUE, lw=1.4); a.plot(t, t**2, color=YELLOW, lw=1.6)
a.axhline(0.5, color=STROKE, lw=0.85, ls='--')
r3 = 0.5**(1/3); r2 = 0.5**0.5
a.scatter([r3], [0.5], s=14, color=BLUE, zorder=5); a.scatter([-r2, r2], [0.5, 0.5], s=14, color=YELLOW, zorder=5)
a.scatter([0], [0], s=16, color=RED, zorder=6)
a.set_xlim(-1.3, 1.3); a.set_ylim(-1.6, 1.8); a.set_xlabel(r'$\theta$', labelpad=1); a.set_ylabel('均值', labelpad=1)
b.plot(t, 9*t**4, color=BLUE, lw=1.4); b.plot(t, 4*t**2, color=YELLOW, lw=1.6)
b.scatter([0], [0], s=16, color=RED, zorder=6)
b.set_xlim(-1.3, 1.3); b.set_ylim(0, 8); b.set_xlabel(r'$\theta$', labelpad=1); b.set_ylabel(r'$G(\theta)$', labelpad=1)
tag(a, '(a)', y=-0.30); tag(b, '(b)', y=-0.30)
save(fig, HERE, 'figure', {'roots_cubic': r3, 'roots_square': [-r2, r2]})
