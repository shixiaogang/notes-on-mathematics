from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Renyi divergence D_alpha(P||Q) = ln(sum p^a q^(1-a))/(a-1) for the running example, alpha in (0,4];
# alpha=1 value is the KL limit 0.4 ln 2. Marked: alpha=1/2 (-2 ln B), 1 (KL), 2 (ln(1+chi^2)).
p, q = P_EX, Q_EX
a = np.linspace(.02, 4, 800)
a = a[np.abs(a-1) > 1e-9]
D = np.array([math.log(np.sum(p**t*q**(1-t)))/(t-1) for t in a])
KL = kl(p, q)
fig, ax = figure(width_mm=84, height_mm=52)
ax.plot(a, D, color=BLUE, lw=1.4)
marks = {.5: -2*math.log(np.sum(np.sqrt(p*q))), 1: KL, 2: math.log(1+np.sum((p-q)**2/q))}
for t, v in marks.items():
    dot(ax, t, v, RED, ms=4)
    ax.plot([t, t], [0, v], color=STROKE, lw=.7, ls=DOT)
lab(ax, .5+.06, marks[.5]-.045, f'{marks[.5]:.3f}', RED, ha='left', va='top')
lab(ax, 1-.05, KL+.03, f'{KL:.3f}', RED, ha='right', va='bottom')
lab(ax, 2+.05, marks[2]-.04, f'{marks[2]:.3f}', RED, ha='left', va='top')
ax.set_xlim(0, 4); ax.set_ylim(0, .62); ax.set_xticks([0, .5, 1, 2, 3, 4]); ax.set_xticklabels(['0', '1/2', '1', '2', '3', '4'])
ax.set_yticks([0, .2, .4, .6])
axlab(ax, r'$\alpha$', r'$D_{\alpha}(P\Vert Q)$')
save(fig, HERE, 'figure', {'marks': {str(k): float(v) for k, v in marks.items()}, 'D4': float(D[-1])})
