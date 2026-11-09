from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
fig, axs = figure(width_mm=112, height_mm=58, ncols=2)
x = np.linspace(0,3,400)
S = [(1,YELLOW,'-',1.5),(2,GREEN,'-',1.4),(4,PURPLE,'-',1.2)]
ax = axs[0]
for T,c,ls,lw in S: ax.plot(x,yT(x,T),color=c,lw=lw,ls=ls)
ax.plot(x,ystar(x),color=BLUE,lw=1.5)
ax.axhline(1,color=MUTED,lw=.85,ls='--')
ax.text(2.4,1.62,'$T=1$',color=YELLOW,fontsize=7.5); ax.text(.08,1.68,'$T=2$',color=GREEN,fontsize=7.5)
ax.text(.28,3.0,'$T=4$',color=PURPLE,fontsize=7.5); ax.text(2.6,.62,r'$y^*$',color=BLUE)
clean(ax,(0,3),(.4,3.3),'$x$','内层输出'); ax.set_xticks([0,1,2,3]); tag(ax,'(a)',-.26)
ax = axs[1]
for T,c,ls,lw in S: ax.plot(x,.5*(yT(x,T)-1)**2,color=c,lw=lw,ls=ls)
ax.plot(x,Phi(x),color=BLUE,lw=1.5)
ax.plot([5/3],[0],'o',color=GREEN,ms=4,zorder=6,clip_on=False)
ax.plot([2],[0],'o',color=RED,ms=4,zorder=7,clip_on=False)
ax.text(.05,.21,r'$\Phi_1$',color=YELLOW,fontsize=7.5); ax.text(.03,.56,r'$\Phi_2$',color=GREEN,fontsize=7.5)
ax.text(.72,.03+.42,r'$\Phi$',color=BLUE,fontsize=8); ax.text(.13,1.62,r'$\Phi_4$',color=PURPLE,fontsize=7.5)
clean(ax,(0,3),(0,2.15),'$x$','外层值'); ax.set_xticks([0,1,2,3]); tag(ax,'(b)',-.26)
save(fig, Path(__file__).resolve().parent, 'figure', {'alpha':.5,'y0':0,'T':[1,2,4]})
