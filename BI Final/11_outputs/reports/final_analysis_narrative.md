# Final Analysis Narrative

## Analysis Scope and Data Preparation

I analyzed the integrated monthly dataset over the complete required-variable overlap period from **2016-01-01** through **2026-02-01**. I used complete monthly observations for CPI overall, CPI food, CPI shelter, CPI transportation, PCE total, disposable personal income, the federal funds rate, consumer sentiment, and the unemployment rate.

I selected this period because it is the window where the main inflation, spending, income, and economic context variables align. I excluded incomplete required-variable months before analysis. The adjustment log records the exact exclusions and the reason for each preparation choice.

## Derived Variables

I calculated year-over-year percentage change for CPI overall, CPI food, CPI shelter, CPI transportation, PCE total, and disposable personal income. I calculated each year-over-year value as:

`((current month value / value from same month one year earlier) - 1) * 100`

I also calculated month-over-month percentage change for the same variables. I used month-over-month values cautiously because they are more sensitive to short-run movement. I did not calculate month-over-month change across a missing calendar month.

Finally, I created indexed variables using the 2016 average as the base value:

`(current value / average value during 2016) * 100`

This lets me compare CPI, spending, and income on a common scale even though the original units differ.

## Descriptive Analysis

The final aligned dataset contains **121 monthly observations**. Over the analysis window, CPI overall increased by **37.79%** from the first available analysis month to the latest analysis month. PCE total increased by **73.23%**, and disposable personal income increased by **70.19%** over the same first-to-latest window.

For year-over-year growth, CPI overall averaged **3.33%** across non-missing YoY observations, with a minimum of **0.20%** and a maximum of **8.98%**. PCE total YoY growth averaged **5.81%**, while disposable personal income YoY growth averaged **5.75%**.

## Correlation Results

I calculated correlation matrices for both level variables and year-over-year growth variables. In the level-variable correlation matrix, the three strongest absolute correlations with PCE total were:

- CPI Overall: **0.994**
- CPI Shelter: **0.986**
- CPI Food: **0.986**

For year-over-year growth, the strongest absolute correlations with PCE total YoY growth were:

- CPI Transportation: **0.790**
- CPI Overall: **0.660**
- CPI Food: **0.284**

I interpret these correlations as descriptive relationships, not causal evidence. Because these are macroeconomic time-series variables, shared time trends and common economic shocks can influence correlations.

## Visualization Explanations

### Inflation Measures Over Time

The inflation trends chart compares CPI overall with food, shelter, and transportation CPI indexes. I use this chart to show how the category-level CPI measures move relative to the broad CPI index within the aligned analysis period.

Chart file: `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_01_inflation_trends.png`

### Consumer Spending Over Time

The consumer spending chart shows PCE total over the aligned monthly analysis period. I use this visual as the main spending-series reference for the project.

Chart file: `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_02_consumer_spending_pce.png`

### Income and Consumer Spending

The income and spending chart compares PCE total with disposable personal income using their source-reported levels. I use this visual to examine the two consumer-side measures side by side before making any interpretation about their relationship.

Chart file: `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_03_income_vs_spending.png`

### Inflation and Spending Growth

The scatter plot compares CPI overall year-over-year percentage change with PCE total year-over-year percentage change. The fitted line summarizes the direction of the linear association in the plotted observations. The correlation for these two YoY growth variables is **0.660**.

Chart file: `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_04_inflation_vs_spending_scatter.png`

### Economic Context Variables

The economic context chart presents unemployment, the federal funds rate, and consumer sentiment in separate panels. I use separate panels because the variables have different units and scales.

Chart file: `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_05_economic_context.png`

### Indexed Comparison

The indexed comparison chart sets CPI overall, PCE total, and disposable personal income equal to 100 based on their 2016 average. I use this chart to compare relative movement across variables with different original units.

Chart file: `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_06_indexed_comparison.png`

## Key Observations

- I observed that the main CPI, spending, and income variables all ended the analysis window above their first-month levels, based on the first-to-latest percentage changes computed from the aligned dataset.
- I observed that CPI category indexes did not have identical first-to-latest changes, which supports the value of including category-level inflation variables rather than only using CPI overall.
- I observed that level-variable correlations with PCE total were generally high for variables that also trend over time, so I treated the growth-rate correlation matrix as an important supporting check.
- I observed that the CPI overall YoY and PCE total YoY scatter plot produced a correlation of **0.660**, which I report as a descriptive association rather than a causal claim.
- I observed that the economic context variables require separate visual treatment because unemployment, interest rates, and sentiment are measured on different scales.

## Transition Into Findings

These outputs give me the evidence base for the findings section. In the final findings, I should connect each claim directly to a chart, summary statistic, or correlation table. I should avoid claiming causation unless I add a separate causal research design, which this project does not currently include.
