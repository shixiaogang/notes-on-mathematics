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
panel(fig,.11,.98,.97,.27,wspace=.3)
D=np.array([[1,1],[1,0],[0,1.]]);y=np.array([3,2,-1.]);gam=1.
S=lambda v,t:np.sign(v)*np.maximum(abs(v)-t,0)
def run(rho,T=2000,tol=None):
    K=np.linalg.inv(D.T@D+rho*np.eye(2));z=np.zeros(2);u=np.zeros(2);R=[];Dd=[]
    for t in range(T):
        x=K@(D.T@y+rho*(z-u));zo=z;z=S(x+u,gam/rho);u=u+x-z
        R.append(np.linalg.norm(x-z));Dd.append(rho*np.linalg.norm(z-zo))
        if tol and max(R[-1],Dd[-1])<=tol: return t+1
    return R,Dd
R,Dd=run(1.,T=30)
T=np.arange(1,31)
a.semilogy(T,R,color=RED,lw=1.4);a.semilogy(T,Dd,color=PURPLE,lw=1.4,ls='--')
a.set_xlabel('$t$',labelpad=1);a.set_ylabel('残差范数',labelpad=1);a.set_xticks([1,10,20,30]);a.set_ylim(1e-6,3)
a.text(19,.012,'$\\|\\mathbf{r}^{(t)}\\|_2$',color=RED);a.text(5.5,1e-4,'$\\|\\mathbf{s}^{(t)}\\|_2$',color=PURPLE)
rs=np.logspace(-2,2,41);n=[run(r,T=20000,tol=1e-6) for r in rs]
b.loglog(rs,n,color=GREEN,lw=1.4);b.set_xlabel('$\\rho$',labelpad=1);b.set_ylabel('轮数',labelpad=1)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'rho_grid':rs.round(4).tolist(),'iters':n})
