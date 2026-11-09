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
# F(x)=(x-3)^2/2+3.5 log(1+|x|)，MM：x^+=soft(3,3.5/(1+|x|))。
F=lambda x:.5*(x-3)**2+3.5*np.log(1+abs(x))
S=lambda z,t:np.sign(z)*max(abs(z)-t,0)
def run(x0,T=14):
    P=[x0]
    for t in range(T): P.append(S(3.,3.5/(1+abs(P[-1]))))
    return np.array(P)
Q=lambda x,c:.5*(x-3)**2+3.5*(np.log(1+abs(c))+(abs(x)-abs(c))/(1+abs(c)))
P1=run(1.);P2=run(.2);print(P1[:5],F(P1[:5]),P2[:5],F(P2[:5]),P1[-1])
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.07,.97,.98,.26,wspace=.24)
X=np.linspace(-.8,3.5,1001);A.plot(X,F(X),color=BLUE,lw=1.4);A.plot(X,Q(X,1.),color=GREEN,lw=1.2,ls='--');A.plot([1],[F(1.)],'o',color=GREEN,ms=4,mew=0,zorder=6);A.plot([P1[1]],[Q(P1[1],1.)],'o',color=GREEN,ms=4,mew=0,zorder=6)
xm=1+.5**.5;opt(A,xm,float(F(xm)));A.plot([0],[F(0.)],'o',color=PURPLE,ms=4.4,mew=0,zorder=6)
A.set_xlim(-.8,3.5);A.set_ylim(3.6,8);A.set_xticks([0,1,2,3]);A.set_yticks([4,6,8]);A.set_xlabel('$x$',labelpad=1)
tt=np.arange(15);B.plot(tt,P1,'-o',color=GREEN,lw=1.3,ms=3,mew=0);B.plot(tt,P2,'-o',color=YELLOW,lw=1.3,ms=3,mew=0)
B.axhline(xm,color=RED,lw=.85,ls=':');B.axhline(0,color=PURPLE,lw=.85,ls=':')
B.set_xlim(0,14);B.set_xticks([0,4,8,12]);B.set_yticks([0,1,1.707],['$0$','$1$','$1.71$']);B.set_ylim(-.15,2);B.set_xlabel('$t$',labelpad=1);B.set_ylabel('$x^{(t)}$',labelpad=1)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'x_from_1':P1.tolist(),'x_from_02':P2.tolist()})
