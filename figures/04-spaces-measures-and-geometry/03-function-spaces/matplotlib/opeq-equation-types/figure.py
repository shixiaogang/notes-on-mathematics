from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Multipliers: T: 1,1/3,0,0,0; I-T/2: 1/2,5/6,1,1,1 on e_1=1, e_2=sqrt3 x, h_1,h_2,h_3.
fig, ax = figure(width_mm=86, height_mm=44)
lab = ['$e_1$', '$e_2$', '$h_1$', '$h_2$', '$h_3$']
T = [1, 1/3, 0, 0, 0]; S = [.5, 5/6, 1, 1, 1]; tt = ['1', '1/3', '0', '0', '0']; st = ['1/2', '5/6', '1', '1', '1']
x = np.arange(5); w = .34
ax.bar(x-w/2, T, w, color=BLUE, lw=0, label='$T$')
ax.bar(x+w/2, S, w, color=GREEN_FILL, edgecolor=GREEN, lw=.85, label='$I-\\frac{1}{2}T$')
for i in range(5):
    ax.text(x[i]-w/2, T[i]+.03, tt[i], ha='center', va='bottom', fontsize=7.5)
    ax.text(x[i]+w/2, S[i]+.03, st[i], ha='center', va='bottom', fontsize=7.5)
ax.set_xticks(x); ax.set_xticklabels(lab); ax.set_yticks([0, .5, 1]); ax.set_ylim(0, 1.32); ax.set_xlim(-.6, 4.6)
ax.tick_params(axis='x', length=0)
ax.legend(loc='upper center', ncol=2, handlelength=1.0, handleheight=.8, columnspacing=1.4, bbox_to_anchor=(.5, 1.05), borderaxespad=0)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'T e1=e1, T e2=e2/3, T h=0; I-T/2 multipliers 1-mu/2'})
