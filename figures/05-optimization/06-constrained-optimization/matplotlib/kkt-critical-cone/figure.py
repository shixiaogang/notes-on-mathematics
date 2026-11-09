from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Critical cones. Gradients (1,1),(0,-1). (a) tau=.5, both multipliers positive: K={0}. (b) tau=1, lam3=0: K=ray(-1,1). (c) min -x^2, x>=0.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panels(fig, .02, .985, .985, .3, .1)
a, b, c = axes
for ax in (a, b):
    off(ax, (-1.7, 1.2), (-.45, 1.5))
    R = 1.3; th = np.radians(np.linspace(135, 180, 30))
    ax.fill(np.r_[0, R*np.cos(th)], np.r_[0, R*np.sin(th)], facecolor=GREEN_FILL, edgecolor='none', zorder=1)
    ax.plot([0, R*np.cos(np.radians(135))], [0, R*np.sin(np.radians(135))], color=GREEN, lw=.9, zorder=2); ax.plot([0, -R], [0, 0], color=GREEN, lw=.9, zorder=2)
    ax.plot([-1.6, 1.1], [0, 0], color=MUTED, lw=.6, zorder=1); ax.plot([0, 0], [-.4, 1.4], color=MUTED, lw=.6, zorder=1)
    ax.text(-1.25, .17, '$F$', color=GREEN, fontsize=8)
dot(a, (0, 0), RED, ms=5.2); a.text(.1, .1, '$K=\\{0\\}$', color=RED, fontsize=8)
b.plot([0, R*np.cos(np.radians(135))], [0, R*np.sin(np.radians(135))], color=RED, lw=2.4, zorder=4); dot(b, (0, 0), RED, ms=5.2)
b.text(-.32, 1.02, '$K$', color=RED, fontsize=8)
x = np.linspace(-1.1, 1.3, 300); c.axvspan(0, 1.3, ymin=.0, facecolor=BLUE_FILL, edgecolor='none', zorder=0)
c.plot(x, -x*x, color=BLUE, lw=1.4)
c.spines['left'].set_position('zero'); setup(c, (-1.1, 1.3), (-1.55, .3), [-1, 1], [-1], xl='$x$', yl='', equal=False)
dot(c, (0, 0), YELLOW)
c.text(.65, -1.42, 'x≥0', color=INK, fontsize=7.5, ha='center') if 0 else None
tags(fig, axes, y=.01)
save(fig, HERE, 'figure', {'a': 'tau=.5', 'b': 'tau=1,lam=(1,0)', 'c': 'min -x^2 x>=0'})
