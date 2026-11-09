"""Slice charts: polar chart (theta,r-1) straightening the unit circle; (x,y-x^2) straightening a parabola."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 56
fig, ax = canvas(W, H)
# (a) polar
c = np.array([19., 30.]); u = 11.5
th = np.linspace(-np.pi+.05, np.pi-.05, 361)
for rr in (.5, 1.5):
    ax.plot(c[0]+u*rr*np.cos(th), c[1]+u*rr*np.sin(th), color=MUTED, lw=.5, zorder=1)
for a in np.arange(-3, 4)*np.pi/4:
    ax.plot(c[0]+u*np.array([.5, 1.5])*np.cos(a), c[1]+u*np.array([.5, 1.5])*np.sin(a), color=MUTED, lw=.4, zorder=1)
ax.plot(c[0]+u*np.cos(th), c[1]+u*np.sin(th), color=BLUE, lw=1.3, zorder=3)
q = np.array([.6, .8]); a0 = np.arctan2(.8, .6)
Pa = c+u*q; Pb = c+u*1.5*q
dot(ax, Pa, INK, zorder=8); dot(ax, Pb, RED, size=1.3, zorder=8)
label(ax, Pa+[-4.5, -1.4], r'$q$', 7.5, halo=True); label(ax, Pb+[3.2, 1.8], r"$q'$", 7.5, RED, halo=True)
label(ax, c+[0, 1], '$S^1$', 7.5, BLUE)
ax.plot([c[0]-u*.5, c[0]-u*1.5], [c[1], c[1]], color=RED, lw=1.1, zorder=3)
rx = 58; ry = 30; sx = 3.6; sy = 11.5
def rect(t, s): return (rx+sx*t, ry+sy*s)
xx = np.array([-np.pi, np.pi])
for s in (-.5, .5):
    ax.plot(rx+sx*xx, [ry+sy*s]*2, color=MUTED, lw=.5, zorder=1)
for a in np.arange(-3, 4)*np.pi/4:
    ax.plot([rx+sx*a]*2, [ry-sy*.5, ry+sy*.5], color=MUTED, lw=.4, zorder=1)
ax.plot(rx+sx*xx, [ry, ry], color=BLUE, lw=1.3, zorder=3)
dot(ax, rect(a0, 0), INK, zorder=8); dot(ax, rect(a0, .5), RED, size=1.3, zorder=8)
label(ax, np.array(rect(a0, 0))+[0, -2.8], r'$(0.927,0)$', 7.5, halo=True)
label(ax, np.array(rect(a0, .5))+[0, 2.8], r'$(0.927,0.5)$', 7.5, RED, halo=True)
label(ax, (rx-sx*np.pi-3.2, ry), r'$\theta$', 7.5, MUTED) if False else None
label(ax, (rx+sx*np.pi+.5, ry+3.0), r'$\theta$', 7.5, MUTED)
label(ax, (rx-sx*np.pi+1.5, ry+sy*.5+3.2), r'$r-1$', 7.5, MUTED)
arrow(ax, (c[0]+u*1.5+.8, 30), (rx-sx*np.pi-.8, 30), color=STROKE, lw=.9)
label(ax, ((c[0]+u*1.5+rx-sx*np.pi)/2, 33), r'$\varphi$', 7.5)
panel_tag(ax, (c[0]+rx)/2, 1.6, '(a)')
# (b) graph
ox = 89.; oy = 13.; s = 9.0
xr = np.linspace(-1.35, 1.35, 200)
xx1 = ox+s*0
for cc in (-.6, .6, 1.2):
    y = xr**2+cc
    ax.plot(ox+s*xr, oy+s*y, color=MUTED, lw=.45, zorder=1)
ax.plot(ox+s*xr, oy+s*xr**2, color=BLUE, lw=1.3, zorder=3)
arrow(ax, (ox-1.7*s, oy-.9*s/s), (ox+1.7*s, oy-.9*s/s), color=MUTED, lw=.75, scale=5.5) if False else None
ax.plot([ox-1.5*s, ox+1.5*s], [oy, oy], color=MUTED, lw=.6, zorder=1)
ax.plot([ox, ox], [oy-.75*s, oy+3.3*s], color=MUTED, lw=.6, zorder=1)
dot(ax, (ox+s, oy+s), INK, zorder=8); dot(ax, (ox+s, oy+2*s), RED, size=1.3, zorder=8)
label(ax, (ox+s+6.5, oy+s-.8), '$(1,1)$', 7.5, halo=True)
label(ax, (ox+s+6.5, oy+2*s), '$(1,2)$', 7.5, RED, halo=True)
label(ax, (ox-1.5*s, oy+1.05*s), r'$\Gamma_f$', 7.5, BLUE, halo=True)
panel_tag(ax, ox, 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'phi(y)=(atan2(y2,y1), r-1) on the slit plane, q=(.6,.8), q2=(.9,1.2); Gamma_f: f(x)=x^2 with curves f+c'})
