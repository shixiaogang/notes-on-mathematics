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
fig,a=figure(width_mm=92,height_mm=48); panel(fig,.16,.965,.97,.18)
x=np.array([.3,.2]); v=np.array([1,1])/np.sqrt(2); Hv=np.array([(3*x[0]**2-1)*v[0],v[1]])
h=np.logspace(-13,0,160); e=[np.linalg.norm((G(x+t*v)-G(x))/t-Hv) for t in h]
a.loglog(h,e,color=GREEN,lw=1.4); a.loglog(h,3*h,color=PURPLE,lw=.95,ls=(0,(3,2)))
a.text(.018,.33,'$Mh/2$',fontsize=7.5,ha='right'); a.text(1.5e-11,2.5e-6,'舍入误差主导',fontsize=7.5,ha='left'); a.text(2e-6,1.2e-9,'实际误差',fontsize=7.5)
a.set_xlabel('$h$',labelpad=1); a.set_ylabel('$\\Vert \\hat h-Hv\\Vert_2$',labelpad=1); a.set_ylim(1e-11,10); a.set_xlim(1e-13,1)
save(fig,HERE,'figure',{'x':[.3,.2],'v':'(1,1)/sqrt2','M':6})
