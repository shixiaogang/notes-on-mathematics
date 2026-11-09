from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')

# 原点处四种驻点的等值线，f<0 的区域填浅红。
fig, axes = figure(width_mm=104, height_mm=112, ncols=2, nrows=2, sharex=True, sharey=True)
fig.set_layout_engine(None); fig.subplots_adjust(left=.085,right=.985,top=.985,bottom=.125,wspace=.08,hspace=.3)
X,Y=np.meshgrid(np.linspace(-1,1,600),np.linspace(-1,1,600))
fs=[X**2+Y**2,X**2-Y**2,X**2+Y**4,X**2+Y**3]
for ax,F,tg in zip(axes.ravel(),fs,'abcd'):
    ax.contourf(X,Y,F,levels=[-5,0],colors=[RED_FILL])
    ax.contour(X,Y,F,levels=[.1,.3,.6,1.0],colors=[BLUE],linewidths=.75)
    ax.contour(X,Y,F,levels=[-.6,-.3,-.1],colors=[BLUE],linewidths=.75,linestyles=[(0,(3,2))])
    if tg in 'bd': ax.contour(X,Y,F,levels=[0],colors=[RED],linewidths=1.1)
    ax.plot([0],[0],'o',ms=4.2,color=INK,mew=0,zorder=5)
    ax.set_aspect('equal'); ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1])
    ax.tick_params(labelbottom=True)
    ax.set_xlabel('$x_1$',labelpad=0)
    p=ax.get_position(); fig.text((p.x0+p.x1)/2,p.y0-.112,f'({tg})',ha='center',va='bottom')
for ax in axes[:,0]: ax.set_ylabel('$x_2$',labelpad=1)
save(fig, HERE, 'figure', {'a':'x^2+y^2','b':'x^2-y^2','c':'x^2+y^4','d':'x^2+y^3'})
