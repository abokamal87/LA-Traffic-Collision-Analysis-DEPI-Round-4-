import streamlit as st
import pandas as pd

from utils.loaders import load_many_datasets
from utils.formatters import (
    format_count,
    format_percent,
    shorten_label,
)

# ============================================================
# Page config
# ============================================================

st.title("MO Analysis")
st.caption(
    "Analytical interpretation of traffic-related and broader MO-coded collision patterns."
)

# ============================================================
# Load datasets
# ============================================================

required_datasets = load_many_datasets([
    "mo_analytical_domain_summary",
    "mo_analytical_category_summary",
    "mo_analytical_subcategory_summary",
    "traffic_only_mo_domain_summary",
    "traffic_only_mo_subcategory_summary",
])

mo_analytical_domain_summary = required_datasets["mo_analytical_domain_summary"].copy()
mo_analytical_category_summary = required_datasets["mo_analytical_category_summary"].copy()
mo_analytical_subcategory_summary = required_datasets["mo_analytical_subcategory_summary"].copy()
traffic_only_mo_domain_summary = required_datasets["traffic_only_mo_domain_summary"].copy()
traffic_only_mo_subcategory_summary = required_datasets["traffic_only_mo_subcategory_summary"].copy()

# ============================================================
# Helper functions
# ============================================================

def safe_top_row(df: pd.DataFrame, sort_col: str) -> pd.Series | None:
    if df.empty or sort_col not in df.columns:
        return None
    return df.sort_values(sort_col, ascending=False).iloc[0]

# ============================================================
# Focus mode
# ============================================================

focus_mode = st.radio(
    "MO Analysis Focus",
    options=["Traffic-Only Focus", "All MO Summaries"],
    horizontal=True,
)

if focus_mode == "Traffic-Only Focus":
    domain_df = traffic_only_mo_domain_summary.copy()
    subcategory_df = traffic_only_mo_subcategory_summary.copy()
    category_df = None
else:
    domain_df = mo_analytical_domain_summary.copy()
    subcategory_df = mo_analytical_subcategory_summary.copy()
    category_df = mo_analytical_category_summary.copy()

# ============================================================
# KPI logic
# ============================================================

top_domain_row = safe_top_row(domain_df, "collision_count")
top_subcategory_row = safe_top_row(subcategory_df, "collision_count")

domain_count = int(domain_df.shape[0])
subcategory_count = int(subcategory_df.shape[0])

top_domain_name = str(top_domain_row["analytical_domain"]) if top_domain_row is not None else "N/A"
top_domain_collisions = int(top_domain_row["collision_count"]) if top_domain_row is not None else 0
top_domain_coverage = (
    float(top_domain_row["collision_coverage_rate"])
    if top_domain_row is not None and "collision_coverage_rate" in top_domain_row.index
    else None
)

top_subcategory_name = (
    str(top_subcategory_row["analytical_subcategory"])
    if top_subcategory_row is not None and "analytical_subcategory" in top_subcategory_row.index
    else "N/A"
)
top_subcategory_collisions = int(top_subcategory_row["collision_count"]) if top_subcategory_row is not None else 0

# ============================================================
# KPI row
# ============================================================

kpi_col_1, kpi_col_2, kpi_col_3, kpi_col_4 = st.columns(4)

kpi_col_1.metric("Domains in Scope", format_count(domain_count))
kpi_col_2.metric("Subcategories in Scope", format_count(subcategory_count))
kpi_col_3.metric("Top Domain", top_domain_name, delta=f"{format_count(top_domain_collisions)} collisions")
kpi_col_4.metric("Top Domain Coverage", format_percent(top_domain_coverage))

st.markdown("---")

# ============================================================
# Domain ranking
# ============================================================

st.subheader("Domain Ranking")

domain_chart_view = (
    domain_df.sort_values("collision_count", ascending=False)
    .head(12)
    .copy()
)
domain_chart_view["domain_chart_label"] = domain_chart_view["analytical_domain"].apply(
    lambda x: shorten_label(x, max_len=26)
)

domain_chart_df = domain_chart_view[["domain_chart_label", "collision_count"]].set_index("domain_chart_label")
st.bar_chart(domain_chart_df)

domain_display_cols = [
    col for col in [
        "analytical_domain",
        "collision_count",
        "mo_row_count",
        "collision_coverage_rate",
        "mo_row_share",
        "domain_rank_by_collision_count",
    ]
    if col in domain_df.columns
]

domain_display = (
    domain_df.sort_values("collision_count", ascending=False)[domain_display_cols]
    .reset_index(drop=True)
)

for col in ["collision_count", "mo_row_count", "domain_rank_by_collision_count"]:
    if col in domain_display.columns:
        domain_display[col] = domain_display[col].apply(format_count)

for col in ["collision_coverage_rate", "mo_row_share"]:
    if col in domain_display.columns:
        domain_display[col] = domain_display[col].apply(format_percent)

