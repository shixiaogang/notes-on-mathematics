from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# P = (1/2,1/4,1/8,1/8) (blue), Q1 uniform (yellow), Q2 = (1/8,1/8,1/4,1/2) (purple).
# (a) the three probability tables; (b) cross-entropy in bits split as H(P) (blue) + KL (red):
#     H(P,P) = 1.75, H(P,Q1) = 1.75 + 0.25, H(P,Q2) = 1.75 + 0.875.
P = np.array([.5, .25, .125, .125]); Q1 = np.full(4, .25); Q2 = np.array([.125, .125, .25, .5])
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.3)
k = np.arange(4); w = .26
for off, q, c, f in ((-w, P, BLUE, BLUE_FILL), (0, Q1, YELLOW, YELLOW_FILL), (w, Q2, PURPLE, PURPLE_FILL)):
    a.bar(k+off, q, width=w, color=f, edgecolor=c, lw=.8)
a.set_xticks(k); a.set_xticklabels(['$1$', '$2$', '$3$', '$4$']); a.set_ylim(0, .58)
lab(a, -.4, .53, '$P$', BLUE); lab(a, .05, .53, '$Q_1$', YELLOW); lab(a, .5, .53, '$Q_2$', PURPLE)
axlab(a, '$x$', '概率')
log2 = np.log2
HP = float(-(P*log2(P)).sum()); facts = {'H(P)': HP}
names = ('$Q=P$', '$Q=Q_1$', '$Q=Q_2$')
for i, q in enumerate((P, Q1, Q2)):
    D = float((P*log2(P/q)).sum()); facts['D%d' % i] = D; facts['CE%d' % i] = HP+D
    b.bar(i, HP, width=.55, color=BLUE_FILL, edgecolor=BLUE, lw=.8)
    if D > 0: b.bar(i, D, bottom=HP, width=.55, color=RED_FILL, edgecolor=RED, lw=.8)
    b.text(i, HP+D+.06, '$%.3g$' % (HP+D), ha='center', va='bottom', fontsize=7.5)
b.set_xticks(range(3)); b.set_xticklabels(names); b.set_ylim(0, 3.1); axlab(b, '', 'bit')
lab(b, -.22, .8, '$H(P)$', BLUE)
lab(b, 1.3, 2.2, r'$D_{\mathrm{KL}}$', RED)
tags(fig, (a, b))
save(fig, HERE, 'figure', facts)
