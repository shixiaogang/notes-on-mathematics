from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 三次读数后的各采集函数。
xo=np.array(RUN_X[:3]);yo=f(xo);b0=yo.min()
m,s2=posterior(xo,yo,XG);s=np.sqrt(s2)
fig,axs=figure(width_mm=105,height_mm=88,nrows=4,sharex=True,gridspec_kw=dict(height_ratios=[1.35,1,1,1.15]))
a=axs[0];band(a,XG,m,s);a.plot(XG,m,color=INK,lw=1.0,zorder=3);a.axhline(b0,color=STROKE,lw=.85,ls=':');obs(a,xo,yo)
a.text(.05,b0-.15,'$b_3$',va='top',color=INK);a.set_ylim(-2.3,2.5);axes_style(a,None,'后验')
a=axs[1];p0=pi(b0,m,s);p1=pi(b0,m,s,xi=.3);a.plot(XG,p0,color=YELLOW,lw=1.4);a.plot(XG,p1,color=PURPLE,lw=1.2,ls='--')
a.text(5.0,.34,'$\\xi=0$',color=YELLOW);a.text(3.62,.09,'$\\xi=0.3$',color=PURPLE);a.set_ylim(0,.58);axes_style(a,None,'PI')
a=axs[2];E=ei(b0,m,s);a.plot(XG,E,color=GREEN,lw=1.4);a.set_ylim(0,.36);axes_style(a,None,'EI')
g=XG[E.argmax()];a.scatter([g],[E.max()],s=14,color=GREEN,zorder=5,lw=0)
a=axs[3]
for kp,c,ls,yt in [(1.,YELLOW,'-',.0),(3.,PURPLE,'--',-1.)]:
    l=m-kp*s;a.plot(XG,l,color=c,lw=1.3,ls=ls)
a.text(1.9,-.3,'$\\kappa=1$',color=YELLOW);a.text(1.9,-2.25,'$\\kappa=3$',color=PURPLE);a.set_ylim(-3.1,1.0);a.set_xlim(0,8);a.set_xticks(range(9));axes_style(a,'$x$','LCB')
FACTS={'b':float(b0),'argmax_EI':float(g)}
print('EI max',g,E.max(),'PI argmax',XG[p0.argmax()],p0.max(),'PI .3 argmax',XG[p1.argmax()],p1.max(),'LCB1',XG[(m-s).argmin()],'LCB3',XG[(m-3*s).argmin()])
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
