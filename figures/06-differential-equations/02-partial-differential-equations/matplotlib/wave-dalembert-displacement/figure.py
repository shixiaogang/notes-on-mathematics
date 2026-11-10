from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: d'Alembert for the tent with c=1, showing the left- and right-going halves.
fig, axs = figure(width_mm=112, height_mm=64, nrows=2, ncols=2, sharex=True, sharey=True)
x = np.linspace(-4, 4, 1601)
for ax, t, l in zip(axs.flat, [0, .5, 1, 2], 'abcd'):
    style(ax)
    ax.plot(x, .5*tent(x-t), color=PURPLE, lw=1.1, ls=(0, (3, 2)))
    ax.plot(x, .5*tent(x+t), color=YELLOW, lw=1.5, ls=(0, (3, 2)))
    ax.plot(x, wave_tent(x, t), color=RED if t == 0 else BLUE, lw=1.5)
    ax.text(3.9, .84, f'$t={t:g}$', ha='right')
    ax.set_xlim(-4, 4); ax.set_ylim(0, 1.08); ax.set_xticks([-3, -1, 1, 3]); ax.set_yticks([0, .5, 1])
    sub(ax, l, '$x$')
save(fig, HERE(__file__), 'figure', {'formula': 'u=(T(x-t)+T(x+t))/2, T=max(1-|x|,0), c=1'})
