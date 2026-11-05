#!/usr/bin/env python3
"""Render actual Volume 1 figure pages; this collects evidence, not verdicts."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import pymupdf as fitz
from book_catalog import volumes

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--labels',nargs='*')
    p.add_argument('--extra',nargs='*',default=[])
    p.add_argument('--between',nargs=2,action='append',default=[],metavar=('FROM_LABEL','TO_LABEL'))
    p.add_argument('--dpi',type=int,default=180)
    p.add_argument('--volume', type=int, choices=[v["number"] for v in volumes()], default=1)
    a=p.parse_args();root=a.root.resolve();out=a.output.resolve()
    volume = next(v for v in volumes(root) if v["number"] == a.volume)
    pdf=root/'target'/volume["pdf"]
    aux=root/'build'/(volume["slug"] + ".aux")
    registry=root/'figures/00-shared/academic-drawing/integration-manifest.json'
    rows=[x for x in json.loads(registry.read_text())['records']
          if x["owner"].startswith("tex/" + volume["slug"] + "/")]
    if a.labels:rows=[x for x in rows if x['label'] in a.labels]
    rows += [{'label':label,'kind':'table'} for label in a.extra]
    labels={label:(num,page) for label,num,page in re.findall(
        r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',aux.read_text())}
    doc=fitz.open(pdf);page_map={doc[i].get_label():i for i in range(len(doc))}
    for left,right in a.between:
        first=page_map[labels[left][1]];last=page_map[labels[right][1]]
        if last<first:raise ValueError(f'Reversed label interval: {left} to {right}')
        rows += [{'label':f'{left}..{right}:pdf-page-{i+1}',
                  'kind':'context_page','context_pdf_page':i+1,
                  'context_from':left,'context_to':right} for i in range(first,last+1)]
    pdf_sha=digest(pdf);dest=out/pdf_sha[:16];dest.mkdir(parents=True,exist_ok=True)
    page_records={};items=[]
    for row in rows:
        label=row['label']
        if 'context_pdf_page' in row:
            index=row['context_pdf_page']-1;number='context';printed_page=doc[index].get_label()
        else:
            number,printed_page=labels[label];index=page_map[printed_page]
        page=doc[index]
        if index not in page_records:
            name=f'page-{index+1:04d}-{a.dpi}dpi.png'
            page.get_pixmap(dpi=a.dpi,alpha=False).save(dest/name)
            fonts=[]
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines',[]):
                    for span in line['spans']:
                        if any(x in span['font'].lower() for x in ['fira','sourcehansanssc','wenkai']):
                            fonts.append({'text':span['text'],'font':span['font'],
                                          'size_pt':span['size'],'bbox_pt':span['bbox']})
            images=[{'bbox_pt':x['bbox'],'pixels':[x['width'],x['height']],
                     'actual_width_mm':(x['bbox'][2]-x['bbox'][0])*25.4/72}
                    for x in page.get_image_info()]
            page_records[index]={'pdf_page':index+1,'printed_page':printed_page,
                'image':name,'image_sha256':digest(dest/name),'image_bboxes':images,
                'figure_font_spans':fonts,'inspection_status':'awaiting human inspection'}
        item={'label':label,'number':number,'printed_page':printed_page,
              'pdf_page':index+1,'page_image':page_records[index]['image'],
              'page_image_sha256':page_records[index]['image_sha256'],
              'inspection_status':'awaiting human inspection'}
        for key in ['owner','asset']:
            if key in row:item[key]=row[key];item[key+'_sha256']=digest(root/row[key])
        sources=row.get('source',[])
        for key in ['kind','context_from','context_to']:
            if key in row:item[key]=row[key]
        if isinstance(sources,str):sources=[sources]
        item['source_sha256']={s:digest(root/s) for s in sources}
        if row.get('asset','').endswith('.pdf'):
            with fitz.open(root/row['asset']) as native:
                item['native_size_mm']=[native[0].rect.width*25.4/72,native[0].rect.height*25.4/72]
        items.append(item)
    report={'pdf':str(pdf.relative_to(root)),'pdf_sha256':pdf_sha,
        'aux':str(aux.relative_to(root)),'aux_sha256':digest(aux),
        'registry':str(registry.relative_to(root)),'registry_sha256':digest(registry),
        'dpi':a.dpi,'scope':'actual book page renders; no automated acceptance',
        'items':items,'pages':list(page_records.values())}
    (dest/'binding.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'binding':str(dest/'binding.json'),'items':len(items),'pages':len(page_records)},ensure_ascii=False))

if __name__=='__main__':main()
