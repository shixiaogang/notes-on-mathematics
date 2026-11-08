from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Truncated singular expansion of the Volterra kernel 1_{t<x}: slice x=1/2 and the two errors.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.23, wspace=.26)
om = lambda j: (j-.5)*np.pi
def km(m, t, x=.5):
    return sum(2/om(j)*np.sin(om(j)*x)*np.cos(om(j)*t) for j in range(1, m+1))
ax = axes[0]
t = np.linspace(0, 1, 4001)
ax.plot(t, km(3, t), color=GREEN, lw=1.1); ax.plot(t, km(30, t), color=YELLOW, lw=1.1)
ax.plot([0, .5], [1, 1], color=BLUE, lw=1.4); ax.plot([.5, 1], [0, 0], color=BLUE, lw=1.4)
ax.text(.78, .14, '$m=3$', ha='left'); ax.text(.54, .66, '$m=30$', ha='left'); ax.text(.1, 1.24, r'$\mathbf{1}_{\{t<1/2\}}$')
ax.set_xlim(0, 1); ax.set_ylim(-.35, 1.45); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$t$', labelpad=0)
ax = axes[1]
J = 200000; sq = 1/om(np.arange(1, J+1))**2
tail = .5-np.cumsum(sq)
m = np.arange(1, 501)
sig = 1/om(m+1); ker = np.sqrt(tail[m-1])
for q in (1, 2, 3, 4): print(q, round(sig[q-1], 4), round(ker[q-1], 4))
print('||k||^2 sum', sq.sum())
ax.loglog(m, sig, color=RED, lw=1.4); ax.loglog(m, ker, color=PURPLE, lw=1.4)
ax.text(2.2, .012, r'$\sigma_{m+1}$'); ax.text(30, .24, r'$(\sum_{j>m}\sigma_j^2)^{1/2}$', ha='center')
ax.set_xlim(1, 500); ax.set_ylim(5e-4, .7); ax.set_xlabel('$m$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'k_m(1/2,t)=sum_{j<=m} sigma_j u_j(1/2) v_j(t); sigma_{m+1}; sqrt(tail)'})
