"""I standardize dates, column names, data types, and obvious formatting issues."""

from __future__ import annotations

import logging
from typing import Any

import pandas as pd

LOGGER = logging.getLogger(__name__)


def clean_dataset(frame: pd.DataFrame, dataset: dict[str, Any]) -> pd.DataFrame:
    """I clean one dataset without creating analytical findings or derived conclusions."""
    value_column = dataset["value_column"]
    cleaned = frame.copy()

    cleaned.columns = [_standardize_column_name(column) for column in cleaned.columns]
    if value_column not in cleaned.columns:
        raise ValueError(f"I expected {value_column} after column standardization.")

    cleaned["date"] = pd.to_datetime(cleaned["date"], errors="coerce")
    cleaned[value_column] = pd.to_numeric(cleaned[value_column], errors="coerce")
    cleaned["dataset_id"] = dataset["dataset_id"]
    cleaned["display_name"] = dataset["display_name"]
    cleaned["expected_frequency"] = dataset["expected_frequency"]
    cleaned["project_role"] = dataset["role"]

    before_drop = len(cleaned)
    cleaned = cleaned.dropna(subset=["date"]).copy()
    dropped = before_drop - len(cleaned)
    if dropped:
        LOGGER.warning("I dropped %s rows from %s because the date could not be parsed.", dropped, dataset["dataset_id"])

    cleaned["date"] = cleaned["date"].dt.to_period("M").dt.to_timestamp()
    cleaned = cleaned.sort_values("date").reset_index(drop=True)

    return cleaned[
        [
            "date",
            value_column,
            "dataset_id",
            "display_name",
            "source_file",
            "source_series",
            "expected_frequency",
            "project_role",
        ]
    ]


def _standardize_column_name(column: object) -> str:
    """I convert source headers into predictable snake_case names."""
    text = str(column).strip().lower()
    for old, new in [(" ", "_"), ("-", "_"), ("/", "_"), ("(", ""), (")", ""), (".", "")]:
        text = text.replace(old, new)
    while "__" in text:
        text = text.replace("__", "_")
    return text.strip("_")
