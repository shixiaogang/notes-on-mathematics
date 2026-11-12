from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Energy per letter |x^n|^2 / n of a random codeword with iid N(0, P') entries, P' = 2.4 = 0.8 P, budget P = 3.
# Exact law: P' * chi^2_n / n = Gamma(n/2, rate n/(2P')). Curves for n = 25 (yellow) and n = 400 (blue);
# red line: budget P; red fill: violation probability P(|x|^2 > nP) by numerical integration of the density.
Pp, P = 2.4, 3.0
t = np.linspace(1e-4, 6.5, 6500); dt = t[1]-t[0]
def dens(n):
    a = n/2; b = n/(2*Pp)
    return np.exp(a*np.log(b) + (a-1)*np.log(t) - b*t - math.lgamma(a))
fig, ax = figure(width_mm=88, height_mm=48)
panel(fig, left=.05, right=.97, top=.95, bottom=.2)
facts = {}
for n, col in ((25, YELLOW), (400, BLUE)):
    f = dens(n); m = t > P
    ax.fill_between(t[m], 0, f[m], color=RED_FILL, lw=0)
    ax.plot(t, f, color=col, lw=1.5 if n == 25 else 1.4)
    facts['P(violate), n=%d' % n] = float(f[m].sum()*dt)
ax.axvline(P, color=RED, lw=1.1); ax.axvline(Pp, color=STROKE, lw=.8, ls=DOT)
ax.set_xlim(0, 6.5); ax.set_ylim(0, 2.6); ax.set_yticks([]); ax.spines['left'].set_visible(False)
ax.set_xticks([0, 2.4, 3, 5]); ax.set_xticklabels(['0', r"$P'$", r'$P$', '5'])
ax.set_xlabel(r'$\Vert x^n\Vert_2^2/n$', labelpad=1)
lab(ax, 3.9, .45, r'$n=25$', YELLOW); lab(ax, 3.25, 2.0, r'$n=400$', BLUE)
save(fig, HERE, 'figure', facts)
