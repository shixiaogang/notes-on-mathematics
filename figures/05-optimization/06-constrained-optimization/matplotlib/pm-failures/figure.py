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
panel(fig,.08,.99,.97,.27,wspace=.2)
X=np.linspace(-6,1.2,801)
a.axvspan(0,1.2,color=BLUE_FILL,lw=0,zorder=0);a.axvline(0,color=STROKE,lw=1.7)
for r in (2,6):
    a.plot(X,X**3+r/2*np.maximum(-X,0)**2,color=BLUE,lw=1.4)
a.plot(X[X>=-1.9],(X**3)[X>=-1.9],color=BLUE,lw=.9,ls='--')
opt(a,0,0);a.set_xlim(-6,1.2);a.set_ylim(-14,10);a.set_xticks([-6,-4,-2,0]);a.set_yticks([-10,0,10]);a.set_xlabel('$x$',labelpad=1)
a.text(-5.6,-3.6,'$\\rho=2$',color=INK);a.text(-4.5,8,'$\\rho=6$',color=INK);a.text(-1.65,-11.5,'$f$',color=MUTED)
X=np.linspace(-2.6,2,801);h=X**3-3*X+3
b.axhline(0,color=STROKE,lw=.85)
b.plot(X,h,color=PURPLE,lw=1.1,ls='--')
def bis(fn,lo,hi):
    flo=fn(lo)
    for _ in range(200):
        m=(lo+hi)/2;fm=fn(m)
        if flo*fm<=0: hi=m
        else: lo,flo=m,fm
    return (lo+hi)/2
r=3.
Q=.5*X**2+r/2*h**2
b.plot(X,Q,color=BLUE,lw=1.4)
hr=lambda x:x**3-3*x+3
g=lambda x:x+r*hr(x)*(3*x**2-3)
xloc=bis(g,.5,1.)
xstar=bis(hr,-3,0)
it(b,xloc,.5*xloc**2+r/2*hr(xloc)**2);b.plot([xloc,xloc],[0,.5*xloc**2+r/2*hr(xloc)**2],color=MUTED,lw=.85,ls=':')
opt(b,xstar,0)
b.set_xlim(-2.6,2);b.set_ylim(-3,12);b.set_xticks([-2,-1,0,1,2]);b.set_yticks([0,5,10]);b.set_xlabel('$x$',labelpad=1)
b.text(1.42,10.4,'$Q_3$',color=INK);b.text(-.5,2.6,'$h$',color=PURPLE);b.text(xstar+.12,-2.,'$x^*$',color=INK)
fig.canvas.draw();tag(fig,a,'(a)');tag(fig,b,'(b)')
save(fig,HERE,'figure',{'a':'x^3+rho/2*max(-x,0)^2','b':'x^2/2+3/2*(x^3-3x+3)^2','local_min':float(xloc),'root':float(xstar)})
