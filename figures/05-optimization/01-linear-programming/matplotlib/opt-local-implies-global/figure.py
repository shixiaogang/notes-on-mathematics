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

# 若局部最优 u 不是全局最优，连到更低点 v 的弦紧靠 u 处就低于图像，违反凸性。
f = lambda x: x**4/4-x**3/3-x**2
fig, ax = figure(width_mm=92, height_mm=54)
x=np.linspace(-1.5,1.5,400); ax.plot(x,f(x),color=BLUE,lw=1.4,zorder=2)
u,v=-1,1.5; xs=np.linspace(u,v,300); ch=f(u)+(f(v)-f(u))/(v-u)*(xs-u)
ax.fill_between(xs,ch,f(xs),where=f(xs)>ch,facecolor=RED_FILL,edgecolor='none',zorder=0)
ax.plot([u,v],[f(u),f(v)],color=GREEN,lw=1.3,zorder=3)
ax.plot([u],[f(u)],'o',ms=4.6,color=YELLOW,mew=0,zorder=5); ax.plot([v],[f(v)],'o',ms=5,color=RED,mew=0,zorder=5)
t=.14; z=u+t*(v-u); fz=f(u)+(f(v)-f(u))*t
ax.plot([z],[fz],'o',ms=3.6,color=GREEN,mew=0,zorder=5)
ax.annotate('弦上更低的点',xy=(z,fz),xytext=(-1.42,-1.72),fontsize=7.5,color=INK,arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=2))
ax.text(u-.04,f(u)+.13,'$u$',ha='center'); ax.text(v+.04,f(v)-.04,'$v$',ha='left',va='center')
r=.6; ax.plot([u-r,u+r],[-2.72,-2.72],color=STROKE,lw=1.5,solid_capstyle='butt'); ax.text(u,-2.66,'邻域',ha='center',va='bottom',color=STROKE,fontsize=7.5)
ax.set_xlim(-1.75,1.85); ax.set_ylim(-2.95,.5); ax.set_xticks([-1,0,1]); ax.set_yticks([-2,-1,0]); ax.set_xlabel('$x$',labelpad=1); ax.set_ylabel('$f(x)$',labelpad=2)
save(fig, HERE, 'figure', {'f':'x^4/4-x^3/3-x^2','u':-1,'v':1.5})
