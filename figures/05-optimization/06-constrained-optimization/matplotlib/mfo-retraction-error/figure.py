from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Arc length reached on the circle: exp reaches s, normalization reaches arctan(s).
fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
s=np.linspace(0,3.2,300)
ax=axs[0]
ax.plot(s,s,color=PURPLE,lw=1.4,label='指数映射')
ax.plot(s,np.arctan(s),color=GREEN,lw=1.6,label='归一化')
ax.axhline(np.pi/2,color=GRAY,lw=.85,ls='--')
ax.text(3.15,np.pi/2+.08,r'$\pi/2$',ha='right',va='bottom',fontsize=7.5,color=MUTED)
ax.set_xlabel(r'$\Vert\mathbf{v}\Vert_2$'+'\n(a)'); ax.set_ylabel('走过的角度'); ax.legend(loc='upper left',handlelength=1.6)
ax=axs[1]
t=np.logspace(-2,.5,200)
ax.loglog(t,t-np.arctan(t),color=GREEN,lw=1.6,label='角度差')
ax.loglog(t,t**3/3,color=YELLOW,lw=1.4,ls='--',label=r'$\Vert\mathbf{v}\Vert_2^3/3$')
ax.set_xlabel(r'$\Vert\mathbf{v}\Vert_2$'+'\n(b)'); ax.legend(loc='upper left',handlelength=1.8)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'theta_exp=s, theta_norm=arctan s, difference ~ s^3/3'})
