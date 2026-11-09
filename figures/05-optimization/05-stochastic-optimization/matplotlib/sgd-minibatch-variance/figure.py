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

def run(a,B,T):
    m,s=4.,16.; out=[s]
    for t in range(T):
        s=(1-4*a+4*a*a)*s+a*a*(2*s-20*m+56)/(3*B); m=(1-2*a)*m; out.append(s)
    return np.array(out)
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.085,.965,.97,.25,wspace=.3)
Bs=np.array([1,2,3]); s2=56/3
a.plot(Bs,s2/Bs,'-o',color=GREEN,lw=1.4,ms=4,mew=0); a.plot(Bs,s2/Bs*(3-Bs)/2,'-o',color=YELLOW,lw=1.7,ms=4,mew=0)
a.text(2.1,10.6,'有放回',fontsize=7.5); a.text(1.42,5.2,'无放回',fontsize=7.5,ha='right')
a.set_xticks([1,2,3]); a.set_xlabel('$B$',labelpad=1); a.set_ylabel('最优点处的读数方差',labelpad=1); a.set_ylim(-.8,20.5); a.set_xlim(.8,3.2)
r=np.arange(0,601)
b.semilogy(r,run(.1,1,600),color=GREEN,lw=1.4)
b.semilogy(3*np.arange(201),run(.1,3,200),color=YELLOW,lw=1.7)
b.semilogy(3*np.arange(201),run(.3,3,200),color=PURPLE,lw=1.2,ls=(0,(4,2)))
b.text(300,.31,r'$B=1,\alpha=0.1$',fontsize=7.5); b.text(130,.1,r'$B=3,\alpha=0.1$',fontsize=7.5); b.text(230,.95,r'$B=3,\alpha=0.3$',fontsize=7.5)
b.set_xlabel('累计读取的项数',labelpad=1); b.set_ylabel(r'$\mathrm{E}[f-f^*]$',labelpad=1); b.set_xlim(0,600); b.set_ylim(.05,20)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
print('floors',run(.1,1,600)[-1],run(.1,3,200)[-1],run(.3,3,200)[-1])
save(fig,HERE,'figure',{'d0':4})
