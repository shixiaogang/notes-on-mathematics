from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# g=y^4/4-x*y, unique global minimizer y*=x^(1/3), H=3y^2 vanishes at x=0.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
y = np.linspace(-1.5,1.7,300)
ax = axs[0]
for xv,c,ls in [(0,BLUE,'-'),(1,BLUE,'--')]:
    ax.plot(y,y**4/4-xv*y,color=c,lw=1.3,ls=ls)
    yy = np.cbrt(xv); ax.plot([yy],[yy**4/4-xv*yy],'o',color=RED,ms=4,zorder=6)
ax.text(-1.32,.85,'$x=0$',color=BLUE,fontsize=7.5); ax.text(-.5,1.0,'$x=1$',color=BLUE,fontsize=7.5)
clean(ax,(-1.5,1.7),(-1,1.7),'$y$','$g(x,y)$'); tag(ax,'(a)',-.3)
ax = axs[1]
x = np.linspace(-1,1,801)
ax.plot(x,np.cbrt(x),color=ACTIVE,lw=1.8)
ax.plot([0],[0],'o',color=RED,ms=4.2,zorder=6)
ax.text(.3,.45,r'$y^*=x^{1/3}$',color=ACTIVE)
clean(ax,(-1,1),(-1.15,1.15),'$x$','$y$'); tag(ax,'(b)',-.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'g':'y^4/4-xy'})
