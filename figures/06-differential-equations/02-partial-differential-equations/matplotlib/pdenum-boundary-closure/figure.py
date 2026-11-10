from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Explicit heat, h=1/20, r=0.45: Dirichlet closure vs Robin u_x(0)=20u(0) through ghost value.
n = 20; h = 1/n; r = .45; be = 20
def B(robin):
    m = n; M_ = np.zeros((m, m))
    for j in range(m):
        M_[j, j] = 1-2*r
        if j: M_[j, j-1] = r
        if j < m-1: M_[j, j+1] = r
    if robin: M_[0, 0] = 1-2*r*(1+be*h); M_[0, 1] = 2*r
    return M_
x = np.arange(n)*h
U0 = np.sin(PI*(x+h/2)); steps = np.arange(0, 121, 1)
hist = {}
for name, robin in (('d', False), ('r', True)):
    U = U0.copy(); v = []
    if not robin: U[0] = 0
    Mx = B(robin)
    if not robin: Mx[0, :] = 0
    for k in steps:
        v.append(np.max(np.abs(U))); U = Mx@U
    hist[name] = np.array(v)
fig, ax = figure(width_mm=88, height_mm=50)
ax.semilogy(steps, hist['d'], color=GREEN, lw=1.4); ax.semilogy(steps, hist['r'], color=RED, lw=1.4)
ax.set_xlabel('时间步 $k$'.replace(' $k$', ''), labelpad=1); ax.set_ylabel('最大模', labelpad=1); ax.set_xlim(0, 120)
rho = {k: float(np.abs(np.linalg.eigvals(B(k == 'r'))).max()) for k in ('d', 'r')}
save(fig, HERE, 'figure', {'r': r, 'beta': be, 'h': h, 'rho': rho, 'end': [float(hist['d'][-1]), float(hist['r'][-1])]}); print(rho, hist['d'][-1], hist['r'][-1])
