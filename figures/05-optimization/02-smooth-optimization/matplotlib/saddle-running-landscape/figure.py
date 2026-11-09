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
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2); panel(fig,.07,.985,.97,.25,wspace=.28)
contour(a,(-1.6,1.6),(-1.2,1.2)); minima(a); saddle(a)
A=dict(arrowstyle='-|>',lw=1.2,mutation_scale=7,shrinkA=2.5,shrinkB=0)
for s in (1,-1):
    a.annotate('',xy=(.52*s,0),xytext=(0,0),arrowprops=dict(color=RED,**A))
    a.annotate('',xy=(0,.42*s),xytext=(0,0),arrowprops=dict(color=STROKE,**A))
a.text(.09,.36,'$+1$',fontsize=7.5); a.text(.27,-.17,'$-1$',fontsize=7.5)
a.text(1.0,.11,'$(1,0)$',fontsize=7.5,ha='center'); a.text(-1.0,.11,'$(-1,0)$',fontsize=7.5,ha='center')
a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0); a.set_xticks([-1,0,1]); a.set_yticks([-1,0,1])
x=np.linspace(-1.6,1.6,400); b.plot(x,.25*(x*x-1)**2,color=BLUE,lw=1.4)
minima(b); saddle(b,0,.25); b.plot([-1.6,1.6],[.25,.25],color=MUTED,lw=.85,ls=(0,(3,2)))
b.text(.08,.285,'$f=1/4$',fontsize=7.5); b.set_xlabel('$x_1$',labelpad=1); b.set_ylabel('$f(x_1,0)$',labelpad=1); b.set_ylim(-.04,.62); b.set_xticks([-1,0,1])
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'f':'(x1^2-1)^2/4+x2^2/2'})
