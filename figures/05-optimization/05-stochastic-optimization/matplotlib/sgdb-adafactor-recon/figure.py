from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
# 平方统计的行列压缩：V 由 40 个随机读数算出，重建 Vhat=R C^T / sum(R)。
rng=np.random.default_rng(13)
m,d=6,8; r=np.linspace(2,.5,m); c=np.linspace(.4,1.6,d)
V=np.zeros((m,d))
T=40
for _ in range(T):
    z=rng.standard_normal(m); E=rng.standard_normal((m,d))
    G=np.outer(r*z,c)+.6*E; V+=G*G/T
R=V.sum(1);C=V.sum(0);Vh=np.outer(R,C)/R.sum()
err=np.abs(Vh-V)/V
print('err mean,max',err.mean(),err.max(),'R match',np.abs(Vh.sum(1)-R).max())
fig,axs=figure(width_mm=112,height_mm=46,ncols=3)
panel(fig,.02,.98,.96,.2,wspace=.12)
vm=max(V.max(),Vh.max())
from matplotlib.colors import LinearSegmentedColormap
cb=LinearSegmentedColormap.from_list('b',['#FFFFFF',BLUE]); cr=LinearSegmentedColormap.from_list('r',['#FFFFFF',RED])
axs[0].imshow(V,cmap=cb,vmin=0,vmax=vm); axs[1].imshow(Vh,cmap=cb,vmin=0,vmax=vm); axs[2].imshow(err,cmap=cr,vmin=0,vmax=.7)
for ax,s in zip(axs,'abc'):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(True); sp.set_linewidth(.6); sp.set_color(STROKE)
    tag(fig,ax,'(%s)'%s,y=.02)
save(fig,HERE,'figure',{'seed':13})
