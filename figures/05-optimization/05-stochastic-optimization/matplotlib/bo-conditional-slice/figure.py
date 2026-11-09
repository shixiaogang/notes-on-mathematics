from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# (F(3),F(4)) 联合高斯，相关系数 1/2；读数 F(3)=1 后 F(4)|F(3)=1 ~ N(1/2,3/4)。
fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2,gridspec_kw=dict(width_ratios=[1,1.15]))
u=np.linspace(-3,3,241); U,V=np.meshgrid(u,u); rho=.5
Q=(U*U-2*rho*U*V+V*V)/(1-rho*rho)
a.contour(U,V,Q,levels=[.4,1.2,2.4,4.2,6.5],colors=BLUE,linewidths=.8)
a.axvline(1,color=MUTED,lw=.85,ls='--')
xs=np.array([-2.6,2.6]); a.plot(xs,.5*xs,color=PURPLE,lw=1.0)
a.scatter([1],[.5],s=20,color=GREEN,zorder=5,lw=0)
a.text(1.12,-2.75,'$F(3)=1$',color=INK,fontsize=7.5,va='bottom',ha='left')
a.set_xlim(-3,3);a.set_ylim(-3,3);a.set_aspect('equal',adjustable='box')
axes_style(a,'$F(3)$','$F(4)$')
v=np.linspace(-3.5,3.5,281)
pr=np.exp(-v*v/2)/np.sqrt(2*np.pi); po=np.exp(-(v-.5)**2/(2*.75))/np.sqrt(2*np.pi*.75)
b.plot(v,pr,color=BLUE,lw=1.4,ls='--');b.plot(v,po,color=GREEN,lw=1.4)
b.text(-2.75,.2,'先验',color=BLUE);b.text(1.65,.3,'读数后',color=GREEN)
b.axvline(.5,color=MUTED,lw=.85,ls=':')
b.set_xlim(-3.5,3.5);b.set_ylim(0,.52);b.set_xticks([-2,0,.5,2]);b.set_xticklabels(['-2','0','0.5','2'])
axes_style(b,'$F(4)$','密度')
panel_label(a,'(a)',-.27);panel_label(b,'(b)',-.27)
FACTS={'rho':.5,'cond_mean':.5,'cond_var':.75}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
