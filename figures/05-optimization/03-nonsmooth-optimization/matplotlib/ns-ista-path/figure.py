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
def tag(fig, ax, s, y=None, d=.15):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
# 贯穿 Lasso：A=[[1,1],[1,0],[0,1]]，b=(3,2,-1)，lambda=1，L=3，x0=(0,0)，x*=(2,0)。
import math
A_=np.array([[1.,1],[1,0],[0,1]]);b=np.array([3.,2,-1]);lam=1.;L=3.
AtA=A_.T@A_;c=A_.T@b
S=lambda x,t:np.sign(x)*np.maximum(abs(x)-t,0)
def ista(T):
    x=np.zeros(2);P=[x.copy()]
    for t in range(T):
        x=S(x-(AtA@x-c)/L,lam/L);P.append(x.copy())
    return np.array(P)
def fista(T):
    x=np.zeros(2);y=x.copy();th=1.;P=[x.copy()]
    for t in range(T):
        xn=S(y-(AtA@y-c)/L,lam/L);thn=(1+math.sqrt(1+4*th*th))/2;y=xn+(th-1)/thn*(xn-x);x=xn;th=thn;P.append(x.copy())
    return np.array(P)
I=ista(30);Fi=fista(30)
X,Y=np.meshgrid(np.linspace(-.3,2.7,900),np.linspace(-.5,1.1,900))
Z=.5*((X+Y-3)**2+(X-2)**2+(Y+1)**2)+abs(X)+abs(Y)
fig,(a,bb)=figure(width_mm=112,height_mm=58,ncols=2,gridspec_kw={'width_ratios':[1.65,1]})
panel(fig,.07,.99,.98,.24,wspace=.2)
a.contour(X,Y,Z,levels=[3.05,3.2,3.5,4,5,6,7],colors=[BLUE],linewidths=.7)
a.plot([-.3,2.7],[0,0],color=STROKE,lw=1.4,zorder=2)
a.plot(I[:,0],I[:,1],'-o',color=GREEN,lw=1.2,ms=3.2,mew=0,zorder=5);a.plot(Fi[:,0],Fi[:,1],'-o',color=YELLOW,lw=1.2,ms=3.,mew=0,zorder=4);opt(a,2,0)
a.text(-.25,.08,'$x^{(0)}$',color=INK);a.text(1.2,.42,'$x^{(1)}$',color=INK);a.text(2.05,.1,'$x^{*}$',color=INK)
a.set_xlim(-.3,2.7);a.set_ylim(-.5,1.1);a.set_aspect('equal');a.set_xticks([0,1,2]);a.set_yticks([0,1]);a.set_xlabel('$x_1$',labelpad=1);a.set_ylabel('$x_2$',labelpad=0)
XX,YY=np.meshgrid(np.linspace(1.58,2.16,700),np.linspace(-.13,.13,700));ZZ=.5*((XX+YY-3)**2+(XX-2)**2+(YY+1)**2)+abs(XX)+abs(YY)
bb.contour(XX,YY,ZZ,levels=[3.003,3.015,3.05,3.1,3.2],colors=[BLUE],linewidths=.7)
bb.plot([1.58,2.16],[0,0],color=STROKE,lw=1.4,zorder=2)
bb.plot(I[:,0],I[:,1],'-o',color=GREEN,lw=1.2,ms=3.2,mew=0,zorder=5);bb.plot(Fi[:,0],Fi[:,1],'-o',color=YELLOW,lw=1.2,ms=3.,mew=0,zorder=4);opt(bb,2,0)
bb.set_xlim(1.58,2.16);bb.set_ylim(-.13,.13);bb.set_xticks([1.6,1.8,2,],['$1.6$','$1.8$','$2$']);bb.set_yticks([-.1,0,.1],['$-0.1$','$0$','$0.1$']);bb.set_xlabel('$x_1$',labelpad=1)
fig.canvas.draw();tag(fig,a,'(a)',y=.055);tag(fig,bb,'(b)',y=.055)
save(fig,HERE,'figure',{'ista':I[:5].tolist(),'fista':Fi[:5].tolist()})
