from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ccode-common"))
from ccode_fig import *
# Exact bit error rate versus flip probability p on BSC(p): uncoded (rate 1), 3-fold repetition with majority
# decoding (rate 1/3), and the [7,4,3] Hamming code with syndrome decoding (rate 4/7, exact enumeration of 128 patterns).
ps = np.logspace(-3, np.log10(.5), 120)
rep = np.array([tail(3, 1, q) for q in ps]); ham = np.array([ham_ber(q) for q in ps])
fig, ax = figure(width_mm=88, height_mm=56)
panel(fig, left=.15, right=.96, top=.96, bottom=.17)
ax.plot(ps, ps, color=MUTED, lw=1.0, ls=DASH)
ax.plot(ps, ham, color=BLUE, lw=1.4)
ax.plot(ps, rep, color=YELLOW, lw=1.4)
for v in (P, ham_ber(P), tail(3, 1, P)):
    dot(ax, P, v, ms=3.4)
lab(ax, 1.15e-3, 2.4e-3, '不编码', MUTED)
lab(ax, 1.15e-3, 3e-4, 'Hamming', BLUE)
lab(ax, 2.2e-2, 2.5e-4, '三次重复', YELLOW)
lab(ax, .045, .0669*0.9, r'$0.067$', RED, ha='right'); lab(ax, .085, .028*0.35, r'$0.028$', RED, ha='right')
ax.set_xscale('log'); ax.set_yscale('log'); logticks(ax, [-3, -2, -1], axis='x'); logticks(ax, [-6, -4, -2, 0])
ax.set_xlim(1e-3, .5); ax.set_ylim(1e-6, 1)
ax.set_xlabel(r'$p$', labelpad=1); ax.set_ylabel('比特错误率', labelpad=1)
save(fig, HERE, 'figure', {'ber_at_0.1': {'uncoded': P, 'rep3': tail(3, 1, P), 'hamming': ham_ber(P)},
     'ber_at_0.01': {'rep3': tail(3, 1, .01), 'hamming': ham_ber(.01)}})
