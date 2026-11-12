from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Z-channel with costs c(0)=0, c(1)=1, so E c(X) = q = P(X=1).
# (a) I(q) = h2(q/2) - q with the feasible inputs q <= Gamma = 0.25 shaded; red dot = constrained optimum,
#     grey dot = unconstrained optimum q = 0.4.
# (b) capacity-cost function C(Gamma) = h2(Gamma/2) - Gamma for Gamma <= 0.4 and log2(5/4) beyond;
#     purple tangent at Gamma = 0.25 with slope s = (1/2) log2 7 - 1 = 0.404 bit per unit cost.
G0 = .25; q = np.linspace(0, 1, 801); I = h2(q/2) - q
def Cg(g):
    g = np.asarray(g, float); return np.where(g <= .4, h2(np.minimum(g, .4)/2) - np.minimum(g, .4), np.log2(1.25))
s = .5*np.log2(7) - 1
fig, axs = figure(width_mm=110, height_mm=50, ncols=2)
panel(fig, left=.1, right=.97, top=.95, bottom=.27, wspace=.34)
ax = axs[0]
m = q <= G0; ax.fill_between(q[m], 0, I[m], color=BLUE_FILL, lw=0)
ax.plot(q, I, color=BLUE, lw=1.4); ax.axvline(G0, color=STROKE, lw=.8)
dot(ax, G0, float(h2(G0/2)-G0)); dot(ax, .4, np.log2(1.25), color=MUTED, ms=3.5)
lab(ax, G0-.02, .02, r'$\Gamma$', INK, ha='right'); lab(ax, .45, np.log2(1.25)+.005, '无约束最优', MUTED)
ax.set_xlim(0, 1); ax.set_ylim(0, .36); ax.set_xlabel(r'$q$', labelpad=1); ax.set_ylabel(r'$I$ / bit', labelpad=1)
ax = axs[1]
g = np.linspace(0, 1, 801); ax.plot(g, Cg(g), color=BLUE, lw=1.4)
c0 = float(Cg(G0)); t = np.linspace(.08, .36, 50); ax.plot(t, c0 + s*(t-G0), color=PURPLE, lw=1.0)
dot(ax, G0, c0); ax.axvline(.4, color=STROKE, lw=.6, ls=DOT)
lab(ax, .47, .25, r'$s\approx0.404$', PURPLE); lab(ax, .42, .02, r'$0.4$', MUTED)
ax.set_xlim(0, 1); ax.set_ylim(0, .36); ax.set_xlabel(r'$\Gamma$', labelpad=1); ax.set_ylabel(r'$C(\Gamma)$', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', {'Gamma': G0, 'C_Gamma': c0, 'slope': float(s), 'C_unconstrained': float(np.log2(1.25))})
