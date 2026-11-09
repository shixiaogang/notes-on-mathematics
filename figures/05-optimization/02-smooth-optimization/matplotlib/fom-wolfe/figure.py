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
# 贯穿例沿 d0=(-9,-9) 的一维函数 phi(alpha)=45-162 alpha+405 alpha^2，c1=0.1，c2=0.45。
fig,ax=figure(width_mm=92,height_mm=54)
panel(fig,.095,.985,.97,.16)
a=np.linspace(0,.42,400); phi=45-162*a+405*a*a; c1,c2=.1,.45
ax.plot(a,phi,color=BLUE,lw=1.5); ax.plot(a,45-162*c1*a,color=STROKE,lw=.95)
ax.plot(a,45-162*a,color=MUTED,lw=.85,ls=(0,(3,2)))
lo=(1-c2)/5; hi=(1+c2)/5; am=(1-c1)*162/405
ax.plot([lo,hi],[1.5,1.5],color=GREEN,lw=3,solid_capstyle='butt'); ax.plot([0,am],[6,6],color=PURPLE,lw=2.2,solid_capstyle='butt')
v=1/9; ax.plot([v],[45-162*v+405*v*v],'o',color=GREEN,ms=5,mew=0,zorder=6); ax.plot([.2],[45-162*.2+405*.04],'o',color=RED,ms=5,mew=0,zorder=6)
ax.plot([v,v],[0,32],color=MUTED,lw=.7,ls=':'); ax.plot([.2,.2],[0,29],color=MUTED,lw=.7,ls=':')
ax.text(.3,42,'Armijo 直线',fontsize=7.5,color=INK,ha='left') if 0 else None
ax.text(.33,42.5,'充分下降线',fontsize=7.5,ha='center',color=INK); ax.text(.3,9,'Armijo',fontsize=7.5,color=INK,ha='center'); ax.text(.355,1.5,'强 Wolfe',fontsize=7.5,color=INK,va='center',ha='center')
ax.text(.135,2.0,'',fontsize=7.5); ax.set_xlim(0,.42); ax.set_ylim(0,50); ax.set_xticks([0,1/9,.2,.3,.4]); ax.set_xticklabels(['0','$1/9$','$1/5$','0.3','0.4'])
ax.set_xlabel(r'$\alpha$',labelpad=1); ax.set_ylabel(r'$\varphi(\alpha)$',labelpad=1)
save(fig,HERE,'figure',{'phi':'45-162a+405a^2','c1':c1,'c2':c2,'armijo_max':am,'wolfe_interval':[lo,hi]})
