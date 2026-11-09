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
# 偏差与噪声的残余（贯穿例 f=(x-1)^2+5，读数 f'+b+xi，xi 方差 1），以及延迟读取对稳定性的影响（f=x^2/2，alpha=1）。
rng=np.random.default_rng(5)
def noisy(al,sig,b,T=1500,R=2000):
    d=np.full(R,8.); out=[]
    for k in range(T):
        out.append((d*d).mean()); d=d-al*(2*d+b+sig*rng.standard_normal(R))
    return np.array(out)
fig,(a,c)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.125,.965,.97,.26,wspace=.3)
for al,col in ((.2,GREEN),(.05,YELLOW)):
    y=noisy(al,1.,0.); a.semilogy(y,color=col,lw=1.1)
    y2=noisy(al,0.,.6); a.semilogy(np.maximum(y2,1e-9),color=col,lw=1.1,ls='--'); print(al,'noise',y[-400:].mean(),'theory',al/(2*(2-2*al)),'bias',y2[-1],.09)
a.axhline(.09,color=RED,lw=.9,ls=':'); a.set_xlim(0,300); a.set_ylim(3e-3,100); a.set_xlabel('$t$',labelpad=1); a.set_ylabel('期望目标差',labelpad=1)
def delay(tau,al=1.,T=40):
    x=[1.]*(tau+1)
    for k in range(T): x.append(x[-1]-al*x[-1-tau])
    return np.array(x[tau:])
for tau,col in ((0,GREEN),(1,YELLOW),(2,RED)):
    y=delay(tau); c.plot(y,color=col,lw=1.1,marker='o',ms=2,mew=0); print(tau,y[:12])
c.set_ylim(-4,4); c.set_xlim(0,22); c.set_xlabel('$t$',labelpad=1); c.set_ylabel('$x^{(t)}$',labelpad=1); c.axhline(0,color=STROKE,lw=.6)
c.text(9.5,3.3,r'$\tau=2$',fontsize=7.5); c.text(14.5,1.25,r'$\tau=1$',fontsize=7.5); c.text(1.4,.3,r'$\tau=0$',fontsize=7.5)
tag(fig,a,'(a)'); tag(fig,c,'(b)')
save(fig,HERE,'figure',{'seed':5,'objective':'(x-1)^2+5','noise_var':1,'bias':.6})
