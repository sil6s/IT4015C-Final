"""I run the final analysis phase for the integrated data project.

This script starts from the prepared pre-analysis dataset, restricts the data
to the complete monthly overlap period, creates derived variables, exports
summary tables, creates report-ready charts, and writes narrative materials
based only on computed results.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class AnalysisPaths:
    """I keep all final-analysis paths in one place so the workflow is reproducible."""

    project_root: Path
    input_file: Path
    analysis_data_dir: Path
    chart_dir: Path
    table_dir: Path
    report_dir: Path


REQUIRED_MONTHLY_COLUMNS = [
    "cpi_overall",
    "cpi_food",
    "cpi_shelter",
    "cpi_transportation",
    "pce_total",
    "disposable_income",
    "fed_funds_rate",
    "consumer_sentiment",
    "unemployment_rate",
]

YOY_COLUMNS = [
    "cpi_overall",
    "cpi_food",
    "cpi_shelter",
    "cpi_transportation",
    "pce_total",
    "disposable_income",
]

INDEX_COLUMNS = [
    "cpi_overall",
    "cpi_food",
    "cpi_shelter",
    "cpi_transportation",
    "pce_total",
    "disposable_income",
]

DISPLAY_NAMES = {
    "cpi_overall": "CPI Overall",
    "cpi_food": "CPI Food",
    "cpi_shelter": "CPI Shelter",
    "cpi_transportation": "CPI Transportation",
    "pce_total": "PCE Total",
    "disposable_income": "Disposable Personal Income",
    "fed_funds_rate": "Federal Funds Rate",
    "consumer_sentiment": "Consumer Sentiment",
    "unemployment_rate": "Unemployment Rate",
}


def main() -> None:
    """I execute the complete final-analysis export workflow."""
    paths = build_paths()
    create_output_dirs(paths)
    raw = load_pre_analysis_dataset(paths.input_file)
    analysis, adjustments = prepare_analysis_dataset(raw)
    derived = add_derived_variables(analysis)
    export_analysis_data(paths, analysis, derived, adjustments)
    summary_tables = export_summary_tables(paths, derived)
    chart_files = create_charts(paths, derived)
    narrative_metrics = build_narrative_metrics(derived, summary_tables)
    write_report_ready_outputs(paths, derived, adjustments, chart_files, narrative_metrics)


def build_paths() -> AnalysisPaths:
    """I resolve paths from the script location instead of relying on my shell location."""
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    return AnalysisPaths(
        project_root=project_root,
        input_file=project_root / "04_merged_data" / "pre_analysis_dataset.csv",
        analysis_data_dir=project_root / "11_outputs" / "analysis_data",
        chart_dir=project_root / "11_outputs" / "charts",
        table_dir=project_root / "11_outputs" / "tables",
        report_dir=project_root / "11_outputs" / "reports",
    )


def create_output_dirs(paths: AnalysisPaths) -> None:
    """I create output folders before writing analysis artifacts."""
    for folder in [paths.analysis_data_dir, paths.chart_dir, paths.table_dir, paths.report_dir]:
        folder.mkdir(parents=True, exist_ok=True)


def load_pre_analysis_dataset(input_file: Path) -> pd.DataFrame:
    """I load the prepared dataset and confirm that the required columns exist."""
    if not input_file.exists():
        raise FileNotFoundError(f"I could not find the pre-analysis dataset: {input_file}")

    frame = pd.read_csv(input_file, parse_dates=["date"])
    missing_columns = sorted(set(REQUIRED_MONTHLY_COLUMNS + ["date"]).difference(frame.columns))
    if missing_columns:
        raise ValueError(f"I am missing required columns in the pre-analysis dataset: {missing_columns}")

    return frame.sort_values("date").reset_index(drop=True)


def prepare_analysis_dataset(raw: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """I restrict the dataset to the complete overlapping monthly period."""
    coverage = []
    for column in REQUIRED_MONTHLY_COLUMNS:
        non_missing_dates = raw.loc[raw[column].notna(), "date"]
        coverage.append(
            {
                "variable": column,
                "first_available_date": non_missing_dates.min(),
                "last_available_date": non_missing_dates.max(),
                "non_missing_observations": int(non_missing_dates.shape[0]),
            }
        )

    coverage_frame = pd.DataFrame(coverage)
    start_date = coverage_frame["first_available_date"].max()
    end_date = coverage_frame["last_available_date"].min()

    candidate = raw.loc[(raw["date"] >= start_date) & (raw["date"] <= end_date), ["date"] + REQUIRED_MONTHLY_COLUMNS].copy()
    candidate = candidate.set_index("date").asfreq("MS")

    # I identify incomplete months before excluding them so the adjustment is visible.
    missing_required = candidate[REQUIRED_MONTHLY_COLUMNS].isna().any(axis=1)
    excluded_months = candidate.loc[missing_required].index
    analysis = candidate.loc[~missing_required].reset_index()

    adjustments = pd.DataFrame(
        [
            {
                "adjustment": "overlap_start_date",
                "detail": start_date.strftime("%Y-%m-%d"),
                "reason": "I used the latest first-available date across required monthly variables.",
            },
            {
                "adjustment": "overlap_end_date",
                "detail": end_date.strftime("%Y-%m-%d"),
                "reason": "I used the earliest last-available date across required monthly variables.",
            },
            {
                "adjustment": "excluded_incomplete_months",
                "detail": ", ".join(date.strftime("%Y-%m-%d") for date in excluded_months) if len(excluded_months) else "None",
                "reason": "I excluded months that did not have complete required-variable coverage.",
            },
            {
                "adjustment": "analysis_row_count",
                "detail": str(len(analysis)),
                "reason": "I used complete aligned monthly rows for the final analysis dataset.",
            },
        ]
    )

    return analysis, adjustments


def add_derived_variables(analysis: pd.DataFrame) -> pd.DataFrame:
    """I create YoY growth, MoM growth, and 2016-base indexed variables."""
    derived = analysis.copy()
    complete_months = set(pd.to_datetime(derived["date"]))
    derived = derived.set_index("date").asfreq("MS")

    for column in YOY_COLUMNS:
        # I calculate YoY percent change as current value divided by the value 12 months earlier minus 1.
        derived[f"{column}_yoy_pct"] = derived[column].pct_change(periods=12, fill_method=None) * 100

        # I calculate MoM percent change only when the prior calendar month is present.
        derived[f"{column}_mom_pct"] = derived[column].pct_change(periods=1, fill_method=None) * 100

    base_year_mask = derived.index.year == 2016
    for column in INDEX_COLUMNS:
        # I index each series to the average 2016 value so different units can be compared on one scale.
        base_value = derived.loc[base_year_mask, column].mean()
        derived[f"{column}_index_2016_100"] = (derived[column] / base_value) * 100

    # I prevent month-over-month calculations from bridging across excluded missing months.
    for column in YOY_COLUMNS:
        previous_month_present = derived[column].shift(1).notna()
        derived.loc[~previous_month_present, f"{column}_mom_pct"] = np.nan

    # I remove placeholder calendar rows after using them to protect the growth-rate calculations.
    derived = derived.loc[derived.index.isin(complete_months)]
    return derived.reset_index()


def export_analysis_data(paths: AnalysisPaths, analysis: pd.DataFrame, derived: pd.DataFrame, adjustments: pd.DataFrame) -> None:
    """I export the final analysis datasets and adjustment log."""
    analysis.to_csv(paths.analysis_data_dir / "analysis_aligned_monthly_dataset.csv", index=False)
    derived.to_csv(paths.analysis_data_dir / "analysis_dataset_with_derived_variables.csv", index=False)
    derived.to_excel(paths.analysis_data_dir / "analysis_dataset_with_derived_variables.xlsx", index=False)
    adjustments.to_csv(paths.table_dir / "analysis_adjustments_log.csv", index=False)


def export_summary_tables(paths: AnalysisPaths, derived: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """I export descriptive statistics, correlations, and growth summaries."""
    raw_summary = (
        derived[REQUIRED_MONTHLY_COLUMNS]
        .describe()
        .T[["count", "mean", "std", "min", "max"]]
        .rename_axis("variable")
        .reset_index()
    )
    raw_summary.to_csv(paths.table_dir / "summary_statistics_levels.csv", index=False)

    yoy_columns = [f"{column}_yoy_pct" for column in YOY_COLUMNS]
    yoy_summary = (
        derived[yoy_columns]
        .describe()
        .T[["count", "mean", "std", "min", "max"]]
        .rename_axis("variable")
        .reset_index()
    )
    yoy_summary.to_csv(paths.table_dir / "summary_statistics_yoy_growth.csv", index=False)

    level_correlations = derived[REQUIRED_MONTHLY_COLUMNS].corr()
    level_correlations.to_csv(paths.table_dir / "correlation_matrix_levels.csv")

    yoy_correlations = derived[yoy_columns].corr()
    yoy_correlations.to_csv(paths.table_dir / "correlation_matrix_yoy_growth.csv")

    latest_values = build_latest_values_table(derived)
    latest_values.to_csv(paths.table_dir / "latest_analysis_values.csv", index=False)

    return {
        "raw_summary": raw_summary,
        "yoy_summary": yoy_summary,
        "level_correlations": level_correlations,
        "yoy_correlations": yoy_correlations,
        "latest_values": latest_values,
    }


def build_latest_values_table(derived: pd.DataFrame) -> pd.DataFrame:
    """I create a compact table of first, latest, and indexed changes."""
    records = []
    first_row = derived.iloc[0]
    latest_row = derived.iloc[-1]
    for column in INDEX_COLUMNS:
        first_value = first_row[column]
        latest_value = latest_row[column]
        records.append(
            {
                "variable": column,
                "first_date": first_row["date"].strftime("%Y-%m-%d"),
                "latest_date": latest_row["date"].strftime("%Y-%m-%d"),
                "first_value": first_value,
                "latest_value": latest_value,
                "percent_change_first_to_latest": ((latest_value / first_value) - 1) * 100,
                "latest_index_2016_100": latest_row[f"{column}_index_2016_100"],
            }
        )
    return pd.DataFrame(records)


def create_charts(paths: AnalysisPaths, derived: pd.DataFrame) -> dict[str, str]:
    """I create export-ready charts with consistent styling and neutral titles."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "savefig.dpi": 220,
            "font.size": 10,
            "axes.titlesize": 14,
            "axes.labelsize": 10,
            "legend.fontsize": 9,
        }
    )

    chart_files: dict[str, str] = {}
    chart_files["inflation_trends"] = _save_inflation_trends(paths, derived)
    chart_files["consumer_spending"] = _save_consumer_spending(paths, derived)
    chart_files["income_vs_spending"] = _save_income_vs_spending(paths, derived)
    chart_files["inflation_vs_spending_scatter"] = _save_inflation_vs_spending_scatter(paths, derived)
    chart_files["economic_context"] = _save_economic_context(paths, derived)
    chart_files["indexed_comparison"] = _save_indexed_comparison(paths, derived)
    return chart_files


