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
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
# 逐坐标缩放与坐标系：H=diag(1,9)，x0=(9,1)，精确梯度；旋转 45 度后的同一问题。
H0=np.diag([1.,9.]); th=np.pi/4; Q=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
def adagrad(H,x0,al,T):
    x=x0.copy();v=np.zeros(2);P=[x.copy()]
    for _ in range(T):
        g=H@x;v=v+g*g;x=x-al*g/(np.sqrt(v)+1e-8);P.append(x.copy())
    return np.array(P)
def adam(H,x0,al,T,b1=.9,b2=.999):
    x=x0.copy();m=np.zeros(2);v=np.zeros(2);P=[x.copy()]
    for k in range(1,T+1):
        g=H@x;m=b1*m+(1-b1)*g;v=b2*v+(1-b2)*g*g
        x=x-al*(m/(1-b1**k))/(np.sqrt(v/(1-b2**k))+1e-8);P.append(x.copy())
    return np.array(P)
def gd(H,x0,al,T):
    x=x0.copy();P=[x.copy()]
    for _ in range(T): x=x-al*H@x;P.append(x.copy())
    return np.array(P)
def fv(H,P): return .5*np.einsum('ij,jk,ik->i',P,H,P)
x0=np.array([9.,1.]); T=60; Hr=Q@H0@Q.T; xr=Q@x0
G=gd(H0,x0,1/9,T);A=adagrad(H0,x0,3.,T);M=adam(H0,x0,.5,T)
Gr=gd(Hr,xr,1/9,T);Ar=adagrad(Hr,xr,3.,T);Mr=adam(Hr,xr,.5,T)
for n,P,H in (('gd',G,H0),('ada',A,H0),('adam',M,H0),('gdr',Gr,Hr),('adar',Ar,Hr),('adamr',Mr,Hr)): print(n,fv(H,P)[[5,10,20,60]])
fig,(a,b)=figure(width_mm=112,height_mm=58,ncols=2,gridspec_kw={'width_ratios':[1.15,1]})
panel(fig,.075,.965,.97,.25,wspace=.3)
X,Y=np.meshgrid(np.linspace(-2,10,500),np.linspace(-3.2,3.2,400)); a.contour(X,Y,.5*(X*X+9*Y*Y),levels=[1,4,10,20,40,65],colors=[BLUE],linewidths=.65)
for P,c in ((G,YELLOW),(A,GREEN),(M,PURPLE)): a.plot(P[:26,0],P[:26,1],'-o',color=c,lw=1.,ms=2.2,mew=0)
a.plot([0],[0],'o',color=RED,ms=4.6,mew=0,zorder=6); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=1); a.set_xlim(-2,10); a.set_ylim(-3.2,3.2)
for P,H,ls in ((G,H0,'-'),(Gr,Hr,'--')): b.semilogy(np.maximum(fv(H,P),1e-14),color=YELLOW,ls=ls,lw=1.25)
for P,H,ls in ((A,H0,'-'),(Ar,Hr,'--')): b.semilogy(np.maximum(fv(H,P),1e-14),color=GREEN,ls=ls,lw=1.25)
for P,H,ls in ((M,H0,'-'),(Mr,Hr,'--')): b.semilogy(np.maximum(fv(H,P),1e-14),color=PURPLE,ls=ls,lw=1.25)
b.set_xlabel('$t$',labelpad=1); b.set_ylabel('$f$',labelpad=1); b.set_xlim(0,60)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'alphas':{'gd':'1/9','adagrad':3,'adam':.5}})
