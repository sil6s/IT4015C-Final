# Data Source Documentation

## Purpose of This Document

I use this document to record the datasets I selected, why I selected them, and how each file supports my integrated data analysis project. This documentation is part of my evidence that the project is independently sourced, deliberate, and reproducible.

I am not using this document to state findings. I am using it to justify dataset selection and clarify the role of each variable before analysis begins.

## Source Summary Table

| Dataset | Raw File | Variable Purpose | Source Organization | Format | Frequency | Project Role |
|---|---|---|---|---|---|---|
| CPI Overall | `CPI_Overall.xlsx` | Broad consumer price index | U.S. Bureau of Labor Statistics | Excel | Monthly | Primary inflation variable |
| CPI Food | `CPI_Food.xlsx` | Food price index category | U.S. Bureau of Labor Statistics | Excel | Monthly | Supporting inflation detail |
| CPI Shelter | `CPI_Shelter.xlsx` | Shelter price index category | U.S. Bureau of Labor Statistics | Excel | Monthly | Supporting inflation detail |
| CPI Transportation | `CPI_Transportation.xlsx` | Transportation price index category | U.S. Bureau of Labor Statistics | Excel | Monthly | Supporting inflation detail |
| PCE Total | `PCE_Total.csv` | Personal consumption expenditures | Federal Reserve Economic Data / BEA series | CSV | Monthly | Primary spending variable |
| PCE Price Index / PCECC96 | `PCE_Price_Index.csv` | Price-related PCE comparison series | Federal Reserve Economic Data / BEA series | CSV | Quarterly in current file | Supporting inflation comparison variable |
| Disposable Personal Income | `Disposable_Income.csv` | Disposable personal income | Federal Reserve Economic Data / BEA series | CSV | Monthly | Supporting income context |
| Federal Funds Rate | `Interest_Rate_FedFunds.csv` | Federal funds effective rate | Federal Reserve Economic Data / Federal Reserve source series | CSV | Monthly | Supporting monetary policy context |
| Consumer Sentiment | `Consumer_Sentiment.csv` | Consumer sentiment index | Federal Reserve Economic Data / University of Michigan source series | CSV | Monthly | Supporting household context |
| Unemployment Rate | `Unemployment_Rate.csv` | Civilian unemployment rate | Federal Reserve Economic Data / BLS source series | CSV | Monthly | Supporting labor market context |

## Dataset Notes

### CPI Overall

- **Dataset name:** CPI Overall
- **Raw file:** `01_raw_data/inflation/CPI_Overall.xlsx`
- **Source organization:** U.S. Bureau of Labor Statistics
- **Variable purpose:** I use this file as the broad inflation measure for consumer prices.
- **Frequency:** Monthly
- **Why I included it:** I need a general consumer price index to anchor the inflation side of the project.
- **How it contributes:** It provides the broad inflation measure that later analysis can compare with spending and supporting economic variables.
- **Known limitations:** CPI is an index, not a dollar amount. I need to document transformations carefully before comparing it with spending or income series.
- **Role:** Primary analysis variable.

### CPI Food

- **Dataset name:** CPI Food
- **Raw file:** `01_raw_data/inflation/CPI_Food.xlsx`
- **Source organization:** U.S. Bureau of Labor Statistics
- **Variable purpose:** I use this file to represent food-related price movements as a major consumer budget category.
- **Frequency:** Monthly
- **Why I included it:** Food is a visible and recurring consumer expense category, so it helps me prepare a more detailed inflation view.
- **How it contributes:** It supports category-level comparison after the main dataset is prepared.
- **Known limitations:** Category-specific CPI series should not be treated as the same concept as overall inflation.
- **Role:** Supporting contextual variable.

### CPI Shelter

- **Dataset name:** CPI Shelter
- **Raw file:** `01_raw_data/inflation/CPI_Shelter.xlsx`
- **Source organization:** U.S. Bureau of Labor Statistics
- **Variable purpose:** I use this file to represent shelter-related consumer price changes.
- **Frequency:** Monthly
- **Why I included it:** Shelter is a major household cost category and can add useful context to inflation preparation.
- **How it contributes:** It helps prepare the dataset for later category-level inflation comparisons.
- **Known limitations:** Shelter CPI methodology has specific measurement conventions, so I need to describe it carefully in the final report if I use it in interpretation.
- **Role:** Supporting contextual variable.

### CPI Transportation

