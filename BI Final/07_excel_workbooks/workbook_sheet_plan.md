# Excel Workbook Sheet Plan

## Purpose

I use this sheet plan to design the Excel workbook before building formulas, charts, or pivots. The workbook should support validation and later analysis without mixing preparation notes with findings.

## Sheet Plan

| Order | Sheet Name | Source | Main Contents | Notes |
|---:|---|---|---|---|
| 1 | `README` | Manual documentation | Workbook purpose, update date, sheet map | I keep this first so the workbook is self-explanatory. |
| 2 | `Raw_Import` | Python export | Imported pre-analysis dataset | I do not edit source import values manually. |
| 3 | `Data_Dictionary` | Markdown data dictionary | Variable names, source files, descriptions, units | I use this for reviewer clarity. |
| 4 | `QA_Checks` | Excel formulas | Row counts, column counts, blank checks, duplicate checks | I treat this as the workbook validation gate. |
| 5 | `Integrated_Data` | Linked/validated import | Workbook-ready table | I use this as the source for later analysis objects. |
| 6 | `Chart_Prep` | Integrated data | Controlled ranges for visuals | I avoid adding interpretation here. |
| 7 | `Pivot_Prep` | Integrated data | Pivot-ready source columns | I keep pivot preparation separate from charts. |
| 8 | `Notes` | Manual documentation | Assumptions, issues, future decisions | I document preparation choices here. |

## Workbook Standards

- I freeze the top row on data-heavy sheets.
- I use Excel Tables for all rectangular datasets.
- I apply consistent date formatting as `yyyy-mm-dd`.
- I apply consistent numeric formatting based on each variable's unit.
- I avoid hidden sheets unless I document why a sheet is hidden.
- I avoid hardcoded formulas that cannot be audited.
