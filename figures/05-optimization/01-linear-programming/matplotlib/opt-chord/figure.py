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

# 凸函数在弦下方；非凸函数的图像可以越过弦。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .095, .985, .955, .25, .25)
a=axes[0]; f=lambda x:x**2/2; x=np.linspace(-2,2.6,300); a.plot(x,f(x),color=BLUE,lw=1.4)
u,v=-1,2; a.plot([u,v],[f(u),f(v)],color=GREEN,lw=1.3)
xs=np.linspace(u,v,200); a.fill_between(xs,f(xs),f(u)+(f(v)-f(u))/(v-u)*(xs-u),facecolor=GREEN_FILL,edgecolor='none',zorder=0)
a.plot([u,v],[f(u),f(v)],'o',ms=3.8,color=GREEN,mew=0,zorder=4)
a.text(u-.05,f(u)+.2,'$u$',ha='right'); a.text(v+.08,f(v)-.05,'$v$',ha='left',va='top')
a.set_xlim(-2.1,2.7); a.set_ylim(-.3,3.4); a.set_xticks([-2,-1,0,1,2]); a.set_yticks([0,1,2,3]); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('$f$',labelpad=2)
b=axes[1]; g=lambda x:x**4/4-x**2; x=np.linspace(-2.3,2.3,400); b.plot(x,g(x),color=BLUE,lw=1.4)
u,v=-1.6,1; b.plot([u,v],[g(u),g(v)],color=RED,lw=1.3)
xs=np.linspace(u,v,300); ch=g(u)+(g(v)-g(u))/(v-u)*(xs-u)
b.fill_between(xs,ch,g(xs),where=g(xs)>ch,facecolor=RED_FILL,edgecolor='none',zorder=0)
b.plot([u,v],[g(u),g(v)],'o',ms=3.8,color=RED,mew=0,zorder=4)
b.text(u-.06,g(u)-.08,'$u$',ha='right',va='top'); b.text(v+.08,g(v)-.08,'$v$',ha='left',va='top')
b.set_xlim(-2.4,2.4); b.set_ylim(-1.5,1.5); b.set_xticks([-2,-1,0,1,2]); b.set_yticks([-1,0,1]); b.set_xlabel('$x$',labelpad=1); b.set_ylabel('$g$',labelpad=2)
tags(fig, axes)
save(fig, HERE, 'figure', {'a':'x^2/2 on chord [-1,2]','b':'x^4/4-x^2 on chord [-1.6,1]'})
