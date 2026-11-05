"""Check the figure data and the chapter's finite numerical examples."""

from cmath import exp
from fractions import Fraction as Q
from math import cos, pi, sin
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent


def close(actual, expected, tolerance=1e-11):
    assert abs(actual - expected) < tolerance, (actual, expected)


def linear(x, h):
    result = [0] * (len(x) + len(h) - 1)
    for i, left in enumerate(x):
        for j, right in enumerate(h):
            result[i + j] += left * right
    return result


def circular(x, h):
    return [
        sum(x[r] * h[(n - r) % len(x)] for r in range(len(x)))
        for n in range(len(x))
    ]


def dft(x, inverse=False):
    sign = 1 if inverse else -1
    scale = len(x) if inverse else 1
    return [
        sum(value * exp(sign * 2j * pi * k * n / len(x))
            for n, value in enumerate(x)) / scale
        for k in range(len(x))
    ]


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def remainder(values, modulus):
    result = list(map(Q, values))
    while len(result) >= len(modulus):
        factor = result[-1] / modulus[-1]
        shift = len(result) - len(modulus)
        for j, value in enumerate(modulus):
            result[shift + j] -= factor * value
        result.pop()
    return result


def figure_data():
    text = (HERE / "basic-operations.tex").read_text()
    series = re.findall(r"coordinates\s*\{([^}]+)\}", text)
    energies = []
    for coordinates in series:
        points = [
            (Q(x), Q(y))
            for x, y in re.findall(r"\(([-.\d]+),([-.\d]+)\)", coordinates)
        ]
        energies.append(sum(
            (b - a) * (u * u + u * v + v * v) / 3
            for (a, u), (b, v) in zip(points, points[1:])
        ))
    assert energies == [4, 4, 4, 4, 4, 16, 4, 2], energies
    text = (HERE / "channel-mixing.tex").read_text()
    rows = re.findall(r"(\d)/(\d+)/(-?\d+)/(-?\d+)/(-?\d+)/(-?\d+)", text)
    x = [[int(a), int(b)] for _, _, a, b, _, _ in rows]
    y = [[int(c), int(d)] for _, _, _, _, c, d in rows]
    assert x == [[1, 0], [2, 1], [1, 2]]
    assert [matvec([[1, 1], [1, -1]], row) for row in x] == y
    assert sum(v * v for row in x for v in row) == 11
    assert sum(v * v for row in y for v in row) == 22
    print("Figures: all eight waveforms and all channel table entries verified.")


def finite_transforms():
    x, h = [1, 2, 1], [1, -1]
    assert linear(x, h) == [1, 1, -1, -1]
    assert circular(x, h + [0]) == [0, 1, -1]
    zero = lambda n: x[n] if 0 <= n < len(x) else 0
    assert [sum(zero(n + r) * h[r] for r in range(2))
            for n in range(-1, 3)] == [-1, -1, 1, 1]
    xf, hf = dft(x + [0]), dft(h + [0, 0])
    for a, b in zip(xf, [4, -2j, 0, 2j]):
        close(a, b)
    for a, b in zip(hf, [0, 1 + 1j, 2, 1 - 1j]):
        close(a, b)
    for a, b in zip(dft([a * b for a, b in zip(xf, hf)], inverse=True),
                    [1, 1, -1, -1]):
        close(a, b)
    close(sum(abs(v) ** 2 for v in xf) / 4, 6)
    wave = [cos(2 * pi * n / 8) for n in range(8)]
    shifted = [wave[(n - 2) % 8] for n in range(8)]
    wf, sf = dft(wave), dft(shifted)
    close(wf[1], 4)
    close(wf[7], 4)
    close(sf[1], -4j)
    close(sf[7], 4j)
    print("Convolution, correlation, DFT/IDFT, phase shift and Parseval verified.")


def polynomial_algorithms():
    x, h = [1, 2, 1], [1, -1]
    evaluate = lambda p, z: sum(v * z ** n for n, v in enumerate(p))
    r0 = evaluate(x, 0) * evaluate(h, 0)
    rp = evaluate(x, 1) * evaluate(h, 1)
    rm = evaluate(x, -1) * evaluate(h, -1)
    top = x[-1] * h[-1]
    assert [r0, Q(rp - rm, 2) - top, Q(rp + rm, 2) - r0, top] == linear(x, h)
    product = linear(x, h)
    assert remainder(product, [-1, 1]) == [0]
    assert remainder(product, [1, 1]) == [0]
    assert remainder(product, [1, 0, 1]) == [2, 2]
    bt = [[1, 0, -1, 0], [0, 1, 1, 0], [0, -1, 1, 0], [0, 1, 0, -1]]
    g = [[1, 0, 0], [Q(1, 2)] * 3, [Q(1, 2), Q(-1, 2), Q(1, 2)], [0, 0, 1]]
    at = [[1, 1, 1, 0], [0, 1, -1, -1]]
    winograd = lambda d, kernel: matvec(
        at, [a * b for a, b in zip(matvec(bt, d), matvec(g, kernel))]
    )
    assert winograd([1, 2, 3, 4], [2, -1, 1]) == [3, 5]
    # Testing all basis pairs verifies the entire bilinear identity exactly.
    for i in range(4):
        for j in range(3):
            d = [int(k == i) for k in range(4)]
            kernel = [int(k == j) for k in range(3)]
            expected = [sum(d[n + r] * kernel[r] for r in range(3)) for n in range(2)]
            assert winograd(d, kernel) == expected
    print("Toom recovery, CRT remainders and all 12 Winograd basis pairs verified.")


def sampling_and_history():
    for n in range(-20, 21):
        close(cos(.8 * pi * n), cos(1.2 * pi * n))
    for m in range(1, 8):
        for w in (0, .2 * pi, .7 * pi, pi):
            direct = sum(exp(-1j * w * n) for n in range(m)) / m
            formula = (exp(-1j * w * (m - 1) / 2) * sin(m * w / 2)
                       / (m * sin(w / 2))) if w else 1
            close(direct, formula)
    x = lambda n: cos(.2 * pi * n) + cos(.8 * pi * n)
    for k in range(-10, 11):
        close(x(2 * k), 2 * cos(.4 * pi * k))
        expected = (cos(.1 * pi) * cos(.4 * pi * k - .1 * pi)
                    + cos(.4 * pi) * cos(1.6 * pi * k - .4 * pi))
        close((x(2 * k) + x(2 * k - 1)) / 2, expected)
    u = [1, 2, 1]
    kernel = lambda r: Q(1, 2 ** (r - 1)) if r >= 1 else 0
    response = [sum(u[r] * kernel(n - r) for r in range(3)) for n in range(4)]
    assert response == [0, 1, Q(5, 2), Q(9, 4)]
    print("Aliasing, moving-average response, two-frequency example and given history kernel verified.")


if __name__ == "__main__":
    figure_data()
    finite_transforms()
    polynomial_algorithms()
    sampling_and_history()
