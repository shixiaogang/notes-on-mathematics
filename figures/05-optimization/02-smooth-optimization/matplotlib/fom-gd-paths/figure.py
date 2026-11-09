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
# 贯穿例上不同固定步长的路径。
import matplotlib.gridspec as gs
fig=figure(width_mm=112,height_mm=78)[0]; fig.clf(); fig.set_layout_engine(None)
G=gs.GridSpec(2,1,height_ratios=[2.4,3.6],left=.06,right=.99,top=.985,bottom=.14,hspace=.5)
def run(a,T):
    P=[X0.copy()]
    for t in range(T): P.append(P[-1]-a*H*P[-1])
    return np.array(P)
A=fig.add_subplot(G[0]); B=fig.add_subplot(G[1])
lv=[1,5,15,30,45]
contour_ex(A,(-1,10),(-1.2,1.2),lv); path(A,run(1/9,14),YELLOW); path(A,run(1/5,14),GREEN); opt(A)
contour_ex(B,(-1,10),(-1.8,1.8),lv); P=run(.23,8); path(B,P,RED); opt(B)
for a,yl in ((A,(-1.2,1.2)),(B,(-1.8,1.8))):
    a.set_xlim(-1,10); a.set_ylim(*yl); a.set_aspect('equal'); a.set_xticks([0,3,6,9]); a.set_yticks([-1,0,1])
A.text(5.7,.33,r'$\alpha=1/9$',color=INK,fontsize=7.5); A.text(7.6,-1.05,r'$\alpha=1/5$',color=INK,fontsize=7.5)
B.text(4.7,1.3,r'$\alpha=0.23$',color=INK,fontsize=7.5)
A.set_ylabel('$x_2$',labelpad=0); B.set_ylabel('$x_2$',labelpad=0); B.set_xlabel('$x_1$',labelpad=1)
tag(fig,A,'(a)',d=.06); tag(fig,B,'(b)',y=.052)
B.set_xlabel('')
fig.text(.04,.985,'',)
save(fig,HERE,'figure',{'steps':[1/9,1/5,.23],'x0':[9,1]})
