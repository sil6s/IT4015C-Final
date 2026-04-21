"""I run pre-analysis validation checks and write transparent QA summaries."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import pandas as pd

LOGGER = logging.getLogger(__name__)


def validate_cleaned_dataset(frame: pd.DataFrame, dataset: dict[str, Any]) -> dict[str, Any]:
    """I validate one cleaned dataset and return a compact audit record."""
    value_column = dataset["value_column"]
    required_columns = {"date", value_column, "dataset_id", "source_file", "source_series"}
    missing_columns = sorted(required_columns.difference(frame.columns))
    duplicate_dates = int(frame["date"].duplicated().sum()) if "date" in frame.columns else None
    missing_values = int(frame[value_column].isna().sum()) if value_column in frame.columns else None
    row_count = int(len(frame))
    column_count = int(len(frame.columns))

    date_min = frame["date"].min() if row_count and "date" in frame.columns else pd.NaT
    date_max = frame["date"].max() if row_count and "date" in frame.columns else pd.NaT
    expected_periods = _expected_month_count(date_min, date_max)
    actual_unique_dates = int(frame["date"].nunique()) if "date" in frame.columns else 0
    potential_missing_periods = max(expected_periods - actual_unique_dates, 0) if expected_periods is not None else None

    passed = not missing_columns and duplicate_dates == 0 and row_count > 0
    status = "PASS" if passed else "REVIEW"

    return {
        "dataset_id": dataset["dataset_id"],
        "display_name": dataset["display_name"],
        "status": status,
        "row_count": row_count,
        "column_count": column_count,
        "date_min": _format_date(date_min),
        "date_max": _format_date(date_max),
        "duplicate_dates": duplicate_dates,
        "missing_value_count": missing_values,
        "potential_missing_months_within_range": potential_missing_periods,
        "missing_required_columns": "; ".join(missing_columns),
        "expected_frequency": dataset["expected_frequency"],
        "notes": "I treat REVIEW as a prompt for inspection, not as an analytical result.",
    }


def validate_merged_dataset(merged: pd.DataFrame, datasets: list[dict[str, Any]]) -> pd.DataFrame:
    """I validate the merged dataset without interpreting relationships among variables."""
    records: list[dict[str, Any]] = []
    records.append(
        {
            "check_name": "merged_dataset_has_rows",
            "status": "PASS" if len(merged) > 0 else "FAIL",
            "detail": f"I found {len(merged)} rows in the merged dataset.",
        }
    )
    records.append(
        {
            "check_name": "merged_dataset_has_date",
            "status": "PASS" if "date" in merged.columns else "FAIL",
            "detail": "I confirmed whether the merged dataset contains the date key.",
        }
    )
    records.append(
        {
            "check_name": "merged_dataset_duplicate_dates",
            "status": "PASS" if "date" in merged.columns and merged["date"].duplicated().sum() == 0 else "REVIEW",
            "detail": f"I found {int(merged['date'].duplicated().sum()) if 'date' in merged.columns else 'unknown'} duplicate merged dates.",
        }
    )

    for dataset in datasets:
        column = dataset["value_column"]
        if column not in merged.columns:
            status = "FAIL"
            detail = f"I did not find expected merged column {column}."
        else:
            missing = int(merged[column].isna().sum())
            status = "PASS" if missing == 0 else "REVIEW"
            detail = f"I found {missing} missing values in {column} after the outer merge."
        records.append({"check_name": f"merged_column_{column}", "status": status, "detail": detail})

    return pd.DataFrame(records)


def build_missing_value_summary(merged: pd.DataFrame) -> pd.DataFrame:
    """I summarize missing values so I can inspect coverage before analysis."""
    records = []
    for column in merged.columns:
        missing = int(merged[column].isna().sum())
        records.append(
            {
                "column_name": column,
                "missing_count": missing,
                "non_missing_count": int(merged[column].notna().sum()),
                "missing_percent": round((missing / len(merged) * 100), 2) if len(merged) else 0,
            }
        )
    return pd.DataFrame(records)


def write_validation_outputs(
    qa_dir: Path,
    cleaned_records: list[dict[str, Any]],
    merged_validation: pd.DataFrame,
    missing_summary: pd.DataFrame,
) -> None:
    """I export validation records so the preparation work can be reviewed later."""
    qa_dir.mkdir(parents=True, exist_ok=True)
    cleaned_summary = pd.DataFrame(cleaned_records)
    cleaned_summary.to_csv(qa_dir / "cleaned_dataset_validation_summary.csv", index=False)
    merged_validation.to_csv(qa_dir / "merged_dataset_validation_summary.csv", index=False)
    missing_summary.to_csv(qa_dir / "merged_missing_value_summary.csv", index=False)

    overall = pd.concat(
        [
            cleaned_summary.assign(validation_area="cleaned_dataset"),
            merged_validation.rename(columns={"check_name": "dataset_id", "detail": "notes"}).assign(
                validation_area="merged_dataset",
                display_name="",
                row_count="",
                column_count="",
                date_min="",
                date_max="",
                duplicate_dates="",
                missing_value_count="",
                potential_missing_months_within_range="",
                missing_required_columns="",
                expected_frequency="",
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    overall.to_csv(qa_dir / "validation_summary.csv", index=False)
    LOGGER.info("I wrote validation outputs to %s", qa_dir)


def _expected_month_count(date_min: pd.Timestamp, date_max: pd.Timestamp) -> int | None:
    """I calculate monthly coverage length as a QA check only."""
    if pd.isna(date_min) or pd.isna(date_max):
        return None
    return len(pd.period_range(date_min, date_max, freq="M"))


def _format_date(value: pd.Timestamp) -> str:
    """I format dates consistently in validation exports."""
    if pd.isna(value):
        return ""
    return pd.Timestamp(value).strftime("%Y-%m-%d")
