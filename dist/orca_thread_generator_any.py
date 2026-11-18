# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=1.26"]
#
# [tool.orcaslicer.plugin]
# id = "orca-thread-studio"
# name = "Orca Thread Studio"
# description = "Offline threaded containers, caps, adapters and mechanical fasteners"
# author = "Orca Thread Studio"
# version = "1.0.0"
# ///

from __future__ import annotations

import sys as _orca_init_sys
import types as _orca_init_types
if __name__ not in _orca_init_sys.modules:
    _orca_init_sys.modules[__name__] = _orca_init_types.ModuleType(__name__)

# ===========================================================================
# MODULE: thread_studio.schema
# ===========================================================================

"""Validated offline Thread Studio parameters. Dimensions are millimetres."""

pass  # [bundled] hoisted __future__ import
import math
from dataclasses import dataclass, asdict
from typing import Any

SCHEMA_VERSION = 1


@dataclass
class ThreadSpec:
    nominal_dia: float = 40.0
    pitch: float = 3.0
    thread_length: float = 12.0
    starts: int = 1
    hand: str = "right"


DEFAULT_PARAMS = dict(
    asdict(ThreadSpec()),
    module="container_and_lid",
    standard="fdm_trapezoid_45",
    part="cap",
    name="Orca Thread",
    diameter=44.0,
    height=55.0,
    wall_thickness=2.4,
    floor_thickness=2.4,
    diametral_clearance=0.26,
    axial_clearance=0.15,
    higbee_turns=0.65,
    knurl_depth=0.5,
    knurl_count=40,
    texture="knurled",
    head="hex",
    head_height=5.0,
    bore_diameter=0.0,
    inlet_diameter=35.0,
    outlet_diameter=58.0,
    adapter_length=65.0,
    end_length=15.0,
    end_a="smooth",
    end_b="barb",
    gasket=True,
    gasket_depth=0.6,
    gasket_width=1.1,
    gasket_offset=1.1,
    auto_configure_slicer=True,
    export_target="all",
    measurements_confirmed=False,
    measured_major_dia=0.0,
    measured_root_dia=0.0,
    measured_pitch=0.0,
    measured_length=0.0,
    lang="pt",
    theme="dark",
    resolution=96,
)
ISO_COARSE = {
    6: 1.0,
    8: 1.25,
    10: 1.5,
    12: 1.75,
    16: 2.0,
    20: 2.5,
    24: 3.0,
    30: 3.5,
    36: 4.0,
    42: 4.5,
    48: 5.0,
    64: 6.0,
    80: 6.0,
    100: 6.0,
}


def _number(value, default, low, high):
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError):
        value = default
    return min(high, max(low, value)) if math.isfinite(value) else default


def normalize_params(raw: dict[str, Any] | None = None) -> dict[str, Any]:
    p = dict(DEFAULT_PARAMS)
    if isinstance(raw, dict):
        p.update({k: v for k, v in raw.items() if k in p})
    choices = {
        "module": [
            "container_and_lid",
            "standard_bottle_cap",
            "hose_vacuum_adapter",
            "bolt_nut_knob",
        ],
        "standard": [
            "iso_metric",
            "fdm_trapezozoid_45",
            "fdm_trapezoid_45",
            "pco1881",
            "mason_70",
            "mason_86",
        ],
        "hand": ["right", "left"],
        "texture": ["smooth", "knurled", "fluted", "faceted"],
        "head": ["hex", "knurled", "wing"],
        "end_a": ["smooth", "barb", "male", "female"],
        "end_b": ["smooth", "barb", "male", "female"],
        "part": ["cap", "neck"],
        "export_target": ["all", "primary", "secondary", "calibration"],
        "lang": ["pt", "en"],
        "theme": ["dark", "light"],
    }
    for k, opts in choices.items():
        if p[k] not in opts:
            p[k] = DEFAULT_PARAMS[k]
    limits = {
        "nominal_dia": (6, 100),
        "pitch": (0.5, 10),
        "thread_length": (3, 100),
        "height": (12, 200),
        "diameter": (12, 150),
        "wall_thickness": (1.2, 8),
        "floor_thickness": (1.2, 8),
        "diametral_clearance": (0.05, 0.6),
        "axial_clearance": (0, 0.6),
        "higbee_turns": (0.1, 1),
        "knurl_depth": (0, 1.5),
        "knurl_count": (12, 100),
        "head_height": (3, 15),
        "bore_diameter": (0, 90),
        "inlet_diameter": (10, 100),
        "outlet_diameter": (10, 120),
        "adapter_length": (30, 180),
        "end_length": (7, 35),
        "gasket_depth": (0.2, 1.2),
        "gasket_width": (0.6, 2),
        "gasket_offset": (0.6, 3),
        "resolution": (48, 192),
        "measured_major_dia": (0, 120),
        "measured_root_dia": (0, 120),
        "measured_pitch": (0, 10),
        "measured_length": (0, 40),
    }
    for k, (lo, hi) in limits.items():
        p[k] = _number(p[k], DEFAULT_PARAMS[k], lo, hi)
    p["starts"] = int(_number(p["starts"], 1, 1, 3))
    p["resolution"] = int(p["resolution"])
    p["knurl_count"] = int(p["knurl_count"])
    for k in ["gasket", "auto_configure_slicer", "measurements_confirmed"]:
        p[k] = p[k] is True or p[k] == 1
    p["name"] = str(p["name"])[:80]
    p["standard"] = (
        "fdm_trapezoid_45" if p["standard"] == "fdm_trapezozoid_45" else p["standard"]
    )
    p["height"] = max(p["height"], p["floor_thickness"] + p["thread_length"] + 4)
    p["axial_clearance"] = min(p["axial_clearance"], p["pitch"] * 0.2)
    p["end_length"] = min(p["end_length"], p["adapter_length"] * 0.28)
    p["gasket_depth"] = min(p["gasket_depth"], p["floor_thickness"] * 0.45)
    if p["module"] == "standard_bottle_cap":
        if p["standard"] == "pco1881":
            p.update(nominal_dia=27.4, pitch=2.7, thread_length=7.0, starts=1)
        elif p["standard"] == "mason_70":
            p.update(nominal_dia=70.0, pitch=6.35, thread_length=7.9375, starts=1)
        elif p["standard"] == "mason_86" and p["measurements_confirmed"]:
            if not (
                p["measured_major_dia"] > p["measured_root_dia"] > 0
                and p["measured_pitch"] >= 0.5
                and p["measured_length"] >= 3
            ):
                raise ValueError(
                    "Mason 86: confirme diametro maior, raiz, passo e comprimento medidos / confirm measured major, root, pitch and length"
                )
            p.update(
                nominal_dia=p["measured_major_dia"],
                pitch=p["measured_pitch"],
                thread_length=p["measured_length"],
            )
    p["lead"] = p["pitch"] * p["starts"]
    p["bore_diameter"] = min(
        p["bore_diameter"],
        max(0, p["nominal_dia"] - 2 * p["wall_thickness"] - 1.3 * p["pitch"]),
    )
    return p

# ===========================================================================
# MODULE: thread_studio.thread_math
# ===========================================================================

"""Analytic radial helical envelopes, ISO-inspired/FDM profiles and Higbee starts."""

pass  # [bundled] hoisted __future__ import

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

pass  # [bundled] resolved intra-package import


def thread_depth(params):
    p = normalize_params(params)
    if p["standard"] == "pco1881":
        return (27.40 - 24.20) / 2
    if p["standard"] == "mason_86" and p["measurements_confirmed"]:
        return 0.5 * (p["measured_major_dia"] - p["measured_root_dia"])
    return min(
        p["nominal_dia"] * 0.12,
        p["pitch"] * (0.61343 if p["standard"] == "iso_metric" else 0.375),
    )


def higbee_envelope(z, length, ramp):
    u = np.clip(
        np.minimum(np.asarray(z), length - np.asarray(z)) / max(ramp, 1e-6), 0, 1
    )
    return u * u * (3 - 2 * u)


def thread_profile(phase, standard="iso_metric", axial_widening=0.0):
    # Symmetric truncated 60 degree / 45 degree radial tooth.
    signed = (np.asarray(phase) + 0.5) % 1.0 - 0.5
    if standard == "pco1881":
        # ISBT-derived asymmetric experimental envelope; rounded tooling details omitted.
        q = signed
        return np.where(
            q < -0.12,
            np.clip((q + 0.31) / 0.19, 0, 1),
            np.where(q > 0.10, np.clip((0.30 - q) / 0.20, 0, 1), 1.0),
        )
    q = np.abs(signed)
    crest = 0.0625 if standard == "iso_metric" else 0.125
    root = (0.0625 + 0.61343 / np.sqrt(3)) if standard == "iso_metric" else 0.5
    q = np.maximum(0, q - axial_widening)
    return np.clip((root - q) / (root - crest), 0, 1)


def thread_radius(theta, z, params, female=False):
    p = normalize_params(params)
    z = np.asarray(z)
    theta = np.asarray(theta)
    sign = 1 if p["hand"] == "right" else -1
    phase = z / p["pitch"] - sign * p["starts"] * theta / (2 * np.pi)
    depth = thread_depth(p)
    widen = p["axial_clearance"] / p["pitch"] / 2 if female else 0
    tooth = thread_profile(phase, p["standard"], widen)
    if female and p["standard"] == "pco1881":
        tooth = np.maximum.reduce(
            [
                thread_profile(phase + shift, p["standard"])
                for shift in np.linspace(-widen, widen, 9)
            ]
        )
    envelope = higbee_envelope(z, p["thread_length"], p["lead"] * p["higbee_turns"])
    # Female groove retains the full envelope, including a major-diameter lead-in.
    radius = p["nominal_dia"] / 2 - depth + depth * tooth * (1 if female else envelope)
    return radius + (p["diametral_clearance"] / 2 if female else 0)


def analyze_engagement(params):
    p = normalize_params(params)
    theta = np.linspace(0, 2 * np.pi, 97)[:, None]
    z = np.linspace(0, p["thread_length"], 257)[None, :]
    clearance = thread_radius(theta, z, p, True) - thread_radius(theta, z, p, False)
    return {
        "lead_mm": p["lead"],
        "radial_clearance_mm": p["diametral_clearance"] / 2,
        "axial_clearance_mm": p["axial_clearance"],
        "minimum_radial_gap_mm": float(np.min(clearance)),
        "interference": bool(np.any(clearance < -1e-8)),
        "experimental": p["standard"] in ("pco1881", "mason_70", "mason_86"),
        "physical_fit_verified": False,
    }

# ===========================================================================
# MODULE: thread_studio.mesh_generator
# ===========================================================================

"""Connected watertight radial meshes. Threads are surface coordinates, never added solids."""

pass  # [bundled] hoisted __future__ import
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
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import


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

# ===========================================================================
# MODULE: thread_studio.exporters
# ===========================================================================

"""Binary STL and OrcaSlicer 2.5.1+ multi-object 3MF project exporters for Orca Thread Studio."""

pass  # [bundled] hoisted __future__ import

import datetime as _dt
import json
import math
import re
import struct
import uuid
import zipfile
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape as _xml_escape

import numpy as np

_STL_RECORD_DTYPE = np.dtype(
    [
        ("normal", "<f4", (3,)),
        ("v0", "<f4", (3,)),
        ("v1", "<f4", (3,)),
        ("v2", "<f4", (3,)),
        ("attr", "<u2"),
    ]
)

_CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="config" ContentType="text/xml"/>
 <Default Extension="png" ContentType="image/png"/>
 <Default Extension="json" ContentType="application/json"/>
</Types>
"""

_RELS_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>
"""


