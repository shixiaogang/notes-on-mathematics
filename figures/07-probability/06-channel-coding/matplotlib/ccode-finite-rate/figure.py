from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ccode-common"))
from ccode_fig import *
# Finite-length limits on BSC(0.1) at target average block error eps = 1e-3.
# Purple: converse  log2 M <= n - log2 s*(eps), s* = smallest (fractional) number of received words whose
#         probabilities p^d (1-p)^(n-d), taken in decreasing order, add to 1 - eps (sphere-packing argument).
# Green:  achievability from the random-coding union bound with uniform codewords and ML decoding (ties = errors):
#         Pe <= sum_k Bin(n,p)(k) min(1, (M-1) V(n,k) 2^-n),   V(n,k) = sum_{j<=k} C(n,j).
# Blue:   capacity C = 1 - h2(0.1).  (b) the gaps C - R on log-log axes with a reference slope n^(-1/2).
EPS = 1e-3; C = float(1-h2(P)); lp, lq = math.log(P), math.log(1-P)


def lse(a, b):
    m = max(a, b); return m+math.log(math.exp(a-m)+math.exp(b-m))


def conv_rate(n, eps=EPS):
    acc = 0.0; ls = -math.inf
    for d in range(n+1):
        lc = lbinom(n, d); lw = d*lp+(n-d)*lq; mass = math.exp(lc+lw)
        if acc+mass >= 1-eps:
            lfrac = math.log(1-eps-acc)-lw
            ls = lfrac if ls == -math.inf else lse(ls, lfrac)
            return 1-ls/math.log(2)/n
        acc += mass; ls = lc if ls == -math.inf else lse(ls, lc)


def rcu(n, logM):
    tot = 0.0; cum = -math.inf
    lM1 = math.log(2**logM-1) if logM < 60 else logM*math.log(2)
    for k in range(n+1):
        lc = lbinom(n, k); cum = lc if k == 0 else lse(cum, lc)
        tot += math.exp(lc+k*lp+(n-k)*lq+min(0.0, lM1+cum-n*math.log(2)))
    return tot


def ach_rate(n, eps=EPS):
    lo, hi = 0.0, float(n)
    for _ in range(45):
        m = (lo+hi)/2
        if rcu(n, m) <= eps: lo = m
        else: hi = m
    return lo/n


ns = np.unique(np.round(np.logspace(np.log10(20), np.log10(3000), 40)).astype(int))
cr = np.array([conv_rate(n) for n in ns]); ar = np.array([ach_rate(n) for n in ns])
fig, axs = figure(width_mm=110, height_mm=52, ncols=2)
panel(fig, left=.09, right=.97, top=.95, bottom=.27, wspace=.36)
ax = axs[0]
ax.axhline(C, color=BLUE, lw=1.1, ls=DASH)
ax.plot(ns, cr, color=PURPLE, lw=1.4); ax.plot(ns, ar, color=GREEN, lw=1.4)
lab(ax, 2400, C+.02, r'$C$', BLUE); ax.annotate('逆向上界', xy=(2000, conv_rate(2000)), xytext=(1500, .25), fontsize=7.5, color=PURPLE, arrowprops=dict(arrowstyle='-', color=PURPLE, lw=.7))
ax.annotate('随机码保证', xy=(600, ach_rate(600)), xytext=(700, .13), fontsize=7.5, color=GREEN, arrowprops=dict(arrowstyle='-', color=GREEN, lw=.7))
ax.set_xlim(0, 3000); ax.set_ylim(0, .6); ax.set_xticks([0, 1000, 2000, 3000])
ax.set_xlabel(r'$n$', labelpad=1); ax.set_ylabel(r'$R$', labelpad=1)
ax = axs[1]
ax.plot(ns, C-cr, color=PURPLE, lw=1.4); ax.plot(ns, C-ar, color=GREEN, lw=1.4)
ref = 3.6/np.sqrt(ns); ax.plot(ns, ref, color=MUTED, lw=.85, ls=DOT)
lab(ax, 250, 3.6/np.sqrt(250)*1.2, r'$\propto n^{-1/2}$', MUTED)
ax.set_xscale('log'); ax.set_yscale('log'); logticks(ax, [2, 3], axis='x'); ax.minorticks_off(); ax.set_yticks([.05, .1, .2, .5]); ax.set_yticklabels(['$0.05$', '$0.1$', '$0.2$', '$0.5$'])
ax.set_xlim(18, 3300); ax.set_ylim(.03, .7)
ax.set_xlabel(r'$n$', labelpad=1); ax.set_ylabel(r'$C-R$', labelpad=1)
tags(fig, axs)
extra = {n: (ach_rate(n), conv_rate(n)) for n in (7, 100, 1000)}
save(fig, HERE, 'figure', {'eps': EPS, 'C': C, 'n_ach_conv': extra})
print(extra)
