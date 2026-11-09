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
# 显式与隐式：(a) f=|x|, x0=1, alpha=0.4；(b) f=4.5 x^2, x0=1, alpha=0.4。
fig,(A,B)=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.10,.97,.98,.26,wspace=.33)
T=12
x=1.;F=[x]
for t in range(T): x=x-.4*np.sign(x);F.append(x)
x=1.;P=[x]
for t in range(T): x=np.sign(x)*max(abs(x)-.4,0);P.append(x)
tt=np.arange(T+1)
A.axhline(0,color=MUTED,lw=.7,ls=':');A.plot(tt,F,'-o',color=YELLOW,lw=1.3,ms=3,mew=0);A.plot(tt,P,'-o',color=GREEN,lw=1.3,ms=3,mew=0)
A.set_xticks([0,4,8,12]);A.set_yticks([-.5,0,.5,1],['$-0.5$','$0$','$0.5$','$1$']);A.set_xlim(0,12);A.set_ylim(-.5,1.1);A.set_xlabel('$t$',labelpad=1);A.set_ylabel('$x^{(t)}$',labelpad=0)

c=9;a=.4;tt=np.arange(0,13)
B.semilogy(tt,np.abs(1-a*c)**tt,'-o',color=YELLOW,lw=1.3,ms=3,mew=0);B.semilogy(tt,(1/(1+a*c))**tt,'-o',color=GREEN,lw=1.3,ms=3,mew=0)
B.set_xticks([0,4,8,12]);B.set_xlim(0,12);B.set_xlabel('$t$',labelpad=1);B.set_ylabel('$|x^{(t)}|$',labelpad=3)
B.text(6.2,12,'梯度步',color=INK,fontsize=7.5);B.text(6.5,.0065,'邻近步',color=INK,fontsize=7.5)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'a':'|x|','b':'4.5x^2','alpha':.4,'forward_a':F,'backward_a':P})
