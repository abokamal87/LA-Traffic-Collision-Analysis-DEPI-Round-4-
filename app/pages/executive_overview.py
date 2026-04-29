import streamlit as st
import pandas as pd
import altair as alt

from utils.loaders import load_many_datasets
from utils.formatters import (
    format_count,
    format_percent,
    format_year_over_year_delta,
    safe_int,
)

# ============================================================
# Page config
# ============================================================

st.title("Executive Overview")
st.caption(
    "High-level summary of traffic collision trends, risk patterns, and priority indicators."
)

# ============================================================
# Load datasets
# ============================================================

required_datasets = load_many_datasets([
    "yearly_summary",
    "area_summary",
    "injury_severity_summary",
    "hit_run_summary",
    "vulnerable_users_summary",
])

yearly_summary = required_datasets["yearly_summary"].copy()
area_summary = required_datasets["area_summary"].copy()
injury_severity_summary = required_datasets["injury_severity_summary"].copy()
hit_run_summary = required_datasets["hit_run_summary"].copy()
vulnerable_users_summary = required_datasets["vulnerable_users_summary"].copy()

# ============================================================
# Core KPI logic
# ============================================================

total_collisions = safe_int(yearly_summary["collision_count"].sum())

complete_year_view = (
    yearly_summary.loc[yearly_summary["is_complete_year"] == True]
    .sort_values("occ_year")
    .copy()
    if "is_complete_year" in yearly_summary.columns
    else yearly_summary.sort_values("occ_year").copy()
)

if complete_year_view.empty:
    complete_year_view = yearly_summary.sort_values("occ_year").copy()

latest_complete_row = complete_year_view.iloc[-1]
latest_complete_year = safe_int(latest_complete_row["occ_year"])
latest_complete_collisions = safe_int(latest_complete_row["collision_count"])

if len(complete_year_view) >= 2:
    previous_complete_row = complete_year_view.iloc[-2]
    latest_delta_value = latest_complete_collisions - safe_int(previous_complete_row["collision_count"])
else:
    latest_delta_value = None

top_area_row = area_summary.sort_values("collision_count", ascending=False).iloc[0]
top_area_name = str(top_area_row["area_name"])
top_area_collisions = safe_int(top_area_row["collision_count"])

non_injury_row = injury_severity_summary.loc[
    injury_severity_summary["injury_severity_label"] == "(N) Non-injury"
]
non_injury_share = (
    float(non_injury_row["collision_pct_of_traffic_only_collisions"].iloc[0])
    if (
        not non_injury_row.empty
        and "collision_pct_of_traffic_only_collisions" in non_injury_row.columns
    )
    else None
)

fatal_row = injury_severity_summary.loc[
    injury_severity_summary["injury_severity_label"] == "(K) Fatal injury"
]
fatal_collisions = (
    safe_int(fatal_row["collision_count"].iloc[0])
    if not fatal_row.empty and "collision_count" in fatal_row.columns
    else 0
)

hit_run_share = (
    float(hit_run_summary["collision_pct_of_traffic_only_collisions"].sum())
    if "collision_pct_of_traffic_only_collisions" in hit_run_summary.columns
    else None
)

vulnerable_user_total = (
    safe_int(vulnerable_users_summary["collision_count"].sum())
    if "collision_count" in vulnerable_users_summary.columns
    else 0
)

# ============================================================
# KPI row
# ============================================================

kpi_col_1, kpi_col_2, kpi_col_3, kpi_col_4 = st.columns(4)

kpi_col_1.metric("Total Collisions", format_count(total_collisions))
kpi_col_2.metric(
    f"Latest Complete Year ({latest_complete_year})",
    format_count(latest_complete_collisions),
    delta=format_year_over_year_delta(latest_delta_value),
)
kpi_col_3.metric("Top Area", top_area_name, delta=f"{format_count(top_area_collisions)} collisions")
kpi_col_4.metric("Hit-and-Run Share", format_percent(hit_run_share))

sec_col_1, sec_col_2, sec_col_3 = st.columns(3)
sec_col_1.metric("Non-Injury Share", format_percent(non_injury_share))
sec_col_2.metric("Fatal Collisions", format_count(fatal_collisions))
sec_col_3.metric("Vulnerable User Collisions", format_count(vulnerable_user_total))

st.markdown("---")

# ============================================================
# Annual trend
# ============================================================

st.subheader("Annual Collision Trend")

