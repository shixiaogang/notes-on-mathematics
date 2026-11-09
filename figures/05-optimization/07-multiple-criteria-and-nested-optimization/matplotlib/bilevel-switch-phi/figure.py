from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# F=.5(y-.5)^2. Phi_+=.5(x+.5)^2, Phi_-=.5(x-1.5)^2. Warm-started outer GD along + branch, eta=.3, x0=.8.
fig, ax = figure(width_mm=100, height_mm=56)
Pp = lambda x: .5*(x+.5)**2; Pm = lambda x: .5*(x-1.5)**2
a = np.linspace(0,1.2,100); b=np.linspace(-1,0,100)
ax.plot(a,Pp(a),color=BLUE,lw=1.5); ax.plot(b,Pm(b),color=BLUE,lw=1.5)
ax.plot(b,Pp(b),color=YELLOW,lw=1.5,ls='--')
xs=[.8]
for t in range(18): xs.append(xs[-1]-.3*(xs[-1]+.5))
xs=np.array(xs)
ax.plot(xs[:10],Pp(xs[:10]),'o-',color=GREEN,ms=2.8,lw=.9,zorder=5)
ax.plot([-.5],[0],'o',color=GREEN,ms=3.4,zorder=6,clip_on=False)
ax.plot([-.5,-.5],[0,2],color=RED,lw=1,ls=':',zorder=4)
ax.plot([-.5],[2],'o',color=RED,mfc=RED_FILL,mec=RED,ms=4,zorder=6)
ax.plot([0],[1/8],'o',color=RED,ms=4.4,zorder=7)
ax.plot([0],[9/8],'o',mfc='white',mec=BLUE,mew=.9,ms=4,zorder=6)
ax.text(.75,.42,r'$\Phi_+$',color=BLUE)
ax.text(-.9,1.95,r'$\Phi_-$',color=BLUE,va='center')
ax.text(-.98,.26,'分支的延续',color=YELLOW,fontsize=7.5)
ax.text(-.46,1.42,'真实外层值',color=RED,fontsize=7.5)
clean(ax,(-1,1.2),(0,2.6),'$x$','外层值')
save(fig, Path(__file__).resolve().parent, 'figure', {'eta':.3,'x0':.8})
