"""Planar poses (a) composition in the two orders, (b) the coordinate change T_AB."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 62
fig, ax = canvas(W, H)
def R(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
def frame(O, ang, c, s, L1=.55, L2=.34):
    Rm = R(ang)
    o = O
    arrow(ax, to(o, s), to(o+L1*Rm[:, 0], s), color=c, lw=1.25, scale=6.5, zorder=6)
    arrow(ax, to(o, s), to(o+L2*Rm[:, 1], s), color=c, lw=1.25, scale=6.5, zorder=6)
    dot(ax, to(o, s), c, size=1.2, zorder=7)
to = lambda q, s: np.array([s[0]+s[2]*q[0], s[1]+s[2]*q[1]])
# (a) composition
sa = (26, 13, 14.5)
frame(np.array([0.0, 0]), 0, MUTED, sa)
frame(np.array([1.0, 0]), np.pi/2, BLUE, sa)
frame(np.array([0.0, 2]), np.pi, RED, sa)
frame(np.array([0.0, 0]), np.pi, GREEN, sa)
label(ax, to((.3, -.24), sa), r'$I$', 7.5, MUTED)
label(ax, to((1.38, .34), sa), r'$T_1$', color=BLUE)
label(ax, to((.58, 2.12), sa), r'$T_2T_1$', color=RED)
label(ax, to((-.72, -.27), sa), r'$T_1T_2$', color=GREEN)
# (b) coordinate change
sb = (72, 12, 11.5)
frame(np.array([0.0, 0]), 0, BLUE, sb, L1=1.25, L2=1.25)
frame(np.array([2.0, 1]), np.pi/2, GREEN, sb, L1=.82, L2=.82)
x = np.array([2.0, 2])
ax.plot(*zip(to((0, 0), sb), to(x, sb)), color=BLUE, lw=.6, ls=(0, (3, 2)), zorder=3)
dot(ax, to(x, sb), INK, zorder=8)
arrow(ax, to(x, sb), to(x+[0, .8], sb), color=RED, lw=1.2, scale=6.5, zorder=7)
label(ax, to(x, sb)+[-2.4, 2.4], '$x$', halo=True)
label(ax, to(x+[0, .84], sb)+[2.8, .7], '$d$', color=RED, halo=True)
label(ax, to((0, 0), sb)+[-3.1, -1.4], '$A$', color=BLUE)
label(ax, to((2, 1), sb)+[3.4, -1.5], '$B$', color=GREEN)
label(ax, to((2, 1), sb)+[-7.6, -3.3], r'$t_{AB}$', 7.5, MUTED, halo=True)
ax.plot(*zip(to((0, 0), sb), to((2, 1), sb)), color=MUTED, lw=.75, zorder=2)
panel_tag(ax, sa[0]+7, 1.7, '(a)'); panel_tag(ax, sb[0]+13, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'T1:(90deg,(1,0)),T2:(90deg,(0,1)); T2T1:(180deg,(0,2)); T1T2:(180deg,0); T_AB:(90deg,(2,1)); x_B=(1,0)->x_A=(2,2); d_B=(1,0)->d_A=(0,1)'})