def _extract_mesh_arrays(mesh: Any) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Extract validated (vertices, triangles, face_normals) arrays from duck-typed MeshData."""
    vertices = np.asarray(mesh.vertices, dtype=np.float32)
    if vertices.ndim != 2 or vertices.shape[1] != 3:
        raise ValueError(f"Expected vertices shape (V, 3), got {vertices.shape!r}")
    if not np.all(np.isfinite(vertices)):
        raise ValueError("Mesh contains nonfinite coordinates")

    triangles = np.asarray(mesh.triangles, dtype=np.int32)
    if triangles.size == 0:
        triangles = np.zeros((0, 3), dtype=np.int32)
    elif triangles.ndim != 2 or triangles.shape[1] != 3:
        raise ValueError(f"Expected triangles shape (F, 3), got {triangles.shape!r}")

    if (
        len(vertices) == 0
        or len(triangles) == 0
        or np.any(triangles < 0)
        or np.any(triangles >= len(vertices))
    ):
        raise ValueError("Mesh has empty or invalid topology")
    area_vectors = np.cross(
        vertices[triangles[:, 1]] - vertices[triangles[:, 0]],
        vertices[triangles[:, 2]] - vertices[triangles[:, 0]],
    )
    if np.any(np.linalg.norm(area_vectors, axis=1) <= 1e-10):
        raise ValueError("Mesh contains degenerate faces")
    num_tris = triangles.shape[0]
    raw_normals = getattr(mesh, "face_normals", None)
    if (
        raw_normals is not None
        and np.asarray(raw_normals).shape == (num_tris, 3)
        and np.all(np.isfinite(raw_normals))
    ):
        normals = np.asarray(raw_normals, dtype=np.float32)
    elif num_tris > 0:
        tris_xyz = vertices[triangles]
        e1 = tris_xyz[:, 1, :] - tris_xyz[:, 0, :]
        e2 = tris_xyz[:, 2, :] - tris_xyz[:, 0, :]
        cross = np.cross(e1, e2)
        lengths = np.linalg.norm(cross, axis=1, keepdims=True)
        safe_lengths = np.where(lengths > 1e-12, lengths, 1.0)
        normals = (cross / safe_lengths).astype(np.float32)
        normals = np.where(
            lengths > 1e-12, normals, np.array([[0.0, 0.0, 1.0]], dtype=np.float32)
        )
    else:
        normals = np.zeros((0, 3), dtype=np.float32)

    return vertices, triangles, normals


def _mesh_xy_extents(
    mesh: Any, vertices: np.ndarray | None = None
) -> tuple[float, float]:
    """Return (width_x_mm, depth_y_mm) of a mesh from vertices or bounds_mm."""
    verts = (
        vertices
        if vertices is not None
        else np.asarray(getattr(mesh, "vertices", []), dtype=np.float32)
    )
    if verts.ndim == 2 and verts.shape[0] > 0 and verts.shape[1] >= 2:
        dx = float(np.max(verts[:, 0]) - np.min(verts[:, 0]))
        dy = float(np.max(verts[:, 1]) - np.min(verts[:, 1]))
        return max(dx, 1.0), max(dy, 1.0)
    bounds = getattr(mesh, "bounds_mm", None)
    if isinstance(bounds, dict):
        size = bounds.get("size")
        if isinstance(size, (list, tuple)) and len(size) >= 2:
            return max(float(size[0]), 1.0), max(float(size[1]), 1.0)
        bmin = bounds.get("min")
        bmax = bounds.get("max")
        if (
            isinstance(bmin, (list, tuple))
            and isinstance(bmax, (list, tuple))
            and len(bmin) >= 2
            and len(bmax) >= 2
        ):
            return max(float(bmax[0]) - float(bmin[0]), 1.0), max(
                float(bmax[1]) - float(bmin[1]), 1.0
            )
    return 10.0, 10.0


def _mesh_xy_center_offset(
    mesh: Any, vertices: np.ndarray | None = None
) -> tuple[float, float]:
    """Return the local XY bounding-box midpoint `(mid_x, mid_y)` of `mesh`."""
    verts = (
        vertices
        if vertices is not None
        else np.asarray(mesh.vertices, dtype=np.float32)
    )
    if verts.shape[0] == 0:
        return 0.0, 0.0
    mx = 0.5 * float(np.max(verts[:, 0]) + np.min(verts[:, 0]))
    my = 0.5 * float(np.max(verts[:, 1]) + np.min(verts[:, 1]))
    return mx, my


def _resolve_bed_dimensions(host_config: dict[str, Any] | None) -> tuple[float, float]:
    """Use actual printer dimensions without enlarging a small bed silently."""
    config = host_config or {}
    printer = config.get("printer", {})
    dimensions = []
    for key in ("bed_x", "bed_y"):
        raw = config.get(key, printer.get(key, 220.0))
        value = float(raw)
        if not math.isfinite(value) or value <= 8:
            raise ValueError("Invalid printable bed dimensions")
        dimensions.append(value)
    return tuple(dimensions)


def _resolve_line_width(host_config: dict[str, Any] | None) -> float:
    """Resolve active outer wall line width in mm from host_config (default 0.42 mm)."""
    if isinstance(host_config, dict):
        for direct_key in ("line_width_mm",):
            if direct_key in host_config:
                try:
                    lw = float(host_config[direct_key])
                    if 0.18 <= lw <= 2.5:
                        return lw
                except (TypeError, ValueError):
                    pass
        printer = host_config.get("printer")
        if isinstance(printer, dict) and "line_width_mm" in printer:
            try:
                lw = float(printer["line_width_mm"])
                if 0.18 <= lw <= 2.5:
                    return lw
            except (TypeError, ValueError):
                pass
        ps = host_config.get("project_settings")
        if isinstance(ps, dict):
            raw_lw = ps.get("outer_wall_line_width") or ps.get("line_width")
            if isinstance(raw_lw, (list, tuple)) and raw_lw:
                raw_lw = raw_lw[0]
            if raw_lw is not None:
                s = str(raw_lw).strip()
                if not s.endswith("%"):
                    m = re.search(r"[-+]?\d*\.?\d+", s)
                    if m:
                        try:
                            lw = float(m.group(0))
                            if 0.18 <= lw <= 2.5:
                                return lw
                        except ValueError:
                            pass
    return 0.42


def _positions_overlap(
    positions: list[tuple[float, float, float]],
    extents: list[tuple[float, float]],
    min_clearance_mm: float = 3.0,
) -> bool:
    """Return True if any two axis-aligned bounding boxes overlap on the XY build plate."""
    n = len(positions)
    for i in range(n):
        xi, yi, _ = positions[i]
        wxi, wyi = extents[i]
        for j in range(i + 1, n):
            xj, yj, _ = positions[j]
            wxj, wyj = extents[j]
            overlap_x = abs(xi - xj) < (0.5 * (wxi + wxj) + min_clearance_mm)
            overlap_y = abs(yi - yj) < (0.5 * (wyi + wyj) + min_clearance_mm)
            if overlap_x and overlap_y:
                return True
    return False


def _pack_shelves(
    ordered_indices: list[int],
    extents: list[tuple[float, float]],
    max_row_width: float,
    gap_mm: float,
) -> tuple[list[list[int]], float, float]:
    """Pack `ordered_indices` greedily into horizontal shelves bounded by `max_row_width`."""
    rows: list[list[int]] = []
    cur_row: list[int] = []
    cur_w = 0.0

    for idx in ordered_indices:
        w, _ = extents[idx]
        needed_w = w if not cur_row else (cur_w + gap_mm + w)
        if cur_row and needed_w > max_row_width:
            rows.append(cur_row)
            cur_row = [idx]
            cur_w = w
        else:
            cur_row.append(idx)
            cur_w = needed_w
    if cur_row:
        rows.append(cur_row)

    total_w = 0.0
    total_h = 0.0
    for r_idx, row in enumerate(rows):
        rw = sum(extents[i][0] for i in row) + gap_mm * (len(row) - 1)
        rh = max(extents[i][1] for i in row)
        total_w = max(total_w, rw)
        total_h += rh + (gap_mm if r_idx > 0 else 0.0)

    return rows, total_w, total_h


def _arrange_items_on_bed(extents, z_offsets, bed_x, bed_y, gap_mm=8.0):
    usable_x = bed_x - 8
    usable_y = bed_y - 8
    best = None
    for cap in [usable_x, usable_x * 0.8, usable_x * 0.6]:
        rows, w, h = _pack_shelves(list(range(len(extents))), extents, cap, gap_mm)
        if w <= usable_x and h <= usable_y and (best is None or w * h < best[0]):
            best = (w * h, rows, w, h)
    if best is None:
        raise ValueError(
            "Objects do not fit this print bed; export individual parts or select a larger printer"
        )
    _, rows, w, h = best
    out = [None] * len(extents)
    y = (bed_y - h) / 2
    for row in rows:
        rw = sum(extents[i][0] for i in row) + gap_mm * (len(row) - 1)
        rh = max(extents[i][1] for i in row)
        x = (bed_x - rw) / 2
        for i in row:
            wi, di = extents[i]
            out[i] = (x + wi / 2, y + rh / 2, z_offsets[i])
            x += wi + gap_mm
        y += rh + gap_mm
    return out


def _build_project_settings_dict(
    params: dict[str, Any] | None, host_config: dict[str, Any] | None
) -> dict[str, Any]:
    """Merge host project settings with structural mechanical thread overrides for OrcaSlicer 2.5.1+."""
    merged: dict[str, Any] = {}
    if isinstance(host_config, dict):
        raw_ps = host_config.get("project_settings")
        if isinstance(raw_ps, dict):
            merged.update(raw_ps)

    p = params if isinstance(params, dict) else {}

    # Threaded components are structural mechanical parts: NEVER slice in spiral vase mode!
    merged["spiral_mode"] = "0"
    merged["spiral_mode_smooth"] = "0"

    if bool(p.get("auto_configure_slicer", True)):
        merged["wall_loops"] = "5"
        merged["top_shell_layers"] = "5"
        merged["bottom_shell_layers"] = "5"
        merged["sparse_infill_density"] = "30%"
        merged["sparse_infill_pattern"] = "gyroid"
        merged["layer_height"] = str(
            min(0.16, max(0.06, float(p.get("pitch", 3)) / 12))
        )
        merged["elefant_foot_compensation"] = "0.15"

    return merged


def write_binary_stl(
    path: str | Path, mesh: Any, header_name: str = "OrcaThreadStudio"
) -> Path:
    """Write a duck-typed MeshData object to a standard little-endian binary STL file.

    Binary layout: 80-byte ASCII header + uint32 triangle count + F * 50-byte facet records.
    """
    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    vertices, triangles, normals = _extract_mesh_arrays(mesh)
    num_triangles = int(triangles.shape[0])

    clean_header = str(header_name or "OrcaThreadStudio").strip() or "OrcaThreadStudio"
    if clean_header.lower().startswith("solid"):
        clean_header = f"Orca_{clean_header}"
    header_text = f"{clean_header} - Orca Thread Studio Binary STL"
    header_bytes = header_text.encode("ascii", errors="replace")[:80].ljust(80, b"\x00")

    records = np.zeros(num_triangles, dtype=_STL_RECORD_DTYPE)
    if num_triangles > 0:
        tris_xyz = vertices[triangles]
        records["normal"] = normals.astype("<f4", copy=False)
        records["v0"] = tris_xyz[:, 0, :].astype("<f4", copy=False)
        records["v1"] = tris_xyz[:, 1, :].astype("<f4", copy=False)
        records["v2"] = tris_xyz[:, 2, :].astype("<f4", copy=False)
        records["attr"] = 0

    with open(out_path, "wb") as fh:
        fh.write(header_bytes)
        fh.write(struct.pack("<I", num_triangles))
        if num_triangles > 0:
            fh.write(records.tobytes())

    return out_path


def write_orca_3mf(
    path: str | Path,
    items: list[tuple[str, Any] | tuple[str, Any, tuple[float, float, float] | None]],
    params: dict[str, Any],
    host_config: dict[str, Any] | None = None,
) -> Path:
    """Write an OrcaSlicer 2.5.1+ compatible .3mf project archive with multi-object layout & slicer settings."""
    if not items:
        raise ValueError("write_orca_3mf requires at least one item in 'items'.")

    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    bed_x, bed_y = _resolve_bed_dimensions(host_config)
    cx, cy = bed_x * 0.5, bed_y * 0.5

    parsed_items: list[
        tuple[str, np.ndarray, np.ndarray, tuple[float, float], tuple[float, float]]
    ] = []
    raw_positions: list[tuple[float, float, float] | None] = []
    z_offsets: list[float] = []

    for idx, entry in enumerate(items):
        if len(entry) == 2:
            raw_name, mesh = entry  # type: ignore[misc]
            raw_pos = None
        elif len(entry) >= 3:
            raw_name, mesh, raw_pos = entry[0], entry[1], entry[2]
        else:
            raise ValueError(f"Invalid item tuple at index {idx}: {entry!r}")

        item_name = str(raw_name or f"Part_{idx + 1}").strip() or f"Part_{idx + 1}"
        vertices, triangles, _ = _extract_mesh_arrays(mesh)
        ext = _mesh_xy_extents(mesh, vertices)
        local_mid = _mesh_xy_center_offset(mesh, vertices)
        parsed_items.append((item_name, vertices, triangles, ext, local_mid))

        if raw_pos is None:
            raw_positions.append(None)
            z_offsets.append(0.0)
        else:
            px, py, pz = float(raw_pos[0]), float(raw_pos[1]), float(raw_pos[2])
            raw_positions.append((px, py, pz))
            z_offsets.append(pz)

    extents_list = [it[3] for it in parsed_items]
    if any(pos is None for pos in raw_positions):
        box_centers = _arrange_items_on_bed(
            extents_list, z_offsets, bed_x, bed_y, gap_mm=8.0
        )
        # Subtract local mesh midpoint so even asymmetric sector/gauge meshes land centered on their box!
        final_positions = [
            (bx - parsed_items[i][4][0], by - parsed_items[i][4][1], bz)
            for i, (bx, by, bz) in enumerate(box_centers)
        ]
    else:
        concrete_centers = [
            (pos[0] + parsed_items[i][4][0], pos[1] + parsed_items[i][4][1], pos[2])
            for i, pos in enumerate(raw_positions)
            if pos is not None
        ]
        if len(concrete_centers) >= 2 and _positions_overlap(
            concrete_centers, extents_list, min_clearance_mm=3.0
        ):
            box_centers = _arrange_items_on_bed(
                extents_list, z_offsets, bed_x, bed_y, gap_mm=8.0
            )
            final_positions = [
                (bx - parsed_items[i][4][0], by - parsed_items[i][4][1], bz)
                for i, (bx, by, bz) in enumerate(box_centers)
            ]
        else:
            final_positions = [pos for pos in raw_positions if pos is not None]

    for index, (name, vertices, triangles, extent, midpoint) in enumerate(parsed_items):
        tx, ty, tz = final_positions[index]
        placed = vertices + np.array([tx, ty, tz])
        if (
            np.any(placed[:, 0] < 4)
            or np.any(placed[:, 0] > bed_x - 4)
            or np.any(placed[:, 1] < 4)
            or np.any(placed[:, 1] > bed_y - 4)
        ):
            raise ValueError(
                "An object extends beyond the printable bed; export individual parts"
            )
        if np.min(placed[:, 2]) < -0.001 or np.max(placed[:, 2]) > float(
            (host_config or {}).get("max_z", 1000)
        ):
            raise ValueError("An object exceeds the printable height")

    title = str(
        (params or {}).get("name") or parsed_items[0][0] or "Orca Thread Studio"
    ).strip()
    escaped_title = _xml_escape(title, {'"': "&quot;"})
    today_iso = _dt.date.today().isoformat()
    ns_seed = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
    build_uuid = str(uuid.uuid5(ns_seed, f"orca-thread-build-{title}"))

    object_blocks: list[str] = []
    build_items_xml: list[str] = []
    model_settings_objects: list[str] = []
    model_settings_instances: list[str] = []
    model_settings_assemble: list[str] = []

    for idx, (item_name, vertices, triangles, _, _) in enumerate(parsed_items):
        obj_id = idx + 1
        tx, ty, tz = final_positions[idx]
        esc_name = _xml_escape(item_name, {'"': "&quot;"})
        obj_uuid = str(uuid.uuid5(ns_seed, f"orca-thread-obj-{obj_id}-{item_name}"))
        item_uuid = str(uuid.uuid5(ns_seed, f"orca-thread-item-{obj_id}-{item_name}"))

        verts_py = vertices.tolist()
        tris_py = triangles.tolist()

        vertex_lines = "\n".join(
            f'     <vertex x="{vx:.9g}" y="{vy:.9g}" z="{vz:.9g}"/>'
            for vx, vy, vz in verts_py
        )
        triangle_lines = "\n".join(
            f'     <triangle v1="{v1}" v2="{v2}" v3="{v3}"/>' for v1, v2, v3 in tris_py
        )

        object_blocks.append(
            f'  <object id="{obj_id}" p:UUID="{obj_uuid}" name="{esc_name}" type="model">\n'
            f"   <mesh>\n"
            f"    <vertices>\n"
            f"{vertex_lines}\n"
            f"    </vertices>\n"
            f"    <triangles>\n"
            f"{triangle_lines}\n"
            f"    </triangles>\n"
            f"   </mesh>\n"
            f"  </object>"
        )

        transform_3x4 = f"1 0 0 0 1 0 0 0 1 {tx:.4f} {ty:.4f} {tz:.4f}"
        build_items_xml.append(
            f'  <item objectid="{obj_id}" p:UUID="{item_uuid}" transform="{transform_3x4}" printable="1"/>'
        )

        model_settings_objects.append(
            f'  <object id="{obj_id}">\n'
            f'    <metadata key="name" value="{esc_name}"/>\n'
            f'    <metadata key="extruder" value="1"/>\n'
            f'    <part id="1" subtype="normal_part">\n'
            f'      <metadata key="name" value="{esc_name}"/>\n'
            f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
            f'      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
            f"    </part>\n"
            f"  </object>"
        )
        model_settings_instances.append(
            f"    <model_instance>\n"
            f'      <metadata key="object_id" value="{obj_id}"/>\n'
            f'      <metadata key="instance_id" value="0"/>\n'
            f'      <metadata key="identify_id" value="{100 + obj_id}"/>\n'
            f"    </model_instance>"
        )
        model_settings_assemble.append(
            f'    <assemble_item object_id="{obj_id}" instance_id="0" transform="{transform_3x4}" offset="0 0 0"/>'
        )

    model_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<model unit="millimeter" xml:lang="en-US" '
        'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
        'xmlns:BambuStudio="http://schemas.bambulab.com/package/2021" '
        'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" '
        'requiredextensions="p">\n'
        ' <metadata name="Application">OrcaSlicer-2.5.1</metadata>\n'
        ' <metadata name="OrcaSlicer">2.5.1</metadata>\n'
        ' <metadata name="BambuStudio:3mfVersion">1</metadata>\n'
        f' <metadata name="Title">{escaped_title}</metadata>\n'
        f' <metadata name="CreationDate">{today_iso}</metadata>\n'
        " <resources>\n"
        + "\n".join(object_blocks)
        + "\n </resources>\n"
        + f' <build p:UUID="{build_uuid}">\n'
        + "\n".join(build_items_xml)
        + "\n </build>\n"
        "</model>\n"
    )

    model_settings_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<config>\n" + "\n".join(model_settings_objects) + "\n  <plate>\n"
        '    <metadata key="plater_id" value="1"/>\n'
        '    <metadata key="plater_name" value=""/>\n'
        '    <metadata key="locked" value="false"/>\n'
        + "\n".join(model_settings_instances)
        + "\n  </plate>\n"
        "  <assemble>\n" + "\n".join(model_settings_assemble) + "\n  </assemble>\n"
        "</config>\n"
    )

    project_settings = _build_project_settings_dict(params, host_config)
    project_settings_json = json.dumps(project_settings, indent=2, ensure_ascii=False)

    with zipfile.ZipFile(
        out_path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=6
    ) as zf:
        zf.writestr("[Content_Types].xml", _CONTENT_TYPES_XML)
        zf.writestr("_rels/.rels", _RELS_XML)
        zf.writestr("3D/3dmodel.model", model_xml)
        zf.writestr("Metadata/model_settings.config", model_settings_xml)
        zf.writestr("Metadata/project_settings.config", project_settings_json)

    return out_path

# ===========================================================================
# MODULE: thread_studio.presets_catalog
# ===========================================================================

"""Twelve bilingual starting points and atomic user preset persistence."""

pass  # [bundled] hoisted __future__ import
import json, uuid, random
from pathlib import Path
pass  # [bundled] resolved intra-package import

_PRESET_ROWS = [
    ("edc", "Pote EDC 40", "EDC jar 40", dict()),
    (
        "small",
        "Pote compacto 28",
        "Compact jar 28",
        dict(nominal_dia=28, diameter=32, height=35, pitch=2, thread_length=8),
    ),
    (
        "large",
        "Pote oficina 70",
        "Workshop jar 70",
        dict(nominal_dia=70, diameter=75, height=80, pitch=4),
    ),
    (
        "pco",
        "PET PCO-1881 experimental",
        "PET PCO-1881 experimental",
        dict(module="standard_bottle_cap", standard="pco1881"),
    ),
    (
        "mason70",
        "Mason 70 experimental",
        "Mason 70 experimental",
        dict(module="standard_bottle_cap", standard="mason_70"),
    ),
    (
        "mason86",
        "Mason 86: medir primeiro",
        "Mason 86: measure first",
        dict(module="standard_bottle_cap", standard="mason_86"),
    ),
    (
        "vacuum35",
        "Aspirador 35 para 58",
        "Vacuum 35 to 58",
        dict(module="hose_vacuum_adapter", inlet_diameter=35, outlet_diameter=58),
    ),
    (
        "hose25",
        "Mangueira 25 para 32",
        "Hose 25 to 32",
        dict(
            module="hose_vacuum_adapter",
            inlet_diameter=25,
            outlet_diameter=32,
            end_a="barb",
            end_b="barb",
        ),
    ),
    (
        "adapter",
        "Adaptador rosqueado M40",
        "M40 threaded adapter",
        dict(
            module="hose_vacuum_adapter",
            inlet_diameter=40,
            outlet_diameter=32,
            end_a="female",
            end_b="male",
        ),
    ),
    (
        "m6",
        "Parafuso e porca M6",
        "M6 bolt and nut",
        dict(
            module="bolt_nut_knob",
            standard="iso_metric",
            nominal_dia=6,
            pitch=1,
            thread_length=15,
            head_height=3,
            wall_thickness=1.2,
            gasket=False,
        ),
    ),
    (
        "m12",
        "Manipulo M12",
        "M12 hand knob",
        dict(
            module="bolt_nut_knob",
            standard="iso_metric",
            nominal_dia=12,
            pitch=1.75,
            thread_length=22,
            head="knurled",
            gasket=False,
        ),
    ),
    (
        "wing",
        "Borboleta M20 esquerda",
        "M20 left-hand wing bolt",
        dict(
            module="bolt_nut_knob",
            standard="fdm_trapezoid_45",
            nominal_dia=20,
            pitch=2.5,
            hand="left",
            head="wing",
            gasket=False,
        ),
    ),
]
BUILTIN_PRESETS = [
    dict(id=i, name_pt=pt, name_en=en, params=normalize_params(p))
    for i, pt, en, p in _PRESET_ROWS
]


def load_user_presets(directory):
    f = Path(directory) / "user_presets.json"
    if not f.is_file():
        return []
    data = json.loads(f.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Invalid preset list")
    return [
        dict(
            id=str(x["id"]),
            name=str(x["name"])[:80],
            params=normalize_params(x["params"]),
        )
        for x in data
    ]


def _write_presets(directory, data):
    d = Path(directory)
    d.mkdir(parents=True, exist_ok=True)
    f = d / "user_presets.json"
    temp = d / "user_presets.tmp"
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(f)
    return data


def save_user_preset(directory, name, params, preset_id=None):
    data = load_user_presets(directory)
    pid = str(preset_id or uuid.uuid4().hex)
    data = [x for x in data if x["id"] != pid]
    data.append(dict(id=pid, name=str(name)[:80], params=normalize_params(params)))
    return _write_presets(directory, data)


def delete_user_preset(directory, preset_id):
    return _write_presets(
        directory,
        [x for x in load_user_presets(directory) if x["id"] != str(preset_id)],
    )


def generate_random_printable_params(seed=None, current_params=None):
    rng = random.Random(seed)
    p = normalize_params(current_params)
    p.update(
        nominal_dia=rng.choice([24, 32, 40, 50]),
        pitch=rng.choice([2.0, 2.5, 3.0]),
        texture=rng.choice(["knurled", "fluted", "smooth"]),
    )
    return normalize_params(p)

# ===========================================================================
# MODULE: thread_studio.studio_ui
# ===========================================================================

"""Offline bilingual WebGL2 studio. Preview uses the exported NumPy triangles."""

pass  # [bundled] hoisted __future__ import
import json
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import


def get_studio_html(mode="page", initial_context=None):
    context = initial_context or dict(
        params=DEFAULT_PARAMS,
        builtin_presets=BUILTIN_PRESETS,
        user_presets=[],
        lang="pt",
        theme="dark",
    )
    safe = (
        json.dumps(context, ensure_ascii=False)
        .replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    return _HTML.replace("__CONTEXT__", safe).replace("__MODE__", mode)


_HTML = r"""<!doctype html>
<html lang="pt" data-theme="dark">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Orca Thread Studio</title>
    <style>
      :root {
        --bg: #15171b;
        --panel: #1d2026;
        --card: #242830;
        --input: #16181d;
        --line: #313641;
        --text: #eef2f7;
        --muted: #9aa4b4;
        --accent: #00a896;
        --soft: rgba(0, 191, 165, 0.13);
        --view: #171c24;
        --gold: #ffb74d;
        --danger: #ff6868;
        color-scheme: dark;
        font:
          13px "Segoe UI",
          Ubuntu,
          sans-serif;
      }
      [data-theme="light"] {
        --bg: #edf1f6;
        --panel: #fff;
        --card: #f5f7fb;
        --input: #fff;
        --line: #d4dce5;
        --text: #1b222c;
        --muted: #525e6f;
        --accent: #00897b;
        --soft: rgba(0, 137, 123, 0.12);
        --view: #dce3ec;
        color-scheme: light;
      }
      * {
        box-sizing: border-box;
      }
      [hidden] {
        display: none !important;
      }
      body {
        margin: 0;
        background: var(--bg);
        color: var(--text);
        overflow: hidden;
      }
      button,
      select,
      input {
        font: inherit;
        color: inherit;
      }
      button {
        cursor: pointer;
        border: 1px solid var(--line);
        border-radius: 6px;
        background: var(--card);
        padding: 8px 11px;
      }
      button:hover {
        border-color: var(--accent);
      }
      button:focus-visible,
      input:focus-visible,
      select:focus-visible {
        outline: 2px solid var(--accent);
        outline-offset: 2px;
      }
      button:disabled {
        opacity: 0.4;
        cursor: default;
      }
      header {
        height: 68px;
        border-bottom: 1px solid var(--line);
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 0 20px;
        background: var(--panel);
      }
      .brandmark {
        height: 36px;
        width: 36px;
        border: 1px solid var(--accent);
        border-radius: 9px;
        color: var(--accent);
        font: bold 23px Consolas;
        text-align: center;
        line-height: 34px;
      }
      h1 {
        font-size: 17px;
        margin: 0;
        letter-spacing: 0.2px;
      }
      .subtitle {
        font-size: 11px;
        color: var(--muted);
        margin-top: 4px;
      }
      .spacer {
        flex: 1;
      }
      .header-actions {
        display: flex;
        gap: 6px;
      }
      .layout {
        display: grid;
        grid-template-columns: 300px minmax(300px, 1fr) 280px;
        height: calc(100vh - 68px);
        gap: 1px;
        background: var(--line);
      }
      aside {
        background: var(--panel);
        overflow: auto;
        padding: 16px;
      }
      .section-title {
        text-transform: uppercase;
        color: var(--muted);
        font-size: 10px;
        letter-spacing: 1.5px;
        margin: 18px 0 12px;
        font-weight: 700;
      }
      .section-title:first-child {
        margin-top: 0;
      }
      label.field {
        display: grid;
        grid-template-columns: 1fr 108px;
        gap: 8px;
        align-items: center;
        margin: 10px 0;
        font-size: 12px;
      }
      label.field span {
        line-height: 1.4;
      }
      input,
      select {
        width: 100%;
        border: 1px solid var(--line);
        background: var(--input);
        border-radius: 5px;
        padding: 7px;
        min-width: 0;
      }
      input[type="checkbox"] {
        width: 18px;
        height: 18px;
        justify-self: end;
        accent-color: var(--accent);
      }
      input[type="range"] {
        accent-color: var(--accent);
        padding: 0;
      }
      select {
        font-size: 12px;
      }
      .group {
        border-top: 1px solid var(--line);
        padding-top: 10px;
        margin-top: 18px;
      }
      .preview {
        background: var(--view);
        display: flex;
        flex-direction: column;
        min-width: 0;
        overflow: hidden;
      }
      .toolbar {
        display: flex;
        gap: 6px;
        align-items: center;
        padding: 10px 12px;
        flex-wrap: wrap;
        border-bottom: 1px solid var(--line);
        background: var(--panel);
      }
      .toolbar button {
        padding: 6px 9px;
        font-size: 11px;
      }
      .view-wrap {
        flex: 1;
        min-height: 200px;
        position: relative;
      }
      #viewport {
        width: 100%;
        height: 100%;
        display: block;
        touch-action: none;
      }
      .hud {
        position: absolute;
        left: 16px;
        top: 16px;
        pointer-events: none;
        font:
          11px Consolas,
          monospace;
        color: var(--muted);
        line-height: 1.8;
      }
      .axis {
        position: absolute;
        bottom: 14px;
        right: 18px;
        font: 11px Consolas;
        color: var(--muted);
      }
      .loupe {
        height: 190px;
        min-height: 150px;
        border-top: 1px solid var(--line);
        background: var(--panel);
        padding: 12px;
        position: relative;
      }
      .loupe-title {
        font-size: 11px;
        color: var(--muted);
        display: flex;
        justify-content: space-between;
      }
      .loupe canvas {
        height: 130px;
        width: 100%;
      }
      .key {
        display: inline-block;
        width: 8px;
        height: 8px;
        margin-right: 5px;
        background: var(--accent);
        border-radius: 50%;
      }
      .key.female {
        background: var(--gold);
      }
      .metric {
        padding: 12px;
        border: 1px solid var(--line);
        border-radius: 8px;
        background: var(--card);
        margin: 8px 0;
      }
      .metric strong {
        font:
          22px Consolas,
          monospace;
        display: block;
        margin: 4px 0;
        color: var(--accent);
      }
      .metric small {
        color: var(--muted);
      }
      .row {
        display: flex;
        gap: 6px;
        margin: 8px 0;
      }
      .row > * {
        flex: 1;
      }
      .primary {
        background: var(--accent);
        color: #fff;
        border-color: var(--accent);
        font-weight: 600;
        width: 100%;
        margin: 9px 0;
        padding: 12px;
      }
      .hint {
        font-size: 11px;
        color: var(--muted);
        line-height: 1.65;
      }
      .warning {
        background: #ffb74d14;
        border: 1px solid #ffb74d66;
        color: var(--gold);
        padding: 10px;
        border-radius: 6px;
        font-size: 11px;
        line-height: 1.6;
        margin: 10px 0;
      }
      .status {
        white-space: pre-wrap;
        overflow-wrap: anywhere;
        padding: 10px;
        font-size: 11px;
        line-height: 1.5;
        border-left: 2px solid var(--accent);
        margin: 10px 0;
        max-height: 180px;
        overflow: auto;
      }
      .status.error {
        border-color: var(--danger);
      }
      .chip {
        padding: 4px 7px;
        background: var(--soft);
        color: var(--accent);
        border-radius: 4px;
        font-size: 10px;
      }
      .docknav {
        display: none;
      }
      .compact .layout {
        display: block;
        overflow: auto;
        height: calc(100vh - 108px);
      }
      .compact header {
        height: 68px;
        padding: 0 10px;
      }
      .compact h1 {
        font-size: 14px;
      }
      .compact .subtitle {
        font-size: 10px;
      }
      .compact .header-actions button {
        padding: 6px;
      }
      .compact .docknav {
        display: flex;
        background: var(--panel);
        height: 40px;
        border-bottom: 1px solid var(--line);
      }
      .docknav button {
        flex: 1;
        border-radius: 0;
        border: 0;
        background: transparent;
      }
      .docknav button.active {
        color: var(--accent);
        border-bottom: 2px solid var(--accent);
      }
      .compact aside,
      .compact .preview {
        display: none;
      }
      .compact [data-tab="controls"] #controls,
      .compact [data-tab="output"] #output {
        display: block;
      }
      .compact [data-tab="preview"] .preview {
        display: flex;
        height: calc(100vh - 108px);
      }
      .compact header .brandmark {
        display: none;
      }
      @media (max-width: 1000px) {
        .layout {
          grid-template-columns: 255px minmax(250px, 1fr) 235px;
        }
        aside {
          padding: 12px;
        }
      }
      @media (prefers-reduced-motion: reduce) {
        * {
          scroll-behavior: auto;
        }
      }
    </style>
  </head>
  <body>
    <header>
      <div class="brandmark">≋</div>
      <div>
        <h1>Orca Thread Studio</h1>
        <div class="subtitle" data-i="subtitle">
          Roscas, potes e adaptadores · projeto paramétrico
        </div>
      </div>
      <div class="spacer"></div>
      <div class="header-actions">
        <button id="reset" data-i="reset">Resetar</button
        ><button id="undo" title="Undo">↶</button
        ><button id="redo" title="Redo">↷</button
        ><button id="theme" aria-label="Theme">◐</button
        ><button id="language">EN</button>
      </div>
    </header>
    <nav class="docknav">
      <button data-view="controls" class="active" data-i="parameters">
        Parâmetros</button
      ><button data-view="preview" data-i="preview">Visualização</button
      ><button data-view="output" data-i="output">Exportação</button>
    </nav>
    <main class="layout" data-tab="controls">
      <aside id="controls">
        <div class="section-title" data-i="presets">Biblioteca de projetos</div>
        <select id="preset" aria-label="Preset"></select>
        <div class="row">
          <button id="save" data-i="save">Salvar preset</button
          ><button id="remove" data-i="remove">Excluir</button>
        </div>
        <div class="group">
          <div class="section-title" data-i="parameters">Parâmetros</div>
          <div id="fields"></div>
        </div>
      </aside>
      <section class="preview">
        <div class="toolbar">
          <span class="chip">WebGL2 · mm</span
          ><button id="fit" data-i="fit">Enquadrar</button
          ><button id="cut" data-i="cut">Corte axial</button
          ><button id="animate" data-i="animate">Rosquear</button
          ><span class="spacer"></span
          ><label class="hint"
            ><span data-i="explode">Abertura</span>
            <input
              id="explode"
              aria-label="Opening"
              type="range"
              min="0"
              max="40"
              value="12"
              style="width: 95px"
          /></label>
        </div>
        <div class="view-wrap">
          <canvas id="viewport" aria-label="3D model preview"></canvas>
          <div class="hud" id="hud"></div>
          <div class="axis">X · Y · Z ↑</div>
        </div>
        <div class="loupe">
          <div class="loupe-title">
            <span data-i="loupe">Lupa de flancos · seção axial</span
            ><span
              ><i class="key"></i><span data-i="male">Macho</span>
              <i class="key female"></i><span data-i="female">Fêmea</span></span
            >
          </div>
          <canvas id="loupe" aria-label="Thread engagement section"></canvas>
        </div>
      </section>
      <aside id="output">
        <div class="section-title" data-i="analysis">Análise de encaixe</div>
        <div class="metric">
          <small data-i="radial">Folga radial nominal</small
          ><strong id="radial">—</strong><small id="axial">—</small>
        </div>
        <div class="metric">
          <small data-i="lead">Avanço por volta</small
          ><strong id="lead">—</strong><small id="check">—</small>
        </div>
        <div id="warning" class="warning" hidden></div>
        <p class="hint" data-i="physical">
          O encaixe depende do filamento e da impressora. Imprima o calibrador
          antes da peça final.
        </p>
        <div class="section-title" data-i="output">Exportação</div>
        <label class="field"
          ><span data-i="target">Peças</span
          ><select id="target"></select></label
        ><button id="send" class="primary" data-i="send">
          Enviar para a mesa
        </button>
        <div class="row">
          <button id="stl">STL</button><button id="three">3MF</button>
        </div>
        <button id="folder" style="width: 100%" data-i="folder">
          Abrir pasta de exportações
        </button>
        <div id="status" class="status" role="status" aria-live="polite"></div>
        <div class="section-title" data-i="printer">Impressora conectada</div>
        <p id="host" class="hint"></p>
        <p class="hint" data-i="settings">
          3MF: 5 paredes, 5 camadas de topo/base e camada fina para as roscas.
          As peças são distribuídas sem alterar a escala.
        </p>
      </aside>
    </main>
    <script>
      "use strict";
      const INITIAL = __CONTEXT__,
        MODE = "__MODE__";
      let params = { ...INITIAL.params },
        lang = INITIAL.lang === "en" ? "en" : "pt",
        meshes = [],
        profile = null,
        report = null,
        userPresets = INITIAL.user_presets || [],
        builtins = INITIAL.builtin_presets || [],
        cut = false,
        animating = false,
        spin = 0,
        yaw = -0.65,
        pitch = -0.5,
        zoom = 1,
        opening = 12,
        drag = null,
        frameTime = 0;
      const $ = (id) => document.getElementById(id);
      const words = {
        pt: {
          reset: "Resetar",
          subtitle: "Roscas, potes e adaptadores · projeto paramétrico",
          parameters: "Parâmetros",
          preview: "Visualização",
          output: "Exportação",
          presets: "Biblioteca de projetos",
          save: "Salvar preset",
          remove: "Excluir",
          fit: "Enquadrar",
          cut: "Corte axial",
          animate: "Rosquear",
          explode: "Abertura",
          loupe: "Lupa de flancos · seção axial",
          male: "Macho",
          female: "Fêmea",
          analysis: "Análise de encaixe",
          radial: "Folga radial nominal",
          lead: "Avanço por volta",
          physical:
            "O encaixe depende do filamento e da impressora. Imprima o calibrador antes da peça final.",
          target: "Peças",
          send: "Enviar para a mesa",
          folder: "Abrir pasta de exportações",
          printer: "Impressora conectada",
          settings:
            "3MF: 5 paredes, 5 camadas de topo/base e camada fina para as roscas. As peças são distribuídas sem alterar a escala.",
          experimental:
            "Experimental: perfil simplificado; encaixe físico não homologado. Sem garantia de vedação, pressão ou uso alimentar.",
          clear: "Sem interferência no envelope analítico",
          waiting: "Aguardando o host do OrcaSlicer.",
          local:
            "A prévia depende do plugin nativo. Abra este estúdio no OrcaSlicer.",
          notch: "Anéis: 1 / 2 / 3 entalhes = 0,10 / 0,18 / 0,26 mm",
        },
        en: {
          reset: "Reset",
          subtitle: "Threads, containers and adapters · parametric design",
          parameters: "Parameters",
          preview: "Preview",
          output: "Export",
          presets: "Project library",
          save: "Save preset",
          remove: "Delete",
          fit: "Fit view",
          cut: "Axial section",
          animate: "Screw motion",
          explode: "Opening",
          loupe: "Thread loupe · axial section",
          male: "Male",
          female: "Female",
          analysis: "Engagement analysis",
          radial: "Nominal radial clearance",
          lead: "Lead per revolution",
          physical:
            "Fit depends on your filament and printer. Print calibration rings before the final part.",
          target: "Parts",
          send: "Send to plater",
          folder: "Open export folder",
          printer: "Connected printer",
          settings:
            "3MF: 5 walls, 5 top/bottom layers and fine thread layers. Parts are arranged at their original scale.",
          experimental:
            "Experimental: simplified profile; physical fit is unverified. No sealing, pressure or food-use guarantee.",
          clear: "No analytical envelope interference",
          waiting: "Waiting for the OrcaSlicer host.",
          local:
            "Preview requires the native plugin. Open this studio in OrcaSlicer.",
          notch: "Rings: 1 / 2 / 3 notches = 0.10 / 0.18 / 0.26 mm",
        },
      };
      const labels = {
        module: ["Tipo de projeto", "Project type"],
        standard: ["Perfil de rosca", "Thread profile"],
        part: ["Peça de garrafa", "Bottle part"],
        name: ["Nome", "Name"],
        nominal_dia: ["Diâmetro nominal · mm", "Nominal diameter · mm"],
        pitch: ["Passo axial · mm", "Axial pitch · mm"],
        thread_length: ["Comprimento roscado · mm", "Thread length · mm"],
        starts: ["Entradas", "Starts"],
        hand: ["Sentido", "Handedness"],
        diameter: ["Diâmetro do corpo · mm", "Body diameter · mm"],
        height: ["Altura do pote · mm", "Container height · mm"],
        wall_thickness: ["Parede · mm", "Wall · mm"],
        floor_thickness: ["Fundo · mm", "Floor · mm"],
        diametral_clearance: [
          "Folga diametral · mm",
          "Diametral clearance · mm",
        ],
        axial_clearance: ["Folga axial · mm", "Axial clearance · mm"],
        higbee_turns: ["Higbee · voltas", "Higbee · turns"],
        texture: ["Textura", "Texture"],
        knurl_depth: ["Profundidade da textura · mm", "Texture depth · mm"],
        knurl_count: ["Repetições da textura", "Texture repeats"],
        head: ["Cabeça / porca", "Head / nut"],
        head_height: ["Altura da cabeça · mm", "Head height · mm"],
        bore_diameter: ["Furo do parafuso · mm", "Bolt bore · mm"],
        inlet_diameter: ["Entrada · mm", "Inlet · mm"],
        outlet_diameter: ["Saída · mm", "Outlet · mm"],
        adapter_length: ["Comprimento total · mm", "Overall length · mm"],
        end_length: ["Comprimento das pontas · mm", "End length · mm"],
        end_a: ["Ponta de entrada", "Inlet end"],
        end_b: ["Ponta de saída", "Outlet end"],
        gasket: ["Canal para vedação", "Gasket groove"],
        gasket_width: ["Largura do canal · mm", "Groove width · mm"],
        gasket_depth: ["Profundidade do canal · mm", "Groove depth · mm"],
        gasket_offset: ["Recuo do canal · mm", "Groove inset · mm"],
        auto_configure_slicer: ["Ajustar fatiamento", "Configure slicing"],
        measurements_confirmed: [
          "Confirmo as medidas reais",
          "I confirm measured dimensions",
        ],
        measured_major_dia: [
          "Mason 86: diâmetro maior",
          "Mason 86: major diameter",
        ],
        measured_root_dia: [
          "Mason 86: diâmetro da raiz",
          "Mason 86: root diameter",
        ],
        measured_pitch: ["Mason 86: passo medido", "Mason 86: measured pitch"],
        measured_length: ["Mason 86: comprimento", "Mason 86: thread length"],
      };
      const options = {
        module: [
          ["container_and_lid", "Pote + tampa", "Container + lid"],
          ["standard_bottle_cap", "Tampa / gargalo", "Bottle cap / neck"],
          ["hose_vacuum_adapter", "Adaptador", "Hose adapter"],
          ["bolt_nut_knob", "Parafuso + porca", "Bolt + nut"],
        ],
        standard: [
          ["fdm_trapezoid_45", "FDM 45°", "FDM 45°"],
          ["iso_metric", "Métrica 60°", "Metric 60°"],
          ["pco1881", "PCO-1881 experimental", "PCO-1881 experimental"],
          ["mason_70", "Mason 70 experimental", "Mason 70 experimental"],
          ["mason_86", "Mason 86 · medir", "Mason 86 · measure"],
        ],
        part: [
          ["cap", "Tampa", "Cap"],
          ["neck", "Gargalo", "Neck"],
        ],
        starts: [
          ["1", "1", "1"],
          ["2", "2", "2"],
          ["3", "3", "3"],
        ],
        hand: [
          ["right", "Direita", "Right"],
          ["left", "Esquerda", "Left"],
        ],
        texture: [
          ["knurled", "Recartilhado", "Knurled"],
          ["fluted", "Canelado", "Fluted"],
          ["smooth", "Liso", "Smooth"],
          ["faceted", "Facetado", "Faceted"],
        ],
        head: [
          ["hex", "Sextavada", "Hex"],
          ["knurled", "Recartilhada", "Knurled"],
          ["wing", "Borboleta", "Wing"],
        ],
        end_a: [
          ["smooth", "Liso cônico", "Smooth tapered"],
          ["barb", "Espigão", "Barb"],
          ["male", "Rosca macho", "Male thread"],
          ["female", "Rosca fêmea", "Female thread"],
        ],
        export_target: [
          ["all", "Conjunto", "All parts"],
          ["primary", "Peça principal", "Primary part"],
          ["secondary", "Peça secundária", "Secondary part"],
          ["calibration", "3 anéis de calibração", "3 calibration rings"],
        ],
      };
      options.end_b = options.end_a;
      const ranges = {
        nominal_dia: [6, 100, 0.1],
        pitch: [0.5, 10, 0.05],
        thread_length: [3, 100, 0.1],
        starts: [1, 3, 1],
        diameter: [12, 150, 0.1],
        height: [12, 200, 0.1],
        wall_thickness: [1.2, 8, 0.1],
        floor_thickness: [1.2, 8, 0.1],
        diametral_clearance: [0.05, 0.6, 0.01],
        axial_clearance: [0, 0.6, 0.01],
        higbee_turns: [0.1, 1, 0.05],
        knurl_depth: [0, 1.5, 0.1],
        knurl_count: [12, 100, 1],
        head_height: [3, 15, 0.1],
        bore_diameter: [0, 90, 0.1],
        inlet_diameter: [10, 100, 0.1],
        outlet_diameter: [10, 120, 0.1],
        adapter_length: [30, 180, 0.1],
        end_length: [7, 35, 0.1],
      };
      function text(key) {
        return words[lang][key] || key;
      }
      function optionFill(el, rows, value) {
        el.replaceChildren();
        rows.forEach((row) => {
          const opt = document.createElement("option");
          opt.value = row[0];
          opt.textContent = row[lang === "pt" ? 1 : 2];
          el.append(opt);
        });
        el.value = String(value);
      }
      function buildFields() {
        const box = $("fields");
        box.replaceChildren();
        Object.keys(labels).forEach((key) => {
          const row = document.createElement("label");
          row.className = "field";
          row.dataset.field = key;
          const title = document.createElement("span");
          title.textContent = labels[key][lang === "pt" ? 0 : 1];
          const input = document.createElement(
            options[key] ? "select" : "input",
          );
          input.dataset.key = key;
          if (options[key]) optionFill(input, options[key], params[key]);
          else if (typeof params[key] === "boolean") {
            input.type = "checkbox";
            input.checked = params[key];
          } else {
            input.type = typeof params[key] === "number" ? "number" : "text";
            input.value = params[key];
            if (ranges[key]) {
              input.min = ranges[key][0];
              input.max = ranges[key][1];
              input.step = ranges[key][2];
            } else if (input.type === "number") input.step = ".1";
          }
          input.addEventListener("change", () => {
            params[key] =
              input.type === "checkbox"
                ? input.checked
                : input.type === "number" || key === "starts"
                  ? Number(input.value)
                  : input.value;
            refreshVisibility();
            scheduleUpdate();
          });
          row.append(title, input);
          box.append(row);
        });
        refreshVisibility();
      }
      function refreshVisibility() {
        const mod = params.module,
          standard = mod === "standard_bottle_cap",
          adapter = mod === "hose_vacuum_adapter",
          bolt = mod === "bolt_nut_knob";
        document.querySelectorAll("[data-field]").forEach((row) => {
          const k = row.dataset.field;
          let show = true;
          if (["part"].includes(k)) show = standard;
          if (["diameter", "height"].includes(k))
            show = mod === "container_and_lid";
          if (["head", "head_height", "bore_diameter"].includes(k)) show = bolt;
          if (
            [
              "inlet_diameter",
              "outlet_diameter",
              "adapter_length",
              "end_length",
              "end_a",
              "end_b",
            ].includes(k)
          )
            show = adapter;
          if (k.startsWith("measured_") || k === "measurements_confirmed")
            show = standard && params.standard === "mason_86";
          row.hidden = !show;
          const input = row.querySelector("input,select");
          if (["nominal_dia", "pitch", "thread_length", "starts"].includes(k))
            input.disabled =
              standard && ["pco1881", "mason_70"].includes(params.standard);
        });
      }
      function syncFields() {
        document.querySelectorAll("[data-key]").forEach((el) => {
          if (el.type === "checkbox") el.checked = params[el.dataset.key];
          else el.value = params[el.dataset.key];
        });
        $("target").value = params.export_target;
        refreshVisibility();
      }
      function rebuildPresets() {
        const el = $("preset");
        el.replaceChildren();
        const empty = document.createElement("option");
        empty.value = "";
        empty.textContent =
          lang === "pt" ? "Selecionar projeto…" : "Choose project…";
        el.append(empty);
        builtins.forEach((p) => {
          let o = document.createElement("option");
          o.value = p.id;
          o.textContent = lang === "pt" ? p.name_pt : p.name_en;
          el.append(o);
        });
        userPresets.forEach((p) => {
          let o = document.createElement("option");
          o.value = "user:" + p.id;
          o.textContent = "★ " + p.name;
          el.append(o);
        });
      }
      function translate() {
        document.documentElement.lang = lang;
        document
          .querySelectorAll("[data-i]")
          .forEach((el) => (el.textContent = text(el.dataset.i)));
        $("language").textContent = lang === "pt" ? "EN" : "PT";
        buildFields();
        rebuildPresets();
        optionFill($("target"), options.export_target, params.export_target);
        drawLoupe();
      }
      function status(message, error = false) {
        $("status").textContent = message;
        $("status").classList.toggle("error", error);
      }
      function send(payload) {
        try {
          if (window.orca && typeof window.orca.postMessage === "function") {
            window.orca.postMessage(payload);
            return true;
          }
          if (window.chrome && window.chrome.webview) {
            window.chrome.webview.postMessage(payload);
            return true;
          }
        } catch (e) {
          status(String(e), true);
        }
        return false;
      }
      let updateTimer;
      function scheduleUpdate() {
        clearTimeout(updateTimer);
        updateTimer = setTimeout(() => {
          if (!send({ type: "update", params })) status(text("local"), true);
        }, 180);
      }
      function handleHostMessage(raw) {
        let data = raw && raw.data !== undefined ? raw.data : raw;
        if (typeof data === "string") {
          try {
            data = JSON.parse(data);
          } catch (e) {
            return;
          }
        }
        if (!data || typeof data !== "object") return;
        if (data.type === "init_state") {
          params = { ...data.params };
          userPresets = data.user_presets || userPresets;
          builtins = data.builtin_presets || builtins;
          const host = data.host || {};
          $("host").textContent = [
            host.printer_name,
            host.process_name,
            host.filament_name,
            host.bed_x &&
              `${host.bed_x} × ${host.bed_y} mm · Ø${host.nozzle_mm}`,
          ]
            .filter(Boolean)
            .join("\n");
          translate();
          return;
        }
        if (data.type === "busy") {
          status(
            data.busy
              ? lang === "pt"
                ? "Gerando malha…"
                : "Generating mesh…"
              : "",
          );
          return;
        }
        if (data.type === "presets_updated") {
          userPresets = data.user_presets;
          rebuildPresets();
          return;
        }
        if (data.type === "geometry") {
          params = { ...data.params };
          if (params.lang !== lang || document.documentElement.dataset.theme !== params.theme) {
            lang = params.lang;
            document.documentElement.dataset.theme = params.theme;
            translate();
          }
          syncFields();
          profile = data.profile;
          report = data.report;
          uploadMeshes(data.meshes || []);
          $("undo").disabled = !data.can_undo;
          $("redo").disabled = !data.can_redo;
          $("radial").textContent =
            report.radial_clearance_mm.toFixed(3) + " mm";
          $("axial").textContent =
            (lang === "pt" ? "Folga axial: " : "Axial clearance: ") +
            report.axial_clearance_mm.toFixed(3) +
            " mm";
          $("lead").textContent = report.lead_mm.toFixed(2) + " mm";
          $("check").textContent = report.interference
            ? "INTERFERENCE"
            : text("clear");
          $("warning").hidden = !(data.warning || report.experimental);
          $("warning").textContent = data.warning || text("experimental");
          $("hud").textContent = meshes
            .map(
              (m) =>
                `${m.name} · ${(m.indices.length / 3).toLocaleString()} △ · ${m.volume.toFixed(2)} cm³`,
            )
            .join("\n");
          if (params.export_target === "calibration") status(text("notch"));
          drawLoupe();
          return;
        }
        if (data.type === "action_result") {
          status(
            (data.message || "") +
              (data.paths && data.paths.length
                ? "\n" + data.paths.join("\n")
                : ""),
            data.ok === false,
          );
        }
      }
      window.handleHostMessage = handleHostMessage;
      window.addEventListener("message", handleHostMessage);
      if (window.chrome && window.chrome.webview)
        window.chrome.webview.addEventListener("message", handleHostMessage);
      if (window.orca && typeof window.orca.onMessage === "function")
        window.orca.onMessage(handleHostMessage);
      const canvas = $("viewport"),
        gl = canvas.getContext("webgl2", { antialias: true, alpha: false });
      let program,
        loc = {};
      function shader(type, code) {
        const s = gl.createShader(type);
        gl.shaderSource(s, code);
        gl.compileShader(s);
        if (!gl.getShaderParameter(s, gl.COMPILE_STATUS))
          throw Error(gl.getShaderInfoLog(s));
        return s;
      }
      if (gl) {
        try {
          program = gl.createProgram();
          gl.attachShader(
            program,
            shader(
              gl.VERTEX_SHADER,
              `#version 300 es
precision highp float;in vec3 aPosition;uniform vec3 center;uniform vec3 offset;uniform float scale;uniform float aspect;uniform float yaw;uniform float pitch;uniform float spin;uniform bool invert;out vec3 world;out vec3 eye;void main(){vec3 p=aPosition;if(invert)p.yz=-p.yz;float cs=cos(spin),sn=sin(spin);p.xy=mat2(cs,sn,-sn,cs)*p.xy;p+=offset;world=p; p=(p-center)*scale;float cy=cos(yaw),sy=sin(yaw),cp=cos(pitch),sp=sin(pitch);p.xy=mat2(cy,sy,-sy,cy)*p.xy;vec3 e=vec3(p.x,cp*p.z-sp*p.y,sp*p.z+cp*p.y);eye=e;gl_Position=vec4(e.x/aspect,e.y,e.z*.12,1.);}`,
            ),
          );
          gl.attachShader(
            program,
            shader(
              gl.FRAGMENT_SHADER,
              `#version 300 es
precision highp float;in vec3 world;in vec3 eye;uniform vec3 color;uniform bool clipping;out vec4 frag;void main(){if(clipping&&world.y<0.)discard;vec3 normal=normalize(cross(dFdx(eye),dFdy(eye)));float light=.38+.62*abs(dot(normal,normalize(vec3(-.5,.7,1.))));frag=vec4(color*light,1.);}`,
            ),
          );
          gl.linkProgram(program);
          if (!gl.getProgramParameter(program, gl.LINK_STATUS))
            throw Error(gl.getProgramInfoLog(program));
          gl.useProgram(program);
          [
            "center",
            "offset",
            "scale",
            "aspect",
            "yaw",
            "pitch",
            "spin",
            "invert",
            "color",
            "clipping",
          ].forEach((k) => (loc[k] = gl.getUniformLocation(program, k)));
          loc.position = gl.getAttribLocation(program, "aPosition");
          gl.enable(gl.DEPTH_TEST);
        } catch (e) {
          status(String(e), true);
        }
      } else status("WebGL2 unavailable", true);
      function uploadMeshes(raw) {
        meshes.forEach((m) => {
          if (gl) {
            gl.deleteBuffer(m.vertex);
            gl.deleteBuffer(m.index);
          }
        });
        meshes = raw.map((m) => {
          let vertices = new Float32Array(m.vertices),
            indices = new Uint32Array(m.triangles),
            vertex,
            index;
          if (gl) {
            vertex = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, vertex);
            gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
            index = gl.createBuffer();
            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, index);
            gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);
          }
          return {
            name: m.name,
            vertices,
            indices,
            vertex,
            index,
            volume: m.volume_cm3,
            bounds: m.bounds,
          };
        });
      }
      function draw(now) {
        requestAnimationFrame(draw);
        if (!gl || !program) return;
        const rect = canvas.getBoundingClientRect(),
          dpr = Math.min(window.devicePixelRatio || 1, 2),
          w = Math.max(1, Math.round(rect.width * dpr)),
          h = Math.max(1, Math.round(rect.height * dpr));
        if (canvas.width !== w || canvas.height !== h) {
          canvas.width = w;
          canvas.height = h;
        }
        gl.viewport(0, 0, w, h);
        const light = document.documentElement.dataset.theme === "light";
        gl.clearColor(
          ...(light ? [0.83, 0.87, 0.92, 1] : [0.08, 0.1, 0.13, 1]),
        );
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
        if (!meshes.length) return;
        const dt = Math.min(0.05, (now - frameTime) / 1000 || 0);
        frameTime = now;
        if (animating) {
          spin = (spin + dt * 0.7) % (Math.PI * 4);
          drawLoupe();
        }
        let dia = Math.max(
            ...meshes.map((m) => Math.max(m.bounds.size[0], m.bounds.size[1])),
          ),
          top = Math.max(...meshes.map((m) => m.bounds.size[2])),
          pair =
            meshes.length === 2 &&
            params.export_target === "all" &&
            ["container_and_lid", "bolt_nut_knob"].includes(params.module);
        if (pair)
          top += params.thread_length + opening + params.floor_thickness + 15;
        const radialKit = params.export_target === "calibration",
          extent = radialKit ? dia * 3.5 : dia * 1.5,
          size = Math.max(top, extent);
        gl.uniform3f(loc.center, 0, 0, top * 0.48);
        gl.uniform1f(loc.scale, (1.65 * zoom) / size);
        gl.uniform1f(loc.aspect, w / h);
        gl.uniform1f(loc.yaw, yaw);
        gl.uniform1f(loc.pitch, pitch);
        gl.uniform1i(loc.clipping, cut);
        meshes.forEach((m, i) => {
          gl.bindBuffer(gl.ARRAY_BUFFER, m.vertex);
          gl.enableVertexAttribArray(loc.position);
          gl.vertexAttribPointer(loc.position, 3, gl.FLOAT, false, 0, 0);
          gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, m.index);
          let z = 0,
            x = 0,
            invert = false,
            rotation = 0;
          if (pair && i === 1) {
            invert = true;
            rotation = spin * (params.hand === "left" ? -1 : 1);
            z =
              (params.module === "container_and_lid"
                ? params.height + params.floor_thickness
                : params.head_height + params.thread_length) +
              opening +
              (spin / (2 * Math.PI)) * params.lead;
          } else if (meshes.length > 1 && !pair)
            x = (i - (meshes.length - 1) / 2) * dia * 1.15;
          gl.uniform3f(loc.offset, x, 0, z);
          gl.uniform1f(loc.spin, rotation);
          gl.uniform1i(loc.invert, invert);
          gl.uniform3f(
            loc.color,
            ...(i === 1 ? [0.98, 0.64, 0.26] : [0.0, 0.72, 0.61]),
          );
          gl.drawElements(gl.TRIANGLES, m.indices.length, gl.UNSIGNED_INT, 0);
        });
      }
      function radialProfile(q, female) {
        const p = params,
          phase = q / p.pitch,
          signed = ((((phase + 0.5) % 1) + 1) % 1) - 0.5;
        let depth =
          p.standard === "pco1881"
            ? 1.6
            : p.standard === "mason_86" && p.measurements_confirmed
              ? (p.measured_major_dia - p.measured_root_dia) / 2
              : Math.min(
                  p.nominal_dia * 0.12,
                  p.pitch * (p.standard === "iso_metric" ? 0.61343 : 0.375),
                );
        const widen = female ? p.axial_clearance / p.pitch / 2 : 0;
        function tooth(v) {
          const q = ((((v + 0.5) % 1) + 1) % 1) - 0.5;
          if (p.standard === "pco1881")
            return q < -0.12
              ? Math.max(0, Math.min(1, (q + 0.31) / 0.19))
              : q > 0.1
                ? Math.max(0, Math.min(1, (0.3 - q) / 0.2))
                : 1;
          const crest = p.standard === "iso_metric" ? 0.0625 : 0.125,
            root =
              p.standard === "iso_metric"
                ? 0.0625 + 0.61343 / Math.sqrt(3)
                : 0.5;
          return Math.max(
            0,
            Math.min(
              1,
              (root - Math.max(0, Math.abs(q) - widen)) / (root - crest),
            ),
          );
        }
        let f = tooth(phase);
        if (female && p.standard === "pco1881")
          for (let j = 0; j < 9; j++)
            f = Math.max(f, tooth(phase - widen + (2 * widen * j) / 8));
        const u = Math.max(
            0,
            Math.min(
              1,
              Math.min(q, p.thread_length - q) / (p.lead * p.higbee_turns),
            ),
          ),
          envelope = u * u * (3 - 2 * u);
        return (
          p.nominal_dia / 2 -
          depth +
          depth * f * (female ? 1 : envelope) +
          (female ? p.diametral_clearance / 2 : 0)
        );
      }
      function drawLoupe() {
        const c = $("loupe"),
          rect = c.getBoundingClientRect(),
          dpr = window.devicePixelRatio || 1;
        c.width = Math.max(1, rect.width * dpr);
        c.height = Math.max(1, rect.height * dpr);
        const ctx = c.getContext("2d");
        ctx.scale(dpr, dpr);
        const w = rect.width,
          h = rect.height;
        ctx.clearRect(0, 0, w, h);
        if (!profile) return;
        const center = params.thread_length / 2,
          minimum = Math.max(0, center - params.pitch),
          maximum = Math.min(params.thread_length, center + params.pitch),
          z = [],
          male = [],
          female = [],
          advance = (spin / (2 * Math.PI)) * params.lead;
        let interference = false,
          engaged = 0;
        for (let j = 0; j <= 240; j++) {
          const q = minimum + ((maximum - minimum) * j) / 240;
          z.push(q);
          male.push(radialProfile(q, false));
          const local = q - opening - advance;
          female.push(
            local >= 0 && local <= params.thread_length
              ? radialProfile(q - opening, true)
              : null,
          );
          if (female.at(-1) !== null) {
            engaged++;
            if (female.at(-1) < male.at(-1) - 1e-6) interference = true;
          }
        }
        const all = male.concat(female.filter((v) => v !== null)),
          lo = Math.min(...all) - 0.3,
          hi = Math.max(...all) + 0.3;
        const point = (i, values) => [
          15 + ((w - 30) * (z[i] - minimum)) / (maximum - minimum),
          h - 20 - ((h - 35) * (values[i] - lo)) / (hi - lo),
        ];
        ctx.strokeStyle = getComputedStyle(
          document.documentElement,
        ).getPropertyValue("--line");
        ctx.lineWidth = 1;
        for (let x = 20; x < w; x += 25) {
          ctx.beginPath();
          ctx.moveTo(x, 10);
          ctx.lineTo(x, h - 15);
          ctx.stroke();
        }
        [
          [male, "#00bfa5"],
          [female, interference ? "#ff6868" : "#ffb74d"],
        ].forEach(([values, color]) => {
          ctx.beginPath();
          let started = false;
          values.forEach((v, i) => {
            if (v === null) {
              started = false;
              return;
            }
            const q = point(i, values);
            started ? ctx.lineTo(...q) : ctx.moveTo(...q);
            started = true;
          });
          ctx.strokeStyle = color;
          ctx.lineWidth = 2;
          ctx.stroke();
        });
        ctx.fillStyle = getComputedStyle(
          document.documentElement,
        ).getPropertyValue("--muted");
        ctx.font = "10px Consolas";
        ctx.fillText(
          `z · ${params.pitch.toFixed(2)} mm     cᵣ = ${(params.diametral_clearance / 2).toFixed(3)} · cₐ = ${params.axial_clearance.toFixed(3)} mm`,
          15,
          h - 3,
        );
        $("check").textContent = interference
          ? lang === "pt"
            ? "Interferência nesta posição"
            : "Interference at this position"
          : engaged
            ? text("clear")
            : lang === "pt"
              ? "Tampa fora da região de engate"
              : "Lid outside engagement region";
      }
      canvas.addEventListener("pointerdown", (e) => {
        drag = [e.clientX, e.clientY];
        canvas.setPointerCapture(e.pointerId);
      });
      canvas.addEventListener("pointermove", (e) => {
        if (!drag) return;
        yaw += (e.clientX - drag[0]) * 0.008;
        pitch = Math.max(
          -1.4,
          Math.min(1.4, pitch + (e.clientY - drag[1]) * 0.008),
        );
        drag = [e.clientX, e.clientY];
      });
      canvas.addEventListener("pointerup", () => (drag = null));
      canvas.addEventListener(
        "wheel",
        (e) => {
          e.preventDefault();
          zoom = Math.max(0.3, Math.min(4, zoom * Math.exp(-e.deltaY * 0.001)));
        },
        { passive: false },
      );
      $("fit").onclick = () => {
        yaw = -0.65;
        pitch = -0.5;
        zoom = 1;
        spin = 0;
      };
      $("cut").onclick = () => {
        cut = !cut;
        $("cut").setAttribute("aria-pressed", cut);
      };
      $("animate").onclick = () => {
        animating = !animating;
        $("animate").setAttribute("aria-pressed", animating);
      };
      $("explode").oninput = (e) => {
        opening = Number(e.target.value);
        drawLoupe();
      };
      $("reset").onclick = () => send({ type: "reset" });
      $("undo").onclick = () => send({ type: "undo" });
      $("redo").onclick = () => send({ type: "redo" });
      $("theme").onclick = () => {
        document.documentElement.dataset.theme =
          document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        params.theme = document.documentElement.dataset.theme;
        drawLoupe();
        scheduleUpdate();
      };
      $("language").onclick = () => {
        lang = lang === "pt" ? "en" : "pt";
        params.lang = lang;
        translate();
        scheduleUpdate();
      };
      $("preset").onchange = (e) => {
        let value = e.target.value;
        let preset = value.startsWith("user:")
          ? userPresets.find((p) => p.id === value.slice(5))
          : builtins.find((p) => p.id === value);
        if (preset) {
          params = { ...preset.params };
          syncFields();
          scheduleUpdate();
        }
      };
      $("save").onclick = () => {
        const name = window.prompt(
          lang === "pt" ? "Nome do preset" : "Preset name",
          params.name,
        );
        if (name) send({ type: "preset_save", name, params });
      };
      $("remove").onclick = () => {
        const value = $("preset").value;
        if (value.startsWith("user:"))
          send({ type: "preset_delete", id: value.slice(5) });
      };
      $("target").onchange = (e) => {
        params.export_target = e.target.value;
        scheduleUpdate();
      };
      $("stl").onclick = () =>
        send({ type: "export_file", params, format: "stl" });
      $("three").onclick = () =>
        send({ type: "export_file", params, format: "3mf" });
      $("send").onclick = () =>
        send({ type: "send_to_plater", params, format: "3mf" });
      $("folder").onclick = () => send({ type: "open_exports" });
      document.querySelectorAll("[data-view]").forEach(
        (el) =>
          (el.onclick = () => {
            document.querySelector("main").dataset.tab = el.dataset.view;
            document
              .querySelectorAll("[data-view]")
              .forEach((e) => e.classList.toggle("active", e === el));
            drawLoupe();
          }),
      );
      window.addEventListener("resize", () => {
        document.body.classList.toggle("compact", MODE === "dock" || window.innerWidth < 760);
        drawLoupe();
      });
      if (MODE === "dock" || window.innerWidth < 760)
        document.body.classList.add("compact");
      document.documentElement.dataset.theme =
        INITIAL.theme === "light" ? "light" : "dark";
      translate();
      status(text("waiting"));
      requestAnimationFrame(draw);
      if (!send({ type: "ready", mode: MODE })) status(text("local"), true);
    </script>
  </body>
