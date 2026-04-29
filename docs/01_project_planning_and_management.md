# 01 — Project Planning & Management

## Project Title

**LA Traffic Collision Intelligence Project**

## Project Tagline

**Turning raw traffic collision records into structured, explainable, and dashboard-ready intelligence.**

---

## 1. Project Overview

The **LA Traffic Collision Intelligence Project** is an end-to-end data analytics and business intelligence project focused on transforming raw Los Angeles traffic collision records into structured insights, analytical datasets, SQL models, and interactive dashboards.

The project started with a large raw traffic collision dataset containing more than **621,000 collision records** and **18 original columns**. One of the most important columns in the dataset was the **MO Codes** column, which contained coded information describing collision-related circumstances and contextual patterns.

To make the dataset more useful for analysis, the team used an official MO codes dictionary and created a custom **MO Codes Classification** file. This classification layer converted raw coded values into clear analytical domains, categories, subcategories, and dashboard-friendly labels.

The project is designed to support multiple analytical and reporting tools, including:

- Python
- SQLite
- Excel
- Tableau
- Power BI
- Streamlit
- Machine Learning / Prediction extension

---

## 2. Project Selection and Idea

Traffic collisions are a major public safety and urban planning concern. Large public collision datasets often contain valuable information, but they are usually difficult to interpret directly because of inconsistent formats, coded fields, missing values, and complex location or time-related patterns.

The team selected this project because it provides a strong opportunity to apply the full data analytics lifecycle:

1. understanding raw public records
2. cleaning and validating data quality
3. engineering meaningful analytical features
4. transforming coded fields into useful categories
5. building SQL-ready data structures
6. designing dashboards for decision support
7. extending the work into prediction and risk intelligence

The core idea is to convert raw traffic collision records into a practical intelligence system that helps users explore:

- collision volume and trends
- time-based collision patterns
- geographic hotspots
- area-level collision concentration
- victim demographics
- injury severity and risk indicators
- hit-and-run and DUI-related patterns
- MO-code-based collision behavior and context

---

## 3. Initial Project Inputs

The project started with three main input files.

| Input File | Description | Source / Ownership | Purpose |
|---|---|---|---|
| Traffic Collision Dataset | Large raw dataset containing collision records, dates, locations, victim details, premise information, and MO codes | Source data | Main analytical dataset |
| Official MO Codes Dictionary | Reference file explaining official MO code meanings | External reference | Used to interpret coded MO values |
| MO Codes Classification File | Custom classification file created by the team | Created by project team | Converts raw MO codes into analytical domains, categories, subcategories, and dashboard-ready labels |

### Initial Data Profile

| Item | Value |
|---|---:|
| Raw collision records | 621,000+ records |
| Original columns | 18 columns |
| Key coded field | MO Codes |
| Official MO reference size | 777 official MO codes |
| Custom analytical layer | MO Codes Classification |

---

## 4. Project Objectives

The main objectives of the project are to:

1. transform raw traffic collision data into a clean analytical dataset
2. validate data quality before analysis and dashboarding
3. make MO codes understandable and useful for analysis
4. create reusable outputs for SQL, Excel, Tableau, Power BI, and Streamlit
5. build an analytical SQLite database
6. develop interactive dashboards for multiple platforms
7. support future prediction and risk-scoring functionality
8. prepare professional documentation suitable for GitHub and academic review

---

## 5. Project Scope

### In Scope

The project includes:

- raw data audit and profiling
- data cleaning and standardization
- MO code classification and engineering
- exploratory data analysis
- dashboard-ready data aggregation
- SQLite database implementation
- SQL schema, indexes, views, and sample queries
- Tableau dashboard development
- Streamlit dashboard development
- planned Excel dashboard development
- planned Power BI dashboard development
- planned prediction model development
- planned prediction integration into Streamlit
- project documentation and final presentation preparation

### Out of Scope for the Current Submission

The current documentation submission does not include final model performance validation or final dashboard deployment because these are planned for later phases of the project.

The current submission focuses on:

- project planning and management
- literature review
- requirements gathering
- system analysis and design

---

## 6. Completed Work

The following work has already been completed:

### Data Preparation and Analysis

- raw data audit and profiling
- data cleaning and standardization
- MO codes engineering
- exploratory data analysis
- aggregation and export layer
- dashboard-ready datasets

### SQL Implementation

- SQLite analytical database implementation
- final SQL-ready tables
- schema creation scripts
- index scripts
- analytical views
- validation queries
- sample business queries

### Streamlit Dashboard

A multi-page Streamlit dashboard has been developed with the following pages:

