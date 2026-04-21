# Integrated Data Analysis Project Starter Repository

## Project Title

Inflation, Consumer Spending, Income, and Economic Conditions in the United States

## Project Overview

I am preparing an integrated data analysis project that brings together multiple United States economic datasets related to inflation, consumer spending, disposable income, interest rates, unemployment, and consumer sentiment. The purpose of this repository is to organize my data, document my sources, prepare the datasets for integration, and establish a reproducible workflow before I begin the actual analysis.

This repository is intentionally structured as a pre-analysis project package. I have not written findings, interpreted relationships, or made recommendations in this setup stage. Instead, I have focused on building a reliable foundation so that later analysis in Excel, Python, and Power BI can be completed with clear documentation and traceable preparation steps.

## Research Focus

My planned research focus is to examine how inflation-related measures can be compared with consumer spending while also incorporating economic context from income, interest rates, unemployment, and consumer sentiment. At this stage, I am framing the project around relationships that may be evaluated later, but I am not making claims about what those relationships show.

The planned analysis will use inflation indicators as central variables, consumer spending as a major outcome-oriented economic measure, and supporting variables to provide context for the broader economic environment. I am keeping the pre-analysis workflow separate from the interpretation stage so that my final conclusions are based on documented, validated, and reproducible data preparation.

## Why I Selected These Datasets

I selected these datasets because they represent connected but distinct parts of the consumer economy:

- CPI Overall provides a broad measure of consumer price inflation.
- CPI Food, CPI Shelter, and CPI Transportation provide category-level inflation detail for major consumer budget areas.
- PCE Total provides a broad measure of consumer spending.
- PCE Price Index / PCECC96 provides an additional price-related macroeconomic series that can support inflation comparison decisions later.
- Disposable Personal Income provides income context for consumer behavior.
- Federal Funds Rate provides monetary policy context.
- Unemployment Rate provides labor market context.
- Consumer Sentiment provides a household expectations and confidence context.

I included these files because the project is stronger when inflation and spending are not viewed in isolation. The supporting economic variables help me prepare a more complete analytical environment without requiring me to make conclusions during the setup stage.

## Dataset Summary

| Dataset | Current Raw File | Main Purpose | Primary or Supporting Role |
|---|---|---|---|
| CPI Overall | `CPI_Overall.xlsx` | Broad CPI inflation index | Primary inflation variable |
| CPI Food | `CPI_Food.xlsx` | Food category CPI index | Supporting inflation detail |
| CPI Shelter | `CPI_Shelter.xlsx` | Shelter category CPI index | Supporting inflation detail |
| CPI Transportation | `CPI_Transportation.xlsx` | Transportation category CPI index | Supporting inflation detail |
| PCE Total | `PCE_Total.csv` | Personal consumption expenditures | Primary spending variable |
| PCE Price Index / PCECC96 | `PCE_Price_Index.csv` | Price-related PCE comparison series | Supporting inflation comparison variable |
| Disposable Personal Income | `Disposable_Income.csv` | Income context | Supporting economic context |
| Federal Funds Rate | `Interest_Rate_FedFunds.csv` | Interest-rate context | Supporting economic context |
| Consumer Sentiment | `Consumer_Sentiment.csv` | Household sentiment context | Supporting economic context |
| Unemployment Rate | `Unemployment_Rate.csv` | Labor market context | Supporting economic context |

## Data Source Documentation

I maintain a dedicated source documentation file at:

`02_source_documentation/data_sources.md`

That file records each dataset, its source organization, frequency, purpose, known limitations, and how I plan to use it in the project. I am separating source documentation from analysis notes so that the credibility of the dataset collection can be reviewed independently.

## Project Structure

| Folder | Purpose |
|---|---|
| `01_raw_data/` | I keep original downloaded files here so I always have an untouched data source layer. |
| `02_source_documentation/` | I document where the data came from, why I included it, and how each file supports the project. |
| `03_cleaned_data/` | I export standardized versions of each dataset here after cleaning and date normalization. |
| `04_merged_data/` | I export the integrated master dataset and pre-analysis dataset here. |
| `05_scripts/` | I keep the reproducible Python pipeline here, including configuration and helper modules. |
| `06_notebooks/` | I keep notebook templates here for documented preparation and later analysis work. |
| `07_excel_workbooks/` | I keep Excel workflow planning materials and future workbook files here. |
| `08_power_bi/` | I keep Power BI planning materials and future `.pbix` files here. |
| `09_documentation/` | I keep project-wide documentation, naming standards, and data dictionary materials here. |
| `10_qa_validation/` | I keep validation checklists, QA templates, and automated validation outputs here. |
| `11_outputs/` | I keep generated non-final outputs here, including logs, tables, charts, reports, and exports. |
| `12_final_submission/` | I keep final report, presentation, and submission checklist materials here. |
| `13_project_management/` | I keep the project log, assumptions log, issue tracker, change log, and handoff notes here. |

## Workflow

My planned workflow is:

