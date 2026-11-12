from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
# Blocks of n symbols from p = (0.4,0.3,0.2,0.1), n = 1..6 (codebook size 4^n up to 4096).
# (a) per-symbol average length of the Huffman code on blocks (green dots) and of the Shannon block code
# ceil(-log2 p(x_{1:n})) (yellow dots), with H (blue) and H + 1/n (purple dashed).
# (b) shortest and longest Huffman codeword (green, filled / open) against the fixed length 2n (gray dotted).
ns = np.arange(1, 7); Lh, Ls, mx, mn = [], [], [], []
for n in ns:
    Pb = block_probs(n); L = huffman_lengths(Pb)
    Lh.append((Pb*L).sum()/n); Ls.append((Pb*np.ceil(-np.log2(Pb)-1e-12)).sum()/n); mx.append(L.max()); mn.append(L.min())
fig, (a1, a2) = figure(width_mm=110, height_mm=52, ncols=2)
panel(fig, left=.1, right=.98, bottom=.27, top=.95, wspace=.3)
nn = np.linspace(1, 6, 200)
a1.plot(nn, H+1/nn, color=PURPLE, lw=1.1, ls=DASH)
a1.axhline(H, color=BLUE, lw=1.4)
a1.plot(ns, Ls, 'o', color=YELLOW, ms=4, mew=0)
a1.plot(ns, Lh, 'o', color=GREEN, ms=4, mew=0)
a1.set_xlim(.7, 6.3); a1.set_ylim(1.8, 2.9); a1.set_xticks(ns)
lab(a1, 2.4, 2.45, r'$H+1/n$', PURPLE); lab(a1, 4.2, H-.06, r'$H$', BLUE, va='top')
lab(a1, 1.3, 2.36, 'Shannon', YELLOW); lab(a1, 1.3, 1.95, 'Huffman', GREEN)
a1.set_xlabel('$n$', labelpad=1); a1.set_ylabel('bit/符号', labelpad=1)
a2.plot(ns, 2*ns, color=STROKE, lw=.85, ls=DOT, marker='s', ms=2.5)
a2.plot(ns, mx, 'o', color=GREEN, ms=4, mew=0)
a2.plot(ns, mn, 'o', color=GREEN, ms=4, mfc='white', mew=.9)
a2.set_xlim(.7, 6.3); a2.set_ylim(0, 21); a2.set_xticks(ns)
lab(a2, 4.1, 6.2, '最短', GREEN); lab(a2, 3.3, 13.0, '最长', GREEN); lab(a2, 5.0, 8.0, r'$2n$', STROKE)
a2.set_xlabel('$n$', labelpad=1); a2.set_ylabel('bit', labelpad=1)
tags(fig, (a1, a2))
save(fig, HERE, 'figure', {'per_symbol_huffman': [float(v) for v in Lh], 'per_symbol_shannon': [float(v) for v in Ls],
     'max_len': [int(v) for v in mx], 'min_len': [int(v) for v in mn], 'H': H})
