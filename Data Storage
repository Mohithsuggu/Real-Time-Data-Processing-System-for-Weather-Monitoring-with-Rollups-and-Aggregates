import sqlite3

def initialize_database():
    conn = sqlite3.connect('weather_monitoring.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                        date TEXT PRIMARY KEY,
                        average_temp REAL,
                        max_temp REAL,
                        min_temp REAL,
                        dominant_condition TEXT)''')
    
    conn.commit()
    conn.close()

def store_daily_summary(summary):
    conn = sqlite3.connect('weather_monitoring.db')
    cursor = conn.cursor()
    
    cursor.execute('''INSERT OR REPLACE INTO daily_summary 
                      (date, average_temp, max_temp, min_temp, dominant_condition) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (summary['date'], summary['average_temp'], summary['max_temp'], 
                    summary['min_temp'], summary['dominant_condition']))
    
    conn.commit()
    conn.close()
