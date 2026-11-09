from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 同一组三个读数，两个候选长度尺度与按边缘似然加权的混合预测。
xo=np.array(RUN_X[:3]);yo=f(xo)
hyp=[(1/(2*np.log(2)),'a'),(9.0,'b')]
def logml(l2):
    K=k(xo,xo,l2)+1e-10*np.eye(3);L=np.linalg.cholesky(K);al=np.linalg.solve(L,yo)
    return -.5*al@al-np.log(np.diag(L)).sum()-1.5*np.log(2*np.pi)
lm=np.array([logml(h[0]) for h in hyp]);w_=np.exp(lm-lm.max());w_=w_/w_.sum()
res=[posterior(xo,yo,XG,ell2=h[0]) for h in hyp]
mm=sum(wi*r[0] for wi,r in zip(w_,res));vv=sum(wi*(r[1]+r[0]**2) for wi,r in zip(w_,res))-mm**2
fig,axs=figure(width_mm=112,height_mm=44,ncols=3,sharey=True)
D=[(res[0][0],res[0][1]),(res[1][0],res[1][1]),(mm,vv)]
for i,(ax,(m,v)) in enumerate(zip(axs,D)):
    s=np.sqrt(np.maximum(v,0));band(ax,XG,m,s);ax.plot(XG,m,color=INK,lw=1.0,zorder=3);ax.plot(XG,f(XG),color=BLUE,lw=1.2,zorder=2)
    obs(ax,xo,yo);ax.set_xlim(0,8);ax.set_xticks([0,2,4,6,8]);ax.set_ylim(-2.6,2.6)
    axes_style(ax,'$x$','函数值' if i==0 else None);panel_label(ax,'(%s)'%'abc'[i],-.32)
print('logml',lm,'weights',w_)
FACTS={'ell2':[h[0] for h in hyp],'log_marginal_likelihood':lm.tolist(),'weights':w_.tolist()}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
