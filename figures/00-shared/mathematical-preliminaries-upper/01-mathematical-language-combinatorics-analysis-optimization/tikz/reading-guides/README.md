# 数学准备阅读结构重构插图

`chNN/`按最终17章编号保存TikZ/PGFPlots源文件、教学数据、生成脚本及插图PDF/PNG。正式正文通过相对路径使用图源或插图；`preview.tex`等入口只供独立插图校样。

所有命令从仓库根目录执行。已有`render.py`的章节可运行：

```sh
python3 figures/00-shared/mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/tikz/combinatorics/render.py
```

脚本使用仓库字体、XeLaTeX、xdvipdfmx和PyMuPDF，输出插图到本章目录，编译缓存写到`build/math-restructure-figures/chNN/`。不需要安装或修改全局依赖。第1章的`export-previews.py`读取该缓存目录中的`figures-preview.pdf`，对应校样入口是本章的`figures-preview.tex`；编译时也应指定此输出目录。

直接编译其他`preview.tex`时，同样将输出目录设在`build/math-restructure-figures/chNN/`。整卷验收使用项目根目录的`./build.sh all`，不以独立插图校样代替正式成品。

早期作者报告中的`render/`、`.render/`、`.preview/`和`review/`记录生成时的位置。齐稿后，这些临时文件已逐文件校验哈希并迁到`build/math-restructure-figures/`，迁移对应表保存在该目录的`relocations.json`。历史报告不据此改写成新的视觉验收记录。
