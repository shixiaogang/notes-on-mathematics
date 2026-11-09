from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Linearization at 0 of g(x)=x and g(x)=x^2: tangent line sets F; true feasible set is T.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .08, .985, .985, .27, .22)
xs = np.linspace(-1.2, 1.2, 300)
for ax, g in zip(axes, [xs, xs**2]):
    ax.axhline(0, color=MUTED, lw=.6, zorder=1)
    ax.plot(xs, g, color=EDGE, lw=1.4, zorder=3)
    setup(ax, (-1.2, 1.2), (-.9, 1.45), [-1, 0, 1], [0, 1], xl='$x$', yl='$g(x)$', equal=False)
a, b = axes
a.plot([-1.2, 0], [-.72, -.72], color=BLUE, lw=3, solid_capstyle='butt'); a.plot([-1.2, 0], [-.55, -.55], color=YELLOW, lw=2.2, solid_capstyle='butt')
a.text(.1, -.58, '线性化：d≤0', color=INK, fontsize=7.5); a.text(-.55, -.86, '', fontsize=7.5)
a.text(.1, -.8, '真实可行：x≤0', color=INK, fontsize=7.5)
dot(a, (0, 0), INK, ms=4.5)
b.plot(xs, 0*xs, color=YELLOW, lw=2.0, zorder=2); b.plot([-1.2, 1.2], [-.55, -.55], color=YELLOW, lw=2.2, solid_capstyle='butt')
dot(b, (0, -.72), BLUE, ms=5)
b.text(0, -.44, '线性化：所有 d', color=INK, fontsize=7.5, ha='center'); b.text(.1, -.8, '真实可行：只有 0', color=INK, fontsize=7.5)
dot(b, (0, 0), INK, ms=4.5)
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'g(x)=x', 'b': 'g(x)=x^2, g prime 0 =0'})
