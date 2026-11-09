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
# 一元例 f(x)=sqrt(1+x^2)，f''<=1 故 L=1；在 x=2.4 处的切线与二次上界。
fig, ax = figure(width_mm=92, height_mm=54)
panel(fig,.08,.985,.97,.13)
F=lambda x:np.sqrt(1+x*x); dF=lambda x:x/np.sqrt(1+x*x)
x0=2.4; xp=x0-dF(x0); xx=np.linspace(-.6,3.4,400)
q=F(x0)+dF(x0)*(xx-x0)+.5*(xx-x0)**2; lin=F(x0)+dF(x0)*(xx-x0)
ax.plot(xx,F(xx),color=BLUE,lw=1.5); ax.plot(xx,q,color=GREEN,lw=1.3); ax.plot(xx,lin,color=MUTED,lw=.85,ls=(0,(3,2)))
ax.plot([x0],[F(x0)],'o',color=GREEN,ms=4.6,mew=0,zorder=5); ax.plot([xp],[F(xp)],'o',color=GREEN,ms=4.6,mew=0,zorder=5)
qp=F(x0)-.5*dF(x0)**2; ax.plot([xp],[qp],'o',mfc='white',mec=GREEN,ms=4.6,mew=1,zorder=5)
ax.plot([xp,xp],[0.7,F(xp)],color=MUTED,lw=.7,ls=':'); ax.plot([x0,x0],[0.7,F(x0)],color=MUTED,lw=.7,ls=':')
ax.plot([x0+.08,x0+.08],[qp,F(x0)],color=INK,lw=.85); ax.plot([xp,x0+.08],[qp,qp],color=MUTED,lw=.7,ls=':')
ax.text(x0+.13,(qp+F(x0))/2,r'$\frac{1}{2L}f^{\prime}(x)^2$',va='center',fontsize=7.5)
ax.text(-.45,1.3,'$f$',color=INK); ax.text(.42,2.9,'二次上界',ha='left',color=INK,fontsize=7.5); ax.text(3.0,3.28,'切线',color=MUTED,fontsize=7.5,ha='right')
ax.set_xticks([xp,x0]); ax.set_xticklabels(['$x^{+}$','$x$']); ax.set_yticks([]); ax.set_xlim(-.6,3.4); ax.set_ylim(.7,4.1)
save(fig,HERE,'figure',{'f':'sqrt(1+x^2)','L':1,'x':x0,'x_plus':xp})
