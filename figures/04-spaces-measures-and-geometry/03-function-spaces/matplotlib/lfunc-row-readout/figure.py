from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# 三种读取作用于 f(t)=t^2：g=1 给 1/3，g=t 给 1/4，t0=2/3 处取值 4/9。
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.97, bottom=.235, wspace=.14)
t = np.linspace(0, 1, 500)
f = t**2
for a in axes:
    a.set_xlim(0, 1.04); a.set_ylim(0, 1.2)
    a.set_xticks([0, 1]); a.set_yticks([0, 1])
a = axes[0]
a.fill_between(t, 0, f, color=YELLOW_FILL, lw=0)
a.plot(t, np.ones_like(t), color=GREEN, lw=1.4); a.plot(t, f, color=BLUE, lw=1.4)
a.text(.38, 1.04, '$g=1$', color=INK, ha='center', va='bottom'); a.text(.72, .26, '$f$', ha='center', color=INK); a.text(.66, .09, r'$\frac{1}{3}$', ha='center', color=INK)
a = axes[1]
a.fill_between(t, 0, t*f, color=YELLOW_FILL, lw=0)
a.plot(t, t, color=GREEN, lw=1.4); a.plot(t, f, color=BLUE, lw=1.4)
a.plot(t, t*f, color=YELLOW, lw=1.0)
a.text(.38, .47, '$g=t$', ha='center', va='bottom'); a.text(.87, .55, '$f$', ha='center'); a.text(.66, .05, r'$\frac{1}{4}$', ha='center'); 
a = axes[2]
a.plot(t, f, color=BLUE, lw=1.4)
x0 = 2/3
a.plot([x0, x0], [0, 1.13], color=GREEN, lw=1.4)
a.plot([0, x0], [x0**2, x0**2], color=MUTED, lw=.85, ls=(0, (3, 2)))
a.plot([x0], [x0**2], 'o', color=BLUE, ms=4.2, mew=0, zorder=4)
a.set_xticks([0, x0, 1]); a.set_xticklabels(['0', r'$\frac{2}{3}$', '1'])
a.set_yticks([0, 4/9, 1]); a.set_yticklabels(['0', r'$\frac{4}{9}$', '1'])
a.tick_params(axis='y', labelleft=True)
a.text(.48, .63, '单点', ha='center', color=INK); a.text(.92, .55, '$f$', ha='center')
for ax, s in zip(axes, '(a) (b) (c)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f(t)=t^2; int f=1/3; int t f=1/4; f(2/3)=4/9'})
