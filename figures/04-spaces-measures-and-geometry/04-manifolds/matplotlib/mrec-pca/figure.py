"""Local PCA on the parabola y=u^2/2 (R=1,h=.25): symmetric versus one-sided; bending vs noise as the radius grows."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 50
fig, ax = canvas(W, H)
def pca(p):
    c = p-p.mean(0); C = c.T@c/len(p); w, V = np.linalg.eigh(C); return p.mean(0), V[:, 1]*np.sign(V[0, 1]), C
R, h = 1, .25
f = lambda u: u*u/(2*R)
for pts, x0, tag in ((np.array([-h, 0, h]), 19, '(a)'), (np.array([0, h, 2*h]), 58, '(b)')):
    u = 34 if tag == '(a)' else 34
    o = np.array([x0 if tag == '(a)' else x0-8.5, 16])
    xs = np.linspace(-.5, .7, 241)
    if tag == '(a)':
        xs = np.linspace(-.5, .5, 201)
    else:
        xs = np.linspace(-.2, .75, 201)
    ax.plot(o[0]+u*xs, o[1]+u*f(xs), color=BLUE, lw=1.4, zorder=3)
    ax.plot([o[0]+u*xs[0], o[0]+u*xs[-1]], [o[1], o[1]], color=MUTED, lw=.85, ls=(0, (2.2, 1.8)), zorder=2)
    P = np.stack([pts, f(pts)], 1)
    m, d, C = pca(P)
    s = .5
    ax.plot(*zip(o+u*(m-s*d), o+u*(m+s*d)), color=GREEN, lw=1.2, zorder=4)
    for q in P:
        dot(ax, o+u*q, INK, size=1.0)
    dot(ax, o+u*m, GREEN, size=1.0, hollow=True)
    dot(ax, o, RED, size=1.1)
    label(ax, o+(0, -3), r'$\mathbf{p}$', 8, RED)
    print(tag, 'angle(deg)=', np.degrees(np.arctan2(d[1], d[0])), 'C=', C.round(5).tolist())
    panel_tag(ax, o[0]+u*(xs[0]+xs[-1])/2, 1.4, tag)
# (c) log-log: circle radius 1, one-sided arc [0,r], normal noise sigma*sign(u-mean), 41 samples.
def inset(x, y, w, h):
    a = fig.add_axes([x/W, y/H, w/W, h/H]); a.spines[['top', 'right']].set_visible(False); a.tick_params(length=2, width=.75, pad=1.5); return a
sigma = .005
a = inset(82, 11.5, 27, 35)
rs = np.geomspace(.02, 1, 60)
errs = []
for r in rs:
    th = np.linspace(0, r, 41)
    p = np.stack([np.sin(th), 1-np.cos(th)], 1)
    n = np.stack([-np.sin(th), np.cos(th)], 1)
    x = p+sigma*np.sign(th-th.mean())[:, None]*n
    _, d, _ = pca(x)
    errs.append(abs(d[1]))
a.loglog(rs, errs, color=BLUE, lw=1.4)
a.loglog(rs, rs, color=GREEN, lw=1.0, ls=(0, (4, 2)))
a.loglog(rs, 2*sigma/rs, color=RED, lw=1.0, ls=(0, (1.5, 1.5)))
a.set_xlim(.02, 1); a.set_ylim(.005, 1.1)
a.set_xlabel('$r$', labelpad=.5); a.set_xticks([.02, .1, 1], ['$0.02$', '$0.1$', '$1$']); a.set_yticks([.01, .1, 1], ['$0.01$', '$0.1$', '$1$']); a.minorticks_off()
a.text(.12, .53, r'$r/\tau$', color=GREEN, fontsize=7.5, transform=a.transAxes)
a.text(.04, .08, r'$2\sigma/r$', color=RED, fontsize=7.5, transform=a.transAxes)
a.text(.46, .80, r'$\sin\theta$', color=BLUE, fontsize=8, transform=a.transAxes)
panel_tag(ax, 95.5, 1.4, '(c)')
save(fig, OUT, 'figure', {'formula': 'parabola y=u^2/2, h=.25; panel c: arc [0,r] of unit circle, 41 samples, normal noise .005*sign(t-mean), sin of tilt of leading PCA direction'})
