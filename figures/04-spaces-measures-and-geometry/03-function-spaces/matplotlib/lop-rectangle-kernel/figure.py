from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle, Ellipse, Circle

# (a) n=4 的格内平均核 k_4(x,y)=1+xbar*ybar；(b) 两种误差。
# ||k-k_n||=sqrt(2n^2-1)/(3n^2)，||T-T_n||=(s+sqrt(s^2+4qs))/2，s=1/(3n^2)，q=1/3-s。
cmap = LinearSegmentedColormap.from_list('b', ['#FFFFFF', BLUE_FILL, BLUE])
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2, width_ratios=[1, 1.25])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.96, bottom=.26, wspace=.25)
n0 = 4; h = 2/n0
mid = -1+h/2+h*np.arange(n0)
K = 1+np.outer(mid, mid)
for i in range(n0):
    for j in range(n0):
        a.add_patch(Rectangle((-1+h*j, -1+h*i), h, h, fc=cmap(K[i, j]/2), ec='white', lw=.8))
        a.text(-1+h*j+h/2, -1+h*i+h/2, f'{K[i,j]:.2f}', ha='center', va='center', fontsize=7.5)
a.set_xlim(-1, 1); a.set_ylim(1, -1); a.set_aspect('equal'); a.set_xticks([-1, 0, 1]); a.set_yticks([-1, 0, 1]); a.tick_params(length=2, pad=1.5)
a.set_xlabel('$y$', labelpad=-1); a.set_ylabel('$x$', labelpad=3, rotation=0)
ns = 2.0**np.arange(0, 7)
hs = np.sqrt(2*ns**2-1)/(3*ns**2)
s = 1/(3*ns**2); q = 1/3-s
op = (s+np.sqrt(s**2+4*q*s))/2
b.loglog(ns, hs, 'o-', color=RED, lw=1.4, ms=3.2, mew=0, base=2)
b.loglog(ns, op, 's-', color=GREEN, lw=1.4, ms=3.0, mew=0, base=2)
b.set_xlim(.85, 76); b.set_ylim(.0035, .65)
b.set_xticks([1, 2, 4, 8, 16, 32, 64]); b.set_xticklabels(['1', '2', '4', '8', '16', '32', '64']); b.minorticks_off()
b.set_yticks([.005, .02, .08, .32]); b.set_yticklabels(['0.005', '0.02', '0.08', '0.32'])
b.set_xlabel('$n$', labelpad=0); b.tick_params(length=2, pad=1.5)
b.text(7.2, .092, r'$\|k-k_n\|_{L^2}$', ha='left', va='bottom')
b.text(1.55, .022, r'$\|T-T_n\|$', ha='left', va='bottom')
for ax, s_ in zip((a, b), '(a) (b)'.split()):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s_, ha='center', va='bottom')
print(dict(zip(ns.astype(int), np.round(hs, 4))), dict(zip(ns.astype(int), np.round(op, 4))))
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': '||k-k_n||=sqrt(2n^2-1)/(3n^2); ||T-T_n||=(s+sqrt(s^2+4qs))/2, s=1/(3n^2), q=1/3-s'})
