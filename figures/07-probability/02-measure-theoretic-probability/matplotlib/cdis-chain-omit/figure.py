"""Random coin, three flips: true P(x1,x2,x3) = s!(3-s)!/4! (blue) vs the product that drops X1 in the
third factor, 1/2 * q(x2|x1) * q(x3|x2) with q(1|1)=2/3, q(1|0)=1/3 (yellow)."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
HERE = Path(__file__).resolve().parent
seqs = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
true = [math.factorial(sum(s))*math.factorial(3 - sum(s))/24 for s in seqs]
def q(a, b): p1 = (1 + b)/3; return p1 if a == 1 else 1 - p1
wrong = [0.5*q(s[1], s[0])*q(s[2], s[1]) for s in seqs]
fig, ax = figure(width_mm=104, height_mm=44)
idx = np.arange(8)
ax.bar(idx - 0.19, true, width=0.36, color=BLUE_FILL, edgecolor=BLUE, lw=0.8)
ax.bar(idx + 0.19, wrong, width=0.36, color=YELLOW_FILL, edgecolor=YELLOW, lw=0.8)
ax.set_xticks(idx); ax.set_xticklabels([''.join(map(str, s)) for s in seqs])
ax.set_yticks([0, 1/12, 1/9, 2/9, 1/4]); ax.set_yticklabels(['0', '1/12', '1/9', '2/9', '1/4'])
ax.set_xlim(-0.6, 7.6); ax.set_ylim(0, 0.27); ax.set_xlabel('$x_1x_2x_3$', labelpad=1)
save(fig, HERE, 'figure', {'true': true, 'omitted': wrong, 'sum_true': sum(true), 'sum_omitted': sum(wrong)})
