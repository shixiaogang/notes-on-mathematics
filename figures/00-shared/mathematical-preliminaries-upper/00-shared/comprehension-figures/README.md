# 卷一概念图解

本组新增50幅图，补充当前正文中不易仅凭公式理解的关系、条件、运算与反例。章间数量按理解难度及已有图解覆盖分配：第1—9章分别为2、3、6、8、7、8、9、4、3幅。原有图及正文推理保留。

## 资源与制作

各部分 `tikz/comprehension-additions/` 保存基本几何、规则格表与少量节点关系的可编辑图源及导出；`matplotlib/comprehension-additions/` 保存精确解析曲线的生成脚本、公式、参数和导出。图片不承担一般性证明，图注写明教学设定和条件。没有用生成图像近似精确曲线或数值。

`support.py` 只服务本组图，按 `specs/figures.md` 使用当前低饱和度色板、思源黑体 Normal 和 Fira Math。字体来源、版本、许可证见 `fonts/README.md`，逐文件校验值保存在本组 `typography.json` 及图像元数据中。Matplotlib的PDF采用真实CFF字形生成的矢量Type 3字形程序，避免TrueType强制嵌入在XeLaTeX导入时出现中文文字层存在而字形不可见的问题；仍为可缩放的矢量内容。正文数学字体不变。

正文主要按112 mm宽引用；需要并列对照的宽图按169 mm引用。制作时先定物理尺寸，主标签约8 pt、辅助标注约7.5 pt，再核查实际输出及正文缩放。每图在正文有语义化标签和阅读引导，相应部分大纲说明新增图解所支持的推理。

## 复现

从项目根目录运行各部分 `matplotlib/comprehension-additions/` 下的生成脚本。需要 Python、NumPy、Matplotlib 和 Pillow；字体直接从仓库加载。三个生成器可以独立维护，不改变共享旧图样式。

TikZ 图由同一队列串行编译，需 XeLaTeX 与 Poppler：

```sh
python3 figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/render-tikz.py
```

也可以在命令后指定一个或多个项目相对图源路径。所有临时编译文件留在当前工作区的 `build/`，不使用其他工作区缓存。完成图源修改和导出后，在本工作区重建卷一并检查最终书页；图像集成清单登记实际导出哈希。

验收记录与页码以本次实际构建为准，历史预览不替代最终PDF检查。
