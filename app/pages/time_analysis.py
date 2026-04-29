import streamlit as st
import pandas as pd
import altair as alt

from utils.loaders import load_many_datasets
from utils.formatters import (
    format_count,
    format_percent,
    safe_int,
)

# ============================================================
# Page config
# ============================================================

st.title("Time Analysis")
st.caption("Temporal analysis of collision patterns across years, months, weekdays, and hours.")

# ============================================================
# Load datasets
# ============================================================

required_datasets = load_many_datasets([
    "yearly_summary",
    "monthly_summary",
    "weekday_hour_summary",
])

yearly_summary = required_datasets["yearly_summary"].copy()
monthly_summary = required_datasets["monthly_summary"].copy()
weekday_hour_summary = required_datasets["weekday_hour_summary"].copy()

# ============================================================
# Filters
# ============================================================

available_years = sorted(monthly_summary["occ_year"].dropna().unique().tolist())

filter_col_1, filter_col_2 = st.columns([2, 2])

with filter_col_1:
    year_filter_mode = st.radio(
        "Year Filter Mode",
        options=["All Years", "Complete Years Only", "Single Year"],
        horizontal=True,
    )

with filter_col_2:
    selected_year = None
    if year_filter_mode == "Single Year":
        selected_year = st.selectbox(
            "Select Year",
            options=available_years,
            index=len(available_years) - 1 if available_years else 0,
        )

# ============================================================
# Filtered views
# ============================================================

if year_filter_mode == "Complete Years Only":
    yearly_view = yearly_summary.loc[yearly_summary["is_complete_year"] == True].copy()
    monthly_view = monthly_summary.loc[monthly_summary["is_complete_year"] == True].copy()
elif year_filter_mode == "Single Year" and selected_year is not None:
    yearly_view = yearly_summary.loc[yearly_summary["occ_year"] == selected_year].copy()
    monthly_view = monthly_summary.loc[monthly_summary["occ_year"] == selected_year].copy()
else:
    yearly_view = yearly_summary.copy()
    monthly_view = monthly_summary.copy()

weekday_hour_view = weekday_hour_summary.copy()

# ============================================================
# KPI row
# ============================================================

total_collisions = safe_int(monthly_view["collision_count"].sum()) if not monthly_view.empty else 0
years_covered = safe_int(monthly_view["occ_year"].nunique()) if not monthly_view.empty else 0

peak_month_row = (
    monthly_view.sort_values("collision_count", ascending=False).iloc[0]
    if not monthly_view.empty
    else None
)

peak_weekday_hour_row = (
    weekday_hour_view.sort_values("collision_count", ascending=False).iloc[0]
    if not weekday_hour_view.empty
    else None
)

kpi_col_1, kpi_col_2, kpi_col_3, kpi_col_4 = st.columns(4)

kpi_col_1.metric("Filtered Collisions", format_count(total_collisions))
kpi_col_2.metric("Years Covered", format_count(years_covered))

if peak_month_row is not None:
    peak_month_label = f"{peak_month_row['occ_month_name']} {safe_int(peak_month_row['occ_year'])}"
    kpi_col_3.metric(
        "Peak Month",
        peak_month_label,
        delta=f"{format_count(peak_month_row['collision_count'])} collisions",
    )
else:
    kpi_col_3.metric("Peak Month", "N/A")

if peak_weekday_hour_row is not None:
    peak_time_label = f"{peak_weekday_hour_row['occ_weekday_name']} - {safe_int(peak_weekday_hour_row['occ_hour']):02d}:00"
    kpi_col_4.metric(
        "Peak Weekday-Hour",
        peak_time_label,
        delta=f"{format_count(peak_weekday_hour_row['collision_count'])} collisions",
    )
else:
    kpi_col_4.metric("Peak Weekday-Hour", "N/A")

st.markdown("---")

# ============================================================
# Annual trend
# ============================================================

st.subheader("Annual Collision Trend")

annual_chart_df = yearly_view.sort_values("occ_year").copy()

if not annual_chart_df.empty:
    st.line_chart(
        annual_chart_df.set_index("occ_year")["collision_count"]
    )
else:
    st.warning("No annual data available for the selected filter.")

# ============================================================
# Monthly trend
# ============================================================

st.subheader("Monthly Collision Trend")

