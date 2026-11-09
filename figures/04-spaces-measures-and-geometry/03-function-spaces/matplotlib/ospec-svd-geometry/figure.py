from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# SVD of A=[[3,0],[4,5]]: v1=(1,1)/sqrt2, v2=(1,-1)/sqrt2, sigma=3sqrt5, sqrt5, u1=(1,3)/sqrt10, u2=(3,-1)/sqrt10.
fig, axes = figure(width_mm=112, height_mm=58, ncols=2, gridspec_kw={'width_ratios': [1, 1.25]})
fig.set_layout_engine(None)
fig.subplots_adjust(left=.03, right=.98, top=.98, bottom=.16, wspace=.12)
A = np.array([[3., 0], [4, 5]])
U, s, Vt = np.linalg.svd(A)
v1 = np.array([1, 1])/2**.5; v2 = np.array([1, -1])/2**.5
u1 = np.array([1, 3])/10**.5; u2 = np.array([3, -1])/10**.5
s1, s2 = 3*5**.5, 5**.5
assert abs(s[0]-s1) < 1e-12 and abs(s[1]-s2) < 1e-12
assert np.allclose(A@v1, s1*u1) and np.allclose(A@v2, s2*u2)
th = np.linspace(0, 2*np.pi, 361); c = np.vstack([np.cos(th), np.sin(th)])
def arrow(ax, p, col):
    ax.annotate('', xy=p, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=col, lw=1.1, shrinkA=0, shrinkB=0, mutation_scale=8))
ax = axes[0]
ax.axhline(0, color=MUTED, lw=.85); ax.axvline(0, color=MUTED, lw=.85)
ax.plot(*c, color=BLUE, lw=1.4)
arrow(ax, v1, GREEN); arrow(ax, v2, YELLOW)
ax.plot([1], [0], 'o', color=INK, ms=2.8, mew=0)
ax.text(v1[0]+.04, v1[1]+.05, '$v_1$'); ax.text(v2[0]+.04, v2[1]-.2, '$v_2$'); ax.text(1.06, .07, '$e_1$')
ax.set_xlim(-1.45, 1.55); ax.set_ylim(-1.55, 1.55)
ax = axes[1]
ax.axhline(0, color=MUTED, lw=.85); ax.axvline(0, color=MUTED, lw=.85)
E = A@c
ax.plot(*E, color=BLUE, lw=1.4)
arrow(ax, s1*u1, GREEN); arrow(ax, s2*u2, YELLOW)
ax.plot([3], [4], 'o', color=INK, ms=2.8, mew=0)
ax.text(s1*u1[0], 6.75, r'$\sigma_1u_1$', ha='center'); ax.text(*(s2*u2+np.array([.2, -.5])), r'$\sigma_2u_2$'); ax.text(3.2, 3.8, r'$Ae_1$', va='top')
ax.set_xlim(-6.2, 6.2); ax.set_ylim(-7.6, 7.6)
for ax in axes:
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    for s_ in ('left', 'bottom'): ax.spines[s_].set_visible(False)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'A=[[3,0],[4,5]], A(unit circle)=ellipse; sigma_1=3 sqrt5, sigma_2=sqrt5'})
