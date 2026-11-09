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
panel(fig,.11,.97,.97,.27,wspace=.32)
q=lambda l:np.where(l<=.5,l-2,-3*l)
L=np.linspace(0,1,401)
a.plot(L,q(L),color=PURPLE,lw=1.4)
for l,s,c in ((.5,1,MUTED),(.5,-3,MUTED)):
    t=np.array([.32,.68]);a.plot(t,-1.5+s*(t-.5),color=c,lw=.85,ls=':')
# supergradient ascent, alpha=.12, ties broken not needed
lam=0.;alpha=.12;Lam=[];Sx=[]
for t in range(40):
    x=1. if lam<.5 else 0.
    Lam.append(lam);Sx.append(2*x)
    g=2*x*2-3
    lam=max(0,lam+alpha*g)
Lam=np.array(Lam);Sx=np.array(Sx)
for i in range(9):
    it(a,Lam[i],float(q(Lam[i])),ms=3.6)
opt(a,.5,-1.5)
a.set_xlim(0,1);a.set_ylim(-3.1,-1.2);a.set_xticks([0,.5,1]);a.set_xticklabels(['$0$','$0.5$','$1$']);a.set_yticks([-3,-2.5,-2,-1.5]);a.set_xlabel('$\\lambda$',labelpad=1);a.set_ylabel('$q(\\lambda)$',labelpad=1)
T=np.arange(1,41);avg=np.cumsum(Sx)/T
b.plot(T,Sx,color=GREEN,lw=.95,marker='o',ms=2.4,mew=0)
b.plot(T,avg,color=YELLOW,lw=1.8)
b.axhline(1.5,color=STROKE,lw=1.5)
b.set_xlim(1,40);b.set_ylim(-.15,2.2);b.set_xticks([1,10,20,30,40]);b.set_yticks([0,1,1.5,2]);b.set_yticklabels(['$0$','$1$','$1.5$','$2$']);b.set_xlabel('$t$',labelpad=1);b.set_ylabel('$x_1^{(t)}+x_2^{(t)}$',labelpad=1)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'lambda_seq':Lam[:10].round(4).tolist(),'avg_last':float(avg[-1])})
