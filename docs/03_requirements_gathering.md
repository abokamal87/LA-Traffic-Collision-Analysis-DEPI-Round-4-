# 03 — Requirements Gathering

## Project Title

**LA Traffic Collision Intelligence Project**

---

## 1. Purpose of This Document

This document defines the requirements gathered for the **LA Traffic Collision Intelligence Project**. It identifies the project stakeholders, user needs, use cases, functional requirements, non-functional requirements, data requirements, dashboard requirements, and future prediction requirements.

The goal is to ensure that the project is built around clear user needs and measurable deliverables rather than only technical processing steps.

---

## 2. Project Context

The project focuses on analyzing Los Angeles traffic collision records and converting them into a structured intelligence system.

The project started with:

1. a large raw traffic collision dataset containing more than **621,000 records** and **18 original columns**
2. an official MO codes dictionary
3. a custom MO codes classification file created by the team

The dataset contains important fields related to:

- collision date and time
- reporting area
- reporting district
- premise information
- address and location
- victim age
- victim sex
- victim descent
- MO codes
- collision descriptors

One of the most important requirements of the project is to make the raw **MO Codes** column analytically useful by transforming it into readable domains, categories, subcategories, and dashboard-ready labels.

---

## 3. Stakeholder Analysis

The project stakeholders are divided into internal stakeholders, academic and evaluation stakeholders, direct system users, potential external stakeholders, and indirect public beneficiaries.

This classification is important because the project is an academic analytics project, not an officially commissioned system by Los Angeles city agencies. Therefore, external public entities are described as potential or indirect stakeholders rather than direct clients.

### 3.1 Internal Stakeholders

| Stakeholder | Role / Interest | Needs |
|---|---|---|
| Project Team | Builds the analytical workflow, dashboards, documentation, and future prediction extension | Clear task distribution, reliable data, agreed output structure, and documentation standards |
| Team Leader | Coordinates workflow, reviews outputs, manages GitHub delivery, and supervises documentation quality | Progress visibility, consistency, quality control, and complete documentation |

### 3.2 Academic and Evaluation Stakeholders

| Stakeholder | Role / Interest | Needs |
|---|---|---|
| Project Supervisor / Evaluator | Reviews the academic and technical quality of the project | Clear documentation, structured methodology, working outputs, dashboards, and final presentation |
| Technical Reviewers | Review code, SQL, architecture, dashboards, and repository structure | Clean repository structure, documented pipeline, SQL scripts, reproducible steps, and validated outputs |

### 3.3 Direct System Users

| Stakeholder | Role / Interest | Needs |
|---|---|---|
| Data Analyst Users | Explore collision trends, patterns, and summary outputs | Clean data, analytical summaries, charts, filters, and exportable results |
| BI Dashboard Users | Use dashboards for decision support and visual exploration | Interactive dashboards, KPIs, filters, maps, clear labels, and readable visual design |
| Non-Technical Users | Understand the project story and main insights without reading raw data | Simple explanations, visual summaries, and easy-to-read dashboards |
| Future ML Users | Use prepared data for prediction and risk modeling | Clean features, target variables, interpretable model outputs, and Streamlit integration |

### 3.4 Potential External Stakeholders

| Stakeholder | Role / Interest | Potential Value |
|---|---|---|
| Los Angeles City Decision-Makers | Could use similar analytics to monitor traffic collision trends and risk areas | Better visibility into collision patterns, hotspots, and safety priorities |
| Traffic and Transportation Planning Teams | Could use collision intelligence for planning and prioritization | Area-level insights, hotspot ranking, time patterns, and severity indicators |
| Road Safety Departments | Could use dashboards to support safety programs and intervention planning | Risk-focused analysis, vulnerable user indicators, and severity trends |
| Public Safety Analysts | Could use structured collision data for monitoring and reporting | Cleaned data, SQL views, and dashboard-ready summaries |

### 3.5 Indirect Public Beneficiaries

| Stakeholder | Role / Interest | Potential Value |
|---|---|---|
| Los Angeles Residents | Indirect beneficiaries of better traffic safety analysis | Safer roads, better awareness of high-risk areas, and improved public safety decisions |
| Road Users | Drivers, pedestrians, cyclists, and other mobility users affected by traffic safety conditions | Better understanding of collision risk and safer transportation planning |


---

