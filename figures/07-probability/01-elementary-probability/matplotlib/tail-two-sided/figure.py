from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'tail-common'))
from tail_fig import *
# X ~ Exp(1), mean 1, deviation t=0.5: P(|X-1|>=0.5) = (1-e^{-0.5}) + e^{-1.5}.
x = np.linspace(0, 5, 1001); f = np.exp(-x)
fig, ax = figure(width_mm=90, height_mm=46)
L = x <= .5; R = x >= 1.5
ax.fill_between(x[L], 0, f[L], color=BLUE_FILL, lw=0)
ax.fill_between(x[R], 0, f[R], color=BLUE_FILL, lw=0)
ax.plot(x, f, color=BLUE, lw=1.4)
for v in (.5, 1.5):
    ax.plot([v, v], [0, np.exp(-v)], color=BLUE, lw=.85)
ax.plot([1, 1], [0, 1.02], color=RED, lw=1.2)
lab(ax, 1, 1.05, r'$\mu=1$', RED, ha='center', va='bottom')
ax.annotate('', xy=(.5, .08), xytext=(1, .08), arrowprops=dict(arrowstyle='<->', color=STROKE, lw=.85, shrinkA=0, shrinkB=0))
ax.annotate('', xy=(1.5, .08), xytext=(1, .08), arrowprops=dict(arrowstyle='<->', color=STROKE, lw=.85, shrinkA=0, shrinkB=0))
lab(ax, .75, .11, '$0.5$', MUTED, ha='center', va='bottom'); lab(ax, 1.25, .11, '$0.5$', MUTED, ha='center', va='bottom')
pl = 1-np.exp(-.5); pr = np.exp(-1.5)
lab(ax, .25, .3, '%.4f' % pl, INK, ha='center')
lab(ax, 2.1, .2, '%.4f' % pr, INK, ha='left')
ax.set_xlim(0, 5); ax.set_ylim(0, 1.18); ax.set_xticks([0, .5, 1, 1.5, 2, 3, 4, 5]); ax.set_xticklabels(['0', '0.5', '1', '1.5', '2', '3', '4', '5']); ax.set_yticks([0, .5, 1])
axlab(ax, '$x$', '$f_X(x)$')
save(fig, HERE, 'figure', {'left': float(pl), 'right': float(pr), 'total': float(pl+pr)})