</html>
"""

# ===========================================================================
# MODULE: thread_studio.linux_ipc
# ===========================================================================

"""OrcaSlicer session-bus transport. No subprocess or third-party package.

Protocol reference: OrcaSlicer v2.5.1 src/slic3r/GUI/InstanceCheck.cpp.
Transport completion does not confirm the host has loaded the objects.
"""

pass  # [bundled] hoisted __future__ import

import ctypes
import os
import re
import sys


def send_linux_plater_request(
    payload: str, *, process_id: int | None = None
) -> tuple[bool, str]:
    """Send only to the Orca instance hosted in this process (or explicit PID)."""
    if not sys.platform.startswith("linux"):
        return False, "Linux session D-Bus transport is unavailable on this platform."
    if not isinstance(payload, str) or not payload or "\x00" in payload:
        return False, "The import request must be a nonempty string without NUL."
    connection = None
    library = None
    try:
        library = ctypes.CDLL("libdbus-1.so.3")
        pointer = ctypes.c_void_p
        string = ctypes.c_char_p
        uint = ctypes.c_uint32
        signatures = {
            "dbus_threads_init_default": (ctypes.c_int, []),
            "dbus_bus_get_private": (pointer, [ctypes.c_int, pointer]),
            "dbus_connection_set_exit_on_disconnect": (None, [pointer, ctypes.c_int]),
            "dbus_message_new_method_call": (pointer, [string, string, string, string]),
            "dbus_message_append_args": (ctypes.c_int, [pointer, ctypes.c_int]),
            "dbus_message_get_args": (ctypes.c_int, [pointer, pointer, ctypes.c_int]),
            "dbus_connection_send_with_reply_and_block": (
                pointer,
                [pointer, pointer, ctypes.c_int, pointer],
            ),
            "dbus_message_get_type": (ctypes.c_int, [pointer]),
            "dbus_message_set_no_reply": (None, [pointer, ctypes.c_int]),
            "dbus_message_set_auto_start": (None, [pointer, ctypes.c_int]),
            "dbus_connection_send": (
                ctypes.c_int,
                [pointer, pointer, ctypes.POINTER(uint)],
            ),
            "dbus_connection_flush": (None, [pointer]),
            "dbus_connection_get_is_connected": (ctypes.c_int, [pointer]),
            "dbus_message_unref": (None, [pointer]),
            "dbus_connection_close": (None, [pointer]),
            "dbus_connection_unref": (None, [pointer]),
            "dbus_free_string_array": (None, [ctypes.POINTER(string)]),
        }
        for name, (result, arguments) in signatures.items():
            function = getattr(library, name)
            function.restype = result
            function.argtypes = arguments
        if not library.dbus_threads_init_default():
            return False, "Unable to initialize D-Bus threading."
        connection = library.dbus_bus_get_private(0, None)
        if not connection:
            return False, "No usable session D-Bus connection; export a 3MF instead."
        library.dbus_connection_set_exit_on_disconnect(connection, 0)

        def daemon_call(method: bytes, argument: str | None = None):
            request = library.dbus_message_new_method_call(
                b"org.freedesktop.DBus",
                b"/org/freedesktop/DBus",
                b"org.freedesktop.DBus",
                method,
            )
            if not request:
                raise RuntimeError("Cannot allocate D-Bus request.")
            try:
                if argument is not None:
                    encoded = string(argument.encode("utf-8"))
                    if not library.dbus_message_append_args(
                        request, ord("s"), ctypes.byref(encoded), ctypes.c_int(0)
                    ):
                        raise RuntimeError("Cannot encode D-Bus request.")
                reply = library.dbus_connection_send_with_reply_and_block(
                    connection, request, 1500, None
                )
                if not reply:
                    raise RuntimeError("D-Bus daemon request timed out or failed.")
                if library.dbus_message_get_type(reply) != 2:
                    library.dbus_message_unref(reply)
                    raise RuntimeError("D-Bus daemon rejected the request.")
                return reply
            finally:
                library.dbus_message_unref(request)

        reply = daemon_call(b"ListNames")
        names = ctypes.POINTER(string)()
        count = ctypes.c_int()
        try:
            if not library.dbus_message_get_args(
                reply,
                None,
                ord("a"),
                ctypes.c_int(ord("s")),
                ctypes.byref(names),
                ctypes.byref(count),
                ctypes.c_int(0),
            ):
                raise RuntimeError("Invalid D-Bus service listing.")
            candidates = [names[i].decode("utf-8") for i in range(count.value)]
        finally:
            if names:
                library.dbus_free_string_array(names)
            library.dbus_message_unref(reply)
        expected_pid = os.getpid() if process_id is None else int(process_id)
        owned = []
        for name in candidates:
            if not re.fullmatch(
                r"com\.orcaslicer\.OrcaSlicer\.InstanceCheck\.Object[0-9]+", name
            ):
                continue
            try:
                reply = daemon_call(b"GetNameOwner", name)
                unique_owner = string()
                try:
                    valid = library.dbus_message_get_args(
                        reply,
                        None,
                        ord("s"),
                        ctypes.byref(unique_owner),
                        ctypes.c_int(0),
                    )
                    if not valid or not unique_owner.value:
                        continue
                    owner = unique_owner.value.decode("utf-8")
                finally:
                    library.dbus_message_unref(reply)
                reply = daemon_call(b"GetConnectionUnixProcessID", owner)
            except RuntimeError:
                continue
            pid = uint()
            try:
                valid = library.dbus_message_get_args(
                    reply, None, ord("u"), ctypes.byref(pid), ctypes.c_int(0)
                )
                if valid and pid.value == expected_pid:
                    owned.append((name, owner))
            finally:
                library.dbus_message_unref(reply)
        if len(owned) != 1:
            return (
                False,
                "Unable to identify exactly one OrcaSlicer service for this process; export a 3MF instead.",
            )
        interface, destination = owned[0]
        suffix = interface.rsplit("Object", 1)[1]
        request = library.dbus_message_new_method_call(
            destination.encode("ascii"),
            ("/com/orcaslicer/OrcaSlicer/InstanceCheck/Object" + suffix).encode(
                "ascii"
            ),
            interface.encode("ascii"),
            b"AnotherInstance",
        )
        if not request:
            return False, "Unable to allocate the import request."
        try:
            encoded = string(payload.encode("utf-8"))
            if not library.dbus_message_append_args(
                request, ord("s"), ctypes.byref(encoded), ctypes.c_int(0)
            ):
                return False, "Unable to encode the import request."
            library.dbus_message_set_no_reply(request, 1)
            library.dbus_message_set_auto_start(request, 0)
            serial = uint()
            if not library.dbus_connection_send(
                connection, request, ctypes.byref(serial)
            ):
                return False, "D-Bus could not queue the import request."
            library.dbus_connection_flush(connection)
            if not library.dbus_connection_get_is_connected(connection):
                return False, "D-Bus disconnected while sending the import request."
            return True, "Import request sent; object loading has not been confirmed."
        finally:
            library.dbus_message_unref(request)
    except (OSError, AttributeError, RuntimeError, ValueError) as error:
        return False, "Linux import unavailable: " + str(error)
    finally:
        if connection and library is not None:
            library.dbus_connection_close(connection)
            library.dbus_connection_unref(connection)

# ===========================================================================
# MODULE: thread_studio.plugin_main
# ===========================================================================

pass  # [bundled] hoisted __future__ import

from collections.abc import Sequence
import copy
import ctypes
import json
import locale
import os
import re
import sys
import threading
import time
import types
import uuid
from pathlib import Path
from typing import Any, Callable

pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
import numpy as np


def _build_fallback_orca_module() -> types.ModuleType:
    """Create a lightweight stand-in when imported outside OrcaSlicer."""
    mod = types.ModuleType("orca")
    mod._registered_capabilities = []
    mod._requested_permissions = {}
    mod._plugin_cls = None

    class PythonPluginBase:
        def __init__(self) -> None:
            self._stored_config: str = "{}"

        def get_name(self) -> str:
            return ""

        def on_load(self) -> None:
            pass

        def on_unload(self) -> None:
            pass

        def has_config_ui(self) -> bool:
            return False

        def get_config_ui(self) -> str:
            return ""

        def get_default_config(self) -> dict[str, Any]:
            return {}

        def get_config(self) -> str:
            return self._stored_config

        def get_config_version(self) -> str:
            return "1.0.0"

        def save_config(self, config: str) -> bool:
            self._stored_config = str(config or "{}")
            return True

    class BasePlugin:
        def __init__(self) -> None:
            pass

        def register_capabilities(self) -> None:
            pass

    class PagesPluginCapabilityBase(PythonPluginBase):
        def get_ui(self) -> str:
            return ""

        def get_icon(self) -> str:
            return ""

        def on_message(self, data: Any) -> None:
            pass

        def post_message(self, data: Any) -> None:
            pass

    class ScriptPluginCapabilityBase(PythonPluginBase):
        def execute(self) -> Any:
            return None

    class PluginResult:
        Success = 0
        Skipped = 1
        RecoverableError = 2
        FatalError = 3

    class ExecutionResult:
        def __init__(self, status: int = 0, message: str = "", data: str = "") -> None:
            self.status = status
            self.message = message
            self.data = data

        @classmethod
        def success(cls, message: str = "", data: str = "") -> "ExecutionResult":
            return cls(PluginResult.Success, message, data)

        @classmethod
        def skipped(cls, message: str = "") -> "ExecutionResult":
            return cls(PluginResult.Skipped, message, "")

        @classmethod
        def failure(
            cls, status: int, message: str, data: str = ""
        ) -> "ExecutionResult":
            return cls(status, message, data)

    def plugin_decorator(cls: type) -> type:
        mod._plugin_cls = cls
        return cls

    def register_capability(cap_cls: type) -> None:
        mod._registered_capabilities.append(cap_cls)

    def request_permissions(**kwargs: Any) -> None:
        mod._requested_permissions.update(kwargs)

    pages_mod = types.ModuleType("orca.pages")
    pages_mod.PagesPluginCapabilityBase = PagesPluginCapabilityBase

    script_mod = types.ModuleType("orca.script")
    script_mod.ScriptPluginCapabilityBase = ScriptPluginCapabilityBase

    plugin_sub = types.ModuleType("orca.plugin")
    plugin_sub.storage = lambda: str(
        _orca_user_config_root() / "plugin_data" / "orca_thread_generator"
    )

    class NotificationLevel:
        RegularNotificationLevel = 0
        HintNotificationLevel = 1
        ProgressBarNotificationLevel = 2
        PrintInfoNotificationLevel = 3
        PrintInfoShortNotificationLevel = 4
        ImportantNotificationLevel = 5
        WarningNotificationLevel = 6
        SeriousWarningNotificationLevel = 7
        ErrorNotificationLevel = 8

    host_mod = types.ModuleType("orca.host")
    host_mod.app_language = lambda: "pt_BR"
    host_mod.app_info = lambda: {"version": "2.5.1", "language": "pt_BR"}
    host_mod.preset_bundle = lambda: None
    host_mod.plater = lambda: None
    host_mod.model = lambda: None
    host_mod.selected_printer = lambda: None
    host_mod.plugin = plugin_sub
    host_mod.ui = types.SimpleNamespace(
        NotificationLevel=NotificationLevel,
        create_dock_panel=None,
        create_window=None,
        push_notification=None,
        message=None,
    )
    host_mod.preset = types.SimpleNamespace(
        process=None,
        printer=None,
        filament=None,
    )

    mod.base = BasePlugin
    mod.PythonPluginBase = PythonPluginBase
    mod.PluginResult = PluginResult
    mod.ExecutionResult = ExecutionResult
    mod.plugin = plugin_decorator
    mod.register_capability = register_capability
    mod.request_permissions = request_permissions
    mod.pages = pages_mod
    mod.script = script_mod
    mod.host = host_mod

    return mod


try:
    import orca  # type: ignore[import-not-found]
except ImportError:
    orca = _build_fallback_orca_module()


PLUGIN_SLUG = "orca_thread_generator"
WM_COPYDATA = 0x004A
SMTO_ABORTIFHUNG = 0x0002
ORCA_OTHER_INSTANCE_DWDATA = 1

ICON_SVG_CONTENT = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64"><defs><linearGradient id="thread" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#80ffea"/><stop offset="1" stop-color="#00897b"/></linearGradient></defs><ellipse cx="32" cy="55" rx="25" ry="5" fill="none" stroke="#00bfa5" opacity=".5"/><path d="M18 17l14-7 14 7v29l-14 8-14-8z" fill="#17252b" stroke="url(#thread)" stroke-width="2"/><path d="M19 23l26-9m-26 16l26-9m-26 16l26-9m-26 16l26-9m-26 16l26-9" fill="none" stroke="url(#thread)" stroke-width="4" stroke-linejoin="round"/><path d="M27 7h10v8H27z" fill="#ffb74d"/></svg>'

# ---------------------------------------------------------------------------
# Cross-Platform Environment, Storage & In-Process Plater IPC (Win32 + macOS)
# ---------------------------------------------------------------------------

_MACOS_PENDING_DISPATCH_CBS: list[Any] = []


def _is_native_orca_host() -> bool:
    """Return True only when running inside the real C++ pybind11 OrcaSlicer host."""
    base_cls = getattr(orca, "base", None)
    return base_cls is not None and type(base_cls).__name__ == "pybind11_type"


def _is_mock_callable(obj: Any) -> bool:
    """Detect unittest.mock objects without importing unittest.mock eagerly."""
    cls_mod = getattr(type(obj), "__module__", "")
    return cls_mod.startswith("unittest.mock")


def _orca_user_config_root(platform_name: str | None = None) -> Path:
    """Return OrcaSlicer's user configuration directory on Windows, macOS, and Linux."""
    plat = platform_name or sys.platform
    if plat == "win32":
        appdata = os.environ.get("APPDATA", "").strip()
        if appdata:
            return Path(appdata) / "OrcaSlicer"
        return Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    if plat == "darwin":
        return Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    xdg = os.environ.get("XDG_CONFIG_HOME", "").strip()
    base = Path(xdg) if xdg else (Path.home() / ".config")
    return base / "OrcaSlicer"


