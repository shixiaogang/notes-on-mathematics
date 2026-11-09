from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
fig, ax = figure(width_mm=92, height_mm=54); triangle(ax, labels=False); contours(ax, levels=FS+np.array([.012, .05, .12, .25])); active(ax, V[0], V[1])
a = 1/L
for x, c in ((XS, RED), (np.array([.2, .8, 0.]), GREEN)):
    z = x-a*grad(x); za = z-(z.sum()-1)/3; p = proj(z)[0]; P = bary(x); Z = bary(za); Q = bary(p)
    arrow(ax, P, Z, GREEN, lw=1.2); hollow(ax, Z, GREEN, ms=4); 
    if np.linalg.norm(Q-P) > 1e-3:
        arrow(ax, Z, Q, YELLOW, lw=1.1, ls=(0, (2, 1.4))); dot(ax, Q, GREEN, ms=4.4); dot(ax, P, GREEN, ms=4.4)
    else:
        ax.plot([Z[0], Q[0]], [Z[1], Q[1]], color=YELLOW, lw=1.1, ls=(0, (2, 1.4)))
        dot(ax, P, RED, ms=5.4)
xs = bary(XS); ax.text(xs[0]+.012, xs[1]+.02, '$x^*$', fontsize=8)
ax.text(.8+.0, .022, '$x$', fontsize=8); ax.text(.6125+.005, .03, '$x^{+}$', fontsize=8, ha='center')
ax.text(.53, -.083, '$z$', fontsize=8, va='top', ha='left')
ax.set_xlim(.12, .98); ax.set_ylim(-.11, .28); ax.set_aspect('equal'); ax.axis('off')
save(fig, HERE, 'figure', {'alpha': a, 'x': [.2, .8, 0], 'xstar': [.5, .5, 0]})
