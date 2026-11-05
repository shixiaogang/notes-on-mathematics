# 卷二第3部分“函数空间”图像

本目录保存第3—8章（函数空间、线性泛函与线性算子、算子谱与算子方程、弱导数与Sobolev空间、再生核Hilbert空间、函数与函数类的逼近）独用的图像。全部为 TikZ 图源（含 pgfplots 曲线），图中数值来自正文算例或解析式；图名前缀 `c1`—`c6` 对应本部分第1—6章。

每幅图一个目录，`figure.tex` 为可编辑图源，`figure.pdf/png/svg` 与 `figure.render.json` 由下列命令导出（从项目根目录运行）：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/02-abstract-mathematics/03-function-spaces/tikz/<图名>/figure.tex
```

以下目录附有计算数据的脚本（纯 Python 标准库，从项目根目录运行），输出的数据文件与图源放在同一目录：`c1-legendre-truncation/generate.py`、`c1-step-density/generate.py`、`c3-spectrum-resolvent/generate.py`、`c4-bump-cutoff/generate.py`、`c4-cantor/generate.py`、`c4-compactness-loss/generate.py`、`c4-ddelta-test/generate.py`、`c4-holder-1d/generate.py`、`c4-mollifier/generate.py`、`c4-partition-unity/generate.py`、`c4-step-delta/generate.py`、`c4-test-sequences/generate.py`、`c5-gram-matrices/generate.py`、`c5-mercer-spectrum/generate.py`、`c5-observation-residual/generate.py`、`c5-truncation-comparison/generate.py`、`c6-bernstein-approx/generate.py`、`c6-bernstein-weights/generate.py`、`c6-gaussian-sections/generate.py`、`c6-lowrank-errors/generate.py`、`c6-spline-rates/generate.py`。

| 图名 | 引用位置（章目录/节文件） | 物理尺寸（mm） |
| --- | --- | --- |
| `c1-ae-representatives` | 01-function-spaces/01-elements.tex | 82.236×32.946 |
| `c1-change-of-measure` | 01-function-spaces/05-space-relations.tex | 58.053×37.172 |
| `c1-convergence-modes` | 01-function-spaces/05-space-relations.tex | 100.422×38.495 |
| `c1-essential-sup` | 01-function-spaces/04-integral-spaces.tex | 56.053×34.41 |
| `c1-even-odd-projection` | 01-function-spaces/06-orthogonal-structure.tex | 51.925×31.803 |
| `c1-inclusions` | 01-function-spaces/05-space-relations.tex | 105.671×38.477 |
| `c1-integral-orthogonality` | 01-function-spaces/02-norms-completeness.tex | 78.232×30.388 |
| `c1-legendre-gram-schmidt` | 01-function-spaces/06-orthogonal-structure.tex | 87.33×44.796 |
| `c1-legendre-truncation` | 01-function-spaces/06-orthogonal-structure.tex | 94.901×40.107 |
| `c1-projection-geometry` | 01-function-spaces/06-orthogonal-structure.tex | 71.67×42.711 |
| `c1-ramp-step` | 01-function-spaces/02-norms-completeness.tex | 71.565×31.799 |
| `c1-step-density` | 01-function-spaces/05-space-relations.tex | 88.685×37.229 |
| `c1-uniform-tube` | 01-function-spaces/03-continuous-functions.tex | 92.206×36.1 |
| `c1-unit-balls` | 01-function-spaces/04-integral-spaces.tex | 48.623×48.32 |
| `c1-xn-norms` | 01-function-spaces/04-integral-spaces.tex | 92.276×36.382 |
| `c1-young-area` | 01-function-spaces/04-integral-spaces.tex | 49.608×41.984 |
| `c2-baire-layers` | 02-linear-functionals-and-operators/04-weak-convergence.tex | 69.346×38.82 |
| `c2-conditional-expectation` | 02-linear-functionals-and-operators/05-adjoint.tex | 91.433×33.33 |
| `c2-dense-range` | 02-linear-functionals-and-operators/05-adjoint.tex | 102.514×43.921 |
| `c2-escaping-mass` | 02-linear-functionals-and-operators/04-weak-convergence.tex | 80.821×32.434 |
| `c2-four-subspaces` | 02-linear-functionals-and-operators/05-adjoint.tex | 97.688×37.073 |
| `c2-hahn-banach` | 02-linear-functionals-and-operators/03-dual-spaces.tex | 98.891×45.586 |
| `c2-observation-matrix` | 02-linear-functionals-and-operators/02-functional-representation.tex | 98.242×34.1 |
| `c2-open-mapping` | 02-linear-functionals-and-operators/06-inverse.tex | 107.442×51.47 |
| `c2-operator-norm-stretch` | 02-linear-functionals-and-operators/01-operators.tex | 95.088×54.455 |
| `c2-point-spike` | 02-linear-functionals-and-operators/02-functional-representation.tex | 101.653×32.431 |
| `c2-projection-strong-norm` | 02-linear-functionals-and-operators/01-operators.tex | 107.209×43.162 |
| `c2-projections` | 02-linear-functionals-and-operators/05-adjoint.tex | 107.029×47.516 |
| `c2-riesz-kernel` | 02-linear-functionals-and-operators/02-functional-representation.tex | 65.088×64.004 |
| `c2-sine-derivative` | 02-linear-functionals-and-operators/01-operators.tex | 101.459×40.555 |
| `c2-weak-norm-drop` | 02-linear-functionals-and-operators/04-weak-convergence.tex | 92.766×30.667 |
| `c2-weak-unit-vectors` | 02-linear-functionals-and-operators/04-weak-convergence.tex | 102.277×35.285 |
| `c3-compact-ellipse` | 03-operator-spectra-and-equations/01-compact-operators.tex | 91.916×47.279 |
| `c3-equation-types` | 03-operator-spectra-and-equations/04-integral-equations.tex | 75.494×47.145 |
| `c3-finite-rank-error` | 03-operator-spectra-and-equations/01-compact-operators.tex | 81.195×45.424 |
| `c3-fredholm-alternative` | 03-operator-spectra-and-equations/04-integral-equations.tex | 81.809×43.515 |
| `c3-identity-orthonormal` | 03-operator-spectra-and-equations/01-compact-operators.tex | 89.556×47.787 |
| `c3-kernel-action` | 03-operator-spectra-and-equations/03-integral-operators.tex | 110.878×44.87 |
| `c3-kernel-adjoint` | 03-operator-spectra-and-equations/03-integral-operators.tex | 75.233×40.852 |
| `c3-neumann-error` | 03-operator-spectra-and-equations/04-integral-equations.tex | 85.697×47.413 |
| `c3-noise-amplification` | 03-operator-spectra-and-equations/04-integral-equations.tex | 100.196×44.21 |
| `c3-picard-coefficients` | 03-operator-spectra-and-equations/04-integral-equations.tex | 99.61×44.27 |
| `c3-rectangle-kernel` | 03-operator-spectra-and-equations/03-integral-operators.tex | 97.437×46.221 |
| `c3-spectral-stretch` | 03-operator-spectra-and-equations/02-spectra-singular-values.tex | 94.583×48.757 |
| `c3-spectrum-resolvent` | 03-operator-spectra-and-equations/02-spectra-singular-values.tex | 97.751×64.449 |
| `c3-svd-decay` | 03-operator-spectra-and-equations/02-spectra-singular-values.tex | 110.349×44.789 |
| `c4-abs-sign` | 04-weak-derivatives-and-sobolev-spaces/02-weak-derivatives.tex | 85.746×30.614 |
| `c4-bump-cutoff` | 04-weak-derivatives-and-sobolev-spaces/01-distributions.tex | 102.168×40.898 |
| `c4-cantor` | 04-weak-derivatives-and-sobolev-spaces/02-weak-derivatives.tex | 94.686×44.711 |
| `c4-compactness-loss` | 04-weak-derivatives-and-sobolev-spaces/05-regularity.tex | 108.589×40.502 |
| `c4-ddelta-test` | 04-weak-derivatives-and-sobolev-spaces/01-distributions.tex | 84.402×30.688 |
| `c4-embedding-exponents` | 04-weak-derivatives-and-sobolev-spaces/05-regularity.tex | 96.255×42.097 |
| `c4-holder-1d` | 04-weak-derivatives-and-sobolev-spaces/02-weak-derivatives.tex | 96.203×41.18 |
| `c4-mollifier` | 04-weak-derivatives-and-sobolev-spaces/04-smoothing.tex | 124.421×41.123 |
| `c4-object-relations` | 04-weak-derivatives-and-sobolev-spaces/06-summary.tex | 140.649×46.778 |
| `c4-partition-unity` | 04-weak-derivatives-and-sobolev-spaces/04-smoothing.tex | 92.019×34.745 |
| `c4-poincare` | 04-weak-derivatives-and-sobolev-spaces/05-regularity.tex | 114.441×24.511 |
| `c4-reflection` | 04-weak-derivatives-and-sobolev-spaces/04-smoothing.tex | 90.237×31.443 |
| `c4-step-delta` | 04-weak-derivatives-and-sobolev-spaces/02-weak-derivatives.tex | 101.477×31.634 |
| `c4-test-sequences` | 04-weak-derivatives-and-sobolev-spaces/01-distributions.tex | 140.388×37.902 |
| `c4-trace` | 04-weak-derivatives-and-sobolev-spaces/05-regularity.tex | 90.293×46.013 |
| `c5-affine-norm-balls` | 05-reproducing-kernel-hilbert-spaces/04-spectral.tex | 82.377×74.101 |
| `c5-construction-steps` | 05-reproducing-kernel-hilbert-spaces/02-construction.tex | 106.391×23.707 |
| `c5-gram-matrices` | 05-reproducing-kernel-hilbert-spaces/01-point-evaluation.tex | 104.786×44.252 |
| `c5-kernel-operations` | 05-reproducing-kernel-hilbert-spaces/02-construction.tex | 90.745×36.107 |
| `c5-kernel-sections` | 05-reproducing-kernel-hilbert-spaces/01-point-evaluation.tex | 99.896×38.142 |
| `c5-mercer-spectrum` | 05-reproducing-kernel-hilbert-spaces/04-spectral.tex | 95.483×38.95 |
| `c5-norm-weights` | 05-reproducing-kernel-hilbert-spaces/04-spectral.tex | 94.622×38.139 |
| `c5-observation-residual` | 05-reproducing-kernel-hilbert-spaces/03-finite-observations.tex | 97.942×39.666 |
| `c5-pointwise-envelope` | 05-reproducing-kernel-hilbert-spaces/01-point-evaluation.tex | 79.558×35.8 |
| `c5-power-function` | 05-reproducing-kernel-hilbert-spaces/03-finite-observations.tex | 77.526×42.958 |
| `c5-reproducing-geometry` | 05-reproducing-kernel-hilbert-spaces/01-point-evaluation.tex | 92.654×59.972 |
| `c5-section-distance` | 05-reproducing-kernel-hilbert-spaces/01-point-evaluation.tex | 94.721×43.43 |
| `c5-truncation-comparison` | 05-reproducing-kernel-hilbert-spaces/04-spectral.tex | 98.203×39.91 |
| `c5-visible-parameters` | 05-reproducing-kernel-hilbert-spaces/02-construction.tex | 68.114×67.811 |
| `c6-bernstein-approx` | 06-function-approximation/01-single-function.tex | 66.657×30.663 |
| `c6-bernstein-weights` | 06-function-approximation/01-single-function.tex | 92.999×35.719 |
| `c6-constant-cover` | 06-function-approximation/03-function-classes.tex | 102.168×23.266 |
| `c6-covering-centers` | 06-function-approximation/03-function-classes.tex | 103.205×59.729 |
| `c6-empirical-distance` | 06-function-approximation/03-function-classes.tex | 81.181×30.667 |
| `c6-equicontinuity` | 06-function-approximation/03-function-classes.tex | 94.195×34.11 |
| `c6-gaussian-sections` | 06-function-approximation/01-single-function.tex | 98.937×41.924 |
| `c6-lipschitz-quantization` | 06-function-approximation/03-function-classes.tex | 79.396×37.031 |
| `c6-lowrank-errors` | 06-function-approximation/02-multivariate.tex | 95.889×43.071 |
| `c6-relu-units` | 06-function-approximation/01-single-function.tex | 96.576×41.723 |
| `c6-spline-hat` | 06-function-approximation/01-single-function.tex | 96.203×34.593 |
| `c6-spline-rates` | 06-function-approximation/01-single-function.tex | 93.377×41.448 |
| `c6-tensor-grid` | 06-function-approximation/02-multivariate.tex | 94.968×53.361 |
| `c6-xn-powers` | 06-function-approximation/03-function-classes.tex | 60.018×32.667 |
