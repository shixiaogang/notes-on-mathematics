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

fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.085,.985,.97,.25,wspace=.28)
x=np.linspace(-4.5,4.5,300)
fi=[.5*Ai*(x-Bi)**2 for Ai,Bi in zip(A,B)]
for f_,s,(px,py) in zip(fi,['$f_1$','$f_2$','$f_3$'],[(-3.9,8.6),(-2.55,10.2),(3.35,7.0)]):
    a.plot(x,f_,color=MUTED,lw=.85,ls=(0,(3,2))); a.text(px,py,s,fontsize=7.5,color=INK)
a.plot(x,(x-1)**2+5,color=BLUE,lw=1.5); a.text(3.75,16.2,'$f$',fontsize=8,color=INK,ha='right')
a.plot([1],[5],'o',ms=4.6,color=RED,mew=0,zorder=6); a.text(1.15,3.6,'$x^*$',fontsize=8)
a.set_xlim(-4.5,4.5); a.set_ylim(0,20); a.set_xlabel('$x$',labelpad=1)
b.axvspan(-3,3,color=RED_FILL,lw=0,zorder=0)
for k,(Ai,Bi,s,(px,py)) in enumerate(zip(A,B,["$f_1'$","$f_2'$","$f_3'$"],[(-4.3,.6),(-4.3,-6.7),(-.85,-15.2)])):
    b.plot(x,Ai*(x-Bi),color=MUTED,lw=.85,ls=(0,(3,2))); b.text(px,py,s,fontsize=7.5,color=INK,ha='left')
b.plot(x,2*x-2,color=BLUE,lw=1.5); b.text(-3.85,-13.4,"$f'$",fontsize=8,color=INK,ha='left')
b.axhline(0,color=STROKE,lw=.7)
b.plot([2,2],[-3,5],color=GREEN,lw=.85)
b.plot([2,2,2],[5,4,-3],'o',ms=3.6,color=GREEN,mew=0,zorder=5)
b.plot([2],[2],'o',ms=4.4,mfc='white',mec=BLUE,mew=1.1,zorder=6)
b.text(1.75,-4.9,'$x=2$',fontsize=7.5,ha='right')
b.set_xlim(-4.5,5.2); b.set_ylim(-16,14); b.set_xlabel('$x$',labelpad=1)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'a':list(A),'b':list(B),'formula':'f=(x-1)^2+5'})
