"""Analytic radial helical envelopes, ISO-inspired/FDM profiles and Higbee starts."""

from __future__ import annotations

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
