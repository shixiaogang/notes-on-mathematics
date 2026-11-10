from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: Burgers from the box datum: fan and shock interact at (2,2), then shock sqrt(2t), profile a decaying triangle.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax=axs[0]; style(ax); tm=8
t=np.linspace(0,2,50); ax.plot(1+t/2,t,color=LINE,lw=2.2)
t=np.linspace(2,tm,200); ax.plot(np.sqrt(2*t),t,color=LINE,lw=2.2)
for k in np.linspace(0,1,7)[1:]:
    # fan ray x=k t hits shock
    tk=(2 if k>=1 else 2/k**2)
    if k>=1:
        ax.plot([0,2],[0,2],color=BLUE,lw=.95)
    else:
        e=min(tk,tm); ax.plot([0,k*e],[0,e],color=BLUE,lw=.95)
ax.plot([0,0],[0,tm],color=BLUE,lw=.95)
ax.plot([2],[2],'o',ms=4.5,color=RED,zorder=5)
ax.plot([-1,5],[0,0],color=RED,lw=2,clip_on=False)
ax.set_xlim(-1,5); ax.set_ylim(0,tm); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); ax.plot([-1,0,0,1,1,6],[0,0,1,1,0,0],color=RED,lw=1.4)
ax.plot([-1,0,1,1.5,1.5,6],[0,0,1,1,0,0],color=SHADES[0],lw=1.4)
ax.plot([-1,0,2,2,6],[0,0,1,0,0],color=SHADES[1],lw=1.4)
g=np.sqrt(8); ax.plot([-1,0,g,g,6],[0,0,g/4,0,0],color=SHADES[2],lw=1.4)
g=4.0; ax.plot([-1,0,g,g,6],[0,0,g/8,0,0],color=SHADES[3],lw=1.4)
ax.text(.45,1.04,'$t=0$',color=RED,ha='center'); ax.text(1.2,1.04,'$1$',color=SHADES[0]); ax.text(2.1,.92,'$2$',color=SHADES[1]); ax.text(2.93,.62,'$4$',color=SHADES[2]); ax.text(4.1,.45,'$8$',color=SHADES[3])
ax.set_xlim(-1,6); ax.set_ylim(0,1.2); ax.set_ylabel('$u$'); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'box datum, fan x/t, shock 1+t/2 then sqrt(2t)'})
