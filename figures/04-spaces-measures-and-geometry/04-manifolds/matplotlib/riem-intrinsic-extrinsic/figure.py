"""A flat rectangle, the unit cylinder it rolls onto, and the sphere; the normal directions on each surface."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 48
fig, ax = canvas(W, H)
ox, oy, sc = 3.5, 18.0, 5.0
R = np.array([[ox, oy], [ox+sc*2*np.pi, oy], [ox+sc*2*np.pi, oy+sc*2], [ox, oy+sc*2]])
ax.add_patch(Polygon(R, fc=BLUE_FILL, ec=STROKE, lw=.9, zorder=1))
for s_ in np.arange(1, 6)*np.pi/3:
    ax.plot([ox+sc*s_]*2, [oy, oy+sc*2], color=BLUE, lw=.65, zorder=2)
for z_ in (.5, 1, 1.5):
    ax.plot([ox, ox+sc*2*np.pi], [oy+sc*z_]*2, color=BLUE, lw=.65, zorder=2)
ax.plot([ox, ox+sc*2*np.pi], [oy, oy+sc*2], color=RED, lw=1.3, zorder=3)
label(ax, (ox+sc*np.pi, oy-2.6), r'$s$', 7.5, MUTED); label(ax, (ox-2.2, oy+sc), r'$z$', 7.5, MUTED)
panel_tag(ax, ox+sc*np.pi, 3, '(a)')
pl = Placed(View(12, 18), 54, 15.0, 11.0)
f = pl.view.f
th = np.linspace(0, 2*np.pi, 721)
def cyl(t, z, color, lw=1.0, hidden=False, zorder=3):
    P = np.c_[np.cos(t), np.sin(t), z]
    N = np.c_[np.cos(t), np.sin(t), 0*t]
    split_plot(ax, pl(P), N@f >= 0, color, lw=lw, hidden=hidden, zorder=zorder)
for z_ in (.5, 1, 1.5):
    cyl(th, np.full_like(th, z_), BLUE, lw=.65, hidden=False, zorder=2)
for s_ in np.arange(0, 6)*np.pi/3:
    a = np.array([[np.cos(s_), np.sin(s_), 0], [np.cos(s_), np.sin(s_), 2]])
    if np.cos(s_)*f[0]+np.sin(s_)*f[1] >= 0:
        ax.plot(*pl(a).T, color=BLUE, lw=.65, zorder=2)
cyl(th, np.full_like(th, 0.0), STROKE, lw=.95, hidden=True, zorder=2.5)
ax.plot(*pl(np.c_[np.cos(th), np.sin(th), np.full_like(th, 2.0)]).T, color=STROKE, lw=.95, zorder=2.5)
for sg in (-1, 1):
    a = np.arctan2(f[1], f[0])+sg*np.pi/2
    ax.plot(*pl(np.array([[np.cos(a), np.sin(a), 0], [np.cos(a), np.sin(a), 2]])).T, color=STROKE, lw=.95, zorder=2.5)
t = np.linspace(0, 2*np.pi, 721)
cyl(t, t/np.pi, RED, lw=1.25, hidden=True, zorder=4)
for s_, z_ in ((-1.1, 1.0), (1.1, .4), (1.1, 1.0), (1.1, 1.6)):
    P = np.array([np.cos(s_), np.sin(s_), z_]); n = np.array([np.cos(s_), np.sin(s_), 0])
    arrow(ax, pl(P), pl(P+.55*n), color=GREEN, lw=1.3, scale=7, zorder=8)
    dot(ax, pl(P), INK, size=.9)
panel_tag(ax, 54, 3, '(b)')
ps = Placed(View(20, 22), 92.5, 25.5, 16.5)
sphere_disc(ax, ps, fill=BLUE_FILL, edge=STROKE)
for lat in (-45, 0, 45):
    sphere_curve(ax, ps, parallel(np.radians(lat)), BLUE, lw=.65, hidden=False, zorder=2)
for lon in (-60, 0, 60):
    sphere_curve(ax, ps, meridian(np.radians(lon)), BLUE, lw=.65, hidden=False, zorder=2)
for lat, lon in ((0, -60), (0, 80), (50, 10), (-50, 10), (22, 42)):
    P = spherical(np.radians(lat), np.radians(lon))
    arrow(ax, ps(P), ps(P*1.4), color=GREEN, lw=1.3, scale=7, zorder=8)
    dot(ax, ps(P), INK, size=.9)
panel_tag(ax, 92.5, 3, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F(s,z)=(cos s, sin s, z); normal n=(cos s,sin s,0); sphere normal n=x'})
