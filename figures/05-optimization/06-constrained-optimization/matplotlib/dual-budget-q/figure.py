from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    H=fig.get_figheight()*25.4
    if len(fig.axes)>1: bottom=15.5/H
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tag(fig, ax, s, y=None):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, 1.0/(fig.get_figheight()*25.4), s, ha='center', va='bottom')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
def dot(ax, x, y, c=GREEN, ms=4.2, z=6, m='o'): ax.plot([x],[y],m,ms=ms,color=c,mew=0,zorder=z)
def hollow(ax, x, y, c=BLUE, ms=4.4, z=7): ax.plot([x],[y],'o',ms=ms,mfc='white',mec=c,mew=1.0,zorder=z)

# min ((x1-2)^2+(x2-1)^2)/2, x>=0 为规定定义域，乘子对应 x1+x2<=2。
def xl(l): return np.maximum(2-l,0),np.maximum(1-l,0)
def q(l):
    a,b=xl(l); return .5*((a-2)**2+(b-1)**2)+l*(a+b-2)
fig,(A,B)=figure(width_mm=112,height_mm=58,ncols=2)
panel(fig,.065,.985,.975,.21,wspace=.24)
A.fill([0,2,0],[0,0,2],color=BLUE_FILL,lw=0,zorder=0)
x=np.linspace(-.3,2.8,300);y=np.linspace(-.3,2.4,300);X,Y=np.meshgrid(x,y)
A.contour(X,Y,.5*((X-2)**2+(Y-1)**2),levels=[.05,.25,.75,1.5,2.5],colors=BLUE,linewidths=.8)
A.plot([0,2],[2,0],color=STROKE,lw=1.7);A.plot([0,2],[0,0],color=BLUE,lw=.9);A.plot([0,0],[0,2],color=BLUE,lw=.9)
L=np.linspace(0,2,200);a,b=xl(L);A.plot(a,b,color=PURPLE,lw=1.4,ls='--')
for l in (0,1,2): 
    p=xl(l);dot(A,float(p[0]),float(p[1]),PURPLE,ms=3.8)
A.text(2.05,1.1,r'$\lambda=0$',fontsize=7.5);A.text(.98,-.2,r'$\lambda=1$',fontsize=7.5,ha='center');A.text(-.04,-.2,r'$\lambda=2$',fontsize=7.5,ha='center')
opt(A,1.5,.5);A.text(1.0,.45,r'$x^\star$',color=INK)
A.set_xlim(-.3,2.8);A.set_ylim(-.35,2.4);A.set_xticks([0,1,2]);A.set_yticks([0,1,2]);A.set_xlabel('$x_1$',labelpad=1);A.set_ylabel('$x_2$',labelpad=1)
L=np.linspace(0,2.7,400);B.plot(L,q(L),color=PURPLE,lw=1.5)
B.axhline(.25,color=BLUE,lw=.95,ls='--');B.text(2.68,.3,r'$f^\star=1/4$',ha='right',fontsize=7.5)
opt(B,.5,.25)
for l in (1,2): dot(B,l,float(q(np.array(l))),PURPLE,ms=3.8)
B.text(1.06,.05,r'$\lambda=1$',fontsize=7.5);B.text(2.08,-1.45,r'$\lambda=2$',fontsize=7.5)
B.set_xlim(0,2.7);B.set_ylim(-2.1,.65);B.set_xticks([0,.5,1,2]);B.set_yticks([-2,-1,0,.25]);B.set_xlabel(r'$\lambda$',labelpad=1);B.text(1.25,-.9,r'$q(\lambda)$',color=INK)
for a_,s in zip((A,B),('(a)','(b)')):tag(fig,a_,s)
save(fig,HERE,'figure',{'q':'lam-lam^2 on [0,1]; 1/2-lam^2/2 on [1,2]; 5/2-2lam for lam>2'})
