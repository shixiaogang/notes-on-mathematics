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

fig,ax=figure(width_mm=96,height_mm=52)
x=np.linspace(-4.5,4.5,901)
ms=np.mean(np.sign(gi(x[:,None]) if 0 else np.stack([A[k]*(x-B[k]) for k in range(3)])),axis=0)
ms[np.abs(x+3)<1e-9]=np.nan; ms[np.abs(x)<1e-9]=np.nan; ms[np.abs(x-3)<1e-9]=np.nan
ax.axhline(0,color=STROKE,lw=.7)
ax.plot(x,(2*x-2)/6,color=BLUE,lw=1.5)
ax.step(x,ms,where='mid',color=YELLOW,lw=1.7)
ax.plot([1],[0],'o',ms=4.6,color=RED,mew=0,zorder=6); ax.text(1.05,-.2,'$x^*=1$',fontsize=8,va='top')
ax.plot([0],[0],'o',ms=4.4,mfc='white',mec=INK,mew=1,zorder=6); ax.text(-.1,.13,'$x=0$',fontsize=8,ha='right')
ax.axvspan(0,1,color=RED_FILL,lw=0,zorder=0)
ax.text(-3.05,-.85,'读数符号的平均',fontsize=7.5,ha='left'); ax.text(3.55,.47,"$f'(x)/6$",fontsize=7.5,ha='left')
ax.set_xlim(-4.5,4.5); ax.set_ylim(-1.2,1.2); ax.set_xlabel('$x$',labelpad=1); ax.set_ylabel('平均读数',labelpad=1)
save(fig,HERE,'figure',{'note':'f prime scaled by 1/6 for visual comparison'})
