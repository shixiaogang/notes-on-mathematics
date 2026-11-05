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
gs=fig.add_gridspec(1,2,width_ratios=[1.35,1],left=.075,right=.985,bottom=.24,top=.86,wspace=.35)
ax=fig.add_subplot(gs[0,0]); geo=fig.add_subplot(gs[0,1])
sigma=1.; n=25; a=sigma/(2*np.sqrt(n)); sd=sigma/np.sqrt(n)
x=np.linspace(-.7,.7,1201)
p0=np.exp(-.5*((x+a)/sd)**2)/(sd*np.sqrt(2*np.pi))
p1=np.exp(-.5*((x-a)/sd)**2)/(sd*np.sqrt(2*np.pi))
ax.fill_between(x,0,np.minimum(p0,p1),facecolor=ps.BLUE_FILL,zorder=0)
ax.plot(x,p0,color=ps.BLUE,label=r'$P_0:\ \mu=-a$')
ax.plot(x,p1,color=ps.GREEN,ls='--',label=r'$P_1:\ \mu=a$')
ax.axvline(0,color=ps.STROKE,lw=.6,ls=':')
ax.set(xlim=(-.65,.65),ylim=(0,2.7),xticks=[-.4,-.2,0,.2,.4],yticks=[0,1,2],xlabel=r'样本均值 $\overline{X}$',ylabel='概率密度')
ax.set_title('(a) 可用观测仍有重叠',loc='left',pad=10)
ax.legend(loc='upper right',handlelength=1.8,borderaxespad=.25)
ax.text(-.63,2.32,r'$n=25,\ a=0.1$',fontsize=8)
ax.text(-.46,.20,r'选 $0$',fontsize=8); ax.text(.40,.20,r'选 $1$',fontsize=8)
geo.set_title('(b) 小估计误差能正确解码',loc='left',pad=10)
geo.axvline(0,color=ps.STROKE,lw=.6,ls=':')
for y,center,color,label in [(.72,-a,ps.BLUE,r'$|\widehat{\theta}-\theta_0|<a$'),(.35,a,ps.GREEN,r'$|\widehat{\theta}-\theta_1|<a$')]:
    geo.plot([center-a,center+a],[y,y],color=color,lw=2.2)
    geo.scatter([center-a,center+a],[y,y],s=25,facecolors='white',edgecolors=color,zorder=3,lw=.8)
    geo.scatter([center],[y],s=18,color=color,zorder=4)
    geo.text(center,y+.12,label,ha='center',fontsize=8)
geo.text(-a,.08,r'$\theta_0$',ha='center'); geo.text(a,.08,r'$\theta_1$',ha='center')
geo.set(xlim=(-.27,.27),ylim=(-.02,1.08),xticks=[-2*a,-a,0,a,2*a],xticklabels=[r'$-2a$',r'$-a$',r'$0$',r'$a$',r'$2a$'],yticks=[],xlabel=r'估计值 $\widehat{\theta}$')
geo.spines['left'].set_visible(False)
kl=2*n*a*a/(sigma*sigma); tv=math.erf(.5/math.sqrt(2)); error=.5*(1-tv)
assert abs(kl-.5)<1e-12 and abs(error-.3085375387259869)<1e-12
finish(fig,'Le Cam: observation overlap and disjoint target error neighborhoods',size,
 {'sigma':sigma,'n':n,'a':a,'sample_mean_sd':sd,'density':'N(-a,sigma²/n), N(a,sigma²/n)','target_radius':'s=a','target_separation':'2a'},
 {'batch_KL':kl,'TV_exact':tv,'minimal_equal_prior_test_error':error,'Pinsker_bad_event_lower_bound':.25},
 'Exposes the two separate steps: overlapping observation laws limit tests, while an estimate inside a small target neighborhood yields a correct nearest-target test.')
