"""Twelve bilingual starting points and atomic user preset persistence."""

from __future__ import annotations
import json, uuid, random
from pathlib import Path
from .schema import normalize_params

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
