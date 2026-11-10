from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：Cantor 函数连续且几乎处处导数为零，却不是 x'=0, x(0)=0 的解。
fig, ax = figure(width_mm=80, height_mm=50)
panel(fig, .125, .98, .965, .16)
def cantor(t, n=30):
    out = np.zeros_like(t); s = t.copy(); w = .5
    for _ in range(n):
        h = (s >= 1/3) & (s <= 2/3)
        l = s < 1/3
        r = s > 2/3
        out = out + np.where(h, w, 0) + np.where(r, w, 0)
        s = np.where(l, 3*s, np.where(r, 3*s - 2, 0.0))
        s = np.where(h, -1.0, s)
        w = w/2
        s[s < 0] = -1
        out[s < 0] = out[s < 0]
    return out
def cf(t):
    # Base-3 definition computed value by value.
    v = []
    for s in t:
        val = 0.; w = .5; x = s
        for _ in range(40):
            if x < 1/3: x = 3*x
            elif x > 2/3: val += w; x = 3*x - 2
            else: val += w; break
            w /= 2
        v.append(val)
    return np.array(v)
t = np.linspace(0, 1, 2401)
ax.plot(t, 0*t, color=BLUE, lw=1.4, zorder=3)
ax.plot(t, cf(t), color=RED, lw=1.2, zorder=4)
dot(ax, 0, 0)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.05, 1.05); ax.set_xticks([0, 1/3, 2/3, 1]); ax.set_xticklabels(['0', '1/3', '2/3', '1']); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
save(fig, HERE, 'figure', {'curve': 'Cantor function, base-3 digits to depth 40'})
