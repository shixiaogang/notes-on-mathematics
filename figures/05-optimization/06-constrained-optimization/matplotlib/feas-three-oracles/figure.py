from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
# The three subproblems at the third PGD iterate x2 of the running example.
x = pgd(T=3)[1]; g = grad(x); a = .6
fig, axs = figure(width_mm=112, height_mm=48, ncols=3)
for ax in axs: triangle(ax); contours(ax, z=1.5); off(ax, (-.17, 1.17), (-.14, .94))
ax = axs[0]; z = x-a*g; za = z-(z.sum()-1)/3; p = proj(z)[0]; P = bary(x); Z = bary(za); Q = bary(p)
arrow(ax, P, Z, GREEN); arrow(ax, Z, Q, YELLOW, ls=(0, (2, 1.4)), lw=1.1); hollow(ax, Z, GREEN, ms=4); dot(ax, Q, GREEN, ms=4.4); dot(ax, P, GREEN, ms=4.4)
ax.text(P[0]+.04, P[1]+.03, '$x$', fontsize=8); ax.text(Q[0]-.06, Q[1]+.05, '$x^{+}$', fontsize=8, ha='right'); ax.text(Z[0]+.05, Z[1]-.01, '$z$', fontsize=8, ha='left', va='center')
ax = axs[1]; s = np.eye(3)[int(np.argmin(g))]; S = bary(s)
ax.plot([P[0], S[0]], [P[1], S[1]], color=GREEN, lw=1.4, zorder=5); dot(ax, P, GREEN, ms=4.4); dot(ax, S, GREEN, ms=5)
Y = P+(.25)*(S-P); dot(ax, Y, GREEN, ms=3.8); ax.text(Y[0], Y[1]+.05, '$x^{+}$', fontsize=8, ha='center')
ax.text(P[0]+.02, P[1]+.05, '$x$', fontsize=8); ax.text(S[0]+.03, S[1]+.07, '$s$', fontsize=8, ha='center')
ax = axs[2]; A_ = np.linspace(0, 2.2, 120); W = x*np.exp(-A_[:, None]*g); W = W/W.sum(axis=1, keepdims=True); XY = bary(W)
ax.plot(XY[:, 0], XY[:, 1], color=GREEN, lw=1.4, zorder=5); dot(ax, P, GREEN, ms=4.4)
W1 = x*np.exp(-a*g); W1 = W1/W1.sum(); dot(ax, bary(W1), GREEN, ms=4.4); ax.text(P[0]+.04, P[1]+.03, '$x$', fontsize=8); ax.text(bary(W1)[0]-.06, bary(W1)[1]+.0, '$x^{+}$', fontsize=8, ha='right', va='center')
panels(fig, .01, .99, .99, .1, .03); tags(fig, axs)
save(fig, HERE, 'figure', {'x': x.tolist(), 'alpha': a, 'z': z.tolist(), 'projection': p.tolist(), 'mirror': W1.tolist()})
