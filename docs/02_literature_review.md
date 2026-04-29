# 02 — Literature Review

## Project Title

**LA Traffic Collision Intelligence Project**

---

## 1. Purpose of the Literature Review

This literature review summarizes the main concepts, approaches, and best practices related to traffic collision analysis, road safety intelligence, coded crash data interpretation, dashboard design, and predictive analytics.

The purpose is to connect the project idea with recognized practices in data-driven road safety and business intelligence. The review also explains why the project focuses on data quality, MO code interpretation, SQL modeling, Tableau dashboards, Power BI dashboards, Excel dashboards, Streamlit analytics, and future prediction modeling.

---

## 2. Background: Traffic Collision Data as a Decision-Support Asset

Traffic collision datasets are valuable public safety resources because they contain information about when, where, and how crashes occur. These datasets can support decision-making for transportation planning, road safety improvement, law enforcement analysis, public safety reporting, and urban mobility planning.

However, raw collision records are often not immediately ready for analysis. They may include:

- coded fields that are difficult to interpret directly
- inconsistent naming conventions
- missing values
- duplicate or repeated records
- partial-year reporting issues
- incomplete geographic coordinates
- mixed categorical and numeric data
- multiple values stored in one field

Because of these challenges, a structured data preparation workflow is required before reliable analysis or dashboarding can take place.

In this project, the raw traffic collision dataset was treated as a decision-support asset rather than a simple spreadsheet. The team transformed it into cleaned datasets, classified MO-code layers, SQL-ready tables, dashboard-ready summaries, Tableau dashboards, Streamlit analytics, and future prediction-ready structures.

---

## 3. Data-Driven Road Safety

Modern road safety programs increasingly depend on data-driven analysis. Instead of relying only on manual observation or isolated incident reports, agencies and analysts use crash data to identify patterns, prioritize locations, monitor risk, and support safety interventions.

Data-driven road safety commonly focuses on:

- collision frequency
- collision severity
- crash location concentration
- time-of-day and day-of-week patterns
- vulnerable road user involvement
- behavioral risk factors
- roadway and premise context
- high-risk corridors and hotspots
- trend changes over time

This project follows the same direction by analyzing collision trends, location hotspots, injury severity, hit-and-run signals, DUI/sobriety indicators, victim profiles, and MO-code-based behavioral/contextual patterns.

---

## 4. Safe System and Vision Zero Context

Road safety frameworks such as the Safe System approach and Vision Zero encourage cities and agencies to use evidence-based safety planning. These approaches focus on reducing fatal and serious injuries by understanding road system risks and improving design, enforcement, education, and policy decisions.

A key principle in these frameworks is that serious traffic injuries and deaths should not be treated as random events. Instead, they should be studied through data to identify preventable patterns.

This project supports this concept by creating an analytical system that can help users understand:

- where collisions are concentrated
- when collisions are most frequent
- which areas show higher risk exposure
- which victim groups are most represented
- which severity and behavioral indicators appear most often
- how coded MO information can reveal hidden context

---

## 5. Importance of Data Quality in Collision Analysis

Data quality is a critical foundation for any traffic collision analysis. If the raw data contains invalid dates, duplicate identifiers, inconsistent categories, missing coordinates, or unclear coded fields, then dashboards and conclusions may become misleading.

Important data quality checks in traffic collision projects include:

- schema review
- missing value analysis
- duplicate record checks
- date parsing validation
- time field validation
- categorical consistency checks
- coordinate validity checks
- primary key uniqueness checks
- reference data mapping checks

This project applied these concepts through a structured data audit and cleaning workflow before building SQL tables or dashboards. This helped reduce the risk of inaccurate reporting and improved confidence in the final analytical outputs.

---

## 6. Coded Fields and MO Code Interpretation

Many public safety datasets contain coded fields. These codes are useful for compact reporting, but they are often difficult for analysts, dashboard users, and non-technical reviewers to understand directly.

