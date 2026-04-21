# Environment Setup Notes

## Purpose

I use this file to document how to recreate the Python environment for the project.

## Recommended Setup

From the project root:

```bash
cd Project_Data/05_scripts
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 run_pipeline.py
```

## Dependency Purpose

| Package | Purpose |
|---|---|
| `pandas` | I use pandas for loading, cleaning, reshaping, validating, merging, and exporting tabular data. |
| `openpyxl` | I use openpyxl through pandas so Excel source files and Excel exports can be read and written. |
| `numpy` | I include numpy because pandas depends on numeric array handling and it is useful for validation work. |

## Troubleshooting Notes

- If `pandas` is not installed, I need to install dependencies from `requirements.txt`.
- If Excel loading fails, I need to confirm that `openpyxl` installed correctly.
- If paths fail, I should run the command from `Project_Data/05_scripts`.
- If a raw file is missing, I should check `01_raw_data/` before changing code.
