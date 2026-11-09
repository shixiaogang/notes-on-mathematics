from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# ridge: d=30, A 40x30 random seed 3, x=0.5; outer F=.5||Cy-e||^2, C 25x30 random. GD inner alpha=1/L from y0=0; CG on H(yhat)=H for k steps.
rng=np.random.default_rng(3); d=30
A=rng.normal(size=(40,d))/np.sqrt(40); b=rng.normal(size=40)+A@rng.normal(size=d)
C=rng.normal(size=(25,d))/np.sqrt(25); e=rng.normal(size=25)
x=.05; H=A.T@A+x*np.eye(d); L=np.linalg.eigvalsh(H)[-1]; mu=np.linalg.eigvalsh(H)[0]; print('kappa',L/mu)
ys=np.linalg.solve(H,A.T@b); gF=lambda y:C.T@(C@y-e)
true=-ys@np.linalg.solve(H,gF(ys))
def est(K,k):
    y=np.zeros(d)
    for _ in range(K): y=y-(H@y-A.T@b)/L
    f=gF(y); v=np.zeros(d); r=f.copy(); p=r.copy()
    for _ in range(k):
        if np.linalg.norm(r)<1e-14: break
        Hp=H@p; a=(r@r)/(p@Hp); v=v+a*p; r2=r-a*Hp; p=r2+(r2@r2)/(r@r)*p; r=r2
    return abs(-y@v-true)
fig, axs = figure(width_mm=112, height_mm=56, ncols=2, sharey=True)
Ks=np.unique(np.round(np.logspace(0,4,40)).astype(int)); ax=axs[0]
for k,c,lw in [(3,YELLOW,1.6),(10,GREEN,1.4),(30,PURPLE,1.3)]:
    ax.loglog(Ks,[max(est(int(K),k),1e-12) for K in Ks],color=c,lw=lw)
ax.text(1.5e3,.32,'$k=3$',color=YELLOW,fontsize=7.5); ax.text(1.5e3,1.8e-2,'$k=10$',color=GREEN,fontsize=7.5); ax.text(1.5e3,1.5e-7,'$k=30$',color=PURPLE,fontsize=7.5)
clean(ax,(1,1e4),(1e-9,30),'内层步数 K','超梯度误差'); ax.set_yticks([1e-8,1e-5,1e-2,10]); tag(ax,'(a)',-.27)
ax=axs[1]
ks=np.arange(1,41)
for K,c,lw in [(20,YELLOW,1.6),(300,GREEN,1.4),(20000,PURPLE,1.3)]:
    ax.semilogy(ks,[max(est(K,int(k)),1e-12) for k in ks],color=c,lw=lw)
ax.text(29,3.2,'$K=20$',color=YELLOW,fontsize=7.5); ax.text(29,.003,'$K=300$',color=GREEN,fontsize=7.5); ax.text(17,8e-7,'$K=20000$',color=PURPLE,fontsize=7.5)
clean(ax,(1,40),(1e-9,30),'共轭梯度步数 k',None); tag(ax,'(b)',-.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'seed':3,'x':x})
