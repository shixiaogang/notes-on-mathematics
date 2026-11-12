from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# Joint table p(0,0)=1/4, p(0,1)=0, p(1,0)=3/8, p(1,1)=3/8 (rows X, columns Y).
# (a) mosaic split by X: widths P(X=x), heights P(Y=y|X=x); labels H(Y|X=x).
# (b) mosaic split by Y: widths P(Y=y), heights P(X=x|Y=y); grey bar on the right is P_X.
J = np.array([[1/4, 0], [3/8, 3/8]]); px = J.sum(1); py = J.sum(0)
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.07, right=.98, bottom=.25, top=.88, wspace=.25)
F = {0: (BLUE_FILL, BLUE), 1: (YELLOW_FILL, YELLOW)}
x0 = 0; facts = {}
for x in (0, 1):
    w = px[x]; cond = J[x]/w; y0 = 0
    for y in (0, 1):
        if cond[y] > 0:
            a.add_patch(__import__('matplotlib').patches.Rectangle((x0, y0), w, cond[y], fc=F[y][0], ec=F[y][1], lw=.8))
            a.text(x0+w/2, y0+cond[y]/2, '$Y=%d$' % y, ha='center', va='center', fontsize=7.5)
        y0 += cond[y]
    hx = H(cond); facts['H(Y|X=%d)' % x] = hx
    a.text(x0+w/2, 1.05, '$%.3f$' % abs(hx), ha='center', va='bottom', color=RED, fontsize=7.5)
    a.text(x0+w/2, -.08, '$X=%d$' % x, ha='center', va='top', fontsize=7.5)
    x0 += w
a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis('off')
G = {0: (GREEN_FILL, GREEN), 1: (PURPLE_FILL, PURPLE)}
x0 = 0
for y in (0, 1):
    w = py[y]*.8; cond = J[:, y]/py[y]; y0 = 0
    for x in (0, 1):
        if cond[x] > 0:
            b.add_patch(__import__('matplotlib').patches.Rectangle((x0, y0), w, cond[x], fc=G[x][0], ec=G[x][1], lw=.8))
            b.text(x0+w/2, y0+cond[x]/2, '$X=%d$' % x, ha='center', va='center', fontsize=7.5)
        y0 += cond[x]
    hy = H(cond); facts['H(X|Y=%d)' % y] = hy
    b.text(x0+w/2, 1.05, '$%.3f$' % abs(hy), ha='center', va='bottom', color=RED, fontsize=7.5)
    b.text(x0+w/2, -.08, '$Y=%d$' % y, ha='center', va='top', fontsize=7.5)
    x0 += w
xp = .86; wp = .14; y0 = 0
for x in (0, 1):
    b.add_patch(__import__('matplotlib').patches.Rectangle((xp, y0), wp, px[x], fc=G[x][0], ec=G[x][1], lw=.8))
    y0 += px[x]
b.text(xp+wp/2, 1.05, '$%.3f$' % H(px), ha='center', va='bottom', color=RED, fontsize=7.5)
b.text(xp+wp/2, -.08, '$P_X$', ha='center', va='top', fontsize=7.5)
b.set_xlim(0, 1); b.set_ylim(0, 1); b.axis('off')
for ax in (a, b): ax.set_clip_on(False)
tags(fig, (a, b))
facts.update({'H(Y|X)': H(J)-H(px), 'H(X|Y)': H(J)-H(py), 'H(X)': H(px)})
save(fig, HERE, 'figure', facts)