def _default_installed_plugin_dir() -> Path:
    return _orca_user_config_root() / "orca_plugins" / PLUGIN_SLUG


def _default_plugin_data_dir() -> Path:
    return _orca_user_config_root() / "orca_plugins" / "plugin_data" / PLUGIN_SLUG


def _resolve_storage_dir() -> Path:
    """Resolve current plugin storage folder safely (inside or outside callbacks)."""
    # 1. Try orca.plugin.storage() or orca.host.plugin.storage()
    for holder in (
        getattr(orca, "plugin", None),
        getattr(getattr(orca, "host", None), "plugin", None),
    ):
        storage_fn = getattr(holder, "storage", None)
        if callable(storage_fn):
            try:
                raw = storage_fn()
                if isinstance(raw, (str, os.PathLike)) and str(raw).strip():
                    return Path(raw)
            except Exception:
                pass

    # 2. In native OrcaSlicer, prefer `plugin_data/orca_thread_generator`
    if _is_native_orca_host():
        data_dir = _default_plugin_data_dir()
        try:
            data_dir.mkdir(parents=True, exist_ok=True)
            return data_dir
        except Exception:
            pass

    # 3. Fallback to __file__ parent if available
    try:
        here = Path(__file__).resolve().parent
        if here.exists():
            return here
    except Exception:
        pass

    return _default_installed_plugin_dir()


