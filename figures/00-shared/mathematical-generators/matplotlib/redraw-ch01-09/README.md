# 卷一第1—9章确定性绘图

本入口重放正文实际引用的76张旧确定性图，并导出4张补充图。原标签`fig:cnn-fft-blocks`扩展为重叠相加/重叠保留并列图，不增加同义第三张图。表示定理与CNN总览由根任务制作，不在本白名单内。第7章8个`functionalinlinefigurecaption`是有效编号图，不按标准浮动环境遗漏。

图中的数值来自既有解析式或准确有限构造；N1/N2/N3/N5均在图旁保存`scientific-input.json`，N4保存完整两路输入/输出数组。曲线不平滑重拟合、不重采样实验数据、不为补图虚设因子值。跨章共享的科学脚本维持单一canonical路径。

`scope-baseline.json`记录引用、原始f70基线、当前源哈希与原生宽度；`registry-fragment.json`供根任务合并路由。`review-observations.tsv`是作者逐图实际读源和看输出后的语义观察，`review-bindings.json`只绑定这些人工记录的版本、数据和物理尺寸。计数、文本外框与数值相等不替代科学审查。`caption-self-review.md`记录本轮新图注与局部回指的三遍自查；这些记录不是独立复核。

在项目根目录运行：

```sh
PYTHONPATH=/path/to/read-only-drawing-deps MPLCONFIGDIR=/path/to/private-cache python3 figures/00-shared/mathematical-generators/matplotlib/redraw-ch01-09/replay.py
```

可追加一个或多个key只重放相应canonical组。输出先落在本worktree的`build/figure-proofs/redraw-ch01-09/`。共享源的其他图落在`_unselected/`，本入口不安装它们；经复核后仅按本白名单复制当前导出物。临时数值回放使用`git show`读取基线源，保存在`build/`，不建立第二套活跃科学源。

图源按物理字号8pt（说明7.5pt）制作；正文引用记录中的实际PDF宽度，缩放比例约1。两张混合图以82mm面板、5mm间隔组合为169mm，避免把完整页面压缩后改变字号。原生TikZ框图保持各自画布，无需放大填满版心。统一五主色、固定浅底、数学上需要的格表/圆/因子形状均保留；模块局部圆角1.8pt。字体实际文件、版本与许可证在`review-bindings.json`和`fonts/README.md`可追溯。

本轮作者自查关闭了：N1点标签与等值线/图例挤压、N2底部导数说明出界、N3错误使用TeX保留命令作循环变量、基函数图右刻度裁切、割线穿过容量标签、低秩图与连续性图配色未完整落地。Möbius柱添加斜纹、主化图采用三线型，避免只凭颜色区分。全书构建与最终整合书页仍由当前构建/PDF检查记录另行绑定；不沿用历史成品的接受结论。
