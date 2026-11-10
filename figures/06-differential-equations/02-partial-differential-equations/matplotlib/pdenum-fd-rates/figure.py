from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Max-norm error under refinement: smooth running example vs u=x^(3/2)-x.
ns = np.array([8, 16, 32, 64, 128, 256, 512]); E1 = []; E2 = []
for n in ns:
    h = 1/n; xi = np.linspace(h, 1-h, n-1); A = lap1d(n)
    b = PI**2*np.sin(PI*xi); b[-1] += 1/h**2
    E1.append(np.max(abs(np.linalg.solve(A, b)-uex(xi))))
    f = -.75*xi**(-.5); E2.append(np.max(abs(np.linalg.solve(A, f)-(xi**1.5-xi))))
E1, E2 = np.array(E1), np.array(E2); hs = 1/ns
fig, ax = figure(width_mm=88, height_mm=56)
ax.loglog(hs, E1, color=GREEN, lw=1.4, marker='o', ms=3.4, mew=0)
ax.loglog(hs, E2, color=YELLOW, lw=1.5, marker='s', ms=3.2, mew=0)
ax.loglog(hs, 1.6*E1[-1]*(hs/hs[-1])**2, color=PURPLE, lw=.9, ls=DASH)
ax.loglog(hs, 1.7*E2[-1]*(hs/hs[-1])**1.5, color=PURPLE, lw=.9, ls=DOT)
lab(ax, .018, 1.4e-3, '光滑解', GREEN, ha='left'); lab(ax, .0022, 7e-5, r'$x^{3/2}-x$', YELLOW, ha='left')
ax.set_xlabel('$h$', labelpad=1); ax.set_ylabel('最大模误差', labelpad=1)
save(fig, HERE, 'figure', {'n': ns.tolist(), 'smooth': E1.tolist(), 'rough': E2.tolist()})
print(np.log2(E1[:-1]/E1[1:]), np.log2(E2[:-1]/E2[1:]), E1[-1], E2[-1])
