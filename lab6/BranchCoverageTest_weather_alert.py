"""Test suite targeting 100% branch and decision coverage for weather_alert.py."""

import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


def test_wind_alert_all_branches():
    # Test all decision thresholds and the fallthrough branch
    assert wind_alert(100) == "warning"  # speed >= 89
    assert wind_alert(89) == "warning"   # boundary
    assert wind_alert(75) == "watch"     # speed >= 62
    assert wind_alert(62) == "watch"     # boundary
    assert wind_alert(45) == "advisory"  # speed >= 39
    assert wind_alert(39) == "advisory"  # boundary
    assert wind_alert(20) == "none"      # speed < 39


def test_rain_alert_all_branches():
    # mm >= 50: both saturated and not saturated
    assert rain_alert(55, True) == "warning"
    assert rain_alert(55, False) == "watch"
    # 10 <= mm < 50: both saturated and not saturated
    assert rain_alert(20, True) == "watch"
    assert rain_alert(20, False) == "advisory"
    # mm < 10: fallthrough branch with both saturation states
    assert rain_alert(5, True) == "none"
    assert rain_alert(5, False) == "none"


def test_heat_alert_all_branches():
    # Branch 1: humidity > 40 (adjusts index)
    assert heat_alert(45, 50) == "warning"   # index >= 45
    assert heat_alert(40, 50) == "watch"     # index in [40, 45)
    assert heat_alert(35, 50) == "advisory"  # index in [35, 40)
    assert heat_alert(30, 50) == "none"      # index < 35

    # Branch 2: humidity <= 40 (index stays temp_c)
    assert heat_alert(46, 30) == "warning"   # temp_c >= 45
    assert heat_alert(41, 30) == "watch"     # temp_c in [40, 45)
    assert heat_alert(36, 30) == "advisory"  # temp_c in [35, 40)
    assert heat_alert(25, 30) == "none"      # temp_c < 35


def test_overall_alert_all_branches():
    # Empty list branch
    assert overall_alert([]) == "none"

    # Monotonically increasing severity
    assert overall_alert(["none", "advisory", "watch", "warning"]) == "warning"

    # Decreasing severity (exercises the False branch of SEVERITY[alert] > SEVERITY[worst])
    assert overall_alert(["warning", "watch", "advisory", "none"]) == "warning"

    # Same severity repetition (exercises the False branch on equal value)
    assert overall_alert(["watch", "watch"]) == "watch"

    # Invalid alert raising ValueError
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid_alert_code"])
