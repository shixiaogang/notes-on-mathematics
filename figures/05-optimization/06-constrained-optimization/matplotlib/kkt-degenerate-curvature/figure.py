from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Three functions with zero second derivative at 0: x^4 (strict min), x^3 (none), -x^4 (max).
fig, axes = figure(width_mm=112, height_mm=38, ncols=3, sharey=True)
panels(fig, .06, .985, .98, .32, .16)
x = np.linspace(-1.15, 1.15, 300)
for ax, f, s, m in zip(axes, (x**4, x**3, -x**4), ('$f=x^4$', '$f=x^3$', '$f=-x^4$'), (RED, YELLOW, YELLOW)):
    ax.axhline(0, color=MUTED, lw=.6, zorder=1); ax.plot(x, f, color=BLUE, lw=1.4)
    setup(ax, (-1.15, 1.15), (-1.3, 1.3), [-1, 0, 1], [-1, 0, 1], xl='$x$', yl='', equal=False); dot(ax, (0, 0), m)
    ax.text(0, 1.0, s, fontsize=8, color=BLUE, ha='center')
tags(fig, axes, y=.01)
save(fig, HERE, 'figure', {'H': 'second derivative 0 at 0 in all panels'})
