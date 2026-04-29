# Submission 01 Summary

## LA Traffic Collision Intelligence Project

---

## 1. Submission Purpose

This document summarizes the first official submission for the **LA Traffic Collision Intelligence Project**.

The purpose of Submission 01 is to provide the required project documentation covering:

1. Project Planning & Management
2. Literature Review
3. Requirements Gathering
4. System Analysis & Design

This submission is prepared for GitHub delivery and LMS submission through the Graduation Project Assignment.

---

## 2. Project Overview

The **LA Traffic Collision Intelligence Project** is an end-to-end data analytics and business intelligence project that transforms raw Los Angeles traffic collision records into structured, explainable, and dashboard-ready intelligence.

The project started with a large raw traffic collision dataset containing more than **621,000 records** and **18 original columns**. One of the key fields in the dataset is the **MO Codes** column, which contains coded collision-related information.

To make the MO Codes useful for analysis, the project team used an official MO codes dictionary and created a custom **MO Codes Classification** file. This classification layer converts raw MO codes into analytical domains, categories, subcategories, and dashboard-friendly labels.

The project supports multiple tools and delivery layers, including:

- Python
- SQLite
- Tableau
- Streamlit
- Excel dashboards — planned
- Power BI dashboards — planned
- Prediction model — planned

---

## 3. Initial Project Inputs

The project started with three main input files:

| Input | Description | Purpose |
|---|---|---|
| Traffic Collision Dataset | Large raw dataset with 621,000+ records and 18 columns | Main analytical source |
| Official MO Codes Dictionary | Reference file explaining official MO codes | Supports MO interpretation |
| MO Codes Classification File | Custom file created by the project team | Converts MO codes into analytical domains, categories, and subcategories |

---

## 4. Current Project Progress

The project has already progressed beyond the initial documentation stage and includes several implemented technical components.

### Completed Work

- raw data audit and profiling
- data cleaning and standardization
- MO code classification and engineering
- exploratory data analysis
- aggregation and export layer
- dashboard-ready output files
- SQLite analytical database implementation
- SQL schema, indexes, views, and sample queries
- multi-page Streamlit dashboard application
- five functional Tableau dashboards
- GitHub-ready documentation structure

### In Progress

- final formatting and visual polishing of Tableau dashboards
- formal GitHub documentation preparation
- LMS submission package preparation

### Planned Work

- Excel dashboards
- Power BI dashboards
- prediction model
- prediction integration into Streamlit
- final testing and validation report
- final presentation

---

## 5. Submitted Documentation Files

The following documentation files are included in this submission:

| File | Purpose |
|---|---|
| `01_project_planning_and_management.md` | Defines the project idea, objectives, scope, team roles, timeline, deliverables, risks, mitigation plan, and KPIs |
| `02_literature_review.md` | Reviews the background concepts related to traffic collision analysis, road safety analytics, MO code interpretation, SQL modeling, dashboards, and prediction |
| `03_requirements_gathering.md` | Defines stakeholders, user needs, user stories, use cases, functional requirements, non-functional requirements, data requirements, dashboard requirements, and acceptance criteria |
| `04_system_analysis_and_design.md` | Defines the problem statement, system objectives, architecture, data flow, database design, dashboard design, technology stack, validation strategy, and future prediction extension |
| `submission_01_summary.md` | Provides this high-level summary of Submission 01 |

---

## 6. Documentation Requirement Mapping

| Official Requirement | Covered In |
|---|---|
| Project Planning & Management | `01_project_planning_and_management.md` |
| Literature Review | `02_literature_review.md` |
| Requirements Gathering | `03_requirements_gathering.md` |
| System Analysis & Design | `04_system_analysis_and_design.md` |

---

## 7. Project Planning & Management Coverage

The project planning and management document includes:

- project title and tagline
- project overview
- project selection and idea
- initial project inputs
- project objectives
- project scope
- completed work
- planned work
- team roles and responsibilities
- project milestones
- high-level timeline
- deliverables
- risk assessment and mitigation plan
- key performance indicators
- communication and collaboration plan
- current project status

---

## 8. Literature Review Coverage

The literature review document includes:

- traffic collision data as a decision-support asset
- data-driven road safety
- Safe System and Vision Zero context
- importance of data quality
- coded fields and MO code interpretation
- multi-value field normalization
- temporal collision analysis
- geographic and hotspot analysis
- injury severity and behavioral risk analysis
- victim demographic analysis
- dashboarding and business intelligence
- SQL and dimensional modeling
- planned predictive analytics extension
- related work and practical references

---

## 9. Requirements Gathering Coverage

The requirements gathering document includes:

- project context
- stakeholder analysis
- internal stakeholders
- academic and evaluation stakeholders
- direct system users
- potential external stakeholders
- indirect public beneficiaries
- user groups
- user needs
- user stories
- use cases
- functional requirements
- non-functional requirements
- data requirements
- dashboard requirements
- system requirements
- acceptance criteria
- requirements traceability matrix

---

## 10. System Analysis & Design Coverage

The system analysis and design document includes:

- purpose of the system design
- problem statement
- system objectives
- system boundary
- high-level architecture
- input data design
- data processing design
- database design
- entity relationship design
- data flow design
- Streamlit application design
- BI dashboard design
- planned prediction model design
- UI/UX design guidelines
- component design
- repository structure
- security, privacy, and ethical considerations
- assumptions and constraints
- validation strategy

---

## 11. Team Roles Summary

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

## 12. Current Technical Deliverables

The current project repository is expected to include:

- project documentation files
- raw and cleaned data folders where applicable
- five data analysis notebooks
- SQL scripts
- SQLite database file
- dashboard-ready output files
- Streamlit application files
- Tableau dashboard files or screenshots
- README file

---

## 13. Recommended GitHub Documentation Structure

```text
project_root/
├── docs/
│   ├── 01_project_planning_and_management.md
│   ├── 02_literature_review.md
│   ├── 03_requirements_gathering.md
│   ├── 04_system_analysis_and_design.md
│   └── submission_01_summary.md
├── notebooks/
├── sql/
├── database/
├── outputs/
├── tableau/
├── streamlit_app/
└── README.md
```

---

## 14. Submission Readiness Checklist

| Item | Status |
|---|---|
| Project planning document prepared | Completed |
| Literature review document prepared | Completed |
| Requirements gathering document prepared | Completed |
| System analysis and design document prepared | Completed |
| Submission summary prepared | Completed |
| README prepared / updated | Completed / Under Review |
| GitHub repository structure prepared | In Progress |
| Tableau dashboard final formatting | In Progress |
| Excel dashboards | Planned |
| Power BI dashboards | Planned |
| Prediction model | Planned |
| Final presentation | Planned |

---

## 15. Notes for Submission 01

This submission focuses on the required documentation package. Some technical components have already been implemented, including the Python pipeline, SQLite database, Streamlit dashboard, and Tableau dashboards.

However, final dashboard formatting, Excel dashboards, Power BI dashboards, prediction modeling, final testing, and final presentation are planned for later project phases.

This separation ensures that the documentation accurately reflects both the completed work and the remaining roadmap.

---

## 16. Conclusion

Submission 01 provides the foundation documentation for the **LA Traffic Collision Intelligence Project**.

The submitted documents explain why the project was selected, how the system is planned, what requirements it must satisfy, how the system is designed, and how the current and future deliverables are organized.

The project is currently in a strong implementation stage, with completed data preparation, SQL implementation, Streamlit dashboarding, and Tableau dashboard prototypes. The next phases will focus on final dashboard polishing, Excel and Power BI dashboards, prediction modeling, final testing, and final presentation delivery.

