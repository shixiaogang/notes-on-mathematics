from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: the first three spatial modes for three boundary combinations on (0,1).
fig, axs = figure(width_mm=112, height_mm=42, ncols=3, sharey=True)
x = np.linspace(0, 1, 401)
modes = [[lambda z: np.sin((n)*np.pi*z) for n in (1, 2, 3)],
         [lambda z: np.ones_like(z), lambda z: np.cos(np.pi*z), lambda z: np.cos(2*np.pi*z)],
         [lambda z: np.sin(.5*np.pi*z), lambda z: np.sin(1.5*np.pi*z), lambda z: np.sin(2.5*np.pi*z)]]
modes[0] = [(lambda n: (lambda z: np.sin(n*np.pi*z)))(n) for n in (1, 2, 3)]
kinds = [('D', 'D'), ('N', 'N'), ('D', 'N')]
for ax, ms, k, l in zip(axs, modes, kinds, 'abc'):
    style(ax)
    for m, col, lw in zip(ms, [BLUE, YELLOW, PURPLE], [1.5, 1.6, 1.3]):
        ax.plot(x, m(x), color=col, lw=lw)
    ax.axhline(0, color=GRID, lw=.85)
    for xe, kk in zip([0, 1], k):
        if kk == 'D':
            ax.plot([xe], [0], 'o', ms=4, color=RED, clip_on=False, zorder=5)
        else:
            ax.plot([xe, xe], [-1.15, 1.15], color=LINE, lw=1.6, clip_on=False)
    ax.set_xlim(0, 1); ax.set_ylim(-1.15, 1.15); ax.set_xticks([0, .5, 1]); sub(ax, l, '$x$')
save(fig, HERE(__file__), 'figure', {'formula': 'DD sin(n pi x); NN cos(n pi x), n=0,1,2; DN sin((n-1/2) pi x)'})
