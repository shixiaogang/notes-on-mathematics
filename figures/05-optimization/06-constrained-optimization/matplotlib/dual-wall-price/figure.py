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

# 硬约束的无穷墙与线性价格；一元例 f=(x-2)^2/2, g=x-1, L=f+lam*g.
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.07,.985,.97,.25,wspace=.24)
U=np.linspace(-2,2,5)
A.plot([-2,0],[0,0],color=STROKE,lw=2.0,solid_capstyle='butt'); A.plot([0,0],[0,3],color=STROKE,lw=2.0,solid_capstyle='butt')
for lam,ls in ((.5,':'),(1,'--'),(2,'-')):
    A.plot(U,lam*U,color=PURPLE,lw=1.3,ls=ls); A.text(2.04 if lam<2 else 1.5,lam*2 if lam<2 else 3.0,fr'$\lambda={lam:g}$',ha='left' if lam<2 else 'right',va='center',color=INK,fontsize=7.5)
A.text(-1.9,.22,r'$\iota_{\leq0}(u)$',color=INK)
A.axhline(0,color=MUTED,lw=.5,zorder=0)
A.set_xlim(-2,2.95);A.set_ylim(-3.2,3.4);A.set_xticks([-2,0,2]);A.set_yticks([-2,0,2]);A.set_xlabel('$u$',labelpad=1)
X=np.linspace(-.6,3.6,400); f=.5*(X-2)**2
B.axvspan(-.6,1,color=BLUE_FILL,lw=0,zorder=0); B.plot([1,1],[-.9,3.5],color=STROKE,lw=1.5,zorder=2)
B.plot(X,f,color=BLUE,lw=1.5,zorder=4)
for lam,ls in ((.5,':'),(1,'--'),(2,'-')):
    B.plot(X,f+lam*(X-1),color=PURPLE,lw=1.3,ls=ls,zorder=3); x0=2-lam; dot(B,x0,.5*(x0-2)**2+lam*(x0-1),PURPLE,ms=4.0)
opt(B,1,.5)
B.text(3.0,.62,'$f$',color=INK); B.text(.05,.2,'$x\\leq1$',color=INK)
B.text(2.28,3.1,r'$\lambda=2$',color=INK,fontsize=7.5,ha='right')
B.set_xlim(-.6,3.6);B.set_ylim(-.9,3.5);B.set_xticks([0,1,2,3]);B.set_yticks([0,1,2,3]);B.set_xlabel('$x$',labelpad=1)
for a,s in zip((A,B),('(a)','(b)')):tag(fig,a,s)
save(fig,HERE,'figure',{'f':'(x-2)^2/2','g':'x-1','lambda':[.5,1,2]})
