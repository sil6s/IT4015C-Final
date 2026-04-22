# Inflation, Consumer Spending, Income, and Economic Conditions in the United States

**Student:** Silas Curry
**Course:** IT4015C — Applied Business Intelligence, Section 001 (3 Credit Hours)
**Instructor:** Tyler Woebkenberg — tyler.woebkenberg@uc.edu
**Prerequisite:** IT2060C Database Management I

---

## Project Overview

This repository contains a complete integrated data analysis project examining relationships between inflation, consumer spending, disposable personal income, and broader economic conditions in the United States. The project integrates ten monthly macroeconomic time-series datasets sourced from the Bureau of Labor Statistics (BLS) and the Federal Reserve Economic Data (FRED) system, builds a reproducible Python data preparation pipeline, produces a validated master dataset, performs descriptive analysis, and delivers charts, summary tables, and a written report.

The final analysis covers **121 complete monthly observations from January 2016 through February 2026** — the window where all required variables have uninterrupted coverage. All intermediate datasets, validation outputs, scripts, charts, and documentation are organized into a numbered folder structure described below.

---

## Research Focus

The central question is how inflation-related measures relate to consumer spending patterns, with income, monetary policy, labor market conditions, and consumer sentiment providing economic context. The analysis uses CPI measures as the primary inflation indicators and PCE Total as the primary spending measure, then examines descriptive statistics, year-over-year growth trends, and correlation structure across all nine core variables.

---

## Key Findings (Analysis Period: 2016-01 to 2026-02)

| Metric | Value |
|---|---|
| Analysis observations | 121 complete monthly rows |
| CPI Overall change (first to latest) | +37.79% |
| PCE Total change (first to latest) | +73.23% |
| Disposable Personal Income change | +70.19% |
| CPI Overall avg YoY growth | 3.33% (max 8.98%) |
| PCE Total avg YoY growth | 5.81% |
| Correlation: PCE Total vs CPI Overall (levels) | 0.994 |
| Correlation: PCE Total vs CPI Shelter (levels) | 0.986 |
| Correlation: PCE YoY vs CPI Transportation YoY | 0.790 |
| Correlation: PCE YoY vs CPI Overall YoY | 0.660 |

Correlation results are descriptive. Shared time trends and common macroeconomic shocks affect level-variable correlations in particular. See the full narrative in `11_outputs/reports/final_analysis_narrative.md` and the written report in `12_final_submission/`.

---

## Datasets

Ten monthly U.S. macroeconomic time series were collected and integrated. All are joined on a standardized `date` column (first-of-month, YYYY-MM-DD format) using a full outer join.

| Dataset | Raw File | Source | Role | Cleaned Rows | Coverage |
|---|---|---|---|---|---|
| CPI Overall | `CPI_Overall.xlsx` | BLS (CUSR0000SA0) | Primary inflation variable | 122 | 2016-01 to 2026-03 |
| CPI Food | `CPI_Food.xlsx` | BLS (CUSR0000SAF1) | Supporting inflation detail | 122 | 2016-01 to 2026-03 |
| CPI Shelter | `CPI_Shelter.xlsx` | BLS (CUSR0000SAH1) | Supporting inflation detail | 122 | 2016-01 to 2026-03 |
| CPI Transportation | `CPI_Transportation.xlsx` | BLS (CUSR0000SAT) | Supporting inflation detail | 122 | 2016-01 to 2026-03 |
| PCE Total | `PCE_Total.csv` | FRED (PCE) | Primary spending variable | 806 | 1959-01 to 2026-02 |
| PCE Price Index | `PCE_Price_Index.csv` | FRED (PCECC96) | Supporting inflation comparison | 316 | 1947-01 to 2026-01 |
| Disposable Personal Income | `Disposable_Income.csv` | FRED (DSPI) | Supporting income context | 806 | 1959-01 to 2026-02 |
| Federal Funds Rate | `Interest_Rate_FedFunds.csv` | FRED (FEDFUNDS) | Supporting monetary policy context | 861 | 1948-01 to 2026-02 |
| Consumer Sentiment | `Consumer_Sentiment.csv` | FRED (UMCSENT) | Supporting household context | 880 | 1952-11 to 2026-02 |
| Unemployment Rate | `Unemployment_Rate.csv` | FRED (UNRATE) | Supporting labor market context | 939 | 1948-01 to 2026-02 |

The full outer merge of all ten datasets produces **944 rows spanning 1947-01 to 2026-03**. Missing values are preserved as NULLs where a source dataset does not cover a given month. See `10_qa_validation/merged_missing_value_summary.csv` for the complete per-column missing-value inventory.

The ER diagram below (also at `11_outputs/charts/er_diagram_date_outer_join.png`) shows how all source tables are joined on the `date` primary key:

![ER Diagram](11_outputs/charts/er_diagram_date_outer_join.png)

---

## Project Structure

