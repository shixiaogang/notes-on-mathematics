from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# energy J(v)=1/2 int v'^2-int v, Dirichlet f=1.
tent = lambda s: s*np.minimum(X, 1-X)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, wspace=.3, bottom=.27)
ax = axes[0]
c1 = 4/np.pi**3
ax.plot(X, tent(.25), color=YELLOW, lw=1.5); ax.plot(X, c1*np.sin(np.pi*X), color=PURPLE, lw=1.3); ax.plot(X, X*(1-X)/2, color=BLUE, lw=1.4)
lab(ax, .5, .04, r'$\frac{1}{4}\min(x,1-x)$', YELLOW, ha='center', fontsize=7.5); lab(ax, .78, .107, r'$\frac{4}{\pi^3}\sin\pi x$', PURPLE); lab(ax, .5, .134, r'$u_{*}$', BLUE, ha='center', va='bottom')
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.003, .155); ax.set_xticks([0, 1]); ax.set_yticks([0, .125]); ax.set_yticklabels(['0', '1/8']); hat01(ax)
ax = axes[1]
c = np.linspace(-.1, 1.1, 400)
J = c**2/6-c/6
ax.plot(c, J, color=BLUE, lw=1.4); dot(ax, .5, -1/24)
ax.axhline(-1/32, color=YELLOW, lw=1.2, ls=DASH); ax.axhline(-4/np.pi**4, color=PURPLE, lw=1.1, ls=DOT)
ax.set_xlim(-.1, 1.1); ax.set_ylim(-.05, .03); ax.set_xticks([0, .5, 1]); ax.set_yticks([-.04, -.02, 0, .02]); hat01(ax, '$c$', r'$J(c\,x(1-x))$')
tags(fig, axes)
xx = np.linspace(0, 1, 200001)
def J_of(v):
    dv = np.gradient(v, xx); return float(.5*np.trapezoid(dv**2, xx)-np.trapezoid(v, xx))
vals = {'exact': J_of(xx*(1-xx)/2), 'tent': J_of(.25*np.minimum(xx, 1-xx)), 'sin': J_of(c1*np.sin(np.pi*xx))}
print(vals, -1/24, -1/32, -4/np.pi**4)
save(fig, HERE, 'figure', vals)
