from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 三个读数 x=1,4,7 下的后验抽样；固定种子。
rng = np.random.default_rng(16)
xo=np.array(RUN_X[:3]); yo=f(xo)
m,Sig=posterior(xo,yo,XG,full=True)
L=np.linalg.cholesky(Sig+1e-8*np.eye(len(XG)))
Z=rng.standard_normal((len(XG),5))
fig, ax = figure(width_mm=100, height_mm=48)
s=np.sqrt(np.maximum(np.diag(Sig),0))
band(ax,XG,m,s)
for j in range(5): ax.plot(XG,m+L@Z[:,j],color=PURPLE,lw=.75,zorder=2)
ax.plot(XG,f(XG),color=BLUE,lw=1.5,zorder=3)
obs(ax,xo,yo)
ax.set_xlim(0,8); ax.set_ylim(-2.6,2.6); ax.set_xticks(range(9))
axes_style(ax,'$x$','函数值')
FACTS={'seed':16,'kernel':'2^{-(x-x\')^2}','data':'x=1,4,7'}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
