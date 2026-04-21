# Excel Final Analysis Guide

## Workbook Structure

I will build the final Excel workbook with these sheets:

| Sheet | Purpose |
|---|---|
| `README` | I explain the workbook purpose, data source, refresh date, and sheet map. |
| `Analysis_Data` | I import `analysis_dataset_with_derived_variables.xlsx`. |
| `Summary_Stats` | I import or recreate summary statistics. |
| `Correlations` | I import or recreate correlation matrices. |
| `Chart_Inflation` | I recreate the CPI overall and category trend chart. |
| `Chart_Spending` | I recreate the PCE chart. |
| `Chart_Income_Spending` | I recreate the income versus spending chart. |
| `Chart_Scatter` | I recreate the inflation versus spending growth scatter plot. |
| `Chart_Context` | I recreate or reference economic context visuals. |
| `Notes` | I document assumptions, exclusions, and interpretation boundaries. |

## Import File

I will import:

`11_outputs/analysis_data/analysis_dataset_with_derived_variables.xlsx`

## Excel Formulas

### Year-over-Year Percent Change

If my table is named `tbl_analysis`, I can calculate CPI overall YoY percent change with:

```excel
=IFERROR(([@cpi_overall]/XLOOKUP(EDATE([@date],-12),tbl_analysis[date],tbl_analysis[cpi_overall])-1)*100,"")
```

I can replace `cpi_overall` with `cpi_food`, `cpi_shelter`, `cpi_transportation`, `pce_total`, or `disposable_income`.

### Month-over-Month Percent Change

```excel
=IFERROR(([@cpi_overall]/XLOOKUP(EDATE([@date],-1),tbl_analysis[date],tbl_analysis[cpi_overall])-1)*100,"")
```

I will use this only when the prior calendar month exists in the table.

### 2016 Base Index

```excel
=([@cpi_overall]/AVERAGEIFS(tbl_analysis[cpi_overall],tbl_analysis[date],">="&DATE(2016,1,1),tbl_analysis[date],"<="&DATE(2016,12,31)))*100
```

I can replace `cpi_overall` with any numeric variable I want to index.

## Chart Recreation Instructions

### Inflation Trends

- Use `date` on the x-axis.
- Add `cpi_overall`, `cpi_food`, `cpi_shelter`, and `cpi_transportation` as line series.
- Use a line chart with a clear legend.

### Consumer Spending

- Use `date` on the x-axis.
- Add `pce_total` as the line series.
- Use a single-series line chart.

### Income vs Spending

- Use `date` on the x-axis.
- Add `pce_total` and `disposable_income`.
- Use a line chart and keep the legend visible.

### Inflation vs Spending Scatter

- Use `cpi_overall_yoy_pct` on the x-axis.
- Use `pce_total_yoy_pct` on the y-axis.
- Add a linear trendline and display the equation only if required.

### Indexed Comparison

- Use `date` on the x-axis.
- Add `cpi_overall_index_2016_100`, `pce_total_index_2016_100`, and `disposable_income_index_2016_100`.
- Label the y-axis as `Index, 2016 Average = 100`.
