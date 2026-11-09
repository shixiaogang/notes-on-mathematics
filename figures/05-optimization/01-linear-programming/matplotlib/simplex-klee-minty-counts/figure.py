from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import simplex,klee_minty
Ns=range(1,11);D=[];B_=[]
for n in Ns:
    a,b,c,B=klee_minty(n)
    st,tr,_=simplex(a,b,c,B,max_rounds=2**n+2);D.append(len(tr)-1)
    st2,tr2,_=simplex(a,b,c,B,'bland',max_rounds=2**n+2);B_.append(len(tr2)-1)
a,b,c,B=klee_minty(5);st,tr,_=simplex(a,b,c,B,max_rounds=40)
fig,axs=figure(width_mm=112,height_mm=54,ncols=2)
ax=axs[0];ax.semilogy(list(Ns),D,'-o',color=GREEN,lw=1.4,ms=3.2);ax.semilogy(list(Ns),B_,'-o',color=YELLOW,lw=1.6,ms=3.2)
ax.text(7.4,D[6]*2.6,'Dantzig',fontsize=7.5,color=INK,ha='right');ax.text(7.7,B_[6]*.42,'Bland',fontsize=7.5,color=INK)
ax.set_xticks(range(2,11,2));ax.set_xlabel('$n$\n(a)',labelpad=1);ax.set_ylabel('换基次数',labelpad=1)
ax=axs[1];z=[-float(t['f']) for t in tr];ax.plot(range(len(z)),z,'-o',color=GREEN,lw=1.4,ms=2.8);opt_point(ax,(len(z)-1,z[-1]))
ax.set_xlabel('$t$\n(b)',labelpad=1);ax.set_ylabel('$z$',labelpad=1);ax.set_xticks(range(0,32,10))
save(fig,Path(__file__).resolve().parent,'figure',{'n':list(Ns),'dantzig':D,'bland':B_})
print(D,B_)
