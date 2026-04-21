"""I merge cleaned datasets into a pre-analysis master dataset by date."""

from __future__ import annotations

import logging
from functools import reduce
from typing import Any

import pandas as pd

LOGGER = logging.getLogger(__name__)


def merge_cleaned_datasets(cleaned_frames: dict[str, pd.DataFrame], datasets: list[dict[str, Any]]) -> pd.DataFrame:
    """I outer-join all cleaned datasets so coverage differences remain visible."""
    merge_ready_frames = []
    for dataset in datasets:
        dataset_id = dataset["dataset_id"]
        value_column = dataset["value_column"]
        frame = cleaned_frames[dataset_id][["date", value_column]].copy()
        merge_ready_frames.append(frame)
        LOGGER.info("I prepared %s for merging with %s rows.", dataset_id, len(frame))

    merged = reduce(lambda left, right: pd.merge(left, right, on="date", how="outer"), merge_ready_frames)
    merged = merged.sort_values("date").reset_index(drop=True)
    LOGGER.info("I created the merged dataset with %s rows and %s columns.", len(merged), len(merged.columns))
    return merged


def create_pre_analysis_dataset(merged: pd.DataFrame) -> pd.DataFrame:
    """I create a clearly labeled analysis-ready dataset without deriving findings."""
    pre_analysis = merged.copy()
    pre_analysis["date"] = pd.to_datetime(pre_analysis["date"]).dt.strftime("%Y-%m-%d")
    return pre_analysis
