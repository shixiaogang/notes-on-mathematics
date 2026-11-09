from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# Inner g=0.5(y-3)^2+0.5*x*y^2; outer F=0.5(y-1)^2; reaction curve y*=3/(1+x).
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax = axs[0]
X, Y = np.meshgrid(np.linspace(0,5,300), np.linspace(0,3.6,300))
G = .5*(Y-3)**2+.5*X*Y**2
ax.contour(X, Y, G, levels=[.5,1.5,3,4.5,7,10], colors=BLUE, linewidths=.6)
x = np.linspace(0,5,200)
ax.plot(x, ystar(x), color=ACTIVE, lw=1.8)
ax.axhline(1, color=MUTED, lw=.85, ls='--')
ax.plot([0],[3],'o',mfc='white',mec=BLUE,ms=4,mew=.9,clip_on=False,zorder=5)
ax.plot([2],[1],'o',color=RED,ms=4.2,zorder=6)
ax.text(3.9,.2,r'$y^*(x)$',color=ACTIVE); ax.text(4.25,.8,'$y=1$',color=MUTED,fontsize=7.5)
clean(ax,(0,5),(0,3.6),'$x$','$y$'); tag(ax,'(a)',-.27)
ax = axs[1]
ax.plot(x, Phi(x), color=BLUE, lw=1.4)
ax.plot([2],[0],'o',color=RED,ms=4.2,zorder=6,clip_on=False)
ax.text(.75,1.4,r'$\Phi(x)$',color=BLUE)
clean(ax,(0,5),(0,2.1),'$x$',None); tag(ax,'(b)',-.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'g':'0.5(y-3)^2+0.5xy^2','F':'0.5(y-1)^2'})