## 4. User Groups

The project is designed for multiple user groups:

### 4.1 Academic Reviewers

Academic reviewers need to understand the project problem, scope, methodology, outputs, and team responsibilities.

### 4.2 Data Analysts

Data analysts need access to cleaned datasets, summary tables, MO classification outputs, and SQL-ready files.

### 4.3 Dashboard Consumers

Dashboard consumers need interactive dashboards that make it easy to explore collision trends, hotspots, severity, victim profiles, and MO-based patterns.

### 4.4 Technical Reviewers

Technical reviewers need to inspect the repository structure, SQL model, Streamlit app, Python workflow, and documentation.

### 4.5 Future Prediction Users

Future prediction users need a clean and structured data foundation to support severity prediction, risk scoring, or hotspot prediction.

---

## 5. User Needs

The main user needs identified for this project are:

1. understand overall traffic collision volume and trends
2. identify which years, months, weekdays, and hours show higher collision activity
3. identify geographic hotspots and high-collision areas
4. understand victim demographic patterns
5. review injury severity and risk indicators
6. analyze hit-and-run and DUI/sobriety signals
7. interpret raw MO codes in a meaningful way
8. use SQL to query structured analytical tables
9. explore dashboards in Tableau, Power BI, Excel, and Streamlit
10. prepare the project for future prediction and risk modeling
11. present the project clearly through GitHub documentation and final presentation material

---

## 6. User Stories

| ID | User Story | Priority |
|---|---|---|
| US-01 | As a reviewer, I want to understand the project idea and methodology so that I can evaluate the project clearly. | High |
| US-02 | As a data analyst, I want cleaned collision data so that I can perform reliable analysis. | High |
| US-03 | As a dashboard user, I want to see total collisions and yearly trends so that I can understand overall movement over time. | High |
| US-04 | As a dashboard user, I want to filter by year and area so that I can focus on specific reporting contexts. | High |
| US-05 | As a safety analyst, I want to identify collision hotspots so that I can detect concentrated risk locations. | High |
| US-06 | As a safety analyst, I want severity and hit-and-run summaries so that I can distinguish between high-volume and high-risk patterns. | High |
| US-07 | As a BI user, I want charts and maps so that I can understand the data visually. | High |
| US-08 | As a project evaluator, I want MO codes translated into readable categories so that coded data becomes understandable. | High |
| US-09 | As a SQL user, I want a structured database so that I can query collision, area, date, premise, and MO data. | High |
| US-10 | As a Streamlit user, I want a multi-page app so that I can explore different analysis themes easily. | High |
| US-11 | As a Power BI user, I want prepared datasets so that I can build interactive Microsoft BI reports. | Medium |
| US-12 | As an Excel user, I want summary tables so that I can create lightweight dashboards and pivot reports. | Medium |
| US-13 | As a future ML user, I want prepared features so that I can build a prediction model. | Medium |
| US-14 | As a team member, I want clear task responsibilities so that project delivery is organized. | High |

---

## 7. Use Cases

## Use Case 1 — Review Overall Collision Summary

| Item | Description |
|---|---|
| Actor | Dashboard user / evaluator |
| Goal | View total collisions, latest complete-year trend, top area, hit-and-run share, severity indicators, and vulnerable-user count |
| Input | Yearly summary, area summary, severity summary, hit-run summary, vulnerable-user summary |
| Output | Executive overview dashboard and KPI cards |
| Priority | High |

## Use Case 2 — Analyze Time Patterns

| Item | Description |
|---|---|
| Actor | Data analyst / dashboard user |
| Goal | Analyze collision activity by year, month, weekday, and hour |
| Input | Yearly, monthly, and weekday-hour summary datasets |
| Output | Annual trend, monthly trend, weekday-hour heatmap, peak periods |
| Priority | High |

## Use Case 3 — Explore Geographic Hotspots

| Item | Description |
|---|---|
| Actor | Safety analyst / dashboard user |
| Goal | Identify top collision areas, reporting divisions, premises, and hotspot coordinates |
| Input | Area summary, reporting division summary, premise summary, hotspot coordinate summary |
| Output | Maps, hotspot ranking, area tables, division tables |
| Priority | High |

## Use Case 4 — Analyze Risk and Severity

