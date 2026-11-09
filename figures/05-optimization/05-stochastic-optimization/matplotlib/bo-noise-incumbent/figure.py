from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 含噪读数：最低读数不是最低潜在值；比较以最低读数/最小后验均值为阈值的 EI 与 NEI（蒙特卡罗）。
tau=.3;xo=np.array([1.,2.,3.,5.,6.,7.]);rng=np.random.default_rng(23);eps=np.array([-.05,-.45,.1,-.7,.45,.15])*1.
yo=f(xo)+eps
xs=np.linspace(0,8,81)
m,v=posterior(xo,yo,xs,tau2=tau*tau);s=np.sqrt(v);mo,So=posterior(xo,yo,xo,tau2=tau*tau,full=True)
allx=np.concatenate([xo,xs]);mf,Sf=posterior(xo,yo,allx,tau2=tau*tau,full=True);n=len(allx);L=np.linalg.cholesky(Sf+1e-8*np.eye(n))
S=mf[:,None]+L@rng.standard_normal((n,40000));best=S[:6].min(axis=0);nei=np.mean(np.maximum(best[None,:]-S[6:],0),axis=1)
fig,(a,b)=figure(width_mm=105,height_mm=74,nrows=2,sharex=True,gridspec_kw=dict(height_ratios=[1.2,1]))
band(a,xs,m,s);a.plot(xs,m,color=INK,lw=1.0,zorder=3);a.plot(xs,f(xs),color=BLUE,lw=1.3,zorder=2);obs(a,xo,yo)
i=yo.argmin();a.scatter([xo[i]],[yo[i]],s=24,facecolors='none',edgecolors=RED,lw=1,zorder=6);a.axhline(yo.min(),color=STROKE,lw=.8,ls=':')
a.set_ylim(-2.2,2.0);axes_style(a,None,'函数值')
E1=ei(yo.min(),m,s);E2=ei(mo.min(),m,s)
b.plot(xs,E1,color=YELLOW,lw=1.3,ls='-',label='阈值为最低读数');b.plot(xs,E2,color=PURPLE,lw=1.2,ls='--',label='阈值为最小后验均值');b.plot(xs,nei,color=GREEN,lw=1.4,label='NEI')
b.legend(loc='upper left',borderpad=0,labelspacing=.25);b.set_xlim(0,8);b.set_xticks(range(9));b.set_ylim(0,max(nei.max(),E2.max())*1.55);axes_style(b,'$x$','采集分数')
print('y',np.round(yo,3),'argmin y at',xo[i],'f there',f(xo[i]),'mo',np.round(mo,3),'NEI argmax',xs[nei.argmax()],'E1',xs[E1.argmax()],E1.max(),'E2',xs[E2.argmax()],E2.max(),'nei max',nei.max())
FACTS={'tau':tau,'eps':eps.tolist(),'seed':23}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
