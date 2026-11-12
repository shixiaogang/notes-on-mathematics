from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ccode-common"))
from ccode_fig import *
# The [5,2,3] code (G5, H5) with syndrome (coset-leader) decoding on BSC(0.1).
# Error patterns grouped by weight w: (a) number of patterns C(5,w) and how many are coset leaders (corrected);
# (b) probability of each weight class, split into corrected (blue) and not corrected (red). Exact enumeration.
from collections import defaultdict
cos = defaultdict(list)
for e in words(5):
    cos[tuple(H5 @ e % 2)].append(e)
leaders = []
for s, es in sorted(cos.items()):
    mw = min(int(e.sum()) for e in es)
    leaders.append([e for e in es if e.sum() == mw][0])     # any minimum-weight member
lw_ = [int(e.sum()) for e in leaders]
cnt = [math.comb(5, w) for w in range(6)]
cor = [lw_.count(w) for w in range(6)]
prob = [P**w*(1-P)**(5-w) for w in range(6)]
fig, axs = figure(width_mm=110, height_mm=50, ncols=2)
panel(fig, left=.09, right=.97, top=.95, bottom=.27, wspace=.36)
x = np.arange(6)
ax = axs[0]
ax.bar(x, cnt, width=.62, color='white', edgecolor=STROKE, lw=.8)
ax.bar(x, cor, width=.62, color=BLUE_FILL, edgecolor=BLUE, lw=.8)
for w in range(6):
    lab(ax, w, cnt[w]+.3, r'$%d/%d$' % (cor[w], cnt[w]), MUTED, ha='center')
ax.axvline(1.5, color=STROKE, lw=.85, ls=DASH)
ax.set_xticks(x); ax.set_ylim(0, 12); ax.set_xlabel(r'$w$', labelpad=1); ax.set_ylabel('错误模式个数', labelpad=1)
ax = axs[1]
pc = [cor[w]*prob[w] for w in range(6)]; pf = [(cnt[w]-cor[w])*prob[w] for w in range(6)]
ax.bar(x, pc, width=.62, color=BLUE_FILL, edgecolor=BLUE, lw=.8)
ax.bar(x, pf, width=.62, bottom=pc, color=RED_FILL, edgecolor=RED, lw=.8)
for w, s in [(0, r'$0.590$'), (1, r'$0.328$')]:
    lab(ax, w, pc[w]+.015, s, BLUE, ha='center')
lab(ax, 2, pc[2]+pf[2]+.015, r'$0.073$', MUTED, ha='center')
ax.annotate('其中纠正 0.015', xy=(2.2, pc[2]*.6), xytext=(2.6, .2), fontsize=7.5, color=BLUE,
            arrowprops=dict(arrowstyle='-', color=BLUE, lw=.7))
ax.axvline(1.5, color=STROKE, lw=.85, ls=DASH)
ax.set_xticks(x); ax.set_ylim(0, .66); ax.set_yticks([0, .2, .4, .6])
ax.set_xlabel(r'$w$', labelpad=1); ax.set_ylabel('概率', labelpad=1)
tags(fig, axs)
Pc = sum(pc)
save(fig, HERE, 'figure', {'p': P, 'leader_weights': lw_, 'corrected_per_weight': cor, 'P_correct': Pc, 'P_error': 1-Pc})