| Item | Description |
|---|---|
| Actor | Safety analyst / reviewer |
| Goal | Understand fatal, severe, non-injury, hit-and-run, and DUI/sobriety-related patterns |
| Input | Injury severity summary, hit-run summary, DUI/sobriety summary |
| Output | Severity charts, risk KPI cards, risk signal table |
| Priority | High |

## Use Case 5 — Analyze MO Code Patterns

| Item | Description |
|---|---|
| Actor | Data analyst / evaluator |
| Goal | Convert raw MO code patterns into readable analytical domains, categories, and subcategories |
| Input | MO classification file, MO domain/category/subcategory summaries |
| Output | MO dashboard, domain ranking, category ranking, traffic-only focus |
| Priority | High |

## Use Case 6 — Analyze Victim Profile

| Item | Description |
|---|---|
| Actor | Dashboard user / reviewer |
| Goal | Review victim age groups, sex, descent, and vulnerable road user categories |
| Input | Victim age group summary, victim sex summary, victim descent summary, vulnerable-user summary |
| Output | Victim profile dashboard and segmentation tables |
| Priority | High |

## Use Case 7 — Query the SQLite Database

| Item | Description |
|---|---|
| Actor | SQL user / technical reviewer |
| Goal | Query the structured database using tables and analytical views |
| Input | SQLite database and SQL scripts |
| Output | SQL query results and reusable views |
| Priority | High |

## Use Case 8 — Build BI Dashboards

| Item | Description |
|---|---|
| Actor | BI developer |
| Goal | Use prepared summary outputs to build Tableau, Power BI, and Excel dashboards |
| Input | Dashboard-ready CSV outputs |
| Output | Interactive BI dashboards |
| Priority | High |

## Use Case 9 — Develop Prediction Model

| Item | Description |
|---|---|
| Actor | ML developer |
| Goal | Build a prediction model using cleaned and engineered data |
| Input | Cleaned data, engineered fields, MO categories, time/location features |
| Output | Prediction model, evaluation metrics, and future Streamlit integration |
| Priority | Medium |

---

## 8. Functional Requirements

## 8.1 Data Loading Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-01 | The system must load the main raw traffic collision dataset. | High | Completed |
| FR-02 | The system must load the official MO codes dictionary. | High | Completed |
| FR-03 | The system must use the custom MO codes classification file. | High | Completed |
| FR-04 | The system must validate that input files are readable and structurally usable. | High | Completed |

## 8.2 Data Cleaning Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-05 | The system must standardize column names. | High | Completed |
| FR-06 | The system must parse and validate date fields. | High | Completed |
| FR-07 | The system must validate time fields and create time-based features. | High | Completed |
| FR-08 | The system must check duplicate collision identifiers. | High | Completed |
| FR-09 | The system must clean and standardize text fields. | Medium | Completed |
| FR-10 | The system must validate victim demographic fields. | Medium | Completed |
| FR-11 | The system must validate geographic coordinates. | High | Completed |

## 8.3 MO Code Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-12 | The system must identify collision records with MO codes. | High | Completed |
| FR-13 | The system must split multi-value MO fields into individual codes. | High | Completed |
| FR-14 | The system must create a collision-to-MO bridge table. | High | Completed |
| FR-15 | The system must map MO codes to the custom classification file. | High | Completed |
| FR-16 | The system must create analytical MO domains, categories, and subcategories. | High | Completed |
| FR-17 | The system must document unmapped MO codes. | High | Completed |

## 8.4 Analytical Output Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-18 | The system must generate yearly collision summaries. | High | Completed |
| FR-19 | The system must generate monthly collision summaries. | High | Completed |
| FR-20 | The system must generate weekday-hour summaries. | High | Completed |
| FR-21 | The system must generate area and reporting division summaries. | High | Completed |
| FR-22 | The system must generate premise summaries. | Medium | Completed |
| FR-23 | The system must generate injury severity summaries. | High | Completed |
| FR-24 | The system must generate hit-and-run summaries. | High | Completed |
| FR-25 | The system must generate DUI/sobriety summaries. | Medium | Completed |
| FR-26 | The system must generate victim demographic summaries. | High | Completed |
| FR-27 | The system must generate MO analytical summaries. | High | Completed |
| FR-28 | The system must generate hotspot coordinate summaries. | High | Completed |