def _format_other_instance_payload(file_paths: Sequence[str | Path]) -> str:
    """Format Win32 `WM_COPYDATA` payload matching `OrcaSlicer.dll` `unescape_strings_cstyle`.

    Produces `"orca-slicer.exe";"<resolved_path_1>";...` where every token escapes
    `\\` -> `\\\\`, `"` -> `\\"`, `\\r` -> `\\r`, `\\n` -> `\\n`, wrapped in double quotes and
    joined by `;` with NO trailing `;` (`OtherInstanceMessageHandler::handle_message` skips `args[0]`).
    """
    resolved_files = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved_files:
        raise ValueError("file_paths must contain at least one model path")

    tokens = ["orca-slicer.exe", *resolved_files]
    escaped: list[str] = []
    for tok in tokens:
        s = (
            tok.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\r", "\\r")
            .replace("\n", "\\n")
        )
        escaped.append(f'"{s}"')
    return ";".join(escaped)


def _find_orca_mainframe_hwnd(target_pid: int | None = None) -> int | None:
    """Locate OrcaSlicer's `MainFrame` `wxWindowNR` `HWND` in `target_pid` (`os.getpid()` by default).

    Prefers `wxWindowNR` windows marked with OrcaSlicer's `Instance_Hash_Minor` or
    `Instance_Hash_Major` properties, falling back to a visible top-level `wxWindowNR` of that PID.
    """
    if sys.platform != "win32":
        return None

    from ctypes import wintypes

    pid = int(target_pid) if target_pid is not None else os.getpid()
    user32 = ctypes.windll.user32

    WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    enum_windows = user32.EnumWindows
    if not _is_mock_callable(enum_windows):
        enum_windows.argtypes = [WNDENUMPROC, wintypes.LPARAM]
        enum_windows.restype = wintypes.BOOL

    get_pid = user32.GetWindowThreadProcessId
    if not _is_mock_callable(get_pid):
        get_pid.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
        get_pid.restype = wintypes.DWORD

    get_class = user32.GetClassNameW
    if not _is_mock_callable(get_class):
        get_class.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
        get_class.restype = ctypes.c_int

    get_prop = user32.GetPropW
    if not _is_mock_callable(get_prop):
        get_prop.argtypes = [wintypes.HWND, wintypes.LPCWSTR]
        get_prop.restype = wintypes.HANDLE

    is_visible = user32.IsWindowVisible
    if not _is_mock_callable(is_visible):
        is_visible.argtypes = [wintypes.HWND]
        is_visible.restype = wintypes.BOOL

    get_parent = user32.GetParent
    if not _is_mock_callable(get_parent):
        get_parent.argtypes = [wintypes.HWND]
        get_parent.restype = wintypes.HWND

    hash_visible: list[int] = []
    hash_any: list[int] = []
    fallback_visible: list[int] = []

    def _enum_cb(hwnd: int, _lparam: int) -> bool:
        if not hwnd:
            return True
        win_pid = wintypes.DWORD(0)
        get_pid(hwnd, ctypes.byref(win_pid))
        if int(win_pid.value) != pid:
            return True

        cls_buf = ctypes.create_unicode_buffer(64)
        cls_len = get_class(hwnd, cls_buf, 64)
        if cls_len <= 0 or cls_buf.value != "wxWindowNR":
            return True

        minor = get_prop(hwnd, "Instance_Hash_Minor")
        major = get_prop(hwnd, "Instance_Hash_Major")
        vis = bool(is_visible(hwnd))
        hwnd_int = int(hwnd)

        if bool(minor) or bool(major):
            if vis:
                hash_visible.append(hwnd_int)
            else:
                hash_any.append(hwnd_int)
        elif vis and not get_parent(hwnd):
            fallback_visible.append(hwnd_int)
        return True

    cb_ref = WNDENUMPROC(_enum_cb)
    enum_windows(cb_ref, 0)

    if hash_visible:
        return hash_visible[0]
    if hash_any:
        return hash_any[0]
    if fallback_visible:
        return fallback_visible[0]
    return None


