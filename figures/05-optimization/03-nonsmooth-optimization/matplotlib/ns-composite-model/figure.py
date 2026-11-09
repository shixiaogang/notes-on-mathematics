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
# F(x)=(x-2)^2/2+0.5|x|，L=1，当前点 x=-1。(a) alpha=0.5；(b) alpha=2.5。
f=lambda x:.5*(x-2)**2;r=lambda x:.5*abs(x);F=lambda x:f(x)+r(x)
xc=-1.;g=xc-2
def S(z,t):return np.sign(z)*max(abs(z)-t,0)
fig,(A,B)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.08,.97,.98,.26,wspace=.2)
X=np.linspace(-2.5,7,901)
for ax,a in ((A,.5),(B,2.5)):
    M=f(xc)+g*(X-xc)+(X-xc)**2/(2*a)+r(X)
    p=S(xc-a*g,a*.5)
    ax.plot(X,F(X),color=BLUE,lw=1.4);ax.plot(X,M,color=GREEN,lw=1.3,ls='--')
    ax.plot([xc],[F(xc)],'o',color=GREEN,ms=4.2,mew=0,zorder=6)
    Mp=f(xc)+g*(p-xc)+(p-xc)**2/(2*a)+r(p);ax.plot([p],[Mp],'o',color=GREEN,ms=4.2,mew=0,zorder=6)
    ax.plot([p,p],[Mp,F(p)],color=MUTED,lw=.85,ls=':');ax.plot([p],[F(p)],'o',color=BLUE,ms=4,mew=0,zorder=6)
    ax.set_xlabel('$x$',labelpad=1);ax.set_xlim(-2.5,7);ax.set_ylim(-3,9);ax.set_xticks([-2,0,2,4,6]);ax.set_yticks([0,4,8])
A.text(5.1,3.9,'$F$',color=INK);A.text(1.0,6.6,'模型',color=INK,fontsize=7.5)
A.text(-.85,5.5,'$x^{(t)}$',color=INK);A.text(.45,.3,'$x^{(t+1)}$',color=INK)
B.text(5.9,6.1,'$F$',color=INK);B.text(.2,-2.3,'模型',color=INK,fontsize=7.5);B.text(-.85,5.5,'$x^{(t)}$',color=INK);B.text(3.4,8.3,'$x^{(t+1)}$',color=INK)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'F':'(x-2)^2/2+0.5|x|','x':-1,'alphas':[.5,2.5]})
