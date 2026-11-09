from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Weighted values of candidates as functions of the weight w on f1; lower envelope.
fig, ax = figure(width_mm=96, height_mm=58)
setup(ax, (0, 1), (0, 9), [0, .25, .5, .75, 1], range(0, 10, 2), '$w$', '加权值')
w = np.linspace(0, 1, 401)
vals = {k: w*v[0]+(1-w)*v[1] for k, v in CANDS.items()}
for k in 'ABD': ax.plot(w, vals[k], color=BLUE, lw=1.0, zorder=2)
ax.plot(w, vals['C'], color=YELLOW, lw=1.6, zorder=3)
for k in 'EF': ax.plot(w, vals[k], color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2)
env = np.min([vals[k] for k in 'ABCDEF'], axis=0); ax.plot(w, env, color=RED, lw=2.2, zorder=4, solid_capstyle='round')
for x in (.5, .75): ax.plot([x, x], [0, 9], color=MUTED, lw=.85, ls=(0, (1, 2)), zorder=1)
for k, (x, y) in {'A': (.05, 7.85), 'B': (.05, 4.4), 'C': (.12, 4.15), 'D': (.1, 1.0), 'E': (.31, 6.05), 'F': (.34, 3.5)}.items(): ax.text(x, y, k, color=INK)
save(fig, HERE, 'figure', {'breaks': [.5, .75]})
