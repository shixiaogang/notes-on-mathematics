"""Parallel transport around the coordinate square of side s in normal coordinates at N: the arrows for s=0.8 and the rotation angle against s^2 (RK4 on the projection ODE)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 50
fig, ax = canvas(W, H)
def expN(x):
    r = np.linalg.norm(x)
    if r < 1e-12:
        return np.array([0, 0, 1.0])
    return np.array([np.sin(r)*x[0]/r, np.sin(r)*x[1]/r, np.cos(r)])
def corners(s):
    return np.array([[0, 0], [s, 0], [s, s], [0, s], [0, 0]], float)
def transport(s, n=800, keep=None):
    pts = corners(s)
    V = np.array([1.0, 0, 0])
    trace = []
    h = 1.0/n
    def poly(t):
        i = min(int(t*4), 3); f = t*4-i
        return pts[i]*(1-f)+pts[i+1]*f
    def dV(t, V):
        e = 1e-5
        g = expN(poly(t)); dg = (expN(poly(min(t+e, 1)))-expN(poly(max(t-e, 0))))/(min(t+e, 1)-max(t-e, 0))
        return -np.dot(V, dg)*g
    t = 0.0
    for k in range(n):
        if keep and k % (n//keep) == 0:
            trace.append((expN(poly(t)), V.copy()))
        k1 = dV(t, V); k2 = dV(t+h/2, V+h/2*k1); k3 = dV(t+h/2, V+h/2*k2); k4 = dV(t+h, V+h*k3)
        V = V+h/6*(k1+2*k2+2*k3+k4); t += h
    trace.append((expN(poly(1.0)), V.copy()))
    return V, trace
s = .8
pl = Placed(View(25, 58), 25.5, 27.5, 20)
sphere_disc(ax, pl, fill='white')
for r in (np.pi/6, np.pi/3):
    sphere_curve(ax, pl, parallel(np.pi/2-r), GRID, lw=.5, hidden=False, zorder=2)
ts = np.linspace(0, 1, 401)
pts = corners(s)
def poly(t):
    i = min(int(t*4), 3); f = t*4-i
    return pts[i]*(1-f)+pts[i+1]*f
loop = np.array([expN(poly(t)) for t in ts])
ax.add_patch(Polygon(pl(loop), fc=YELLOW_FILL, ec='none', zorder=1.5))
ax.plot(*pl(loop).T, color=BLUE, lw=1.3, zorder=3)
V, tr = transport(s, n=800, keep=12)
for i, (p, v) in enumerate(tr):
    if i == 0 or i == len(tr)-1:
        continue
    arrow(ax, pl(p), pl(p+.3*v), color=RED, lw=1.1, scale=6)
P0, V0 = tr[0]
arrow(ax, pl(P0), pl(P0+.3*V0), color=RED, lw=1.3, scale=6.8)
arrow(ax, pl(P0), pl(P0+.3*V), color=GREEN, lw=1.5, scale=7.5)
dot(ax, pl(P0), INK); label(ax, pl(P0)+[-3.0, 2.0], '$N$', halo=True)
label(ax, pl(P0+.3*V0)+[-1.5, 2.6], '$w$', color=RED, halo=True)
label(ax, pl(P0+.3*V)+[3.4, 1.4], '$P_s w$', 7.5, GREEN, halo=True)
panel_tag(ax, 25.5, 3, '(a)')
ss = np.linspace(.1, 1.1, 11)
ang = []
for q in ss:
    V_, _ = transport(q, n=400)
    ang.append(np.arctan2(V_[1], V_[0]))
ang = np.array(ang)
x0, y0, sx, sy = 66.0, 11.0, 28.0, 24.5
arrow(ax, (x0-1, y0), (x0+1.34*sx, y0), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (x0, y0-1), (x0, y0+1.42*sy), color=MUTED, lw=.75, scale=5.5)
line = np.array([0, 1.25])
ax.plot(x0+sx*line, y0+sy*line, color=BLUE, lw=1.4, zorder=2)
ax.plot(x0+sx*ss**2, y0+sy*ang, 'o', ms=3.2, mfc=RED, mec='white', mew=.5, zorder=4)
for v in (.5, 1.0):
    ax.plot([x0+sx*v]*2, [y0-1, y0], color=MUTED, lw=.8); label(ax, (x0+sx*v, y0-3.1), f'{v:g}', 7.5, MUTED)
    ax.plot([x0-1, x0], [y0+sy*v]*2, color=MUTED, lw=.8); label(ax, (x0-3.4, y0+sy*v), f'{v:g}', 7.5, MUTED)
label(ax, (x0+1.36*sx, y0+2.4), '$s^2$', 7.5, MUTED); label(ax, (x0+5, y0+1.42*sy-.5), '转角', 7.5, MUTED)
panel_tag(ax, x0+.62*sx, 3, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'P_s via RK4 on dV/dt=-<V,gamma_dot>gamma; rotation angle vs s^2; s=0.1..1.1', 'angles': ang.round(4).tolist()})
print(ang.round(4).tolist(), (ang/ss**2).round(3).tolist())
