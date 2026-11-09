"""Level set of Phi=|y|^2: at p the gradient 2p, tangent plane = ker dPhi_p, and the planar section."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 50
fig, ax = canvas(W, H)
view = View(72, 20)
pl = Placed(view, 24, 23, 18)
sphere_disc(ax, pl)
for lat in (-30, 0, 30, 60):
    sphere_curve(ax, pl, parallel(np.radians(lat)), MUTED, lw=.4, hidden=False)
p = np.array([0, .6, .8]); e1 = np.array([1.0, 0, 0]); e2 = np.array([0, .8, -.6])
a, b = .55, .44
corners = np.array([p+a*e1+b*e2, p+a*e1-b*e2, p-a*e1-b*e2, p-a*e1+b*e2])
ax.add_patch(Polygon(pl(corners), fc=YELLOW_FILL, ec=YELLOW, lw=1.1, zorder=4))
P = pl(p)
k = 1.0
arrow(ax, P, pl(p+.52*p), color=RED, lw=1.5, scale=7.5, zorder=8)
arrow(ax, P, pl(p+2.4*np.array([.2, 0, 0])), color=GREEN, lw=1.5, scale=7.5, zorder=8)
dot(ax, P, INK, zorder=9)
label(ax, P+[-3, -2.8], '$p$', halo=True)
label(ax, pl(p+.52*p)+[-5.5, 1.5], r'$\nabla\Phi$', color=RED, halo=True)
label(ax, pl(p+2.4*np.array([.2, 0, 0]))+[-2.8, 1.0], '$v$', color=GREEN, halo=True)
label(ax, pl(corners[0])+[11.5, -3.2], r'$\ker\,\mathrm{d}\Phi_p$', 7.5, YELLOW, halo=True)
panel_tag(ax, 24, 1.6, '(a)')
# (b) planar section y1=0
c = np.array([84., 21.]); u = 15.
th = np.linspace(0, 2*np.pi, 721)
for rr, lw, col in ((.7, .55, MUTED), (1.3, .55, MUTED), (1.0, 1.3, BLUE)):
    ax.plot(c[0]+u*rr*np.cos(th), c[1]+u*rr*np.sin(th), color=col, lw=lw, zorder=2)
pp = np.array([.6, .8]); tan = np.array([.8, -.6])
A = c+u*pp
ax.plot([A[0]-u*.62*tan[0], A[0]+u*.62*tan[0]], [A[1]-u*.62*tan[1], A[1]+u*.62*tan[1]], color=YELLOW, lw=1.3, zorder=3)
arrow(ax, A, A+u*.42*pp, color=RED, lw=1.5, scale=7.5, zorder=8)
dot(ax, A, INK, zorder=9)
label(ax, A+[-3, -2.2], '$p$', 7.5, halo=True)
label(ax, A+u*.42*pp+[3.2, 1.8], r'$\nabla\Phi$', color=RED, halo=True)
label(ax, c+u*np.array([-.9, 1.08]), r'$c=1.69$', 7.5, MUTED, halo=True)
label(ax, c+u*np.array([.0, .42]), r'$c=0.49$', 7.5, MUTED)
label(ax, c+u*np.array([.0, -.82]), r'$c=1$', 7.5, BLUE)
panel_tag(ax, c[0], 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'Phi(y)=|y|^2, p=(0,.6,.8), grad=2p (drawn at .26 of its length), v=(.2,0,0) drawn 2.4x; (b) section y1=0 with levels 0.49,1,1.69'})
