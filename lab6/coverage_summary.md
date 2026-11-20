# Lab 6: Code and Branch Coverage Analysis

## 1. Line Coverage
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
Line coverage achieved: **100%** (exceeds the 90% requirement).

---

## 2. Branch Coverage
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
Branch coverage achieved: **100%** (28/28 branches tested, 0 missing).

---

## 3. Difference Between Line and Branch Coverage
- In the initial test case (`test_weather_alert.py`), only **32%** of lines were tested.
- In `CodeCoverageTest_weather_alert.py`, all statements were executed at least once to get **100% line coverage**. However, running with the `--branch` flag showed **98%** branch coverage because the false condition for `if humidity > 40:` was never hit (all test inputs used humidity > 40).
- In `BranchCoverageTest_weather_alert.py`, additional test cases were added for both true and false paths (e.g. humidity <= 40, wind boundary values 39/62/89, and equal alert severities in `overall_alert`), achieving **100% branch coverage**.
