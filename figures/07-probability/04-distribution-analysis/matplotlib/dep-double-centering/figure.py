"""Three-point parabola (X uniform on {-1,0,1}, Y = X^2): pairwise distance matrices A = |x_i - x_j|, B = |y_i - y_j|
and their double-centred versions (row/column means removed, grand mean added back), entries shown as multiples of 1/9.
A, B: white-to-blue; centred matrices: red-white-blue diverging with midpoint 0.  dCov^2 = (1/9) sum A~ B~ = 8/81."""
from pathlib import Path
import sys
from fractions import Fraction
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

x = np.array([-1, 0, 1]); y = x**2
A = np.abs(x[:, None]-x[None, :]).astype(object); B = np.abs(y[:, None]-y[None, :]).astype(object)
def dc(M):
    M = np.array([[Fraction(int(v)) for v in row] for row in M], dtype=object)
    r = [sum(M[i])/3 for i in range(3)]; g = sum(r)/3
    return np.array([[M[i, j]-r[i]-r[j]+g for j in range(3)] for i in range(3)], dtype=object)
At, Bt = dc(A), dc(B)
dcov2 = sum(At[i, j]*Bt[i, j] for i in range(3) for j in range(3))/9
wb = LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE_FILL, BLUE])
rwb = LinearSegmentedColormap.from_list('rwb', [RED, RED_FILL, '#FFFFFF', BLUE_FILL, BLUE])
fig, axs = figure(width_mm=112, height_mm=34, ncols=4)
def fmt(v, centred):
    v = Fraction(v)
    if not centred:
        return str(v)
    n = v*9
    return str(int(n)) if n.denominator == 1 else str(n)
for ax, M, centred, lab in [(axs[0], A, False, '(a)'), (axs[1], At, True, '(b)'), (axs[2], B, False, '(c)'), (axs[3], Bt, True, '(d)')]:
    F = np.array(M, dtype=float)
    if centred:
        ax.imshow(F, cmap=rwb, norm=TwoSlopeNorm(0, -1.2, 1.2))
    else:
        ax.imshow(F, cmap=wb, vmin=0, vmax=2.4)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, fmt(M[i, j], centred), ha='center', va='center', fontsize=7.5, color=INK)
    ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
    lbl = ['$-1$', '$0$', '$1$']
    ax.set_xticklabels(lbl); ax.set_yticklabels(lbl)
    ax.tick_params(length=0)
    for sp in ax.spines.values(): sp.set_visible(False)
    tag(ax, lab, y=-.2)
save(fig, HERE, 'figure', {'A_tilde_times_9': [[str(v*9) for v in r] for r in At], 'B_tilde_times_9': [[str(v*9) for v in r] for r in Bt], 'dCov2': str(dcov2)})
