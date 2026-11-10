from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: the same curvature means acceleration for the wave equation and velocity for the heat equation.
fig, axs = figure(width_mm=112, height_mm=44, ncols=3, sharey=True)
x = np.linspace(-4, 4, 1201); B = lambda x: np.exp(-x**2)
ax = axs[0]; style(ax)
ax.plot(x, B(x), color=RED, lw=1.5)
for p in [-1.6, -.9, 0, .9, 1.6]:
    a = (4*p**2-2)*B(p)
    ax.annotate('', xy=(p, B(p)+.28*a), xytext=(p, B(p)), arrowprops=dict(arrowstyle='-|>', color=PURPLE, lw=1, mutation_scale=7, shrinkA=0, shrinkB=0))
ax.set_xlim(-3, 3); ax.set_ylim(-.45, 1.15); ax.set_ylabel('$u$'); sub(ax, 'a', '$x$')
ax = axs[1]; style(ax)
ax.plot(x, B(x), color=RED, lw=1.3)
def heat(x, t):
    return np.exp(-x**2/(1+4*t))/np.sqrt(1+4*t)
for t, col in zip([.05, .2, .6], SHADES[1:]):
    ax.plot(x, heat(x, t), color=col, lw=1.4)
ax.set_xlim(-3, 3); sub(ax, 'b', '$x$')
ax = axs[2]; style(ax)
ax.plot(x, B(x), color=RED, lw=1.3)
for t, col in zip([.3, .8, 1.8], SHADES[1:]):
    ax.plot(x, .5*(B(x-t)+B(x+t)), color=col, lw=1.4)
ax.set_xlim(-3.6, 3.6); ax.set_xticks([-2, 0, 2]); sub(ax, 'c', '$x$')
save(fig, HERE(__file__), 'figure', {'formula': 'B=exp(-x^2); heat exp(-x^2/(1+4t))/sqrt(1+4t); wave (B(x-t)+B(x+t))/2; arrows 0.28 c^2 B'})