The MO Codes column in this project was one of the most important examples. A single collision record could contain multiple MO codes, and each code required interpretation before it could be used in dashboards or SQL analysis.

The literature and practical data analytics experience both highlight the importance of converting coded values into meaningful analytical labels. Without this step, coded fields usually remain underused.

In this project, the team created a custom **MO Codes Classification** layer to convert raw MO codes into:

- analytical domains
- analytical categories
- analytical subcategories
- traffic relevance indicators
- dashboard-friendly groupings
- interpretable labels for reporting

This classification layer became one of the strongest analytical foundations of the project because it transformed a difficult coded field into an explainable insight layer.

---

## 7. Multi-Value Field Normalization

A common data modeling issue occurs when one field contains multiple values. In relational data modeling, this creates problems because one record may need to link to several related codes or categories.

The MO Codes field had this issue because multiple MO codes could appear within one collision record. To solve this, the project normalized the field by separating individual MO codes and creating a bridge structure between collisions and MO codes.

This approach supports:

- cleaner SQL modeling
- many-to-many relationships
- better filtering in dashboards
- accurate aggregation by MO category
- improved maintainability
- scalable future modeling

This design is aligned with standard relational modeling principles where repeated or multi-value fields are separated into dedicated tables.

---

## 8. Temporal Collision Analysis

Time-based analysis is one of the most important areas in collision intelligence. Traffic collisions often vary by year, month, weekday, and hour of day. These patterns may reflect commuting behavior, school/work schedules, nightlife activity, seasonal changes, enforcement patterns, and reporting coverage.

Typical temporal analysis includes:

- annual collision trends
- year-over-year changes
- complete-year versus partial-year interpretation
- monthly trends
- weekday distribution
- hourly concentration
- weekday-hour heatmaps

This project applies temporal analysis through yearly summaries, monthly summaries, and weekday-hour summaries. The Streamlit and Tableau dashboards use these outputs to help users identify collision timing patterns and avoid misleading comparisons caused by partial-year data.

---

## 9. Geographic and Hotspot Analysis

Geographic analysis is a central part of traffic collision intelligence. Collision records often include area names, reporting districts, addresses, and coordinates. When cleaned and validated, these fields can help identify high-risk locations and spatial concentrations.

Common geographic analysis techniques include:

- area-level collision ranking
- reporting district analysis
- coordinate validation
- map-ready point layers
- hotspot ranking
- dominant area or premise by hotspot
- location-based filtering

This project created map-ready outputs and hotspot summary files that support Tableau, Power BI, and Streamlit mapping. The hotspot layer reduces performance issues by aggregating repeated coordinate locations and ranking them by collision count.

---

## 10. Injury Severity and Behavioral Risk Analysis

Collision analysis should not focus only on total collision count. Severity and behavioral indicators provide important context for public safety prioritization.

Relevant risk dimensions include:

- fatal injuries
- severe injuries
- non-injury collisions
- hit-and-run involvement
- DUI or sobriety-related indicators
- vulnerable user involvement

This project includes dedicated summaries and dashboards for risk and severity. These outputs help users distinguish between high-volume collision patterns and high-risk collision patterns.

---

## 11. Victim Demographic Analysis

Victim demographic analysis helps identify which groups are most represented in collision records. This can support equity-aware safety planning, targeted interventions, and clearer understanding of collision impact.

Common demographic fields include:

- victim age
- age group
- victim sex
- victim descent
- vulnerable road user category

This project created victim profile summaries to analyze age groups, sex distribution, descent distribution, and vulnerable user involvement. These summaries are used in both Streamlit and Tableau dashboard pages.

---

## 12. Dashboarding and Business Intelligence in Road Safety

Dashboards are important because they convert analytical outputs into accessible decision-support tools. For public safety and traffic analysis, dashboards should help users quickly understand the main indicators without reading raw tables.

Effective traffic collision dashboards usually include:

- clear KPIs
- trend charts
- maps
- filters
- severity summaries
- demographic breakdowns
- hotspot tables
- user-friendly labels
- notes about data limitations

