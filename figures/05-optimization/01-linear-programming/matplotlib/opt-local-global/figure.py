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

# f(x)=x^4/4-x^3/3-x^2 在 C=[-1.5,1.5] 上。
f = lambda x: x**4/4-x**3/3-x**2
fig, ax = figure(width_mm=98, height_mm=56)
ax.axvspan(-1.5,1.5,facecolor=BLUE_FILL,edgecolor='none',zorder=0)
x = np.linspace(-1.5,1.5,400); ax.plot(x,f(x),color=BLUE,lw=1.4,zorder=2)
x = np.linspace(1.5,2.35,100); ax.plot(x,f(x),color=BLUE,lw=1.0,ls=(0,(3,2)),zorder=2)
x = np.linspace(-1.72,-1.5,50); ax.plot(x,f(x),color=BLUE,lw=1.0,ls=(0,(3,2)),zorder=2)
ax.plot([-1],[f(-1)],'o',ms=4.6,color=YELLOW,mew=0,zorder=4)
ax.plot([0],[0],'o',ms=4.4,mfc='white',mec=BLUE,mew=1,zorder=4)
ax.plot([1.5],[f(1.5)],'o',ms=5,color=RED,mew=0,zorder=4)
ax.plot([2],[f(2)],'o',ms=4.4,mfc='white',mec=MUTED,mew=1,zorder=4)
xt=np.array([1.2,1.8]); s=1.5**3-1.5**2-3; ax.plot(xt,f(1.5)+s*(xt-1.5),color=STROKE,lw=.9,zorder=3)
ax.text(-1,f(-1)-.2,'局部最优',ha='center',va='top')
ax.text(.03,.13,'局部极大',ha='center',va='bottom')
ax.text(1.42,f(1.5)-.18,'全局最优',ha='right',va='top')
ax.text(2.02,f(2)-.14,'可行域外',ha='center',va='top',color=MUTED)
ax.axhline(0,color=GRID,lw=.0)
ax.set_xlim(-1.8,2.5); ax.set_ylim(-3.3,1.2); ax.set_xticks([-1.5,-1,0,1,1.5,2]); ax.set_xticklabels(['$-1.5$','$-1$','0','1','1.5','2']); ax.set_yticks([-3,-2,-1,0,1])
ax.set_xlabel('$x$',labelpad=1); ax.set_ylabel('$f(x)$',labelpad=2)
save(fig, HERE, 'figure', {'f':'x^4/4-x^3/3-x^2','C':[-1.5,1.5]})
