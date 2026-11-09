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
# f=max{-x,x/2,2x-3}，mu=1，梯度下降 alpha=mu/4，从原最优点 x=0 出发。
a=np.array([-1,.5,2.]);b=np.array([0,0,-3.]);m=3;mu=1.
f=lambda x:np.maximum.reduce([-x,x/2,2*x-3])
def fm(x):
    l=np.outer(np.atleast_1d(x),a)+b;return mu*np.logaddexp.reduce(l/mu,axis=1)-mu*np.log(m)
def dm(x):
    l=a*x+b;w=np.exp((l-l.max())/mu);w/=w.sum();return float(a@w)
x=0.;P=[x]
for t in range(60): x=x-mu/4*dm(x);P.append(x)
P=np.array(P);print(P[:3],f(P[:3]),fm(P[:3]),'lim',P[-1],f(P[-1]),fm(P[-1]),dm(0.))
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.08,.97,.98,.26,wspace=.26)
X=np.linspace(-2,4,801);A.plot(X,f(X),color=BLUE,lw=1.4);A.plot(X,fm(X),color=GREEN,lw=1.3);opt(A,0,0)
A.plot([P[-1]],[fm(P[-1])[0]],'o',color=GREEN,ms=4.4,mew=0,zorder=6)
A.set_xlim(-2,4);A.set_ylim(-1.3,5);A.set_xticks([-2,0,2,4]);A.set_yticks([0,2,4]);A.set_xlabel('$x$',labelpad=1)
A.text(3.15,4.3,'$f$',color=INK);A.text(2.9,1.1,'$f_\\mu$',color=INK)
tt=np.arange(61);B.plot(tt,f(P),color=BLUE,lw=1.4);B.plot(tt,fm(P),color=GREEN,lw=1.4)
B.set_xlim(0,60);B.set_xlabel('$t$',labelpad=1);B.set_xticks([0,20,40,60]);B.set_yticks([-.4,-.2,0,.2],['$-0.4$','$-0.2$','$0$','$0.2$']);B.set_ylim(-.5,.3)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'mu':mu,'alpha':mu/4,'x_lim':float(P[-1])})
