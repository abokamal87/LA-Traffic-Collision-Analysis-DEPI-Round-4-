# LA Traffic Collision Intelligence Project

## From Raw Los Angeles Collision Records to SQL Modeling, BI Dashboards, Streamlit Analytics, and Future Prediction

---

## Project Tagline

**Turning raw traffic collision records into structured, explainable, and dashboard-ready intelligence.**

---

## 1. Executive Summary

The **LA Traffic Collision Intelligence Project** is an end-to-end data analytics and business intelligence project focused on transforming raw Los Angeles traffic collision records into clean analytical datasets, SQL-ready structures, interactive dashboards, and future prediction-ready outputs.

The project started with a large raw traffic collision dataset containing more than **621,000 records** and **18 original columns**. One of the most important fields in the dataset is the **MO Codes** column, which contains coded information describing collision-related circumstances and context.

To make the MO Codes useful for analysis, the team used an official MO codes dictionary and created a custom **MO Codes Classification** layer. This layer transforms raw MO codes into readable analytical domains, categories, subcategories, and dashboard-friendly labels.

The project currently includes:

- Python data preparation and analysis workflow
- MO code classification and engineering
- cleaned analytical datasets
- dashboard-ready summary outputs
- SQLite analytical database implementation
- SQL schema, indexes, views, and sample queries
- multi-page Streamlit dashboard
- five Tableau dashboards
- professional documentation for GitHub and academic submission
- planned Excel dashboards, Power BI dashboards, and prediction model extension

---

## 2. Project Objectives

The main objectives of this project are to:

1. transform raw collision records into a clean and trusted analytical base
2. validate data quality before analysis and dashboarding
3. convert raw MO codes into meaningful analytical categories
4. build reusable outputs for SQL, Tableau, Power BI, Excel, and Streamlit
5. implement a structured SQLite analytical database
6. create interactive dashboards for visual exploration and storytelling
7. prepare the project for future prediction and risk intelligence
8. deliver professional GitHub-ready documentation

---

## 3. Initial Project Inputs

The project started with three main input files.

| Input File | Description | Purpose |
|---|---|---|
| Traffic Collision Dataset | Large raw dataset with 621,000+ collision records and 18 original columns | Main analytical source |
| Official MO Codes Dictionary | Reference file containing official MO code meanings | Used to interpret raw MO code values |
| MO Codes Classification File | Custom file created by the project team | Converts MO codes into analytical domains, categories, subcategories, and dashboard-ready labels |

---

## 4. Project Workflow

The implemented workflow consists of five core data preparation and analysis stages followed by SQL implementation and dashboard development.

```text
1. Data Audit & Profiling
2. Data Cleaning & Standardization
3. MO Codes Engineering
4. Exploratory Data Analysis
5. Aggregation & Export Layer
6. SQLite Analytical Database Implementation
7. Streamlit Dashboard Application
8. Tableau Dashboard Development
9. Planned Excel Dashboards
10. Planned Power BI Dashboards
11. Planned Prediction Model and Streamlit Extension
```

---

## 5. Methodology Overview

## Phase 1 — Data Audit & Profiling

This phase established the raw-data baseline before cleaning or modeling.

Key activities included:

- loading and validating source files
- reviewing schema and data types
- checking missing values
- checking duplicate rows and duplicate identifiers
- auditing date coverage
- reviewing time field readiness
- checking coordinate quality
- reviewing raw MO code availability
- testing MO mapping readiness

Key result:

- raw collision dataset loaded successfully with more than **621,000 records**

---

## Phase 2 — Data Cleaning & Standardization

This phase converted raw records into a trusted analytical base.

Key activities included:

- standardizing column names
- parsing and validating dates
- deriving time-based fields
- cleaning text fields
- validating victim demographic fields
- validating premise fields
- parsing latitude and longitude
- validating coordinate readiness
- creating supporting dimensions

Main outputs include:

