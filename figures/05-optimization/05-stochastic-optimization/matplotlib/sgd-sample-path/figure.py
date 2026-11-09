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

rng=np.random.default_rng(5)
al=.1;T=140;x=5.;p=[x];gd=[5.]
for t in range(T):
    i=rng.integers(3); x=x-al*gi(x)[i]; p.append(x); gd.append(gd[-1]-al*(2*gd[-1]-2))
fig,ax=figure(width_mm=104,height_mm=50)
fl=28*al/(6-7*al); r=np.sqrt(fl)
ax.axhspan(1-r,1+r,color=GREEN_FILL,lw=0,zorder=0)
ax.plot(p,color=GREEN,lw=1.05); ax.plot(gd,color=YELLOW,lw=1.6)
ax.axhline(1,color=RED,lw=.85); ax.text(T+1,1,'$x^*$',fontsize=8,va='center')
ax.text(33,2.6,'随机梯度',fontsize=8); ax.text(8,4.0,'完整梯度',fontsize=8)
ax.set_xlim(0,T); ax.set_ylim(-.9,5.3); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x^{(t)}$',labelpad=1)
save(fig,HERE,'figure',{'seed':5,'alpha':al,'floor':fl})
