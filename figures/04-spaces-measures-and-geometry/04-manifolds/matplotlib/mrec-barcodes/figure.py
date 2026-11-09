"""Rips and Cech barcodes of the unit hexagon; Cech H1 of 24 points on the circle with the recovery window."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from itertools import combinations
OUT = Path(__file__).resolve().parent

def mincircle(P):
    P = np.asarray(P); best = None
    for i, j in combinations(range(len(P)), 2):
        c = (P[i]+P[j])/2; r = np.linalg.norm(P[i]-c)
        if np.all(np.linalg.norm(P-c, axis=1) <= r+1e-9):
            best = min(best, r) if best is not None else r
    for i, j, k in combinations(range(len(P)), 3):
        a, b, cc = P[i], P[j], P[k]
        d = 2*(a[0]*(b[1]-cc[1])+b[0]*(cc[1]-a[1])+cc[0]*(a[1]-b[1]))
        if abs(d) < 1e-12:
            continue
        ux = ((a@a)*(b[1]-cc[1])+(b@b)*(cc[1]-a[1])+(cc@cc)*(a[1]-b[1]))/d
        uy = ((a@a)*(cc[0]-b[0])+(b@b)*(a[0]-cc[0])+(cc@cc)*(b[0]-a[0]))/d
        c = np.array([ux, uy]); r = np.linalg.norm(a-c)
        if np.all(np.linalg.norm(P-c, axis=1) <= r+1e-9):
            best = min(best, r) if best is not None else r
    return best

def persistence(simplices):
    """Mod-2 column reduction; `simplices` is a list of (value, tuple). Returns {dim: [(birth, death)]}."""
    simplices = sorted(simplices, key=lambda s: (round(s[0], 9), len(s[1]), s[1]))
    index = {s[1]: i for i, s in enumerate(simplices)}
    low = {}; cols = []; pivots = {}
    out = {}
    for j, (val, s) in enumerate(simplices):
        col = set(index[f] for f in combinations(s, len(s)-1)) if len(s) > 1 else set()
        while col and max(col) in pivots:
            col ^= cols[pivots[max(col)]]
        cols.append(col)
        if col:
            pivots[max(col)] = j
    paired = set()
    for b, d in pivots.items():
        paired |= {b, d}
        v0, v1 = simplices[b][0], simplices[d][0]
        if v1 > v0+1e-9:
            out.setdefault(len(simplices[b][1])-1, []).append((v0, v1))
    for j, (v, s) in enumerate(simplices):
        if j not in paired:
            out.setdefault(len(s)-1, []).append((v, np.inf))
    return out

def rips(P, maxdim):
    n = len(P)
    return [(max(np.linalg.norm(P[a]-P[b]) for a, b in combinations(s, 2)) if len(s) > 1 else 0., s)
            for k in range(1, maxdim+2) for s in combinations(range(n), k)]

def cech(P, maxdim):
    n = len(P)
    return [(mincircle(P[list(s)]) if len(s) > 1 else 0., s) for k in range(1, maxdim+2) for s in combinations(range(n), k)]

ang = lambda n: np.arange(n)*2*np.pi/n
Hex = np.stack([np.cos(ang(6)), np.sin(ang(6))], 1)
R = persistence(rips(Hex, 3)); C = persistence(cech(Hex, 3))
print('Rips hex', {k: sorted((round(a, 4), round(b, 4)) for a, b in v) for k, v in R.items()})
print('Cech hex', {k: sorted((round(a, 4), round(b, 4)) for a, b in v) for k, v in C.items()})
C24 = persistence(cech(np.stack([np.cos(ang(24)), np.sin(ang(24))], 1), 2))
print('Cech 24 H1', [(round(a, 4), round(b, 4)) for a, b in C24[1]], 'H0 finite', len([1 for a, b in C24[0] if np.isfinite(b)]), sorted(set(round(b, 4) for a, b in C24[0] if np.isfinite(b))))
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], float)
print('Rips square', {k: sorted((round(a, 4), round(b, 4)) for a, b in v) for k, v in persistence(rips(square, 3)).items()})
line = np.array([[0, 0], [1, 0], [3, 0]], float)
print('Rips line', {k: sorted((round(a, 4), round(b, 4)) for a, b in v) for k, v in persistence(rips(line, 2)).items()})

W, H = 112, 36
fig, ax = canvas(W, H)
COL = {0: BLUE, 1: GREEN, 2: PURPLE}
def bars(x0, width, xmax, xticks, ticklabels, rows, shade=None):
    """Rows of (y, a, b, colour); axis at y=9.5."""
    X = lambda v: x0+v/xmax*width
    y0 = 9.5
    ax.plot([X(0), X(xmax)], [y0, y0], color=STROKE, lw=.75, zorder=2)
    for v, t in zip(xticks, ticklabels):
        ax.plot([X(v)]*2, [y0-.9, y0], color=STROKE, lw=.75, zorder=2)
        label(ax, (X(v), y0-3.2), t, 7.5, INK)
    if shade:
        ax.add_patch(Polygon([(X(shade[0]), y0), (X(shade[1]), y0), (X(shade[1]), 34), (X(shade[0]), 34)], fc=YELLOW_FILL, ec='none', zorder=1))
    for y, a, b, c in rows:
        ax.plot([X(a), X(min(b, xmax))], [y, y], color=c, lw=1.8, solid_capstyle='butt', zorder=3)
        if not np.isfinite(b):
            arrow(ax, (X(xmax)-1.5, y), (X(xmax)+.8, y), color=c, lw=1.2, scale=6)
    return X
# (a) Rips hexagon
rows = []
y = 31
for a, b in sorted(R[0], key=lambda t: -t[1]):
    rows.append((y, a, b, COL[0])); y -= 2.0
y -= 1.0
for a, b in sorted(R[1]):
    rows.append((y, a, b, COL[1])); y -= 3
y -= .4
for a, b in sorted(R[2]):
    rows.append((y, a, b, COL[2])); y -= 3
Xa = bars(8.5, 26, 2.3, [0, 1, np.sqrt(3), 2], ['$0$', '$1$', r'$\sqrt{3}$', '$2$'], rows)
yk = {0: 36, 1: 26.5, 2: 23.3}
label(ax, (4.2, 26), '$H_0$', 7.5, COL[0]); label(ax, (4.2, 17.2), '$H_1$', 7.5, COL[1]); label(ax, (4.2, 13.4), '$H_2$', 7.5, COL[2])
panel_tag(ax, 21.5, 1.4, '(a)')
# (b) Cech hexagon
rows = []; y = 31
for a, b in sorted(C[0], key=lambda t: -t[1]):
    rows.append((y, a, b, COL[0])); y -= 2.0
y -= 1.0
for a, b in sorted(C[1]):
    rows.append((y, a, b, COL[1])); y -= 3
bars(46, 26, 1.3, [0, .5, 1], ['$0$', '$0.5$', '$1$'], rows)
label(ax, (41.7, 26), '$H_0$', 7.5, COL[0]); label(ax, (41.7, 17.2), '$H_1$', 7.5, COL[1])
panel_tag(ax, 59, 1.4, '(b)')
# (c) Cech 24 points: H0 bundle, H1 bar, recovery window
h0short = max(b for a, b in C24[0] if np.isfinite(b))
a1, b1 = C24[1][0]
eps1, eps2 = 2*2*np.sin(np.pi/48), np.sqrt(3/5)
rows = [(30, 0, np.inf, COL[0]), (26.5, 0, h0short, COL[0]), (17.2, a1, b1, COL[1])]
X = bars(84, 25, 1.25, [0, eps1, eps2, 1], ['$0$', '', '', '$1$'], rows, shade=(eps1, eps2))
label(ax, (X(eps1), 6.3), r'$\varepsilon_1$', 7.5, INK); label(ax, (X(eps2), 6.3), r'$\varepsilon_2$', 7.5, INK)
label(ax, (79.7, 28), '$H_0$', 7.5, COL[0]); label(ax, (79.7, 17.2), '$H_1$', 7.5, COL[1])
label(ax, (X(h0short)+5, 26.5), r'$\times 23$', 7.5, COL[0])
panel_tag(ax, 96.5, 1.4, '(c)')
save(fig, OUT, 'figure', {'formula': 'Column reduction of Rips (dim<=3) and Cech (min enclosing circle) filtrations of the unit hexagon and 24 equally spaced points'})
