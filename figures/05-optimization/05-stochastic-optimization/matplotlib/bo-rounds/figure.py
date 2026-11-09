from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 整数候选上连续三轮 EI 选点。
xo=list(RUN_X[:3]);fig,axs=figure(width_mm=112,height_mm=66,nrows=2,ncols=3,sharex=True,gridspec_kw=dict(height_ratios=[1.6,1]))
info=[]
for r in range(3):
    X=np.array(xo);Y=f(X);b0=Y.min();m,s2=posterior(X,Y,XG);s=np.sqrt(s2);mc,s2c=posterior(X,Y,C);Ec=ei(b0,mc,np.sqrt(s2c));nx=C[Ec.argmax()]
    a=axs[0,r];band(a,XG,m,s);a.plot(XG,m,color=INK,lw=1.0,zorder=3);a.plot(XG,f(XG),color=BLUE,lw=1.2,zorder=2);a.axhline(b0,color=STROKE,lw=.8,ls=':');obs(a,X,Y);a.axvline(nx,color=GREEN,lw=.85,ls='--',zorder=1)
    a.set_ylim(-2.4,2.4);axes_style(a,None,'后验' if r==0 else None)
    b=axs[1,r];b.plot(XG,ei(b0,m,s),color=GREEN,lw=1.3);b.scatter(C,Ec,s=9,color=GREEN,zorder=5,lw=0,clip_on=False);b.axvline(nx,color=GREEN,lw=.85,ls='--')
    b.set_xlim(0,8);b.set_xticks(range(0,9,2));b.set_ylim(0,.42);axes_style(b,'$x$','EI' if r==0 else None)
    panel_label(b,'(%s)'%'abc'[r],-.5)
    info.append(float(nx));xo.append(float(nx))
FACTS={'next_points':info}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
