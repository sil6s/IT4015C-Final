# Reproducibility Checklist

## Purpose

This checklist confirms that the project can be reviewed, understood, and reproduced without relying on hidden manual steps. It ensures transparency across data sourcing, preparation, analysis, and final outputs.

---

## Environment

- [x] Project tools and environment are documented (Power BI, data sources).
- [x] All required software (Power BI Desktop / Service) is clearly identified.
- [x] Data preparation steps are documented in methodology notes.
- [x] Workflow from raw data to final dashboard is clearly explained.

---

## Data

- [x] Raw datasets are sourced from publicly available and documented sources.
- [x] Raw files are not manually altered after download.
- [x] Cleaned datasets can be recreated using documented preparation steps.
- [x] Integrated dataset structure is clearly defined and reproducible.
- [x] All data sources are explicitly listed and referenced.

---

## Data Preparation and Integration

- [x] Date fields are standardized across all datasets.
- [x] Variable naming conventions are consistent and documented.
- [x] Data type conversions are clearly defined.
- [x] CPI data transformation (wide to long format) is documented.
- [x] Integration logic using date as the key is clearly explained.
- [x] Handling of missing values and coverage differences is documented.

---

## Analysis Methods

- [x] All derived metrics (YoY growth, indexed values) are defined and explained.
- [x] Lagged variables (3-month inflation lag) are documented and justified.
- [x] Analytical decisions are explained in methodology and project log.
- [x] Key insights are directly tied to computed metrics and visuals.

---

## Visualization

- [x] All dashboard pages are clearly structured and labeled.
- [x] Each visual supports a defined analytical question.
- [x] Advanced visualization (Deneb) is implemented and documented.
- [x] Custom visual logic (scatter + regression + lag) is explained.

---

## Outputs

- [x] Final Power BI dashboard is complete and exportable.
- [x] All figures used in the report are derived from the dashboard.
- [x] Visual outputs are organized and consistently named.
- [x] Final report integrates visuals with analysis and explanation.

---

## Final Review

- [x] The project can be reviewed from raw data through final output.
- [x] All major steps are documented (data, cleaning, analysis, visualization).
- [x] There are no hidden or undocumented transformations.
- [x] The workflow can be explained clearly from start to finish.
- [x] Raw, intermediate, and final outputs are conceptually distinguished.

---

## Summary

This project meets reproducibility expectations by clearly documenting data sources, preparation steps, analytical methods, and final outputs. The workflow is transparent, structured, and can be followed without relying on undocumented steps.
