# Methodology Notes

## Purpose

This document captures the full methodology used to prepare, integrate, analyze, and visualize macroeconomic data for the Applied Business Intelligence project. It serves as a technical reference for how the final dashboard and analysis were constructed.

---

## Data Collection

Data was collected from official U.S. economic data sources to ensure reliability and consistency.

### Sources Used

- **Bureau of Labor Statistics (BLS)**
  - Consumer Price Index (CPI-U)
  - Categories: Overall, Food, Shelter, Transportation

- **Bureau of Economic Analysis (BEA)**
  - Personal Consumption Expenditures (PCE)
  - Disposable Personal Income

- **Federal Reserve Economic Data (FRED)**
  - Federal Funds Rate
  - Unemployment Rate

- **University of Michigan**
  - Consumer Sentiment Index

### Selection Rationale

These datasets were selected because:
- They represent **core macroeconomic indicators**
- They are **published at consistent monthly intervals**
- They allow analysis of relationships between:
  - inflation
  - consumer behavior
  - income
  - monetary policy
  - economic sentiment

---

## Data Cleaning

### Date Standardization

- All datasets were converted to a **monthly date format**
- Date columns were unified into a single `date` field
- Ensured alignment across all datasets for time series analysis

### Variable Naming

- Renamed columns to consistent naming conventions:
  - `cpi_overall_yoy_pct`
  - `cpi_food_yoy_pct`
  - `cpi_shelter_yoy_pct`
  - `cpi_transportation_yoy_pct`
  - `pce_total_yoy_pct`
  - `disposable_income_yoy_pct`

### Data Type Conversion

- Dates → Date format
- Numeric fields → Decimal / Whole Number
- Percentage values stored as numeric and formatted in Power BI

### Handling BLS CPI Format

- BLS CPI data was originally in **wide format (monthly columns)**
- Converted to **long format**:
  - Month columns unpivoted into rows
  - Resulting structure: `date`, `value`, `category`

### Raw vs Clean Data

- Raw data was preserved separately
- All transformations were applied in a **cleaned dataset layer**
- This allows reproducibility and auditing

---

## Data Integration

### Integration Key

- All datasets were joined using the **date field**
- Monthly granularity ensured consistent alignment

### Merge Strategy

- Used an **outer join** during preparation
- This ensured:
  - no data loss across sources
  - visibility into missing values

### Missing Data Handling

- Reviewed null values after merging
- Identified:
  - differences in coverage across datasets
  - missing recent values in certain series
- Retained rows with partial data where appropriate for time series continuity

---

## Quality Assurance (QA)

### Validation Checks

- Verified date continuity across all datasets
- Checked for:
  - duplicate rows
  - incorrect joins
  - misaligned time periods

### Metric Validation

- Cross-checked YoY calculations against expected economic trends
- Confirmed:
  - inflation spikes (2021–2022)
  - unemployment spike (2020)
  - interest rate increases (post-2022)

### Remaining Considerations

- Some datasets have different reporting lags
- Minor gaps exist in most recent months for certain variables

---

## Analysis Methods

### Derived Metrics

#### Year-over-Year (YoY) Growth

Used to smooth short-term volatility and capture meaningful trends:

- Inflation YoY
- Consumer Spending YoY
- Disposable Income YoY

---

#### Index Normalization

- Base year: **2016 = 100**
- Applied to:
  - CPI
  - Consumer Spending
  - Disposable Income

Purpose:
- Compare relative growth across variables with different units

---

#### Lag Analysis

- Created **3-month lagged inflation variable**
- Used to analyze delayed policy response

Purpose:
- Evaluate how interest rates respond to prior inflation conditions

---

## Visualization Methods

### Standard Power BI Visuals

- Line charts (time series trends)
- KPI cards (latest values)
- Indexed comparison charts
- Multi-variable dashboards

Each dashboard page focused on a specific analytical question:
- Executive summary
- Inflation decomposition
- Income vs spending
- Economic context

---

### Advanced Visualization (Deneb)

A custom **Deneb (Vega-Lite) visual** was implemented.

#### Structure

- X-axis: Inflation (lagged 3 months)
- Y-axis: Federal Funds Rate
- Color: Time progression
- Regression line included

#### Purpose

- Move beyond time series comparison
- Identify **relationship between variables**
- Reveal **delayed monetary policy response**

---

## Key Methodological Decisions

- Used **YoY instead of MoM** to reduce noise
- Used **outer joins** to preserve full dataset coverage
- Used **indexing** for cross-variable comparison
- Used **lag transformation** to capture temporal relationships
- Used **Deneb** to introduce advanced analytical visualization

---

## Final Outcome

This methodology enabled:

- Integrated analysis across multiple macroeconomic indicators
- Identification of:
  - inflation volatility vs persistence
  - income and spending alignment
  - divergence in sentiment vs labor recovery
  - delayed monetary policy response

The result is a multi-layered BI dashboard that supports both descriptive and explanatory analysis.
