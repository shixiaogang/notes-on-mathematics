from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: a smooth test function approximating the indicator of a space-time box; its gradient lives at the box edge.
def step(z):
    z=np.clip(z,0,1); return z*z*(3-2*z)
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
ax=axs[0]; style(ax); x=np.linspace(-.5,3.5,1000); d=.3
ax.plot(x,((x>=1)&(x<=2.5))*1.0,color=YELLOW,lw=1.4,drawstyle='steps-mid')
ax.plot(x,step((x-(1-d))/d)*step(((2.5+d)-x)/d),color=BLUE,lw=1.4)
ax.set_xticks([1,2.5],['$a$','$b$']); ax.set_yticks([0,1]); ax.set_xlim(-.5,3.5); ax.set_ylim(0,1.15); ax.set_ylabel('权重'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); x=np.linspace(-.5,3.5,400); t=np.linspace(0,2.4,300); XX,TT=np.meshgrid(x,t)
P=step((XX-(1-d))/d)*step(((2.5+d)-XX)/d)*step((TT-(.6-d))/d)*step(((1.8+d)-TT)/d)
ax.pcolormesh(XX,TT,P,cmap=FIELD,vmin=0,vmax=1,shading='auto',rasterized=True)
ax.plot([1,2.5,2.5,1,1],[.6,.6,1.8,1.8,.6],color=LINE,lw=1.2)
ax.set_xticks([1,2.5],['$a$','$b$']); ax.set_yticks([.6,1.8],['$t_1$','$t_2$']); ax.set_xlim(-.5,3.5); ax.set_ylim(0,2.4); ax.set_ylabel('$t$'); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'product of smoothsteps, delta=.3'})
