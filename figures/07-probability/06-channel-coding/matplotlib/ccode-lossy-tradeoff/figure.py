from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ccode-common"))
from ccode_fig import *
# Uniform binary source, Hamming distortion, over BSC(0.1). R(D) = 1 - h2(D) on [0, 1/2], C = 1 - h2(0.1).
# Blue: the smallest asymptotically attainable distortion D*(r) solving r R(D) = C (D* = 0 for r <= C);
#       the region below it (red fill) is excluded by the converse r R(D) <= C.
# Green points (exact): repetition 3 and 5 per bit, [7,4,3] Hamming per-bit error, and "send one bit of two, guess
# the other" at r = 2.  Red point: uncoded transmission r = 1, D = 0.1, which already lies on the curve.
C = float(1-h2(P))
rs = np.linspace(0, 2.5, 500)
Ds = np.array([0.0 if r <= C else h2inv(1-C/r) for r in rs])
fig, ax = figure(width_mm=96, height_mm=54)
panel(fig, left=.12, right=.97, top=.96, bottom=.18)
ax.fill_between(rs, 0, Ds, color=RED_FILL, lw=0)
ax.plot(rs, Ds, color=BLUE, lw=1.4)
pts = [(1/5, tail(5, 2, P)), (1/3, tail(3, 1, P)), (4/7, ham_ber(P)), (2.0, (P+.5)/2)]
for x, y in pts:
    ax.plot([x], [y], 'o', ms=4, color=GREEN, mew=0, zorder=5)
dot(ax, 1.0, P)
for (x, y), s, xt in zip(pts[:3], ['五次重复', '三次重复', 'Hamming'], [(.02, .10), (.17, .16), (.62, .18)]):
    ax.annotate(s, xy=(x, y), xytext=xt, fontsize=7.5, color=GREEN, arrowprops=dict(arrowstyle='-', color=GREEN, lw=.7))
lab(ax, 1.72, .325, '发一猜一', GREEN)
lab(ax, .9, .13, '不编码', RED)
lab(ax, 1.6, .215, r'$D^{*}(r)$', BLUE); lab(ax, 1.75, .08, '不可达', RED)
ax.axvline(C, color=STROKE, lw=.85, ls=DASH); lab(ax, C+.03, .45, r'$r=C$', MUTED)
ax.set_xlim(0, 2.5); ax.set_ylim(0, .5)
ax.set_xlabel(r'$r=k/n$', labelpad=1); ax.set_ylabel('每源比特平均失真', labelpad=1)
save(fig, HERE, 'figure', {'C': C, 'points': [(float(x), float(y)) for x, y in pts], 'Dstar_r2': h2inv(1-C/2),
     'Dstar_r4/7': h2inv(1-C/(4/7))})
