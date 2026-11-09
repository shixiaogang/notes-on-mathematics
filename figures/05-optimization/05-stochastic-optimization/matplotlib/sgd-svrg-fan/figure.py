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

xt=2.;gt=2.
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.085,.985,.97,.25,wspace=.3)
x=np.linspace(.2,3.8,200)
for Ai,Bi in zip(A,B):
    a.plot(x,Ai*(x-Bi),color=MUTED,lw=.85,ls=(0,(3,2)))
    a.plot(x,Ai*(x-xt)+gt,color=GREEN,lw=1.2)
a.plot(x,2*x-2,color=BLUE,lw=1.5)
a.plot([xt],[gt],'o',ms=5,color=GREEN,mew=0,zorder=6)
a.axhline(0,color=STROKE,lw=.7)
a.text(.25,-2.2,"$f'$",fontsize=8,color=INK); a.text(2.1,.95,r'$\tilde{x}$',fontsize=8,va='top')
a.set_xlim(.2,3.8); a.set_ylim(-9,9); a.set_xlabel('$x$',labelpad=1)
xx=np.linspace(-1,4,300); d=xx-1
b.plot(xx,(2*d*d-20*d+56)/3,color=YELLOW,lw=1.7)
b.plot(xx,(2/3)*(xx-2)**2,color=GREEN,lw=1.4)
b.plot(xx,(2/3)*(xx-1)**2,color=GREEN,lw=1.1,ls=(0,(4,2)))
b.text(1.55,25.5,'随机梯度',fontsize=7.5); b.text(1.25,5.2,r'$\tilde{x}=2$',fontsize=7.5); b.text(3.0,.25,r'$\tilde{x}=1$',fontsize=7.5,va='bottom')
b.set_xlabel('$x$',labelpad=1); b.set_ylabel('读数的条件方差',labelpad=1); b.set_xlim(-1,4); b.set_ylim(0,34)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'snapshot':xt})
