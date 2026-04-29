import streamlit as st
import pandas as pd

from utils.loaders import load_many_datasets

# ============================================================
# Page config
# ============================================================

st.title("Victim Profile")
st.caption(
    "Victim segmentation and vulnerable road user review across age groups, sex, descent, "
    "and vulnerable-user categories."
)

# ============================================================
# Load datasets
# ============================================================

required_datasets = load_many_datasets([
    "victim_age_group_summary",
    "victim_sex_summary",
    "victim_descent_summary",
    "vulnerable_users_summary",
])

victim_age_group_summary = required_datasets["victim_age_group_summary"].copy()
victim_sex_summary = required_datasets["victim_sex_summary"].copy()
victim_descent_summary = required_datasets["victim_descent_summary"].copy()
vulnerable_users_summary = required_datasets["vulnerable_users_summary"].copy()

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


def is_metric_like_column(column_name: str) -> bool:
    lower_col = column_name.lower()
    metric_tokens = [
        "count",
        "pct",
        "percent",
        "rate",
        "rank",
        "order",
        "share",
        "flag",
        "quality",
        "row",
    ]
    return any(token in lower_col for token in metric_tokens)


def find_best_label_column(df: pd.DataFrame, preferred_candidates: list[str]) -> str | None:
    for col in preferred_candidates:
        if col in df.columns:
            return col

    object_like_candidates = [
        col for col in df.columns
        if not is_metric_like_column(col) and df[col].dtype == "object"
    ]
    if object_like_candidates:
        return object_like_candidates[0]

    fallback_candidates = [
        col for col in df.columns
        if not is_metric_like_column(col)
    ]
    if fallback_candidates:
        return fallback_candidates[0]

    return None


def clean_string_series(series: pd.Series) -> pd.Series:
    cleaned = series.astype(str).str.strip()
    cleaned = cleaned.replace(
        {
            "nan": "Unknown / Invalid",
            "None": "Unknown / Invalid",
            "": "Unknown / Invalid",
        }
    )
    return cleaned


def is_numeric_like_label_series(series: pd.Series) -> bool:
    test_series = clean_string_series(series)
    return test_series.str.fullmatch(r"\d+(\.0+)?").all()


def build_display_label(
    df: pd.DataFrame,
    preferred_candidates: list[str],
    order_col: str | None = None,
    fallback_prefix: str = "Group",
) -> pd.Series:
    label_col = find_best_label_column(df, preferred_candidates)

    if label_col is not None:
        label_series = clean_string_series(df[label_col])

        # Use real text labels directly when available
        if not is_numeric_like_label_series(label_series):
            return label_series

        # If the label column contains sex codes like M/F/X/U, translate them
        unique_labels = set(label_series.dropna().unique().tolist())
        sex_code_map = {
            "M": "Male",
            "F": "Female",
            "X": "Other / Unknown",
            "U": "Unknown / Invalid",
        }
        if unique_labels.issubset(set(sex_code_map.keys())):
            return label_series.map(sex_code_map).fillna(label_series)

    if order_col is not None and order_col in df.columns:
        def map_order_value(x):
            if pd.isna(x):
                return "Unknown / Invalid"

            x_str = str(x).strip()
            if x_str in {"99", "999", "Unknown", "Unknown / Invalid"}:
                return "Unknown / Invalid"

            try:
                x_int = int(float(x))
                return f"{fallback_prefix} {x_int}"
            except Exception:
                return f"{fallback_prefix} {x_str}"

        return df[order_col].apply(map_order_value)

    return pd.Series(
        [f"{fallback_prefix} {i + 1}" for i in range(len(df))],
        index=df.index
    )


def prefer_valid_rows(df: pd.DataFrame, display_label_col: str, rank_candidates: list[str]) -> pd.DataFrame:
    for col in rank_candidates:
        if col in df.columns:
            valid_view = df.loc[df[col].notna()].copy()
            if not valid_view.empty:
                return valid_view

    non_unknown_view = df.loc[df[display_label_col] != "Unknown / Invalid"].copy()
    if not non_unknown_view.empty:
        return non_unknown_view

    return df.copy()


# ============================================================
# Column detection
# ============================================================

age_count_col = detect_count_column(victim_age_group_summary)
sex_count_col = detect_count_column(victim_sex_summary)
descent_count_col = detect_count_column(victim_descent_summary)
vulnerable_count_col = detect_count_column(vulnerable_users_summary)

age_label_col = find_best_label_column(
    victim_age_group_summary,
    ["victim_age_group", "age_group", "victim_age_group_label"]
) or victim_age_group_summary.columns[0]

vulnerable_label_col = find_best_label_column(
    vulnerable_users_summary,
    ["vulnerable_user_group", "user_group", "group_label", "vulnerable_user_label"]
) or vulnerable_users_summary.columns[0]

# Build better display labels for sex and descent
victim_sex_summary["sex_display_label"] = build_display_label(
    victim_sex_summary,
    preferred_candidates=[
        "victim_sex",
        "victim_sex_label",
        "sex_label",
        "victim_sex_group",
        "victim_sex_group_label",
        "sex_group",
    ],
    order_col="victim_sex_group_order",
    fallback_prefix="Sex Group",
)

victim_descent_summary["descent_display_label"] = build_display_label(
    victim_descent_summary,
    preferred_candidates=[
        "victim_descent",
        "victim_descent_label",
        "descent_label",
        "victim_descent_group",
        "victim_descent_group_label",
        "descent_group",
    ],
    order_col="victim_descent_group_order",
    fallback_prefix="Descent Group",
)

# ============================================================
# Filter valid-age rows for ranking
# ============================================================

if "age_data_quality_flag" in victim_age_group_summary.columns:
    age_valid_view = victim_age_group_summary.loc[
        victim_age_group_summary["age_data_quality_flag"] == "Valid Age"
    ].copy()
