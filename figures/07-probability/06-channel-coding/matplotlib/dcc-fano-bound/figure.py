from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Weak converse for BSC(0.1), C = 0.531: every code with M >= 2^{nR} messages has average error
#   Pe >= 1 - C/R - 1/(nR).  Curves (clipped at 0) for n = 20, 100 and the limit n -> infinity, as functions of R.
p = BSC_P; C = 1-float(h2(p))
R = np.linspace(.05, 1, 600)
fig, ax = figure(width_mm=90, height_mm=50)
panel(fig, left=.14, right=.97, top=.95, bottom=.2)
for n, col in ((20, YELLOW), (100, GREEN), (None, BLUE)):
    v = 1 - C/R - (0 if n is None else 1/(n*R)); ax.plot(R, np.maximum(v, 0), color=col, lw=1.4)
ax.axvline(C, color=PURPLE, lw=1.0, ls=DASH)
lab(ax, C-.02, .4, r'$C$', PURPLE, ha='right')
lab(ax, .93, .48, r'$n\to\infty$', BLUE, ha='center'); lab(ax, .93, .31, r'$n=100$', GREEN, ha='center'); lab(ax, .8, .1, r'$n=20$', YELLOW, ha='center')
ax.set_xlim(0, 1); ax.set_ylim(0, .55); ax.set_xlabel(r'$R$', labelpad=1); ax.set_ylabel(r'$P_{\mathrm{e}}$', labelpad=1)
save(fig, HERE, 'figure', {'C': C, 'bound_R1_inf': 1-C, 'bound_R1_n100': 1-C-1/100})
