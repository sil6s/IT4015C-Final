"""I load and normalize project configuration for the preparation pipeline."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ProjectConfig:
    """I store resolved paths and dataset definitions in one predictable object."""

    project_name: str
    script_dir: Path
    project_root: Path
    raw_data_dir: Path
    cleaned_data_dir: Path
    merged_data_dir: Path
    qa_dir: Path
    log_dir: Path
    date_column: str
    datasets: list[dict[str, Any]]


def load_config(config_path: Path) -> ProjectConfig:
    """I read the JSON config and resolve all relative paths from the scripts folder."""
    config_path = config_path.resolve()
    script_dir = config_path.parent.parent
    with config_path.open("r", encoding="utf-8") as file:
        raw = json.load(file)

    return ProjectConfig(
        project_name=raw["project_name"],
        script_dir=script_dir,
        project_root=script_dir.parent,
        raw_data_dir=(script_dir / raw["raw_data_dir"]).resolve(),
        cleaned_data_dir=(script_dir / raw["cleaned_data_dir"]).resolve(),
        merged_data_dir=(script_dir / raw["merged_data_dir"]).resolve(),
        qa_dir=(script_dir / raw["qa_dir"]).resolve(),
        log_dir=(script_dir / raw["log_dir"]).resolve(),
        date_column=raw["date_column"],
        datasets=raw["datasets"],
    )


def ensure_output_dirs(config: ProjectConfig) -> None:
    """I create output folders before the pipeline writes any generated files."""
    for path in [
        config.cleaned_data_dir,
        config.merged_data_dir,
        config.qa_dir,
        config.log_dir,
    ]:
        path.mkdir(parents=True, exist_ok=True)
