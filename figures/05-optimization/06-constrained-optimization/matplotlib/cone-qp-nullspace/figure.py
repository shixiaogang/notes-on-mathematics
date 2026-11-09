from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Equality QP: running objective on x1+x2=2, x=x_p+u z, x_p=(2,0), z=(1,-1).
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .065, .985, .985, .25, .24)
a, b = axes
xl, yl = (-.25, 3.1), (-.65, 2.35)
X, Y = grid2(xl, yl)
a.contour(X, Y, fls(X, Y), levels=[1.75, 2.25, 3, 4, 5.5, 7.5], colors=BLUE, linewidths=.7, zorder=2)
active(a, (-.25, 2.25), (2.65, -.65))
xp = np.array([2., 0.]); z = np.array([1., -1.])
hollow(a, xp, GREEN); dot(a, XSTAR)
arrow(a, xp, xp-.5*z, color=GREEN, lw=1.5, z=6)
arrow(a, XSTAR, XSTAR+.42*np.array([1, 1]), color=PURPLE, lw=1.4, z=6)
setup(a, xl, yl, range(0, 4), [0, 1, 2])
a.text(2.1, .03, '$x_{\\mathrm{p}}$', color=INK, fontsize=8)
a.text(1.46, .15, '$x^*$', color=RED, fontsize=8, ha='right')
a.text(2.02, .9, '$(1,1)$', color=PURPLE, fontsize=7.5)
a.text(.42, 1.92, '$x_1+x_2=2$', fontsize=7.5)
u = np.linspace(-2, 1, 300)
phi = u**2+u+2.5
b.plot(u, phi, color=BLUE, lw=1.4)
dot(b, (-.5, 2.25)); hollow(b, (0, 2.5), GREEN)
setup(b, (-2.1, 1.1), (1.7, 4.8), [-2, -1, 0, 1], [2, 3, 4], xl='$u$', yl='$\\varphi(u)$', equal=False)
b.text(-.5, 1.88, '$u^*=-\\frac{1}{2}$', color=RED, fontsize=7.5, ha='center')
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'phi': 'u^2+u+5/2', 'u*': -.5, 'x*': XSTAR.tolist(), 'nu': 1.5})
