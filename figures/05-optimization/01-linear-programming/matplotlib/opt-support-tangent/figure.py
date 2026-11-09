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

# 切线：凸函数处处在切线之上；非凸函数的切线不是全局下界。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .095, .985, .955, .25, .25)
a=axes[0]; f=lambda x:x**2/2; x=np.linspace(-2.2,2.6,300); a.plot(x,f(x),color=BLUE,lw=1.4,zorder=2)
x0=.5; a.plot(x,f(x0)+x0*(x-x0),color=PURPLE,lw=1.2,zorder=3); a.plot([x0],[f(x0)],'o',ms=4.2,color=PURPLE,mew=0,zorder=5)
a.text(x0+.03,f(x0)-.22,'$u$',ha='left',va='top')
a.set_xlim(-2.3,2.7); a.set_ylim(-1.5,3.2); a.set_xticks([-2,0,2]); a.set_yticks([-1,0,1,2,3]); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('$f$',labelpad=2)
b=axes[1]; g=lambda x:x**4/4-x**2; x=np.linspace(-2.45,2.45,400); b.plot(x,g(x),color=BLUE,lw=1.4,zorder=2)
b.plot(x,0*x,color=PURPLE,lw=1.2,zorder=3); b.plot([0],[0],'o',ms=4.2,color=PURPLE,mew=0,zorder=5)
xs=np.linspace(-2,2,300); b.fill_between(xs,g(xs),0,facecolor=RED_FILL,edgecolor='none',zorder=0)
b.text(.05,.12,'$u$',ha='left',va='bottom')
b.set_xlim(-2.5,2.5); b.set_ylim(-1.5,1.5); b.set_xticks([-2,0,2]); b.set_yticks([-1,0,1]); b.set_xlabel('$x$',labelpad=1); b.set_ylabel('$g$',labelpad=2)
tags(fig, axes)
save(fig, HERE, 'figure', {'a':'x^2/2 tangent at .5','b':'x^4/4-x^2 tangent at 0'})
