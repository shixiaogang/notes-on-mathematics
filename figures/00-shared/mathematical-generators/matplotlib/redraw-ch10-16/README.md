# 第一卷第10—16章确定性重绘资源

日期：2026-10-11。范围：45张既有确定性图（33张数据图、12张简单TikZ图），新增N15探索树与N16信息集树。N10查看时刻保证、N11候选支持对照为正文native LaTeX表。生成式资源由其他任务负责，不在本目录白名单。

`baseline-source-map.json`保存基线制作方式、原canonical源和摘要、原插入/导出尺寸；它是历史快照，不能作为当前尺寸通过证据。`additions-source-map.json`是新增两图的路由片段。`render.py`从唯一canonical生成器复现本组；共享脚本未选中的输出只写入当前工作树`build/redraw-ch10-16/unselected/`，不更新其他图。

在具有Matplotlib、Numpy、PyMuPDF、fontTools及项目TeX环境的Python中，从项目根目录运行：

```sh
python3 figures/00-shared/mathematical-generators/matplotlib/redraw-ch10-16/render.py
python3 figures/00-shared/mathematical-generators/matplotlib/redraw-ch10-16/validate_inputs.py
```

可在`render.py`后传完整资源键（`v1-...`）选择本组子集，未知键会报错。字体从项目`fonts/`实际加载；临时依赖/缓存目录不写入科学源。TikZ通过共享font preamble编译，当前runner用0pt预览边框，按native112或169mm插入，不放大文字填版心。数学脚标保留必要的较小字形；8pt/7.5pt指主标签/辅助说明基准，TeX pt到PDF bp的差异在契约注明。

`quantitative-current-validation.json`绑定33张当前artist数据的96项解析关系和4份保留CSV/TSV摘要。布朗增量、温度状态、OU路径与控制输入不重新采样。`tikz-mathematics-preflight.json`是26项教学格表/几何/新增树的数值预核查，不能代替拓扑、条件或真实图片审查。

当前作者验收入口为`review-20261011/`：

- `contracts.json`：47图源、导出、正文及字体版本的摘要，native尺寸、引用宽度、真实缩放和角色字号。
- `scientific-visual-review.json`：逐图实际数学对象/成立条件和真实PNG预览判断；作者自查不是独立复核。
- `caption-closure.json`：24图注完整前后版本、句级ID及颜色/语义接受依据。
- `text-self-review.md`与`text-snapshot.tex`：四项新增文字、图内标签、表格及7个证明框等价分行的三遍自查和恢复片段。
- `book-page-review.json`：本树7版构建后的PDF摘要、实际书页观察及已查看页；完整整合版须另复验，不由本树的局部通过代替。

各资源`redraw-20261011.json`保存本次尺寸契约和作者判断。旧`review.json`、`validation.json`等仍描述旧版本，只有其原日期范围有效。整合A/B共享脚本后，需按最终canonical源重绘、重新核对数值与书页，并由未参与制图的审查者独立复核。
