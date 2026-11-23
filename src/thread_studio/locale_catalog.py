"""Thread translation adapter. Catalog content and available languages are JSON data."""
from __future__ import annotations

from .language_packs import load_language_packs, resolve_language, language_pack_payload

LANGUAGE_PACKS, LANGUAGE_PACK_ERRORS = load_language_packs()
SUPPORTED_LANGUAGES = tuple(LANGUAGE_PACKS)
LANGUAGE_NAMES = tuple(pack["native_name"] for pack in LANGUAGE_PACKS.values())
LANGUAGE_METADATA = language_pack_payload(LANGUAGE_PACKS)
TRANSLATIONS = {code: pack["translations"] for code, pack in LANGUAGE_PACKS.items()}


def normalize_language(value: object, default: str = "pt") -> str:
    return resolve_language(value, LANGUAGE_PACKS, default)


def translate_text(english: str, language: object, portuguese: str | None = None,
                   context: str | None = None) -> str:
    code = normalize_language(language)
    catalog = TRANSLATIONS.get(code, {})
    if context and context + "::" + english in catalog:
        return catalog[context + "::" + english]
    return catalog.get(english,
        portuguese if code == "pt" and portuguese is not None else english)
