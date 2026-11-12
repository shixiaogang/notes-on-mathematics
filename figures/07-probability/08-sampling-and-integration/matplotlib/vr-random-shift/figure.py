from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Random shift of the Fibonacci lattice a_i = ((i-1)/13, frac(8(i-1)/13)), i = 1..13, by Delta = (0.37, 0.81):
# U_i = (a_i + Delta) mod 1 coordinatewise.  (a) a_i and the translated points a_i + Delta in [0,2)^2 with the four
# unit tiles; (b) the wrapped points U_i in [0,1)^2 over the original points.
n = 13; i = np.arange(n); A = np.stack([i/n, (8*i % n)/n], 1); D = np.array([.37, .81])
S = A + D; U = S % 1
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, left=.08, right=.98, bottom=.22, top=.97, wspace=.25)
a, b = axs
for t in (1,):
    a.plot([t, t], [0, 2], color=STROKE, lw=.6, ls=DASH); a.plot([0, 2], [t, t], color=STROKE, lw=.6, ls=DASH)
a.plot(A[:, 0], A[:, 1], 'o', ms=3.2, mfc='white', mec=INK, mew=.8, clip_on=False)
a.plot(S[:, 0], S[:, 1], 'o', ms=3.2, color=GREEN, mew=0)
a.annotate('', xy=D, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.1, mutation_scale=7))
lab(a, .03, .42, r'$\Delta$', RED)
a.set_xlim(0, 2); a.set_ylim(0, 2); a.set_aspect('equal'); a.set_xticks([0, 1, 2]); a.set_yticks([0, 1, 2])
axlab(a, '$u_1$', '$u_2$')
b.plot(A[:, 0], A[:, 1], 'o', ms=3.2, mfc='white', mec=INK, mew=.8, clip_on=False)
b.plot(U[:, 0], U[:, 1], 'o', ms=3.4, color=GREEN, mew=0)
b.set_xlim(0, 1); b.set_ylim(0, 1); b.set_aspect('equal'); b.set_xticks([0, .5, 1]); b.set_yticks([0, .5, 1])
axlab(b, '$u_1$')
tags(fig, axs)
save(fig, HERE, 'figure', {'Delta': D.tolist(), 'U': U.tolist()})
