#!/usr/bin/env python3
"""Typeset real-font labels over the unchanged model-generated background."""
import hashlib
import json
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'tex/volumes.json').is_file())
FONT_PATHS = {
    'cn': ROOT / 'fonts/SourceHanSansSC-Normal.otf',
    'math': ROOT / 'fonts/FiraMath-Regular.otf',
    'note': ROOT / 'fonts/LXGWWenKai-Regular.ttf',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    config = json.loads((HERE / 'labels.json').read_text())
    background = Image.open(HERE / config['background']).convert('RGBA')
    layer = Image.new('RGBA', background.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cmaps = {role: TTFont(path).getBestCmap() for role, path in FONT_PATHS.items()}
    boxes = []
    for label in config['labels']:
        runs = label['runs']
        widths = []
        for run in runs:
            missing = [c for c in run['text'] if not c.isspace() and ord(c) not in cmaps[run['font']]]
            if missing:
                raise ValueError((label['id'], missing))
            font = ImageFont.truetype(str(FONT_PATHS[run['font']]), run['size'])
            widths.append(draw.textlength(run['text'], font=font))
        x = label['center'][0] - sum(widths) / 2
        y = label['center'][1]
        for run, width in zip(runs, widths):
            font = ImageFont.truetype(str(FONT_PATHS[run['font']]), run['size'])
            xy = (x, y + run.get('dy', 0))
            bbox = draw.textbbox(xy, run['text'], font=font, anchor='lm')
            if not (0 <= bbox[0] <= bbox[2] < background.width and 0 <= bbox[1] <= bbox[3] < background.height):
                raise ValueError((label['id'], bbox))
            draw.text(xy, run['text'], font=font, fill=label.get('color', '#3B4252'), anchor='lm')
            boxes.append({'id': label['id'], 'text': run['text'], 'font': run['font'], 'size_px': run['size'], 'bbox': list(bbox)})
            x += width
    layer.save(HERE / 'text-layer.png')
    final = Image.alpha_composite(background, layer).convert('RGB')
    final.save(HERE / 'figure.png', dpi=(290, 290))
    # This preview represents the 169 mm book figure rendered at 125 dpi.
    width = round(config['book_width_mm'] / 25.4 * 125)
    final.resize((width, round(width * final.height / final.width)), Image.Resampling.LANCZOS).save(HERE / 'book-size-preview.png')
    font_records = {}
    for role, path in FONT_PATHS.items():
        font = TTFont(path)
        font_records[role] = {
            'path': str(path.relative_to(ROOT)), 'sha256': digest(path),
            'version': next((n.toUnicode() for n in font['name'].names if n.nameID == 5), None),
        }
    report = {
        'background_sha256': digest(HERE / config['background']),
        'final_sha256': digest(HERE / 'figure.png'),
        'canvas_px': list(background.size),
        'book_width_mm': config['book_width_mm'],
        'effective_ppi': background.width / (config['book_width_mm'] / 25.4),
        'font_records': font_records,
        'font_licenses': ['fonts/licenses/SourceHanSans-OFL.txt', 'fonts/licenses/FiraMath-font-license.txt', 'fonts/licenses/LXGWWenKai-OFL.txt'],
        'book_point_sizes': {str(n): n * config['book_width_mm'] / 25.4 * 72 / background.width for n in [24, 30, 32, 34]},
        'glyph_coverage_passed': True, 'label_bounds_passed': True,
        'artwork_modified': False, 'texture_cleanup': False,
        'labels': boxes,
    }
    (HERE / 'typography-check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
