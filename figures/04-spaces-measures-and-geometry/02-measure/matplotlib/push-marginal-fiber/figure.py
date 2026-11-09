from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# p(x,z)=x+z on [0,1]^2; fiber at x0=0.3; p1(x)=x+1/2; mass of [0,1/2]=3/8.
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.27, wspace=.3)
a, b, c = axes
x0 = .3
for lev in (.5, 1, 1.5):
    if lev <= 1: X = [0, lev]; Z = [lev, 0]
    else: X = [lev-1, 1]; Z = [1, lev-1]
    a.plot(X, Z, color=MUTED, lw=.85, ls=(0, (2, 1.5)))
for lev, xx, zz in ((.5, .12, .46), (1, .4, .68), (1.5, .72, .86)):
    a.text(xx, zz, f'{lev:g}', color=MUTED, fontsize=7.5, ha='left', va='bottom')
a.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=BLUE, lw=.95)
a.plot([x0, x0], [0, 1], color=BLUE, lw=2.0)
a.set_xlim(-.03, 1.05); a.set_ylim(-.03, 1.05); a.set_aspect('equal', adjustable='box')
a.set_xticks([0, x0, 1]); a.set_xticklabels(['0', '0.3', '1']); a.set_yticks([0, 1]); a.set_xlabel('$x$', labelpad=1); a.set_ylabel('$z$', labelpad=-4)
z = np.linspace(0, 1, 100)
b.fill_between(z, 0, x0+z, color=BLUE_FILL, lw=0)
b.plot(z, x0+z, color=BLUE, lw=1.4); b.plot([0, 0], [0, x0], color=BLUE, lw=.85); b.plot([1, 1], [0, 1.3], color=BLUE, lw=.85)
b.set_xlim(-.03, 1.05); b.set_ylim(0, 1.5); b.set_xticks([0, 1]); b.set_yticks([0, .3, 1.3]); b.set_yticklabels(['0', '0.3', '1.3']); b.set_xlabel('$z$', labelpad=1)
b.text(.5, .35, '$0.8$', color=INK, ha='center')
t = np.linspace(0, 1, 100); s = np.linspace(0, .5, 60)
c.fill_between(s, 0, s+.5, color=YELLOW_FILL, lw=0)
c.plot(t, t+.5, color=GREEN, lw=1.4); c.plot([0, 0], [0, .5], color=GREEN, lw=.85); c.plot([1, 1], [0, 1.5], color=GREEN, lw=.85); c.plot([.5, .5], [0, 1], color=YELLOW, lw=.85)
c.plot([x0], [.8], 'o', ms=3.6, color=BLUE, mew=0, zorder=5)
c.plot([0, x0], [.8, .8], color=MUTED, lw=.85, ls=(0, (2, 1.5))); c.plot([x0, x0], [0, .8], color=MUTED, lw=.85, ls=(0, (2, 1.5)))
c.set_xlim(-.03, 1.05); c.set_ylim(0, 1.7); c.set_xticks([0, x0, .5, 1]); c.set_xticklabels(['0', '0.3', '0.5', '1']); c.set_yticks([.5, .8, 1.5]); c.set_yticklabels(['0.5', '0.8', '1.5']); c.set_xlabel('$x$', labelpad=1)
c.text(.68, 1.35, '$p_1$', color=INK)
for ax, s_ in zip(axes, ('(a)', '(b)', '(c)')):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, .03, s_, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'p=x+z; fiber x0=0.3; integral 0.8; p1=x+1/2; mass[0,1/2]=3/8'})
