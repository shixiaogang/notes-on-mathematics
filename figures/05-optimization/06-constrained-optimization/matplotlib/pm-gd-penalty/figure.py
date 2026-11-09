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
def opt(ax, x, y, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
def it(ax, x, y, ms=4.2, z=6, c=GREEN): ax.plot([x],[y],'o',ms=ms,color=c,mew=0,zorder=z)
def bare(ax): ax.set_aspect('equal'); 
# Running example: f(x)=x1^2/2+3x2^2/2, h(x)=x1+x2-4, x*=(3,1), nu*=-3.
G = np.diag([1.,3.]); A1 = np.ones(2)
def fq(X,Y): return .5*X**2+1.5*Y**2
def line(ax,lo=-2,hi=7):
    t=np.array([lo,hi]); ax.plot(t,4-t,color=STROKE,lw=1.7,solid_capstyle='butt',zorder=3)

fig,axs=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.07,.99,.98,.27,wspace=.12)
X,Y=np.meshgrid(np.linspace(-.5,5,500),np.linspace(-1.5,4,500))
for ax,r in zip(axs,(1.5,15)):
    H=G+r*np.outer(A1,A1);L=np.linalg.eigvalsh(H)[1];rhs=4*r*A1
    xr=np.linalg.solve(H,rhs)
    Q=.5*(((X-xr[0])**2)*H[0,0]+2*(X-xr[0])*(Y-xr[1])*H[0,1]+((Y-xr[1])**2)*H[1,1])
    ax.contour(X,Y,Q,levels=[.5,2,5,10,18,30],colors=BLUE,linewidths=.75)
    line(ax)
    x=np.array([0.,3.5]);P=[x]
    for _ in range(25):
        x=x-(H@x-rhs)/L;P.append(x)
    P=np.array(P);ax.plot(P[:,0],P[:,1],'-',color=GREEN,lw=1.1,marker='o',ms=2.4,mew=0,zorder=5)
    opt(ax,*xr,ms=4.2)
    ax.set_xlim(-.5,5);ax.set_ylim(-1.5,4);ax.set_aspect('equal');ax.set_xticks([0,2,4]);ax.set_xlabel('$x_1$',labelpad=1)
    ax.set_yticks([0,2,4] if ax is axs[0] else [])
    if ax is not axs[0]: ax.spines['left'].set_visible(False)
axs[0].set_ylabel('$x_2$',labelpad=1)
fig.canvas.draw();tag(fig,axs[0],'(a) $\\rho=1.5$');tag(fig,axs[1],'(b) $\\rho=15$')
save(fig,HERE,'figure',{'start':[0,3.5],'steps':25,'stepsize':'1/L'})
