from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# 三个变换对：方框—sinc，双边指数—2/(1+4 pi^2 xi^2)，Gauss—Gauss。
fig, axes = figure(width_mm=112, height_mm=66, nrows=2, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.99, top=.97, bottom=.2, wspace=.2, hspace=.42)
x = np.linspace(-2.2, 2.2, 1500); xi = np.linspace(-3.2, 3.2, 1500)
fs = [lambda s: (np.abs(s) <= .5)*1., lambda s: np.exp(-np.abs(s)), lambda s: np.exp(-np.pi*s**2)]
gs = [lambda s: np.sinc(s), lambda s: 2/(1+4*np.pi**2*s**2), lambda s: np.exp(-np.pi*s**2)]
lim = [(-.3, 1.15), (-.1, 2.2), (-.1, 1.15)]
for j in range(3):
    a = axes[0, j]
    if j == 0:
        a.plot([-2.2, -.5, -.5, .5, .5, 2.2], [0, 0, 1, 1, 0, 0], color=BLUE, lw=1.4)
    else:
        a.plot(x, fs[j](x), color=BLUE, lw=1.4)
    a.set_xlim(-2.2, 2.2); a.set_ylim(-.1, 1.15); a.set_xticks([-2, 0, 2]); a.set_yticks([0, 1]); a.set_xlabel('$x$', labelpad=0)
    b = axes[1, j]
    b.axhline(0, color=MUTED, lw=.85)
    b.plot(xi, gs[j](xi), color=GREEN, lw=1.4)
    b.set_xlim(-3.2, 3.2); b.set_ylim(*lim[j]); b.set_xticks([-3, 0, 3]); b.set_yticks([0, 2] if j == 1 else [0, 1]); b.set_xlabel(r'$\xi$', labelpad=0)
tag(fig, axes[1])
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'B<->sinc, exp(-|x|)<->2/(1+4pi^2 xi^2), G<->G'})