class _COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ("dwData", ctypes.c_size_t),
        ("cbData", ctypes.c_uint32),
        ("lpData", ctypes.c_void_p),
    ]


def _dispatch_copydata_to_hwnd(
    hwnd: int,
    payload_str: str,
    timeout_ms: int = 5000,
) -> tuple[bool, str]:
    """Send UTF-16LE `WM_COPYDATA` (`dwData = 1`) to `hwnd` via `SendMessageTimeoutW` (`0x0002`)."""
    if not hwnd or int(hwnd) <= 0:
        return (False, "OrcaSlicer MainFrame HWND not found")
    if not payload_str:
        return (False, "Empty WM_COPYDATA payload")
    if sys.platform != "win32":
        return (False, "WM_COPYDATA requires win32")

    from ctypes import wintypes

    wchar_buf = ctypes.create_unicode_buffer(payload_str)
    cds = _COPYDATASTRUCT(
        dwData=ORCA_OTHER_INSTANCE_DWDATA,
        cbData=ctypes.sizeof(wchar_buf),
        lpData=ctypes.cast(wchar_buf, ctypes.c_void_p),
    )
    result = ctypes.c_size_t(0)

    user32 = ctypes.windll.user32
    send_msg = user32.SendMessageTimeoutW
    if not _is_mock_callable(send_msg):
        send_msg.argtypes = [
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            ctypes.c_void_p,
            wintypes.UINT,
            wintypes.UINT,
            ctypes.POINTER(ctypes.c_size_t),
        ]
        send_msg.restype = ctypes.c_size_t

    ret = send_msg(
        int(hwnd),
        WM_COPYDATA,
        0,
        ctypes.byref(cds),
        SMTO_ABORTIFHUNG,
        max(100, int(timeout_ms)),
        ctypes.byref(result),
    )
    if not ret:
        err = ctypes.windll.kernel32.GetLastError()
        return (False, f"SendMessageTimeoutW failed (GetLastError={err})")
    return (True, "ok")


class _MacDispatchQueueS(ctypes.Structure):
    pass


def _load_macos_objc_and_gcd() -> tuple[Any, Any]:
    """Load Objective-C runtime (`libobjc`) and GCD (`libSystem`) on macOS (`arm64` & `x86_64`)."""
    for fw in (
        "/System/Library/Frameworks/Foundation.framework/Foundation",
        "/System/Library/Frameworks/AppKit.framework/AppKit",
    ):
        try:
            ctypes.CDLL(fw)
        except OSError:
            pass

    objc = None
    for cand in ("/usr/lib/libobjc.A.dylib", "libobjc.A.dylib", "libobjc.dylib"):
        try:
            objc = ctypes.CDLL(cand)
            break
        except OSError:
            continue
    if objc is None:
        raise RuntimeError("Could not load macOS libobjc.A.dylib")

    libsystem = None
    for cand in ("/usr/lib/libSystem.B.dylib", "libSystem.B.dylib", "libSystem.dylib"):
        try:
            libsystem = ctypes.CDLL(cand)
            break
        except OSError:
            continue
    if libsystem is None:
        raise RuntimeError("Could not load macOS libSystem.B.dylib")

    if not _is_mock_callable(objc.objc_getClass):
        objc.objc_getClass.argtypes = [ctypes.c_char_p]
        objc.objc_getClass.restype = ctypes.c_void_p
    if not _is_mock_callable(objc.sel_registerName):
        objc.sel_registerName.argtypes = [ctypes.c_char_p]
        objc.sel_registerName.restype = ctypes.c_void_p

    return objc, libsystem


def _resolve_macos_app_bundle_path() -> str | None:
    """Find running `.app` bundle path on macOS from `sys.executable` or `/Applications`."""
    try:
        exe_resolved = Path(sys.executable).resolve()
        for parent in exe_resolved.parents:
            if parent.suffix.lower() == ".app" and parent.is_dir():
                return str(parent)
    except Exception:
        pass

    for cand in (
        Path("/Applications/OrcaSlicer.app"),
        Path.home() / "Applications" / "OrcaSlicer.app",
    ):
        try:
            if cand.is_dir():
                return str(cand)
        except Exception:
            continue
    return None


