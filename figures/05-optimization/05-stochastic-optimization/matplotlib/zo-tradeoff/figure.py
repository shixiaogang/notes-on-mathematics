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
# 扰动尺度的 U 形：phi=s^2/2+s^3/6，s0=1，sigma=0.01，独立噪声。曲线为偏差平方加方差的精确值，点为 2e5 次 Monte Carlo 的均方根误差。
fig,ax=figure(width_mm=92,height_mm=58)
phi=lambda s:.5*s**2+s**3/6; s0=1.; sig=.01
h=np.logspace(-3,0,200)
bf=(phi(s0+h)-phi(s0))/h-1.5; bc=(phi(s0+h)-phi(s0-h))/(2*h)-1.5
Rf=(bf**2+2*sig**2/h**2)**.5; Rc=(bc**2+sig**2/(2*h**2))**.5
ax.loglog(h,Rf,color=YELLOW,lw=1.6); ax.loglog(h,Rc,color=GREEN,lw=1.4)
rng=np.random.default_rng(6); hs=np.logspace(-2.7,-.2,9); N=200000
Mf=[];Mc=[]
for b in hs:
    z=sig*rng.standard_normal((N,2)); Mf.append(((((phi(s0+b)-phi(s0)+z[:,0]-z[:,1])/b-1.5)**2).mean())**.5)
    z=sig*rng.standard_normal((N,2)); Mc.append(((((phi(s0+b)-phi(s0-b)+z[:,0]-z[:,1])/(2*b)-1.5)**2).mean())**.5)
ax.loglog(hs,Mf,'o',color=YELLOW,ms=3.6,mew=0); ax.loglog(hs,Mc,'o',color=GREEN,ms=3.6,mew=0)
i=Rf.argmin(); j=Rc.argmin(); ax.plot([h[i]],[Rf[i]],'o',color=RED,ms=5,mew=0,zorder=6); ax.plot([h[j]],[Rc[j]],'o',color=RED,ms=5,mew=0,zorder=6)
ax.set_xlabel('$h$',labelpad=1); ax.set_ylabel('均方根误差',labelpad=1); ax.set_xlim(1e-3,1)
ax.text(.012,1.75,'前向',fontsize=7.5,color=INK); ax.text(.0025,.8,'',fontsize=7.5); ax.text(.03,.05,'中心',fontsize=7.5,color=INK)
save(fig,HERE,'figure',{'sigma':sig,'h_forward':float(h[i]),'rmse_forward':float(Rf[i]),'h_central':float(h[j]),'rmse_central':float(Rc[j])})
print(h[i],Rf[i],h[j],Rc[j])
