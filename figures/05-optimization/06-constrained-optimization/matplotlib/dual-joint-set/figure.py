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

# (a) v(u)=max(1-u,0)^2/2；(b) min x, x^2<=u，v(u)=-sqrt(u)，q(lam)=-1/(4lam)。
fig,(A,B)=figure(width_mm=112,height_mm=58,ncols=2)
panel(fig,.08,.985,.975,.21,wspace=.22)
U=np.linspace(-1.3,2,300);v=.5*np.maximum(1-U,0)**2
A.fill_between(U,v,3.2,color=BLUE_FILL,lw=0,zorder=0);A.plot(U,v,color=BLUE,lw=1.5,zorder=4)
A.plot(U,.5-U,color=PURPLE,lw=1.3,zorder=3);A.plot([0,0],[-1,3.2],color=STROKE,lw=1.4,zorder=2)
opt(A,0,.5);dot(A,-1,2,GREEN,ms=4.6);A.text(-.92,2.08,'Slater点',fontsize=7.5,va='bottom')
A.text(.08,.58,r'$(0,f^\star)$',fontsize=7.5);A.text(1.0,2.2,r'$\bm{A}$'.replace(r'\bm{A}','A'),color=INK);A.text(1.6,-.3,r'$t=\frac{1}{2}-u$',fontsize=7.5,ha='center')
A.set_xlim(-1.3,2);A.set_ylim(-1,3.2);A.set_xticks([-1,0,1,2]);A.set_yticks([-1,0,1,2,3]);A.set_xlabel('$u$',labelpad=1);A.set_ylabel('$t$',labelpad=1)
U=np.linspace(0,2.2,300)
B.axvspan(-1,0,color=RED_FILL,lw=0,zorder=0);B.fill_between(U,-np.sqrt(U),1.25,color=BLUE_FILL,lw=0,zorder=0);B.plot(U,-np.sqrt(U),color=BLUE,lw=1.5,zorder=4)
W=np.linspace(-1,2.2,50)
for lam,ls in ((.5,':'),(1.5,'--'),(5,'-')):
    q=-1/(4*lam);B.plot(W,q-lam*W,color=PURPLE,lw=1.15,ls=ls,zorder=3);dot(B,0,q,PURPLE,ms=3.8)
B.plot([0,0],[-1.8,1.25],color=STROKE,lw=1.9,zorder=5);opt(B,0,0,z=8)
B.text(-.5,.72,'不可行',fontsize=7.5,ha='center');B.text(1.3,.5,'A',color=INK)
B.text(2.1,-1.0,r'$\lambda=0.5$',fontsize=7.5,ha='right',va='bottom') if 0 else None
B.set_xlim(-1,2.2);B.set_ylim(-1.8,1.25);B.set_xticks([-1,0,1,2]);B.set_yticks([-1,0,1]);B.set_xlabel('$u$',labelpad=1)
for a_,s in zip((A,B),('(a)','(b)')):tag(fig,a_,s)
save(fig,HERE,'figure',{'a':'v(u)=max(1-u,0)^2/2, lam*=1','b':'v(u)=-sqrt(u); lam=.5,1.5,5'})