1. Executive Overview
2. Time Analysis
3. Location Analysis
4. Risk and Severity
5. MO Analysis
6. Victim Profile

### Tableau Dashboards

Five Tableau dashboards have been created as functional BI dashboards and are currently pending final formatting and visual polishing:

1. Executive Overview
2. Time Intelligence
3. Geographic Hotspots & Area Explorer
4. Victim Demographics Explorer
5. MO Intelligence & Collision Pattern Explorer

---

## 7. Planned Work

The following work is planned for the next phases:

| Planned Work | Description | Owner(s) |
|---|---|---|
| Excel Dashboards | Build Excel-based dashboards using prepared summary outputs | Aml Eid Khalil |
| Power BI Dashboards | Build Power BI dashboards for interactive reporting | Aml Eid Khalil, Nada Hany, Said Allam |
| Tableau Final Formatting | Improve visual consistency, layout, spacing, formatting, and final storytelling design | Mariam El-Shazly, Nada Hany, Said Allam |
| Prediction Model | Build a predictive model for future analytical extension | Mahmoud Awad |
| Streamlit Prediction Page | Add prediction results or prediction interface to the existing Streamlit app | Mohamed Kamal, Mahmoud Awad |
| Final Presentation | Prepare final project presentation and storytelling slides | Aml Eid Khalil, Mohamed Kamal |
| Final Documentation | Complete GitHub-ready project documentation | Mohamed Kamal and full team |

---

## 8. Team Roles and Responsibilities

| Team Member | Role / Responsibility |
|---|---|
| Mohamed Kamal | Team Leader; project coordination, workflow planning, quality review, GitHub delivery, documentation supervision, Python pipeline, SQL implementation |
| Aml Eid Khalil | Excel dashboards, Power BI dashboards, final presentation preparation |
| Mariam El-Shazly | Tableau dashboard development and BI visual storytelling |
| Mahmoud Awad | Prediction model development and machine learning extension |
| Nada Hany | Power BI dashboard development and Tableau support |
| Said Allam | Power BI dashboard development and Tableau support |
| Full Team | MO Codes Classification review, interpretation, validation, and analytical grouping |

### Team Leadership

Mohamed Kamal is responsible for coordinating the overall project workflow, ensuring consistency across technical outputs, reviewing deliverables, managing the GitHub submission structure, and supervising final documentation quality.

### MO Codes Classification Collaboration

The **MO Codes Classification** layer was developed collaboratively by the full team because it is one of the most important analytical foundations of the project. The team reviewed raw MO code meanings and transformed them into structured analytical domains, categories, subcategories, and dashboard-ready labels.

---

## 9. Project Milestones

| Milestone | Description | Status |
|---|---|---|
| M1 — Project Selection | Select project topic, define problem, and identify data source | Completed |
| M2 — Data Understanding | Review raw dataset structure, columns, quality, and MO code presence | Completed |
| M3 — MO Classification | Build custom MO classification layer | Completed |
| M4 — Data Cleaning | Clean and standardize collision data | Completed |
| M5 — MO Engineering | Normalize MO codes and create analytical MO structures | Completed |
| M6 — EDA | Generate exploratory analysis and insight summaries | Completed |
| M7 — Aggregation Layer | Create dashboard-ready and tool-ready output files | Completed |
| M8 — SQLite Implementation | Build and validate SQLite analytical database | Completed |
| M9 — Streamlit Dashboard | Build multi-page interactive Streamlit dashboard | Completed |
| M10 — Tableau Dashboards | Build five Tableau dashboards | In Progress — final formatting pending |
| M11 — Excel Dashboards | Build Excel dashboards | Planned |
| M12 — Power BI Dashboards | Build Power BI dashboards | Planned |
| M13 — Prediction Model | Build machine learning prediction extension | Planned |
| M14 — Final Documentation | Complete all required project documentation | In Progress |
| M15 — Final Presentation | Prepare final presentation and project delivery package | Planned |

---

## 10. High-Level Timeline

| Phase | Work Package | Status |
|---|---|---|
| Phase 1 | Project idea, data selection, and initial planning | Completed |
| Phase 2 | Data audit and profiling | Completed |
| Phase 3 | Data cleaning and standardization | Completed |
| Phase 4 | MO codes classification and engineering | Completed |
| Phase 5 | Exploratory data analysis | Completed |
| Phase 6 | Aggregation and dashboard-ready exports | Completed |
| Phase 7 | SQLite implementation and validation | Completed |
| Phase 8 | Streamlit dashboard development | Completed |
| Phase 9 | Tableau dashboard development | In Progress |
| Phase 10 | Excel dashboard development | Planned |
| Phase 11 | Power BI dashboard development | Planned |
| Phase 12 | Prediction model and Streamlit extension | Planned |
| Phase 13 | Final documentation and presentation | In Progress / Planned |

