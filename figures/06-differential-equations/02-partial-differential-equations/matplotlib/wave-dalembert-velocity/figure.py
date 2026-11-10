from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: the velocity contribution of d'Alembert with c=1 for the indicator of (-1,1).
fig, axs = figure(width_mm=112, height_mm=42, ncols=3, sharey=True)
x = np.linspace(-5.5, 5.5, 2201)
for ax, t, l in zip(axs, [.5, 1, 3], 'abc'):
    style(ax)
    ax.plot(x, box(x), color=RED, lw=1.1, ls=(0, (3, 2)))
    ax.plot(x, wave_box(x, t), color=BLUE, lw=1.5)
    ax.text(5.3, 1.1, f'$t={t:g}$', ha='right')
    ax.set_xlim(-5.5, 5.5); ax.set_ylim(0, 1.25); ax.set_xticks([-4, 0, 4]); ax.set_yticks([0, .5, 1])
    sub(ax, l, '$x$')
save(fig, HERE(__file__), 'figure', {'formula': 'u=(1/2)|(x-t,x+t) cap (-1,1)|, c=1'})
