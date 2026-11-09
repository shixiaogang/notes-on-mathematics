from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Weighted Chebyshev level sets: (a) concave front, z=(-1,-1), w=(1/2,1/2). (b) dented front, rays from z=(-0.1,-0.1).
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .08, .985, .985, .18, .24)
def L(ax, z, w, lev, **kw):
    c = z+lev/np.asarray(w); ax.plot([z[0], c[0], c[0]], [c[1], c[1], z[1]], **kw)
ax = axes[0]; setup(ax, (-1.1, 1.3), (-1.1, 1.3), [-1, 0, 1], [-1, 0, 1], equal=True)
x = np.linspace(0, 1, 300); ax.fill(np.r_[x, 1, 1.3, 1.3, 0], np.r_[1-x**2, 0, 0, 1.3, 1.3], color=BLUE_FILL, lw=0, zorder=1); ax.plot(x, 1-x**2, color=RED, lw=2, zorder=3)
z = np.array([-1., -1.]); w = np.array([.5, .5]); g = (np.sqrt(5)-1)/2
for lev in (.4, .6): L(ax, z, w, lev, color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2)
L(ax, z, w, .5*(g+1), color=PURPLE, lw=1.2, zorder=4)
ax.plot([-1, g], [-1, g], color=GREEN, lw=1.1, zorder=3); hollow(ax, z, INK); dot(ax, (g, g))
ax.text(-.95, -.8, '$z$', color=INK); ax.text(g+.05, g+.05, '$(0.618,0.618)$', color=INK, fontsize=7.5)
ax = axes[1]; setup(ax, (-.15, 1.2), (-.15, 1.2), [0, .5, 1], [0, .5, 1], equal=True)
u = np.linspace(0, 1, 4001); v = bump(u); ax.fill(np.r_[u, 1, 1.2, 1.2, 0], np.r_[v, 0, 0, 1.2, 1.2], color=BLUE_FILL, lw=0, zorder=1); ax.plot(u, v, color=RED, lw=1.8, zorder=3)
z = np.array([-.1, -.1]); out = []
for ang in (.9, .75, .55):  # ratio (f2-z2)/(f1-z1)=tan(angle)
    r = np.tan(ang); i = np.argmin(abs((v-z[1])-r*(u-z[0]))); p = (u[i], v[i]); out.append(p)
    ax.plot([z[0], p[0]], [z[1], p[1]], color=GREEN, lw=1.0, zorder=2); dot(ax, p, RED, ms=5.5)
    w = 1/(np.array(p)-z); w /= w.sum()
    L(ax, z, w, w[0]*(p[0]-z[0]), color=PURPLE, lw=.9, zorder=4)
hollow(ax, z, INK); ax.text(-.1, -.04, '$z$', color=INK) if 0 else ax.text(-.13, -.03, '$z$', color=INK)
tags(fig, axes)
save(fig, HERE, 'figure', {'golden': float(g), 'dent_points': [tuple(map(float, p)) for p in out]}); print(out)
