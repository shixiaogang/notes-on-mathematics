"""Mixture parameters. (a) w2 in {0.5,0.7,0.9} for N(-1.5,1),N(1.5,1); (b) equal weights, second comp N(1.5,1),N(1.5,.25),N(2,.25)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

x = np.linspace(-4.5, 4.5, 900)
fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2)
for w, c in [(0.5, BLUE), (0.7, YELLOW), (0.9, PURPLE)]:
    a.plot(x, (1-w)*phi(x+1.5)+w*phi(x-1.5), color=c, lw=1.4)
a.text(1.5, 0.375, r'$0.9$', color=PURPLE, fontsize=7.5, ha='center', va='bottom')
a.text(2.55, 0.27, r'$0.7$', color=YELLOW, fontsize=7.5)
a.text(2.75, 0.16, r'$0.5$', color=BLUE, fontsize=7.5)
for (m, s), c in [((1.5, 1.0), BLUE), ((1.5, 0.5), YELLOW), ((2.0, 0.5), PURPLE)]:
    b.plot(x, 0.5*phi(x+1.5)+0.5*phi((x-m)/s)/s, color=c, lw=1.4)
b.text(1.1, 0.41, r'$\mathcal{N}(1.5,0.5^2)$', color=YELLOW, fontsize=7.5, ha='right')
b.text(2.35, 0.36, r'$\mathcal{N}(2,0.5^2)$', color=PURPLE, fontsize=7.5)
b.annotate(r'$\mathcal{N}(1.5,1)$', xy=(2.45, 0.5*phi(3.95)+0.5*phi(0.95)), xytext=(2.75, 0.24), color=BLUE, fontsize=7.5, arrowprops=dict(arrowstyle='-', color=BLUE, lw=0.8))
for ax_ in (a, b):
    ax_.set_xlim(-4.5, 4.5); ax_.set_xlabel('$x$', labelpad=1)
a.set_ylim(0, 0.45); b.set_ylim(0, 0.48)
a.set_ylabel('$f(x)$')
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, HERE, 'figure', {'a': 'weights of second component 0.5,0.7,0.9', 'b': 'second component varied'})