monthly_chart_df = monthly_view.copy()
monthly_chart_df["year_month_label"] = (
    monthly_chart_df["occ_year"].astype(str)
    + "-"
    + monthly_chart_df["occ_month"].astype(str).str.zfill(2)
)

if not monthly_chart_df.empty:
    st.line_chart(
        monthly_chart_df.set_index("year_month_label")["collision_count"]
    )
else:
    st.warning("No monthly data available for the selected filter.")

# ============================================================
# Weekday-hour heatmap
# ============================================================

st.subheader("Weekday-Hour Heatmap")

weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

hour_order = [f"{hour:02d}:00" for hour in range(24)]

heatmap_chart_df = weekday_hour_view.copy()
heatmap_chart_df["hour_label"] = heatmap_chart_df["occ_hour"].apply(lambda x: f"{safe_int(x):02d}:00")

heatmap_chart = (
    alt.Chart(heatmap_chart_df)
    .mark_rect()
    .encode(
        x=alt.X(
            "hour_label:O",
            sort=hour_order,
            title="Hour of Day"
        ),
        y=alt.Y(
            "occ_weekday_name:N",
            sort=weekday_order,
            title="Weekday"
        ),
        color=alt.Color(
            "collision_count:Q",
            title="Collision Count",
            scale=alt.Scale(scheme="blues")
        ),
        tooltip=[
            alt.Tooltip("occ_weekday_name:N", title="Weekday"),
            alt.Tooltip("hour_label:O", title="Hour"),
            alt.Tooltip("collision_count:Q", title="Collision Count", format=","),
            alt.Tooltip("collision_pct:Q", title="Collision %", format=".4f"),
            alt.Tooltip("weekday_total_collisions:Q", title="Weekday Total", format=","),
            alt.Tooltip("hour_share_within_weekday:Q", title="Hour Share Within Weekday", format=".4f"),
        ]
    )
    .properties(height=360)
)

st.altair_chart(heatmap_chart, use_container_width=True)

# ============================================================
# Detailed summary tables
# ============================================================

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Yearly Summary")
    yearly_display_cols = [
        "occ_year",
        "collision_count",
        "collision_pct",
        "yoy_change",
        "yoy_pct_change",
        "months_covered",
        "is_complete_year",
    ]
    yearly_display = yearly_view[yearly_display_cols].copy().reset_index(drop=True)

    yearly_display["collision_count"] = yearly_display["collision_count"].apply(format_count)
    yearly_display["collision_pct"] = yearly_display["collision_pct"].apply(format_percent)
    yearly_display["yoy_pct_change"] = yearly_display["yoy_pct_change"].apply(format_percent)

    if "yoy_change" in yearly_display.columns:
        yearly_display["yoy_change"] = yearly_display["yoy_change"].apply(
            lambda x: "N/A" if pd.isna(x) else format_count(x)
        )

    st.dataframe(yearly_display, use_container_width=True)

with right_col:
    st.subheader("Top Monthly Periods")
    monthly_top_display = (
        monthly_view.sort_values("collision_count", ascending=False)
        .head(15)
        [
            [
                "occ_year",
                "occ_month",
                "occ_month_name",
                "collision_count",
                "monthly_share_within_year",
                "is_complete_year",
            ]
        ]
        .copy()
        .reset_index(drop=True)
    )

    monthly_top_display["collision_count"] = monthly_top_display["collision_count"].apply(format_count)
    monthly_top_display["monthly_share_within_year"] = monthly_top_display["monthly_share_within_year"].apply(format_percent)

    st.dataframe(monthly_top_display, use_container_width=True)

st.subheader("Weekday-Hour Detail")

weekday_hour_display = (
    weekday_hour_view.sort_values("collision_count", ascending=False)
    .copy()
    .reset_index(drop=True)
)

for col in ["collision_count", "weekday_total_collisions"]:
    if col in weekday_hour_display.columns:
        weekday_hour_display[col] = weekday_hour_display[col].apply(format_count)

for col in ["collision_pct", "hour_share_within_weekday"]:
    if col in weekday_hour_display.columns:
        weekday_hour_display[col] = weekday_hour_display[col].apply(format_percent)

st.dataframe(weekday_hour_display, use_container_width=True)

# ============================================================
# Data note
# ============================================================

st.markdown("---")
st.info(
    "This page uses yearly, monthly, and weekday-hour aggregated datasets prepared in the analytical pipeline. "
    "It is designed to support time trend analysis in Tableau, Power BI, and Streamlit."
)