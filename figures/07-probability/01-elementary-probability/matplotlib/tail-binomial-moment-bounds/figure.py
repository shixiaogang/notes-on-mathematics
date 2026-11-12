from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# X ~ Bin(20,1/2): exact P(|X-10|>=t) and moment bounds m_p/t^p for p=2,4,6 (m_2=5, m_4=72.5, m_6=1692.5).
t = np.linspace(1, 10, 400); ti = np.arange(1, 11)
ex = np.array([2*bin_tail(10+int(j)) for j in ti])
fig, ax = figure(width_mm=96, height_mm=56)
for p, c in ((2, PURPLE), (4, YELLOW), (6, GREEN)):
    m = bin_central_moment(p)
    ax.semilogy(t, np.minimum(1, m/t**p), color=c, lw=1.4)
ax.semilogy(ti, ex, 'o', color=BLUE, ms=3.6, mew=0)
lab(ax, 9.6, 5/9.6**2*1.3, '$p=2$', PURPLE, ha='right', va='bottom')
lab(ax, 9.6, 72.5/9.6**4*1.3, '$p=4$', YELLOW, ha='right', va='bottom')
lab(ax, 9.6, 1692.5/9.6**6*.75, '$p=6$', GREEN, ha='right', va='top')
lab(ax, 7.2, 2*bin_tail(17)*.6, '精确值', BLUE, ha='left', va='top')
ax.axvline(5, color=RED, lw=.9, ls=DASH)
ax.set_xlim(1, 10); ax.set_ylim(1e-6, 1.5); logticks(ax, [0, -2, -4, -6]); ax.set_xticks(range(1, 11))
axlab(ax, '$t$', 'ℙ$(|X-10|\\geq t)$')
save(fig, HERE, 'figure', {'m2': bin_central_moment(2), 'm4': bin_central_moment(4), 'm6': bin_central_moment(6), 'exact_t5': float(2*bin_tail(15))})
