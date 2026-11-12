from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# mu_0 = N(-2, 0.5^2) (blue), mu_1 = N(2, 1) (yellow). Squared cost on the line.
# (a) displacement interpolation mu_t = N((1-t)(-2)+2t, ((1-t)0.5+t)^2), t = 0.25, 0.5, 0.75 (green);
# (b) mixtures (1-t) mu_0 + t mu_1 at the same t (green).  W_2(mu_0,mu_1)^2 = 16 + 0.25 = 16.25.
xs = np.linspace(-4, 5, 900)
def npdf(x, m, s): return np.exp(-(x-m)**2/(2*s*s))/(s*np.sqrt(2*np.pi))
fig, axs = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
panel(fig, left=.06, right=.99, top=.96, bottom=.3, wspace=.1)
for ax in axs:
    ax.plot(xs, npdf(xs, -2, .5), color=BLUE, lw=1.4)
    ax.plot(xs, npdf(xs, 2, 1), color=YELLOW, lw=1.6)
    ax.set_xlim(-4, 5); ax.set_ylim(0, .85); ax.set_xticks([-2, 0, 2]); ax.set_xlabel('$x$', labelpad=1)
lt = {.25: (0, (5, 1.5)), .5: '-', .75: (0, (1.5, 1.2))}
for t, ls in lt.items():
    m, s = (1-t)*(-2)+2*t, (1-t)*.5+t
    axs[0].plot(xs, npdf(xs, m, s), color=GREEN, lw=1.2, ls=ls)
    axs[1].plot(xs, (1-t)*npdf(xs, -2, .5)+t*npdf(xs, 2, 1), color=GREEN, lw=1.2, ls=ls)
    axs[0].text(m, npdf(m, m, s)+.03, f'{t}', color=GREEN, fontsize=7, ha='center')
axs[0].set_yticks([0, .4, .8])
tags(fig, axs)
save(fig, HERE, 'figure', {'W2sq': 16.25})
