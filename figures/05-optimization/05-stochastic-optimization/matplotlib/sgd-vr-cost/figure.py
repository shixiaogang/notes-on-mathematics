from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
# 贯穿例：f_i(x)=a_i(x-b_i)^2/2，a=(1,2,3)，b=(-3,0,3)；f(x)=(x-1)^2+5，x*=1。
A = np.array([1., 2., 3.]); B = np.array([-3., 0., 3.])
def gi(x): return A*(x-B)
def panel(fig, left, right, top, bottom, wspace=.3, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.05):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='top')

# 教学实例：N=500，n=20 的正则最小二乘，种子 7，||a_i||=1。
rng=np.random.default_rng(7)
N,n=500,20
S=np.diag(np.logspace(0,-2.2,n)**.5)
Am=rng.normal(size=(N,n))@S; Am/=np.linalg.norm(Am,axis=1,keepdims=True)
xt=rng.normal(size=n); b_=Am@xt+.1*rng.normal(size=N); gam=.005
H=Am.T@Am/N+gam*np.eye(n); xs=np.linalg.solve(H,Am.T@b_/N)
fv=lambda x:.5*np.mean((Am@x-b_)**2)+.5*gam*x@x; fs=fv(xs); Lf=np.linalg.eigvalsh(H)[-1]; mu=np.linalg.eigvalsh(H)[0]; Lm=1+gam
print('kappa_f',Lf/mu,'Lmax/mu',Lm/mu)
gi_=lambda x,i:(Am[i]@x-b_[i])*Am[i]+gam*x
gf=lambda x:H@x-Am.T@b_/N
ep=40
def rec(R,c,x,o):
    if c>=o[0]: R[0].append(c/N); R[1].append(fv(x)-fs); o[0]+=N/2
x0=np.zeros(n)
# GD
R=[[],[]];x=x0.copy();c=0;o=[0]
while c<=ep*N: rec(R,c,x,o); x=x-gf(x)/Lf; c+=N
gd=R
# SGD
r=np.random.default_rng(1)
R=[[],[]];x=x0.copy();c=0;o=[0]
while c<=ep*N: rec(R,c,x,o); x=x-.1*gi_(x,r.integers(N)); c+=1
sg=R
# SVRG
R=[[],[]];x=x0.copy();c=0;o=[0];al=.2/Lm;m=2*N
while c<=ep*N:
    xs_=x.copy();gt=gf(xs_);c+=N
    for _ in range(m):
        i=r.integers(N);x=x-al*(gi_(x,i)-gi_(xs_,i)+gt);c+=2
        rec(R,c,x,o)
sv=R
# SAGA
R=[[],[]];x=x0.copy();c=N;o=[0];al=1/(3*Lm);tab=np.array([gi_(x,i) for i in range(N)]);mean=tab.mean(0)
while c<=ep*N:
    i=r.integers(N);gn=gi_(x,i);d=gn-tab[i]+mean;x=x-al*d;mean=mean+(gn-tab[i])/N;tab[i]=gn;c+=1
    rec(R,c,x,o)
sa=R
fig,ax=figure(width_mm=104,height_mm=58)
ax.semilogy(*gd,color=YELLOW,lw=1.7); ax.semilogy(*sg,color=PURPLE,lw=1.3); ax.semilogy(*sv,color=GREEN,lw=1.4); ax.semilogy(*sa,color=BLUE,lw=1.3,ls=(0,(4,2)))
print('finals',gd[1][-1],sg[1][-1],sv[1][-1],sa[1][-1])
ax.text(31,3.5e-5,'完整梯度',fontsize=7.5); ax.text(31,1.7e-3,'随机梯度',fontsize=7.5)
ax.text(30,1.2e-7,'SVRG',fontsize=7.5); ax.text(13.5,2e-8,'SAGA',fontsize=7.5)
ax.set_xlabel('完整遍历轮数',labelpad=1); ax.set_ylabel(r'$f-f^*$',labelpad=1); ax.set_xlim(0,ep); ax.set_ylim(1e-12,3)
save(fig,HERE,'figure',{'seed':7,'N':N,'n':n,'gamma':gam,'kappa_f':float(Lf/mu)})
