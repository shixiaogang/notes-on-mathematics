from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：dx/dt=-x+sin t 的解族都被同一个特解吸引；x0=2 的解分解为瞬态与特解。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .075, .985, .96, .25, .28)
a, b = axes
xlim, ylim = (0, 10), (-2.4, 2.4)
a.set_xlim(*xlim); a.set_ylim(*ylim)
field(a, lambda t, x: -x+np.sin(t), xlim, ylim, nx=20, ny=11)
t = np.linspace(0, 10, 500)
xp = (np.sin(t)-np.cos(t))/2
for x0 in (-2, -1, 0, 1, 2):
    a.plot(t, (x0+.5)*np.exp(-t)+xp, color=BLUE, lw=MAIN, zorder=3)
    a.plot([0], [x0], 'o', ms=3.6, color=RED, mew=0, zorder=5, clip_on=False)
a.plot(t, xp, color=YELLOW, lw=1.7, zorder=4)
a.text(8.05, -1.25, '$x_{\\mathrm{p}}$', color=YELLOW)
label(a, '$t$', '$x$'); a.set_xticks([0, 5, 10]); a.set_yticks([-2, 0, 2])
x0 = 2
b.plot(t, (x0+.5)*np.exp(-t)+xp, color=BLUE, lw=MAIN)
b.plot(t, xp, color=YELLOW, lw=1.5)
b.plot(t, (x0+.5)*np.exp(-t), color=PURPLE, lw=1.2, ls=(0, (4, 2)))
b.plot([0], [2], 'o', ms=3.8, color=RED, mew=0, clip_on=False, zorder=5)
b.axhline(0, color=GRID, lw=.6, zorder=0)
b.text(1.3, 1.75, '$x$', color=BLUE)
b.text(1.5, .76, '$2.5\\mathrm{e}^{-t}$', color=PURPLE)
b.text(7.2, 1.0, '$x_{\\mathrm{p}}$', color=YELLOW)
b.set_xlim(0, 10); b.set_ylim(-1.0, 2.6); b.set_xticks([0, 5, 10]); b.set_yticks([-1, 0, 1, 2]); label(b, '$t$', '')
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': 'x=(x0+1/2)e^-t+(sin t-cos t)/2', 'x0': [-2, -1, 0, 1, 2]})
