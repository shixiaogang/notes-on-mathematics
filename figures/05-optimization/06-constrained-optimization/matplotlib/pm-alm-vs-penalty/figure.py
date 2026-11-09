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
T=np.arange(1,7)
# penalty: rho_t=1.5*10^(t-1); ALM: rho=1.5, nu update
pen=[12/(3+4*1.5*10**(t-1)) for t in T]
nu=0.;alm=[]
for t in T:
    c=np.linalg.solve(G+1.5*np.outer(A1,A1),(6-nu)*A1);h=c.sum()-4;alm.append(abs(h));nu+=1.5*h
a.semilogy(T,pen,'-o',color=YELLOW,lw=1.8,ms=4,mew=0)
a.semilogy(T,alm,'-o',color=GREEN,lw=1.4,ms=4,mew=0)
a.set_xticks(T);a.set_xlabel('外层轮数',labelpad=1);a.set_ylabel('$|h(\\mathbf{x}^{(t)})|$',labelpad=1)
a.text(1.2,.004,'二次罚',color=YELLOW,fontsize=7.5);a.text(4.35,.11,'ALM',color=GREEN,ha='center',fontsize=7.5)
R=np.logspace(-1,3,120)
fac=3/(3+4*R)
kap=[(lambda e:e[1]/e[0])(np.linalg.eigvalsh(G+r*np.outer(A1,A1))) for r in R]
b.loglog(R,fac,color=GREEN,lw=1.4);b.loglog(R,kap,color=BLUE,lw=1.4)
b.set_xlabel('$\\rho$',labelpad=1);b.text(.13,.03,'外层压缩因子',color=GREEN,fontsize=7.5);b.text(20,120,'内层条件数',color=BLUE,fontsize=7.5,ha='right')
b.set_ylim(2e-3,1e3)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'alm':alm,'penalty':pen,'factor':'3/(3+4rho)'})
