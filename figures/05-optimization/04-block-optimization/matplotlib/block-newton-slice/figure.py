from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Block Newton model on a conditional function. (a) z^2+4z+16 at z=3. (b) z^4+2z at z=1.
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, .085, .985, .97, .25, wspace=.27)
z = np.linspace(-6, 4, 300); p = z**2+4*z+16
a.plot(z, p, color=BLUE, lw=2.6); a.plot(z, p, color=GREEN, lw=1.1, ls=(0, (4, 3)))
a.plot([3], [37], 'o', color=GREEN, ms=4.5, mew=0, zorder=5); opt(a, -2, 12)
a.text(1.7, 39.5, '$z$', fontsize=7.5, color=INK); a.text(-2.8, 16, '$z^+$', fontsize=7.5, color=INK)
a.set_xlabel('$z$', labelpad=1); a.set_ylabel('条件目标', labelpad=1); a.set_ylim(0, 46)
z = np.linspace(-1.5, 1.7, 400); ph = z**4+2*z; m = 3+6*(z-1)+6*(z-1)**2
b.plot(z, ph, color=BLUE, lw=1.4); b.plot(z, m, color=GREEN, lw=1.4)
zs = -(.5)**(1/3); b.plot([1], [3], 'o', color=GREEN, ms=4.5, mew=0, zorder=5); b.plot([.5], [.5**4+1], 's', color=GREEN, ms=4, mew=0, zorder=5); b.plot([.5], [3-3+1.5], 'o', mfc='white', mec=GREEN, ms=4.5, zorder=5); opt(b, zs, zs**4+2*zs)
b.text(1.08, 2.55, '$z$', fontsize=7.5, color=INK); b.text(.56, .72, '$z^+$', fontsize=7.5, color=INK); b.text(-1.35, 5.2, '原函数', fontsize=7.5, color=INK); b.text(-.45, 8.3, '二阶模型', fontsize=7.5, color=INK); b.text(-.42, -1.75, '精确解', fontsize=7.5, color=INK, ha='left')
b.set_xlabel('$z$', labelpad=1); b.set_xlim(-1.5, 1.7); b.set_ylim(-2.1, 10)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'exact': float(zs)})
