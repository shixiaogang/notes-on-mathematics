from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: absolute stability regions of Euler, midpoint and RK4 (|R(z)|<=1).
Rs = [lambda z: 1+z, lambda z: 1+z+z**2/2, lambda z: 1+z+z**2/2+z**3/6+z**4/24]
caps = ['(a) Euler', '(b) 中点方法', '(c) RK4']
X, Y = np.meshgrid(np.linspace(-3.4, 1, 900), np.linspace(-3.2, 3.2, 1100))
Z = X+1j*Y
fig, ax = figure(width_mm=112, height_mm=58, ncols=3, sharey=True)
for a, R, c in zip(ax, Rs, caps):
    v = np.abs(R(Z))
    a.contourf(X, Y, v, levels=[0, 1], colors=[BLUE_FILL])
    a.contour(X, Y, v, levels=[1], colors=[BLUE], linewidths=1.2)
    a.axhline(0, color=STROKE, lw=.7); a.axvline(0, color=STROKE, lw=.7)
    a.set_xlim(-3.4, 1); a.set_ylim(-3.2, 3.2); a.set_aspect('equal')
    a.set_xlabel(r'$\mathrm{Re}\,z$'); a.set_xticks([-3, -2, -1, 0, 1])
    panel(a, c, -.3)
ax[0].set_ylabel(r'$\mathrm{Im}\,z$')
ax[0].plot([-2.5], [0], 'o', color=RED, ms=4, zorder=5); ax[0].plot([-1.5], [0], 'o', color=GREEN, ms=4, zorder=5)
ax[0].text(-2.5, .3, r'$-2.5$', color=RED, ha='center'); ax[0].text(-1.15, .22, r'$-1.5$', color=GREEN, ha='center')
save(fig, Path(__file__).resolve().parent, 'figure', {'R': ['1+z', '1+z+z^2/2', 'degree 4 Taylor']})
