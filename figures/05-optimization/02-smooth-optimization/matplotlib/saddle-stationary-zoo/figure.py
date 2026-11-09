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
fig,axs=figure(width_mm=112,height_mm=38,ncols=4); panel(fig,.015,.985,.97,.19,wspace=.1)
fs=[lambda x,y:-x**2-y**2,lambda x,y:x**2-y**4,lambda x,y:x**4-y**4,lambda x,y:x**3-3*x*y**2]
X,Y=np.meshgrid(np.linspace(-1,1,500),np.linspace(-1,1,500))
lv=[[-1.2,-.7,-.3,-.08],[-.6,-.2,-.05,.05,.2,.6],[-.6,-.2,-.05,.05,.2,.6],[-1.2,-.5,-.1,.1,.5,1.2]]
for ax,h,l,s in zip(axs,fs,lv,'abcd'):
    Z=h(X,Y); ax.contourf(X,Y,Z,levels=[-99,0],colors=[RED_FILL])
    ax.contour(X,Y,Z,levels=sorted(l),colors=[BLUE],linewidths=.65)
    ax.plot([0],[0],'o',mfc='white',mec=RED,ms=4.5,mew=1,zorder=6)
    ax.set_xlim(-1,1); ax.set_ylim(-1,1); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    for k in ax.spines: ax.spines[k].set_visible(True); ax.spines[k].set_linewidth(.6); ax.spines[k].set_color(GRID)
    tag(fig,ax,f'({s})',y=.13)
save(fig,HERE,'figure',{'f':['-x1^2-x2^2','x1^2-x2^4','x1^4-x2^4','x1^3-3x1x2^2'],'fill':'f<f(0)'})
