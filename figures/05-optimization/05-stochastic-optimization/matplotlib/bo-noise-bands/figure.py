from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 独立高斯噪声 tau=0.3，五个读数（固定种子）。
tau=.3;rng=np.random.default_rng(9);xo=np.array([1.,2.,4.,6.,7.]);yo=f(xo)+tau*rng.standard_normal(5)
m,v=posterior(xo,yo,XG,tau2=tau*tau);s=np.sqrt(v);sp=np.sqrt(v+tau*tau)
fig,ax=figure(width_mm=100,height_mm=46)
band(ax,XG,m,s);ax.plot(XG,m+2*sp,color=PURPLE,lw=.9,ls='--');ax.plot(XG,m-2*sp,color=PURPLE,lw=.9,ls='--')
ax.plot(XG,m,color=INK,lw=1.0,zorder=3);ax.plot(XG,f(XG),color=BLUE,lw=1.3,zorder=2)
ax.errorbar(xo,yo,yerr=None,fmt='none');obs(ax,xo,yo)
ax.set_xlim(0,8);ax.set_xticks(range(9));ax.set_ylim(-2.6,2.6);axes_style(ax,'$x$','函数值')
print('y',np.round(yo,3))
FACTS={'tau':tau,'seed':9,'y':yo.tolist()}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
