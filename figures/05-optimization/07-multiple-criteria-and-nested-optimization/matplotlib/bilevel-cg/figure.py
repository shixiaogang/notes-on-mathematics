from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# H=Q diag(logspace(log10(1/kappa),0,d)) Q^T, d=60, seed 7; B random unit, gradF random unit; CG from 0.
rng=np.random.default_rng(7); d=60
fig, ax = figure(width_mm=100, height_mm=58)
Q,_=np.linalg.qr(rng.normal(size=(d,d))); b=rng.normal(size=d); f=rng.normal(size=d); b/=np.linalg.norm(b); f/=np.linalg.norm(f)
for kap,c,lab in [(10,GREEN,0),(1000,YELLOW,1)]:
    H=Q@np.diag(np.logspace(-np.log10(kap),0,d))@Q.T
    vs=np.linalg.solve(H,f); tr=-b@vs
    v=np.zeros(d); r=f-H@v; p=r.copy(); R=[np.linalg.norm(r)]; E=[abs(-b@v-tr)]
    for k in range(60):
        Hp=H@p; a=(r@r)/(p@Hp); v=v+a*p; r2=r-a*Hp; p=r2+(r2@r2)/(r@r)*p; r=r2
        R.append(np.linalg.norm(r)); E.append(abs(-b@v-tr))
    ks=np.arange(61)
    ax.semilogy(ks,R,color=c,lw=1.5); ax.semilogy(ks,E,color=c,lw=1.2,ls='--')
    print(kap,R[0],E[0],R[10],E[10],R[30],E[30])
ax.text(14,3e-3,r'$\kappa=10$',color=GREEN,fontsize=7.5); ax.text(42,3e-1,r'$\kappa=1000$',color=YELLOW,fontsize=7.5)
clean(ax,(0,60),(1e-8,3e2),'共轭梯度步数 k','误差')
save(fig, Path(__file__).resolve().parent, 'figure', {'d':d,'seed':7})
