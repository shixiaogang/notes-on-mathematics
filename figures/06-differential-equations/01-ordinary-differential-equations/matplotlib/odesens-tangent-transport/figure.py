from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x1'=-x1, x2'=x2+x1^2 的小圆像与线性化椭圆。显式流：
# phi_t(a,b)=(a e^{-t}, (b+a^2/3)e^t-(a^2/3)e^{-2t})；(a,b)=(1,0)，t=ln2 时 S=[[1/2,0],[7/6,2]]。
fig, ax = figure(width_mm=58, height_mm=84)
panel(fig, .16, .985, .985, .1)
T = np.log(2); r = .4; c = np.array([1., 0.])
def phi(a, b, t): return a*np.exp(-t), (b+a**2/3)*np.exp(t)-a**2/3*np.exp(-2*t)
S = np.array([[.5, 0], [7/6, 2]]); end = np.array(phi(1., 0., T))
th = np.linspace(0, 2*np.pi, 361); ca, cb = c[0]+r*np.cos(th), c[1]+r*np.sin(th)
X, Y = phi(ca, cb, T); ax.fill(X, Y, facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.2)
lin = end[:, None]+S@np.vstack([r*np.cos(th), r*np.sin(th)]); ax.plot(lin[0], lin[1], color=GREEN, lw=1.2, ls=(0, (4, 2)))
ax.fill(ca, cb, facecolor='white', edgecolor=RED, lw=1.2)
t = np.linspace(0, T, 200); ax.plot(*phi(1., 0., t), color=BLUE, lw=1.1)
def arrow(p, v, col): ax.annotate('', xy=p+v, xytext=p, arrowprops=dict(arrowstyle='-|>', color=col, lw=1.1, mutation_scale=7, shrinkA=0, shrinkB=0))
for e in (np.array([r, 0.]), np.array([0., r])):
    arrow(c, e, RED); arrow(end, S@e, BLUE)
ax.plot(*c, 'o', ms=3.6, color=RED, mew=0, zorder=5); ax.plot(*end, 'o', ms=3.6, color=BLUE, mew=0, zorder=5)
ax.text(1.0, -.46, '$t=0$', color=RED, fontsize=7.5, ha='center', va='top'); ax.text(.08, 1.55, '$t=\\ln 2$', color=BLUE, fontsize=7.5, ha='left', va='bottom')
ax.set_aspect('equal'); ax.set_xlim(.05, 1.5); ax.set_ylim(-.62, 1.85); ax.set_xticks([.5, 1]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$x_1$', labelpad=0); ax.set_ylabel('$x_2$', labelpad=1)
print('end', end, 'area', shoelace(np.c_[X, Y]), np.pi*r**2, 'det', np.linalg.det(S))
save(fig, HERE, 'figure', {'field': '(-x1, x2+x1^2)', 'center': [1, 0], 'r': r, 'T': 'ln 2', 'S': S.tolist()})
