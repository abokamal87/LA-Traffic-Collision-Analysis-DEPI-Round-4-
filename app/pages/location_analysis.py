import streamlit as st
import pandas as pd

from utils.loaders import load_many_datasets, load_dataset
from utils.formatters import (
    format_count,
    format_percent,
    safe_int,
)

# ============================================================
# Page config
# ============================================================

st.title("Location Analysis")
st.caption(
    "Geographic and operational hotspot analysis across areas, reporting divisions, "
    "premise types, and mapped coordinates."
)

# ============================================================
# Load datasets
# ============================================================

required_datasets = load_many_datasets([
    "area_summary",
    "reporting_division_summary",
    "premise_summary_non_street",
    "map_hotspots_by_coordinate",
])

area_summary = required_datasets["area_summary"].copy()
reporting_division_summary = required_datasets["reporting_division_summary"].copy()
premise_summary_non_street = required_datasets["premise_summary_non_street"].copy()
map_hotspots_by_coordinate = required_datasets["map_hotspots_by_coordinate"].copy()

# ============================================================
# Helper functions
# ============================================================

def detect_label_column(df: pd.DataFrame, preferred: list[str]) -> str:
    for col in preferred:
        if col in df.columns:
            return col

    fallback_candidates = [
        col for col in df.columns
        if all(token not in col.lower() for token in ["count", "pct", "rate", "rank", "latitude", "longitude"])
    ]
    return fallback_candidates[0] if fallback_candidates else df.columns[0]


def detect_count_column(df: pd.DataFrame) -> str:
    preferred = ["collision_count", "valid_coordinate_collision_count", "complete_premise_collision_count"]
    for col in preferred:
        if col in df.columns:
            return col

    count_candidates = [col for col in df.columns if "count" in col.lower()]
    return count_candidates[0] if count_candidates else df.columns[0]


area_label_col = detect_label_column(area_summary, ["area_name"])
area_count_col = detect_count_column(area_summary)

division_label_col = detect_label_column(
    reporting_division_summary,
    ["reporting_division_label", "reporting_division", "reporting_district", "division_label"]
)
division_count_col = detect_count_column(reporting_division_summary)

premise_label_col = detect_label_column(
    premise_summary_non_street,
    ["premise_description", "premise_label"]
)
premise_count_col = detect_count_column(premise_summary_non_street)

# ============================================================
# Filters
# ============================================================

filter_col_1, filter_col_2 = st.columns([2, 2])

with filter_col_1:
    hotspot_top_n = st.slider(
        "Number of Hotspots to Display",
        min_value=100,
        max_value=3000,
        value=1000,
        step=100,
    )

with filter_col_2:
    show_detail_points = st.checkbox(
        "Load detailed collision points layer (heavy)",
        value=False,
    )

hotspot_view = (
    map_hotspots_by_coordinate
    .sort_values("collision_count", ascending=False)
    .head(hotspot_top_n)
    .reset_index(drop=True)
    .copy()
)

# ============================================================
# KPI row
# ============================================================

total_collisions = safe_int(area_summary[area_count_col].sum())

top_area_row = area_summary.sort_values(area_count_col, ascending=False).iloc[0]
top_area_name = str(top_area_row[area_label_col])
top_area_collisions = safe_int(top_area_row[area_count_col])

top_hotspot_row = map_hotspots_by_coordinate.sort_values("collision_count", ascending=False).iloc[0]
top_hotspot_count = safe_int(top_hotspot_row["collision_count"])

hotspot_coordinate_count = safe_int(map_hotspots_by_coordinate.shape[0])

kpi_col_1, kpi_col_2, kpi_col_3, kpi_col_4 = st.columns(4)

kpi_col_1.metric("Total Collisions", format_count(total_collisions))
kpi_col_2.metric("Top Area", top_area_name, delta=f"{format_count(top_area_collisions)} collisions")
kpi_col_3.metric("Top Hotspot Count", format_count(top_hotspot_count))
kpi_col_4.metric("Hotspot Coordinates", format_count(hotspot_coordinate_count))

st.markdown("---")

# ============================================================
# Hotspot map
# ============================================================

st.subheader("Hotspot Map")
st.caption(f"Displaying the top {format_count(len(hotspot_view))} hotspot coordinates by collision count.")

hotspot_map_df = hotspot_view[["latitude", "longitude"]].dropna().copy()

if not hotspot_map_df.empty:
    st.map(hotspot_map_df, use_container_width=True)
else:
    st.warning("No hotspot coordinates are available for mapping.")

# ============================================================
# Hotspot detail table
# ============================================================

st.subheader("Top Hotspots")

hotspot_display_cols = [
    col for col in [
        "hotspot_rank",
        "collision_count",
        "latitude",
        "longitude",
        "dominant_area_name",
        "dominant_reporting_district",
        "dominant_premise_description",
        "latest_year",
        "latest_collision_date",
        "hotspot_popup_label",
    ]
    if col in hotspot_view.columns
]

hotspot_display = hotspot_view[hotspot_display_cols].copy().reset_index(drop=True)

if "hotspot_rank" in hotspot_display.columns:
    hotspot_display["hotspot_rank"] = hotspot_display["hotspot_rank"].apply(format_count)