- **Dataset name:** CPI Transportation
- **Raw file:** `01_raw_data/inflation/CPI_Transportation.xlsx`
- **Source organization:** U.S. Bureau of Labor Statistics
- **Variable purpose:** I use this file to represent transportation-related consumer price changes.
- **Frequency:** Monthly
- **Why I included it:** Transportation is another major consumer category that can support a broader view of inflation.
- **How it contributes:** It provides additional category-level detail for later visualization and comparison.
- **Known limitations:** Transportation CPI may reflect multiple components, so I need to avoid overgeneralizing the category without reviewing source definitions.
- **Role:** Supporting contextual variable.

### PCE Total

- **Dataset name:** PCE Total
- **Raw file:** `01_raw_data/spending/PCE_Total.csv`
- **Source organization:** Federal Reserve Economic Data, based on BEA source series
- **Variable purpose:** I use this file as the main consumer spending measure.
- **Frequency:** Monthly
- **Why I included it:** The project is centered on inflation and consumer spending, so I need a broad spending measure.
- **How it contributes:** It provides the spending side of the integrated dataset.
- **Known limitations:** PCE is measured differently from CPI, so later comparisons must respect differences in source concepts and units.
- **Role:** Primary analysis variable.

### PCE Price Index / PCECC96

- **Dataset name:** PCE Price Index / related PCE price file
- **Raw file:** `01_raw_data/inflation/PCE_Price_Index.csv`
- **Source organization:** Federal Reserve Economic Data, based on BEA source series
- **Variable purpose:** I use this file as a supporting price-related comparison series.
- **Frequency:** The current file appears quarterly based on the downloaded observations.
- **Why I included it:** It gives me an additional price-related perspective that may be useful when explaining dataset choices later.
- **How it contributes:** It can support inflation comparison decisions after I review frequency alignment and scope.
- **Known limitations:** The current file frequency differs from the monthly files, so the pipeline preserves it and flags coverage/frequency issues rather than forcing an analytical assumption.
- **Role:** Supporting contextual variable.

### Disposable Personal Income

- **Dataset name:** Disposable Personal Income
- **Raw file:** `01_raw_data/income/Disposable_Income.csv`
- **Source organization:** Federal Reserve Economic Data, based on BEA source series
- **Variable purpose:** I use this file as income context.
- **Frequency:** Monthly
- **Why I included it:** Spending behavior should be prepared alongside income context, even if the final analysis later decides how heavily to use it.
- **How it contributes:** It helps frame consumer spending in relation to household financial capacity.
- **Known limitations:** Aggregate income data does not show distributional differences across households.
- **Role:** Supporting contextual variable.

### Federal Funds Rate

- **Dataset name:** Federal Funds Rate
- **Raw file:** `01_raw_data/economic_conditions/Interest_Rate_FedFunds.csv`
- **Source organization:** Federal Reserve Economic Data / Federal Reserve source series
- **Variable purpose:** I use this file as monetary policy context.
- **Frequency:** Monthly
- **Why I included it:** Interest rates are an important economic condition that can be documented alongside inflation and spending.
- **How it contributes:** It provides context for the broader economic environment.
- **Known limitations:** The federal funds rate is not a direct household-level variable, so later interpretation must be cautious.
- **Role:** Supporting contextual variable.

### Consumer Sentiment

- **Dataset name:** Consumer Sentiment
- **Raw file:** `01_raw_data/economic_conditions/Consumer_Sentiment.csv`
- **Source organization:** Federal Reserve Economic Data / University of Michigan source series
- **Variable purpose:** I use this file as a household expectations and confidence measure.
- **Frequency:** Monthly
- **Why I included it:** Consumer sentiment can provide non-price context for consumer behavior.
- **How it contributes:** It supports later dashboard and analysis design as a contextual series.
- **Known limitations:** Sentiment is survey-based and should be interpreted differently from transaction or administrative measures.
- **Role:** Supporting contextual variable.

### Unemployment Rate

- **Dataset name:** Unemployment Rate
- **Raw file:** `01_raw_data/economic_conditions/Unemployment_Rate.csv`
- **Source organization:** Federal Reserve Economic Data / BLS source series
- **Variable purpose:** I use this file as labor market context.
- **Frequency:** Monthly
- **Why I included it:** Labor market conditions can provide important background for consumer spending analysis.
- **How it contributes:** It helps prepare a more complete economic context for the final project.
- **Known limitations:** The unemployment rate is an aggregate measure and does not capture all labor market conditions.
- **Role:** Supporting contextual variable.

## Documentation Safeguards

- I keep raw files separate from cleaned and merged files.
- I document whether each variable is primary or supporting.
- I avoid making any findings in the source documentation stage.
- I identify frequency differences before analysis.
- I preserve source file names in the data dictionary and validation outputs.
