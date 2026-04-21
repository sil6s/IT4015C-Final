"""I run the full pre-analysis data preparation workflow.

This script loads my raw files, standardizes dates and column names, validates
the cleaned structures, merges the datasets by date, and exports preparation
artifacts. I intentionally do not perform analysis, interpret patterns, or
write findings in this pipeline.
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from src.cleaning import clean_dataset
from src.config import ensure_output_dirs, load_config
from src.data_loading import load_dataset
from src.integration import create_pre_analysis_dataset, merge_cleaned_datasets
from src.logging_utils import configure_logging
from src.validation import (
    build_missing_value_summary,
    validate_cleaned_dataset,
    validate_merged_dataset,
    write_validation_outputs,
)

LOGGER = logging.getLogger(__name__)


def main() -> None:
    """I execute the preparation pipeline from raw files through QA exports."""
    script_dir = Path(__file__).resolve().parent
    config = load_config(script_dir / "config" / "project_config.json")
    ensure_output_dirs(config)
    configure_logging(config.log_dir)

    LOGGER.info("I loaded project config for %s.", config.project_name)
    LOGGER.info("I am reading raw data from %s.", config.raw_data_dir)

    cleaned_frames: dict[str, pd.DataFrame] = {}
    validation_records: list[dict[str, object]] = []

    for dataset in config.datasets:
        raw = load_dataset(config.raw_data_dir, dataset)
        cleaned = clean_dataset(raw, dataset)

        cleaned_path = config.cleaned_data_dir / f"cleaned_{dataset['dataset_id']}.csv"
        cleaned.to_csv(cleaned_path, index=False)
        LOGGER.info("I exported %s cleaned rows to %s.", len(cleaned), cleaned_path)

        cleaned_frames[dataset["dataset_id"]] = cleaned
        validation_records.append(validate_cleaned_dataset(cleaned, dataset))

    merged = merge_cleaned_datasets(cleaned_frames, config.datasets)
    master_path = config.merged_data_dir / "master_monthly_dataset.csv"
    merged.to_csv(master_path, index=False)
    LOGGER.info("I exported the merged master dataset to %s.", master_path)

    pre_analysis = create_pre_analysis_dataset(merged)
    pre_analysis_csv = config.merged_data_dir / "pre_analysis_dataset.csv"
    pre_analysis_xlsx = config.merged_data_dir / "pre_analysis_dataset.xlsx"
    pre_analysis.to_csv(pre_analysis_csv, index=False)
    pre_analysis.to_excel(pre_analysis_xlsx, index=False)
    LOGGER.info("I exported the pre-analysis dataset to %s and %s.", pre_analysis_csv, pre_analysis_xlsx)

    merged_validation = validate_merged_dataset(merged, config.datasets)
    missing_summary = build_missing_value_summary(merged)
    write_validation_outputs(config.qa_dir, validation_records, merged_validation, missing_summary)

    inventory = pd.DataFrame(
        [
            {"artifact": str(master_path), "artifact_type": "merged_dataset", "status": "created"},
            {"artifact": str(pre_analysis_csv), "artifact_type": "pre_analysis_dataset_csv", "status": "created"},
            {"artifact": str(pre_analysis_xlsx), "artifact_type": "pre_analysis_dataset_xlsx", "status": "created"},
            {"artifact": str(config.qa_dir / "validation_summary.csv"), "artifact_type": "validation_summary", "status": "created"},
        ]
    )
    inventory.to_csv(config.qa_dir / "pipeline_artifact_manifest.csv", index=False)
    LOGGER.info("I wrote the pipeline artifact manifest.")
    LOGGER.info("I completed the pre-analysis data preparation pipeline.")


if __name__ == "__main__":
    main()
