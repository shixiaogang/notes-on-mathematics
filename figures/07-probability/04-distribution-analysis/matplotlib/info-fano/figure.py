from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# (a) M = 4: Fano function phi(p) = h_b(p) + p ln 3 (blue), increasing on [0,3/4] up to ln 4.
#     Example: Y = X w.p. 0.7, otherwise uniform on the other 3 labels; H(X|Y) = 0.9404 (red line)
#     meets phi at p = 0.3, which is exactly the MAP error (equality case).
# (b) uniform X on M labels: smallest error allowed by Fano, i.e. phi^{-1}(ln M - I), against I/ln M,
#     for M = 4 (yellow), 16 (purple), 256 (blue); grey dashed: weakened bound 1 - (I+ln2)/ln M for M=256.
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.3)
def phi(p, M): return hb(p) + p*math.log(M-1)
p = np.linspace(0, 1, 801)
a.plot(p, phi(p, 4), color=BLUE, lw=1.4)
Hc = float(hb(.3)) + .3*math.log(3)
a.axhline(Hc, color=RED, lw=.9); dot(a, .3, Hc)
a.plot([.3, .3], [0, Hc], color=STROKE, lw=.6, ls=DOT)
a.axhline(math.log(4), color=PURPLE, lw=.85, ls=DASH)
lab(a, .02, math.log(4)+.03, r'$\ln 4$', PURPLE); lab(a, .55, Hc-.13, r'$H(X\mid Y)=0.940$', RED)
a.set_xlim(0, 1); a.set_ylim(0, 1.55); a.set_xticks([0, .3, .75, 1]); axlab(a, r'$P_{\mathrm{e}}$', 'nat')
def inv(t, M):
    lo, hi = 0.0, (M-1)/M
    if t <= 0: return 0.0
    for _ in range(80):
        m = (lo+hi)/2
        if phi(np.array([m]), M)[0] < t: lo = m
        else: hi = m
    return (lo+hi)/2
u = np.linspace(0, 1, 301); facts = {}
for M, c in ((4, YELLOW), (16, PURPLE), (256, BLUE)):
    L = math.log(M); pe = [inv(L*(1-x), M) for x in u]
    b.plot(u, pe, color=c, lw=1.3); facts['M%d_at_I0.5lnM' % M] = inv(L*.5, M)
b.plot(u, np.maximum(0, 1-(u*math.log(256)+LN2)/math.log(256)), color=STROKE, lw=.85, ls=DASH)
for M, c, ux, tx in ((4, YELLOW, .5, (.62, .32)), (16, PURPLE, .3, (.42, .62)), (256, BLUE, .12, (.22, .9))):
    yv = inv(math.log(M)*(1-ux), M)
    b.annotate('$M=%d$' % M, xy=(ux, yv), xytext=tx, color=c, fontsize=7.5, arrowprops=dict(arrowstyle='-', color=c, lw=.6))
b.set_xlim(0, 1); b.set_ylim(0, 1); axlab(b, r'$I(X;Y)/\ln M$', '错误概率下界')
tags(fig, (a, b))
facts.update({'H(X|Y)': Hc, 'phi(0.3)': float(phi(np.array([.3]), 4)[0])})
save(fig, HERE, 'figure', facts)
