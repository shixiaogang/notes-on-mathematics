from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
# Arithmetic coding of the message abac under p = (0.4,0.3,0.2,0.1), symbol order a,b,c,d.
# Each row redraws the current interval at full width and splits it in proportion 4:3:2:1; the kept
# sub-interval (light blue) is magnified into the next row. Exact rationals: final interval
# [0.1936, 0.2032), width 0.0096; codeword length ceil(log2(1/0.0096))+1 = 8, dyadic interval
# [50/256, 51/256) (red) lies inside it.
msg = [0, 1, 0, 2]
F = [Fraction(0)]
for q in PF[:-1]:
    F.append(F[-1]+q)
lo, w = Fraction(0), Fraction(1); rows = [(lo, w)]
for s in msg:
    lo, w = lo + w*F[s], w*PF[s]; rows.append((lo, w))
ell = math.ceil(-math.log2(float(w))) + 1
k = math.ceil(lo * 2**ell)
fig, ax = figure(width_mm=110, height_mm=70)
panel(fig, left=.13, right=.97, bottom=.04, top=.97)
X0, X1 = 0., 1.; ys = [4, 3, 2, 1, 0]; hh = .32
for r, (a, ww) in enumerate(rows):
    y = ys[r]
    ax.plot([X0, X1], [y, y], color=STROKE, lw=.95)
    if r < 4:
        s = msg[r]
        for j in range(4):
            u0 = float(F[j]); u1 = u0 + float(PF[j])
            if j == s:
                ax.add_patch(__import__('matplotlib').patches.Rectangle((u0, y-hh/2), u1-u0, hh, fc=BLUE_FILL, ec=BLUE, lw=.8, zorder=2))
            ax.plot([u0, u0], [y-hh/2, y+hh/2], color=STROKE, lw=.85, zorder=3)
            lab(ax, (u0+u1)/2, y+hh/2+.05, '$%s$' % NAMES[j], INK if j == s else MUTED, ha='center', va='bottom', fontsize=7.5 if j == s else 7)
        ax.plot([1, 1], [y-hh/2, y+hh/2], color=STROKE, lw=.85, zorder=3)
        u0 = float(F[s]); u1 = u0+float(PF[s])
        ax.plot([u0, 0], [y-hh/2, ys[r+1]+hh/2], color=MUTED, lw=.6, ls=DOT)
        ax.plot([u1, 1], [y-hh/2, ys[r+1]+hh/2], color=MUTED, lw=.6, ls=DOT)
    else:
        ax.plot([0, 0], [y-hh/2, y+hh/2], color=STROKE, lw=.85); ax.plot([1, 1], [y-hh/2, y+hh/2], color=STROKE, lw=.85)
        c0 = (Fraction(k, 2**ell)-a)/ww; c1 = (Fraction(k+1, 2**ell)-a)/ww
        ax.add_patch(__import__('matplotlib').patches.Rectangle((float(c0), y-hh/2), float(c1-c0), hh, fc=RED_FILL, ec=RED, lw=1.0, zorder=2))
        lab(ax, float(c0+c1)/2, y-hh/2-.08, r'$[50/256,\,51/256)$', RED, ha='center', va='top')
    lab(ax, -.02, y, '%.4f' % float(a), INK, ha='right', va='center', fontsize=7)
    lab(ax, 1.02, y, '%.4f' % float(a+ww), INK, ha='left', va='center', fontsize=7)
ax.set_xlim(-.16, 1.14); ax.set_ylim(-.75, 4.55); ax.axis('off')
save(fig, HERE, 'figure', {'rows': [[float(a), float(a+ww), float(ww)] for a, ww in rows], 'ell': ell, 'k': k})
