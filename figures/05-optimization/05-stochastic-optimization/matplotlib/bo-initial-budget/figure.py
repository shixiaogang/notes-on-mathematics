from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 预算 T=8，初始点数 n0 从 1 到 8；每个 n0 用 300 组种子的均匀随机初始点（网格 0.1）。
xs=np.linspace(0,8,81);fstar=f(np.linspace(0,8,8001)).min();rng=np.random.default_rng(11)
T=8;res={}
for n0 in range(1,T+1):
    vals=[]
    for _ in range(300):
        X=list(rng.choice(xs,n0,replace=False))
        while len(X)<T:
            A=np.array(X);Y=f(A);m,v=posterior(A,Y,xs);E_=ei(Y.min(),m,np.sqrt(v));X.append(xs[E_.argmax()])
        vals.append(f(np.array(X)).min()-fstar)
    res[n0]=(np.mean(vals),np.mean(np.array(vals)<.1))
ns=np.array(list(res));mean=np.array([res[n][0] for n in ns]);hit=np.array([res[n][1] for n in ns])
print('n0 mean hit',np.round(mean,3),np.round(hit,3))
fig,ax=figure(width_mm=88,height_mm=44)
ax.plot(ns,mean,color=GREEN,lw=1.4,marker='o',ms=3.2)
ax.set_xlim(.7,8.3);ax.set_ylim(0,mean.max()*1.15);ax.set_xticks(ns);axes_style(ax,'初始点数','平均终端误差')
FACTS={'T':T,'seeds':300,'mean_final_gap':mean.tolist(),'hit_rate_gap_below_0.1':hit.tolist()}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
