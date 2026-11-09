from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
sys.path.insert(0, str(ROOT/"figures/05-optimization/02-smooth-optimization/matplotlib/qn-common"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
from qnlib import *
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = "#4C4D4F"

# 第一次 BFGS 更新：B0=I，s=(-1.6,-1.6)，y=(-3.2,-12.8)。依次画 p^T M p=1。
B = np.eye(2); s = np.array([-1.6, -1.6]); y = np.array([-3.2, -12.8]); A = np.diag([2., 8.])
Bs = B@s; P = B-np.outer(Bs, Bs)/float(s@Bs); B1 = P+np.outer(y, y)/float(s@y)
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
th = np.linspace(0, 2*np.pi, 400); C = np.stack([np.cos(th), np.sin(th)])
def ell(M):
    return np.linalg.solve(np.linalg.cholesky(M).T, C)
u = s/np.linalg.norm(s)
for ax in axs:
    ax.set_aspect('equal'); ax.set_xlim(-2.1, 2.1); ax.set_ylim(-2.1, 2.1); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2]); ax.set_xlabel('$p_1$', labelpad=1)
    ax.annotate('', xy=1.75*u, xytext=-1.75*u, arrowprops=dict(arrowstyle='<->', color=MUTED, lw=.85, shrinkA=0, shrinkB=0))
axs[0].set_ylabel('$p_2$', labelpad=1)
axs[0].plot(*ell(B), color=YELLOW, lw=1.4)
n = np.array([u[1], -u[0]])
for sgn in (1, -1):
    a = sgn*n-3*u; b = sgn*n+3*u
    axs[1].plot([a[0], b[0]], [a[1], b[1]], color=PURPLE, lw=1.4)
axs[2].plot(*ell(B1), color=GREEN, lw=1.4)
axs[2].plot(*ell(A), color=BLUE, lw=1.1, ls=(0, (4, 2)))
axs[0].text(-1.9, 1.55, '$B^{(0)}$', color=INK)
axs[2].text(-1.9, 1.55, '$B^{(1)}$', color=INK)
axs[1].text(-1.9, 1.55, '$P$', color=INK)
axs[0].text(1.25*u[0]+.2, 1.25*u[1]-.32, '$s$', color=INK)
panel(fig, .07, .99, .985, .26, .22); tags(fig, list(axs))
save(fig, HERE, 'figure', {'B0': B.tolist(), 'P': P.tolist(), 'B1': B1.tolist(), 's': s.tolist(), 'y': y.tolist()})