st.dataframe(domain_display, use_container_width=True)

# ============================================================
# Category ranking (all-MO mode only)
# ============================================================

if category_df is not None:
    st.subheader("Category Ranking")

    category_chart_view = (
        category_df.sort_values("collision_count", ascending=False)
        .head(12)
        .copy()
    )
    category_chart_view["category_chart_label"] = category_chart_view["analytical_category"].apply(
        lambda x: shorten_label(x, max_len=28)
    )

    category_chart_df = (
        category_chart_view[["category_chart_label", "collision_count"]]
        .set_index("category_chart_label")
    )
    st.bar_chart(category_chart_df)

    category_display_cols = [
        col for col in [
            "analytical_domain",
            "analytical_category",
            "collision_count",
            "mo_row_count",
            "collision_coverage_rate",
            "mo_row_share",
            "category_rank_by_collision_count",
        ]
        if col in category_df.columns
    ]

    category_display = (
        category_df.sort_values("collision_count", ascending=False)[category_display_cols]
        .reset_index(drop=True)
    )

    for col in ["collision_count", "mo_row_count", "category_rank_by_collision_count"]:
        if col in category_display.columns:
            category_display[col] = category_display[col].apply(format_count)

    for col in ["collision_coverage_rate", "mo_row_share"]:
        if col in category_display.columns:
            category_display[col] = category_display[col].apply(format_percent)

    st.dataframe(category_display, use_container_width=True)

# ============================================================
# Subcategory analysis
# ============================================================

st.subheader("Subcategory Analysis")

available_domains = (
    sorted(subcategory_df["analytical_domain"].dropna().unique().tolist())
    if "analytical_domain" in subcategory_df.columns
    else []
)

selected_domain = None
if available_domains:
    selected_domain = st.selectbox(
        "Filter Subcategories by Domain",
        options=["All Domains"] + available_domains,
        index=0,
    )

if selected_domain and selected_domain != "All Domains":
    subcategory_view = subcategory_df.loc[
        subcategory_df["analytical_domain"] == selected_domain
    ].copy()
else:
    subcategory_view = subcategory_df.copy()

st.caption(
    f"Showing {'all domains' if selected_domain in [None, 'All Domains'] else selected_domain} "
    f"with subcategories ranked by collision count."
)

subcategory_chart_view = (
    subcategory_view.sort_values("collision_count", ascending=False)
    .head(12)
    .copy()
)
subcategory_chart_view["subcategory_chart_label"] = subcategory_chart_view["analytical_subcategory"].apply(
    lambda x: shorten_label(x, max_len=30)
)

subcategory_chart_df = (
    subcategory_chart_view[["subcategory_chart_label", "collision_count"]]
    .set_index("subcategory_chart_label")
)
st.bar_chart(subcategory_chart_df)

subcategory_display_cols = [
    col for col in [
        "analytical_domain",
        "analytical_category",
        "analytical_subcategory",
        "collision_count",
        "mo_row_count",
        "collision_coverage_rate",
        "mo_row_share",
        "subcategory_rank_by_collision_count",
    ]
    if col in subcategory_view.columns
]

subcategory_display = (
    subcategory_view.sort_values("collision_count", ascending=False)[subcategory_display_cols]
    .reset_index(drop=True)
)

for col in ["collision_count", "mo_row_count", "subcategory_rank_by_collision_count"]:
    if col in subcategory_display.columns:
        subcategory_display[col] = subcategory_display[col].apply(format_count)

for col in ["collision_coverage_rate", "mo_row_share"]:
    if col in subcategory_display.columns:
        subcategory_display[col] = subcategory_display[col].apply(format_percent)

st.dataframe(subcategory_display, use_container_width=True)

# ============================================================
# Key MO signals
# ============================================================

st.subheader("Key MO Signals")

mo_signal_table = pd.DataFrame([
    {
        "signal_name": "Top Domain",
        "value": top_domain_name,
        "supporting_count": format_count(top_domain_collisions),
    },
    {
        "signal_name": "Top Subcategory",
        "value": top_subcategory_name,
        "supporting_count": format_count(top_subcategory_collisions),
    },
    {
        "signal_name": "Domain Count in Scope",
        "value": focus_mode,
        "supporting_count": format_count(domain_count),
    },
    {
        "signal_name": "Subcategory Count in Scope",
        "value": focus_mode,
        "supporting_count": format_count(subcategory_count),
    },
])

st.dataframe(mo_signal_table, use_container_width=True)

# ============================================================
# Data note
# ============================================================

st.markdown("---")
st.info(
    "This page uses domain, category, and subcategory MO summary datasets prepared in the analytical pipeline. "
    "The traffic-only focus highlights the most relevant behavioral and contextual traffic collision patterns, "
    "while the all-MO mode provides a wider analytical reference view."
)