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
panel(fig,.12,.98,.97,.27,wspace=.3)
R=np.logspace(0,4,60)
viol=12/(3+4*R)
a.loglog(R,viol,color=RED,lw=1.4)
a.loglog(R,12/(3+4*R)*R/(R),color=RED,lw=0)
for r in (1.5,15,150,1500): it(a,r,12/(3+4*r))
a.set_xlabel('$\\rho$',labelpad=1);a.set_ylabel('$|h(\\mathbf{x}_\\rho)|$',labelpad=1)
kap=[]
for r in R:
    e=np.linalg.eigvalsh(G+r*np.outer(A1,A1));kap.append(e[1]/e[0])
b.loglog(R,kap,color=BLUE,lw=1.4)
# gradient descent with step 1/L, warm started, inner tolerance 1e-3
def gd(H,rhs,x):
    L=np.linalg.eigvalsh(H)[1];c=0
    while True:
        gr=H@x-rhs
        if np.linalg.norm(gr)<=1e-3: return x,c
        x=x-gr/L;c+=1
x=np.zeros(2);cs=[]
RR=[1.5,15,150,1500]
for r in RR:
    x,c=gd(G+r*np.outer(A1,A1),4*r*A1,x);cs.append(c)
b.loglog(RR,cs,'-o',color=GREEN,ms=4,lw=1.4,mew=0)
b.set_xlabel('$\\rho$',labelpad=1)
b.text(120,6,'条件数',color=BLUE);b.text(4.5,500,'梯度步数',color=GREEN)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'gd_steps':cs,'rho':RR,'inner_tol':1e-3})
