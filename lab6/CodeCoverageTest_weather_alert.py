"""Test suite targeting 100% code (line) coverage for weather_alert.py."""

import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


def test_wind_alert_line_coverage():
    assert wind_alert(95) == "warning"
    assert wind_alert(70) == "watch"
    assert wind_alert(45) == "advisory"
    assert wind_alert(20) == "none"


def test_rain_alert_line_coverage():
    assert rain_alert(60, True) == "warning"
    assert rain_alert(60, False) == "watch"
    assert rain_alert(25, True) == "watch"
    assert rain_alert(25, False) == "advisory"
    assert rain_alert(5, False) == "none"


def test_heat_alert_line_coverage():
    # humidity > 40 triggering index calculation
    assert heat_alert(45, 50) == "warning"   # index = 46 >= 45 -> warning
    assert heat_alert(40, 50) == "watch"     # index = 41 >= 40 -> watch
    assert heat_alert(35, 50) == "advisory"  # index = 36 >= 35 -> advisory
    assert heat_alert(30, 50) == "none"      # index = 31 < 35  -> none


def test_overall_alert_line_coverage():
    assert overall_alert([]) == "none"
    assert overall_alert(["none", "advisory", "watch", "warning"]) == "warning"
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["cyclone"])
