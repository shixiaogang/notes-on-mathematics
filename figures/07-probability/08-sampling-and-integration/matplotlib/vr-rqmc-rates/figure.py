from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# RMSE/sigma of the randomly shifted grid a_k = k/n (one shift Delta ~ Unif(0,1)) against independent sampling.
# Var(Q) = n int_0^{1/n} Q(D)^2 dD - I^2,  Q(D) = (1/n) sum_k F(D + k/n).  The integral is computed by the
# midpoint rule after the substitution D = (1 - t^3)/n, t in (0,1], dD = 3t^2/n dt, which removes the
# (1/n - D)^{-2/3} singularity of F3^2; M = 40000 and 80000 nodes agree to < 0.1%.
# F1(u) = e^u (smooth, not periodic); F2(u) = e^{1-|2u-1|} (tent-periodised e^u, same integral);
# F3(u) = (1-u)^{-1/3} = T(u) for X ~ Pareto(3) on [1,inf), f(x) = x (I = 3/2, sigma^2 = 3/4).
def rmse(F, I, n, M):
    tt = (np.arange(M)+.5)/M; D = (1-tt**3)/n; wgt = 3*tt**2
    # pass u and 1-u = ((n-1-k) + t^3)/n separately so the singular end is resolved without rounding
    Q = np.mean([F(D + k/n, ((n-1-k) + tt**3)/n) for k in range(n)], axis=0)
    return math.sqrt(np.mean(wgt*(Q-I)**2))
F1 = lambda u, v: np.exp(u); F2 = lambda u, v: np.exp(1-np.abs(2*u-1)); F3 = lambda u, v: v**(-1/3)
s1 = math.sqrt((E*E-1)/2-(E-1)**2); s3 = math.sqrt(.75)
ns = 2**np.arange(0, 11)
r1 = [rmse(F1, E-1, n, 40000)/s1 for n in ns]; r2 = [rmse(F2, E-1, n, 40000)/s1 for n in ns]
r3 = [rmse(F3, 1.5, n, 40000)/s3 for n in ns]; r3b = [rmse(F3, 1.5, n, 80000)/s3 for n in ns]
mc = 1/np.sqrt(ns)
fig, ax = figure(width_mm=100, height_mm=56)
panel(fig, left=.12, right=.97, bottom=.18, top=.96)
ax.plot(ns, mc, 'o-', color=BLUE, lw=1.2, ms=2.6)
ax.plot(ns, r3, 'o-', color=RED, lw=1.2, ms=2.6)
ax.plot(ns, r1, 'o-', color=GREEN, lw=1.2, ms=2.6)
ax.plot(ns, r2, 'o-', color=YELLOW, lw=1.4, ms=2.6)
ax.set_xscale('log', base=2); ax.set_yscale('log'); ax.set_xlim(.8, 1300); ax.set_ylim(1e-7, 2)
ax.set_xticks([1, 4, 16, 64, 256, 1024]); ax.set_xticklabels(['1', '4', '16', '64', '256', '1024']); ax.minorticks_off()
logticks(ax, [-6, -4, -2, 0])
lab(ax, 300, .1, r'$n^{-1/2}$', BLUE); lab(ax, 330, 6e-3, r'$n^{-2/3}$', RED)
lab(ax, 330, 3e-4, r'$n^{-1}$', GREEN); lab(ax, 70, 1.5e-6, r'$n^{-2}$', YELLOW)
axlab(ax, '$n$')
ax.set_ylabel('相对均方根误差', labelpad=1)
save(fig, HERE, 'figure', {'ns': ns.tolist(), 'mc': mc.tolist(), 'shift_exp': r1, 'shift_tent': r2, 'shift_pareto': r3,
     'shift_pareto_M80000': r3b})
