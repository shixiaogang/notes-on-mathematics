from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 未完成点 xp=6：对假想结果积分（后验分位点 201 个）后的 EI。
xo=np.array(RUN_X[:3]);yo=f(xo);xp=6.0;b0=yo.min()
m,v=posterior(xo,yo,XG);s=np.sqrt(v);E0=ei(b0,m,s)
mp,sp2=posterior(xo,yo,[xp]);sp=float(np.sqrt(sp2[0]));mp=float(mp[0])
us=(np.arange(201)+.5)/201;zs=np.array([norm_ppf(u) for u in us]);Ef=np.zeros_like(XG)
for z in zs:
    yp=mp+sp*z;X=np.append(xo,xp);Y=np.append(yo,yp);m1,v1=posterior(X,Y,XG);Ef+=ei(min(b0,yp),m1,np.sqrt(v1))
Ef/=len(zs)
fig,ax=figure(width_mm=100,height_mm=44)
ax.plot(XG,E0,color=YELLOW,lw=1.3,label='未计入运行中的试验');ax.plot(XG,Ef,color=GREEN,lw=1.4,label='对假想结果平均')
ax.axvline(xp,color=MUTED,lw=.85,ls='--');ax.legend(loc='upper left',borderpad=0)
ax.set_xlim(0,8);ax.set_xticks(range(9));ax.set_ylim(0,.42);axes_style(ax,'$x$','采集分数')
print('E0 argmax',XG[E0.argmax()],'Ef argmax',XG[Ef.argmax()],Ef.max(),'E0(6)',float(E0[300]),'Ef(6)',float(Ef[300]),'mp sp',mp,sp)
FACTS={'pending':xp}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
