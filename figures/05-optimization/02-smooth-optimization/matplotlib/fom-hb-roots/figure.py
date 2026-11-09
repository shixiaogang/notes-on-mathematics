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
# 重球特征根：alpha=beta=1/4，lambda∈[1,9]。
fig,(a,b)=figure(width_mm=112,height_mm=58,ncols=2,gridspec_kw={'width_ratios':[1,1.25]})
panel(fig,.095,.985,.97,.25,wspace=.3)
def roots(l,al,be):
    return np.roots([1,-(1+be-al*l),be])
th=np.linspace(0,2*np.pi,300); a.plot(np.cos(th),np.sin(th),color=STROKE,lw=.85); a.plot(.5*np.cos(th),.5*np.sin(th),color=MUTED,lw=.7,ls=':')
L=np.linspace(1,9,120); R=np.array([roots(l,.25,.25) for l in L])
for i in range(2): pass
a.plot(np.real(R).flatten(),np.imag(R).flatten(),'.',color=GREEN,ms=2.4,mew=0)
g=1-.2*L; a.plot(g,0*g,color=YELLOW,lw=2)
for l,lab,dx,dy in ((1,r'$\lambda=1$',.06,.13),(9,r'$\lambda=9$',-.06,.13),(5,r'$\lambda=5$',0,.56)):
    r=roots(l,.25,.25); a.plot(np.real(r),np.imag(r),'o',color=GREEN,ms=3.8,mew=0,zorder=6)
    a.text(np.real(r[0])+dx,np.imag(r[0])*0+dy,lab,fontsize=7.5,ha='center')
a.set_xlim(-1.08,1.08); a.set_ylim(-1.08,1.08); a.set_aspect('equal'); a.set_xlabel('实部',labelpad=1); a.set_ylabel('虚部',labelpad=0); a.set_xticks([-1,0,1]); a.set_yticks([-1,0,1])
ll=np.linspace(.4,11,1000); md=lambda al,be:np.array([np.max(np.abs(roots(l,al,be))) for l in ll])
b.axvspan(1,9,color=BLUE_FILL,lw=0); b.plot(ll,np.abs(1-.2*ll),color=YELLOW,lw=1.5); b.plot(ll,md(.25,.25),color=GREEN,lw=1.7); b.plot(ll,md(.19,.06),color=PURPLE,lw=1.2)
b.axhline(1,color=STROKE,lw=.85)
b.text(1.3,.09,'$\\beta=0$',fontsize=7.5,color=INK) if 0 else None
b.text(3.6,.545,r'$\beta=1/4$',fontsize=7.5,color=INK,ha='left'); b.annotate(r'$\beta=0.06$',xy=(7.4,.245),xytext=(7.5,.06),fontsize=7.5,ha='center',arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1))
b.text(8.1,.18,'梯度下降',fontsize=7.5,color=INK,ha='left') if 0 else None
b.annotate('梯度下降',xy=(2.2,1-.44),xytext=(1.0,.15),fontsize=7.5,arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1))
b.set_xlim(.4,11); b.set_ylim(0,1.15); b.set_xticks([1,3,5,7,9,11]); b.set_yticks([0,.5,1]); b.set_xlabel(r'$\lambda$',labelpad=1); b.set_ylabel('模最大的根',labelpad=1)
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
save(fig,HERE,'figure',{'alpha_beta':[.25,.25]})
