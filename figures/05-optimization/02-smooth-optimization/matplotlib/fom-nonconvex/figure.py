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
# f=-cos x1 + 4.5 x2^2，L=9，下确界 -1，alpha=1/9。
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.075,.985,.97,.25,wspace=.3)
F=lambda x:-np.cos(x[0])+4.5*x[1]**2; G=lambda x:np.array([np.sin(x[0]),9*x[1]])
def run(x0,T):
    P=[np.array(x0,float)]
    for t in range(T): P.append(P[-1]-G(P[-1])/9)
    return np.array(P)
X,Y=np.meshgrid(np.linspace(-1,4.4,600),np.linspace(-1.3,1.3,400))
a.contour(X,Y,-np.cos(X)+4.5*Y*Y,levels=[-.8,-.4,0,.6,1,1.6,3,5],colors=[BLUE],linewidths=.65)
P=run([3,1],80); S=run([np.pi,1],5)
a.plot(P[:,0],P[:,1],'-',color=GREEN,lw=1.3); a.plot(P[::2,0],P[::2,1],'o',color=GREEN,ms=2.6,mew=0)
a.plot(S[:2,0],S[:2,1],'-',color=YELLOW,lw=1.5); opt(a); a.plot([np.pi],[0],'o',mfc='white',mec=RED,ms=5,mew=1,zorder=6)
a.text(.05,.14,r'$x^*$',fontsize=7.5); a.text(3.3,.05,'鞍点',fontsize=7.5)
a.set_xlim(-1,4.4); a.set_ylim(-1.3,1.3); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0); a.set_xticks([0,1,2,3,4]); a.set_yticks([-1,0,1])
T=2000; P=run([3,1],T); g=np.linalg.norm(np.array([np.sin(P[:,0]),9*P[:,1]]).T,axis=1); gm=np.sqrt(np.minimum.accumulate(g**2))
d=F(P[0])+1; t=np.arange(1,T+1)
b.loglog(t,gm[:T],color=GREEN,lw=1.5); b.loglog(t,np.sqrt(2*9*d/t),color=PURPLE,lw=.95,ls=(0,(3,2)))
b.text(30,2.4,'定理上界',fontsize=7.5,color=INK); b.text(3,.06,r'$\min_{t<T}\Vert g^{(t)}\Vert_2$',fontsize=7.5,color=INK)
b.set_xlabel('$T$',labelpad=1); b.set_ylim(1e-3,20); b.set_xlim(1,2000)
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
save(fig,HERE,'figure',{'f':'-cos x1+4.5 x2^2','L':9,'x0':[3,1],'saddle_start':'(pi,1)'})
