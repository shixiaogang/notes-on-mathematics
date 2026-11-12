from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# (a) J(theta) = E[sin(kX)], X = theta + eps ~ N(theta, 1), theta = 0.3.  Single-sample variances (closed form,
#     checked against 2*10^6 seeded draws):
#     reparameterisation k cos(k(theta+eps)):  k^2 (1 + cos(2k theta) e^{-2k^2})/2 - g^2,
#     score sin(k(theta+eps)) eps:            1/2 - cos(2k theta)(1-4k^2) e^{-2k^2}/2 - g^2,  g = k cos(k theta) e^{-k^2/2}.
# (b) J(theta) = E||X||^2, X ~ N(theta, I_d), theta = 0: trace of single-sample covariance
#     reparameterisation 2X: 4d;  score ||X||^2 X: d(d+2)(d+4);  score with baseline d: 2d^2 + 8d.
th = .3
def g(k): return k*np.cos(k*th)*np.exp(-k*k/2)
def vr(k): return k*k*(1+np.cos(2*k*th)*np.exp(-2*k*k))/2-g(k)**2
def vs(k): return .5-np.cos(2*k*th)*(1-4*k*k)*np.exp(-2*k*k)/2-g(k)**2
k = np.linspace(.02, 5, 500)
fig, axs = figure(width_mm=108, height_mm=52, ncols=2)
a1, a2 = axs
panel(fig, left=.12, right=.98, bottom=.3, top=.96, wspace=.38)
a1.plot(k, vr(k), color=BLUE, lw=1.4); a1.plot(k, vs(k), color=YELLOW, lw=1.6)
kk = np.linspace(.5, 2, 200001); d = vr(kk)-vs(kk); kx = kk[np.argmin(np.abs(d))]
dot(a1, kx, vr(kx))
a1.set_yscale('log'); a1.set_xlim(0, 5); a1.set_ylim(1e-3, 30); logticks(a1, [-2, 0])
lab(a1, 3.2, 3.0, '重参数化', BLUE); lab(a1, 3.2, .2, '得分函数', YELLOW)
axlab(a1, r'$k$', '单样本方差')
dd = np.arange(1, 201)
a2.plot(dd, 4*dd, color=BLUE, lw=1.4); a2.plot(dd, dd*(dd+2)*(dd+4), color=YELLOW, lw=1.6)
a2.plot(dd, 2*dd*dd+8*dd, color=YELLOW, lw=1.2, ls=DASH)
a2.set_xscale('log'); a2.set_yscale('log'); a2.set_xlim(1, 200); a2.set_ylim(1, 1e7)
logticks(a2, [0, 1, 2], 'x'); logticks(a2, [0, 2, 4, 6])
lab(a2, 20, 25, '重参数化', BLUE); lab(a2, 1.4, 2e3, '得分函数', YELLOW)
lab(a2, 25, 250, '带基线', YELLOW)
axlab(a2, r'$d$', '协方差矩阵的迹')
tags(fig, axs)
rng = np.random.default_rng(1); eps = rng.standard_normal(2_000_000)
sim = {kv: (float(np.var(kv*np.cos(kv*(th+eps)))), float(np.var(np.sin(kv*(th+eps))*eps))) for kv in (1.0, 3.0)}
save(fig, HERE, 'figure', {'crossover_k': float(kx), 'var_at_k': {str(a): (float(vr(a)), float(vs(a))) for a in (0.5, 1.0, 2.0, 3.0)},
     'simulated': {str(a): b for a, b in sim.items()}})
print(kx, sim)
