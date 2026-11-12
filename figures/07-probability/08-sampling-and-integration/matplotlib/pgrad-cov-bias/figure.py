from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# p_0 on {0,1,2} = (1/4, 1/2, 1/4) (the theta = 0 member of h(x) e^{theta x}, h = (1,2,1)); f = x^2, a = x; Cov(f, a) = 1 = J'(0).
# Sample covariance with denominator n-1 (unbiased, mean 1) vs n (mean (n-1)/n).  Lines: exact means;
# dots: averages over R = 40000 seeded repetitions for n = 2..12.
rng = np.random.default_rng(SEED+3)
ns = np.arange(2, 13); R = 40000; p = np.array([.25, .5, .25])
m1, m0 = [], []
for n in ns:
    X = rng.choice(3, size=(R, n), p=p); F = X**2.0; A = X*1.0
    S = ((F-F.mean(1, keepdims=True))*(A-A.mean(1, keepdims=True))).sum(1)
    m1.append(float((S/(n-1)).mean())); m0.append(float((S/n).mean()))
fig, ax = figure(width_mm=80, height_mm=48)
panel(fig, left=.14, right=.97, bottom=.2, top=.96)
nn = np.linspace(2, 12, 200)
ax.plot(nn, np.ones_like(nn), color=BLUE, lw=1.4)
ax.plot(nn, (nn-1)/nn, color=YELLOW, lw=1.5)
ax.plot(ns, m1, 'o', color=GREEN, ms=3.4, mew=0); ax.plot(ns, m0, 's', color=GREEN, ms=3.2, mew=0)
lab(ax, 8.2, 1.04, '分母', BLUE); lab(ax, 9.45, 1.04, r'$n-1$', BLUE); lab(ax, 8.2, .8, '分母', YELLOW); lab(ax, 9.45, .8, r'$n$', YELLOW)
ax.set_xlim(1.5, 12.5); ax.set_ylim(.4, 1.15); ax.set_xticks([2, 4, 6, 8, 10, 12]); ax.set_yticks([.5, .75, 1])
ax.set_yticklabels(['0.5', '0.75', '1'])
axlab(ax, r'$n$')
save(fig, HERE, 'figure', {'n': ns.tolist(), 'mean_n_minus_1': m1, 'mean_n': m0})
