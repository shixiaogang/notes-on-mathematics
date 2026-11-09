from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 目标 f 与约束 g(x)=(x-4.5)/4；同一核，读数 x=1,4,7。
xo=np.array(RUN_X[:3]);yo=f(xo);g_=(xo-4.5)/4;b0=yo[g_<=0].min()  # best feasible reading
m,v=posterior(xo,yo,XG);s=np.sqrt(v);mg,vg=posterior(xo,g_,XG);sg=np.sqrt(vg);pf=np.zeros_like(XG);pos=sg>1e-5;pf[pos]=Phi(-mg[pos]/sg[pos]);pf[~pos]=(mg[~pos]<=0)*1.;E_=ei(b0,m,s);cE=E_*pf
fig,axs=figure(width_mm=105,height_mm=86,nrows=3,sharex=True,gridspec_kw=dict(height_ratios=[1.2,1.2,1]))
a=axs[0];band(a,XG,m,s);a.plot(XG,m,color=INK,lw=1.0,zorder=3);a.plot(XG,f(XG),color=BLUE,lw=1.2,zorder=2);a.axhline(b0,color=STROKE,lw=.8,ls=':');obs(a,xo,yo);a.set_ylim(-2.4,2.4);axes_style(a,None,'目标')
a=axs[1];band(a,XG,mg,sg,fill=PURPLE_FILL);a.plot(XG,mg,color=INK,lw=1.0,zorder=3);a.plot(XG,(XG-4.5)/4,color=PURPLE,lw=1.2,zorder=2);a.axhline(0,color=STROKE,lw=1.3);obs(a,xo,g_);a.set_ylim(-2.4,2.4);axes_style(a,None,'约束')
a=axs[2];a.plot(XG,E_,color=YELLOW,lw=1.3,label='EI');a.plot(XG,cE,color=GREEN,lw=1.4,label='约束 EI');a.legend(loc='upper center',ncols=2,borderpad=0);a.set_xlim(0,8);a.set_xticks(range(9));a.set_ylim(0,.68);axes_style(a,'$x$','采集分数')
print('cEI argmax',XG[cE.argmax()],cE.max(),'EI argmax',XG[E_.argmax()],E_.max())
FACTS={'g':'(x-4.5)/4'}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
