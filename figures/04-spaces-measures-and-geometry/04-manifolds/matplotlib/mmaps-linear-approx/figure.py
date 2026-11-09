"""A small grid and its image under hat pi(u)=2u/(|u|^2+1) near (0,3), compared with the linear map J."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 46
fig, ax = canvas(W, H)
Pi = lambda u: 2*u/(np.sum(u**2, 1)+1)[:, None]
J = np.diag([.2, -.16]); c = np.array([0, 3.0]); ic = Pi(c[None])[0]
def grid(F, d, color, lw, n=5, ls='-', zo=3):
    ss = np.linspace(-d, d, 101)
    for k in np.linspace(-d, d, n):
        for line in (np.c_[np.full_like(ss, k), ss], np.c_[ss, np.full_like(ss, k)]):
            ax.plot(*F(line).T, color=color, lw=lw, ls=ls, zorder=zo)
s = 15.0; C0 = np.array([19.0, 24.0])
A = lambda d: (C0+s*d)
grid(A, .8, BLUE, .85)
dot(ax, C0, INK); label(ax, C0+[0, -3], '', 7.5)
label(ax, (19, 9.2), r'$(0,3)$', 7.5, halo=True)
ax.plot([19, 19], [11, 23.3], color=MUTED, lw=.5, zorder=2)
def panel(cx, cy, sc, d):
    O = np.array([cx, cy])
    grid(lambda z: O+sc*(Pi(z+c)-ic), d, BLUE, .9)
    grid(lambda z: O+sc*(z@J.T), d, RED, .8, ls=(0, (3, 1.7)), zo=4)
    dot(ax, O, INK, size=1.1)
panel(57, 24, 72, .8)
panel(95, 24, 245, .2)
arrow(ax, (35, 24), (42, 24), color=INK); label(ax, (38.5, 26.8), r'$\hat\pi$')
panel_tag(ax, 19, 1.7, '(a)'); panel_tag(ax, 57, 1.7, '(b)'); panel_tag(ax, 95, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'hat pi(u)=2u/(|u|^2+1), base u=(0,3), J=diag(.2,-.16); half-widths .8 and .2, scales 72 and 245 mm per unit'})
