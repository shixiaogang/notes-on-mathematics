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

# 弦与图像的间隔：|x| 上为零，x^4 很小，x^2 按距离平方。
fig, axes = figure(width_mm=112, height_mm=46, ncols=3, sharey=True)
panel(fig, .095, .985, .955, .26, .13)
fs=[lambda x:np.abs(x),lambda x:x**4,lambda x:x**2]
ends=[(.25,1.0),(-.5,.5),(-.5,.5)]
for ax,f,(u,v) in zip(axes,fs,ends):
    x=np.linspace(-1.05,1.05,400); ax.plot(x,f(x),color=BLUE,lw=1.4,zorder=2)
    xs=np.linspace(u,v,200); ch=f(u)+(f(v)-f(u))/(v-u)*(xs-u)
    ax.fill_between(xs,f(xs),ch,facecolor=GREEN_FILL,edgecolor='none',zorder=0)
    ax.plot([u,v],[f(u),f(v)],color=GREEN,lw=1.2,zorder=3); ax.plot([u,v],[f(u),f(v)],'o',ms=3.5,color=GREEN,mew=0,zorder=4)
    ax.set_xlim(-1.08,1.08); ax.set_ylim(-.06,1.12); ax.set_xticks([-1,0,1]); ax.set_yticks([0,.5,1]); ax.set_yticklabels(['0','0.5','1']); ax.set_xlabel('$x$',labelpad=1)
axes[0].set_ylabel('$f$',labelpad=2)
tags(fig, axes)
save(fig, HERE, 'figure', {'a':'|x| chord .25..1','b':'x^4 chord -.5...5','c':'x^2 chord -.5...5'})
