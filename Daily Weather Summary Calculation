from collections import defaultdict

daily_summaries = defaultdict(lambda: {'temps': [], 'conditions': []})

def update_daily_summary(weather_data):
    date = datetime.fromtimestamp(weather_data['dt']).date()
    daily_summaries[date]['temps'].append(weather_data['temp'])
    daily_summaries[date]['conditions'].append(weather_data['main'])

def calculate_daily_summary(date):
    if date in daily_summaries:
        temps = daily_summaries[date]['temps']
        conditions = daily_summaries[date]['conditions']
        
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        dominant_condition = max(set(conditions), key=conditions.count)
        
        return {
            'date': date,
            'average_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }
    return None
