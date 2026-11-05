from pathlib import Path
import sys, json, hashlib, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p / "build.sh").exists())
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
import plot_style as ps
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from fontTools.ttLib import TTFont
ps.configure()
OUT = Path(__file__).resolve().parent
FONT_LICENSES = ["fonts/licenses/SourceHanSans-OFL.txt", "fonts/licenses/LXGWWenKai-OFL.txt", "fonts/licenses/FiraMath-font-license.txt", "fonts/licenses/STIX-OFL.txt"]

def finish(fig, title, size_mm, formulas, data, rationale):
    ps.prepare_figure(fig)
    fig.savefig(OUT / "figure.pdf")
    fig.savefig(OUT / "figure.png", dpi=400)
    versions = {}
    for path in [ps.CN_FILE, ps.NOTE_FILE, ps.EN_FILE, ps.STIX_FILE]:
        with TTFont(path) as font:
            values = [n.toUnicode() for n in font["name"].names if n.nameID == 5]
            versions[path.name] = values[0] if values else "not recorded in font"
    record = {"title":title,"kind":"analytic teaching construction; not experimental data",
      "formula_and_parameters":formulas,"data":data,"physical_size_mm":size_mm,
      "body_reference_width_mm":size_mm[0],"scale":1,"main_label_size_pt":8,"note_size_pt":7.5,
      "provenance":"Original figure computed from the explicit teaching model in the adjoining textbook passage",
      "teaching_necessity":rationale,"external_data":None,"missing_values":None,"filtering":None,
      "sampling":"Deterministic analytic grids; no experimental or simulated observations",
      "generation_date":"2026-10-17","preview_dpi":400,"font_licenses":FONT_LICENSES,
      "font_versions":versions,"style":ps.style_record(),
      "files_sha256":{name:hashlib.sha256((OUT/name).read_bytes()).hexdigest() for name in ["source.py","figure.pdf","figure.png"]}}
    (OUT / "metadata.json").write_text(json.dumps(record, ensure_ascii=False, indent=2)+"\n")
    plt.close(fig)

size=(105,89)
fig=plt.figure(figsize=(size[0]/25.4,size[1]/25.4))
ax=fig.add_axes([.16,.21,.62,.70]); cbax=fig.add_axes([.83,.21,.035,.70])
a=np.linspace(0,1,301); b=np.linspace(0,1,301); aa,bb=np.meshgrid(a,b)
tau=.34+.4*aa-.6*bb
cmap=mcolors.LinearSegmentedColormap.from_list('effect',[(0,ps.BLUE),(.26,'white'),(1,ps.GREEN)])
image=ax.pcolormesh(a,b,tau,cmap=cmap,vmin=-.26,vmax=.74,shading='nearest',rasterized=True)
cont=ax.contour(aa,bb,tau,levels=[-.2,0,.2,.4,.6],colors=ps.STROKE,linewidths=.6)
ax.clabel(cont,inline=True,fmt='%g',fontsize=8,manual=[(.07,.9467),(.33,.7867),(.50,.5667),(.55,.2333),(.91,.1733)])
ax.scatter([0,1],[1,0],s=34,c=[ps.BLUE,ps.GREEN],edgecolor=ps.STROKE,lw=.6,zorder=4,clip_on=False)
ax.annotate(r'$-0.26$',xy=(0,1),xytext=(.17,.88),ha='left',va='center',fontsize=8,color=ps.INK,arrowprops={'arrowstyle':'-','color':ps.STROKE,'lw':.6})
ax.annotate(r'$0.74$',xy=(1,0),xytext=(.58,.12),ha='left',va='center',fontsize=8,color=ps.INK,arrowprops={'arrowstyle':'-','color':ps.STROKE,'lw':.6})
ax.set(xlim=(0,1),ylim=(0,1),aspect='equal',xticks=[0,.5,1],yticks=[0,.5,1],xlabel=r'未处理者缺失均值 $a=\mathbb{E}[Y(1)\mid T=0]$',ylabel=r'已处理者缺失均值 $b=\mathbb{E}[Y(0)\mid T=1]$')
ax.set_title(r'$\tau=0.34+0.4a-0.6b$',loc='left',pad=11)
cb=fig.colorbar(image,cax=cbax,ticks=[-.26,0,.25,.5,.74]); cb.set_label(r'平均处理效应 $\tau$',labelpad=5)
assert abs(tau[0,-1]-.74)<1e-12 and abs(tau[-1,0]+.26)<1e-12
finish(fig,'Manski sharp bounds from the two missing potential-outcome means',size,
 {'P_T1':.6,'observed_mean_Y_T1':.7,'observed_mean_Y_T0':.2,'a':'E[Y(1)|T=0] in [0,1]','b':'E[Y(0)|T=1] in [0,1]','effect':'.34+.4a-.6b','grid':[0,1,301]},
 {'known_E_TY':.42,'known_E_1minusT_Y':.08,'lower':-.26,'upper':.74,'width':1,'lower_corner':[0,1],'upper_corner':[1,0]},
 'Shows exactly which two unobserved conditional means remain free and which corner assignments attain the lower and upper effects without changing any observed law.')
