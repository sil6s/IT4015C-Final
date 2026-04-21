# Integrated Dataset Data Dictionary

## Purpose

I use this data dictionary to define the variables expected in the cleaned and merged datasets. This document is a preparation artifact, not an analysis artifact. I am documenting what each field means, where it comes from, and how it should be handled before I begin interpretation.

## Integrated Dataset Fields

| Variable Name | Source File | Original Source Series | Description | Frequency | Unit | Expected Data Type | Transformation Notes | Missing Value Notes | Role in Project | Inclusion Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `date` | All files | Varies by file | Standardized observation date used for joins | Monthly target, with quarterly source retained where applicable | Date | Date | I standardize all source date fields into `YYYY-MM-DD` month-start dates. | Missing dates are not expected within individual observations, but coverage gaps may exist across sources. | Integration key | Included |
| `cpi_overall` | `CPI_Overall.xlsx` | `CUSR0000SA0` | Consumer Price Index for all items | Monthly | Index, 1982-84=100 | Float | I reshape the BLS workbook from wide month columns into a tidy date/value structure. | Missing values may occur for incomplete current-year months. | Primary inflation variable | Included |
| `cpi_food` | `CPI_Food.xlsx` | `CUSR0000SAF1` | Consumer Price Index for food | Monthly | Index, 1982-84=100 | Float | I reshape the BLS workbook from wide month columns into a tidy date/value structure. | Missing values may occur for incomplete current-year months. | Supporting inflation detail | Included |
| `cpi_shelter` | `CPI_Shelter.xlsx` | `CUSR0000SAH1` | Consumer Price Index for shelter | Monthly | Index, 1982-84=100 | Float | I reshape the BLS workbook from wide month columns into a tidy date/value structure. | Missing values may occur for incomplete current-year months. | Supporting inflation detail | Included |
| `cpi_transportation` | `CPI_Transportation.xlsx` | `CUSR0000SAT` | Consumer Price Index for transportation | Monthly | Index, 1982-84=100 | Float | I reshape the BLS workbook from wide month columns into a tidy date/value structure. | Missing values may occur for incomplete current-year months. | Supporting inflation detail | Included |
| `pce_price_index` | `PCE_Price_Index.csv` | `PCECC96` | Price-related PCE comparison series from downloaded file | Quarterly in current file | Source-defined index or chained dollars depending on final source metadata review | Float | I preserve the downloaded observation frequency and join on available dates. | Quarterly coverage will naturally create missing months in a monthly master dataset. | Supporting inflation comparison variable | Included with caution |
| `pce_total` | `PCE_Total.csv` | `PCE` | Personal consumption expenditures | Monthly | Billions of dollars, source-defined | Float | I rename the source series column and standardize the date field. | Missing values should be reviewed if present. | Primary spending variable | Included |
| `disposable_income` | `Disposable_Income.csv` | `DSPI` | Disposable personal income | Monthly | Billions of dollars, source-defined | Float | I rename the source series column and standardize the date field. | Missing values should be reviewed if present. | Supporting income context | Included |
| `fed_funds_rate` | `Interest_Rate_FedFunds.csv` | `FEDFUNDS` | Federal funds effective rate | Monthly | Percent | Float | I rename the source series column and standardize the date field. | Missing values should be reviewed if present. | Supporting monetary policy context | Included |
| `consumer_sentiment` | `Consumer_Sentiment.csv` | `UMCSENT` | Consumer sentiment index | Monthly | Index | Float | I rename the source series column and standardize the date field. | Survey series may contain missing months or source-specific gaps. | Supporting household context | Included |
| `unemployment_rate` | `Unemployment_Rate.csv` | `UNRATE` | Civilian unemployment rate | Monthly | Percent | Float | I rename the source series column and standardize the date field. | Missing values should be reviewed if present. | Supporting labor market context | Included |

## Metadata and QA Fields

| Variable Name | Source File | Original Source Series | Description | Frequency | Unit | Expected Data Type | Transformation Notes | Missing Value Notes | Role in Project | Inclusion Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `source_file` | Cleaned individual exports | Pipeline-generated | Name of the raw file used to create a cleaned dataset | N/A | Text | String | I include this in cleaned long files where useful for traceability. | Not applicable. | Audit support | Included where useful |
| `source_series` | Cleaned individual exports | Pipeline-generated | Source series code or source column name | N/A | Text | String | I add this so I can trace renamed variables back to source labels. | Not applicable. | Audit support | Included where useful |
| `value_missing_flag` | QA outputs | Pipeline-generated | Indicates whether an observation has a missing value | N/A | Boolean | Boolean | I create missing-value summaries rather than treating missing values as findings. | Used only for QA. | QA support | Included in reports |

## Notes for Later Completion

- I will update units after I confirm source metadata for every final variable used in interpretation.
- I will document any transformations such as percent change, indexing, normalization, or lagging only if I choose to use them later.
- I will not add analytical findings to this data dictionary.
