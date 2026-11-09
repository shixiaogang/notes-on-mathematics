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
def tag(fig, ax, s, y=None, d=.15):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
# f(x)=|x1|+2|x2|，x0=(1,1)，R=sqrt2，G=sqrt5；递减步长 alpha_t=R/(G sqrt(t+1))。
def sg(x): return np.array([1. if x[0]>=0 else -1., 2. if x[1]>=0 else -2.])
f=lambda x:abs(x[0])+2*abs(x[1])
R,G=2**.5,5**.5
T=30000;x=np.array([1.,1.]);b=f(x);s=np.zeros(2);sa=0.;sa2=0.
last,best,avg,bd=[],[],[],[]
for t in range(T):
    a=R/G/(t+1)**.5;s+=a*x;sa+=a;sa2+=a*a
    x=x-a*sg(x);b=min(b,f(x));last.append(f(x));best.append(b);avg.append(f(s/sa));bd.append((R*R+G*G*sa2)/(2*sa))
tt=np.arange(1,T+1)
fig,A=figure(width_mm=96,height_mm=58)
panel(fig,.11,.98,.98,.15)
A.loglog(tt,bd,color=INK,lw=.95,ls='--');idx=np.unique(np.round(np.logspace(0,np.log10(T),70)).astype(int))-1;A.loglog(tt[idx],np.array(last)[idx],'o',color=YELLOW,ms=2.4,mew=0);A.loglog(tt,avg,'-',color=GREEN,lw=1.4);A.loglog(tt,best,'-',color=PURPLE,lw=1.3)
A.text(1500,.2,'误差上界',color=INK,fontsize=7.5);
A.set_xlabel('$T$',labelpad=1);A.set_ylabel('目标差',labelpad=1);A.set_xlim(1,T);A.set_ylim(3e-3,8)
save(fig,HERE,'figure',{'T':T,'final_bound':bd[-1],'final_avg':avg[-1],'final_best':best[-1],'final_last':last[-1]})
