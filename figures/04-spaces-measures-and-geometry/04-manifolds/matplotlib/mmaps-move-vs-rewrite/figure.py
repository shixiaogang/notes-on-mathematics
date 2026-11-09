"""Chart change keeps the point; a map moves it. Tangent vector records in red."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 44
fig, ax = canvas(W, H)
def planes(c, sc, r, xn, yn):
    cx, cy = c
    arrow(ax, (cx-sc*r, cy), (cx+sc*r, cy), color=MUTED, lw=.75, scale=5.5)
    arrow(ax, (cx, cy-sc*r), (cx, cy+sc*r), color=MUTED, lw=.75, scale=5.5)
    label(ax, (cx+sc*r-.2, cy+2.3), xn, 7.5, MUTED); label(ax, (cx+2.8, cy+sc*r-.3), yn, 7.5, MUTED)
    return lambda u: (cx+sc*u[0], cy+sc*u[1])
s1, s2, r1 = 2.6, 20, 3.95
A = planes((12, 22), s1, r1, '$u_1$', '$u_2$'); B = planes((42, 22), s2, .5, '$w_1$', '$w_2$')
C = planes((70, 22), s1, r1, '$u_1$', '$u_2$'); D = planes((100, 22), s1, r1, '$u_1$', '$u_2$')
def tang(F, u, v, lab, off, labv, offv):
    P = np.array(F(u)); Q = np.array(F((u[0]+v[0], u[1]+v[1])))
    arrow(ax, P, Q, color=RED, lw=1.3, scale=7, zorder=7); dot(ax, P, INK)
    label(ax, P+off, lab, 7.5, halo=True); label(ax, Q+offv, labv, 7.5, RED, halo=True)
tang(A, (0, 3), (1, 0), '$(0,3)$', [-6.0, 1.4], '$(1,0)$', [2.6, -2.6])
tang(B, (0, 1/3), (1/9, 0), r'$(0,\frac{1}{3})$', [-5.4, 2.0], r'$(\frac{1}{9},0)$', [3.5, -2.9])
tang(C, (0, 3), (1, 0), '$(0,3)$', [-6.0, 1.4], '$(1,0)$', [2.6, -2.6])
tang(D, (-3, 0), (0, 1), '$(-3,0)$', [-1.0, -2.9], '$(0,1)$', [1.0, 2.3])
arrow(ax, (24, 34), (31, 34), color=INK); label(ax, (27.5, 36.8), r'$\tau$')
arrow(ax, (82, 34), (89, 34), color=INK); label(ax, (85.5, 37), r'$\hat R_\theta$')
panel_tag(ax, 27, 4, '(a)'); panel_tag(ax, 85, 4, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'tau(u)=u/|u|^2 with J_tau(0,3)=diag(1/9,-1/9); hat R_theta=R(pi/2), R(pi/2)(0,3)=(-3,0), R(pi/2)(1,0)=(0,1)'})
