"""Three bivariate models with mean 0 and covariance I: Gaussian (yellow), elliptical Laplace X=sqrt(W)Z,
W~Exp(1) (blue), t with nu=5 rescaled to unit variance, X=sqrt(3/U)Z, U~chi^2_5 (purple).
(a) marginal tail P(|X1|>r), log scale;
(b) joint-exceedance ratio P(|X1|>r,|X2|>r)/P(|X1|>r)^2; equals 1 for independent components
(Gaussian, and the product-Laplace model). Computed as E[h(V)] and E[h(V)^2] with h(v)=2(1-Phi(r/sqrt v)),
by numerical integration over the exact density of V."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

s = np.linspace(-12, 7, 6001)  # log-grid for V
def mix(wfun):
    v = np.exp(s); w = wfun(v)*v  # density in s
    return v, w/np.trapezoid(w, s)
vL, wL = mix(lambda v: np.exp(-v))
nu = 5
def ft(v):  # V = 3/U, U ~ chi2_5 -> density of V
    u = 3/v
    return np.exp((nu/2-1)*np.log(u)-u/2-(nu/2)*math.log(2)-math.lgamma(nu/2))*3/v**2
vT, wT = mix(ft)
def tails(v, w, r):
    h = 2*(1-Phi(r/np.sqrt(v)))
    return float(np.trapezoid(w*h, s)), float(np.trapezoid(w*h*h, s))
rs = np.linspace(0, 5, 101)[1:]
TL = np.array([tails(vL, wL, r) for r in rs]); TT = np.array([tails(vT, wT, r) for r in rs])
G = 2*(1-Phi(rs))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, top=.96, bottom=.28, wspace=.3)
ax = axes[0]; style(ax)
ax.plot(rs, G, color=YELLOW, lw=1.6); ax.plot(rs, TL[:, 0], color=BLUE, lw=1.4); ax.plot(rs, TT[:, 0], color=PURPLE, lw=1.4)
ax.set_yscale('log'); ax.set_xlim(0, 5); ax.set_ylim(1e-6, 1.2); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([1e-6, 1e-4, 1e-2, 1])
lab(ax, 3.3, 2e-5, r'$\mathcal{N}$', YELLOW, ha='left'); lab(ax, 3.9, 2.5e-4, 'Laplace', BLUE, ha='left'); lab(ax, 3.5, 2.5e-2, '$t_5$', PURPLE, ha='left')
axlab(ax, '$r$')
ax = axes[1]; style(ax)
ax.plot(rs, np.ones_like(rs), color=YELLOW, lw=1.6)
ax.plot(rs, TL[:, 1]/TL[:, 0]**2, color=BLUE, lw=1.4); ax.plot(rs, TT[:, 1]/TT[:, 0]**2, color=PURPLE, lw=1.4)
ax.set_xlim(0, 5); ax.set_ylim(0, 12); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([1, 4, 8, 12])
lab(ax, 4.0, 1.5, r'$\mathcal{N}$', YELLOW, ha='left'); lab(ax, 3.2, 6.2, 'Laplace', BLUE, ha='left'); lab(ax, 2.0, 9.5, '$t_5$', PURPLE, ha='left')
axlab(ax, '$r$')
tags(fig, axes)
i3 = int(np.argmin(np.abs(rs-3)))
save(fig, HERE(__file__), 'figure', {'r': float(rs[i3]), 'gauss_tail': float(G[i3]), 'laplace_tail': TL[i3, 0], 't5_tail': TT[i3, 0],
     'ratio_laplace': TL[i3, 1]/TL[i3, 0]**2, 'ratio_t5': TT[i3, 1]/TT[i3, 0]**2, 'laplace_tail_exact_r3': math.exp(-3*math.sqrt(2))})
