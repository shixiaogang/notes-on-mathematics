from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Index entropy of the infinite mid-tread uniform quantizer of step delta for Laplace(0,1):
# exact H(J) in bits (blue) against the high-resolution approximation h(X) - log2(delta), h = log2(2e) (purple dashed).
# Red point: delta = 1.
ds = np.exp(np.linspace(np.log(.05), np.log(8), 300))
H = np.array([entropy_bits(midtread(d)[0]) for d in ds])
fig, ax = figure(width_mm=92, height_mm=50)
panel(fig, left=.11, right=.97, bottom=.18, top=.97)
ax.plot(ds, H_LAPLACE-np.log2(ds), color=PURPLE, lw=1.1, ls=DASH)
ax.plot(ds, H, color=BLUE, lw=1.4)
H1 = entropy_bits(midtread(1.0)[0]); dot(ax, 1.0, H1)
lab(ax, 1.1, H1+.25, '$\\Delta=1$', RED)
lab(ax, .13, 6.0, '$h(X)-\\log_2\\Delta$', PURPLE); lab(ax, 2.6, 1.75, '$H(J)$', BLUE)
ax.set_xscale('log'); ax.set_xlim(.05, 8); ax.set_ylim(0, 7.5); ax.minorticks_off()
ax.set_xticks([.0625, .25, 1, 4]); ax.set_xticklabels(['$1/16$', '$1/4$', '$1$', '$4$'])
ax.set_xlabel('$\\Delta$', labelpad=1); ax.set_ylabel('bit', labelpad=1)
facts = {'h_bits': H_LAPLACE}
for d in (.25, .5, 1, 2, 4):
    p, D = midtread(d); facts[f'H_{d}'] = entropy_bits(p); facts[f'D_{d}'] = D; facts[f'p0_{d}'] = float(p[len(p)//2])
save(fig, HERE, 'figure', facts)