def _dispatch_macos_open_files(
    file_paths: Sequence[str | Path],
    timeout_ms: int = 5000,
) -> tuple[bool, str]:
    """Send model files in-process to OrcaSlicer's Cocoa `wxAppController` on macOS (`darwin`).

    Marshals onto the Cocoa main queue (`_dispatch_main_q`) using ARM64-safe typed `CFUNCTYPE`
    wrappers around `objc_msgSend`, invoking `[NSApp.delegate application:NSApp openFiles:paths]`
    (`GUI_App::MacOpenFiles` -> `Plater::load_files`), with `NSWorkspace` fallback if needed.
    Requires ZERO external `subprocess` permissions.
    """
    if sys.platform != "darwin":
        return (False, "Cocoa openFiles dispatch requires darwin")

    resolved_files = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved_files:
        return (False, "Empty file_paths for macOS Plater dispatch")

    try:
        objc, libsystem = _load_macos_objc_and_gcd()
    except Exception as exc:
        return (False, f"macOS Objective-C load error: {exc}")

    msg_addr = ctypes.cast(objc.objc_msgSend, ctypes.c_void_p).value
    if not msg_addr:
        return (False, "objc_msgSend address unavailable")

    # Non-variadic ARM64 & x86_64 ABI-safe Objective-C message wrappers
    msg_id0 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(
        msg_addr
    )
    msg_void0 = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)(msg_addr)
    msg_id_cstr = ctypes.CFUNCTYPE(
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p
    )(msg_addr)
    msg_id_id = ctypes.CFUNCTYPE(
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )(msg_addr)
    msg_void_id = ctypes.CFUNCTYPE(
        None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )(msg_addr)
    msg_bool_sel = ctypes.CFUNCTYPE(
        ctypes.c_byte, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )(msg_addr)
    msg_bool_id_id = ctypes.CFUNCTYPE(
        ctypes.c_byte,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
    )(msg_addr)
    msg_void_id_id = ctypes.CFUNCTYPE(
        None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )(msg_addr)
    msg_open_urls = ctypes.CFUNCTYPE(
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_ulong,
        ctypes.c_void_p,
        ctypes.c_void_p,
    )(msg_addr)

    cls_pool = objc.objc_getClass(b"NSAutoreleasePool")
    cls_app = objc.objc_getClass(b"NSApplication")
    cls_str = objc.objc_getClass(b"NSString")
    cls_url = objc.objc_getClass(b"NSURL")
    cls_arr = objc.objc_getClass(b"NSMutableArray")
    cls_ws = objc.objc_getClass(b"NSWorkspace")
    cls_bundle = objc.objc_getClass(b"NSBundle")

    sel_alloc = objc.sel_registerName(b"alloc")
    sel_init = objc.sel_registerName(b"init")
    sel_drain = objc.sel_registerName(b"drain")
    sel_shared_app = objc.sel_registerName(b"sharedApplication")
    sel_delegate = objc.sel_registerName(b"delegate")
    sel_responds = objc.sel_registerName(b"respondsToSelector:")
    sel_open_files = objc.sel_registerName(b"application:openFiles:")
    sel_open_file = objc.sel_registerName(b"application:openFile:")
    sel_str_utf8 = objc.sel_registerName(b"stringWithUTF8String:")
    sel_file_url = objc.sel_registerName(b"fileURLWithPath:")
    sel_array = objc.sel_registerName(b"array")
    sel_add_obj = objc.sel_registerName(b"addObject:")
    sel_shared_ws = objc.sel_registerName(b"sharedWorkspace")
    sel_main_bundle = objc.sel_registerName(b"mainBundle")
    sel_bundle_url = objc.sel_registerName(b"bundleURL")
    sel_open_urls = objc.sel_registerName(
        b"openURLs:withApplicationAtURL:options:configuration:error:"
    )

    done_evt = threading.Event()
    result_box: dict[str, Any] = {
        "ok": False,
        "msg": "macOS main-queue callback pending",
    }

    DISPATCH_FN = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

    def _run_on_cocoa_main(_ctx: int) -> None:
        pool = msg_id0(msg_id0(cls_pool, sel_alloc), sel_init) if cls_pool else None
        try:
            ns_paths = msg_id0(cls_arr, sel_array)
            ns_urls = msg_id0(cls_arr, sel_array)
            for fp in resolved_files:
                ns_s = msg_id_cstr(cls_str, sel_str_utf8, fp.encode("utf-8"))
                if ns_s:
                    msg_void_id(ns_paths, sel_add_obj, ns_s)
                    if cls_url:
                        ns_u = msg_id_id(cls_url, sel_file_url, ns_s)
                        if ns_u:
                            msg_void_id(ns_urls, sel_add_obj, ns_u)

            ns_app = msg_id0(cls_app, sel_shared_app) if cls_app else None
            delegate = msg_id0(ns_app, sel_delegate) if ns_app else None

            if delegate and bool(msg_bool_sel(delegate, sel_responds, sel_open_files)):
                msg_void_id_id(delegate, sel_open_files, ns_app, ns_paths)
                result_box["ok"] = True
                result_box["msg"] = "ok (NSApp.delegate application:openFiles:)"
                return

            if delegate and bool(msg_bool_sel(delegate, sel_responds, sel_open_file)):
                all_ok = True
                for fp in resolved_files:
                    ns_s = msg_id_cstr(cls_str, sel_str_utf8, fp.encode("utf-8"))
                    if not bool(msg_bool_id_id(delegate, sel_open_file, ns_app, ns_s)):
                        all_ok = False
                if all_ok:
                    result_box["ok"] = True
                    result_box["msg"] = "ok (NSApp.delegate application:openFile:)"
                    return

            # Fallback to NSWorkspace openURLs with running bundle URL
            ws = msg_id0(cls_ws, sel_shared_ws) if cls_ws else None
            app_url = None
            if cls_bundle:
                mb = msg_id0(cls_bundle, sel_main_bundle)
                if mb:
                    app_url = msg_id0(mb, sel_bundle_url)
            if not app_url:
                app_path = _resolve_macos_app_bundle_path()
                if app_path and cls_url:
                    ns_app_s = msg_id_cstr(
                        cls_str, sel_str_utf8, app_path.encode("utf-8")
                    )
                    app_url = msg_id_id(cls_url, sel_file_url, ns_app_s)
            if ws and app_url and ns_urls:
                run_app = msg_open_urls(
                    ws, sel_open_urls, ns_urls, app_url, 0, None, None
                )
                if run_app:
                    result_box["ok"] = True
                    result_box["msg"] = "ok (NSWorkspace openURLs)"
                    return

            result_box["ok"] = False
            result_box["msg"] = (
                "No Cocoa openFiles delegate or NSWorkspace target responded"
            )
        except Exception as inner_exc:
            result_box["ok"] = False
            result_box["msg"] = f"Cocoa main-queue exception: {inner_exc}"
        finally:
            if pool:
                try:
                    msg_void0(pool, sel_drain)
                except Exception:
                    pass
            done_evt.set()

    c_cb = DISPATCH_FN(_run_on_cocoa_main)
    _MACOS_PENDING_DISPATCH_CBS.append(c_cb)

    try:
        main_q = ctypes.cast(
            ctypes.byref(_MacDispatchQueueS.in_dll(libsystem, "_dispatch_main_q")),
            ctypes.c_void_p,
        )
        dispatch_async_f = libsystem.dispatch_async_f
        if not _is_mock_callable(dispatch_async_f):
            dispatch_async_f.argtypes = [ctypes.c_void_p, ctypes.c_void_p, DISPATCH_FN]
            dispatch_async_f.restype = None
        dispatch_async_f(main_q, None, c_cb)
    except Exception as exc:
        if c_cb in _MACOS_PENDING_DISPATCH_CBS:
            _MACOS_PENDING_DISPATCH_CBS.remove(c_cb)
        return (False, f"dispatch_async_f failed: {exc}")

    finished = done_evt.wait(timeout=max(0.2, float(timeout_ms) / 1000.0))
    if finished and c_cb in _MACOS_PENDING_DISPATCH_CBS:
        _MACOS_PENDING_DISPATCH_CBS.remove(c_cb)

    if not finished:
        return (False, "Timed out waiting for Cocoa main-queue openFiles")
    return (bool(result_box["ok"]), str(result_box["msg"]))


def _open_folder_native(folder_path: Path) -> bool:
    """Open `folder_path` in Explorer (Windows) or Finder (macOS) without `subprocess`."""
    resolved = str(Path(folder_path).resolve())
    if sys.platform == "win32":
        startfile_fn = getattr(os, "startfile", None)
        if callable(startfile_fn):
            startfile_fn(resolved)
            return True
        return False

    if sys.platform == "darwin":
        objc, _ = _load_macos_objc_and_gcd()
        msg_addr = ctypes.cast(objc.objc_msgSend, ctypes.c_void_p).value
        if not msg_addr:
            return False
        msg_id0 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(
            msg_addr
        )
        msg_id_cstr = ctypes.CFUNCTYPE(
            ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p
        )(msg_addr)
        msg_id_id = ctypes.CFUNCTYPE(
            ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
        )(msg_addr)
        msg_bool_id = ctypes.CFUNCTYPE(
            ctypes.c_byte, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
        )(msg_addr)

        cls_str = objc.objc_getClass(b"NSString")
        cls_url = objc.objc_getClass(b"NSURL")
        cls_ws = objc.objc_getClass(b"NSWorkspace")
        sel_str_utf8 = objc.sel_registerName(b"stringWithUTF8String:")
        sel_file_url = objc.sel_registerName(b"fileURLWithPath:")
        sel_shared_ws = objc.sel_registerName(b"sharedWorkspace")
        sel_open_url = objc.sel_registerName(b"openURL:")

        ns_s = msg_id_cstr(cls_str, sel_str_utf8, resolved.encode("utf-8"))
        ns_u = msg_id_id(cls_url, sel_file_url, ns_s) if ns_s else None
        ws = msg_id0(cls_ws, sel_shared_ws) if cls_ws else None
        if ws and ns_u:
            return bool(msg_bool_id(ws, sel_open_url, ns_u))
        return False

    return False


def _dispatch_files_to_plater(
    file_paths: Sequence[str | Path],
    timeout_ms: int = 5000,
) -> tuple[bool, str, int | None]:
    """Cross-platform in-process Plater file loader for Windows (`win32`) and macOS (`darwin`)."""
    if sys.platform == "win32":
        copydata_payload = _format_other_instance_payload(file_paths)
        hwnd = _find_orca_mainframe_hwnd()
        ok, msg = _dispatch_copydata_to_hwnd(
            hwnd or 0, copydata_payload, timeout_ms=timeout_ms
        )
        return (ok, msg, hwnd)

    if sys.platform == "darwin":
        ok, msg = _dispatch_macos_open_files(file_paths, timeout_ms=timeout_ms)
        return (ok, msg, None)

    ok, msg = send_linux_plater_request(_format_other_instance_payload(file_paths))
    return ok, msg, None


def _slugify_filename(name: str, fallback: str = "thread") -> str:
    """Slugify filename while scrubbing OrcaSlicer `PluginAuditManager` denied path keywords
    (`secret`, `cert`, `conf` — which C++ `is_denied_path_keyword` blocks case-insensitively).
    """
    cleaned = re.sub(r"[^\w\-. ]+", "", str(name or "").strip(), flags=re.ASCII)
    cleaned = re.sub(r"\s+", "_", cleaned).strip("._-")
    cleaned = re.sub(r"secret", "secr", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"cert", "crt", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"conf", "cfg", cleaned, flags=re.IGNORECASE)
    if not cleaned:
        return fallback
    return cleaned[:64]


def _extract_first_float(val: Any, default: float) -> float:
    if val is None:
        return default
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        f = float(val)
        return f if f == f else default
    if isinstance(val, (list, tuple)):
        for item in val:
            res = _extract_first_float(item, float("nan"))
            if res == res:
                return res
        return default
    s = str(val).strip()
    if not s:
        return default
    m = re.search(r"[-+]?\d*\.?\d+", s)
    if not m:
        return default
    try:
        return float(m.group(0))
    except ValueError:
        return default


def _parse_printable_area(
    raw: Any, default_x: float = 220.0, default_y: float = 220.0
) -> tuple[float, float]:
    """Parse OrcaSlicer `printable_area` into `(bed_x_mm, bed_y_mm)`."""
    if raw is None:
        return (default_x, default_y)

    xs: list[float] = []
    ys: list[float] = []

    tokens: list[Any]
    if isinstance(raw, str):
        s = raw.strip()
        if s.startswith("["):
            try:
                parsed = json.loads(s)
                tokens = parsed if isinstance(parsed, list) else [s]
            except Exception:
                tokens = re.split(r"[;,]+", s)
        else:
            tokens = re.split(r"[;,]+", s)
    elif isinstance(raw, (list, tuple)):
        tokens = list(raw)
    else:
        return (default_x, default_y)

    for tok in tokens:
        if isinstance(tok, (list, tuple)) and len(tok) >= 2:
            try:
                xs.append(float(tok[0]))
                ys.append(float(tok[1]))
            except (TypeError, ValueError):
                continue
        elif isinstance(tok, str):
            m = re.search(r"([-+]?\d*\.?\d+)\s*[xX:]\s*([-+]?\d*\.?\d+)", tok)
            if m:
                try:
                    xs.append(float(m.group(1)))
                    ys.append(float(m.group(2)))
                except ValueError:
                    continue

    if len(xs) >= 2 and len(ys) >= 2:
        dx = max(xs) - min(xs)
        dy = max(ys) - min(ys)
        if dx >= 30.0 and dy >= 30.0:
            return (round(dx, 2), round(dy, 2))

    return (default_x, default_y)


def _parse_line_width(raw: Any, nozzle_mm: float) -> float:
    default_lw = round(nozzle_mm * 1.05, 2)
    if raw is None:
        return default_lw
    if isinstance(raw, (list, tuple)):
        return _parse_line_width(raw[0] if raw else None, nozzle_mm)
    s = str(raw).strip()
    if not s:
        return default_lw
    if s.endswith("%"):
        pct = _extract_first_float(s[:-1], 0.0)
        if pct > 10.0:
            return round(max(0.2, min(2.5, nozzle_mm * (pct / 100.0))), 3)
        return default_lw
    val = _extract_first_float(s, 0.0)
    if val <= 0.05:
        return default_lw
    return round(max(0.2, min(2.5, val)), 3)


def _extract_preset_name(obj: Any, fallback: str = "") -> str:
    if obj is None:
        return fallback
    if isinstance(obj, str):
        return obj.strip() or fallback
    if isinstance(obj, dict):
        for k in ("name", "preset_name", "id"):
            v = obj.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
        return fallback
    for attr in ("name", "preset_name"):
        try:
            val = getattr(obj, attr, None)
            if callable(val):
                val = val()
            if isinstance(val, str) and val.strip():
                return val.strip()
        except Exception:
            continue
    return fallback


def _bundle_get_value(bundle: Any, key: str) -> Any:
    if bundle is None:
        return None
    for method_name in ("full_config_value", "config_value", "get"):
        fn = getattr(bundle, method_name, None)
        if callable(fn):
            try:
                val = fn(key)
                if val is not None and val != "":
                    return val
            except Exception:
                continue
    return None


def _detect_language(app_info: dict[str, Any]) -> str:
    raw = str(app_info.get("language") or app_info.get("lang") or "").strip().lower()
    if raw.startswith("en"):
        return "en"
    if raw.startswith("pt"):
        return "pt"
    if raw:
        return "en" if not raw.startswith("pt") else "pt"
    try:
        loc = (locale.getlocale()[0] or "").lower()
        if loc.startswith("en"):
            return "en"
        if loc.startswith("pt"):
            return "pt"
    except Exception:
        pass
    return "pt"


def _detect_theme(app_info: dict[str, Any]) -> str:
    theme_raw = (
        str(app_info.get("theme") or app_info.get("color_mode") or "").strip().lower()
    )
    if theme_raw == "light":
        return "light"
    if theme_raw == "dark":
        return "dark"
    if app_info.get("dark_mode") is False:
        return "light"
    return "dark"


def _make_execution_result_success(message: str) -> Any:
    exec_cls = getattr(orca, "ExecutionResult", None)
    if exec_cls is not None:
        success_fn = getattr(exec_cls, "success", None)
        if callable(success_fn):
            try:
                return success_fn(message)
            except TypeError:
                return success_fn(message, "")
        try:
            ok_code = getattr(getattr(orca, "PluginResult", None), "Success", 0)
            return exec_cls(ok_code, message, "")
        except Exception:
            pass
    return {"status": "Success", "message": message}


# ---------------------------------------------------------------------------
# Shared Thread Studio Session & Message Router
# ---------------------------------------------------------------------------


