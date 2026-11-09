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
def tag(fig, ax, s, y=None, d=.085):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
# 贯穿例：f(x)=(x1^2+9 x2^2)/2，x0=(9,1)，mu=1，L=9，kappa=9。
H = np.array([1., 9.]); X0 = np.array([9., 1.])
def f_ex(x): return .5*(H*np.asarray(x)**2).sum(-1)
def contour_ex(ax, xr, yr, levels):
    X,Y = np.meshgrid(np.linspace(*xr,700), np.linspace(*yr,500))
    ax.contour(X,Y,.5*(X**2+9*Y**2),levels=levels,colors=[BLUE],linewidths=.65)
def path(ax, P, c, ms=3.2, lw=1.2, **k):
    P=np.asarray(P); ax.plot(P[:,0],P[:,1],'-o',color=c,lw=lw,ms=ms,mew=0,zorder=4,**k)
def opt(ax, x=0, y=0): ax.plot([x],[y],'o',ms=4.8,color=RED,mew=0,zorder=6)
# (a) 贯穿例目标差；(b) diag(1,kappa) 上达到相对精度 1e-6 的步数。
fig,(a,b)=figure(width_mm=112,height_mm=58,ncols=2)
panel(fig,.115,.985,.97,.25,wspace=.32)
T=np.arange(0,41)
def gapfor(al):
    return np.array([.5*(1*(1-al)**(2*t)*81+9*(1-9*al)**(2*t)*1) if not (t==0) else 45. for t in T])
a.semilogy(T,gapfor(1/9),color=YELLOW,lw=1.5); a.semilogy(T,gapfor(.2),color=GREEN,lw=1.5)
a.semilogy(T,45*(8/9)**T,color=PURPLE,lw=.95,ls=(0,(3,2)))
a.text(25,.18,r'$\alpha=1/9$',fontsize=7.5,color=INK); a.text(6,.02,r'$\alpha=1/5$',fontsize=7.5,color=INK); a.text(14,11,'定理上界',fontsize=7.5,color=INK,ha='left')
a.set_xlabel('$t$',labelpad=1); a.set_ylabel(r'$f(x^{(t)})-f^*$',labelpad=1); a.set_xlim(0,40); a.set_ylim(1e-3,100)
ks=np.array([2,3,5,9,20,50,100,200,500,1000.]); eps=1e-6; Ts=[]
for k in ks:
    Hk=np.array([1,k]); x=np.array([k,1.]); al=2/(k+1); f0=.5*(Hk*x*x).sum(); t=0
    while .5*(Hk*x*x).sum()>eps*f0: x=x-al*Hk*x; t+=1
    Ts.append(t)
kk=np.logspace(np.log10(2),3,100)
b.loglog(kk,np.log(1/eps)*kk/4,color=MUTED,lw=.95,ls=(0,(3,2))); b.loglog(ks,Ts,'o',color=GREEN,ms=4,mew=0)
b.text(35,20,r'$\frac{\kappa}{4}\ln\frac{1}{\varepsilon}$',fontsize=8,color=INK)
b.set_xlabel(r'$\kappa$',labelpad=1); b.set_ylabel('所需步数',labelpad=1)
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
save(fig,HERE,'figure',{'kappa_list':list(ks),'steps':Ts,'eps':eps})
