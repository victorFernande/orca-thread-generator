"""Validated offline Thread Studio parameters. Dimensions are millimetres."""

from __future__ import annotations
import math
from dataclasses import dataclass, asdict
from typing import Any

from .locale_catalog import normalize_language

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
    p["lang"] = normalize_language(p["lang"])
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
                    "Mason 86: confirm measured major diameter, root diameter, pitch and length"
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
