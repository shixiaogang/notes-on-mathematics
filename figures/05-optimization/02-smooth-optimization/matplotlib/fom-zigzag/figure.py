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
# 梯度下降 alpha=1/5 在贯穿例上的每步位移分解与相邻两步平均。
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2,sharey=True)
panel(fig,.085,.985,.97,.25,wspace=.1)
P=[X0.copy()]
for t in range(9): P.append(P[-1]-.2*H*P[-1])
P=np.array(P); s=P[1:]-P[:-1]; av=.5*(s[1:]+s[:-1])
w=.38; t=np.arange(8)
for ax,d in ((a,s[:8]),(b,av[:8])):
    ax.bar(t-w/2,d[:,0],w,color=BLUE); ax.bar(t+w/2,d[:,1],w,color=GREEN); ax.axhline(0,color=STROKE,lw=.75)
    ax.set_xlabel('$t$',labelpad=1); ax.set_xticks(range(0,8,2))
a.set_ylabel('位移分量',labelpad=1); a.set_ylim(-2,2)
a.text(4,-1.4,'$x_1$',fontsize=7.5,color=INK); a.text(2.9,1.2,'$x_2$',fontsize=7.5,color=INK)
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
save(fig,HERE,'figure',{'alpha':.2})
