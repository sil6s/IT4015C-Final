# Presentation Content

## Slide 1: Project Title

**Bullets**

- Inflation, Consumer Spending, Income, and Economic Conditions in the United States
- Integrated Data Analysis Final Project
- Prepared by: [My Name]

**Speaking Notes**

I introduce the project as an integrated analysis of inflation, spending, income, and broader economic context.

## Slide 2: Research Focus

**Bullets**

- I analyze monthly U.S. economic data from 2016-01-01 through 2026-02-01.
- I compare inflation measures with consumer spending and income.
- I include unemployment, interest rates, and consumer sentiment as economic context.

**Speaking Notes**

I explain that the project is descriptive and evidence-based, and I avoid making causal claims.

## Slide 3: Data Preparation

**Bullets**

- I used the complete monthly overlap period across required variables.
- I excluded incomplete required-variable months.
- I calculated YoY growth, MoM growth, and 2016-base indexed values.

**Visual**

- Optional table: `analysis_adjustments_log.csv`

**Speaking Notes**

I describe how I aligned the data by month before analysis.

## Slide 4: Inflation Trends

**Bullets**

- CPI overall and category-level CPI measures are shown together.
- I use category-level CPI to avoid relying only on the broad index.

**Visual**

- `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_01_inflation_trends.png`

**Speaking Notes**

I explain what the chart compares and avoid overstating the cause of any movement.

## Slide 5: Consumer Spending

**Bullets**

- PCE total is the primary consumer spending variable.
- The chart shows the spending series across the aligned analysis period.

**Visual**

- `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_02_consumer_spending_pce.png`

**Speaking Notes**

I describe the spending measure and connect it to the project question.

## Slide 6: Income and Spending

**Bullets**

- I compare disposable personal income and PCE total.
- This helps me evaluate spending alongside income context.

**Visual**

- `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_03_income_vs_spending.png`

**Speaking Notes**

I explain why income belongs in the project and note that comparison does not automatically prove causation.

## Slide 7: Inflation vs Spending Growth

**Bullets**

- I compare CPI overall YoY growth with PCE total YoY growth.
- The computed correlation is 0.660.
- I interpret the relationship descriptively.

**Visual**

- `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_04_inflation_vs_spending_scatter.png`

**Speaking Notes**

I explain the scatter plot and regression line as descriptive tools.

## Slide 8: Economic Context

**Bullets**

- I include unemployment, interest rates, and consumer sentiment as context variables.
- I chart them separately because they use different scales.

**Visual**

- `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_05_economic_context.png`

**Speaking Notes**

I explain that these variables help frame the economic environment around inflation and spending.

## Slide 9: Indexed Comparison

**Bullets**

- I set CPI overall, PCE total, and disposable income to a 2016 average of 100.
- This allows comparison across variables with different units.

**Visual**

- `/Users/silascurry/Documents/New project/Project_Data/11_outputs/charts/chart_06_indexed_comparison.png`

**Speaking Notes**

I explain why indexing improves comparability.

## Slide 10: Key Observations

**Bullets**

- I observed that the main variables ended above their first analysis-month levels.
- I observed that CPI categories did not move identically.
- I observed that correlations should be interpreted carefully because the data are time series.

**Speaking Notes**

I connect observations to computed outputs and prepare the audience for the written findings.

## Slide 11: Limitations

**Bullets**

- The analysis is descriptive, not causal.
- The analysis period is constrained by variable overlap.
- Source definitions and units differ across datasets.
- Some variables are indexes while others are monetary or percentage measures.

**Speaking Notes**

I explain that these limitations shape how strongly I can interpret the results.

## Slide 12: Closing

**Bullets**

- I integrated multiple economic datasets into one aligned monthly analysis file.
- I used Python, Excel planning, and Power BI planning to support a reproducible workflow.
- I based observations on computed tables and charts.

**Speaking Notes**

I close by emphasizing the integrated workflow and evidence-based interpretation.
