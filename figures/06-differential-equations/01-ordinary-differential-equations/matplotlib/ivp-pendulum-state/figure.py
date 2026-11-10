from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：单摆 y''=-sin y。同一角度、不同角速度的未来不同；状态平面中轨道由 (y,v) 决定。
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, .075, .985, .97, .24, .27)
a, b = axes
f = lambda t, z: np.array([z[1], -np.sin(z[0])])
for v, c in [(0, BLUE), (1, YELLOW), (-1, PURPLE)]:
    ts, zs = rk4(f, 0, np.array([1., v]), 8, 4000)
    a.plot(ts, zs[:, 0], color=c, lw=1.4, zorder=3)
    Ts, Zs = rk4(f, 0, np.array([1., v]), 14, 7000)
    b.plot(Zs[:, 0], Zs[:, 1], color=c, lw=1.4, zorder=3)
    dot(b, 1, v)
dot(a, 0, 1)
y = np.linspace(-np.pi, np.pi, 400)
s = 2*np.cos(y/2)
b.plot(y, s, color=STROKE, lw=1.0, zorder=2); b.plot(y, -s, color=STROKE, lw=1.0, zorder=2)
a.set_xlim(0, 8); a.set_ylim(-2.4, 2.4); a.set_xticks([0, 2, 4, 6, 8]); a.set_yticks([-2, -1, 0, 1, 2])
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$y$', labelpad=1)
b.set_xlim(-np.pi, np.pi); b.set_ylim(-2.4, 2.4); b.set_xticks([-np.pi, 0, np.pi]); b.set_xticklabels(['$-\\pi$', '0', '$\\pi$']); b.set_yticks([-2, -1, 0, 1, 2])
b.set_xlabel('$x_1=y$', labelpad=1); b.set_ylabel('$x_2=\\dot y$', labelpad=1)
Y, V = np.meshgrid(np.linspace(-2.8, 2.8, 11), np.linspace(-2.05, 2.05, 9))
U1, U2 = V, -np.sin(Y)
n = np.hypot(U1/(2*np.pi), U2/4.8); n[n == 0] = 1
b.quiver(Y, V, U1/(2*np.pi)/n*.075*2*np.pi, U2/4.8/n*.075*4.8, angles='xy', scale_units='xy', scale=1, color=FIELD, width=.004, headwidth=4, headlength=4, zorder=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': "y''=-sin y", 'y0': 1, 'v0': [0, 1, -1]})
