from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
# f=1_{[1/3,1)}; P_jf=interval means, computed exactly. j=1,3,5: interval containing 1/3 has mean 1/3.
fig, axes = figure(width_mm=112, height_mm=36, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.26, wspace=.22)
T = 1/3
for ax, j, s in zip(axes,(1,3,5),'abc'):
    n=2**j; e=np.arange(n+1)/n
    means=[max(0.0, e[k+1]-max(e[k],T))/(e[k+1]-e[k]) for k in range(n)]
    ax.plot([0,T],[0,0],color=BLUE,lw=2.6,solid_capstyle='butt'); ax.plot([T,1],[1,1],color=BLUE,lw=2.6,solid_capstyle='butt')
    ax.step(e,means+[means[-1]],where='post',color=GREEN,lw=1.1,solid_joinstyle='miter')
    k0=int(np.floor(T*n)); 
    ax.axvspan(e[k0],e[k0+1],color=RED_FILL,lw=0,zorder=0)
    ax.set_xlim(0,1); ax.set_ylim(-.08,1.12); ax.set_xticks([0,1/3,1]); ax.set_xticklabels(['0','1/3','1']); ax.set_yticks([0,1/3,1]); ax.set_yticklabels(['0','1/3','1'])
    ax.tick_params(labelsize=7, length=2, pad=1.5)
    ax.text(.03,.97,r'$P_{%d}f$'%j,transform=ax.transAxes,ha='left',va='top')
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,'(%s)'%s,ha='center',va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=1_[1/3,1); P_jf=dyadic means; j=1,3,5, mean on interval containing 1/3 equals 1/3'})
