from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: ramp and step data have entropy solutions whose L1 distance shrinks as (1-t)/4 and vanishes at t=1.
fig, axs = figure(width_mm=112, height_mm=66, nrows=2, ncols=2)
def ramp_sol(x,t):
    if t<1: return np.where(x<t,1.0,np.where(x>1,0.0,(1-x)/(1-t)))
    return np.where(x<(1+t)/2,1.0,0.0)
def step_sol(x,t): return np.where(x<(1+t)/2,1.0,0.0)
x=np.linspace(-.5,2,5001)
for ax,t,l in zip(axs.flat[:3],(0,.5,1),'abc'):
    style(ax); a=ramp_sol(x,t); b=step_sol(x,t)
    ax.fill_between(x,a,b,color=RED_FILL,lw=0)
    ax.plot(x,a,color=BLUE,lw=1.4); g=(1+t)/2; ax.plot([-.5,g,g,2],[1,1,0,0],color=YELLOW,lw=1.5)
    ax.set_xlim(-.5,2); ax.set_ylim(0,1.15); sub(ax,l,'$x$'); ax.set_ylabel('$u$')
    ax.text(1.97,1.0,f'$t={t:g}$',ha='right',va='top')
ax=axs[1,1]; style(ax); t=np.linspace(0,2,200); num=[]
for tt in t: num.append(np.trapezoid(np.abs(ramp_sol(x,tt)-step_sol(x,tt)),x) if hasattr(np,'trapezoid') else np.trapz(np.abs(ramp_sol(x,tt)-step_sol(x,tt)),x))
ax.plot(t,num,color=RED,lw=1.4); ax.set_xlim(0,2); ax.set_ylim(0,.3); ax.set_ylabel('$\\|u-v\\|_1$'); sub(ax,'d','$t$')
fig.get_layout_engine().set(w_pad=0.09,h_pad=0.04)
save(fig, HERE(__file__), 'figure', {'formula':'L1 distance (1-t)/4 for t<1; 0 after'})
