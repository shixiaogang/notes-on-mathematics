"""Reference measure changes the maximum-entropy answer on [1,e] without moment constraints.
Reference dx (Lebesgue): uniform density 1/(e-1) (blue).
Reference dx/x (Lebesgue in y=ln x): density 1/x on [1,e] (yellow), i.e. Y=ln X ~ Unif(0,1).
Red points mark the medians: (1+e)/2 = 1.859 and sqrt(e) = 1.649."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

e = math.e
x = np.linspace(1, e, 400)
fig, ax = figure(width_mm=78, height_mm=44)
ax.plot([0.8, 1, 1, e, e, 2.9], [0, 0, 1/(e-1), 1/(e-1), 0, 0], color=BLUE, lw=1.4)
ax.plot(np.r_[0.8, 1, x, e, 2.9], np.r_[0, 0, 1/x, 0, 0], color=YELLOW, lw=1.5)
ax.scatter([(1+e)/2, math.sqrt(e)], [0, 0], s=16, color=RED, zorder=5, clip_on=False)
ax.text(2.2, 1/(e-1)+0.04, r'$\mathrm{d}x$', color=BLUE, fontsize=7.5, ha='left', va='bottom')
ax.text(1.06, 0.97, r'$\mathrm{d}x/x$', color=YELLOW, fontsize=7.5, ha='left', va='bottom')
ax.set_xlim(0.8, 2.9); ax.set_ylim(0, 1.15)
ax.set_xticks([1, 1.5, 2, 2.5, e]); ax.set_xticklabels(['1', '1.5', '2', '2.5', r'$\mathrm{e}$'])
ax.set_xlabel(r'$x$', labelpad=1)
save(fig, HERE, 'figure', {'uniform_density': 1/(e-1), 'median_uniform': (1+e)/2, 'median_log_uniform': math.sqrt(e)})
