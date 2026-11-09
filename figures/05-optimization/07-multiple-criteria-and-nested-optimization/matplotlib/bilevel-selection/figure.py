from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# x in [-1,1], Y=[-1,1], g=x*y, F=x^2+y. S(x)={-sign x}, S(0)=[-1,1].
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
ax = axs[0]
ax.axhspan(-1,1,facecolor=BLUE_FILL,edgecolor='none',zorder=0)
ax.plot([-1,0],[1,1],color=ACTIVE,lw=1.8); ax.plot([0,1],[-1,-1],color=ACTIVE,lw=1.8); ax.plot([0,0],[-1,1],color=ACTIVE,lw=1.8)
ax.text(-.72,.62,'$y=1$',color=INK); ax.text(.3,-.78,'$y=-1$',color=INK)
ax.text(.06,.05,r'$S(0)=[-1,1]$',color=INK,fontsize=7.5)
clean(ax,(-1,1),(-1.25,1.25),'$x$','$y$'); ax.set_yticks([-1,0,1]); tag(ax,'(a)',-.27)
ax = axs[1]
a = np.linspace(-1,-.0,100); b = np.linspace(0,1,100)
ax.plot(a,a**2+1,color=BLUE,lw=1.4); ax.plot(b,b**2-1,color=BLUE,lw=1.4)
ax.plot([0],[1],'o',color=YELLOW,ms=4.6,zorder=6)
ax.plot([0],[-1],'o',color=RED,ms=4.6,zorder=6)
ax.plot([0],[.3],'o',color=GREEN,ms=4.2,zorder=6)
ax.text(.07,1.0,r'$\Phi_{\mathrm{p}}(0)=1$',color=INK,fontsize=7.5,va='center')
ax.text(.07,-1.17,r'$\Phi_{\mathrm{o}}(0)=-1$',color=INK,fontsize=7.5,va='center')
ax.text(.07,.3,r'$F(0,y^{(0)})$',color=INK,fontsize=7.5,va='center')
clean(ax,(-1,1),(-1.45,2.15),'$x$',None); ax.set_yticks([-1,0,1,2]); tag(ax,'(b)',-.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'g':'xy','F':'x^2+y','y0':.3})