annual_chart_df = yearly_summary.sort_values("occ_year").copy()
annual_chart_df["year_type"] = annual_chart_df["is_complete_year"].map(
    {True: "Complete Year", False: "Partial Year"}
) if "is_complete_year" in annual_chart_df.columns else "Year"

annual_trend_chart = (
    alt.Chart(annual_chart_df)
    .mark_line(point=True)
    .encode(
        x=alt.X("occ_year:O", title="Year"),
        y=alt.Y("collision_count:Q", title="Collision Count"),
        color=alt.Color("year_type:N", title="Coverage"),
        tooltip=[
            alt.Tooltip("occ_year:O", title="Year"),
            alt.Tooltip("collision_count:Q", title="Collision Count", format=","),
            alt.Tooltip("collision_pct:Q", title="Collision Share", format=".4f"),
            alt.Tooltip("yoy_change:Q", title="YoY Change", format=","),
            alt.Tooltip("yoy_pct_change:Q", title="YoY % Change", format=".4f"),
            alt.Tooltip("months_covered:Q", title="Months Covered"),
            alt.Tooltip("is_complete_year:N", title="Complete Year"),
        ],
    )
    .properties(height=360)
)

st.altair_chart(annual_trend_chart, use_container_width=True)

if "is_complete_year" in annual_chart_df.columns and not annual_chart_df["is_complete_year"].all():
    st.caption("The trend includes both complete and partial years. KPI comparison uses the latest complete year.")

# ============================================================
# Top areas and severity
# ============================================================

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Top Areas by Collision Count")

    top_areas_display = (
        area_summary.sort_values("collision_count", ascending=False)
        .head(10)
        [["area_name", "collision_count", "collision_pct", "area_rank_by_collision_count"]]
        .reset_index(drop=True)
    )
    top_areas_display["collision_count"] = top_areas_display["collision_count"].apply(format_count)
    top_areas_display["collision_pct"] = top_areas_display["collision_pct"].apply(format_percent)

    st.dataframe(top_areas_display, use_container_width=True)

with right_col:
    st.subheader("Injury Severity Distribution")

    severity_display = (
        injury_severity_summary.sort_values("injury_severity_order")
        [["injury_severity_label", "collision_count", "collision_pct_of_traffic_only_collisions"]]
        .reset_index(drop=True)
    )
    severity_display["collision_count"] = severity_display["collision_count"].apply(format_count)
    severity_display["collision_pct_of_traffic_only_collisions"] = (
        severity_display["collision_pct_of_traffic_only_collisions"].apply(format_percent)
    )

    st.dataframe(severity_display, use_container_width=True)

# ============================================================
# Hit-and-run and vulnerable users
# ============================================================

left_col_2, right_col_2 = st.columns(2)

with left_col_2:
    st.subheader("Hit-and-Run Breakdown")

    hit_run_display = (
        hit_run_summary.copy()
        [["hit_run_status_label", "collision_count", "collision_pct_of_traffic_only_collisions"]]
        .reset_index(drop=True)
    )
    hit_run_display["collision_count"] = hit_run_display["collision_count"].apply(format_count)
    hit_run_display["collision_pct_of_traffic_only_collisions"] = (
        hit_run_display["collision_pct_of_traffic_only_collisions"].apply(format_percent)
    )

    st.dataframe(hit_run_display, use_container_width=True)

with right_col_2:
    st.subheader("Vulnerable Users Summary")

    vulnerable_display = vulnerable_users_summary.copy().reset_index(drop=True)
    if "collision_count" in vulnerable_display.columns:
        vulnerable_display["collision_count"] = vulnerable_display["collision_count"].apply(format_count)
    if "mo_row_count" in vulnerable_display.columns:
        vulnerable_display["mo_row_count"] = vulnerable_display["mo_row_count"].apply(format_count)
    if "collision_pct_within_vulnerable_groups" in vulnerable_display.columns:
        vulnerable_display["collision_pct_within_vulnerable_groups"] = (
            vulnerable_display["collision_pct_within_vulnerable_groups"].apply(format_percent)
        )

    st.dataframe(vulnerable_display, use_container_width=True)

# ============================================================
# Data note
# ============================================================

st.markdown("---")
st.info(
    "This page uses pre-aggregated dashboard datasets prepared in the analytical pipeline. "
    "KPI comparison for the yearly collision card is based on the latest complete year to avoid "
    "partial-year distortion."
)