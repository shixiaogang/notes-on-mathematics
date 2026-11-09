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
# |x| 的三种光滑替代，mu=1/2：Huber、上方 lse、下方归一化 lse。
m=.5;X=np.linspace(-2.5,2.5,1501)
h=np.where(abs(X)<=m,X*X/(2*m),abs(X)-m/2)
up=m*np.logaddexp(X/m,-X/m);lo=up-m*np.log(2)
fig,(A,B)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.07,.97,.98,.26,wspace=.22)
A.plot(X,abs(X),color=BLUE,lw=1.4);A.plot(X,h,color=GREEN,lw=1.3);A.plot(X,up,color=YELLOW,lw=1.3);A.plot(X,lo,color=PURPLE,lw=1.3,ls='--')
A.set_xlim(-1.6,1.6);A.set_ylim(-.1,1.7);A.set_xticks([-1,0,1]);A.set_yticks([0,.5,1,1.5],['$0$','$0.5$','$1$','$1.5$']);A.set_xlabel('$x$',labelpad=1)
B.axhline(0,color=MUTED,lw=.7,ls=':')
B.plot(X,h-abs(X),color=GREEN,lw=1.3);B.plot(X,up-abs(X),color=YELLOW,lw=1.3);B.plot(X,lo-abs(X),color=PURPLE,lw=1.3,ls='--')
B.axhline(-m/2,color=GREEN,lw=.7,ls=':');B.axhline(m*np.log(2),color=YELLOW,lw=.8,ls=':');B.axhline(-m*np.log(2),color=PURPLE,lw=.7,ls=':')
B.set_xlim(-2.5,2.5);B.set_ylim(-.45,.45);B.set_xticks([-2,0,2]);B.set_yticks([-.3466,-.25,0,.3466],['$-\\frac{\\ln 2}{2}$','$-\\frac{1}{4}$','$0$','$\\frac{\\ln 2}{2}$']);B.set_xlabel('$x$',labelpad=1)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'mu':m})
