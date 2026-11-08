"""Finite atlas on the circle, a partition of unity and the two localised pieces read in their own charts."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 44
fig, ax = canvas(W, H)
eta = lambda t: np.where(t > 0, np.exp(-1/np.maximum(t, 1e-12)), 0.)
S = lambda t: eta(t)/(eta(t)+eta(1-t))
def psi1(th):
    return S((5*np.pi/6-np.abs(th))/(2*np.pi/3))
u = lambda th: 1+.5*np.cos(th)
# (a) circle
c = np.array([17., 24.]); R = 13.
th = np.linspace(-np.pi, np.pi, 721)
ax.plot(c[0]+R*np.cos(th), c[1]+R*np.sin(th), color=MUTED, lw=.7, zorder=1)
a1 = np.linspace(-5*np.pi/6, 5*np.pi/6, 361)
ax.plot(c[0]+(R+1.3)*np.cos(a1), c[1]+(R+1.3)*np.sin(a1), color=BLUE, lw=1.4, zorder=3)
a2 = np.linspace(np.pi/6, 11*np.pi/6, 361)
ax.plot(c[0]+(R-1.3)*np.cos(a2), c[1]+(R-1.3)*np.sin(a2), color=GREEN, lw=1.4, zorder=3)
ax.plot([c[0]-R], [c[1]], 'o', ms=3.4, mfc='white', mec=BLUE, mew=.9, zorder=5)
ax.plot([c[0]+R], [c[1]], 'o', ms=3.4, mfc='white', mec=GREEN, mew=.9, zorder=5)
label(ax, c+[R+4.2, 6.5], r'$\operatorname{supp}\psi_1$', 7.5, BLUE, halo=True, ha='left') if 0 else None
label(ax, c+[R+5.2, 0], r'$\psi_1$', 7.5, BLUE, halo=True)
label(ax, c-[R-6.8, 0], r'$\psi_2$', 7.5, GREEN, halo=True)
panel_tag(ax, c[0], 1.7, '(a)')
# (b) partition
x0, y0, sx, sy = 44, 11, 22/np.pi/2, 21
G = lambda t, v: np.c_[x0+sx*(t+np.pi), y0+sy*v]
arrow(ax, G(-np.pi, 0)[0], G(np.pi*1.08, 0)[0], color=MUTED, lw=.75, scale=5.5); arrow(ax, G(-np.pi, 0)[0], G(-np.pi, 1.2)[0], color=MUTED, lw=.75, scale=5.5)
p1 = psi1(th)
ax.plot(*G(th, p1).T, color=BLUE, lw=1.4, zorder=3); ax.plot(*G(th, 1-p1).T, color=GREEN, lw=1.4, ls='--', zorder=3)
for t0, n in ((-np.pi, r'$-\pi$'), (0, '$0$'), (np.pi, r'$\pi$')):
    ax.plot([G(t0, 0)[0, 0]]*2, [y0-1, y0+1], color=MUTED, lw=.75); label(ax, G(t0, 0)[0]+[0, -2.7], n, 7.5, MUTED)
ax.plot([x0-1, x0+1], [y0+sy]*2, color=MUTED, lw=.75); label(ax, (x0-2.8, y0+sy), '$1$', 7.5, MUTED)
panel_tag(ax, G(0, 0)[0, 0], 1.7, '(b)')
# (c) pieces in the charts
x1 = 74; sy2 = 13.5
C = lambda t, v, x0_: np.c_[x0_+sx*.86*t, y0+sy2*v]
xa = x1; 
for off, lo, hi in ((x1+12, -np.pi, np.pi), ):
    pass
ca = lambda t, v: np.c_[x1+sx*.72*(t+np.pi), y0+sy2*v]
cb = lambda t, v: np.c_[x1+sx*.72*(2*np.pi+1.15+t), y0+sy2*v]
arrow(ax, ca(-np.pi, 0)[0], ca(np.pi*1.05, 0)[0], color=MUTED, lw=.75, scale=5.5); arrow(ax, ca(-np.pi, 0)[0], ca(-np.pi, 1.68)[0], color=MUTED, lw=.75, scale=5.5)
ax.plot(*ca(th, p1*u(th)).T, color=BLUE, lw=1.4, zorder=3)
th2 = np.linspace(0, 2*np.pi, 721)
p2 = 1-psi1(np.angle(np.exp(1j*th2)))
arrow(ax, cb(0, 0)[0], cb(2*np.pi*1.05, 0)[0], color=MUTED, lw=.75, scale=5.5); arrow(ax, cb(0, 0)[0], cb(0, 1.68)[0], color=MUTED, lw=.75, scale=5.5)
ax.plot(*cb(th2, p2*u(th2)).T, color=GREEN, lw=1.4, zorder=3)
label(ax, ca(0, 1.5)[0]+[5, 1.5], r'$\psi_1u$', 7.5, BLUE, halo=True)
label(ax, cb(np.pi, .55)[0]+[3, 3], r'$\psi_2u$', 7.5, GREEN, halo=True)
for g, t0, n in ((ca, -np.pi, r'$-\pi$'), (ca, np.pi, r'$\pi$'), (cb, 0, '$0$'), (cb, 2*np.pi, r'$2\pi$')):
    ax.plot([g(t0, 0)[0, 0]]*2, [y0-1, y0+1], color=MUTED, lw=.75); label(ax, g(t0, 0)[0]+[0, -2.7], n, 7.5, MUTED)
panel_tag(ax, (ca(-np.pi, 0)[0, 0]+cb(2*np.pi, 0)[0, 0])/2, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'psi1=S((5pi/6-|theta|)/(2pi/3)), S=eta/(eta+eta(1-.)), eta=exp(-1/t); psi2=1-psi1; u=1+0.5 cos theta'})
