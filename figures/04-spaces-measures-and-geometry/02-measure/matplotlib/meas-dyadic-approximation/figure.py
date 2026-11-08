from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# phi_n = 2^{-n} floor(2^n min(f,n)), f(x)=x^2 on [0,2], n=1,2.
fig, axes = figure(width_mm=108, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.19, wspace=.16)
x = np.linspace(0, 2, 8001); f = x**2
for ax, n in zip(axes, (1, 2)):
    phi = np.floor(2**n*np.minimum(f, n))/2**n
    ax.plot(x, f, color=INK, lw=1.1)
    ax.step(x, phi, where='post', color=BLUE, lw=1.4)
    ax.fill_between(x, 0, phi, color=BLUE_FILL, lw=0, step='post', zorder=0)
    ax.axhline(n, color=MUTED, lw=.85, ls=(0, (3, 2)))
    ax.set_xlim(0, 2.02); ax.set_ylim(0, 4.3)
    ax.text(.05, n+.12, rf'$y={n}$', color=MUTED, ha='left', va='bottom', fontsize=7.5)
    ax.text(1.72, 3.55, r'$f$', color=INK, ha='right', va='center')
    ax.text(1.7, n-.55, rf'$\varphi_{n}$', color=BLUE, ha='center', va='center')
axes[0].set_xticks([0, np.sqrt(.5), 1, 2]); axes[0].set_xticklabels(['0', r'$\sqrt{0.5}$', '1', '2']); axes[0].set_yticks([0, .5, 1, 4]); axes[0].set_yticklabels(['0', '0.5', '1', '4'])
axes[1].set_xticks([0, .5, 1, np.sqrt(2), 2]); axes[1].set_xticklabels(['0', '0.5', '1', r'$\sqrt{2}$', '2']); axes[1].set_yticks([0, 1, 2, 4]); axes[1].set_yticklabels(['0', '1', '2', '4'])
fig.text(.285, .018, '(a)', ha='center', va='bottom', color=INK); fig.text(.76, .018, '(b)', ha='center', va='bottom', color=INK)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'phi_n=2^-n floor(2^n min(x^2,n)), n=1,2'})
