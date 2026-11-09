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

fig,ax=figure(width_mm=100,height_mm=58)
panel(fig,.11,.98,.97,.15)
H0=G
def gd(H,rhs,x,tol,cnt,log,h):
    L=np.linalg.eigvalsh(H)[1]
    for _ in range(200000):
        gr=H@x-rhs
        if np.linalg.norm(gr)<=tol: break
        x=x-gr/L;cnt[0]+=1
    return x
tol=1e-6
# quadratic penalty, tenfold increase, warm start
x=np.zeros(2);c=[0];Pc=[];Ph=[]
for k in range(5):
    r=1.5*10**k;x=gd(G+r*np.outer(A1,A1),4*r*A1,x,tol,c,0,0);Pc.append(c[0]);Ph.append(abs(x.sum()-4))
# dual ascent alpha=.6, inner gradient on L
x=np.zeros(2);nu=0.;c=[0];Dc=[];Dh=[]
for k in range(10):
    x=gd(G,-nu*A1,x,tol,c,0,0);h=x.sum()-4;Dc.append(c[0]);Dh.append(abs(h));nu+=.6*h
# ALM rho=1.5
x=np.zeros(2);nu=0.;c=[0];Ac=[];Ah=[];r=1.5;H=G+r*np.outer(A1,A1)
for k in range(10):
    x=gd(H,(4*r-nu)*A1,x,tol,c,0,0);h=x.sum()-4;Ac.append(c[0]);Ah.append(abs(h));nu+=r*h
# ADMM rho=1.5: each block has a closed form, one gradient-equivalent per block evaluation counted as one
x=0.;z=0.;u=0.;Mc=[];Mh=[];r=1.5
for k in range(24):
    x=r*(4-z-u)/(1+r);z=r*(4-x-u)/(3+r);h=x+z-4;u+=h;Mc.append(k+1);Mh.append(abs(h))
ax.loglog(Pc,Ph,'-o',color=YELLOW,lw=1.8,ms=3.8,mew=0)
ax.loglog(Dc[1:],Dh[1:],'-o',color=PURPLE,lw=1.2,ms=3.4,mew=0)
ax.loglog(Ac,Ah,'-o',color=GREEN,lw=1.4,ms=3.6,mew=0)
ax.loglog(Mc,Mh,'-o',color=BLUE,lw=1.2,ms=2.8,mew=0)
ax.set_xlabel('累计内层梯度步数（ADMM 记轮数）',labelpad=1);ax.set_ylabel('$|h(\\mathbf{x}^{(t)})|$',labelpad=1)
ax.set_xlim(.8,3e4);ax.set_ylim(1e-5,6)
ax.text(3000,.25,'二次罚',color=YELLOW);ax.text(320,2.3e-4,'ALM',color=GREEN);ax.text(95,1.2e-4,'对偶上升',color=PURPLE,ha='right');ax.text(2.3,1.3e-2,'ADMM',color=BLUE)
save(fig,HERE,'figure',{'penalty':[Pc,Ph],'dual':[Dc,Dh],'alm':[Ac,Ah],'admm':[Mc,Mh],'inner_tol':tol})