## 8.5 SQL Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-29 | The project must implement a SQLite analytical database. | High | Completed |
| FR-30 | The database must contain fact and dimension tables. | High | Completed |
| FR-31 | The database must include a bridge table for collision-to-MO relationships. | High | Completed |
| FR-32 | SQL scripts must be created for schema creation. | High | Completed |
| FR-33 | SQL indexes must be created to support analytical queries. | Medium | Completed |
| FR-34 | Analytical SQL views must be created. | High | Completed |
| FR-35 | Sample SQL queries must be provided. | Medium | Completed |

## 8.6 Streamlit Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-36 | The Streamlit app must include multi-page navigation. | High | Completed |
| FR-37 | The app must include an Executive Overview page. | High | Completed |
| FR-38 | The app must include a Time Analysis page. | High | Completed |
| FR-39 | The app must include a Location Analysis page. | High | Completed |
| FR-40 | The app must include a Risk and Severity page. | High | Completed |
| FR-41 | The app must include an MO Analysis page. | High | Completed |
| FR-42 | The app must include a Victim Profile page. | High | Completed |
| FR-43 | The app must use reusable loading and formatting utilities. | Medium | Completed |
| FR-44 | The app should be extended with a prediction page. | Medium | Planned |

## 8.7 Dashboard Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-45 | Tableau dashboards must be created for executive, time, location, victim, and MO analysis. | High | In Progress |
| FR-46 | Tableau dashboards must be visually formatted and polished for final delivery. | High | Planned / In Progress |
| FR-47 | Excel dashboards must be created using prepared summary outputs. | Medium | Planned |
| FR-48 | Power BI dashboards must be created using prepared summary outputs. | High | Planned |

## 8.8 Prediction Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-49 | A prediction model must be developed using cleaned and engineered project data. | Medium | Planned |
| FR-50 | The prediction model must include clear input features and target definition. | Medium | Planned |
| FR-51 | The prediction model must include evaluation metrics. | Medium | Planned |
| FR-52 | Prediction results should be added to Streamlit. | Medium | Planned |

---

## 9. Non-Functional Requirements

| ID | Requirement | Description | Priority |
|---|---|---|---|
| NFR-01 | Usability | Dashboards must be understandable for both technical and non-technical users. | High |
| NFR-02 | Reliability | Outputs must be based on validated and cleaned data. | High |
| NFR-03 | Maintainability | Code, SQL, and documentation must be organized clearly in the repository. | High |
| NFR-04 | Scalability | The project structure should allow future dashboards and prediction modules to be added. | Medium |
| NFR-05 | Performance | Streamlit and BI dashboards should use summary outputs where possible to improve speed. | High |
| NFR-06 | Interpretability | MO codes and prediction outputs must be presented using clear labels and explanations. | High |
| NFR-07 | Reproducibility | Processing steps, SQL scripts, and documentation should allow the workflow to be repeated. | High |
| NFR-08 | Accessibility | Dashboard labels, titles, and visuals should be readable and clear. | Medium |
| NFR-09 | Data Governance | Approved outputs should be separated from raw or non-final files. | High |
| NFR-10 | Documentation Quality | All major project components must be documented for GitHub and academic review. | High |

---

## 10. Data Requirements

## 10.1 Required Input Data

| Data Requirement | Description |
|---|---|
| Collision Records | Must include collision identifiers, dates, times, location fields, victim fields, premise fields, and MO codes |
| MO Codes Dictionary | Must provide official meanings for MO codes |
| MO Classification File | Must classify MO codes into analytical domains, categories, subcategories, and dashboard groups |

## 10.2 Required Output Data

| Output Dataset Type | Purpose |
|---|---|
| Cleaned Collision Dataset | Main trusted analytical base |
| Date Dimension | Supports time-based SQL and dashboard analysis |
| Area Dimension | Supports area-level analysis |
| Premise Dimension | Supports premise and location-context analysis |
| MO Dimension | Stores classified MO code metadata |
| Collision-MO Bridge Table | Supports many-to-many collision-to-MO relationships |
| Dashboard Summary Files | Support Tableau, Power BI, Excel, and Streamlit dashboards |
| Hotspot Files | Support map-based analysis |
| SQL Views | Support reusable analytical queries |

---

## 11. Dashboard Requirements

## 11.1 Executive Dashboard Requirements

The executive dashboard must provide:

