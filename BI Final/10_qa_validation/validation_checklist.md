# Validation Checklist

## Purpose

I use this checklist to make sure my project is ready for analysis before I begin writing findings. I treat this as a gatekeeping document: if a major preparation check fails, I should resolve or document it before moving into interpretation.

## Raw Data Checks

- [ ] I confirmed that every expected raw data file is present in `01_raw_data/`.
- [ ] I confirmed that raw files have not been edited directly after download.
- [ ] I confirmed that CPI files are stored as Excel files and FRED-style files are stored as CSV files.
- [ ] I confirmed that file names match the source documentation.
- [ ] I recorded any replaced or updated source files in the change log.

## Loading Checks

- [ ] I ran `python3 run_pipeline.py` from `05_scripts/`.
- [ ] I reviewed the processing log in `11_outputs/logs/`.
- [ ] I confirmed that every raw file loaded without a file-not-found error.
- [ ] I confirmed that CPI workbooks were reshaped from wide month columns into tidy date/value rows.
- [ ] I confirmed that CSV files used `observation_date` and the expected source series code.

## Cleaned Data Checks

- [ ] I confirmed that cleaned files were created in `03_cleaned_data/`.
- [ ] I confirmed that every cleaned file contains a standardized `date` column.
- [ ] I confirmed that every cleaned file contains the expected value column.
- [ ] I confirmed that date values use month-start dates.
- [ ] I confirmed that numeric values were converted to numeric types.
- [ ] I reviewed missing value counts without treating them as findings.

## Duplicate and Coverage Checks

- [ ] I reviewed duplicate-date counts for each cleaned dataset.
- [ ] I reviewed potential missing months within each dataset's date range.
- [ ] I documented any date coverage differences that may affect later analysis choices.
- [ ] I avoided dropping coverage gaps without documenting the reason.

## Merged Dataset Checks

- [ ] I confirmed that `master_monthly_dataset.csv` was created in `04_merged_data/`.
- [ ] I confirmed that `pre_analysis_dataset.csv` was created in `04_merged_data/`.
- [ ] I confirmed that `pre_analysis_dataset.xlsx` was created in `04_merged_data/`.
- [ ] I confirmed that the merged dataset has one row per date.
- [ ] I reviewed missing values caused by different source coverage periods.
- [ ] I confirmed that the merged dataset is not being interpreted in the preparation stage.

## QA Output Checks

- [ ] I reviewed `cleaned_dataset_validation_summary.csv`.
- [ ] I reviewed `merged_dataset_validation_summary.csv`.
- [ ] I reviewed `merged_missing_value_summary.csv`.
- [ ] I reviewed `validation_summary.csv`.
- [ ] I reviewed `pipeline_artifact_manifest.csv`.
- [ ] I recorded unresolved issues in `13_project_management/issue_tracker.md`.

## Readiness Decision

- [ ] I am ready to begin analysis.
- [ ] I am not ready to begin analysis because unresolved preparation issues remain.

## Reviewer Notes

I will use this space to record any preparation issues that need to be explained in the final methodology section.

| Date | Check Area | Issue or Note | Resolution Status |
|---|---|---|---|
|  |  |  |  |