- `collisions_clean.csv`
- `dim_date.csv`
- `dim_area.csv`
- `dim_premise.csv`

---

## Phase 3 — MO Codes Engineering

This phase transformed the raw MO Codes field into a structured analytical layer.

Key activities included:

- identifying records with MO codes
- splitting multi-value MO fields into individual codes
- creating a collision-to-MO bridge table
- joining MO codes to the custom classification layer
- creating a classified MO dimension table
- identifying unmapped MO codes
- creating MO analytical summaries

Main outputs include:

- `bridge_collision_mo.csv`
- `dim_mo_codes.csv`
- `fact_collision_mo_enriched.csv`
- `mo_unmapped_codes.csv`
- `mo_mapping_quality_report.csv`

---

## Phase 4 — Exploratory Data Analysis

This phase created the main analytical story of the project.

Analysis areas included:

- yearly and monthly trends
- weekday and hourly patterns
- geographic distribution
- premise analysis
- injury severity
- hit-and-run indicators
- DUI/sobriety indicators
- victim age, sex, and descent
- vulnerable road users
- MO analytical domains, categories, and subcategories

---

## Phase 5 — Aggregation & Export Layer

This phase created governed outputs for dashboarding, SQL implementation, and BI tools.

Representative outputs include:

- `yearly_summary.csv`
- `monthly_summary.csv`
- `weekday_hour_summary.csv`
- `area_summary.csv`
- `reporting_division_summary.csv`
- `premise_summary_non_street.csv`
- `injury_severity_summary.csv`
- `hit_run_summary.csv`
- `dui_sobriety_summary.csv`
- `victim_age_group_summary.csv`
- `victim_sex_summary.csv`
- `victim_descent_summary.csv`
- `vulnerable_users_summary.csv`
- `mo_analytical_domain_summary.csv`
- `mo_analytical_category_summary.csv`
- `mo_analytical_subcategory_summary.csv`
- `traffic_only_mo_domain_summary.csv`
- `traffic_only_mo_subcategory_summary.csv`
- `map_collision_points.csv`
- `map_hotspots_by_coordinate.csv`

Output folders are prepared for:

- Excel
- SQL
- Tableau
- Power BI
- Streamlit usage

---

## 6. SQLite Analytical Database

The project includes a direct SQLite implementation using the cleaned and SQL-ready outputs.

### Database Purpose

The SQLite database provides a structured analytical model that supports SQL querying, validation, and reusable views.

### Core Tables

| Table | Type | Purpose |
|---|---|---|
| `fact_collisions` | Fact table | Stores cleaned collision-level records |
| `dim_date` | Dimension table | Supports time-based analysis |
| `dim_area` | Dimension table | Supports area-level analysis |
| `dim_premise` | Dimension table | Supports premise and scene-context analysis |
| `dim_mo_codes` | Dimension table | Stores classified MO code metadata |
| `bridge_collision_mo` | Bridge table | Supports many-to-many collision-to-MO relationships |

### SQL Deliverables

- SQLite database file
- schema creation scripts
- index scripts
- analytical views
- validation queries
- sample business queries

---

## 7. Streamlit Dashboard Application

The project includes a multi-page Streamlit dashboard application.

### Streamlit Pages

| Page | Purpose |
|---|---|
| Executive Overview | High-level KPIs, annual trend, top area, severity, hit-and-run, vulnerable users |
| Time Analysis | Yearly, monthly, weekday, and hourly collision patterns |
| Location Analysis | Area ranking, reporting divisions, hotspot map, and premise analysis |
| Risk and Severity | Fatal, severe, non-injury, hit-and-run, and DUI/sobriety indicators |
| MO Analysis | MO domain, category, subcategory, and traffic-only analysis |
| Victim Profile | Victim age group, sex, descent, and vulnerable user analysis |

### Streamlit App Structure

