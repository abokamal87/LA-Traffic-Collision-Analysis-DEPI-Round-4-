from pathlib import Path
import streamlit as st

# ============================================================
# App configuration
# ============================================================

st.set_page_config(
    page_title="LA Traffic Collision Intelligence Project",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# Project paths
# ============================================================

APP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = APP_DIR.parent
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
TABLEAU_READY_DIR = OUTPUTS_DIR / "tableau_ready"
POWERBI_READY_DIR = OUTPUTS_DIR / "powerbi_ready"

# ============================================================
# Navigation
# ============================================================

pages = [
    st.Page(
        str(APP_DIR / "pages" / "executive_overview.py"),
        title="Executive Overview",
        icon="📊",
        default=True,
    ),
    st.Page(
        str(APP_DIR / "pages" / "time_analysis.py"),
        title="Time Analysis",
        icon="⏱️",
    ),
    st.Page(
        str(APP_DIR / "pages" / "location_analysis.py"),
        title="Location Analysis",
        icon="📍",
    ),
    st.Page(
        str(APP_DIR / "pages" / "risk_severity.py"),
        title="Risk and Severity",
        icon="⚠️",
    ),
    st.Page(
        str(APP_DIR / "pages" / "mo_analysis.py"),
        title="MO Analysis",
        icon="🧩",
    ),
    st.Page(
        str(APP_DIR / "pages" / "victim_profile.py"),
        title="Victim Profile",
        icon="👤",
    ),
]

pg = st.navigation(pages, position="sidebar")
pg.run()

# ============================================================
# Sidebar footer
# ============================================================

with st.sidebar:
    st.markdown("---")
    st.caption("LA Traffic Collision Intelligence Project")
    st.caption("Dashboard App Skeleton")