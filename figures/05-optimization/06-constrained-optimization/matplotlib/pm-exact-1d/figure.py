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
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def opt(ax, x, y, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
def it(ax, x, y, ms=4.2, z=6, c=GREEN): ax.plot([x],[y],'o',ms=ms,color=c,mew=0,zorder=z)
def bare(ax): ax.set_aspect('equal'); 
# Running example: f(x)=x1^2/2+3x2^2/2, h(x)=x1+x2-4, x*=(3,1), nu*=-3.
G = np.diag([1.,3.]); A1 = np.ones(2)
def fq(X,Y): return .5*X**2+1.5*Y**2
def line(ax,lo=-2,hi=7):
    t=np.array([lo,hi]); ax.plot(t,4-t,color=STROKE,lw=1.7,solid_capstyle='butt',zorder=3)

fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2)
panel(fig,.08,.99,.97,.27,wspace=.22)
X=np.linspace(-1.5,2.2,801)
a.axvspan(1,2.2,color=BLUE_FILL,lw=0);a.axvline(1,color=STROKE,lw=1.7)
for r in (.5,1,2):
    a.plot(X,X+r*np.maximum(1-X,0),color=BLUE,lw=1.4)
opt(a,1,1);a.set_xlim(-1.5,2.2);a.set_ylim(-.9,3.4);a.set_xticks([-1,0,1,2]);a.set_yticks([0,1,2,3]);a.set_xlabel('$x$',labelpad=1)
a.text(-1.38,.15,'$\\rho=0.5$',color=INK);a.text(-.72,1.1,'$\\rho=1$',color=INK);a.text(-.62,2.75,'$\\rho=2$',color=INK)
r=2.
b.axvspan(1,2.2,color=BLUE_FILL,lw=0);b.axvline(1,color=STROKE,lw=1.7)
E=X+r*np.maximum(1-X,0)
b.plot(X,E,color=BLUE,lw=1.4)
b.axhline(1,color=PURPLE,lw=1.3,ls='--')
xv=-.2;b.annotate('',xy=(xv,1),xytext=(xv,xv+r*(1-xv)),arrowprops=dict(arrowstyle='<->',color=RED,lw=.9,shrinkA=0,shrinkB=0))
b.text(xv+.08,1.75,'$(\\rho-\\lambda^*)[1-x]_+$',color=RED,fontsize=7.5)
opt(b,1,1);b.set_xlim(-1.5,2.2);b.set_ylim(-.9,3.4);b.set_xticks([-1,0,1,2]);b.set_yticks([0,1,2,3]);b.set_xlabel('$x$',labelpad=1)
b.text(-1.4,.62,'$\\mathcal{L}(x,\\lambda^*)=1$',color=PURPLE);b.text(-.95,3.1,'$E_2$',color=INK)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'E':'x+rho*max(1-x,0)','lambda_star':1})
