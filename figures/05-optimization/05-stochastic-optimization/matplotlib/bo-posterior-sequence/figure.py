from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
fig,axs=figure(width_mm=112,height_mm=44,ncols=3,sharey=True)
xo=np.array(RUN_X[:3]);yo=f(xo)
for n,ax in enumerate(axs,1):
    m,s2=posterior(xo[:n],yo[:n],XG);s=np.sqrt(s2)
    band(ax,XG,m,s); ax.plot(XG,m,color=INK,lw=1.0,zorder=3); ax.plot(XG,f(XG),color=BLUE,lw=1.2,zorder=2)
    obs(ax,xo[:n],yo[:n]); ax.set_xlim(0,8);ax.set_xticks([0,2,4,6,8]);ax.set_ylim(-2.4,2.4)
    axes_style(ax,'$x$','函数值' if n==1 else None)
    panel_label(ax,'(%s)'%'abc'[n-1],-.32)
FACTS={'band':'m +/- 2s'}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
