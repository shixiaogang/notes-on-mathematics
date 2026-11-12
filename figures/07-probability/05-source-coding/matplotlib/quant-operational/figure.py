from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Mean squared error against description rate (bits per sample) for Laplace(0,1):
# yellow squares: best fixed-length mid-rise uniform quantizer with N = 2^R levels (step by grid search);
# green circles: fixed-length Lloyd-Max with N = 2^R; blue curve: infinite mid-tread uniform quantizer, rate = index entropy H(J);
# purple dashed: high-resolution formula (2e)^2/12 * 2^{-2R}; red points: Lloyd-Max N=4 with Huffman index code
# (average length 1.8048) and with ideal length H(J) = 1.7286.
Rs = np.arange(1, 6)
Du, Dl = [], []
for R in Rs:
    N = 2**R; ds = np.linspace(.05, 4, 8001)
    Du.append(min(sum(uniform_parts(N, d)) for d in ds))
    Dl.append(lloyd(np.linspace(-1.5, 1.5, N)*(4/N)**.3, 4000)[-1][2])
ds = np.exp(np.linspace(np.log(.045), np.log(6), 200))
HE = []; DE = []
for d in ds:
    p, D = midtread(d); HE.append(entropy_bits(p)); DE.append(D)
lm4 = lloyd([-1.5, -.5, .5, 1.5], 400)[-1]; e = [-math.inf]+list(lm4[0])+[math.inf]
p4 = [mass(e[j], e[j+1]) for j in range(4)]; H4 = entropy_bits(p4)
fig, ax = figure(width_mm=100, height_mm=58)
panel(fig, left=.11, right=.99, bottom=.15, top=.97)
rr = np.linspace(.5, 5.1, 100)
ax.plot(rr, (2*math.e)**2/12*2.0**(-2*rr), color=PURPLE, lw=1.1, ls=DASH)
ax.plot(HE, DE, color=BLUE, lw=1.4)
ax.plot(Rs, Du, 's-', color=YELLOW, lw=1.3, ms=3.6)
ax.plot(Rs, Dl, 'o-', color=GREEN, lw=1.1, ms=3.4)
dot(ax, 1.8048, lm4[2]); dot(ax, H4, lm4[2], ms=3.2)
lab(ax, 5.12, Du[-1], '定长均匀', YELLOW, va='center'); lab(ax, 5.12, Dl[-1], '定长 Lloyd–Max', GREEN, va='center')
lab(ax, 1.25, .045, '均匀+熵编码', BLUE)
ax.set_yscale('log'); ax.set_xlim(.5, 6.6); ax.set_ylim(.002, 2.2); ax.minorticks_off()
ax.set_yticks([.01, .1, 1]); ax.set_yticklabels(['$10^{-2}$', '$10^{-1}$', '$1$'])
ax.set_xticks([1, 2, 3, 4, 5]); ax.spines['bottom'].set_bounds(.5, 5.2); ax.set_xlabel('每样本 bit', labelpad=1); ax.set_ylabel('$D$', labelpad=1)
save(fig, HERE, 'figure', {'uniform_fixed': dict(zip(map(int, Rs), map(float, Du))), 'lloyd_fixed': dict(zip(map(int, Rs), map(float, Dl))),
     'lm4_D': float(lm4[2]), 'lm4_H': H4, 'lm4_p': p4,
     'ec_at_H_near_2': [(float(h), float(D)) for h, D in zip(HE, DE) if 1.7 < h < 2.6][::6]})
