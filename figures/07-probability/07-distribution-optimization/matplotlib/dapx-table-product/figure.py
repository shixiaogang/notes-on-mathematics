from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# (a) target table PI2 on {0,1}^2; (b) product of its marginals (both uniform) = 0.25 everywhere.
pi = PI2
m1 = pi.sum(1); m2 = pi.sum(0); prod = np.outer(m1, m2)
fig, axs = figure(width_mm=84, height_mm=42, ncols=2)
panel(fig, left=.1, right=.97, top=.8, bottom=.17, wspace=.45)
for ax, T in zip(axs, (pi, prod)):
    table_heat(ax, T, fmt='{:.2f}', vmax=.5)
    ax.set_xlabel('$x_2$', labelpad=1); ax.set_ylabel('$x_1$', labelpad=1)
    ax.xaxis.set_label_position('top'); ax.xaxis.tick_top()
tags(fig, axs)
save(fig, HERE, 'figure', {'pi': pi.tolist(), 'marginals': [m1.tolist(), m2.tolist()], 'product': prod.tolist(),
                           'mutual_information_nat': kl(pi.ravel(), prod.ravel())})
