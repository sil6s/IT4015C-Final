# Power BI Final Analysis Guide

## Data Import

I will import:

`11_outputs/analysis_data/analysis_dataset_with_derived_variables.csv`

Main table name:

`FactEconomicMonthly`

## Data Model

I will use a simple star-style model:

- `FactEconomicMonthly` contains the prepared monthly economic variables and derived fields.
- `DimDate` contains one row per calendar date and supports filtering by year, quarter, and month.

Relationship:

`DimDate[Date]` one-to-many to `FactEconomicMonthly[date]`

## Recommended Dashboard Pages

| Page | Visuals |
|---|---|
| `Overview` | KPI cards for date range and observation count, plus a short project scope note. |
| `Inflation` | CPI overall and category line chart; CPI YoY line chart. |
| `Spending and Income` | PCE line chart; income and spending comparison; indexed comparison. |
| `Inflation vs Spending` | Scatter plot using CPI overall YoY and PCE YoY; optional trendline. |
| `Economic Context` | Unemployment, fed funds rate, and sentiment visuals. |
| `Data Quality` | Date coverage, missing-value notes, and source documentation references. |

## Suggested DAX Measures

```DAX
Observation Count = COUNTROWS('FactEconomicMonthly')
```

```DAX
Selected Start Date = MIN('DimDate'[Date])
```

```DAX
Selected End Date = MAX('DimDate'[Date])
```

```DAX
Average CPI Overall YoY % = AVERAGE('FactEconomicMonthly'[cpi_overall_yoy_pct])
```

```DAX
Average PCE YoY % = AVERAGE('FactEconomicMonthly'[pce_total_yoy_pct])
```

```DAX
Average Disposable Income YoY % = AVERAGE('FactEconomicMonthly'[disposable_income_yoy_pct])
```

```DAX
Latest PCE Total =
CALCULATE(
    MAX('FactEconomicMonthly'[pce_total]),
    LASTDATE('DimDate'[Date])
)
```

## Visual Design Notes

I will use consistent colors across pages. CPI overall should use the same color wherever it appears, and PCE total should also use a consistent color. I will avoid using color to imply good or bad outcomes unless the final report explicitly supports that interpretation.
