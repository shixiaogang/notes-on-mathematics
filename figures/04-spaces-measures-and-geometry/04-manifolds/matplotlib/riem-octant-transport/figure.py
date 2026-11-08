"""Parallel transport of e_1 around the octant N-A-B-N of S^2; V(t) is the exact solution listed in the text."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 76, 54
fig, ax = canvas(W, H)
pl = Placed(View(42, 28), 38, 27, 22.5)
sphere_disc(ax, pl, fill='white')
for lat in (0,):
    pass
tt = np.linspace(0, np.pi/2, 121)
arc1 = np.c_[np.sin(tt), 0*tt, np.cos(tt)]
arc2 = np.c_[np.cos(tt), np.sin(tt), 0*tt]
arc3 = np.c_[0*tt, np.cos(tt), np.sin(tt)]
ax.add_patch(Polygon(np.r_[pl(arc1), pl(arc2), pl(arc3)], fc=YELLOW_FILL, ec='none', zorder=1.5))
for a in (arc1, arc2, arc3):
    ax.plot(*pl(a).T, color=BLUE, lw=1.35, zorder=3)
def seg(g, V, ts, col=RED):
    for t in ts:
        p = g(t); v = V(t)
        arrow(ax, pl(p), pl(p+.36*v), color=col, lw=1.2, scale=6.5)
seg(lambda t: np.array([np.sin(t), 0, np.cos(t)]), lambda t: np.array([np.cos(t), 0, -np.sin(t)]), [0, np.pi/6, np.pi/3])
seg(lambda t: np.array([np.cos(t), np.sin(t), 0]), lambda t: np.array([0, 0, -1.0]), [0, np.pi/4])
seg(lambda t: np.array([0, np.cos(t), np.sin(t)]), lambda t: np.array([0, np.sin(t), -np.cos(t)]), [0, np.pi/4])
N = np.array([0, 0, 1.0]); A = np.array([1.0, 0, 0]); B = np.array([0, 1.0, 0])
arrow(ax, pl(N), pl(N+.36*B), color=GREEN, lw=1.5, scale=7.5)
for p in (N, A, B):
    dot(ax, pl(p), INK)
label(ax, pl(N)+[-1.6, 3.2], '$N$', halo=True)
label(ax, pl(A)+[-2.0, -3.0], '$A$', halo=True)
label(ax, pl(B)+[3.0, -2.6], '$B$', halo=True)
label(ax, pl(N+.36*np.array([1.0, 0, 0]))+[-2.4, 2.0], r'$\bm{e}_1$'.replace(r'\bm{e}', 'e'), color=RED, halo=True)
label(ax, pl(N+.36*B)+[3.0, 1.8], '$e_2$', color=GREEN, halo=True)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'V on N->A: (cos t,0,-sin t); A->B: (0,0,-1); B->N: (0,sin t,-cos t)'})
