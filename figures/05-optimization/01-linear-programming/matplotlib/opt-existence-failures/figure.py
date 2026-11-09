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

# 存在性论证三个环节的失效。
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, .07, .985, .955, .26, .36)
a=axes[0]; x=np.linspace(0,1,50); a.plot(x,x,color=BLUE,lw=1.4)
s=2.0**-np.arange(0,6); a.plot(s,s,'o',ms=3.8,color=GREEN,mew=0,zorder=4)
a.plot([0],[0],'o',ms=4.4,mfc='white',mec=RED,mew=1,zorder=5)
a.set_xlim(-.06,1.08); a.set_ylim(-.08,1.12); a.set_xticks([0,1]); a.set_yticks([0,1]); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('$f$',labelpad=1)
b=axes[1]; x=np.linspace(1,20,300); b.plot(x,1/x,color=BLUE,lw=1.4)
s=2.0**np.arange(0,5); b.plot(s,1/s,'o',ms=3.8,color=GREEN,mew=0,zorder=4)
b.axhline(0,color=PURPLE,lw=1.0,ls=(0,(4,2)))
b.annotate('',xy=(20,.17),xytext=(16.8,.17),arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=.9,mutation_scale=7,shrinkA=0,shrinkB=0))
b.set_xlim(0,20.5); b.set_ylim(-.08,1.12); b.set_xticks([1,8,16]); b.set_yticks([0,1]); b.set_xlabel('$x$',labelpad=1); b.set_ylabel('$f$',labelpad=1)
c=axes[2]; x=np.linspace(-1,1,300); c.plot(x,x**2,color=BLUE,lw=1.4)
s=1/np.arange(1,7); c.plot(s,s**2,'o',ms=3.8,color=GREEN,mew=0,zorder=4)
c.plot([0],[0],'o',ms=4.4,mfc='white',mec=RED,mew=1,zorder=5)
c.plot([0],[.6],'o',ms=4.6,color=RED,mew=0,zorder=5)
c.set_xlim(-1.08,1.08); c.set_ylim(-.08,1.12); c.set_xticks([-1,0,1]); c.set_yticks([0,.6,1]); c.set_yticklabels(['0','0.6','1']); c.set_xlabel('$x$',labelpad=1); c.set_ylabel('$f$',labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'a':'f=x on (0,1], x_k=2^-k','b':'f=1/x on [1,inf), x_k=2^k','c':'f=x^2, f(0)=0.6, x_k=1/k'})
