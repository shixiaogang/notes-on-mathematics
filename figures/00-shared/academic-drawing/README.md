# 前三卷科研图共用样式

本目录保存已重绘图片使用的实际字体加载、蓝绿为主的五色低饱和度色板和独立 TikZ 导出工具。数据使用 Matplotlib；简单关系图使用 TikZ；复杂机制图采用无字模型 PNG 与真实字体文字层。各卷的图源、数值、标签、提示词、生成记录及重放入口随对应图保存，资源索引见上级 README。

中文主体为 `fonts/SourceHanSansSC-Normal.otf`，辅助说明为 `fonts/LXGWWenKai-Regular.ttf`；英文、数字和数学为 `fonts/FiraMath-Regular.otf`。仅 Fira Math 缺失的数学字形使用 `fonts/STIXTwoMath-Regular.otf`；`font-policy.json` 和 `font-exceptions.tex` 记录字形范围。版本与 SHA-256 见 `font-manifest.json` 和 `fonts/SHA256SUMS`，许可见 `fonts/licenses/`。

`plot_style.py` 固定 Agg 后端，明确绑定仓库字体，保留数据、解析式和字母表语义。`render_tikz.py` 使用 `preamble.tex` 独立编译 TikZ，输出嵌入字体的 PDF、SVG 与 300dpi PNG；正文使用 PDF，不将独立的 unicode-math 加载到书籍正文。运行示例（项目根目录）：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/<卷>/<部分>/tikz/<图组>/source.tex
```

Python 依赖包括 Matplotlib、NumPy、PyMuPDF、Pillow、fontTools；TikZ 导出需要 XeLaTeX 和 xdvipdfmx。各卷的重放说明列出实际依赖及组合图路径。文字位置或科学关系修改后须重新绘图并检查原尺寸及书页尺寸，再按项目要求构建当前登记的三卷。模型背景的重新生成不保证逐像素复现；保留原始背景与提示词，排字重放从已保存背景开始。


2026-11-08 的前三卷修订在主工作区 `e289a73` 的正文上新增 78 幅独立图，现用清单共 273 图（卷一 42、卷二 101、卷三 130）。所有现用图采用清晰线条，删除背景网格；矩阵单元、换元坐标网等数学结构不作背景网格处理。图内只保留必要短标注，条件、例子和结论集中在图注或正文。

`render_inventory.py` 根据现用清单批量导出 TikZ 图，逐图隔离局部定义，保留可编辑源文件。导出时对源中显式线宽乘 1.35，并设 0.65 pt 下限，默认线宽为 0.95 pt；调整只作用于临时编译输入，重复运行不会叠加。`plot_style.prepare_figure` 以一次性标记加粗主线与轮廓，并关闭二维和三维背景网格。解析曲线的公式、采样和参数保存在各图生成器及来源记录中。

```sh
python3 figures/00-shared/academic-drawing/render_inventory.py
python3 scripts/check_figure_integration.py
```

资产一致性、书页视觉检查和数学核对是不同步骤，清单中的校验值不代替视觉验收。

按逐图反馈，矩阵示意改用深灰括号与有留白的色块，避免浅灰内格线；过程图可使用 `BookInlineFigure` 紧随解释，跨栏图放在页底，为右侧页顶导航留出空间。卷三五组大图拆为十九幅步骤图，净增十四幅。

子图字母统一放在图元下方约 3 mm，同一行共享水平基线。TikZ 使用各子图的内容边界和整行边界定位；Matplotlib 在最后一次布局调整之后、导出之前按实际文字与坐标边界定位，不改变曲线与字号的物理大小，必要时只略增画布高度。树的三种性质另拆为三张独立图，分别贴近对应证明或示例。
