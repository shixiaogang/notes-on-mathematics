"""Neighbourhood radius: noise-dominated, adequate, and strand-mixing; deterministic seed."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 42
fig, ax = canvas(W, H)
rng = np.random.default_rng(4310)
top = lambda x: .34+.1*np.sin(2.2*x); bot = lambda x: -.34+.1*np.sin(2.2*x+1.0)
xs = np.linspace(-1, 1, 301)
xt = rng.uniform(-1, 1, 75); xb = rng.uniform(-1, 1, 75)
sigma = .035
ptop = np.stack([xt, top(xt)], 1); pbot = np.stack([xb, bot(xb)], 1)
pts = np.r_[ptop, pbot]+sigma*rng.normal(size=(150, 2)).clip(-1, 1)
c = np.array([0, top(0.)])
for k, (r, cx, tag) in enumerate(((.07, 19, '(a)'), (.30, 56, '(b)'), (.78, 93, '(c)'))):
    u = 16; o = np.array([cx, 22.5])
    ax.plot(o[0]+u*xs, o[1]+u*top(xs), color=BLUE, lw=1.3, zorder=2)
    ax.plot(o[0]+u*xs, o[1]+u*bot(xs), color=BLUE, lw=1.3, zorder=2)
    d = np.linalg.norm(pts-c, axis=1) <= r
    q = o+u*pts
    ax.plot(q[~d, 0], q[~d, 1], 'o', ms=1.5, mfc=MUTED, mec=MUTED, mew=0, zorder=3)
    ax.plot(q[d, 0], q[d, 1], 'o', ms=2.1, mfc=RED, mec=RED, mew=0, zorder=4)
    tt = np.linspace(0, 2*np.pi, 241)
    ax.plot(o[0]+u*(c[0]+r*np.cos(tt)), o[1]+u*(c[1]+r*np.sin(tt)), color=RED, lw=.9, zorder=5)
    panel_tag(ax, cx, 1.4, tag)
save(fig, OUT, 'figure', {'formula': 'two strands y=.34+.1 sin 2.2x and y=-.34+.1 sin(2.2x+1); 150 samples, noise .035, seed 4310; r=.07,.30,.78'})
