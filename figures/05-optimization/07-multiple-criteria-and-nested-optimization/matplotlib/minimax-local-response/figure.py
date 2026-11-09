from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# f(x,y)=x^2/2+xy+y^2-y^4/4 on Y=[-2,2]: local versus global response.
f = lambda x, y: .5*x**2+x*y+y**2-.25*y**4
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panels(fig, .075, .985, .975, .225, .28)
y = np.linspace(-2, 2, 800); ax = axes[0]; setup(ax, (-2, 2), (-2, 3.6), (-2, -1, 0, 1, 2), (-2, 0, 2), xl='$y$', yl='$f(1,y)$')
ax.plot(y, f(1, y), color=BLUE, lw=1.4)
gr = (1+5**.5)/2
dot(ax, (gr, f(1, gr))); dot(ax, (-1, f(1, -1)), YELLOW); hollow(ax, (1-gr, f(1, 1-gr)))
ax = axes[1]; x = np.linspace(-2, 2, 500); Yg = np.linspace(-2, 2, 4001)
phi = np.array([f(v, Yg).max() for v in x]); setup(ax, (-2, 2), (-1, 7), (-2, -1, 0, 1, 2), (0, 2, 4, 6), yl='值')
ax.plot(x, phi, color=BLUE, lw=1.5)
yb = np.linspace(-2, -np.sqrt(2/3), 500); xb = yb**3-2*yb; keep = xb >= -2
ax.plot(xb[keep], f(xb[keep], yb[keep]), color=YELLOW, lw=1.6)
dot(ax, (0, 1)); dot(ax, (1, .25), YELLOW); hollow(ax, (1, f(1, gr)), BLUE)
ax.plot([1, 1], [.25, f(1, gr)], color=RED, lw=1.0, ls=(0, (3, 2)))
ax.text(1.12, 1.5, '差 2.77', color=INK, fontsize=7.5)
ax.text(-1.2, 3.75, r'$\phi$', color=BLUE)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': 'x^2/2+xy+y^2-y^4/4', 'Y': '[-2,2]'})
print(f(1, gr), f(1, -1), f(1, 1-gr), f(1, gr)-f(1, -1))
