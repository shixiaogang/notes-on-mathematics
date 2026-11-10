from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: odd and even reflection on the half line, c=1, data T(x-3), u1=0.
fig, axs = figure(width_mm=112, height_mm=66, nrows=2, ncols=3, sharex=True, sharey=True)
x = np.linspace(-3.2, 8.5, 2341); tv = [1.5, 3, 4.5]
for r, sg in enumerate([-1, 1]):
    for c, t in enumerate(tv):
        ax = axs[r, c]; style(ax)
        L = .5*tent(x-3+t); R = .5*tent(x-3-t); I = sg*.5*tent(x+3-t)
        ax.plot(x, L, color=PURPLE, lw=1.1, ls=(0, (3, 2)))
        ax.plot(x, I, color=YELLOW, lw=1.5, ls=(0, (3, 2)))
        m = x >= 0
        ax.plot(x[m], (L+R+I)[m], color=BLUE, lw=1.5)
        ax.axvline(0, color=LINE, lw=1.7)
        ax.text(8.3, 1.02, f'$t={t:g}$', ha='right')
        ax.set_xlim(-3.2, 8.5); ax.set_ylim(-.7, 1.22); ax.set_xticks([0, 3, 6]); ax.set_yticks([-.5, 0, .5, 1])
        sub(ax, 'abcdef'[r*3+c], '$x$')
save(fig, HERE(__file__), 'figure', {'formula': 'u=(T(x-3+t)+T(x-3-t))/2 + s T(x+3-t)/2, s=-1 fixed, s=+1 free, on x>=0'})
