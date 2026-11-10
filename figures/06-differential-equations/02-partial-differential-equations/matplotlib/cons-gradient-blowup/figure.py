from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: gradients blow up at T* on the compressive side while values stay in [0,1]; expansive side decays.
fig, axs = figure(width_mm=112, height_mm=44, ncols=2)
x0=np.linspace(-20,20,400001); du=dbump(x0)
t=np.linspace(0,TSTAR*.985,300)
mn=np.array([np.max(-du/(1+tt*du)) for tt in t]); mx=np.array([np.max(du/(1+tt*du)) for tt in t])
ax=axs[0]; style(ax); ax.plot(t,mn,color=RED,lw=1.4); ax.plot(t,mx,color=YELLOW,lw=1.4)
ax.axvline(TSTAR,color=LINE,lw=.85,ls='--'); ax.text(TSTAR-.05,16.4,'$T^{*}$',ha='right')
ax.text(.82,5.0,'压缩侧',color=RED); ax.text(.45,1.7,'膨胀侧',color=YELLOW)
ax.set_xlim(0,1.75); ax.set_ylim(0,18); ax.set_ylabel('斜率大小'); sub(ax,'a','$t$')
ax=axs[1]; style(ax); ax.plot([0,TSTAR],[1,1],color=BLUE,lw=1.4); ax.plot([0,TSTAR],[0,0],color=BLUE,lw=1.4,clip_on=False)
ax.axvline(TSTAR,color=LINE,lw=.85,ls='--'); ax.text(.1,.86,'$\\max u$'); ax.text(.1,.07,'$\\inf u$')
ax.set_xlim(0,1.75); ax.set_ylim(0,1.15); ax.set_ylabel('场值'); sub(ax,'b','$t$')
save(fig, HERE(__file__), 'figure', {'formula':'max over x0 of -+u0prime/(1+t u0prime)'})
