from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: two fair dice, 36 equally likely outcomes; the sum S and the maximum M are two records of the same trial.
# Panel (a): outcome grid, event {S=7} (anti-diagonal) and event {M=4} (L-shape). Panels (b),(c): exact mass tables.
fig, axs = figure(width_mm=112, height_mm=46, ncols=3, gridspec_kw={'width_ratios': [1.0, 1.15, 1.15]})
ax = axs[0]; style(ax)
for i in range(1, 7):
    for j in range(1, 7):
        s7 = i + j == 7; m4 = max(i, j) == 4
        if m4:
            ax.plot(i, j, 's', ms=6.4 if s7 else 4.2, mfc=YELLOW_FILL, mec=YELLOW, mew=1.0, zorder=3)
        if s7:
            ax.plot(i, j, 'o', ms=4.6, color=BLUE, zorder=4)
        elif not m4:
            ax.plot(i, j, 'o', ms=2.4, color=MUTED, zorder=2)
ax.plot([.6, 6.4], [6.4, .6], color=BLUE, lw=.85, ls=(0, (3, 2)), zorder=1)
ax.set_xlim(.4, 6.6); ax.set_ylim(.4, 6.6); ax.set_aspect('equal')
ax.set_xticks(range(1, 7)); ax.set_yticks(range(1, 7))
ax.set_ylabel('第二枚')
sub(ax, 'a', '第一枚')
S = np.arange(2, 13); pS = (6 - np.abs(S - 7)) / 36
ax = axs[1]; style(ax)
bars(ax, S, pS)
ax.bar([7], [pS[5]], width=.55, color=BLUE, edgecolor=BLUE, linewidth=.9)
ax.set_xticks([2, 4, 7, 10, 12]); ax.set_ylim(0, .3)
ax.set_yticks([1/36, 6/36]); ax.set_yticklabels(['1/36', '6/36'])
ax.set_ylabel('$p_S(s)$')
sub(ax, 'b', '$s$')
M = np.arange(1, 7); pM = (2*M - 1) / 36
ax = axs[2]; style(ax)
bars(ax, M, pM, color=YELLOW, fill=YELLOW_FILL)
ax.bar([4], [pM[3]], width=.55, color=YELLOW, edgecolor=YELLOW, linewidth=.9)
ax.set_xticks(M); ax.set_ylim(0, .34)
ax.set_yticks([1/36, 7/36, 11/36]); ax.set_yticklabels(['1/36', '7/36', '11/36'])
ax.set_ylabel('$p_M(m)$')
sub(ax, 'c', '$m$')
assert abs(pS.sum() - 1) < 1e-12 and abs(pM.sum() - 1) < 1e-12
save(fig, HERE(__file__), 'figure', {'pS': (pS*36).tolist(), 'pM_times36': (pM*36).tolist()})
