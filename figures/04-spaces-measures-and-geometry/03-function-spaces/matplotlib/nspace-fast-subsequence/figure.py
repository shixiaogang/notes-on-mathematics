from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Telescoping series: F_1=sin(2 pi x)/2, F_(k+1)=F_k+2^(-k) sin(2^(k+1) pi x); S_m=|F_1|+sum_{k<=m}|F_(k+1)-F_k|.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.3, wspace=.2)
x = np.linspace(0, 1, 3000)
F = [.5*np.sin(2*np.pi*x)]; D = []
for k in range(1, 10):
    d = 2.**(-k)*np.sin(2**(k+1)*np.pi*x); D.append(d); F.append(F[-1]+d)
S = lambda m: abs(F[0])+sum(abs(d) for d in D[:m])
ax = axes[0]
for i, c in ((0, BLUE), (2, GREEN), (9, YELLOW)):
    ax.plot(x, F[i], color=c, lw=1.2 if i == 9 else 1.4)
ax.annotate('$f_{n_1}$', xy=(.42, .24), xytext=(.46, .95), ha='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.85))
ax.annotate('$f_{n_3}$', xy=(.1, .87), xytext=(.05, 1.22), ha='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.85))
ax.annotate('$f_{n_{10}}$', xy=(.9, -.8), xytext=(.72, -1.27), ha='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.85))
ax.set_xlim(0, 1); ax.set_ylim(-1.4, 1.5); ax.set_xticks([0, .5, 1]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
for m, c in ((0, BLUE), (2, GREEN), (9, YELLOW)):
    ax.plot(x, S(m), color=c, lw=1.2 if m == 9 else 1.4)
ax.text(.13, .5, '$S_0$', ha='left'); ax.annotate('$S_2$', xy=(.09, .85), xytext=(.05, 1.5), ha='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.85))
ax.annotate('$S_9$', xy=(.33, 1.28), xytext=(.42, 1.58), ha='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.85))
ax.set_xlim(0, 1); ax.set_ylim(0, 1.75); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F1=.5 sin(2 pi x); increments 2^-k sin(2^(k+1) pi x), k=1..9; S_m=|F1|+sum|inc|'})
