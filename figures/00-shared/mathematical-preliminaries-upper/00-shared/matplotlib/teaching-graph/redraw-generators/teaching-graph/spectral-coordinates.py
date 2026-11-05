"""Exact four-vertex path: shapes of RatioCut and NCut relaxations.

Teaching construction from the chapter's displayed matrices, no observations
or stochastic simulation. Both directions are shown with Euclidean norm 2
only to compare their shapes; the NCut minimization itself uses the D norm.
"""
from pathlib import Path
import json
import sys

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, style_record, BLUE, RED, GRID, MUTED

from plot_style import BLUE, GREEN, YELLOW, RED, PURPLE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
configure()
L = np.array([[1, -1, 0, 0], [-1, 2, -1, 0],
              [0, -1, 2, -1], [0, 0, -1, 1]], dtype=float)
D = np.diag([1, 2, 2, 1])
ratio = np.array([1 + np.sqrt(2), 1, -1, -1 - np.sqrt(2)])
ncut = np.array([1, .5, -.5, -1])
ratio = ratio * 2 / np.linalg.norm(ratio)
ncut = ncut * 2 / np.linalg.norm(ncut)
assert np.allclose(L @ ratio, (2 - np.sqrt(2)) * ratio)
assert np.allclose(L @ ncut, .5 * D @ ncut)
assert np.isclose(ratio.sum(), 0)
assert np.isclose(np.ones(4) @ D @ ncut, 0)

fig, ax = plt.subplots(figsize=(112 / 25.4, 58 / 25.4))
fig.subplots_adjust(left=.14, right=.97, bottom=.21, top=.90)
x = np.arange(1, 5)
ax.axhline(0, color=MUTED, lw=.6, zorder=0)
ax.axvline(2.5, color=GRID, lw=.6, linestyle=':', zorder=0)
ax.plot(x, ratio, color=BLUE, marker='o', markersize=4,
        label=r'RatioCut：$L u_2=(2-\sqrt{2})u_2$')
ax.plot(x, ncut, color=GREEN, marker='s', markersize=4, linestyle='--',
        label=r'NCut：$L y_2=\frac{1}{2} D^{(w)}y_2$')
ax.set_xticks(x)
ax.set_xlabel('路径上的顶点编号')
ax.set_ylabel('谱坐标')
ax.set_xlim(.8, 4.2)
ax.set_ylim(-1.6, 2.8)
ax.legend(loc='upper right', handlelength=2, borderaxespad=.1)
prepare_figure(fig)
for extension in ['pdf', 'svg', 'png']:
    fig.savefig(HERE / f'spectral-coordinates.{extension}', dpi=300)
plt.close(fig)
(HERE / 'spectral-data.json').write_text(json.dumps({
    'type': 'exact teaching construction, not experimental observations',
    'graph': {'vertices': [1, 2, 3, 4], 'edges': [[1, 2], [2, 3], [3, 4]],
              'weights': [1, 1, 1]},
    'L': L.tolist(), 'D': D.tolist(),
    'ratio_eigenvalue': float(2 - np.sqrt(2)), 'ncut_eigenvalue': .5,
    'display_vectors': {'ratio': ratio.tolist(), 'ncut': ncut.tolist()},
    'display_normalization': 'both vectors have Euclidean norm 2',
    'threshold': 0, 'partition': [[1, 2], [3, 4]],
    'line_between_nodes': 'visual guide only; no continuous domain interpolation',
    'style': style_record(), 'width_mm': 112, 'height_mm': 58,
}, ensure_ascii=False, indent=2) + '\n')
