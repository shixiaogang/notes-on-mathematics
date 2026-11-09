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

fig,ax=figure(width_mm=88,height_mm=64)
panel(fig,.09,.98,.98,.13)
X,Y=np.meshgrid(np.linspace(-.3,4.6,700),np.linspace(-.6,3,700))
rho=4.
E=fq(X,Y)+rho*abs(X+Y-4)
ax.contour(X,Y,E,levels=[7,8.5,10.5,13,16],colors=BLUE,linewidths=.75)
line(ax)
# proximal gradient, step 1/3, closed form prox
x=np.zeros(2);P=[x];tau=rho/3
for _ in range(12):
    v=x-np.array([x[0],3*x[1]])/3
    x=v-np.clip((v.sum()-4)/2,-tau,tau)*A1;P.append(x)
P=np.array(P)
# subgradient method, step 0.12 constant
y=np.zeros(2);S=[y]
for _ in range(22):
    sg=np.array([y[0],3*y[1]])+rho*np.sign(y.sum()-4)*A1
    y=y-.07*sg;S.append(y)
S=np.array(S)
ax.plot(S[:,0],S[:,1],'-',color=YELLOW,lw=1.1,marker='o',ms=2.2,mew=0,zorder=4)
ax.plot(P[:,0],P[:,1],'-',color=GREEN,lw=1.3,marker='o',ms=3.2,mew=0,zorder=6)
opt(ax,3,1,z=8)
ax.set_xlim(-.3,4.6);ax.set_ylim(-.6,3);ax.set_aspect('equal');ax.set_xticks([0,1,2,3,4]);ax.set_yticks([0,1,2,3]);ax.set_xlabel('$x_1$',labelpad=1);ax.set_ylabel('$x_2$',labelpad=1)
save(fig,HERE,'figure',{'E':'f+4|x1+x2-4|','prox_grad':P[:4].tolist(),'subgrad_step':.07})
