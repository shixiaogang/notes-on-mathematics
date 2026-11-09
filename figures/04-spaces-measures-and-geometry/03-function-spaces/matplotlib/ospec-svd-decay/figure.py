from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Volterra operator on L2(0,1): sigma_k=2/((2k-1)pi), v_k=sqrt2 cos((k-1/2)pi t).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.09, right=.975, top=.96, bottom=.25, wspace=.26)
ax = axes[0]
k = np.arange(1, 11); s = 2/((2*k-1)*np.pi)
print(np.round(s[:6], 4))
ax.vlines(k, 0, s, color=MUTED, lw=.85)
ax.vlines(k[:3], 0, s[:3], color=BLUE, lw=1.4); ax.vlines([4], 0, s[3], color=RED, lw=1.4)
ax.plot(k[:3], s[:3], 'o', color=BLUE, ms=3.8, mew=0); ax.plot([4], [s[3]], 'o', color=RED, ms=3.8, mew=0)
ax.plot(k[4:], s[4:], 'o', mfc='white', mec=MUTED, ms=3.2, mew=.85)
ax.text(4.25, s[3]+.05, r'$\sigma_4\approx0.091$', ha='left')
ax.set_xlim(.4, 10.6); ax.set_ylim(0, .72); ax.set_xticks([1, 2, 3, 4, 6, 8, 10]); ax.set_yticks([0, .2, .4, .6]); ax.set_xlabel('$k$', labelpad=0); ax.set_ylabel(r'$\sigma_k$', labelpad=1)
ax = axes[1]
t = np.linspace(0, 1, 401)
ax.axhline(0, color=MUTED, lw=.85)
for j, c in ((1, BLUE), (2, GREEN), (3, YELLOW)):
    ax.plot(t, 2**.5*np.cos((j-.5)*np.pi*t), color=c, lw=1.4)
ax.text(.62, .95, '$v_1$'); ax.text(.67, -1.82, '$v_2$', ha='center'); ax.text(.4, -1.82, '$v_3$', ha='center')
ax.set_xlim(0, 1); ax.set_ylim(-2, 1.6); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$t$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'sigma_k=2/((2k-1)pi), v_k(t)=sqrt2 cos((k-1/2)pi t)'})
