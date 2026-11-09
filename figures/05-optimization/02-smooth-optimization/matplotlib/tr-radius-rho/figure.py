from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 沿 -g 取长度 Delta 的步，|1-rho| 随 Delta：精确 Hessian 与粗糙模型 B=I。点 (2,2)。
fig, ax = figure(width_mm=90, height_mm=58)
D = np.logspace(-4, -.5, 40); g = A_G; u = -g/np.linalg.norm(g)
for B, c in ((A_B, GREEN), (np.eye(2), YELLOW)):
    v = [abs(1 - (f(A_X) - f(A_X + d*u))/(-mdec(d*u, g, B))) for d in D]
    ax.loglog(D, v, color=c, lw=1.5)
ax.set_xlabel('$\\Delta$', labelpad=1); ax.set_ylabel(r'$\vert 1-\rho\vert$', labelpad=1); ax.set_xlim(1e-4, .4); ax.set_ylim(1e-8, 2)
ax.text(.012, .1, '$B=I$', fontsize=7.5); ax.text(.022, 8e-6, '$B=\\nabla^2 f$', fontsize=7.5)
save(fig, HERE, 'figure', {'x': [2, 2], 'direction': '-g'})
