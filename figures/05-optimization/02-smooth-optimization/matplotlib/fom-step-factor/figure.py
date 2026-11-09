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
def tag(fig, ax, s, y=None, d=.085):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
# 贯穿例：f(x)=(x1^2+9 x2^2)/2，x0=(9,1)，mu=1，L=9，kappa=9。
H = np.array([1., 9.]); X0 = np.array([9., 1.])
def f_ex(x): return .5*(H*np.asarray(x)**2).sum(-1)
def contour_ex(ax, xr, yr, levels):
    X,Y = np.meshgrid(np.linspace(*xr,700), np.linspace(*yr,500))
    ax.contour(X,Y,.5*(X**2+9*Y**2),levels=levels,colors=[BLUE],linewidths=.65)
def path(ax, P, c, ms=3.2, lw=1.2, **k):
    P=np.asarray(P); ax.plot(P[:,0],P[:,1],'-o',color=c,lw=lw,ms=ms,mew=0,zorder=4,**k)
def opt(ax, x=0, y=0): ax.plot([x],[y],'o',ms=4.8,color=RED,mew=0,zorder=6)
# 贯穿例两方向的收缩因子 |1-alpha*lambda|，lambda=1,9。
fig, ax = figure(width_mm=92, height_mm=54)
panel(fig,.105,.985,.97,.17)
a=np.linspace(0,.27,600); f1=np.abs(1-a); f9=np.abs(1-9*a); m=np.maximum(f1,f9)
ax.plot(a,f1,color=BLUE,lw=.95,ls=(0,(3,2))); ax.plot(a,f9,color=BLUE,lw=.95)
ax.plot(a,m,color=GREEN,lw=1.7)
ax.axhline(1,color=STROKE,lw=.85); ax.fill_between(a[a>2/9],1,1.5,color=RED_FILL,lw=0)
for v,c,mk in ((1/9,YELLOW,'o'),(1/5,RED,'o')):
    ax.plot([v],[max(abs(1-v),abs(1-9*v))],mk,color=c,ms=5,mew=0,zorder=6)
ax.text(.005,.70,r'$\lambda=9$',fontsize=7.5); ax.text(.035,1.03,r'$\lambda=1$',fontsize=7.5)
ax.text(.2455,1.3,'发散',ha='center',color=INK); ax.plot([2/9,2/9],[0,1.5],color=MUTED,lw=.7,ls=':')
ax.set_xticks([0,1/9,1/5,2/9,]); ax.set_xticklabels(['0','$1/9$','$1/5$','$2/9$'])
ax.set_yticks([0,.5,.8,1,1.5]); ax.set_yticklabels(['0','0.5','0.8','1','1.5']); ax.set_xlim(0,.27); ax.set_ylim(0,1.5)
ax.set_xlabel(r'$\alpha$',labelpad=1); ax.set_ylabel('收缩因子',labelpad=1)
save(fig,HERE,'figure',{'lambdas':[1,9]})
