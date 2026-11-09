from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# f=(x1^2+9x2^2)/2，x=(9,1)。各向同性变异的成功样本与成功概率
f=lambda x1,x2:(x1**2+9*x2**2)/2; rng=np.random.default_rng(5); x0=np.array([9.,1.]); f0=f(*x0)
fig,axes=figure(width_mm=112,height_mm=60,ncols=2); panel(fig,.08,.985,.965,.245,.3)
a=axes[0]; g=np.linspace(0,16,500); h=np.linspace(-4.5,6.5,400); X,Y=np.meshgrid(g,h); a.contour(X,Y,f(X,Y),levels=[10,45,100,160],colors=[BLUE],linewidths=.7)
Z=rng.standard_normal((60,2)); S=x0+2*Z; ok=f(S[:,0],S[:,1])<f0
a.plot(S[ok,0],S[ok,1],'o',ms=2.9,color=GREEN,mew=0); a.plot(S[~ok,0],S[~ok,1],'o',ms=2.9,mfc='white',mec=RED,mew=.7); a.plot([9],[1],'o',ms=4.4,mfc=INK,mec=INK,mew=0,zorder=6)
a.set_aspect('equal'); a.set_xlim(2,15.5); a.set_ylim(-4.5,6.5); a.set_xticks([4,9,14]); a.set_yticks([-4,0,4]); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0)
print('rate',ok.mean())
b=axes[1]; rng=np.random.default_rng(6); Z=rng.standard_normal((800000,2)); sig=np.logspace(-1,1.3,36)
p_iso=[np.mean(f(9+s*Z[:,0],1+s*Z[:,1])<f0) for s in sig]; p_ad=[np.mean(f(9+s*np.sqrt(3)*Z[:,0],1+s/np.sqrt(3)*Z[:,1])<f0) for s in sig]
b.plot(sig,p_iso,color=YELLOW,lw=1.6); b.plot(sig,p_ad,color=GREEN,lw=1.6); b.set_xscale('log'); b.set_xlim(.1,20); b.set_ylim(0,.55); b.set_xticks([.1,1,10]); b.set_xticklabels(['0.1','1','10']); b.minorticks_off(); b.set_yticks([0,.25,.5]); b.set_yticklabels(['0','0.25','0.5']); b.set_xlabel(r'$\sigma$',labelpad=1); b.set_ylabel('改善概率',labelpad=1)
b.text(.55,.08,'各向同性',fontsize=7.5,ha='center'); b.text(4.8,.42,'按等高线拉伸',fontsize=7.5,ha='center')
i=[np.argmin(abs(sig-s)) for s in (1,2,4,8)]; print([p_iso[j] for j in i],[p_ad[j] for j in i],sig[i])
tags(fig,axes); save(fig,HERE,'figure',{'x':[9,1],'seed':[5,6],'sigmas':sig.tolist(),'p_iso':p_iso,'p_shaped':p_ad})
