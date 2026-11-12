from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# Binary entropy h(p) in nat (left axis; right axis in bit). Concavity check:
# chord between p=0.1 and p=0.7 lies below the curve; the mixture p=0.4 (weights 1/2,1/2)
# has h(0.4) > (h(0.1)+h(0.7))/2. Red point: p=1/4 (h=0.5623 nat = 0.8113 bit).
fig, ax = figure(width_mm=86, height_mm=50)
panel(fig, left=.12, right=.86, bottom=.2, top=.95)
p = np.linspace(0, 1, 801)
ax.plot(p, hb(p), color=BLUE, lw=1.4)
a, b = .1, .7; ha, hb_ = hb(a), hb(b)
ax.plot([a, b], [ha, hb_], color=YELLOW, lw=1.2)
for x in (a, b): dot(ax, x, float(hb(x)), color=YELLOW, ms=3.6)
m = (a+b)/2; dot(ax, m, float((ha+hb_)/2), color=YELLOW, ms=3.6); dot(ax, m, float(hb(m)), color=BLUE, ms=3.6)
ax.plot([m, m], [float((ha+hb_)/2), float(hb(m))], color=STROKE, lw=.7, ls=DOT)
dot(ax, .25, float(hb(.25)))
lab(ax, .27, float(hb(.25))-.06, '$p=1/4$', RED)
ax.axhline(LN2, color=PURPLE, lw=.85, ls=DASH)
lab(ax, .62, LN2+.02, r'$\ln 2$', PURPLE)
ax.set_xlim(0, 1); ax.set_ylim(0, .78)
axlab(ax, '$p$', r'$h_{\mathrm{b}}(p)$ / nat')
r = ax.twinx(); r.spines['right'].set_visible(True); r.spines['top'].set_visible(False)
r.set_ylim(0, .78/LN2); r.set_yticks([0, .25, .5, .75, 1]); r.set_ylabel('bit', labelpad=2)
save(fig, HERE, 'figure', {'h(1/4)': float(hb(.25)), 'h(0.1)': float(ha), 'h(0.7)': float(hb_), 'h(0.4)': float(hb(m)), 'chord_mid': float((ha+hb_)/2)})
