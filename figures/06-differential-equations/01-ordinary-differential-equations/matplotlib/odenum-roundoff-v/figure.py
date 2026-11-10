from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: truncation vs rounding: Euler with state rounded to six decimals at every step.
T = 1.0; x1 = float(exact(T))
Ns = np.unique(np.round(2**np.linspace(1, 16, 46)).astype(int))
err, eperf = [], []
for n in Ns:
    h = T/n; x = y = X0
    for k in range(int(n)):
        x = round(x+h*x*(1-x), 6)
        y = y+h*y*(1-y)
    err.append(abs(x-x1)); eperf.append(abs(y-x1))
err = np.array(err); eperf = np.array(eperf); hs = T/Ns
fig, ax = figure(width_mm=92, height_mm=56)
ax.loglog(hs, eperf, color=GREEN, lw=1.2)
ax.loglog(hs, err, 'o', color=RED, ms=2.2)
ax.set_xlabel('步长 h'); ax.set_ylabel('终点误差')
ax.set_ylim(2e-6, .1)
ax.text(.012, 1.4e-4, '无舍入', color=GREEN, ha='left')
ax.text(5e-5, 4e-3, '每步舍入到\n小数点后 6 位', color=RED, ha='left')
save(fig, Path(__file__).resolve().parent, 'figure', {'N': Ns.tolist(), 'rounded': err.tolist(), 'unrounded': eperf.tolist()})
print(hs[np.argmin(err)], err.min())
