from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
def axes_box(ax, x0, y0, w, h, xlim, ylim):
    """Plain axes at mm position on the canvas (data coordinates in the returned callable)."""
    sx, sy = w/(xlim[1]-xlim[0]), h/(ylim[1]-ylim[0])
    return (lambda x, y: (x0+(np.asarray(x)-xlim[0])*sx, y0+(np.asarray(y)-ylim[0])*sy))
def axis(ax, a, b, **kw):
    arrow(ax, a, b, color=MUTED, lw=.75, scale=5.5, zorder=2)

"""Stability: (a) lambda2(d13) with a=1.01; (b) axis rotation theta=arctan(2e/g)/2 for gaps; (c) amplification 1/(2 eta)."""
W, H = 112, 48
fig, ax = canvas(W, H)
TW = 28
def panel(x0, xlim, ylim):
    return axes_box(ax, x0, 10, TW, 33, xlim, ylim)
# (a)
xlim, ylim = (1.975, 2.05), (-.016, .016)
T = panel(5, xlim, ylim)
axis(ax, T(xlim[0], ylim[0]), T(xlim[0], ylim[1])); axis(ax, T(xlim[0], 0), T(xlim[1], 0))
d = np.linspace(1.988, 2.032, 200); l = (4.04-d**2)/6
ax.plot(*T(d[l >= 0], l[l >= 0]), color=GREEN, lw=1.4, zorder=3); ax.plot(*T(d[l < 0], l[l < 0]), color=RED, lw=1.4, zorder=3)
for dv, c in ((2, GREEN), (2.02, RED)):
    v = (4.04-dv**2)/6; dot(ax, T(dv, v), c)
    ax.plot(*T([dv, dv], [0, v]), color=c, lw=.7, ls=(0, (2.2, 1.8)), zorder=2)
label(ax, T(2, .0067)+np.array([2.2, 2.2]), '$2.00$', 7.5, GREEN, ha='left'); label(ax, T(2.02, -.0067)+np.array([2.6, -1.5]), '$2.02$', 7.5, RED, ha='left')
label(ax, T(xlim[1], 0)+np.array([.2, 2.0]), r'$d_{1,3}$', 7.5, MUTED, ha='right'); label(ax, T(xlim[0], ylim[1])+np.array([2.0, -.6]), r'$\lambda_2$', 7.5, MUTED, ha='left')
panel_tag(ax, 5+TW/2, 1.7, '(a)')
# (b)
xlim, ylim = (0, .22), (0, 50)
T = panel(44, xlim, ylim)
axis(ax, T(0, 0), T(xlim[1], 0)); axis(ax, T(0, 0), T(0, ylim[1]))
e = np.linspace(0, .21, 300)
for g, c, name, pos in ((1, BLUE, '$g=1$', (.19, 16)), (.2, GREEN, '$g=0.2$', (.19, 33.5)), (.02, YELLOW, '$g=0.02$', (.12, 47.5))):
    th = .5*np.degrees(np.arctan2(2*e, g)); ax.plot(*T(e, th), color=c, lw=1.4, zorder=3)
    label(ax, T(*pos), name, 7.5, c, ha='right', halo=True)
label(ax, T(.22, 0)+np.array([-.3, 2]), r'$e$', 7.5, MUTED, ha='right'); label(ax, T(0, 50)+np.array([1.5, -.6]), r'$\theta$', 7.5, MUTED, ha='left')
label(ax, T(0, 45)+np.array([-1.2, 0]), '45°', 7.5, MUTED, ha='right'); ax.plot(*T([0, -.006], [45, 45]), color=MUTED, lw=.7)
panel_tag(ax, 44+TW/2, 1.7, '(b)')
# (c)
xlim, ylim = (0, 1.05), (0, 11.5)
T = panel(82, xlim, ylim)
axis(ax, T(0, 0), T(xlim[1], 0)); axis(ax, T(0, 0), T(0, ylim[1]))
eta = np.linspace(.0455, 1, 300); ax.plot(*T(eta, 1/(2*eta)), color=BLUE, lw=1.4, zorder=3)
for ev in (.5, .1):
    dot(ax, T(ev, 1/(2*ev)), RED)
label(ax, T(.1, 5)+np.array([1.8, .9]), '$(0.1,5)$', 7.5, RED, ha='left'); label(ax, T(.5, 1)+np.array([1, 2.2]), '$(0.5,1)$', 7.5, RED, ha='left')
label(ax, T(1.05, 0)+np.array([-.3, 3.6]), r'$\eta$', 7.5, MUTED, ha='right'); label(ax, T(0, 11.5)+np.array([1.6, -.6]), r'$1/(2\eta)$', 7.5, MUTED, ha='left')
panel_tag(ax, 82+TW/2, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'lambda2=(4a-b)/6, a=1.01; theta=0.5 atan(2e/g); amplification 1/(2 eta)'})
