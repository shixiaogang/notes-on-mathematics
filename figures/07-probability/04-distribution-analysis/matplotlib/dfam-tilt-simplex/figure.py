"""Tilted family p_theta(x) ∝ e^{theta x} on {0,1,2} drawn in the simplex; theta in [-6,6]; points theta=-1,0,1 (green), ln2 (red); line E X = 10/7."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

import math
def p_of(t):
    w = np.exp(t*np.arange(3)); return w/w.sum()
fig, ax = figure(width_mm=88, height_mm=70)
V = np.array([[0, 0], [1, 0], [0.5, math.sqrt(3)/2]])
ax.fill(V[:, 0], V[:, 1], color=BLUE_FILL, lw=0)
ax.plot(np.r_[V[:, 0], 0], np.r_[V[:, 1], 0], color=STROKE, lw=0.95)
th = np.linspace(-6, 6, 600)
P = np.array([p_of(t) for t in th])
x, y = simplex_xy(P)
ax.plot(x, y, color=BLUE, lw=1.4)
# mean line p1+2p2 = 10/7: endpoints on boundary: p2=0 -> p1=10/7 >1 invalid; p0=0: p1+p2=1, p1+2p2=10/7 -> p2=3/7,p1=4/7; p1=0: p2=5/7, p0=2/7
L = np.array([[0, 4/7, 3/7], [2/7, 0, 5/7]])
lx, ly = simplex_xy(L)
ax.plot(lx, ly, color=STROKE, lw=0.9, ls='--')
G = np.array([p_of(t) for t in (-1, 0, 1)]); gx, gy = simplex_xy(G)
ax.scatter(gx, gy, s=14, color=GREEN, zorder=4)
R = p_of(math.log(2)); rx, ry = simplex_xy(R)
ax.scatter([rx], [ry], s=18, color=RED, zorder=5)
ax.text(rx-0.06, ry-0.05, r'$(1/7,\,2/7,\,4/7)$', fontsize=7.5, va='top', ha='right')
for t, xx_, yy_ in zip((-1, 0, 1), gx, gy):
    ax.text(xx_+0.025, yy_-0.035, rf'$\theta={t}$', fontsize=7.5, color=MUTED, va='top')
ax.text(-0.03, -0.03, r'$\delta_0$', ha='right', va='top'); ax.text(1.03, -0.03, r'$\delta_1$', ha='left', va='top')
ax.text(0.5, math.sqrt(3)/2+0.03, r'$\delta_2$', ha='center', va='bottom')
ax.set_aspect('equal'); ax.axis('off')
ax.set_xlim(-0.08, 1.08); ax.set_ylim(-0.08, 0.95)
save(fig, HERE, 'figure', {'p_ln2': [float(v) for v in R], 'p_at_6': [float(v) for v in p_of(6)], 'mean_line_endpoints': L.tolist()})
