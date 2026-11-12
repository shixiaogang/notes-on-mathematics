from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
# Running source p = (0.4,0.3,0.2,0.1): self-information -log2 p(x) (blue outline, light fill),
# Shannon lengths ceil(-log2 p(x)) (yellow) and Huffman lengths (green) for each symbol.
si = -np.log2(P); sh = np.ceil(si); hf = huffman_lengths(P)
x = np.arange(4); w = .26
fig, ax = figure(width_mm=86, height_mm=50)
panel(fig, left=.11, right=.97, bottom=.15, top=.95)
ax.bar(x-w, si, w*.92, color=BLUE_FILL, edgecolor=BLUE, lw=.8)
ax.bar(x, sh, w*.92, color=YELLOW_FILL, edgecolor=YELLOW, lw=1.0)
ax.bar(x+w, hf, w*.92, color=GREEN_FILL, edgecolor=GREEN, lw=.8)
for i in range(4):
    lab(ax, x[i]-w, si[i]+.08, '%.2f' % si[i], BLUE, ha='center', fontsize=6.8)
    lab(ax, x[i], sh[i]+.08, '%d' % sh[i], YELLOW, ha='center', fontsize=6.8)
    lab(ax, x[i]+w, hf[i]+.08, '%d' % hf[i], GREEN, ha='center', fontsize=6.8)
ax.set_xticks(x); ax.set_xticklabels(['$a$', '$b$', '$c$', '$d$'])
ax.set_ylim(0, 5.0); ax.set_yticks([0, 1, 2, 3, 4]); ax.set_xlim(-.6, 3.6)
ax.set_ylabel('bit', labelpad=1)
lab(ax, -.55, 4.7, r'$-\log_2 p(x)$', BLUE); lab(ax, 1.05, 4.7, 'Shannon码长', YELLOW); lab(ax, 2.35, 4.7, 'Huffman码长', GREEN)
save(fig, HERE, 'figure', {'self_info': si.tolist(), 'shannon': sh.tolist(), 'huffman': hf.tolist(),
     'H': H, 'L_shannon': float((P*sh).sum()), 'L_huffman': float((P*hf).sum())})
