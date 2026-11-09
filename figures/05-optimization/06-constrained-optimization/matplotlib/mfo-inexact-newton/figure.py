from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Newton-CG on the sphere with three forcing rules. n=500, spectrum 1..100, Armijo backtracking on the pullback.
n=500; a=np.linspace(1,100,n); rng=np.random.default_rng(3)
xs=rng.normal(size=n); xs[:10]*=40; xs/=np.linalg.norm(xs)
def ncg(g,Hv,eta):
    # Linear CG on the tangent system; stops at negative curvature (returns current iterate, or -g at first step).
    v=0*g; r=g.copy(); d=-r; r0=np.linalg.norm(r); cnt=0
    for j in range(2000):
        Hd=Hv(d); cnt+=1; dHd=d@Hd
        if dHd<=1e-14*(d@d):
            return (d if j==0 else v),cnt
        a=(r@r)/dHd; v=v+a*d; rn=r+a*Hd
        if np.linalg.norm(rn)<=eta*r0: return v,cnt
        d=-rn+(rn@rn)/(r@r)*d; r=rn
    return v,cnt
def run(rule,T=60):
    x=xs.copy(); H=[];C=[];c=0
    for t in range(T):
        Ax=a*x; q=x@Ax; g=Ax-q*x; ng=np.linalg.norm(g); H.append(ng); C.append(c)
        if ng<1e-10: break
        Hv=lambda v:(lambda w:w-(x@w)*x)(a*v-q*v)
        v,cnt=ncg(g,Hv,rule(ng)); c+=cnt
        v-=(x@v)*x
        al=1.; f0=.5*q; gv=g@v
        while True:
            y=retr(x,al*v)
            if .5*y@(a*y)<=f0+1e-4*al*gv or al<1e-12: break
            al/=2
        x=y
    return np.array(H),np.array(C)
fig,axs=figure(width_mm=112,height_mm=48,ncols=2,sharey=True)
for rule,c,nm in [(lambda g:.5,YELLOW,r'$\eta=0.5$'),(lambda g:min(.5,g**.5),PURPLE,r'$\eta=\Vert\mathbf{g}\Vert_2^{1/2}$'),(lambda g:min(.5,g),GREEN,r'$\eta=\Vert\mathbf{g}\Vert_2$')]:
    H,C=run(rule); print(nm,len(H),C[-1],H[-1])
    axs[0].semilogy(H,'-o',color=c,lw=1.4,ms=2.6,label=nm); axs[1].semilogy(C,H,'-o',color=c,lw=1.4,ms=2.6)
axs[0].set_xlabel('外层迭代\n(a)'); axs[0].set_ylabel(r'$\Vert\mathbf{g}^{(t)}\Vert_2$'); axs[0].legend(handlelength=1.8)
axs[1].set_xlabel('累计 Hessian-向量乘积\n(b)')
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'tCG forcing rules, n=500, spectrum 1..100, seed 3'})
