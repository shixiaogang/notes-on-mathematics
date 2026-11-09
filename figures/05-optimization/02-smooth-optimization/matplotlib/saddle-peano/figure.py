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
fig,(a,b)=figure(width_mm=112,height_mm=54,ncols=2); panel(fig,.105,.985,.97,.26,wspace=.32)
x=np.linspace(-1,1,500); a.fill_between(x,x*x,2*x*x,color=RED_FILL,lw=0)
a.plot(x,x*x,color=STROKE,lw=1.2); a.plot(x,2*x*x,color=STROKE,lw=1.2)
for m in (.3,1,3,-1,-3): a.plot(x,m*x,color=BLUE,lw=.85)
a.plot([-.0],[0],'o',mfc='white',mec=RED,ms=5,mew=1,zorder=6)
a.text(.47,.08,'$x_2=x_1^2$',fontsize=7.5); a.text(-.32,.72,'$x_2=2x_1^2$',fontsize=7.5,ha='right')
a.set_xlim(-.8,.8); a.set_ylim(-.4,1.1); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0)
t=np.linspace(-.3,.3,400)
b.plot(t,t*t*(1-t)*(1-2*t),color=BLUE,lw=1.4); b.plot(t,-.25*t**4,color=RED,lw=1.4)
b.plot([-.3,.3],[0,0],color=MUTED,lw=.85,ls=(0,(3,2)))
b.text(-.15,.078,'$x_2=x_1$',fontsize=7.5,color=INK); b.text(.02,-.006,'$x_2=\\frac{3}{2}x_1^2$',fontsize=7.5,color=INK,va='top')
b.set_ylim(-.016,.1); b.set_xlabel('$x_1$',labelpad=1); b.set_ylabel('$f$',labelpad=1)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'f':'(x2-x1^2)(x2-2x1^2)'})
