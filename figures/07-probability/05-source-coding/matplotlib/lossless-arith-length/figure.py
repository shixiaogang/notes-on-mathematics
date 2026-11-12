from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
# One message of length 400 drawn i.i.d. from p = (0.4,0.3,0.2,0.1) (numpy default_rng seed 7). For each prefix
# length n: (a) per-symbol arithmetic code length ell_n/n, ell_n = ceil(-log2 q(x_{1:n})) + 1, under the true model
# q = p (green) and the uniform model q = u (yellow, exactly 2 + 1/n); blue: H(p); purple dashed: H + D(p||u) = 2.
# (b) overhead ell_n - (-log2 p(x_{1:n})) in bits for the true model; it always lies in [1, 2).
rng = np.random.default_rng(7); N = 400
x = rng.choice(4, size=N, p=P)
cl = np.cumsum(-np.log2(P[x])); n = np.arange(1, N+1)
ell = np.ceil(cl - 1e-9) + 1
ellu = 2*n + 1
fig, (a1, a2) = figure(width_mm=110, height_mm=50, ncols=2)
panel(fig, left=.1, right=.98, bottom=.27, top=.95, wspace=.3)
a1.axhline(2, color=PURPLE, lw=1.1, ls=DASH)
a1.axhline(H, color=BLUE, lw=1.4)
a1.plot(n, ellu/n, color=YELLOW, lw=1.5)
a1.plot(n, ell/n, color=GREEN, lw=1.1)
a1.set_xscale('log'); a1.set_xlim(1, N); a1.set_ylim(1.4, 3.4)
a1.minorticks_off(); a1.set_xticks([1, 10, 100]); a1.set_xticklabels(['$1$', '$10$', '$10^{2}$'])
lab(a1, 30, H-.18, r'$H(p)$', BLUE); lab(a1, 30, 2.06, r'$H+D(p\Vert u)$', PURPLE)
lab(a1, 2.2, 3.05, '均匀模型', YELLOW); lab(a1, 1.3, 1.62, '真实模型', GREEN)
a1.set_xlabel('$n$', labelpad=1); a1.set_ylabel('bit/符号', labelpad=1)
a2.plot(n, ell-cl, color=GREEN, lw=.0, marker='o', ms=1.3, mew=0)
a2.axhline(1, color=STROKE, lw=.85, ls=DOT); a2.axhline(2, color=PURPLE, lw=1.1, ls=DASH)
a2.set_xlim(0, N); a2.set_ylim(.6, 2.4); a2.set_yticks([1, 2])
a2.set_xlabel('$n$', labelpad=1); a2.set_ylabel('bit', labelpad=1)
tags(fig, (a1, a2))
save(fig, HERE, 'figure', {'seed': 7, 'N': N, 'ell_over_n_at_N': float(ell[-1]/N), 'H': H,
     'overhead_min': float((ell-cl).min()), 'overhead_max': float((ell-cl).max())})
