from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Stationarity is weak: (a) f1=x1^2, f2=x2 at 0. (b) f1=f2=-x^2 at 0.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .08, .985, .985, .21, .28)
ax = axes[0]; setup(ax, (-1.2, 1.2), (-1.2, 1.2), [-1, 0, 1], [-1, 0, 1], '$x_1$', '$x_2$', equal=True)
for c in (.25, .75): ax.plot([c, c], [-1.2, 1.2], color=BLUE, lw=.8); ax.plot([-c, -c], [-1.2, 1.2], color=BLUE, lw=.8)
for c in (-.8, -.4, 0, .4, .8): ax.plot([-1.2, 1.2], [c, c], color=BLUE, lw=.8, ls=(0, (3, 2)))
arrow(ax, (0, 0), (0, -.8), GREEN, lw=1.5); hollow(ax, (0, 0), GREEN, ms=5.2); dot(ax, (0, -.8), RED)
arrow(ax, (0, 0), (0, .55), BLUE); ax.text(.07, .42, r'$g_2$', color=BLUE); ax.text(.08, .06, '$0$', color=INK); 
ax = axes[1]; setup(ax, (-1.3, 1.3), (-1.8, .35), [-1, 0, 1], [-1, 0], '$x$', '$f_1=f_2$')
x = np.linspace(-1.3, 1.3, 300); ax.plot(x, -x**2, color=BLUE, lw=1.2); hollow(ax, (0, 0), GREEN, ms=5.2); dot(ax, (1, -1), GREEN, ms=4.6); dot(ax, (-1, -1), GREEN, ms=4.6)
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'f1=x1^2, f2=x2', 'b': 'f1=f2=-x^2'})
