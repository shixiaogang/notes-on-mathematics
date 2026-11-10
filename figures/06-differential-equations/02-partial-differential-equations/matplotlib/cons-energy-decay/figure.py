from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: for the bump datum mass stays constant and energy is constant before T*, then decays at the rate (u_- - u_+)^3/12.
fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
T,Xs,UL,UR=bump_shock(12.0)
s=GRID0; ds=np.gradient(s)
E0=np.pi/4
Es=[]; Ms=[]
tt=np.linspace(TSTAR,12,120)
for t in tt:
    br=branches(max(t,TSTAR+1e-5)); il,ir=br; g=np.interp(t,T,Xs); X=s+t*bump(s)
    xl=np.interp(g,X[:il+1],s[:il+1]); xr=np.interp(g,X[ir:],s[ir:])
    k=(s<xl)|(s>xr); J=1+t*dbump(s)
    Es.append(np.sum((bump(s)**2/2*J*ds)[k])); Ms.append(np.sum((bump(s)*J*ds)[k]))
Es=np.array(Es)/np.sum(bump(s)**2/2*ds); Ms=np.array(Ms)/np.sum(bump(s)*ds)
ax=axs[0]; style(ax); ax.plot(np.r_[0,tt],np.r_[Ms[0],Ms],color=YELLOW,lw=1.5); ax.plot(np.r_[0,tt],np.r_[1,Es],color=BLUE,lw=1.4)
ax.axvline(TSTAR,color=LINE,lw=.85,ls='--'); ax.text(TSTAR+.15,.56,'$T^{*}$')
ax.text(6.7,1.03,'总量',color=YELLOW); ax.text(7,.86,'$\\int u^2/2$',color=BLUE)
ax.set_xlim(0,12); ax.set_ylim(.5,1.12); ax.set_ylabel('相对初值'); sub(ax,'a','$t$')
ax=axs[1]; style(ax); ax.plot(np.r_[0,TSTAR,T],np.r_[0,0,(UL-UR)**3/12],color=RED,lw=1.4)
ax.axvline(TSTAR,color=LINE,lw=.85,ls='--'); ax.set_xlim(0,12); ax.set_ylim(0,None); ax.set_ylabel('$(u_--u_+)^3/12$'); sub(ax,'b','$t$')
save(fig, HERE(__file__), 'figure', {'formula':'integrals in Lagrangian variable; dissipation rate'})
