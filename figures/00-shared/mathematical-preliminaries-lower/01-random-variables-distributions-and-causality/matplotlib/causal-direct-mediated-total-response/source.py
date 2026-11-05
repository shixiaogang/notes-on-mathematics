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

size=(169,60)
fig=plt.figure(figsize=(size[0]/25.4,size[1]/25.4))
gs=fig.add_gridspec(1,2,width_ratios=[1.4,1],left=.065,right=.985,bottom=.24,top=.86,wspace=.34)
response=fig.add_subplot(gs[0,0]); parts=fig.add_subplot(gs[0,1])
t=np.linspace(0,1,201)
response.plot(t,7*t,color=ps.STROKE,label=r'让中介重算：$Y(t)=7t$')
response.plot(t,t,color=ps.BLUE,ls='--',label=r'同时固定中介：$Y(t,0)=t$')
response.scatter([1,1],[7,1],color=[ps.STROKE,ps.BLUE],s=22,zorder=3)
response.set(xlim=(0,1.08),ylim=(0,8.4),xticks=[0,.5,1],yticks=[0,1,3,5,7],xlabel=r'培训处理 $t$',ylabel='行动后成绩')
response.set_title('(a) 同一背景下的两种行动',loc='left',pad=10)
response.legend(loc='upper left',handlelength=1.7,labelspacing=.35,borderaxespad=.2)
parts.bar([0,1],[1,1],width=.5,color=ps.BLUE_FILL,edgecolor=ps.BLUE,lw=.9,label='直接贡献')
parts.bar([0],[6],bottom=[1],width=.5,color=ps.GREEN_FILL,edgecolor=ps.GREEN,lw=.9,label='经中介的贡献')
parts.text(0,.5,r'$1$',ha='center',va='center'); parts.text(0,4,r'$6$',ha='center',va='center')
parts.text(1,.5,r'$1$',ha='center',va='center'); parts.text(0,7.2,r'$7$',ha='center')
parts.set(xlim=(-.65,1.65),ylim=(0,8.4),xticks=[0,1],xticklabels=['让中介重算','固定中介为 0'],yticks=[0,1,3,5,7],ylabel='处理从 0 到 1 的成绩增量')
parts.set_title('(b) 增量按局部机制合成',loc='left',pad=10)
parts.legend(loc='upper right',bbox_to_anchor=(1.01,1.03),handlelength=.9,labelspacing=.3)
assert 1+3*2==7
finish(fig,'Direct and mediated mechanisms compose the total response',size,
 {'M':'2T+U_M','Y':'T+3M+U_Y','fixed_background':'U_M=U_Y=0','total_intervention':'do(T=t), gives M=2t and Y=7t','controlled_intervention':'do(T=t,M=0), gives Y=t'},
 {'t_grid':[0,1,201],'direct_increment':1,'mediated_increment':6,'total_increment':7,'controlled_increment':1},
 'Separates preserving a downstream equation from freezing its current value, and connects the chain-rule formula beta+gamma alpha to the exact 1+6=7 construction.')
