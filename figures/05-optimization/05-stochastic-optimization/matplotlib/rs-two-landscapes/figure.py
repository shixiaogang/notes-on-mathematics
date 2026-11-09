from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# 有限状态双谷代价 f=(3,1,3,5,2,0,2) 与二维 Rastrigin 上的局部下降
fig, axes = figure(width_mm=112, height_mm=62, ncols=2)
panel(fig, .075, .985, .965, .245, .26)
a=axes[0]; s=np.arange(1,8); f=np.array([3,1,3,5,2,0,2.])
a.plot(s,f,color=BLUE,lw=1.4,marker='o',ms=3.6,mfc=BLUE,mew=0)
a.annotate('',xy=(2,1.32),xytext=(3,2.75),arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=1.3,shrinkA=0,shrinkB=0,mutation_scale=8))
a.plot([2],[1],'o',ms=5,color=GREEN,mew=0,zorder=5); a.plot([6],[0],'o',ms=5.2,color=RED,mew=0,zorder=5)
a.text(1.75,.55,'局部低谷',ha='center',va='top',fontsize=7.5,color=INK); a.text(4.55,.05,'全局最小',ha='center',va='center',fontsize=7.5)
a.set_xlim(.6,7.4); a.set_ylim(-.5,5.6); a.set_xticks(s); a.set_yticks([0,1,2,3,4,5]); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('$f(x)$',labelpad=1)
b=axes[1]; g=np.linspace(-3.4,3.4,700); X,Y=np.meshgrid(g,g); b.contour(X,Y,rastrigin(X,Y),levels=[8,24,40],colors=[BLUE],linewidths=.55)
def grad(x): return 2*x+20*np.pi*np.sin(2*np.pi*x)
ends=[]
for x0 in [(-2.3,2.6),(2.55,1.6),(1.45,-2.45),(-1.5,-1.45)]:
    x=np.array(x0,float); path=[x.copy()]
    for t in range(1500):
        x=x-.0022*grad(x); path.append(x.copy())
    p=np.array(path); b.plot(p[:,0],p[:,1],color=GREEN,lw=1.3); b.plot([x0[0]],[x0[1]],'o',ms=3.4,mfc='white',mec=GREEN,mew=.9,zorder=5); b.plot([x[0]],[x[1]],'o',ms=4,color=GREEN,mew=0,zorder=5); ends.append(x.tolist())
b.plot([0],[0],'o',ms=5.2,color=RED,mew=0,zorder=6)
b.set_aspect('equal'); b.set_xlim(-3.4,3.4); b.set_ylim(-3.4,3.4); b.set_xticks([-3,0,3]); b.set_yticks([-3,0,3]); b.set_xlabel('$x_1$',labelpad=1); b.set_ylabel('$x_2$',labelpad=0)
tags(fig,axes); print(ends)
save(fig,HERE,'figure',{'f':[3,1,3,5,2,0,2],'rastrigin':'20+sum(x_i^2-10cos(2 pi x_i))','gd_step':.0022,'iters':1500,'ends':ends})
