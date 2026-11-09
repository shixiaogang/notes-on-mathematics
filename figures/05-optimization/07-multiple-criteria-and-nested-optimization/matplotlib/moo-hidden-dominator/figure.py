from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Four mutually non-dominated candidates and an unseen point that dominates C.
fig, ax = figure(width_mm=78, height_mm=56)
setup(ax, (0, 8), (0, 9.5), range(0, 9, 2), range(0, 10, 2))
P = (3, 3); ax.fill([P[0], 8, 8, P[0]], [P[1], P[1], 9.5, 9.5], color=RED_FILL, lw=0, zorder=1)
cands(ax, 'ABCD', off={'A': (.2, .15), 'B': (.2, .25), 'C': (.2, .2), 'D': (.15, .3)})
hollow(ax, P, RED, ms=5.2); ax.text(2.6, 2.3, '$P$', color=RED)
arrow(ax, CANDS['C'], (3.1, 3.1), RED, lw=.95, ms=6)
save(fig, HERE, 'figure', {'P': P})
