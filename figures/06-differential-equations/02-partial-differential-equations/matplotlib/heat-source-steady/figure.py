from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Constant source f=1 on (0,1), zero ends: approach to steady state x(1-x)/2.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.105, wspace=.3, bottom=.27)
k = np.arange(1, 1601, 2); lam = (k*pi)**2; fk = 2*np.sqrt(2)/(k*pi)
def U(t, x=X): return (fk[:, None]/lam[:, None]*(1-np.exp(-lam*t))[:, None]*np.sqrt(2)*np.sin(np.outer(k, pi*np.atleast_1d(x)))).sum(0)
ax = axes[0]; cc = shades(4)
ax.plot(X, X*(1-X)/2, color=YELLOW, lw=1.3, ls=DASH)
for t, c in zip((.02, .05, .1, .3), cc): ax.plot(X, U(t), color=c, lw=1.4)
lab(ax, .5, .134, '稳态', YELLOW, ha='center'); lab(ax, .5, .033, '$t=0.02$', cc[0], ha='center')
ax.set_xlim(0, 1); ax.set_ylim(0, .15); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .05, .1, .15]); ax.set_yticklabels(['0', '0.05', '0.1', '0.15']); axlab(ax, yl='$u$')
ax = axes[1]; T = np.linspace(0, .3, 300)
for kk, c in zip((1, 3, 5), (BLUE, YELLOW, PURPLE)): ax.plot(T, 1-np.exp(-(kk*pi)**2*T), color=c, lw=1.4)
lab(ax, .155, .62, '$k=1$', BLUE, ha='left'); lab(ax, .03, .72, '$k=3$', YELLOW, ha='left'); 
ax.set_xlim(0, .3); ax.set_ylim(0, 1.2); ax.set_xticks([0, .1, .2, .3]); ax.set_yticks([0, 1]); axlab(ax, '$t$', r'$a_k(t)\lambda_k/f_k$')
lab(ax, .008, 1.06, '$k=5$', PURPLE, ha='left')
tags(fig, axes)
save(fig, HERE, 'figure', {'center': {t: float(U(t, .5)[0]) for t in (.05, .1, .2, .5)}})
