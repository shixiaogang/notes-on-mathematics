from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# (a) A=diag(1/j): coefficients of u=(1/j) and Au=(1/j^2). (b) kernel 1-6xz in the e1,e2 coefficient plane: diag(1,-2).
fig, axes = figure(width_mm=112, height_mm=56, ncols=2, gridspec_kw={'width_ratios': [1.25, 1]})
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.975, bottom=.235, wspace=.2)
ax = axes[0]
j = np.arange(1, 9); w = .36
ax.bar(j-w/2, 1/j, width=w, color=BLUE_FILL, edgecolor=BLUE, lw=.75)
ax.bar(j+w/2, 1/j**2, width=w, color=BLUE, edgecolor=BLUE, lw=.75)
ax.set_xticks(j); ax.set_yticks([0, .5, 1]); ax.set_ylim(0, 1.1); ax.set_xlim(.3, 8.7); ax.set_xlabel('$j$', labelpad=0)
ax.text(2.3, .6, r'$\langle e_j,u\rangle$', ha='left'); ax.text(1.7, .1, '', ha='left')
ax.annotate(r'$\langle e_j,Au\rangle$', xy=(2.18, .25), xytext=(4.2, .38), arrowprops=dict(arrowstyle='-', color=MUTED, lw=.75, shrinkA=1, shrinkB=1), va='center')
ax = axes[1]
th = np.linspace(0, 2*np.pi, 361)
ax.axhline(0, color=MUTED, lw=.85); ax.axvline(0, color=MUTED, lw=.85)
ax.plot(np.cos(th), np.sin(th), color=BLUE, lw=1.1, ls='--')
ax.plot(np.cos(th), 2*np.sin(th), color=BLUE, lw=1.4)
a = np.deg2rad(50); p = np.array([np.cos(a), np.sin(a)]); q = np.array([p[0], -2*p[1]])
ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', color=INK, lw=.85, shrinkA=1.5, shrinkB=1.5, mutation_scale=7))
ax.plot(*p, 'o', color=INK, ms=2.8, mew=0); ax.plot(*q, 'o', color=INK, ms=2.8, mew=0)
ax.text(p[0]-.14, p[1]+.02, '$u$', ha='right'); ax.text(q[0]+.1, q[1]-.28, '$Tu$')
ax.text(1.55, -.3, '$e_1$', ha='center'); ax.text(.17, 2.3, '$e_2$', ha='left')
ax.set_aspect('equal'); ax.set_xlim(-1.8, 1.8); ax.set_ylim(-2.6, 2.6); ax.set_xticks([-1, 1]); ax.set_yticks([-2, -1, 1, 2])
for s in ('left', 'bottom'): ax.spines[s].set_visible(False)
ax.tick_params(length=0, pad=1)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'bars 1/j and 1/j^2; (x,y)->(x,-2y) on the coefficient plane of e1=1, e2=sqrt3 x'})
