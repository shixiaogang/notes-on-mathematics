from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Deterministic post-processing of the running example.
# (a) original P,Q on {0,1,2}: TV 0.3, KL 0.2773.
# (b) merge 1 and 2 into one label: P->(0.6,0.4), Q->(0.3,0.7): TV 0.3, KL 0.1920.
# (c) merge 0 and 2: P->(0.7,0.3), Q->(0.7,0.3): every divergence is 0.
p, q = P_EX, Q_EX
cases = [(['0', '1', '2'], p, q),
         (['0', r'$\{1,2\}$'], np.array([.6, .4]), np.array([.3, .7])),
         ([r'$\{0,2\}$', '1'], np.array([.7, .3]), np.array([.7, .3]))]
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.09, right=.99, top=.95, bottom=.28, wspace=.25)
facts = {}
for ax, (labels, a, b) in zip(axs, cases):
    xs = np.arange(len(a))
    bars(ax, xs, a, BLUE, BLUE_FILL, width=.34, offset=-.18)
    bars(ax, xs, b, YELLOW, YELLOW_FILL, width=.34, offset=.18)
    for xi, ai, bi in zip(xs, a, b):
        lab(ax, xi-.18, ai+.02, f'{ai:.1f}', BLUE, ha='center', fontsize=6.5)
        lab(ax, xi+.18, bi+.02, f'{bi:.1f}', YELLOW, ha='center', fontsize=6.5)
    ax.set_xticks(xs); ax.set_xticklabels(labels)
    ax.set_xlim(-.6, len(a)-.4); ax.set_ylim(0, .82); ax.set_yticks([0, .4, .8])
    facts[str(labels)] = {'TV': float(.5*np.abs(a-b).sum()), 'KL': kl(a, b)}
axs[0].set_ylabel('概率', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', facts)
