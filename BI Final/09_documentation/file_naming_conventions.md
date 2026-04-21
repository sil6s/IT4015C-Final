# File Naming and Organization Standards

## Purpose

I use strict naming conventions so that my final project is easy to audit, reproduce, and grade. I want file names to communicate the workflow stage, content, and status without requiring someone to open each file.

## General Rules

- I use lowercase snake_case for generated files.
- I preserve original raw file names unless I intentionally rename them during organization.
- I avoid spaces in generated file names.
- I use dates in `YYYY-MM-DD` format.
- I use version labels only when a file is manually revised.
- I do not overwrite final deliverables without recording the change in `13_project_management/change_log.md`.

## Raw Data Files

Raw files are stored in `01_raw_data/` and should remain unchanged after download.

Pattern:

`descriptive_source_name.ext`

Examples:

- `CPI_Overall.xlsx`
- `PCE_Total.csv`
- `Interest_Rate_FedFunds.csv`

I keep these names close to the source meaning so I can trace each cleaned file back to its origin.

## Cleaned Data Files

Cleaned files are stored in `03_cleaned_data/`.

Pattern:

`cleaned_<variable_name>.csv`

Examples:

- `cleaned_cpi_overall.csv`
- `cleaned_pce_total.csv`
- `cleaned_unemployment_rate.csv`

I use the `cleaned_` prefix to show that the file has been standardized but not analytically transformed.

## Merged Data Files

Merged files are stored in `04_merged_data/`.

Patterns:

- `master_monthly_dataset.csv`
- `pre_analysis_dataset.csv`
- `pre_analysis_dataset.xlsx`

I reserve `master_monthly_dataset` for the full outer-joined dataset and `pre_analysis_dataset` for the analysis-ready export that has passed preparation checks but has not yet been interpreted.

## Python Scripts

Scripts are stored in `05_scripts/`.

Patterns:

- `run_pipeline.py`
- `src/<module_name>.py`
- `config/project_config.json`

Examples:

- `src/data_loading.py`
- `src/validation.py`
- `src/integration.py`

I keep the pipeline modular so that loading, cleaning, validation, and integration are easy to review separately.

## Notebooks

Notebooks are stored in `06_notebooks/`.

Pattern:

`##_short_purpose_template.ipynb`

Example:

- `01_pre_analysis_workflow_template.ipynb`

I number notebooks in the order I expect to use them.

## Excel Workbooks

Excel materials are stored in `07_excel_workbooks/`.

Patterns:

- `excel_workflow_guide.md`
- `integrated_analysis_workbook_v01.xlsx`
- `integrated_analysis_workbook_final.xlsx`

I use version numbers while work is in progress and reserve `final` only for the version included in the submission package.

## Power BI Files

Power BI materials are stored in `08_power_bi/`.

Patterns:

- `power_bi_planning_document.md`
- `inflation_spending_dashboard_v01.pbix`
- `inflation_spending_dashboard_final.pbix`

I keep Power BI planning documentation beside the dashboard file so the model design can be reviewed.

## Visuals and Exports

Visuals and exports are stored in `11_outputs/`.

Patterns:

- `chart_<topic>_<view>_v01.png`
- `table_<topic>_<view>_v01.csv`
- `validation_report_<YYYY-MM-DD>.csv`
- `processing_log_<YYYY-MM-DD>.log`

I do not name a chart or table as final until the analysis has been completed and checked.

## Final Submission Files

Final files are stored in `12_final_submission/`.

Patterns:

- `final_report_template.md`
- `final_report_final.docx`
- `presentation_outline.md`
- `presentation_final.pptx`
- `submission_checklist.md`

I keep templates and final deliverables in the same folder, but I make the status clear in the file name.

## Versioning Rules

- `v01` is the first manually prepared version.
- `v02`, `v03`, and later versions represent meaningful revisions.
- `draft` means the file is not ready for submission.
- `final` means the file is ready to include in the final package.
- I record meaningful final-file changes in `13_project_management/change_log.md`.
