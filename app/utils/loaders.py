from pathlib import Path
import pandas as pd
import streamlit as st

# ============================================================
# Project paths
# ============================================================

UTILS_DIR = Path(__file__).resolve().parent
APP_DIR = UTILS_DIR.parent
PROJECT_ROOT = APP_DIR.parent

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
TABLEAU_READY_DIR = OUTPUTS_DIR / "tableau_ready"
POWERBI_READY_DIR = OUTPUTS_DIR / "powerbi_ready"

# ============================================================
# Canonical BI source
# ============================================================

DEFAULT_BI_SOURCE = "tableau_ready"

BI_SOURCE_DIRS = {
    "tableau_ready": TABLEAU_READY_DIR,
    "powerbi_ready": POWERBI_READY_DIR,
}

# ============================================================
# Core dataset catalog
# ============================================================

DATASET_FILE_MAP = {
    "yearly_summary": "yearly_summary.csv",
    "monthly_summary": "monthly_summary.csv",
    "weekday_hour_summary": "weekday_hour_summary.csv",
    "area_summary": "area_summary.csv",
    "reporting_division_summary": "reporting_division_summary.csv",
    "premise_summary_non_street": "premise_summary_non_street.csv",
    "injury_severity_summary": "injury_severity_summary.csv",
    "hit_run_summary": "hit_run_summary.csv",
    "dui_sobriety_summary": "dui_sobriety_summary.csv",
    "mo_analytical_domain_summary": "mo_analytical_domain_summary.csv",
    "mo_analytical_category_summary": "mo_analytical_category_summary.csv",
    "mo_analytical_subcategory_summary": "mo_analytical_subcategory_summary.csv",
    "traffic_only_mo_domain_summary": "traffic_only_mo_domain_summary.csv",
    "traffic_only_mo_subcategory_summary": "traffic_only_mo_subcategory_summary.csv",
    "victim_age_group_summary": "victim_age_group_summary.csv",
    "victim_sex_summary": "victim_sex_summary.csv",
    "victim_descent_summary": "victim_descent_summary.csv",
    "vulnerable_users_summary": "vulnerable_users_summary.csv",
    "map_collision_points": "map_collision_points.csv",
    "map_hotspots_by_coordinate": "map_hotspots_by_coordinate.csv",
}

# ============================================================
# Helper functions
# ============================================================

def get_bi_source_dir(source_name: str = DEFAULT_BI_SOURCE) -> Path:
    if source_name not in BI_SOURCE_DIRS:
        raise ValueError(f"Unsupported BI source: {source_name}")
    return BI_SOURCE_DIRS[source_name]


def get_dataset_path(dataset_name: str, source_name: str = DEFAULT_BI_SOURCE) -> Path:
    if dataset_name not in DATASET_FILE_MAP:
        raise KeyError(f"Dataset not registered: {dataset_name}")
    return get_bi_source_dir(source_name) / DATASET_FILE_MAP[dataset_name]


@st.cache_data(show_spinner=False)
def load_dataset(dataset_name: str, source_name: str = DEFAULT_BI_SOURCE) -> pd.DataFrame:
    dataset_path = get_dataset_path(dataset_name, source_name)

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {dataset_path}")

    return pd.read_csv(dataset_path)


@st.cache_data(show_spinner=False)
def load_many_datasets(dataset_names: list[str], source_name: str = DEFAULT_BI_SOURCE) -> dict[str, pd.DataFrame]:
    return {name: load_dataset(name, source_name) for name in dataset_names}


def get_dataset_brief(dataset_name: str, source_name: str = DEFAULT_BI_SOURCE) -> dict:
    df = load_dataset(dataset_name, source_name)
    return {
        "dataset_name": dataset_name,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_cells": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


def get_available_dataset_names() -> list[str]:
    return sorted(DATASET_FILE_MAP.keys())