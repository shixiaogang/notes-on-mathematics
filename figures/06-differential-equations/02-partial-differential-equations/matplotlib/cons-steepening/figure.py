from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: profile steepening of the bump datum up to T*, then the overturned multi-valued graph.
fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
s=np.concatenate([np.linspace(-6,8,5000),np.linspace(8,40,500)])
ax=axs[0]; style(ax); ax.plot(s,bump(s),color=RED,lw=1.4)
ax.plot(s+.8*bump(s),bump(s),color=SHADES[1],lw=1.4); ax.plot(s+TSTAR*bump(s),bump(s),color=SHADES[3],lw=1.4)
ax.plot([XSTAR],[.75],'o',ms=4,color=RED,zorder=5)
ax.text(-2.6,.5,'$t=0$',color=RED); ax.text(.7,1.05,'$t=0.8$',color=SHADES[2],ha='center'); ax.text(2.0,.92,'$T^{*}$',color=SHADES[3])
ax.set_xlim(-4,6); ax.set_ylim(0,1.2); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); t=3; X=s+t*bump(s); neg=1+t*dbump(s)<0
ax.plot(np.where(neg,np.nan,X),bump(s),color=BLUE,lw=1.4); ax.plot(np.where(neg,X,np.nan),bump(s),color=RED,lw=1.5,ls='--')
x=2.55; g=X-x; idx=np.where(np.diff(np.sign(g)))[0]
ax.plot([x,x],[0,1.05],color=MUTED,lw=.85,ls=':')
for i in idx: ax.plot([x],[bump(s[i])],'o',ms=3.5,color=RED,zorder=5)
ax.set_xlim(-4,6); ax.set_ylim(0,1.12); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'graph (x0+t u0, u0) for t=0,0.8,T*,3'})
