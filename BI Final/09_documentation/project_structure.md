# Project Structure Guide

## Purpose

I organized this project so that each stage of the workflow has a clear place. The structure separates raw inputs, prepared data, scripts, documentation, QA, outputs, and final submission materials. This makes the project easier to review and helps me avoid mixing analysis products with source data.

## Folder Explanations

### `01_raw_data/`

I store original downloaded files here. I treat this folder as read-only after the initial organization step.

### `02_source_documentation/`

I use this folder to document where each dataset came from and why I included it.

### `03_cleaned_data/`

I use this folder for cleaned individual datasets created by the Python pipeline. These files are standardized but not interpreted.

### `04_merged_data/`

I use this folder for the integrated master dataset and pre-analysis dataset.

### `05_scripts/`

I use this folder for reproducible Python code, configuration, helper modules, and dependency notes.

### `06_notebooks/`

I use this folder for notebook-based workflow documentation and later analysis notebooks.

### `07_excel_workbooks/`

I use this folder for Excel workbook planning materials and future workbook files.

### `08_power_bi/`

I use this folder for Power BI planning documents and future dashboard files.

### `09_documentation/`

I use this folder for cross-project documentation such as the data dictionary and naming rules.

### `10_qa_validation/`

I use this folder for manual and automated validation materials.

### `11_outputs/`

I use this folder for generated outputs that support the project but are not necessarily final submission files.

### `12_final_submission/`

I use this folder for final report, presentation, and submission packaging materials.

### `13_project_management/`

I use this folder for planning and audit records, including assumptions, issues, decisions, and changes.
