from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# EI（0.1 网格）与均匀随机搜索，200 组随机初始 3 点，同一目标，T=15；终端误差的中位数（实线）与累积损失。
xs=np.linspace(0,8,81);fine=np.linspace(0,8,8001);fstar=f(fine).min();T=15;rng=np.random.default_rng(29)
Rb=[];Rr=[];Cb=[];Cr=[]
for _ in range(200):
    X=list(rng.choice(xs,3,replace=False));Z=list(rng.choice(xs,T,replace=True))
    X0=X[:]
    while len(X)<T:
        A=np.array(X);Y=f(A);m,v=posterior(A,Y,xs);E_=ei(Y.min(),m,np.sqrt(v));X.append(xs[E_.argmax()])
    Y=f(np.array(X));Rb.append(np.minimum.accumulate(Y)-fstar);Cb.append(np.cumsum(Y-fstar))
    Y2=f(np.array(X0+Z[3:]));Rr.append(np.minimum.accumulate(Y2)-fstar);Cr.append(np.cumsum(Y2-fstar))
Rb,Rr,Cb,Cr=[np.array(z) for z in (Rb,Rr,Cb,Cr)]
t=np.arange(1,T+1)
fig,(a,b)=figure(width_mm=112,height_mm=48,ncols=2)
a.plot(t,np.mean(Rb,axis=0),color=GREEN,lw=1.4);a.plot(t,np.mean(Rr,axis=0),color=YELLOW,lw=1.4)
a.text(8.2,.06,'贝叶斯优化',color=GREEN);a.text(7.5,.58,'随机搜索',color=YELLOW)
a.set_xlim(1,T);a.set_ylim(0,None);axes_style(a,'评价次数','平均简单误差')
b.plot(t,np.mean(Cb,axis=0),color=GREEN,lw=1.4);b.plot(t,np.mean(Cr,axis=0),color=YELLOW,lw=1.4)
b.set_xlim(1,T);b.set_ylim(0,None);axes_style(b,'评价次数','平均累积损失')
panel_label(a,'(a)',-.32);panel_label(b,'(b)',-.32)
print('simple last',Rb.mean(0)[-1],Rr.mean(0)[-1],'cum last',Cb.mean(0)[-1],Cr.mean(0)[-1])
FACTS={'T':T,'seeds':200,'fstar':float(fstar)}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
