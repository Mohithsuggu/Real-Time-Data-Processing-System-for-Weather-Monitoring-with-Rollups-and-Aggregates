def start_monitoring():
    while True:
        for city in CITIES:
            data = fetch_weather_data(city)
            if data:
                temp = convert_temperature(data['main']['temp'])
                weather_data = {
                    'temp': temp,
                    'main': data['weather'][0]['main'],
                    'dt': data['dt']
                }
                update_daily_summary(weather_data)
                check_alert_conditions(weather_data)
        time.sleep(300)  # Wait for 5 minutes before next fetch
