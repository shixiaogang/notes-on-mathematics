from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Dual cones in the plane, drawn in (first, second) coordinates.
def wedge(ax, a0, a1, R, fc, ec, z=1):
    th = np.radians(np.linspace(a0, a1, 60))
    ax.fill(np.r_[0, R*np.cos(th)], np.r_[0, R*np.sin(th)], facecolor=fc, edgecolor='none', zorder=z)
    ax.plot([0, R*np.cos(th[0])], [0, R*np.sin(th[0])], color=ec, lw=1.2, zorder=z+1)
    ax.plot([0, R*np.cos(th[-1])], [0, R*np.sin(th[-1])], color=ec, lw=1.2, zorder=z+1)
def bound(ax, a0, a1, R):
    for an in (a0, a1): ax.plot([0, R*np.cos(np.radians(an))], [0, R*np.sin(np.radians(an))], color=PURPLE, lw=1.3, ls=(0, (4, 2)), zorder=4)
    th = np.radians(np.linspace(a0, a1, 60)); ax.plot(R*np.cos(th), R*np.sin(th), color=PURPLE, lw=1.0, ls=(0, (4, 2)), zorder=4)
fig, axes = figure(width_mm=112, height_mm=40, ncols=3)
panels(fig, .01, .99, .99, .13, .06)
a, b, c = axes
R = 1.0
off(a, (-1.15, 1.15), (-.72, 1.28)); wedge(a, 0, 90, R, BLUE_FILL, BLUE); bound(a, 0, 90, R*1.12)
a.text(.42, .42, '$K$', color=BLUE, fontsize=8); a.text(.86, .86, '$K^*$', color=PURPLE, fontsize=8, ha='left', va='center')
ang = np.degrees(np.arctan(2.))  # K: |u|<=t/2 opens +-26.57deg around the t axis
off(b, (-1.15, 1.15), (-.72, 1.28)); wedge(b, 90-(90-ang), 90+(90-ang), R, BLUE_FILL, BLUE)
angd = np.degrees(np.arctan(.5))  # K*: |v|<=2w opens +-63.43deg
bound(b, angd, 180-angd, R*1.12)
b.text(0, .6, '$K$', color=BLUE, fontsize=8, ha='center'); b.text(1.0, .8, '$K^*$', color=PURPLE, fontsize=8, ha='center')
off(c, (-1.15, 1.15), (-.72, 1.28))
d = np.array([.6, .8]); c.plot([0, d[0]*R], [0, d[1]*R], color=BLUE, lw=2, zorder=3)
nang = np.degrees(np.arctan2(.8, .6))
th = np.radians(np.linspace(nang-90, nang+90, 80)); c.fill(np.r_[R*np.cos(th)], np.r_[R*np.sin(th)], facecolor=PURPLE_FILL, edgecolor='none', zorder=1)
c.plot([R*np.cos(th[0]), R*np.cos(th[-1])], [R*np.sin(th[0]), R*np.sin(th[-1])], color=PURPLE, lw=1.3, zorder=2)
c.text(d[0]*R+.03, d[1]*R+.1, '$K$', color=BLUE, fontsize=8, ha='center'); c.text(.62, -.42, '$K^*$', color=PURPLE, fontsize=8)
for ax in axes: ax.plot([0], [0], 'o', color=INK, ms=2.6, zorder=6)
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'a': 'orthant self-dual', 'b': 'K=|u|<=t/2; K*=|v|<=2w', 'c': 'K=ray along (3,4)/5; K*=half-plane'})
