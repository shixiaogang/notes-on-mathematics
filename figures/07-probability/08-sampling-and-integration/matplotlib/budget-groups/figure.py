from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# I = int_0^1 e^u du = e - 1.  Randomly shifted grid: n points a_k = k/n, one shift Delta ~ Unif(0,1) per group,
# group estimate Q = (1/n) sum_k exp((a_k + Delta) mod 1).  Fixed total N = nR = 1024 evaluations, R groups.
# Exact Var(Q_n) = (e-1)^2 (x coth x - 1), x = 1/(2n).  Report: RMSE of the average sqrt(Var/R);
# mean half-width and coverage of the interval Qbar +- t_{R-1,0.975} s_Q/sqrt(R) from 40000 simulated runs (seed 3);
# naive half-width 1.96 sqrt(S^2/N) from the pooled N points (S^2 their sample variance), averaged likewise.
N = 1024; Rs = [2, 4, 8, 16, 32, 64, 128, 256, 512]
rng = np.random.default_rng(3); reps = 40000
def varQ(n): x = 1/(2*n); return (E-1)**2*(x/math.tanh(x)-1)
rmse, hw, cov, naive = [], [], [], []
for R in Rs:
    n = N//R; a = np.arange(n)/n; tq = tquant(R-1)
    D = rng.random((reps, R))
    d = np.mod(D, 1/n)                        # the shifted grid only depends on Delta mod 1/n
    S1 = np.exp(d)*np.sum(np.exp(a))/n        # Q for each group
    S2 = np.exp(2*d)*np.sum(np.exp(2*a))/n    # mean of squares within group
    Qb = S1.mean(1); sQ = S1.std(1, ddof=1)
    h = tq*sQ/math.sqrt(R); hw.append(h.mean()); cov.append(np.mean(np.abs(Qb-(E-1)) <= h))
    pooled_var = (S2.mean(1)-Qb**2)*N/(N-1); naive.append(np.mean(1.96*np.sqrt(pooled_var/N)))
    rmse.append(math.sqrt(varQ(n)/R))
fig, axs = figure(width_mm=108, height_mm=52, ncols=2)
a1, a2 = axs
panel(fig, left=.11, right=.98, bottom=.3, top=.96, wspace=.38)
a1.plot(Rs, rmse, 'o-', color=BLUE, lw=1.3, ms=2.4); a1.plot(Rs, hw, 'o-', color=GREEN, lw=1.3, ms=2.4)
a1.plot(Rs, naive, color=RED, lw=1.1, ls=DASH)
a1.set_xscale('log', base=2); a1.set_yscale('log'); a1.set_xlim(1.6, 640); a1.set_ylim(3e-4, .1)
a1.set_xticks([2, 8, 32, 128, 512]); a1.set_xticklabels(['2', '8', '32', '128', '512']); a1.minorticks_off()
logticks(a1, [-3, -2, -1])
lab(a1, 20, 1.1e-3, '均方根误差', BLUE); lab(a1, 3, 1.0e-2, '区间半宽', GREEN); lab(a1, 2.2, .045, '全部点当独立样本', RED)
axlab(a1, r'$R$', '误差尺度')
a2.plot(Rs, cov, 'o-', color=GREEN, lw=1.3, ms=2.4); a2.axhline(.95, color=PURPLE, lw=.85, ls=DASH)
a2.set_xscale('log', base=2); a2.set_xlim(1.6, 640); a2.set_ylim(.9, 1.0)
a2.set_xticks([2, 8, 32, 128, 512]); a2.set_xticklabels(['2', '8', '32', '128', '512']); a2.minorticks_off()
lab(a2, 100, .953, '0.95', PURPLE)
axlab(a2, r'$R$', '覆盖率')
tags(fig, axs)
facts = {str(R): {'n': N//R, 'rmse': r, 'half_width': h, 'coverage': c, 'naive_half_width': nv} for R, r, h, c, nv in zip(Rs, rmse, hw, cov, naive)}
save(fig, HERE, 'figure', facts)
for k, v in facts.items(): print(k, {a: round(float(b), 7) for a, b in v.items()})
