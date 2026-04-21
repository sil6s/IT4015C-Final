# Project Log

## Purpose

This project log documents the step-by-step workflow used to build the Applied Business Intelligence project. It captures what was completed, when it was completed, and why key decisions were made. This demonstrates that the final deliverable was developed through a structured and iterative process rather than assembled at the end.

---

## Log Entries

| Date | Work Completed | Files or Folders Affected | Decision Made | Follow-Up Needed |
|---|---|---|---|---|
| April 14, 2026 | Identified project topic and selected macroeconomic focus (inflation, spending, income, policy) | Planning notes | Chose macroeconomic analysis due to strong data availability and clear relationships | Confirm datasets and sources |
| April 15, 2026 | Collected CPI data from BLS and reviewed structure | `/data/raw/bls/` | Selected CPI-U and key categories (food, shelter, transportation) | Convert wide format to long format |
| April 16, 2026 | Collected PCE and disposable income data from BEA | `/data/raw/bea/` | Selected monthly PCE and income for consistency with CPI | Align time ranges across datasets |
| April 17, 2026 | Imported datasets into Power BI and began cleaning | `/powerbi/model/` | Standardized date fields and variable naming conventions | Validate joins after cleaning |
| April 18, 2026 | Created YoY measures and calculated key metrics | Power BI measures table | Chose YoY instead of MoM to reduce volatility and improve interpretability | Verify calculations against expected trends |
| April 19, 2026 | Built initial dashboard pages (executive, inflation, income vs spending) | Power BI report pages | Structured dashboard into multiple pages for clarity and storytelling | Add economic context page |
| April 20, 2026 | Integrated FRED data (interest rates, unemployment) and sentiment data | `/data/raw/fred/`, `/data/raw/sentiment/` | Included policy and sentiment variables to provide broader economic context | Align missing values and coverage gaps |
| April 20, 2026 | Built economic context dashboard and refined visuals | Power BI report pages | Grouped unemployment, interest rates, and sentiment into a single contextual view | Improve labeling and insights |
| April 21, 2026 | Developed advanced Deneb visual (lagged inflation vs interest rates) | Power BI Deneb visual | Introduced 3-month lag to analyze delayed policy response | Validate interpretation of regression trend |
| April 21, 2026 | Finalized dashboard layout, insights, and formatting | Full Power BI report | Prioritized clarity, narrative flow, and insight-driven design | Export final visuals for report |
| April 21, 2026 | Wrote final report and integrated figures into ACM format | `/report/` | Used structured sections (data, methods, results, advanced analysis) | Final proofreading and formatting |

---

## Decision Notes

### Decision Entry 1

**Date:** April 18, 2026  
**Decision:** Use Year-over-Year (YoY) growth instead of Month-over-Month (MoM)  
**Reason:** MoM data introduced too much short-term noise and made trends harder to interpret  
**Alternatives Considered:** MoM growth, rolling averages  
**Impact on Project:** Improved clarity of trends and made comparisons across variables more meaningful  
**Follow-Up:** Verified YoY values aligned with known economic events  

---

### Decision Entry 2

**Date:** April 19, 2026  
**Decision:** Structure dashboard into multiple pages instead of a single view  
**Reason:** A single page became too cluttered and reduced interpretability  
**Alternatives Considered:** One-page dashboard with filters  
**Impact on Project:** Improved storytelling and allowed deeper analysis per topic  
**Follow-Up:** Ensure consistent layout and labeling across pages  

---

### Decision Entry 3

**Date:** April 20, 2026  
**Decision:** Use index normalization (2016 = 100) for income, spending, and CPI  
**Reason:** Raw values were not directly comparable due to scale differences  
**Alternatives Considered:** Standardization (z-scores), raw value comparison  
**Impact on Project:** Enabled meaningful comparison of growth trends across variables  
**Follow-Up:** Clearly explain indexing method in report  

---

### Decision Entry 4

**Date:** April 21, 2026  
**Decision:** Introduce lagged inflation variable for advanced analysis  
**Reason:** Monetary policy does not respond instantly to inflation changes  
**Alternatives Considered:** No lag, longer lag periods (6–12 months)  
**Impact on Project:** Enabled deeper insight into delayed policy response  
**Follow-Up:** Validate lag assumption and interpret results carefully  

---

### Decision Entry 5

**Date:** April 21, 2026  
**Decision:** Use Deneb custom visual instead of standard Power BI visuals  
**Reason:** Needed an advanced visualization not covered in class and better suited for regression analysis  
**Alternatives Considered:** Scatter plot without regression, standard visuals  
**Impact on Project:** Added advanced analytical capability and improved credibility of findings  
**Follow-Up:** Ensure visual is clearly explained in report  

---

### Decision Entry 6

**Date:** April 21, 2026  
**Decision:** Include economic context variables (unemployment, sentiment)  
**Reason:** Inflation and spending alone did not fully explain economic behavior  
**Alternatives Considered:** Limiting analysis to core variables only  
**Impact on Project:** Provided broader context and strengthened interpretation  
**Follow-Up:** Align time series and handle missing data  

---

## Final Reflection

The project was developed through a structured, iterative workflow that included data collection, cleaning, integration, analysis, and visualization. Key decisions focused on improving interpretability, reducing noise, and uncovering relationships between variables. The addition of lag analysis and a custom Deneb visualization allowed the project to move beyond descriptive reporting into deeper analytical insight.
