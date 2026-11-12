"""Y~Unif(-1,1), X=1{Y>0}: y->K(y,{1}) is 0 for y<0 and 1 for y>0; the value at y=0 is free."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
from matplotlib.colors import LinearSegmentedColormap
HERE = Path(__file__).resolve().parent
fig, a = figure(width_mm=72, height_mm=40)
a.plot([-1, 0], [0, 0], color=BLUE, lw=1.4); a.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
a.plot([0, 0], [0, 1], color=RED, lw=1.2, ls=DASH)
for v in (0, 1):
    a.scatter([0], [v], s=16, facecolor='white', edgecolor=BLUE, lw=0.9, zorder=4)
a.set_xlim(-1, 1); a.set_ylim(-0.08, 1.12); a.set_xticks([-1, 0, 1]); a.set_yticks([0, 1])
a.set_xlabel('$y$', labelpad=1); a.set_ylabel('$K(y,\\{1\\})$')
save(fig, HERE, 'figure', {'model': 'Y~Unif(-1,1), X=1{Y>0}'})