- total collision count
- latest complete-year indicator
- top area
- hit-and-run share
- non-injury share
- fatal collision count
- vulnerable user collision count
- annual trend
- top area summary
- severity summary

## 11.2 Time Dashboard Requirements

The time dashboard must provide:

- annual collision trend
- monthly collision trend
- weekday-hour heatmap
- year filtering
- complete-year logic
- peak month indicator
- peak weekday-hour indicator

## 11.3 Location Dashboard Requirements

The location dashboard must provide:

- area-level collision ranking
- reporting division ranking
- hotspot map
- hotspot ranking table
- top non-street premise types
- optional detailed collision point layer

## 11.4 Risk and Severity Dashboard Requirements

The risk and severity dashboard must provide:

- fatal collision count
- severe injury collision count
- non-injury share
- hit-and-run share
- severity distribution
- hit-and-run breakdown
- DUI/sobriety summary
- key risk signals

## 11.5 MO Analysis Dashboard Requirements

The MO dashboard must provide:

- MO domain ranking
- MO category ranking
- MO subcategory ranking
- traffic-only focus mode
- all-MO summary mode
- domain filtering
- key MO signals

## 11.6 Victim Profile Dashboard Requirements

The victim profile dashboard must provide:

- top age group
- top victim sex
- top victim descent
- vulnerable user collisions
- victim age group distribution
- victim sex distribution
- victim descent distribution
- vulnerable-user summary

---

## 12. System Requirements

## 12.1 Software Requirements

| Tool | Purpose |
|---|---|
| Python | Data processing, analysis, Streamlit app, future prediction model |
| pandas | Data manipulation and aggregation |
| SQLite | Analytical database implementation |
| DB Browser for SQLite / DBeaver | Database review and validation |
| Tableau | BI dashboard development |
| Power BI | Planned BI dashboard development |
| Excel | Planned lightweight dashboarding |
| Streamlit | Interactive Python dashboard application |
| GitHub | Repository hosting and project submission |
| Markdown | Documentation format |

## 12.2 Hardware Requirements

The project should run on a standard development laptop or desktop capable of handling large CSV files and dashboard tools.

Recommended minimum:

- 8 GB RAM or higher
- modern multi-core CPU
- sufficient storage for raw data, cleaned outputs, dashboard exports, and database files

---

## 13. Acceptance Criteria

The project requirements are considered successfully met when:

1. raw data is loaded and profiled
2. cleaned data is produced and validated
3. MO codes are classified into readable analytical structures
4. dashboard-ready summary files are generated
5. SQLite database is implemented and queryable
6. SQL scripts and sample queries are available
7. Streamlit dashboard runs with all required pages
8. Tableau dashboards exist and are prepared for final formatting
9. Excel and Power BI dashboards are planned using the same governed output layer
10. prediction model requirements are defined for future implementation
11. GitHub repository includes professional documentation
12. team roles and responsibilities are clearly documented

---

## 14. Requirements Traceability Matrix

| Requirement Area | Related Deliverables |
|---|---|
| Data Understanding | audit outputs, profiling summaries |
| Data Cleaning | cleaned collision dataset, dimensions |
| MO Interpretation | MO classification file, MO dimension, bridge table, MO summaries |
| Time Analysis | yearly, monthly, weekday-hour summaries, time dashboard |
| Location Analysis | area summary, division summary, hotspot outputs, location dashboard |
| Risk Analysis | severity, hit-run, DUI summaries, risk dashboard |
| Victim Analysis | victim age, sex, descent, vulnerable-user summaries, victim dashboard |
| SQL Modeling | SQLite database, schema scripts, views, sample queries |
| Streamlit Analytics | app.py, page files, loaders, formatters |
| BI Dashboards | Tableau dashboards, planned Excel and Power BI dashboards |
| Prediction | planned model and Streamlit extension |
| Documentation | README and docs folder |

---

## 15. Summary

The requirements gathered for this project confirm that the solution must be more than a basic data analysis exercise. It must provide a complete, structured, and explainable analytics workflow.

The main requirement is to transform raw traffic collision records and difficult MO-coded information into a reliable decision-support system. This includes cleaned data, SQL modeling, dashboard-ready outputs, interactive dashboards, and a foundation for future prediction.

The project requirements support both current delivery and planned future extensions across Excel, Power BI, Tableau, Streamlit, and machine learning.

