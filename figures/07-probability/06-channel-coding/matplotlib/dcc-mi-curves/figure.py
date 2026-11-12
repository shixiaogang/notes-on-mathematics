from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Mutual information I(X;Y) in bits as a function of the input probability q = P(X=1) for three fixed channels:
# BSC(0.1), BEC(0.25), Z-channel (1 -> 0 with probability 1/2). Red dots mark the maxima (the capacities).
q = np.linspace(0, 1, 801)
chans = [('BSC', bsc(BSC_P), BLUE), ('BEC', bec(BEC_E), GREEN), ('Z', Z, YELLOW)]
fig, ax = figure(width_mm=92, height_mm=52)
panel(fig, left=.13, right=.97, top=.95, bottom=.18)
facts = {}
for name, W, col in chans:
    I = np.array([mi(np.array([1-t, t]), W) for t in q])
    k = I.argmax(); ax.plot(q, I, color=col, lw=1.4 if name != 'Z' else 1.6)
    dot(ax, q[k], I[k]); facts[name] = {'argmax_q': float(q[k]), 'capacity': float(I[k]), 'I_uniform': float(I[400])}
lab(ax, .3, .76, r'BEC $\varepsilon=0.25$', GREEN, ha='center')
lab(ax, .3, .53, r'BSC $p=0.1$', BLUE, ha='center')
lab(ax, .72, .28, 'Z 信道', YELLOW)
lab(ax, .36, facts['Z']['capacity']+.04, r'$q=0.4$', RED, ha='center')
ax.axvline(.5, color=STROKE, lw=.6, ls=DOT)
ax.set_xlim(0, 1); ax.set_ylim(0, .88); ax.set_xlabel(r'$q$', labelpad=1); ax.set_ylabel(r'$I(X;Y)$ / bit', labelpad=1)
save(fig, HERE, 'figure', facts)
