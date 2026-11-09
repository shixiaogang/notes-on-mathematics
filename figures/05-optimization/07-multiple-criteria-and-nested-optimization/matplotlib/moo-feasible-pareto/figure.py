from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Isotropic pair on the half-plane x1+x2<=1/2. (a) decision plane, (b) objective plane.
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panels(fig, .08, .985, .985, .19, .24)
ax = axes[0]; setup(ax, (-.65, 1.35), (-.65, 1.35), [0, 1], [0, 1], '$x_1$', '$x_2$', equal=True)
ax.fill([-.65, 1.15, -.65], [1.15, -.65, -.65], color=BLUE_FILL, lw=0, zorder=1); ax.plot([-.65, 1.15], [1.15, -.65], color=EDGE, lw=2, zorder=2)
ax.plot([1, 0], [0, 1], color=MUTED, lw=1.1, ls=(0, (3, 2)), zorder=3); ax.plot([.75, -.25], [-.25, .75], color=RED, lw=2.4, zorder=4, solid_capstyle='round')
hollow(ax, A0, BLUE); hollow(ax, B0, BLUE); ax.text(1.05, -.13, '$a$', color=BLUE); ax.text(-.12, 1.06, '$b$', color=BLUE)
p = np.array([.25, .25]); g1, g2 = p-A0, p-B0
arrow(ax, p, p+g1, BLUE); arrow(ax, p, p+g2, BLUE); arrow(ax, p, p+.25*np.array([1., 1.]), PURPLE, lw=1.4); dot(ax, p)
ax.text(.42, .68, r'$\lambda\nabla g$', color=PURPLE); ax.text(-.62, .6, r'$g_1$', color=BLUE); ax.text(.45, -.55, r'$g_2$', color=BLUE)
ax.text(.1, .09, '$\\bar x$', color=INK) if 0 else ax.text(.02, .14, r'$\bar x$', color=INK)
ax = axes[1]; setup(ax, (0, 1.2), (0, 1.2), [0, .5, 1], [0, .5, 1], equal=True)
u, v = iso_front(); ax.plot(u, v, color=MUTED, lw=1.1, ls=(0, (3, 2)), zorder=3); ax.plot(u+1/16, v+1/16, color=RED, lw=2.2, zorder=4)
dot(ax, (5/16, 5/16)); ax.text(.36, .36, r'$f(\bar x)$', color=INK)
tags(fig, axes)
save(fig, HERE, 'figure', {'constraint': 'x1+x2<=1/2', 'front': '((1-t)^2+1/16, t^2+1/16)'})
