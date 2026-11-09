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
panel(fig,.09,.98,.97,.27,wspace=.26)
g=np.linspace(-2.5,1.5,801);r=2.
for lam,ls in ((0,'-'),(1,'-'),(2,'-')):
    a.plot(g,(np.maximum(lam+r*g,0)**2-lam**2)/(2*r),color=BLUE,lw=1.4)
    if lam>0:
        g0=-lam/r;it(a,g0,-lam**2/(2*r),ms=4)
a.axvline(0,color=STROKE,lw=1.2)
a.set_xlim(-2.5,1.5);a.set_ylim(-1.3,3.5);a.set_xticks([-2,-1,0,1]);a.set_yticks([-1,0,1,2,3]);a.set_xlabel('$g$',labelpad=1)
a.text(.95,.42,'$\\lambda=0$',color=INK);a.text(.72,3.02,'$\\lambda=2$',color=INK,ha='right');a.text(1.12,1.72,'$\\lambda=1$',color=INK,ha='left')
lam=1.
b.plot(g,lam+r*g,color=YELLOW,lw=1.8,ls='--')
b.plot(g,np.maximum(lam+r*g,0),color=GREEN,lw=1.4)
b.axhline(0,color=PURPLE,lw=.85)
b.set_xlim(-2.5,1.5);b.set_ylim(-3,4);b.set_xticks([-2,-1,-.5,0,1]);b.set_xticklabels(['$-2$','$-1$','$-\\lambda/\\rho$','$0$','$1$'],fontsize=7.5);b.set_yticks([-2,0,1,2,4]);b.set_xlabel('$g$',labelpad=1)
b.axvline(-.5,color=MUTED,lw=.85,ls=':')
b.text(-.95,-2.2,'无投影',color=YELLOW);b.text(-2.3,.28,'$[\\lambda+\\rho g]_+$',color=GREEN)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'rho':2,'psi':'([lam+rho g]_+^2-lam^2)/(2rho)'})
