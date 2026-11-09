from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Riemannian trust region (tCG, theta=1) n=300, spectrum 1..100, starting radius 2.
n=300; a=np.linspace(1,100,n); rng=np.random.default_rng(5)
x=rng.normal(size=n); x/=np.linalg.norm(x); D=2.0
RHO=[];DEL=[];G=[];ST=[]
for t in range(200):
    Ax=a*x; q=x@Ax; g=Ax-q*x; ng=np.linalg.norm(g); G.append(ng); DEL.append(D)
    if ng<1e-8: break
    Hv=lambda v:(lambda w:w-(x@w)*x)(a*v-q*v)
    v,st,cnt=tcg(g,Hv,D,min(.1,ng))
    v-=(x@v)*x
    pred=-(g@v+.5*v@Hv(v)); y=retr(x,v); ared=.5*q-.5*y@(a*y); r=ared/pred
    RHO.append(r); ST.append(st)
    if r<.25: D/=4
    elif r>.75 and abs(np.linalg.norm(v)-D)<1e-9: D=min(2*D,np.pi)
    if r>=.25: x=y
print(len(G),G[-1],sum(r<.25 for r in RHO),[round(float(r),3) for r in RHO],[round(float(d),3) for d in DEL])
fig,axs=figure(width_mm=112,height_mm=48,ncols=2)
ax=axs[0]; tt=np.arange(len(RHO))
ax.axhline(.25,color=GRAY,lw=.85,ls='--'); ax.axhline(.75,color=GRAY,lw=.85,ls='--')
RH=np.clip(RHO,-1,1.5)
acc=np.array(RHO)>=.25
ax.plot(tt[acc],RH[acc],'o',ms=3.2,color=GREEN,label='接受'); ax.plot(tt[~acc],RH[~acc],'x',ms=4.2,color=RED,mew=1.2,label='拒绝')
ax.set_xlabel('外层迭代'+'\n(a)'); ax.set_ylabel(r'$\rho^{(t)}$'); ax.legend(handlelength=1,loc='center right')
ax=axs[1]
ax.semilogy(G,color=GREEN,lw=1.5,label=r'$\Vert\mathbf{g}^{(t)}\Vert_2$'); ax.semilogy(DEL,color=PURPLE,lw=1.4,drawstyle='steps-post',label=r'$\Delta^{(t)}$')
ax.set_xlabel('外层迭代'+'\n(b)'); ax.legend(handlelength=1.6)
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'RTR tCG theta=1, n=300, spectrum 1..100, seed 5, Delta0=2, reject rho<1/4'})
