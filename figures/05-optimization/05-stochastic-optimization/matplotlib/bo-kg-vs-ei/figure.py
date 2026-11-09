from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 三次读数后的 EI 与 KG（无噪声观测），推荐集合为 0.1 网格，用等分位的 401 个 z 求期望。
xs=np.linspace(0,8,81);xo=np.array(RUN_X[:3]);yo=f(xo);b0=yo.min()
m,S=posterior(xo,yo,xs,full=True);s=np.sqrt(np.maximum(np.diag(S),0))
us=(np.arange(401)+.5)/401;zs=np.array([norm_ppf(u) for u in us])
base=m.min();kg=np.zeros(81)
for i in range(81):
    if s[i]<1e-5: continue
    col=S[:,i]/s[i]
    kg[i]=base-np.mean(np.min(m[:,None]+col[:,None]*zs[None,:],axis=0))
E_=ei(b0,m,s)
fig,ax=figure(width_mm=100,height_mm=44)
ax.plot(xs,E_,color=YELLOW,lw=1.4,label='EI');ax.plot(xs,kg,color=GREEN,lw=1.4,label='KG')
ax.legend(loc='upper center',ncols=2,borderpad=0)
ax.set_xlim(0,8);ax.set_xticks(range(9));ax.set_ylim(0,.42);axes_style(ax,'$x$','采集分数')
print('min post mean',base,'KG max at',xs[kg.argmax()],kg.max(),'EI max at',xs[E_.argmax()],E_.max(),'KG(7)',kg[70],'EI(7)',E_[70])
FACTS={'kg_argmax':float(xs[kg.argmax()])}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
