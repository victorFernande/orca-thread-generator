"""Connected watertight radial meshes. Threads are surface coordinates, never added solids."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any

try:
    import numpy as np
except ModuleNotFoundError:
    import sys, os
    from pathlib import Path

    base = (
        Path(os.environ.get("APPDATA", "")) / "OrcaSlicer"
        if sys.platform == "win32"
        else Path.home()
        / (
            ".config/OrcaSlicer"
            if sys.platform != "darwin"
            else "Library/Application Support/OrcaSlicer"
        )
    )
    sys.path.insert(
        0,
        str(
            base
            / "python/packages"
            / f"cp{sys.version_info.major}{sys.version_info.minor}"
        ),
    )
    import numpy as np
from .schema import normalize_params
from .thread_math import thread_radius, thread_depth


@dataclass
class MeshData:
    vertices: np.ndarray
    triangles: np.ndarray
    face_normals: np.ndarray
    bounds_mm: dict
    volume_cm3: float


def _finish(vertices, triangles):
    v = np.asarray(vertices, dtype=np.float64)
    t = np.asarray(triangles, dtype=np.int32)
    cross = np.cross(v[t[:, 1]] - v[t[:, 0]], v[t[:, 2]] - v[t[:, 0]])
    lengths = np.linalg.norm(cross, axis=1)
    if np.any(lengths < 1e-10):
        raise ValueError("Degenerate generated surface")
    volume = float(
        np.sum(np.einsum("ij,ij->i", v[t[:, 0]], np.cross(v[t[:, 1]], v[t[:, 2]]))) / 6
    )
    if volume < 0:
        t = t[:, [0, 2, 1]]
        cross = -cross
        volume = -volume
    mn = v.min(axis=0)
    mx = v.max(axis=0)
    return MeshData(
        v.astype(np.float32),
        t,
        (cross / lengths[:, None]).astype(np.float32),
        {"min": mn.tolist(), "max": mx.tolist(), "size": (mx - mn).tolist()},
        volume / 1000,
    )


def _surface(path, n, flip_diagonal=False):
    # Ordered meridian rings/poles form a closed loop. Consecutive rings share exact indices.
    if len(path) * n > 350_000:
        raise ValueError(
            "Mesh exceeds the supported vertex budget; reduce length/resolution or increase pitch"
        )
    theta = np.arange(n) * 2 * np.pi / n
    vertices = []
    rings = []
    triangles = []
    for z, rad in path:
        rr = np.broadcast_to(np.asarray(rad, dtype=float), (n,))
        if not np.isfinite(rr).all() or np.any(rr < 0):
            raise ValueError("Surface contains an invalid radius")
        if np.max(np.abs(rr)) < 1e-9:
            rings.append([len(vertices)])
            vertices.append((0, 0, float(z)))
        else:
            ids = list(range(len(vertices), len(vertices) + n))
            rings.append(ids)
            vertices.extend(zip(rr * np.cos(theta), rr * np.sin(theta), np.full(n, z)))
    for a, b in zip(rings, rings[1:] + rings[:1]):
        if len(a) == len(b) == 1:
            continue
        for j in range(n):
            k = (j + 1) % n
            if len(a) == 1:
                triangles.append((a[0], b[j], b[k]))
            elif len(b) == 1:
                triangles.append((a[j], b[0], a[k]))
            elif flip_diagonal:
                triangles.extend(((a[j], b[j], a[k]), (a[k], b[j], b[k])))
            else:
                triangles.extend(((a[j], b[j], b[k]), (a[j], b[k], a[k])))
    return _finish(vertices, triangles)


def _levels(a, b, step):
    return np.linspace(a, b, max(2, int(np.ceil(abs(b - a) / step)) + 1))


def _texture(theta, z, r, p, kind=None):
    kind = kind or p["texture"]
    depth = min(p["knurl_depth"], p["wall_thickness"] * 0.3)
    if kind == "knurled":
        return r + depth * (
            0.5 + 0.5 * np.cos(p["knurl_count"] * theta) * np.cos(z * 2 * np.pi / 3)
        )
    if kind == "fluted":
        return r + depth * (0.5 + 0.5 * np.cos(p["knurl_count"] * theta))
    if kind == "faceted":
        return (
            r
            * np.cos(np.pi / 8)
            / np.cos((theta + np.pi / 8) % (np.pi / 4) - np.pi / 8)
        )
    return np.full(theta.shape, r)


def _head_radius(theta, r, p):
    if p["head"] == "hex":
        return (
            r
            * np.cos(np.pi / 6)
            / np.cos((theta + np.pi / 6) % (np.pi / 3) - np.pi / 6)
        )
    if p["head"] == "wing":
        return r * (1 + 0.65 * np.abs(np.cos(theta)) ** 6)
    return _texture(theta, 0, r, p, "fluted")


def _validate_standard(p):
    if (
        p["module"] == "standard_bottle_cap"
        and p["standard"] == "mason_86"
        and not p["measurements_confirmed"]
    ):
        raise ValueError(
            "Mason 86 experimental: confirme medidas reais antes de gerar / confirm measured dimensions before generation"
        )


def _jar(p, neck=False):
    n = p["resolution"]
    theta = np.arange(n) * 2 * np.pi / n
    h = p["thread_length"] + p["floor_thickness"] + 3 if neck else p["height"]
    floor = p["floor_thickness"]
    length = p["thread_length"]
    wall = p["wall_thickness"]
    root = p["nominal_dia"] / 2 - thread_depth(p)
    inner = root - wall
    if inner <= 0.5:
        raise ValueError(
            "Container wall leaves no usable bore at thread root; increase nominal diameter or reduce wall"
        )
    outer = max(p["diameter"] / 2, p["nominal_dia"] / 2 + 1) if not neck else root
    if p["texture"] == "faceted" and not neck:
        outer = max(outer, (inner + wall) / np.cos(np.pi / 8))
    path = []
    if not neck:
        path.append((0, 0.0))
    path.append((0, outer))
    shoulder = h - length - 1
    for z in _levels(0.2, shoulder, 0.8):
        path.append((z, _texture(theta, z, outer, p) if not neck else root))
    path.append((h - length, root))
    for q in _levels(0, length, p["pitch"] / 12)[1:]:
        path.append((h - length + q, thread_radius(theta, q, p)))
    path.append((h, inner))
    for z in _levels(h, floor if not neck else 0, 1)[1:]:
        path.append((z, inner))
    if not neck:
        path.append((floor, 0.0))
    return _surface(path, n)


def _female(p, ring=False, nut=False, mark=0):
    n = p["resolution"]
    theta = np.arange(n) * 2 * np.pi / n
    length = p["thread_length"]
    floor = 0 if ring or nut else p["floor_thickness"]
    h = length + floor
    wall = p["wall_thickness"]
    outer = p["nominal_dia"] / 2 + wall + p["diametral_clearance"] / 2
    if mark:
        outer += min(0.55, wall * 0.25)
    if not nut and p["texture"] == "faceted":
        outer /= np.cos(np.pi / 8)
    if nut and p["head"] == "hex":
        outer /= np.cos(np.pi / 6) * 1.12
    path = []
    if floor:
        path.extend([(0, 0.0), (0, _texture(theta, 0, outer, p))])
    else:
        path.append(
            (0, _head_radius(theta, outer * 1.12, p) if nut else np.full(n, outer))
        )
    for z in _levels(0.2, h, 0.8):
        rr = (
            _head_radius(theta, outer * 1.12, p)
            if nut
            else _texture(theta, z, outer, p)
        )
        if mark:
            # One, two or three tangible notches in the outer rim, outside the thread bore.
            notch = np.zeros(n)
            for k in range(mark):
                notch = np.maximum(
                    notch,
                    np.clip(
                        1
                        - np.abs(
                            np.angle(
                                np.exp(1j * (theta - (k - 0.5 * (mark - 1)) * 0.23))
                            )
                        )
                        / 0.065,
                        0,
                        1,
                    ),
                )
            rr = rr - min(0.55, wall * 0.25) * notch * (z > h - 1.1)
        path.append((z, rr))
    # Inner female mirrored for printing open side up. On assembly rotate 180deg about X.
    for q in _levels(length, 0, p["pitch"] / 12):
        z = floor + q
        rr = thread_radius(-theta, length - q, p, True)
        path.append((z, rr))
    if floor:
        bore = float(np.min(thread_radius(theta, length, p, True)))
        if p["gasket"]:
            go = min(p["gasket_offset"], max(0.6, bore * 0.2))
            gw = min(p["gasket_width"], bore * 0.15)
            path.extend(
                [
                    (floor, bore - go),
                    (floor - p["gasket_depth"], bore - go),
                    (floor - p["gasket_depth"], bore - go - gw),
                    (floor, bore - go - gw),
                ]
            )
        path.append((floor, 0.0))
    return _surface(path, n, flip_diagonal=True)


def _bolt(p):
    n = p["resolution"]
    th = np.arange(n) * 2 * np.pi / n
    root = p["nominal_dia"] / 2 - thread_depth(p)
    hh = p["head_height"]
    path = []
    bore = p["bore_diameter"] / 2
    if not bore:
        path.append((0, 0.0))
    else:
        path.append((0, bore))
    head = _head_radius(th, p["nominal_dia"] * 0.85, p)
    path.extend([(0, head), (hh, head), (hh, root)])
    for q in _levels(0.001, p["thread_length"], p["pitch"] / 12):
        path.append((hh + q, thread_radius(th, q, p)))
    if bore:
        path.extend([(hh + p["thread_length"], bore), (0.001, bore)])
    else:
        path.append((hh + p["thread_length"], 0.0))
    return _surface(path, n)


def _adapter(p):
    n = p["resolution"]
    th = np.arange(n) * 2 * np.pi / n
    h = p["adapter_length"]
    el = p["end_length"]
    wall = p["wall_thickness"]
    step = min(0.6, p["pitch"] / 12)
    start_step = step if p["end_a"] in ("male", "female") else 0.5
    end_step = step if p["end_b"] in ("male", "female") else 0.5
    zs = np.unique(
        np.r_[
            _levels(0, el, start_step),
            _levels(el, h - el, 0.8),
            _levels(h - el, h, end_step),
        ]
    )
    path = []

    # Smooth/barb end diameters describe clear bore; male/female describe thread nominal.
    def radii(z):
        u = np.clip((z - el) / (h - 2 * el), 0, 1)
        diam = (1 - u) * p["inlet_diameter"] + u * p["outlet_diameter"]
        inner = np.full(n, diam / 2)
        outer = inner + wall
        which = 0 if z <= el else 1 if z >= h - el else -1
        if which >= 0:
            kind = p["end_a"] if which == 0 else p["end_b"]
            q = z if which == 0 else h - z
            local = dict(p, nominal_dia=diam, thread_length=el)
            if kind == "barb":
                outer = outer + wall * 0.42 * np.maximum(
                    0, 1 - ((q - 1) % 4) / 3
                ) * np.clip(q / 1.5, 0, 1) * np.clip((el - q) / 1.5, 0, 1)
            elif kind == "smooth":
                outer = outer + 0.35 * (1 - q / el)
            elif kind == "male":
                outer = thread_radius(th if which == 0 else -th, q, local)
                inner = np.full(n, diam / 2 - thread_depth(local) - wall)
                if np.min(inner) <= 0.5:
                    raise ValueError(
                        "Adapter wall leaves no usable bore at threaded end; reduce wall or increase end diameter"
                    )
            elif kind == "female":
                inner = thread_radius(th if which == 0 else -th, q, local, True)
                outer = np.full(n, diam / 2 + wall + p["diametral_clearance"] / 2)
        return inner, outer

    for z in zs:
        path.append((z, radii(z)[1]))
    for z in zs[::-1]:
        path.append((z, radii(z)[0]))
    return _surface(path, n)


def generate_thread_calibration_kit(params=None):
    p = normalize_params(params)
    p.update(
        thread_length=max(3, min(p["pitch"] * 1.8, 6)), gasket=False, texture="smooth"
    )
    return [
        (
            f"Ring_{i}_{gap:.2f}mm",
            _female(dict(p, diametral_clearance=gap), ring=True, mark=i),
        )
        for i, gap in enumerate((0.10, 0.18, 0.26), 1)
    ]


def generate_parts(params=None):
    p = normalize_params(params)
    _validate_standard(p)
    if p["module"] == "container_and_lid":
        return [("Container", _jar(p)), ("Lid", _female(p))]
    if p["module"] == "standard_bottle_cap":
        return (
            [("Cap", _female(p))] if p["part"] == "cap" else [("Neck", _jar(p, True))]
        )
    if p["module"] == "hose_vacuum_adapter":
        return [("Adapter", _adapter(p))]
    return [("Bolt", _bolt(p)), ("Nut", _female(p, ring=True, nut=True))]


def collect_target_meshes(params=None, target=None, lang="pt"):
    p = normalize_params(params)
    target = target or p["export_target"]
    if target == "calibration":
        return generate_thread_calibration_kit(p)
    parts = generate_parts(p)
    if target == "primary":
        return parts[:1]
    if target == "secondary":
        return parts[1:] or parts[:1]
    return parts
