from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：旋转矩阵 A=[[0,1],[-1,0]] 的指数级数：部分和轨迹逼近单位圆；固定 t 的截断误差先升后超指数下降。
A = np.array([[0., 1], [-1, 0]])
def partial(t, K):
    S = np.eye(2); T = np.eye(2)
    for k in range(1, K+1):
        T = T@(t*A)/k
        S = S+T
    return S
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, .07, .985, .96, .23, .3)
a, b = axes
th = np.linspace(0, 2*np.pi, 400)
a.plot(np.cos(th), -np.sin(th), color=BLUE, lw=MAIN, zorder=2)
for K, col, ls in ((2, YELLOW, '-'), (4, PURPLE, '-'), (8, GREEN, '-')):
    p = np.array([partial(t, K)@np.array([1., 0]) for t in np.linspace(0, np.pi*1.5, 300)])
    a.plot(p[:, 0], p[:, 1], color=col, lw=1.15, ls=ls, zorder=3)
a.plot([1], [0], 'o', ms=3.8, color=RED, mew=0, zorder=5)
a.text(-1.78, -1.62, '$K=2$', color=YELLOW); a.text(.34, 1.42, '$K=4$', color=PURPLE); a.text(-1.62, 1.28, '$K=8$', color=GREEN)
a.set_aspect('equal'); a.set_xlim(-1.85, 2.0); a.set_ylim(-1.85, 1.85); a.set_xticks([-1, 0, 1]); a.set_yticks([-1, 0, 1]); label(a, '$x_1$', '$x_2$')
Ks = np.arange(0, 26)
for t, col in ((1, BLUE), (3, YELLOW), (8, PURPLE)):
    E = expm(t*A)
    err = [max(np.linalg.norm(partial(t, K)-E, 2), 1e-16) for K in Ks]
    b.semilogy(Ks, err, '-', color=col, lw=1.3)
    i = min(9, 23)
    b.text({1: 9.4, 3: 16, 8: 20}[t], {1: 3e-5, 3: 1.5e-3, 8: 3e0}[t], f'$t={t}$', color=col)
b.set_xlim(0, 25); b.set_ylim(1e-12, 2e3); b.set_xticks([0, 10, 20]); b.set_yticks([1e-12, 1e-8, 1e-4, 1]); label(b, '$K$', '误差')
tags(fig, axes)
save(fig, HERE, 'figure', {'A': A.tolist(), 'error': 'spectral norm of partial sum minus expm', 'partial sums': 'K=2,4,8, t in [0,1.5 pi]'})
