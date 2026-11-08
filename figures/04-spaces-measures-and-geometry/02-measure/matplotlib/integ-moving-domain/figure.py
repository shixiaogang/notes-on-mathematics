from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.patches import Rectangle

def labels(fig, axes, y=.03):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)']):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')

# f(x,t)=x t, F(t)=int_0^t x t dx=t^3/2; from t=1 to t=1.25 split interior and boundary gains.
fig, ax = figure(width_mm=88, height_mm=56)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.08, right=.97, top=.97, bottom=.11)
t = 1.0; s = 1.25
x = np.linspace(0, t, 200); xb = np.linspace(t, s, 100)
ax.fill_between(x, 0, t*x, fc=BLUE_FILL, lw=0)
ax.fill_between(x, t*x, s*x, fc=GREEN_FILL, lw=0)
ax.fill_between(xb, 0, s*xb, fc=YELLOW_FILL, lw=0)
ax.plot([0, t], [0, t*t], color=BLUE, lw=1.4)
ax.plot([0, s], [0, s*s], color=GREEN, lw=1.4)
ax.plot([t, t], [0, s*t], color=MUTED, lw=.85, dashes=(3, 2))
ax.plot([s, s], [0, s*s], color=YELLOW, lw=1.2)
ax.text(1.03, 1.02, '', ha='left')
ax.text(.68, .28, '$F(1)$', ha='center', color=INK)
ax.text(1.125, .55, '边界', ha='center', va='center', color=INK, fontsize=7.5)
ax.text(.40, .78, '内部变化', ha='center', color=INK, fontsize=7.5)
ax.annotate('', xy=(.80, .92), xytext=(.48, .86), arrowprops=dict(arrowstyle='-', color=MUTED, lw=.65))
ax.text(.58, .36, '', ha='center')
ax.set_xlim(0, 1.42); ax.set_ylim(0, 1.72); ax.set_xticks([0, t, s]); ax.set_xticklabels(['0', '$t$', '$t+h$']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=-7, loc='right')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f(x,t)=x t, t=1, h=.25; F(1)=.5, interior gain .125, boundary gain .3516, F(1.25)=.9766'})