else:
    age_valid_view = victim_age_group_summary.copy()

# Prefer valid/non-unknown rows for KPI ranking
sex_valid_view = prefer_valid_rows(
    victim_sex_summary,
    "sex_display_label",
    ["sex_rank_valid_only"]
)

descent_valid_view = prefer_valid_rows(
    victim_descent_summary,
    "descent_display_label",
    ["descent_rank_valid_only"]
)

# ============================================================
# KPI logic
# ============================================================

top_age_row = age_valid_view.sort_values(age_count_col, ascending=False).iloc[0]
top_age_group = str(top_age_row[age_label_col])
top_age_count = int(top_age_row[age_count_col])

top_sex_row = sex_valid_view.sort_values(sex_count_col, ascending=False).iloc[0]
top_sex_value = str(top_sex_row["sex_display_label"])
top_sex_count = int(top_sex_row[sex_count_col])

top_descent_row = descent_valid_view.sort_values(descent_count_col, ascending=False).iloc[0]
top_descent_value = str(top_descent_row["descent_display_label"])
top_descent_count = int(top_descent_row[descent_count_col])

vulnerable_user_total = int(vulnerable_users_summary[vulnerable_count_col].sum())

# ============================================================
# KPI row
# ============================================================

kpi_col_1, kpi_col_2, kpi_col_3, kpi_col_4 = st.columns(4)

kpi_col_1.metric("Top Age Group", top_age_group, delta=f"{top_age_count:,} collisions")
kpi_col_2.metric("Top Victim Sex", top_sex_value, delta=f"{top_sex_count:,} collisions")
kpi_col_3.metric("Top Victim Descent", top_descent_value, delta=f"{top_descent_count:,} collisions")
kpi_col_4.metric("Vulnerable User Collisions", f"{vulnerable_user_total:,}")

st.markdown("---")

# ============================================================
# Age group analysis
# ============================================================

st.subheader("Victim Age Group Distribution")

age_chart_df = (
    age_valid_view.sort_values(age_count_col, ascending=False)
    [[age_label_col, age_count_col]]
    .set_index(age_label_col)
)

st.bar_chart(age_chart_df)

age_display_cols = [
    col for col in [
        "victim_age_group_order",
        "victim_age_group",
        "age_data_quality_flag",
        "collision_count",
        "collision_pct_total",
        "collision_pct_valid_age_only",
        "age_group_rank_valid_only",
    ]
    if col in victim_age_group_summary.columns
]

st.dataframe(
    victim_age_group_summary.reset_index(drop=True)[age_display_cols],
    use_container_width=True,
)

# ============================================================
# Sex and descent analysis
# ============================================================

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Victim Sex Distribution")

    sex_chart_df = (
        victim_sex_summary
        .sort_values(sex_count_col, ascending=False)
        [["sex_display_label", sex_count_col]]
        .set_index("sex_display_label")
    )

    st.bar_chart(sex_chart_df)

    sex_display_cols = [
        col for col in [
            "sex_display_label",
            "collision_count",
            "collision_pct_total",
            "collision_pct_valid_sex_only",
            "sex_rank_valid_only",
        ]
        if col in victim_sex_summary.columns
    ]
    st.dataframe(
        victim_sex_summary.sort_values(sex_count_col, ascending=False)[sex_display_cols].reset_index(drop=True),
        use_container_width=True,
    )

with right_col:
    st.subheader("Victim Descent Distribution")

    descent_chart_df = (
        victim_descent_summary
        .sort_values(descent_count_col, ascending=False)
        .head(15)
        [["descent_display_label", descent_count_col]]
        .set_index("descent_display_label")
    )

    st.bar_chart(descent_chart_df)

    descent_display_cols = [
        col for col in [
            "descent_display_label",
            "collision_count",
            "collision_pct_total",
            "collision_pct_valid_descent_only",
            "descent_rank_valid_only",
        ]
        if col in victim_descent_summary.columns
    ]
    st.dataframe(
        victim_descent_summary.sort_values(descent_count_col, ascending=False)[descent_display_cols].reset_index(drop=True),
        use_container_width=True,
    )

# ============================================================
# Vulnerable users and key signals
# ============================================================

left_col_2, right_col_2 = st.columns(2)

with left_col_2:
    st.subheader("Vulnerable User Summary")

    vulnerable_chart_df = (
        vulnerable_users_summary
        .sort_values(vulnerable_count_col, ascending=False)
        [[vulnerable_label_col, vulnerable_count_col]]
        .set_index(vulnerable_label_col)
    )

    st.bar_chart(vulnerable_chart_df)
    st.dataframe(vulnerable_users_summary.reset_index(drop=True), use_container_width=True)

with right_col_2:
    st.subheader("Key Victim Signals")

    victim_signal_table = pd.DataFrame([
        {
            "signal_name": "Top Age Group",
            "value": top_age_group,
            "supporting_count": top_age_count,
        },
        {
            "signal_name": "Top Victim Sex",
            "value": top_sex_value,
            "supporting_count": top_sex_count,
        },
        {
            "signal_name": "Top Victim Descent",
            "value": top_descent_value,
            "supporting_count": top_descent_count,
        },
        {
            "signal_name": "Vulnerable User Collisions",
            "value": "Pedestrian + Bicycle related",
            "supporting_count": vulnerable_user_total,
        },
    ])
    st.dataframe(victim_signal_table, use_container_width=True)

# ============================================================
# Data note
# ============================================================

st.markdown("---")
st.info(
    "This page uses victim age, sex, descent, and vulnerable user summary datasets prepared in the analytical pipeline. "
    "It is designed to highlight the main victim segmentation patterns in traffic collision reporting."
)