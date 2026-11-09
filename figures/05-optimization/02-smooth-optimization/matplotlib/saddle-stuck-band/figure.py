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
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2); panel(fig,.07,.985,.97,.24,wspace=.2)
r=.25; Fth=.05
X,Y=np.meshgrid(np.linspace(-r,r,1001),np.linspace(-r,r,1001))
for ax,T,s in ((a,3,'(a)'),(b,8,'(b)')):
    u,v=X.copy(),Y.copy()
    for t in range(T): u,v=u-.5*(u**3-u),v-.5*v
    stuck=.25*(u**2-1)**2+.5*v**2>.25-Fth; ball=X*X+Y*Y<=r*r
    Z=np.where(ball&stuck,1.,0.); ax.contourf(X,Y,Z,levels=[.5,2],colors=[RED_FILL])
    ax.contour(X,Y,Z,levels=[.5],colors=[RED],linewidths=.85)
    t=np.linspace(0,2*np.pi,400); ax.plot(r*np.cos(t),r*np.sin(t),color=BLUE,lw=1.1); saddle(ax)
    ax.set_aspect('equal'); ax.set_xlim(-.28,.28); ax.set_ylim(-.28,.28); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=0); ax.set_xticks([-.2,0,.2]); ax.set_yticks([-.2,0,.2]); tag(fig,ax,s)
    h=np.abs(X[ball&stuck]).max(); print(T,h)
save(fig,HERE,'figure',{'r':r,'F':Fth,'T':[3,8],'alpha':.5})
