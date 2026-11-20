# Lab 7: Fuzz Testing Report

## Objective
Use Hypothesis to fuzz test `weather_alert.py`, find inputs that crash the functions, and fix them with defensive checks.

---

## 1. Initial Function Analysis
Looking at the initial code in `weather_alert.py`:
- `parse_reading(text)` directly split the string on `/` and casted to float and int without verifying format or types.
- `wind_category(speed_text)` passed input directly into `int()` without checking for None or non-numeric strings.
- `rainfall_spread(readings_csv)` split on commas and called `max()` and `min()` directly without handling empty strings or missing numbers.

---

## 2. Fuzz Testing Results (Before Fix)
Running `pytest test_weather_alert.py` with `@given(st.text() | st.none())` found failing inputs across all 3 functions:

1. **`parse_reading`**:
   - `s = None` -> `AttributeError: 'NoneType' object has no attribute 'split'`
   - `s = ""` -> `ValueError: not enough values to unpack (expected 2, got 1)`
   - `s = "/"` -> `ValueError: could not convert string to float: ''`
   - `s = "abc/def"` -> `ValueError: could not convert string to float: 'abc'`

2. **`wind_category`**:
   - `s = None` -> `TypeError: int() argument must be a string, not 'NoneType'`
   - `s = ""` -> `ValueError: invalid literal for int() with base 10: ''`
   - `s = "xyz"` -> `ValueError: invalid literal for int() with base 10: 'xyz'`

3. **`rainfall_spread`**:
   - `s = None` -> `AttributeError: 'NoneType' object has no attribute 'split'`
   - `s = ""` -> `ValueError: could not convert string to float: ''`
   - `s = "1,,2"` -> `ValueError: could not convert string to float: ''`

All 3 tests failed as expected when random inputs were supplied.

---

## 3. Fixes Applied
I updated `weather_alert.py` to handle edge cases defensively:
1. Checked that inputs are valid strings and not `None`.
2. Verified that `/` exists and splits into exactly 2 parts before parsing in `parse_reading`, returning `(0.0, 0)` on any bad input.
3. Wrapped string-to-number conversions in `try-except` blocks to catch `ValueError`, `TypeError`, and `OverflowError`.
4. Handled empty lists and missing values in `rainfall_spread`, returning `0.0` if no valid numbers are found.

---

## 4. Re-running Fuzz Tests (After Fix)
Command:
```bash
pytest test_weather_alert.py
```
Output:
```
============================= test session starts =============================
platform win32 -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0
collected 3 items

test_weather_alert.py ...                                                [100%]

============================== 3 passed in 7.03s ==============================
```
All 3 tests passed without any crashes. Standard valid inputs were also tested manually and still work correctly (`parse_reading('35.5/80') == (35.5, 80)`, `wind_category('45') == 'advisory'`, `rainfall_spread('2,5.5,10') == 8.0`).