1. Preserve all downloaded files in `01_raw_data/`.
2. Document dataset sources and roles in `02_source_documentation/`.
3. Run the Python preparation pipeline from `05_scripts/`.
4. Export cleaned individual files into `03_cleaned_data/`.
5. Merge cleaned datasets by standardized monthly date into `04_merged_data/`.
6. Generate validation outputs and quality reports in `10_qa_validation/` and `11_outputs/logs/`.
7. Import the prepared dataset into Excel and Power BI for later analysis and visualization work.
8. Complete final interpretation, findings, recommendations, and report writing only after the prepared dataset has passed QA checks.

## Software and Tools Used

I am preparing the project to use:

- Python for reproducible data loading, cleaning, validation, integration, and exports.
- Excel for workbook-based review, validation tabs, chart preparation, and presentation-ready supporting materials.
- Power BI for dashboard preparation and interactive visual planning.
- Markdown for documentation, project management notes, and final report drafting.
- CSV and Excel files for transparent intermediate and final prepared datasets.

## Data Preparation Plan

My preparation plan focuses on structure and reliability:

- I standardize date columns to a consistent `date` field.
- I convert BLS-style CPI workbooks from wide monthly format into tidy monthly time series.
- I standardize column names using clear snake_case names.
- I convert numeric values to appropriate numeric types.
- I preserve raw source files and export cleaned copies separately.
- I retain source metadata where appropriate so that transformations remain traceable.
- I create validation reports before using the data for analysis.

## Integration Plan

I plan to integrate the datasets by monthly date. The pipeline uses an outer join so that differences in historical coverage are not silently dropped. After merging, validation outputs identify missing values and coverage gaps so I can decide later whether to filter, impute, or limit the analysis period.

I am not making those analysis-period decisions in this setup stage. Instead, I am making the coverage differences visible and documented.

## Quality Assurance

The project includes a QA framework that checks:

- Whether expected files exist.
- Whether each file loads successfully.
- Whether date fields can be parsed.
- Whether duplicate dates appear within a cleaned dataset.
- Whether output files are created and non-empty.
- Whether expected columns are present.
- Whether each dataset has a documented row count and column count.
- Whether missing values and coverage gaps are flagged.
- Whether the merged dataset contains a clear merge indicator by source.

The QA materials are stored in `10_qa_validation/`, and automated pipeline logs are exported to `11_outputs/logs/`.

## Limitations and Scope

This repository prepares the data and workflow, but it does not complete the analytical interpretation. Some datasets may begin at different dates, may use different source conventions, or may have missing periods. The setup is designed to expose those issues before analysis rather than hide them.

I am also keeping the topic scope focused on macroeconomic time-series data for the United States. I am not adding household-level microdata, regional breakdowns, or survey-level records in this starter package.

## Completed So Far

- I organized raw downloaded files into a professional project structure.
- I created documentation files for source tracking, naming conventions, and data dictionary planning.
- I created a reproducible Python pipeline for loading, cleaning, validating, merging, and exporting pre-analysis datasets.
- I created QA templates and automated validation output locations.
- I created Excel and Power BI preparation documents.
- I created final report and presentation templates that leave findings and conclusions blank for later work.

## Remaining Work

- I still need to run the final analysis after the prepared dataset is validated.
- I still need to decide the final analysis period after reviewing coverage gaps.
- I still need to build actual charts and dashboards after the analysis plan is finalized.
- I still need to write findings, recommendations, and conclusions based only on completed analysis.
- I still need to complete the final report and presentation after analysis is done.

## Reproducibility Instructions

From the project root, I can run:

```bash
cd Project_Data/05_scripts
python3 -m pip install -r requirements.txt
python3 run_pipeline.py
```

If I use a virtual environment, I can create it before installing requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 run_pipeline.py
```

The pipeline reads from `01_raw_data/`, writes cleaned files to `03_cleaned_data/`, writes merged files to `04_merged_data/`, and writes logs and validation outputs to `10_qa_validation/` and `11_outputs/logs/`.

## Submission Roadmap

My final submission package should eventually include:

- Final report in Word or PDF format.
- Final presentation slides if required.
- Excel workbook with documented tabs and chart preparation materials.
- Power BI dashboard file if required.
- Python scripts and notebook demonstrating reproducible preparation.
- Cleaned and merged datasets.
- README, data source documentation, data dictionary, QA checklist, and validation reports.

## File Naming Conventions

I use descriptive snake_case names for processed outputs and title-style descriptive names only where the original raw files already use that format. I keep dates in `YYYY-MM-DD` format and use version labels such as `v01`, `v02`, and `final` only when a file is manually revised.

Detailed standards are documented in:

`09_documentation/file_naming_conventions.md`

## Versioning Notes

I am treating raw data as immutable. If I download a newer version of a dataset later, I will preserve the previous version or document the replacement in `13_project_management/change_log.md`. For scripts, documentation, and final materials, I will record meaningful changes in the change log so that my workflow remains auditable.
