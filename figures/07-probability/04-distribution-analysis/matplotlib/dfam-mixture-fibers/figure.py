"""Redundancy and overlap. (a) slice mu2=0 of w N(mu1,1)+(1-w)N(0,1): representations of N(0,1) are mu1=0 (any w) and w=0 (any mu1); green (0.5,1.5).
(b) 0.5N(-0.5,1)+0.5N(0.5,1) vs N(0,1.25) and 10x their difference."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

fig, (a, b) = figure(width_mm=108, height_mm=48, ncols=2)
a.plot([0, 1], [0, 0], color=RED, lw=2.0)
a.plot([0, 0], [-3, 3], color=RED, lw=2.0)
a.scatter([0.5], [1.5], s=18, color=GREEN, zorder=4)
a.text(0.55, 1.65, r'$(0.5,\,1.5)$', fontsize=7.5)
a.text(0.55, -0.45, r'$\mu_1=0$', color=RED, fontsize=7.5, ha='center')
a.text(0.05, 2.5, r'$w=0$', color=RED, fontsize=7.5)
a.set_xlim(-0.05, 1.05); a.set_ylim(-3, 3); a.set_xlabel('$w$', labelpad=1); a.set_ylabel(r'$\mu_1$', labelpad=1)
x = np.linspace(-4.5, 4.5, 901)
mix = 0.5*phi(x+0.5)+0.5*phi(x-0.5)
nn = phi(x/np.sqrt(1.25))/np.sqrt(1.25)
b.plot(x, mix, color=BLUE, lw=1.4)
b.plot(x, nn, color=YELLOW, lw=1.4, ls='--')
off = -0.06
b.axhline(off, color=GRID, lw=0.6)
b.plot(x, off+10*(mix-nn), color=STROKE, lw=1.0)
b.text(-4.4, off+0.022, '10倍差值', fontsize=7.5, ha='left', color=STROKE)
b.set_xlim(-4.5, 4.5); b.set_ylim(-0.125, 0.42); b.set_yticks([0, 0.1, 0.2, 0.3, 0.4]); b.set_xlabel('$x$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, HERE, 'figure', {'max_abs_diff': float(np.abs(mix-nn).max()), 'peak': float(mix.max()), 'ratio': float(np.abs(mix-nn).max()/mix.max())})
