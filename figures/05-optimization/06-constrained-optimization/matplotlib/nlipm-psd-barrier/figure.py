from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Positive definite matrices: X=[[2,1],[1,2]], D=[[-1,-1],[-1,-2]].
X = np.array([[2., 1.], [1., 2.]]); D = np.array([[-1., -1.], [-1., -2.]])
al = np.linspace(0, 1.25, 300); ev = np.array([np.linalg.eigvalsh(X+t*D) for t in al])
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
a.plot(al, ev[:, 1], color=BLUE, lw=1.5); a.plot(al, ev[:, 0], color=BLUE, lw=1.5, ls='--'); a.axhline(0, color=EDGE, lw=1.7)
a.plot([1], [0], 'o', color=RED, ms=4.5, zorder=6); a.set_xlim(0, 1.25); a.set_ylim(-.4, 3.2); tag(a, '$\\alpha$', '(a)')
a.text(.3, 2.35, '较大特征值', fontsize=7.5); a.text(.1, .45, '较小特征值', fontsize=7.5)
Xi = np.linalg.inv(X); R = Xi@D; d1 = -np.trace(R); d2 = np.trace(R@R)
t = np.linspace(0, .9995, 400); phi = -np.log(3-4*t+t**2)
b.plot(t, phi, color=BLUE, lw=1.5); b.plot(t, -np.log(3)+d1*t+.5*d2*t**2, color=YELLOW, lw=1.6, ls='--'); b.axvline(1, color=EDGE, lw=1.7)
b.set_xlim(0, 1.05); b.set_ylim(-1.3, 3.2); tag(b, '$\\alpha$', '(b)')
save(fig, OUT, 'figure', {'d1': d1, 'd2': d2, 'eig_XinvD': sorted(np.linalg.eigvals(R).real.tolist())})