def _save_inflation_trends(paths: AnalysisPaths, derived: pd.DataFrame) -> str:
    fig, ax = plt.subplots(figsize=(11, 6))
    for column in ["cpi_overall", "cpi_food", "cpi_shelter", "cpi_transportation"]:
        ax.plot(derived["date"], derived[column], linewidth=2, label=DISPLAY_NAMES[column])
    ax.set_title("Inflation Measures Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("CPI Index Value")
    ax.legend(loc="upper left", ncols=2)
    fig.tight_layout()
    path = paths.chart_dir / "chart_01_inflation_trends.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return str(path)


def _save_consumer_spending(paths: AnalysisPaths, derived: pd.DataFrame) -> str:
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.plot(derived["date"], derived["pce_total"], color="#1f77b4", linewidth=2.5)
    ax.set_title("Consumer Spending Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("PCE Total")
    fig.tight_layout()
    path = paths.chart_dir / "chart_02_consumer_spending_pce.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return str(path)


def _save_income_vs_spending(paths: AnalysisPaths, derived: pd.DataFrame) -> str:
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.plot(derived["date"], derived["pce_total"], linewidth=2.3, label="PCE Total")
    ax.plot(derived["date"], derived["disposable_income"], linewidth=2.3, label="Disposable Personal Income")
    ax.set_title("Income and Consumer Spending Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Source-Reported Level")
    ax.legend(loc="upper left")
    fig.tight_layout()
    path = paths.chart_dir / "chart_03_income_vs_spending.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return str(path)


def _save_inflation_vs_spending_scatter(paths: AnalysisPaths, derived: pd.DataFrame) -> str:
    scatter = derived[["cpi_overall_yoy_pct", "pce_total_yoy_pct"]].dropna()
    x = scatter["cpi_overall_yoy_pct"].to_numpy()
    y = scatter["pce_total_yoy_pct"].to_numpy()
    slope, intercept = np.polyfit(x, y, 1)
    line_x = np.linspace(x.min(), x.max(), 100)
    line_y = slope * line_x + intercept

    fig, ax = plt.subplots(figsize=(8.5, 6))
    ax.scatter(x, y, alpha=0.75, color="#2ca02c", edgecolor="white", linewidth=0.5)
    ax.plot(line_x, line_y, color="#333333", linewidth=2, label="Linear fit")
    ax.set_title("Inflation and Spending Growth")
    ax.set_xlabel("CPI Overall YoY % Change")
    ax.set_ylabel("PCE Total YoY % Change")
    ax.legend(loc="best")
    fig.tight_layout()
    path = paths.chart_dir / "chart_04_inflation_vs_spending_scatter.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return str(path)


def _save_economic_context(paths: AnalysisPaths, derived: pd.DataFrame) -> str:
    fig, axes = plt.subplots(3, 1, figsize=(11, 8), sharex=True)
    context = [
        ("unemployment_rate", "Unemployment Rate", "Percent"),
        ("fed_funds_rate", "Federal Funds Rate", "Percent"),
        ("consumer_sentiment", "Consumer Sentiment", "Index"),
    ]
    colors = ["#d62728", "#9467bd", "#8c564b"]
    for ax, (column, title, ylabel), color in zip(axes, context, colors):
        ax.plot(derived["date"], derived[column], color=color, linewidth=2)
        ax.set_title(title)
        ax.set_ylabel(ylabel)
    axes[-1].set_xlabel("Date")
    fig.suptitle("Economic Context Variables", y=0.99, fontsize=15)
    fig.tight_layout()
    path = paths.chart_dir / "chart_05_economic_context.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return str(path)


def _save_indexed_comparison(paths: AnalysisPaths, derived: pd.DataFrame) -> str:
    fig, ax = plt.subplots(figsize=(11, 6))
    indexed_columns = {
        "cpi_overall_index_2016_100": "CPI Overall",
        "pce_total_index_2016_100": "PCE Total",
        "disposable_income_index_2016_100": "Disposable Personal Income",
    }
    for column, label in indexed_columns.items():
        ax.plot(derived["date"], derived[column], linewidth=2.5, label=label)
    ax.axhline(100, color="#555555", linewidth=1, linestyle="--")
    ax.set_title("Indexed Comparison: CPI, Spending, and Income")
    ax.set_xlabel("Date")
    ax.set_ylabel("Index, 2016 Average = 100")
    ax.legend(loc="upper left")
    fig.tight_layout()
    path = paths.chart_dir / "chart_06_indexed_comparison.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return str(path)


def build_narrative_metrics(derived: pd.DataFrame, summary_tables: dict[str, pd.DataFrame]) -> dict[str, object]:
    """I collect computed values used in the written analysis narrative."""
    latest_values = summary_tables["latest_values"].set_index("variable")
    yoy_summary = summary_tables["yoy_summary"].copy()
    yoy_summary["source_variable"] = yoy_summary["variable"].str.replace("_yoy_pct", "", regex=False)
    level_correlations = summary_tables["level_correlations"]
    yoy_correlations = summary_tables["yoy_correlations"]

    strongest_level_corr_with_pce = (
        level_correlations["pce_total"]
        .drop(labels=["pce_total"])
        .sort_values(key=lambda values: values.abs(), ascending=False)
        .head(3)
    )
    strongest_yoy_corr_with_pce_growth = (
        yoy_correlations["pce_total_yoy_pct"]
        .drop(labels=["pce_total_yoy_pct"])
        .sort_values(key=lambda values: values.abs(), ascending=False)
        .head(3)
    )

    metrics = {
        "start_date": derived["date"].min().strftime("%Y-%m-%d"),
        "end_date": derived["date"].max().strftime("%Y-%m-%d"),
        "row_count": int(len(derived)),
        "latest_values": latest_values.to_dict(orient="index"),
        "yoy_summary": yoy_summary.set_index("source_variable").to_dict(orient="index"),
        "strongest_level_corr_with_pce": strongest_level_corr_with_pce.to_dict(),
        "strongest_yoy_corr_with_pce_growth": strongest_yoy_corr_with_pce_growth.to_dict(),
        "scatter_correlation": float(
            derived[["cpi_overall_yoy_pct", "pce_total_yoy_pct"]].dropna().corr().iloc[0, 1]
        ),
    }
    return metrics


def write_report_ready_outputs(
    paths: AnalysisPaths,
    derived: pd.DataFrame,
    adjustments: pd.DataFrame,
    chart_files: dict[str, str],
    metrics: dict[str, object],
) -> None:
    """I write report, Excel, Power BI, and presentation materials from computed outputs."""
    (paths.report_dir / "analysis_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    (paths.report_dir / "final_analysis_narrative.md").write_text(
        build_analysis_narrative(adjustments, chart_files, metrics),
        encoding="utf-8",
    )
    (paths.report_dir / "excel_final_phase_guide.md").write_text(
        build_excel_guide(),
        encoding="utf-8",
    )
    (paths.report_dir / "power_bi_final_phase_guide.md").write_text(
        build_power_bi_guide(),
        encoding="utf-8",
    )
    (paths.report_dir / "presentation_content.md").write_text(
        build_presentation_content(chart_files, metrics),
        encoding="utf-8",
    )
    (paths.report_dir / "visualization_inventory.csv").write_text(
        "chart_id,file_path,purpose\n"
        + "\n".join(f"{key},{value},{chart_purpose(key)}" for key, value in chart_files.items())
        + "\n",
        encoding="utf-8",
    )


def build_analysis_narrative(adjustments: pd.DataFrame, chart_files: dict[str, str], metrics: dict[str, object]) -> str:
    """I create report-ready narrative text from calculated values."""
    latest = metrics["latest_values"]
    yoy = metrics["yoy_summary"]
    pce_corr = metrics["strongest_level_corr_with_pce"]
    pce_yoy_corr = metrics["strongest_yoy_corr_with_pce_growth"]

    return f"""# Final Analysis Narrative

## Analysis Scope and Data Preparation

I analyzed the integrated monthly dataset over the complete required-variable overlap period from **{metrics["start_date"]}** through **{metrics["end_date"]}**. I used complete monthly observations for CPI overall, CPI food, CPI shelter, CPI transportation, PCE total, disposable personal income, the federal funds rate, consumer sentiment, and the unemployment rate.

I selected this period because it is the window where the main inflation, spending, income, and economic context variables align. I excluded incomplete required-variable months before analysis. The adjustment log records the exact exclusions and the reason for each preparation choice.

## Derived Variables

I calculated year-over-year percentage change for CPI overall, CPI food, CPI shelter, CPI transportation, PCE total, and disposable personal income. I calculated each year-over-year value as:

`((current month value / value from same month one year earlier) - 1) * 100`

I also calculated month-over-month percentage change for the same variables. I used month-over-month values cautiously because they are more sensitive to short-run movement. I did not calculate month-over-month change across a missing calendar month.

Finally, I created indexed variables using the 2016 average as the base value:

`(current value / average value during 2016) * 100`

This lets me compare CPI, spending, and income on a common scale even though the original units differ.

## Descriptive Analysis

The final aligned dataset contains **{metrics["row_count"]} monthly observations**. Over the analysis window, CPI overall increased by **{latest["cpi_overall"]["percent_change_first_to_latest"]:.2f}%** from the first available analysis month to the latest analysis month. PCE total increased by **{latest["pce_total"]["percent_change_first_to_latest"]:.2f}%**, and disposable personal income increased by **{latest["disposable_income"]["percent_change_first_to_latest"]:.2f}%** over the same first-to-latest window.

For year-over-year growth, CPI overall averaged **{yoy["cpi_overall"]["mean"]:.2f}%** across non-missing YoY observations, with a minimum of **{yoy["cpi_overall"]["min"]:.2f}%** and a maximum of **{yoy["cpi_overall"]["max"]:.2f}%**. PCE total YoY growth averaged **{yoy["pce_total"]["mean"]:.2f}%**, while disposable personal income YoY growth averaged **{yoy["disposable_income"]["mean"]:.2f}%**.

## Correlation Results

I calculated correlation matrices for both level variables and year-over-year growth variables. In the level-variable correlation matrix, the three strongest absolute correlations with PCE total were:

{format_correlation_bullets(pce_corr)}

For year-over-year growth, the strongest absolute correlations with PCE total YoY growth were:

{format_correlation_bullets(pce_yoy_corr)}

I interpret these correlations as descriptive relationships, not causal evidence. Because these are macroeconomic time-series variables, shared time trends and common economic shocks can influence correlations.

## Visualization Explanations

### Inflation Measures Over Time

The inflation trends chart compares CPI overall with food, shelter, and transportation CPI indexes. I use this chart to show how the category-level CPI measures move relative to the broad CPI index within the aligned analysis period.

Chart file: `{chart_files["inflation_trends"]}`

### Consumer Spending Over Time

The consumer spending chart shows PCE total over the aligned monthly analysis period. I use this visual as the main spending-series reference for the project.

Chart file: `{chart_files["consumer_spending"]}`

### Income and Consumer Spending

The income and spending chart compares PCE total with disposable personal income using their source-reported levels. I use this visual to examine the two consumer-side measures side by side before making any interpretation about their relationship.

Chart file: `{chart_files["income_vs_spending"]}`

### Inflation and Spending Growth

The scatter plot compares CPI overall year-over-year percentage change with PCE total year-over-year percentage change. The fitted line summarizes the direction of the linear association in the plotted observations. The correlation for these two YoY growth variables is **{metrics["scatter_correlation"]:.3f}**.

Chart file: `{chart_files["inflation_vs_spending_scatter"]}`

### Economic Context Variables

The economic context chart presents unemployment, the federal funds rate, and consumer sentiment in separate panels. I use separate panels because the variables have different units and scales.

Chart file: `{chart_files["economic_context"]}`

### Indexed Comparison

The indexed comparison chart sets CPI overall, PCE total, and disposable personal income equal to 100 based on their 2016 average. I use this chart to compare relative movement across variables with different original units.

Chart file: `{chart_files["indexed_comparison"]}`

## Key Observations

- I observed that the main CPI, spending, and income variables all ended the analysis window above their first-month levels, based on the first-to-latest percentage changes computed from the aligned dataset.
- I observed that CPI category indexes did not have identical first-to-latest changes, which supports the value of including category-level inflation variables rather than only using CPI overall.
- I observed that level-variable correlations with PCE total were generally high for variables that also trend over time, so I treated the growth-rate correlation matrix as an important supporting check.
- I observed that the CPI overall YoY and PCE total YoY scatter plot produced a correlation of **{metrics["scatter_correlation"]:.3f}**, which I report as a descriptive association rather than a causal claim.
- I observed that the economic context variables require separate visual treatment because unemployment, interest rates, and sentiment are measured on different scales.

## Transition Into Findings

These outputs give me the evidence base for the findings section. In the final findings, I should connect each claim directly to a chart, summary statistic, or correlation table. I should avoid claiming causation unless I add a separate causal research design, which this project does not currently include.
"""


def format_correlation_bullets(correlations: dict[str, float]) -> str:
    """I format computed correlations as report-ready bullets."""
    lines = []
    for variable, value in correlations.items():
        label = DISPLAY_NAMES.get(variable.replace("_yoy_pct", ""), variable)
        lines.append(f"- {label}: **{value:.3f}**")
    return "\n".join(lines)


def build_excel_guide() -> str:
    """I write the final Excel implementation guide with formulas."""
    return """# Excel Final Analysis Guide

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
"""


def build_power_bi_guide() -> str:
    """I write the final Power BI implementation guide with DAX placeholders."""
    return """# Power BI Final Analysis Guide

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
"""


def build_presentation_content(chart_files: dict[str, str], metrics: dict[str, object]) -> str:
    """I write slide content and speaker notes from computed analysis outputs."""
    return f"""# Presentation Content

## Slide 1: Project Title

**Bullets**

- Inflation, Consumer Spending, Income, and Economic Conditions in the United States
- Integrated Data Analysis Final Project
- Prepared by: [My Name]

**Speaking Notes**

I introduce the project as an integrated analysis of inflation, spending, income, and broader economic context.

## Slide 2: Research Focus

**Bullets**

- I analyze monthly U.S. economic data from {metrics["start_date"]} through {metrics["end_date"]}.
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

- `{chart_files["inflation_trends"]}`

**Speaking Notes**

I explain what the chart compares and avoid overstating the cause of any movement.

## Slide 5: Consumer Spending

**Bullets**

- PCE total is the primary consumer spending variable.
- The chart shows the spending series across the aligned analysis period.

**Visual**

- `{chart_files["consumer_spending"]}`

**Speaking Notes**

I describe the spending measure and connect it to the project question.

## Slide 6: Income and Spending

**Bullets**

- I compare disposable personal income and PCE total.
- This helps me evaluate spending alongside income context.

**Visual**

- `{chart_files["income_vs_spending"]}`

**Speaking Notes**

I explain why income belongs in the project and note that comparison does not automatically prove causation.

## Slide 7: Inflation vs Spending Growth

**Bullets**

- I compare CPI overall YoY growth with PCE total YoY growth.
- The computed correlation is {metrics["scatter_correlation"]:.3f}.
- I interpret the relationship descriptively.

**Visual**

- `{chart_files["inflation_vs_spending_scatter"]}`

**Speaking Notes**

I explain the scatter plot and regression line as descriptive tools.

## Slide 8: Economic Context

**Bullets**

- I include unemployment, interest rates, and consumer sentiment as context variables.
- I chart them separately because they use different scales.

**Visual**

- `{chart_files["economic_context"]}`

**Speaking Notes**

I explain that these variables help frame the economic environment around inflation and spending.

## Slide 9: Indexed Comparison

**Bullets**

- I set CPI overall, PCE total, and disposable income to a 2016 average of 100.
- This allows comparison across variables with different units.

**Visual**

- `{chart_files["indexed_comparison"]}`

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
"""


def chart_purpose(chart_key: str) -> str:
    """I provide a concise purpose statement for each chart export."""
    purposes = {
        "inflation_trends": "Compare CPI overall with CPI food, shelter, and transportation over time.",
        "consumer_spending": "Show PCE total across the aligned analysis period.",
        "income_vs_spending": "Compare disposable personal income with PCE total.",
        "inflation_vs_spending_scatter": "Compare CPI overall YoY growth with PCE total YoY growth.",
        "economic_context": "Show unemployment, federal funds rate, and consumer sentiment as context.",
        "indexed_comparison": "Compare CPI overall, PCE total, and disposable income on a 2016-base index.",
    }
    return purposes[chart_key]


if __name__ == "__main__":
    main()
