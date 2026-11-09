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
X,Y=np.meshgrid(np.linspace(-1,5,500),np.linspace(-1.5,3,500))
for ax,nu in zip(axs,(0,-2.4,-3)):
    c=np.array([-nu,-nu/3])
    ax.contour(X,Y,.5*(X-c[0])**2+1.5*(Y-c[1])**2,levels=[.25,1,2.25,4,6.25],colors=BLUE,linewidths=.75)
    line(ax)
    if nu!=-3: it(ax,*c)
    opt(ax,3,1)
    ax.plot([0,3],[0,1],color=MUTED,lw=.85,ls=':')
    ax.set_xlim(-1,5);ax.set_ylim(-1.5,3);ax.set_aspect('equal');ax.set_xticks([0,3]);ax.set_yticks([-1,1,3] if ax is axs[0] else []);ax.set_xlabel('$x_1$',labelpad=1)
    if ax is not axs[0]: ax.spines['left'].set_visible(False)
axs[0].set_ylabel('$x_2$',labelpad=1)
fig.canvas.draw()
for ax,l in zip(axs,('(a) $\\nu=0$','(b) $\\nu=-2.4$','(c) $\\nu=-3$')): tag(fig,ax,l)
save(fig,HERE,'figure',{'L':'f+nu*(x1+x2-4)','x(nu)':'-nu*(1,1/3)'})
