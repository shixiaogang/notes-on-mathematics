"""The three instantaneous rotation axes of Rz(a)Ry(b)Rx(g) in general position and at b=pi/2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 64
fig, ax = canvas(W, H)
view = View(32, 22)
pa, pb = Placed(view, 28, 34, 19), Placed(view, 84, 34, 19)
def Rz(t): return np.array([[np.cos(t), -np.sin(t), 0], [np.sin(t), np.cos(t), 0], [0, 0, 1]])
def Ry(t): return np.array([[np.cos(t), 0, np.sin(t)], [0, 1, 0], [-np.sin(t), 0, np.cos(t)]])
e1, e2, e3 = np.eye(3)
def ring(place, axis, r, c):
    axis = axis/np.linalg.norm(axis)
    a = np.cross(axis, [.31, .47, .83]); a /= np.linalg.norm(a); b = np.cross(axis, a)
    t = np.linspace(0, 2*np.pi, 361)
    pts = r*(np.cos(t)[:, None]*a+np.sin(t)[:, None]*b)
    ax.plot(*place(pts).T, color=c, lw=.85, zorder=3)
def draw(pl, beta, alpha=np.radians(20)):
    a1, a2, a3 = e3, Rz(alpha)@e2, Rz(alpha)@Ry(beta)@e1
    O = 0*e3
    for a, r, c, s in ((a1, .92, BLUE, r'$a_\alpha$'), (a2, 1.06, GREEN, r'$a_\beta$'), (a3, 1.2, RED, r'$a_\gamma$')):
        ring(pl, a, r, c)
        arrow(ax, pl(O), pl(1.3*a), color=c, lw=1.3, scale=7, zorder=7)
    dot(ax, pl(O), INK, size=1.1, zorder=8)
    return a1, a2, a3
a1, a2, a3 = draw(pa, np.radians(35))
L = lambda pl, P, d, t, c: label(ax, pl(P)+np.array(d), t, color=c, halo=True)
L(pa, 1.3*a1, (3.6, .6), r'$a_\alpha$', BLUE)
L(pa, 1.3*a2, (2.2, 2.1), r'$a_\beta$', GREEN)
L(pa, 1.3*a3, (3.2, -1.8), r'$a_\gamma$', RED)
a1, a2, a3 = draw(pb, np.pi/2)
L(pb, 1.3*a1, (3.6, .6), r'$a_\alpha$', BLUE)
L(pb, 1.3*a2, (2.2, 2.1), r'$a_\beta$', GREEN)
L(pb, 1.3*a3, (-3.8, -.4), r'$a_\gamma$', RED)
panel_tag(ax, 28, 1.7, '(a)'); panel_tag(ax, 84, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'a_alpha=e3, a_beta=Rz(a)e2, a_gamma=Rz(a)Ry(b)e1; a=20deg; b=35deg and 90deg; det[a_alpha,a_beta,a_gamma]=-cos b'})
