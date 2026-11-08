from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# N=8 的 Dirichlet 核与 Fejér 核，由闭式计算。
fig, axes = figure(width_mm=112, height_mm=46, ncols=2, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.96, bottom=.26, wspace=.1)
N = 8
t = np.linspace(-np.pi, np.pi, 2401); t[t == 0] = 1e-9
D = np.sin((N+.5)*t)/np.sin(t/2)
F = (np.sin((N+1)*t/2)/np.sin(t/2))**2/(N+1)
for ax, y in zip(axes, (D, F)):
    ax.axhline(0, color=MUTED, lw=.85)
    ax.plot(t, y, color=BLUE, lw=1.4)
    ax.set_xlim(-np.pi, np.pi); ax.set_ylim(-5, 18.5)
    ax.set_xticks([-np.pi, 0, np.pi]); ax.set_xticklabels([r'$-\pi$', '$0$', r'$\pi$']); ax.set_yticks([0, 9, 17])
    ax.set_xlabel('$t$', labelpad=0)
axes[0].text(1.35, 13, r'$D_8$', color=BLUE, ha='center'); axes[1].text(1.35, 13, r'$F_8$', color=BLUE, ha='center')
tag(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'D_8(t)=sin(8.5t)/sin(t/2), F_8(t)=sin^2(4.5t)/(9 sin^2(t/2))'})
