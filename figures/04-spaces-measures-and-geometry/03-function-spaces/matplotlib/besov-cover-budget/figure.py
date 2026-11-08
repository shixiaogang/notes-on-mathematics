from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# s=1,R=1,C0=1,j0=0,J=6; eps/2=C_s 2^{-6}; rho_j, delta_j, and dim_j*log(1+2 rho_j/delta_j).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.085, right=.985, top=.96, bottom=.27, wspace=.2)
J = 6; Cs = (1-2.0**-2)**-.5; eps = 2*Cs*2.0**-J
j = np.arange(0, J)
rho = 2.0**-j; rho[0] = np.sqrt(2)
delta = eps/2*2.0**(-(J-j)/2)
dim = 2.0**j; dim[0] = 2
cost = dim*np.log(1+2*rho/delta)
print(eps, list(zip(j.tolist(), rho.tolist(), delta.tolist(), dim.tolist(), cost.tolist())), cost.sum())
ax = axes[0]
ax.semilogy(j, rho, color=BLUE, lw=1.4, marker='o', ms=3.4, mew=0); ax.semilogy(j, delta, color=GREEN, lw=1.4, marker='o', ms=3.4, mew=0)
ax.set_xlim(-.3, 5.3); ax.set_ylim(1e-3, 3); ax.set_xticks(j); ax.set_yticks([1e-2, 1e-1, 1]); ax.set_yticklabels(['0.01', '0.1', '1']); ax.minorticks_off(); ax.set_xlabel('$j$', labelpad=0)
ax.text(2.6, .35, r'$\rho_j$', color=BLUE, ha='left', va='bottom'); ax.text(2.2, .0075, r'$\delta_j$', color=GREEN, ha='left', va='bottom')
ax = axes[1]
ax.bar(j, cost, width=.62, color=BLUE_FILL, edgecolor=BLUE, lw=.85)
for x, c in zip(j, cost): ax.text(x, c+1.5, f'{c:.1f}', ha='center', va='bottom', fontsize=7.5)
ax.set_xlim(-.6, 5.6); ax.set_ylim(0, 68); ax.set_xticks(j); ax.set_yticks([0, 20, 40, 60]); ax.set_xlabel('$j$', labelpad=0)
for a, t in zip(axes, '(a) (b)'.split()):
    q = a.get_position(); fig.text((q.x0+q.x1)/2, .02, t, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 's=1,R=1,C0=1,j0=0,J=6', 'total': float(cost.sum())})
