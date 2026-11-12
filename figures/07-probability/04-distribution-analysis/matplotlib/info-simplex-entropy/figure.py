from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# Entropy (nat) of three-point distributions (p1,p2,p3) drawn in the simplex
# (barycentric coordinates). Level lines at 0.3,0.6,0.9; max ln 3 = 1.0986 at the centre (red).
# Green point: (0.7,0.2,0.1) with H = 0.8018 nat.
fig, ax = figure(width_mm=70, height_mm=60)
fig.set_layout_engine(None); fig.subplots_adjust(left=.03, right=.97, top=.95, bottom=.05)
V = np.array([[0, 0], [1, 0], [.5, math.sqrt(3)/2]])
n = 400
xs = np.linspace(0, 1, n); ys = np.linspace(0, math.sqrt(3)/2, n)
X, Y = np.meshgrid(xs, ys)
# barycentric
p3 = Y/(math.sqrt(3)/2); p2 = X - .5*p3; p1 = 1 - p2 - p3
inside = (p1 >= -1e-9) & (p2 >= -1e-9) & (p3 >= -1e-9)
def ent(*ps):
    out = np.zeros_like(ps[0])
    for q in ps:
        qq = np.clip(q, 1e-300, 1); out -= np.where(q > 0, qq*np.log(qq), 0)
    return out
Hm = np.where(inside, ent(p1, p2, p3), np.nan)
cs = ax.contour(X, Y, Hm, levels=[.3, .6, .9], colors=[BLUE], linewidths=.85)
ax.clabel(cs, fmt='%.1f', fontsize=7)
ax.plot(*np.vstack([V, V[:1]]).T, color=STROKE, lw=.95)
c = V.mean(0); dot(ax, *c)
lab(ax, c[0]+.03, c[1]-.05, r'$\ln 3$', RED)
q = np.array([.7, .2, .1]); pt = q @ V; dot(ax, *pt, color=GREEN)
ax.plot([pt[0], pt[0]], [pt[1], -.035], color=GREEN, lw=.6); lab(ax, pt[0], -.075, '$(0.7,0.2,0.1)$', GREEN, ha='center')
for v, s, off in zip(V, ('$p_1=1$', '$p_2=1$', '$p_3=1$'), ((-.12, -.02), (.02, -.02), (.04, -.02))):
    lab(ax, v[0]+off[0], v[1]+off[1], s)
ax.set_xlim(-.14, 1.14); ax.set_ylim(-.11, .92); ax.set_aspect('equal'); ax.axis('off')
save(fig, HERE, 'figure', {'H(0.7,0.2,0.1)': H(q), 'ln3': math.log(3)})
