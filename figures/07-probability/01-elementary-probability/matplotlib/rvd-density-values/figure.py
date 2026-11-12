from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: density heights are not probabilities.
# (a) f=2 on (0,1/2): P(0.1<X<=0.3)=0.4. (b) f=6x(1-x) on (0,1): P(X<=1/3)=7/27. (c) f=1/(2 sqrt x) on (0,1]: P(X<=1/4)=1/2.
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
ax = axs[0]; style(ax)
ax.fill_between([.1, .3], 0, 2, color=BLUE_FILL, lw=0)
ax.plot([-.15, 0], [0, 0], color=BLUE, lw=1.4); ax.plot([0, 0], [0, 2], color=BLUE, lw=.85, ls=':')
ax.plot([0, .5], [2, 2], color=BLUE, lw=1.4); ax.plot([.5, .5], [0, 2], color=BLUE, lw=.85, ls=':')
ax.plot([.5, .75], [0, 0], color=BLUE, lw=1.4)
ax.axhline(1, color=LINE, lw=.85, ls='--')
ax.text(.2, 1.3, '0.4', ha='center', fontsize=7.5)
ax.set_xlim(-.15, .75); ax.set_ylim(0, 3.2); ax.set_xticks([0, .25, .5]); ax.set_xticklabels(['0', '1/4', '1/2']); ax.set_yticks([0, 1, 2, 3])
ax.set_ylabel('密度')
sub(ax, 'a', '$x$')
ax = axs[1]; style(ax)
x = np.linspace(0, 1, 400); f = 6*x*(1-x)
m = x <= 1/3
ax.fill_between(x[m], 0, f[m], color=BLUE_FILL, lw=0)
ax.plot(x, f, color=BLUE, lw=1.4)
ax.axhline(1, color=LINE, lw=.85, ls='--')
ax.text(.2, .3, '7/27', ha='center', fontsize=7.5)
ax.set_xlim(-.05, 1.05); ax.set_ylim(0, 3.2); ax.set_xticks([0, 1/3, 1]); ax.set_xticklabels(['0', '1/3', '1']); ax.set_yticks([0, 1, 1.5, 3])
sub(ax, 'b', '$x$')
ax = axs[2]; style(ax)
x = np.linspace(1e-4, 1, 2000); f = 1/(2*np.sqrt(x))
m = x <= .25
ax.fill_between(x[m], 0, np.minimum(f[m], 3.2), color=BLUE_FILL, lw=0)
ax.plot(x, f, color=BLUE, lw=1.4, clip_on=True)
ax.axhline(1, color=LINE, lw=.85, ls='--')
ax.text(.125, .3, '1/2', ha='center', fontsize=7.5)
ax.set_xlim(-.05, 1.05); ax.set_ylim(0, 3.2); ax.set_xticks([0, .25, 1]); ax.set_xticklabels(['0', '1/4', '1']); ax.set_yticks([0, .5, 1, 3])
sub(ax, 'c', '$x$')
save(fig, HERE(__file__), 'figure', {'a': 0.4, 'b': 7/27, 'c': 0.5})
