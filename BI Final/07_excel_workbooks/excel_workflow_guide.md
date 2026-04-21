# Excel Workflow Guide

## Purpose

I use Excel as a transparent review, validation, and chart-preparation environment. I am not using this guide to complete analysis yet. I am using it to define the workbook structure I will build after the Python pipeline produces the pre-analysis dataset.

## Recommended Workbook Name

`integrated_analysis_workbook_v01.xlsx`

I will save the final submission version as:

`integrated_analysis_workbook_final.xlsx`

## Recommended Workbook Structure

| Sheet Name | Purpose |
|---|---|
| `README` | I explain the workbook purpose, data source, refresh date, and sheet map. |
| `Raw_Import` | I import `pre_analysis_dataset.xlsx` or `pre_analysis_dataset.csv` exactly as exported. |
| `Data_Dictionary` | I summarize variable definitions from the project data dictionary. |
| `QA_Checks` | I run workbook-level validation formulas and compare row counts. |
| `Integrated_Data` | I store the clean working table that will feed charts and pivot tables later. |
| `Chart_Prep` | I create chart-ready fields and controlled ranges without interpreting results. |
| `Pivot_Prep` | I prepare pivot-table source ranges if needed later. |
| `Notes` | I document decisions, caveats, and unresolved preparation issues. |

## Import Steps

1. I open a new Excel workbook and save it in `07_excel_workbooks/`.
2. I import `04_merged_data/pre_analysis_dataset.xlsx` into the `Raw_Import` sheet.
3. I convert the imported range into an Excel Table named `tbl_pre_analysis_raw`.
4. I confirm that the `date` column is recognized as a date.
5. I confirm that numeric columns are recognized as numbers.
6. I copy or link the imported table into `Integrated_Data` only after the QA checks are reviewed.

## Excel Table and Named Range Plan

| Object | Type | Purpose |
|---|---|---|
| `tbl_pre_analysis_raw` | Excel Table | Original import from Python output. |
| `tbl_integrated_data` | Excel Table | Clean workbook-ready dataset. |
| `tbl_data_dictionary` | Excel Table | Variable definitions and source notes. |
| `tbl_qa_checks` | Excel Table | Workbook validation results. |
| `rng_analysis_start_date` | Named Range | Placeholder for later analysis-period decision. |
| `rng_analysis_end_date` | Named Range | Placeholder for later analysis-period decision. |

## Validation Formulas for Later Use

I can place these formulas in `QA_Checks` after importing the dataset:

```excel
=ROWS(tbl_pre_analysis_raw)
```

I use this to confirm the imported row count.

```excel
=COLUMNS(tbl_pre_analysis_raw)
```

I use this to confirm the imported column count.

```excel
=COUNTBLANK(tbl_pre_analysis_raw[date])
```

I use this to check for blank date values.

```excel
=SUM(--(COUNTIF(tbl_pre_analysis_raw[date],tbl_pre_analysis_raw[date])>1))
```

I use this to flag duplicate date entries.

```excel
=COUNTBLANK(tbl_pre_analysis_raw[pce_total])
```

I can adapt this formula for each variable to review missing values.

```excel
=MIN(tbl_pre_analysis_raw[date])
```

I use this to check the earliest imported date.

```excel
=MAX(tbl_pre_analysis_raw[date])
```

I use this to check the latest imported date.

## Conditional Formatting Plan

- I will highlight blank date cells in red.
- I will highlight missing numeric values in a neutral warning color.
- I will highlight duplicate dates in the QA sheet only.
- I will avoid using color to imply positive or negative interpretation before analysis.

## Chart Preparation Rules

- I will create chart-ready ranges in `Chart_Prep`, not directly from raw import.
- I will label every chart source range clearly.
- I will avoid adding conclusions or trend language to chart titles during the setup phase.
- I will use neutral titles such as `CPI Overall Over Time` only after charts are created later.

## Documentation Tab Notes

The `README` sheet should include:

- Workbook purpose.
- Data export file used.
- Pipeline run date.
- Sheet descriptions.
- Known preparation limitations.
- Statement that findings are not included until analysis is completed.
