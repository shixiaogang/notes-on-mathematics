"""Gibbs reweighting on {0,1,2}: P uniform, V(x)=x, tau=1/ln2 so e^{-V/tau}=2^{-x}.
Bars: P (yellow), unnormalized P e^{-V/tau} = (1/3,1/6,1/12) (white, dashed grey edge), Q*=(4/7,2/7,1/7) (blue).
Z = 1/3+1/6+1/12 = 7/12."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

tau = 1/math.log(2)
w = U3*np.exp(-X3/tau); Z = w.sum(); Q = w/Z
fig, ax = figure(width_mm=80, height_mm=46)
b = 0.26
ax.bar(X3-b, U3, width=b, color=YELLOW_FILL, edgecolor=YELLOW, lw=0.9)
ax.bar(X3, w, width=b, color='white', edgecolor=STROKE, lw=0.8, ls='--')
ax.bar(X3+b, Q, width=b, color=BLUE_FILL, edgecolor=BLUE, lw=0.9)
for xi, (a, c, d) in enumerate(zip(U3, w, Q)):
    ax.text(xi-b, a+0.012, r'$\frac{1}{3}$', ha='center', va='bottom', fontsize=7.5, color=MUTED)
    ax.text(xi, c+0.012, [r'$\frac{1}{3}$', r'$\frac{1}{6}$', r'$\frac{1}{12}$'][xi], ha='center', va='bottom', fontsize=7.5, color=MUTED)
    ax.text(xi+b, d+0.012, [r'$\frac{4}{7}$', r'$\frac{2}{7}$', r'$\frac{1}{7}$'][xi], ha='center', va='bottom', fontsize=7.5, color=INK)
ax.set_xticks(X3); ax.set_xticklabels([r'$x=0$', r'$x=1$', r'$x=2$'])
ax.set_ylim(0, 0.68); ax.set_yticks([0, 0.2, 0.4, 0.6])
ax.text(1.55, 0.6, r'$P$', color=YELLOW, ha='left'); ax.text(1.55, 0.53, r'$P\,\mathrm{e}^{-V/\tau}$', color=STROKE, ha='left')
ax.text(1.55, 0.46, r'$Q^{*}$', color=BLUE, ha='left')
save(fig, HERE, 'figure', {'Z': float(Z), 'Qstar': Q.tolist(), 'weights': w.tolist()})
