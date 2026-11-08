from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# (a) x^(4) truncation of (1/k) ; (b) g_n(x)=clip(n x,-1,1), n=2,8; ||g_n-sgn||^2=2/(3n)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.3, wspace=.22)
ax = axes[0]
k = np.arange(1, 13)
ax.vlines(k, 0, 1/k, color=BLUE, lw=.85); ax.plot(k, 1/k, 'o', ms=3.6, mfc='white', mec=BLUE, mew=.85)
k4 = np.arange(1, 5)
ax.plot(k4, 1/k4, 'o', ms=3.8, color=GREEN, mew=0)
ax.plot(np.arange(5, 13), 0*np.arange(5, 13), 'o', ms=3.2, color=GREEN, mew=0)
ax.text(1.5, .88, '$x^{(4)}$', color=INK); ax.text(6.6, .24, '$(1/k)$', color=INK)
ax.axhline(0, color=MUTED, lw=.85)
ax.set_xlim(.3, 12.7); ax.set_ylim(-.06, 1.12); ax.set_xticks([1, 4, 8, 12]); ax.set_yticks([0, 1]); ax.set_xlabel('$k$', labelpad=0)
ax = axes[1]
x = np.linspace(-1, 1, 2001)
g = lambda n: np.clip(n*x, -1, 1)
s = np.sign(x)
ax.fill_between(x, g(2), s, color=RED_FILL, lw=0)
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(x, g(2), color=GREEN, lw=1.4); ax.plot(x, g(8), color=YELLOW, lw=1.4)
ax.plot([-1, 0], [-1, -1], color=BLUE, lw=1.4); ax.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
ax.text(.55, 1.09, r'$\mathrm{sgn}$', color=INK); ax.text(.26, .2, '$g_2$', color=INK); ax.text(-.2, .62, '$g_8$', color=INK)
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.2, 1.3); ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_xticklabels(['-1', '-1/2', '0', '1/2', '1']); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x^(4) truncates (1/k); g_n=clip(nx,-1,1); ||g_n-sgn||_2^2=2/(3n)'})
