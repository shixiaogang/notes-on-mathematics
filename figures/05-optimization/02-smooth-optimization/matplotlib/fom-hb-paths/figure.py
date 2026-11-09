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
# 贯穿例上重球（alpha=beta=1/4）与梯度下降（alpha=1/5）。
import matplotlib.gridspec as gs
fig=figure(width_mm=112,height_mm=88)[0]; fig.clf(); fig.set_layout_engine(None)
G=gs.GridSpec(2,2,height_ratios=[1,1.45],left=.105,right=.985,top=.985,bottom=.15,hspace=.62,wspace=.32)
A=fig.add_subplot(G[0,:]); B=fig.add_subplot(G[1,0]); C=fig.add_subplot(G[1,1])
def hb(a,b,T):
    P=[X0.copy(),X0.copy()]
    for t in range(T): P.append(P[-1]-a*H*P[-1]+b*(P[-1]-P[-2]))
    return np.array(P[1:])
T=30; PG=hb(.2,0,T); PH=hb(.25,.25,T)
contour_ex(A,(-1,10),(-1.2,1.3),[1,5,15,30,45]); path(A,PG[:14],YELLOW); path(A,PH[:14],GREEN); opt(A)
A.set_xlim(-1,10); A.set_ylim(-1.2,1.3); A.set_aspect('equal'); A.set_xticks([0,3,6,9]); A.set_yticks([-1,0,1]); A.set_xlabel('$x_1$',labelpad=1); A.set_ylabel('$x_2$',labelpad=0)
t=np.arange(0,11); y1=(9+4.5*t)/2.**t; y2=(1+1.5*t)*(-.5)**t
B.plot(t,y1/9,'-o',color=BLUE,ms=3,mew=0,lw=1); B.plot(t,y2,'-o',color=GREEN,ms=3,mew=0,lw=1)
B.plot(t,.5**t,color=PURPLE,lw=.95,ls=(0,(3,2))); B.plot(t,-.5**t,color=PURPLE,lw=.95,ls=(0,(3,2))); B.axhline(0,color=STROKE,lw=.7)
B.text(4.6,.45,'$x_1^{(t)}/x_1^{(0)}$',fontsize=7.5); B.text(2.8,-.9,'$x_2^{(t)}/x_2^{(0)}$',fontsize=7.5)
B.set_xlabel('$t$',labelpad=1); B.set_xlim(0,10); B.set_xticks(range(0,11,2))
ts=np.arange(T+1); C.semilogy(ts,f_ex(PG),color=YELLOW,lw=1.5); C.semilogy(ts,f_ex(PH),color=GREEN,lw=1.6); C.semilogy(ts,45*.25**ts,color=PURPLE,lw=.95,ls=(0,(3,2)))
C.text(17,4,'梯度下降',fontsize=7.5,color=INK); C.text(19,3e-6,'重球',fontsize=7.5,color=INK,ha='left')
C.set_xlabel('$t$',labelpad=1); C.set_ylabel(r'$f-f^*$',labelpad=1); C.set_xlim(0,30); C.set_ylim(1e-10,200); C.set_yticks([1e-10,1e-5,1])
tag(fig,A,'(a)',d=.1); tag(fig,B,'(b)',y=.042); tag(fig,C,'(c)',y=.042)
save(fig,HERE,'figure',{'gd_alpha':.2,'hb':[.25,.25],'x0':[9,1]})
