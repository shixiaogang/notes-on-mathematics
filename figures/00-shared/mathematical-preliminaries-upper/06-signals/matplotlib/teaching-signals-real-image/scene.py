#!/usr/bin/env python3
"""Deterministic grayscale "photograph-like" scene shared by the signal chapter's
real-image demonstrations.

The scene is rendered once from analytic shapes at high resolution with a fixed
random seed, then downsampled with a small Gaussian to produce a smooth, natural
looking 256x256 picture. It deliberately contains:

* smooth large regions (sky gradient, rolling hills) -> low-frequency energy;
* sharp edges (house, door/window, tree silhouette)   -> high-frequency energy;
* fine, slightly irregular texture                    -> energy spread outward.

All downstream figures (spectrum / DCT / downsampling / filtering / quantization)
load ``scene.npy`` instead of regenerating, so every panel uses the exact same
record and panels are directly comparable.
"""
from pathlib import Path

import numpy as np
from PIL import Image

SIZE = 256
SS = 4  # supersampling factor
SEED = 20261023
HERE = Path(__file__).resolve().parent


def _supersampled_scene(n: int) -> np.ndarray:
    """Render the scene at grid resolution n (already supersampled by caller)."""
    rng = np.random.default_rng(SEED)
    yy, xx = np.mgrid[0:n, 0:n].astype(np.float64)
    u, v = xx / n, yy / n
    img = np.zeros((n, n), dtype=np.float64)

    # Sky: smooth vertical gradient with a soft horizontal haze band.
    sky = 0.86 - 0.34 * v
    sky += 0.05 * np.exp(-((v - 0.18) ** 2) / (2 * 0.05**2)) * (0.6 + 0.4 * np.cos(2 * np.pi * u))
    img = sky

    # Two rolling hill silhouettes (smooth sinusoidal horizon lines).
    ridge1 = 0.52 + 0.10 * np.sin(2 * np.pi * u * 1.25 + 0.7)
    ridge2 = 0.66 + 0.07 * np.sin(2 * np.pi * u * 2.30 + 2.1)
    hill1 = np.clip((v - ridge1) / 0.18, 0, 1)
    hill2 = np.clip((v - ridge2) / 0.16, 0, 1)
    img = img * (1 - 0.55 * hill1) + (0.46 - 0.05 * v) * (0.55 * hill1)
    img = img * (1 - 0.45 * hill2) + (0.34 - 0.04 * v) * (0.45 * hill2)

    # Ground plane with gentle perspective shading.
    ground_t = np.clip((v - 0.74) / 0.26, 0, 1)
    img = img * (1 - ground_t) + (0.30 + 0.06 * ground_t) * ground_t

    def disk(cy, cx, r):
        return (yy - cy) ** 2 + (xx - cx) ** 2 <= r * r

    def rect(r0, r1, c0, c1):
        return (yy >= r0) & (yy < r1) & (xx >= c0) & (xx < c1)

    # Tree (behind the house): trunk plus layered round canopy.
    trunk = rect(int(0.62 * n), int(0.86 * n), int(0.245 * n), int(0.275 * n))
    img = np.where(trunk, 0.26, img)
    for (dr, dc, rr, shade) in ((0.47, 0.26, 0.075, 0.42), (0.52, 0.225, 0.055, 0.40),
                               (0.52, 0.295, 0.055, 0.40), (0.44, 0.30, 0.05, 0.44)):
        img = np.where(disk(int(dr * n), int(dc * n), int(rr * n)), shade, img)

    # House body with a subtle front-light gradient.
    body = rect(int(0.55 * n), int(0.83 * n), int(0.43 * n), int(0.70 * n))
    house_shade = 0.62 + 0.08 * (1 - v)
    img = np.where(body, house_shade, img)
    # Roof: a wedge (triangle) sitting on top of the body.
    roof_center_x, roof_y, roof_half_w, roof_h = 0.565, 0.55, 0.165, 0.13
    roof = (v > roof_y - roof_h) & (v < roof_y) & \
        (np.abs(u - roof_center_x) < roof_half_w * (1 - (roof_y - v) / roof_h + 0.06))
    img = np.where(roof, 0.40, img)
    # Door and window (dark shapes).
    img = np.where(rect(int(0.68 * n), int(0.83 * n), int(0.50 * n), int(0.56 * n)), 0.17, img)
    img = np.where(rect(int(0.60 * n), int(0.67 * n), int(0.61 * n), int(0.66 * n)), 0.24, img)
    # Window cross frame (slightly lighter lines).
    img = np.where(rect(int(0.632 * n), int(0.638 * n), int(0.61 * n), int(0.66 * n)), 0.55, img)
    img = np.where(rect(int(0.60 * n), int(0.67 * n), int(0.632 * n), int(0.638 * n)), 0.55, img)

    # Small distant bush in front on the right for an extra soft blob.
    yy_disk = ((yy / n - 0.80) / 0.05) ** 2 + ((xx / n - 0.86) / 0.09) ** 2
    img = np.where(yy_disk <= 1, 0.30 + 0.05 * (1 - yy_disk), img)

    # Fine, low-amplitude irregular texture (grain + faint blades/noise).
    img += 0.012 * rng.standard_normal((n, n))
    # Slightly stronger grain in the ground region only.
    img += ground_t * 0.010 * rng.standard_normal((n, n))

    return np.clip(img, 0.0, 1.0)


def build() -> np.ndarray:
    big = _supersampled_scene(SIZE * SS)
    im = Image.fromarray((big * 255.0).round().astype(np.uint8))
    # Separable box average over each SSxSS block acts as a mild anti-alias filter.
    im = im.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    x = np.asarray(im, dtype=np.float64) / 255.0
    return x


def main():
    x = build()
    np.save(HERE / "scene.npy", x.astype(np.float32))
    Image.fromarray((x * 255).round().astype(np.uint8)).save(HERE / "scene.png")
    print(f"saved scene {x.shape} range=({x.min():.3f},{x.max():.3f}) mean={x.mean():.3f}")


if __name__ == "__main__":
    main()
