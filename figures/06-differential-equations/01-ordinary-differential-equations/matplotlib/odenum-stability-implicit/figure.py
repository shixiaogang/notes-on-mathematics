from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: stability regions of backward Euler and the trapezoidal rule.
X, Y = np.meshgrid(np.linspace(-3, 3, 900), np.linspace(-2.4, 2.4, 800))
Z = X+1j*Y
fig, ax = figure(width_mm=112, height_mm=56, ncols=2, sharey=True)
for a, R, c in zip(ax, (1/(1-Z), (1+Z/2)/(1-Z/2)), ('(a) 后向 Euler', '(b) 梯形方法')):
    v = np.abs(R)
    a.contourf(X, Y, v, levels=[0, 1], colors=[BLUE_FILL])
    a.contour(X, Y, v, levels=[1], colors=[BLUE], linewidths=1.2)
    a.axhline(0, color=STROKE, lw=.7); a.axvline(0, color=STROKE, lw=.7)
    a.set_aspect('equal'); a.set_xlabel(r'$\mathrm{Re}\,z$'); a.set_xlim(-3, 3); a.set_ylim(-2.4, 2.4)
    panel(a, c, -.3)
ax[0].set_ylabel(r'$\mathrm{Im}\,z$')
ax[1].plot([-10/4], [0], 'o', color=GREEN, ms=0) if 0 else None
save(fig, Path(__file__).resolve().parent, 'figure', {'R': ['1/(1-z)', '(1+z/2)/(1-z/2)']})
