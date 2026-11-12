from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# Running example: a=(0.5,0.3,0.2) at x=0,1,2 (rows); b=(0.2,0.3,0.5) at y=0,1,2 (columns); c=(x-y)^2.
# (a) independent coupling a b^T, cost 1.58; (b) jump plan, cost 1.2; (c) monotone plan, cost 0.6.
a, b, C = A_EX, B_EX, C_EX
plans = [np.outer(a, b), PI_JUMP, PI_OPT]
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.06, right=.99, top=.88, bottom=.2, wspace=.38)
facts = []
for ax, P in zip(axs, plans):
    assert np.allclose(P.sum(1), a) and np.allclose(P.sum(0), b)
    heat(ax, P, vmax=.36)
    ax.set_xlabel('$y$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
    facts.append({'plan': P.round(4).tolist(), 'cost': float((C*P).sum())})
tags(fig, axs)
save(fig, HERE, 'figure', {'costs': facts})
