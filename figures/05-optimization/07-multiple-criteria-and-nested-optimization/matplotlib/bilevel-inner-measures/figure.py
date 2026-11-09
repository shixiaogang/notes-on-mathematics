from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
fig, axs = figure(width_mm=112, height_mm=54, ncols=2, sharey=True)
d=np.logspace(-3,0,60)
for ax,(r,g,t,lr,lg) in zip(axs,[(d,.5*d**2,'(a)',(.05,.1),(.05,1.5e-4)),(d**3,.25*d**4,'(b)',(.08,1.7e-5),(.15,4e-7))]):
    ax.loglog(d,d,color=GREEN,lw=1.4); ax.loglog(d,r,color=PURPLE,lw=1.4,ls='--'); ax.loglog(d,g,color=BLUE,lw=1.4)
    clean(ax,(1e-3,1),(1e-10,3),'到解的距离 d',None); ax.set_yticks([1e-9,1e-6,1e-3,1]); tag(ax,t,-.28)
axs[0].set_ylabel('误差度量',labelpad=1.5)
axs[0].text(.012,.6e-3,'$\\delta$',color=BLUE); axs[0].text(.012,.04,'$d=r$',color=PURPLE,fontsize=7.5)
axs[1].text(.03,.09,'$d$',color=GREEN); axs[1].text(.03,1.2e-3,'$r$',color=PURPLE); axs[1].text(.3,1.5e-5,r'$\delta$',color=BLUE)
save(fig, Path(__file__).resolve().parent, 'figure', {'a':'g=y^2/2','b':'g=y^4/4'})
