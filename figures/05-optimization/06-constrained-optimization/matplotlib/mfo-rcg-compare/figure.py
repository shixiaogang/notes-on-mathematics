from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Rayleigh minimisation, n=200, A=diag(linspace(1,100)), exact pullback line search, projection transport.
n=200; a=np.linspace(1,100,n); rng=np.random.default_rng(1)
xs=rng.normal(size=n); xs/=np.linalg.norm(xs)
Af=lambda v:a*v
def rg(x):
    Ax=Af(x); return Ax-(x@Ax)*x
def run(kind,T=350):
    x=xs.copy(); g=rg(x); d=-g; hist=[np.linalg.norm(g)]; restarts=0
    for t in range(T):
        if g@d>=0: d=-g; restarts+=1
        al=sphere_exact_step(x,Af(x),d,Af(d))
        y=retr(x,al*d); gn=rg(y)
        Tg=g-(y@g)*y; Td=d-(y@d)*y
        if kind=='sd': b=0.
        elif kind=='fr': b=gn@gn/(g@g)
        else: b=max(0,gn@(gn-Tg)/(g@g))
        d=-gn+b*Td; d-= (y@d)*y; x,g=y,gn; hist.append(np.linalg.norm(g))
        if hist[-1]<1e-6: break
    return np.array(hist),restarts
fig,ax=figure(width_mm=100,height_mm=52)
for k,c,nm,lw in [('pr',GREEN,'PR+',1.6),('fr',PURPLE,'FR',1.4),('sd',YELLOW,'最速下降',1.5)]:
    h,r=run(k); print(k,len(h),h[-1],r)
    ax.semilogy(h,color=c,lw=lw,label=nm)
ax.set_xlabel('迭代次数'); ax.set_ylabel(r'$\Vert\mathbf{g}^{(t)}\Vert_2$'); ax.legend(handlelength=1.8)
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'n=200, spectrum 1..100, seed 1, exact pullback line search, projection transport'})
