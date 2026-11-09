"""Parallel transport around the latitude through p=(0,3/5,4/5), and its development on the flat tangent cone (sector angle 8pi/5, radius tan theta0=3/4)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 58
fig, ax = canvas(W, H)
pl = Placed(View(90, 30), 26, 31, 19.5)
sphere_disc(ax, pl, fill='white')
t0 = np.arccos(.8); s0, c0 = .6, .8
def G(t):
    f = np.pi/2+t
    return np.array([s0*np.cos(f), s0*np.sin(f), c0])
def Eth(t):
    f = np.pi/2+t
    return np.array([c0*np.cos(f), c0*np.sin(f), -s0])
def Ephi(t):
    f = np.pi/2+t
    return np.array([-np.sin(f), np.cos(f), 0.0])
def V(t):
    return np.cos(c0*t)*Eth(t)-np.sin(c0*t)*Ephi(t)
tt = np.linspace(0, 2*np.pi, 361)
sphere_curve(ax, pl, np.array([G(t) for t in tt]), BLUE, lw=1.3, hidden=True)
for lat in (0,):
    sphere_curve(ax, pl, parallel(0.0), GRID, lw=.5, hidden=False, zorder=2)
ts = 2*np.pi*np.arange(0, 10)/10
for t in ts:
    p = G(t)
    arrow(ax, pl(p), pl(p+.3*V(t)), color=RED, lw=1.15, scale=6.2)
p = G(0)
arrow(ax, pl(p), pl(p+.3*V(2*np.pi)), color=GREEN, lw=1.5, scale=7.2)
dot(ax, pl(p), INK)
label(ax, pl(p)+[-2.5, 3.0], '$p$', halo=True)
N = np.array([0, 0, 1.0]); dot(ax, pl(N), MUTED, size=.9); label(ax, pl(N)+[0, 2.6], '$N$', 7.5, MUTED, halo=True)
panel_tag(ax, 26, 3, '(a)')
# (b) developed sector; gap of 2pi/5 centred on the upward axis.
O = np.array([84.0, 31.0]); R = 20.5
a0 = np.pi/2+np.pi/5
aa = a0+.8*tt
sect = np.r_[[O], O+R*np.c_[np.cos(aa), np.sin(aa)]]
ax.add_patch(Polygon(sect, fc=YELLOW_FILL, ec=STROKE, lw=.8, zorder=1))
ax.plot(O[0]+R*np.cos(aa), O[1]+R*np.sin(aa), color=BLUE, lw=1.3, zorder=3)
vdir = np.array([np.cos(a0), np.sin(a0)])
for k in range(0, 11):
    t = 2*np.pi*k/10
    a = a0+.8*t
    Pt = O+R*np.array([np.cos(a), np.sin(a)])
    col = GREEN if k == 10 else RED
    arrow(ax, Pt-8.0*vdir*0, Pt+6.2*vdir, color=col, lw=1.5 if k == 10 else 1.15, scale=7.2 if k == 10 else 6.2)
    if k in (0, 10):
        dot(ax, Pt, INK)
        label(ax, Pt+([3.2, .8] if k == 0 else [3.6, 2.8]), '$p$', halo=True)
dot(ax, O, INK, size=.9); label(ax, O+[2.8, -2.2], '$O$', 7.5, MUTED, halo=True)
b = np.linspace(np.pi/2-np.pi/5, np.pi/2+np.pi/5, 40)
ax.plot(O[0]+8*np.cos(b), O[1]+8*np.sin(b), color=MUTED, lw=.8, zorder=4)
label(ax, O+[0, 11.0], r'$2\pi/5$', 7.5, MUTED, halo=True)
panel_tag(ax, O[0], 3, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'a=cos(ct), b=-sin(ct), c=cos(theta0)=4/5; sector angle 2pi c, gap 2pi(1-c)=2pi/5'})
