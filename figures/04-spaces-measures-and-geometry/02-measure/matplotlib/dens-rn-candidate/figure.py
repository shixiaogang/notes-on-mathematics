from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# f(x)=1.2+0.6 sin(2 pi x); h=min(f,1); eps=0.25; P={f-h>=eps}
fig, ax = figure(width_mm=100, height_mm=56)
x = np.linspace(0, 1, 2001)
f = 1.2 + .6*np.sin(2*np.pi*x)
h = np.minimum(f, 1.0)
eps = .25
P = (f - h) >= eps
ax.fill_between(x, 0, h, color=BLUE_FILL, lw=0)
ax.fill_between(x, h, f, color=YELLOW_FILL, lw=0)
ax.fill_between(x, h, h+eps, where=P, color=GREEN_FILL, lw=0)
ax.plot(x, f, color=RED, lw=1.4, ls=(0, (4, 2)))
ax.plot(x, h, color=BLUE, lw=1.4)
ax.plot(x[P], (h+eps)[P], color=GREEN, lw=1.4)
a = np.arcsin(.05/.6)/(2*np.pi); b = .5 - a
ax.plot([a, b], [0, 0], color=GREEN, lw=3, solid_capstyle='butt', clip_on=False)
ax.text((a+b)/2, .07, r'$P$', ha='center', va='bottom')
ax.text(.25, .55, r'$h$', ha='center', va='center')
ax.text(.285, 1.125, r'$\varepsilon$', ha='center', va='center')
ax.text(.25, 1.87, r'$f$', ha='center', va='center')
ax.text(.27, 1.40, r'$h+\varepsilon\mathbf{1}_P$', ha='center', va='center', color=INK)
ax.set_xlim(0, 1.0); ax.set_ylim(0, 1.95)
ax.set_xticks([a, b, 1]); ax.set_xticklabels([f'{a:.3f}', f'{b:.3f}', '1'])
ax.set_yticks([0, 1, 1.25]); ax.set_yticklabels(['0', '1', '1.25'])
ax.set_xlabel(r'$x$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=1.2+0.6 sin(2 pi x), h=min(f,1), eps=0.25, P={f-h>=eps}', 'P': [float(a), float(b)]})
