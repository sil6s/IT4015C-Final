"""I load raw source files safely before any cleaning or merging occurs."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import pandas as pd

LOGGER = logging.getLogger(__name__)

MONTH_MAP = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12",
}


def load_dataset(raw_data_dir: Path, dataset: dict[str, Any]) -> pd.DataFrame:
    """I choose the correct loader based on the documented source format."""
    path = raw_data_dir / dataset["relative_path"]
    if not path.exists():
        raise FileNotFoundError(f"I expected this raw file, but it was not found: {path}")

    LOGGER.info("I am loading %s from %s", dataset["display_name"], path)
    source_format = dataset["source_format"]

    if source_format == "fred_csv":
        return _load_fred_csv(path, dataset)
    if source_format == "bls_cpi_excel":
        return _load_bls_cpi_excel(path, dataset)

    raise ValueError(f"I do not have a loader configured for source_format={source_format}")


def _load_fred_csv(path: Path, dataset: dict[str, Any]) -> pd.DataFrame:
    """I load a FRED-style CSV with observation_date and one source series column."""
    frame = pd.read_csv(path)
    expected_columns = {"observation_date", dataset["source_series"]}
    missing = expected_columns.difference(frame.columns)
    if missing:
        raise ValueError(f"I found missing expected columns in {path.name}: {sorted(missing)}")

    frame = frame.rename(
        columns={
            "observation_date": "date",
            dataset["source_series"]: dataset["value_column"],
        }
    )
    frame["source_file"] = path.name
    frame["source_series"] = dataset["source_series"]
    return frame[["date", dataset["value_column"], "source_file", "source_series"]]


def _load_bls_cpi_excel(path: Path, dataset: dict[str, Any]) -> pd.DataFrame:
    """I reshape a BLS CPI workbook from wide years/months into tidy observations."""
    raw = pd.read_excel(path, header=None)
    header_index = _find_bls_header_row(raw)
    table = raw.iloc[header_index + 1 :].copy()
    headers = raw.iloc[header_index].tolist()
    table.columns = headers

    if "Year" not in table.columns:
        raise ValueError(f"I could not find a Year column after parsing {path.name}")

    month_columns = [month for month in MONTH_MAP if month in table.columns]
    if not month_columns:
        raise ValueError(f"I could not find month columns in {path.name}")

    tidy = table.melt(
        id_vars=["Year"],
        value_vars=month_columns,
        var_name="month_name",
        value_name=dataset["value_column"],
    )
    tidy = tidy.dropna(subset=["Year"])
    tidy["Year"] = pd.to_numeric(tidy["Year"], errors="coerce")
    tidy = tidy.dropna(subset=["Year"])
    tidy["year"] = tidy["Year"].astype(int).astype(str)
    tidy["month"] = tidy["month_name"].map(MONTH_MAP)
    tidy["date"] = tidy["year"] + "-" + tidy["month"] + "-01"
    # I remove blank month cells from the BLS workbook because they are not actual observations.
    tidy[dataset["value_column"]] = pd.to_numeric(tidy[dataset["value_column"]], errors="coerce")
    tidy = tidy.dropna(subset=[dataset["value_column"]])
    tidy["source_file"] = path.name
    tidy["source_series"] = dataset["source_series"]

    return tidy[["date", dataset["value_column"], "source_file", "source_series"]]


def _find_bls_header_row(raw: pd.DataFrame) -> int:
    """I scan for the BLS row where the monthly table begins."""
    for index, row in raw.iterrows():
        values = [str(value).strip() for value in row.tolist()]
        if "Year" in values and "Jan" in values:
            return int(index)
    raise ValueError("I could not locate the BLS CPI table header row.")
