"""O(2) in R^{2x2} written A=uI+vJ+wD+sB: rotations and reflections are unit circles in two orthogonal planes."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 100, 50
fig, ax = canvas(W, H)
def panel(cx, hx, hy, col, base_lab, tip_lab):
    c = np.array([cx, 27.]); u = 15.
    arrow(ax, (cx-20, 27), (cx+21, 27), color=MUTED, lw=.75, scale=5.5)
    arrow(ax, (cx, 27-19.5), (cx, 27+20.5), color=MUTED, lw=.75, scale=5.5)
    label(ax, (cx+21, 29.4), hx, 7.5, MUTED); label(ax, (cx+2.6, 27+20.2), hy, 7.5, MUTED)
    th = np.linspace(0, 2*np.pi, 721)
    ax.plot(cx+u*np.cos(th), 27+u*np.sin(th), color=col, lw=1.3, zorder=3)
    dot(ax, (cx+u, 27), INK, zorder=8)
    return c, u
c, u = panel(25, '$u$', '$v$', BLUE, '', '')
arrow(ax, (25+u, 27), (25+u, 27+9), color=RED, lw=1.5, scale=7.5, zorder=9)
label(ax, (25+u+3.2, 27+9), '$J$', color=RED, halo=True)
label(ax, (25+u-3.2, 27-3), '$I$', 8, halo=True)
arrow(ax, (25+u, 27), (25+u+7, 27), color=YELLOW, lw=1.5, scale=7.5, zorder=9)
label(ax, (25+u+4.6, 27-2.8), '$I$', 7.5, YELLOW, halo=True)
a = np.pi/3
dot(ax, (25+u*np.cos(a), 27+u*np.sin(a)), INK, size=1.2, zorder=8)
label(ax, (25+u*.5-7.5, 27+u*.866+.6), r'$R(\theta)$', 7.5, halo=True)
panel_tag(ax, 25, 1.6, '(a)')
panel(74, '$w$', '$s$', GREEN, '', '')
label(ax, (74+u-3.2, 27-3), '$D$', 8, halo=True)
panel_tag(ax, 74, 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'A=uI+vJ+wD+sB, J=[[0,-1],[1,0]], D=diag(1,-1), B=[[0,1],[1,0]]; rotations u^2+v^2=1,w=s=0; reflections w^2+s^2=1,u=v=0'})