class ThreadStudioController:
    def __init__(self):
        self._lock = threading.RLock()
        self._current_params = normalize_params()
        self._listeners = []
        self._undo = []
        self._redo = []
        self._last_plater_worker = None
        self._last_plater_outcome = {}
        self._revision = 0
        self._worker_lock = threading.Lock()
        self._last_geometry_worker = None
        self._preferences_initialized = False

    @property
    def current_params(self):
        with self._lock:
            return copy.deepcopy(self._current_params)

    def set_current_params(self, raw, history=True):
        p = normalize_params(raw)
        with self._lock:
            if p != self._current_params and history:
                self._undo.append(self._current_params)
                self._undo = self._undo[-50:]
                self._redo = []
            self._current_params = p
        return copy.deepcopy(p)

    def get_presets_dir(self):
        return _resolve_storage_dir() / "presets"

    def get_export_dir(self):
        d = _resolve_storage_dir() / "exports"
        d.mkdir(parents=True, exist_ok=True)
        return d

    def read_host_context(self) -> dict[str, Any]:
        """Defensively inspect `orca.host.app_language()` and `orca.host.preset_bundle()`."""
        app_info: dict[str, Any] = {}
        host = getattr(orca, "host", None)
        if host is not None:
            # Official OrcaSlicer API Reference (`orca.host.app_language()`)
            app_lang_fn = getattr(host, "app_language", None)
            if callable(app_lang_fn):
                try:
                    raw_lang = app_lang_fn()
                    if isinstance(raw_lang, str) and raw_lang.strip():
                        app_info["language"] = raw_lang.strip()
                except Exception:
                    pass

            app_info_fn = getattr(host, "app_info", None)
            if callable(app_info_fn):
                try:
                    info = app_info_fn()
                    if isinstance(info, dict):
                        for k, v in info.items():
                            app_info.setdefault(k, v)
                except Exception:
                    pass

        lang = _detect_language(app_info)
        theme = _detect_theme(app_info)
        theme_explicit = bool(
            app_info.get("theme")
            or app_info.get("color_mode")
            or ("dark_mode" in app_info)
        )
        orca_version = str(app_info.get("version") or "2.5.1")

        bundle = None
        if host is not None:
            bundle_fn = getattr(host, "preset_bundle", None)
            if callable(bundle_fn):
                try:
                    bundle = bundle_fn()
                except Exception:
                    bundle = None

        printer_name = "Generic FDM 220x220"
        process_name = "0.20mm Standard"
        filament_name = "Generic PLA"

        if bundle is not None:
            for m in ("current_printer_preset",):
                fn = getattr(bundle, m, None)
                if callable(fn):
                    try:
                        printer_name = _extract_preset_name(fn(), printer_name)
                    except Exception:
                        pass

            for m in ("current_print_preset", "current_process_preset"):
                fn = getattr(bundle, m, None)
                if callable(fn):
                    try:
                        got = _extract_preset_name(fn(), "")
                        if got:
                            process_name = got
                            break
                    except Exception:
                        pass

            for m in ("current_filament_preset_names", "current_filament_presets"):
                fn = getattr(bundle, m, None)
                if callable(fn):
                    try:
                        fils = fn()
                        if isinstance(fils, (list, tuple)) and fils:
                            got = _extract_preset_name(fils[0], "")
                            if got:
                                filament_name = got
                                break
                    except Exception:
                        pass

            if printer_name == "Generic FDM 220x220":
                p_id = _bundle_get_value(bundle, "printer_settings_id")
                if isinstance(p_id, str) and p_id.strip():
                    printer_name = p_id.strip()

        bed_x, bed_y = _parse_printable_area(
            _bundle_get_value(bundle, "printable_area"),
            default_x=220.0,
            default_y=220.0,
        )
        max_z = max(
            50.0,
            min(
                1000.0,
                _extract_first_float(
                    _bundle_get_value(bundle, "printable_height"), 250.0
                ),
            ),
        )
        nozzle_mm = max(
            0.15,
            min(
                2.0,
                _extract_first_float(_bundle_get_value(bundle, "nozzle_diameter"), 0.4),
            ),
        )
        layer_height_mm = max(
            0.04,
            min(
                1.2,
                _extract_first_float(_bundle_get_value(bundle, "layer_height"), 0.2),
            ),
        )
        line_width_mm = _parse_line_width(
            _bundle_get_value(bundle, "outer_wall_line_width"),
            nozzle_mm=nozzle_mm,
        )

        return {
            "lang": lang,
            "theme": theme,
            "theme_explicit": theme_explicit,
            "orca_version": orca_version,
            "printer_name": printer_name,
            "process_name": process_name,
            "filament_name": filament_name,
            "bed_x": float(bed_x),
            "bed_y": float(bed_y),
            "max_z": float(max_z),
            "nozzle_mm": float(nozzle_mm),
            "layer_height_mm": float(layer_height_mm),
            "line_width_mm": float(line_width_mm),
        }

    def read_full_host_config_snapshot(
        self, host_ctx: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Collect full resolved `project_settings` snapshot from `preset_bundle()` for `.3mf` export."""
        ctx = dict(host_ctx) if host_ctx is not None else self.read_host_context()
        project_settings: dict[str, Any] = {}

        host = getattr(orca, "host", None)
        bundle = None
        if host is not None:
            bundle_fn = getattr(host, "preset_bundle", None)
            if callable(bundle_fn):
                try:
                    bundle = bundle_fn()
                except Exception:
                    bundle = None

        if bundle is not None:
            keys_fn = getattr(bundle, "full_config_keys", None)
            val_fn = getattr(bundle, "full_config_value", None) or getattr(
                bundle, "config_value", None
            )
            if callable(keys_fn) and callable(val_fn):
                try:
                    keys = keys_fn()
                    if isinstance(keys, (list, tuple, set)):
                        for k in keys:
                            ks = str(k)
                            if not ks:
                                continue
                            try:
                                v = val_fn(ks)
                                if v is not None:
                                    project_settings[ks] = v
                            except Exception:
                                continue
                except Exception:
                    pass

        ctx["project_settings"] = project_settings
        return ctx

    def build_initial_context(self, mode="page"):
        host = self.read_host_context()
        if not self._preferences_initialized:
            self.set_current_params(
                dict(self.current_params, lang=host["lang"], theme=host["theme"]),
                history=False,
            )
            self._preferences_initialized = True
        p = self.current_params
        return dict(
            params=p,
            host=host,
            mode=mode,
            builtin_presets=BUILTIN_PRESETS,
            user_presets=load_user_presets(self.get_presets_dir()),
            lang=p["lang"],
            theme=p["theme"],
        )

    def _geometry_message(self, params=None):
        p = normalize_params(params or self.current_params)
        parts = []
        warning = ""
        try:
            parts = collect_target_meshes(p)
        except ValueError as exc:
            warning = str(exc)
        theta = np.zeros(241)
        z = np.linspace(0, 2 * p["pitch"], 241)
        profile = dict(
            z=z.tolist(),
            male=thread_radius(theta, z, p).tolist(),
            female=thread_radius(theta, z, p, True).tolist(),
        )
        return dict(
            type="geometry",
            params=p,
            meshes=[
                dict(
                    name=name,
                    vertices=m.vertices.ravel().tolist(),
                    triangles=m.triangles.ravel().tolist(),
                    volume_cm3=m.volume_cm3,
                    bounds=m.bounds_mm,
                )
                for name, m in parts
            ],
            report=analyze_engagement(p),
            profile=profile,
            warning=warning,
            can_undo=bool(self._undo),
            can_redo=bool(self._redo),
        )

    def _queue_geometry(self):
        with self._lock:
            self._revision += 1
            revision = self._revision
            p = self.current_params
        self._broadcast(dict(type="busy", busy=True))

        def generate():
            with self._worker_lock:
                if revision != self._revision:
                    return
                try:
                    result = self._geometry_message(p)
                except Exception as exc:
                    if revision == self._revision:
                        self._broadcast(
                            dict(
                                type="action_result",
                                ok=False,
                                paths=[],
                                message=str(exc),
                            )
                        )
                        self._broadcast(dict(type="busy", busy=False))
                    return
                if revision == self._revision:
                    self._broadcast(result)
                    self._broadcast(dict(type="busy", busy=False))

        self._last_geometry_worker = threading.Thread(target=generate, daemon=True)
        self._last_geometry_worker.start()

    def _broadcast(self, payload):
        for callback in self._listeners[:]:
            try:
                callback(payload)
            except Exception:
                self._listeners.remove(callback)

    def _write_exports(self, p, fmt):
        items = collect_target_meshes(p)
        base = self.get_export_dir() / (
            _slugify_filename(p["name"], fallback="thread") + "_" + uuid.uuid4().hex[:8]
        )
        if fmt == "3mf":
            return [
                str(
                    write_orca_3mf(
                        base.with_suffix(".3mf"),
                        items,
                        p,
                        self.read_full_host_config_snapshot(),
                    )
                )
            ]
        if fmt != "stl":
            raise ValueError("Unsupported export format")
        return [
            str(
                write_binary_stl(
                    base.with_name(base.name + "_" + name).with_suffix(".stl"), mesh
                )
            )
            for name, mesh in items
        ]

    def handle_message(self, raw_data, send_fn, default_mode="page"):
        try:
            msg = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
            if not isinstance(msg, dict):
                raise ValueError("Expected message object")
            action = msg.get("type", "")
            if action == "ready":
                if send_fn not in self._listeners:
                    self._listeners.append(send_fn)
                send_fn(
                    dict(type="init_state", **self.build_initial_context(default_mode))
                )
                self._queue_geometry()
                return
            if action in ("update", "analyze", "randomize", "reset"):
                p = (
                    DEFAULT_PARAMS
                    if action == "reset"
                    else msg.get("params", self.current_params)
                )
                if action == "randomize":
                    p = generate_random_printable_params(msg.get("seed"), p)
                self.set_current_params(p)
                self._queue_geometry()
                return
            if action in ("undo", "redo"):
                with self._lock:
                    source, target = (
                        (self._undo, self._redo)
                        if action == "undo"
                        else (self._redo, self._undo)
                    )
                    if source:
                        target.append(self._current_params)
                        self._current_params = source.pop()
                self._queue_geometry()
                return
            if action == "preset_save":
                data = save_user_preset(
                    self.get_presets_dir(),
                    msg.get("name", "Preset"),
                    msg.get("params", self.current_params),
                    msg.get("id"),
                )
                self._broadcast(dict(type="presets_updated", user_presets=data))
                return
            if action == "preset_delete":
                data = delete_user_preset(self.get_presets_dir(), msg.get("id", ""))
                self._broadcast(dict(type="presets_updated", user_presets=data))
                return
            if action in ("export_file", "send_to_plater"):
                p = self.set_current_params(msg.get("params", self.current_params))
                fmt = msg.get("format", "3mf")
                send_fn(
                    dict(
                        type="action_result",
                        ok=None,
                        action=action,
                        paths=[],
                        message="Preparando malha / Preparing mesh",
                    )
                )

                def export_worker():
                    try:
                        paths = self._write_exports(p, fmt)
                        if action == "export_file":
                            result = dict(
                                type="action_result",
                                ok=True,
                                action=action,
                                paths=paths,
                                message="Exportado / Exported",
                            )
                        else:
                            ok, detail, hwnd = _dispatch_files_to_plater(paths)
                            result = dict(
                                type="action_result",
                                ok=ok,
                                action=action,
                                paths=paths,
                                message=(
                                    "Pedido de importacao enviado; carregamento nao confirmado / Import request sent; loading not confirmed. "
                                    if ok
                                    else "Falha de envio / Transport failed. "
                                )
                                + detail,
                            )
                    except Exception as exc:
                        result = dict(
                            type="action_result",
                            ok=False,
                            action=action,
                            paths=[],
                            message=str(exc),
                        )
                    self._last_plater_outcome = result
                    send_fn(result)

                self._last_plater_worker = threading.Thread(
                    target=export_worker, daemon=True
                )
                self._last_plater_worker.start()
                return
            if action == "open_exports":
                ok = _open_folder_native(self.get_export_dir())
                send_fn(
                    dict(
                        type="action_result",
                        ok=ok,
                        paths=[str(self.get_export_dir())],
                        message="Pasta de exportacoes / Export folder",
                    )
                )
                return
            raise ValueError("Unknown command: " + str(action))
        except Exception as exc:
            send_fn(dict(type="action_result", ok=False, paths=[], message=str(exc)))


_SHARED_CONTROLLER = ThreadStudioController()


class ThreadStudioPageCapability(orca.pages.PagesPluginCapabilityBase):
    """Full-screen top-bar tab (`Gerador de Roscas`) beside Prepare / Preview / Device."""

    def __init__(self, controller: ThreadStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Gerador de Roscas"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "default_module": "container_and_lid",
            "default_standard": "fdm_trapezoid_45",
            "default_export_target": "all",
            "auto_configure_slicer": True,
        }

    def get_icon(self) -> str:
        storage_dir = _resolve_storage_dir()
        existing_candidates: list[Path] = []
        try:
            existing_candidates.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        existing_candidates.extend(
            [
                storage_dir / "icon.svg",
                _default_installed_plugin_dir() / "icon.svg",
            ]
        )
        for cand in existing_candidates:
            try:
                if cand.is_file() and cand.stat().st_size > 0:
                    return str(cand)
            except Exception:
                continue

        # Auto-materialize embedded `icon.svg` when user side-loaded only `orca_thread_generator.py`
        write_targets: list[Path] = [
            storage_dir / "icon.svg",
            _default_plugin_data_dir() / "icon.svg",
        ]
        try:
            write_targets.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        write_targets.append(
            Path.home() / "Documents" / "OrcaThreadStudio" / "icon.svg"
        )

        seen_dirs: set[str] = set()
        for target in write_targets:
            key = str(target)
            if key in seen_dirs:
                continue
            seen_dirs.add(key)
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                with open(target, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(ICON_SVG_CONTENT)
                if target.is_file() and target.stat().st_size > 0:
                    return str(target)
            except Exception:
                continue
        return ""

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="page")
        return get_studio_html(mode="page", initial_context=initial_ctx)

    def post_message(self, data: Any) -> None:
        super_post = getattr(super(), "post_message", None)
        if callable(super_post):
            super_post(data)

    def on_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self.post_message,
            default_mode="page",
        )


class ThreadStudioDockCapability(orca.script.ScriptPluginCapabilityBase):
    """Opens/shows a docked right-hand Thread Studio panel directly beside the 3D Plater."""

    _active_panel: Any = None
    _panel_lock = threading.RLock()

    def __init__(self, controller: ThreadStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Orca Thread Studio - Painel Lateral"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "default_export_target": "all",
            "auto_configure_slicer": True,
            "dock_side": "right",
        }

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="dock")
        return get_studio_html(mode="dock", initial_context=initial_ctx)

    def _post_to_panel(self, payload: dict[str, Any]) -> None:
        with self._panel_lock:
            panel = ThreadStudioDockCapability._active_panel
        if panel is None:
            return
        try:
            is_open_fn = getattr(panel, "is_open", None)
            if callable(is_open_fn) and not is_open_fn():
                return
            post_fn = getattr(panel, "post", None)
            if callable(post_fn):
                post_fn(payload)
        except Exception:
            pass

    def _on_panel_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self._post_to_panel,
            default_mode="dock",
        )

    def _on_panel_close(self) -> None:
        with self._panel_lock:
            ThreadStudioDockCapability._active_panel = None

    def on_message(self, data: Any) -> None:
        """Direct message entry point for testing or programmatic invocation."""
        self._on_panel_message(data)

    def execute(self) -> Any:
        """Invoked on OrcaSlicer's background Script worker thread."""
        with self._panel_lock:
            existing = ThreadStudioDockCapability._active_panel

        if existing is not None:
            try:
                is_open_fn = getattr(existing, "is_open", None)
                if not callable(is_open_fn) or is_open_fn():
                    show_fn = getattr(existing, "show", None)
                    if callable(show_fn):
                        show_fn()
                    init_ctx = self._controller.build_initial_context(mode="dock")
                    self._post_to_panel({"type": "init_state", **init_ctx})
                    return _make_execution_result_success(
                        "Painel lateral Orca Thread Studio exibido."
                    )
            except Exception:
                with self._panel_lock:
                    ThreadStudioDockCapability._active_panel = None

        html = self.get_ui()
        host = getattr(orca, "host", None)
        ui = getattr(host, "ui", None) if host is not None else None
        create_dock_fn = (
            getattr(ui, "create_dock_panel", None) if ui is not None else None
        )

        if callable(create_dock_fn):
            panel = create_dock_fn(
                html,
                title="Orca Thread Studio",
                width=430,
                height=800,
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
                dock="right",
            )
            with self._panel_lock:
                ThreadStudioDockCapability._active_panel = panel
            if panel is not None:
                show_fn = getattr(panel, "show", None)
                if callable(show_fn):
                    try:
                        show_fn()
                    except Exception:
                        pass
            return _make_execution_result_success(
                "Painel lateral Orca Thread Studio aberto."
            )

        create_win_fn = getattr(ui, "create_window", None) if ui is not None else None
        if callable(create_win_fn):
            panel = create_win_fn(
                html,
                title="Orca Thread Studio",
                width=450,
                height=820,
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
            )
            with self._panel_lock:
                ThreadStudioDockCapability._active_panel = panel
            return _make_execution_result_success("Janela Orca Thread Studio aberta.")

        return orca.ExecutionResult.failure(
            orca.PluginResult.RecoverableError,
            "This host does not provide a dock or window API",
        )


# ---------------------------------------------------------------------------
# Single `@orca.plugin` Entry Point Class
# ---------------------------------------------------------------------------


@orca.plugin
class OrcaThreadStudioPlugin(orca.base):
    """OrcaSlicer 2.5.1+ Native Plugin Entry Point for Orca Thread Studio."""

    def __init__(self) -> None:
        super().__init__()

    def register_capabilities(self) -> None:
        """Declare required plugin permissions and register Page + Script Dock capabilities.

        Per OrcaSlicer's `Plugin Audit Hook` specification:
        - `data_dir()` (`orca_plugins` and `orca.host.plugin.storage()`) is already a global
          read+write Allowed Root requiring zero `fs_read`/`fs_readwrite` prompts.
        - `has_permission` uses exact string equality (glob wildcards like `/*` are invalid).
        - `threading=True` declares the fixed `"thread"` audit target once up front.
        """
        req_fn = getattr(orca, "request_permissions", None)
        if callable(req_fn):
            req_fn(threading=True)

        orca.register_capability(ThreadStudioPageCapability)
        orca.register_capability(ThreadStudioDockCapability)
