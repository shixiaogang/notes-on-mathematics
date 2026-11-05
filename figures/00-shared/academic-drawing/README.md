# 前三卷科研图共用样式

本目录保存已重绘图片使用的实际字体加载、Lancet 2024-07 颜色和独立 TikZ 导出工具。数据使用 Matplotlib；简单关系图使用 TikZ；复杂机制图采用无字模型 PNG 与真实字体文字层。各卷的图源、数值、标签、提示词、生成记录及重放入口随对应图保存，资源索引见上级 README。

中文主体为 `fonts/SourceHanSansSC-Normal.otf`，辅助说明为 `fonts/LXGWWenKai-Regular.ttf`；英文、数字和数学为 `fonts/FiraMath-Regular.otf`。仅 Fira Math 缺失的数学字形使用 `fonts/STIXTwoMath-Regular.otf`；`font-policy.json` 和 `font-exceptions.tex` 记录字形范围。版本与 SHA-256 见 `font-manifest.json` 和 `fonts/SHA256SUMS`，许可见 `fonts/licenses/`。

`plot_style.py` 固定 Agg 后端，明确绑定仓库字体，保留数据、解析式和字母表语义。`render_tikz.py` 使用 `preamble.tex` 独立编译 TikZ，输出嵌入字体的 PDF、SVG 与 300dpi PNG；正文使用 PDF，不将独立的 unicode-math 加载到书籍正文。运行示例（项目根目录）：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/<卷>/<部分>/tikz/<图组>/source.tex
```

Python 依赖包括 Matplotlib、NumPy、PyMuPDF、Pillow、fontTools；TikZ 导出需要 XeLaTeX 和 xdvipdfmx。各卷的重放说明列出实际依赖及组合图路径。文字位置或科学关系修改后须重新绘图并检查原尺寸及书页尺寸，再按项目要求构建全部七个版本。模型背景的重新生成不保证逐像素复现；保留原始背景与提示词，排字重放从已保存背景开始。
