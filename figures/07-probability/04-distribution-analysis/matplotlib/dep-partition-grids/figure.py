"""Continuous parabola X ~ Unif(-1,1), Y = X^2 (blue curve) with two fixed partitions (grey lines):
(a) x cut at 0, y cut at 1/4 (equal-probability 2 x 2 grid): every cell has probability 1/4, label MI = 0;
(b) x cuts at -1/2, 0, 1/2 and y cut at 1/4: cell probabilities 0 or 1/4, label MI = ln 2."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

xx = np.linspace(-1, 1, 400)
fig, axs = figure(width_mm=104, height_mm=46, ncols=2)
def cellp(xc, yc):
    x, w = grid_x(200000)
    P = np.zeros((len(xc)-1, len(yc)-1))
    ix = np.searchsorted(xc, x, side='right')-1; iy = np.searchsorted(yc, x**2, side='right')-1
    np.add.at(P, (np.clip(ix, 0, len(xc)-2), np.clip(iy, 0, len(yc)-2)), w)
    return P
res = {}
for ax, xc, lab in [(axs[0], [-1, 0, 1], '(a)'), (axs[1], [-1, -.5, 0, .5, 1], '(b)')]:
    yc = [0, .25, 1]
    P = cellp(np.array(xc, float), np.array(yc, float))
    ax.plot(xx, xx**2, color=BLUE, lw=1.4)
    for c in xc[1:-1]: ax.axvline(c, color=STROKE, lw=.8)
    ax.axhline(.25, color=STROKE, lw=.8)
    for i in range(len(xc)-1):
        for j in range(2):
            v = P[i, j]
            txt = '0' if v < 1e-9 else '1/4'
            cx = (xc[i]+xc[i+1])/2
            if len(xc) == 3 and j == 0: cx = 0.8*np.sign(cx)
            ax.text(cx, 0.86 if j == 1 else 0.12, txt, ha='center', va='center',
                    fontsize=7.5, color=RED if v < 1e-9 else INK)
    ax.set_xlim(-1, 1); ax.set_ylim(0, 1); ax.set_xticks(xc); ax.set_yticks([0, .25, 1])
    ax.set_xticklabels([f'{c:g}' for c in xc])
    ax.set_xlabel('$x$', labelpad=0); ax.set_ylabel('$y$', labelpad=0)
    ax.set_box_aspect(.8)
    gfmt(ax)
    tag(ax, lab, y=-.3)
    res[lab] = {'P': P.round(6).tolist(), 'MI': mi_table(P)}
save(fig, HERE, 'figure', res)
