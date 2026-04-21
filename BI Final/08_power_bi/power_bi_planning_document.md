# Power BI Planning Document

## Purpose

I use this document to plan the Power BI model and dashboard structure before building visuals. I am not using it to interpret the data or describe results.

## Recommended Power BI File Name

`inflation_spending_dashboard_v01.pbix`

Final submission version:

`inflation_spending_dashboard_final.pbix`

## Data Import Plan

I will import:

`04_merged_data/pre_analysis_dataset.csv`

Power BI import settings:

- `date` should be set to Date.
- Numeric economic variables should be set to Decimal Number.
- The table should be named `FactEconomicMonthly`.
- I will avoid summarizing text fields.

## Proposed Data Model

### `FactEconomicMonthly`

This table contains one row per available observation date in the integrated monthly dataset. It includes inflation, spending, income, interest rate, unemployment, and sentiment variables.

Recommended columns:

- `date`
- `cpi_overall`
- `cpi_food`
- `cpi_shelter`
- `cpi_transportation`
- `pce_price_index`
- `pce_total`
- `disposable_income`
- `fed_funds_rate`
- `consumer_sentiment`
- `unemployment_rate`

### `DimDate`

I will create a date table in Power BI so slicers and time intelligence are organized cleanly.

Recommended columns:

- `Date`
- `Year`
- `Quarter`
- `Month Number`
- `Month Name`
- `Year-Month`

Relationship:

- `DimDate[Date]` one-to-many with `FactEconomicMonthly[date]`

## Recommended Dashboard Pages

| Page | Purpose | Notes |
|---|---|---|
| `Project Overview` | I explain the dashboard purpose, data sources, and scope. | This page should not state findings until analysis is complete. |
| `Inflation Measures` | I prepare visuals for overall and category-level CPI measures. | I use neutral labels and avoid interpretive captions during setup. |
| `Spending and Income` | I prepare visuals for PCE and disposable income. | I keep the page ready for later comparison. |
| `Economic Conditions` | I prepare visuals for interest rates, unemployment, and sentiment. | I frame these as context variables. |
| `Integrated View` | I prepare a dashboard page where selected variables can be viewed together. | I use slicers and controlled filters. |
| `Data Quality` | I document missing values, date coverage, and source notes. | This page strengthens transparency. |

## Suggested Slicers and Filters

- Date range slicer using `DimDate[Date]`.
- Year slicer using `DimDate[Year]`.
- Variable group selector if I create a field parameter later.
- Data coverage filter if I add a coverage flag after QA review.

## Structural DAX Placeholders

I can add these later as structural helpers. I will not treat them as findings.

```DAX
Selected Start Date = MIN('DimDate'[Date])
```

```DAX
Selected End Date = MAX('DimDate'[Date])
```

```DAX
Observation Count = COUNTROWS('FactEconomicMonthly')
```

```DAX
Missing PCE Total Count =
COUNTROWS(
    FILTER(
        'FactEconomicMonthly',
        ISBLANK('FactEconomicMonthly'[pce_total])
    )
)
```

## Advanced Feature Planned for Later

I plan to consider a Power BI field parameter that lets the viewer switch among prepared economic variables on the same visual. This would make the dashboard more flexible while keeping the data model organized.

I will only add this after the prepared dataset has passed validation and I have decided which variables belong in the final dashboard.

## Import Verification Steps

1. I import `pre_analysis_dataset.csv`.
2. I confirm the row count against Python validation outputs.
3. I confirm the date range against `merged_dataset_validation_summary.csv`.
4. I confirm each numeric column is typed as Decimal Number.
5. I create or verify the date table.
6. I create the date relationship.
7. I build a `Data Quality` page before final dashboard interpretation.
