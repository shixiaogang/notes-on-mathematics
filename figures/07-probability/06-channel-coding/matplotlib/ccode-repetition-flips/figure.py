from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ccode-common"))
from ccode_fig import *
# Repetition codes with majority decoding on BSC(p).
# (a) exact Bin(5, 0.1) distribution of the number of flips in a block of length 5; at most t=2 flips are corrected.
# (b) exact block error P(Bin(n,p) > (n-1)/2) versus p for n = 1, 3, 5, 7 (log scale); red dots at p = 0.1.
n = 5; t = 2
pm = np.array([math.comb(n, j)*P**j*(1-P)**(n-j) for j in range(n+1)])
fig, axs = figure(width_mm=110, height_mm=50, ncols=2)
panel(fig, left=.09, right=.97, top=.95, bottom=.27, wspace=.36)
ax = axs[0]
for j in range(n+1):
    ok = j <= t
    ax.bar(j, pm[j], width=.62, color=BLUE_FILL if ok else RED_FILL, edgecolor=BLUE if ok else RED, lw=.8)
ax.axvline(t+.5, color=STROKE, lw=.85, ls=DASH)
for j, s in [(0, r'$0.590$'), (1, r'$0.328$'), (2, r'$0.073$')]:
    lab(ax, j, pm[j]+.02, s, MUTED, ha='center')
lab(ax, 4.0, .30, '判错概率', RED, ha='center'); lab(ax, 4.0, .24, r'$0.00856$', RED, ha='center')
ax.set_xticks(range(n+1)); ax.set_ylim(0, .68); ax.set_yticks([0, .2, .4, .6])
ax.set_xlabel('翻转个数', labelpad=1); ax.set_ylabel('概率', labelpad=1)
ax = axs[1]
ps = np.logspace(-3, np.log10(.5), 200)
cols = {1: MUTED, 3: YELLOW, 5: GREEN, 7: BLUE}
for m, c in cols.items():
    tt = (m-1)//2
    e = np.array([tail(m, tt, q) for q in ps])
    ax.plot(ps, e, color=c, lw=1.4 if m > 1 else 1.0, ls=DASH if m == 1 else '-')
    dot(ax, P, tail(m, tt, P), ms=3.4)
for m, y in [(1, 4e-3), (3, 3e-5), (5, 1.5e-7)]:
    lab(ax, 1.15e-3, y, r'$n=%d$' % m, cols[m])
lab(ax, 1.6e-2, 2.2e-9, r'$n=7$', BLUE)
ax.set_xscale('log'); ax.set_yscale('log'); logticks(ax, [-3, -2, -1], axis='x'); logticks(ax, [-8, -6, -4, -2, 0])
ax.set_ylim(1e-9, 1.5); ax.set_xlim(1e-3, .5)
ax.set_xlabel(r'$p$', labelpad=1); ax.set_ylabel('块错误概率', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', {'p': P, 'bin5': list(map(float, pm)), 'pe_at_0.1': {m: tail(m, (m-1)//2, P) for m in cols}})
