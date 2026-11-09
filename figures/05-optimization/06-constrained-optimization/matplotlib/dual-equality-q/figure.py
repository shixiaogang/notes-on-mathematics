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

# min (x1^2+4x2^2)/2 s.t. x1+x2=1；内层解 x(nu)=(-nu,-nu/4)，q(nu)=-5nu^2/8-nu。
fig,(A,B)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.065,.985,.975,.22,wspace=.22)
x=np.linspace(-1.3,1.7,300);y=np.linspace(-.8,1.2,300);X,Y=np.meshgrid(x,y)
A.contour(X,Y,.5*(X**2+4*Y**2),levels=[.1,.4,.9,1.6],colors=BLUE,linewidths=.8)
A.plot(x,1-x,color=STROKE,lw=1.6)
nu=np.linspace(-1.3,.9,50);A.plot(-nu,-nu/4,color=PURPLE,lw=1.3,ls='--')
for v in (.6,0,-1.2): dot(A,-v,-v/4,PURPLE,ms=3.8)
for v,dx,dy,ha in ((.6,0,-.17,'center'),(0,-.02,.07,'center'),(-1.2,.03,.08,'center')): A.text(-v+dx,-v/4+dy,fr'$\nu={v:g}$',fontsize=7.5,ha=ha)
opt(A,.8,.2); A.text(.72,-.06,r'$x^\star$',color=INK,ha='center')
A.text(-.75,.98,'$x_1+x_2=1$',color=INK,fontsize=7.5,ha='left',va='bottom') if 0 else None
A.text(.02,1.03,'$x_1+x_2=1$',color=INK,fontsize=7.5)
A.set_xlim(-1.3,1.7);A.set_ylim(-.8,1.2);A.set_xticks([-1,0,1]);A.set_yticks([-.5,0,.5,1]);A.set_xlabel('$x_1$',labelpad=1);A.set_ylabel('$x_2$',labelpad=1)
N=np.linspace(-1.9,.4,300);B.plot(N,-5/8*N**2-N,color=PURPLE,lw=1.5)
B.axhline(.4,color=BLUE,lw=.95,ls='--');B.text(.38,.43,'$f^\\star=2/5$',ha='right',fontsize=7.5)
opt(B,-.8,.4); B.text(-.8,.2,r'$\nu^\star=-4/5$',ha='center',fontsize=7.5)
B.plot([-.8,-.8],[.28,.37],color=MUTED,lw=.6)
B.set_xlim(-1.9,.4);B.set_ylim(-.65,.6);B.set_xticks([-1.5,-1,-.5,0]);B.set_yticks([-.5,0,.4]);B.set_xlabel(r'$\nu$',labelpad=1);B.text(-1.0,-.1,r'$q(\nu)$',color=INK,ha='center')
for a,s in zip((A,B),('(a)','(b)')):tag(fig,a,s)
save(fig,HERE,'figure',{'q':'-5nu^2/8-nu','nu_star':-.8,'f_star':.4})
