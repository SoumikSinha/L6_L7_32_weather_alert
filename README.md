# Lab 6 & Lab 7: Code Coverage, Branch Coverage & Fuzz Testing

**Student Name:** Soumik Sinha  
**USN / SRN:** PES1UG24CS463  
**Section:** 5H  
**Roll / Sl. No:** 32  
**Assigned Repository:** `L6_L7_32_weather_alert`  

---

## Repository Structure

This repository contains the completed implementations and evaluation reports for both **Lab 6** and **Lab 7**:

```
L6_L7_32_weather_alert/
├── lab6/                         # Lab 6: Code and Branch Coverage Analysis
│   ├── weather_alert.py          # Application module under test
│   ├── CodeCoverageTest_weather_alert.py   # Test suite achieving 100% line coverage
│   ├── BranchCoverageTest_weather_alert.py # Test suite achieving 100% branch coverage
│   ├── code_coverage_report.png  # Terminal screenshot of line coverage report
│   ├── branch_coverage_report.png# Terminal screenshot of branch coverage report
│   ├── coverage_summary.md       # Summary of tested edge cases and missing paths
│   └── README.md
│
├── lab7/                         # Lab 7: Fuzz Testing for Input Validation Bugs
│   ├── weather_alert.py          # Hardened application script
│   ├── test_weather_alert.py     # Property-based fuzz tests using Hypothesis
│   ├── Lab7_FuzzTesting_Screenshots_PES1UG24CS463.pdf # Deliverable PDF with all required step screenshots
│   ├── step2_initial_output.png  # Step 2: Initial script execution screenshot
│   ├── step4_fuzz_failures.png   # Step 4: Hypothesis test failures screenshot
│   ├── step5_fixed_app_output.png# Step 5: Hardened script execution screenshot
│   ├── step6_fuzz_passed.png     # Step 6: 100% tests passing screenshot
│   ├── fuzz_testing_report.md    # Documentation of uncovered bugs and defensive fixes
│   └── README.md
│
└── README.md
```

---

## Lab 6: Code and Branch Coverage Summary
- **Line Coverage:** 100% (38/38 statements in `weather_alert.py`)
- **Branch Coverage:** 100% (28/28 execution branches covered across all conditions)
- **Commands Executed:**
  - `coverage run -m pytest CodeCoverageTest_weather_alert.py && coverage report -m`
  - `coverage run --branch -m pytest BranchCoverageTest_weather_alert.py && coverage report -m`

---

## Lab 7: Fuzz Testing Summary
- **Fuzzing Engine:** `Hypothesis` property-based testing
- **Hardened Functions:**
  - `parse_reading()`: Handles malformed strings, missing slash delimiters, non-numeric values, and out-of-range readings safely.
  - `wind_category()`: Robust to negative values, non-numeric types, floats, and extreme bounds.
  - `rainfall_spread()`: Handles empty inputs, single-value lists, non-numeric elements, and floating-point ranges without crashing.
- **Verification:** All Hypothesis fuzz tests pass 100% over randomized property runs.
