from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Hypervolume (r=(1.1,1.1)), reference-front distance IGD and non-dominated count over the NSGA-II run.
import json
H = np.array(json.loads((HERE.parent/'moo-nsga-run/run.json').read_text())['hist']); t = np.arange(len(H))
x = np.linspace(0, 1.0, 200001); hv_true = float(np.trapezoid(1.1-(1-x**2), x)+.1*1.1)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panels(fig, .08, .985, .985, .23, .28)
ax = axes[0]; setup(ax, (0, 200), (0, .85), range(0, 201, 50), [0, .2, .4, .6, .8], '代数', '超体积')
ax.plot(t, H[:, 0], color=GREEN, lw=1.4); ax.plot([0, 200], [hv_true]*2, color=RED, lw=.95, ls=(0, (3, 2)))
ax = axes[1]; setup(ax, (0, 200), (.005, 3), range(0, 201, 50), None, '代数', '到参考前沿的平均距离')
ax.semilogy(t, H[:, 1], color=GREEN, lw=1.4); ax.tick_params(axis='y', which='minor', length=0); ax.set_ylim(.005, 3)
tags(fig, axes)
save(fig, HERE, 'figure', {'hv_true': hv_true, 'hv_final': float(H[-1, 0])}); print(hv_true, H[-1])
