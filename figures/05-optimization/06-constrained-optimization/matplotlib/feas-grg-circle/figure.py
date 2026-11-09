from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
y, z = .8, .6; G = -z/y
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
ax = axs[0]; t = np.linspace(0, 2*np.pi, 400); ax.plot(np.sin(t), np.cos(t), color=EDGE, lw=1.8, zorder=2)
ax.plot([z-.5, z+.5], [y+.5*.75, y-.5*.75], color=YELLOW, lw=1.2, zorder=3); dz = .35; dy = -z/y*dz
arrow(ax, (z, y), (z+dz, y), GREEN); arrow(ax, (z+dz, y), (z+dz, y+dy), PURPLE); dot(ax, (z, y), GREEN, ms=4.8); dot(ax, (0, -1), RED)
ax.text(z+dz/2, y+.05, '$\\mathrm{d}z$', color=INK, fontsize=8, ha='center'); ax.text(z+dz+.04, y+dy/2, '$\\mathrm{d}y$', color=INK, fontsize=8, va='center')
ax.text(-.02, .36, '$(y,z)=(4/5,3/5)$', fontsize=7.5, ha='center')
ax.axhline(0, color=MUTED, lw=.6, zorder=0); ax.axvline(0, color=MUTED, lw=.6, zorder=0)
ax.set_aspect('equal'); setup(ax, (-1.3, 1.3), (-1.3, 1.3), [-1, 0, 1], [-1, 0, 1], xl='$z$', yl='$y$', equal=True)
ax = axs[1]; Z = np.linspace(0, .995, 300); ax.plot(Z, np.sqrt(1-Z**2), color=BLUE, lw=1.4); ax.plot([.25, .95], [y+G*(.25-z), y+G*(.95-z)], color=YELLOW, lw=1.2); dot(ax, (z, y), GREEN, ms=4.8)
ax.text(.68, .86, '斜率 -3/4', fontsize=7.5)
setup(ax, (0, 1.05), (0, 1.15), [0, .3, .6, .9], [0, .5, 1], xl='$z$', yl='$F(z)=y(z)$')
panels(fig, .08, .985, .98, .2, .3); tags(fig, axs)
save(fig, HERE, 'figure', {'reduced_gradient': G})
