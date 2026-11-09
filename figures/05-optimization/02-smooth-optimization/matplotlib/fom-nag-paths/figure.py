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
# 贯穿例：Nesterov alpha=1/9,beta=1/2；重球 alpha=beta=1/4；梯度下降 alpha=1/5。
import matplotlib.gridspec as gs
fig=figure(width_mm=112,height_mm=88)[0]; fig.clf(); fig.set_layout_engine(None)
G=gs.GridSpec(2,2,height_ratios=[1,1.45],left=.105,right=.985,top=.985,bottom=.15,hspace=.62,wspace=.32)
A=fig.add_subplot(G[0,:]); B=fig.add_subplot(G[1,0]); C=fig.add_subplot(G[1,1])
def hb(a,b,T):
    P=[X0.copy(),X0.copy()]
    for t in range(T): P.append(P[-1]-a*H*P[-1]+b*(P[-1]-P[-2]))
    return np.array(P[1:])
def nag(a,b,T):
    P=[X0.copy(),X0.copy()]
    for t in range(T):
        y=P[-1]+b*(P[-1]-P[-2]); P.append(y-a*H*y)
    return np.array(P[1:])
T=30; PG=hb(.2,0,T); PH=hb(.25,.25,T); PN=nag(1/9,.5,T)
contour_ex(A,(-1,10),(-1.2,1.3),[1,5,15,30,45]); path(A,PH[:14],YELLOW); path(A,PN[:14],GREEN); opt(A)
A.set_xlim(-1,10); A.set_ylim(-1.2,1.3); A.set_aspect('equal'); A.set_xticks([0,3,6,9]); A.set_yticks([-1,0,1]); A.set_xlabel('$x_1$',labelpad=1); A.set_ylabel('$x_2$',labelpad=0)
ll=np.linspace(.4,9.6,700)
def md(c1,c0): return np.array([np.max(np.abs(np.roots([1,-c1(l),c0(l)]))) for l in ll])
B.axvspan(1,9,color=BLUE_FILL,lw=0)
B.plot(ll,md(lambda l:1.25-.25*l,lambda l:.25),color=YELLOW,lw=1.5)
B.plot(ll,md(lambda l:1.5*(1-l/9),lambda l:.5*(1-l/9)),color=GREEN,lw=1.7)
B.plot(ll,np.abs(1-.2*ll),color=PURPLE,lw=1.1)
B.set_xlim(.4,9.6); B.set_ylim(0,1.0); B.set_xticks([1,3,5,7,9]); B.set_yticks([0,.5,2/3,1]); B.set_yticklabels(['0','1/2','2/3','1']); B.set_xlabel(r'$\lambda$',labelpad=1); B.set_ylabel('模最大的根',labelpad=1)
B.annotate('重球',xy=(2.2,.5),xytext=(1.6,.2),fontsize=7.5,ha='center',arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1)); B.text(4.7,.40,'Nesterov',fontsize=7.5,color=INK,ha='left') ; B.annotate('梯度下降',xy=(8.2,.64),xytext=(7.0,.82),fontsize=7.5,ha='center',arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1))
ts=np.arange(T+1); C.semilogy(ts,f_ex(PG),color=PURPLE,lw=1.1); C.semilogy(ts,f_ex(PH),color=YELLOW,lw=1.5); C.semilogy(ts,f_ex(PN),color=GREEN,lw=1.6); C.semilogy(ts,86*(2/3)**ts,color=INK,lw=.85,ls=(0,(3,2)))
C.text(20,12,'定理上界',fontsize=7.5,ha='center',color=INK); C.annotate('Nesterov',xy=(27,1.2e-6),xytext=(26,2e-9),fontsize=7.5,ha='center',arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1)); C.text(9,3e-8,'重球',fontsize=7.5,color=INK,ha='center'); C.text(30,.09,'梯度下降',fontsize=7.5,color=INK,ha='right')
C.set_xlabel('$t$',labelpad=1); C.set_ylabel(r'$f-f^*$',labelpad=1); C.set_xlim(0,30); C.set_ylim(1e-10,300); C.set_yticks([1e-10,1e-5,1])
tag(fig,A,'(a)',d=.1); tag(fig,B,'(b)',y=.042); tag(fig,C,'(c)',y=.042)
save(fig,HERE,'figure',{'nag':[1/9,.5],'hb':[.25,.25],'gd':.2})
