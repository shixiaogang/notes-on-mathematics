"""Graph distance: chain s_k along a curve (proof), a gap in the sample on the circle, a short circuit between spiral layers."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 50
fig, ax = canvas(W, H)
# (a) sample chain near gamma(t_k)
g = lambda t: np.stack([t, .35*np.sin(1.3*t)+.08*t], -1)
ts = np.linspace(0, 3.6, 361)
u = 9.6; o = np.array([3.5, 28])
ax.plot(*(o+u*g(ts)).T, color=BLUE, lw=1.4, zorder=3)
tk = np.array([0, .9, 1.8, 2.7, 3.6])
offs = np.array([[0, 0], [.12, -.3], [-.22, .28], [.2, .3], [0, 0]])
gk = g(tk); sk = gk+offs
for a, b in zip(sk[:-1], sk[1:]):
    ax.plot(*zip(o+u*a, o+u*b), color=GREEN, lw=1.1, zorder=4)
for a, b in zip(gk, sk):
    if np.linalg.norm(a-b) > 0:
        ax.plot(*zip(o+u*a, o+u*b), color=RED, lw=.8, ls=(0, (1.6, 1.4)), zorder=4)
for k, (a, b) in enumerate(zip(gk, sk)):
    dot(ax, o+u*a, BLUE, size=.9, hollow=True, zorder=6)
    dot(ax, o+u*b, INK, size=.95, zorder=7)
label(ax, o+u*sk[0]+(-.8, 3), r'$\mathbf{p}$', 8); label(ax, o+u*sk[-1]+(.6, 3), r'$\mathbf{q}$', 8)
label(ax, o+u*sk[2]+(0, 3), r'$\mathbf{s}_2$', 7.5)
label(ax, o+u*gk[1]+(-.6, 3.2), r'$\gamma(t_1)$', 7.5, BLUE)
label(ax, o+u*(gk[3]+sk[3])/2+(4.5, .4), r'$\leq\delta$', 7.5, RED)
panel_tag(ax, o[0]+u*1.8, 1.4, '(a)')
# (b) unit circle with samples every 18 degrees except an arc gap of 90 degrees centred at the top.
u = 12.5; o = np.array([62.5, 27])
th = np.linspace(0, 2*np.pi, 721)
ax.plot(o[0]+u*np.cos(th), o[1]+u*np.sin(th), color=BLUE, lw=1.4, zorder=2)
gap = np.pi/2
angs = np.arange(np.pi/2+gap/2, np.pi/2+2*np.pi-gap/2+1e-9, np.pi/10)
pts = np.stack([np.cos(angs), np.sin(angs)], 1)
ax.plot(*(o+u*pts).T, color=GREEN, lw=1.1, zorder=3)
for p in pts:
    dot(ax, o+u*p, INK, size=.95, zorder=5)
a0 = o+u*pts[0]; a1 = o+u*pts[-1]
ax.plot(*zip(a0, a1), color=RED, lw=.95, ls=(0, (2.2, 1.8)), zorder=4)
label(ax, o+(0, u*1.16), r'$\alpha$', 7.5, MUTED)
panel_tag(ax, o[0], 1.4, '(b)')
# (c) Archimedean spiral rho(t)=b0 + a t; a short edge across two layers.
o = np.array([96, 27]); u = 2.0
tt = np.linspace(0, 4.6*np.pi, 1401)
A = .46
rho = 1.0+A*tt
c = np.stack([rho*np.cos(tt), rho*np.sin(tt)], 1)
ax.plot(*(o+u*c).T, color=BLUE, lw=1.3, zorder=2)
t1 = 2.6*np.pi; t2 = t1+2*np.pi
p1 = c[np.argmin(np.abs(tt-t1))]; p2 = c[np.argmin(np.abs(tt-t2))]
idx = (tt >= t1) & (tt <= t2)
ax.plot(*(o+u*c[idx]).T, color=GREEN, lw=1.5, zorder=3)
ax.plot(*zip(o+u*p1, o+u*p2), color=RED, lw=1.3, zorder=4)
dot(ax, o+u*p1, INK, size=1.0, zorder=5); dot(ax, o+u*p2, INK, size=1.0, zorder=5)
panel_tag(ax, o[0], 1.4, '(c)')
save(fig, OUT, 'figure', {'formula': 'curve (t, .35 sin 1.3t+.08t); unit circle 18-degree samples with 90-degree gap; spiral rho=1+.46t'})
