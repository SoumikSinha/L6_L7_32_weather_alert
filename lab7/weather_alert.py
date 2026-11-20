"""Hardened weather alert parser and classifier resilient against malformed inputs."""


def parse_reading(text):
    """Safely parse temperature and humidity from string formatted as 'temp/humidity'.

    Returns (temp_float, humidity_int), or (0.0, 0) on invalid or malformed input.
    """
    if not isinstance(text, str) or "/" not in text:
        return 0.0, 0
    parts = text.split("/")
    if len(parts) != 2:
        return 0.0, 0
    try:
        temp = float(parts[0].strip())
        humidity = int(float(parts[1].strip()))
        return temp, humidity
    except (ValueError, TypeError, OverflowError):
        return 0.0, 0


def wind_category(speed_text):
    """Safely categorize wind speed string into severity category.

    Returns 'warning', 'advisory', or 'none'.
    """
    if speed_text is None:
        return "none"
    try:
        speed = int(float(str(speed_text).strip()))
    except (ValueError, TypeError, OverflowError):
        return "none"

    if speed >= 89:
        return "warning"
    if speed >= 39:
        return "advisory"
    return "none"


def rainfall_spread(readings_csv):
    """Safely calculate rainfall spread (max - min) from comma-separated readings.

    Returns float difference, or 0.0 on empty or invalid inputs.
    """
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        return 0.0
    valid_readings = []
    for item in readings_csv.split(","):
        cleaned = item.strip()
        if not cleaned:
            continue
        try:
            val = float(cleaned)
            valid_readings.append(val)
        except (ValueError, TypeError, OverflowError):
            continue

    if not valid_readings:
        return 0.0
    return max(valid_readings) - min(valid_readings)


def main():
    print("==== Running parse_reading ====")
    user_input = input("Enter temperature/humidity (e.g. 35.5/80): ")
    result = parse_reading(user_input)
    print("Temperature and Humidity:", result)

    print("\n==== Running wind_category ====")
    user_input = input("Enter a wind speed in km/h (e.g. 45): ")
    result = wind_category(user_input)
    print("Wind Category:", result)

    print("\n==== Running rainfall_spread ====")
    user_input = input("Enter hourly rainfall in mm as CSV (e.g. 2,5.5,10): ")
    result = rainfall_spread(user_input)
    print("Rainfall Spread:", result)


if __name__ == "__main__":
    main()
