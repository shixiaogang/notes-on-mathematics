"""Euler polygons (I+J/n)^n for theta=1 approaching exp(J) on the circle."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 80, 62
fig, ax = canvas(W, H)
ox, oy, s = 14, 11, 42
t = np.linspace(0, 1.12, 200)
ax.plot(ox+s*np.cos(t), oy+s*np.sin(t), color=BLUE, lw=1.4, zorder=3)
arrow(ax, (ox-3, oy), (ox+s*1.32, oy), color=MUTED, lw=.7, scale=5)
arrow(ax, (ox, oy-3), (ox, oy+s*1.2), color=MUTED, lw=.7, scale=5)
label(ax, (ox+s*1.33, oy-2.6), '$I$', 7.5, MUTED); label(ax, (ox-2.5, oy+s*1.17), '$J$', 7.5, MUTED)
COL = {2: GREEN, 4: YELLOW, 8: RED}
for n, c in COL.items():
    z = (1+1j/n)**np.arange(n+1)
    ax.plot(ox+s*z.real, oy+s*z.imag, color=c, lw=1.0, marker='o', ms=2.6, zorder=4)
    end = z[-1]
    off = {2: (6.4, 1.0), 4: (0, 3.3), 8: (-6.8, 3.4)}[n]
    label(ax, (ox+s*end.real+off[0], oy+s*end.imag+off[1]), f'$n={n}$', 7.5, c, halo=True)
E = (ox+s*np.cos(1), oy+s*np.sin(1))
dot(ax, E, BLUE, size=2.0, zorder=8)
label(ax, (E[0]-3.6, E[1]-5.2), r'$\exp(J)$', color=BLUE, halo=True)
dot(ax, (ox+s, oy), INK, zorder=8); label(ax, (ox+s+1.6, oy-3.0), '$I$', halo=True)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': '(1+i/n)^k, k=0..n, n=2,4,8; arc cos t + i sin t; exp(J)=cos 1 I + sin 1 J'})