```
BI Final/
├── 01_raw_data/                    Original downloaded files (never modified)
│   ├── inflation/                  CPI_Overall.xlsx, CPI_Food.xlsx, CPI_Shelter.xlsx,
│   │                               CPI_Transportation.xlsx, PCE_Price_Index.csv
│   ├── spending/                   PCE_Total.csv
│   ├── income/                     Disposable_Income.csv
│   └── economic_conditions/        Interest_Rate_FedFunds.csv, Consumer_Sentiment.csv,
│                                   Unemployment_Rate.csv
│
├── 02_source_documentation/        data_sources.md — why each dataset was selected,
│                                   source organization, frequency, limitations
│
├── 03_cleaned_data/                10 cleaned CSVs (one per dataset), each with:
│                                   date, {value_column}, dataset_id, display_name,
│                                   source_file, source_series, expected_frequency,
│                                   project_role
│
├── 04_merged_data/                 master_monthly_dataset.csv (944 rows, full outer join)
│                                   pre_analysis_dataset.csv / .xlsx (same, formatted
│                                   for Excel and Power BI import)
│
├── 05_scripts/                     Reproducible Python pipeline
│   ├── config/project_config.json  All dataset definitions and path configuration
│   ├── src/
│   │   ├── config.py               Configuration loader
│   │   ├── data_loading.py         Loads BLS Excel and FRED CSV formats
│   │   ├── cleaning.py             Standardizes dates, column names, and types
│   │   ├── integration.py          Outer-joins all datasets on date
│   │   └── validation.py           QA checks and validation report generation
│   ├── run_pipeline.py             Main orchestrator: load → clean → validate → merge
│   ├── run_final_analysis.py       Analysis phase: align → derive → summarize → chart
│   ├── create_er_diagram.py        Generates the ER diagram PNG
│   └── requirements.txt            Python dependencies
│
├── 06_notebooks/                   Notebook templates for documented analysis work
├── 07_excel_workbooks/             Excel planning materials
├── 08_power_bi/                    Power BI planning materials and guides
│
├── 09_documentation/               data_dictionary.md, file_naming_conventions.md,
│                                   project_structure.md
│
├── 10_qa_validation/               Automated validation outputs
│   ├── cleaned_dataset_validation_summary.csv   Per-dataset structure checks
│   ├── merged_dataset_validation_summary.csv    Merged dataset integrity checks
│   ├── merged_missing_value_summary.csv         Per-column NULL inventory
│   ├── validation_summary.csv                   Consolidated QA summary
│   ├── pipeline_artifact_manifest.csv           All generated artifact statuses
│   ├── validation_checklist.md                  Manual QA checklist
│   └── data_quality_report_template.md          QA report template
│
├── 11_outputs/                     Generated analysis outputs
│   ├── analysis_data/
│   │   ├── analysis_aligned_monthly_dataset.csv        121 rows, 9 core variables
│   │   ├── analysis_dataset_with_derived_variables.csv 121 rows, 27 columns
│   │   └── analysis_dataset_with_derived_variables.xlsx
│   ├── charts/
│   │   ├── chart_01_inflation_trends.png           CPI overall vs category CPIs over time
│   │   ├── chart_02_consumer_spending_pce.png      PCE total over time
│   │   ├── chart_03_income_vs_spending.png         PCE vs disposable income
│   │   ├── chart_04_inflation_vs_spending_scatter.png  CPI YoY vs PCE YoY with fit line
│   │   ├── chart_05_economic_context.png           Unemployment, fed funds, sentiment
│   │   ├── chart_06_indexed_comparison.png         CPI, PCE, income indexed to 2016=100
│   │   └── er_diagram_date_outer_join.png          ER diagram: outer join on date PK
│   ├── tables/
│   │   ├── summary_statistics_levels.csv           Descriptive stats for 9 variables
│   │   ├── summary_statistics_yoy_growth.csv       Descriptive stats for YoY growth
│   │   ├── correlation_matrix_levels.csv           9x9 level correlation matrix
│   │   ├── correlation_matrix_yoy_growth.csv       6x6 YoY growth correlation matrix
│   │   ├── latest_analysis_values.csv              First, latest, and % change values
│   │   └── analysis_adjustments_log.csv            Documents alignment decisions
│   └── reports/
│       ├── final_analysis_narrative.md             Full written analysis narrative
│       ├── excel_final_phase_guide.md              Excel formulas and workflow guide
│       ├── power_bi_final_phase_guide.md           Power BI data model and DAX guide
│       └── presentation_content.md                Slide-by-slide outline with talking points
│
├── 12_final_submission/            Final deliverables
│   ├── Final Written Report.pdf    Completed project report
│   ├── presentation_outline.md     Presentation structure and talking points
│   └── submission_checklist.md     Pre-submission review checklist
│
├── 13_project_management/          Project log, assumptions log, issue tracker,
│                                   change log, and handoff notes
│
└── README.md                       This file
```

---

## Data Preparation Pipeline

The Python pipeline in `05_scripts/` handles all data preparation in a fully reproducible way.

### Loading

- **FRED CSV files** — `observation_date` is renamed to `date`; the value column is renamed to the configured `value_column` name.
- **BLS Excel workbooks** — Wide format (year rows × month columns) is reshaped to tidy monthly rows. Dates are constructed as `YYYY-MM-01`.

