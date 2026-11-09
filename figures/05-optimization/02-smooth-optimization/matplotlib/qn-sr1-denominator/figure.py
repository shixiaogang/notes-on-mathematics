from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
sys.path.insert(0, str(ROOT/"figures/05-optimization/02-smooth-optimization/matplotlib/qn-common"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
from qnlib import *
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = "#4C4D4F"

# A=diag(2,8)，B0=diag(3,7)，s=(1,1+e)，r=(A-B0)s。e->0 时 r^T s->0 而 r 不趋于 0。
A = np.diag([2., 8.]); B = np.diag([3., 7.])
es = np.logspace(-9, 0, 200); dn, up, thr = [], [], []
for e in es:
    s = np.array([1, 1+e]); r = (A-B)@s
    rs = float(r@s); dn.append(abs(rs)); up.append(np.linalg.norm(r)**2/abs(rs)); thr.append(1e-8*np.linalg.norm(r)*np.linalg.norm(s))
fig, ax = figure(width_mm=86, height_mm=54)
ax.loglog(es, up, color=RED, lw=1.4); ax.loglog(es, dn, color=BLUE, lw=1.4); ax.loglog(es, thr, color=STROKE, lw=.95, ls=(0, (4, 2)))
ax.text(4e-8, 7e7, '$\\|\\Delta B\\|_F$', color=INK); ax.text(3e-5, 3e-3, '分母', color=INK); ax.text(1.3e-3, 5e-7, '跳过阈值', color=INK)
ax.set_xlim(1e-9, 1); ax.set_ylim(1e-9, 1e10); ax.set_xlabel('$\\epsilon$', labelpad=1); ax.set_xticks([1e-8, 1e-4, 1]); ax.set_yticks([1e-8, 1, 1e8]); ax.minorticks_off()
save(fig, HERE, 'figure', {'A': A.tolist(), 'B0': B.tolist(), 's': '(1,1+e)', 'c_r': 1e-8})
