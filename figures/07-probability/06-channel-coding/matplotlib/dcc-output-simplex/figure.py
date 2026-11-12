from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Output distributions reachable by choosing the input law: p_Y = q W is a convex combination of the rows of W.
# (a) BEC with eps = 0.25 drawn in the output simplex over {0, 1, e}: rows W_0, W_1 and the segment between them;
#     red dot = output law of the uniform input.
# (b) a three-input, three-output channel W3 (rows below): the reachable set is the triangle spanned by the rows;
#     red dot = output law of the uniform input.
W3 = np.array([[.8, .1, .1], [.1, .7, .2], [.2, .2, .6]])
V = np.array([[0, 0], [1, 0], [.5, np.sqrt(3)/2]])        # vertices: point masses on the three outputs
def bary(p): return np.asarray(p) @ V
fig, axs = figure(width_mm=104, height_mm=46, ncols=2)
panel(fig, left=.02, right=.98, top=.95, bottom=.14, wspace=.12)
for ax in axs:
    ax.set_aspect('equal'); ax.axis('off')
    tri = np.vstack([V, V[:1]]); ax.plot(tri[:, 0], tri[:, 1], color=STROKE, lw=.85)
    ax.set_xlim(-.12, 1.12); ax.set_ylim(-.14, .98)
Wb = bec(BEC_E)[:, [0, 2, 1]]                              # columns (0, 1, e): erasure at the top vertex
a, b = bary(Wb[0]), bary(Wb[1])
ax = axs[0]
ax.plot([a[0], b[0]], [a[1], b[1]], color=BLUE, lw=1.4)
for P, s, ha in ((a, r'$W_0$', 'right'), (b, r'$W_1$', 'left')):
    dot(ax, *P, color=BLUE); lab(ax, P[0]+(-.04 if ha == 'right' else .04), P[1]+.03, s, BLUE, ha=ha, fontsize=8)
m = bary(.5*Wb[0]+.5*Wb[1]); dot(ax, *m)
for P, s, dy in ((V[0], r'$0$', -.1), (V[1], r'$1$', -.1), (V[2], r'$\mathrm{e}$', .03)):
    lab(ax, P[0], P[1]+dy, s, MUTED, ha='center')
ax = axs[1]
R = np.array([bary(w) for w in W3]); poly = np.vstack([R, R[:1]])
ax.fill(poly[:, 0], poly[:, 1], color=BLUE_FILL, lw=0); ax.plot(poly[:, 0], poly[:, 1], color=BLUE, lw=1.4)
off = [(.1, -.06), (.07, -.06), (.0, .05)]
for k, P in enumerate(R):
    dot(ax, *P, color=BLUE)
    lab(ax, P[0]+off[k][0], P[1]+off[k][1], r'$W_%d$' % k, BLUE, ha='center', fontsize=8)
qm = np.ones(3)/3; m = bary(qm @ W3); dot(ax, *m)
for P, s, dy in ((V[0], r'$0$', -.1), (V[1], r'$1$', -.1), (V[2], r'$2$', .03)):
    lab(ax, P[0], P[1]+dy, s, MUTED, ha='center')
tags(fig, axs)
save(fig, HERE, 'figure', {'bec_eps': BEC_E, 'W3': W3.tolist(), 'uniform_output_W3': (qm @ W3).tolist()})
