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

fig,ax=figure(width_mm=100,height_mm=56)
panel(fig,.08,.98,.98,.15)
q=lambda n:-(2/3)*n**2-4*n
N=np.linspace(-7.2,1.2,601)
ax.plot(N,q(N),color=PURPLE,lw=1.4)
# explicit from 0 with alpha=rho=1.5: slope -4 ; implicit lands at -2 where slope is -4/3
s0=-4.;t=np.array([-1.5,.9]);ax.plot(t,s0*t,color=YELLOW,lw=1.2,ls='--')
s1=-(4/3)*(-2)-4;t=np.array([-3.3,-.7]);ax.plot(t,q(-2.)+s1*(t+2),color=GREEN,lw=1.2,ls='--')
it(ax,0,0,c=INK,ms=4.2);it(ax,-6,q(-6.),c=YELLOW,ms=5);it(ax,-2,q(-2.),ms=5);opt(ax,-3,6)
ax.annotate('',xy=(-6,-.9),xytext=(0,-.9),arrowprops=dict(arrowstyle='-|>',mutation_scale=8,color=YELLOW,lw=1.3,shrinkA=0,shrinkB=0))
ax.annotate('',xy=(-2,-2.2),xytext=(0,-2.2),arrowprops=dict(arrowstyle='-|>',mutation_scale=8,color=GREEN,lw=1.3,shrinkA=0,shrinkB=0))
ax.text(-3.0,-.65,'显式步',color=YELLOW,ha='center');ax.text(-1.0,-3.45,'隐式步',color=GREEN,ha='center')
ax.text(.15,.45,'$\\nu^{(0)}$',color=INK);ax.text(-1.8,5.05,'$\\nu^{(1)}$',color=INK);ax.text(-6.75,.55,'$-6$',color=INK);ax.text(-3,4.9,'$\\nu^*$',color=INK,ha='center')
ax.set_xlim(-7.2,1.2);ax.set_ylim(-5,7.5);ax.set_xticks([-6,-3,-2,0]);ax.set_yticks([0,3,6]);ax.set_xlabel('$\\nu$',labelpad=1);ax.set_ylabel('$q(\\nu)$',labelpad=1)
save(fig,HERE,'figure',{'q':'-(2/3)nu^2-4nu','rho':1.5,'explicit':-6,'implicit':-2})
