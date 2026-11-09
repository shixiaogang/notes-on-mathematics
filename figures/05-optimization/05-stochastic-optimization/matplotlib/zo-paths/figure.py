from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panels(w,h,n,left=.07,right=.99,top=.97,bottom=.22,wspace=.25,rows=1,**k):
    fig=figure(width_mm=w,height_mm=h)[0]; fig.clf(); fig.set_layout_engine(None)
    A=[fig.add_subplot(rows,n,i+1,**k) for i in range(n*rows)]
    fig.subplots_adjust(left=left,right=right,top=top,bottom=bottom,wspace=wspace)
    return fig,A
def tag(fig,ax,s,y):
    p=ax.get_position(); fig.text((p.x0+p.x1)/2,y,s,ha='center',va='bottom')
H2=np.array([1.,9.]); X0=np.array([9.,1.])
def f2(x): return .5*(H2*np.asarray(x,float)**2).sum(-1)
def g2(x): return H2*np.asarray(x,float)
def sphere(rng,k,n=2):
    u=rng.standard_normal((k,n)); return u/np.linalg.norm(u,axis=1,keepdims=True)
# 贯穿例，sigma=0.1。绿：双点球面估计 alpha=0.05, delta=0.5，单次运行前三轮用正文手算的方向与噪声；
# 黄：中心坐标差分的梯度下降 alpha=0.1, h=0.5。(b) 为 200 次运行的平均目标差。
fig=figure(width_mm=112,height_mm=92)[0]; fig.clf(); fig.set_layout_engine(None)
A=[fig.add_axes([.11,.60,.86,.385]),fig.add_axes([.11,.155,.86,.30])]
rng=np.random.default_rng(7); a=.05; d=.5; s=.1; T=120
U=[np.array(u) for u in ((.6,.8),(.8,-.6),(.28,.96))]; Z=[(.1,-.1),(-.1,.1),(.05,.15)]
x=X0.copy(); P=[x.copy()]
for t in range(T):
    if t<3: u=U[t]; z=Z[t]
    else: u=sphere(rng,1)[0]; z=s*rng.standard_normal(2)
    D=(f2(x+d*u)+z[0]-f2(x-d*u)-z[1])/(2*d); x=x-a*2*D*u; P.append(x.copy())
P=np.array(P)
g=X0.copy(); Pg=[g.copy()]
for t in range(T//2):
    g=g-.1*(g2(g)+s/(2**.5*.5)*rng.standard_normal(2)); Pg.append(g.copy())
Pg=np.array(Pg)
X,Y=np.meshgrid(np.linspace(-1.2,10,500),np.linspace(-2.3,2.3,400))
A[0].contour(X,Y,.5*(X**2+9*Y**2),levels=[1,5,15,30,45],colors=[BLUE],linewidths=.65)
A[0].plot(Pg[:,0],Pg[:,1],'-o',color=YELLOW,lw=1.3,ms=2.4,mew=0,zorder=3); A[0].plot(P[:,0],P[:,1],'-o',color=GREEN,lw=1.1,ms=2.2,mew=0,zorder=4)
A[0].plot([0],[0],'o',color=RED,ms=4.8,mew=0,zorder=6); A[0].set_xlim(-1.2,10); A[0].set_ylim(-2.3,2.3); A[0].set_aspect('equal'); A[0].set_xticks([0,3,6,9]); A[0].set_yticks([-2,0,2]); A[0].set_ylabel('$x_2$',labelpad=0); A[0].set_xlabel('$x_1$',labelpad=0)
R=200; x=np.tile(X0,(R,1)); V=[f2(x).mean()]
for t in range(T):
    u=sphere(rng,R); z=s*rng.standard_normal((R,2)); D=(f2(x+d*u)+z[:,0]-f2(x-d*u)-z[:,1])/(2*d); x=x-a*2*D[:,None]*u; V.append(f2(x).mean())
g=np.tile(X0,(R,1)); Vg=[f2(g).mean()]
for t in range(T//2):
    g=g-.1*(H2*g+s/(2**.5*.5)*rng.standard_normal((R,2))); Vg.append(f2(g).mean())
A[1].semilogy(2*np.arange(T+1),V,color=GREEN,lw=1.3); A[1].semilogy(4*np.arange(T//2+1),Vg,color=YELLOW,lw=1.6)
A[1].set_xlabel('函数读数次数',labelpad=0); A[1].set_ylabel('平均目标差',labelpad=1); A[1].set_xlim(0,240)
tag(fig,A[0],'(a)',.485); tag(fig,A[1],'(b)',.012)
save(fig,HERE,'figure',{'alpha':a,'delta':d,'sigma':s,'seed':7,'final':float(V[-1]),'final_gd':float(Vg[-1])})
print(V[-1],Vg[-1],V[60],Vg[30])
