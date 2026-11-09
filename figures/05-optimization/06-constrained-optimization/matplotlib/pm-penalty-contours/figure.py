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

fig,axs=figure(width_mm=112,height_mm=46,ncols=3)
panel(fig,.07,.99,.97,.25,wspace=.1)
X,Y=np.meshgrid(np.linspace(0,5,500),np.linspace(-1.5,3,500))
for ax,r,lab in zip(axs,(1.5,15,150),('(a) $\\rho=1.5$','(b) $\\rho=15$','(c) $\\rho=150$')):
    H=G+r*np.outer(A1,A1); xr=np.linalg.solve(H,4*r*A1); v0=fq(*xr)+r/2*(xr.sum()-4)**2
    Q=fq(X,Y)+r/2*(X+Y-4)**2
    ax.contour(X,Y,Q-v0,levels=[.15,.6,1.5,3,6,10,16],colors=BLUE,linewidths=.75)
    line(ax); opt(ax,3,1); it(ax,*xr)
    ax.set_xlim(0,5);ax.set_ylim(-1.5,3);ax.set_aspect('equal');ax.set_xticks([0,3]);ax.set_yticks([-1,1,3] if ax is axs[0] else [])
    ax.set_xlabel('$x_1$',labelpad=1)
    if ax is not axs[0]: ax.spines['left'].set_visible(False)
axs[0].set_ylabel('$x_2$',labelpad=1)
fig.canvas.draw()
for ax,lab in zip(axs,('(a) $\\rho=1.5$','(b) $\\rho=15$','(c) $\\rho=150$')): tag(fig,ax,lab)
save(fig,HERE,'figure',{'Q':'f+rho/2*(x1+x2-4)^2','rho':[1.5,15,150]})
