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

# 三种没有最优解的方式：不可行、无下界、下确界未达到。
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
panel(fig, .07, .985, .955, .27, .36)
a = axes[0]
a.plot([-2.2, 0], [.28,.28], color=BLUE, lw=2.2, solid_capstyle='butt')
a.plot([1, 3.2], [.62,.62], color=BLUE, lw=2.2, solid_capstyle='butt')
a.plot([0],[.28],'o',ms=3.8,color=BLUE,mew=0); a.plot([1],[.62],'o',ms=3.8,color=BLUE,mew=0)
a.vlines([0,1],0,[.28,.62],color=MUTED,lw=.7,ls=':')
a.text(-1.1,.38,r'$x\leq 0$',ha='center',va='bottom'); a.text(2.1,.72,r'$x\geq 1$',ha='center',va='bottom')
a.set_xlim(-2.3,3.3); a.set_ylim(0,1.25); a.set_yticks([]); a.set_xticks([-2,0,1,3]); a.spines['left'].set_visible(False)
a.set_xlabel('$x$',labelpad=1)
b = axes[1]; x = np.linspace(-3,2,50)
b.plot(x,x,color=BLUE,lw=1.4)
b.annotate('',xy=(-3,-3),xytext=(-1.8,-1.8),arrowprops=dict(arrowstyle='-|>',color=BLUE,lw=1.0,mutation_scale=8,shrinkA=0,shrinkB=0))
b.set_xlim(-3.1,2.1); b.set_ylim(-3.1,2.1); b.set_xticks([-2,0,2]); b.set_yticks([-2,0,2]); b.set_xlabel('$x$',labelpad=1); b.set_ylabel('$f$',labelpad=1)
c = axes[2]; x = np.linspace(-5,1,200)
c.plot(x,np.exp(x),color=BLUE,lw=1.4)
c.axhline(0,color=PURPLE,lw=1.0,ls=(0,(4,2)))
c.text(.9,.12,r'$f^*=0$',color=PURPLE,ha='right',va='bottom')
c.set_xlim(-5,1); c.set_ylim(-.3,2.8); c.set_xticks([-4,-2,0]); c.set_yticks([0,1,2]); c.set_xlabel('$x$',labelpad=1); c.set_ylabel('$f$',labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'a':'x<=0 and x>=1','b':'f(x)=x','c':'f(x)=exp(x)'})