### Cleaning

- All dates are parsed and normalized to first-of-month ISO 8601 (`YYYY-MM-DD`).
- All value columns are cast to numeric with coercion; non-parseable rows are dropped.
- Column names are standardized to `snake_case`.
- Metadata columns (`dataset_id`, `display_name`, `source_file`, `source_series`, `expected_frequency`, `project_role`) are appended to each cleaned file for full traceability.

### Integration

All ten cleaned datasets are outer-joined on `date` using `pandas.merge(how="outer", on="date")` applied iteratively with `functools.reduce`. The result is sorted by date and exported. Missing values are preserved as NaN wherever a source dataset does not cover a given month.

### Derived Variables (Analysis Phase)

For the six primary variables (CPI overall, food, shelter, transportation, PCE total, disposable income):

| Derived Type | Formula |
|---|---|
| Year-over-Year % change | `((current / prior_year_month) - 1) * 100` |
| Month-over-Month % change | `((current / prior_month) - 1) * 100` |
| 2016-Base Index | `(current / 2016_annual_average) * 100` |

### Analysis Period

The final analysis dataset uses the complete-overlap window: **2016-01 through 2026-02** (121 rows after excluding one incomplete month, 2025-10). This is the latest first-available date across all required variables and the earliest last-available date.

---

## Quality Assurance

The automated QA pipeline (`validation.py`) checks:

- Expected columns are present in each cleaned dataset
- No duplicate dates exist within any cleaned dataset
- Dates parse without errors
- Row and column counts match expectations
- Missing values and coverage gaps are flagged and quantified
- The merged dataset contains no duplicate dates after joining
- All output files are created and non-empty

All QA outputs are in `10_qa_validation/`. Every cleaned dataset passed structural validation. Missing-value flagging is documented in `merged_missing_value_summary.csv` — large NULL counts (e.g., 87% for CPI columns in the full 944-row master) reflect intentional outer-join coverage preservation, not data errors.

---

## Charts Produced

| File | Contents |
|---|---|
| `chart_01_inflation_trends.png` | CPI overall and category CPIs (food, shelter, transportation) over the analysis period |
| `chart_02_consumer_spending_pce.png` | PCE total monthly level over time |
| `chart_03_income_vs_spending.png` | PCE total vs disposable personal income (level comparison) |
| `chart_04_inflation_vs_spending_scatter.png` | CPI overall YoY% vs PCE total YoY% scatter with linear fit (r = 0.660) |
| `chart_05_economic_context.png` | Three-panel: unemployment rate, federal funds rate, consumer sentiment |
| `chart_06_indexed_comparison.png` | CPI overall, PCE total, and disposable income indexed to 2016 = 100 |
| `er_diagram_date_outer_join.png` | ER diagram showing all 10 source tables outer-joined on `date` |

---

## Reproducibility

### Requirements

```
pandas
openpyxl
matplotlib
```

### Run the full pipeline

```bash
cd "BI Final/05_scripts"
pip install -r requirements.txt
python3 run_pipeline.py
```

This reads from `01_raw_data/`, writes cleaned files to `03_cleaned_data/`, writes merged datasets to `04_merged_data/`, and writes validation reports to `10_qa_validation/`.

### Run the analysis phase

```bash
python3 run_final_analysis.py
```

This reads from `04_merged_data/`, writes the aligned and derived-variable datasets to `11_outputs/analysis_data/`, writes charts to `11_outputs/charts/`, writes summary tables to `11_outputs/tables/`, and writes the analysis narrative to `11_outputs/reports/`.

### Regenerate the ER diagram

```bash
python3 create_er_diagram.py
```

---

## Source Documentation

Full dataset-level documentation is in `02_source_documentation/data_sources.md`. It records the source organization, series identifier, retrieval date, frequency, known limitations, and intended project role for each of the ten datasets.

The data dictionary is in `09_documentation/data_dictionary.md`. It records field names, data types, units, value ranges, and transformation notes.

---

## Limitations

- **Correlation is not causation.** All statistical results are descriptive. Shared time trends inflate level-variable correlations for macroeconomic time series.
- **Analysis period is constrained by CPI coverage.** The CPI data begins in 2016, which limits the complete-overlap window even though PCE, income, and economic context series extend back to the 1940s–1960s.
- **PCE Price Index is quarterly.** It produces monthly NULLs in the merged dataset and is excluded from the primary 121-row analysis period calculations.
- **Scope is national U.S. aggregates only.** No regional, demographic, or household-level breakdowns are included.

---

## File Naming Conventions

- Processed outputs use lowercase `snake_case`.
- Dates use `YYYY-MM-DD`.
- Raw data file names are preserved from their original download to maintain source traceability.
- Detailed standards are in `09_documentation/file_naming_conventions.md`.

---

## Versioning

Raw data files are treated as immutable. Any dataset update is documented in `13_project_management/change_log.md`. Script and documentation changes are also recorded there so the workflow remains auditable.
