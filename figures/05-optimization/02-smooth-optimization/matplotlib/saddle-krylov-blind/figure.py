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
def tag(fig, ax, s, y=.05):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='top')
# 贯穿例 f(x)=(x1^2-1)^2/4+x2^2/2，L=2 与 M=6 在 |x1|<=1 上成立，alpha=1/2。
def F(x): return .25*(x[0]**2-1)**2+.5*x[1]**2
def G(x): return np.array([x[0]**3-x[0],x[1]])
LEV=[.02,.08,.16,.25,.4,.65,1,1.5]
def contour(ax,xr,yr,levels=LEV):
    X,Y=np.meshgrid(np.linspace(*xr,700),np.linspace(*yr,500))
    ax.contour(X,Y,.25*(X**2-1)**2+.5*Y**2,levels=levels,colors=[BLUE],linewidths=.65)
def minima(ax,pts=((1,0),(-1,0))):
    for x,y in pts: ax.plot([x],[y],'o',ms=4.8,color=RED,mew=0,zorder=6)
def saddle(ax,x=0,y=0): ax.plot([x],[y],'o',mfc='white',mec=RED,ms=5,mew=1,zorder=7)
fig,a=figure(width_mm=100,height_mm=48); panel(fig,.12,.985,.97,.18)
lam=np.array([-1.,1.]); K=55; 
for s,c,lw,ls in ((0.,YELLOW,1.8,'-'),(1e-8,GREEN,1.3,'-'),(1e-4,GREEN,1.3,(0,(4,2))),(.7,GREEN,1.3,(0,(1,1.5)))):
    v=np.array([s,np.sqrt(1-s*s)]); R=[]
    for k in range(K+1):
        R.append(v@(lam*v)); v=(2-lam)*v; v/=np.linalg.norm(v)
    a.plot(R,color=c,lw=lw,ls=ls)
a.axhline(0,color=MUTED,lw=.85,ls=(0,(3,2))); a.set_xlim(0,K); a.set_ylim(-1.15,1.2)
a.text(38,1.04,'$s=0$',fontsize=7.5); a.text(19.5,-.55,'$10^{-8}$',fontsize=7.5); a.text(10.5,-.6,'$10^{-4}$',fontsize=7.5); a.text(2.3,-.55,'$0.7$',fontsize=7.5)
a.set_xlabel('Hessian 向量积次数',labelpad=1); a.set_ylabel('Rayleigh 商',labelpad=1)
save(fig,HERE,'figure',{'H':'diag(-1,1)','c':2,'v0':'(s,sqrt(1-s^2))'})
