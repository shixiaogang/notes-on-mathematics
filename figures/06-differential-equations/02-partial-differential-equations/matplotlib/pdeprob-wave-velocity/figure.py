from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: same initial displacement, different initial velocities; the heat equation needs only one datum.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
ax=axs[0]; style(ax); X=np.linspace(0,1,300); S=np.sin(np.pi*X)
ax.plot(X,S,color=RED,lw=1.6)
ax.plot(X,np.cos(np.pi/4)*S,color=BLUE,lw=1.4)
ax.plot(X,(np.cos(np.pi/4)+np.sin(np.pi/4))*S,color=YELLOW,lw=1.6)
ax.text(.5,.5,r'$u_1=0$',ha='center',color=BLUE); ax.text(.5,1.47,r'$u_1=\pi\sin\pi x$',ha='center',color=YELLOW); ax.text(.5,.87,r'$u_0$',ha='center',color=RED)
ax.set_xlim(0,1); ax.set_ylim(0,1.7); ax.set_xticks([0,.5,1]); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); t=np.linspace(0,2,500)
ax.axhline(0,color=GRID,lw=.85)
ax.plot(t,np.cos(np.pi*t),color=BLUE,lw=1.4)
ax.plot(t,np.cos(np.pi*t)+np.sin(np.pi*t),color=YELLOW,lw=1.6)
ax.plot(t,np.exp(-np.pi**2*t),color=PURPLE,lw=1.4)
ax.plot([0],[1],'o',ms=3.8,color=RED)
ax.text(.1,-.28,'热方程',color=PURPLE)
ax.set_xlim(0,2); ax.set_xticks([0,1,2]); ax.set_ylabel(r'$u(1/2,t)$'); sub(ax,'b','$t$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'wave c=1: cos(pi t) sin(pi x), (cos(pi t)+sin(pi t)) sin(pi x); heat exp(-pi^2 t) sin(pi x)'})
