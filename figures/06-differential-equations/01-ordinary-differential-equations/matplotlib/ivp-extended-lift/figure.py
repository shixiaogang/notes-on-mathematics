from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：受迫振子 y''+y=cos(3t) 的轨线在状态平面上自交，抬升到 (x1,x2,s) 后不再相交。
import matplotlib.pyplot as plt
from support import configure
configure()
fig = plt.figure(figsize=(112/25.4, 62/25.4))
a = fig.add_axes([.105, .22, .36, .74])
b = fig.add_axes([.50, .10, .48, .92], projection='3d')
T = 2*np.pi
t = np.linspace(0, 4.6, 6000)
# 解析解 y=0.3 cos t+0.2 sin t-cos(3t)/8，满足 y''+y=cos 3t。
x1 = .3*np.cos(t) + .2*np.sin(t) - np.cos(3*t)/8
x2 = -.3*np.sin(t) + .2*np.cos(t) + 3*np.sin(3*t)/8
ddy = -.3*np.cos(t) - .2*np.sin(t) + 9*np.cos(3*t)/8
assert np.max(np.abs(ddy + x1 - np.cos(3*t))) < 1e-9
# 寻找自交点：不相邻时刻距离最小者
idx = np.arange(0, len(t), 3)
X = np.c_[x1[idx], x2[idx]]
D = np.hypot(X[:, None, 0] - X[None, :, 0], X[:, None, 1] - X[None, :, 1])
D[np.abs(idx[:, None] - idx[None, :]) < 900] = 9
i, j = np.unravel_index(np.argmin(D), D.shape)
ti, tj = t[idx[i]], t[idx[j]]
print('crossing', ti, tj, X[i], X[j], D[i, j])
vi = np.array([x2[idx[i]], np.cos(3*ti) - x1[idx[i]]]); vj = np.array([x2[idx[j]], np.cos(3*tj) - x1[idx[j]]])
print('fields', vi, vj)
a.plot(x1, x2, color=BLUE, lw=1.4, zorder=3)
dot(a, x1[0], x2[0])
hollow(a, X[i, 0], X[i, 1], ms=5)
for tt, v, c in [(ti, vi, PURPLE), (tj, vj, PURPLE)]:
    a.annotate('', xy=(X[i, 0] + .2*v[0]/np.linalg.norm(v), X[i, 1] + .2*v[1]/np.linalg.norm(v)), xytext=(X[i, 0], X[i, 1]), arrowprops=dict(arrowstyle='-|>', color=c, lw=1, mutation_scale=7, shrinkA=0, shrinkB=0), zorder=7)
a.set_xlabel('$x_1$', labelpad=1); a.set_ylabel('$x_2$', labelpad=1)
b.plot(x1, x2, t, color=BLUE, lw=1.4)
b.plot(x1, x2, 0*t, color=FIELD, lw=.8)
b.plot([x1[0]], [x2[0]], [0], 'o', ms=4, color=RED, mew=0)
for tt in (ti, tj):
    k = np.argmin(np.abs(t - tt))
    b.plot([x1[k]], [x2[k]], [tt], 'o', ms=4.2, mfc='white', mec=RED, mew=1)
    b.plot([x1[k], x1[k]], [x2[k], x2[k]], [0, tt], color=RED, lw=.8, ls=(0, (3, 2)))
b.set_xlabel('$x_1$', labelpad=-8); b.set_ylabel('$x_2$', labelpad=-8); b.set_zlabel('$s$', labelpad=-8)
b.tick_params(pad=-3, labelsize=7)
b.set_xticks([-.4, .4]); b.set_yticks([-.6, .6]); b.set_zticks([0, 2, 4])
for ax3 in (b.xaxis, b.yaxis, b.zaxis):
    ax3.pane.set_visible(False); ax3._axinfo['grid']['linewidth'] = 0; ax3.line.set_color(STROKE)
b.grid(False)
b.view_init(elev=20, azim=-58)
for ax_, s, in zip((a,), ('(a)',)):
    p = ax_.get_position(); fig.text((p.x0 + p.x1)/2, .015, s, ha='center', va='bottom')
p = b.get_position(); fig.text((p.x0 + p.x1)/2, .015, '(b)', ha='center', va='bottom')
save(fig, HERE, 'figure', {'formula': "y''+y=cos 3t, y(0)=0.175, y'(0)=0.2", 'crossing_times': [float(ti), float(tj)], 'crossing_state': [float(X[i, 0]), float(X[i, 1])]})
