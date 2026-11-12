from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
# Actual source p = (0.4,0.3,0.2,0.1); design model q_t = (1-t) p + t r with r = (0.1,0.2,0.3,0.4).
# Average length under p of the Shannon code designed for q_t (yellow), of the Huffman code designed for q_t
# (green), and the curves H(p)+D(p||q_t) (blue) and H(p)+D(p||q_t)+1 (purple dashed);
# at t=1 the Huffman code for r has lengths (3,3,2,1) giving 0.4*3+0.3*3+0.2*2+0.1*1 = 2.6.
r = P[::-1]
ts = np.linspace(0, 1, 801)
Ls, Lh, D = [], [], []
for t in ts:
    q = (1-t)*P + t*r
    Ls.append(float((P*np.ceil(-np.log2(q)-1e-12)).sum()))
    Lh.append(float((P*huffman_lengths(q)).sum()))
    D.append(float((P*np.log2(P/q)).sum()))
Ls, Lh, D = map(np.array, (Ls, Lh, D))
fig, ax = figure(width_mm=96, height_mm=54)
panel(fig, left=.11, right=.97, bottom=.2, top=.95)
ax.plot(ts, H+D+1, color=PURPLE, lw=1.1, ls=DASH)
ax.plot(ts, Ls, color=YELLOW, lw=1.5)
ax.plot(ts, Lh, color=GREEN, lw=1.4)
ax.plot(ts, H+D, color=BLUE, lw=1.4)
ax.axhline(H, color=STROKE, lw=.85, ls=DOT)
dot(ax, 0, Lh[0]); dot(ax, 1, Lh[-1])
ax.set_xlim(0, 1); ax.set_ylim(1.7, 3.8)
lab(ax, .72, H-.05, r'$H(p)=1.846$', STROKE, ha='center', va='top')
lab(ax, .62, (H+D+1)[500]+.1, r'$H+D+1$', PURPLE)
lab(ax, .66, 2.3, r'$H+D(p\Vert q_t)$', BLUE, ha='center')
lab(ax, .1, 2.48, 'Shannon码', YELLOW, ha='center')
lab(ax, .3, 2.05, 'Huffman码', GREEN, ha='center')
lab(ax, .025, Lh[0]+.05, '1.9', RED); lab(ax, .97, Lh[-1]+.07, '2.6', RED, ha='right')
ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('bit', labelpad=1)
save(fig, HERE, 'figure', {'L_huff_t0': Lh[0], 'L_huff_t1': Lh[-1], 'D_t1': D[-1], 'L_shannon_t1': Ls[-1]})
