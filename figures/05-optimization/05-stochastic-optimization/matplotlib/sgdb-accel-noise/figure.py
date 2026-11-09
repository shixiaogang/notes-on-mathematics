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
# H=diag(1,9), x0=(9,1)，加性噪声方差 sigma^2=1：确定性参数下的二阶矩精确递推。
H=[1.,9.]; x0=[9.,1.]
def traj(lam,d0,a1,a2,s2,T):
    # z'=a1 z + a2 zp + noise, var noise=s2
    Ez=[d0,d0]; 
    Ezz,Ezzp,Epp=d0*d0,d0*d0,d0*d0; out=[]
    for t in range(T):
        out.append(.5*lam*Ezz)
        nzz=a1*a1*Ezz+a2*a2*Epp+2*a1*a2*Ezzp+s2
        nzp=a1*Ezz+a2*Ezzp
        Ezz,Ezzp,Epp=nzz,nzp,Ezz
    return np.array(out)
def method(kind,sig2,T=400):
    tot=np.zeros(T)
    for lam,d0 in zip(H,x0):
        if kind=='gd': al=1/9; a1=1-al*lam; a2=0.; s=al*al*sig2
        if kind=='hb': al=.25; be=.25; a1=1+be-al*lam; a2=-be; s=al*al*sig2
        if kind=='nag': al=1/9; be=.5; a1=(1+be)*(1-al*lam); a2=-be*(1-al*lam); s=al*al*sig2
        tot+=traj(lam,d0,a1,a2,s,T)
    return tot
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2,sharey=True)
panel(fig,.125,.965,.97,.25,wspace=.1)
for ax,sig2 in ((a,0.),(b,1.)):
    ax.semilogy(np.maximum(method('gd',sig2),1e-30),color=YELLOW,lw=1.3); ax.semilogy(np.maximum(method('hb',sig2),1e-30),color=GREEN,lw=1.4); ax.semilogy(np.maximum(method('nag',sig2),1e-30),color=PURPLE,lw=1.3)
    ax.set_xlim(0,60); ax.set_ylim(1e-6,200); ax.set_xlabel('$t$',labelpad=1)
    if sig2: print('floors gd,hb,nag',method('gd',sig2)[-1],method('hb',sig2)[-1],method('nag',sig2)[-1])
a.set_ylabel('期望目标差',labelpad=1)
a.text(36,8e-1,'梯度下降',fontsize=7.5); a.text(9,4e-5,'Nesterov',fontsize=7.5); a.text(23,8e-5,'重球',fontsize=7.5)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'H':H,'x0':x0,'sigma2':[0,1]})
