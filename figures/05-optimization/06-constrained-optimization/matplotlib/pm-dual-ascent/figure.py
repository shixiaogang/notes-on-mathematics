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

fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.08,.99,.97,.27,wspace=.2)
q=lambda n:-(2/3)*n**2-4*n
N=np.linspace(-6.8,1,601)
for ax,alpha,T in ((a,.6,5),(b,1.5,4)):
    ax.plot(N,q(N),color=PURPLE,lw=1.4)
    n=0.
    for t in range(T):
        h=-(4/3)*n-4;m=n+alpha*h
        ax.annotate('',xy=(m,q(m)),xytext=(n,q(n)),arrowprops=dict(arrowstyle='-|>',mutation_scale=7,color=GREEN,lw=1.0,shrinkA=1.5,shrinkB=1.5,connectionstyle='arc3,rad=-.25' if ax is b and t%2==0 else 'arc3,rad=-.25'))
        it(ax,n,q(n));n=m
    it(ax,n,q(n))
    ax.axhline(6,color=RED,lw=.85,ls=':');opt(ax,-3,6)
    ax.set_xlim(-6.8,1);ax.set_ylim(-5,7.5);ax.set_xticks([-6,-3,0]);ax.set_yticks([0,3,6]);ax.set_xlabel('$\\nu$',labelpad=1)
a.set_ylabel('$q(\\nu)$',labelpad=1)
fig.canvas.draw();tag(fig,a,'(a) $\\alpha=0.6$');tag(fig,b,'(b) $\\alpha=1.5$')
save(fig,HERE,'figure',{'q':'-(2/3)nu^2-4nu','alpha':[.6,1.5]})
