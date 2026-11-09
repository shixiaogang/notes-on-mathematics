from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# x=0: y^(T)=3(1-2^-T), D^(T)=-3+3(T+1)2^-T; truncated reverse with T=20.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
def run(T,ell=None,x=0.,al=.5):
    y=[0.]
    for t in range(T): y.append(y[-1]-al*((1+x)*y[-1]-3))
    q=y[-1]-1; h=0.
    for t in range(T-1,-1,-1):
        if ell is not None and t<T-ell: break
        h+=-al*y[t]*q; q*=1-al*(1+x)
    return h
ax=axs[0]
Ts=np.arange(1,26)
err=np.abs(-3+3*(Ts+1)*.5**Ts-(-3))
ax.semilogy(Ts,err,color=GREEN,lw=1.4,marker='o',ms=2.4)
ax.semilogy(Ts,.5**Ts*Ts*6,color=MUTED,lw=.85,ls='--')
ax.text(9.5,.45,r'$T\rho^{T}$',color=MUTED,fontsize=7.5)
clean(ax,(0,25),(1e-7,10),'$T$',r'$|D^{(T)}-D^*|$'); tag(ax,'(a)',-.27)
ax=axs[1]
L=np.arange(1,13)
ax.plot(L,[run(int(l)) for l in L],color=YELLOW,lw=1.6,marker='o',ms=2.6)
ax.plot(L,[run(20,int(l)) for l in L],color=GREEN,lw=1.4,marker='o',ms=2.6)
ax.axhline(-6,color=BLUE,lw=1,ls='--')
ax.text(5.3,-1.75,'少跑步数',color=YELLOW,fontsize=7.5); ax.text(1.2,-6.65,'只截短反传',color=GREEN,fontsize=7.5,va='center')
ax.text(8,-6.5,'隐式导数 -6',color=BLUE,fontsize=7.5,va='center')
clean(ax,(1,12),(-7.2,.6),r'$\ell$','导数值'); tag(ax,'(b)',-.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'x':0,'alpha':.5})
print([run(T) for T in (1,2,3,20)],[run(20,l) for l in (1,2,3)])
