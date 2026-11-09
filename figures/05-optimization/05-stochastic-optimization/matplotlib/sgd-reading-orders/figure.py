from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
# 贯穿例：f_i(x)=a_i(x-b_i)^2/2，a=(1,2,3)，b=(-3,0,3)；f(x)=(x-1)^2+5，x*=1。
A = np.array([1., 2., 3.]); B = np.array([-3., 0., 3.])
def gi(x): return A*(x-B)
def panel(fig, left, right, top, bottom, wspace=.3, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.05):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='top')

rng=np.random.default_rng(13)
N,E=3,4
wr=rng.integers(1,4,size=N*E)
cy=np.tile([1,2,3],E)
rr=np.concatenate([rng.permutation([1,2,3]) for _ in range(E)])
fig,ax=figure(width_mm=104,height_mm=38)
fig.set_layout_engine(None); fig.subplots_adjust(left=.22,right=.99,top=.99,bottom=.12)
col={1:BLUE_FILL,2:GREEN_FILL,3:YELLOW_FILL}
names=['有放回','固定循环','随机重排']
for r,(row,nm) in enumerate(zip([wr,cy,rr],names)):
    y=2-r
    for t,v in enumerate(row):
        ax.add_patch(__import__('matplotlib').patches.Rectangle((t,y+.08),1,.84,fc=col[int(v)],ec='white',lw=.8))
        ax.text(t+.5,y+.5,str(int(v)),ha='center',va='center',fontsize=8)
    ax.text(-.25,y+.5,nm,ha='right',va='center',fontsize=8)
for k in range(E+1):
    ax.plot([k*N,k*N],[0,3],color=STROKE,lw=1.0)
for k in range(E):
    ax.text(k*N+N/2,-.32,f'第{k+1}轮',ha='center',va='center',fontsize=7.5,color=MUTED)
ax.set_xlim(-.1,N*E+.1); ax.set_ylim(-.6,3.02); ax.axis('off')
save(fig,HERE,'figure',{'seed':13,'with_replacement':wr.tolist(),'reshuffle':rr.tolist()})
