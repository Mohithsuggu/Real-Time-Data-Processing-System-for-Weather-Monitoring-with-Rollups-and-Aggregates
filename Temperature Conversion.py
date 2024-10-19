def convert_temperature(kelvin_temp, to_celsius=True):
    if to_celsius:
        return kelvin_temp - 273.15  # Convert to Celsius
    return (kelvin_temp - 273.15) * 9/5 + 32  # Convert to Fahrenheit

