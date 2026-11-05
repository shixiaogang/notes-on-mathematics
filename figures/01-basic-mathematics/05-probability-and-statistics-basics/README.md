# 卷一第5部分“概率与统计基础”图像

本目录保存第20—24章独用的图像。Matplotlib图由解析式、精确概率计算或固定种子的模拟生成；每幅图目录下的`figure.json`记录公式、参数、随机种子、样本量、尺寸与字体校验值。`matplotlib/pred-exponential-coverage/facts.json`只保存正文引用的覆盖率模拟结果，不出图。

## 重放

Matplotlib每章一个生成器，从项目根目录运行（依赖Matplotlib、NumPy；第4、5章另用SciPy）：

```sh
python3 figures/01-basic-mathematics/05-probability-and-statistics-basics/matplotlib/generate_ch1.py
```

字体、色板和导出方式来自`figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py`。Matplotlib字符串不混排中文与数学文本，以免数学字体缺少中文字形。

TikZ图以`tikz/<图名>/figure.tex`为图源，用共享工具导出PDF、SVG与PNG，`figure.render.json`记录源文件校验值与物理尺寸：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/01-basic-mathematics/05-probability-and-statistics-basics/tikz/<图名>/figure.tex
```

## 图目

| 章 | 生成器 | Matplotlib | TikZ |
| --- | --- | --- | --- |
| 第20章 随机变量与概率分布 | `generate_ch1.py` | `prob-binomial-poisson`、`prob-cdf-three-types`、`prob-continuous-densities`、`prob-density-above-one`、`prob-discrete-pmfs`、`prob-pmf-cdf`、`prob-quantile-inverse`、`prob-skewed-locations`、`prob-square-transform` | `prob-die-indicator-map`、`prob-event-operations` |
| 第21章 随机向量与联合分布 | `generate_ch2.py` | `rvec-convolution`、`rvec-correlation`、`rvec-gaussian-conditional`、`rvec-inverse-transform`、`rvec-mixture`、`rvec-same-marginals`、`rvec-total-variance`、`rvec-whitening` | `rvec-bayes-tree`、`rvec-joint-table` |
| 第22章 样本、统计量与参数估计 | `generate_ch3.py` | `est-bernoulli-loglik`、`est-beta-updating`、`est-empirical-cdf`、`est-gaussian-contours`、`est-gaussian-posterior`、`est-posterior-summaries`、`est-sample-quantiles`、`est-unbounded-likelihood` | `est-population-sample-estimate` |
| 第23章 抽样分布与估计误差 | `generate_ch4.py` | `samp-bernoulli-clt`、`samp-chebyshev-sample-size`、`samp-chi-square-densities`、`samp-f-densities`、`samp-markov-chebyshev`、`samp-normal-approximation-range`、`samp-running-means`、`samp-sample-proportion`、`samp-shrinkage-mse`、`samp-t-normal-tails`、`samp-three-distributions` | `samp-mean-residual-projection` |
| 第24章 区间估计、假设检验与预测 | `generate_ch5.py` | `pred-binomial-test`、`pred-coverage-simulation`、`pred-error-types`、`pred-exponential-coverage`、`pred-interval-widths`、`pred-p-value-tail`、`pred-posterior-predictive`、`pred-power-curves`、`pred-proportion-coverage`、`pred-regression-bands`、`pred-test-interval-duality` | `pred-regression-projection` |
