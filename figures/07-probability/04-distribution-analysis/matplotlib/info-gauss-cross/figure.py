from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# P = N(0,1), Q_s = N(0,s^2): cross-entropy H(P,Q_s) = 0.5 ln(2 pi s^2) + 1/(2 s^2) (blue);
# h(P) = 0.5 ln(2 pi e) = 1.419 (purple dashed); gap = KL (red segment at s = 2).
fig, ax = figure(width_mm=86, height_mm=48)
panel(fig, left=.12, right=.96, bottom=.21, top=.95)
s = np.linspace(.3, 3.2, 600)
ce = .5*np.log(2*math.pi*s*s) + 1/(2*s*s); h = .5*math.log(2*math.pi*math.e)
ax.plot(s, ce, color=BLUE, lw=1.4); ax.axhline(h, color=PURPLE, lw=.85, ls=DASH)
c2 = .5*math.log(2*math.pi*4) + 1/8
ax.plot([2, 2], [h, c2], color=RED, lw=1.6); dot(ax, 1, h)
lab(ax, 2.07, (h+c2)/2-.04, r'$D_{\mathrm{KL}}(P\Vert Q_2)$', RED)
lab(ax, .35, h-.25, '$h(P)$', PURPLE); lab(ax, .62, 2.6, r'$H(P,Q_s)$', BLUE)
ax.set_xlim(.3, 3.2); ax.set_ylim(.8, 3.6); axlab(ax, '$s$', 'nat')
save(fig, HERE, 'figure', {'h': h, 'CE(s=2)': c2, 'KL(s=2)': c2-h, 'CE(s=1/2)': .5*math.log(2*math.pi*.25)+2})
