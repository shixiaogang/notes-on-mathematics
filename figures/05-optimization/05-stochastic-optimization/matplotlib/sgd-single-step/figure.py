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

fig,ax=figure(width_mm=92,height_mm=54)
x=np.linspace(.7,2.6,200)
ax.plot(x,(x-1)**2,color=BLUE,lw=1.5)
al=.1; x0=2.; g=gi(x0); xs=x0-al*g; ys=(xs-1)**2
ax.plot([x0],[1],'o',ms=5,color=GREEN,mew=0,zorder=6); ax.text(x0+.02,.86,'$x^{(0)}$',fontsize=8,va='top')
ax.plot(xs,ys,'o',ms=4,mfc='white',mec=GREEN,mew=1.1,zorder=6)
for k,(a_,b_) in enumerate(zip(xs,ys)):
    ax.text(a_+(.03 if k==2 else -.04),b_+.09,f'$i={k+1}$',fontsize=7.5,ha='left' if k==2 else 'right')
ax.axhline(ys.mean(),color=YELLOW,lw=1.3,ls=(0,(4,2))); ax.text(.72,ys.mean()+.04,'三种结果的平均 0.767',fontsize=7.5)
ax.axhline(1,color=MUTED,lw=.85,ls=(0,(1.5,1.5))); ax.text(.72,1.04,'当前目标差 1',fontsize=7.5)
ax.plot([1],[0],'o',ms=4.6,color=RED,mew=0,zorder=6); ax.text(1.05,.02,'$x^*$',fontsize=8)
ax.set_xlim(.7,2.65); ax.set_ylim(-.05,2.15); ax.set_xlabel('$x$',labelpad=1); ax.set_ylabel(r'$f(x)-f^*$',labelpad=1)
print(xs,ys,ys.mean())
save(fig,HERE,'figure',{'x1':xs.tolist(),'gap':ys.tolist(),'mean':ys.mean()})
