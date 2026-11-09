from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 三种长度尺度：同一组标准正态向量产生的先验样本。
rng=np.random.default_rng(5)
ells=[('$\\ell=0.4$',0.16,YELLOW,'--'),('$\\ell=0.85$',1/(2*np.log(2)),BLUE,'-'),('$\\ell=2$',4.0,PURPLE,'-.')]
fig,(a,b)=figure(width_mm=112,height_mm=46,ncols=2,gridspec_kw=dict(width_ratios=[1,1.6]))
d=np.linspace(0,4,201)
for lab,l2,c,ls in ells: a.plot(d,np.exp(-d*d/(2*l2)),color=c,lw=1.4,ls=ls,label=lab)
a.legend(loc='upper right',handlelength=2.4,borderpad=0,labelspacing=.25)
a.set_xlim(0,4);a.set_ylim(0,1.05);axes_style(a,"$|x-x'|$","$k(x,x')$")
z=rng.standard_normal(len(XG))
for lab,l2,c,ls in ells:
    K=k(XG,XG,l2)+1e-6*np.eye(len(XG))
    b.plot(XG,np.linalg.cholesky(K)@z,color=c,lw=1.3,ls=ls)
b.set_xlim(0,8);b.set_xticks(range(9));axes_style(b,'$x$','$F(x)$')
panel_label(a,'(a)',-.38);panel_label(b,'(b)',-.38)
FACTS={'seed':5,'ell':[.4,float(np.sqrt(1/(2*np.log(2)))),2.]}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
