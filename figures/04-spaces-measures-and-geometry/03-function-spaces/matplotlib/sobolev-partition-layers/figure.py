from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c) (d)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Omega=(0,1), t=dist(x,boundary). eta_j rises on [1/(j+1),1/j], falls on [1/(j-1),1/(j-2)]; zeta_j=eta_j/S. Plotted on (0,1/2].
def sm(s):
    s = np.clip(s, 0, 1); out = np.zeros_like(s)
    i = (s > 0) & (s < 1); a = np.exp(-1/s[i]); b = np.exp(-1/(1-s[i])); out[i] = a/(a+b); out[s >= 1] = 1
    return out
def eta(j, t):
    up = sm((t-1/(j+1))/(1/j-1/(j+1)))
    down = 1-sm((t-1/(j-1))/(1/(j-2)-1/(j-1))) if j > 3 else 1+0*t
    return up*down
x = np.linspace(.002, .5, 4000); J = range(3, 700)
S = sum(eta(j, x) for j in J)
fig, ax = figure(width_mm=112, height_mm=46)
fig.set_layout_engine(None); fig.subplots_adjust(left=.07, right=.98, top=.97, bottom=.21)
cols = [BLUE, GREEN, YELLOW]
for j, c in zip(range(3, 10), cols*3):
    ax.plot(x, eta(j, x)/S, color=c, lw=1.4)
ax.axhline(0, color=MUTED, lw=.85)
for j, xp, yp in [(3, .455, 1.09), (4, .29, .62), (5, .225, .62), (6, .183, .62), (7, .155, .62)]:
    ax.text(xp, yp, f'$\\zeta_{j}$', ha='center')
for j, c in zip(range(3, 10), cols*3):
    e = (1/j-1/(j+1))/2; m = (1/j+1/(j+1))/2
    ax.plot([m-e/2, m+e/2], [-.14, -.14], color=c, lw=2.2, solid_capstyle='butt')
ax.text(.47, -.14, r'$\varepsilon_j$', ha='center', va='center')
ax.set_xlim(0, .5); ax.set_ylim(-.26, 1.25); ax.set_yticks([0, 1])
ax.set_xticks([1/j for j in (2, 3, 4, 5, 6)]+[0]); ax.set_xticklabels(['1/2', '1/3', '1/4', '1/5', '1/6', '0'])
ax.set_xlabel('到边界的距离', labelpad=0)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'partition of unity zeta_j=eta_j/sum eta on (0,1/2]'})
