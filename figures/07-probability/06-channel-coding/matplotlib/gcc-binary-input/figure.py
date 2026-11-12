from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Information rates against s = P/sigma^2 (dB) for sigma^2 = 1:
#   blue: Gaussian input, capacity 0.5 log2(1+s);
#   yellow: equiprobable binary input +-sqrt(s), real output (numerical integration);
#   purple: same binary input followed by sign decisions -> BSC with p = Q(sqrt(s)), rate 1 - h2(p).
# Red dots at s = 3 (4.77 dB): 1.000, 0.845, 0.750.
db = np.linspace(-10, 20, 121); s = 10**(db/10)
cg = cap(s)
cb = np.array([binary_input_capacity(v) for v in s])
ch = 1-h2(Qf(np.sqrt(s)))
fig, ax = figure(width_mm=90, height_mm=50)
panel(fig, left=.12, right=.97, top=.95, bottom=.2)
ax.plot(db, ch, color=PURPLE, lw=1.3)
ax.plot(db, cb, color=YELLOW, lw=1.5)
ax.plot(db, cg, color=BLUE, lw=1.4)
x3 = 10*math.log10(3)
v = [1.0, binary_input_capacity(3.0), float(1-h2(Qf(math.sqrt(3.0))))]
for t in v:
    dot(ax, x3, t)
ax.set_xlim(-10, 20); ax.set_ylim(0, 2.0); ax.set_yticks([0, .5, 1, 1.5, 2])
ax.set_xlabel(r'$10\log_{10}(P/\sigma^2)$ (dB)', labelpad=1); ax.set_ylabel('bit/次', labelpad=2)
lab(ax, 9.5, 1.78, '高斯输入', BLUE)
lab(ax, 13.0, 1.07, '二点输入', YELLOW)
lab(ax, 9.0, .62, '二点输入+符号判决', PURPLE)
save(fig, HERE, 'figure', {'at_s=3': v})
