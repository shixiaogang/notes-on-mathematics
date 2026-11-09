from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 单位方形上 9 点：均匀随机、拉丁超立方、规则网格。
rng=np.random.default_rng(7);n=9
rand=rng.random((n,2))
lhs=np.column_stack([(rng.permutation(n)+rng.random(n))/n,(rng.permutation(n)+rng.random(n))/n])
g=(np.arange(3)+.5)/3;grid=np.array([(a,b) for a in g for b in g])
fig,axs=figure(width_mm=112,height_mm=47,ncols=3,sharey=True)
for i,(ax,P) in enumerate(zip(axs,[rand,lhs,grid])):
    ax.scatter(P[:,0],P[:,1],s=12,color=GREEN,lw=0,zorder=3)
    ax.plot(P[:,0],np.zeros(n)-.0,'|',color=INK,ms=5,mew=.7,clip_on=False,zorder=4);ax.plot(np.zeros(n)-.0,P[:,1],'_',color=INK,ms=5,mew=.7,clip_on=False,zorder=4)
    if i==1:
        for v in np.arange(1,n)/n: ax.axvline(v,color=GRID,lw=.65,zorder=1);ax.axhline(v,color=GRID,lw=.65,zorder=1)
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal',adjustable='box');ax.set_xticks([0,1]);ax.set_yticks([0,1]);axes_style(ax,'$x_1$','$x_2$' if i==0 else None);panel_label(ax,'(%s)'%'abc'[i],-.26)
FACTS={'seed':7,'n':9}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
