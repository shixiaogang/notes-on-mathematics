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

fig,ax=figure(width_mm=96,height_mm=50)
panel(fig,.12,.97,.97,.17)
Am=np.array([[1,1,1],[1,1,2],[1,2,2.]])
# min 0 s.t. A1 x1+A2 x2+A3 x3=0, rho=1: direct three-block ADMM, Gauss-Seidel order
def run3(T):
    x=np.ones(3);nu=np.zeros(3);R=[]
    for t in range(T):
        for i in range(3):
            ai=Am[:,i];x[i]=-(ai@(Am@x-ai*x[i])+ai@nu)/(ai@ai)
        r=Am@x;nu=nu+r;R.append(np.linalg.norm(r))
    return R
# merged blocks: x1 | (x2,x3), two-block ADMM, same matrix
def run2(T):
    x=np.ones(3);nu=np.zeros(3);R=[];B=Am[:,1:]
    for t in range(T):
        a=Am[:,0];x[0]=-(a@(B@x[1:])+a@nu)/(a@a)
        x[1:]=np.linalg.solve(B.T@B,-B.T@(a*x[0]+nu))
        r=Am@x;nu=nu+r;R.append(np.linalg.norm(r))
    return R
T=np.arange(1,301)
R3=run3(300);R2=run2(300)
ax.semilogy(T,R3,color=RED,lw=1.4);ax.semilogy(T,np.maximum(R2,1e-16),color=GREEN,lw=1.4)
ax.set_xlim(1,300);ax.set_ylim(1e-9,1e5);ax.set_xticks([1,100,200,300]);ax.set_xlabel('$t$',labelpad=1);ax.set_ylabel('$\\|\\mathbf{r}^{(t)}\\|_2$',labelpad=1)
ax.text(190,1.8e3,'三块',color=RED);ax.text(100,1e-6,'两块',color=GREEN)
save(fig,HERE,'figure',{'A':Am.tolist(),'rho':1,'start':[1,1,1]})
