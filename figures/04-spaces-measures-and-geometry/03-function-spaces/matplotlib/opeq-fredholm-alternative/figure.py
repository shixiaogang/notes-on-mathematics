from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Multipliers 1-lambda, 1-lambda/3, 1 and resolvent norm max{1/|1-l|,1/|1-l/3|,1}.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.25, wspace=.24)
L = np.linspace(-1, 4.5, 8001)
ax = axes[0]
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(L, np.ones_like(L), color=YELLOW, lw=1.4)
ax.plot(L, 1-L, color=BLUE, lw=1.4)
ax.plot(L, 1-L/3, color=GREEN, lw=1.4)
for l0 in (1, 3):
    ax.plot([l0], [0], 'o', ms=4.2, mfc='white', mec=INK, mew=.85)
for l0 in (.5, 2):
    ax.plot([l0, l0], [-3.5, 2.2], color=MUTED, lw=.85, ls=(0, (1, 2)))
ax.text(3.5, 1.14, '1', ha='center', fontsize=7.5)
ax.text(-.62, 1.92, '$1-\\lambda$', ha='left', va='bottom', fontsize=7.5, color=INK)
ax.text(3.9, -.62, '$1-\\lambda/3$', ha='center', va='top', fontsize=7.5, color=INK)
ax.text(.5, 2.28, '1/2', ha='center', fontsize=7.5, color=MUTED); ax.text(2, 2.28, '2', ha='center', fontsize=7.5, color=MUTED)
ax.set_xlim(-1, 4.5); ax.set_ylim(-3.5, 2.75); ax.set_xticks([-1, 1, 3]); ax.set_yticks([-2, 0, 2]); ax.set_xlabel('$\\lambda$', labelpad=0)
ax = axes[1]
R = np.maximum.reduce([1/np.abs(1-L+1e-12), 1/np.abs(1-L/3+1e-12), np.ones_like(L)])
for lo, hi in ((-1, .9999), (1.0001, 2.9999), (3.0001, 4.5)):
    m = (L >= lo) & (L <= hi)
    ax.semilogy(L[m], R[m], color=BLUE, lw=1.4)
for l0 in (1, 3):
    ax.axvline(l0, color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.plot([.99], [100], 'o', ms=3.6, color=RED, mew=0)
ax.text(.5, 120, '$\\lambda=0.99$', ha='right', va='bottom', fontsize=7.5)
ax.set_xlim(-1, 4.5); ax.set_ylim(.7, 700); ax.set_xticks([-1, 1, 3]); ax.set_yticks([1, 10, 100]); ax.set_yticklabels(['1', '10', '100']); ax.minorticks_off(); ax.set_xlabel('$\\lambda$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'multipliers 1-lambda mu for mu=1,1/3,0; norm=max 1/|1-lambda mu|'})
