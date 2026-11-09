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

fig,ax=figure(width_mm=100,height_mm=52)
panel(fig,.09,.98,.97,.17)
X=np.linspace(-1.2,2.2,801)
ax.axvspan(1,2.2,color=BLUE_FILL,lw=0,zorder=0)
ax.axvline(1,color=STROKE,lw=1.7,zorder=2)
ax.plot(X,X,color=BLUE,lw=1.0,ls='--')
for r,ls in ((1,'-'),(2,'-'),(5,'-')):
    Q=X+r/2*np.maximum(1-X,0)**2
    ax.plot(X,Q,color=BLUE,lw=1.4)
    xr=1-1/r; it(ax,xr,xr+r/2*(1/r)**2)
opt(ax,1,1)
ax.set_xlim(-1.2,2.2);ax.set_ylim(-1.1,2.2);ax.set_xticks([-1,0,.5,.8,1,2]);ax.set_xticklabels(['$-1$','$0$','$0.5$','$0.8$','$1$','$2$'])
ax.set_yticks([-1,0,1,2]);ax.set_xlabel('$x$',labelpad=1)
ax.text(-.72,1.55,'$\\rho=1$',color=INK);ax.text(.02,1.32,'$\\rho=2$',color=INK);ax.text(.26,1.12,'$\\rho=5$',color=INK)
ax.text(-.95,-.5,'$f(x)=x$',color=MUTED,fontsize=7.5);ax.text(1.42,.25,'可行',color=INK)
ax.text(.5,-.62,'不可行',color=RED)
save(fig,HERE,'figure',{'objective':'x+rho/2*max(1-x,0)^2','rho':[1,2,5],'minimizers':[0,.5,.8]})
