from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Correlated Gaussian pair, unit variances, correlation 0.9; N = 16 points (2 bits per component).
# (a) product of two 4-level Gaussian Lloyd-Max quantizers; (b) joint codebook from the Lloyd iteration on
# n = 200000 simulated vectors (seed 1), started from the product codebook; distortion of both evaluated on an
# independent sample of 200000 vectors (seed 2). Green dots: 1500 of the test vectors; red: codebook; gray: cells.
rho = .9; S = np.array([[1, rho], [rho, 1]]); A = np.linalg.cholesky(S)
Xtr = np.random.default_rng(1).standard_normal((200000, 2))@A.T
Xte = np.random.default_rng(2).standard_normal((200000, 2))@A.T
t4, c4, D4 = gauss_lloyd(4)
Cp = np.array([[a, b] for a in c4 for b in c4])
Cj = lloyd_samples(Xtr, Cp, 80)
Dp = nearest(Xte, Cp)[1].mean()/2; Dj = nearest(Xte, Cj)[1].mean()/2
box = (-3.6, 3.6, -3.6, 3.6)
fig, (a, b) = figure(width_mm=108, height_mm=60, ncols=2)
panel(fig, left=.07, right=.98, bottom=.23, top=.97, wspace=.22)
for ax in (a, b):
    ax.plot(Xte[:1500, 0], Xte[:1500, 1], '.', ms=1.2, color=GREEN, mew=0)
    ax.set_xlim(box[0], box[1]); ax.set_ylim(box[2], box[3]); ax.set_aspect('equal')
    ax.set_xticks([-3, 0, 3]); ax.set_yticks([-3, 0, 3])
for t in t4: a.axvline(t, color=STROKE, lw=.8); a.axhline(t, color=STROKE, lw=.8)
a.plot(Cp[:, 0], Cp[:, 1], 'o', ms=3.2, color=RED, mew=0)
for p, q in voronoi_edges(Cj, box): b.plot([p[0], q[0]], [p[1], q[1]], color=STROKE, lw=.8)
b.plot(Cj[:, 0], Cj[:, 1], 'o', ms=3.2, color=RED, mew=0)
a.set_xlabel('$x_1$', labelpad=1); b.set_xlabel('$x_1$', labelpad=1); a.set_ylabel('$x_2$', labelpad=1)
tags(fig, (a, b), y=.005)
nused = int(sum((nearest(Xte, Cp)[0] == k).mean() > 1e-3 for k in range(16)))
save(fig, HERE, 'figure', {'scalar_lloyd_max_4': [float(v) for v in c4], 'scalar_D': float(D4),
     'product_D_per_component_test': float(Dp), 'joint_D_per_component_test': float(Dj),
     'product_cells_with_prob_above_1e-3': nused,
     'product_cell_probs': sorted([float((nearest(Xte, Cp)[0] == k).mean()) for k in range(16)])})
