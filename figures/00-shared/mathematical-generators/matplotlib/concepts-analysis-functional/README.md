# 积分、最优化与函数空间的概念比较图

七张解析图与一张三节点查询树只解释正文中的具体难点，不展示实验数据。
曲线和几何对象的公式、定义域、采样、配色职责与精确尺寸见 `sources.json`。
运行 `plots.py` 重建 PDF、SVG、PNG；字体来自仓库，中文为霞鹜文楷 Regular，西文为
Source Sans 3 Regular，数学由 STIX mathtext 排版。第一卷与第二卷共用这些图内字族；样式入口为上级目录的 `plot_style.py`。
PDF 使用 Type3 矢量字形，SVG 将字形转曲，避免把 CFF 字体错误标成 TrueType；书籍编译无需这些字体的外部安装。

查询树源文件 `query-tree.tex` 由书籍的 TikZ 环境编译，保留已选分支与预先指定中心值的区别。
这是三节点简单分支，不含任何概率假设，文字用共享图形字体。

验收须核对最终书页中的字号、曲线、断点、球心和图注，原版记录见 `review.json`；本轮风格统一记录见 `style-review.json`，未重新编译整书。
