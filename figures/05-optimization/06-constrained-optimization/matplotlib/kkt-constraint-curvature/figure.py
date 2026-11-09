from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# min 1/2||x-(2,0)||^2 on unit circle. (a) geometry. (b) phi(theta)=5/2-2cos(theta) with osculating parabolas of curvature 2, -2.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .03, .985, .985, .24, .14)
a, b = axes
off(a, (-1.5, 3.3), (-1.55, 1.55))
th = np.linspace(0, 2*np.pi, 400); a.plot(np.cos(th), np.sin(th), color=EDGE, lw=1.8, zorder=3)
for r in (.6, 1.0, 1.8, 2.3, 3.0): a.plot(2+r*np.cos(th), r*np.sin(th), color=BLUE, lw=.7, zorder=1)
a.set_xlim(-1.5, 3.3); a.set_ylim(-1.55, 1.55)
hollow(a, (2, 0), BLUE); dot(a, (1, 0)); dot(a, (-1, 0), YELLOW)
a.text(2.08, .1, '$c$', color=BLUE, fontsize=8); a.text(.85, .12, '最近', color=RED, fontsize=7.5, ha='right'); a.text(-.85, .12, '最远', color=INK, fontsize=7.5)
s = np.linspace(-np.pi, np.pi, 400); b.plot(s, 2.5-2*np.cos(s), color=BLUE, lw=1.4)
near = np.linspace(-1.2, 1.2, 80); b.plot(near, .5+near**2, color=YELLOW, lw=1.3)
far = np.linspace(np.pi-1.2, np.pi, 40); b.plot(far, 4.5-(far-np.pi)**2, color=YELLOW, lw=1.3); b.plot(-far, 4.5-(far-np.pi)**2, color=YELLOW, lw=1.3)
setup(b, (-np.pi-.1, np.pi+.1), (0, 5.2), [-3, 0, 3], [0, 2, 4], xl='$\\theta$', yl='$\\phi(\\theta)$', equal=False)
dot(b, (0, .5)); dot(b, (np.pi, 4.5), YELLOW); dot(b, (-np.pi, 4.5), YELLOW)
tags(fig, axes, y=.01)
save(fig, HERE, 'figure', {'phi': '5/2-2cos(theta)', 'curvatures': [2, -2]})
