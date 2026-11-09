from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 后验联合抽样与独立边际抽样，固定种子，网格 0.1。
xs=np.linspace(0,8,81);xo=np.array(RUN_X[:3]);yo=f(xo)
m,Sig=posterior(xo,yo,xs,full=True);L=np.linalg.cholesky(Sig+1e-8*np.eye(81));s=np.sqrt(np.maximum(np.diag(Sig),0))
rng=np.random.default_rng(3)
fig,axs=figure(width_mm=112,height_mm=48,ncols=2,sharey=True)
Z=rng.standard_normal(81)
joint=m+L@Z;ind=m+s*rng.standard_normal(81)
for i,(ax,y,c) in enumerate(zip(axs,[joint,ind],[GREEN,YELLOW])):
    band(ax,xs,m,s);ax.plot(xs,y,color=c,lw=1.1,zorder=3);ax.scatter([xs[y.argmin()]],[y.min()],s=20,color=RED,zorder=6,lw=0)
    obs(ax,xo,yo,zorder=5,color=INK,s=9);ax.set_xlim(0,8);ax.set_xticks(range(0,9,2));ax.set_ylim(-3.1,2.8);axes_style(ax,'$x$','函数值' if i==0 else None);panel_label(ax,'(%s)'%'ab'[i],-.3)
n=20000;Zs=rng.standard_normal((81,n));S=m[:,None]+L@Zs;arg=S.argmin(axis=0)
freq=np.array([np.mean(xs[arg].round()==v) for v in range(9)])
print('TS argmin rounded freq 0..8',np.round(freq,3))
FACTS={'seed':3,'argmin_freq_nearest_integer':freq.tolist()}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
