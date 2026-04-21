# Export Manifest

## Purpose

I use this manifest to track important exported files and decide what belongs in the final submission package.

## Exported Files

| File | Folder | Created By | Purpose | Include in Final Submission | Notes |
|---|---|---|---|---|---|
| `cleaned_*.csv` | `03_cleaned_data/` | Python pipeline | Standardized individual datasets | Maybe | I include these if the professor wants preparation evidence. |
| `master_monthly_dataset.csv` | `04_merged_data/` | Python pipeline | Full integrated dataset | Yes | I use this as the main integrated data artifact. |
| `pre_analysis_dataset.csv` | `04_merged_data/` | Python pipeline | Analysis-ready CSV export | Yes | I use this for Power BI import. |
| `pre_analysis_dataset.xlsx` | `04_merged_data/` | Python pipeline | Analysis-ready Excel export | Yes | I use this for Excel import. |
| `validation_summary.csv` | `10_qa_validation/` | Python pipeline | Overall validation status | Yes | I include this as QA evidence. |
| `processing_log_*.log` | `11_outputs/logs/` | Python pipeline | Run log | Maybe | I include the most recent log if space allows. |

## Final Packaging Decision

I will update this table after final analysis is complete.
