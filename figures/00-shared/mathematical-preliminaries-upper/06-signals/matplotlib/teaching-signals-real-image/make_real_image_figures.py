#!/usr/bin/env python3
"""Real grayscale-image demonstrations for the signal chapter.

Loads the shared deterministic scene (scene.npy / scene.py) and renders six
figures that translate abstract signal concepts into a single picture:

* real-image-spectrum     二维 DFT：低频在中央、边缘对应外围高频；
* real-image-downsampling 直接隔点抽取与先平均再抽取（混叠/锯齿）；
* real-image-filter       均值平滑（低通）与 Sobel 边缘（高通）；
* real-image-dct          只保留中心一小片 DCT 系数的重建；
* real-image-quantize     把连续灰度归到少数几档（量化）；
* real-image-morphology   二值化后的膨胀与腐蚀。

All operations are written directly with NumPy (no scipy/skimage), so every
panel is fully reproducible from scene.npy. Outputs are PDF (a vector frame
holding the raster panel) plus PNG, like the book's other matplotlib figures.
"""
from pathlib import Path
import sys

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())
SHARED = ROOT / "figures" / "00-shared" / "mathematical-generators" / "matplotlib"
sys.path.insert(0, str(SHARED))
import plot_style  # noqa: E402

plot_style.configure()
INK = "#3B4252"
CN_FONT = font_manager.FontProperties(
    fname=str(ROOT / "fonts/LXGWWenKai-Regular.ttf"))
font_manager.fontManager.addfont(str(ROOT / "fonts/LXGWWenKai-Regular.ttf"))
mpl.rcParams["font.family"] = CN_FONT.get_name()


def load_scene() -> np.ndarray:
    if not (HERE / "scene.npy").exists():
        import runpy
        runpy.run_path(str(HERE / "scene.py"), run_name="__main__")
    return np.load(HERE / "scene.npy").astype(np.float64)


def reflect_pad(a: np.ndarray, p: int) -> np.ndarray:
    return np.pad(a, p, mode="reflect")


def box_blur(a: np.ndarray, k: int) -> np.ndarray:
    """Centered k*k moving mean with reflect padding, separable, same size."""
    p = k // 2
    b = a
    for axis in (0, 1):
        pad_width = [(0, 0), (0, 0)]
        pad_width[axis] = (p, p)
        bp = np.pad(b, tuple(pad_width), mode="reflect")
        zero_shape = list(bp.shape)
        zero_shape[axis] = 1
        cs = np.cumsum(bp, axis=axis)
        cs = np.concatenate([np.zeros(zero_shape), cs], axis=axis)
        size = bp.shape[axis]
        hi = np.take(cs, np.arange(k, size + 1), axis=axis)
        lo = np.take(cs, np.arange(0, size + 1 - k), axis=axis)
        b = (hi - lo) / k
    return b


def sobel_edges(a: np.ndarray) -> np.ndarray:
    sx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], dtype=np.float64)
    b = reflect_pad(a, 1)
    h, w = a.shape

    def conv(kernel):
        out = np.zeros_like(a)
        for i in range(3):
            for j in range(3):
                out += kernel[i, j] * b[i:i + h, j:j + w]
        return out

    return np.hypot(conv(sx), conv(sx.T))


def dilate(mask: np.ndarray) -> np.ndarray:
    b = np.pad(mask, 1, mode="constant", constant_values=False)
    out = np.zeros_like(mask)
    for i in range(3):
        for j in range(3):
            out |= b[i:i + mask.shape[0], j:j + mask.shape[1]]
    return out


def erode(mask: np.ndarray) -> np.ndarray:
    b = np.pad(mask, 1, mode="constant", constant_values=True)
    out = np.ones_like(mask)
    for i in range(3):
        for j in range(3):
            out &= b[i:i + mask.shape[0], j:j + mask.shape[1]]
    return out


def dct_matrix(n: int) -> np.ndarray:
    k = np.arange(n)
    c = np.cos(np.pi * (2 * k[None, :] + 1) * k[:, None] / (2 * n))
    c *= np.sqrt(2.0 / n)
    c[0, :] = 1.0 / np.sqrt(n)
    return c


def im(ax, a, title, cmap="gray"):
    ax.imshow(a, cmap=cmap, vmin=0, vmax=1, interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, color=INK, pad=4)


