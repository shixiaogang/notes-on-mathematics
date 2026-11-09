from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 保守可行：g(x)=(x-4.5)/4，beta=2，把上界 u=m+2s<=0 的点视为安全；每轮评价安全集右端点。
fig,axs=figure(width_mm=112,height_mm=46,ncols=3,sharey=True)
X=[1.0];hist=[]
for r in range(3):
    ax=axs[r];A=np.array(X);G=(A-4.5)/4;m,v=posterior(A,G,XG);s=np.sqrt(v);u=m+2*s;safe=u<=0
    band(ax,XG,m,s,fill=PURPLE_FILL);ax.plot(XG,u,color=PURPLE,lw=1.2);ax.plot(XG,(XG-4.5)/4,color=BLUE,lw=1.2,zorder=2);ax.axhline(0,color=STROKE,lw=1.3);obs(ax,A,G)
    ax.plot(XG[safe],np.full(safe.sum(),-2.25),color=GREEN,lw=3,solid_capstyle='butt');ax.set_xlim(0,5.2);ax.set_ylim(-2.5,2.3);ax.set_xticks([0,2,4]);axes_style(ax,'$x$','$g$' if r==0 else None);panel_label(ax,'(%s)'%'abc'[r],-.32)
    hist.append((float(XG[safe].min()),float(XG[safe].max())));X.append(float(XG[safe].max()))
print(hist,X)
FACTS={'safe_intervals':hist,'queries':X,'beta':2}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
