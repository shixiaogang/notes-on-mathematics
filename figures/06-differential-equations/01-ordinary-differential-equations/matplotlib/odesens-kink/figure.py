from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=|x| 的流映射 Lipschitz 但在 0 处不可微：x0>=0 时 x0 e^t，x0<0 时 x0 e^{-t}。
fig, axes = figure(width_mm=100, height_mm=46, ncols=2)
panel(fig, .085, .985, .955, .29, .24)
ax = axes[0]; t = np.linspace(0, 1, 201)
for x0 in (.3, .6, 1.): ax.plot(t, x0*np.exp(t), color=BLUE, lw=1.2)
for x0 in (-.3, -.6, -1.): ax.plot(t, x0*np.exp(-t), color=YELLOW, lw=1.2)
ax.plot(t, 0*t, color=RED, lw=1.4)
ax.set_xlim(0, 1); ax.set_ylim(-1.1, 2.8); ax.set_xticks([0, .5, 1]); ax.set_yticks([-1, 0, 1, 2]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$x$', labelpad=1)
ax = axes[1]; x0 = np.linspace(-1, 1, 401); ax.plot(x0, np.where(x0 >= 0, x0*np.e, x0/np.e), color=BLUE, lw=1.4); ax.plot([0], [0], 'o', ms=4.4, color=RED, mew=0, zorder=5)
ax.text(.28, 1.6, '$k=\\mathrm{e}$', color=BLUE, fontsize=7.5, ha='right'); ax.text(-.5, -.62, '$k=1/\\mathrm{e}$', color=BLUE, fontsize=7.5, ha='center')
ax.set_xlim(-1, 1); ax.set_ylim(-.9, 2.8); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$x_0$', labelpad=0); ax.set_ylabel('$\\varphi_1(x_0)$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'equation': "x'=|x|"})
