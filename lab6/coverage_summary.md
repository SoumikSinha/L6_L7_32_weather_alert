# Lab 6: Code and Branch Coverage Analysis Report

## Summary of Results

### 1. Line (Code) Coverage Results
Command executed:
```bash
coverage run -m pytest CodeCoverageTest_weather_alert.py
coverage report -m
```
Output:
```
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
CodeCoverageTest_weather_alert.py      23      0   100%
weather_alert.py                       38      0   100%
-----------------------------------------------------------------
TOTAL                                  61      0   100%
```
**Line Coverage achieved: 100%** (Well exceeds the 90% rubric threshold).

---

### 2. Branch Coverage Results
Command executed:
```bash
coverage run --branch -m pytest BranchCoverageTest_weather_alert.py
coverage report -m
```
Output:
```
Name                                  Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------------
BranchCoverageTest_weather_alert.py      33      0      0      0   100%
weather_alert.py                         38      0     28      0   100%
---------------------------------------------------------------------------------
TOTAL                                    71      0     28      0   100%
```
**Branch Coverage achieved: 100%** (28/28 decision branches exercised, 0 missing).

---

### 3. Key Findings: Line Coverage vs. Branch Coverage
- In the initial test case (`test_weather_alert.py`), only **32%** of lines were executed.
- When writing tests solely for line execution (`CodeCoverageTest_weather_alert.py`), **100% line coverage** was achieved. However, when evaluating with the `--branch` flag, branch coverage was **98%** because the false condition `humidity <= 40` at line 28 (`if humidity > 40:`) was never tested.
- `BranchCoverageTest_weather_alert.py` was created to test both `True` and `False` outcomes for every conditional branch, boundary values (e.g. `speed_kmh = 39, 62, 89`), falling-through rain conditions, and both increasing and decreasing severity transitions in `overall_alert()`, reaching **100% full branch coverage**.
