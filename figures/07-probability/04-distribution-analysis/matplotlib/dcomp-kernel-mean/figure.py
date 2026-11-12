from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Gaussian kernel k(x,y)=exp(-(x-y)^2/2) (sigma=1), running example on {0,1,2}.
# (a) kernel means m_P(y)=sum_i p_i k(x_i,y) (blue), m_Q (yellow); thin dotted: weighted sections p_i k(x_i,.).
# (b) witness g*=(m_P-m_Q)/MMD with MMD=sqrt(0.18(1-e^{-2}))=0.3945; red dots g*(x_i).
p, q, xs = P_EX, Q_EX, X_EX
y = np.linspace(-2.5, 4.5, 800)
Ky = gauss_kernel(xs, y)
mP, mQ = p@Ky, q@Ky
mmd = math.sqrt((p-q)@gauss_kernel(xs, xs)@(p-q))
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.26, wspace=.3)
ax = axs[0]
for pi, row in zip(p, Ky):
    ax.plot(y, pi*row, color=BLUE, lw=.8, ls=DOT)
ax.plot(y, mP, color=BLUE, lw=1.4)
ax.plot(y, mQ, color=YELLOW, lw=1.6)
for xi in xs:
    ax.plot([xi, xi], [0, .02], color=STROKE, lw=.85)
lab(ax, -1.2, .62, '$m_P$', BLUE, ha='center', fontsize=8)
lab(ax, 3.5, .5, '$m_Q$', YELLOW, ha='center', fontsize=8)
ax.set_xlim(-2.5, 4.5); ax.set_ylim(0, .9); ax.set_yticks([0, .4, .8])
axlab(ax, '$y$', None)
ax = axs[1]
w = (mP-mQ)/mmd
ax.axhline(0, color=STROKE, lw=.85)
ax.plot(y, w, color=BLUE, lw=1.4)
wx = (p-q)@gauss_kernel(xs, xs)/mmd
for xi, v in zip(xs, wx):
    dot(ax, xi, v, RED, ms=4)
    lab(ax, xi+.12, v+(.06 if v >= 0 else -.12), '0' if abs(v) < 1e-9 else f'{v:.3f}', RED, ha='left')
ax.set_xlim(-2.5, 4.5); ax.set_ylim(-.95, .95); ax.set_yticks([-.8, -.4, 0, .4, .8])
axlab(ax, '$y$', r'$g^{*}(y)$')
tags(fig, axs)
save(fig, HERE, 'figure', {'mmd': mmd, 'mP_at_x': (p@gauss_kernel(xs, xs)).tolist(),
                            'mQ_at_x': (q@gauss_kernel(xs, xs)).tolist(), 'witness_at_x': wx.tolist(),
                            'EPg-EQg': float((p-q)@wx)})
