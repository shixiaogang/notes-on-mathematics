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

def M(x,p): return (gi(x)**2/p).sum(-1)/9
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.095,.985,.97,.25,wspace=.32)
x=np.linspace(-6,6,300)
X=x[:,None]
pu=np.ones(3)/3; pl=A/6; pg=np.array([1/3,1/6,1/2])
Mv=lambda p:((A*(X-B))**2/p).sum(1)/9
a.plot(x,Mv(pu),color=BLUE,lw=1.4); a.plot(x,Mv(pl),color=GREEN,lw=1.4); a.plot(x,Mv(pg),color=YELLOW,lw=1.7); a.plot(x,(np.abs(A*(X-B)).sum(1))**2/9,color=PURPLE,lw=1.1,ls=(0,(4,2)))
pass
a.axvline(1,color=RED,lw=.85); a.text(1.2,275,'$x^*$',fontsize=8)
a.set_xlabel('$x$',labelpad=1); a.set_ylabel('读数二阶矩',labelpad=1); a.set_xlim(-6,6); a.set_ylim(0,300)
p1=np.logspace(-3,np.log10(.8),200)
g=gi(1.); v=(g[0]**2/p1+g[1]**2*2/(1-p1)+g[2]**2*2/(1-p1))/9
b.loglog(p1,v,color=GREEN,lw=1.4)
b.plot([1/3],[(g**2/pu).sum()/9],'o',ms=4.4,color=BLUE,mew=0,zorder=5); b.text(.38,24,'均匀',fontsize=7.5)
b.set_xlabel(r'$p_1\quad(p_2=p_3)$',labelpad=1); b.set_ylabel('最优点处的二阶矩',labelpad=1)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
print('M at x*',M(1.,pu),M(1.,pl),M(1.,pg),'tiny',((g**2/np.array([.01,.495,.495])).sum())/9)
save(fig,HERE,'figure',{'second_moments_at_opt':[M(1.,pu),M(1.,pl),M(1.,pg)]})
