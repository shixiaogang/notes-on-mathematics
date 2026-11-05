"""Preserve Matplotlib panel paths in a hybrid (raster + vector) SVG.

This file is not a tracing or pure-vector version of the model artwork.
"""
from pathlib import Path
import base64,json,xml.etree.ElementTree as ET
from PIL import Image
O=Path(__file__).resolve().parent
ROOT=next(p for p in O.parents if (p/'build.sh').exists())
N='http://www.w3.org/2000/svg'
ET.register_namespace('',N)
def main():
    w,h=Image.open(O/'background.png').size
    root=ET.Element('{'+N+'}svg',{'width':f'{w/300*25.4:.6f}mm','height':f'{h/300*25.4:.6f}mm','viewBox':f'0 0 {w} {h}'})
    ET.SubElement(root,'{'+N+'}desc').text='Hybrid illustration: raster model schematic and real-font text; five precise Matplotlib vector probability panels. Not a pure-vector illustration.'
    def embed(name):
        ET.SubElement(root,'{'+N+'}image',{'x':'0','y':'0','width':str(w),'height':str(h),
            'href':'data:image/png;base64,'+base64.b64encode((O/name).read_bytes()).decode()})
    embed('background.png')
    d=json.loads((O/'probability-data.json').read_text())
    for p in d['panels']:
        node=ET.parse(O/'panels'/(p['id']+'.svg')).getroot()
        vx,vy,vw,vh=map(float,node.attrib['viewBox'].split())
        group=ET.SubElement(root,'{'+N+'}g',{'transform':f"translate({p['origin'][0]} {p['origin'][1]}) scale({d['plot_width_px']/vw} {d['plot_height_px']/vh})"})
        for child in node:
            if child.tag not in ['{'+N+'}metadata','{'+N+'}desc']:group.append(child)
    embed('text-layer.png')
    ET.ElementTree(root).write(O/'figure-hybrid.svg',encoding='utf-8',xml_declaration=True)
if __name__=='__main__':main()
