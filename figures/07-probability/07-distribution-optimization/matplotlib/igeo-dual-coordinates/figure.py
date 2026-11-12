"""Bernoulli Fisher information in two coordinates. (a) natural theta (logit): G=p(1-p); (b) mean p: G=1/(p(1-p)).
Red: theta=ln 3 <-> p=3/4, G=3/16 and 16/3 (reciprocal)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

import math
fig, (a, b) = figure(width_mm=104, height_mm=46, ncols=2)
t = np.linspace(-6, 6, 400); p = 1/(1+np.exp(-t))
a.plot(t, p*(1-p), color=BLUE, lw=1.4)
a.scatter([math.log(3)], [3/16], s=14, color=RED, zorder=5)
a.set_xlim(-6, 6); a.set_ylim(0, 0.3); a.set_xlabel(r'$\theta$', labelpad=1); a.set_ylabel(r'$G(\theta)$', labelpad=1)
q = np.linspace(0.02, 0.98, 400)
b.plot(q, 1/(q*(1-q)), color=BLUE, lw=1.4)
b.scatter([0.75], [16/3], s=14, color=RED, zorder=5)
b.set_xlim(0, 1); b.set_ylim(0, 30); b.set_xlabel(r'$p$', labelpad=1); b.set_ylabel(r'$G_{p}(p)$', labelpad=1)
tag(a, '(a)', y=-0.30); tag(b, '(b)', y=-0.30)
save(fig, HERE, 'figure', {'G_theta_ln3': 3/16, 'G_p_0.75': 16/3})