if "collision_count" in hotspot_display.columns:
    hotspot_display["collision_count"] = hotspot_display["collision_count"].apply(format_count)
if "dominant_reporting_district" in hotspot_display.columns:
    hotspot_display["dominant_reporting_district"] = hotspot_display["dominant_reporting_district"].apply(format_count)
if "latest_year" in hotspot_display.columns:
    hotspot_display["latest_year"] = hotspot_display["latest_year"].apply(format_count)

st.dataframe(hotspot_display, use_container_width=True)

# ============================================================
# Area and division analysis
# ============================================================

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Top Areas by Collision Count")

    top_area_chart_df = (
        area_summary
        .sort_values(area_count_col, ascending=False)
        .head(10)
        [[area_label_col, area_count_col]]
        .set_index(area_label_col)
    )
    st.bar_chart(top_area_chart_df)

    area_display_cols = [
        col for col in [
            "area_id",
            "area_name",
            "collision_count",
            "collision_pct",
            "valid_coordinate_rate",
            "complete_premise_rate",
            "area_rank_by_collision_count",
        ]
        if col in area_summary.columns
    ]
    area_display = (
        area_summary
        .sort_values(area_count_col, ascending=False)
        [area_display_cols]
        .reset_index(drop=True)
    )

    for count_col in ["area_id", "collision_count", "area_rank_by_collision_count"]:
        if count_col in area_display.columns:
            area_display[count_col] = area_display[count_col].apply(format_count)

    for pct_col in ["collision_pct", "valid_coordinate_rate", "complete_premise_rate"]:
        if pct_col in area_display.columns:
            area_display[pct_col] = area_display[pct_col].apply(format_percent)

    st.dataframe(area_display, use_container_width=True)

with right_col:
    st.subheader("Top Reporting Divisions")

    top_division_chart_df = (
        reporting_division_summary
        .sort_values(division_count_col, ascending=False)
        .head(10)
        [[division_label_col, division_count_col]]
        .set_index(division_label_col)
    )
    st.bar_chart(top_division_chart_df)

    division_display_cols = [
        col for col in [
            division_label_col,
            "collision_count",
            "collision_pct",
            "division_rank_by_collision_count",
            "reporting_division_rank_by_collision_count",
        ]
        if col in reporting_division_summary.columns
    ]
    division_display = (
        reporting_division_summary
        .sort_values(division_count_col, ascending=False)
        [division_display_cols]
        .reset_index(drop=True)
    )

    for count_col in ["collision_count", "division_rank_by_collision_count", "reporting_division_rank_by_collision_count"]:
        if count_col in division_display.columns:
            division_display[count_col] = division_display[count_col].apply(format_count)

    if "collision_pct" in division_display.columns:
        division_display["collision_pct"] = division_display["collision_pct"].apply(format_percent)

    st.dataframe(division_display, use_container_width=True)

# ============================================================
# Premise analysis
# ============================================================

st.subheader("Top Non-Street Premise Types")

premise_chart_df = (
    premise_summary_non_street
    .sort_values(premise_count_col, ascending=False)
    .head(10)
    [[premise_label_col, premise_count_col]]
    .set_index(premise_label_col)
)

st.bar_chart(premise_chart_df)

premise_display_cols = [
    col for col in [
        "premise_code",
        "premise_description",
        "collision_count",
        "collision_pct",
        "valid_coordinate_rate",
        "premise_rank_by_collision_count",
    ]
    if col in premise_summary_non_street.columns
]

premise_display = (
    premise_summary_non_street
    .sort_values(premise_count_col, ascending=False)
    [premise_display_cols]
    .reset_index(drop=True)
)

for count_col in ["premise_code", "collision_count", "premise_rank_by_collision_count"]:
    if count_col in premise_display.columns:
        premise_display[count_col] = premise_display[count_col].apply(format_count)

for pct_col in ["collision_pct", "valid_coordinate_rate"]:
    if pct_col in premise_display.columns:
        premise_display[pct_col] = premise_display[pct_col].apply(format_percent)

st.dataframe(premise_display, use_container_width=True)

# ============================================================
# Optional detailed collision points
# ============================================================

if show_detail_points:
    st.markdown("---")
    st.subheader("Detailed Collision Points (Sampled Layer)")

    point_sample_size = st.slider(
        "Detailed point sample size",
        min_value=1000,
        max_value=50000,
        value=5000,
        step=1000,
    )

    detail_points = load_dataset("map_collision_points")

    if {"latitude", "longitude"}.issubset(detail_points.columns):
        detail_points_clean = detail_points[["latitude", "longitude"]].dropna().copy()

        detail_points_map = detail_points_clean.sample(
            n=min(point_sample_size, len(detail_points_clean)),
            random_state=42
        )

        st.map(detail_points_map, use_container_width=True)
        st.caption("This is a sampled detailed point layer for performance-safe exploration.")
    else:
        st.warning("Detailed collision point coordinates are not available in the expected format.")

# ============================================================
# Data note
# ============================================================

st.markdown("---")
st.info(
    "This page uses area, division, premise, and hotspot datasets prepared in the analytical pipeline. "
    "The hotspot layer is the recommended default view, while the detailed point layer is optional "
    "because it is significantly heavier."
)