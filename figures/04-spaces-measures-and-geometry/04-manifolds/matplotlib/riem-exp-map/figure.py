"""The exponential map at N on the unit sphere: rays and circles of T_NS^2 and their images, and the radial/circle splitting of a velocity."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 54
fig, ax = canvas(W, H)
c = np.array([20.5, 30.5]); s = 5.9
tt = np.linspace(0, 2*np.pi, 361)
rs = [np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
for r in rs[:3]:
    ax.plot(c[0]+s*r*np.cos(tt), c[1]+s*r*np.sin(tt), color=GREEN, lw=.9, zorder=2)
ax.plot(c[0]+s*np.pi*np.cos(tt), c[1]+s*np.pi*np.sin(tt), color=PURPLE, lw=1.3, zorder=2)
for a in np.arange(8)*np.pi/4:
    ax.plot([c[0], c[0]+s*np.pi*np.cos(a)], [c[1], c[1]+s*np.pi*np.sin(a)], color=BLUE, lw=.9, zorder=2)
V = c+s*np.pi/2*np.array([np.cos(np.pi/4), np.sin(np.pi/4)])
arrow(ax, c, V, color=RED, lw=1.5, scale=7.5)
dot(ax, c, INK); dot(ax, V, RED, size=1.0)
label(ax, V+[3.4, .5], '$v$', color=RED, halo=True)
label(ax, c+[-2.6, -2.4], '$0$', 7.5, halo=True)
label(ax, c+[0, -s*np.pi-3], r'$\|v\|=\pi$', 7.5, PURPLE, halo=False)
panel_tag(ax, c[0], 3, '(a)')
pl = Placed(View(35, 30), 58.5, 30, 19.0)
sphere_disc(ax, pl, fill='white')
for r in rs[:3]:
    sphere_curve(ax, pl, parallel(np.pi/2-r), GREEN, lw=.9, hidden=False)
for a in np.arange(8)*np.pi/4:
    tt1 = np.linspace(0, np.pi, 121)
    pts = np.c_[np.sin(tt1)*np.cos(a), np.sin(tt1)*np.sin(a), np.cos(tt1)]
    sphere_curve(ax, pl, pts, BLUE, lw=.9, hidden=False)
a = np.pi/4; tt1 = np.linspace(0, np.pi/2, 91)
ax.plot(*pl(np.c_[np.sin(tt1)*np.cos(a), np.sin(tt1)*np.sin(a), np.cos(tt1)]).T, color=RED, lw=1.5, zorder=4)
N = np.array([0, 0, 1.0]); Q = np.array([np.cos(a), np.sin(a), 0])
dot(ax, pl(N), INK); dot(ax, pl(Q), RED, size=1.0)
label(ax, pl(N)+[-2.4, 3.0], '$N$', halo=True)
label(ax, pl(Q)+[3.3, -2.6], r'$\exp_N(v)$', 7.5, RED, halo=True)
S = np.array([0, 0, -1.0]); dot(ax, pl(S), PURPLE, size=1.0, hollow=True)
label(ax, pl(S)+[4.4, -1.0], '$-N$', 7.5, PURPLE, halo=True)
panel_tag(ax, 58.5, 3, '(b)')
o = np.array([81.0, 13.0]); u = 22.0
b = np.linspace(.35, 1.25, 80)
for rho in (.5, .85, 1.15):
    ax.plot(o[0]+u*rho*np.cos(b), o[1]+u*rho*np.sin(b), color=GREEN, lw=.95, zorder=2)
for a in (.45, .78, 1.15):
    ax.plot([o[0], o[0]+u*1.28*np.cos(a)], [o[1], o[1]+u*1.28*np.sin(a)], color=BLUE, lw=.9, zorder=2)
dot(ax, o, INK); label(ax, o+[-2.4, -1.8], '$p$', halo=True)
rho0 = .85; a0 = .78
P = o+u*rho0*np.array([np.cos(a0), np.sin(a0)])
er = np.array([np.cos(a0), np.sin(a0)]); et = np.array([-np.sin(a0), np.cos(a0)])
t = np.linspace(-.28, .22, 60)
cur = np.array([o+u*(rho0+.9*x)*np.array([np.cos(a0+.7*x), np.sin(a0+.7*x)]) for x in t])
ax.plot(*cur.T, color=RED, lw=1.35, zorder=3)
i0 = np.argmin(abs(t))
v = cur[i0+1]-cur[i0-1]; v = v/np.linalg.norm(v)
Vr = (v@er)*er; Vt = (v@et)*et
scale = 10
arrow(ax, P, P+scale*v, color=RED, lw=1.4, scale=7)
arrow(ax, P, P+scale*Vr, color=BLUE, lw=1.4, scale=7)
arrow(ax, P, P+scale*Vt, color=GREEN, lw=1.4, scale=7)
ax.plot(*np.array([P+scale*Vr, P+scale*v]).T, color=MUTED, lw=.75, ls=(0, (2.5, 1.8)), zorder=2)
ax.plot(*np.array([P+scale*Vt, P+scale*v]).T, color=MUTED, lw=.75, ls=(0, (2.5, 1.8)), zorder=2)
dot(ax, P, INK)
label(ax, P+scale*v+[2.0, 2.4], r'$\dot\gamma$', color=RED, halo=True)
label(ax, P+scale*Vr+[3.6, -1.4], r'$\dot\rho\,\partial_\rho$', 7.5, BLUE, halo=True)
label(ax, P+scale*Vt+[-3.6, 1.6], '横向', 7.5, GREEN, halo=True)
panel_tag(ax, 92, 3, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'exp_N(r(cos a,sin a)) = (sin r cos a, sin r sin a, cos r)'})
