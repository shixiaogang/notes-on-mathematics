from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
# 贯穿例：f_i(x)=a_i(x-b_i)^2/2，a=(1,2,3)，b=(-3,0,3)；f(x)=(x-1)^2+5，x*=1。
A = np.array([1., 2., 3.]); B = np.array([-3., 0., 3.])
def gi(x): return A*(x-B)
def panel(fig, left, right, top, bottom, wspace=.3, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.05):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='top')

def run(alpha,T=800,d0=4.,B=1):
    m,s=d0,d0*d0; out=[s]
    for t in range(T):
        a=alpha(t)
        s=(1-4*a+4*a*a)*s+a*a*(2*s-20*m+56)/(3*B)
        m=(1-2*a)*m; out.append(s)
    return np.array(out)
fig,(a,b)=figure(width_mm=112,height_mm=58,ncols=2)
panel(fig,.095,.985,.97,.24,wspace=.3)
T=np.arange(801)
a.semilogy(T,run(lambda t:.1),color=GREEN,lw=1.4)
a.semilogy(T,run(lambda t:.02),color=YELLOW,lw=1.6)
a.semilogy(T,run(lambda t:1/(2*(t+5))),color=PURPLE,lw=1.3)
a.semilogy(T,run(lambda t:.1*.5**(t//200)),color=BLUE,lw=1.3,ls=(0,(4,2)))
a.text(420,.75,r'$\alpha=0.1$',fontsize=7.5); a.text(120,1.4,r'$\alpha=0.02$',fontsize=7.5)
a.text(330,.0165,r'$\alpha^{(t)}=\frac{1}{2(t+5)}$',fontsize=7.5); a.text(610,.135,'分段',fontsize=7.5)
a.set_xlabel('$t$',labelpad=1); a.set_ylabel(r'$\mathrm{E}[f-f^*]$',labelpad=1); a.set_xlim(0,800); a.set_ylim(.008,30)
al=np.linspace(.005,.6,200)
b.plot(al,28*al/(6-7*al),color=GREEN,lw=1.5)
b.plot(al,al*2*(56/3)/(2*2),color=PURPLE,lw=1.1,ls=(0,(4,2)))
b.text(.27,.85,'精确稳态',fontsize=7.5,ha='left'); b.text(.1,2.5,'上界形式',fontsize=7.5,ha='left')
b.set_xlabel(r'$\alpha$',labelpad=1); b.set_ylabel('噪声底',labelpad=1); b.set_xlim(0,.6); b.set_ylim(0,6)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
print('T800 gaps',[float(run(f)[-1]) for f in (lambda t:.1,lambda t:.02,lambda t:1/(2*(t+5)),lambda t:.1*.5**(t//200))])
save(fig,HERE,'figure',{'d0':4})
