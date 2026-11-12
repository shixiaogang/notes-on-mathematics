from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: successive pairs (u_k, u_{k+1}) of pseudorandom numbers.
# (a) LCG s_{k+1} = (5 s_k + 1) mod 256, u_k = s_k/256, seed s_0 = 7, full period 256: pairs lie on 5 lines.
# (b) numpy PCG64 generator, seed 7, 256 pairs.
m, a, c, s = 256, 5, 1, 7
seq = []
for k in range(m+1):
    seq.append(s); s = (a*s+c) % m
assert len(set(seq[:m])) == m and seq[m] == seq[0]
u = np.array(seq)/m
v = np.random.default_rng(7).random(m+1)
fig, (A, B) = figure(width_mm=104, height_mm=56, ncols=2)
for ax, w, L in ((A, u, 'a'), (B, v, 'b')):
    style(ax)
    ax.plot(w[:-1], w[1:], 'o', ms=1.7, color=GREEN, mec='none')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect('equal')
    ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
    ax.set_ylabel('$u_{k+1}$'); sub(ax, L, '$u_k$')
save(fig, HERE(__file__), 'figure', {'lcg': 'm=256,a=5,c=1,s0=7', 'period': m, 'numpy_seed': 7})
