from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# (a) lambda_min of [[Y,b],[b^T,t]], Y=[[2,1],[1,2]], b=(1,1). (b) [[y,b],[b,1]]>=0 iff y>=b^2.
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panels(fig, .1, .985, .985, .25, .25)
a, b = axes
Y = np.array([[2., 1.], [1., 2.]]); v = np.array([1., 1.])
t = np.linspace(0, 1.5, 300)
lm = [np.linalg.eigvalsh(np.block([[Y, v[:, None]], [v[None], np.array([[s]])]]))[0] for s in t]
a.axhline(0, color=MUTED, lw=.85); a.plot(t, lm, color=BLUE, lw=1.5, zorder=3); dot(a, (2/3, 0))
setup(a, (0, 1.5), (-.7, .55), [0, .5, 1, 1.5], [-.5, 0, .5], xl='$t$', yl='$\\lambda_{\\min}$', equal=False)
a.text(2/3+.05, -.13, '$t=2/3$', color=RED, fontsize=7.5)
y = np.linspace(-.2, 1.3, 300)
bb = np.linspace(-1.2, 1.2, 400)
b.fill_betweenx(bb, bb**2, 1.4, where=bb**2 <= 1.4, facecolor=BLUE_FILL, edgecolor='none', zorder=1)
b.plot(bb**2, bb, color=BLUE, lw=1.5, zorder=2)
b.plot([0, 0], [-1.2, 1.2], color=EDGE, lw=1.3, zorder=3)
dot(b, (0, 0), GREEN); hollow(b, (0, .6), RED); hollow(b, (0, -.6), RED)
setup(b, (-.25, 1.4), (-1.2, 1.2), [0, .5, 1], [-1, 0, 1], xl='$y$', yl='$b$', equal=False)
b.text(.07, .68, '$(0,0.6)$', fontsize=7.5); b.text(.75, .05, '$y\\geq b^2$', fontsize=7.5, color=BLUE)
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'schur at t': 'lambda_min(2/3)=0', 'b': 'P=0 needs b=0'})
