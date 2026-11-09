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
# 贯穿例：最速下降 vs 共轭梯度（精确线搜索）。
fig,ax=figure(width_mm=112,height_mm=46)
panel(fig,.08,.99,.98,.2)
P=[X0.copy()]
for t in range(14):
    g=H*P[-1]; a=(g@g)/(g@(H*g)); P.append(P[-1]-a*g)
Q=np.array([[9,1],[7.2,-.8],[0,0]])
contour_ex(ax,(-1,10),(-1.5,1.5),[1,5,15,30,45]); path(ax,P,YELLOW); path(ax,Q,GREEN,lw=1.5,ms=4); opt(ax)
ax.text(9.15,1.05,'$x^{(0)}$',fontsize=7.5); ax.text(7.2,-1.15,'$x^{(1)}$',fontsize=7.5,ha='center')
ax.set_xlim(-1,10); ax.set_ylim(-1.5,1.5); ax.set_aspect('equal'); ax.set_xticks([0,3,6,9]); ax.set_yticks([-1,0,1]); ax.set_xlabel('$x_1$',labelpad=1); ax.set_ylabel('$x_2$',labelpad=0)
save(fig,HERE,'figure',{'cg_points':[[9,1],[7.2,-.8],[0,0]]})
