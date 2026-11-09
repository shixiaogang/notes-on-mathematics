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
# (a) f=max{-x,x/2,2x-3} 的 Moreau 包络 mu=1；(b) (x-1/2)^2/2+|x| 与只平滑 |x| 的替代 mu=1。
f=lambda x:np.maximum.reduce([-x,x/2,2*x-3])
def prox(x,a=1.):
    if x<-a: return x+a
    if x<=a/2: return 0.
    if x<2+a/2: return x-a/2
    if x<=2+2*a: return 2.
    return x-2*a
X=np.linspace(-3,5,1001)
M=np.array([f(np.array(prox(x)))+(prox(x)-x)**2/2 for x in X])
h=lambda x,m:np.where(abs(x)<=m,x*x/(2*m),abs(x)-m/2)
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.07,.99,.98,.26,wspace=.2)
A.plot(X,f(X),color=BLUE,lw=1.4);A.plot(X,M,color=GREEN,lw=1.4);opt(A)
A.set_xlim(-3,5);A.set_ylim(-.4,7);A.set_xticks([-2,0,2,4]);A.set_yticks([0,2,4,6]);A.set_xlabel('$x$',labelpad=1)
A.text(3.1,5.5,'$f$',color=INK);A.text(4,3.5,'$M_{\\mu f}$',color=INK)
Y=np.linspace(-1,1.5,1001);F=.5*(Y-.5)**2+abs(Y);Fs=.5*(Y-.5)**2+h(Y,1.)
B.plot(Y,F,color=BLUE,lw=1.4);B.plot(Y,Fs,color=GREEN,lw=1.4);opt(B,0,.125)
B.plot([.25],[.5*(.25-.5)**2+.03125],'o',color=GREEN,ms=4.2,mew=0,zorder=6)
B.plot([.25,.25],[.0,.5*(.25-.5)**2+.03125],color=MUTED,lw=.85,ls=':')
B.set_xlim(-1,1.5);B.set_ylim(0,1.9);B.set_xticks([-1,0,.25,1],['$-1$','$0$','$\\frac{1}{4}$','$1$']);B.set_yticks([0,.5,1,1.5],['$0$','$0.5$','$1$','$1.5$']);B.set_xlabel('$x$',labelpad=1)
B.text(.95,1.35,'$F$',color=INK);B.text(1.15,.72,'$f+h_\\mu$',color=INK)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'mu':1})
