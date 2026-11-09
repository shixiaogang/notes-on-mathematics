from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 四次读数后在 0.25 网格上选两点：单点 EI 前二 vs 联合 qEI（公共随机数 40000）。
xs=np.linspace(0,8,33);xo=np.array(RUN_X[:4]);yo=f(xo);b0=yo.min()
m,S=posterior(xo,yo,xs,full=True);s=np.sqrt(np.maximum(np.diag(S),0));L=np.linalg.cholesky(S+1e-8*np.eye(33))
rng=np.random.default_rng(2);D=m[:,None]+L@rng.standard_normal((33,40000));E_=ei(b0,m,s)
order=np.argsort(-E_);top=order[:2]
def q(i,j): return np.mean(np.maximum(b0-np.minimum(D[i],D[j]),0))
Q=np.zeros((33,33))
for i in range(33):
    for j in range(i+1,33): Q[i,j]=Q[j,i]=q(i,j)
bi,bj=np.unravel_index(Q.argmax(),Q.shape)
fig,ax=figure(width_mm=100,height_mm=44)
ax.plot(xs,E_,color=BLUE,lw=1.4);ax.scatter(xs[top],E_[top],s=22,color=YELLOW,lw=0,zorder=5,marker='s');ax.scatter(xs[[bi,bj]],E_[[bi,bj]],s=20,color=GREEN,lw=0,zorder=6)
ax.set_xlim(0,8);ax.set_xticks(range(9));ax.set_ylim(0,E_.max()*1.2);axes_style(ax,'$x$','单点 EI')
print('top two',xs[top],E_[top],'qEI top',q(*top),'joint',xs[bi],xs[bj],Q.max(),'sum top EI',E_[top].sum())
FACTS={'top_two':xs[top].tolist(),'joint_pair':[float(xs[bi]),float(xs[bj])],'qEI_top_two':float(q(*top)),'qEI_joint':float(Q.max())}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
