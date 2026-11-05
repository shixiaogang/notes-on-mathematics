"""Reproduce chapter 13 data and render only its three PGFPlots figures."""

from pathlib import Path
import csv
import math
import os
import random
import subprocess

import fitz


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
FIGURES = {
    "temperature-state-observation": (169, 78),
    "temperature-inference": (169, 97),
    "ou-paths-sections": (169, 77),
}


def save_table(name, columns, rows):
    with (HERE / name).open("w", newline="") as output:
        writer = csv.writer(output, delimiter="\t", lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def solve_spd(matrix, rhs):
    """Small Cholesky solve for the independent batch-conditioning check."""
    n = len(rhs)
    lower = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            residual = matrix[i][j] - dot(lower[i][:j], lower[j][:j])
            lower[i][j] = math.sqrt(residual) if i == j else residual / lower[j][j]
    forward = []
    for i in range(n):
        forward.append((rhs[i] - dot(lower[i][:i], forward)) / lower[i][i])
    solution = [0.0] * n
    for i in range(n - 1, -1, -1):
        residual = forward[i] - sum(lower[j][i] * solution[j] for j in range(i + 1, n))
        solution[i] = residual / lower[i][i]
    return solution


def temperature_data():
    rng = random.Random(20261013)
    n, a, u, q, r = 24, 0.8, 0.4, 0.04, 0.09
    x, deterministic, y = [0.0], [0.0], [math.nan]
    prediction, filtered = [math.nan], [0.0]
    pp, pf = [math.nan], [0.0]
    for t in range(1, n + 1):
        deterministic.append(a * deterministic[-1] + u)
        x.append(a * x[-1] + u + math.sqrt(q) * rng.gauss(0, 1))
        y.append(x[-1] + math.sqrt(r) * rng.gauss(0, 1))
        prediction.append(a * filtered[-1] + u)
        pp.append(a * a * pf[-1] + q)
        gain = pp[-1] / (pp[-1] + r)
        filtered.append(prediction[-1] + gain * (y[-1] - prediction[-1]))
        pf.append((1 - gain) * pp[-1])

    smoothed, ps = filtered.copy(), pf.copy()
    for t in range(n - 1, -1, -1):
        gain = pf[t] * a / pp[t + 1]
        smoothed[t] += gain * (smoothed[t + 1] - prediction[t + 1])
        ps[t] += gain * gain * (ps[t + 1] - pp[t + 1])

    # Verify recursions against conditioning the complete joint Gaussian.
    times = range(1, n + 1)
    covariance = [
        [q * a ** abs(i - j) * (1 - a ** (2 * min(i, j))) / (1 - a * a)
         for j in times]
        for i in times
    ]
    for target in range(1, n + 1):
        for end, expected_mean, expected_variance in (
            (target, filtered[target], pf[target]),
            (n, smoothed[target], ps[target]),
        ):
            obs_cov = [
                [covariance[i][j] + (r if i == j else 0) for j in range(end)]
                for i in range(end)
            ]
            cross = covariance[target - 1][:end]
            residual = [y[i + 1] - deterministic[i + 1] for i in range(end)]
            mean = deterministic[target] + dot(cross, solve_spd(obs_cov, residual))
            variance = covariance[target - 1][target - 1] - dot(
                cross, solve_spd(obs_cov, cross)
            )
            assert abs(mean - expected_mean) < 1e-12
            assert abs(variance - expected_variance) < 1e-12
    for t in range(1, n + 1):
        assert -1e-12 <= ps[t] <= pf[t] + 1e-12 <= pp[t] + 1e-12
    assert smoothed[0] == ps[0] == 0

    columns = ["t", "deterministic", "state", "observation"]
    for key in ("pred", "filter", "smooth"):
        columns.extend([key, key + "_low", key + "_high"])
    rows = []
    for t in range(n + 1):
        row = [t, deterministic[t], x[t], y[t]]
        for values, variances in ((prediction, pp), (filtered, pf), (smoothed, ps)):
            radius = 1.95996398454 * math.sqrt(variances[t])
            row.extend([values[t], values[t] - radius, values[t] + radius])
        rows.append(row)
    save_table("temperature.tsv", columns, rows)
    for key, values, variances, start in (
        ("pred", prediction, pp, 1),
        ("filter", filtered, pf, 0),
        ("smooth", smoothed, ps, 0),
    ):
        band = [
            [t, values[t] - 1.95996398454 * math.sqrt(variances[t])]
            for t in range(start, n + 1)
        ] + [
            [t, values[t] + 1.95996398454 * math.sqrt(variances[t])]
            for t in range(n, start - 1, -1)
        ]
        save_table(key + "-band.tsv", ["t", "bound"], band)
    print("Temperature: seed=20261013, T=24, x0=0, a=0.8, u=0.4, Q=0.04, R=0.09")
    print("Kalman and RTS agree with batch Gaussian conditioning to 1e-12.")
    finite = [v for row in rows for v in row[1:] if math.isfinite(v)]
    print(f"Temperature plotting range: {min(finite):.4f} to {max(finite):.4f}")


def ou_data():
    rng = random.Random(20261014)
    h, rate, sigma = 0.02, 1.0, 0.6
    decay = math.exp(-rate * h)
    sd = sigma * math.sqrt((1 - decay * decay) / (2 * rate))
    paths = [1.0] * 4
    rows = [[0, 1, *paths]]
    for k in range(1, 201):
        paths = [decay * value + sd * rng.gauss(0, 1) for value in paths]
        rows.append([k * h, math.exp(-rate * k * h), *paths])
    save_table("ou.tsv", ["t", "mean", "path1", "path2", "path3", "path4"], rows)
    print("OU: seed=20261014, exact grid transition, h=0.02, lambda=1, sigma=0.6, X0=1")


def render():
    temporary = ROOT / "build/math-restructure-figures/ch13"
    temporary.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    for key, directory in (
        ("TEXINPUTS", ROOT / "tex"),
        ("T1FONTS", ROOT / "fonts/stix2-type1/type1"),
        ("TFMFONTS", ROOT / "fonts/stix2-type1/tfm"),
        ("ENCFONTS", ROOT / "fonts/stix2-type1/enc"),
    ):
        env[key] = str(directory) + "//:" + env.get(key, "")
    driver = (HERE / "preview.tex").relative_to(ROOT).as_posix()
    for name, size in FIGURES.items():
        commands = [
            ["xelatex", "-no-pdf", "-no-shell-escape", "-interaction=nonstopmode",
             "-halt-on-error", "-output-directory=" + str(temporary),
             "-jobname=" + name,
             r"\def\ChThirteenFigure{" + name + r"}\input{" + driver + "}"],
            ["xdvipdfmx", "-f", str(ROOT / "fonts/stix2-type1/map/stix2.map"),
             "-E", "-o", str(HERE / (name + ".pdf")),
             str(temporary / (name + ".xdv"))],
        ]
        for command in commands:
            result = subprocess.run(
                command, cwd=ROOT, env=env, capture_output=True, text=True
            )
            if result.returncode:
                raise RuntimeError((result.stdout + result.stderr)[-7000:])
        with fitz.open(HERE / (name + ".pdf")) as document:
            assert len(document) == 1
            page = document[0]
            actual = (page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72)
            assert all(abs(a - b) < 0.1 for a, b in zip(actual, size)), actual
            page.get_pixmap(dpi=180, alpha=False).save(HERE / (name + ".png"))
        print(f"{name}: PDF and preview rendered at {size[0]} x {size[1]} mm")


if __name__ == "__main__":
    temperature_data()
    ou_data()
    render()