---

## 11. Deliverables

### Current Deliverables

- cleaned analytical collision dataset
- MO codes classification layer
- normalized MO bridge table
- MO dimension table
- dashboard-ready CSV outputs
- SQLite database
- SQL schema scripts
- SQL index scripts
- SQL analytical views
- SQL sample queries
- Streamlit dashboard application
- Tableau dashboard prototypes
- GitHub-ready README
- project planning documentation

### Planned Deliverables

- Excel dashboards
- Power BI dashboards
- final formatted Tableau dashboards
- prediction model outputs
- prediction page in Streamlit
- final presentation
- final technical report
- user guide
- testing and validation documentation

---

## 12. Risk Assessment and Mitigation Plan

| Risk | Description | Impact | Mitigation |
|---|---|---|---|
| Data Quality Issues | Raw data may contain missing, inconsistent, or invalid values | High | Perform audit, cleaning, validation, and quality checks before analysis |
| MO Code Ambiguity | MO codes may be difficult to interpret without structured grouping | High | Use official dictionary and custom MO classification layer |
| Missing MO Values | Some collision records do not contain MO codes | Medium | Track MO coverage and separate Has MO vs No MO analysis |
| Geographic Data Issues | Some records may have invalid or missing coordinates | High | Validate coordinates and create map-readiness indicators |
| Partial-Year Distortion | Incomplete recent years may distort time trends | Medium | Use complete-year logic and clearly label partial-year data |
| Dashboard Complexity | Too many visuals may reduce dashboard clarity | Medium | Use focused dashboard pages and clear KPI sections |
| Tool Integration Risk | Outputs need to work across SQL, Excel, Tableau, Power BI, and Streamlit | Medium | Create governed export folders and standardized CSV outputs |
| Model Accuracy Risk | Future prediction model may not perform well if features are weak | Medium | Use validated features, clear evaluation metrics, and model testing |
| Schedule Risk | Multiple deliverables across several tools may create time pressure | High | Divide tasks by owner and track milestones clearly |
| Documentation Risk | Technical work may not be clearly communicated | Medium | Maintain structured GitHub documentation and professional reports |

---

## 13. Key Performance Indicators

The project uses the following KPIs to measure success:

| KPI | Measurement Target |
|---|---|
| Data Loading Success | Raw files loaded successfully without critical errors |
| Cleaning Completeness | Cleaned dataset created with validated key fields |
| Duplicate Control | No duplicate primary collision identifiers in the cleaned analytical base |
| MO Mapping Coverage | High percentage of MO entries successfully mapped to analytical classification |
| Coordinate Readiness | High percentage of records prepared for map-based analysis |
| SQL Model Validation | Core tables loaded and relationships validated successfully |
| Dashboard Readiness | Approved summary outputs created for dashboard tools |
| Streamlit Functionality | Multi-page app loads required datasets and displays key analysis views |
| Tableau Completion | Five dashboards created and prepared for final formatting |
| Documentation Readiness | Required documentation files prepared for GitHub submission |

---

## 14. Communication and Collaboration Plan

The project is managed through a team-based workflow where responsibilities are distributed by technical area.

### Collaboration Principles

- each member owns a clear part of the project
- the full team contributes to MO code interpretation and validation
- outputs are reviewed before being used in dashboards
- documentation is aligned with the actual implemented workflow
- GitHub is used as the central delivery location

### Review Approach

Key deliverables are reviewed based on:

- correctness
- completeness
- readability
- dashboard usability
- consistency with project objectives
- readiness for final submission

---

## 15. Current Project Status

The project is currently in an advanced implementation stage.

### Completed

- raw data understanding
- MO code classification
- Python data preparation workflow
- SQLite implementation
- Streamlit dashboard
- initial Tableau dashboards
- initial GitHub documentation structure

### In Progress

- final formatting of Tableau dashboards
- formal project documentation
- GitHub delivery preparation

### Planned

- Excel dashboards
- Power BI dashboards
- prediction model
- Streamlit prediction extension
- final presentation
- final testing and reporting

---

## 16. Summary

This project demonstrates a complete analytics workflow that starts from raw public traffic collision data and moves toward a structured decision-support system.

The project combines data engineering, MO code interpretation, SQL modeling, dashboard development, and future predictive analytics planning. The current work already includes strong analytical foundations, while the next phases will expand the project into Excel, Power BI, prediction modeling, and final presentation delivery.

