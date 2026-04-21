# Assumptions Log

## Purpose

I use this assumptions log to separate preparation assumptions from analytical findings. If I make a decision that affects cleaning, integration, or reporting, I document it here before relying on it later.

## Assumptions

| ID | Date | Assumption | Area Affected | Reason for Assumption | Risk if Incorrect | Status |
|---|---|---|---|---|---|---|
| A-001 |  | Monthly date alignment is the intended integration level unless analysis scope changes later. | Data integration | Most source files are monthly, and the project compares time-series economic indicators. | A quarterly source may require special treatment or a restricted comparison. | Open |
| A-002 |  | Raw downloaded files should remain unchanged after organization. | Reproducibility | I need a stable source layer for auditability. | Manual edits to raw data would reduce traceability. | Open |
| A-003 |  | Missing values should be flagged and documented before deciding whether to filter or transform. | QA | Coverage differences are expected across economic series. | Dropping rows too early could bias later analysis choices. | Open |

## Assumption Review Notes

I will revisit this log before final analysis and again before submission.
