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
panel(fig,.07,.99,.99,.25,wspace=.14)
X,Y=np.meshgrid(np.linspace(-.3,3.8,500),np.linspace(-.5,2.,500))
r=1.5;H=G+r*np.outer(A1,A1);c=np.linalg.solve(H,6*A1)
Q=.5*(((X-c[0])**2)*H[0,0]+2*(X-c[0])*(Y-c[1])*H[0,1]+((Y-c[1])**2)*H[1,1])
a.contour(X,Y,Q,levels=[.1,.5,1.2,2.5,4.5,7.5],colors=BLUE,linewidths=.75)
line(a)
a.plot([0,2.4,2.4],[0,0,8/15],color=YELLOW,lw=1.8,marker='o',ms=3.4,mew=0,zorder=5)
it(a,*c,ms=5,z=7)
a.text(1.1,-.3,'更新x',color=YELLOW,fontsize=7.5,ha='center');a.text(2.47,.17,'更新z',color=YELLOW,fontsize=7.5)
a.text(c[0]-.08,c[1]+.14,'联合解',color=GREEN,fontsize=7.5,ha='right')
for ax in (a,b):
    ax.set_xlim(-.3,3.8);ax.set_ylim(-.5,2);ax.set_aspect('equal');ax.set_xticks([0,1,2,3]);ax.set_xlabel('$x$',labelpad=1)
a.set_yticks([0,1,2]);a.set_ylabel('$z$',labelpad=1);b.set_yticks([]);b.spines['left'].set_visible(False)
line(b)
x=0.;z=0.;u=0.;P=[(x,z)]
for t in range(10):
    x=r*(4-z-u)/(1+r);P.append((x,z));z=r*(4-x-u)/(3+r);P.append((x,z));u+=x+z-4
P=np.array(P)
b.plot(P[:,0],P[:,1],color=YELLOW,lw=1.5,zorder=4)
b.plot(P[::2,0],P[::2,1],'o',color=YELLOW,ms=3,mew=0,zorder=5)
nu=0.;Q2=[(0,0)]
for t in range(7):
    v=np.linalg.solve(H,(6-nu)*A1);Q2.append(tuple(v));nu+=r*(v.sum()-4)
Q2=np.array(Q2);b.plot(Q2[:,0],Q2[:,1],'-o',color=GREEN,lw=1.3,ms=3.4,mew=0,zorder=6)
opt(b,3,1,z=8)
b.text(1.05,.72,'ALM',color=GREEN,fontsize=7.5,ha='right');b.text(1.5,.05,'ADMM',color=YELLOW,fontsize=7.5)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'rho':1.5,'one_sweep':[2.4,8/15],'joint':[2,2/3]})
