from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# min (x1^2+4x2^2)/2, x1+x2=1. (a) contours and tangency. (b) restriction phi(s)=f(1-s,s).
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .23, .28)
a, b = axes
xs, ys = np.linspace(-.4, 1.7, 400), np.linspace(-.5, 1.3, 400); X, Y = np.meshgrid(xs, ys)
a.contour(X, Y, .5*(X**2+4*Y**2), levels=[.1, .4, .8, 1.3, 2.0], colors=BLUE, linewidths=.7, zorder=1)
a.plot([-.3, 1.6], [1.3, -.6], color=EDGE, lw=1.8, zorder=3)
setup(a, (-.4, 1.7), (-.5, 1.3), [0, 1], [0, 1])
gf = lambda x: np.array([x[0], 4*x[1]])
p = np.array([.8, .2]); arrow(a, p, p+.55*gf(p), color=BLUE); dot(a, p)
q = np.array([.2, .8]); g = gf(q); arrow(a, q, q+.13*g, color=BLUE)
tang = np.array([1, -1])/np.sqrt(2); pr = np.dot(g, tang)*tang
arrow(a, q, q-.18*pr, color=GREEN); dot(a, q, GREEN)
a.text(.72, .07, '$x^{*}$', color=RED, fontsize=8, ha='right'); a.text(1.22, .62, '$\\nabla f$', color=BLUE, fontsize=8)
a.text(.3, 1.16, '$\\nabla f$', color=BLUE, fontsize=8); a.text(.5, .92, '切向下降', color=INK, fontsize=7.5)
s = np.linspace(-.3, 1.1, 300); phi = .5*((1-s)**2+4*s**2); b.plot(s, phi, color=BLUE, lw=1.4)
setup(b, (-.3, 1.1), (0, 2.5), [0, .2, .8], [0, 1, 2], xl='$s$', yl='$\\phi(s)$', equal=False)
dot(b, (.2, .4)); dot(b, (.8, 1.3), GREEN)
b.text(.2, .1, '$s=1/5$', color=RED, fontsize=8, ha='center')
b.plot([.65, .95], [1.3-.15*3, 1.3+.15*3], color=YELLOW, lw=1.2)
b.text(.98, 1.6, "$\\phi'=3$", color=INK, fontsize=8, ha='right', va='bottom') if 0 else b.text(.58, 1.52, "$\\phi'=3$", color=INK, fontsize=8, ha='right')
tags(fig, axes)
save(fig, HERE, 'figure', {'x*': [.8, .2], 'nu': -.8, 'f*': .4, 'q': [.2, .8], 'grad_q': [.2, 3.2]})