```text
streamlit_app/
├── app.py
├── utils/
│   ├── loaders.py
│   └── formatters.py
└── pages/
    ├── executive_overview.py
    ├── time_analysis.py
    ├── location_analysis.py
    ├── risk_severity.py
    ├── mo_analysis.py
    └── victim_profile.py
```

### How to Run

From the Streamlit app directory:

```bash
streamlit run app.py
```

---

## 8. Tableau Dashboard Layer

Five Tableau dashboards have been created as functional BI dashboards.

| Dashboard | Status |
|---|---|
| Executive Overview | Functional — final formatting pending |
| Time Intelligence | Functional — final formatting pending |
| Geographic Hotspots & Area Explorer | Functional — final formatting pending |
| Victim Demographics Explorer | Functional — final formatting pending |
| MO Intelligence & Collision Pattern Explorer | Functional — final formatting pending |

The Tableau dashboards use the governed Tableau-ready CSV outputs generated from the aggregation and export layer.

---

## 9. Planned Extensions

The project roadmap includes the following planned extensions:

| Planned Work | Description | Owner(s) |
|---|---|---|
| Excel Dashboards | Build lightweight Excel dashboards using prepared summary outputs | Aml Eid Khalil |
| Power BI Dashboards | Build interactive Power BI dashboards using prepared BI outputs | Aml Eid Khalil, Nada Hany, Said Allam |
| Tableau Final Formatting | Improve layout, spacing, styling, labels, and final storytelling quality | Mariam El-Shazly, Nada Hany, Said Allam |
| Prediction Model | Build a machine learning model for future risk intelligence | Mahmoud Awad |
| Streamlit Prediction Extension | Add prediction results or prediction interface to the Streamlit app | Mohamed Kamal, Mahmoud Awad |
| Final Presentation | Prepare project storytelling and final delivery slides | Aml Eid Khalil, Mohamed Kamal |

---

## 10. Team Members and Responsibilities

| Team Member | Main Responsibility |
|---|---|
| Mohamed Kamal | Team Leader, Python pipeline, SQL implementation, documentation supervision, GitHub delivery |
| Aml Eid Khalil | Excel dashboards, Power BI dashboards, final presentation preparation |
| Mariam El-Shazly | Tableau dashboard development and BI visual storytelling |
| Mahmoud Awad | Prediction model and machine learning extension |
| Nada Hany | Power BI dashboard development and Tableau support |
| Said Allam | Power BI dashboard development and Tableau support |
| Full Team | MO Codes Classification review, interpretation, validation, and analytical grouping |

---

## 11. Repository Structure

Recommended repository structure:

```text
project_root/
├── data/
│   ├── raw/
│   └── cleaned/
├── notebooks/
│   ├── 01_data_audit_and_profiling.ipynb
│   ├── 02_data_cleaning_and_standardization.ipynb
│   ├── 03_mo_codes_engineering.ipynb
│   ├── 04_exploratory_data_analysis.ipynb
│   └── 05_aggregation_and_export_layer.ipynb
├── database/
│   └── la_traffic_collision.db
├── sql/
│   ├── create_tables_sqlite.sql
│   ├── index_recommendations_sqlite.sql
│   ├── analytical_views.sql
│   ├── sqlite_setup.sql
│   ├── schema_definition.sql
│   └── sample_queries.sql
├── outputs/
│   ├── excel_ready/
│   ├── sql_ready/
│   ├── tableau_ready/
│   ├── powerbi_ready/
│   ├── reports/
│   └── tables/
├── tableau/
│   ├── dashboard_01_executive_overview.twbx
│   ├── dashboard_02_time_intelligence.twbx
│   ├── dashboard_03_geographic_hotspots.twbx
│   ├── dashboard_04_victim_demographics.twbx
│   └── dashboard_05_mo_intelligence.twbx
├── streamlit_app/
│   ├── app.py
│   ├── utils/
│   │   ├── loaders.py
│   │   └── formatters.py
│   └── pages/
│       ├── executive_overview.py
│       ├── time_analysis.py
│       ├── location_analysis.py
│       ├── risk_severity.py
│       ├── mo_analysis.py
│       └── victim_profile.py
├── docs/
│   ├── 01_project_planning_and_management.md
│   ├── 02_literature_review.md
│   ├── 03_requirements_gathering.md
│   ├── 04_system_analysis_and_design.md
│   └── submission_01_summary.md
└── README.md
```

