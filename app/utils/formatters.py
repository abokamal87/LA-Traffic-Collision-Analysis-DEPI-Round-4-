from __future__ import annotations

from typing import Any

import pandas as pd

# ============================================================
# Generic scalar formatting
# ============================================================

UNKNOWN_LABEL = "Unknown / Invalid"


def is_missing(value: Any) -> bool:
    return pd.isna(value)


def safe_int(value: Any, default: int = 0) -> int:
    if is_missing(value):
        return default
    try:
        return int(float(value))
    except Exception:
        return default


def safe_float(value: Any, default: float = 0.0) -> float:
    if is_missing(value):
        return default
    try:
        return float(value)
    except Exception:
        return default


def format_count(value: Any, default: str = "0") -> str:
    if is_missing(value):
        return default
    try:
        return f"{safe_int(value):,}"
    except Exception:
        return default


def format_percent(
    value: Any,
    decimals: int = 1,
    multiply_by_100: bool = True,
    default: str = "N/A",
) -> str:
    if is_missing(value):
        return default

    try:
        numeric_value = safe_float(value)

        if multiply_by_100:
            numeric_value *= 100

        return f"{numeric_value:.{decimals}f}%"
    except Exception:
        return default


def format_delta_count(
    value: Any,
    suffix: str = "",
    default: str = "N/A",
    include_plus_sign: bool = True,
) -> str:
    if is_missing(value):
        return default

    numeric_value = safe_int(value)
    sign = "+" if include_plus_sign and numeric_value >= 0 else ""
    suffix_part = f" {suffix.strip()}" if suffix else ""

    return f"{sign}{numeric_value:,}{suffix_part}"


def format_year_over_year_delta(value: Any, default: str = "N/A") -> str:
    if is_missing(value):
        return default

    numeric_value = safe_int(value)
    sign = "+" if numeric_value >= 0 else ""
    return f"{sign}{numeric_value:,} vs prior year"


# ============================================================
# Text cleanup and label formatting
# ============================================================

def clean_text(value: Any, default: str = UNKNOWN_LABEL) -> str:
    if is_missing(value):
        return default

    text = str(value).strip()

    if text in {"", "nan", "None", "null", "NULL"}:
        return default

    return text


def shorten_label(value: Any, max_len: int = 30) -> str:
    text = clean_text(value)

    if len(text) <= max_len:
        return text

    return text[: max_len - 3] + "..."


def title_case_label(value: Any) -> str:
    text = clean_text(value)
    return text.title()


def normalize_unknown_label(value: Any, default: str = UNKNOWN_LABEL) -> str:
    text = clean_text(value, default=default)

    normalized_unknown_values = {
        "Unknown",
        "Unknown/Invalid",
        "Unknown / Invalid",
        "Invalid",
        "Not Recorded",
        "Not Specified",
        "Unk",
        "UNK",
        "U",
        "X",
        "99",
        "999",
    }

    return default if text in normalized_unknown_values else text


# ============================================================
# Domain-specific label helpers
# ============================================================

SEX_LABEL_MAP = {
    "M": "Male",
    "F": "Female",
    "X": UNKNOWN_LABEL,
    "U": UNKNOWN_LABEL,
    "1": "Male",
    "2": "Female",
    "9": UNKNOWN_LABEL,
    "99": UNKNOWN_LABEL,
}

DESCENT_LABEL_MAP = {
    "A": "Other Asian",
    "B": "Black",
    "C": "Chinese",
    "D": "Cambodian",
    "F": "Filipino",
    "G": "Guamanian",
    "H": "Hispanic/Latin/Mexican",
    "I": "American Indian/Alaskan Native",
    "J": "Japanese",
    "K": "Korean",
    "L": "Laotian",
    "O": "Other",
    "P": "Pacific Islander",
    "S": "Samoan",
    "U": UNKNOWN_LABEL,
    "V": "Vietnamese",
    "W": "White",
    "X": UNKNOWN_LABEL,
    "Z": "Asian Indian",
    "99": UNKNOWN_LABEL,
}


def map_sex_label(value: Any, default: str = UNKNOWN_LABEL) -> str:
    text = clean_text(value, default=default)
    mapped = SEX_LABEL_MAP.get(text, text)
    return normalize_unknown_label(mapped, default=default)


def map_descent_label(value: Any, default: str = UNKNOWN_LABEL) -> str:
    text = clean_text(value, default=default)
    mapped = DESCENT_LABEL_MAP.get(text, text)
    return normalize_unknown_label(mapped, default=default)


# ============================================================
# Pandas helpers
# ============================================================

def format_percent_series(
    series: pd.Series,
    decimals: int = 1,
    multiply_by_100: bool = True,
    default: str = "N/A",
) -> pd.Series:
    return series.apply(
        lambda x: format_percent(
            x,
            decimals=decimals,
            multiply_by_100=multiply_by_100,
            default=default,
        )
    )


def format_count_series(series: pd.Series, default: str = "0") -> pd.Series:
    return series.apply(lambda x: format_count(x, default=default))


def clean_text_series(series: pd.Series, default: str = UNKNOWN_LABEL) -> pd.Series:
    return series.apply(lambda x: clean_text(x, default=default))


def shorten_label_series(series: pd.Series, max_len: int = 30) -> pd.Series:
    return series.apply(lambda x: shorten_label(x, max_len=max_len))


def map_sex_label_series(series: pd.Series, default: str = UNKNOWN_LABEL) -> pd.Series:
    return series.apply(lambda x: map_sex_label(x, default=default))


def map_descent_label_series(series: pd.Series, default: str = UNKNOWN_LABEL) -> pd.Series:
    return series.apply(lambda x: map_descent_label(x, default=default))