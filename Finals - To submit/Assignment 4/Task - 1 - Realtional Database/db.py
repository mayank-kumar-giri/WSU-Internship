import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        print(sqlite3.version)
        return conn
    except sqlite3.Error as e:
        print(e)
        return e

def display_weather_table(c):
    query = """
    SELECT * FROM Weather;
    """
    c.execute(query)
    rows = c.fetchall()
    for row in range(len(rows)):
        print(row, rows[row])

#CREATING THE TABLE "WEATHER"
if __name__=="__main__":
    conn = create_connection("database.db")
    c = conn.cursor()
    create_weather_table = """
    CREATE TABLE IF NOT EXISTS Weather(
     _id TEXT PRIMARY KEY,
     _index TEXT,
     _type TEXT,
     _score INTEGER,
     _location TEXT,
     timestamp TEXT,
     humidity FLOAT,
     temperature FLOAT,
     wind_desc TEXT,
     wind_direc TEXT,
     feels_like FLOAT
     );
    """
    c.execute(create_weather_table)
    c.close()
    conn.close()