This project uses multiple dashboarding tools to demonstrate the same analytical story across different platforms:

- **Tableau** for visual BI storytelling
- **Streamlit** for interactive Python-based analytics
- **Excel** for lightweight business reporting
- **Power BI** for interactive Microsoft BI reporting

The Tableau dashboards have already been developed as functional prototypes and are pending final formatting. The Streamlit dashboard has already been developed with multiple analytical pages.

---

## 13. SQL and Dimensional Modeling

SQL modeling is important when a project needs reusable, structured, and queryable analytical data. Instead of relying only on isolated CSV files, SQL provides a stronger foundation for validation, relationships, joins, views, and repeatable analysis.

This project uses SQLite to implement an analytical model with:

- fact collision table
- date dimension
- area dimension
- premise dimension
- MO code dimension
- bridge table between collisions and MO codes
- analytical SQL views
- validation queries
- sample business queries

This supports a more professional data structure and makes the project easier to extend into dashboards and future applications.

---

## 14. Predictive Analytics Extension

After building a reliable descriptive analytics foundation, the project can be extended into prediction. Predictive analytics can help estimate future risk, classify likely severity, identify hotspot recurrence, or support decision-making before collisions happen.

Possible prediction directions include:

- collision severity prediction
- hotspot risk prediction
- temporal collision forecasting
- vulnerable user risk classification
- area-level risk scoring

Prediction models require strong input features. The current project already creates many useful features and summaries, including time fields, location fields, MO categories, severity indicators, victim information, and hotspot outputs.

The planned prediction work will build on the cleaned and structured analytical base instead of starting from raw data.

---

## 15. Related Work and Practical References

This project is aligned with common practices from public safety analytics, transportation safety programs, and data-driven decision support. Relevant reference areas include:

1. National traffic crash data systems and crash statistics programs
2. Roadway safety data programs and data-driven safety analysis
3. Vision Zero and Safe System road safety approaches
4. Public health injury data tools and motor vehicle injury prevention resources
5. Business intelligence dashboard design for public safety and mobility data
6. Relational data modeling and dimensional modeling practices
7. Predictive analytics for crash severity and hotspot risk analysis

These references support the project direction by emphasizing that traffic collision analysis should combine data quality, interpretability, location analysis, temporal analysis, severity analysis, and accessible dashboard delivery.

---

## 16. Literature Review Summary

The reviewed concepts show that a strong traffic collision intelligence project should not stop at basic charts. It should include a full workflow that converts raw data into trustworthy and actionable insight.

Key lessons applied in this project include:

- raw public safety data needs quality checks before analysis
- coded fields must be translated into understandable categories
- multi-value fields should be normalized for SQL and dashboard use
- time-based analysis should handle partial-year distortion carefully
- geographic analysis requires coordinate validation and hotspot aggregation
- severity and vulnerable-user analysis are essential for risk interpretation
- dashboards should be clear, interactive, and supported by governed datasets
- SQL modeling improves structure, reusability, and validation
- predictive analytics should be built on top of a clean and validated analytical base

The **LA Traffic Collision Intelligence Project** applies these principles by combining data cleaning, MO code classification, SQL implementation, Tableau dashboards, Streamlit analytics, and a planned prediction extension into one integrated project workflow.

---

## 17. References

The literature review was informed by public and professional resources related to traffic safety analytics, crash data systems, roadway safety programs, Vision Zero, public health injury data, and data-driven safety analysis, including:

- National Highway Traffic Safety Administration — Traffic Safety Facts and Crash Data Systems
- Federal Highway Administration — Safety Data Analysis Tools and Roadway Safety Data Program
- Federal Highway Administration — Data-Driven Safety Analysis resources
- Vision Zero Network — Safe System and Vision Zero approach
- Centers for Disease Control and Prevention — WISQARS injury data and motor vehicle injury prevention resources
- Public safety and business intelligence dashboard design practices
- Relational database and dimensional modeling practices

