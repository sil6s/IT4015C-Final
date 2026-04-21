# Reproducibility Checklist

## Purpose

I use this checklist to make sure the project can be rerun and reviewed without relying on hidden manual steps.

## Environment

- [ ] Python version recorded.
- [ ] `requirements.txt` is present.
- [ ] Dependencies install successfully.
- [ ] Pipeline command is documented.

## Data

- [ ] Raw files are present.
- [ ] Raw files are not edited manually.
- [ ] Cleaned outputs can be regenerated.
- [ ] Merged outputs can be regenerated.
- [ ] Source documentation identifies every dataset.

## Code

- [ ] Scripts use relative project paths from the config file.
- [ ] Scripts produce logs.
- [ ] Scripts produce validation outputs.
- [ ] Scripts fail clearly when expected files or columns are missing.
- [ ] Comments and docstrings explain the workflow in first person.

## Outputs

- [ ] Cleaned files are written to `03_cleaned_data/`.
- [ ] Merged files are written to `04_merged_data/`.
- [ ] QA files are written to `10_qa_validation/`.
- [ ] Logs are written to `11_outputs/logs/`.
- [ ] Final deliverables are separated in `12_final_submission/`.

## Final Review

- [ ] I can rerun the pipeline from a clean working state.
- [ ] I can explain every generated file.
- [ ] I can identify which files are raw, intermediate, and final.
