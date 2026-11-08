"""Orbits of SO(2) on the plane and their quotient half-line; an irrational rotation orbit."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 44
fig, ax = canvas(W, H)
t = np.linspace(0, 2*np.pi, 361)
cx, cy, s = 18, 24, 15
RAD = (0.35, .68, 1.0)
COL = (BLUE, GREEN, PURPLE)
for r, c in zip(RAD, COL):
    ax.plot(cx+s*r*np.cos(t), cy+s*r*np.sin(t), color=c, lw=1.2, zorder=3)
dot(ax, (cx, cy), RED, zorder=8)
# (b) quotient half-line
x0, y0, L = 44, 24, 24
arrow(ax, (x0, y0), (x0+L+3, y0), color=STROKE, lw=.95, scale=6)
dot(ax, (x0, y0), RED, zorder=8)
for r, c in zip(RAD, COL):
    dot(ax, (x0+L*r, y0), c, zorder=8)
label(ax, (x0, y0-3.2), '$0$', 7.5, RED)
label(ax, (x0+L+3, y0-3.2), '$r$', 7.5, MUTED)
# (c) irrational orbit
cx3, s3 = 91, 15
alpha = (np.sqrt(5)-1)/2
ax.plot(cx3+s3*np.cos(t), cy+s3*np.sin(t), color=MUTED, lw=.7, zorder=2)
ang = 2*np.pi*alpha*np.arange(0, 90)
ax.plot(cx3+s3*np.cos(ang[8:]), cy+s3*np.sin(ang[8:]), 'o', ms=2.1, mfc=BLUE, mec=BLUE, mew=0, zorder=4)
ax.plot(cx3+s3*np.cos(ang[:8]), cy+s3*np.sin(ang[:8]), 'o', ms=3.8, mfc=RED, mec=RED, mew=0, zorder=5)
for k in (0, 1, 2):
    a = ang[k]
    label(ax, (cx3+(s3+3.2)*np.cos(a), cy+(s3+3.2)*np.sin(a)), f'${k}$', 7.5, RED, halo=True)
panel_tag(ax, cx, 1.7, '(a)'); panel_tag(ax, x0+L/2, 1.7, '(b)'); panel_tag(ax, cx3, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'circles r=.35,.68,1 -> points of [0,inf); irrational rotation angle 2 pi alpha k, alpha=(sqrt5-1)/2, k=0..89'})
