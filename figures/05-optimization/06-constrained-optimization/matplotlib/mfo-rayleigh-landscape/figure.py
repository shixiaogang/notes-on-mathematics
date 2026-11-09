from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# f(x) = x'Ax/2 on the unit sphere, A = diag(1,2,4); level curves in an orthographic view.
fig, ax = figure(width_mm=62, height_mm=58)
D = Disk(28, 24)
D.outline(ax)
ax.contour(D.U, D.V, D.rayleigh(), levels=[.56,.68,.85,1.0,1.2,1.45,1.7,1.9], colors=BLUE, linewidths=.8)
e = np.eye(3)
ax.plot(*D.xy(e[0]), 'o', ms=4.6, color=RED)
ax.plot(*D.xy(e[1]), 'o', ms=4.6, mfc='white', mec=PURPLE, mew=1.1)
ax.plot(*D.xy(e[2]), 's', ms=4.2, mfc='white', mec=GRAY, mew=1.1)
ax.plot(*D.xy(X0), 'o', ms=4.2, color=GREEN)
for p,t,dx,dy in [(e[0],r'$\mathbf{e}_1$',-.04,-.17),(e[1],r'$\mathbf{e}_2$',.1,-.07),(e[2],r'$\mathbf{e}_3$',.12,-.02),(X0,r'$\mathbf{x}^{(0)}$',.06,.1)]:
    a,b=D.xy(p); ax.text(a+dx,b+dy,t,ha='center',va='center',fontsize=8)
ax.set_xlim(-1.05,1.05); ax.set_ylim(-1.05,1.05)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=x^T A x/2, A=diag(1,2,4), unit sphere, view az=28 el=24', 'x0': '(2,2,1)/3'})