---

## 12. Submission 01 Documentation

The repository includes the required documentation for the first Graduation Project submission.

| Documentation File | Purpose |
|---|---|
| `docs/01_project_planning_and_management.md` | Project idea, objectives, scope, timeline, roles, risks, KPIs, and deliverables |
| `docs/02_literature_review.md` | Background review for traffic collision analysis, road safety analytics, MO code interpretation, SQL, dashboards, and prediction |
| `docs/03_requirements_gathering.md` | Stakeholders, user needs, user stories, use cases, functional and non-functional requirements |
| `docs/04_system_analysis_and_design.md` | Problem statement, architecture, data flow, database design, dashboard design, and system components |
| `docs/submission_01_summary.md` | Summary of the first official documentation submission |

---

## 13. Current Project Status

### Completed

- raw data audit and profiling
- data cleaning and standardization
- MO codes classification and engineering
- exploratory data analysis
- aggregation and export layer
- SQLite analytical database implementation
- SQL views and sample queries
- Streamlit dashboard application
- five functional Tableau dashboards
- first submission documentation package

### In Progress

- final formatting of Tableau dashboards
- GitHub repository organization
- final documentation review

### Planned

- Excel dashboards
- Power BI dashboards
- prediction model
- prediction integration into Streamlit
- final testing and validation report
- final presentation

---

## 14. Key Strengths

### 1. End-to-End Analytics Workflow

The project covers the full workflow from raw data understanding to dashboards and future prediction planning.

### 2. Strong MO Code Methodology

The project transforms raw coded MO values into readable analytical domains, categories, subcategories, and dashboard labels.

### 3. Multi-Tool Delivery

The project supports Python, SQLite, Tableau, Streamlit, Excel, and Power BI.

### 4. SQL Implementation

The project includes a real SQLite analytical database with fact, dimension, bridge, and view structures.

### 5. Dashboard-Ready Design

The project creates governed summary outputs that can be reused across multiple BI tools.

### 6. Scalable Future Extension

The project is prepared for future prediction modeling and Streamlit integration.

---

## 15. Risks and Limitations

| Risk / Limitation | Mitigation |
|---|---|
| Raw data quality issues | Data audit, cleaning, and validation workflow |
| MO code ambiguity | Official dictionary and custom MO classification layer |
| Missing MO codes | MO coverage analysis and separate interpretation |
| Geographic coordinate issues | Coordinate validation and hotspot-ready outputs |
| Partial-year distortion | Complete-year logic and clear interpretation notes |
| Dashboard performance with large data | Use of pre-aggregated dashboard-ready outputs |
| Prediction uncertainty | Planned model evaluation and careful interpretation |
| Documentation mismatch risk | Documentation aligned with actual implemented workflow |

---

## 16. Future Opportunities

Future enhancements may include:

- collision severity prediction
- hotspot recurrence prediction
- area-level risk scoring
- vulnerable-user risk analysis
- Power BI deployment
- Streamlit deployment
- dashboard export functions
- automated data quality checks
- direct database-backed dashboard connection

---

## 17. Conclusion

The **LA Traffic Collision Intelligence Project** demonstrates how raw traffic collision records can be transformed into a structured analytics and decision-support system.

The project combines:

- data auditing
- data cleaning
- MO code interpretation
- exploratory analysis
- SQL modeling
- dashboard-ready aggregation
- Tableau dashboards
- Streamlit analytics
- planned Excel and Power BI dashboards
- planned prediction modeling
- professional documentation

This makes the project a complete and scalable analytics solution rather than a simple one-time analysis.

