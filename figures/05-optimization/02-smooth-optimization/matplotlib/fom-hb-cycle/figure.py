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
# Lessard等分段二次：mu=1, L=25，重球取二次最优参数 alpha=1/9, beta=4/9，x0=3.3。
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2,gridspec_kw={'width_ratios':[1,1.35]})
panel(fig,.095,.985,.97,.25,wspace=.27)
g=lambda x: np.where(x<1,25*x,np.where(x<2,x+24,25*x-24))
xx=np.linspace(-2.6,3,500); a.plot(xx,g(xx),color=BLUE,lw=1.4); a.axhline(0,color=STROKE,lw=.7); a.axvline(0,color=STROKE,lw=.7)
cyc=np.array([792,-2208,2592])/1225
a.plot(cyc,g(cyc),'o',color=YELLOW,ms=4.6,mew=0,zorder=6); a.plot([0],[0],'o',color=RED,ms=4.4,mew=0,zorder=6)
a.set_xlabel('$x$',labelpad=1); a.set_ylabel(r'$f^{\prime}(x)$',labelpad=0); a.set_xticks([-2,0,2]); a.set_xlim(-2.6,3)
def hb(T):
    y=[3.3,3.3]
    for t in range(T): y.append(y[-1]-float(g(y[-1]))/9+4/9*(y[-1]-y[-2]))
    return np.array(y[1:])
def nag(T):
    q=1/5;be=(1-q)/(1+q);y=[3.3,3.3]
    for t in range(T):
        z=y[-1]+be*(y[-1]-y[-2]); y.append(z-float(g(z))/25)
    return np.array(y[1:])
T=45; b.plot(range(T+1),hb(T),'-o',color=YELLOW,lw=1,ms=2.4,mew=0); b.plot(range(T+1),nag(T),'-o',color=GREEN,lw=1.2,ms=2.4,mew=0)
for v in cyc: b.axhline(v,color=MUTED,lw=.65,ls=':')
b.set_xlabel('$t$',labelpad=1); b.set_ylabel('$x^{(t)}$',labelpad=0); b.set_xlim(0,45); b.set_ylim(-4.5,4.5); b.text(21,3.25,'重球',fontsize=7.5,ha='center',color=INK); b.text(27,-.75,'Nesterov',fontsize=7.5,ha='center',color=INK)
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
save(fig,HERE,'figure',{'cycle':'(792,-2208,2592)/1225','alpha':1/9,'beta':4/9,'x0':3.3})
