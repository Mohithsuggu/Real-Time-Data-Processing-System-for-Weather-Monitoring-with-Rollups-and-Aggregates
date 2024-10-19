alert_threshold = 35  # Celsius
alert_count = 0

def check_alert_conditions(weather_data):
    global alert_count
    if weather_data['temp'] > alert_threshold:
        alert_count += 1
        if alert_count >= 2:
            print(f"Alert: High temperature detected! {weather_data['temp']}°C")
    else:
        alert_count = 0  # Reset if condition not met