def save(fig, name):
    fig.savefig(HERE / f"{name}.pdf", bbox_inches="tight", pad_inches=0.04)
    fig.savefig(HERE / f"{name}.png", bbox_inches="tight", pad_inches=0.04, dpi=300)
    fig.savefig(HERE / f"{name}.svg", bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    print("wrote", name)


def figure_spectrum(x):
    X = np.fft.fftshift(np.fft.fft2(x))
    mag = np.log1p(np.abs(X))
    fig, ax = plt.subplots(1, 2, figsize=(4.6, 2.5))
    im(ax[0], x, "原始灰度图 $x[n_1,n_2]$")
    ax[1].imshow(mag, cmap="magma", interpolation="nearest")
    ax[1].set_xticks([]); ax[1].set_yticks([])
    ax[1].set_title("二维 DFT 幅度（对数，零频移到中央）", color=INK, pad=4)
    ax[1].annotate("低频：整体明暗、缓变", xy=(0.5, 0.5), xycoords="axes fraction",
                   xytext=(0.5, 0.9), textcoords="axes fraction", ha="center",
                   fontsize=6.5, color="white")
    ax[1].annotate("高频：边缘、细节", xy=(0.5, 0.5), xycoords="axes fraction",
                   xytext=(0.5, 0.08), textcoords="axes fraction", ha="center",
                   fontsize=6.5, color="white")
    save(fig, "real-image-spectrum")


def figure_downsampling(x):
    direct = x[::4, ::4]
    n = x.shape[0] // 4
    blur = x.reshape(n, 4, n, 4).mean(axis=(1, 3))
    r0, r1, c0, c1 = 110, 175, 95, 175
    fig, ax = plt.subplots(2, 3, figsize=(5.2, 3.8))
    im(ax[0, 0], x, "原图 256×256")
    im(ax[0, 1], direct, "直接每 4 格取 1 格")
    im(ax[0, 2], blur, "先做 4×4 平均再抽取")
    zc = (r0 // 4, r1 // 4, c0 // 4, c1 // 4)
    im(ax[1, 0], x[r0:r1, c0:c1], "局部放大：屋顶与窗")
    im(ax[1, 1], direct[zc[0]:zc[1], zc[2]:zc[3]], "直接抽取：斜线呈锯齿")
    im(ax[1, 2], blur[zc[0]:zc[1], zc[2]:zc[3]], "先平均：边缘更平滑")
    save(fig, "real-image-downsampling")


def figure_filter(x):
    blur = box_blur(x, 5)
    edges = sobel_edges(x)
    edges /= max(edges.max(), 1e-9)
    fig, ax = plt.subplots(1, 3, figsize=(6.6, 2.5))
    im(ax[0], x, "原图")
    im(ax[1], blur, "5×5 均值平滑（压制高频）")
    im(ax[2], edges, "Sobel 边缘（突出高频差异）")
    save(fig, "real-image-filter")


def figure_dct(x):
    n = x.shape[0]
    c = dct_matrix(n)
    Y = c @ x @ c.T
    keep = n // 4
    # DCT orders frequencies from the top-left corner outward (low -> high).
    mask = np.zeros_like(Y)
    mask[:keep, :keep] = 1.0
    recon = c.T @ (Y * mask) @ c
    frac = keep * keep / (n * n)
    fig, ax = plt.subplots(1, 3, figsize=(6.6, 2.5))
    im(ax[0], x, "原图")
    ax[1].imshow(mask, cmap="gray", vmin=0, vmax=1, interpolation="nearest",
                 aspect="auto")
    ax[1].set_xticks([]); ax[1].set_yticks([])
    ax[1].set_title(f"只留左上角 {keep}×{keep} 个低频 DCT 系数\n（约占全部 {frac*100:.1f}%）",
                    color=INK, pad=4)
    im(ax[2], np.clip(recon, 0, 1), "用这些系数重建：轮廓在、细节模糊")
    save(fig, "real-image-dct")


def figure_quantize(x):
    levels = 4
    q = np.round(x * (levels - 1)) / (levels - 1)
    fig, ax = plt.subplots(1, 2, figsize=(4.4, 2.4))
    im(ax[0], x, "原图：灰度可取连续值")
    im(ax[1], q, f"均匀量化到 {levels} 个灰阶")
    save(fig, "real-image-quantize")


def figure_morphology(x):
    # Crop tightly around the house and threshold its light wall; the dark
    # door and window then appear as holes in a single connected object,
    # which makes the "fill / remove" effect of dilation and erosion clear.
    crop = x[150:214, 110:180]
    mask = crop > 0.56
    fig, ax = plt.subplots(1, 3, figsize=(6.6, 2.7))
    im(ax[0], mask, "阈值二值化：浅色墙面=白，\n门、窗是其中的黑洞")
    im(ax[1], dilate(mask), "膨胀：把墙面涨大、\n把小洞填小")
    im(ax[2], erode(mask), "腐蚀：把墙面收窄、\n把小洞扩大")
    save(fig, "real-image-morphology")


def main():
    x = load_scene()
    figure_spectrum(x)
    figure_downsampling(x)
    figure_filter(x)
    figure_dct(x)
    figure_quantize(x)
    figure_morphology(x)


if __name__ == "__main__":
    main()
