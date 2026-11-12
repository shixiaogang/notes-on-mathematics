"""Equal-weight mixture 0.5N(-a,1)+0.5N(a,1), a in {0.5,1,1.5,2}; f_a(0)=(a^2-1)phi(a)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

x = np.linspace(-4.5, 4.5, 900)
fig, ax = figure(width_mm=104, height_mm=46)
rec = {}
for a_, c in [(0.5, BLUE), (1.0, YELLOW), (1.5, PURPLE), (2.0, GREEN)]:
    f = 0.5*phi(x+a_)+0.5*phi(x-a_)
    ax.plot(x, f, color=c, lw=1.4)
    rec[a_] = {'f0': float(0.5*phi(a_)*2), 'curv0': float((a_*a_-1)*phi(a_))}
ax.text(0, 0.372, r'$a=0.5$', color=BLUE, fontsize=7.5, ha='center', va='bottom')
ax.text(1.55, 0.31, r'$a=1$', color=YELLOW, fontsize=7.5)
ax.text(-3.1, 0.17, r'$a=1.5$', color=PURPLE, fontsize=7.5, ha='center')
ax.text(3.35, 0.15, r'$a=2$', color=GREEN, fontsize=7.5)
ax.set_xlim(-4.5, 4.5); ax.set_ylim(0, 0.42); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$f_a(x)$')
save(fig, HERE, 'figure', {'a_values': rec})
