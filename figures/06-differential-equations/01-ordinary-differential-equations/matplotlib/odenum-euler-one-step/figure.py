from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: one Euler step: tangent vs curve, and h^2 scaling of the one-step error.
fig, ax = figure(width_mm=112, height_mm=52, ncols=2)
h = .5; t = np.linspace(0, .56, 200)
a = ax[0]
a.plot(t, exact(t), color=BLUE, lw=1.4)
a.plot([0, h], [X0, X0+h*f(0, X0)], color=GREEN, lw=1.4)
a.plot([0], [X0], 'o', color=RED, ms=4.8, zorder=5)
a.plot([h], [X0+h*f(0, X0)], 'o', color=GREEN, ms=4.2, zorder=5)
xe = float(exact(h))
a.plot([h], [xe], 'o', color=BLUE, ms=4.2, zorder=5)
a.plot([h, h], [X0+h*f(0, X0), xe], color=RED, lw=1.6)
a.text(h+.018, .2835, r'$\ell^{(1)}$', color=RED, va='center')
a.text(.29, .262, r'$x(t)$', color=BLUE, ha='right')
a.text(.3, .226, '切线', color=GREEN)
a.set_xticks([0, h]); a.set_xticklabels([r'$t_0$', r'$t_1$'])
a.set_xlim(-.02, .6); a.set_ylim(.19, .31); a.set_xlabel(r'$t$'); a.set_ylabel(r'$x$')
b = ax[1]
hs = 2.0**-np.arange(1, 9)
loc = np.array([abs(X0+v*f(0, X0)-float(exact(v))) for v in hs])
b.loglog(hs, loc, 'o-', color=GREEN, lw=1.2, ms=3.4)
b.loglog(hs, .048*hs**2, color=PURPLE, lw=.95, ls=(0, (4, 2)))
b.set_xlabel(r'$h$'); b.set_ylabel(r'$|\ell^{(1)}|$')
b.text(.075, 1.0e-4, r'$0.048\,h^2$', color=PURPLE)
panel(ax[0], '(a)', -.3); panel(ax[1], '(b)', -.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x=x(1-x), first Euler step', 'local': loc.tolist()})
