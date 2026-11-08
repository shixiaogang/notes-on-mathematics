from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
# f takes the values 2,4,8,6 on the four dyadic intervals of level 2.
# Row (a): phi_{2,k}=2*1_{I_{2,k}} with coordinates (1,2,4,3). Row (b): phi_{0,0}, psi_{0,0}, psi_{1,0}, psi_{1,1} with coordinates (5,-2,-1/sqrt2,1/sqrt2).
fig, axes = figure(width_mm=112, height_mm=70, nrows=2, ncols=5)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.94, bottom=.19, wspace=.34, hspace=1.15)
r2 = np.sqrt(2.0)
A = [(2,0,0,0),(0,2,0,0),(0,0,2,0),(0,0,0,2)]
B = [(1,1,1,1),(1,1,-1,-1),(r2,-r2,0,0),(0,0,r2,-r2)]
names = [[r'$\varphi_{2,0}$',r'$\varphi_{2,1}$',r'$\varphi_{2,2}$',r'$\varphi_{2,3}$'],
         [r'$\varphi_{0,0}$',r'$\psi_{0,0}$',r'$\psi_{1,0}$',r'$\psi_{1,1}$']]
coefs = [['c=1','c=2','c=4','c=3'],['c=5','c=-2',r'c=-1/\sqrt{2}',r'c=1/\sqrt{2}']]
f = (2,4,8,6)
edges = np.arange(5)/4
def step(ax, v, c, lw=1.4):
    ax.step(edges, list(v)+[v[-1]], where='post', color=c, lw=lw, solid_joinstyle='miter')
for r, basis in enumerate((A,B)):
    for c, v in enumerate(basis):
        ax = axes[r][c]; step(ax, v, GREEN)
        ax.axhline(0, color=MUTED, lw=.6)
        ax.set_xlim(0,1); ax.set_ylim(-2.5,2.7); ax.set_xticks([0,1]); ax.set_yticks([-2,0,2])
        ax.tick_params(labelsize=7, length=2, pad=1.5)
        ax.text(.5,1.05,names[r][c],transform=ax.transAxes,ha='center',va='bottom')
        ax.text(.5,-.26,'$'+coefs[r][c]+'$',transform=ax.transAxes,ha='center',va='top',fontsize=7.5,color=INK)
    ax = axes[r][4]; step(ax, f, BLUE)
    ax.set_xlim(0,1); ax.set_ylim(0,9); ax.set_xticks([0,1]); ax.set_yticks([0,4,8])
    ax.tick_params(labelsize=7, length=2, pad=1.5)
    ax.text(.5,1.05,'$f$',transform=ax.transAxes,ha='center',va='bottom')
for r, s in enumerate('ab'):
    y = {0:.52, 1:.01}[r]
    fig.text(.5, y, '(%s)'%s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=2,4,8,6 on I_{2,k}; two orthonormal bases of V_2 with coordinates (1,2,4,3) and (5,-2,-1/sqrt2,1/sqrt2)'})
