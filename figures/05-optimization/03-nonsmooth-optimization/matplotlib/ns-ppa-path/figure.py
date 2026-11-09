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
# f=(x1^2+9x2^2)/2，x0=(9,1)；邻近点法 alpha=1 与 alpha=4，对照梯度下降 alpha=1/9。
H=np.array([1.,9.]);X0=np.array([9.,1.])
def ppa(a,T):
    P=[X0.copy()]
    for t in range(T): P.append(P[-1]/(1+a*H))
    return np.array(P)
def gd(a,T):
    P=[X0.copy()]
    for t in range(T): P.append(P[-1]-a*H*P[-1])
    return np.array(P)
fv=lambda P:.5*(H*P**2).sum(1)
fig,(A,B)=figure(width_mm=112,height_mm=48,ncols=2,gridspec_kw={'width_ratios':[1.5,1]})
panel(fig,.08,.97,.98,.26,wspace=.2)
X,Y=np.meshgrid(np.linspace(-1,10,600),np.linspace(-1.2,1.2,400))
A.contour(X,Y,.5*(X**2+9*Y**2),levels=[1,5,15,30,45],colors=[BLUE],linewidths=.65)
p=gd(1/5,10);A.plot(p[:,0],p[:,1],'-o',color=YELLOW,lw=1.2,ms=3,mew=0,zorder=4)
p=ppa(1,8);A.plot(p[:,0],p[:,1],'-o',color=GREEN,lw=1.2,ms=3.2,mew=0,zorder=5);opt(A)
A.set_xlim(-1,10);A.set_ylim(-1.2,1.2);A.set_xticks([0,3,6,9]);A.set_yticks([-1,0,1]);A.set_xlabel('$x_1$',labelpad=1);A.set_ylabel('$x_2$',labelpad=0)
tt=np.arange(0,16)
B.semilogy(tt,fv(gd(1/5,15)),'-',color=YELLOW,lw=1.3)
B.semilogy(tt,fv(ppa(1,15)),'-',color=GREEN,lw=1.4);B.semilogy(tt,fv(ppa(4,15)),'--',color=GREEN,lw=1.4)
B.set_xlim(0,15);B.set_ylim(1e-16,100);B.set_yticks([1e-14,1e-9,1e-4,1e1]);B.set_xticks([0,5,10,15]);B.set_xlabel('$t$',labelpad=1)
B.text(9,6,'梯度步',color=INK,fontsize=7.5);B.text(9.5,.01,'$\\alpha=1$',color=INK,fontsize=7.5);B.text(1.3,1e-13,'$\\alpha=4$',color=INK,fontsize=7.5)
fig.canvas.draw()
tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'f':'(x1^2+9x2^2)/2','x0':[9,1]})
