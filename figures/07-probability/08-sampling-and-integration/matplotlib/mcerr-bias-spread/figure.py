from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Target I = E[X] = 1 for X ~ Exp(1), estimate = mean of N = 20 generated values, 20000 replications (seed 3101).
# (a) exact inverse-quantile generator X = -ln(1-U); (b) generator clipped at T = 2, X~ = min(X, 2),
# whose mean is 1 - e^{-2}.  Histograms of the estimate (green), true I (blue), mean of estimate (red).
N, R, T = 20, 20000, 2.0
rng = np.random.default_rng(3101)
X = -np.log1p(-rng.random((R, N)))
est = [X.mean(1), np.minimum(X, T).mean(1)]
fig, axes = figure(width_mm=112, height_mm=46, ncols=2, sharey=True)
panel(fig, left=.07, right=.98, bottom=.3, top=.95, wspace=.12)
bins = np.linspace(0.3, 1.9, 49)
for ax, e in zip(axes, est):
    h, b = np.histogram(e, bins=bins, density=True)
    ax.bar(b[:-1], h, width=b[1]-b[0], align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.5)
    ax.plot([1, 1], [0, 3.0], color=BLUE, lw=1.3)
    m = e.mean(); ax.plot([m, m], [0, 3.0], color=RED, lw=1.0, ls=DASH); dot(ax, m, 3.0)
    ax.set_xlim(.3, 1.9); ax.set_ylim(0, 3.75); ax.set_yticks([0, 1, 2]); axlab(ax, r'$\hat I_{N}$')
    lab(ax, 1.04, 2.75, '$I=1$', BLUE)
axes[1].annotate('', xy=(est[1].mean(), 3.2), xytext=(1, 3.2), arrowprops=dict(arrowstyle='<->', color=RED, lw=.8, shrinkA=0, shrinkB=0))
lab(axes[1], 0.45, 3.0, r'$\mathrm{E}[\hat I_{N}]$', RED)
lab(axes[0], 0.45, 3.0, r'$\mathrm{E}[\hat I_{N}]$', RED)
lab(axes[1], 0.93, 3.3, '偏差', RED, ha='center', va='bottom')
tags(fig, axes)
save(fig, HERE, 'figure', {'N': N, 'R': R, 'mean_exact': float(est[0].mean()), 'sd_exact': float(est[0].std()),
     'mean_clip': float(est[1].mean()), 'sd_clip': float(est[1].std()), 'clip_mean_theory': 1-np.exp(-2)})
