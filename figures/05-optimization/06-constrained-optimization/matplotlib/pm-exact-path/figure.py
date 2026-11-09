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

fig,(a,b)=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.08,.99,.97,.29,wspace=.24)
R=np.linspace(.02,8,800)
a.plot(R,12*R/(3+4*R),color=YELLOW,lw=1.8)
a.plot(R,np.minimum(R,3),color=GREEN,lw=1.4)
a.axhline(3,color=RED,lw=.85,ls=':')
a.set_xlim(0,8);a.set_ylim(0,3.5);a.set_xticks([0,3,6]);a.set_yticks([0,1,2,3]);a.set_xlabel('$\\rho$',labelpad=1);a.set_ylabel('$x_1(\\rho)$',labelpad=1)
a.text(3.5,2.05,'二次罚',color=YELLOW);a.text(.72,2.55,'一次罚',color=GREEN)
b.plot(R,12/(3+4*R),color=YELLOW,lw=1.8)
b.plot(R,np.maximum(4-4/3*R,0),color=GREEN,lw=1.4)
b.axvline(3,color=MUTED,lw=.85,ls=':')
b.set_xlim(0,8);b.set_ylim(0,4.3);b.set_xticks([0,3,6]);b.set_yticks([0,2,4]);b.set_xlabel('$\\rho$',labelpad=1);b.set_ylabel('$|h(\\mathbf{x}(\\rho))|$',labelpad=1)
b.text(3.2,3.5,'$\\rho=|\\nu^*|=3$',color=MUTED,fontsize=7.5)
b.text(4.6,.62,'二次罚',color=YELLOW);b.text(1.45,2.75,'一次罚',color=GREEN)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'quadratic':'x1=12rho/(3+4rho)','exact':'x1=min(rho,3)'})
