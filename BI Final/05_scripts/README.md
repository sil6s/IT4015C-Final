# Python Pipeline README

## Purpose

I use this folder for the reproducible data preparation pipeline. The scripts load raw files, clean and standardize them, validate expected structures, merge the datasets by date, and export pre-analysis files.

The scripts do not perform analysis, create findings, or write recommendations.

## How to Run

```bash
cd Project_Data/05_scripts
python3 -m pip install -r requirements.txt
python3 run_pipeline.py
```

## Script Map

| File | Purpose |
|---|---|
| `run_pipeline.py` | I run the full preparation workflow from this script. |
| `config/project_config.json` | I define source files, expected series codes, and output paths here. |
| `src/config.py` | I load configuration and resolve paths. |
| `src/data_loading.py` | I load FRED-style CSV files and BLS CPI Excel files. |
| `src/cleaning.py` | I standardize dates, columns, and numeric values. |
| `src/validation.py` | I create QA checks and validation summaries. |
| `src/integration.py` | I merge cleaned datasets into the master dataset. |
| `src/logging_utils.py` | I create processing logs for pipeline runs. |

## Expected Outputs

- `03_cleaned_data/cleaned_*.csv`
- `04_merged_data/master_monthly_dataset.csv`
- `04_merged_data/pre_analysis_dataset.csv`
- `04_merged_data/pre_analysis_dataset.xlsx`
- `10_qa_validation/*.csv`
- `11_outputs/logs/processing_log_*.log`
