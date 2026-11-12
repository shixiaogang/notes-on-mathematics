from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# Self-information -ln p (nat, left axis) and -log2 p (bit, right axis).
# Red points: p = 1/2, 1/4, 1/8 from the running table (1/2,1/4,1/8,1/8).
fig, ax = figure(width_mm=86, height_mm=50)
panel(fig, left=.12, right=.86, bottom=.2, top=.95)
p = np.linspace(.004, 1, 600)
ax.plot(p, -np.log(p), color=BLUE, lw=1.4)
facts = {}
for q, s in ((.5, '$1/2$'), (.25, '$1/4$'), (.125, '$1/8$')):
    dot(ax, q, -math.log(q))
    ax.plot([q, q], [0, -math.log(q)], color=STROKE, lw=.6, ls=DOT)
    lab(ax, q+.03, -math.log(q)+.08, '%d bit' % round(-math.log2(q)), RED)
    facts[str(q)] = {'nat': -math.log(q), 'bit': -math.log2(q)}
ax.set_xlim(0, 1.02); ax.set_ylim(0, 4.2)
ax.set_xticks([0, .125, .25, .5, 1]); ax.set_xticklabels(['0', '$1/8$', '$1/4$', '$1/2$', '1'])
axlab(ax, '$p$', r'$-\ln p$ / nat')
r = ax.twinx(); r.spines['right'].set_visible(True); r.spines['top'].set_visible(False)
r.set_ylim(0, 4.2/LN2); r.set_yticks([0, 1, 2, 3, 4, 5, 6]); r.set_ylabel(r'$-\log_2 p$ / bit', labelpad=2)
save(fig, HERE, 'figure', facts)
