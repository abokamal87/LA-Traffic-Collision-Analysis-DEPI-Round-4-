import streamlit as st
import pandas as pd

from utils.loaders import load_many_datasets

# ============================================================
# Page config
# ============================================================

st.title("Risk and Severity")
st.caption("Collision severity and behavioral risk review across injury severity, hit-and-run patterns, and DUI-related indicators.")

# ============================================================
# Load datasets
# ============================================================

required_datasets = load_many_datasets([
    "injury_severity_summary",
    "hit_run_summary",
    "dui_sobriety_summary",
])

injury_severity_summary = required_datasets["injury_severity_summary"]
hit_run_summary = required_datasets["hit_run_summary"]
dui_sobriety_summary = required_datasets["dui_sobriety_summary"]

# ============================================================
# Helper functions
# ============================================================

def detect_count_column(df: pd.DataFrame) -> str:
    preferred = ["collision_count", "mo_row_count"]
    for col in preferred:
        if col in df.columns:
            return col

    count_candidates = [col for col in df.columns if "count" in col.lower()]
    return count_candidates[0] if count_candidates else df.columns[0]


injury_count_col = detect_count_column(injury_severity_summary)
hit_run_count_col = detect_count_column(hit_run_summary)
dui_count_col = detect_count_column(dui_sobriety_summary)

# ============================================================
# KPI logic
# ============================================================

fatal_row = injury_severity_summary.loc[
    injury_severity_summary["injury_severity_label"] == "(K) Fatal injury"
]
fatal_collisions = int(fatal_row[injury_count_col].iloc[0]) if not fatal_row.empty else 0

severe_row = injury_severity_summary.loc[
    injury_severity_summary["injury_severity_label"] == "(A) Severe injury"
]
severe_collisions = int(severe_row[injury_count_col].iloc[0]) if not severe_row.empty else 0

non_injury_row = injury_severity_summary.loc[
    injury_severity_summary["injury_severity_label"] == "(N) Non-injury"
]
non_injury_share = (
    float(non_injury_row["collision_pct_of_traffic_only_collisions"].iloc[0]) * 100
    if (
        not non_injury_row.empty
        and "collision_pct_of_traffic_only_collisions" in non_injury_row.columns
    )
    else 0.0
)

hit_run_share = (
    float(hit_run_summary["collision_pct_of_traffic_only_collisions"].sum() * 100)
    if "collision_pct_of_traffic_only_collisions" in hit_run_summary.columns
    else 0.0
)

top_hit_run_row = hit_run_summary.sort_values(hit_run_count_col, ascending=False).iloc[0]
top_hit_run_label = str(top_hit_run_row["hit_run_status_label"])
top_hit_run_count = int(top_hit_run_row[hit_run_count_col])

top_dui_row = dui_sobriety_summary.sort_values(dui_count_col, ascending=False).iloc[0]

dui_label_candidates = [
    "dui_sobriety_label",
    "sobriety_status_label",
    "dui_status_label",
    "dui_label",
]
dui_label_col = next(
    (col for col in dui_label_candidates if col in dui_sobriety_summary.columns),
    dui_sobriety_summary.columns[0]
)
top_dui_label = str(top_dui_row[dui_label_col])
top_dui_count = int(top_dui_row[dui_count_col])

# ============================================================
# KPI row
# ============================================================

kpi_col_1, kpi_col_2, kpi_col_3, kpi_col_4 = st.columns(4)

kpi_col_1.metric("Fatal Collisions", f"{fatal_collisions:,}")
kpi_col_2.metric("Severe Injury Collisions", f"{severe_collisions:,}")
kpi_col_3.metric("Non-Injury Share", f"{non_injury_share:.1f}%")
kpi_col_4.metric("Hit-and-Run Share", f"{hit_run_share:.1f}%")

st.markdown("---")

# ============================================================
# Severity distribution
# ============================================================

st.subheader("Injury Severity Distribution")

severity_chart_df = (
    injury_severity_summary.sort_values("injury_severity_order")
    [["injury_severity_label", injury_count_col]]
    .set_index("injury_severity_label")
)

st.bar_chart(severity_chart_df)

# ============================================================
# Hit-and-run and DUI charts
# ============================================================

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Hit-and-Run Breakdown")

    hit_run_chart_df = (
        hit_run_summary
        [["hit_run_status_label", hit_run_count_col]]
        .sort_values(hit_run_count_col, ascending=False)
        .set_index("hit_run_status_label")
    )

    st.bar_chart(hit_run_chart_df)

    hit_run_display_cols = [
        col for col in [
            "hit_run_status_label",
            "collision_count",
            "mo_row_count",
            "collision_pct_within_hit_run_statuses",
            "collision_pct_of_traffic_only_collisions",
            "status_rank_by_collision_count",
        ]
        if col in hit_run_summary.columns
    ]
    st.dataframe(
        hit_run_summary.sort_values(hit_run_count_col, ascending=False)[hit_run_display_cols].reset_index(drop=True),
        use_container_width=True
    )

with right_col:
    st.subheader("DUI / Sobriety Summary")

    dui_chart_df = (
        dui_sobriety_summary
        [[dui_label_col, dui_count_col]]
        .sort_values(dui_count_col, ascending=False)
        .set_index(dui_label_col)
    )

    st.bar_chart(dui_chart_df)

    st.dataframe(
        dui_sobriety_summary.sort_values(dui_count_col, ascending=False).reset_index(drop=True),
        use_container_width=True
    )

# ============================================================
# Summary tables
# ============================================================

left_col_2, right_col_2 = st.columns(2)

with left_col_2:
    st.subheader("Severity Summary Table")
    severity_display_cols = [
        col for col in [
            "injury_severity_order",
            "injury_severity_label",
            "collision_count",
            "mo_row_count",
            "collision_pct_within_injury_severity",
            "collision_pct_of_traffic_only_collisions",
            "severity_rank_by_collision_count",
        ]
        if col in injury_severity_summary.columns
    ]
    st.dataframe(
        injury_severity_summary.sort_values("injury_severity_order")[severity_display_cols].reset_index(drop=True),
        use_container_width=True
    )

with right_col_2:
    st.subheader("Key Risk Signals")

    risk_signal_table = pd.DataFrame([
        {
            "risk_signal": "Top Hit-and-Run Status",
            "value": top_hit_run_label,
            "supporting_count": top_hit_run_count,
        },
        {
            "risk_signal": "Top DUI / Sobriety Status",
            "value": top_dui_label,
            "supporting_count": top_dui_count,
        },
        {
            "risk_signal": "Fatal Collisions",
            "value": "Fatal injury",
            "supporting_count": fatal_collisions,
        },
        {
            "risk_signal": "Severe Injury Collisions",
            "value": "Severe injury",
            "supporting_count": severe_collisions,
        },
    ])
    st.dataframe(risk_signal_table, use_container_width=True)

# ============================================================
# Data note
# ============================================================

st.markdown("---")
st.info(
    "This page uses severity, hit-and-run, and DUI/sobriety summary datasets prepared in the analytical pipeline. "
    "It is designed to highlight the main risk signals and severity distribution patterns in traffic-only collisions."
)