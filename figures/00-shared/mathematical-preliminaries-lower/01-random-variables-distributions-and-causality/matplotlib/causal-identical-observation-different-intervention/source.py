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

size=(169,57)
fig,axes=plt.subplots(1,3,figsize=(size[0]/25.4,size[1]/25.4),sharey=True,gridspec_kw={'width_ratios':[1.4,1,1]})
fig.subplots_adjust(left=.065,right=.99,bottom=.26,top=.78,wspace=.30)
probs=[[.5,0,0,.5],[.5,.5],[0,1]]
for ax,pr,col in zip(axes,probs,[ps.BLUE,ps.BLUE,ps.GREEN]):
    positions=np.arange(len(pr))
    ax.bar(positions,pr,width=.52,color=ps.BLUE_FILL if col==ps.BLUE else ps.GREEN_FILL,edgecolor=col,lw=.9,zorder=2)
    for j,v in enumerate(pr):
        if v==0: ax.plot(j,0,'o',ms=3,mfc='white',mec=col,zorder=3)
        ax.text(j,v+.055,f'{v:g}',ha='center',fontsize=8,color=col)
    ax.set(ylim=(0,1.18),yticks=[0,.5,1],xticks=positions)
axes[0].set_xticklabels([r'$(0,0)$',r'$(0,1)$',r'$(1,0)$',r'$(1,1)$'])
axes[0].set(xlabel=r'自然记录 $(T,Y)$',ylabel='概率')
axes[0].set_title('(a) 甲、乙的观测规律相同',loc='left',pad=11)
for ax,title in zip(axes[1:],['(b) 甲保留 Y=U','(c) 乙保留 Y=T']):
    ax.set_xticklabels([r'$0$',r'$1$']); ax.set_xlabel(r'设定 $T=1$ 后的 $Y$')
    ax.set_title(title,loc='left',pad=11)
assert sum(probs[0])==sum(probs[1])==sum(probs[2])==1
finish(fig,'Identical observed joint law and different intervention responses',size,
 {'U':'Bernoulli(1/2)','model_A':'T=U,Y=U','model_B':'T=U,Y=T','action':'replace T=U with T=1; retain the respective Y equation'},
 {'observed_joint_TY':{'00':.5,'01':0,'10':0,'11':.5},'do_T1_Y_model_A':probs[1],'do_T1_Y_model_B':probs[2]},
 'Makes the first causal distinction concrete: identical factual laws do not determine an intervention law unless the response rule is fixed.')
