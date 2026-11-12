from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# X ~ N(theta,1), theta = 1, f = x^2, s = x - theta, target J'(1) = 2.
# Baseline = mean of all n values of f (uses the current sample): mean (n-1)/n * 2 (yellow, exact).
# Leave-one-out baseline (mean of the other n-1 values): unbiased, mean 2 (blue, exact).
# Dots: averages of the two estimators over R = 40000 seeded repetitions, n = 2..12.
rng = np.random.default_rng(SEED+4)
ns = np.arange(2, 13); R = 40000; th = 1.0
mfull, mloo, vloo, vnone = [], [], [], []
for n in ns:
    E = rng.standard_normal((R, n)); F = (th+E)**2
    fb = F.mean(1, keepdims=True); loo = (F.sum(1, keepdims=True)-F)/(n-1)
    g_full = ((F-fb)*E).mean(1); g_loo = ((F-loo)*E).mean(1); g0 = (F*E).mean(1)
    mfull.append(float(g_full.mean())); mloo.append(float(g_loo.mean())); vloo.append(float(g_loo.var()*n)); vnone.append(float(g0.var()*n))
fig, ax = figure(width_mm=80, height_mm=48)
panel(fig, left=.14, right=.97, bottom=.2, top=.96)
nn = np.linspace(2, 12, 200)
ax.plot(nn, 2*np.ones_like(nn), color=BLUE, lw=1.4)
ax.plot(nn, 2*(nn-1)/nn, color=YELLOW, lw=1.5)
ax.plot(ns, mloo, 'o', color=GREEN, ms=3.4, mew=0); ax.plot(ns, mfull, 's', color=GREEN, ms=3.2, mew=0)
lab(ax, 7.6, 2.08, '留一基线', BLUE); lab(ax, 7.6, 1.6, '含当前样本的基线', YELLOW)
ax.set_xlim(1.5, 12.5); ax.set_ylim(.8, 2.3); ax.set_xticks([2, 4, 6, 8, 10, 12]); ax.set_yticks([1, 1.5, 2])
axlab(ax, r'$n$')
save(fig, HERE, 'figure', {'n': ns.tolist(), 'mean_full': mfull, 'mean_loo': mloo, 'n_var_loo': vloo, 'n_var_plain': vnone})
